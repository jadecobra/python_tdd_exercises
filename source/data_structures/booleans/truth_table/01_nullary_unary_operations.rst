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
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``truth_table`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh truth_table

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: python

      ./makePythonTdd.ps1 truth_table

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_truth_table.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_truth_table.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change ``True`` to ``False`` to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

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
  :linenos:
  :emphasize-lines: 2, 5, 7-8

  import unittest
  import src.truth_table


  class TestNullaryOperations(unittest.TestCase):

      def test_logical_true(self):
          self.assertTrue(src.truth_table.logical_true())


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_true'

green: make it pass
---------------------------------------------------------------------------------

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # AttributeError

* I click on ``truth_table.py`` in the ``src`` folder_ to open it in the :ref:`editor<2 editors>`, then I add a :ref:`function<functions>`

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

test_logical_false
#################################################################################

red: make it fail
---------------------------------------------------------------------------------

I add another test to ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 4-5

      def test_logical_true(self):
          self.assertTrue(src.truth_table.logical_true())

      def test_logical_false(self):
          self.assertFalse(src.truth_table.logical_false())


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_false'. Did you mean: 'logical_true'?

green: make it pass
---------------------------------------------------------------------------------

* I add a :ref:`function<functions>` definition to ``truth_table.py``

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
  :lineno-start: 10
  :emphasize-lines: 5, 7-8

      def test_logical_false(self):
          self.assertFalse(src.truth_table.logical_false())


  class TestUnaryOperations(unittest.TestCase):

      def test_logical_identity(self):
          self.assertTrue(src.truth_table.logical_identity(True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_identity'

green: make it pass
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

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 4

    # Exceptions Encountered
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

refactor: make it better
---------------------------------------------------------------------------------

* I add another line to ``test_logical_identity`` in ``test_truth_table.py``

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

  there is a failure for the test that passed before. The expectation of the test is that when :ref:`True<test_what_is_true>` is given, the result is :ref:`True<test_what_is_true>` and when :ref:`False<test_what_is_false>` is given, the result is :ref:`False<test_what_is_true>`

* I change the `return statement`_ of the :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def logical_identity(the_input):
        return the_input

  the test passes. ``logical_identity`` returns its input as output.

----

test_logical_negation
#################################################################################

red: make it fail
---------------------------------------------------------------------------------

I add a new test to ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 5-6

      def test_logical_identity(self):
          self.assertTrue(src.truth_table.logical_identity(True))
          self.assertFalse(src.truth_table.logical_identity(False))

      def test_logical_negation(self):
          self.assertFalse(src.truth_table.logical_negation(True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_negation'

green: make it pass
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

refactor: make it better
---------------------------------------------------------------------------------

* I add another line in ``test_logical_negation`` in ``test_truth_table.py``

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

* I make the :ref:`function<functions>` return its input

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def logical_negation(the_input):
        return the_input

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

  the expectation of the test is that when :ref:`True<test_what_is_true>` is given, the result is :ref:`False<test_what_is_false>` and when :ref:`False<test_what_is_false>` is given, the result is :ref:`True<test_what_is_true>`, I can make that happen with the "not_" keyword. I add it to the `return statement`_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def logical_negation(the_input):
        return not the_input

  the test passes. ``logical_negation`` returns the opposite of its input

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


    # Exceptions Encountered

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

Would you like to :ref:`test binary operations?<truth table: Binary Operations part 1>`

----

:ref:`truth table: tests and solutions`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->