Truth Table
===========

Sometimes we want programs to make decisions based on inputs or conditions, and can make this happen with conditional statements. Let us explore writing conditional statements in python with Test Driven Development using the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_ from mathematics

There are two boolean values


* ``True``
* ``False``

The Truth Table gives the 16 outcomes of binary operations

Prerequisites
-------------


* :doc:`How I setup a Test Driven Development Environment`

----

Nullary Operations
------------------

Nullary operations do not take in inputs and always return the same value. They are singleton :doc:`functions`

RED: make it fail
^^^^^^^^^^^^^^^^^

create a file named ``test_truth_table.py`` in the ``tests`` folder and add the text below

.. code-block:: python

   import unittest
   import truth_table


   class TestNullaryOperations(unittest.TestCase):

       def test_logical_true(self):
           self.assertTrue(truth_table.logical_true())

the terminal updates to show a :doc:`ModuleNotFoundError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add :doc:`ModuleNotFoundError` to the list of exceptions encountered
  .. code-block:: python

     # Exceptions Encountered
     # AssertionError
     # ModuleNotFoundError

* create a file named ``truth_table.py`` in the project folder and the terminal displays an :doc:`AttributeError` which we add to our list of exceptions encountered
  .. code-block:: python

     # Exceptions Encountered
     # AssertionError
     # ModuleNotFoundError
     # AttributeError

* add a singleton function named ``logical_true`` to ``truth_table.py``
  .. code-block:: python

     def logical_true():
         return True
  the terminal updates to show passing tests and we are reminded that ``True`` is ``True``

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* add a test for ``logical_false`` to teh ``TestNullaryOperations`` class in ``test_truth_table.py``
  .. code-block:: python

       def test_logical_false(self):
           self.assertFalse(truth_table.logical_false())
  the terminal gives another :doc:`AttributeError` since there is no definition for ``logical_false`` in ``truth_table.py``
* add a function definition for ``logical_false`` to ``truth_table.py``
  .. code-block:: python

     def logical_false():
         return True
  and the terminal shows an :doc:`AssertionError` since the ``logical_false`` function currently returns a different value from what is expected
* update the return value to ``False`` and the terminal shows passing tests
  .. code-block:: python

     def logical_false():
         return False

* We are again reminded that ``False`` is ``False`` and ``True`` is ``True``

----

Unary Operations
----------------

There are two unary operations


* Logical Identity
* Logical Negation

Logical Identity
^^^^^^^^^^^^^^^^

A Logical Identity operation takes input and returns it as output, it is a passthrough :doc:`function`

RED: make it fail
~~~~~~~~~~~~~~~~~

Add a new ``TestCase`` to ``test_truth_table.py``

.. code-block:: python



   class TestUnaryOperations(unittest.TestCase):

       def test_logical_identity(self):
           self.assertTrue(truth_table.logical_identity(True))
           self.assertFalse(truth_table.logical_identity(False))

the terminal updates to show an :doc:`AttributeError` because there is no definition for ``logical_identity`` in ``truth_table.py``

GREEN: make it pass
~~~~~~~~~~~~~~~~~~~

add a function definition for ``logical_identity`` to ``truth_table.py``

.. code-block:: python

   def logical_identity(value):
       return value

the terminal updates to show passing tests

Logical Negation
^^^^^^^^^^^^^^^^

A Logical Negation operation takes input and returns its opposite as output

RED: make it fail
~~~~~~~~~~~~~~~~~

add a test for ``logical_negation`` to ``test_truth_table.py``

.. code-block:: python

       def test_logical_negation(self):
           self.assertFalse(truth_table.logical_negation(True))
           self.assertTrue(truth_table.logical_negation(False))

the terminal updates to show an :doc:`AttributeError`\ , there is no definition for ``logical_negation`` in ``truth_table.py``

GREEN: make it pass
~~~~~~~~~~~~~~~~~~~


* update ``truth_table.py`` with a definition for ``logical_negation`` using the solution we had for ``logical_identity``
  .. code-block:: python

     def logical_negation(value):
         return value
  the terminal updates to show an :doc:`AssertionError`. The ``logical_negation`` function returns the value it receives as input but the test expects it to return the opposite
* we use the ``not`` keyword to make the function return the opposite of what it receives. Update the return statement in ``logical_negation`` to return the opposite of the value it receives
  .. code-block:: python

     def logical_negation(value):
       return not value
  the terminal updates to show passing tests

Reviewing what we know so far


* ``True`` is ``not False``
* ``False`` is ``not True``
* ``False`` is ``False``
* ``True`` is ``True``

We have not written any conditional statements yet, only boolean values and their opposites. We will write some in `Logical Conjunction <./TRUTH_TABLE_02_LOGICAL_CONJUNCTION.rst>`_ next
