.. meta::
  :description: Part 2 of the beginner Python TDD AssertionError tutorial continuing in the assertion_error project: refactor repeated variable initializations (an_integer = 0, a_float = 0.0, a_string, tuples/lists/sets/dicts) by using class attributes on the TestAssertionError class instead of duplicating inside test_assertion_error_w_none, w_false, w_true (and the equality/is-vs-equal tests). The chapter first explores adding the setUp method (as introduced in the classes chapter) with self.an_integer = 0 etc and updating tests to self.xxx (with old local inits commented out), then concludes "In this case, I do not need the setUp method because the class attributes are the same for every test and I do not need anything to run before each test. I move them out", hits NameError: name 'self' is not defined when trying self. = directly under class, fixes by using bare "an_integer = 0" etc at class level, removes the commented setUp and duplicate locals, commits with 'extract class attributes'. The "I have these tests by the end of the chapter" literalinclude of test_assertion_error_2.py shows the final: 7 class attrs + self. access in the w_* tests (test_what_is_an_assertion keeps its local reality/my_expectation vars), still mixing bare `assert` + self.assertIs / self.assertIsNot / self.assertEqual etc on the same None/True/False/0-vs-0.0 examples from part 1. Teaches choosing plain class attributes vs setUp for DRY unittest.TestCase based on whether fresh-per-test values are required (constants vs randoms/mutables). Continues red-green-refactor + uv run pytest-watcher . --now in the existing project.
  :keywords: Jacob Itegboje, Pumping Python, AssertionError 2, AssertionError 2: use class attributes, use class attributes unittest TestCase, python class attributes for DRY tests, class attributes vs setUp unittest, when not to use setUp, "In this case, I do not need the setUp method", "I do not need anything to run before each test", "extract class attributes", NameError: name 'self' is not defined, self is not defined class body python, an_integer = 0 class attribute, a_float = 0.0, a_string a_tuple a_list a_set a_dictionary class attrs, test_assertion_error_2.py, refactor locals to class attributes python, unittest no setUp needed for constants, red green refactor class attributes, continuing assertion_error project uv pytest-watcher, 0 is not 0.0 class attribute, None is not False, True is not None, is vs == with class attrs, bare assert self.assertIsNot, Pumping Python TDD AssertionError chapter 2, test_what_is_an_assertion, test_assertion_error_w_none w_false w_true w_equality w_is_vs_equal

.. include:: ../../links.rst

#################################################################################
AssertionError 2: use class attributes
#################################################################################

----

I used the :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` in :ref:`classes` to remove repetition of :ref:`variables<what is a variable?>` by making them :ref:`class attributes<what is a class attribute?>` that the test :ref:`methods<what is a method?>` can all use.

I want to do the same thing with the :ref:`assertion_project<what is an assertion?>`.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/assertion_error/test_assertion_error_2.py
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

* I hold :kbd:`ctrl` (Windows_) or :kbd:`option` (MacOS_) on the keyboard, then click on ``tests/test_assertion_error.py`` with the mouse to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
remove repetition with class attributes
*********************************************************************************

* I add the :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to the ``TestAssertionError`` :ref:`class<what is a class?>` with :ref:`a class attribute<what is a class attribute?>` to use to remove repetition of ``an_integer = 0``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-4

    class TestAssertionError(unittest.TestCase):

        def setUp(self):
            self.an_integer = 0

        def test_what_is_an_assertion(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``an_integer = 0`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 11-15

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)

            assert False is not None
            self.assertIsNot(False, None)

            assert True is not None
            self.assertIsNot(True, None)

            # an_integer = 0
            # assert an_integer is not None
            # self.assertIsNot(an_integer, None)
            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)

            a_float = 0.0
            assert a_float is not None
            self.assertIsNot(a_float, None)

            a_string = 'a string'
            assert a_string is not None
            self.assertIsNot(a_string, None)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not None
            self.assertIsNot(a_tuple, None)

            a_list = [1, 2, 3, 'n']
            assert a_list is not None
            self.assertIsNot(a_list, None)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not None
            self.assertIsNot(a_set, None)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not None
            self.assertIsNot(a_dictionary, None)

        def test_assertion_error_w_false(self):

  the test is still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``an_integer = 0`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 11-15

        def test_assertion_error_w_false(self):
            assert None is not False
            self.assertIsNot(None, False)

            assert False is False
            self.assertIs(False, False)

            assert True is not False
            self.assertIsNot(True, False)

            # an_integer = 0
            # assert an_integer is not False
            # self.assertIsNot(an_integer, False)
            assert self.an_integer is not False
            self.assertIsNot(self.an_integer, False)

            a_float = 0.0
            assert a_float is not False
            self.assertIsNot(a_float, False)

            a_string = 'a string'
            assert a_string is not False
            self.assertIsNot(a_string, False)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not False
            self.assertIsNot(a_tuple, False)

            a_list = [1, 2, 3, 'n']
            assert a_list is not False
            self.assertIsNot(a_list, False)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not False
            self.assertIsNot(a_set, False)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not False
            self.assertIsNot(a_dictionary, False)

        def test_assertion_error_w_true(self):

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``an_integer = 0`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 11-15

        def test_assertion_error_w_true(self):
            assert None is not True
            self.assertIsNot(None, True)

            assert False is not True
            self.assertIsNot(False, True)

            assert True is True
            self.assertIs(True, True)

            # an_integer = 0
            # assert an_integer is not True
            # self.assertIsNot(an_integer, True)
            assert self.an_integer is not True
            self.assertIsNot(self.an_integer, True)

            a_float = 0.0
            assert a_float is not True
            self.assertIsNot(a_float, True)

            a_string = 'a string'
            assert a_string is not True
            self.assertIsNot(a_string, True)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not True
            self.assertIsNot(a_tuple, True)

            a_list = [1, 2, 3, 'n']
            assert a_list is not True
            self.assertIsNot(a_list, True)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not True
            self.assertIsNot(a_set, True)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality(self):

  green.

----

* I add a :ref:`class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to use to remove repetition of ``a_float = 0.0``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

        def setUp(self):
            self.an_integer = 0
            self.a_float = 0.0

        def test_what_is_an_assertion(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_float = 0.0`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 17-21

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)

            assert False is not None
            self.assertIsNot(False, None)

            assert True is not None
            self.assertIsNot(True, None)

            # an_integer = 0
            # assert an_integer is not None
            # self.assertIsNot(an_integer, None)
            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)

            # a_float = 0.0
            # assert a_float is not None
            # self.assertIsNot(a_float, None)
            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)

            a_string = 'a string'
            assert a_string is not None
            self.assertIsNot(a_string, None)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not None
            self.assertIsNot(a_tuple, None)

            a_list = [1, 2, 3, 'n']
            assert a_list is not None
            self.assertIsNot(a_list, None)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not None
            self.assertIsNot(a_set, None)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not None
            self.assertIsNot(a_dictionary, None)

        def test_assertion_error_w_false(self):

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_float = 0.0`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 17-21

        def test_assertion_error_w_false(self):
            assert None is not False
            self.assertIsNot(None, False)

            assert False is False
            self.assertIs(False, False)

            assert True is not False
            self.assertIsNot(True, False)

            # an_integer = 0
            # assert an_integer is not False
            # self.assertIsNot(an_integer, False)
            assert self.an_integer is not False
            self.assertIsNot(self.an_integer, False)

            # a_float = 0.0
            # assert a_float is not False
            # self.assertIsNot(a_float, False)
            assert self.a_float is not False
            self.assertIsNot(self.a_float, False)

            a_string = 'a string'
            assert a_string is not False
            self.assertIsNot(a_string, False)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not False
            self.assertIsNot(a_tuple, False)

            a_list = [1, 2, 3, 'n']
            assert a_list is not False
            self.assertIsNot(a_list, False)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not False
            self.assertIsNot(a_set, False)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not False
            self.assertIsNot(a_dictionary, False)

        def test_assertion_error_w_true(self):

  the test is still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_float = 0.0`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 17-21

        def test_assertion_error_w_true(self):
            assert None is not True
            self.assertIsNot(None, True)

            assert False is not True
            self.assertIsNot(False, True)

            assert True is True
            self.assertIs(True, True)

            # an_integer = 0
            # assert an_integer is not True
            # self.assertIsNot(an_integer, True)
            assert self.an_integer is not True
            self.assertIsNot(self.an_integer, True)

            # a_float = 0.0
            # assert a_float is not True
            # self.assertIsNot(a_float, True)
            assert self.a_float is not True
            self.assertIsNot(self.a_float, True)

            a_string = 'a string'
            assert a_string is not True
            self.assertIsNot(a_string, True)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not True
            self.assertIsNot(a_tuple, True)

            a_list = [1, 2, 3, 'n']
            assert a_list is not True
            self.assertIsNot(a_list, True)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not True
            self.assertIsNot(a_set, True)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality(self):

  still green.

----

* I add a :ref:`class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to use to remove repetition of ``a_string = 'a string'``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def setUp(self):
            self.an_integer = 0
            self.a_float = 0.0
            self.a_string = 'a string'

        def test_what_is_an_assertion(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_string = 'a string'`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 23-27

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)

            assert False is not None
            self.assertIsNot(False, None)

            assert True is not None
            self.assertIsNot(True, None)

            # an_integer = 0
            # assert an_integer is not None
            # self.assertIsNot(an_integer, None)
            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)

            # a_float = 0.0
            # assert a_float is not None
            # self.assertIsNot(a_float, None)
            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)

            # a_string = 'a string'
            # assert a_string is not None
            # self.assertIsNot(a_string, None)
            assert self.a_string is not None
            self.assertIsNot(self.a_string, None)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not None
            self.assertIsNot(a_tuple, None)

            a_list = [1, 2, 3, 'n']
            assert a_list is not None
            self.assertIsNot(a_list, None)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not None
            self.assertIsNot(a_set, None)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not None
            self.assertIsNot(a_dictionary, None)

        def test_assertion_error_w_false(self):

  green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_string = 'a string'`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 23-27

        def test_assertion_error_w_false(self):
            assert None is not False
            self.assertIsNot(None, False)

            assert False is False
            self.assertIs(False, False)

            assert True is not False
            self.assertIsNot(True, False)

            # an_integer = 0
            # assert an_integer is not False
            # self.assertIsNot(an_integer, False)
            assert self.an_integer is not False
            self.assertIsNot(self.an_integer, False)

            # a_float = 0.0
            # assert a_float is not False
            # self.assertIsNot(a_float, False)
            assert self.a_float is not False
            self.assertIsNot(self.a_float, False)

            # a_string = 'a string'
            # assert a_string is not False
            # self.assertIsNot(a_string, False)
            assert self.a_string is not False
            self.assertIsNot(self.a_string, False)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not False
            self.assertIsNot(a_tuple, False)

            a_list = [1, 2, 3, 'n']
            assert a_list is not False
            self.assertIsNot(a_list, False)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not False
            self.assertIsNot(a_set, False)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not False
            self.assertIsNot(a_dictionary, False)

        def test_assertion_error_w_true(self):

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_string = 'a string'`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 23-27

        def test_assertion_error_w_true(self):
            assert None is not True
            self.assertIsNot(None, True)

            assert False is not True
            self.assertIsNot(False, True)

            assert True is True
            self.assertIs(True, True)

            # an_integer = 0
            # assert an_integer is not True
            # self.assertIsNot(an_integer, True)
            assert self.an_integer is not True
            self.assertIsNot(self.an_integer, True)

            # a_float = 0.0
            # assert a_float is not True
            # self.assertIsNot(a_float, True)
            assert self.a_float is not True
            self.assertIsNot(self.a_float, True)

            # a_string = 'a string'
            # assert a_string is not True
            # self.assertIsNot(a_string, True)
            assert self.a_string is not True
            self.assertIsNot(self.a_string, True)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not True
            self.assertIsNot(a_tuple, True)

            a_list = [1, 2, 3, 'n']
            assert a_list is not True
            self.assertIsNot(a_list, True)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not True
            self.assertIsNot(a_set, True)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality(self):

  the test is still green.

----

* I add a :ref:`class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to use to remove repetition of ``a_tuple = (1, 2, 3, 'n')``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5

        def setUp(self):
            self.an_integer = 0
            self.a_float = 0.0
            self.a_string = 'a string'
            self.a_tuple = (1, 2, 3, 'n')

        def test_what_is_an_assertion(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_tuple = (1, 2, 3, 'n')`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 29-33

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)

            assert False is not None
            self.assertIsNot(False, None)

            assert True is not None
            self.assertIsNot(True, None)

            # an_integer = 0
            # assert an_integer is not None
            # self.assertIsNot(an_integer, None)
            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)

            # a_float = 0.0
            # assert a_float is not None
            # self.assertIsNot(a_float, None)
            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)

            # a_string = 'a string'
            # assert a_string is not None
            # self.assertIsNot(a_string, None)
            assert self.a_string is not None
            self.assertIsNot(self.a_string, None)

            # a_tuple = (1, 2, 3, 'n')
            # assert a_tuple is not None
            # self.assertIsNot(a_tuple, None)
            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)

            a_list = [1, 2, 3, 'n']
            assert a_list is not None
            self.assertIsNot(a_list, None)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not None
            self.assertIsNot(a_set, None)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not None
            self.assertIsNot(a_dictionary, None)

        def test_assertion_error_w_false(self):

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_tuple = (1, 2, 3, 'n')`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 29-33

        def test_assertion_error_w_false(self):
            assert None is not False
            self.assertIsNot(None, False)

            assert False is False
            self.assertIs(False, False)

            assert True is not False
            self.assertIsNot(True, False)

            # an_integer = 0
            # assert an_integer is not False
            # self.assertIsNot(an_integer, False)
            assert self.an_integer is not False
            self.assertIsNot(self.an_integer, False)

            # a_float = 0.0
            # assert a_float is not False
            # self.assertIsNot(a_float, False)
            assert self.a_float is not False
            self.assertIsNot(self.a_float, False)

            # a_string = 'a string'
            # assert a_string is not False
            # self.assertIsNot(a_string, False)
            assert self.a_string is not False
            self.assertIsNot(self.a_string, False)

            # a_tuple = (1, 2, 3, 'n')
            # assert a_tuple is not False
            # self.assertIsNot(a_tuple, False)
            assert self.a_tuple is not False
            self.assertIsNot(self.a_tuple, False)

            a_list = [1, 2, 3, 'n']
            assert a_list is not False
            self.assertIsNot(a_list, False)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not False
            self.assertIsNot(a_set, False)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not False
            self.assertIsNot(a_dictionary, False)

        def test_assertion_error_w_true(self):

  green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_tuple = (1, 2, 3, 'n')`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 120
    :emphasize-lines: 29-33

        def test_assertion_error_w_true(self):
            assert None is not True
            self.assertIsNot(None, True)

            assert False is not True
            self.assertIsNot(False, True)

            assert True is True
            self.assertIs(True, True)

            # an_integer = 0
            # assert an_integer is not True
            # self.assertIsNot(an_integer, True)
            assert self.an_integer is not True
            self.assertIsNot(self.an_integer, True)

            # a_float = 0.0
            # assert a_float is not True
            # self.assertIsNot(a_float, True)
            assert self.a_float is not True
            self.assertIsNot(self.a_float, True)

            # a_string = 'a string'
            # assert a_string is not True
            # self.assertIsNot(a_string, True)
            assert self.a_string is not True
            self.assertIsNot(self.a_string, True)

            # a_tuple = (1, 2, 3, 'n')
            # assert a_tuple is not True
            # self.assertIsNot(a_tuple, True)
            assert self.a_tuple is not True
            self.assertIsNot(self.a_tuple, True)

            a_list = [1, 2, 3, 'n']
            assert a_list is not True
            self.assertIsNot(a_list, True)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not True
            self.assertIsNot(a_set, True)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality(self):

  still green.

----

* I add a :ref:`class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to use to remove repetition of ``a_list = [1, 2, 3, 'n']``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 6

        def setUp(self):
            self.an_integer = 0
            self.a_float = 0.0
            self.a_string = 'a string'
            self.a_tuple = (1, 2, 3, 'n')
            self.a_list = [1, 2, 3, 'n']

        def test_what_is_an_assertion(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_list = [1, 2, 3, 'n']`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 35-39

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)

            assert False is not None
            self.assertIsNot(False, None)

            assert True is not None
            self.assertIsNot(True, None)

            # an_integer = 0
            # assert an_integer is not None
            # self.assertIsNot(an_integer, None)
            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)

            # a_float = 0.0
            # assert a_float is not None
            # self.assertIsNot(a_float, None)
            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)

            # a_string = 'a string'
            # assert a_string is not None
            # self.assertIsNot(a_string, None)
            assert self.a_string is not None
            self.assertIsNot(self.a_string, None)

            # a_tuple = (1, 2, 3, 'n')
            # assert a_tuple is not None
            # self.assertIsNot(a_tuple, None)
            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)

            # a_list = [1, 2, 3, 'n']
            # assert a_list is not None
            # self.assertIsNot(a_list, None)
            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not None
            self.assertIsNot(a_set, None)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not None
            self.assertIsNot(a_dictionary, None)

        def test_assertion_error_w_false(self):

  the test is still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_list = [1, 2, 3, 'n']`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 35-39

        def test_assertion_error_w_false(self):
            assert None is not False
            self.assertIsNot(None, False)

            assert False is False
            self.assertIs(False, False)

            assert True is not False
            self.assertIsNot(True, False)

            # an_integer = 0
            # assert an_integer is not False
            # self.assertIsNot(an_integer, False)
            assert self.an_integer is not False
            self.assertIsNot(self.an_integer, False)

            # a_float = 0.0
            # assert a_float is not False
            # self.assertIsNot(a_float, False)
            assert self.a_float is not False
            self.assertIsNot(self.a_float, False)

            # a_string = 'a string'
            # assert a_string is not False
            # self.assertIsNot(a_string, False)
            assert self.a_string is not False
            self.assertIsNot(self.a_string, False)

            # a_tuple = (1, 2, 3, 'n')
            # assert a_tuple is not False
            # self.assertIsNot(a_tuple, False)
            assert self.a_tuple is not False
            self.assertIsNot(self.a_tuple, False)

            # a_list = [1, 2, 3, 'n']
            # assert a_list is not False
            # self.assertIsNot(a_list, False)
            assert self.a_list is not False
            self.assertIsNot(self.a_list, False)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not False
            self.assertIsNot(a_set, False)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not False
            self.assertIsNot(a_dictionary, False)

        def test_assertion_error_w_true(self):

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_list = [1, 2, 3, 'n']`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 125
    :emphasize-lines: 35-39

        def test_assertion_error_w_true(self):
            assert None is not True
            self.assertIsNot(None, True)

            assert False is not True
            self.assertIsNot(False, True)

            assert True is True
            self.assertIs(True, True)

            # an_integer = 0
            # assert an_integer is not True
            # self.assertIsNot(an_integer, True)
            assert self.an_integer is not True
            self.assertIsNot(self.an_integer, True)

            # a_float = 0.0
            # assert a_float is not True
            # self.assertIsNot(a_float, True)
            assert self.a_float is not True
            self.assertIsNot(self.a_float, True)

            # a_string = 'a string'
            # assert a_string is not True
            # self.assertIsNot(a_string, True)
            assert self.a_string is not True
            self.assertIsNot(self.a_string, True)

            # a_tuple = (1, 2, 3, 'n')
            # assert a_tuple is not True
            # self.assertIsNot(a_tuple, True)
            assert self.a_tuple is not True
            self.assertIsNot(self.a_tuple, True)

            # a_list = [1, 2, 3, 'n']
            # assert a_list is not True
            # self.assertIsNot(a_list, True)
            assert self.a_list is not True
            self.assertIsNot(self.a_list, True)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not True
            self.assertIsNot(a_set, True)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality(self):

  green.

----

* I add a :ref:`class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to use to remove repetition of ``a_set = {1, 2, 3, 'n'}``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 7

        def setUp(self):
            self.an_integer = 0
            self.a_float = 0.0
            self.a_string = 'a string'
            self.a_tuple = (1, 2, 3, 'n')
            self.a_list = [1, 2, 3, 'n']
            self.a_set = {1, 2, 3, 'n'}

        def test_what_is_an_assertion(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_set = {1, 2, 3, 'n'}`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 41-45

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)

            assert False is not None
            self.assertIsNot(False, None)

            assert True is not None
            self.assertIsNot(True, None)

            # an_integer = 0
            # assert an_integer is not None
            # self.assertIsNot(an_integer, None)
            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)

            # a_float = 0.0
            # assert a_float is not None
            # self.assertIsNot(a_float, None)
            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)

            # a_string = 'a string'
            # assert a_string is not None
            # self.assertIsNot(a_string, None)
            assert self.a_string is not None
            self.assertIsNot(self.a_string, None)

            # a_tuple = (1, 2, 3, 'n')
            # assert a_tuple is not None
            # self.assertIsNot(a_tuple, None)
            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)

            # a_list = [1, 2, 3, 'n']
            # assert a_list is not None
            # self.assertIsNot(a_list, None)
            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)

            # a_set = {1, 2, 3, 'n'}
            # assert a_set is not None
            # self.assertIsNot(a_set, None)
            assert self.a_set is not None
            self.assertIsNot(self.a_set, None)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not None
            self.assertIsNot(a_dictionary, None)

        def test_assertion_error_w_false(self):

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_set = {1, 2, 3, 'n'}`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 41-45

        def test_assertion_error_w_false(self):
            assert None is not False
            self.assertIsNot(None, False)

            assert False is False
            self.assertIs(False, False)

            assert True is not False
            self.assertIsNot(True, False)

            # an_integer = 0
            # assert an_integer is not False
            # self.assertIsNot(an_integer, False)
            assert self.an_integer is not False
            self.assertIsNot(self.an_integer, False)

            # a_float = 0.0
            # assert a_float is not False
            # self.assertIsNot(a_float, False)
            assert self.a_float is not False
            self.assertIsNot(self.a_float, False)

            # a_string = 'a string'
            # assert a_string is not False
            # self.assertIsNot(a_string, False)
            assert self.a_string is not False
            self.assertIsNot(self.a_string, False)

            # a_tuple = (1, 2, 3, 'n')
            # assert a_tuple is not False
            # self.assertIsNot(a_tuple, False)
            assert self.a_tuple is not False
            self.assertIsNot(self.a_tuple, False)

            # a_list = [1, 2, 3, 'n']
            # assert a_list is not False
            # self.assertIsNot(a_list, False)
            assert self.a_list is not False
            self.assertIsNot(self.a_list, False)

            # a_set = {1, 2, 3, 'n'}
            # assert a_set is not False
            # self.assertIsNot(a_set, False)
            assert self.a_set is not False
            self.assertIsNot(self.a_set, False)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not False
            self.assertIsNot(a_dictionary, False)

        def test_assertion_error_w_true(self):

  the test is still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_set = {1, 2, 3, 'n'}`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 130
    :emphasize-lines: 41-45

        def test_assertion_error_w_true(self):
            assert None is not True
            self.assertIsNot(None, True)

            assert False is not True
            self.assertIsNot(False, True)

            assert True is True
            self.assertIs(True, True)

            # an_integer = 0
            # assert an_integer is not True
            # self.assertIsNot(an_integer, True)
            assert self.an_integer is not True
            self.assertIsNot(self.an_integer, True)

            # a_float = 0.0
            # assert a_float is not True
            # self.assertIsNot(a_float, True)
            assert self.a_float is not True
            self.assertIsNot(self.a_float, True)

            # a_string = 'a string'
            # assert a_string is not True
            # self.assertIsNot(a_string, True)
            assert self.a_string is not True
            self.assertIsNot(self.a_string, True)

            # a_tuple = (1, 2, 3, 'n')
            # assert a_tuple is not True
            # self.assertIsNot(a_tuple, True)
            assert self.a_tuple is not True
            self.assertIsNot(self.a_tuple, True)

            # a_list = [1, 2, 3, 'n']
            # assert a_list is not True
            # self.assertIsNot(a_list, True)
            assert self.a_list is not True
            self.assertIsNot(self.a_list, True)

            # a_set = {1, 2, 3, 'n'}
            # assert a_set is not True
            # self.assertIsNot(a_set, True)
            assert self.a_set is not True
            self.assertIsNot(self.a_set, True)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality(self):

  still green.

----

* I add a :ref:`class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to use to remove repetition of ``a_dictionary = {'key': 'value'}``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 8

        def setUp(self):
            self.an_integer = 0
            self.a_float = 0.0
            self.a_string = 'a string'
            self.a_tuple = (1, 2, 3, 'n')
            self.a_list = [1, 2, 3, 'n']
            self.a_set = {1, 2, 3, 'n'}
            self.a_dictionary = {'key': 'value'}

        def test_what_is_an_assertion(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_dictionary = {'key': 'value'}`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 47-51

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)

            assert False is not None
            self.assertIsNot(False, None)

            assert True is not None
            self.assertIsNot(True, None)

            # an_integer = 0
            # assert an_integer is not None
            # self.assertIsNot(an_integer, None)
            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)

            # a_float = 0.0
            # assert a_float is not None
            # self.assertIsNot(a_float, None)
            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)

            # a_string = 'a string'
            # assert a_string is not None
            # self.assertIsNot(a_string, None)
            assert self.a_string is not None
            self.assertIsNot(self.a_string, None)

            # a_tuple = (1, 2, 3, 'n')
            # assert a_tuple is not None
            # self.assertIsNot(a_tuple, None)
            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)

            # a_list = [1, 2, 3, 'n']
            # assert a_list is not None
            # self.assertIsNot(a_list, None)
            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)

            # a_set = {1, 2, 3, 'n'}
            # assert a_set is not None
            # self.assertIsNot(a_set, None)
            assert self.a_set is not None
            self.assertIsNot(self.a_set, None)

            # a_dictionary = {'key': 'value'}
            # assert a_dictionary is not None
            # self.assertIsNot(a_dictionary, None)
            assert self.a_dictionary is not None
            self.assertIsNot(self.a_dictionary, None)

        def test_assertion_error_w_false(self):

  the test is still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_dictionary = {'key': 'value'}`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 47-51

        def test_assertion_error_w_false(self):
            assert None is not False
            self.assertIsNot(None, False)

            assert False is False
            self.assertIs(False, False)

            assert True is not False
            self.assertIsNot(True, False)

            # an_integer = 0
            # assert an_integer is not False
            # self.assertIsNot(an_integer, False)
            assert self.an_integer is not False
            self.assertIsNot(self.an_integer, False)

            # a_float = 0.0
            # assert a_float is not False
            # self.assertIsNot(a_float, False)
            assert self.a_float is not False
            self.assertIsNot(self.a_float, False)

            # a_string = 'a string'
            # assert a_string is not False
            # self.assertIsNot(a_string, False)
            assert self.a_string is not False
            self.assertIsNot(self.a_string, False)

            # a_tuple = (1, 2, 3, 'n')
            # assert a_tuple is not False
            # self.assertIsNot(a_tuple, False)
            assert self.a_tuple is not False
            self.assertIsNot(self.a_tuple, False)

            # a_list = [1, 2, 3, 'n']
            # assert a_list is not False
            # self.assertIsNot(a_list, False)
            assert self.a_list is not False
            self.assertIsNot(self.a_list, False)

            # a_set = {1, 2, 3, 'n'}
            # assert a_set is not False
            # self.assertIsNot(a_set, False)
            assert self.a_set is not False
            self.assertIsNot(self.a_set, False)

            # a_dictionary = {'key': 'value'}
            # assert a_dictionary is not False
            # self.assertIsNot(a_dictionary, False)
            assert self.a_dictionary is not False
            self.assertIsNot(self.a_dictionary, False)

        def test_assertion_error_w_true(self):

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_dictionary = {'key': 'value'}`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 47-51

        def test_assertion_error_w_true(self):
            assert None is not True
            self.assertIsNot(None, True)

            assert False is not True
            self.assertIsNot(False, True)

            assert True is True
            self.assertIs(True, True)

            # an_integer = 0
            # assert an_integer is not True
            # self.assertIsNot(an_integer, True)
            assert self.an_integer is not True
            self.assertIsNot(self.an_integer, True)

            # a_float = 0.0
            # assert a_float is not True
            # self.assertIsNot(a_float, True)
            assert self.a_float is not True
            self.assertIsNot(self.a_float, True)

            # a_string = 'a string'
            # assert a_string is not True
            # self.assertIsNot(a_string, True)
            assert self.a_string is not True
            self.assertIsNot(self.a_string, True)

            # a_tuple = (1, 2, 3, 'n')
            # assert a_tuple is not True
            # self.assertIsNot(a_tuple, True)
            assert self.a_tuple is not True
            self.assertIsNot(self.a_tuple, True)

            # a_list = [1, 2, 3, 'n']
            # assert a_list is not True
            # self.assertIsNot(a_list, True)
            assert self.a_list is not True
            self.assertIsNot(self.a_list, True)

            # a_set = {1, 2, 3, 'n'}
            # assert a_set is not True
            # self.assertIsNot(a_set, True)
            assert self.a_set is not True
            self.assertIsNot(self.a_set, True)

            # a_dictionary = {'key': 'value'}
            # assert a_dictionary is not True
            # self.assertIsNot(a_dictionary, True)
            assert self.a_dictionary is not True
            self.assertIsNot(self.a_dictionary, True)

        def test_assertion_error_w_equality(self):

  green.

----

* I remove the commented lines from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 135

        def test_assertion_error_w_true(self):
            assert None is not True
            self.assertIsNot(None, True)

            assert False is not True
            self.assertIsNot(False, True)

            assert True is True
            self.assertIs(True, True)

            assert self.an_integer is not True
            self.assertIsNot(self.an_integer, True)

            assert self.a_float is not True
            self.assertIsNot(self.a_float, True)

            assert self.a_string is not True
            self.assertIsNot(self.a_string, True)

            assert self.a_tuple is not True
            self.assertIsNot(self.a_tuple, True)

            assert self.a_list is not True
            self.assertIsNot(self.a_list, True)

            assert self.a_set is not True
            self.assertIsNot(self.a_set, True)

            assert self.a_dictionary is not True
            self.assertIsNot(self.a_dictionary, True)

        def test_assertion_error_w_equality(self):

* I remove the commented lines from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 83

        def test_assertion_error_w_false(self):
            assert None is not False
            self.assertIsNot(None, False)

            assert False is False
            self.assertIs(False, False)

            assert True is not False
            self.assertIsNot(True, False)

            assert self.an_integer is not False
            self.assertIsNot(self.an_integer, False)

            assert self.a_float is not False
            self.assertIsNot(self.a_float, False)

            assert self.a_string is not False
            self.assertIsNot(self.a_string, False)

            assert self.a_tuple is not False
            self.assertIsNot(self.a_tuple, False)

            assert self.a_list is not False
            self.assertIsNot(self.a_list, False)

            assert self.a_set is not False
            self.assertIsNot(self.a_set, False)

            assert self.a_dictionary is not False
            self.assertIsNot(self.a_dictionary, False)

        def test_assertion_error_w_true(self):

* I remove the commented lines from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 31

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)

            assert False is not None
            self.assertIsNot(False, None)

            assert True is not None
            self.assertIsNot(True, None)

            assert self.an_integer is not None
            self.assertIsNot(self.an_integer, None)

            assert self.a_float is not None
            self.assertIsNot(self.a_float, None)

            assert self.a_string is not None
            self.assertIsNot(self.a_string, None)

            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)

            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)

            assert self.a_set is not None
            self.assertIsNot(self.a_set, None)

            assert self.a_dictionary is not None
            self.assertIsNot(self.a_dictionary, None)

        def test_assertion_error_w_false(self):

----

* In this case, I do not need the :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` because the :ref:`class attributes<what is a class attribute?>` are the same for every test and I do not need anything to run before each test. I move them out

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-9

    class TestAssertionError(unittest.TestCase):

        self.an_integer = 0
        self.a_float = 0.0
        self.a_string = 'a string'
        self.a_tuple = (1, 2, 3, 'n')
        self.a_list = [1, 2, 3, 'n']
        self.a_set = {1, 2, 3, 'n'}
        self.a_dictionary = {'key': 'value'}

        # def setUp(self):
        #    self.an_integer = 0
        #    self.a_float = 0.0
        #    self.a_string = 'a string'
        #    self.a_tuple = (1, 2, 3, 'n')
        #    self.a_list = [1, 2, 3, 'n']
        #    self.a_set = {1, 2, 3, 'n'}
        #    self.a_dictionary = {'key': 'value'}

        def test_what_is_an_assertion(self):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

  because ``self`` is not defined outside the :ref:`methods<what is a method?>` I can declare the :ref:`class attributes<what is a class attribute?>` the same way I do :ref:`variables<what is a variable?>` as long as it is indented under the :ref:`class definition<how to make a class>`

* I add :ref:`NameError<test_catching_name_error>` to the list of :ref:`Exceptions<errors>`

  .. code-block:: python
    :lineno-start: 200
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

* I remove ``self.``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-9, 11-17

    class TestAssertionError(unittest.TestCase):

        # self.an_integer = 0
        # self.a_float = 0.0
        # self.a_string = 'a string'
        # self.a_tuple = (1, 2, 3, 'n')
        # self.a_list = [1, 2, 3, 'n']
        # self.a_set = {1, 2, 3, 'n'}
        # self.a_dictionary = {'key': 'value'}

        an_integer = 0
        a_float = 0.0
        a_string = 'a string'
        a_tuple = (1, 2, 3, 'n')
        a_list = [1, 2, 3, 'n']
        a_set = {1, 2, 3, 'n'}
        a_dictionary = {'key': 'value'}

        # def setUp(self):
        #     self.an_integer = 0
        #     self.a_float = 0.0
        #     self.a_string = 'a string'
        #     self.a_tuple = (1, 2, 3, 'n')
        #     self.a_list = [1, 2, 3, 'n']
        #     self.a_set = {1, 2, 3, 'n'}
        #     self.a_dictionary = {'key': 'value'}

        def test_what_is_an_assertion(self):

  the test is green again.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 4

    class TestAssertionError(unittest.TestCase):

        an_integer = 0
        a_float = 0.0
        a_string = 'a string'
        a_tuple = (1, 2, 3, 'n')
        a_list = [1, 2, 3, 'n']
        a_set = {1, 2, 3, 'n'}
        a_dictionary = {'key': 'value'}

        def test_what_is_an_assertion(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract class attributes'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use class attributes to remove repetition<remove repetition with class attributes>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_assertion_error.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ where the tests are running, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

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