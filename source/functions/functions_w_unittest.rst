.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): test functions with unittest — move the functions project's bare assert tests onto unittest.TestCase, then extract class attributes to remove repetition. Open functions; uv run pytest-watcher . --now (12 passed). Add class Functions then rename to TestFunctions → AttributeError: 'TestFunctions' object has no attribute 'assertEqual'. Parent unittest.TestCase → NameError name 'unittest' is not defined (pytest: Did you forget to import 'unittest'?); import unittest → AssertionError: True != False then green with assertEqual(False, False). For each of the 12 tests (test_making_a_function_w_pass through test_unknown_number_of_arguments): move into TestFunctions (first method replaces test_failure) → TypeError takes 0 positional arguments but 1 was given (need self); add assertIsNot / assertNotEqual → AssertionError e.g. unexpectedly identical: None, 'the same thing' == 'the same thing', <class 'object'> == <class 'object'>; switch to assertIs / assertEqual; keep helper assert_is_none plus self.assert*; remove the commented lines and unused assert_equal; git commit. Then extract class attributes first, last, a_tuple, a_list, a_set, a_dictionary and replace locals with self.first / self.last / self.a_tuple … in test_positional_arguments, test_keyword_arguments, and test_args_and_kwargs (keyword order still binds by name). Ends with TestFunctions + 6 class attrs + 12 methods + # Exceptions seen AssertionError NameError TypeError SyntaxError AttributeError. Review: unittest.TestCase methods or bare assert; class attributes for values that repeat. What is next: test person with unittest.
  :keywords: Jacob Itegboje, Pumping Python, test functions with unittest, functions unittest, TestFunctions, unittest.TestCase, import unittest, class attributes, self.first self.last, a_tuple a_list a_set a_dictionary, extract class attributes, AttributeError has no attribute assertEqual, NameError name 'unittest' is not defined, Did you forget to import unittest, AssertionError True != False, TypeError takes 0 positional arguments but 1 was given, self first argument method, assertIsNot, assertIs, assertNotEqual, assertEqual, unexpectedly identical None, the same thing, identity function None object, positional arguments, keyword arguments, args and kwargs, optional arguments, unknown_number_of_arguments, bare assert and assertEqual, uv run pytest-watcher . --now, red green refactor, remove the commented lines, git commit -am, another way to write tests, test_functions_w_unittest

.. include:: ../links.rst

#################################################################################
test functions with unittest
#################################################################################

I want to use the :ref:`unittest library<another way to write tests>` in the :ref:`functions<what is a function?>` project. I also want to use :ref:`class attributes<what is a class attribute?>` to remove repetition of some values from the tests.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/functions/tests/test_functions_w_unittest.py
  :caption: functions/tests/test_functions.py
  :language: python
  :linenos:
  :lines: 1-16

.. literalinclude:: ../code/functions/tests/test_functions_w_unittest.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 18
  :lines: 18-26

.. literalinclude:: ../code/functions/tests/test_functions_w_unittest.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 28
  :lines: 28-41

.. literalinclude:: ../code/functions/tests/test_functions_w_unittest.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 43
  :lines: 43-56

.. literalinclude:: ../code/functions/tests/test_functions_w_unittest.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 58
  :lines: 58-71

.. literalinclude:: ../code/functions/tests/test_functions_w_unittest.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 73
  :lines: 73-103

.. literalinclude:: ../code/functions/tests/test_functions_w_unittest.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 105
  :lines: 105-146

.. literalinclude:: ../code/functions/tests/test_functions_w_unittest.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 148
  :lines: 148-154

.. literalinclude:: ../code/functions/tests/test_functions_w_unittest.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 156
  :lines: 156-192

.. literalinclude:: ../code/functions/tests/test_functions_w_unittest.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 194
  :lines: 194-

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd functions

  the terminal_ shows I am in the ``functions`` folder_

  .. code-block:: python

    .../pumping_python/functions

* I open ``test_functions.py`` from the ``tests`` folder_

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    test_functions.py ............                      [100%]

    =================== 12 passed in G.HIs ===================

----

*********************************************************************************
add TestFunctions class
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a :ref:`class<everything is an object>` named ``Functions`` to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 5, 7-8

    def assert_is_none(something):
        assert something is None


    class Functions(object):

        def test_failure(self):
            self.assertEqual(True, False)


    def test_making_a_function_w_pass():
        assert_is_none(src.functions.w_pass())

  the test is still green.

* I change the name of the :ref:`class<everything is an object>` to ``TestFunctions``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 5-6

    def assert_is_none(something):
        assert something is None


    # class Functions(object):
    class TestFunctions(object):

        def test_failure(self):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'TestFunctions' object
                    has no attribute 'assertEqual'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`unittest.TestCase<test_dir_unittest_testcase>` as the parent :ref:`class<everything is an object>` of ``TestFunctions``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2-3

    # class Functions(object):
    # class TestFunctions(object):
    class TestFunctions(unittest.TestCase):

        def test_failure(self):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell

    NameError: name 'unittest' is not defined.
               Did you forget to import 'unittest'?

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import src.functions
    import unittest


    def assert_equal(input_1, input_2):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 6-7

    # class Functions(object):
    # class TestFunctions(object):
    class TestFunctions(unittest.TestCase):

        def test_failure(self):
            # self.assertEqual(True, False)
            self.assertEqual(False, False)


    def test_making_a_function_w_pass():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 9

    def assert_is_none(something):
        assert something is None


    class TestFunctions(unittest.TestCase):

        def test_failure(self):
            self.assertEqual(False, False)


    def test_making_a_function_w_pass():

* I open a new terminal_ then make sure I am in the ``functions`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd functions

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add TestFunctions class'

----

*********************************************************************************
test_making_a_function_w_pass with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I remove ``test_failure``

* I move :ref:`test_making_a_function_w_pass` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3-4

    class TestFunctions(unittest.TestCase):

        def test_making_a_function_w_pass():
            assert_is_none(src.functions.w_pass())


    def test_making_a_function_w_return():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestFunctions.test_making_a_function_w_pass() takes
               0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_making_a_function_w_pass`

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 3-4

  class TestFunctions(unittest.TestCase):

      # def test_making_a_function_w_pass():
      def test_making_a_function_w_pass(self):
          assert_is_none(src.functions.w_pass())

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertIsNot method<test_assert_is_not>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 4-6

        # def test_making_a_function_w_pass():
        def test_making_a_function_w_pass(self):
            assert_is_none(src.functions.w_pass())
            self.assertIsNot(
                src.functions.w_pass(), None
            )


    def test_making_a_function_w_return():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: None

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4-5

        # def test_making_a_function_w_pass():
        def test_making_a_function_w_pass(self):
            assert_is_none(src.functions.w_pass())
            # self.assertIsNot(
            self.assertIs(
                src.functions.w_pass(), None
            )


    def test_making_a_function_w_return():

  the test passes.

* I remove the commented lines from :ref:`test_making_a_function_w_pass`

  .. code-block:: python
    :lineno-start: 13

    class TestFunctions(unittest.TestCase):

        def test_making_a_function_w_pass(self):
            assert_is_none(src.functions.w_pass())
            self.assertIs(src.functions.w_pass(), None)


    def test_making_a_function_w_return():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_making_a_function_w_pass to TestFunctions'

----

*********************************************************************************
test_making_a_function_w_return with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_making_a_function_w_return` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3-4

            self.assertIs(src.functions.w_pass(), None)

        def test_making_a_function_w_return():
            assert_is_none(src.functions.w_return())


    def test_making_a_function_w_return_none():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestFunctions.test_making_a_function_w_return()
        takes 0 positional arguments but 1 was given

  because ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_making_a_function_w_return`

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 3-4

          self.assertIs(src.functions.w_pass(), None)

      # def test_making_a_function_w_return():
      def test_making_a_function_w_return(self):
          assert_is_none(src.functions.w_return())

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertIsNot method<test_assert_is_not>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4-6

        # def test_making_a_function_w_return():
        def test_making_a_function_w_return(self):
            assert_is_none(src.functions.w_return())
            self.assertIsNot(
                src.functions.w_return(), None
            )


    def test_making_a_function_w_return_none():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: None

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4-5

        # def test_making_a_function_w_return():
        def test_making_a_function_w_return(self):
            assert_is_none(src.functions.w_return())
            # self.assertIsNot(
            self.assertIs(
                src.functions.w_return(), None
            )

  the test passes.

* I remove the commented lines from :ref:`test_making_a_function_w_return`

  .. code-block:: python
    :lineno-start: 17

            self.assertIs(src.functions.w_pass(), None)

        def test_making_a_function_w_return(self):
            assert_is_none(src.functions.w_return())
            self.assertIs(
                src.functions.w_return(), None
            )


    def test_making_a_function_w_return_none():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_making_a_function_w_return to TestFunctions'

----

*********************************************************************************
test_making_a_function_w_return_none with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_making_a_function_w_return_none` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-6

            self.assertIs(
                src.functions.w_return(), None
            )

        def test_making_a_function_w_return_none():
            assert_is_none(src.functions.w_return_none())


    def test_what_happens_after_functions_return():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestFunctions.test_making_a_function_w_return_none()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_making_a_function_w_return_none`

.. code-block:: python
  :lineno-start: 21
  :emphasize-lines: 5-6

          self.assertIs(
              src.functions.w_return(), None
          )

      # def test_making_a_function_w_return_none():
      def test_making_a_function_w_return_none(self):
          assert_is_none(src.functions.w_return_none())

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertIsNot method<test_assert_is_not>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4-6

        # def test_making_a_function_w_return_none():
        def test_making_a_function_w_return_none(self):
            assert_is_none(src.functions.w_return_none())
            self.assertIsNot(
                src.functions.w_return_none(), None
            )


    def test_what_happens_after_functions_return():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: None

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4-5

        # def test_making_a_function_w_return_none():
        def test_making_a_function_w_return_none(self):
            assert_is_none(src.functions.w_return_none())
            # self.assertIsNot(
            self.assertIs(
                src.functions.w_return_none(), None
            )


    def test_what_happens_after_functions_return():

  the test passes.

* I remove the commented lines from :ref:`test_making_a_function_w_return_none`

  .. code-block:: python
    :lineno-start: 21

            self.assertIs(
                src.functions.w_return(), None
            )

        def test_making_a_function_w_return_none(self):
            assert_is_none(src.functions.w_return_none())
            self.assertIs(
                src.functions.w_return_none(), None
            )


    def test_what_happens_after_functions_return():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_making_a_function_w_return_none to TestFunctions'

----

*********************************************************************************
test_what_happens_after_functions_return with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_what_happens_after_functions_return` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 5-8

            self.assertIs(
                src.functions.w_return_none(), None
            )

        def test_what_happens_after_functions_return():
            assert_is_none(
                src.functions.return_leaves_the_function()
            )


    def test_constant_function():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestFunctions.test_what_happens_after_functions_return()
        takes 0 positional arguments but 1 was given

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_what_happens_after_functions_return`

.. code-block:: python
  :lineno-start: 27
  :emphasize-lines: 5-6

          self.assertIs(
              src.functions.w_return_none(), None
          )

      # def test_what_happens_after_functions_return():
      def test_what_happens_after_functions_return(self):
          assert_is_none(
              src.functions.return_leaves_the_function()
          )


  def test_constant_function():

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertIsNot method<test_assert_is_not>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 6-9

        # def test_what_happens_after_functions_return():
        def test_what_happens_after_functions_return(self):
            assert_is_none(
                src.functions.return_leaves_the_function()
            )
            self.assertIsNot(
                src.functions.return_leaves_the_function(),
                None
            )


    def test_constant_function():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: None

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 6-7

        # def test_what_happens_after_functions_return():
        def test_what_happens_after_functions_return(self):
            assert_is_none(
                src.functions.return_leaves_the_function()
            )
            # self.assertIsNot(
            self.assertIs(
                src.functions.return_leaves_the_function(),
                None
            )

  the test passes.

* I remove the commented lines from :ref:`test_what_happens_after_functions_return`

  .. code-block:: python
    :lineno-start: 27

            self.assertIs(
                src.functions.w_return_none(), None
            )

        def test_what_happens_after_functions_return(self):
            assert_is_none(
                src.functions.return_leaves_the_function()
            )
            self.assertIs(
                src.functions.return_leaves_the_function(),
                None
            )


    def test_constant_function():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_what_happens_after_functions_return to TestFunctions'

----

*********************************************************************************
test_constant_function with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_constant_function` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 6-9

            self.assertIs(
                src.functions.return_leaves_the_function(),
                None
            )

        def test_constant_function():
            assert_equal(
                src.functions.constant(), 'the same thing'
            )


    def test_identity_function():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestFunctions.test_constant_function()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>`...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_constant_function`

.. code-block:: python
  :lineno-start: 35
  :emphasize-lines: 6-7

          self.assertIs(
              src.functions.return_leaves_the_function(),
              None
          )

      # def test_constant_function():
      def test_constant_function(self):
          assert_equal(
              src.functions.constant(), 'the same thing'
          )

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 6-8

        # def test_constant_function():
        def test_constant_function(self):
            assert_equal(
                src.functions.constant(), 'the same thing'
            )
            self.assertNotEqual(
                src.functions.constant(), 'the same thing'
            )


    def test_identity_function():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'the same thing' == 'the same thing'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 6-7

        # def test_constant_function():
        def test_constant_function(self):
            assert_equal(
                src.functions.constant(), 'the same thing'
            )
            # self.assertNotEqual(
            self.assertEqual(
                src.functions.constant(), 'the same thing'
            )

  the test passes.

* I remove the commented lines and the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` (since it is now a repetition) from :ref:`test_constant_function`

  .. code-block:: python
    :lineno-start: 35

            self.assertIs(
                src.functions.return_leaves_the_function(),
                None
            )

        def test_constant_function(self):
            self.assertEqual(
                src.functions.constant(), 'the same thing'
            )


    def test_identity_function():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_constant_function to TestFunctions'

----

*********************************************************************************
test_identity_function with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_identity_function` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 6-10

        def test_constant_function(self):
            self.assertEqual(
                src.functions.constant(), 'the same thing'
            )

        def test_identity_function():
            assert_is_none(src.functions.identity(None))
            assert_equal(
                src.functions.identity(object), object
            )


    def test_why_use_a_function():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestFunctions.test_identity_function()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_identity_function`

.. code-block:: python
  :lineno-start: 40
  :emphasize-lines: 6-7

      def test_constant_function(self):
          self.assertEqual(
              src.functions.constant(), 'the same thing'
          )

      # def test_identity_function():
      def test_identity_function(self):
          assert_is_none(src.functions.identity(None))

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertIsNot<test_assert_is_not>` and :ref:`assertNotEqual methods<test_assert_not_equal>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4-6, 11-13

        # def test_identity_function():
        def test_identity_function(self):
            assert_is_none(src.functions.identity(None))
            self.assertIsNot(
                src.functions.identity(None), None
            )

            assert_equal(
                src.functions.identity(object), object
            )
            self.assertNotEqual(
                src.functions.identity(object), object
            )


    def test_why_use_a_function():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: None

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>` for the first :ref:`assertion<what is an assertion?>` in :ref:`test_identity_function`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4-5

        # def test_identity_function():
        def test_identity_function(self):
            assert_is_none(src.functions.identity(None))
            # self.assertIsNot(
            self.assertIs(
                src.functions.identity(None), None
            )

            assert_equal(
                src.functions.identity(object), object
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: <class 'object'> == <class 'object'>

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the second :ref:`assertion<what is an assertion?>` in :ref:`test_identity_function`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 4-5

            assert_equal(
                src.functions.identity(object), object
            )
            # self.assertNotEqual(
            self.assertEqual(
                src.functions.identity(object), object
            )


    def test_why_use_a_function():

  the test passes.

* I remove the commented lines and the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` from :ref:`test_identity_function`

  .. code-block:: python
    :lineno-start: 40

        def test_constant_function(self):
            self.assertEqual(
                src.functions.constant(), 'the same thing'
            )

        def test_identity_function(self):
            assert_is_none(src.functions.identity(None))
            self.assertIs(
                src.functions.identity(None), None
            )

            self.assertEqual(
                src.functions.identity(object), object
            )


    def test_why_use_a_function():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_identity_function to TestFunctions'

----

*********************************************************************************
test_why_use_a_function with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_why_use_a_function` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 5-7, 9-18

            self.assertEqual(
                src.functions.identity(object), object
            )

        def test_why_use_a_function():
            def add_x(number):
                return 3 + number

            assert_equal(add_x(0), 3)
            assert_equal(add_x(1), 4)
            assert_equal(add_x(2), 5)
            assert_equal(add_x(3), 6)
            assert_equal(add_x(4), 7)
            assert_equal(add_x(5), 8)
            assert_equal(add_x(6), 9)
            assert_equal(add_x(7), 10)
            assert_equal(add_x(8), 11)
            assert_equal(add_x(9), 12)


    def test_positional_arguments():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestFunctions.test_why_use_a_function()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_why_use_a_function`

.. code-block:: python
  :lineno-start: 51
  :emphasize-lines: 5-6

          self.assertEqual(
              src.functions.identity(object), object
          )

      # def test_why_use_a_function():
      def test_why_use_a_function(self):
          def add_x(number):
              return 3 + number

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_why_use_a_function`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 7, 9

        # def test_why_use_a_function():
        def test_why_use_a_function(self):
            def add_x(number):
                return 3 + number

            assert_equal(add_x(0), 3)
            self.assertNotEqual(add_x(0), 3)
            assert_equal(add_x(1), 4)
            self.assertNotEqual(add_x(1), 4)

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 2, 4, 6, 8

            assert_equal(add_x(2), 5)
            self.assertNotEqual(add_x(2), 5)
            assert_equal(add_x(3), 6)
            self.assertNotEqual(add_x(3), 6)
            assert_equal(add_x(4), 7)
            self.assertNotEqual(add_x(4), 7)
            assert_equal(add_x(5), 8)
            self.assertNotEqual(add_x(5), 8)

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 2, 4, 6, 8

            assert_equal(add_x(6), 9)
            self.assertNotEqual(add_x(6), 9)
            assert_equal(add_x(7), 10)
            self.assertNotEqual(add_x(7), 10)
            assert_equal(add_x(8), 11)
            self.assertNotEqual(add_x(8), 11)
            assert_equal(add_x(9), 12)
            self.assertNotEqual(add_x(9), 12)


    def test_positional_arguments():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`.

* I change the :ref:`calls<how to call a function with input>` from :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_why_use_a_function`

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2-3, 5-6

            assert_equal(add_x(0), 3)
            # self.assertNotEqual(add_x(0), 3)
            self.assertEqual(add_x(0), 3)
            assert_equal(add_x(1), 4)
            # self.assertNotEqual(add_x(1), 4)
            self.assertEqual(add_x(1), 4)

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 2-3, 5-6

            assert_equal(add_x(2), 5)
            # self.assertNotEqual(add_x(2), 5)
            self.assertEqual(add_x(2), 5)
            assert_equal(add_x(3), 6)
            # self.assertNotEqual(add_x(3), 6)
            self.assertEqual(add_x(3), 6)

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 2-3, 5-6

            assert_equal(add_x(4), 7)
            # self.assertNotEqual(add_x(4), 7)
            self.assertEqual(add_x(4), 7)
            assert_equal(add_x(5), 8)
            # self.assertNotEqual(add_x(5), 8)
            self.assertEqual(add_x(5), 8)

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 2-3, 5-6

            assert_equal(add_x(6), 9)
            # self.assertNotEqual(add_x(6), 9)
            self.assertEqual(add_x(6), 9)
            assert_equal(add_x(7), 10)
            # self.assertNotEqual(add_x(7), 10)
            self.assertEqual(add_x(7), 10)

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2-3, 5-6

            assert_equal(add_x(8), 11)
            # self.assertNotEqual(add_x(8), 11)
            self.assertEqual(add_x(8), 11)
            assert_equal(add_x(9), 12)
            # self.assertNotEqual(add_x(9), 12)
            self.assertEqual(add_x(9), 12)


    def test_positional_arguments():

  the test passes.

* I remove the commented lines and the :ref:`calls<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` from :ref:`test_why_use_a_function`

  .. code-block:: python
    :lineno-start: 51

            self.assertEqual(
                src.functions.identity(object), object
            )

        def test_why_use_a_function(self):
            def add_x(number):
                return 3 + number

            self.assertEqual(add_x(0), 3)
            self.assertEqual(add_x(1), 4)
            self.assertEqual(add_x(2), 5)
            self.assertEqual(add_x(3), 6)
            self.assertEqual(add_x(4), 7)
            self.assertEqual(add_x(5), 8)
            self.assertEqual(add_x(6), 9)
            self.assertEqual(add_x(7), 10)
            self.assertEqual(add_x(8), 11)
            self.assertEqual(add_x(9), 12)


    def test_positional_arguments():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_why_use_a_function to TestFunctions'

----

*********************************************************************************
test_positional_arguments with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_positional_arguments` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 3-7

            self.assertEqual(add_x(9), 12)

        def test_positional_arguments():
            positional_arguments = (
                src.functions.positional_arguments
            )
            first, last = 'first', 'last'

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 1-8, 10-12

            assert_equal(
                positional_arguments(first, last),
                (first, last)
            )
            assert_equal(
                positional_arguments(last, first),
                (last, first)
            )

            assert_equal(
                positional_arguments(0, 1), (0, 1)
            )


  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 1-6, 8-15

            a_tuple = (0, 1, 2, 'n')
            a_list = [0, 1, 2, 'n']
            assert_equal(
                positional_arguments(a_tuple, a_list),
                (a_tuple, a_list)
            )

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            assert_equal(
                src.functions.keyword_arguments(
                    a_set, a_dictionary,
                ),
                (a_set, a_dictionary)
            )


    def test_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestFunctions.test_positional_arguments()
        takes 0 positional arguments but 1 was given

  because ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_positional_arguments`

.. code-block:: python
  :lineno-start: 68
  :emphasize-lines: 3-4

          self.assertEqual(add_x(9), 12)

      # def test_positional_arguments():
      def test_positional_arguments(self):
          positional_arguments = (
              src.functions.positional_arguments
          )

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 5-8, 13-16

            assert_equal(
                positional_arguments(first, last),
                (first, last)
            )
            self.assertNotEqual(
                positional_arguments(first, last),
                (first, last)
            )
            assert_equal(
                positional_arguments(last, first),
                (last, first)
            )
            self.assertNotEqual(
                positional_arguments(last, first),
                (last, first)
            )

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 4-6

            assert_equal(
                positional_arguments(0, 1), (0, 1)
            )
            self.assertNotEqual(
                positional_arguments(0, 1), (0, 1)
            )

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 7-10

            a_tuple = (0, 1, 2, 'n')
            a_list = [0, 1, 2, 'n']
            assert_equal(
                positional_arguments(a_tuple, a_list),
                (a_tuple, a_list)
            )
            self.assertNotEqual(
                positional_arguments(a_tuple, a_list),
                (a_tuple, a_list)
            )

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 9-14

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            assert_equal(
                src.functions.keyword_arguments(
                    a_set, a_dictionary,
                ),
                (a_set, a_dictionary)
            )
            self.assertNotEqual(
                src.functions.keyword_arguments(
                    a_set, a_dictionary
                ),
                (a_set, a_dictionary)
            )


    def test_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`.

* I change the :ref:`calls<how to call a function with input>` from :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 5-6, 14-15

            assert_equal(
                positional_arguments(first, last),
                (first, last)
            )
            # self.assertNotEqual(
            self.assertEqual(
                positional_arguments(first, last),
                (first, last)
            )
            assert_equal(
                positional_arguments(last, first),
                (last, first)
            )
            # self.assertNotEqual(
            self.assertEqual(
                positional_arguments(last, first),
                (last, first)
            )

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 4-5

            assert_equal(
                positional_arguments(0, 1), (0, 1)
            )
            # self.assertNotEqual(
            self.assertEqual(
                positional_arguments(0, 1), (0, 1)
            )

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 7-8

            a_tuple = (0, 1, 2, 'n')
            a_list = [0, 1, 2, 'n']
            assert_equal(
                positional_arguments(a_tuple, a_list),
                (a_tuple, a_list)
            )
            # self.assertNotEqual(
            self.assertEqual(
                positional_arguments(a_tuple, a_list),
                (a_tuple, a_list)
            )

  .. code-block:: python
    :lineno-start: 116
    :emphasize-lines: 9-10

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            assert_equal(
                src.functions.keyword_arguments(
                    a_set, a_dictionary,
                ),
                (a_set, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                src.functions.keyword_arguments(
                    a_set, a_dictionary
                ),
                (a_set, a_dictionary)
            )


    def test_keyword_arguments():

  the test passes.

* I remove the commented lines and the :ref:`calls<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` from :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 68

            self.assertEqual(add_x(9), 12)

        def test_positional_arguments(self):
            positional_arguments = (
                src.functions.positional_arguments
            )
            first, last = 'first', 'last'

  .. code-block:: python
    :lineno-start: 76

            self.assertEqual(
                positional_arguments(first, last),
                (first, last)
            )
            self.assertEqual(
                positional_arguments(last, first),
                (last, first)
            )

  .. code-block:: python
    :lineno-start: 85

            self.assertEqual(
                positional_arguments(0, 1), (0, 1)
            )

  .. code-block:: python
    :lineno-start: 89

            a_tuple = (0, 1, 2, 'n')
            a_list = [0, 1, 2, 'n']
            self.assertEqual(
                positional_arguments(a_tuple, a_list),
                (a_tuple, a_list)
            )

  .. code-block:: python
    :lineno-start: 96

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                src.functions.keyword_arguments(
                    a_set, a_dictionary
                ),
                (a_set, a_dictionary)
            )


    def test_keyword_arguments():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_positional_arguments to TestFunctions'

----

*********************************************************************************
test_keyword_arguments with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_keyword_arguments` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 10-14

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                src.functions.keyword_arguments(
                    a_set, a_dictionary
                ),
                (a_set, a_dictionary)
            )

        def test_keyword_arguments():
            keyword_arguments = (
                src.functions.keyword_arguments
            )
            first, last = 'first', 'last'

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 1-12

            assert_equal(
                keyword_arguments(
                    first_input=first, last_input=last,
                ),
                (first, last)
            )
            assert_equal(
                keyword_arguments(
                    last_input=last, first_input=first,
                ),
                (first, last)
            )

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 1-6

            assert_equal(
                keyword_arguments(
                    last_input=0, first_input=1,
                ),
                (1, 0)
            )

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 1-9

            a_tuple = (0, 1, 2, 'n')
            a_list = [0, 1, 2, 'n']
            assert_equal(
                keyword_arguments(
                    first_input=a_tuple,
                    last_input=a_list,
                ),
                (a_tuple, a_list)
            )

  .. code-block:: python
    :lineno-start: 141
    :emphasize-lines: 1-9

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            assert_equal(
                src.functions.positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                ),
                (a_set, a_dictionary)
            )


    def test_args_and_kwargs():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestFunctions.test_keyword_arguments()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_keyword_arguments`

.. code-block:: python
  :lineno-start: 96
  :emphasize-lines: 10-11

          a_set = {0, 1, 2, 'n'}
          a_dictionary = {'key': 'value'}
          self.assertEqual(
              src.functions.keyword_arguments(
                  a_set, a_dictionary
              ),
              (a_set, a_dictionary)
          )

      # def test_keyword_arguments():
      def test_keyword_arguments(self):
          keyword_arguments = (
              src.functions.keyword_arguments
          )
          first, last = 'first', 'last'v

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 7-12, 19-24

            assert_equal(
                keyword_arguments(
                    first_input=first, last_input=last,
                ),
                (first, last)
            )
            self.assertNotEqual(
                keyword_arguments(
                    first_input=first, last_input=last,
                ),
                (first, last)
            )
            assert_equal(
                keyword_arguments(
                    last_input=last, first_input=first,
                ),
                (first, last)
            )
            self.assertNotEqual(
                keyword_arguments(
                    last_input=last, first_input=first,
                ),
                (first, last)
            )

  .. code-block:: python
    :lineno-start: 137
    :emphasize-lines: 7-12

            assert_equal(
                keyword_arguments(
                    last_input=0, first_input=1,
                ),
                (1, 0)
            )
            self.assertNotEqual(
                keyword_arguments(
                    last_input=0, first_input=1,
                ),
                (1, 0)
            )

  .. code-block:: python
    :lineno-start: 150
    :emphasize-lines: 10-16

            a_tuple = (0, 1, 2, 'n')
            a_list = [0, 1, 2, 'n']
            assert_equal(
                keyword_arguments(
                    first_input=a_tuple,
                    last_input=a_list,
                ),
                (a_tuple, a_list)
            )
            self.assertNotEqual(
                keyword_arguments(
                    first_input=a_tuple,
                    last_input=a_list,
                ),
                (a_tuple, a_list)
            )

  .. code-block:: python
    :lineno-start: 167
    :emphasize-lines: 10-16

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            assert_equal(
                src.functions.positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                ),
                (a_set, a_dictionary)
            )
            self.assertNotEqual(
                src.functions.positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                ),
                (a_set, a_dictionary)
            )


    def test_args_and_kwargs():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`.

* I change the :ref:`calls<how to call a function with input>` from :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 7-8, 20-21

            assert_equal(
                keyword_arguments(
                    first_input=first, last_input=last,
                ),
                (first, last)
            )
            # self.assertNotEqual(
            self.assertEqual(
                keyword_arguments(
                    first_input=first, last_input=last,
                ),
                (first, last)
            )
            assert_equal(
                keyword_arguments(
                    last_input=last, first_input=first,
                ),
                (first, last)
            )
            # self.assertNotEqual(
            self.assertEqual(
                keyword_arguments(
                    last_input=last, first_input=first,
                ),
                (first, last)
            )

  .. code-block:: python
    :lineno-start: 139
    :emphasize-lines: 7-8

            assert_equal(
                keyword_arguments(
                    last_input=0, first_input=1,
                ),
                (1, 0)
            )
            # self.assertNotEqual(
            self.assertEqual(
                keyword_arguments(
                    last_input=0, first_input=1,
                ),
                (1, 0)
            )

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 10-11

            a_tuple = (0, 1, 2, 'n')
            a_list = [0, 1, 2, 'n']
            assert_equal(
                keyword_arguments(
                    first_input=a_tuple,
                    last_input=a_list,
                ),
                (a_tuple, a_list)
            )
            # self.assertNotEqual(
            self.assertEqual(
                keyword_arguments(
                    first_input=a_tuple,
                    last_input=a_list,
                ),
                (a_tuple, a_list)
            )

  .. code-block:: python
    :lineno-start: 171
    :emphasize-lines: 10-11

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            assert_equal(
                src.functions.positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                ),
                (a_set, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                src.functions.positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                ),
                (a_set, a_dictionary)
            )


    def test_args_and_kwargs():

  the test passes.

* I remove the commented lines and the :ref:`calls<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` from :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 96

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                src.functions.keyword_arguments(
                    a_set, a_dictionary
                ),
                (a_set, a_dictionary)
            )

        def test_keyword_arguments(self):
            keyword_arguments = (
                src.functions.keyword_arguments
            )
            first, last = 'first', 'last'

  .. code-block:: python
    :lineno-start: 111

            self.assertEqual(
                keyword_arguments(
                    first_input=first, last_input=last,
                ),
                (first, last)
            )
            self.assertEqual(
                keyword_arguments(
                    last_input=last, first_input=first,
                ),
                (first, last)
            )

  .. code-block:: python
    :lineno-start: 124

            self.assertEqual(
                keyword_arguments(
                    last_input=0, first_input=1,
                ),
                (1, 0)
            )

  .. code-block:: python
    :lineno-start: 131

            a_tuple = (0, 1, 2, 'n')
            a_list = [0, 1, 2, 'n']
            self.assertEqual(
                keyword_arguments(
                    first_input=a_tuple,
                    last_input=a_list,
                ),
                (a_tuple, a_list)
            )

  .. code-block:: python
    :lineno-start: 141

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                src.functions.positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                ),
                (a_set, a_dictionary)
            )


    def test_args_and_kwargs():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_keyword_arguments to TestFunctions'

----

*********************************************************************************
test_args_and_kwargs with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_args_and_kwargs` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 141
    :emphasize-lines: 11-12, 14-19

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                src.functions.positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                ),
                (a_set, a_dictionary)
            )

        def test_args_and_kwargs():
            first, last = 'first', 'last'

            assert_equal(
                src.functions.args_and_kwargs(
                    first, last_input=last
                ),
                (first, last)
            )


    def test_optional_arguments():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestFunctions.test_args_and_kwargs()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_args_and_kwargs`

.. code-block:: python
  :lineno-start: 141
  :emphasize-lines: 11-12

          a_set = {0, 1, 2, 'n'}
          a_dictionary = {'key': 'value'}
          self.assertEqual(
              src.functions.positional_arguments(
                  last_input=a_dictionary,
                  first_input=a_set,
              ),
              (a_set, a_dictionary)
          )

      # def test_args_and_kwargs():
      def test_args_and_kwargs(self):
          first, last = 'first', 'last'


the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 11-16

        # def test_args_and_kwargs():
        def test_args_and_kwargs(self):
            first, last = 'first', 'last'

            assert_equal(
                src.functions.args_and_kwargs(
                    first, last_input=last
                ),
                (first, last)
            )
            self.assertNotEqual(
                src.functions.args_and_kwargs(
                    first, last_input=last
                ),
                (first, last)
            )


    def test_optional_arguments():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ('first', 'last') == ('first', 'last')

* I change the :ref:`call<how to call a function with input>` from :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 7-8

            assert_equal(
                src.functions.args_and_kwargs(
                    first, last_input=last
                ),
                (first, last)
            )
            # self.assertNotEqual(
            self.assertEqual(
                src.functions.args_and_kwargs(
                    first, last_input=last
                ),
                (first, last)
            )

  the test passes.

* I add :ref:`variables<what is a variable?>` for the :ref:`call<how to call a function with input>` to ``src.functions.args_and_kwargs`` and my expectation

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 5-8

            assert_equal(
                src.functions.args_and_kwargs(
                    first, last_input=last
                ),
                (first, last)
            )
            # self.assertNotEqual(
            self.assertEqual(
                src.functions.args_and_kwargs(
                    first, last_input=last
                ),
                (first, last)
            )

* I remove the commented lines and the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` from :ref:`test_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 141

            a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                src.functions.positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                ),
                (a_set, a_dictionary)
            )

        def test_args_and_kwargs(self):
            first, last = 'first', 'last'

            self.assertEqual(
                src.functions.args_and_kwargs(
                    first, last_input=last
                ),
                (first, last)
            )


    def test_optional_arguments():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_args_and_kwargs to TestFunctions'

----

*********************************************************************************
test_optional_arguments with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_optional_arguments` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 8-11, 13-19

            self.assertEqual(
                src.functions.args_and_kwargs(
                    first, last_input=last
                ),
                (first, last)
            )

        def test_optional_arguments():
            optional_arguments = (
                src.functions.optional_arguments
            )

            first_name, last_name = 'jane', 'doe'
            assert_equal(
                optional_arguments(
                    first_name,
                ),
                (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 174
    :emphasize-lines: 1-7

            first_name, blow = 'joe', 'blow'
            assert_equal(
                optional_arguments(
                    first_name, blow
                ),
                (first_name, blow)
            )

  .. code-block:: python
    :lineno-start: 182
    :emphasize-lines: 1-7

            first_name = 'john'
            assert_equal(
                optional_arguments(
                    first_input=first_name,
                ),
                (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 1-8

            last_name = 'smith'
            assert_equal(
                optional_arguments(
                    last_input=last_name,
                    first_input=first_name,
                ),
                (first_name, last_name)
            )


    def test_unknown_number_of_arguments():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestFunctions.test_optional_arguments()
        takes 0 positional arguments but 1 was given

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_optional_arguments`

.. code-block:: python
  :lineno-start: 154
  :emphasize-lines: 8-9

          self.assertEqual(
              src.functions.args_and_kwargs(
                  first, last_input=last
              ),
              (first, last)
          )

      # def test_optional_arguments():
      def test_optional_arguments(self):
          optional_arguments = (
              src.functions.optional_arguments
          )

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_optional_arguments`

  .. code-block:: python
    :lineno-start: 167
    :emphasize-lines: 8-13

            first_name, last_name = 'jane', 'doe'
            assert_equal(
                optional_arguments(
                    first_name,
                ),
                (first_name, last_name)
            )
            self.assertNotEqual(
                optional_arguments(
                    first_name,
                ),
                (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 181
    :emphasize-lines: 8-13

            first_name, blow = 'joe', 'blow'
            assert_equal(
                optional_arguments(
                    first_name, blow
                ),
                (first_name, blow)
            )
            self.assertNotEqual(
                optional_arguments(
                    first_name, blow
                ),
                (first_name, blow)
            )

  .. code-block:: python
    :lineno-start: 195
    :emphasize-lines: 8-13

            first_name = 'john'
            assert (
                optional_arguments(
                    first_input=first_name
                )
            == (first_name, last_name)
            )
            self.assertNotEqual(
                optional_arguments(
                    first_input=first_name
                ),
                (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 209
    :emphasize-lines: 9-15

            last_name = 'smith'
            assert (
                optional_arguments(
                    last_input=last_name,
                    first_input=first_name,
                )
            == (first_name, last_name)
            )
            self.assertNotEqual(
                optional_arguments(
                    last_input=last_name,
                    first_input=first_name,
                ),
                (first_name, last_name)
            )


    def test_unknown_number_of_arguments():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`.

* I change the :ref:`calls<how to call a function with input>` from :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_optional_arguments`

  .. code-block:: python
    :lineno-start: 167
    :emphasize-lines: 8-9

            first_name, last_name = 'jane', 'doe'
            assert_equal(
                optional_arguments(
                    first_name,
                ),
                (first_name, last_name)
            )
            # self.assertNotEqual(
            self.assertEqual(
                optional_arguments(
                    first_name,
                ),
                (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 182
    :emphasize-lines: 8-9

            first_name, blow = 'joe', 'blow'
            assert_equal(
                optional_arguments(
                    first_name, blow
                ),
                (first_name, blow)
            )
            # self.assertNotEqual(
            self.assertEqual(
                optional_arguments(
                    first_name, blow
                ),
                (first_name, blow)
            )

  .. code-block:: python
    :lineno-start: 197
    :emphasize-lines: 8-9

            first_name = 'john'
            assert_equal(
                optional_arguments(
                    first_input=first_name,
                ),
                (first_name, last_name)
            )
            # self.assertNotEqual(
            self.assertEqual(
                optional_arguments(
                    first_input=first_name,
                ),
                (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 212
    :emphasize-lines: 9-10

                last_name = 'smith'
                assert_equal(
                    optional_arguments(
                        last_input=last_name,
                        first_input=first_name,
                    ),
                    (first_name, last_name)
                )
                # self.assertNotEqual(
                self.assertEqual(
                    optional_arguments(
                        last_input=last_name,
                        first_input=first_name,
                    ),
                    (first_name, last_name)
                )


        def test_unknown_number_of_arguments():

  the test passes.

* I remove the commented lines and the :ref:`calls<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` from :ref:`test_optional_arguments`

  .. code-block:: python
    :lineno-start: 154

            self.assertEqual(
                src.functions.args_and_kwargs(
                    first, last_input=last
                ),
                (first, last)
            )

        def test_optional_arguments(self):
            optional_arguments = (
                src.functions.optional_arguments
            )

            first_name, last_name = 'jane', 'doe'
            self.assertEqual(
                optional_arguments(
                    first_name,
                ),
                (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 174

            first_name, blow = 'joe', 'blow'
            self.assertEqual(
                optional_arguments(
                    first_name, blow
                ),
                (first_name, blow)
            )

  .. code-block:: python
    :lineno-start: 182

            first_name = 'john'
            self.assertEqual(
                optional_arguments(
                    first_input=first_name,
                ),
                (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 190

            last_name = 'smith'
            self.assertEqual(
                optional_arguments(
                    last_input=last_name,
                    first_input=first_name,
                ),
                (first_name, last_name)
            )


    def test_unknown_number_of_arguments():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_optional_arguments to TestFunctions'

----

*********************************************************************************
test_unknown_number_of_arguments with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_unknown_number_of_arguments` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 10-13, 15-22

            last_name = 'smith'
            self.assertEqual(
                optional_arguments(
                    last_input=last_name,
                    first_input=first_name,
                ),
                (first_name, last_name)
            )

        def test_unknown_number_of_arguments():
            unknown_number_of_arguments = (
                src.functions.unknown_number_of_arguments
            )

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3}
            assert_equal(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 213
    :emphasize-lines: 1-7

            a_dictionary = {'a': 2, 'b': 3, 'c': 4}
            assert_equal(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary,
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 221
    :emphasize-lines: 1-8

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}
            assert_equal(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 230
    :emphasize-lines: 1-5

            a_tuple = (0, 1, 2, 'n')
            assert_equal(
                unknown_number_of_arguments(*a_tuple),
                (a_tuple, {})
            )

  .. code-block:: python
    :lineno-start: 236
    :emphasize-lines: 1-5, 7-9

            a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
            assert_equal(
                unknown_number_of_arguments(**a_dictionary),
                ((), a_dictionary)
            )

            assert_equal(
                unknown_number_of_arguments(), ((), {})
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestFunctions.test_unknown_number_of_arguments()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_unknown_number_of_arguments`

.. code-block:: python
  :lineno-start: 190
  :emphasize-lines: 10-11

          last_name = 'smith'
          self.assertEqual(
              optional_arguments(
                  last_input=last_name,
                  first_input=first_name,
              ),
              (first_name, last_name)
          )

      # def test_unknown_number_of_arguments():
      def test_unknown_number_of_arguments(self):
          unknown_number_of_arguments = (
              src.functions.unknown_number_of_arguments
          )

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_unknown_number_of_arguments`

  .. code-block:: python
    :lineno-start: 205
    :emphasize-lines: 9-14

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3}
            assert_equal(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )
            self.assertNotEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 220
    :emphasize-lines: 8-13

            a_dictionary = {'a': 2, 'b': 3, 'c': 4}
            assert_equal(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary,
                ),
                (a_tuple, a_dictionary)
            )
            self.assertNotEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 234
    :emphasize-lines: 9-14

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}
            assert_equal(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )
            self.assertNotEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 249
    :emphasize-lines: 6-9

            a_tuple = (0, 1, 2, 'n')
            assert_equal(
                unknown_number_of_arguments(*a_tuple),
                (a_tuple, {})
            )
            self.assertNotEqual(
                unknown_number_of_arguments(*a_tuple),
                (a_tuple, {})
            )

  .. code-block:: python
    :lineno-start: 259
    :emphasize-lines: 6-9, 14-16

            a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
            assert_equal(
                unknown_number_of_arguments(**a_dictionary),
                ((), a_dictionary)
            )
            self.assertNotEqual(
                unknown_number_of_arguments(**a_dictionary),
                ((), a_dictionary)
            )

            assert_equal(
                unknown_number_of_arguments(), ((), {})
            )
            self.assertNotEqual(
                unknown_number_of_arguments(), ((), {})
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`.

* I change the :ref:`calls<how to call a function with input>` from :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_unknown_number_of_arguments`

  .. code-block:: python
    :lineno-start: 205
    :emphasize-lines: 9-10

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3}
            assert_equal(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 221
    :emphasize-lines: 8-9

            a_dictionary = {'a': 2, 'b': 3, 'c': 4}
            assert_equal(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary,
                ),
                (a_tuple, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 236
    :emphasize-lines: 9-10

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}
            assert_equal(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 252
    :emphasize-lines: 6-7

            a_tuple = (0, 1, 2, 'n')
            assert_equal(
                unknown_number_of_arguments(*a_tuple),
                (a_tuple, {})
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(*a_tuple),
                (a_tuple, {})
            )

  .. code-block:: python
    :lineno-start: 263
    :emphasize-lines: 6-7, 15-16

            a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
            assert_equal(
                unknown_number_of_arguments(**a_dictionary),
                ((), a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(**a_dictionary),
                ((), a_dictionary)
            )

            assert_equal(
                unknown_number_of_arguments(), ((), {})
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(), ((), {})
            )


    # Exceptions seen

  the test passes.

* I remove the commented lines and the :ref:`calls<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` from :ref:`test_unknown_number_of_arguments`

  .. code-block:: python
    :lineno-start: 190

            last_name = 'smith'
            self.assertEqual(
                optional_arguments(
                    last_input=last_name,
                    first_input=first_name,
                ),
                (first_name, last_name)
            )

        def test_unknown_number_of_arguments(self):
            unknown_number_of_arguments = (
                src.functions.unknown_number_of_arguments
            )

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3}
            self.assertEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 213

            a_dictionary = {'a': 2, 'b': 3, 'c': 4}
            self.assertEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 221

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}
            self.assertEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 230

            a_tuple = (0, 1, 2, 'n')
            self.assertEqual(
                unknown_number_of_arguments(*a_tuple),
                (a_tuple, {})
            )

  .. code-block:: python
    :lineno-start: 236

            a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
            self.assertEqual(
                unknown_number_of_arguments(**a_dictionary),
                ((), a_dictionary)
            )

            self.assertEqual(
                unknown_number_of_arguments(), ((), {})
            )


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # SyntaxError
    # AttributeError

* I remove my :ref:`assert_equal function<extract assert_equal function>` since it is no longer used

  .. code-block:: python
    :linenos:

    import src.functions
    import unittest


    def assert_is_none(something):
        assert something is None


    class TestFunctions(unittest.TestCase):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_unknown_number_of_arguments to TestFunctions'

----

*********************************************************************************
extract first, last class attributes
*********************************************************************************

I want to use :ref:`class attributes<what is a class attribute?>` to remove repetition from the tests.

* I go back to the terminal_ where the tests are running

* I add :ref:`class attributes<what is a class attribute?>` for ``'first'`` and ``'last'``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3-4

    class TestFunctions(unittest.TestCase):

        first = 'first'
        last = 'last'

        def test_making_a_function_w_pass(self):

* I use the :ref:`class attributes<what is a class attribute?>` for ``first`` and ``last`` in :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 5, 8-11, 14-17

        def test_positional_arguments(self):
            positional_arguments = (
                src.functions.positional_arguments
            )
            # first, last = 'first', 'last'

            self.assertEqual(
                # positional_arguments(first, last),
                positional_arguments(self.first, self.last),
                # (first, last)
                (self.first, self.last)
            )
            self.assertEqual(
                # positional_arguments(last, first),
                positional_arguments(self.last, self.first),
                # (last, first)
                (self.last, self.first)
            )

  the test is still green.

* I use the :ref:`class attributes<what is a class attribute?>` for ``first`` and ``last`` in :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 5, 9-11, 13-14, 18-20, 22-23

        def test_keyword_arguments(self):
            keyword_arguments = (
                src.functions.keyword_arguments
            )
            # first, last = 'first', 'last'

            self.assertEqual(
                keyword_arguments(
                    # first_input=first, last_input=last,
                    first_input=self.first,
                    last_input=self.last,
                ),
                # (first, last)
                (self.first, self.last)
            )
            self.assertEqual(
                keyword_arguments(
                    # last_input=last, first_input=first,
                    last_input=self.last,
                    first_input=self.first,
                ),
                # (first, last)
                (self.first, self.last)
            )

  still green.

* I use the :ref:`class attributes<what is a class attribute?>` for ``first`` and ``last`` in :ref:`test_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 160
    :emphasize-lines: 2, 6-7, 9-10

        def test_args_and_kwargs(self):
            # first, last = 'first', 'last'

            self.assertEqual(
                src.functions.args_and_kwargs(
                    # first, last_input=last
                    self.first, last_input=self.last
                ),
                # (first, last)
                (self.first, self.last)
            )

        def test_optional_arguments(self):

  green.

* I remove the commented lines from :ref:`test_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 160

        def test_args_and_kwargs(self):
            self.assertEqual(
                src.functions.args_and_kwargs(
                    self.first, last_input=self.last
                ),
                (self.first, self.last)
            )

        def test_optional_arguments(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract first, last class attributes'

----

*********************************************************************************
extract a_tuple class attribute
*********************************************************************************

* I add a :ref:`class attribute<what is a class attribute?>` for ``(0, 1, 2, 'n')``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5

    class TestFunctions(unittest.TestCase):

        first = 'first'
        last = 'last'
        a_tuple = (0, 1, 2, 'n')

        def test_making_a_function_w_pass(self):

* I use the new :ref:`class attribute<what is a class attribute?>` for ``a_tuple`` in :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 5, 8-13

            self.assertEqual(
                positional_arguments(0, 1), (0, 1)
            )

            # a_tuple = (0, 1, 2, 'n')
            a_list = [0, 1, 2, 'n']
            self.assertEqual(
                # positional_arguments(a_tuple, a_list),
                positional_arguments(
                    self.a_tuple, a_list
                ),
                # (a_tuple, a_list)
                (self.a_tuple, a_list)
            )

            a_set = {0, 1, 2, 'n'}

  still green.

* I use the new :ref:`class attribute<what is a class attribute?>` for ``a_tuple`` in :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 8, 12-13, 16-17

            self.assertEqual(
                keyword_arguments(
                    last_input=0, first_input=1,
                ),
                (1, 0)
            )

            # a_tuple = (0, 1, 2, 'n')
            a_list = [0, 1, 2, 'n']
            self.assertEqual(
                keyword_arguments(
                    # first_input=a_tuple,
                    first_input=self.a_tuple,
                    last_input=a_list,
                ),
                # (a_tuple, a_list)
                (self.a_tuple, a_list)
            )

            a_set = {0, 1, 2, 'n'}


  the test is still green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract a_tuple class attribute'

----

*********************************************************************************
extract a_list class attribute
*********************************************************************************

* I add a :ref:`class attribute<what is a class attribute?>` for ``[0, 1, 2, 'n']``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 6

    class TestFunctions(unittest.TestCase):

        first = 'first'
        last = 'last'
        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']

        def test_making_a_function_w_pass(self):

* I use the new :ref:`class attribute<what is a class attribute?>` for ``a_list`` in :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 2, 6-7, 10-11

            # a_tuple = (0, 1, 2, 'n')
            # a_list = [0, 1, 2, 'n']
            self.assertEqual(
                # positional_arguments(a_tuple, a_list),
                positional_arguments(
                    # self.a_tuple, a_list
                    self.a_tuple, self.a_list
                ),
                # (a_tuple, a_list)
                # (self.a_tuple, a_list)
                (self.a_tuple, self.a_list)
            )

            a_set = {0, 1, 2, 'n'}

  still green.

* I use the new :ref:`class attribute<what is a class attribute?>` for ``a_list`` in :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 2, 7-8, 11-12

            # a_tuple = (0, 1, 2, 'n')
            # a_list = [0, 1, 2, 'n']
            self.assertEqual(
                keyword_arguments(
                    # first_input=a_tuple,
                    first_input=self.a_tuple,
                    # last_input=a_list,
                    last_input=self.a_list,
                ),
                # (a_tuple, a_list)
                # (self.a_tuple, a_list)
                (self.a_tuple, self.a_list)
            )

            a_set = {0, 1, 2, 'n'}

  green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract a_list class attribute'

----

*********************************************************************************
extract a_set class attribute
*********************************************************************************

* I add a :ref:`class attribute<what is a class attribute?>` for ``{0, 1, 2, 'n'}``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 7

    class TestFunctions(unittest.TestCase):

        first = 'first'
        last = 'last'
        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        a_set = {0, 1, 2, 'n'}

        def test_making_a_function_w_pass(self):

* I use the new :ref:`class attribute<what is a class attribute?>` to remove repetition of ``{0, 1, 2, 'n'}`` from :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 1, 5-6, 8-9

            # a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                src.functions.keyword_arguments(
                    # a_set, a_dictionary
                    self.a_set, a_dictionary
                ),
                # (a_set, a_dictionary)
                (self.a_set, a_dictionary)
            )

        def test_keyword_arguments(self):

  still green.

* I use the new :ref:`class attributes<what is a class attribute?>` to remove repetition of ``{0, 1, 2, 'n'}`` from :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 165
    :emphasize-lines: 1, 5-6, 9-10

            # a_set = {0, 1, 2, 'n'}
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                src.functions.positional_arguments(
                    last_input=a_dictionary,
                    # first_input=a_set,
                    first_input=self.a_set,
                ),
                # (a_set, a_dictionary)
                (self.a_set, a_dictionary)
            )

        def test_args_and_kwargs(self):

  still green

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract a_set class attribute'

----

*********************************************************************************
extract a_dictionary class attribute
*********************************************************************************

* I add a :ref:`class attribute<what is a class attribute?>` for ``a_dictionary``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 8

    class TestFunctions(unittest.TestCase):

        first = 'first'
        last = 'last'
        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}

        def test_making_a_function_w_pass(self):

* I use the new :ref:`class attribute<what is a class attribute?>` for ``a_dictionary`` in :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 2, 6-7, 10-11

            # a_set = {0, 1, 2, 'n'}
            # a_dictionary = {'key': 'value'}
            self.assertEqual(
                src.functions.keyword_arguments(
                    # a_set, a_dictionary
                    # self.a_set, a_dictionary
                    self.a_set, self.a_dictionary
                ),
                # (a_set, a_dictionary)
                # (self.a_set, a_dictionary)
                (self.a_set, self.a_dictionary)
            )

        def test_keyword_arguments(self):

  the test is still green.

* I remove the commented lines from :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 73

        def test_positional_arguments(self):
            positional_arguments = (
                src.functions.positional_arguments
            )

            self.assertEqual(
                positional_arguments(self.first, self.last),
                (self.first, self.last)
            )
            self.assertEqual(
                positional_arguments(self.last, self.first),
                (self.last, self.first)
            )

            self.assertEqual(
                positional_arguments(0, 1), (0, 1)
            )

  .. code-block:: python
    :lineno-start: 91

            self.assertEqual(
                positional_arguments(
                    self.a_tuple, self.a_list
                ),
                (self.a_tuple, self.a_list)
            )

            self.assertEqual(
                src.functions.keyword_arguments(
                    self.a_set, self.a_dictionary
                ),
                (self.a_set, self.a_dictionary)
            )

        def test_keyword_arguments(self):

* I use the new :ref:`class attributes<what is a class attribute?>` for ``a_dictionary`` in :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 2, 5-6, 11-12

            # a_set = {0, 1, 2, 'n'}
            # a_dictionary = {'key': 'value'}
            self.assertEqual(
                src.functions.positional_arguments(
                    # last_input=a_dictionary,
                    last_input=self.a_dictionary,
                    # first_input=a_set,
                    first_input=self.a_set,
                ),
                # (a_set, a_dictionary)
                # (self.a_set, a_dictionary)
                (self.a_set, self.a_dictionary)
            )

        def test_args_and_kwargs(self):

  the test is still green.

* I remove the commented lines from :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 105

        def test_keyword_arguments(self):
            keyword_arguments = (
                src.functions.keyword_arguments
            )

            self.assertEqual(
                keyword_arguments(
                    first_input=self.first,
                    last_input=self.last,
                ),
                (self.first, self.last)
            )
            self.assertEqual(
                keyword_arguments(
                    last_input=self.last,
                    first_input=self.first,
                ),
                (self.first, self.last)
            )

  .. code-block:: python
    :lineno-start: 125

            self.assertEqual(
                keyword_arguments(
                    last_input=0, first_input=1,
                ),
                (1, 0)
            )

            self.assertEqual(
                keyword_arguments(
                    first_input=self.a_tuple,
                    last_input=self.a_list,
                ),
                (self.a_tuple, self.a_list)
            )

            self.assertEqual(
                src.functions.positional_arguments(
                    last_input=self.a_dictionary,
                    first_input=self.a_set,
                ),
                (self.a_set, self.a_dictionary)
            )

        def test_args_and_kwargs(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract a_dictionary class attribute'

:ref:`I can use class attributes to remove repetition<what is a class attribute?>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_functions.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``functions``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

* I can use the :ref:`unittest library<another way to write tests>` to write tests with the :ref:`methods of the unittest.TestCase class<test_dir_unittest_testcase>` or I can write them with bare :ref:`assert statements<what is an assertion?>`.
* I can use :ref:`class attributes<what is a class attribute?>` for things that repeat so that :ref:`methods<what is a method?>` of the same :ref:`class<everything is an object>` can use them.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test functions with unittest: tests>`

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

:ref:`Would you like to test the person project with the unittest library?<test person with unittest>`

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