.. include:: ../../../links.rst

#################################
truth table: Logical Conjunction
#################################

.. contents:: table of contents
  :local:
  :depth: 1

----

In this chapter I continue to step through learning conditional statements in Python with the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

I know that there are two boolean values

* :doc:`True </data_structures/booleans/booleans>`
* :doc:`False </data_structures/booleans/booleans>`



red: make it fail
#################################################################################

After making a ``TestCase`` for binary operations in ``test_truth_table.py``

.. code-block:: python

  class TestBinaryOperations(unittest.TestCase):

      def test_logical_conjunction(self):
          self.assertTrue(truth_table.logical_conjunction(True, True))
          self.assertFalse(truth_table.logical_conjunction(True, False))
          self.assertFalse(truth_table.logical_conjunction(False, True))
          self.assertFalse(truth_table.logical_conjunction(False, False))

the terminal shows an :ref:`AttributeError`

green: make it pass
#################################################################################

* I add a definition for ``logical_conjunction`` to ``truth_table.py``

  .. code-block:: python

    def logical_conjunction():
        return None

  the terminal shows a :ref:`TypeError`
* I add the new error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError

* I make the :doc:`function</functions/functions>` signature to include a positional argument

  .. code-block:: python

    def logical_conjunction(p):
        return None

  the terminal shows another :ref:`TypeError` but with a different message
* I add another positional argument to match the expected signature

  .. code-block:: python

    def logical_conjunction(p, q):
        return None

  and the terminal shows an :ref:`AssertionError`
* I make ``logical_conjunction`` in ``truth_table.py`` to return :doc:`True </data_structures/booleans/booleans>`

  .. code-block:: python

    def logical_conjunction(p, q):
        return True

  which makes the first of the four tests pass, the terminal now shows a failure for the second line
* I can make this function return different values based on the input it receives with `if statements <https://docs.python.org/3/tutorial/controlflow.html?highlight=statement#if-statements>`_
* I add an `if statement <https://docs.python.org/3/reference/compound_stmts.html?highlight=return%20true#the-if-statement>`_ for the first case ``self.assertTrue(truth_table.logical_conjunction(True, True))`` where p is :doc:`True </data_structures/booleans/booleans>` and q is :doc:`True </data_structures/booleans/booleans>`

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True:
            return True

  the terminal still shows an :ref:`AssertionError`
* I then add a condition for the second input value

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True:
            if q == True:
                return True

  the terminal shows passing tests. Lovely!

refactor: make it better
#################################################################################

* Why does this work?

  - I add a condition for when the value of ``p`` is equal to :doc:`True </data_structures/booleans/booleans>`
  - Inside the first condition I add another condition for when the value of ``q`` is equal to :doc:`True </data_structures/booleans/booleans>`
  - when both conditions are met, the ``logical_conjunction`` function returns :doc:`True </data_structures/booleans/booleans>`. What does it return when those two conditions are not met?

* I know from :doc:`/functions/functions` that a function returns :ref:`None` by default so it must be returning :ref:`None` for the other cases. This means :ref:`None` is :doc:`False </data_structures/booleans/booleans>` as seen in :doc:`/data_structures/booleans/booleans`
* I can add a test as a reminder

  .. code-block:: python

      def logical_conjunction(p, q):
          if p == True:
              if q == True:
                  return True
          return None

  tests are still passing
* Since :ref:`None` is :doc:`False </data_structures/booleans/booleans>`, I can be more explicit by using the boolean :doc:`False </data_structures/booleans/booleans>`

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True:
            if q == True:
                return True
        return False

  tests still pass

* These are nested conditionals and I can express them on one line by using the ``and`` keyword

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True and q == True:
            return True
        return False

  still green
* I rewrite the opposite of the ``if`` statement by adding an ``else`` clause

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True and q == True:
            return True
        else:
            return False

  tests are still green because this expresses all four cases from ``test_logical_conjunction``

  - in 1 case where ``p is True`` and ``q is True`` it returns True:doc:`True </data_structures/booleans/booleans>`
  - in the 3 remaining cases it returns False
  - does this mean that in a binary operation with 2 outcomes I only need to write a condition for one and write an else for the other? This could save me having to write out a condition for every case

  .. note::

    python `comparisons <https://docs.python.org/3/reference/expressions.html?highlight=ternary%20conditional#comparisons>`_ for booleans can be implicitly stated because python calls ``bool()`` on the values, e.g ``if p == True`` can be rewritten as ``if p``

  I rewrite the ``if`` statement in a simpler way

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

  tests are still green. I don't think I can get a simpler statement than this

After testing ``logical_conjunction`` which is a conditional operation using ``and``, I know that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :doc:`True </data_structures/booleans/booleans>` or :doc:`False </data_structures/booleans/booleans>`


* ``return True if x else y`` can be rewritten as ``return x`` if ``x`` evaluates to :doc:`True </data_structures/booleans/booleans>`
* when there are multiple outcomes I only need to write the condition for the special case and use ``else`` for the others
* ``logical conjunction`` is ``and``
* :doc:`False </data_structures/booleans/booleans>` is ``not True``
* :doc:`True </data_structures/booleans/booleans>` is ``not False``
* :doc:`False </data_structures/booleans/booleans>` is :doc:`False </data_structures/booleans/booleans>`
* :doc:`True </data_structures/booleans/booleans>` is :doc:`True </data_structures/booleans/booleans>`

----

:doc:`/code/code_truth_table`