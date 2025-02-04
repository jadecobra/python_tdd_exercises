.. include:: ../../../links.rst

#################################################################################
truth table: Nullary and Unary Operations
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

.. contents:: table of contents
  :local:
  :depth: 1

----

Nullary operations do not take in inputs and always return the same value. They are :ref:`singleton functions<test_singleton_functions>`

*********************************************************************************
requirements
*********************************************************************************

:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with ``truth_table`` as the name of the project

*********************************************************************************
how to return to the automated tests if you exit
*********************************************************************************

.. code-block:: shell

  cd truth_table
  source .venv/bin/activate
  pytest-watch

*********************************************************************************
how to return to the automated tests on Windows_ without WSL if you exit
*********************************************************************************

.. warning:: This is for Windows_ without `Windows Subsystem Linux`_

  cd truth_table
  .venv/scripts/activate.ps1
  pytest-watch

----

red: make it fail
#################################################################################

* and change the text to

  .. code-block:: python

    import unittest
    import truth_table


    class TestNullaryOperations(unittest.TestCase):


        def test_logical_true(self):
            self.assertTrue(truth_table.logical_true())

  and the terminal shows :ref:`AttributeError` which I add to the list of Exceptions_ encountered

  .. code-block:: python

   # Exceptions Encountered
   # AssertionError
   # AttributeError

green: make it pass
#################################################################################

* I add a :doc:`singleton function </functions/test_singleton_functions>` called ``logical_true`` to ``truth_table.py``

  .. code-block:: python

    def logical_true():
        return True

  and the terminal shows passing tests which remind me that :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`

refactor: make it better
#################################################################################

* I add a test for ``logical_false`` to ``TestNullaryOperations`` class in ``test_truth_table.py``

  .. code-block:: python

    def test_logical_false(self):
        self.assertFalse(truth_table.logical_false())

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

  since there is no definition for ``logical_false`` in ``truth_table.py``
* I add a function definition for ``logical_false`` to ``truth_table.py``

  .. code-block:: python

    def logical_false():
        return True

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

  since the ``logical_false`` function currently returns a different value from what is expected
* When I make the return value to :ref:`False<test_what_is_false>`, the terminal shows passing tests

  .. code-block:: python

    def logical_false():
        return False

* I am again reminded that :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>` and :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`

----

*********************************************************************************
Unary Operations
*********************************************************************************

There are two unary operations

* Logical Identity
* Logical Negation

test_logical_identity
#################################################################################

A Logical Identity operation takes input and returns it as output, it is a :doc:`passthrough function </functions/functions_passthrough>`

red: make it fail
---------------------------------------------------------------------------------

I add a new ``TestCase`` to ``test_truth_table.py``

.. code-block:: python

  class TestUnaryOperations(unittest.TestCase):

      def test_logical_identity(self):
          self.assertTrue(truth_table.logical_identity(True))
          self.assertFalse(truth_table.logical_identity(False))

and the terminal shows :ref:`AttributeError` because there is no definition for ``logical_identity`` in ``truth_table.py``

green: make it pass
---------------------------------------------------------------------------------

I add a function definition for ``logical_identity`` to ``truth_table.py``

.. code-block:: python

  def logical_identity(value):
      return value

and the terminal shows passing tests

.. _test_logical_negation:

test_logical_negation
#################################################################################

A Logical Negation operation takes input and returns its opposite as output

red: make it fail
---------------------------------------------------------------------------------

I add a test for ``logical_negation`` to ``test_truth_table.py``

.. code-block:: python

    def test_logical_negation(self):
        self.assertFalse(truth_table.logical_negation(True))
        self.assertTrue(truth_table.logical_negation(False))

the terminal shows :ref:`AttributeError`, there is no definition for ``logical_negation`` in ``truth_table.py``

green: make it pass
---------------------------------------------------------------------------------

* I add a definition for ``logical_negation``  to ``truth_table.py`` using the solution I had for ``logical_identity``

  .. code-block:: python

    def logical_negation(value):
        return value

  the terminal shows :ref:`AssertionError`.

  The ``logical_negation`` function returns the value it receives as input but the test expects the opposite
* I use the ``not`` keyword to return the opposite of the :doc:`boolean </data_structures/booleans/booleans>` value ``logical_negation`` receives

  .. code-block:: python

    def logical_negation(value):
        return not value

  and the terminal shows passing tests


*********************************************************************************
review
*********************************************************************************

I know that

* :ref:`True<test_what_is_true>` is ``not False``
* :ref:`False<test_what_is_false>` is ``not True``
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`

----

:doc:`/code/code_truth_table`