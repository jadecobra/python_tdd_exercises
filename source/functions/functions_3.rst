.. meta::
   :description: Learn Python functions with TDD! Explore arguments, defaults, and testing techniques in this practical guide. Start coding now!
   :keywords: Jacob Itegboje, Python functions, Test-Driven Development, Python programming, keyword arguments, positional arguments, coding tutorial

.. include:: ../links.rst
.. _product: https://docs.python.org/3/library/itertools.html#itertools.product
.. _product method: product_


#################################################################################
functions 3
#################################################################################

Since I know how to use :ref:`for loops<what is a for loop?>`, I can do better with the :ref:`assertions<what is an assertion?>` of :ref:`test_why_use_a_function`

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``functions`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd functions

  the terminal_ shows I am in the ``functions`` folder_

  .. code-block:: shell

    .../pumping_python/functions

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 5

    rootdir: .../pumping_python/functions
    configfile: pyproject.toml
    collected 12 items

    tests/test_functions.py ............                          [100%]

    ======================= 12 passed in X.YZs =========================

* I hold :kbd:`ctrl` on the keyboard, then click on ``tests/test_functions.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
a better way to test why use a function
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` to :ref:`test_why_use_a_function`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6

        def test_why_use_a_function(self):
            def add(x=3, y=0):
                return x + y

            x = 4
            numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

            y = 0
            self.assertEqual(add(x, y), x+y)

* I add a :ref:`for loop<what is a for loop?>` with an :ref:`assertion<what is an assertion?>` and the `subTest method`_

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3-5

            x = 4
            numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
            for y in numbers:
                with self.subTest(y=y):
                    self.assertEqual(add(x, y), x+x)

            y = 0
            self.assertEqual(add(x, y), x+y)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(y=0) ... - AssertionError: 4 != 104
    SUBFAILED(y=1) ... - AssertionError: 5 != 104
    SUBFAILED(y=2) ... - AssertionError: 6 != 104
    SUBFAILED(y=3) ... - AssertionError: 7 != 104
    SUBFAILED(y=4) ... - AssertionError: 8 != 104
    SUBFAILED(y=5) ... - AssertionError: 9 != 104
    SUBFAILED(y=6) ... - AssertionError: 10 != 104
    SUBFAILED(y=7) ... - AssertionError: 11 != 104
    SUBFAILED(y=8) ... - AssertionError: 12 != 104
    SUBFAILED(y=9) ... - AssertionError: 13 != 104

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the calculation to ``x+y``

.. code-block:: python
  :lineno-start: 11
  :emphasize-lines: 5

            x = 4
            numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
            for y in numbers:
                with self.subTest(y=y):
                    self.assertEqual(add(x, y), x+y)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertions<what is an assertion?>` because the :ref:`for loop<what is a for loop?>` does what they do


  .. code-block:: python
    :lineno-start: 7

          def test_why_use_a_function(self):
              def add(x=3, y=0):
                  return x + y

              x = 4
              numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
              for y in numbers:
                  with self.subTest(y=y):
                      self.assertEqual(add(x, y), x+y)

          def test_making_a_function_w_pass(self):

* I add a :ref:`for loop<what is a for loop?>` for the value of ``x``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4-6

              x = 4
              numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
              for y in numbers:
                  for x in numbers:
                      with self.subTest(x=x, y=y):
                          self.assertEqual(add(x, y), x+100)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    ================== 100 failed, 12 passed in X.YZs ===================

  the two :ref:`for loops<what is a for loop?>` go through every combination of ``x`` and ``y``

  .. code-block:: python

    (x, y)
    (0, 0)
    (0, 1)
    (0, 2)
    ...
    (5, 0)
    (5, 1)
    (5, 2)
    ...
    (9, 7)
    (9, 8)
    (9, 9)

* I change the calculation in the expectation to the right thing

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1

                        self.assertEqual(add(x, y), x+y)

  the test passes

* I remove the ``x`` :ref:`variable<what is a variable?>`, then the :ref:`default values<test_functions_w_default_arguments>` from the ``add`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

        def test_why_use_a_function(self):
            def add(x, y):
                return x + y

            numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
            for y in numbers:
                for x in numbers:
                    with self.subTest(x=x, y=y):
                        self.assertEqual(add(x, y), x+y)

  the test is still green

* I can use a :ref:`list comprehension<test_making_a_list_w_a_list_comprehension>` instead of the 2 :ref:`for loops<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 7-9

            numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
            for y in numbers:
                for x in numbers:
                    with self.subTest(x=x, y=y):
                        self.assertEqual(add(x, y), x+y)

            for x, y in ((x, y) for x in numbers for y in numbers):
                with self.subTest(x=x, y=y):
                    self.assertEqual(add(x, y), x+100)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    ================== 100 failed, 12 passed in X.YZs ===================

* I change the calculation in the expectation

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 1

                    self.assertEqual(add(x, y), x+y)

  the test passes. That used ``for`` 3 times, confusing.

* I can do the same thing with the `product method`_ from the `itertools module`_ which comes with Python_

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 5-8

            for x, y in ((x, y) for x in numbers for y in numbers):
                with self.subTest(x=x, y=y):
                    self.assertEqual(add(x, y), x+y)

            import itertools
            for x, y in itertools.product(numbers, repeat=2):
                with self.subTest(x=x, y=y):
                    self.assertEqual(add(x, y), x+100)


  not as confusing

----

----

----






* I add a :ref:`for loop<what is a for loop?>` and `range object`_ to :ref:`test_why_use_a_function`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5-6

        def test_why_use_a_function(self):
            def add_x(x=3, y=0):
                return x + y

            x = 3
            y = 0
            self.assertEqual(add_x(y=0), 3)

* I use the :ref:`variables<what is a variable?>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3-4

            x = 3
            y = 0
            # self.assertEqual(add_x(y=0), 3)
            self.assertEqual(add_x(x, y), x+x)
            self.assertEqual(add_x(y=1), 4)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 3 != 6

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 4

            x = 3
            y = 0
            # self.assertEqual(add_x(y=0), 3)
            self.assertEqual(add_x(x, y), x+y)
            self.assertEqual(add_x(y=1), 4)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the comment then do the same thing for the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4-6

            x = 3
            y = 0
            self.assertEqual(add_x(x, y), x+y)
            y = 1
            # self.assertEqual(add_x(y=1), 4)
            self.assertEqual(add_x(x, y), x+x)
            self.assertEqual(add_x(y=2), 5)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 4 != 6

* I change the expectation

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 3

            y = 1
            # self.assertEqual(add_x(y=1), 4)
            self.assertEqual(add_x(x, y), x+y)
            self.assertEqual(add_x(y=2), 5)

  the test passes. Wait a minute, ``self.assertEqual(add_x(x, y), x+y)`` is also a repetition!

* I remove the comment then add a :ref:`variable<what is a variable?>` for the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 3-5

            y = 1
            self.assertEqual(add_x(x, y), x+y)
            y = 2
            # self.assertEqual(add_x(y=2), 5)
            self.assertEqual(add_x(x, y), y+y)
            self.assertEqual(add_x(y=3), 6)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 5 != 4

* I change the expectation to the right calculation

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3

            y = 2
            # self.assertEqual(add_x(y=2), 5)
            self.assertEqual(add_x(x, y), x+y)
            self.assertEqual(add_x(y=3), 6)

  the test passes, this is the same as the :ref:`add function<test_addition>` from :ref:`how to make a calculator<how to make a calculator 1>`

* I remove the comment, then add a :ref:`variable<what is a variable?>` for the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3-5

            y = 2
            self.assertEqual(add_x(x, y), x+y)
            y = 3
            # self.assertEqual(add_x(y=3), 6)
            self.assertEqual(add_x(x, y), x+y)
            self.assertEqual(add_x(y=4), 7)

  the test is still green because ``x`` and ``y`` are both ``3``

* on to the next one

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 3-5

            y = 3
            self.assertEqual(add_x(x, y), x+y)
            y = 4
            # self.assertEqual(add_x(y=4), 7)
            self.assertEqual(add_x(x, y), y+y)
            self.assertEqual(add_x(y=5), 8)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 7 != 8

* I change the expectation

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 3

            y = 4
            # self.assertEqual(add_x(y=4), 7)
            self.assertEqual(add_x(x, y), x+y)
            self.assertEqual(add_x(y=5), 8)

  the test passes

* I remove the comment, then add a :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 3-5

            y = 4
            self.assertEqual(add_x(x, y), x+y)
            y = 5
            # self.assertEqual(add_x(y=5), 8)
            self.assertEqual(add_x(x, x), x+y)
            self.assertEqual(add_x(y=6), 9)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 6 != 8

* I change the call

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3

            y = 5
            # self.assertEqual(add_x(y=5), 8)
            self.assertEqual(add_x(x, y), x+y)
            self.assertEqual(add_x(y=6), 9)

  the test passes

* I remove the comment then add a :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3-5

            y = 5
            self.assertEqual(add_x(x, y), x+y)
            y = 6
            # self.assertEqual(add_x(y=6), 9)
            self.assertEqual(add_x(y, y), x+y)
            self.assertEqual(add_x(y=7), 10)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 12 != 9

* I change the call

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 3

            y = 6
            # self.assertEqual(add_x(y=6), 9)
            self.assertEqual(add_x(x, y), x+y)
            self.assertEqual(add_x(y=7), 10)

  the test passes

* I remove the comment then add a :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 3-5

            y = 6
            self.assertEqual(add_x(x, y), x+y)
            y = 7
            # self.assertEqual(add_x(y=7), 10)
            self.assertEqual(add_x(x, y), y+y)
            self.assertEqual(add_x(y=8), 11)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 10 != 14

* I change the expectation

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 3

            y = 7
            # self.assertEqual(add_x(y=7), 10)
            self.assertEqual(add_x(x, y), x+y)
            self.assertEqual(add_x(y=8), 11)

  the test passes

* I remove the comment then add one more :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 3-5

            y = 7
            self.assertEqual(add_x(x, y), x+y)
            y = 8
            # self.assertEqual(add_x(y=8), 11)
            self.assertEqual(add_x(x, y), x+x)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 11 != 6

* I change the expectation

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 3

            y = 8
            # self.assertEqual(add_x(y=8), 11)
            self.assertEqual(add_x(x, y), x+y)

  the test passes

* I remove the comment then use the ``Rename Symbol`` feature to change the name of the ``add_x`` :ref:`function<what is a function?>` to ``add``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2, 7, 9, 11, 13, 15, 17, 19, 21, 23
    :emphasize-text: add

        def test_why_use_a_function(self):
            def add(x=3, y=0):
                return x + y

            x = 4
            y = 0
            self.assertEqual(add(x, y), x+y)
            y = 1
            self.assertEqual(add(x, y), x+y)
            y = 2
            self.assertEqual(add(x, y), x+y)
            y = 3
            self.assertEqual(add(x, y), x+y)
            y = 4
            self.assertEqual(add(x, y), x+y)
            y = 5
            self.assertEqual(add(x, y), x+y)
            y = 6
            self.assertEqual(add(x, y), x+y)
            y = 7
            self.assertEqual(add(x, y), x+y)
            y = 8
            self.assertEqual(add(x, y), x+y)

        def test_making_a_function_w_pass(self):

* I only have to make a change in one place if I want to test what happens when I add ``4`` to a number. I change ``x``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_why_use_a_function(self):
            def add(x=3, y=0):
                return x + y

            x = 4
            y = 0
            self.assertEqual(add(x, y), x+y)

  the test is still green

* I only have to make a change in one place if I want to test what happens when I add ``5`` to a number. I change ``x``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_why_use_a_function(self):
            def add(x=3, y=0):
                return x + y

            x = 5
            y = 0
            self.assertEqual(add_x(x, y), x+y)

  still green.

* I only have to make a change in one place if I want to test what happens when I add ``6`` to a number. I change ``x``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_why_use_a_function(self):
            def add(x=3, y=0):
                return x + y

            x = 6
            y = 0
            self.assertEqual(add_x(x, y), x+y)

  green. Much better than what I had before, the test passes for any number I try, but :ref:`there has to be a better way that does not need all these lines of code<what is a for loop?>`

:ref:`I can use a for loop to remove duplication<what is a for loop?>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_functions.py`` and ``functions.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``functions``

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

I used a :ref:`for loop<what is a variable?>` to remove repetition

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<functions: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to test the calculator with lists<how to make a calculator 4>`
* :ref:`how to use list comprehensions<list comprehensions>`

:ref:`Would you like to test dictionaries?<what is a dictionary?>`

----

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