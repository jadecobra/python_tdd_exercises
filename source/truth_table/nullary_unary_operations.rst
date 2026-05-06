.. meta::
  :description: Stumped by Python's logic? Master nullary and unary operations with our easy-to-follow truth table tutorial. Learn the key differences and start coding.
  :keywords: Jacob Itegboje, python nullary vs unary operations, python truth table tutorial for beginners, logical identity and negation in python, test-driven development with python for truth tables, python boolean logic explained for data structures, how to implement logical operations in python from scratch, what are nullary functions in python, python logical operators and, or, not examples

.. include:: ../links.rst

.. _not: https://docs.python.org/3/reference/expressions.html#not

#################################################################################
truth table: Nullary and Unary Operations
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/HL4kNmo3UIo?si=sv1CU9Flu7kybun5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapters

.. literalinclude:: ../code/truth_table/tests/test_nullary_unary.py
  :language: python
  :linenos:

----

*********************************************************************************
questions about Nullary and Unary Operations
*********************************************************************************

There are answers to these questions in this chapter

* :ref:`what are the Nullary Operations?<Nullary Operations>`
* :ref:`How many inputs do Nullary Operations take?<Nullary Operations>`
* :ref:`what are the Unary Operations?<Unary Operations>`
* :ref:`How many inputs do Unary Operations take?<Unary Operations>`
* :ref:`what is a function that returns its input as output?<test_logical_identity>`
* :ref:`what is a function that returns the negation of its input?<test_logical_negation>`
* :ref:`how can I return the opposite of a boolean?<how to return the opposite of a boolean>`

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`truth table`

----

*********************************************************************************
Nullary Operations
*********************************************************************************

There are 2 Nullary operations - :ref:`Logical True<test_logical_true>` and :ref:`Logical False<test_logical_false>`. They do not take input and always return :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

----

=================================================================================
test_logical_true
=================================================================================

----

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

----

* I open the :ref:`Explorer<explorer on left>` to change the name of ``test_truth_table.py``

* I right click on ``test_truth_table.py`` select ``Rename`` then change it to ``test_nullary_unary.py``

* I change the names of the :ref:`class<what is a class?>` and :ref:`method<what is a function?>` in ``test_nullary_unary.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5, 7-8

    import src.truth_table
    import unittest


    class TestNullaryOperations(unittest.TestCase):

        def test_logical_true(self):
            self.assertTrue(src.truth_table.logical_true())


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_true'

  because I have not added a definition for :ref:`logical_true<test_logical_true>` to ``truth_table.py`` in the ``src`` folder_

----

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

----

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_nullary_unary.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # AttributeError

  I use the :ref:`Explorer<explorer on left>` to open ``truth_table.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>` of my `Integrated Development Environment (IDE)`_

* I add a :ref:`function<what is a function?>` to ``truth_table.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-

    def logical_true():
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not true

  because the :ref:`function<what is a function?>` returns :ref:`None<what is None?>` and the test expects :ref:`True<test_what_is_true>`

* I change :ref:`None<what is None?>` to :ref:`True <test_what_is_true>` in the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def logical_true():
        return True

  the test passes

:ref:`logical_true does not take any input and always returns True<test_logical_true>`

----

=================================================================================
test_logical_false
=================================================================================

----

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

----

I add another test to ``test_nullary_unary.py``

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 6-7

  class TestNullaryOperations(unittest.TestCase):

      def test_logical_true(self):
          self.assertTrue(src.truth_table.logical_true())

      def test_logical_false(self):
          self.assertFalse(src.truth_table.logical_false())


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_false'. Did you mean: 'logical_true'?

because I have not added a definition for :ref:`logical_false<test_logical_false>` to ``truth_table.py``, I only added one for :ref:`logical_true<test_logical_true>`

----

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

----

* I add a :ref:`function<what is a function?>` to ``truth_table.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def logical_true():
        return True


    def logical_false():
        return True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returns :ref:`True<test_what_is_true>` and the test expects :ref:`False<test_what_is_false>`

* I change :ref:`True <test_what_is_true>` to :ref:`False<test_what_is_false>` in the `return statement`_

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def logical_false():
        return False

  the test passes

.. NOTE::

  * :ref:`logical_true<test_logical_true>` always returns :ref:`True<test_what_is_true>`
  * :ref:`logical_false<test_logical_false>` always returns :ref:`False<test_what_is_false>`
  * both Nullary Operations do not take input

  ==============  ========================================
  return          operation
  ==============  ========================================
  :green:`True`   :ref:`logical_true<test_logical_true>`
  :red:`False`    :ref:`logical_false<test_logical_false>`
  ==============  ========================================

----

*********************************************************************************
Unary Operations
*********************************************************************************

There are 2 unary operations: :ref:`Logical Identity<test_logical_identity>` and :ref:`Logical Negation<test_logical_negation>`, they each take one input and return :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

----

=================================================================================
test_logical_identity
=================================================================================

----

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

----

I add a new TestCase_ for Unary Operations with a test for :ref:`logical_identity<test_logical_identity>` when it gets :ref:`True<test_what_is_true>` as input

==============  =============
input           output
==============  =============
:green:`True`   :green:`True`
==============  =============

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 10, 12-14

  class TestNullaryOperations(unittest.TestCase):

      def test_logical_true(self):
          self.assertTrue(src.truth_table.logical_true())

      def test_logical_false(self):
          self.assertFalse(src.truth_table.logical_false())


  class TestUnaryOperations(unittest.TestCase):

      def test_logical_identity(self):
          reality = src.truth_table.logical_identity(True)
          self.assertTrue(reality)


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_identity'

because I need to add a definition for :ref:`logical_identity<test_logical_identity>` to ``truth_table.py``

----

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

----

* I add the :ref:`function<what is a function?>` to ``truth_table.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def logical_false():
        return False


    def logical_identity():
        return False

  the terminal_ is my friend, and shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: logical_identity() takes 0 positional arguments but 1 was given

  because the test called the :ref:`logical_identity function<test_logical_identity>` with 1 argument and this definition only takes calls with 0 arguments

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_nullary_unary.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 4
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # AttributeError
    # TypeError

* I add a name in parentheses for :ref:`logical_identity<test_logical_identity>` to take calls with 1 input, in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

    def logical_identity(the_input):
        return False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  because the :ref:`function<what is a function?>` returns :ref:`False<test_what_is_false>` and the test expects :ref:`True<test_what_is_true>`

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def logical_identity(the_input):
        return True

  the test passes

----

---------------------------------------------------------------------------------
:yellow:`REFACTOR`: make it better
---------------------------------------------------------------------------------

----

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_logical_identity` in ``test_nullary_unary.py`` for the case when it gets :ref:`False<test_what_is_false>` as input

  ==============  =============
  input           output
  ==============  =============
  :red:`False`    :red:`False`
  ==============  =============

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4-5

        def test_logical_identity(self):
            reality = src.truth_table.logical_identity(True)
            self.assertTrue(reality)
            reality = src.truth_table.logical_identity(False)
            self.assertFalse(reality)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returns :ref:`True<test_what_is_true>` and the test expects :ref:`False<test_what_is_false>`

* I change the `return statement`_ of :ref:`logical_identity<test_logical_identity>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def logical_identity(the_input):
        return False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  because the :ref:`assertion<what is an assertion?>` that was passing before, expects :ref:`True<test_what_is_true>` and the :ref:`function<what is a function?>` now returns :ref:`False<test_what_is_false>`

* I change the `return statement`_ of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def logical_identity(the_input):
        return the_input

  the test passes.

  .. TIP::

    ``the_input`` is a name, I can use any name.

  This is what happens when the :ref:`logical_identity function<test_logical_identity>` is called

  - it returns :green:`True` if the input is :ref:`True<test_what_is_true>`
  - it returns :red:`False` if the input is :ref:`False<test_what_is_false>`
  - it returns the input as output

  ==============  =============
  input           output
  ==============  =============
  :green:`True`   :green:`True`
  :red:`False`    :red:`False`
  ==============  =============

----

=================================================================================
test_logical_negation
=================================================================================

----

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

----

I add a test for :ref:`logical_negation<test_logical_negation>` with an :ref:`assertion<what is an assertion?>` for when it gets :ref:`True<test_what_is_true>` as input, to ``test_nullary_unary.py``

==============  =============
input           output
==============  =============
:green:`True`   :red:`False`
==============  =============

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 7-9

      def test_logical_identity(self):
          reality = src.truth_table.logical_identity(True)
          self.assertTrue(reality)
          reality = src.truth_table.logical_identity(False)
          self.assertFalse(reality)

      def test_logical_negation(self):
          reality = src.truth_table.logical_negation(True)
          self.assertFalse(reality)


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_negation'

there is no definition for :ref:`logical_negation<test_logical_negation>` in ``truth_table.py``

----

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

----

* I add the :ref:`function<what is a function?>` to ``truth_table.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def logical_identity(the_input):
        return the_input


    def logical_negation(the_input):
        return the_input

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returned :ref:`True<test_what_is_true>` and the test expects :ref:`False<test_what_is_false>`

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def logical_negation(the_input):
        return False

  the test passes

----

---------------------------------------------------------------------------------
:yellow:`REFACTOR`: make it better
---------------------------------------------------------------------------------

----

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_logical_negation` for when :ref:`logical_negation<test_logical_negation>` gets :ref:`False<test_what_is_false>` as input, in ``test_nullary_unary.py``

  ==============  =============
  input           output
  ==============  =============
  :red:`False`    :green:`True`
  ==============  =============

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4-5

        def test_logical_negation(self):
            reality = src.truth_table.logical_negation(True)
            self.assertFalse(reality)
            reality = src.truth_table.logical_negation(False)
            self.assertTrue(reality)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  because the :ref:`function<what is a function?>` returns :ref:`False<test_what_is_false>` and the new :ref:`assertion<what is an assertion?>` expects :ref:`True<test_what_is_true>`

* I change the `return statement`_ of the :ref:`logical_negation function<test_logical_negation>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def logical_negation(the_input):
        return True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

  the test fails for the :ref:`assertion<what is an assertion?>` that passed before, because the :ref:`function<what is a function?>` now returns :ref:`True<test_what_is_true>` and that :ref:`assertion<what is an assertion?>` expects :ref:`False<test_what_is_false>`

* I make the :ref:`function<what is a function?>` return its input again

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def logical_negation(the_input):
        return the_input

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

  this means the expectation of the test is that the :ref:`logical_negation function<test_logical_negation>`

  - returns :ref:`True<test_what_is_true>` if the input is :ref:`False<test_what_is_false>`
  - returns :ref:`False<test_what_is_false>` if the input is :ref:`True<test_what_is_true>`
  - returns the opposite of the input it gets

----

=================================================================================
how to return the opposite of a boolean
=================================================================================

----

* I can use the "not_" keyword to return the opposite of the :ref:`boolean<what are booleans?>` after it. I add it to the `return statement`_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def logical_negation(the_input):
        return not the_input

  the test passes. This is what happens when the :ref:`logical_identity function<test_logical_identity>` is called

  - it returns :red:`False` if the input is :ref:`True<test_what_is_true>`
  - it returns :green:`True` if the input is :ref:`False<test_what_is_false>`
  - it returns the opposite of the input, as output

* I add to the name of the test

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 7
    :emphasize-text: _aka_not

        def test_logical_identity(self):
            reality = src.truth_table.logical_identity(True)
            self.assertTrue(reality)
            reality = src.truth_table.logical_identity(False)
            self.assertFalse(reality)

        def test_logical_negation_aka_not(self):
            reality = src.truth_table.logical_negation(True)
            self.assertFalse(reality)
            reality = src.truth_table.logical_negation(False)
            self.assertTrue(reality)


    # Exceptions seen

:ref:`logical_negation also known as not returns the opposite of its input<test_logical_negation>`

==============  =============
input           output
==============  =============
:green:`True`   :red:`False`
:red:`False`    :green:`True`
==============  =============

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I can call the :ref:`logical_negation function<test_logical_negation>` directly in the test, I do not need the ``reality`` :ref:`variables<what is a variable?>` because they are only used once for each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3-4, 6-7

        def test_logical_negation_aka_not(self):
            reality = src.truth_table.logical_negation(True)
            # self.assertFalse(reality)
            self.assertFalse(src.truth_table.logical_negation(True))
            reality = src.truth_table.logical_negation(False)
            # self.assertTrue(reality)
            self.assertTrue(src.truth_table.logical_negation(False))


    # Exceptions seen

  the test is still green

* I remove the commented lines and unused :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 22

        def test_logical_negation_aka_not(self):
            self.assertFalse(src.truth_table.logical_negation(True))
            self.assertTrue(src.truth_table.logical_negation(False))


    # Exceptions seen

* I call the :ref:`logical_identity function<test_logical_identity>` directly, in its test

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3-4, 6-7

        def test_logical_identity(self):
            reality = src.truth_table.logical_identity(True)
            # self.assertTrue(reality)
            self.assertTrue(src.truth_table.logical_identity(True))
            reality = src.truth_table.logical_identity(False)
            # self.assertFalse(reality)
            self.assertFalse(src.truth_table.logical_identity(False))

        def test_logical_negation_aka_not(self):

  still green

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_logical_identity`

  .. code-block:: python
    :lineno-start: 16

        def test_logical_identity(self):
            self.assertTrue(src.truth_table.logical_identity(True))
            self.assertFalse(src.truth_table.logical_identity(False))

        def test_logical_negation_aka_not(self):

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_nullary_unary.py`` and ``truth_table.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``truth_table``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I ran these tests for :ref:`Nullary Operations<Nullary Operations>` which take no input

* :ref:`test_logical_true`
* :ref:`test_logical_false``

and for :ref:`Unary operations<Unary Operations>` which take 1 input

* :ref:`test_logical_identity`
* :ref:`test_logical_negation`

the :ref:`truth table` for :ref:`Unary Operations<Unary Operations>` is

==============  ============= ============= ====================================================
return          True          False         operation
==============  ============= ============= ====================================================
the_input       :green:`True` :red:`False`  :ref:`logical_identity<test_logical_identity>`
not the_input   :red:`False`  :green:`True` :ref:`logical_negation (NOT)<test_logical_negation>`
==============  ============= ============= ====================================================

:ref:`How many questions can you answer after going through this chapter?<questions about Nullary and Unary Operations>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed for the Truth Table?<truth table: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like to test binary operations? they take 2 inputs<truth table: Binary Operations>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->