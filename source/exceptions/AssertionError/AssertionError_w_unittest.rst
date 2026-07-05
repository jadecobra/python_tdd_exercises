.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

#################################################################################
AssertionError: use unittest
#################################################################################

----

I want to use the :ref:`unittest library<another way to write tests>` in the :ref:`assertion_error<what is an assertion?>` project.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_unittest.py
  :language: python
  :linenos:

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`assertion_error folder<what is an assertion?>` in the ``pumping_python`` folder_Make sure you are in the ``pumping_python`` folder_ with pwd_ in the terminal_

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

    ================== 7 passed in A.BCs ===================

----

*********************************************************************************
add TestAssertionError class
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a :ref:`class<what is a class?>` named ``AssertionError`` to ``test_assertion_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 3-4

    class AssertionError(object):

        def test_failure(self):
            self.assertFalse(True)


    def test_assert_keyword():

  the test is still green.

* I change the name of the :ref:`class<what is a class?>` to ``TestAssertionError``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # class AssertionError(object):
    class TestAssertionError(object):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'TestAssertionError' object
                    has no attribute 'assertFalse'

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 141
    :emphasize-lines: 6
    :emphasize-text: AttributeError

    # None is None and equal to None


    # Exceptions seen
    # AssertionError
    # AttributeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`unitest.TestCase<test_attributes_and_methods_of_unittest_testcase>` as the parent :ref:`class<what is a class?>` of ``TestAssertionError``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    # class AssertionError(object):
    # class TestAssertionError(object):
    class TestAssertionError(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'unittest' is not defined.
               Did you forget to import 'unittest'?

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 4
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # AttributeError
    # NameError

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import unittest


    # class AssertionError(object):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2-3

        def test_failure(self):
            # self.assertFalse(True)
            self.assertFalse(False)


    def test_assert_keyword():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :linenos:

    import unittest


    class TestAssertionError(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(False)


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
test_assert_keyword
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_assert_keyword` to make it a :ref:`method<what is a method?>` of the :ref:`TestAssertionError class<add TestAssertionError class>` and replace ``test_failure``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-4, 6, 8

    class TestAssertionError(unittest.TestCase):

        def test_assert_keyword():
            assert 1 + 1 == 2

            assert '1' + '1' == '11'

            assert 'I am' + ' alive' == 'I am alive'


    def test_assertion_error_w_none():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestAssertionError.test_assert_keyword()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
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
  :lineno-start: 4
  :emphasize-lines: 3-4

  class TestAssertionError(unittest.TestCase):

      # def test_assert_keyword():
      def test_assert_keyword(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the three :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4, 7, 10

        # def test_assert_keyword():
        def test_assert_keyword(self):
            assert 1 + 1 == 2
            self.assertNotEqual(1+1, 2)

            assert '1' + '1' == '11'
            self.assertNotEqual('1'+'1', '11')

            assert 'I am' + ' alive' == 'I am alive'
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
    :lineno-start: 6
    :emphasize-lines: 4-5

        # def test_assert_keyword():
        def test_assert_keyword(self):
            assert 1 + 1 == 2
            # self.assertNotEqual(1+1, 2)
            self.assertEqual(1+1, 2)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '11' == '11'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for ``('1'+'1', '11')``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 8-9

        # def test_assert_keyword():
        def test_assert_keyword(self):
            assert 1 + 1 == 2
            # self.assertNotEqual(1+1, 2)
            self.assertEqual(1+1, 2)

            assert '1' + '1' == '11'
            # self.assertNotEqual('1'+'1', '11')
            self.assertEqual('1'+'1', '11')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I am alive' == 'I am alive'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for ``('I am'+' alive', 'I am alive')``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 12-13

        # def test_assert_keyword():
        def test_assert_keyword(self):
            assert 1 + 1 == 2
            # self.assertNotEqual(1+1, 2)
            self.assertEqual(1+1, 2)

            assert '1' + '1' == '11'
            # self.assertNotEqual('1'+'1', '11')
            self.assertEqual('1'+'1', '11')

            assert 'I am' + ' alive' == 'I am alive'
            # self.assertNotEqual('I am'+' alive', 'I am alive')
            self.assertEqual('I am'+' alive', 'I am alive')


    def test_assertion_error_w_none():

  the test passes.

----

* I add :ref:`variables<what is a variable?>` for ``'I am' + ' alive'`` and ``'I am alive'``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 5-6

            assert '1' + '1' == '11'
            # self.assertNotEqual('1'+'1', '11')
            self.assertEqual('1'+'1', '11')

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert 'I am' + ' alive' == 'I am alive'
            # self.assertNotEqual('I am'+' alive', 'I am alive')
            self.assertEqual('I am'+' alive', 'I am alive')


    def test_assertion_error_w_none():

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``'I am' + ' alive'`` and ``'I am alive'``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3-4, 6-7

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            # assert 'I am' + ' alive' == 'I am alive'
            assert reality == my_expectation
            # self.assertNotEqual('I am'+' alive', 'I am alive')
            # self.assertEqual('I am'+' alive', 'I am alive')
            self.assertEqual(reality, my_expectation)


    def test_assertion_error_w_none():

  the test is still green.

* I add :ref:`variables<what is a variable?>` for ``'1' + '1'`` and ``'11'``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 7-8

        # def test_assert_keyword():
        def test_assert_keyword(self):
            assert 1 + 1 == 2
            # self.assertNotEqual(1+1, 2)
            self.assertEqual(1+1, 2)

            reality = '1' + '1'
            my_expectation = '11'
            assert '1' + '1' == '11'
            # self.assertNotEqual('1'+'1', '11')
            self.assertEqual('1'+'1', '11')

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``'1' + '1'`` and ``'11'``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3-4, 6-7

            reality = '1' + '1'
            my_expectation = '11'
            # assert '1' + '1' == '11'
            assert reality == my_expectation
            # self.assertNotEqual('1'+'1', '11')
            # self.assertEqual('1'+'1', '11')
            self.assertEqual(reality, my_expectation)

  still green.

* I add :ref:`variables<what is a variable?>` for ``1 + 1`` and ``2``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3-4

        # def test_assert_keyword():
        def test_assert_keyword(self):
            reality = 1 + 1
            my_expectation = 2
            assert 1 + 1 == 2
            # self.assertNotEqual(1+1, 2)
            self.assertEqual(1+1, 2)

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``1 + 1`` and ``2``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-6, 8-9

        # def test_assert_keyword():
        def test_assert_keyword(self):
            reality = 1 + 1
            my_expectation = 2
            # assert 1 + 1 == 2
            assert reality == my_expectation
            # self.assertNotEqual(1+1, 2)
            # self.assertEqual(1+1, 2)
            self.assertEqual(reality, my_expectation)

  green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 4

    class TestAssertionError(unittest.TestCase):

        def test_assert_keyword(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_assertion_error_w_none():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    move test_assert_keyword to TestAssertionError

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

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 6-25


            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

        def test_assertion_error_w_none():
            assert None is None

            assert False is not None

            assert True is not None

            assert 0 is not None

            assert 0.0 is not None

            assert '' is not None

            assert () is not None

            assert [] is not None

            assert set() is not None

            assert {} is not None


    def test_assertion_error_w_false():

  .. caution:: Indentation matters in Python_. It is how it knows what blocks belong to what :ref:`function/method<what is a function?>`, :ref:`class<what is a class?>` or :ref:`module<what is a module?>` (Use 4 spaces)

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
  :lineno-start: 22
  :emphasize-lines: 1-2

      # def test_assertion_error_w_none():
      def test_assertion_error_w_none(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertIs method<test_assert_is>` for each :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4, 7, 10, 13, 16, 19, 22, 25, 28, 31

        # def test_assertion_error_w_none():
        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNot(None, None)

            assert False is not None
            self.assertIs(False, None)

            assert True is not None
            self.assertIs(True, None)

            assert 0 is not None
            self.assertIs(0, None)

            assert 0.0 is not None
            self.assertIs(0.0, None)

            assert '' is not None
            self.assertIs('', None)

            assert () is not None
            self.assertIs((), None)

            assert [] is not None
            self.assertIs([], None)

            assert set() is not None
            self.assertIs(set(), None)

            assert {} is not None
            self.assertIs({}, None)


    def test_assertion_error_w_false():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: None

  compare this with the error message for ``assert None is not None``

  .. code-block:: python

    E       assert None is not None

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4-5

        # def test_assertion_error_w_none():
        def test_assertion_error_w_none(self):
            assert None is None
            # self.assertIsNot(None, None)
            self.assertIs(None, None)

            assert False is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not None

  compare this with the error message for ``assert False is None``

  .. code-block:: python

    E    assert False is None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 2-3

            assert False is not None
            # self.assertIs(False, None)
            self.assertIsNot(False, None)

            assert True is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not None

  compare this with the error message for ``assert True is None``

  .. code-block:: python

    E    assert True is None

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 2-3

            assert True is not None
            # self.assertIs(True, None)
            self.assertIsNot(True, None)

            assert 0 is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 2-3

            assert 0 is not None
            # self.assertIs(0, None)
            self.assertIsNot(0, None)

            assert 0.0 is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.0 is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 2-3

            assert 0.0 is not None
            # self.assertIs(0.0, None)
            self.assertIsNot(0.0, None)

            assert '' is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '' is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2-3

            assert '' is not None
            # self.assertIs('', None)
            self.assertIsNot('', None)

            assert () is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: () is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2-3

            assert () is not None
            # self.assertIs((), None)
            self.assertIsNot((), None)

            assert [] is not None


  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: [] is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2-3

            assert [] is not None
            # self.assertIs([], None)
            self.assertIsNot([], None)

            assert set() is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: set()  is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 2-3

            assert set() is not None
            # self.assertIs(set(), None)
            self.assertIsNot(set(), None)

            assert {} is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {} is not None

* I change :ref:`assertIs<test_assert_is>` to :ref:`assertIsNot<test_assert_is_not>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2-3

            assert {} is not None
            # self.assertIs({}, None)
            self.assertIsNot({}, None)


    def test_assertion_error_w_false():

  the test passes.

----

* I add a :ref:`variable<what is a variable?>` for ``{}``

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 3

            self.assertIsNot(set(), None)

            a_dictionary = {}
            assert {} is not None
            # self.assertIs({}, None)
            self.assertIsNot({}, None)


    def test_assertion_error_w_false():

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{}``

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 4-5, 7-8

            self.assertIsNot(set(), None)

            a_dictionary = {}
            # assert {} is not None
            assert a_dictionary is not None
            # self.assertIs({}, None)
            # self.assertIsNot({}, None)
            self.assertIsNot(a_dictionary, None)


    def test_assertion_error_w_false():

  the test is still green.

* I add a :ref:`variable<what is a variable?>` for ``set()``

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 3

            self.assertIsNot([], None)

            a_set = set()
            assert set() is not None
            # self.assertIs(set(), None)
            self.assertIsNot(set(), None)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``set()``

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 4-5, 7-8

            self.assertIsNot([], None)

            a_set = set()
            # assert set() is not None
            assert a_set is not None
            # self.assertIs(set(), None)
            # self.assertIsNot(set(), None)
            self.assertIsNot(a_set, None)

  still green.

* I add a :ref:`variable<what is a variable?>` for ``[]``

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 3

            self.assertIsNot((), None)

            a_list = []
            assert [] is not None
            # self.assertIs([], None)
            self.assertIsNot([], None)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``[]``

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 4-5, 7-8

            self.assertIsNot((), None)

            a_list = []
            # assert [] is not None
            assert a_list is not None
            # self.assertIs([], None)
            # self.assertIsNot([], None)
            self.assertIsNot(a_list, None)

  green.

* I add a :ref:`variable<what is a variable?>` for ``()``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3

            self.assertIsNot('', None)

            a_tuple = ()
            assert () is not None
            # self.assertIs((), None)
            self.assertIsNot((), None)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``()``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4-5, 7-8

            self.assertIsNot('', None)

            a_tuple = ()
            # assert () is not None
            assert a_tuple is not None
            # self.assertIs((), None)
            # self.assertIsNot((), None)
            self.assertIsNot(a_tuple, None)

  still green.

* I add a :ref:`variable<what is a variable?>` for ``''``

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 3

            self.assertIsNot(0.0, None)

            a_string = ''
            assert '' is not None
            # self.assertIs('', None)
            self.assertIsNot('', None)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``''``

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 4-5, 7-8

            self.assertIsNot(0.0, None)

            a_string = ''
            # assert '' is not None
            assert a_string is not None
            # self.assertIs('', None)
            # self.assertIsNot('', None)
            self.assertIsNot(a_string, None)

  the test is still green.

* I add a :ref:`variable<what is a variable?>` for ``0.0``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 3

            self.assertIsNot(0, None)

            a_float = 0.0
            assert 0.0 is not None
            # self.assertIs(0.0, None)
            self.assertIsNot(0.0, None)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0.0``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 4-5, 7-8

            self.assertIsNot(0, None)

            a_float = 0.0
            # assert 0.0 is not None
            assert a_float is not None
            # self.assertIs(0.0, None)
            # self.assertIsNot(0.0, None)
            self.assertIsNot(a_float, None)

  still green.

* I add a :ref:`variable<what is a variable?>` for ``0``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 3

            self.assertIsNot(True, None)

            an_integer = 0
            assert 0 is not None
            # self.assertIs(0, None)
            self.assertIsNot(0, None)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 4-5, 7-8

            self.assertIsNot(True, None)

            an_integer = 0
            # assert 0 is not None
            assert an_integer is not None
            # self.assertIs(0, None)
            # self.assertIsNot(0, None)
            self.assertIsNot(an_integer, None)

  green.

* I remove the commented lines from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 20

            self.assertEqual(reality, my_expectation)

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)

            assert False is not None
            self.assertIsNot(False, None)

            assert True is not None
            self.assertIsNot(True, None)

            an_integer = 0
            assert an_integer is not None
            self.assertIsNot(an_integer, None)

            a_float = 0.0
            assert a_float is not None
            self.assertIsNot(a_float, None)

            a_string = ''
            assert a_string is not None
            self.assertIsNot(a_string, None)

            a_tuple = ()
            assert a_tuple is not None
            self.assertIsNot(a_tuple, None)

            a_list = []
            assert a_list is not None
            self.assertIsNot(a_list, None)

            a_set = set()
            assert a_set is not None
            self.assertIsNot(a_set, None)

            a_dictionary = {}
            assert a_dictionary is not None
            self.assertIsNot(a_dictionary, None)


    def test_assertion_error_w_false():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    move test_assertion_error_w_none to TestAssertionError

----

*********************************************************************************
test_assertion_error_w_false with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* 

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_assertion_error_w_false`

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    move test_assertion_error_w_false to TestAssertionError

----

*********************************************************************************
test_assertion_error_w_true with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail7
=================================================================================

----
* I go back to the terminal_ where the tests are running
----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_assertion_error_w_true`

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    move test_assertion_error_w_true to TestAssertionError

----

*********************************************************************************
test_assertion_error_w_equality with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----
* I go back to the terminal_ where the tests are running
----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_assertion_error_w_equality`

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    move test_assertion_error_w_equality to TestAssertionError

----

*********************************************************************************
test_assertion_error_w_is_vs_equal with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----
* I go back to the terminal_ where the tests are running
----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_assertion_error_w_is_vs_equal`

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    move test_assertion_error_w_is_vs_equal to TestAssertionError

----

*********************************************************************************
will_not_run with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----
* I go back to the terminal_ where the tests are running
----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`will not run<pytest only calls the function if the name starts with test>`

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    move will_not_run to TestAssertionError

----

*********************************************************************************
test_failure with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----
* I go back to the terminal_ where the tests are running
----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_failure`

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    move test_failure to TestAssertionError

----


*********************************************************************************
remove repetition with class attributes
*********************************************************************************

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

            a_tuple = (0, 1, 2, 'n')
            assert a_tuple is not None
            self.assertIsNot(a_tuple, None)

            a_list = [0, 1, 2, 'n']
            assert a_list is not None
            self.assertIsNot(a_list, None)

            a_set = {0, 1, 2, 'n'}
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

            a_tuple = (0, 1, 2, 'n')
            assert a_tuple is not False
            self.assertIsNot(a_tuple, False)

            a_list = [0, 1, 2, 'n']
            assert a_list is not False
            self.assertIsNot(a_list, False)

            a_set = {0, 1, 2, 'n'}
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

            a_tuple = (0, 1, 2, 'n')
            assert a_tuple is not True
            self.assertIsNot(a_tuple, True)

            a_list = [0, 1, 2, 'n']
            assert a_list is not True
            self.assertIsNot(a_list, True)

            a_set = {0, 1, 2, 'n'}
            assert a_set is not True
            self.assertIsNot(a_set, True)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality(self):

  green.

----

* I add a :ref:`class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

        def setUp(self):
            self.an_integer = 0
            self.a_float = 0.0

        def test_assert_keyword(self):

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

            a_tuple = (0, 1, 2, 'n')
            assert a_tuple is not None
            self.assertIsNot(a_tuple, None)

            a_list = [0, 1, 2, 'n']
            assert a_list is not None
            self.assertIsNot(a_list, None)

            a_set = {0, 1, 2, 'n'}
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

            a_tuple = (0, 1, 2, 'n')
            assert a_tuple is not False
            self.assertIsNot(a_tuple, False)

            a_list = [0, 1, 2, 'n']
            assert a_list is not False
            self.assertIsNot(a_list, False)

            a_set = {0, 1, 2, 'n'}
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

            a_tuple = (0, 1, 2, 'n')
            assert a_tuple is not True
            self.assertIsNot(a_tuple, True)

            a_list = [0, 1, 2, 'n']
            assert a_list is not True
            self.assertIsNot(a_list, True)

            a_set = {0, 1, 2, 'n'}
            assert a_set is not True
            self.assertIsNot(a_set, True)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality(self):

  still green.

----

* I add a :ref:`class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def setUp(self):
            self.an_integer = 0
            self.a_float = 0.0
            self.a_string = 'a string'

        def test_assert_keyword(self):

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

            a_tuple = (0, 1, 2, 'n')
            assert a_tuple is not None
            self.assertIsNot(a_tuple, None)

            a_list = [0, 1, 2, 'n']
            assert a_list is not None
            self.assertIsNot(a_list, None)

            a_set = {0, 1, 2, 'n'}
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

            a_tuple = (0, 1, 2, 'n')
            assert a_tuple is not False
            self.assertIsNot(a_tuple, False)

            a_list = [0, 1, 2, 'n']
            assert a_list is not False
            self.assertIsNot(a_list, False)

            a_set = {0, 1, 2, 'n'}
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

            a_tuple = (0, 1, 2, 'n')
            assert a_tuple is not True
            self.assertIsNot(a_tuple, True)

            a_list = [0, 1, 2, 'n']
            assert a_list is not True
            self.assertIsNot(a_list, True)

            a_set = {0, 1, 2, 'n'}
            assert a_set is not True
            self.assertIsNot(a_set, True)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality(self):

  the test is still green.

----

* I add a :ref:`class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5

        def setUp(self):
            self.an_integer = 0
            self.a_float = 0.0
            self.a_string = 'a string'
            self.a_tuple = (0, 1, 2, 'n')

        def test_assert_keyword(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_tuple = (0, 1, 2, 'n')`` from :ref:`test_assertion_error_w_none`

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

            # a_tuple = (0, 1, 2, 'n')
            # assert a_tuple is not None
            # self.assertIsNot(a_tuple, None)
            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)

            a_list = [0, 1, 2, 'n']
            assert a_list is not None
            self.assertIsNot(a_list, None)

            a_set = {0, 1, 2, 'n'}
            assert a_set is not None
            self.assertIsNot(a_set, None)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not None
            self.assertIsNot(a_dictionary, None)

        def test_assertion_error_w_false(self):

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_tuple = (0, 1, 2, 'n')`` from :ref:`test_assertion_error_w_false`

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

            # a_tuple = (0, 1, 2, 'n')
            # assert a_tuple is not False
            # self.assertIsNot(a_tuple, False)
            assert self.a_tuple is not False
            self.assertIsNot(self.a_tuple, False)

            a_list = [0, 1, 2, 'n']
            assert a_list is not False
            self.assertIsNot(a_list, False)

            a_set = {0, 1, 2, 'n'}
            assert a_set is not False
            self.assertIsNot(a_set, False)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not False
            self.assertIsNot(a_dictionary, False)

        def test_assertion_error_w_true(self):

  green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_tuple = (0, 1, 2, 'n')`` from :ref:`test_assertion_error_w_true`

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

            # a_tuple = (0, 1, 2, 'n')
            # assert a_tuple is not True
            # self.assertIsNot(a_tuple, True)
            assert self.a_tuple is not True
            self.assertIsNot(self.a_tuple, True)

            a_list = [0, 1, 2, 'n']
            assert a_list is not True
            self.assertIsNot(a_list, True)

            a_set = {0, 1, 2, 'n'}
            assert a_set is not True
            self.assertIsNot(a_set, True)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality(self):

  still green.

----

* I add a :ref:`class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 6

        def setUp(self):
            self.an_integer = 0
            self.a_float = 0.0
            self.a_string = 'a string'
            self.a_tuple = (0, 1, 2, 'n')
            self.a_list = [0, 1, 2, 'n']

        def test_assert_keyword(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_list = [0, 1, 2, 'n']`` from :ref:`test_assertion_error_w_none`

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

            # a_tuple = (0, 1, 2, 'n')
            # assert a_tuple is not None
            # self.assertIsNot(a_tuple, None)
            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)

            # a_list = [0, 1, 2, 'n']
            # assert a_list is not None
            # self.assertIsNot(a_list, None)
            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)

            a_set = {0, 1, 2, 'n'}
            assert a_set is not None
            self.assertIsNot(a_set, None)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not None
            self.assertIsNot(a_dictionary, None)

        def test_assertion_error_w_false(self):

  the test is still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_list = [0, 1, 2, 'n']`` from :ref:`test_assertion_error_w_false`

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

            # a_tuple = (0, 1, 2, 'n')
            # assert a_tuple is not False
            # self.assertIsNot(a_tuple, False)
            assert self.a_tuple is not False
            self.assertIsNot(self.a_tuple, False)

            # a_list = [0, 1, 2, 'n']
            # assert a_list is not False
            # self.assertIsNot(a_list, False)
            assert self.a_list is not False
            self.assertIsNot(self.a_list, False)

            a_set = {0, 1, 2, 'n'}
            assert a_set is not False
            self.assertIsNot(a_set, False)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not False
            self.assertIsNot(a_dictionary, False)

        def test_assertion_error_w_true(self):

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_list = [0, 1, 2, 'n']`` from :ref:`test_assertion_error_w_true`

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

            # a_tuple = (0, 1, 2, 'n')
            # assert a_tuple is not True
            # self.assertIsNot(a_tuple, True)
            assert self.a_tuple is not True
            self.assertIsNot(self.a_tuple, True)

            # a_list = [0, 1, 2, 'n']
            # assert a_list is not True
            # self.assertIsNot(a_list, True)
            assert self.a_list is not True
            self.assertIsNot(self.a_list, True)

            a_set = {0, 1, 2, 'n'}
            assert a_set is not True
            self.assertIsNot(a_set, True)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality(self):

  green.

----

* I add a :ref:`class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 7

        def setUp(self):
            self.an_integer = 0
            self.a_float = 0.0
            self.a_string = 'a string'
            self.a_tuple = (0, 1, 2, 'n')
            self.a_list = [0, 1, 2, 'n']
            self.a_set = {0, 1, 2, 'n'}

        def test_assert_keyword(self):

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_set = {0, 1, 2, 'n'}`` from :ref:`test_assertion_error_w_none`

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

            # a_tuple = (0, 1, 2, 'n')
            # assert a_tuple is not None
            # self.assertIsNot(a_tuple, None)
            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)

            # a_list = [0, 1, 2, 'n']
            # assert a_list is not None
            # self.assertIsNot(a_list, None)
            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)

            # a_set = {0, 1, 2, 'n'}
            # assert a_set is not None
            # self.assertIsNot(a_set, None)
            assert self.a_set is not None
            self.assertIsNot(self.a_set, None)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not None
            self.assertIsNot(a_dictionary, None)

        def test_assertion_error_w_false(self):

  still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_set = {0, 1, 2, 'n'}`` from :ref:`test_assertion_error_w_false`

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

            # a_tuple = (0, 1, 2, 'n')
            # assert a_tuple is not False
            # self.assertIsNot(a_tuple, False)
            assert self.a_tuple is not False
            self.assertIsNot(self.a_tuple, False)

            # a_list = [0, 1, 2, 'n']
            # assert a_list is not False
            # self.assertIsNot(a_list, False)
            assert self.a_list is not False
            self.assertIsNot(self.a_list, False)

            # a_set = {0, 1, 2, 'n'}
            # assert a_set is not False
            # self.assertIsNot(a_set, False)
            assert self.a_set is not False
            self.assertIsNot(self.a_set, False)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not False
            self.assertIsNot(a_dictionary, False)

        def test_assertion_error_w_true(self):

  the test is still green.

* I use the :ref:`class attribute<what is a class attribute?>` to remove repetition of ``a_set = {0, 1, 2, 'n'}`` from :ref:`test_assertion_error_w_true`

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

            # a_tuple = (0, 1, 2, 'n')
            # assert a_tuple is not True
            # self.assertIsNot(a_tuple, True)
            assert self.a_tuple is not True
            self.assertIsNot(self.a_tuple, True)

            # a_list = [0, 1, 2, 'n']
            # assert a_list is not True
            # self.assertIsNot(a_list, True)
            assert self.a_list is not True
            self.assertIsNot(self.a_list, True)

            # a_set = {0, 1, 2, 'n'}
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

* I add a :ref:`class attribute<what is a class attribute?>` to the  :ref:`setUp method<how to use the setUp method to reset class attributes for every test>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 8

        def setUp(self):
            self.an_integer = 0
            self.a_float = 0.0
            self.a_string = 'a string'
            self.a_tuple = (0, 1, 2, 'n')
            self.a_list = [0, 1, 2, 'n']
            self.a_set = {0, 1, 2, 'n'}
            self.a_dictionary = {'key': 'value'}

        def test_assert_keyword(self):

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

            # a_tuple = (0, 1, 2, 'n')
            # assert a_tuple is not None
            # self.assertIsNot(a_tuple, None)
            assert self.a_tuple is not None
            self.assertIsNot(self.a_tuple, None)

            # a_list = [0, 1, 2, 'n']
            # assert a_list is not None
            # self.assertIsNot(a_list, None)
            assert self.a_list is not None
            self.assertIsNot(self.a_list, None)

            # a_set = {0, 1, 2, 'n'}
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

            # a_tuple = (0, 1, 2, 'n')
            # assert a_tuple is not False
            # self.assertIsNot(a_tuple, False)
            assert self.a_tuple is not False
            self.assertIsNot(self.a_tuple, False)

            # a_list = [0, 1, 2, 'n']
            # assert a_list is not False
            # self.assertIsNot(a_list, False)
            assert self.a_list is not False
            self.assertIsNot(self.a_list, False)

            # a_set = {0, 1, 2, 'n'}
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

            # a_tuple = (0, 1, 2, 'n')
            # assert a_tuple is not True
            # self.assertIsNot(a_tuple, True)
            assert self.a_tuple is not True
            self.assertIsNot(self.a_tuple, True)

            # a_list = [0, 1, 2, 'n']
            # assert a_list is not True
            # self.assertIsNot(a_list, True)
            assert self.a_list is not True
            self.assertIsNot(self.a_list, True)

            # a_set = {0, 1, 2, 'n'}
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
        self.a_tuple = (0, 1, 2, 'n')
        self.a_list = [0, 1, 2, 'n']
        self.a_set = {0, 1, 2, 'n'}
        self.a_dictionary = {'key': 'value'}

        # def setUp(self):
        #    self.an_integer = 0
        #    self.a_float = 0.0
        #    self.a_string = 'a string'
        #    self.a_tuple = (0, 1, 2, 'n')
        #    self.a_list = [0, 1, 2, 'n']
        #    self.a_set = {0, 1, 2, 'n'}
        #    self.a_dictionary = {'key': 'value'}

        def test_assert_keyword(self):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

  because ``self`` is not defined outside the :ref:`methods<what is a method?>` I can declare the :ref:`class attributes<what is a class attribute?>` the same way I do :ref:`variables<what is a variable?>` as long as it is indented under the :ref:`class definition<how to make a class>`

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>`

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
        # self.a_tuple = (0, 1, 2, 'n')
        # self.a_list = [0, 1, 2, 'n']
        # self.a_set = {0, 1, 2, 'n'}
        # self.a_dictionary = {'key': 'value'}

        an_integer = 0
        a_float = 0.0
        a_string = 'a string'
        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}

        # def setUp(self):
        #     self.an_integer = 0
        #     self.a_float = 0.0
        #     self.a_string = 'a string'
        #     self.a_tuple = (0, 1, 2, 'n')
        #     self.a_list = [0, 1, 2, 'n']
        #     self.a_set = {0, 1, 2, 'n'}
        #     self.a_dictionary = {'key': 'value'}

        def test_assert_keyword(self):

  the test is green again.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 4

    class TestAssertionError(unittest.TestCase):

        an_integer = 0
        a_float = 0.0
        a_string = 'a string'
        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}

        def test_assert_keyword(self):

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

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what causes AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`how to make classes<classes>`
* :ref:`how to use class attributes to remove repetition<AssertionError 2: use class attributes>`

:ref:`Would you like to test what happens when classes have one or more parents?<family ties>`

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