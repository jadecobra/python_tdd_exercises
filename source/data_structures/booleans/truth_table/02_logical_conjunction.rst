.. include:: ../../../links.rst

#################################################################################
truth table: Logical Conjunction
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with ``truth_table`` as the name of the project

test_logical_conjunction
#################################################################################


red: make it fail
---------------------------------------------------------------------------------

I add a TestCase_ for binary operations in ``test_truth_table.py`` with ``test_logical_conjunction`` as the first test

.. code-block:: python

  class TestBinaryOperations(unittest.TestCase):

      def test_logical_conjunction(self):
          self.assertTrue(src.truth_table.logical_conjunction(True, True))
          self.assertFalse(src.truth_table.logical_conjunction(True, False))
          self.assertFalse(src.truth_table.logical_conjunction(False, True))
          self.assertFalse(src.truth_table.logical_conjunction(False, False))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'logical_conjunction'

green: make it pass
---------------------------------------------------------------------------------

* I add a definition

  .. code-block:: python

    def logical_negation(value):
        return not value

    def logical_conjunction():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: logical_conjunction() takes 0 positional arguments but 2 was given

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError

* then I make the :ref:`function<functions>` take input

  .. code-block:: python

    def logical_conjunction(p):
        return None

  the terminal shows :ref:`TypeError`

  .. code-blocK:: python

    TypeError: logical_conjunction() takes 1 positional arguments but 2 was given

* I add another positional argument

  .. code-block:: python

    def logical_conjunction(p, q):
        return None

  and the terminal shows :ref:`AssertionError`

  .. code-block::

    AssertionError: None is not true

* I make it return :ref:`True<test_what_is_true>`

  .. code-block:: python

    def logical_conjunction(p, q):
        return True

  the first line passes and for the second line the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

* I can make this function return different values based on the input it receives with `if statements`_.I add one for the first case ``self.assertTrue(truth_table.logical_conjunction(True, True))`` where ``p`` and ``q`` are both :ref:`True<test_what_is_true>`

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True:
            return True

  the terminal still shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

* I add a condition for the second input value

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True:
            if q == True:
                return True

  and the test passes. Lovely!

refactor: make it better
---------------------------------------------------------------------------------

* Why does this work?

  - I add a condition for when the value of ``p`` is equal to :ref:`True<test_what_is_true>`
  - I add another condition in the first one for when the value of ``q`` is equal to :ref:`True<test_what_is_true>`
  - when both conditions are met, the :ref:`function<functions>` returns :ref:`True<test_what_is_true>`
  - what does it return when those two conditions are not met?

* I know from :ref:`functions` that :ref:`None` is returned by default so the ``logical_conjunction`` :ref:`function<functions>` must be returning :ref:`None` for the other cases, and I also know from :ref:`booleans` that :ref:`None` is :ref:`False<test_what_is_false>`. I add a `return statement` to be explicit

  .. code-block:: python

      def logical_conjunction(p, q):
          if p == True:
              if q == True:
                  return True
          return None

  all tests are still passing
* Since :ref:`None` is :ref:`False<test_what_is_false>`, I can be more explicit by using :ref:`False<test_what_is_false>`

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True:
            if q == True:
                return True
        return False

  still green

* I can express these conditions on one line with the and_ keyword

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True and q == True:
            return True
        return False

  still green
* I rewrite the opposite of the ``if`` statement by adding an else_ clause

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True and q == True:
            return True
        else:
            return False

  tests are still green because this expresses all four cases from ``test_logical_conjunction``

  - in 1 case where ``p is True`` and ``q is True`` it returns True:ref:`True<test_what_is_true>`
  - in the 3 remaining cases it returns False
  - does this mean that in a binary operation with 2 outcomes I only need to write a condition for one and write an else for the other? This could save me having to write out a condition for every case

  .. note::

   Python `comparisons <https://docs.python.org/3/reference/expressions.html?highlight=ternary%20conditional#comparisons>`_ for booleans can be implicitly stated becausePython calls ``bool()`` on the values, e.g ``if p == True`` can be rewritten as ``if p``

  I rewrite the ``if`` statement in a simpler way

  .. code-block:: python

    def logical_conjunction(p, q):
        if p and q:
            return True
        else:
            return False

  the tests still pass, so far so good
* I can also express conditions in a `return statement`_ using `conditional expressions/ternary operators <https://docs.python.org/3/reference/expressions.html?highlight=ternary%20conditional#conditional-expressions>`_

  .. code-block:: python

    def logical_conjunction(p, q):
        return True if p and q else False

* sincePython implicitly tests conditionals I can rewrite the statement this way

  .. code-block:: python

    def logical_conjunction(p, q):
        return p and q

  tests are still green. I don't think I can get a simpler statement than this

After testing ``logical_conjunction`` which is a conditional operation using and_, I know that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`


* ``return True if x else y`` can be rewritten as ``return x`` if ``x`` evaluates to :ref:`True<test_what_is_true>`
* when there are multiple outcomes I only need to write the condition for the special case and use ``else`` for the others
* ``logical conjunction`` is and_
* :ref:`False<test_what_is_false>` is ``not True``
* :ref:`True<test_what_is_true>` is ``not False``
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`

----

:doc:`/code/code_truth_table`