Truth Table
===========

Sometimes I want programs to make decisions based on inputs or conditions, and can make this happen with conditional statements.

I am going to explore writing conditional statements in python with the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_ from mathematics

There are only two boolean values

* :doc:`True <data_structures_booleans>`
* :doc:`False <data_structures_booleans>`

The Truth Table gives the 16 outcomes of binary operations on these two values



Nullary Operations
------------------

Nullary operations do not take in inputs and always return the same value. They are singleton :doc:`functions`

RED: make it fail
^^^^^^^^^^^^^^^^^

I create a file called ``test_truth_table.py`` in the ``tests`` folder and add the text below

.. code-block:: python

  import unittest
  import truth_table

the terminal shows a :doc:`ModuleNotFoundError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I add :doc:`ModuleNotFoundError` to the list of exceptions encountered

  .. code-block:: python

   # Exceptions Encountered
   # AssertionError
   # ModuleNotFoundError

* I then create a file called ``truth_table.py`` in the project folder and the test passes
* I change the code in ``test_truth_table.py`` to include a failing test

  .. code-block:: python

   import unittest
   import truth_table


   class TestNullaryOperations(unittest.TestCase):


      def test_logical_true(self):
          self.assertTrue(truth_table.logical_true())

  and the terminal displays an :doc:`AttributeError` which I add to the list of exceptions encountered

  .. code-block:: python

   # Exceptions Encountered
   # AssertionError
   # ModuleNotFoundError
   # AttributeError

* I add a singleton function called ``logical_true`` to ``truth_table.py``

  .. code-block:: python

    def logical_true():
        return True

  and the terminal shows passing tests and I am reminded that :doc:`True <data_structures_booleans>` is :doc:`True <data_structures_booleans>`

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* I add a test for ``logical_false`` to the ``TestNullaryOperations`` class in ``test_truth_table.py``

  .. code-block:: python

    def test_logical_false(self):
        self.assertFalse(truth_table.logical_false())

  the terminal gives another :doc:`AttributeError` since there is no definition for ``logical_false`` in ``truth_table.py``
* I add a function definition for ``logical_false`` to ``truth_table.py``

  .. code-block:: python

    def logical_false():
      return True

  and the terminal shows an :doc:`AssertionError` since the ``logical_false`` function currently returns a different value from what is expected
* When I change the return value to :doc:`False <data_structures_booleans>`, the terminal shows passing tests

  .. code-block:: python

    def logical_false():
      return False

* I am again reminded that :doc:`False <data_structures_booleans>` is :doc:`False <data_structures_booleans>` and :doc:`True <data_structures_booleans>` is :doc:`True <data_structures_booleans>`

----

Unary Operations
----------------

There are two unary operations


* Logical Identity
* Logical Negation

Logical Identity
^^^^^^^^^^^^^^^^

A Logical Identity operation takes input and returns it as output, it is a passthrough :doc:`function <functions>`

RED: make it fail
~~~~~~~~~~~~~~~~~

I change ``test_truth_table.py`` with a new ``TestCase``

.. code-block:: python



  class TestUnaryOperations(unittest.TestCase):

    def test_logical_identity(self):
      self.assertTrue(truth_table.logical_identity(True))
      self.assertFalse(truth_table.logical_identity(False))

and the terminal shows an :doc:`AttributeError` because there is no definition for ``logical_identity`` in ``truth_table.py``

GREEN: make it pass
~~~~~~~~~~~~~~~~~~~

I add a function definition for ``logical_identity`` to ``truth_table.py``

.. code-block:: python

  def logical_identity(value):
      return value

the terminal shows passing tests

Logical Negation
^^^^^^^^^^^^^^^^

A Logical Negation operation takes input and returns its opposite as output

RED: make it fail
~~~~~~~~~~~~~~~~~

I add a test for ``logical_negation`` to ``test_truth_table.py``

.. code-block:: python

    def test_logical_negation(self):
        self.assertFalse(truth_table.logical_negation(True))
        self.assertTrue(truth_table.logical_negation(False))

the terminal shows an :doc:`AttributeError`\, there is no definition for ``logical_negation`` in ``truth_table.py``

GREEN: make it pass
~~~~~~~~~~~~~~~~~~~


* I add a definition for ``logical_negation``  to ``truth_table.py`` using the solution I had for ``logical_identity``

  .. code-block:: python

    def logical_negation(value):
        return value

  the terminal shows an :doc:`AssertionError`.

  The ``logical_negation`` function returns the value it receives as input but the test expects it to return the opposite
* The ``not`` keyword can be used to make the function return the opposite of what it receives. I change the return statement in ``logical_negation`` to return the opposite of the value it receives

  .. code-block:: python

    def logical_negation(value):
      return not value

  the terminal shows passing tests

Reviewing what I know so far


* :doc:`True <data_structures_booleans>` is ``not False``
* :doc:`False <data_structures_booleans>` is ``not True``
* :doc:`False <data_structures_booleans>` is :doc:`False <data_structures_booleans>`
* :doc:`True <data_structures_booleans>` is :doc:`True <data_structures_booleans>`

on to :doc:`/truth table 02: logical conjunction`