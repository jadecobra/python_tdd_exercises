.. meta::
  :description: Continuation of the assertion_error Python TDD project after unittest and the None chapter. Open the existing project (uv run pytest-watcher . --now, 7 passed), edit tests/test_assertion_error.py, and add assertIsNone / assertIsNotNone next to bare assert and assertIs / assertIsNot in test_assertion_error_w_none. Deliberately trigger AssertionError with the wrong method first: assertIsNotNone(None) → "unexpectedly None"; assertIsNone(False) → "False is not None"; same pattern for True, 0, 0.0, '', (), [], set(), {}. Then green with assertIsNone(None) and assertIsNotNone for every non-None value (False, True, empty containers, class attributes an_integer/a_float/…). Remove the commented wrong calls; keep the triple form (assert + assertIs* + assertIsNone/assertIsNotNone). Git commit 'use assertIsNotNone and assertIsNone'. Shows how None-specific unittest methods remove repeating None in assertIs(x, None) / assertIsNot(x, None) while still teaching raise-by-negation error strings. Pumping Python by Jacob Itegboje.
  :keywords: Jacob Itegboje, Pumping Python, AssertionError assertIsNone, assertIsNotNone, unexpectedly None, False is not None, True is not None, 0 is not None, 0.0 is not None, '' is not None, () is not None, [] is not None, set() is not None, {} is not None, test_assertion_error_w_none, replace assertIs(x, None), assertIsNot(x, None), another way to test if something is None, another way to test if something is NOT None, None chapter continuation, assertion_error project, uv run pytest-watcher, remove the commented lines, red green refactor assertIsNone, python unittest assertIsNone beginner, TDD None identity tests, class attributes empty string list dict set tuple, test AssertionError with assertIsNotNone and assertIsNone

.. include:: ../../links.rst

#################################################################################
test AssertionError with assertIsNotNone and assertIsNone
#################################################################################

----

I want to use the :ref:`assertIsNotNone<another way to test if something is NOT None>` and :ref:`assertIsNone methods<another way to test if something is None>` to test :ref:`None<what is None?>` in :ref:`test_assertion_error_w_none<test_assertion_error_w_none>`.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_none.py
  :language: python
  :linenos:
  :caption: assertion_error/tests/test_assertion_error.py

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`assertion_error folder<what is an assertion?>` in the ``pumping_python`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd assertion_error

* I open ``test_assertion_error.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows

  .. code-block:: shell

    tests/test_assertion_error.py .......             [100%]

    ================== 7 passed in D.EFs ===================

----

*********************************************************************************
use assertIsNotNone and assertIsNone
*********************************************************************************

* I add a :ref:`call<how to call a function with input>` to :ref:`assertIsNotNone<another way to test if something is NOT None>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)
            self.assertIsNotNone(None)

            assert False is not None
            self.assertIsNot(False, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly None

  because :ref:`None is None<what is None?>`

* I change :ref:`assertIsNotNone<another way to test if something is NOT None>` to a call to :ref:`the assertIsNone method<another way to test if something is None>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4-5

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)
            # self.assertIsNotNone(None)
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNot(False, None)

  the test passes

* I add :ref:`assertIsNone<another way to test if something is None>` for :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 3

            assert False is not None
            self.assertIsNot(False, None)
            self.assertIsNone(False)

            assert True is not None
            self.assertIsNot(True, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not None

* I change the call from :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertIsNotNone<another way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 3-4

            assert False is not None
            self.assertIsNot(False, None)
            # self.assertIsNone(False)
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNot(True, None)

  the test passes because :ref:`False<test_what_is_false>` is not :ref:`None<what is None?>`.

* I add :ref:`assertIsNone<another way to test if something is None>` for :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 3

            assert True is not None
            self.assertIsNot(True, None)
            self.assertIsNone(True)

            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not None

* I change the call from :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertIsNotNone<another way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 3-4

            assert True is not None
            self.assertIsNot(True, None)
            # self.assertIsNone(True)
            self.assertIsNotNone(True)

            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)

  the test passes because :ref:`True<test_what_is_true>` is not :ref:`None<what is None?>`.

* I add :ref:`assertIsNone<another way to test if something is None>` for an integer_ (a whole number without decimals)

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3

            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)
            self.assertIsNone(self.an_integer)

            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 is not None

* I change the call from :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertIsNotNone<another way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3-4

            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)
            # self.assertIsNone(self.an_integer)
            self.assertIsNotNone(self.an_integer)

            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)

  the test passes because an integer_ is not :ref:`None<what is None?>`.

* I add :ref:`assertIsNone<another way to test if something is None>` for a float_ (binary floating point decimal number)

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 3

            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)
            self.assertIsNone(self.a_float)

            assert self.a_string is not None
            self.assertIsNot(self.a_string, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.0 is not None

* I change the call from :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertIsNotNone<another way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 3-4

            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)
            # self.assertIsNone(self.a_float)
            self.assertIsNotNone(self.a_float)

            assert self.a_string is not None
            self.assertIsNot(self.a_string, None)

  the test passes because a float_ is not :ref:`None<what is None?>`.

* I add :ref:`assertIsNone<another way to test if something is None>` for a string_ (anything in :ref:`quotes`)

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 3

            assert self.a_string is not None
            self.assertIsNot(self.a_string, None)
            self.assertIsNone(self.a_string)

            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '' is not None

* I change the call from :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertIsNotNone<another way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 3-4

            assert self.a_string is not None
            self.assertIsNot(self.a_string, None)
            # self.assertIsNone(self.a_string)
            self.assertIsNotNone(self.a_string)

            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)

  the test passes because a string_ (anything in :ref:`quotes`) is not :ref:`None<what is None?>`.

* I add :ref:`assertIsNone<another way to test if something is None>` for a tuple_ (anything in parentheses ``( )`` separated by a comma)

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 3

            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)
            self.assertIsNone(self.a_tuple)

            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: () is not None

* I change the call from :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertIsNotNone<another way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 3-4

            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)
            # self.assertIsNone(self.a_tuple)
            self.assertIsNotNone(self.a_tuple)

            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)

  the test passes because a tuple_ is not :ref:`None<what is None?>`.

* I add :ref:`assertIsNone<another way to test if something is None>` for a :ref:`list (anything in square brackets '[ ]')<what is a list?>`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 3

            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)
            self.assertIsNone(self.a_list)

            assert self.a_set is not None
            self.assertIsNot(self.a_set, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: [] is not None

* I change the call from :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertIsNotNone<another way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 3-4

            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)
            # self.assertIsNone(self.a_list)
            self.assertIsNotNone(self.a_list)

            assert self.a_set is not None
            self.assertIsNot(self.a_set, None)

  the test passes because a :ref:`list<what is a list?>` is not :ref:`None<what is None?>`.

* I add :ref:`assertIsNone<another way to test if something is None>` for a set_ (anything in curly braces ``{ }``, not :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`)

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 3

            assert self.a_set is not None
            self.assertIsNot(self.a_set, None)
            self.assertIsNone(self.a_set)

            assert self.a_dictionary is not None
            self.assertIsNot(self.a_dictionary, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: set() is not None

* I change the call from :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertIsNotNone<another way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 3-4

            assert self.a_set is not None
            self.assertIsNot(self.a_set, None)
            # self.assertIsNone(self.a_set)
            self.assertIsNotNone(self.a_set)

            assert self.a_dictionary is not None
            self.assertIsNot(self.a_dictionary, None)

  the test passes because a set_ is not :ref:`None<what is None?>`.

* I add :ref:`assertIsNone<another way to test if something is None>` for a :ref:`dictionary (key-value pairs in curly braces '{ }' separated by commas)<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 3

            assert self.a_dictionary is not None
            self.assertIsNot(self.a_dictionary, None)
            self.assertIsNone(self.a_dictionary)

        def test_assertion_error_w_false(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {} is not None

* I change the call from :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertIsNotNone<another way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 3-4

            assert self.a_dictionary is not None
            self.assertIsNot(self.a_dictionary, None)
            # self.assertIsNone(self.a_dictionary)
            self.assertIsNotNone(self.a_dictionary)

        def test_assertion_error_w_false(self):

  the test passes because a :ref:`dictionary<what is a dictionary?>` is not :ref:`None<what is None?>`.

* I remove the commented lines from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 30

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)
            self.assertIsNone(None)

  .. code-block:: python
    :lineno-start: 35

            assert False is not None
            self.assertIsNot(False, None)
            self.assertIsNotNone(False)

  .. code-block:: python
    :lineno-start: 39

            assert True is not None
            self.assertIsNot(True, None)
            self.assertIsNotNone(True)

  .. code-block:: python
    :lineno-start: 43

            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)
            self.assertIsNotNone(self.an_integer)

  .. code-block:: python
    :lineno-start: 47

            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)
            self.assertIsNotNone(self.a_float)

  .. code-block:: python
    :lineno-start: 51

            assert self.a_string is not None
            self.assertIsNot(self.a_string, None)
            self.assertIsNotNone(self.a_string)

  .. code-block:: python
    :lineno-start: 55

            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)
            self.assertIsNotNone(self.a_tuple)

  .. code-block:: python
    :lineno-start: 59

            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)
            self.assertIsNotNone(self.a_list)

  .. code-block:: python
    :lineno-start: 63

            assert self.a_set is not None
            self.assertIsNot(self.a_set, None)
            self.assertIsNotNone(self.a_set)

  .. code-block:: python
    :lineno-start: 67

            assert self.a_dictionary is not None
            self.assertIsNot(self.a_dictionary, None)
            self.assertIsNotNone(self.a_dictionary)

        def test_assertion_error_w_false(self):

* I open a new terminal_ then change directories to ``assertion_error``

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'use assertIsNotNone and assertIsNone'

:ref:`I can use assertIsNotNone and assertIsNone for assertIsNot(x, None) and assertIs(x, None)<use assertIsNotNone and assertIsNone>`.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_assertion_error.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``assertion_error``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ is my friend, and shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

I can use :ref:`assertIsNone methods<another way to test if something is None>` and :ref:`assertIsNotNone<another way to test if something is NOT None>` for :ref:`assertions<what is an assertion?>` that test if something is :ref:`None<what is None?>` or not - ``assertIs(x, None)`` and ``assertIsNot(x, None)``.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test AssertionError with assertIsNotNone and assertIsNone: tests>`

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
* :ref:`I know how to make a person with a class<how to make a person with a class>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.

:ref:`Would you like to use the assertIsNotNone and assertIsNone methods with the functions project?<test functions with assertIsNotNone and assertIsNone>`

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