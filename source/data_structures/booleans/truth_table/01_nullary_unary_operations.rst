.. meta::
  :description: Stumped by Python's logic? Master nullary and unary operations with our easy-to-follow truth table tutorial. Learn the key differences and start coding.
  :keywords: Jacob Itegboje, python nullary vs unary operations, python truth table tutorial for beginners, logical identity and negation in python, test-driven development with python for truth tables, python boolean logic explained for data structures, how to implement logical operations in python from scratch, what are nullary functions in python, python logical operators and, or, not examples

.. include:: ../../../links.rst

#################################################################################
truth table: Nullary and Unary Operations
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/HL4kNmo3UIo?si=sv1CU9Flu7kybun5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

.. contents:: table of contents
  :local:
  :depth: 2

----

*********************************************************************************
requirements
*********************************************************************************

:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with ``truth_table`` as the name of the project

----

*********************************************************************************
Nullary Operations
*********************************************************************************

There are 2 Nullary operations, they do not take input and always return the same value

* :ref:`Logical True<test_logical_true>`
* :ref:`Logical False<test_logical_false>`

test_logical_true
#################################################################################

red: make it fail
---------------------------------------------------------------------------------

I change the text in ``test_truth_table.py``

.. code-block:: python

  import unittest
  import src.truth_table


  class TestNullaryOperations(unittest.TestCase):

      def test_logical_true(self):
          self.assertTrue(src.truth_table.logical_true())

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'logical_true'


green: make it pass
---------------------------------------------------------------------------------

I add it to the list of Exceptions_ encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # AttributeError

then I add a :ref:`function<functions>` to ``truth_table.py``

.. code-block:: python

  def logical_true():
      return None

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: None is not true

I change :ref:`False <test_what_is_false>` to :ref:`True <test_what_is_true>` in the `return statement`_

.. code-block:: python

  def logical_true():
      return True

and the test passes

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
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_false'. Did you mean: 'logical_true'?

green: make it pass
---------------------------------------------------------------------------------

* I add a :ref:`function<functions>` definition to ``truth_table.py``

  .. code-block:: python

    def logical_true():
        return True


    def logical_false():
        return True

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

* When I change :ref:`True <test_what_is_true>` to :ref:`False<test_what_is_false>` in the `return statement`_

  .. code-block:: python

    def logical_false():
        return False

  the test passes

----

*********************************************************************************
Unary Operations
*********************************************************************************

There are 2 unary operations, they each take one input

* :ref:`Logical Identity<test_logical_identity>`
* :ref:`Logical Negation<test_logical_negation>`

test_logical_identity
#################################################################################

red: make it fail
---------------------------------------------------------------------------------

I add a new TestCase_ and a test to ``test_truth_table.py``

.. code-block:: python

  class TestNullaryOperations(unittest.TestCase):
      ...


  class TestUnaryOperations(unittest.TestCase):

      def test_logical_identity(self):
          self.assertTrue(src.truth_table.logical_identity(True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'logical_identity'

green: make it pass
---------------------------------------------------------------------------------

* I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_false():
        return False


    def logical_identity():
        return False

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
        return False

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

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

when I change the `return statement`_

.. code-block:: python

    def logical_identity(argument):
        return False

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: False is not true

there is a failure for the line that passed before. The expectation of the test is that when :ref:`True<test_what_is_true>` is given, the result is :ref:`True<test_what_is_true>` and when :ref:`False<test_what_is_false>` is given, the result is :ref:`False<test_what_is_true>`. I make ``logical_identity`` return its input

.. code-block:: python

  def logical_identity(argument):
      return argument

the terminal shows passing tests. ``logical_identity`` returns its input as output.

----

test_logical_negation
#################################################################################

red: make it fail
---------------------------------------------------------------------------------

I add a new test

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

* I add a definition for it

  .. code-block:: python


    def logical_identity(argument):
        return argument


    def logical_negation(argument):
        return argument

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  when I make it return False_

  .. code-block:: python

    def logical_negation(argument):
        return False

  the terminal shows passing tests

refactor: make it better
---------------------------------------------------------------------------------

* I add the next case

  .. code-block:: python

    def test_logical_negation(self):
        self.assertFalse(src.truth_table.logical_negation(True))
        self.assertTrue(src.truth_table.logical_negation(False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the `return statement`_

  .. code-block:: python

    def logical_negation(argument):
        return True

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  it fails for the line that passed before. When I make the :ref:`function<functions>` return its input

  .. code-block:: python

    def logical_negation(argument):
        return argument

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  the expectation of the test is that when :ref:`True<test_what_is_true>` is given, the result is :ref:`False<test_what_is_false>` and when :ref:`False<test_what_is_false>` is given, the result is :ref:`True<test_what_is_true>`, I can make that happen with the "not_" keyword

  .. code-block:: python

    def logical_negation(argument):
        return not argument

  the terminal shows passing tests. ``logical_negation`` returns the opposite of its input

* I change the name of the test

  .. code-block:: python

    def test_logical_negation_aka_not(self):
        self.assertFalse(src.truth_table.logical_negation(True))
        self.assertFalse(src.truth_table.logical_negation(False))

----

*********************************************************************************
review
*********************************************************************************

I ran tests for :ref:`Nullary<Nullary Operations>` and :ref:`Unary operations<Unary Operations>`. Would you like to :ref:`test binary operations?<truth table: Binary Operations part 1>`

----

:doc:`/code/code_truth_table`