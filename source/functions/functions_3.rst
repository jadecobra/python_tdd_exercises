.. _test functions with assertIsNotNone and assertIsNone:

.. meta::
  :description: Part 2 / continuation of the beginner Python TDD functions tutorial in the functions project: use class attributes on TestFunctions (first, last, a_tuple, a_list, first_number, second_number) to remove repetition of string literals, tuples, lists and numbers from test_positional_arguments, test_keyword_arguments, test_args_and_kwargs (and cross-call sites) instead of duplicating locals like first, last = 'first', 'last' or a_tuple = (0, 1, 2, 'n') inside each test. Builds directly on :ref:`AssertionError 2: use class attributes` and the setUp / class attributes lessons from the classes chapter. Although classes teaches the setUp method to reset fresh values before every test, here the values are constants identical across tests so plain class attributes at the Test class level suffice (no setUp needed, no per-test reset). The "I have these tests by the end of the chapter" literalinclude of test_functions_w_input.py shows the final state with 6 class attrs + self. access in the affected tests (test_why_use_a_function and maker/optional/unknown tests keep their original structure and local vars). Continues red-green-refactor + uv run pytest-watcher in the existing functions project after the base functions chapter. Demonstrates "extract class attributes" for DRY unittest.TestCase test code.
  :keywords: Jacob Itegboje, Pumping Python, functions 2, test functions with assertIsNotNone and assertIsNone, use class attributes unittest TestCase, python class attributes for DRY tests, class attributes vs setUp unittest, when not to use setUp, "In this case, I do not need the setUp method", "I do not need anything to run before each test", "extract class attributes", test_functions_w_input.py, refactor locals to class attributes python, unittest no setUp needed for constants, red green refactor class attributes, continuing functions project uv pytest-watcher, test_positional_arguments, test_keyword_arguments, 'first', 'last', (0, 1, 2, 'n'), first_number second_number class attr, functions TDD class attributes, Pumping Python functions chapter 2

.. include:: ../links.rst

#################################################################################
test functions with assertIsNotNone and assertIsNone
#################################################################################

In :ref:`AssertionError 2: use class attributes` I used :ref:`class attributes<what is a class attribute?>` to remove repetition from the :ref:`assertion_error project<what is an assertion?>`. The :ref:`classes` chapter teaches the :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to ensure each test method starts with fresh values. In some cases the values I need are the same for every test. In this case, I do not need the setUp method because the class attributes are the same for every test and I do not need anything to run before each test. I want to do the same thing in the :ref:`functions project<what is a function?>`.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/functions/test_functions_w_input.py
  :language: python
  :linenos:

----

*********************************************************************************
continue the project
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

  the terminal_ is my friend, and shows

  .. code-block:: shell
    :emphasize-lines: 5

    rootdir: .../pumping_python/functions
    configfile: pyproject.toml
    collected 12 items

    tests/test_functions.py ............                  [100%]

    =================== 12 passed in X.YZs =====================

* I hold :kbd:`ctrl` on the keyboard, then click on ``tests/test_functions.py`` to open it

----

* I add :ref:`class attributes<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3-4

    class TestFunctions(unittest.TestCase):

        first = 'first'
        last = 'last'

        def test_why_use_a_function(self):

* I use the :ref:`class attributes<what is a class attribute?>` to remove repetition of ``'first'`` and ``'last'`` from :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 2, 5-6, 8-9, 13-14, 16-17

        def test_positional_arguments(self):
            # first, last = 'first', 'last'

            reality = src.functions.positional_arguments(
                # first, last,
                self.first, self.last,
            )
            # my_expectation = (first, last)
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.positional_arguments(
                # last, first,
                self.last, self.first,
            )
            # my_expectation = (last, first)
            my_expectation = (self.last, self.first)
            self.assertEqual(reality, my_expectation)

  the test is still green.

* I use the :ref:`class attributes<what is a class attribute?>` to remove repetition of ``'first'`` and ``'last'`` from :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 170
    :emphasize-lines: 2, 5-7, 9-10, 14-16, 18-19, 23-24, 26-27

        def test_keyword_arguments(self):
            # first, last = 'first', 'last'

            reality = src.functions.w_keyword_arguments(
                # first_input=first, last_input=last,
                first_input=self.first,
                last_input=self.last,
            )
            # my_expectation = (first, last)
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                # last_input=last, first_input=first,
                last_input=self.last,
                first_input=self.first,
            )
            # my_expectation = (first, last)
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                # last, first,
                self.last, self.first,
            )
            # my_expectation = (last, first)
            my_expectation = (self.last, self.first)
            self.assertEqual(reality, my_expectation)

  still green.

* I use the :ref:`class attributes<what is a class attribute?>` to remove ``'first'`` and ``'last'`` from :ref:`test_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 224
    :emphasize-lines: 2, 5-6, 9-10

        def test_args_and_kwargs(self):
            # first, last = 'first', 'last'
            reality = (
                src.functions.args_and_kwargs(
                    # first, last_input=last,
                    self.first, last_input=self.last,
                )
            )
            # my_expectation = (first, last)
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

        def test_optional_arguments(self):

  green.

* I remove the commented lines from :ref:`test_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 224

        def test_args_and_kwargs(self):
            reality = (
                src.functions.args_and_kwargs(
                    self.first, last_input=self.last,
                )
            )
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

        def test_optional_arguments(self):

----

* I add a :ref:`class attribute<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 5

    class TestFunctions(unittest.TestCase):

        first = 'first'
        last = 'last'
        a_tuple = (0, 1, 2, 'n')

        def test_why_use_a_function(self):

* I use the new :ref:`class attribute<what is a class attribute?>` to remove repetition of ``(0, 1, 2, 'n')`` from :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 137
    :emphasize-lines: 27, 30-31, 33-34

        def test_positional_arguments(self):
            # first, last = 'first', 'last'

            reality = src.functions.positional_arguments(
                # first, last,
                self.first, self.last,
            )
            # my_expectation = (first, last)
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.positional_arguments(
                # last, first,
                self.last, self.first,
            )
            # my_expectation = (last, first)
            my_expectation = (self.last, self.first)
            self.assertEqual(reality, my_expectation)

            first_number, second_number = 0, 1
            reality = src.functions.positional_arguments(
                first_number, second_number,
            )
            my_expectation = (first_number, second_number)
            self.assertEqual(reality, my_expectation)

            # a_tuple = (0, 1, 2, 'n')
            a_list = [0, 1, 2, 'n']
            reality = src.functions.positional_arguments(
                # a_tuple, a_list,
                self.a_tuple, a_list,
            )
            # my_expectation = (a_tuple, a_list)
            my_expectation = (self.a_tuple, a_list)
            self.assertEqual(reality, my_expectation)

        def test_keyword_arguments(self):

  still green.

* I use the new :ref:`class attribute<what is a class attribute?>` to remove repetition of ``(0, 1, 2, 'n')`` from :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 173
    :emphasize-lines: 46, 50-51, 53-54

        def test_keyword_arguments(self):
            # first, last = 'first', 'last'

            reality = src.functions.w_keyword_arguments(
                # first_input=first, last_input=last,
                first_input=self.first,
                last_input=self.last,
            )
            # my_expectation = (first, last)
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                # last_input=last, first_input=first,
                last_input=self.last,
                first_input=self.first,
            )
            # my_expectation = (first, last)
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                # last, first,
                self.last, self.first,
            )
            # my_expectation = (last, first)
            my_expectation = (self.last, self.first)
            self.assertEqual(reality, my_expectation)

            zero, one = 0, 1
            reality = src.functions.w_keyword_arguments(
                last_input=zero, first_input=one,
            )
            my_expectation = (one, zero)
            self.assertEqual(reality, my_expectation)

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            reality = src.functions.w_keyword_arguments(
                first_input=a_set,
                last_input=a_dictionary,
            )
            my_expectation = (a_set, a_dictionary)
            self.assertEqual(reality, my_expectation)

            # a_tuple = (0, 1, 2, 'n')
            a_list = [0, 1, 2, 'n']
            reality = src.functions.positional_arguments(
                first_input=a_list,
                # last_input=a_tuple,
                last_input=self.a_tuple,
            )
            # my_expectation = (a_list, a_tuple)
            my_expectation = (a_list, self.a_tuple)
            self.assertEqual(reality, my_expectation)

        def test_args_and_kwargs(self):

  the test is still green.


----

* I add a :ref:`class attribute<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 6

    class TestFunctions(unittest.TestCase):

        first = 'first'
        last = 'last'
        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']

        def test_why_use_a_function(self):

* I use the new :ref:`class attribute<what is a class attribute?>` to remove repetition of ``[0, 1, 2, 'n']`` from :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 28, 31-32, 34-35

        def test_positional_arguments(self):
            # first, last = 'first', 'last'

            reality = src.functions.positional_arguments(
                # first, last,
                self.first, self.last,
            )
            # my_expectation = (first, last)
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.positional_arguments(
                # last, first,
                self.last, self.first,
            )
            # my_expectation = (last, first)
            my_expectation = (self.last, self.first)
            self.assertEqual(reality, my_expectation)

            first_number, second_number = 0, 1
            reality = src.functions.positional_arguments(
                first_number, second_number,
            )
            my_expectation = (first_number, second_number)
            self.assertEqual(reality, my_expectation)

            # a_tuple = (0, 1, 2, 'n')
            # a_list = [0, 1, 2, 'n']
            reality = src.functions.positional_arguments(
                # a_tuple, a_list,
                # self.a_tuple, a_list,
                self.a_tuple, self.a_list,
            )
            # my_expectation = (a_tuple, a_list)
            # my_expectation = (self.a_tuple, a_list)
            my_expectation = (self.a_tuple, self.a_list)
            self.assertEqual(reality, my_expectation)

        def test_keyword_arguments(self):

  still green.

* I use the new :ref:`class attribute<what is a class attribute?>` to remove repetition of ``[0, 1, 2, 'n']`` from :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 176
    :emphasize-lines: 47, 49, 51, 55-56

        def test_keyword_arguments(self):
            # first, last = 'first', 'last'

            reality = src.functions.w_keyword_arguments(
                # first_input=first, last_input=last,
                first_input=self.first,
                last_input=self.last,
            )
            # my_expectation = (first, last)
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                # last_input=last, first_input=first,
                last_input=self.last,
                first_input=self.first,
            )
            # my_expectation = (first, last)
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                # last, first,
                self.last, self.first,
            )
            # my_expectation = (last, first)
            my_expectation = (self.last, self.first)
            self.assertEqual(reality, my_expectation)

            zero, one = 0, 1
            reality = src.functions.w_keyword_arguments(
                last_input=zero, first_input=one,
            )
            my_expectation = (one, zero)
            self.assertEqual(reality, my_expectation)

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            reality = src.functions.w_keyword_arguments(
                first_input=a_set,
                last_input=a_dictionary,
            )
            my_expectation = (a_set, a_dictionary)
            self.assertEqual(reality, my_expectation)

            # a_tuple = (0, 1, 2, 'n')
            # a_list = [0, 1, 2, 'n']
            reality = src.functions.positional_arguments(
                # first_input=a_list,
                # last_input=a_tuple,
                first_input=self.a_list,
                last_input=self.a_tuple,
            )
            # my_expectation = (a_list, a_tuple)
            # my_expectation = (a_list, self.a_tuple)
            my_expectation = (self.a_list, self.a_tuple)
            self.assertEqual(reality, my_expectation)

        def test_args_and_kwargs(self):

  green.

----

* I add :ref:`class attribute<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 7-8

    class TestFunctions(unittest.TestCase):

        first = 'first'
        last = 'last'
        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        first_number = 0
        second_number = 1

        def test_why_use_a_function(self):

* I use the new :ref:`class attributes<what is a class attribute?>` to remove repetition of ``0`` and ``1`` from :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 20, 22-23, 25-28

        def test_positional_arguments(self):
            # first, last = 'first', 'last'

            reality = src.functions.positional_arguments(
                # first, last,
                self.first, self.last,
            )
            # my_expectation = (first, last)
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.positional_arguments(
                # last, first,
                self.last, self.first,
            )
            # my_expectation = (last, first)
            my_expectation = (self.last, self.first)
            self.assertEqual(reality, my_expectation)

            # first_number, second_number = 0, 1
            reality = src.functions.positional_arguments(
                # first_number, second_number,
                self.first_number, self.second_number,
            )
            # my_expectation = (first_number, second_number)
            my_expectation = (
                self.first_number, self.second_number
            )
            self.assertEqual(reality, my_expectation)

            # a_tuple = (0, 1, 2, 'n')
            # a_list = [0, 1, 2, 'n']
            reality = src.functions.positional_arguments(
                # a_tuple, a_list,
                # self.a_tuple, a_list,
                self.a_tuple, self.a_list,
            )
            # my_expectation = (a_tuple, a_list)
            # my_expectation = (self.a_tuple, a_list)
            my_expectation = (self.a_tuple, self.a_list)
            self.assertEqual(reality, my_expectation)

        def test_keyword_arguments(self):

  still green.

* I remove the commented lines from :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 140

        def test_positional_arguments(self):
            reality = src.functions.positional_arguments(
                self.first, self.last,
            )
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.positional_arguments(
                self.last, self.first,
            )
            my_expectation = (self.last, self.first)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.positional_arguments(
                self.first_number, self.second_number,
            )
            my_expectation = (
                self.first_number, self.second_number
            )
            self.assertEqual(reality, my_expectation)

            reality = src.functions.positional_arguments(
                self.a_tuple, self.a_list,
            )
            my_expectation = (self.a_tuple, self.a_list)
            self.assertEqual(reality, my_expectation)

        def test_keyword_arguments(self):

* I use the new :ref:`class attributes<what is a class attribute?>` to remove repetition of ``0`` and ``1`` from :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 167
    :emphasize-lines: 30, 32-34, 36-39

        def test_keyword_arguments(self):
            # first, last = 'first', 'last'

            reality = src.functions.w_keyword_arguments(
                # first_input=first, last_input=last,
                first_input=self.first,
                last_input=self.last,
            )
            # my_expectation = (first, last)
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                # last_input=last, first_input=first,
                last_input=self.last,
                first_input=self.first,
            )
            # my_expectation = (first, last)
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                # last, first,
                self.last, self.first,
            )
            # my_expectation = (last, first)
            my_expectation = (self.last, self.first)
            self.assertEqual(reality, my_expectation)

            # zero, one = 0, 1
            reality = src.functions.w_keyword_arguments(
                # last_input=zero, first_input=one,
                last_input=self.first_number,
                first_input=self.second_number,
            )
            # my_expectation = (one, zero)
            my_expectation = (
                self.second_number, self.first_number
            )
            self.assertEqual(reality, my_expectation)

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            reality = src.functions.w_keyword_arguments(
                first_input=a_set,
                last_input=a_dictionary,
            )
            my_expectation = (a_set, a_dictionary)
            self.assertEqual(reality, my_expectation)

            # a_tuple = (0, 1, 2, 'n')
            # a_list = [0, 1, 2, 'n']
            reality = src.functions.positional_arguments(
                # first_input=a_list,
                # last_input=a_tuple,
                first_input=self.a_list,
                last_input=self.a_tuple,
            )
            # my_expectation = (a_list, a_tuple)
            # my_expectation = (a_list, self.a_tuple)
            my_expectation = (self.a_list, self.a_tuple)
            self.assertEqual(reality, my_expectation)

        def test_args_and_kwargs(self):

* I remove the commented lines from :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 167

        def test_keyword_arguments(self):
            reality = src.functions.w_keyword_arguments(
                first_input=self.first,
                last_input=self.last,
            )
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                last_input=self.last,
                first_input=self.first,
            )
            my_expectation = (self.first, self.last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                self.last, self.first,
            )
            my_expectation = (self.last, self.first)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                last_input=self.first_number,
                first_input=self.second_number,
            )
            my_expectation = (
                self.second_number, self.first_number
            )
            self.assertEqual(reality, my_expectation)

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            reality = src.functions.w_keyword_arguments(
                first_input=a_set,
                last_input=a_dictionary,
            )
            my_expectation = (a_set, a_dictionary)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.positional_arguments(
                first_input=self.a_list,
                last_input=self.a_tuple,
            )
            my_expectation = (self.a_list, self.a_tuple)
            self.assertEqual(reality, my_expectation)

        def test_args_and_kwargs(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract class attributes'

:ref:`I can use class attributes to remove repetition<what is a class attribute?>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_functions.py`` and ``functions.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``functions``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

In :ref:`AssertionError 2: use class attributes` I used :ref:`class attributes<what is a class attribute?>` to remove repetition. The :ref:`classes` chapter shows :ref:`the setUp method<how to use the setUp method to reset class attributes for every test>` to make new values before every test, for example when I want random values for each test.

In some cases the values I need are the same for every test, which means I do not need :ref:`the setUp method<how to use the setUp method to reset class attributes for every test>` because the :ref:`class attributes<what is a class attribute?>` are the same for every test and I do not need anything to run before each test.

I can place the constants directly under the ``TestFunctions`` class:

.. code-block:: python

    first = 'first'
    last = 'last'
    a_tuple = (0, 1, 2, 'n')
    a_list = [0, 1, 2, 'n']
    first_number = 0
    second_number = 1

then :ref:`test_positional_arguments`, :ref:`test_keyword_arguments` and :ref:`test_args_and_kwargs` use ``self.first`` and so on, instead repeated values.

I can use :ref:`class attributes<what is a class attribute?>` for things that repeat (when they are constants), which allows :ref:`methods<what is a method?>` of the same :ref:`class<everything is an object>` to use them without :ref:`the setUp method<how to use the setUp method to reset class attributes for every test>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<functions: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

Here is another reminder, you know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what an assertion is<what is an assertion?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`how to make classes<classes>`
* :ref:`how to use class attributes to remove repetition<AssertionError 2: use class attributes>`
* :ref:`what happens when classes have one or more parents<family ties>`

:ref:`Would you like to test AttributeError?<what causes AttributeError?>`

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