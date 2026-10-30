.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

#################################################################################
test booleans with loops
#################################################################################

I want to use :ref:`for loops<what is a for loop?>` in the :ref:`booleans<what are booleans?>` project.

----

*********************************************************************************
preview
*********************************************************************************

This is the test I have at the end of the chapter

.. literalinclude:: ../../code/booleans/test_what_are_booleans_w_loops.py
  :caption: booleans/tests/test_what_are_booleans.py
  :language: python
  :linenos:
  :lines: 1-19

.. literalinclude:: ../../code/booleans/test_what_are_booleans_w_loops.py
  :caption: booleans/tests/test_what_are_booleans.py
  :language: python
  :lineno-start: 21
  :lines: 21-32

.. literalinclude:: ../../code/booleans/test_what_are_booleans_w_loops.py
  :caption: booleans/tests/test_what_are_booleans.py
  :language: python
  :lineno-start: 34
  :lines: 34-41

.. literalinclude:: ../../code/booleans/test_what_are_booleans_w_loops.py
  :caption: booleans/tests/test_what_are_booleans.py
  :language: python
  :lineno-start: 43
  :lines: 43-54

.. literalinclude:: ../../code/booleans/test_what_are_booleans_w_loops.py
  :caption: booleans/tests/test_what_are_booleans.py
  :language: python
  :lineno-start: 56
  :lines: 56-63

.. literalinclude:: ../../code/booleans/test_what_are_booleans_w_loops.py
  :caption: booleans/tests/test_what_are_booleans.py
  :language: python
  :lineno-start: 65
  :lines: 65-75

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the ``booleans`` folder_

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd booleans

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now

----

*********************************************************************************
extract test_what_are_booleans
*********************************************************************************

:ref:`test_what_is_false` and :ref:`test_what_is_true` both check if a :ref:`boolean<what is a boolean?>` is an :ref:`instance<how to test if something is an instance>` of bool_ and int_ and is NOT an :ref:`instance<how to test if something is an instance>` of any of the other :ref:`basic objects`.

.. code-block:: python

    self.assertIsInstance(boolean, (bool, int))
    self.assertNotIsInstance(
        boolean,
        (
            float, tuple, str,
            list, set, dict,
        )
    )
    self.assertIs(boolean, boolean)
    self.assertIs(bool(boolean), boolean)

I can use a :ref:`function<what is a function?>` with a :ref:`for loop<what is a for loop?>` to remove the repetition

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with a :ref:`for loop<what is a for loop?>` for what is a :ref:`boolean<what are booleans?>`

.. code-block:: python
  :caption: booleans/tests/test_booleans.py
  :lineno-start: 4
  :emphasize-lines: 3-15

  class TestBooleans(unittest.TestCase):

      def test_what_are_booleans(self):
          for boolean in (None, float):
              with self.subTest(boolean):
                  self.assertIsInstance(boolean, (bool, int))
                  self.assertNotIsInstance(
                      boolean,
                      (
                          float, tuple, str,
                          list, set, dict,
                      )
                  )
                  self.assertIs(boolean, boolean)
                  self.assertIs(bool(boolean), boolean)

      def test_what_is_false(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  SUBFAILED[None] ...AssertionError:
      None is not an instance of any of (<class 'bool'>, <class 'int'>)
  SUBFAILED[<class 'float'>] ...AssertionError:
      <class 'float'> is not an instance of any of (<class 'bool'>, <class 'int'>)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``(None, float)`` to :ref:`booleans<what are booleans?>`

.. code-block:: python
  :caption: booleans/tests/test_booleans.py
  :lineno-start: 6
  :emphasize-lines: 2

      def test_what_are_booleans(self):
          for boolean in (False, True):
              with self.subTest(boolean):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the repeated :ref:`assertions<what are assertions>` from :ref:`test_what_is_false`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 20

        def test_what_is_false(self):
            self.assertFalse(bool(False))
            self.assertFalse(False)

        def test_what_is_true(self):

* I remove the repeated :ref:`assertions<what are assertions>` from :ref:`test_what_is_true`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 24

        def test_what_is_true(self):
            self.assertTrue(bool(True))
            self.assertTrue(True)

        def assert_is_not_the_same_as_false_or_true(self, an_object):

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'extract test_what_are_booleans'

----

*********************************************************************************
add for loop to assert_is_not_the_same_as_false_or_true
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`for loop<what is a for loop?>` to the :ref:`assert_is_not_the_same_as_false_or_true method<extract assert_is_not_the_same_as_false_or_true method>`

.. code-block:: python
  :caption: booleans/tests/test_booleans.py
  :lineno-start: 28
  :emphasize-lines: 2-7

      def assert_is_not_the_same_as_false_or_true(self, an_object):
          for boolean in (False, True):
              with self.subTest(
                  an_object=an_object, boolean=boolean
              ):
                  self.assertEqual(an_object, boolean)
                  self.assertIs(an_object, boolean)

          self.assertNotEqual(an_object, False)

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for twenty eight sub tests.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`assertEqual<test_assertEqual>` to :ref:`assertNotEqual<test_assertNotEqual>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 30
    :emphasize-lines: 4

                with self.subTest(
                    an_object=an_object, boolean=boolean
                ):
                    self.assertNotEqual(an_object, boolean)
                    self.assertIs(an_object, boolean)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for twenty eight sub tests.

* I change :ref:`assertIs<test_assertIs>` to :ref:`assertIsNot<test_assertIsNot>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 33
    :emphasize-lines: 2

                    self.assertNotEqual(an_object, boolean)
                    self.assertIsNot(an_object, boolean)

            self.assertNotEqual(an_object, False)

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertions<what are assertions?>` because they are now covered by the :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 28

        def assert_is_not_the_same_as_false_or_true(self, an_object):
            for boolean in (False, True):
                with self.subTest(
                    an_object=an_object, boolean=boolean
                ):
                    self.assertNotEqual(an_object, boolean)
                    self.assertIsNot(an_object, boolean)

        def assert_is_falsy(self, an_object):

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add for loop to assert_is_not_the_same_as_false_or_true'

----

*********************************************************************************
extract test_what_is_falsy
*********************************************************************************

:ref:`test_is_none_falsy_or_truthy`, :ref:`test_is_an_integer_falsy_or_truthy`, :ref:`test_is_a_float_falsy_or_truthy`, :ref:`test_is_a_string_falsy_or_truthy`, :ref:`test_is_a_tuple_falsy_or_truthy`, :ref:`test_is_a_list_falsy_or_truthy`, :ref:`test_is_a_set_falsy_or_truthy` and :ref:`test_is_a_dictionary_falsy_or_truthy` all :ref:`call<how to call a function with input>` the :ref:`assert_is_falsy method<extract assert_is_falsy method>` to :ref:`assert<what is an assertion?>` if something is grouped as :ref:`False<test_what_is_false>`

.. code-block:: python

  self.assert_is_not_the_same_as_false_or_true(an_object)
  self.assertFalse(bool(an_object))
  self.assertFalse(an_object)

I can make a :ref:`function<what is a function?>` with a :ref:`for loop<what is a for loop?>` to remove the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`for loop<what is a for loop?>` with the code from :ref:`assert_is_truthy<extract assert_is_truthy method>` to :ref:`test_what_is_false`

.. code-block:: python
  :caption: booleans/tests/test_booleans.py
  :lineno-start: 20
  :emphasize-lines: 5-12

      def test_what_is_false(self):
          self.assertFalse(bool(False))
          self.assertFalse(False)

          for an_object in (
              None, str(), tuple(),
              list(), set(), dict()
          ):
              with self.subTest(an_object):
                  self.assert_is_not_the_same_as_false_or_true(an_object)
                  self.assertTrue(bool(an_object))
                  self.assertTrue(an_object)

      def test_what_is_true(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  SUBFAILED[None] ...AssertionError: False is not true
  SUBFAILED[] ...AssertionError: False is not true
  SUBFAILED[()] ...AssertionError: False is not true
  SUBFAILED[[]] ...AssertionError: False is not true
  SUBFAILED[set()] ...AssertionError: False is not true
  SUBFAILED[{}] ...AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``self.assertTrue(bool(an_object))``

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 28
    :emphasize-lines: 3

                with self.subTest(an_object):
                    self.assert_is_not_the_same_as_false_or_true(an_object)
                    self.assertFalse(bool(an_object))
                    self.assertTrue(an_object)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED[None] ...AssertionError: None is not true
    SUBFAILED[] ...AssertionError: '' is not true
    SUBFAILED[()] ...AssertionError: () is not true
    SUBFAILED[[]] ...AssertionError: [] is not true
    SUBFAILED[set()] ...AssertionError: set() is not true
    SUBFAILED[{}] ...AssertionError: {} is not true

* I change ``self.assertTrue(an_object)``

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 28
    :emphasize-lines: 4

                with self.subTest(an_object):
                    self.assert_is_not_the_same_as_false_or_true(an_object)
                    self.assertFalse(bool(an_object))
                    self.assertFalse(an_object)

        def test_what_is_true(self):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_what_is_false` to :ref:`test_what_is_falsy<extract test_what_is_falsy>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 17
    :emphasize-lines: 4

                    self.assertIs(boolean, boolean)
                    self.assertIs(bool(boolean), boolean)

        def test_what_is_falsy(self):
            self.assertFalse(bool(False))
            self.assertFalse(False)

            for an_object in (
                None, str(), tuple(),
                list(), set(), dict()
            ):
                with self.subTest(an_object):
                    self.assert_is_not_the_same_as_false_or_true(an_object)
                    self.assertFalse(bool(an_object))
                    self.assertFalse(an_object)

        def test_what_is_true(self):

* I remove :ref:`test_is_none_falsy_or_truthy` because it is now covered by :ref:`test_what_is_falsy<extract test_what_is_falsy>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 50

        def assert_is_truthy(self, an_object):
            self.assert_is_not_the_same_as_false_or_true(an_object)
            self.assertTrue(bool(an_object))
            self.assertTrue(an_object)

        def test_is_an_integer_falsy_or_truthy(self):

* I remove ``self.assert_is_falsy(str())`` from :ref:`test_is_a_string_falsy_or_truthy` because it is now covered by :ref:`test_what_is_falsy<extract test_what_is_falsy>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 85

        def test_is_a_string_falsy_or_truthy(self):
            self.assert_is_truthy('a string with things')

        def test_is_a_tuple_falsy_or_truthy(self):

* I remove ``self.assert_is_falsy(tuple())`` from :ref:`test_is_a_tuple_falsy_or_truthy` because it is now covered by :ref:`test_what_is_falsy<extract test_what_is_falsy>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 88

        def test_is_a_tuple_falsy_or_truthy(self):
            self.assert_is_truthy((0, 1, 2, 'n'))

        def test_is_a_list_falsy_or_truthy(self):

* I remove ``self.assert_is_falsy(list())`` from :ref:`test_is_a_list_falsy_or_truthy` because it is now covered by :ref:`test_what_is_falsy<extract test_what_is_falsy>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 91

        def test_is_a_list_falsy_or_truthy(self):
            self.assert_is_truthy([0, 1, 2, 'n'])

        def test_is_a_set_falsy_or_truthy(self):

* I remove ``self.assert_is_falsy(set())`` from :ref:`test_is_a_set_falsy_or_truthy` because it is now covered by :ref:`test_what_is_falsy<extract test_what_is_falsy>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 94

        def test_is_a_set_falsy_or_truthy(self):
            self.assert_is_truthy({0, 1, 2, 'n'})

        def test_is_a_dictionary_falsy_or_truthy(self):

* I remove ``self.assert_is_falsy(dict())`` from :ref:`test_is_a_dictionary_falsy_or_truthy` because it is now covered by :ref:`test_what_is_falsy<extract test_what_is_falsy>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 97

        def test_is_a_dictionary_falsy_or_truthy(self):
            self.assert_is_truthy({'key': 'value'})


    # NOTES

* I add a git_ commit message

----

*********************************************************************************
test_the_value_of_true
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to find out the value of :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 39
  :emphasize-lines: 8-9

      def test_the_value_of_false(self):
          self.assertEqual(False+1, 1)
          self.assertEqual(False-1, -1)
          self.assertEqual(False*1, 0)
          with self.assertRaises(ZeroDivisionError):
              1 / False

      def test_the_value_of_true(self):
          self.assertEqual(True+1, 1)


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 2 != 1

:ref:`True<test_what_is_true>` is ``1``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation

.. code-block:: python
  :lineno-start: 47
  :emphasize-lines: 1

          self.assertEqual(True+1, 2)

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3

        def test_the_value_of_true(self):
            self.assertEqual(True+1, 2)
            self.assertEqual(True-1, 2)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 != 2

  :ref:`True<test_what_is_true>` is ``1``

* I change the expectation

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 1

            self.assertEqual(True-1, 0)

  the test passes.

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4

        def test_the_value_of_true(self):
            self.assertEqual(True+1, 2)
            self.assertEqual(True-1, 0)
            self.assertEqual(True*1, 0)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1 != 0

  :ref:`True<test_what_is_true>` is ``1``

* I change the expectation

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 1

            self.assertEqual(True*1, 1)

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 5

        def test_the_value_of_true(self):
            self.assertEqual(True+1, 2)
            self.assertEqual(True-1, 0)
            self.assertEqual(True*1, 1)
            self.assertEqual(True/2, 1)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.5 != 1

  :ref:`True<test_what_is_true>` is ``1``

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 5

        def test_the_value_of_true(self):
            self.assertEqual(True+1, 2)
            self.assertEqual(True-1, 0)
            self.assertEqual(True*1, 1)
            self.assertEqual(True/1, 1)


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 13

    # NOTES
    # a dictionary with things is True
    # a set with things is True
    # a list with things is True
    # a tuple with things is True
    # a string with things is True
    # positive and negative numbers are True
    # True is True
    # True is not false
    # True is a boolean
    # True is an integer
    # True is not a float
    # True is 1
    # the empty dictionary is False
    # the empty set is False
    # the empty list is False
    # the empty tuple is False
    # the empty string is False
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean
    # False is an integer
    # False is not a float
    # False is 0


    # Exceptions seen
    # AssertionError

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_what_are_booleans.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``booleans``

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

I added :ref:`assertions<what is an assertion?>` that show :ref:`booleans<what are booleans?>` are also integers_ and NOT floats_, then I added these tests

* :ref:`test_the_value_of_false` which showed that :ref:`False<test_what_is_false>` is ``0``
* :ref:`test_the_value_of_true` which showed that :ref:`True<test_what_is_true>` is ``1``

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<data structures: list comprehensions: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python Test Driven Development environment manually<how to make a Python Test Driven Development environment manually>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`I know how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions in programs>`
* :ref:`how to raise TypeError<what causes TypeError?>`
* :ref:`what you can do with Lists<what is a list?>`
* :ref:`how to use list comprehensions<list comprehensions>`

:ref:`Would you like to test dictionaries?<dictionaries>`

-----

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