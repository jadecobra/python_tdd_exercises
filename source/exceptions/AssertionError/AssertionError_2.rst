.. meta::
  :description: Part 2 of the beginner Python TDD AssertionError tutorial: learn to use the unittest.TestCase setUp method to DRY up repeated variable initialization across test methods. Refactor the tests from part 1 (None, True, False, is vs ==, 0 vs 0.0 identity vs equality) by moving an_integer = 0 and a_float = 0.0 into def setUp(self): so self.an_integer and self.a_float are freshly set for every test without duplicating the lines in test_assertion_error_w_none, w_false, w_true etc. See before/after with commented old local variables, updating asserts to use self.xxx, adding setUp to the class, and running the evolved tests with pytest-watcher in the existing uv project. Teaches how setUp provides per-test isolation for instance attributes, reducing repetition while keeping tests focused on the assertions. Continues the red-green-refactor cycle and same core examples from the first AssertionError chapter.
  :keywords: Jacob Itegboje, Pumping Python, unittest setUp method, setUp python unittest example, python TestCase setUp, refactor tests with setUp, DRY unittest tests setUp, self. in setUp unittest, remove repetition setUp python, an_integer setUp, a_float setUp, AssertionError 2, setUp for None tests, setUp True False tests, unittest setUp beginners, setUp vs local variables in tests, per test setup python unittest, AssertionError setUp method, continuing TDD project setUp, python unittest DRY test data, setUp instance variables, test_assertion_error_2.py

.. include:: ../../links.rst

#################################################################################
AssertionError 2: use the setUp method
#################################################################################

----

I used the :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` in :ref:`classes` to remove repetition of :ref:`variables<what is a variable?>` by making them :ref:`class attributes<what is a class attribute?>` that the test :ref:`methods<what is a method?>` could all use.

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

* I add the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to the ``TestAssertionError`` :ref:`class<what is a class?>` with :ref:`a class attribute<what is a class attribute?>` to use to remove repetition of ``an_integer = 0``

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

* I add a :ref:`a class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to use to remove repetition of ``a_float = 0.0``

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

* I add a :ref:`a class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to use to remove repetition of ``a_string = 'a string'``

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

  still green.

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

  the test is still green.

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

  still green.

----

* I add a :ref:`a class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to use to remove repetition of ``a_tuple = (1, 2, 3, 'n')``

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

  green.

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

  still green.

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

  the test is still green.

----

* I add a :ref:`a class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to use to remove repetition of ``a_list = [1, 2, 3, 'n']``

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

  green.

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

  the test is still green.

----

* I add a :ref:`a class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to use to remove repetition of ``a_set = {1, 2, 3, 'n'}``

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

  green.

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

  still green.

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

  the test is still green.

----

* I add a :ref:`a class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>` to use to remove repetition of ``a_set = {1, 2, 3, 'n'}``

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

  green.

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

  still green.

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

  the test is still green.

----



* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_assertion_error_w_is_vs_equal'

  the terminal_ shows a summary of the changes then goes back to the command line.q

The tests show that an integer_ can be ``EQUAL`` to a float_ but an integer_ ``IS`` NOT a float_.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``assertion_error.py`` in the :ref:`editor<2 editors>`
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

I can use `assert statements`_ and `assert methods`_ to test if something is

* :ref:`NOT None<test_assertion_error_w_none>`
* :ref:`None<test_assertion_error_w_none>`
* :ref:`False or NOT False<test_assertion_error_w_none>`
* :ref:`True or NOT True<test_assertion_error_w_none>`

and to test if 2 things are

* :ref:`NOT Equal<test_assertion_error_w_equality>` with assertNotEqual_
* :ref:`Equal<test_assertion_error_w_equality>` with assertEqual_

The tests show that

* :ref:`True<test_what_is_true>`, :ref:`False<test_what_is_false>` and :ref:`None<what is None?>` are different
* ``is`` and ``Equal`` are different

:ref:`How many questions can you answer about AssertionError?<questions about AssertionError>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<AssertionError: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

Congratulations! You now know

* :ref:`how to make a Python test driven development environment any time you want<how to make a Python test driven development environment>` and
* :ref:`what causes AssertionError?`

:ref:`Would you like to test functions?<what is a function?>`

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