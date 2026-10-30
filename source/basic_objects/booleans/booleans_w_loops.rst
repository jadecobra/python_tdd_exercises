.. meta::
  :description: Beginner Python TDD tutorial — test booleans with loops. Continues the booleans project (pytest-watcher, git) and uses for loops plus subTest to remove repeated unittest checks. Extracts test_what_are_booleans over (False, True) with assertIsInstance of (bool, int), assertNotIsInstance of float/tuple/str/list/set/dict, and assertIs identity. Loops assert_is_not_the_same_as_false_or_true over False and True (assertNotEqual and assertIsNot; 28 subtests). Extracts test_what_is_falsy for None, '', (), [], set(), and {} (assertFalse on bool(x) and on x) and test_what_is_truthy for -1, -0.1, 0.1, a non-empty string, tuple, list, set, and dict. Then test_the_value_of_false loops 0 and 0.0: equal to False, not the False object, not equal to True, not the True object, and falsy. Real AssertionError strings: "None is not an instance of any of (<class 'bool'>, <class 'int'>)", "False is not true", "None is not true", "True is not false", "-1 is not false", "0 != True", "0 == False", "0 is not true". Part of Jacob Itegboje's Pumping Python series.
  :keywords: Jacob Itegboje, Pumping Python, test booleans with loops, python for loop, unittest subTest, SUBFAILED, test_what_are_booleans, test_what_is_falsy, test_what_is_truthy, test_the_value_of_false, test_the_value_of_true, assertIsInstance, assertNotIsInstance, assertIs, assertIsNot, assertNotEqual, assertFalse, assertTrue, False is 0, True is 1, 0 is not False, 0.0 == False, None is not true, False is not true, True is not false, falsy empty containers, truthy non-empty containers, uv run pytest-watcher, red green refactor, booleans/tests/test_booleans.py, Python basic objects TDD

.. include:: ../../links.rst

#################################################################################
test booleans with loops
#################################################################################

I want to use :ref:`for loops<what is a for loop?>` in the :ref:`booleans<what are booleans?>` project.

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/booleans/test_booleans_w_loops.py
  :caption: booleans/tests/test_booleans.py
  :language: python
  :linenos:
  :lines: 1-18

.. literalinclude:: ../../code/booleans/test_booleans_w_loops.py
  :caption: booleans/tests/test_booleans.py
  :language: python
  :lineno-start: 20
  :lines: 20-31

.. literalinclude:: ../../code/booleans/test_booleans_w_loops.py
  :caption: booleans/tests/test_booleans.py
  :language: python
  :lineno-start: 33
  :lines: 33-48

.. literalinclude:: ../../code/booleans/test_booleans_w_loops.py
  :caption: booleans/tests/test_booleans.py
  :language: python
  :lineno-start: 50
  :lines: 50-56

.. literalinclude:: ../../code/booleans/test_booleans_w_loops.py
  :caption: booleans/tests/test_booleans.py
  :language: python
  :lineno-start: 58
  :lines: 58-66

.. literalinclude:: ../../code/booleans/test_booleans_w_loops.py
  :caption: booleans/tests/test_booleans.py
  :language: python
  :lineno-start: 68
  :lines: 68-78

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
  :caption: terminal

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

I add a :ref:`for loop<what is a for loop?>` with the :ref:`assertions<what is an assertion?>` from :ref:`assert_is_truthy<extract assert_is_truthy method>` to :ref:`test_what_is_false`

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
    :caption: terminal

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
            self.assert_is_truthy('string with things')

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

* I remove the :ref:`assert_is_falsy method<extract assert_is_falsy method>` because it is no longer used

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 37

        def assert_is_not_the_same_as_false_or_true(self, an_object):
            for boolean in (False, True):
                with self.subTest(
                    an_object=an_object, boolean=boolean
                ):
                    self.assertNotEqual(an_object, boolean)
                    self.assertIsNot(an_object, boolean)

        def assert_is_truthy(self, an_object):

  the tests are still green.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'extract test_what_is_falsy'

----

*********************************************************************************
extract test_what_is_truthy
*********************************************************************************

:ref:`test_is_an_integer_falsy_or_truthy`, :ref:`test_is_a_float_falsy_or_truthy`, :ref:`test_is_a_string_falsy_or_truthy`, :ref:`test_is_a_tuple_falsy_or_truthy`, :ref:`test_is_a_list_falsy_or_truthy`, :ref:`test_is_a_set_falsy_or_truthy` and :ref:`test_is_a_dictionary_falsy_or_truthy` all :ref:`call<how to call a function with input>` the :ref:`assert_is_truthy method<extract assert_is_truthy method>` to :ref:`assert<what is an assertion?>` if something is grouped as :ref:`True<test_what_is_true>`

.. code-block:: python

  self.assert_is_not_the_same_as_false_or_true(an_object)
  self.assertTrue(bool(an_object))
  self.assertTrue(an_object)

I can make a :ref:`function<what is a function?>` with a :ref:`for loop<what is a for loop?>` to remove the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`for loop<what is a for loop?>` with the :ref:`assertions<what is an assertion?>` from :ref:`test_what_is_falsy<extract test_what_is_falsy>` to :ref:`test_what_is_true`

.. code-block:: python
  :caption: booleans/tests/test_booleans.py
  :lineno-start: 33
  :emphasize-lines: 5-16

      def test_what_is_true(self):
          self.assertTrue(bool(True))
          self.assertTrue(True)

          for an_object in (
              -1, -0.1, 0.1,
              'string with things',
              (0, 1, 2, 'n'),
              [0, 1, 2, 'n'],
              {0, 1, 2, 'n'},
              {'key': 'value'},
          ):
              with self.subTest(an_object):
                  self.assert_is_not_the_same_as_false_or_true(an_object)
                  self.assertFalse(bool(an_object))
                  self.assertFalse(an_object)

      def assert_is_not_the_same_as_false_or_true(self, an_object):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

    SUBFAILED[-1] ... AssertionError: True is not false
    SUBFAILED[-0.1] ... AssertionError: True is not false
    SUBFAILED[0.1] ... AssertionError: True is not false
    SUBFAILED[string with things] ... AssertionError: True is not false
    SUBFAILED[(0, 1, 2, 'n')] ... AssertionError: True is not false
    SUBFAILED[[0, 1, 2, 'n']] ... AssertionError: True is not false
    SUBFAILED[{0, 1, 2, 'n'}] ... AssertionError: True is not false
    SUBFAILED[{'key': 'value'}] ... AssertionError: True is not false

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``self.assertFalse(bool(an_object))``

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 45
    :emphasize-lines: 3

                with self.subTest(an_object):
                    self.assert_is_not_the_same_as_false_or_true(an_object)
                    self.assertTrue(bool(an_object))
                    self.assertFalse(an_object)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    SUBFAILED[-1] ... AssertionError: -1 is not false
    SUBFAILED[-0.1] ... AssertionError: -0.1 is not false
    SUBFAILED[0.1] ... AssertionError: 0.1 is not false
    SUBFAILED[string with things] ... AssertionError: 'string with things' is not false
    SUBFAILED[(0, 1, 2, 'n')] ... AssertionError: (0, 1, 2, 'n') is not false
    SUBFAILED[[0, 1, 2, 'n']] ... AssertionError: [0, 1, 2, 'n'] is not false
    SUBFAILED[{0, 1, 2, 'n'}] ... AssertionError: {0, 1, 2, 'n'} is not false
    SUBFAILED[{'key': 'value'}] ... AssertionError: {'key': 'value'} is not false

* I change ``self.assertFalse(an_object)``

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 45
    :emphasize-lines: 4

                with self.subTest(an_object):
                    self.assert_is_not_the_same_as_false_or_true(an_object)
                    self.assertTrue(bool(an_object))
                    self.assertTrue(an_object)

        def assert_is_not_the_same_as_false_or_true(self, an_object):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_what_is_true` to :ref:`test_what_is_truthy<extract test_what_is_truthy>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 28
    :emphasize-lines: 6

                with self.subTest(an_object):
                    self.assert_is_not_the_same_as_false_or_true(an_object)
                    self.assertFalse(bool(an_object))
                    self.assertFalse(an_object)

        def test_what_is_truthy(self):
            self.assertTrue(bool(True))
            self.assertTrue(True)

            for an_object in (
                -1, -0.1, 0.1,
                'string with things',
                (0, 1, 2, 'n'),
                [0, 1, 2, 'n'],
                {0, 1, 2, 'n'},
                {'key': 'value'},
            ):
                with self.subTest(an_object):
                    self.assert_is_not_the_same_as_false_or_true(an_object)
                    self.assertTrue(bool(an_object))
                    self.assertTrue(an_object)

        def assert_is_not_the_same_as_false_or_true(self, an_object):

* I remove ``self.assert_is_truthy(-1)`` from :ref:`test_is_an_integer_falsy_or_truthy` because it is now covered by :ref:`test_what_is_truthy<extract test_what_is_truthy>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 63

        def test_is_an_integer_falsy_or_truthy(self):
            self.assertEqual(0, False)

* I remove ``self.assert_is_truthy(-0.1)`` and ``self.assert_is_truthy(0.1)`` from :ref:`test_is_a_float_falsy_or_truthy` because they are now covered by :ref:`test_what_is_truthy<extract test_what_is_truthy>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 79

        def test_is_a_float_falsy_or_truthy(self):
            self.assertEqual(0.0, False)
            self.assertIsNot(0.0, False)
            self.assertNotEqual(0.0, True)
            self.assertIsNot(0.0, True)
            self.assertFalse(bool(0.0))
            self.assertFalse(0.0)

        def test_is_a_string_falsy_or_truthy(self):

* I remove :ref:`test_is_a_string_falsy_or_truthy` because it is now covered by :ref:`test_what_is_truthy<extract test_what_is_truthy>`
* I remove :ref:`test_is_a_tuple_falsy_or_truthy` because it is now covered by :ref:`test_what_is_truthy<extract test_what_is_truthy>`
* I remove :ref:`test_is_a_list_falsy_or_truthy` because it is now covered by :ref:`test_what_is_truthy<extract test_what_is_truthy>`
* I remove :ref:`test_is_a_set_falsy_or_truthy` because it is now covered by :ref:`test_what_is_truthy<extract test_what_is_truthy>`
* I remove :ref:`test_is_a_dictionary_falsy_or_truthy` because it is now covered by :ref:`test_what_is_truthy<extract test_what_is_truthy>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 74

        def test_is_a_float_falsy_or_truthy(self):
            self.assertEqual(0.0, False)
            self.assertIsNot(0.0, False)
            self.assertNotEqual(0.0, True)
            self.assertIsNot(0.0, True)
            self.assertFalse(bool(0.0))
            self.assertFalse(0.0)


    # NOTES

* I remove the :ref:`assert_is_truthy method<extract assert_is_truthy method>` because it is no longer used

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 50

        def assert_is_not_the_same_as_false_or_true(self, an_object):
            for boolean in (False, True):
                with self.subTest(
                    an_object=an_object, boolean=boolean
                ):
                    self.assertNotEqual(an_object, boolean)
                    self.assertIsNot(an_object, boolean)

        def test_is_an_integer_falsy_or_truthy(self):

  the tests are still green.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'extract test_what_is_truthy'

----

*********************************************************************************
the values of False and True
*********************************************************************************

:ref:`test_is_an_integer_falsy_or_truthy` and :ref:`test_is_a_float_falsy_or_truthy` both have :ref:`assertions<what is an assertion?>` that show that the value of :ref:`False<test_what_is_false>` is zero.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with a :ref:`for loop<what is a for loop?>` for the value of :ref:`False<test_what_is_false>`

.. code-block:: python
  :caption: booleans/tests/test_booleans.py
  :lineno-start: 55
  :emphasize-lines: 4-12

                    self.assertNotEqual(an_object, boolean)
                    self.assertIsNot(an_object, boolean)

        def test_the_value_of_false(self):
            for zero in (0, 0.0):
                with self.subTest(zero):
                    self.assertEqual(zero, True)
                    self.assertIsNot(zero, True)
                    self.assertNotEqual(zero, False)
                    self.assertIsNot(zero, False)
                    self.assertTrue(bool(zero))
                    self.assertTrue(zero)

        def test_is_an_integer_falsy_or_truthy(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

    SUBFAILED[0] ... AssertionError: 0 != True
    SUBFAILED[0.0] ... AssertionError: 0.0 != True

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``self.assertEqual(zero, True)``

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 58
    :emphasize-lines: 4

        def test_the_value_of_false(self):
            for zero in (0, 0.0):
                with self.subTest(zero):
                    self.assertEqual(zero, False)
                    self.assertIsNot(zero, True)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    SUBFAILED[0] ... AssertionError: 0 == False
    SUBFAILED[0.0] ... AssertionError: 0.0 == False

* I change ``self.assertNotEqual(zero, False)``

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 58
    :emphasize-lines: 6

        def test_the_value_of_false(self):
            for zero in (0, 0.0):
                with self.subTest(zero):
                    self.assertEqual(zero, False)
                    self.assertIsNot(zero, True)
                    self.assertNotEqual(zero, True)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    SUBFAILED[0] ... AssertionError: False is not true
    SUBFAILED[0.0] ... AssertionError: False is not true

* I change ``self.assertTrue(bool(zero))``

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 58
    :emphasize-lines: 8

        def test_the_value_of_false(self):
            for zero in (0, 0.0):
                with self.subTest(zero):
                    self.assertEqual(zero, False)
                    self.assertIsNot(zero, True)
                    self.assertNotEqual(zero, True)
                    self.assertIsNot(zero, False)
                    self.assertFalse(bool(zero))
                    self.assertTrue(zero)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    SUBFAILED[0] ... AssertionError: 0 is not true
    SUBFAILED[0.0] ... AssertionError: 0.0 is not true

* I change ``self.assertTrue(zero)``

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 58
    :emphasize-lines: 9

        def test_the_value_of_false(self):
            for zero in (0, 0.0):
                with self.subTest(zero):
                    self.assertEqual(zero, False)
                    self.assertIsNot(zero, True)
                    self.assertNotEqual(zero, True)
                    self.assertIsNot(zero, False)
                    self.assertFalse(bool(zero))
                    self.assertFalse(zero)

        def test_is_an_integer_falsy_or_truthy(self):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the :ref:`assertions<what is an assertion?>` for ``0`` from :ref:`test_is_an_integer_falsy_or_truthy`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 68

        def test_is_an_integer_falsy_or_truthy(self):
            a_positive_integer = 1
            self.assertNotEqual(a_positive_integer, False)
            self.assertIsNot(a_positive_integer, False)
            self.assertEqual(1, True)
            self.assertIsNot(a_positive_integer, True)
            self.assertTrue(bool(a_positive_integer))
            self.assertTrue(a_positive_integer)

        def test_is_a_float_falsy_or_truthy(self):

* I remove :ref:`test_is_a_float_falsy_or_truthy` because it is now covered by :ref:`test_the_value_of_false<the values of False and True>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 73

            self.assertIsNot(a_positive_integer, True)
            self.assertTrue(bool(a_positive_integer))
            self.assertTrue(a_positive_integer)


    # NOTES

* I change the name of :ref:`test_is_an_integer_falsy_or_truthy` to :ref:`test_the_value_of_true<the values of False and True>`

  .. code-block:: python
    :caption: booleans/tests/test_booleans.py
    :lineno-start: 64
    :emphasize-lines: 5

                    self.assertIsNot(zero, False)
                    self.assertFalse(bool(zero))
                    self.assertFalse(zero)

        def test_the_value_of_true(self):
            a_positive_integer = 1
            self.assertNotEqual(a_positive_integer, False)
            self.assertIsNot(a_positive_integer, False)

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'test the values of False and True'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_booleans.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.
* I `change directory`_ to the parent of ``booleans``

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

----

*********************************************************************************
review
*********************************************************************************

I can use :ref:`for loops<what is a for loop?>` to remove repetition.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test booleans with loops: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python Test Driven Development environment manually<how to make a Python Test Driven Development environment manually>`.
* :ref:`I know what a Python module is<what is a module?>`.
* :ref:`I know how to run tests automatically<how to run tests automatically>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`I know how to make a person with strings<how to make a person with strings>`.
* :ref:`I know how to make functions that take input<functions that take input>`.
* :ref:`I know what causes TypeError<what causes TypeError?>`.
* :ref:`I know how to place values in strings<telephone>`.
* :ref:`I know how to make a person say hello with f-strings<how to make a person with f-strings>`.
* :ref:`I know how to separate tests from solutions<separate and equal>`.
* :ref:`I know what causes AttributeError<what causes AttributeError?>`.
* :ref:`I know how to make a person with an object<how to make a person with an object>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`.
* :ref:`I know how to write programs that make decisions<truth table>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically with variables<how to make a Python Test Driven Development environment automatically with variables>`.
* :ref:`I know how to make a person with Exceptions<how to make a person with Exceptions>`.
* :ref:`I know how to test that an Exception is raised<how to test that an Exception is raised>`.
* :ref:`I know how to use Exception handlers in programs<how to handle Exceptions in programs>`.
* :ref:`I know how to make a person with loops<how to make a person with loops>`.

:ref:`Would you like to test the car project with loops?<test car with loops>`

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