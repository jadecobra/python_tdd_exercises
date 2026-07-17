.. meta::
  :description: Nullary and Unary Operations in Python with Test Driven Development (Pumping Python, Jacob Itegboje). Rename tests/test_truth_table.py to test_nullary_unary.py, import src.truth_table, and build Nullary Operations (logical_true always returns True; logical_false always returns False — zero inputs) then Unary Operations (logical_identity returns the_input; logical_negation aka not returns not the_input — one input). Red-Green-Refactor with AttributeError module has no attribute logical_true/logical_false/logical_identity/logical_negation, TypeError logical_identity() takes 0 positional arguments but 1 was given, AssertionError None is not true, True is not false, False is not true. Reuses assertTrue and assertFalse; ends with unary truth-table review and test_logical_negation_aka_not. Part of the truth_table project after project setup.
  :keywords: Jacob Itegboje, Pumping Python, nullary operations python, unary operations python, logical_true logical_false, logical_identity the_input, logical_negation not keyword, test_nullary_unary.py, test_logical_negation_aka_not, AttributeError has no attribute logical_true, TypeError takes 0 positional arguments but 1 was given, AssertionError None is not true, assertTrue assertFalse truth table, return opposite of boolean python, TDD red green refactor nullary unary, truth table one variable, python boolean logic beginners

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

These are the tests I have at the end of the chapter

.. literalinclude:: ../code/truth_table/tests/test_nullary_unary.py
  :language: python
  :linenos:

----

*********************************************************************************
questions about Nullary and Unary Operations
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`what are the Nullary Operations?<Nullary Operations>`
* :ref:`How many inputs do Nullary Operations take?<Nullary Operations>`
* :ref:`what are the Unary Operations?<Unary Operations>`
* :ref:`How many inputs do Unary Operations take?<Unary Operations>`
* :ref:`what is a function that returns its input as output?<test_logical_identity>`
* :ref:`what is not?<test_logical_negation>`
* :ref:`what is a function that returns the negation of its input as output?<test_logical_negation>`
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

There are 2 Nullary operations - :ref:`Logical True<test_logical_true>` and :ref:`Logical False<test_logical_false>`. They do not take input and always return :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`.

----

=================================================================================
test_logical_true
=================================================================================

----

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

----

* I go to the other terminal_

* I use mv_ to change the name of ``test_truth_table.py`` to ``test_nullary_unary.py``

  .. code-block:: python
    :emphasize-lines: 1

    mv tests/test_truth_table.py tests/test_nullary_unary.py

* I open ``test_nullary_unary.py`` from the ``tests`` folder_

* I add an `import statement`_ at the top of ``test_nullary_unary.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.truth_table
    import unittest

* I change the name of the :ref:`class<everything is an object>` from ``TestTruthTable`` to ``TestNullaryOperations``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.truth_table
    import unittest


    class TestNullaryOperations(unittest.TestCase):

        def test_failure(self):

* I change :ref:`test_failure` to :ref:`test_logical_true`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-6

    class TestNullaryOperations(unittest.TestCase):

        def test_logical_true(self):
            self.assertTrue(
                src.truth_table.logical_true()
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_true'

  because I have not added a definition for :ref:`logical_true<test_logical_true>` to ``truth_table.py`` in the ``src`` folder_.

----

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

----

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen, in ``test_nullary_unary.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # AttributeError

* I open ``truth_table.py`` from the ``src`` folder_

* I remove all the text in the file_ then add a :ref:`function<what is a function?>` to ``truth_table.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def logical_true():
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

  because the :ref:`function<what is a function?>` returns :ref:`None<what is None?>` and the :ref:`assertion<what is an assertion?>` expects :green:`True`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assertTrue(src.truth_table.logical_true())
    assertTrue(None)

* I change :ref:`None<what is None?>` to :ref:`True <test_what_is_true>` in the :ref:`return statement<the return statement>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def logical_true():
        # return None
        return True

  the test passes.

* I remove the commented line

  .. code-block:: python
    :linenos:

    def logical_true():
        return True

* I open a new terminal_, then add ``tests/test_nullary_unary.py`` to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add logical_true'

:ref:`logical_true always returns True because it is True<test_logical_true>`.

----

=================================================================================
test_logical_false
=================================================================================

----

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

----

* I go back to the terminal_ where the tests are running
* I add a test for :ref:`logical_false<test_logical_false>` to ``test_nullary_unary.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6-9

        def test_logical_true(self):
            self.assertTrue(
                src.truth_table.logical_true()
            )

        def test_logical_false(self):
            self.assertFalse(
                src.truth_table.logical_false()
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_false'.
                    Did you mean: 'logical_true'?

  because I have not added a definition for :ref:`logical_false<test_logical_false>` to ``truth_table.py``, I only added one for :ref:`logical_true<test_logical_true>`.

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

  .. code-block:: python

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`.

* I change :ref:`True <test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`return statement<the return statement>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-3

    def logical_false():
        # return True
        return False

  the test passes.

* I remove the commented line

  .. code-block:: python
    :linenos:

    def logical_true():
        return True


    def logical_false():
        return False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add logical_false'

:ref:`logical_false always returns False because it is False<test_logical_false>`.


The two Nullary Operations do not take input

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

There are 2 unary operations: :ref:`Logical Identity<test_logical_identity>` and :ref:`Logical Negation<test_logical_negation>`, they each take one input and return :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`.

----

=================================================================================
test_logical_identity
=================================================================================

----

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

----

* I go back to the terminal_ where the tests are running
* I add a new :ref:`TestCase<test_dir_unittest_testcase>` for Unary Operations with a test for :ref:`logical_identity<test_logical_identity>` when it gets :ref:`True<test_what_is_true>` as input, in ``test_nullary_unary.py``

  ==============  =============
  input           output
  ==============  =============
  :green:`True`   :green:`True`
  ==============  =============

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 7, 9-12

        def test_logical_false(self):
            self.assertFalse(
                src.truth_table.logical_false()
            )


    class TestUnaryOperations(unittest.TestCase):

        def test_logical_identity(self):
            self.assertTrue(
                src.truth_table.logical_identity(True)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_identity'

  because I need to add a :ref:`definition<how to make a function>` for :ref:`logical_identity<test_logical_identity>` to ``truth_table.py``

----

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

----

* I add a :ref:`function<what is a function?>` named ``logical_identity`` to ``truth_table.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def logical_false():
        return False


    def logical_identity():
        return False

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: logical_identity() takes
               0 positional arguments but 1 was given

  because the test called the :ref:`logical_identity function<test_logical_identity>` with one argument and the definition does not allow any arguments (the parentheses are empty).

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen, in ``test_nullary_unary.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 4
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # AttributeError
    # TypeError

* I add a name in parentheses so that :ref:`logical_identity<test_logical_identity>` can take calls with one input, in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1-2

    # def logical_identity():
    def logical_identity(the_input):
        return False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the :ref:`function<what is a function?>` returns :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`.

* I change the :ref:`return statement<the return statement>` to give the test what it wants

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3-4

    # def logical_identity():
    def logical_identity(the_input):
        # return False
        return True

  the test passes.

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
    :lineno-start: 20
    :emphasize-lines: 5-7

        def test_logical_identity(self):
            self.assertTrue(
                src.truth_table.logical_identity(True)
            )
            self.assertFalse(
                src.truth_table.logical_identity(False)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`.

* I change the :ref:`return statement<the return statement>` of :ref:`logical_identity<test_logical_identity>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3-4

    # def logical_identity():
    def logical_identity(the_input):
        return False
        # return True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the :ref:`assertion<what is an assertion?>` that was passing before, expects :green:`True` and the :ref:`function<what is a function?>` now returns :red:`False`.

* I change the :ref:`return statement<the return statement>` of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3, 5

    # def logical_identity():
    def logical_identity(the_input):
        # return False
        # return True
        return the_input

  the test passes because the :ref:`logical_identity function<test_logical_identity>` returns its input as output

  .. code-block:: python

    logical_identity(the_input) -> the_input

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 5

    def logical_false():
        return False


    def logical_identity(the_input):
        return the_input

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add logical_identity'

This is what happens when the :ref:`logical_identity function<test_logical_identity>` is called

- it returns :green:`True`, if the input is :ref:`True<test_what_is_true>`
- it returns :red:`False`, if the input is :ref:`False<test_what_is_false>`
- it returns the input as output

.. tip::

  ``the_input`` is a name, I can use any name.

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
  :lineno-start: 20
  :emphasize-lines: 9-12

      def test_logical_identity(self):
          self.assertTrue(
              src.truth_table.logical_identity(True)
          )
          self.assertFalse(
              src.truth_table.logical_identity(False)
          )

      def test_logical_negation(self):
          self.assertFalse(
              src.truth_table.logical_negation(True)
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.truth_table'
                  has no attribute 'logical_negation'

there is no definition for :ref:`logical_negation<test_logical_negation>` in ``truth_table.py``

----

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

----

* I add ``logical_negation`` to ``truth_table.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def logical_identity(the_input):
        return the_input


    def logical_negation(the_input):
        return the_input

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returned :ref:`True<test_what_is_true>` and the :ref:`assertion<what is an assertion?>` expects :red:`False`.

* I change the :ref:`return statement<the return statement>` to give the test what it wants

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2-3

    def logical_negation(the_input):
        # return the_input
        return False

  the test passes.

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
    :lineno-start: 28
    :emphasize-lines: 5-7

        def test_logical_negation(self):
            self.assertFalse(
                src.truth_table.logical_negation(True)
            )
            self.assertTrue(
                src.truth_table.logical_negation(False)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the :ref:`function<what is a function?>` returns :red:`False` and the new :ref:`assertion<what is an assertion?>` expects :green:`True`.

* I change the :ref:`return statement<the return statement>` of the :ref:`logical_negation function<test_logical_negation>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3-4

    def logical_negation(the_input):
        # return the_input
        # return False
        return True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the test fails for the :ref:`assertion<what is an assertion?>` that passed before, because the :ref:`function<what is a function?>` now returns :green:`True` and that :ref:`assertion<what is an assertion?>` expects :red:`False`.

* I make the :ref:`function<what is a function?>` return its input again

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2, 4

    def logical_negation(the_input):
        return the_input
        # return False
        # return True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  this means the expectation of the test is that the :ref:`logical_negation function<test_logical_negation>`

  - returns :green:`True` if the input is :red:`False`
  - returns :red:`False` if the input is :green:`True`
  - returns the opposite of the input it gets

----

=================================================================================
how to return the opposite of a boolean
=================================================================================

----

I can use the not_ keyword to return the opposite of the :ref:`boolean<what are booleans?>` after it.

* I add not_ to the :ref:`return statement<the return statement>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2, 5

    def logical_negation(the_input):
        # return the_input
        # return False
        # return True
        return not the_input

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 13

    def logical_negation(the_input):
        return not the_input

* I add to the name of the test as a note, in ``test_nullary_unary.py``

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 11
    :emphasize-text: _aka_not

    class TestUnaryOperations(unittest.TestCase):

        def test_logical_identity(self):
            self.assertTrue(
                src.truth_table.logical_identity(True)
            )
            self.assertFalse(
                src.truth_table.logical_identity(False)
            )

        def test_logical_negation_aka_not(self):
            self.assertFalse(
                src.truth_table.logical_negation(True)
            )
            self.assertTrue(
                src.truth_table.logical_negation(False)
            )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add logical_negation'

:ref:`logical_negation also known as not returns the opposite of its input<test_logical_negation>`

==============  =============
input           output
==============  =============
:green:`True`   :red:`False`
:red:`False`    :green:`True`
==============  =============

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_nullary_unary.py`` and ``truth_table.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``truth_table``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

I ran these tests for :ref:`Nullary Operations<Nullary Operations>` which take no input

* :ref:`test_logical_true`
* :ref:`test_logical_false`

and for :ref:`Unary operations<Unary Operations>` which take one input

* :ref:`test_logical_identity`
* :ref:`test_logical_negation`

the :ref:`truth table` for :ref:`Unary Operations<Unary Operations>` is

==============  ============= ============= ====================================================
return          :green:`True` :red:`False`  operation
==============  ============= ============= ====================================================
the_input       :green:`True` :red:`False`  :ref:`logical_identity<test_logical_identity>`
not the_input   :red:`False`  :green:`True` :ref:`logical_negation (NOT)<test_logical_negation>`
==============  ============= ============= ====================================================

:ref:`How many questions can you answer after going through this chapter?<questions about Nullary and Unary Operations>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed for Nullary and Unary Operations?<Nullary and Unary Operations tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like to test binary operations? They take only two inputs.<truth table: Binary Operations>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->