.. include:: ../../../links.rst

#################################################################################
truth table: Nullary and Unary Operations
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with ``truth_table`` as the name of the project

----

*********************************************************************************
Nullary Operations
*********************************************************************************

Nullary operations do not take input and always return the same value. They are :ref:`singleton functions<test_singleton_functions>`

test_logical_true
#################################################################################

red: make it fail
---------------------------------------------------------------------------------

* I change the text in ``test_truth_table.py`` to

  .. code-block:: python

    import unittest
    import src.truth_table


    class TestNullaryOperations(unittest.TestCase):

        def test_logical_true(self):
            self.assertTrue(src.truth_table.logical_true())

  and the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'logical_true'

* I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError

green: make it pass
---------------------------------------------------------------------------------

* then I add a :ref:`function<functions>` to ``truth_table.py``

  .. code-block:: python

    def logical_true():
        return True

  and the terminal shows passing tests which remind me that :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`

test_logical_false
#################################################################################

red: make it fail
---------------------------------------------------------------------------------

I add another test

.. code-block:: python

  def test_logical_true(self):
      self.assertTrue(src.truth_table.logical_true())

  def test_logical_false(self):
      self.assertFalse(src.truth_table.logical_false())

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'logical_false'. Did you mean: 'logical_true'?

green: make it pass
---------------------------------------------------------------------------------

* I add a :ref:`function<functions>` definition to ``truth_table.py``

  .. code-block:: python

    def logical_true():
        return True


    def logical_false():
        return True

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not False

* When I change the `return statement`_

  .. code-block:: python

    def logical_false():
        return False

  the test passes

* I am reminded that :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>` and :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`

----

*********************************************************************************
Unary Operations
*********************************************************************************

There are two unary operations

* :ref:`Logical Identity<test_logical_identity>`
* :ref:`Logical Negation<test_logical_negation>`

test_logical_identity
#################################################################################

`Logical Identity`_ is a :ref:`passthrough function<test_passthrough_functions>`, it takes input and returns it

red: make it fail
---------------------------------------------------------------------------------

I add a new TestCase_ to ``test_truth_table.py``

.. code-block:: python

  class TestUnaryOperations(unittest.TestCase):

      def test_logical_identity(self):
          self.assertTrue(src.truth_table.logical_identity(True))

and the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'logical_identity'

green: make it pass
---------------------------------------------------------------------------------

* I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_false():
        return False


    def logical_identity():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: logical_identity() takes 0 positional arguments but 1 was given

  I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # TypeError

  then I add a parameter

  .. code-block:: python

    def logical_identity(argument):
        return None

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not true

  I change the `return statement`_

  .. code-block:: python

    def logical_identity(argument):
        return True

  and the test passes

refactor: make it better
---------------------------------------------------------------------------------

I add another line to the test

.. code-block:: python

  def test_logical_identity(self):
      self.assertTrue(src.truth_table.logical_identity(True))
      self.assertFalse(src.truth_table.logical_identity(False))

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: True is not false

I make ``logical_identity`` return its input

.. code-block:: python

  def logical_identity(argument):
      return argument

and the terminal shows passing tests

----

test_logical_negation
#################################################################################

`Logical Negation`_ takes input and returns the opposite

red: make it fail
---------------------------------------------------------------------------------

I add a test for it

.. code-block:: python

  def test_logical_identity(self):
      self.assertTrue(src.truth_table.logical_identity(True))
      self.assertFalse(src.truth_table.logical_identity(False))

  def test_logical_negation(self):
      self.assertFalse(src.truth_table.logical_negation(True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'logical_negation'

green: make it pass
---------------------------------------------------------------------------------

* I add a definition for ``logical_negation``  to ``truth_table.py`` using the solution I had for ``logical_identity``

  .. code-block:: python


    def logical_identity(argument):
        return argument


    def logical_negation(argument):
        return argument

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  The ``logical_negation`` :ref:`function<functions>` returns the value it receives as input but the test expects the opposite
* I add the not_ keyword to the `return statement`_

  .. code-block:: python

    def logical_negation(argument):
        return not argument

  and the terminal shows passing tests

refactor: make it better
---------------------------------------------------------------------------------

I add another line

.. code-block:: python

  def test_logical_negation(self):
      self.assertFalse(src.truth_table.logical_negation(True))
      self.assertFalse(src.truth_table.logical_negation(False))

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: True is not false

when I change the :ref:`method<functions>`

.. code-block:: python

  def test_logical_negation(self):
      self.assertFalse(src.truth_table.logical_negation(True))
      self.assertTrue(src.truth_table.logical_negation(False))

the test passes

----

*********************************************************************************
review
*********************************************************************************

the tests show that

* :ref:`True<test_what_is_true>` is not_ :ref:`False<test_what_is_false>`
* :ref:`False<test_what_is_false>` is not_ :ref:`True<test_what_is_true>`
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`

----

:doc:`/code/code_truth_table`