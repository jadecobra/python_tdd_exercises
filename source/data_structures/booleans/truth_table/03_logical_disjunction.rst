.. include:: ../../../links.rst

#################################
Truth Table: Logical Disjunction
#################################

This chapter continues the adventure with conditional statements for Logical Disjunction from the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

Reviewing the tests I have so far, I know that

* I can express ``conditional statements`` on one line with ``return``
* when there are multiple outcomes I only need to write the condition for the special case and use ``else`` for the others
* ``logical conjunction`` is ``and``
* :doc:`False </data_structures/booleans/booleans>` is ``not True``
* :doc:`True </data_structures/booleans/booleans>` is ``not False``
* :doc:`False </data_structures/booleans/booleans>` is :doc:`False </data_structures/booleans/booleans>`
* :doc:`True </data_structures/booleans/booleans>` is :doc:`True </data_structures/booleans/booleans>`


red: make it fail
~~~~~~~~~~~~~~~~~

I add a test for logical disjunction to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_logical_disjunction(self):
        self.assertTrue(truth_table.logical_disjunction(True, True))
        self.assertTrue(truth_table.logical_disjunction(True, False))
        self.assertTrue(truth_table.logical_disjunction(False, True))
        self.assertFalse(truth_table.logical_disjunction(False, False))

and the terminal shows an :ref:`AttributeError`

green: make it pass
~~~~~~~~~~~~~~~~~~~


* Then I make ``truth_table.py`` with a function definition like I did for ``logical_conjunction``

  .. code-block:: python

    def logical_disjunction(p, q):
        return True

  and the terminal shows an :ref:`AssertionError`

* 3 of the test cases are passing because ``logical_disjunction`` returns :doc:`True </data_structures/booleans/booleans>` for each one of them. I need a condition for the fourth case to pass, so I make the definition

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == False:
            if q == False:
                return False
        return True

  the terminal shows passing tests

refactor: make it better
~~~~~~~~~~~~~~~~~~~~~~~~


* I know from :doc:`/data_structures/booleans/truth_table/02_logical_conjunction` that when I have a nested if statement it can be replaced with an ``and`` so I make the condition

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == False and q == False:
            return False
        return True

  the terminal shows the tests are still passing

* I can restate the equality comparison against :doc:`False </data_structures/booleans/booleans>` in terms of :doc:`True </data_structures/booleans/booleans>` by using the ``not equal`` comparison operator ``!=``

  .. code-block:: python

    def logical_disjunction(p, q):
        if p != True and q != True:
            return False
        return True

* I can also express the ``if`` statement with the ``not`` keyword like I did with ``logical_negation`` to express the opposite of a :doc:`boolean </data_structures/booleans/booleans>`

  .. code-block:: python

    def logical_disjunction(p, q):
        if not p and not q:
            return False
        return True

* ``not`` happens twice in that statement, which I can "factor" out like in algebra

  .. code-block:: python

    def logical_disjunction(p, q):
        if not(p and q):
            return False
        return True

  the terminal shows a failing test. OOPS! I have introduced a regression. If I expand the statement using "multiplication" rules. What I have above is

  .. code-block:: python

    def logical_disjunction(p, q):
        if not p not and not q:
            return False
        return True

  I get a ``SyntaxError`` which I add to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError
    # SyntaxError

* The result of the "multiplication" is different from what I started with so I need something different. It should be something that expands out to

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

  okay, this looks more like what will get the original statement when "multiplied" since ``the opposite of the opposite of something is something``. To fix the syntax I use the opposite of ``and`` which is ``or``

  .. code-block:: python

    def logical_disjunction(p, q):
        if not(p or q):
            return False
        return True

  Hooray! tests are passing again

* I add an else statement to be explicit

  .. code-block:: python

    def logical_disjunction(p, q):
        if not(p or q):
            return False
        else:
            return True

* the ``else`` clause that returns :doc:`True </data_structures/booleans/booleans>` can be restated as the opposite of the ``if`` statement

  .. code-block:: python

    def logical_disjunction(p, q):
        if not(p or q):
            return False
        if not(not(p or q)):
            return True

  since the ``the opposite of the opposite of something is something`` I could restate it by canceling out the ``nots``

  .. code-block:: python

    def logical_disjunction(p, q):
        if not(p or q):
            return False
        if p or q:
            return True

* I then reorder the statements

  .. code-block:: python

    def logical_disjunction(p, q):
        if p or q:
            return True
        if not(p or q):
            return False

* I restate using ``else``

  .. code-block:: python

    def logical_disjunction(p, q):
        if p or q:
            return True
        else:
            return False

* then rewrite to one line with a ``return`` statement

  .. code-block:: python

    def logical_disjunction(p, q):
        return True if p or q else return False

* using python's implicit conditional evaluation I simplify to

  .. code-block:: python

    def logical_disjunction(p, q):
        return p or q

  *VOILA!* the tests still pass and I have a simple statement that makes all 4 states pass for ``logical_disjunction``

The tests so far show that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :doc:`True </data_structures/booleans/booleans>` or :doc:`False </data_structures/booleans/booleans>`


* ``logical disjunction`` is ``or``
* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* ``logical conjunction`` is ``and``
* :doc:`False </data_structures/booleans/booleans>` is ``not True``
* :doc:`True </data_structures/booleans/booleans>` is ``not False``
* :doc:`False </data_structures/booleans/booleans>` is :doc:`False </data_structures/booleans/booleans>`
* :doc:`True </data_structures/booleans/booleans>` is :doc:`True </data_structures/booleans/booleans>`
