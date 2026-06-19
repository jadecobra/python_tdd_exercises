.. meta::
  :description: Continuation (part 3) of the beginner Python TDD AssertionError tutorial in the existing assertion_error project: after class attributes (from AssertionError 2), use the None-specific assertIsNone and assertIsNotNone (introduced with full RED/GREEN/REFACTOR + "unexpectedly None" / "X is not None" errors + caution box in the None chapter) to remove repetition of None checks from test_assertion_error_w_none. Replace patterns like assertIs(x, None) / assertIsNot(x, None) / bare assert for None tests while retaining class attrs (an_integer etc.) and mixing with general assertIsNot where appropriate (e.g. assertIsNot(False, None)). "I have these tests by the end" is test_assertion_error_3.py. Teaches when the convenience methods are useful for None. Continues uv run pytest-watcher + git in the shared project. Links from the data_structures/none chapter.
  :keywords: Jacob Itegboje, Pumping Python, AssertionError 3, AssertionError 3: use assertIsNotNone and assertIsNone, assertIsNone, assertIsNotNone, python None assert methods, remove repetition None checks unittest, test_assertion_error_w_none, AssertionError unexpectedly None, AssertionError X is not None, class attributes continuation, assertion_error project, uv pytest-watcher, red green refactor assertIsNone, None is not False with class attrs, Pumping Python TDD AssertionError chapter 3, what is None continuation

.. include:: ../../links.rst

#################################################################################
AssertionError 3: use assertIsNotNone and assertIsNone
#################################################################################

----

I used the :ref:`assertIsNotNone<one more way to test if something is NOT None>` and :ref:`assertIsNone methods<one more way to test if something is None>` to test :ref:`None<what is None?>`. I want to use them to replace :ref:`assertIs and assertIsNot in test_assertion_error_w_none<test_assertion_error_w_none>`.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/assertion_error/test_assertion_error_3.py
  :language: python
  :linenos:

----

*********************************************************************************
continue the project
*********************************************************************************

* Make sure you are in the ``pumping_python`` folder_ with pwd_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  if the terminal_ does not show

  .. code-block:: shell

    .../pumping_python

  `change directory`_ to the ``pumping_python`` folder

* Once in ``pumping_python``, `change directory`_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd assertion_error

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/assertion_error

* I run the tests with `pytest-watcher`_

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows

  .. code-block:: shell
    :emphasize-lines: 5

    rootdir: .../pumping_python/assertion_error
    configfile: pyproject.toml
    collected 6 items

    tests/test_assertion_error.py ......              [100%]

    ================== 6 passed in A.BCs ===================

* I hold :kbd:`ctrl` (Windows_) or :kbd:`option` (MacOS_) on the keyboard, then click on ``tests/test_assertion_error.py`` with the mouse to open it

----

*********************************************************************************
use assertIsNotNone and assertIsNone
*********************************************************************************

* I add a call to :ref:`assertIsNotNone<one more way to test if something is NOT None>` in :ref:`test_assertion_error_w_none`

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

* I change :ref:`assertIsNotNone<one more way to test if something is NOT None>` to a call to :ref:`the assertIsNone method<one more way to test if something is None>`

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

* I add :ref:`assertIsNone<one more way to test if something is None>` for :ref:`False<test_what_is_false>`

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

* I change the call from :ref:`assertIsNone<one more way to test if something is None>` to :ref:`assertIsNotNone<one more way to test if something is NOT None>`

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

* I add :ref:`assertIsNone<one more way to test if something is None>` for :ref:`True<test_what_is_true>`

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

* I change the call from :ref:`assertIsNone<one more way to test if something is None>` to :ref:`assertIsNotNone<one more way to test if something is NOT None>`

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

* I add :ref:`assertIsNone<one more way to test if something is None>` for an integer_ (a whole number without decimals)

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

* I change the call from :ref:`assertIsNone<one more way to test if something is None>` to :ref:`assertIsNotNone<one more way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3-4

            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)
            # self.assertIsNone(self.an_integer)
            self.assertIsNotNone(self.an_integer)

            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)

  the test passes because an integer_ (a whole number without decimals) is not :ref:`None<what is None?>`.

* I add :ref:`assertIsNone<one more way to test if something is None>` for a float_ (binary floating point decimal number)

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

* I change the call from :ref:`assertIsNone<one more way to test if something is None>` to :ref:`assertIsNotNone<one more way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 3-4

            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)
            # self.assertIsNone(self.a_float)
            self.assertIsNotNone(self.a_float)

            assert self.a_string is not None
            self.assertIsNot(self.a_string, None)

  the test passes because a float_ (binary floating point decimal number) is not :ref:`None<what is None?>`.

* I add :ref:`assertIsNone<one more way to test if something is None>` for a string_ (anything in :ref:`quotes`)

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

    AssertionError: 'a string' is not None

* I change the call from :ref:`assertIsNone<one more way to test if something is None>` to :ref:`assertIsNotNone<one more way to test if something is NOT None>`

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

* I add :ref:`assertIsNone<one more way to test if something is None>` for a tuple_ (anything in parentheses ``( )`` separated by a comma)

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

    AssertionError: (1, 2, 3, 'n') is not None

* I change the call from :ref:`assertIsNone<one more way to test if something is None>` to :ref:`assertIsNotNone<one more way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 3-4

            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)
            # self.assertIsNone(self.a_tuple)
            self.assertIsNotNone(self.a_tuple)

            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)

  the test passes because a tuple_ (anything in parentheses ``( )`` separated by a comma) is not :ref:`None<what is None?>`.

* I add :ref:`assertIsNone<one more way to test if something is None>` for a :ref:`list (anything in square brackets '[ ]')<what is a list?>`

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

    AssertionError: [1, 2, 3, 'n'] is not None

* I change the call from :ref:`assertIsNone<one more way to test if something is None>` to :ref:`assertIsNotNone<one more way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 3-4

            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)
            # self.assertIsNone(self.a_list)
            self.assertIsNotNone(self.a_list)

            assert self.a_set is not None
            self.assertIsNot(self.a_set, None)

  the test passes because a :ref:`list (anything in square brackets '[ ]')<what is a list?>` is not :ref:`None<what is None?>`.

* I add :ref:`assertIsNone<one more way to test if something is None>` for a set_ (anything in curly braces ``{ }``, not :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`)

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

    AssertionError: {1, 2, 3, 'n'} is not None

* I change the call from :ref:`assertIsNone<one more way to test if something is None>` to :ref:`assertIsNotNone<one more way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 3-4

            assert self.a_set is not None
            self.assertIsNot(self.a_set, None)
            # self.assertIsNone(self.a_set)
            self.assertIsNotNone(self.a_set)

            assert self.a_dictionary is not None
            self.assertIsNot(self.a_dictionary, None)

  the test passes because a set_ (anything in curly braces ``{ }``, not :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`) is not :ref:`None<what is None?>`.

* I add :ref:`assertIsNone<one more way to test if something is None>` for a :ref:`dictionary (key-value pairs in curly braces '{ }' separated by a comma)<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 3

            assert self.a_dictionary is not None
            self.assertIsNot(self.a_dictionary, None)
            self.assertisNone(self.a_dictionary)

        def test_assertion_error_w_false(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {1, 2, 3, 'n'} is not None

* I change the call from :ref:`assertIsNone<one more way to test if something is None>` to :ref:`assertIsNotNone<one more way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 3-4

            assert self.a_dictionary is not None
            self.assertIsNot(self.a_dictionary, None)
            # self.assertisNone(self.a_dictionary)
            self.assertIsNotNone(self.a_dictionary)

        def test_assertion_error_w_false(self):

  the test passes because a :ref:`dictionary (key-value pairs in curly braces '{ }' separated by a comma)<what is a dictionary?>` is not :ref:`None<what is None?>`.

* I remove the commented lines and :ref:`assertions<what is an assertion?>` that use :ref:`assertIsNot<another way to test if something is NOT the same object as None>`, :ref:`assertIs<another way to test if something is the same object as None>`, and basic `assert statements`_ from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 30

        def test_assertion_error_w_none(self):
            self.assertIsNone(None)
            self.assertIsNotNone(False)
            self.assertIsNotNone(True)
            self.assertIsNotNone(self.an_integer)
            self.assertIsNotNone(self.a_float)
            self.assertIsNotNone(self.a_string)
            self.assertIsNotNone(self.a_tuple)
            self.assertIsNotNone(self.a_list)
            self.assertIsNotNone(self.a_set)
            self.assertIsNotNone(self.a_dictionary)

        def test_assertion_error_w_false(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'use assertIsNotNone and assertIsNone'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use assertIsNotNone and assertIsNone instead of assertIsNot(x, None) and assertIs(x, None)<use assertIsNotNone and assertIsNone>`.

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

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I can use :ref:`assertIsNotNone<one more way to test if something is NOT None>` and :ref:`assertIsNone methods<one more way to test if something is None>` to remove repetition of :ref:`None<what is None?>` from :ref:`assertions<what is an assertion?>` that test if something is :ref:`None<what is None?>` or not - ``assertIs(x, None)`` and ``assertIsNot(x, None)``.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<AssertionError 3: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

I know

:ref:`how to make a Python test driven development environment manually`
* :ref:`what causes AssertionError?`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`how to make classes<classes>`
* :ref:`how to use class attributes to remove repetition<AssertionError 2: use class attributes>`
* :ref:`what happens when classes have one or more parents<family ties>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`what None is and is not<what is None?>`
* :ref:`how to use the assertIsNotNone and assertIsNone<AssertionError 3: use assertIsNotNone and assertIsNone>`

:ref:`Would you like to test the booleans (there are only 2)?<what are booleans?>`

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