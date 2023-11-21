Truth Table: Logical Conjunction
================================

I will continue to step through learning conditional statements in python using Test Driven Development using the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

I know that there are two boolean values


* :doc:`True </data structures: booleans>`
* :doc:`False </data structures: booleans>`


Prerequisites
-------------


:doc:`How to Setup a Test Driven Development Environment`

----

Logical Conjunction
-------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

create a ``TestCase`` for binary operations in ``test_truth_table.py``

.. code-block:: python



  class TestBinaryOperations(unittest.TestCase):

    def test_logical_conjunction(self):
      self.assertTrue(truth_table.logical_conjunction(True, True))
      self.assertFalse(truth_table.logical_conjunction(True, False))
      self.assertFalse(truth_table.logical_conjunction(False, True))
      self.assertFalse(truth_table.logical_conjunction(False, False))

the terminal updates to show an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add a definition for ``logical_conjunction`` to ``truth_table.py``
  .. code-block:: python

    def logical_conjunction():
      return None
  the terminal updates to show a :doc:`TypeError`
* update the function signature with a positional argument
  .. code-block:: python

    def logical_conjunction(p):
      return None
  the terminal updates to show another :doc:`TypeError`
* add another positional argument
  .. code-block:: python

    def logical_conjunction(p, q):
      return None
  the terminal updates to show an :doc:`AssertionError`
* update ``logical_conjunction`` in ``truth_table.py``
  .. code-block:: python

    def logical_conjunction(p, q):
      return True
  this makes the first of the four tests pass. the terminal updates to show the second line fails
* how can I make this function return different values based on the input it receives? I can use `if statements <https://docs.python.org/3/tutorial/controlflow.html?highlight=statement#if-statements>`_
* add an `if statement <https://docs.python.org/3/reference/compound_stmts.html?highlight=return%20true#the-if-statement>`_ for the first case ``self.assertTrue(truth_table.logical_conjunction(True, True))`` where p is :doc:`True </data structures: booleans>` and q is :doc:`True </data structures: booleans>`
  .. code-block:: python

    def logical_conjunction(p, q):
      if p == True:
       return True
  the terminal still shows an :doc:`AssertionError`
* add a condition for the second input value
  .. code-block:: python

    def logical_conjunction(p, q):
      if p == True:
       if q == True:
         return True
  the test updates to show passing tests. Lovely!

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* Why does this work?

  * I add a condition for when the value of ``p`` is equal to :doc:`True </data structures: booleans>` and inside that condition I have another for when the value of ``q`` is equal to :doc:`True </data structures: booleans>`
  * if both conditions are met, the ``logical_conjunction`` function returns True but what does it do when those two conditions are not met?

* I know by default a function returns :doc:`None </data structures: None>` so it must be returning :doc:`None </data structures: None>` for the other cases. Does this mean :doc:`None </data structures: None>` is :doc:`False </data structures: booleans>`? I know the answer to this from `data structures <./06_DATA_STRUCTURES.rst>`_\ , What if I test it as a reminder. add another return statement to the definition of ``logical_conjunction``
  .. code-block:: python

    def logical_conjunction(p, q):
      if p == True:
       if q == True:
         return True
      return None
  tests are still passing
* if :doc:`None </data structures: None>` is :doc:`False </data structures: booleans>` I can be more explicit by using the boolean :doc:`False </data structures: booleans>`
  .. code-block:: python

    def logical_conjunction(p, q):
      if p == True:
       if q == True:
         return True
      return False
  tests still pass
* can I express these nested conditionals as one line? yes, I can use the ``and`` keyword
  .. code-block:: python

    def logical_conjunction(p, q):
      if p == True and q == True:
       return True
      return False
  still green
* I can rewrite the opposite of the ``if`` statement by using the ``else`` keyword
  .. code-block:: python

    def logical_conjunction(p, q):
      if p == True and q == True:
       return True
      else:
       return False
  tests are still green because this expresses all four cases from ``test_logical_conjunction``

  * in 1 case where ``p is True`` and ``q is True`` it returns True
  * in the 3 remaining cases it returns False
  * this means in a binary operation with 2 outcomes I only need to write a condition for one and write an else for the other. This will save us having to write out a condition for every case

* python equality `comparisons <https://docs.python.org/3/reference/expressions.html?highlight=ternary%20conditional#comparisons>`_ for booleans can be implicitly stated because python calls ``bool()`` on the values, e.g ``if p == True`` can be rewritten as ``if p`` so I can rewrite the ``if`` statement in a simpler way
  .. code-block:: python

    def logical_conjunction(p, q):
      if p and q:
       return True
      else:
       return False
  the tests still pass, so far so good
* I can also express conditions in a return statement using `conditional expressions/ternary operators <https://docs.python.org/3/reference/expressions.html?highlight=ternary%20conditional#conditional-expressions>`_
  .. code-block:: python

    def logical_conjunction(p, q):
      return True if p and q else False

* since python implicitly tests conditionals I can rewrite the statement this way
  .. code-block:: python

    def logical_conjunction(p, q):
      return p and q
  things are still green. I don't think I can get a simpler statement than this

*FANTASTIC!* You have tested logical_conjunction which is a conditional operation using ``and``. I now know that for any boolean operation involving 2 inputs - ``p`` and ``q`` which can take the values :doc:`True </data structures: booleans>` or :doc:`False </data structures: booleans>`


* ``return True if x else y`` can be rewritten as ``return x`` if ``x`` evaluates to :doc:`True </data structures: booleans>`
* when there are multiple outcomes I only need to write the condition for the special case and use ``else`` for the others
* ``logical_conjunction`` is ``and``
* :doc:`False </data structures: booleans>` is ``not True``
* :doc:`True </data structures: booleans>` is ``not False``
* :doc:`False </data structures: booleans>` is :doc:`False </data structures: booleans>`
* :doc:`True </data structures: booleans>` is :doc:`True </data structures: booleans>`
