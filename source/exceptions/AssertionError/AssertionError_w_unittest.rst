.. meta::
  :description: Pumping Python TDD continuation: "test AssertionError with unittest" in the assertion_error project. Move the existing test_* functions into TestAssertionError(unittest.TestCase), add self as the first method argument, and pair each helper/bare assert with unittest methods (assertEqual, assertNotEqual, assertIs, assertIsNot). See the unittest cores this chapter actually quotes: "AssertionError: True != False", "2 == 2", "'11' == '11'", "unexpectedly identical: None", "False is not None", "0 is not 0.0", "0 == 0.0", plus TypeError when a method is defined without self. Then extract repeated locals (an_integer=0, a_float=0.0, a_string, tuple, list, set, dict) into class attributes used as self.an_integer across test_assertion_error_w_none/false/true — no setUp. will_not_run stays skipped until renamed test_will_not_run. uv run pytest-watcher . --now, git commit after each move, remove the commented lines. Builds on the functions chapter (7 passed at open).
  :keywords: Jacob Itegboje, Pumping Python, test AssertionError with unittest, TestAssertionError, unittest.TestCase, another way to write tests, assertEqual, assertNotEqual, assertIs, assertIsNot, self first argument, TypeError takes 0 positional arguments but 1 was given, AssertionError True != False, unexpectedly identical None, AssertionError 2 == 2, False is not None, 0 is not 0.0, 0 == 0.0, class attributes an_integer a_float, will_not_run, test_ prefix, test_assert_keyword, test_assertion_error_w_none, test_assertion_error_w_is_vs_equal, uv run pytest-watcher . --now, red green refactor, remove the commented lines, python TDD unittest beginner, identity vs equality 0 vs 0.0

.. include:: ../../links.rst

#################################################################################
test AssertionError with unittest
#################################################################################

----

I want to use the :ref:`unittest library<another way to write tests>` in the :ref:`assertion_error<what is an assertion?>` project.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_unittest.py
  :caption: assertion_error/tests/test_assertion_error.py
  :language: python
  :lineno-start: 28
  :lines: 28-36

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_unittest.py
  :caption: assertion_error/tests/test_assertion_error.py
  :language: python
  :lineno-start: 38
  :lines: 38-52

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_unittest.py
  :caption: assertion_error/tests/test_assertion_error.py
  :language: python
  :lineno-start: 54
  :lines: 54-83

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_unittest.py
  :caption: assertion_error/tests/test_assertion_error.py
  :language: python
  :lineno-start: 85
  :lines: 85-114

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_unittest.py
  :caption: assertion_error/tests/test_assertion_error.py
  :language: python
  :lineno-start: 116
  :lines: 116-145

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_unittest.py
  :caption: assertion_error/tests/test_assertion_error.py
  :language: python
  :lineno-start: 147
  :lines: 147-164

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_unittest.py
  :caption: assertion_error/tests/test_assertion_error.py
  :language: python
  :lineno-start: 166
  :lines: 166-171

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_unittest.py
  :caption: assertion_error/tests/test_assertion_error.py
  :language: python
  :lineno-start: 173
  :lines: 173-184

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_unittest.py
  :caption: assertion_error/tests/test_assertion_error.py
  :language: python
  :lineno-start: 220
  :lines: 220-

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`assertion_error folder<what is an assertion?>` in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

* I open ``test_assertion_error.py`` from the ``tests`` folder_

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows

  .. code-block:: shell

    tests/test_assertion_error.py .......             [100%]

    ================== 7 passed in A.BCs ===================

----

*********************************************************************************
add TestAssertionError class
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a :ref:`class<everything is an object>` named ``AssertionError`` with a :ref:`method<what is a method?>` for the :ref:`first failing test<test_failure>` to ``test_assertion_error.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5, 7-8

    def assert_equal(x, y):
        assert x == y


    class AssertionError(object):

        def test_failure(self):
            self.assertEqual(True, False)


    def test_assert_keyword():

  the test is still green.

* I change the name of the :ref:`class<everything is an object>` to ``TestAssertionError``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-6

    def assert_equal(x, y):
        assert x == y


    # class AssertionError(object):
    class TestAssertionError(object):

        def test_failure(self):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'TestAssertionError' object
                    has no attribute 'assertEqual'

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<how to test that an Exception is raised>` seen

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 7
    :emphasize-text: AttributeError

    # None is None and equal to None


    # Exceptions seen
    # AssertionError
    # IndentationError
    # AttributeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`unittest.TestCase<test_dir_unittest_testcase>` as the parent :ref:`class<everything is an object>` of ``TestAssertionError``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 6-7

    def assert_equal(x, y):
        assert x == y


    # class AssertionError(object):
    # class TestAssertionError(object):
    class TestAssertionError(unittest.TestCase):

        def test_failure(self):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell

    NameError: name 'unittest' is not defined.
               Did you forget to import 'unittest'?

* I add :ref:`NameError<test_catching_name_error>` to the list of :ref:`Exceptions<how to test that an Exception is raised>` seen

  .. code-block:: python
    :lineno-start: 146
    :emphasize-lines: 5
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # IndentationError
    # AttributeError
    # NameError

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import unittest


    def assert_is_not(x, y):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

* I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the :ref:`assertion<what is an assertion?>` in :ref:`test_failure` in the :ref:`TestAssertionError class<add TestAssertionError class>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 6-7

    # class AssertionError(object):
    # class TestAssertionError(object):
    class TestAssertionError(unittest.TestCase):

        def test_failure(self):
            # self.assertEqual(True, False)
            self.assertEqual(True, True)


    def test_assert_keyword():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`TestAssertionError<add TestAssertionError class>`

  .. code-block:: python
    :lineno-start: 24

    def assert_equal(x, y):
        assert x == y


    class TestAssertionError(unittest.TestCase):

        def test_failure(self):
            self.assertEqual(True, True)


    def test_assert_keyword():

* I open a new terminal_ then make sure I am in the ``assertion_error`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add TestAssertionError class'

----

*********************************************************************************
test_assert_keyword with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I remove :ref:`test_failure`

* I move :ref:`test_assert_keyword` to make it a :ref:`method<what is a method?>` of the :ref:`TestAssertionError class<add TestAssertionError class>` and replace ``test_failure``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 3-6

    class TestAssertionError(unittest.TestCase):

        def test_assert_keyword():
            assert_equal(1+1, 2)
            assert_equal('1'+'1', '11')
            assert_equal('I am'+' alive', 'I am alive')


    def test_assertion_error_w_none():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestAssertionError.test_assert_keyword()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<how to test that an Exception is raised>` seen

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 6
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # IndentationError
    # AttributeError
    # NameError
    # TypeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_assert_keyword`

.. code-block:: python
  :lineno-start: 28
  :emphasize-lines: 3-4

  class TestAssertionError(unittest.TestCase):

      # def test_assert_keyword():
      def test_assert_keyword(self):
          assert_equal(1+1, 2)

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the three :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 4, 7, 10

        # def test_assert_keyword():
        def test_assert_keyword(self):
            assert_equal(1+1, 2)
            self.assertNotEqual(1+1, 2)

            assert_equal('1'+'1', '11')
            self.assertNotEqual('1'+'1', '11')

            assert_equal('I am'+' alive', 'I am alive')
            self.assertNotEqual('I am'+' alive', 'I am alive')


    def test_assertion_error_w_none():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 2 == 2

  compare this with the error message for ``assert 1 + 1 == 11``

  .. code-block:: python

    E   assert (1 + 1) == 11

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for ``(1+1, 2)``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4-5

        # def test_assert_keyword():
        def test_assert_keyword(self):
            assert_equal(1+1, 2)
            # self.assertNotEqual(1+1, 2)
            self.assertEqual(1+1, 2)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '11' == '11'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for ``('1'+'1', '11')``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 8-9

        # def test_assert_keyword():
        def test_assert_keyword(self):
            assert_equal(1+1, 2)
            # self.assertNotEqual(1+1, 2)
            self.assertEqual(1+1, 2)

            assert_equal('1'+'1', '11')
            # self.assertNotEqual('1'+'1', '11')
            self.assertEqual('1'+'1', '11')

            assert_equal('I am'+' alive', 'I am alive')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I am alive' == 'I am alive'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for ``('I am'+' alive', 'I am alive')``

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 2-3

            assert_equal('I am'+' alive', 'I am alive')
            # self.assertNotEqual('I am'+' alive', 'I am alive')
            self.assertEqual('I am'+' alive', 'I am alive')


    def test_assertion_error_w_none():

  the test passes.

----

* I add :ref:`variables<what is a variable?>` for ``'I am' + ' alive'`` and ``'I am alive'``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 3-4

            self.assertEqual('1'+'1', '11')

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert_equal('I am'+' alive', 'I am alive')
            # self.assertNotEqual('I am'+' alive', 'I am alive')
            self.assertEqual('I am'+' alive', 'I am alive')


    def test_assertion_error_w_none():

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``'I am' + ' alive'`` and ``'I am alive'``

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 3-4, 6-7

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            # assert_equal('I am'+' alive', 'I am alive')
            assert_equal(reality, my_expectation)
            # self.assertNotEqual('I am'+' alive', 'I am alive')
            # self.assertEqual('I am'+' alive', 'I am alive')
            self.assertEqual(reality, my_expectation)


    def test_assertion_error_w_none():

  the test is still green.

* I add :ref:`variables<what is a variable?>` for ``'1' + '1'`` and ``'11'``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 7-8

        # def test_assert_keyword():
        def test_assert_keyword(self):
            assert_equal(1+1, 2)
            # self.assertNotEqual(1+1, 2)
            self.assertEqual(1+1, 2)

            reality = '1' + '1'
            my_expectation = '11'
            assert_equal('1'+'1', '11')
            # self.assertNotEqual('1'+'1', '11')
            self.assertEqual('1'+'1', '11')

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``'1' + '1'`` and ``'11'``

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 3-4, 6-7

            reality = '1' + '1'
            my_expectation = '11'
            # assert_equal('1'+'1', '11')
            assert_equal(reality, my_expectation)
            # self.assertNotEqual('1'+'1', '11')
            # self.assertEqual('1'+'1', '11')
            self.assertEqual(reality, my_expectation)

            reality = 'I am' + ' alive'

  still green.

* I add :ref:`variables<what is a variable?>` for ``1 + 1`` and ``2``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 3-4

        # def test_assert_keyword():
        def test_assert_keyword(self):
            reality = 1 + 1
            my_expectation = 2
            assert_equal(1+1, 2)
            # self.assertNotEqual(1+1, 2)
            self.assertEqual(1+1, 2)

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``1 + 1`` and ``2``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 5-6, 8-9

        # def test_assert_keyword():
        def test_assert_keyword(self):
            reality = 1 + 1
            my_expectation = 2
            # assert_equal(1+1, 2)
            assert_equal(reality, my_expectation)
            # self.assertNotEqual(1+1, 2)
            # self.assertEqual(1+1, 2)
            self.assertEqual(reality, my_expectation)

            reality = '1' + '1'

  green.

* I remove the commented lines from :ref:`test_assert_keyword`

  .. code-block:: python
    :lineno-start: 28

    class TestAssertionError(unittest.TestCase):

        def test_assert_keyword(self):
            reality = 1 + 1
            my_expectation = 2
            assert_equal(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = '1' + '1'
            my_expectation = '11'
            assert_equal(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert_equal(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_assertion_error_w_none():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_assert_keyword to TestAssertionError'

----

*********************************************************************************
test_assertion_error_w_none with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_assertion_error_w_none` to make it a :ref:`method<what is a method?>` of :ref:`TestAssertionError<add TestAssertionError class>`

  .. caution:: Indentation matters in Python_. It is how it knows what blocks belong to what :ref:`function/method<what is a function?>`, :ref:`class<everything is an object>` or :ref:`module<what is a module?>` (Use 4 spaces)

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 6-7, 9-17

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert_equal(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

        def test_assertion_error_w_none():
            assert None is None

            assert_is_not_none(False)
            assert_is_not_none(True)
            assert_is_not_none(0)
            assert_is_not_none(0.0)
            assert_is_not_none('')
            assert_is_not_none(())
            assert_is_not_none([])
            assert_is_not_none(set())
            assert_is_not_none({})


    def test_assertion_error_w_false():


  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestAssertionError.test_assertion_error_w_none()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_assertion_error_w_none`

.. code-block:: python
  :lineno-start: 41
  :emphasize-lines: 6-7

          reality = 'I am' + ' alive'
          my_expectation = 'I am alive'
          assert_equal(reality, my_expectation)
          self.assertEqual(reality, my_expectation)

      # def test_assertion_error_w_none():
      def test_assertion_error_w_none(self):
          assert None is None

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertIsNot<test_assert_is_not>` and :ref:`assertIs methods<test_assert_is>` for the :ref:`assertions<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4, 7, 10

        # def test_assertion_error_w_none():
        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNot(None, None)

            assert_is_not_none(False)
            self.assertIs(False, None)

            assert_is_not_none(True)
            self.assertIs(True, None)

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 2, 5, 8, 11

            assert_is_not_none(0)
            self.assertIs(0, None)

            assert_is_not_none(0.0)
            self.assertIs(0.0, None)

            assert_is_not_none('')
            self.assertIs('', None)

            assert_is_not_none(())
            self.assertIs((), None)

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2, 5, 8

            assert_is_not_none([])
            self.assertIs([], None)

            assert_is_not_none(set())
            self.assertIs(set(), None)

            assert_is_not_none({})
            self.assertIs({}, None)


    def test_assertion_error_w_false():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: None

  compare this with the error message for ``assert None is not None``

  .. code-block:: python

    E       assert None is not None

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>` for ``(None, None)``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4-5

        # def test_assertion_error_w_none():
        def test_assertion_error_w_none(self):
            assert None is None
            # self.assertIsNot(None, None)
            self.assertIs(None, None)

            assert_is_not_none(False)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not None

  compare this with the error message for ``assert False is None``

  .. code-block:: python

    E    assert False is None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(False, None)``

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2-3

            assert_is_not_none(False)
            # self.assertIs(False, None)
            self.assertIsNot(False, None)

            assert_is_not_none(True)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not None

  compare this with the error message for ``assert True is None``

  .. code-block:: python

    E    assert True is None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(True, None)``

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 2-3

            assert_is_not_none(True)
            # self.assertIs(True, None)
            self.assertIsNot(True, None)

            assert_is_not_none(0)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(0, None)``

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2-3

            assert_is_not_none(0)
            # self.assertIs(0, None)
            self.assertIsNot(0, None)

            assert_is_not_none(0.0)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.0 is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(0.0, None)``

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 2-3

            assert_is_not_none(0.0)
            # self.assertIs(0.0, None)
            self.assertIsNot(0.0, None)

            assert_is_not_none('')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '' is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``('', None)``

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 2-3

            assert_is_not_none('')
            # self.assertIs('', None)
            self.assertIsNot('', None)

            assert_is_not_none(())

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: () is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``((), None)``

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 2-3

            assert_is_not_none(())
            # self.assertIs((), None)
            self.assertIsNot((), None)

            assert_is_not_none([])

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: [] is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``([], None)``

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 2-3

            assert_is_not_none([])
            # self.assertIs([], None)
            self.assertIsNot([], None)

            assert_is_not_none(set())

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: set() is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(set(), None)``

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 2-3

            assert_is_not_none(set())
            # self.assertIs(set(), None)
            self.assertIsNot(set(), None)

            assert_is_not_none({})

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {} is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``({}, None)``

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2-3

            assert_is_not_none({})
            # self.assertIs({}, None)
            self.assertIsNot({}, None)


    def test_assertion_error_w_false():

  the test passes.

----

* I add a :ref:`variable<what is a variable?>` for ``{}``

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 5

            assert_is_not_none(set())
            # self.assertIs(set(), None)
            self.assertIsNot(set(), None)

            a_dictionary = {}
            assert_is_not_none({})
            # self.assertIs({}, None)
            self.assertIsNot({}, None)


    def test_assertion_error_w_false():

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{}``

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2-3, 5-6

            a_dictionary = {}
            # assert_is_not_none({})
            assert_is_not_none(a_dictionary)
            # self.assertIs({}, None)
            # self.assertIsNot({}, None)
            self.assertIsNot(a_dictionary, None)


    def test_assertion_error_w_false():

  the test is still green.

* I add a :ref:`variable<what is a variable?>` for ``set()``

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 5

            assert_is_not_none([])
            # self.assertIs([], None)
            self.assertIsNot([], None)

            a_set = set()
            assert_is_not_none(set())
            # self.assertIs(set(), None)
            self.assertIsNot(set(), None)

            a_dictionary = {}

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``set()``

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 2-3, 5-6

            a_set = set()
            # assert_is_not_none(set())
            assert_is_not_none(a_set)
            # self.assertIs(set(), None)
            # self.assertIsNot(set(), None)
            self.assertIsNot(a_set, None)

            a_dictionary = {}

  still green.

* I add a :ref:`variable<what is a variable?>` for ``[]``

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 5

            assert_is_not_none(())
            # self.assertIs((), None)
            self.assertIsNot((), None)

            a_list = []
            assert_is_not_none([])
            # self.assertIs([], None)
            self.assertIsNot([], None)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``[]``

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 2-3, 5-6

            a_list = []
            # assert_is_not_none([])
            assert_is_not_none(a_list)
            # self.assertIs([], None)
            # self.assertIsNot([], None)
            self.assertIsNot(a_list, None)

            a_set = set()

  green.

* I add a :ref:`variable<what is a variable?>` for ``()``

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 5

            assert_is_not_none('')
            # self.assertIs('', None)
            self.assertIsNot('', None)

            a_tuple = ()
            assert_is_not_none(())
            # self.assertIs((), None)
            self.assertIsNot((), None)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``()``

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 2-3, 5-6

            a_tuple = ()
            # assert_is_not_none(())
            assert_is_not_none(a_tuple)
            # self.assertIs((), None)
            # self.assertIsNot((), None)
            self.assertIsNot(a_tuple, None)

            a_list = []

  still green.

* I add a :ref:`variable<what is a variable?>` for ``''``

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 5

            assert_is_not_none(0.0)
            # self.assertIs(0.0, None)
            self.assertIsNot(0.0, None)

            a_string = ''
            assert_is_not_none('')
            # self.assertIs('', None)
            self.assertIsNot('', None)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``''``

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 2-3, 5-6

            a_string = ''
            # assert_is_not_none('')
            assert_is_not_none(a_string)
            # self.assertIs('', None)
            # self.assertIsNot('', None)
            self.assertIsNot(a_string, None)

            a_tuple = ()

  the test is still green.

* I add a :ref:`variable<what is a variable?>` for ``0.0``

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 5

            assert_is_not_none(0)
            # self.assertIs(0, None)
            self.assertIsNot(0, None)

            a_float = 0.0
            assert_is_not_none(0.0)
            # self.assertIs(0.0, None)
            self.assertIsNot(0.0, None)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0.0``

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 2-3, 5-6

            a_float = 0.0
            # assert_is_not_none(0.0)
            assert_is_not_none(a_float)
            # self.assertIs(0.0, None)
            # self.assertIsNot(0.0, None)
            self.assertIsNot(a_float, None)

            a_string = ''

  still green.

* I add a :ref:`variable<what is a variable?>` for ``0``

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 5

            assert_is_not_none(True)
            # self.assertIs(True, None)
            self.assertIsNot(True, None)

            an_integer = 0
            assert_is_not_none(0)
            # self.assertIs(0, None)
            self.assertIsNot(0, None)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0``

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2-3, 5-6

            an_integer = 0
            # assert_is_not_none(0)
            assert_is_not_none(an_integer)
            # self.assertIs(0, None)
            # self.assertIsNot(0, None)
            self.assertIsNot(an_integer, None)

            a_float = 0.0

  green.

* I remove the commented lines from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 41

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert_equal(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)

            assert_is_not_none(False)
            self.assertIsNot(False, None)

            assert_is_not_none(True)
            self.assertIsNot(True, None)

  .. code-block:: python
    :lineno-start: 56

            an_integer = 0
            assert_is_not_none(an_integer)
            self.assertIsNot(an_integer, None)

            a_float = 0.0
            assert_is_not_none(a_float)
            self.assertIsNot(a_float, None)

            a_string = ''
            assert_is_not_none(a_string)
            self.assertIsNot(a_string, None)

  .. code-block:: python
    :lineno-start: 68

            a_tuple = ()
            assert_is_not_none(a_tuple)
            self.assertIsNot(a_tuple, None)

            a_list = []
            assert_is_not_none(a_list)
            self.assertIsNot(a_list, None)

            a_set = set()
            assert_is_not_none(a_set)
            self.assertIsNot(a_set, None)

            a_dictionary = {}
            assert_is_not_none(a_dictionary)
            self.assertIsNot(a_dictionary, None)


    def test_assertion_error_w_false():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_assertion_error_w_none to TestAssertionError'

----

*********************************************************************************
test_assertion_error_w_false with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_assertion_error_w_false` to make it a :ref:`method<what is a method?>` of :ref:`TestAssertionError<add TestAssertionError class>`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 5-6, 8-16

            a_dictionary = {}
            assert_is_not_none(a_dictionary)
            self.assertIsNot(a_dictionary, None)

        def test_assertion_error_w_false():
            assert False is False

            assert_is_not_false(None)
            assert_is_not_false(True)
            assert_is_not_false(0)
            assert_is_not_false(0.0)
            assert_is_not_false('')
            assert_is_not_false(())
            assert_is_not_false([])
            assert_is_not_false(set())
            assert_is_not_false({})


    def test_assertion_error_w_true():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestAssertionError.test_assertion_error_w_false()
        takes 0 positional arguments but 1 was given

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_assertion_error_w_false`

.. code-block:: python
  :lineno-start: 80
  :emphasize-lines: 5-6

          a_dictionary = {}
          assert_is_not_none(a_dictionary)
          self.assertIsNot(a_dictionary, None)

      # def test_assertion_error_w_false():
      def test_assertion_error_w_false(self):
          assert False is False

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add calls to :ref:`assertIsNot<test_assert_is_not>` and :ref:`assertIs<test_assert_is>` to :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 4, 7, 10

        # def test_assertion_error_w_false():
        def test_assertion_error_w_false(self):
            assert False is False
            self.assertIsNot(False, False)

            assert_is_not_false(None)
            self.assertIs(None, False)

            assert_is_not_false(True)
            self.assertIs(True, False)

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 2, 5, 8, 11

            assert_is_not_false(0)
            self.assertIs(0, False)

            assert_is_not_false(0.0)
            self.assertIs(0.0, False)

            assert_is_not_false('')
            self.assertIs('', False)

            assert_is_not_false(())
            self.assertIs((), False)

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 2, 5, 8

            assert_is_not_false([])
            self.assertIs([], False)

            assert_is_not_false(set())
            self.assertIs(set(), False)

            assert_is_not_false({})
            self.assertIs({}, False)


    def test_assertion_error_w_true():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: False

  compare this with the error message for ``assert False is not False``

  .. code-block:: python

    E       assert False is not False

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>` for ``(False, False)``

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 4-5

        # def test_assertion_error_w_false():
        def test_assertion_error_w_false(self):
            assert False is False
            # self.assertIsNot(False, False)
            self.assertIs(False, False)

            assert_is_not_false(None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not False

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(None, False)``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 2-3

            assert_is_not_false(None)
            # self.assertIs(None, False)
            self.assertIsNot(None, False)

            assert_is_not_false(True)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not False

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(True, False)``

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 2-3

            assert_is_not_false(True)
            # self.assertIs(True, False)
            self.assertIsNot(True, False)

            assert_is_not_false(0)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 is not False

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(0, False)``

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 2-3

            assert_is_not_false(0)
            # self.assertIs(0, False)
            self.assertIsNot(0, False)

            assert_is_not_false(0.0)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.0 is not False

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(0.0, False)``

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 2-3

            assert_is_not_false(0.0)
            # self.assertIs(0.0, False)
            self.assertIsNot(0.0, False)

            assert_is_not_false('')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '' is not False

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``('', False)``

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 2-3

            assert_is_not_false('')
            # self.assertIs('', False)
            self.assertIsNot('', False)

            assert_is_not_false(())

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: () is not False

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``((), False)``

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 2-3

            assert_is_not_false(())
            # self.assertIs((), False)
            self.assertIsNot((), False)

            assert_is_not_false([])

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: [] is not False

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``([], False)``

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 2-3

            assert_is_not_false([])
            # self.assertIs([], False)
            self.assertIsNot([], False)

            assert_is_not_false(set())

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: set() is not False

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(set(), False)``

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 2-3

            assert set() is not False
            # self.assertIs(set(), False)
            self.assertIsNot(set(), False)

            assert {} is not False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {} is not False

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``({}, False)``

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 2-3

            assert_is_not_false({})
            # self.assertIs({}, False)
            self.assertIsNot({}, False)


    def test_assertion_error_w_true():

  the test passes.

----

* I add a :ref:`variable<what is a variable?>` for ``{}``

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 5

            assert_is_not_false(set())
            # self.assertIs(set(), False)
            self.assertIsNot(set(), False)

            a_dictionary = {}
            assert_is_not_false({})
            # self.assertIs({}, False)
            self.assertIsNot({}, False)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{}``

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 2-3, 5-6

            a_dictionary = {}
            # assert_is_not_false({})
            assert_is_not_false(a_dictionary)
            # self.assertIs({}, False)
            # self.assertIsNot({}, False)
            self.assertIsNot(a_dictionary, False)


    def test_assertion_error_w_true():

  the test is still green.

* I add a :ref:`variable<what is a variable?>` for ``set()``

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 5

            assert_is_not_false([])
            # self.assertIs([], False)
            self.assertIsNot([], False)

            a_set = set()
            assert_is_not_false(set())
            # self.assertIs(set(), False)
            self.assertIsNot(set(), False)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``set()``

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 2-3, 5-6

            a_set = set()
            # assert_is_not_false(set())
            assert_is_not_false(a_set)
            # self.assertIs(set(), False)
            # self.assertIsNot(set(), False)
            self.assertIsNot(a_set, False)

            a_dictionary = {}

  still green.

* I add a :ref:`variable<what is a variable?>` for ``[]``

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 5

            assert_is_not_false(())
            # self.assertIs((), False)
            self.assertIsNot((), False)

            a_list = []
            assert_is_not_false([])
            # self.assertIs([], False)
            self.assertIsNot([], False)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``[]``

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 2-3, 5-6

            a_list = []
            # assert_is_not_false([])
            assert_is_not_false(a_list)
            # self.assertIs([], False)
            # self.assertIsNot([], False)
            self.assertIsNot(a_list, False)

            a_set = set()

  green.

* I add a :ref:`variable<what is a variable?>` for ``()``

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 5

            assert_is_not_false('')
            # self.assertIs('', False)
            self.assertIsNot('', False)

            a_tuple = ()
            assert_is_not_false(())
            # self.assertIs((), False)
            self.assertIsNot((), False)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``()``

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 2-3, 5-6

            a_tuple = ()
            # assert_is_not_false(())
            assert_is_not_false(a_tuple)
            # self.assertIs((), False)
            # self.assertIsNot((), False)
            self.assertIsNot(a_tuple, False)

            a_list = []

  still green.

* I add a :ref:`variable<what is a variable?>` for ``''``

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 5

            assert_is_not_false(0.0)
            # self.assertIs(0.0, False)
            self.assertIsNot(0.0, False)

            a_string = ''
            assert_is_not_false('')
            # self.assertIs('', False)
            self.assertIsNot('', False)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``''``

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 2-3, 5-6

            a_string = ''
            # assert_is_not_false('')
            assert_is_not_false(a_string)
            # self.assertIs('', False)
            # self.assertIsNot('', False)
            self.assertIsNot(a_string, False)

            a_tuple = ()

  the test is still green.

* I add a :ref:`variable<what is a variable?>` for ``0.0``

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 5

            assert_is_not_false(0)
            # self.assertIs(0, False)
            self.assertIsNot(0, False)

            a_float = 0.0
            assert_is_not_false(0.0)
            # self.assertIs(0.0, False)
            self.assertIsNot(0.0, False)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0.0``

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 2-3, 5-6

            a_float = 0.0
            # assert_is_not_false(0.0)
            assert_is_not_false(a_float)
            # self.assertIs(0.0, False)
            # self.assertIsNot(0.0, False)
            self.assertIsNot(a_float, False)

            a_string = ''

  still green.

* I add a :ref:`variable<what is a variable?>` for ``0``

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 5

            assert_is_not_false(True)
            # self.assertIs(True, False)
            self.assertIsNot(True, False)

            an_integer = 0
            assert_is_not_false(0)
            # self.assertIs(0, False)
            self.assertIsNot(0, False)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0``

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 2-3, 5-6

            an_integer = 0
            # assert_is_not_false(0)
            assert_is_not_false(an_integer)
            # self.assertIs(0, False)
            # self.assertIsNot(0, False)
            self.assertIsNot(an_integer, False)

            a_float = 0.0

  green.

* I remove the commented lines from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 80

            a_dictionary = {}
            assert_is_not_none(a_dictionary)
            self.assertIsNot(a_dictionary, None)

        def test_assertion_error_w_false(self):
            assert False is False
            self.assertIs(False, False)

            assert_is_not_false(None)
            self.assertIsNot(None, False)

            assert_is_not_false(True)
            self.assertIsNot(True, False)

  .. code-block:: python
    :lineno-start: 94

            an_integer = 0
            assert_is_not_false(an_integer)
            self.assertIsNot(an_integer, False)

            a_float = 0.0
            assert_is_not_false(a_float)
            self.assertIsNot(a_float, False)

            a_string = ''
            assert_is_not_false(a_string)
            self.assertIsNot(a_string, False)

  .. code-block:: python
    :lineno-start: 106

            a_tuple = ()
            assert_is_not_false(a_tuple)
            self.assertIsNot(a_tuple, False)

            a_list = []
            assert_is_not_false(a_list)
            self.assertIsNot(a_list, False)

            a_set = set()
            assert_is_not_false(a_set)
            self.assertIsNot(a_set, False)

            a_dictionary = {}
            assert_is_not_false(a_dictionary)
            self.assertIsNot(a_dictionary, False)


    def test_assertion_error_w_true():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_assertion_error_w_false to TestAssertionError'

----

*********************************************************************************
test_assertion_error_w_true with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_assertion_error_w_true` to make it a :ref:`method<what is a method?>` of the :ref:`TestAssertionError class<add TestAssertionError class>`

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 5-6, 8-16

            a_dictionary = {}
            assert_is_not_false(a_dictionary)
            self.assertIsNot(a_dictionary, False)

        def test_assertion_error_w_true():
            assert True is True

            assert_is_not_true(None)
            assert_is_not_true(False)
            assert_is_not_true(0)
            assert_is_not_true(0.0)
            assert_is_not_true('')
            assert_is_not_true(())
            assert_is_not_true([])
            assert_is_not_true(set())
            assert_is_not_true({})


    def test_assertion_error_w_equality():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestAssertionError.test_assertion_error_w_true()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_assertion_error_w_true`

.. code-block:: python
  :lineno-start: 118
  :emphasize-lines: 5-6

          a_dictionary = {}
          assert_is_not_false(a_dictionary)
          self.assertIsNot(a_dictionary, False)

      # def test_assertion_error_w_true():
      def test_assertion_error_w_true(self):
          assert True is True


the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to :ref:`assertIsNot<test_assert_is_not>` and :ref:`assertIs<test_assert_is>` to :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 4, 7, 10, 13, 16, 19, 22, 25, 28, 31

        # def test_assertion_error_w_true():
        def test_assertion_error_w_true(self):
            assert True is True
            self.assertIsNot(True, True)

            assert_is_not_true(None)
            self.assertIs(None, True)

            assert_is_not_true(False)
            self.assertIs(False, True)

            assert_is_not_true(0)
            self.assertIs(0, True)

            assert_is_not_true(0.0)
            self.assertIs(0.0, True)

            assert_is_not_true('')
            self.assertIs('', True)

            assert_is_not_true(())
            self.assertIs((), True)

            assert_is_not_true([])
            self.assertIs([], True)

            assert_is_not_true(set())
            self.assertIs(set(), True)

            assert_is_not_true({})
            self.assertIs({}, True)


    def test_assertion_error_w_equality():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: True

  compare this with the error message for ``assert True is not True``

  .. code-block:: python

    E       assert True is not True

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>` for ``(True, True)``

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 4-5

        # def test_assertion_error_w_true():
        def test_assertion_error_w_true(self):
            assert True is True
            # self.assertIsNot(True, True)
            self.assertIs(True, True)

            assert_is_not_true(None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not True

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(None, True)``

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 2-3

            assert_is_not_true(None)
            # self.assertIs(None, True)
            self.assertIsNot(None, True)

            assert_is_not_true(False)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not True

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>` for ``(False, True)``

  .. code-block:: python
    :lineno-start: 132
    :emphasize-lines: 2-3

            assert_is_not_true(False)
            # self.assertIs(False, True)
            self.assertIsNot(False, True)

            assert_is_not_true(0)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 is not True

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(0, True)``

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 2-3

            assert_is_not_true(0)
            # self.assertIs(0, True)
            self.assertIsNot(0, True)

            assert_is_not_true(0.0)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.0 is not True

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(0.0, True)``

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 2-3

            assert_is_not_true(0.0)
            # self.assertIs(0.0, True)
            self.assertIsNot(0.0, True)

            assert_is_not_true('')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '' is not True

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``('', True)``

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 2-3

            assert_is_not_true('')
            # self.assertIs('', True)
            self.assertIsNot('', True)

            assert_is_not_true(())

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: () is not True

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``((), True)``

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 2-3

            assert_is_not_true(())
            # self.assertIs((), True)
            self.assertIsNot((), True)

            assert_is_not_true([])

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: [] is not True

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``([], True)``

  .. code-block:: python
    :lineno-start: 152
    :emphasize-lines: 2-3

            assert_is_not_true([])
            # self.assertIs([], True)
            self.assertIsNot([], True)

            assert_is_not_true(set())

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: set() is not True

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``(set(), True)``

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 2-3

            assert_is_not_true(set())
            # self.assertIs(set(), True)
            self.assertIsNot(set(), True)

            assert_is_not_true({})

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {} is not True

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` for ``({}, True)``

  .. code-block:: python
    :lineno-start: 160
    :emphasize-lines: 2-3

            assert_is_not_true({})
            # self.assertIs({}, True)
            self.assertIsNot({}, True)


    def test_assertion_error_w_equality():

  the test passes.

----

* I add a :ref:`variable<what is a variable?>` for ``{}``

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 5

            assert_is_not_true(set())
            # self.assertIs(set(), True)
            self.assertIsNot(set(), True)

            a_dictionary = {}
            assert_is_not_true({})
            # self.assertIs({}, True)
            self.assertIsNot({}, True)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{}``

  .. code-block:: python
    :lineno-start: 160
    :emphasize-lines: 2-3, 5-6

            a_dictionary = {}
            # assert_is_not_true({})
            assert_is_not_true(a_dictionary)
            # self.assertIs({}, True)
            # self.assertIsNot({}, True)
            self.assertIsNot(a_dictionary, True)


    def test_assertion_error_w_equality():

  the test is still green.

* I add a :ref:`variable<what is a variable?>` for ``set()``

  .. code-block:: python
    :lineno-start: 152
    :emphasize-lines: 5

            assert_is_not_true([])
            # self.assertIs([], True)
            self.assertIsNot([], True)

            a_set = set()
            assert_is_not_true(set())
            # self.assertIs(set(), True)
            self.assertIsNot(set(), True)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``set()``

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 2-3, 5-6

            a_set = set()
            # assert_is_not_true(set())
            assert_is_not_true(a_set)
            # self.assertIs(set(), True)
            # self.assertIsNot(set(), True)
            self.assertIsNot(a_set, True)

            a_dictionary = {}

  still green.

* I add a :ref:`variable<what is a variable?>` for ``[]``

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 5

            assert_is_not_true(())
            # self.assertIs((), True)
            self.assertIsNot((), True)

            a_list = []
            assert_is_not_true([])
            # self.assertIs([], True)
            self.assertIsNot([], True)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``[]``

  .. code-block:: python
    :lineno-start: 152
    :emphasize-lines: 2-3, 5-6

            a_list = []
            # assert_is_not_true([])
            assert_is_not_true(a_list)
            # self.assertIs([], True)
            # self.assertIsNot([], True)
            self.assertIsNot(a_list, True)

            a_set = set()

  green.

* I add a :ref:`variable<what is a variable?>` for ``()``

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 3

            assert_is_not_true('')
            # self.assertIs('', True)
            self.assertIsNot('', True)

            a_tuple = ()
            assert_is_not_true(())
            # self.assertIs((), True)
            self.assertIsNot((), True)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``()``

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 2-3, 5-6

            a_tuple = ()
            # assert_is_not_true(())
            assert_is_not_true(a_tuple)
            # self.assertIs((), True)
            # self.assertIsNot((), True)
            self.assertIsNot(a_tuple, True)

            a_list = []

  still green.

* I add a :ref:`variable<what is a variable?>` for ``''``

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 5

            assert_is_not_true(0.0)
            # self.assertIs(0.0, True)
            self.assertIsNot(0.0, True)

            a_string = ''
            assert_is_not_true('')
            # self.assertIs('', True)
            self.assertIsNot('', True)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``''``

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 2-3, 5-6

            a_string = ''
            # assert_is_not_true('')
            assert_is_not_true(a_string)
            # self.assertIs('', True)
            # self.assertIsNot('', True)
            self.assertIsNot(a_string, True)

            a_tuple = ()

  the test is still green.

* I add a :ref:`variable<what is a variable?>` for ``0.0``

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 5

            assert_is_not_true(0)
            # self.assertIs(0, True)
            self.assertIsNot(0, True)

            a_float = 0.0
            assert_is_not_true(0.0)
            # self.assertIs(0.0, True)
            self.assertIsNot(0.0, True)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0.0``

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 2-3, 5-6

            a_float = 0.0
            # assert_is_not_true(0.0)
            assert_is_not_true(a_float)
            # self.assertIs(0.0, True)
            # self.assertIsNot(0.0, True)
            self.assertIsNot(a_float, True)

            a_string = ''

  still green.

* I add a :ref:`variable<what is a variable?>` for ``0``

  .. code-block:: python
    :lineno-start: 132
    :emphasize-lines: 5

            assert_is_not_true(False)
            # self.assertIs(False, True)
            self.assertIsNot(False, True)

            an_integer = 0
            assert_is_not_true(0)
            # self.assertIs(0, True)
            self.assertIsNot(0, True)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0``

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 2-3, 5-6

            an_integer = 0
            # assert_is_not_true(0)
            assert_is_not_true(an_integer)
            # self.assertIs(0, True)
            # self.assertIsNot(0, True)
            self.assertIsNot(an_integer, True)

            a_float = 0.0

  green.

* I remove the commented lines from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 118

            a_dictionary = {}
            assert_is_not_false(a_dictionary)
            self.assertIsNot(a_dictionary, False)

        def test_assertion_error_w_true(self):
            assert True is True
            self.assertIs(True, True)

            assert_is_not_true(None)
            self.assertIsNot(None, True)

            assert_is_not_true(False)
            self.assertIsNot(False, True)

  .. code-block:: python
    :lineno-start: 132

            an_integer = 0
            assert_is_not_true(an_integer)
            self.assertIsNot(an_integer, True)

            a_float = 0.0
            assert_is_not_true(a_float)
            self.assertIsNot(a_float, True)

            a_string = ''
            assert_is_not_true(a_string)
            self.assertIsNot(a_string, True)

  .. code-block:: python
    :lineno-start: 144

            a_tuple = ()
            assert_is_not_true(a_tuple)
            self.assertIsNot(a_tuple, True)

            a_list = []
            assert_is_not_true(a_list)
            self.assertIsNot(a_list, True)

            a_set = set()
            assert_is_not_true(a_set)
            self.assertIsNot(a_set, True)

            a_dictionary = {}
            assert_is_not_true(a_dictionary)
            self.assertIsNot(a_dictionary, True)


    def test_assertion_error_w_equality():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_assertion_error_w_true to TestAssertionError'

----

*********************************************************************************
test_assertion_error_w_equality with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_assertion_error_w_equality` to make it a :ref:`method<what is a method?>` of the :ref:`TestAssertionError<add TestAssertionError class>`

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 5-8, 10-12

            a_dictionary = {}
            assert_is_not_true(a_dictionary)
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality():
            assert_equal(None, None)
            assert_equal(False, False)
            assert_equal(True, True)

            assert_not_equal(False, None)
            assert_not_equal(False, True)
            assert_not_equal(True, None)


    def test_assertion_error_w_is_vs_equal():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestAssertionError.test_assertion_error_w_equality()
        takes 0 positional arguments but 1 was given

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_assertion_error_w_equality`

.. code-block:: python
  :lineno-start: 156
  :emphasize-lines: 5-6

          a_dictionary = {}
          assert_is_not_true(a_dictionary)
          self.assertIsNot(a_dictionary, True)

      # def test_assertion_error_w_equality():
      def test_assertion_error_w_equality(self):
          assert_equal(None, None)
          assert_equal(False, False)
          assert_equal(True, True)

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to :ref:`assertNotEqual<test_assert_not_equal>` and :ref:`assertEqual<test_assert_equal>` to :ref:`test_assertion_error_w_equality`

  .. code-block:: python
    :lineno-start: 160
    :emphasize-lines: 4, 7, 10, 13, 16, 19

        # def test_assertion_error_w_equality():
        def test_assertion_error_w_equality(self):
            assert_equal(None, None)
            self.assertNotEqual(None, None)

            assert_equal(False, False)
            self.assertNotEqual(False, False)

            assert_equal(True, True)
            self.assertNotEqual(True, True)

            assert_not_equal(False, None)
            self.assertEqual(False, None)

            assert_not_equal(False, True)
            self.assertEqual(False, True)

            assert_not_equal(True, None)
            self.assertEqual(True, None)


    def test_assertion_error_w_is_vs_equal():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None == None

  compare this with the error for ``assert None != None``

  .. code-block:: python

    E   assert None != None

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for ``(None, None)``

  .. code-block:: python
    :lineno-start: 160
    :emphasize-lines: 4-5

        # def test_assertion_error_w_equality():
        def test_assertion_error_w_equality(self):
            assert_equal(None, None)
            # self.assertNotEqual(None, None)
            self.assertEqual(None, None)

            assert_equal(False, False)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False == False

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for ``(False, False)``

  .. code-block:: python
    :lineno-start: 166
    :emphasize-lines: 2-3

            assert_equal(False, False)
            # self.assertNotEqual(False, False)
            self.assertEqual(False, False)

            assert_equal(True, True)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True == True

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for ``(True, True)``

  .. code-block:: python
    :lineno-start: 170
    :emphasize-lines: 2-3

            assert_equal(True, True)
            # self.assertNotEqual(True, True)
            self.assertEqual(True, True)

            assert_not_equal(False, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False != None

* I change :ref:`assertEqual<test_assert_equal>` to :ref:`assertNotEqual<test_assert_not_equal>` for ``(False, None)``

  .. code-block:: python
    :lineno-start: 174
    :emphasize-lines: 2-3

            assert_not_equal(False, None)
            # self.assertEqual(False, None)
            self.assertNotEqual(False, None)

            assert_not_equal(False, True)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False != True

  compare this with the error for ``assert False == True``

  .. code-block:: python

    E    assert False == True

* I change :ref:`assertEqual<test_assert_equal>` to :ref:`assertNotEqual<test_assert_not_equal>` for ``(False, True)``

  .. code-block:: python
    :lineno-start: 178
    :emphasize-lines: 2-3

            assert_not_equal(False, True)
            # self.assertEqual(False, True)
            self.assertNotEqual(False, True)

            assert_not_equal(True, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != None

* I change :ref:`assertEqual<test_assert_equal>` to :ref:`assertNotEqual<test_assert_not_equal>` for ``(True, None)``

  .. code-block:: python
    :lineno-start: 182
    :emphasize-lines: 2-3

            assert_not_equal(True, None)
            # self.assertEqual(True, None)
            self.assertNotEqual(True, None)


    def test_assertion_error_w_is_vs_equal():

  the test passes.

* I remove the commented lines from :ref:`test_assertion_error_w_equality`

  .. code-block:: python
    :lineno-start: 156

            a_dictionary = {}
            assert_is_not_true(a_dictionary)
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality(self):
            assert_equal(None, None)
            self.assertEqual(None, None)

            assert_equal(False, False)
            self.assertEqual(False, False)

            assert_equal(True, True)
            self.assertEqual(True, True)

  .. code-block:: python
    :lineno-start: 170

            assert_not_equal(False, None)
            self.assertNotEqual(False, None)

            assert_not_equal(False, True)
            self.assertNotEqual(False, True)

            assert_not_equal(True, None)
            self.assertNotEqual(True, None)


    def test_assertion_error_w_is_vs_equal():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_assertion_error_w_equality to TestAssertionError'

----

*********************************************************************************
test_assertion_error_w_is_vs_equal with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_assertion_error_w_is_vs_equal` to make it a :ref:`method<what is a method?>` of :ref:`TestAssertionError<add TestAssertionError class>`

  .. code-block:: python
    :lineno-start: 176
    :emphasize-lines: 4-6

            assert_not_equal(True, None)
            self.assertNotEqual(True, None)

        def test_assertion_error_w_is_vs_equal():
            assert_is_not(0, 0.0)
            assert_equal(0, 0.0)


    def will_not_run():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestAssertionError.test_assertion_error_w_is_vs_equal()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the :ref:`definition<how to make a function that takes input>` of :ref:`test_assertion_error_w_is_vs_equal`

.. code-block:: python
  :lineno-start: 176
  :emphasize-lines: 4-5

          assert_not_equal(True, None)
          self.assertNotEqual(True, None)

      # def test_assertion_error_w_is_vs_equal():
      def test_assertion_error_w_is_vs_equal(self):
          assert_is_not(0, 0.0)
          assert_equal(0, 0.0)

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to :ref:`assertIs<test_assert_is>` for ``assert 0 is not 0.0``

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 4

        # def test_assertion_error_w_is_vs_equal():
        def test_assertion_error_w_is_vs_equal(self):
            assert_is_not(0, 0.0)
            self.assertIs(0, 0.0)

            assert_equal(0, 0.0)

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: python

    AssertionError: 0 is not 0.0

  compare the :ref:`assertions<what is an assertion?>`: ``assertIs(0, 0.0)`` vs ``assert 0 is 0.0``.

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>`

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 4-5

        # def test_assertion_error_w_is_vs_equal():
        def test_assertion_error_w_is_vs_equal(self):
            assert_is_not(0, 0.0)
            # self.assertIs(0, 0.0)
            self.assertIsNot(0, 0.0)

            assert_equal(0, 0.0)

  the test passes. Compare the :ref:`assertions<what is an assertion?>`: ``assertIsNot(0, 0.0)`` vs ``assert 0 is not 0.0``.

* I add a :ref:`call<how to call a function with input>` to :ref:`assertNotEqual<test_assert_not_equal>` for ``assert 0 == 0.0``

  .. code-block:: python
    :lineno-start: 185
    :emphasize-lines: 2

            assert_equal(0, 0.0)
            self.assertNotEqual(0, 0.0)


    def will_not_run():

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: python

    AssertionError: 0 == 0.0

  compare the :ref:`assertions<what is an assertion?>`: ``assertNotEqual(0, 0.0)`` vs ``assert 0 != 0.0``.

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>`

  .. code-block:: python
    :lineno-start: 185
    :emphasize-lines: 2-3

            assert_equal(0, 0.0)
            # self.assertNotEqual(0, 0.0)
            self.assertEqual(0, 0.0)


    def will_not_run():

  the test passes. Compare the :ref:`assertions<what is an assertion?>`: ``assertIsNot(0, 0.0)`` vs ``assert 0 is not 0.0``.

* I remove the commented lines from :ref:`test_assertion_error_w_is_vs_equal`

  .. code-block:: python
    :lineno-start: 176

            assert_not_equal(True, None)
            self.assertNotEqual(True, None)

        def test_assertion_error_w_is_vs_equal(self):
            assert_is_not(0, 0.0)
            self.assertIsNot(0, 0.0)

            assert_equal(0, 0.0)
            self.assertEqual(0, 0.0)


    def will_not_run():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_assertion_error_w_is_vs_equal to TestAssertionError'

----

*********************************************************************************
will_not_run with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`will not run<pytest only calls the function if the name starts with test>` to the :ref:`TestAssertionError class<add TestAssertionError class>`

  .. code-block:: python
    :lineno-start: 183
    :emphasize-lines: 4-7

            assert_equal(0, 0.0)
            self.assertEqual(0, 0.0)

        def will_not_run():
            # will not run because
            # the name does not start with test
            assert False == True


    def test_failure():

  the tests are still green.

* I add a :ref:`call<how to call a function with input>` to :ref:`test_assert_equal`

  .. code-block:: python
    :lineno-start: 186
    :emphasize-lines: 5

        def will_not_run():
            # will not run because
            # the name does not start with test
            assert False == True
            self.assertEqual(False, True)


    def test_failure():

  still green, it does not raise :ref:`NameError<test_catching_name_error>` because this :ref:`method<what is a method?>` never gets :ref:`called<how to call a function with input>` by pytest_.

* I add ``self`` to the parentheses of :ref:`will not run<pytest only calls the function if the name starts with test>`

  .. code-block:: python
    :lineno-start: 183
    :emphasize-lines: 4-5

            assert_equal(0, 0.0)
            self.assertEqual(0, 0.0)

        # def will_not_run():
        def will_not_run(self):
            # will not run because
            # the name does not start with test
            assert False == True
            self.assertEqual(False, True)

  green, it does not raise :ref:`AssertionError<what causes AssertionError?>`.

* I change the name from :ref:`will not run<pytest only calls the function if the name starts with test>` to ``test_will_not_run``

  .. code-block:: python
    :lineno-start: 186
    :emphasize-lines: 2-3

        # def will_not_run():
        # def will_not_run(self):
        def test_will_not_run(self):
            # will not run because
            # the name does not start with test
            assert False == True
            self.assertEqual(False, True)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert False == True

  a reminder that the test only runs if :ref:`the method/function name starts with test<pytest only calls the function if the name starts with test>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I undo the change

.. code-block:: python
  :lineno-start: 183
  :emphasize-lines: 4, 6

          assert_equal(0, 0.0)
          self.assertEqual(0, 0.0)

      def will_not_run():
      # def will_not_run(self):
      # def test_will_not_run(self):
          # will not run because
          # the name does not start with test
          assert False == True
          self.assertEqual(False, True)


  def test_failure():

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the new commented lines from :ref:`will not run<pytest only calls the function if the name starts with test>`

  .. code-block:: python
    :lineno-start: 186

        def will_not_run():
            # will not run because
            # the name does not start with test
            assert False == True
            self.assertEqual(False, True)


    def test_failure():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move will_not_run to TestAssertionError'

----

*********************************************************************************
test_failure with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_failure<pytest only calls the function if the name starts with test>` to :ref:`TestAssertionError<add TestAssertionError class>`

  .. code-block:: python
    :lineno-start: 186
    :emphasize-lines: 7-9

        def will_not_run():
            # will not run because
            # the name does not start with test
            assert False == True
            self.assertEqual(False, True)

        def test_failure():
            # assert False == True
            assert_not_equal(False, True)


    # NOTES

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestAssertionError.test_failure()
        takes 0 positional arguments but 1 was given

  because ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_failure<pytest only calls the function if the name starts with test>` in :ref:`TestAssertionError<add TestAssertionError class>`

.. code-block:: python
  :lineno-start: 186
  :emphasize-lines: 7-8

      def will_not_run():
          # will not run because
          # the name does not start with test
          assert False == True
          self.assertEqual(False, True)

      # def test_failure():
      def test_failure(self):
          # assert False == True
          assert_not_equal(False, True)

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>`

  .. code-block:: python
    :lineno-start: 192
    :emphasize-lines: 5

        # def test_failure():
        def test_failure(self):
            # assert False == True
            assert_not_equal(False, True)
            self.assertNotEqual(False, False)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False == False

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>`

  .. code-block:: python
    :lineno-start: 192
    :emphasize-lines: 5-6

        # def test_failure():
        def test_failure(self):
            # assert False == True
            assert_not_equal(False, True)
            # self.assertNotEqual(False, False)
            self.assertEqual(False, False)


    # NOTES

  the test passes.

* I remove the commented lines from :ref:`test_failure<pytest only calls the function if the name starts with test>`

  .. code-block:: python
    :lineno-start: 186

        def will_not_run():
            # will not run because
            # the name does not start with test
            assert False == True
            self.assertEqual(False, True)

        def test_failure(self):
            assert_not_equal(False, True)
            self.assertEqual(False, False)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_failure to TestAssertionError'

----

*********************************************************************************
remove repetition with class attributes
*********************************************************************************

Three of the tests have the exact same :ref:`variables<what is a variable?>`. I can make them :ref:`class attributes<what is a class attribute?>` to remove repetition of making the same :ref:`variables<what is a variable?>` in the tests.

* I add a :ref:`class attribute<what is a class attribute?>` for ``an_integer = 0`` to :ref:`TestAssertionError<add TestAssertionError class>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 3

    class TestAssertionError(unittest.TestCase):

        an_integer = 0

        def test_assert_keyword(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``an_integer = 0`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 11-15

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)

            assert_is_not_none(False)
            self.assertIsNot(False, None)

            assert_is_not_none(True)
            self.assertIsNot(True, None)

            # an_integer = 0
            # assert_is_not_none(an_integer)
            # self.assertIsNot(an_integer, None)
            assert_is_not_none(self.an_integer)
            self.assertIsNot(self.an_integer, None)

            a_float = 0.0

  the test is still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``an_integer = 0`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 15-19

            a_dictionary = {}
            assert_is_not_none(a_dictionary)
            self.assertIsNot(a_dictionary, None)

        def test_assertion_error_w_false(self):
            assert False is False
            self.assertIs(False, False)

            assert_is_not_false(None)
            self.assertIsNot(None, False)

            assert_is_not_false(True)
            self.assertIsNot(True, False)

            # an_integer = 0
            # assert_is_not_false(an_integer)
            # self.assertIsNot(an_integer, False)
            assert_is_not_false(self.an_integer)
            self.assertIsNot(self.an_integer, False)

            a_float = 0.0

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``an_integer = 0`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 15-19

            a_dictionary = {}
            assert_is_not_false(a_dictionary)
            self.assertIsNot(a_dictionary, False)

        def test_assertion_error_w_true(self):
            assert True is True
            self.assertIs(True, True)

            assert_is_not_true(None)
            self.assertIsNot(None, True)

            assert_is_not_true(False)
            self.assertIsNot(False, True)

            # an_integer = 0
            # assert_is_not_true(an_integer)
            # self.assertIsNot(an_integer, True)
            assert_is_not_true(self.an_integer)
            self.assertIsNot(self.an_integer, True)

            a_float = 0.0

  green.

----

* I add a :ref:`class attribute<what is a class attribute?>` for ``a_float = 0.0``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 4

    class TestAssertionError(unittest.TestCase):

        an_integer = 0
        a_float = 0.0

        def test_assert_keyword(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_float = 0.0`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 3-7

            self.assertIsNot(self.an_integer, None)

            # a_float = 0.0
            # assert_is_not_none(a_float)
            # self.assertIsNot(a_float, None)
            assert_is_not_none(self.a_float)
            self.assertIsNot(self.a_float, None)

            a_string = ''

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_float = 0.0`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 3-7

            self.assertIsNot(self.an_integer, False)

            # a_float = 0.0
            # assert_is_not_false(a_float)
            # self.assertIsNot(a_float, False)
            assert_is_not_false(self.a_float)
            self.assertIsNot(self.a_float, False)

            a_string = ''

  the test is still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_float = 0.0`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 3-7

            self.assertIsNot(self.an_integer, True)

            # a_float = 0.0
            # assert_is_not_true(a_float)
            # self.assertIsNot(a_float, True)
            assert_is_not_true(self.a_float)
            self.assertIsNot(self.a_float, True)

            a_string = ''

  still green.

----

* I add a :ref:`class attribute<what is a class attribute?>` for ``a_string = ''``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 5

    class TestAssertionError(unittest.TestCase):

        an_integer = 0
        a_float = 0.0
        a_string = ''

        def test_assert_keyword(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_string = ''`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_float, None)

            # a_string = ''
            # assert_is_not_none(a_string)
            # self.assertIsNot(a_string, None)
            assert_is_not_none(self.a_string)
            self.assertIsNot(self.a_string, None)

            a_tuple = ()

  green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_string = ''`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_float, False)

            # a_string = ''
            # assert_is_not_false(a_string)
            # self.assertIsNot(a_string, False)
            assert_is_not_false(self.a_string)
            self.assertIsNot(self.a_string, False)

            a_tuple = ()

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_string = ''`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_float, True)

            # a_string = ''
            # assert_is_not_true(a_string)
            # self.assertIsNot(a_string, True)
            assert_is_not_true(self.a_string)
            self.assertIsNot(self.a_string, True)

            a_tuple = ()

  the test is still green.

----

* I add a :ref:`class attribute<what is a class attribute?>` for ``a_tuple = ()``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 6

    class TestAssertionError(unittest.TestCase):

        an_integer = 0
        a_float = 0.0
        a_string = ''
        a_tuple = ()

        def test_assert_keyword(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_tuple = ()`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_string, None)

            # a_tuple = ()
            # assert_is_not_none(a_tuple)
            # self.assertIsNot(a_tuple, None)
            assert_is_not_none(self.a_tuple)
            self.assertIsNot(self.a_tuple, None)

            a_list = []

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_tuple = ()`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 123
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_string, False)

            # a_tuple = ()
            # assert_is_not_false(a_tuple)
            # self.assertIsNot(a_tuple, False)
            assert_is_not_false(self.a_tuple)
            self.assertIsNot(self.a_tuple, False)

            a_list = []

  green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_tuple = ()`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 169
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_string, True)

            # a_tuple = ()
            # assert_is_not_true(a_tuple)
            # self.assertIsNot(a_tuple, True)
            assert_is_not_true(self.a_tuple)
            self.assertIsNot(self.a_tuple, True)

            a_list = []

  still green.

----

* I add a :ref:`class attribute<what is a class attribute?>` for ``a_list = []``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 7

    class TestAssertionError(unittest.TestCase):

        an_integer = 0
        a_float = 0.0
        a_string = ''
        a_tuple = ()
        a_list = []

        def test_assert_keyword(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_list = []`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_tuple, None)

            # a_list = []
            # assert_is_not_none(a_list)
            # self.assertIsNot(a_list, None)
            assert_is_not_none(self.a_list)
            self.assertIsNot(self.a_list, None)

            a_set = set()

  the test is still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_list = []`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 132
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_tuple, False)

            # a_list = []
            # assert_is_not_false(a_list)
            # self.assertIsNot(a_list, False)
            assert_is_not_false(self.a_list)
            self.assertIsNot(self.a_list, False)

            a_set = set()

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_list = []`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 180
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_tuple, True)

            # a_list = []
            # assert_is_not_true(a_list)
            # self.assertIsNot(a_list, True)
            assert_is_not_true(self.a_list)
            self.assertIsNot(self.a_list, True)

            a_set = set()

  green.

----

* I add a :ref:`class attribute<what is a class attribute?>` for ``a_set = set()``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 8

    class TestAssertionError(unittest.TestCase):

        an_integer = 0
        a_float = 0.0
        a_string = ''
        a_tuple = ()
        a_list = []
        a_set = set()

        def test_assert_keyword(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_set = set()`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_list, None)

            # a_set = set()
            # assert_is_not_none(a_set)
            # self.assertIsNot(a_set, None)
            assert_is_not_none(self.a_set)
            self.assertIsNot(self.a_set, None)

            a_dictionary = {}

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_set = set()`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 141
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_list, False)

            # a_set = set()
            # assert_is_not_false(a_set)
            # self.assertIsNot(a_set, False)
            assert_is_not_false(self.a_set)
            self.assertIsNot(self.a_set, False)

            a_dictionary = {}

  the test is still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_set = set()`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_list, True)

            # a_set = set()
            # assert_is_not_true(a_set)
            # self.assertIsNot(a_set, True)
            assert_is_not_true(self.a_set)
            self.assertIsNot(self.a_set, True)

            a_dictionary = {}

  still green.

----

* I add a :ref:`class attribute<what is a class attribute?>` for ``a_dictionary = {}``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 9

    class TestAssertionError(unittest.TestCase):

        an_integer = 0
        a_float = 0.0
        a_string = ''
        a_tuple = ()
        a_list = []
        a_set = set()
        a_dictionary = {}

        def test_assert_keyword(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_dictionary = {}`` from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_set, None)

            # a_dictionary = {}
            # assert_is_not_none(a_dictionary)
            # self.assertIsNot(a_dictionary, None)
            assert_is_not_none(self.a_dictionary)
            self.assertIsNot(self.a_dictionary, None)

        def test_assertion_error_w_false(self):

  the test is still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_dictionary = {}`` from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 150
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_set, False)

            # a_dictionary = {}
            # assert_is_not_false(a_dictionary)
            # self.assertIsNot(a_dictionary, False)
            assert_is_not_false(self.a_dictionary)
            self.assertIsNot(self.a_dictionary, False)

        def test_assertion_error_w_true(self):

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_dictionary = {}`` from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 202
    :emphasize-lines: 3-7

            self.assertIsNot(self.a_set, True)

            # a_dictionary = {}
            # assert_is_not_true(a_dictionary)
            # self.assertIsNot(a_dictionary, True)
            assert_is_not_true(self.a_dictionary)
            self.assertIsNot(self.a_dictionary, True)

        def test_assertion_error_w_equality(self):

  green.

----

* I remove the commented lines from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 158

        def test_assertion_error_w_true(self):
            assert True is True
            self.assertIs(True, True)

            assert_is_not_true(None)
            self.assertIsNot(None, True)

            assert_is_not_true(False)
            self.assertIsNot(False, True)

  .. code-block:: python
    :lineno-start: 168

            assert_is_not_true(self.an_integer)
            self.assertIsNot(self.an_integer, True)

            assert_is_not_true(self.a_float)
            self.assertIsNot(self.a_float, True)

            assert_is_not_true(self.a_string)
            self.assertIsNot(self.a_string, True)

  .. code-block:: python
    :lineno-start: 177

            assert_is_not_true(self.a_tuple)
            self.assertIsNot(self.a_tuple, True)

            assert_is_not_true(self.a_list)
            self.assertIsNot(self.a_list, True)

            assert_is_not_true(self.a_set)
            self.assertIsNot(self.a_set, True)

            assert_is_not_true(self.a_dictionary)
            self.assertIsNot(self.a_dictionary, True)

        def test_assertion_error_w_equality(self):

* I remove the commented lines from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 106

        def test_assertion_error_w_false(self):
            assert False is False
            self.assertIs(False, False)

            assert_is_not_false(None)
            self.assertIsNot(None, False)

            assert_is_not_false(True)
            self.assertIsNot(True, False)

  .. code-block:: python
    :lineno-start: 116

            assert_is_not_false(self.an_integer)
            self.assertIsNot(self.an_integer, False)

            assert_is_not_false(self.a_float)
            self.assertIsNot(self.a_float, False)

            assert_is_not_false(self.a_string)
            self.assertIsNot(self.a_string, False)

  .. code-block:: python
    :lineno-start: 125

            assert_is_not_false(self.a_tuple)
            self.assertIsNot(self.a_tuple, False)

            assert_is_not_false(self.a_list)
            self.assertIsNot(self.a_list, False)

            assert_is_not_false(self.a_set)
            self.assertIsNot(self.a_set, False)

            assert_is_not_false(self.a_dictionary)
            self.assertIsNot(self.a_dictionary, False)

        def test_assertion_error_w_true(self):

* I remove the commented lines from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 54

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)

            assert_is_not_none(False)
            self.assertIsNot(False, None)

            assert_is_not_none(True)
            self.assertIsNot(True, None)

  .. code-block:: python
    :lineno-start: 64

            assert_is_not_none(self.an_integer)
            self.assertIsNot(self.an_integer, None)

            assert_is_not_none(self.a_float)
            self.assertIsNot(self.a_float, None)

            assert_is_not_none(self.a_string)
            self.assertIsNot(self.a_string, None)

  .. code-block:: python
    :lineno-start: 73

            assert_is_not_none(self.a_tuple)
            self.assertIsNot(self.a_tuple, None)

            assert_is_not_none(self.a_list)
            self.assertIsNot(self.a_list, None)

            assert_is_not_none(self.a_set)
            self.assertIsNot(self.a_set, None)

            assert_is_not_none(self.a_dictionary)
            self.assertIsNot(self.a_dictionary, None)

        def test_assertion_error_w_false(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract class attributes'

:ref:`I can use class attributes to remove repetition<remove repetition with class attributes>`. I make them once and other things in the :ref:`class<everything is an object>` can reference them.

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

* I can use the :ref:`unittest library<another way to write tests>` to write tests with the :ref:`methods of the unittest.TestCase class<test_dir_unittest_testcase>` or I can write them with bare :ref:`assert statements<what is an assertion?>`.
* I can use :ref:`class attributes<what is a class attribute?>` for things that repeat, which allows :ref:`methods<what is a method?>` of the same :ref:`class<everything is an object>` to use them.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test AssertionError with unittest: tests>`

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