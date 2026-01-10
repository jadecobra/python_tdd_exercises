.. meta::
  :description: Stumped by Python's logic? Master nullary and unary operations with our easy-to-follow truth table tutorial. Learn the key differences and start coding.
  :keywords: Jacob Itegboje, python nullary vs unary operations, python truth table tutorial for beginners, logical identity and negation in python, test-driven development with python for truth tables, python boolean logic explained for data structures, how to implement logical operations in python from scratch, what are nullary functions in python, python logical operators and, or, not examples

.. include:: ../../../links.rst

#################################################################################
truth table: Nullary and Unary Operations
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/HL4kNmo3UIo?si=sv1CU9Flu7kybun5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
questions about Nullary and Unary Operations
*********************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`What are the Nullary Operations?<Nullary Operations>`
* :ref:`How many inputs do Nullary Operations take?<Nullary Operations>`
* :ref:`What are the Unary Operations?<Unary Operations>`
* :ref:`How many inputs do Unary Operations take?<Unary Operations>`
* :ref:`What is a function that returns its input as output?<test_logical_identity>`
* :ref:`What is a function that returns the negation of its input?<test_logical_negation>`
* :ref:`How can I return the opposite of a boolean?<how to return the opposite of a boolean>`

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`booleans: truth table`

----

*********************************************************************************
Nullary Operations
*********************************************************************************

There are 2 Nullary operations - :ref:`Logical True<test_logical_true>` and :ref:`Logical False<test_logical_false>`. They do NOT take input and return :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

=================================================================================
test_logical_true
=================================================================================

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

I change the :ref:`class<classes>` and :ref:`method<functions>` in ``test_truth_table.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 5, 7-8

  import unittest
  import src.truth_table


  class TestNullaryOperations(unittest.TestCase):

      def test_logical_true(self):
          self.assertTrue(src.truth_table.logical_true())


  # Exceptions seen

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_true'

I have not added a definition for ``logical_true`` to ``truth_table.py`` in the ``src`` folder_

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

* I add it to the list of :ref:`Exceptions<errors>` seen in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

    # Exceptions seen
    # AssertionError
    # AttributeError

* I open ``truth_table.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>` of my `Integrated Development Environment (IDE)`_, then I add a :ref:`function<functions>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-

    def logical_true():
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not true

  I change :ref:`False <test_what_is_false>` to :ref:`True <test_what_is_true>` in the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def logical_true():
        return True

  the test passes

* Adding the ``logical_true`` :ref:`function<functions>` to ``truth_table.py`` solved the :ref:`AttributeError`
* ``logical_true`` always returns :ref:`True<test_what_is_true>`
* ``logical_true`` does not take any input

=================================================================================
test_logical_false
=================================================================================

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

I add another test in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 4-5

      def test_logical_true(self):
          self.assertTrue(src.truth_table.logical_true())

      def test_logical_false(self):
          self.assertFalse(src.truth_table.logical_false())


  # Exceptions seen

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_false'. Did you mean: 'logical_true'?

I have not added a definition for ``logical_false`` to ``truth_table.py``, I only added one for ``logical_true``

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

* I add a :ref:`function<functions>` definition in ``truth_table.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def logical_true():
        return True


    def logical_false():
        return True

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I change :ref:`True <test_what_is_true>` to :ref:`False<test_what_is_false>` in the `return statement`_

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def logical_false():
        return False

  the test passes

* Adding the ``logical_true`` and ``logical_false``:ref:`function<functions>` to ``truth_table.py`` solved the :ref:`AttributeError` in both cases
* ``logical_true`` always returns :ref:`True<test_what_is_true>`
* ``logical_false`` always returns :ref:`False<test_what_is_false>`
* both Nullary Operations do not take input

----

*********************************************************************************
Unary Operations
*********************************************************************************

There are 2 unary operations

* :ref:`Logical Identity<test_logical_identity>` and
* :ref:`Logical Negation<test_logical_negation>`

they each take one input and return :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

=================================================================================
test_logical_identity
=================================================================================

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

I add a new TestCase_ and a test for Unary Operations to ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 5, 7-8

      def test_logical_false(self):
          self.assertFalse(src.truth_table.logical_false())


  class TestUnaryOperations(unittest.TestCase):

      def test_logical_identity(self):
          self.assertTrue(src.truth_table.logical_identity(True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_identity'

I need to add a definition for it

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

* I add the :ref:`function<functions>` to ``truth_table.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def logical_false():
        return False


    def logical_identity():
        return False

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: logical_identity() takes 0 positional arguments but 1 was given

  I need to make the :ref:`function<functions>` accept input since the test sends :ref:`True<test_what_is_true>` as input

* I add the error to the list of :ref:`Exceptions<errors>` seen in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 4

    # Exceptions seen
    # AssertionError
    # AttributeError
    # TypeError

* I add a name in parentheses for ``logical_identity`` to take input in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

    def logical_identity(the_input):
        return False

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

  I change the `return statement`_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def logical_identity(the_input):
        return True

  the test passes

---------------------------------------------------------------------------------
:yellow:`REFACTOR`: make it better
---------------------------------------------------------------------------------

* I add another line to ``test_logical_identity`` in ``test_truth_table.py`` for the case when ``logical_identity`` gets :ref:`False<test_what_is_false>` as input

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3

        def test_logical_identity(self):
            self.assertTrue(src.truth_table.logical_identity(True))
            self.assertFalse(src.truth_table.logical_identity(False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I change the `return statement`_ of ``logical_identity`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def logical_identity(the_input):
        return False

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

  there is a failure for the test that passed before. The expectation of the test is that when :ref:`True<test_what_is_true>` is given, the result is :ref:`True<test_what_is_true>` and when :ref:`False<test_what_is_false>` is given, the result is :ref:`False<test_what_is_false>`

* I change the `return statement`_ of the :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def logical_identity(the_input):
        return the_input

  the test passes.

``logical_identity`` returns its input as output. I think of it as a passthrough :ref:`function<functions>`, it does not process the input it gets, it just passes it along.

----

=================================================================================
test_logical_negation
=================================================================================

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

I add a new test to ``test_truth_table.py`` for ``logical_negation``

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 5-6

      def test_logical_identity(self):
          self.assertTrue(src.truth_table.logical_identity(True))
          self.assertFalse(src.truth_table.logical_identity(False))

      def test_logical_negation(self):
          self.assertFalse(src.truth_table.logical_negation(True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_negation'

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

I add a definition for the :ref:`function<functions>` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 9
  :emphasize-lines: 5-6

  def logical_identity(the_input):
      return the_input


  def logical_negation(the_input):
      return the_input

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: True is not false

I change the `return statement`_

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 2

  def logical_negation(the_input):
      return False

the test passes

---------------------------------------------------------------------------------
:yellow:`REFACTOR`: make it better
---------------------------------------------------------------------------------

* I add another line to ``test_logical_negation`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 3

        def test_logical_negation(self):
            self.assertFalse(src.truth_table.logical_negation(True))
            self.assertTrue(src.truth_table.logical_negation(False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

* I change the `return statement`_ of the ``logical_negation`` :ref:`function<functions>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def logical_negation(the_input):
        return True

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

  the test fails for the line that passed before

* I make the :ref:`function<functions>` return its input, remember the :ref:`identity function<test_identity_function>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def logical_negation(the_input):
        return the_input

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

  the expectation of the test is that when :ref:`True<test_what_is_true>` is given, the result is :ref:`False<test_what_is_false>` and when :ref:`False<test_what_is_false>` is given, the result is :ref:`True<test_what_is_true>`

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
how to return the opposite of a boolean
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* I can make this happen with the "not_" keyword which returns the opposite of the :ref:`boolean<booleans>` after it. I add it to the `return statement`_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def logical_negation(the_input):
        return not the_input

  the test passes


* I change the name of the test

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 7

    class TestUnaryOperations(unittest.TestCase):

        def test_logical_identity(self):
            self.assertTrue(src.truth_table.logical_identity(True))
            self.assertFalse(src.truth_table.logical_identity(False))

        def test_logical_negation_aka_not(self):
            self.assertFalse(src.truth_table.logical_negation(True))
            self.assertTrue(src.truth_table.logical_negation(False))


    # Exceptions seen

``logical_negation`` aka not_ returns the opposite of its input

* when it receives :ref:`True<test_what_is_true>` it returns :ref:`False<test_what_is_false>`
* when it receives :ref:`False<test_what_is_false>` it returns :ref:`True<test_what_is_true>`

----

*********************************************************************************
review
*********************************************************************************

I ran the following tests for :ref:`Nullary<Nullary Operations>`

* :ref:`test_logical_true`
* :ref:`test_logical_false`

and

for :ref:`Unary operations<Unary Operations>`

* :ref:`test_logical_identity`
* :ref:`test_logical_negation`

:ref:`How many questions can you answer after going through this chapter?<questions about Nullary and Unary Operations>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed for the Truth Table?<truth table: tests and solutions>`

----

*********************************************************************************
what is next?
*********************************************************************************

Would you like to :ref:`test binary operations?<truth table: Binary Operations part 1>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please leave a 5 star review. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->