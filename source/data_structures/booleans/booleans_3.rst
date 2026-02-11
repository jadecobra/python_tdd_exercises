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
is a boolean an integer or a float?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new :ref:`assertion<what is an assertion?>` to the ``test_what_is_false`` :ref:`method<what is a function?>`

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
  :lineno-start: 7
  :emphasize-lines: 2

          self.assertIsInstance(False, bool)
          self.assertIsInstance(False, int)
          self.assertFalse(False)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 4

    # False is False
    # False is not true
    # False is a boolean
    # False is an integer


    # Exceptions Encountered
    # AssertionError

* I add another :ref:`assertion<what is an assertion?>` to see if :ref:`False<test_what_is_false>` is a float_

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3

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
    :lineno-start: 53
    :emphasize-lines: 3

    # False is a boolean
    # False is an integer
    # False is not a float


    # Exceptions Encountered
    # AssertionError

* I add an :ref:`assertion<what is an assertion?>` to the ``test_what_is_true`` :ref:`method<what is a function?>` to test if :ref:`True<test_what_is_true>` is also an integer_

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 3

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertNotIsInstance(True, int)
            self.assertTrue(True)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is an instance of <class 'int'>

  in Python_, :ref:`True<test_what_is_true>` is a :ref:`boolean<what are booleans?>` and an integer_

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

            self.assertIsInstance(True, bool)
            self.assertIsInstance(True, int)
            self.assertTrue(True)

  the test passes

* I add a comment

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2

    # True is a boolean
    # True is an integer
    # the empty dictionary is False
    # the empty set is False

* I add another :ref:`assertion<what is an assertion?>` to test if :ref:`True<test_what_is_true>` is a float_

  .. code-block:: python
    :lineno-start: 20
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
    :lineno-start: 22
    :emphasize-lines: 2

            self.assertIsInstance(True, int)
            self.assertNotIsInstance(True, float)
            self.assertTrue(True)

  the test passes

* I add a comment

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 3

    # True is a boolean
    # True is an integer
    # True is not a float
    # the empty dictionary is False

  This explains why my test with different :ref:`data types<data structures>` failed. :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>` are integers_ and the :ref:`if statement<if statements>` in the ``only_takes_numbers`` :ref:`function<what is a function?>` only allowed integers_ and floats_.


  The :ref:`add function<test_addition>` returned numbers in the calculation with :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>` because they are integers_. I want to know what their values are

* I can use an :ref:`iterable<what is an iterable?>` with the `assertIsInstance method`_, the same way I do with the `isinstance function` in the ``only_takes_numbers`` :ref:`function` in the :ref:`calculator<how to make a calculator>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 4

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertIsInstance(True, int)
            self.assertIsInstance(True, (bool, int))
            self.assertNotIsInstance(True, float)

  the test is still green

* I remove the first two :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 20

        def test_what_is_true(self):
            self.assertIsInstance(True, (bool, int))
            self.assertNotIsInstance(True, float)
            self.assertTrue(True)

  still green

* I do the same thing in the ``test_what_is_false`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertIsInstance(False, int)
            self.assertIsInstance(False, (bool, int))
            self.assertNotIsInstance(False, float)

  the tests are still passing

* I remove the first two :ref:`assertions<what is an assertion?>` in the test

  .. code-block:: python
    :lineno-start: 6

        def test_what_is_false(self):
            self.assertIsInstance(False, (bool, int))
            self.assertNotIsInstance(False, float)
            self.assertFalse(False)

  still green

* I can use a `for loop`_ for the :ref:`assertions<what is an assertion?>` that :ref:`test what is False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4-24

        def test_what_is_false(self):
            self.assertIsInstance(False, (bool, int))
            self.assertNotIsInstance(False, float)
            # self.assertFalse(False)
            # self.assertFalse(None)
            # self.assertFalse(0)
            # self.assertFalse(0.0)
            # self.assertFalse(str())
            # self.assertFalse(tuple())
            # self.assertFalse(list())
            # self.assertFalse(set())
            # self.assertFalse(dict())
            for false_item in (
                False,
                None,
                0, 0.0,
                str(),
                tuple(),
                list(),
                set(),
                dict(),
            ):
                with self.subTest(i=false_item):
                    self.assertFalse(false_item)

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 6

        def test_what_is_false(self):
            self.assertIsInstance(False, (bool, int))
            self.assertNotIsInstance(False, float)
            for false_item in (
                False,
                None,
                0, 0.0,
                str(),
                tuple(),
                list(),
                set(),
                dict(),
            ):
                with self.subTest(i=false_item):
                    self.assertFalse(false_item)

  still green

* I add :ref:`True<test_what_is_true>` to make sure the test works

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

                dict(),
                True,
            ):
                with self.subTest(i=false_item):
                    self.assertFalse(false_item)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(i=True) tests/test_booleans.py::TestBooleans::test_what_is_false - AssertionError: True is not false

* I remove the failing line and the test is green again

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
    :lineno-start: 44
    :emphasize-lines: 1

            self.assertEqual(True-1, 0)

  the test passes

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2

            self.assertEqual(True-1, 0)
            self.assertEqual(True*1, 0)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1 != 0

  :ref:`True<test_what_is_true>` is ``1``

* I change the expectation

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 1

            self.assertEqual(True*1, 1)

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 45
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