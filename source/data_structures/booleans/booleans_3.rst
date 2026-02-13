.. meta::
  :description: Master Python list comprehensions with this hands-on TDD tutorial. Learn to create lists efficiently with code examples. Start coding now!
  :keywords: Jacob Itegboje, Python list comprehensions, test-driven development, Python programming, coding tutorials, data structures, Python for beginners

.. include:: ../../links.rst

#################################################################################
booleans 3
#################################################################################

I added a new :ref:`if statement<if statements>` to the ``only_takes_numbers`` :ref:`function<what is a function?>` in the :ref:`calculator program<how to make a calculator>` because when I tested it with different :ref:`data types<data structures>`, :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>` passed the condition, and made the test fail.

This means that they are also integers_ or floats_ even though they are :ref:`booleans<what are booleans?>`. I want to find out if :ref:`booleans<what are booleans?>` are integers_ or floats_

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``booleans`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd booleans

  the terminal_ shows I am in the ``booleans`` folder_

  .. code-block:: shell

    .../pumping_python/booleans

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 5

    rootdir: .../pumping_python/booleans
    configfile: pyproject.toml
    collected 2 items

    tests/test_booleans.py ..                                        [100%]

    ======================== 2 passed in X.YZs =========================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_booleans.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
is False an integer or a float?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false`

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 3

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)
          self.assertNotIsInstance(False, int)
          self.assertFalse(False)

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: False is an instance of <class 'int'>

in Python_, False_ is a :ref:`boolean<what are booleans?>` and an integer_

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertNotIsInstance_ to assertIsInstance_

.. code-block:: python
  :lineno-start: 8
  :emphasize-lines: 1

          self.assertIsInstance(False, int)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 4

    # False is False
    # False is not true
    # False is a boolean
    # False is an integer


    # Exceptions Encountered
    # AssertionError

* I add another :ref:`assertion<what is an assertion?>` to see if :ref:`False<test_what_is_false>` is a float_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertIsInstance(False, int)
            self.assertIsInstance(False, float)
            self.assertFalse(False)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not an instance of <class 'float'>

  :ref:`False<test_what_is_false>` is not a float_

* I change assertIsInstance_ to assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2

            self.assertIsInstance(False, int)
            self.assertNotIsInstance(False, float)
            self.assertFalse(False)

  the test passes

* I add a comment

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 3

    # False is a boolean
    # False is an integer
    # False is not a float


    # Exceptions Encountered
    # AssertionError

* I can use an :ref:`iterable<what is an iterable?>` with the `assertIsInstance method`_, the same way I do with the `isinstance function`_ in the ``only_takes_numbers`` :ref:`function<what is a function?>` in the :ref:`calculator<how to make a calculator>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertIsInstance(False, int)
            self.assertNotIsInstance(False, (bool, int))
            self.assertNotIsInstance(False, float)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is an instance of (<class 'bool'>, <class 'int'>)

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

            self.assertIsInstance(False, (bool, int))

  the test passes

* I remove the first two :ref:`assertions<what is an assertion?>` in the test since they are covered by the new one

  .. code-block:: python
    :lineno-start: 6

        def test_what_is_false(self):
            self.assertIsInstance(False, (bool, int))
            self.assertNotIsInstance(False, float)
            self.assertFalse(False)

* I use a `for loop`_ for the :ref:`assertions<what is an assertion?>` that :ref:`test_what_is_false`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4-32

        def test_what_is_false(self):
            self.assertIsInstance(False, (bool, int))
            self.assertNotIsInstance(False, float)
            # self.assertFalse(False)
            # self.assertFalse(None)
            # self.assertFalse(bool(None))
            # self.assertFalse(0)
            # self.assertFalse(bool(0))
            # self.assertFalse(0.0)
            # self.assertFalse(bool(0.0))
            # self.assertFalse(str())
            # self.assertFalse(bool(str()))
            # self.assertFalse(tuple())
            # self.assertFalse(bool(tuple()))
            # self.assertFalse(list())
            # self.assertFalse(bool(list()))
            # self.assertFalse(set())
            # self.assertFalse(bool(set()))
            # self.assertFalse(dict())
            # self.assertFalse(bool(dict()))
            for false_item in (
                False,
                None, bool(None),
                0, 0.0, bool(0), bool(0.0),
                str(), bool(str()),
                tuple(), bool(tuple()),
                list(), bool(list()),
                set(), bool(set()),
                dict(), bool(dict()),
            ):
                with self.subTest(item=false_item):
                    self.assertTrue(false_item)

        def test_what_is_true(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for all of them

  .. code-block:: shell

    SUBFAILED(item=False) ... - AssertionError: False is not true
    SUBFAILED(item=None) ...  - AssertionError: None is not true
    SUBFAILED(item=False) ... - AssertionError: False is not true
    SUBFAILED(item=0) ...     - AssertionError: 0 is not true
    SUBFAILED(item=0.0) ...   - AssertionError: 0.0 is not true
    SUBFAILED(item=False) ... - AssertionError: False is not true
    SUBFAILED(item=False) ... - AssertionError: False is not true
    SUBFAILED(item='') ...    - AssertionError: '' is not true
    SUBFAILED(item=False)...  - AssertionError: False is not true
    SUBFAILED(item=()) ...    - AssertionError: () is not true
    SUBFAILED(item=False) ... - AssertionError: False is not true
    SUBFAILED(item=[]) ...    - AssertionError: [] is not true
    SUBFAILED(item=False) ... - AssertionError: False is not true
    SUBFAILED(item=set()) ... - AssertionError: set() is not true
    SUBFAILED(item=False) ... - AssertionError: False is not true
    SUBFAILED(item={}) ...    - AssertionError: {} is not true
    SUBFAILED(item=False) ... - AssertionError: False is not true

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

                    self.assertFalse(false_item)

  the test is green again

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 6

        def test_what_is_false(self):
            self.assertIsInstance(False, (bool, int))
            self.assertNotIsInstance(False, float)
            for false_item in (
                False,
                None, bool(None),
                0, 0.0, bool(0), bool(0.0),
                str(), bool(str()),
                tuple(), bool(tuple()),
                list(), bool(list()),
                set(), bool(set()),
                dict(), bool(dict()),
            ):
                with self.subTest(item=false_item):
                    self.assertFalse(false_item)

        def test_what_is_true(self):

----

*********************************************************************************
is True an integer or a float?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true` to test if :ref:`True<test_what_is_true>` is also an integer_

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 3

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)
          self.assertNotIsInstance(True, int)
          self.assertTrue(True)

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: True is an instance of <class 'int'>

in Python_, :ref:`True<test_what_is_true>` is a :ref:`boolean<what are booleans?>` and an integer_

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertNotIsInstance_ to assertIsInstance_

.. code-block:: python
  :lineno-start: 24
  :emphasize-lines: 1

          self.assertIsInstance(True, int)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2

    # True is a boolean
    # True is an integer
    # the empty dictionary is False
    # the empty set is False

* I add another :ref:`assertion<what is an assertion?>` to test if :ref:`True<test_what_is_true>` is a float_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertIsInstance(True, int)
            self.assertIsInstance(True, float)
            self.assertTrue(True)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not an instance of <class 'float'>

  :ref:`True<test_what_is_true>` is not a float_

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 1

            self.assertNotIsInstance(True, float)

  the test passes. This is why my test with different :ref:`data types<data structures>` failed. :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>` are integers_ and the :ref:`if statement<if statements>` in the ``only_takes_numbers`` :ref:`function<what is a function?>` allows integers_ and floats_

* I add a comment

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 3

    # True is a boolean
    # True is an integer
    # True is not a float
    # the empty dictionary is False

* I can use an :ref:`iterable<what is an iterable?>` with the `assertIsInstance method`_, the same way I do with the `isinstance function`_ in the ``only_takes_numbers`` :ref:`function<what is a function?>` in the :ref:`calculator<how to make a calculator>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertIsInstance(True, int)
            self.assertNotIsInstance(True, (bool, int))
            self.assertNotIsInstance(True, float)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is an instance of (<class 'bool'>, <class 'int'>)

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 1

            self.assertIsInstance(True, (bool, int))

  the test passes

* I remove the first two :ref:`assertions<what is an assertion?>` in the test since they are covered by the new one

  .. code-block:: python
    :lineno-start: 22

        def test_what_is_true(self):
            self.assertIsInstance(True, (bool, int))
            self.assertNotIsInstance(True, float)
            self.assertTrue(True)

* I use a `for loop`_ for the :ref:`assertions<what is an assertion?>` that :ref:`test_what_is_true`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4-34

        def test_what_is_true(self):
            self.assertIsInstance(True, (bool, int))
            self.assertNotIsInstance(True, float)
            # self.assertTrue(True)
            # self.assertTrue(-1)
            # self.assertTrue(bool(-1))
            # self.assertTrue(1)
            # self.assertTrue(bool(1))
            # self.assertTrue(-0.1)
            # self.assertTrue(bool(-0.1))
            # self.assertTrue(0.1)
            # self.assertTrue(bool(0.1))
            # self.assertTrue("text")
            # self.assertTrue(bool("text"))
            # self.assertTrue((1, 2, 3, 'n'))
            # self.assertTrue(bool((1, 2, 3, 'n')))
            # self.assertTrue([1, 2, 3, 'n'])
            # self.assertTrue(bool([1, 2, 3, 'n']))
            # self.assertTrue({1, 2, 3, 'n'})
            # self.assertTrue(bool({1, 2, 3, 'n'}))
            # self.assertTrue({'key': 'value'})
            # self.assertTrue(bool({'key': 'value'}))
            for true_item in (
                True,
                -1, bool(-1), 1, bool(1),
                -0.1, bool(-0.1), 0.1, bool(0.1),
                "text", bool("text"),
                ((1, 2, 3, 'n')), bool((1, 2, 3, 'n')),
                [1, 2, 3, 'n'], bool([1, 2, 3, 'n']),
                {1, 2, 3, 'n'}, bool({1, 2, 3, 'n'}),
                {'key': 'value'}, bool({'key': 'value'}),
            ):
                with self.subTest(item=true_item):
                    self.assertFalse(true_item)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for all of them

  .. code-block:: shell

    SUBFAILED(item=True) ...             - AssertionError: True is not false
    SUBFAILED(item=-1) ...               - AssertionError: -1 is not false
    SUBFAILED(item=True) ...             - AssertionError: True is not false
    SUBFAILED(item=1) ...                - AssertionError: 1 is not false
    SUBFAILED(item=True) ...             - AssertionError: True is not false
    SUBFAILED(item=-0.1) ...             - AssertionError: -0.1 is not false
    SUBFAILED(item=True) ...             - AssertionError: True is not false
    SUBFAILED(item=0.1) ...              - AssertionError: 0.1 is not false
    SUBFAILED(item=True) ...             - AssertionError: True is not false
    SUBFAILED(item='text') ...           - AssertionError: 'text' is not false
    SUBFAILED(item=True) ...             - AssertionError: True is not false
    SUBFAILED(item=(1, 2, 3, 'n')) ...   - AssertionError: (1, 2, 3, 'n') is not false
    SUBFAILED(item=True) ...             - AssertionError: True is not false
    SUBFAILED(item=[1, 2, 3, 'n']) ...   - AssertionError: [1, 2, 3, 'n'] is not false
    SUBFAILED(item=True) ...             - AssertionError: True is not false
    SUBFAILED(item={1, 2, 3, 'n'}) ...   - AssertionError: {1, 2, 3, 'n'} is not false
    SUBFAILED(item=True) ...             - AssertionError: True is not false
    SUBFAILED(item={'key': 'value'}) ... - AssertionError: {'key': 'value'} is not false
    SUBFAILED(item=True) ...             - AssertionError: True is not false

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 1

                    self.assertTrue(true_item)

  the test is green again

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 22

        def test_what_is_true(self):
            self.assertIsInstance(True, (bool, int))
            self.assertNotIsInstance(True, float)

            for true_item in (
                True,
                -1, bool(-1), 1, bool(1),
                -0.1, bool(-0.1), 0.1, bool(0.1),
                "text", bool("text"),
                ((1, 2, 3, 'n')), bool((1, 2, 3, 'n')),
                [1, 2, 3, 'n'], bool([1, 2, 3, 'n']),
                {1, 2, 3, 'n'}, bool({1, 2, 3, 'n'}),
                {'key': 'value'}, bool({'key': 'value'}),
            ):
                with self.subTest(item=true_item):
                    self.assertTrue(true_item)


    # NOTES

----

*********************************************************************************
what are the values of True and False?
*********************************************************************************

The :ref:`add function<test_addition>` returned numbers in the calculation with :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>` because they are integers_. I want to know what their values are

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----




----

* I add a `for loop`_ for all the :ref:`assertions<what is an assertion?>` that :ref:`test what is True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4-25

        def test_what_is_true(self):
            self.assertIsInstance(True, (bool, int))
            self.assertNotIsInstance(True, float)
            # self.assertTrue(True)
            # self.assertTrue(-1)
            # self.assertTrue(1)
            # self.assertTrue(-0.1)
            # self.assertTrue(0.1)
            # self.assertTrue('text')
            # self.assertTrue((1, 2, 3, 'n'))
            # self.assertTrue([1, 2, 3, 'n'])
            # self.assertTrue({1, 2, 3, 'n'})
            # self.assertTrue({'key': 'value'})
            for true_item in (
                True,
                -1, 1,
                -0.1, 0.1,
                'text',
                (1, 2, 3, 'n'),
                [1, 2, 3, 'n'],
                {1, 2, 3, 'n'},
                {'key': 'value'},
            ):
                with self.subTest(i=true_item):
                    self.assertTrue(true_item)

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 22

        def test_what_is_true(self):
            self.assertIsInstance(True, (bool, int))
            self.assertNotIsInstance(True, float)
            for true_item in (
                True,
                -1, 1,
                -0.1, 0.1,
                'text',
                (1, 2, 3, 'n'),
                [1, 2, 3, 'n'],
                {1, 2, 3, 'n'},
                {'key': 'value'},
            ):
                with self.subTest(i=true_item):
                    self.assertTrue(true_item)

  still green

* I add :ref:`False<test_what_is_false>` to make sure the test still works as expected

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

                {'key': 'value'},
                False,
            ):
                with self.subTest(i=true_item):
                    self.assertTrue(true_item)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(i=False) tests/test_booleans.py::TestBooleans::test_what_is_true - AssertionError: False is not true

* I remove the line I just added and the test is green again

----

*********************************************************************************
test_the_value_of_false
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to find out the value of :ref:`False<test_what_is_false>`

.. code-block:: python
  :lineno-start: 33
  :emphasize-lines: 3-4

          self.assertTrue({'key': 'value'})

      def test_the_value_of_false(self):
          self.assertEqual(False+1, None)


  # NOTES

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 1 != None

:ref:`False<test_what_is_false>` is ``0``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation to match

.. code-block:: python
  :lineno-start: 36
  :emphasize-lines: 1

          self.assertEqual(False+1, 1)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 2

            self.assertEqual(False+1, 1)
            self.assertEqual(False-1, 1)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: -1 != 1

  :ref:`False<test_what_is_false>` is ``0``

* I change the expectation

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

            self.assertEqual(False-1, -1)

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

            self.assertEqual(False-1, -1)
            self.assertEqual(False*1, -1)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 != -1

  :ref:`False<test_what_is_false>` is ``0``

* I change the expectation

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 1

            self.assertEqual(False*1, 0)

  the test passes

* what happens if I divide a number by :ref:`False?<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2

            self.assertEqual(False*1, 0)
            1 / False


    # NOTES

  the terminal_ shows :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` because :ref:`False<test_what_is_false>` is ``0``

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 5-6

        def test_the_value_of_false(self):
            self.assertEqual(False+1, 1)
            self.assertEqual(False-1, -1)
            self.assertEqual(False*1, 0)
            with self.assertRaises(ZeroDivisionError):
                1 / False

  the test passes

* I add a comment

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 8

    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean
    # False is an integer
    # False is not a float
    # False is 0

time to test the value of :ref:`True<test_what_is_true>`

----

*********************************************************************************
test_the_value_of_true
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to find out the value of :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 39
  :emphasize-lines: 4-5

          with self.assertRaises(ZeroDivisionError):
              1 / False

      def test_the_value_of_true(self):
          self.assertEqual(True+1, 1)


  # NOTES

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

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
  :lineno-start: 43
  :emphasize-lines: 1

          self.assertEqual(True+1, 2)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2

            self.assertEqual(True+1, 2)
            self.assertEqual(True-1, 2)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 != 2

  :ref:`True<test_what_is_true>` is ``1``

* I change the expectation

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 1

            self.assertEqual(True-1, 0)

  the test passes

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2

            self.assertEqual(True-1, 0)
            self.assertEqual(True*1, 0)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1 != 0

  :ref:`True<test_what_is_true>` is ``1``

* I change the expectation

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 1

            self.assertEqual(True*1, 1)

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 2

            self.assertEqual(True*1, 1)
            self.assertEqual(True/2, 1)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.5 != 1

  :ref:`True<test_what_is_true>` is ``1``

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 1

            self.assertEqual(True/1, 1)

  the test passes

* I add a comment

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 3

    # True is an integer
    # True is not a float
    # True is 1
    # the empty dictionary is False

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_booleans.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and use :kbd:`q` on the keyboard to leave the tests and the terminal_ goes back to the command line

* I `change directory`_ to the parent of ``booleans``

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

I added :ref:`assertions<what is an assertion?>` that show :ref:`booleans<what are booleans?>` are also integers_ and NOT floats_ then added the following tests

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

you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<list comprehensions>`

:ref:`Would you like to test dictionaries?<dictionaries>`

-----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->