.. meta::
  :description: Part 2 of the beginner Python TDD AssertionError tutorial continuing in the assertion_error project: refactor repeated variable initializations (an_integer = 0, a_float = 0.0, a_string, tuples/lists/sets/dicts) by using class attributes on the TestAssertionError class instead of duplicating inside test_assertion_error_w_none, w_false, w_true (and the equality/is-vs-equal tests). The chapter first explores adding the setUp method (as introduced in the classes chapter) with self.an_integer = 0 etc and updating tests to self.xxx (with old local inits commented out), then concludes "In this case, I do not need the setUp method because the class attributes are the same for every test and I do not need anything to run before each test. I move them out", hits NameError: name 'self' is not defined when trying self. = directly under class, fixes by using bare "an_integer = 0" etc at class level, removes the commented setUp and duplicate locals, commits with 'extract class attributes'. The "I have these tests by the end of the chapter" literalinclude of test_assertion_error_2.py shows the final: 7 class attrs + self. access in the w_* tests (test_what_is_an_assertion keeps its local reality/my_expectation vars), still mixing bare `assert` + self.assertIs / self.assertIsNot / self.assertEqual etc on the same None/True/False/0-vs-0.0 examples from part 1. Teaches choosing plain class attributes vs setUp for DRY unittest.TestCase based on whether fresh-per-test values are required (constants vs randoms/mutables). Continues red-green-refactor + uv run pytest-watcher . --now in the existing project.
  :keywords: Jacob Itegboje, Pumping Python, AssertionError 2, AssertionError 2: use class attributes, use class attributes unittest TestCase, python class attributes for DRY tests, class attributes vs setUp unittest, when not to use setUp, "In this case, I do not need the setUp method", "I do not need anything to run before each test", "extract class attributes", NameError: name 'self' is not defined, self is not defined class body python, an_integer = 0 class attribute, a_float = 0.0, a_string a_tuple a_list a_set a_dictionary class attrs, test_assertion_error_2.py, refactor locals to class attributes python, unittest no setUp needed for constants, red green refactor class attributes, continuing assertion_error project uv pytest-watcher, 0 is not 0.0 class attribute, None is not False, True is not None, is vs == with class attrs, bare assert self.assertIsNot, Pumping Python TDD AssertionError chapter 2, test_what_is_an_assertion, test_assertion_error_w_none w_false w_true w_equality w_is_vs_equal

.. include:: ../../links.rst

#################################################################################
AssertionError 3: user assertIsNotNone and assertIsNone
#################################################################################

----

I used the :ref:`assertIsNotNone<how I test if something is NOT None>` and :ref:`assertIsNone methods<how I test if something is None>` to test :ref:`None<what is None?>`. I want to use them to replace :ref:`assertIs and assertIsNot in test_assertion_error_w_none<test_assertion_error_w_none>`.

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
user assertIsNotNone and assertIsNone
*********************************************************************************

* I add a call to :ref:`assertIsNotNone<how I test if something is NOT None>` in :ref:`test_assertion_error_w_none`

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

* I change :ref:`assertIsNotNone<how I test if something is NOT None>` to a call to :ref:`the assertIsNone method<how I test if something is None>`

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

* I add :ref:`assertIsNone<how I test if something is None>` for :ref:`False<test_what_is_false>`

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

* I change the call to :ref:`assertIsNone<how I test if something is None>` to :ref:`assertIsNotNone<how I test if something is NOT None>`

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

* I add :ref:`assertIsNone<how I test if something is None>` for :ref:`True<test_what_is_true>`

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


* I change the call to :ref:`assertIsNone<how I test if something is None>` to :ref:`assertIsNotNone<how I test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 3-4

            assert False is not None
            self.assertIsNot(False, None)
            # self.assertIsNone(False)
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNot(True, None)

  the test passes because :ref:`True<test_what_is_true>` is not :ref:`None<what is None?>`.


:ref:`I can use assertIsNotNone and assertIsNone instead of assertIsNot(x, None) and assertIs(x, None)<user assertIsNotNone and assertIsNone>`

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

I can use :ref:`class attributes<what is a class attribute?>` for things that repeat, which allows :ref:`methods<what is a method?>` of the same :ref:`class<what is a class?>` to use them.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<AssertionError 2: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

As a reminder, you know

* :ref:`how to make a Python test driven development environment manually<how to make a Python test driven development environment>`
* :ref:`what causes AssertionError?`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`how to make classes<classes>`
* :ref:`how to use class attributes to remove repetition<AssertionError 2: use class attributes>`

:ref:`Would you like to use class attributes with the 'functions' project?<Functions 2: use class attributes>`

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