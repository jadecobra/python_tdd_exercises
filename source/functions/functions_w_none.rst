.. meta::
  :description:
  :keywords:

.. include:: ../links.rst

#################################################################################
test functions with assertIsNotNone and assertIsNone
#################################################################################

I want to use the :ref:`unittest library<another way to write tests>` in the :ref:`functions` project.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/functions/tests/test_functions_w_unittest.py
  :language: python
  :linenos:

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

* I open ``test_functions.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

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
    :linenos:
    :emphasize-lines: 4, 6-7

    import src.functions


    class Functions(object):

        def test_failure(self):
            self.assertEqual(True, False)


    def test_making_a_function_w_pass():

  the test is still green.

* I change the name of the :ref:`class<everything is an object>` to ``TestFunctions``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import src.functions


    # class Functions(object):
    class TestFunctions(object):

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
    :linenos:
    :emphasize-lines: 5-6

    import src.functions


    # class Functions(object):
    # class TestFunctions(object):
    class TestFunctions(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'unittest' is not defined.
               Did you forget to import 'unittest'?

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import src.functions
    import unittest


    # class Functions(object):
    # class TestFunctions(object):
    class TestFunctions(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 5
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
    :linenos:

    import src.functions
    import unittest


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

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_making_a_function_w_pass` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>` and replace ``test_failure``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-4

    class TestFunctions(unittest.TestCase):

        def test_making_a_function_w_pass():
            assert src.functions.w_pass() is None


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
  :lineno-start: 7
  :emphasize-lines: 1-2

      # def test_making_a_function_w_pass():
      def test_making_a_function_w_pass(self):
          assert src.functions.w_pass() is None

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertIsNot method<test_assert_is_not>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4-6

        # def test_making_a_function_w_pass():
        def test_making_a_function_w_pass(self):
            assert src.functions.w_pass() is None
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
            assert src.functions.w_pass() is None
            # self.assertIsNot(
            self.assertIs(
                src.functions.w_pass(), None
            )


    def test_making_a_function_w_return():

  the test passes.

* I add a :ref:`variable<what is a variable?>` for ``src.functions.w_pass()``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3

        # def test_making_a_function_w_pass():
        def test_making_a_function_w_pass(self):
            result = src.functions.w_pass()

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.functions.w_pass()``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4-5, 8-9

        # def test_making_a_function_w_pass():
        def test_making_a_function_w_pass(self):
            result = src.functions.w_pass()
            # assert src.functions.w_pass() is None
            assert result is None
            # self.assertIsNot(
            self.assertIs(
                # src.functions.w_pass(), None
                result, None
            )


    def test_making_a_function_w_return():

* I remove the commented lines from :ref:`test_making_a_function_w_pass`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 7

    class TestFunctions(unittest.TestCase):

        def test_making_a_function_w_pass(self):
            result = src.functions.w_pass()

            assert result is None
            self.assertIs(result, None)


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

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_making_a_function_w_return` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3-4

            self.assertIs(result, None)

        def test_making_a_function_w_return():
            assert src.functions.w_return() is None


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
  :lineno-start: 13
  :emphasize-lines: 1-2

      # def test_making_a_function_w_return():
      def test_making_a_function_w_return(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertIsNot method<test_assert_is_not>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4-6

        # def test_making_a_function_w_return():
        def test_making_a_function_w_return(self):
            assert src.functions.w_return() is None
            self.assertIsNot(
                src.functions.w_return(), None
            )


    def test_making_a_function_w_return_none():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: None

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4-5

        # def test_making_a_function_w_return():
        def test_making_a_function_w_return(self):
            assert src.functions.w_return() is None
            # self.assertIsNot(
            self.assertIs(
                src.functions.w_return(), None
            )


    def test_making_a_function_w_return_none():

  the test passes.

* I add a :ref:`variable<what is a variable?>` for ``src.functions.w_return()``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

        # def test_making_a_function_w_return():
        def test_making_a_function_w_return(self):
            result = src.functions.w_return()

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.functions.w_return()``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4-5, 8-9

        # def test_making_a_function_w_return():
        def test_making_a_function_w_return(self):
            result = src.functions.w_return()
            # assert src.functions.w_return() is None
            assert result is None
            # self.assertIsNot(
            self.assertIs(
                # src.functions.w_return(), None
                result, None
            )


    def test_making_a_function_w_return_none():

* I remove the commented lines from :ref:`test_making_a_function_w_return`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 7

            self.assertIs(result, None)

        def test_making_a_function_w_return(self):
            result = src.functions.w_return()

            assert result is None
            self.assertIs(result, None)


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

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_making_a_function_w_return_none` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3-4

            self.assertIs(result, None)

        def test_making_a_function_w_return_none():
            assert src.functions.w_return_none() is None


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
  :lineno-start: 19
  :emphasize-lines: 1-2

      # def test_making_a_function_w_return_none():
      def test_making_a_function_w_return_none(self):
          assert src.functions.w_return_none() is None

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertIsNot method<test_assert_is_not>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4-6

        # def test_making_a_function_w_return_none():
        def test_making_a_function_w_return_none(self):
            assert src.functions.w_return_none() is None
            self.assertIsNot(
                src.functions.w_return_none(), None
            )


    def test_what_happens_after_functions_return():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: None

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4-5

        # def test_making_a_function_w_return_none():
        def test_making_a_function_w_return_none(self):
            assert src.functions.w_return_none() is None
            # self.assertIsNot(
            self.assertIs(
                src.functions.w_return_none(), None
            )


    def test_what_happens_after_functions_return():

  the test passes.

* I add a :ref:`variable<what is a variable?>` for ``src.functions.w_return_none()``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3

        # def test_making_a_function_w_return_none():
        def test_making_a_function_w_return_none(self):
            result = src.functions.w_return_none()

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.functions.w_return_none()``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4-5, 8-9

        # def test_making_a_function_w_return_none():
        def test_making_a_function_w_return_none(self):
            result = src.functions.w_return_none()
            # assert src.functions.w_return_none() is None
            assert result is None
            # self.assertIsNot(
            self.assertIs(
                # src.functions.w_return_none(), None
                result, None
            )


    def test_what_happens_after_functions_return():

* I remove the commented lines from :ref:`test_making_a_function_w_return_none`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 7

            self.assertIs(result, None)

        def test_making_a_function_w_return_none(self):
            result = src.functions.w_return_none()

            assert result is None
            self.assertIs(result, None)


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

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_what_happens_after_functions_return` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-7

            self.assertIs(result, None)

        def test_what_happens_after_functions_return():
            assert (
                src.functions
                   .return_leaves_the_function()
            ) is None


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
  :lineno-start: 25
  :emphasize-lines: 1-2

      # def test_what_happens_after_functions_return():
      def test_what_happens_after_functions_return(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertIsNot method<test_assert_is_not>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 7-13

        # def test_what_happens_after_functions_return():
        def test_what_happens_after_functions_return(self):
            assert (
                src.functions
                   .return_leaves_the_function()
            ) is None
            self.assertIsNot(
                (
                    src.functions
                       .return_leaves_the_function()
                ),
                None
            )


    def test_constant_function():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: None

* I change :ref:`assertIsNot<test_assert_is_not>` to :ref:`assertIs<test_assert_is>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 7-8

        # def test_what_happens_after_functions_return():
        def test_what_happens_after_functions_return(self):
            assert (
                src.functions
                   .return_leaves_the_function()
            ) is None
            # self.assertIsNot(
            self.assertIs(
                (
                    src.functions
                       .return_leaves_the_function()
                ),
                None
            )


    def test_constant_function():

  the test passes.

* I add a :ref:`variable<what is a variable?>` for ``src.functions.return_leaves_the_function()``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3

        # def test_what_happens_after_functions_return():
        def test_what_happens_after_functions_return(self):
            result = src.functions.return_leaves_the_function()

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.functions.return_leaves_the_function()``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4-7, 9-17

        # def test_what_happens_after_functions_return():
        def test_what_happens_after_functions_return(self):
            result = src.functions.return_leaves_the_function()
            # assert (
            #     src.functions
            #        .return_leaves_the_function()
            # ) is None
            # self.assertIsNot(
            # self.assertIs(
            #     (
            #         src.functions
            #            .return_leaves_the_function()
            #     ),
            #     None
            # )
            assert result is None
            self.assertIs(result, None)


    def test_constant_function():

* I remove the commented lines from :ref:`test_what_happens_after_functions_return`

  .. code-block:: python
    :lineno-start: 23

            self.assertIs(result, None)

        def test_what_happens_after_functions_return(self):
            result = src.functions.return_leaves_the_function()

            assert result is None
            self.assertIs(result, None)


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

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_constant_function` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3-4

            self.assertIs(result, None)

        def test_constant_function():
            assert src.functions.constant() == 'the same thing'


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
  :lineno-start: 31
  :emphasize-lines: 1-2

      # def test_constant_function():
      def test_constant_function(self):
          assert src.functions.constant() == 'the same thing'

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 4-7

        # def test_constant_function():
        def test_constant_function(self):
            assert src.functions.constant() == 'the same thing'
            self.assertNotEqual(
                src.functions.constant(),
                'the same thing'
            )


    def test_identity_function():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'the same thing' == 'the same thing'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 4-5

        # def test_constant_function():
        def test_constant_function(self):
            assert src.functions.constant() == 'the same thing'
            # self.assertNotEqual(
            self.assertEqual(
                src.functions.constant(),
                'the same thing'
            )


    def test_identity_function():

  the test passes.

* I add :ref:`variables<what is a variable?>` for ``src.functions.constant()`` and ``'the same thing'``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 3-4

        # def test_constant_function():
        def test_constant_function(self):
            result = src.functions.constant()
            expectation = 'the same thing'
            assert src.functions.constant() == 'the same thing'

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.functions.constant()`` and ``'the same thing'``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 5, 7-12

        # def test_constant_function():
        def test_constant_function(self):
            result = src.functions.constant()
            expectation = 'the same thing'
            # assert src.functions.constant() == 'the same thing'
            # self.assertNotEqual(
            # self.assertEqual(
            #     src.functions.constant(),
            #     'the same thing'
            # )
            assert result == expectation
            self.assertEqual(result, expectation)


    def test_identity_function():

* I remove the commented lines from :ref:`test_constant_function`

  .. code-block:: python
    :lineno-start: 29

            self.assertIs(result, None)

        def test_constant_function(self):
            result = src.functions.constant()
            expectation = 'the same thing'

            assert result == expectation
            self.assertEqual(result, expectation)


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

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_identity_function` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 3-5

            self.assertEqual(result, expectation)

        def test_identity_function():
            assert src.functions.identity(None) == None
            assert src.functions.identity(object) == object


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
  :lineno-start: 38
  :emphasize-lines: 1-2

      # def test_identity_function():
      def test_identity_function(self):

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 4-6, 8-10

        # def test_identity_function():
        def test_identity_function(self):
            assert src.functions.identity(None) == None
            self.assertNotEqual(
                src.functions.identity(None), None
            )
            assert src.functions.identity(object) == object
            self.assertNotEqual(
                src.functions.identity(object), object
            )


    def test_why_use_a_function():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None == None

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the first :ref:`assertion<what is an assertion?>` in :ref:`test_identity_function`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 4-5

        # def test_identity_function():
        def test_identity_function(self):
            assert src.functions.identity(None) == None
            # self.assertNotEqual(
            self.assertEqual(
                src.functions.identity(None), None
            )
            assert src.functions.identity(object) == object
            self.assertNotEqual(
                src.functions.identity(object), object
            )


    def test_why_use_a_function():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: <class 'object'> == <class 'object'>

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the second :ref:`assertion<what is an assertion?>` in :ref:`test_identity_function`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 9-10

        # def test_identity_function():
        def test_identity_function(self):
            assert src.functions.identity(None) == None
            # self.assertNotEqual(
            self.assertEqual(
                src.functions.identity(None), None
            )
            assert src.functions.identity(object) == object
            # self.assertNotEqual(
            self.assertEqual(
                src.functions.identity(object), object
            )


    def test_why_use_a_function():

  the test passes.

* I add :ref:`variables<what is a variable?>` for ``src.functions.identity``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 3, 10

        # def test_identity_function():
        def test_identity_function(self):
            result = src.functions.identity(None)
            assert src.functions.identity(None) == None
            # self.assertNotEqual(
            self.assertEqual(
                src.functions.identity(None), None
            )

            result = src.functions.identity(object)
            assert src.functions.identity(object) == object
            # self.assertNotEqual(
            self.assertEqual(
                src.functions.identity(object), object
            )


    def test_why_use_a_function():

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``src.functions.identity``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 4-5, 8-9, 13-14, 17-18

        # def test_identity_function():
        def test_identity_function(self):
            result = src.functions.identity(None)
            # assert src.functions.identity(None) == None
            assert result == None
            # self.assertNotEqual(
            self.assertEqual(
                # src.functions.identity(None), None
                result, None
            )

            result = src.functions.identity(object)
            # assert src.functions.identity(object) == object
            assert result == object
            # self.assertNotEqual(
            self.assertEqual(
                # src.functions.identity(object), object
                result, object
            )


    def test_why_use_a_function():

* I remove the commented lines from :ref:`test_identity_function`

  .. code-block:: python
    :lineno-start: 36

            self.assertEqual(result, expectation)

        def test_identity_function(self):
            result = src.functions.identity(None)

            assert result == None
            self.assertEqual(result, None)

            result = src.functions.identity(object)

            assert result == object
            self.assertEqual(result, object)


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

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_why_use_a_function` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 3-5, 7-16

            self.assertEqual(result, object)

        def test_why_use_a_function():
            def add_x(number):
                return 3 + number

            assert add_x(0) == 3
            assert add_x(1) == 4
            assert add_x(2) == 5
            assert add_x(3) == 6
            assert add_x(4) == 7
            assert add_x(5) == 8
            assert add_x(6) == 9
            assert add_x(7) == 10
            assert add_x(8) == 11
            assert add_x(9) == 12


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
  :lineno-start: 49
  :emphasize-lines: 1-2

      # def test_why_use_a_function():
      def test_why_use_a_function(self):
          def add_x(number):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_why_use_a_function`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 7, 9

        # def test_why_use_a_function():
        def test_why_use_a_function(self):
            def add_x(number):
                return 3 + number

            assert add_x(0) == 3
            self.assertNotEqual(add_x(0), 3)
            assert add_x(1) == 4
            self.assertNotEqual(add_x(1), 4)

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 2, 4, 6, 8

            assert add_x(2) == 5
            self.assertNotEqual(add_x(2), 5)
            assert add_x(3) == 6
            self.assertNotEqual(add_x(3), 6)
            assert add_x(4) == 7
            self.assertNotEqual(add_x(4), 7)
            assert add_x(5) == 8
            self.assertNotEqual(add_x(5), 8)

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 2, 4, 6, 8

            assert add_x(6) == 9
            self.assertNotEqual(add_x(6), 9)
            assert add_x(7) == 10
            self.assertNotEqual(add_x(7), 10)
            assert add_x(8) == 11
            self.assertNotEqual(add_x(8), 11)
            assert add_x(9) == 12
            self.assertNotEqual(add_x(9), 12)


    def test_positional_arguments():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`.

* I change the :ref:`calls<how to call a function with input>` from :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_why_use_a_function`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 7-8, 10-11

        # def test_why_use_a_function():
        def test_why_use_a_function(self):
            def add_x(number):
                return 3 + number

            assert add_x(0) == 3
            # self.assertNotEqual(add_x(0), 3)
            self.assertEqual(add_x(0), 3)
            assert add_x(1) == 4
            # self.assertNotEqual(add_x(1), 4)
            self.assertEqual(add_x(1), 4)

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2-3, 5-6

            assert add_x(2) == 5
            # self.assertNotEqual(add_x(2), 5)
            self.assertEqual(add_x(2), 5)
            assert add_x(3) == 6
            # self.assertNotEqual(add_x(3), 6)
            self.assertEqual(add_x(3), 6)

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 2-3, 5-6

            assert add_x(4) == 7
            # self.assertNotEqual(add_x(4), 7)
            self.assertEqual(add_x(4), 7)
            assert add_x(5) == 8
            # self.assertNotEqual(add_x(5), 8)
            self.assertEqual(add_x(5), 8)

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 2-3, 5-6

            assert add_x(6) == 9
            # self.assertNotEqual(add_x(6), 9)
            self.assertEqual(add_x(6), 9)
            assert add_x(7) == 10
            # self.assertNotEqual(add_x(7), 10)
            self.assertEqual(add_x(7), 10)

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 2-3, 5-6

            assert add_x(8) == 11
            # self.assertNotEqual(add_x(8), 11)
            self.assertEqual(add_x(8), 11)
            assert add_x(9) == 12
            # self.assertNotEqual(add_x(9), 12)
            self.assertEqual(add_x(9), 12)


    def test_positional_arguments():

  the test passes.

* I add :ref:`variables<what is a variable?>` for ``add_x`` and the expectations

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 6-7

        # def test_why_use_a_function():
        def test_why_use_a_function(self):
            def add_x(number):
                return 3 + number

            result = add_x(0)
            expectation = 3
            assert add_x(0) == 3
            # self.assertNotEqual(add_x(0), 3)
            self.assertEqual(add_x(0), 3)

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 1-2

            result = add_x(1)
            expectation = 4
            assert add_x(1) == 4
            # self.assertNotEqual(add_x(1), 4)
            self.assertEqual(add_x(1), 4)

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 1-2

            result = add_x(2)
            expectation = 5
            assert add_x(2) == 5
            # self.assertNotEqual(add_x(2), 5)
            self.assertEqual(add_x(2), 5)

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 1-2

            result = add_x(3)
            expectation = 6
            assert add_x(3) == 6
            # self.assertNotEqual(add_x(3), 6)
            self.assertEqual(add_x(3), 6)

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 1-2

            result = add_x(4)
            expectation = 7
            assert add_x(4) == 7
            # self.assertNotEqual(add_x(4), 7)
            self.assertEqual(add_x(4), 7)

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 1-2

            result = add_x(5)
            expectation = 8
            assert add_x(5) == 8
            # self.assertNotEqual(add_x(5), 8)
            self.assertEqual(add_x(5), 8)

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 1-2

            result = add_x(6)
            expectation = 9
            assert add_x(6) == 9
            # self.assertNotEqual(add_x(6), 9)
            self.assertEqual(add_x(6), 9)

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 1-2

            result = add_x(7)
            expectation = 10
            assert add_x(7) == 10
            # self.assertNotEqual(add_x(7), 10)
            self.assertEqual(add_x(7), 10)

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 1-2

            result = add_x(8)
            expectation = 11
            assert add_x(8) == 11
            # self.assertNotEqual(add_x(8), 11)
            self.assertEqual(add_x(8), 11)

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 1-2

            result = add_x(9)
            expectation = 12
            assert add_x(9) == 12
            # self.assertNotEqual(add_x(9), 12)
            self.assertEqual(add_x(9), 12)


    def test_positional_arguments():

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``add_x`` and the expectations

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 8-12

        # def test_why_use_a_function():
        def test_why_use_a_function(self):
            def add_x(number):
                return 3 + number

            result = add_x(0)
            expectation = 3
            # assert add_x(0) == 3
            # self.assertNotEqual(add_x(0), 3)
            # self.assertEqual(add_x(0), 3)
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3-7

            result = add_x(1)
            expectation = 4
            # assert add_x(1) == 4
            # self.assertNotEqual(add_x(1), 4)
            # self.assertEqual(add_x(1), 4)
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 3-7

            result = add_x(2)
            expectation = 5
            # assert add_x(2) == 5
            # self.assertNotEqual(add_x(2), 5)
            # self.assertEqual(add_x(2), 5)
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 3-7

            result = add_x(3)
            expectation = 6
            # assert add_x(3) == 6
            # self.assertNotEqual(add_x(3), 6)
            # self.assertEqual(add_x(3), 6)
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 3-7

            result = add_x(4)
            expectation = 7
            # assert add_x(4) == 7
            # self.assertNotEqual(add_x(4), 7)
            # self.assertEqual(add_x(4), 7)
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 3-7

            result = add_x(5)
            expectation = 8
            # assert add_x(5) == 8
            # self.assertNotEqual(add_x(5), 8)
            # self.assertEqual(add_x(5), 8)
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 3-7

            result = add_x(6)
            expectation = 9
            # assert add_x(6) == 9
            # self.assertNotEqual(add_x(6), 9)
            # self.assertEqual(add_x(6), 9)
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 3-7

            result = add_x(7)
            expectation = 10
            # assert add_x(7) == 10
            # self.assertNotEqual(add_x(7), 10)
            # self.assertEqual(add_x(7), 10)
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 3-7

            result = add_x(8)
            expectation = 11
            # assert add_x(8) == 11
            # self.assertNotEqual(add_x(8), 11)
            # self.assertEqual(add_x(8), 11)
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 126
    :emphasize-lines: 3-7

            result = add_x(9)
            expectation = 12
            # assert add_x(9) == 12
            # self.assertNotEqual(add_x(9), 12)
            # self.assertEqual(add_x(9), 12)
            assert result == expectation
            self.assertEqual(result, expectation)


    def test_positional_arguments():

  the test is still green.

* I remove the commented lines from :ref:`test_why_use_a_function`

  .. code-block:: python
    :lineno-start: 47

            self.assertEqual(result, object)

        def test_why_use_a_function(self):
            def add_x(number):
                return 3 + number

            result = add_x(0)
            expectation = 3
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 58

            result = add_x(1)
            expectation = 4
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 63

            result = add_x(2)
            expectation = 5
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 68

            result = add_x(3)
            expectation = 6
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 73

            result = add_x(4)
            expectation = 7
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 78

            result = add_x(5)
            expectation = 8
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 83

            result = add_x(6)
            expectation = 9
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 88

            result = add_x(7)
            expectation = 10
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 93

            result = add_x(8)
            expectation = 11
            assert result == expectation
            self.assertEqual(result, expectation)

  .. code-block:: python
    :lineno-start: 98

            result = add_x(9)
            expectation = 12
            assert result == expectation
            self.assertEqual(result, expectation)


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

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_positional_arguments` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 3-7

            self.assertEqual(result, expectation)

        def test_positional_arguments():
            positional_arguments = (
                src.functions.positional_arguments
            )
            first, last = 'first', 'last'

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 1-12

            assert (
                positional_arguments(first, last)
            == (first, last)
            )
            assert (
                positional_arguments(last, first)
            == (last, first)
            )
            assert (
                positional_arguments(0, 1)
            == (0, 1)
            )

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 1-6

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']
            assert (
                positional_arguments(a_tuple, a_list)
            == (a_tuple, a_list)
            )

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 1-11

            keyword_arguments = (
                src.functions.keyword_arguments
            )
            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}
            assert (
                keyword_arguments(
                    a_set, a_dictionary,
                )
            == (a_set, a_dictionary)
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
  :lineno-start: 103
  :emphasize-lines: 1-2

      # def test_positional_arguments():
      def test_positional_arguments(self):

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 12-15

        # def test_positional_arguments():
        def test_positional_arguments(self):
            positional_arguments = (
                src.functions.positional_arguments
            )
            first, last = 'first', 'last'

            assert (
                positional_arguments(first, last)
            == (first, last)
            )
            self.assertNotEqual(
                positional_arguments(first, last),
                (first, last)
            )

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 5-8

            assert (
                positional_arguments(last, first)
            == (last, first)
            )
            self.assertNotEqual(
                positional_arguments(last, first),
                (last, first)
            )

  .. code-block:: python
    :lineno-start: 126
    :emphasize-lines: 5-7

            assert (
                positional_arguments(0, 1)
            == (0, 1)
            )
            self.assertNotEqual(
                positional_arguments(0, 1), (0, 1)
            )

  .. code-block:: python
    :lineno-start: 134
    :emphasize-lines: 7-10

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']
            assert (
                positional_arguments(a_tuple, a_list)
            == (a_tuple, a_list)
            )
            self.assertNotEqual(
                positional_arguments(a_tuple, a_list),
                (a_tuple, a_list)
            )

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 12-17

            keyword_arguments = (
                src.functions.keyword_arguments
            )
            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}
            assert (
                keyword_arguments(
                    a_set, a_dictionary,
                )
            == (a_set, a_dictionary)
            )
            self.assertNotEqual(
                keyword_arguments(
                    a_set, a_dictionary,
                ),
                (a_set, a_dictionary)
            )


    def test_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`.

* I change the :ref:`calls<how to call a function with input>` from :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 12-13

        # def test_positional_arguments():
        def test_positional_arguments(self):
            positional_arguments = (
                src.functions.positional_arguments
            )
            first, last = 'first', 'last'

            assert (
                positional_arguments(first, last)
            == (first, last)
            )
            # self.assertNotEqual(
            self.assertEqual(
                positional_arguments(first, last),
                (first, last)
            )

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 5-6

            assert (
                positional_arguments(last, first)
            == (last, first)
            )
            # self.assertNotEqual(
            self.assertEqual(
                positional_arguments(last, first),
                (last, first)
            )

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 5-6

            assert (
                positional_arguments(0, 1)
            == (0, 1)
            )
            # self.assertNotEqual(
            self.assertEqual(
                positional_arguments(0, 1), (0, 1)
            )

  .. code-block:: python
    :lineno-start: 137
    :emphasize-lines: 7-8

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']
            assert (
                positional_arguments(a_tuple, a_list)
            == (a_tuple, a_list)
            )
            # self.assertNotEqual(
            self.assertEqual(
                positional_arguments(a_tuple, a_list),
                (a_tuple, a_list)
            )

  .. code-block:: python
    :lineno-start: 149
    :emphasize-lines: 12-13

            keyword_arguments = (
                src.functions.keyword_arguments
            )
            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}
            assert (
                keyword_arguments(
                    a_set, a_dictionary,
                )
            == (a_set, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                keyword_arguments(
                    a_set, a_dictionary,
                ),
                (a_set, a_dictionary)
            )


    def test_keyword_arguments():

  the test passes.

* I add :ref:`variables<what is a variable?>` for the :ref:`calls<how to call a function with input>` to ``positional_arguments``, ``keyword_arguments`` and my expectations

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 8-9

        # def test_positional_arguments():
        def test_positional_arguments(self):
            positional_arguments = (
                src.functions.positional_arguments
            )
            first, last = 'first', 'last'

            reality = positional_arguments(first, last)
            my_expectation = (first, last)
            assert (
                positional_arguments(first, last)
            == (first, last)
            )
            # self.assertNotEqual(

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 6-7

            self.assertEqual(
                positional_arguments(first, last),
                (first, last)
            )

            reality = positional_arguments(last, first)
            my_expectation = (last, first)
            assert (
                positional_arguments(last, first)
            == (last, first)
            )
            # self.assertNotEqual(

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 6-7

            self.assertEqual(
                positional_arguments(last, first),
                (last, first)
            )

            reality = positional_arguments(0, 1)
            my_expectation = (0, 1)
            assert (
                positional_arguments(0, 1)
            == (0, 1)
            )
            # self.assertNotEqual(
            self.assertEqual(
                positional_arguments(0, 1), (0, 1)
            )

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 4-6

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']

            reality = positional_arguments(
                a_tuple, a_list
            )
            my_expectation = (a_tuple, a_list)
            assert (
                positional_arguments(a_tuple, a_list)
            == (a_tuple, a_list)
            )
            # self.assertNotEqual(
            self.assertEqual(
                positional_arguments(a_tuple, a_list),
                (a_tuple, a_list)
            )

  .. code-block:: python
    :lineno-start: 162
    :emphasize-lines: 7-10

            keyword_arguments = (
                src.functions.keyword_arguments
            )
            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}

            reality = keyword_arguments(
                a_set, a_dictionary,
            )
            my_expectation = (a_set, a_dictionary)
            assert (
                keyword_arguments(
                    a_set, a_dictionary,
                )
            == (a_set, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                keyword_arguments(
                    a_set, a_dictionary,
                ),
                (a_set, a_dictionary)
            )


    def test_keyword_arguments():

* I use the :ref:`variables<what is a variable?>` to remove repetition of the :ref:`calls<how to call a function with input>` to ``positional_arguments``, ``keyword_arguments`` and my expectations, from :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 10-13, 15-20

        # def test_positional_arguments():
        def test_positional_arguments(self):
            positional_arguments = (
                src.functions.positional_arguments
            )
            first, last = 'first', 'last'

            reality = positional_arguments(first, last)
            my_expectation = (first, last)
            # assert (
            #     positional_arguments(first, last)
            # == (first, last)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     positional_arguments(first, last),
            #     (first, last)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 3-6, 8-13

            reality = positional_arguments(last, first)
            my_expectation = (last, first)
            # assert (
            #     positional_arguments(last, first)
            # == (last, first)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     positional_arguments(last, first),
            #     (last, first)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 3-6, 8-12

            reality = positional_arguments(0, 1)
            my_expectation = (0, 1)
            # assert (
            #     positional_arguments(0, 1)
            # == (0, 1)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     positional_arguments(0, 1), (0, 1)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 8-11, 13-18

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']

            reality = positional_arguments(
                a_tuple, a_list
            )
            my_expectation = (a_tuple, a_list)
            # assert (
            #     positional_arguments(a_tuple, a_list)
            # == (a_tuple, a_list)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     positional_arguments(a_tuple, a_list),
            #     (a_tuple, a_list)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 170
    :emphasize-lines: 11-16, 18-25

            keyword_arguments = (
                src.functions.keyword_arguments
            )
            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}

            reality = keyword_arguments(
                a_set, a_dictionary,
            )
            my_expectation = (a_set, a_dictionary)
            # assert (
            #     keyword_arguments(
            #         a_set, a_dictionary,
            #     )
            # == (a_set, a_dictionary)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     keyword_arguments(
            #         a_set, a_dictionary,
            #     ),
            #     (a_set, a_dictionary)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_keyword_arguments():

  the test is still green.

* I remove the commented lines from :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 101

            self.assertEqual(result, expectation)

        def test_positional_arguments(self):
            positional_arguments = (
                src.functions.positional_arguments
            )
            first, last = 'first', 'last'

  .. code-block:: python
    :lineno-start: 109

            reality = positional_arguments(first, last)
            my_expectation = (first, last)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 114

            reality = positional_arguments(last, first)
            my_expectation = (last, first)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 119

            reality = positional_arguments(0, 1)
            my_expectation = (0, 1)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 124

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']

            reality = positional_arguments(
                a_tuple, a_list
            )
            my_expectation = (a_tuple, a_list)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 134

            keyword_arguments = (
                src.functions.keyword_arguments
            )
            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}

            reality = keyword_arguments(
                a_set, a_dictionary,
            )
            my_expectation = (a_set, a_dictionary)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


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

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_keyword_arguments` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 3-7

            self.assertEqual(reality, my_expectation)

        def test_keyword_arguments():
            keyword_arguments = (
                src.functions.keyword_arguments
            )
            first, last = 'first', 'last'

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 1-18

            assert (
                keyword_arguments(
                    first_input=first, last_input=last,
                )
            == (first, last)
            )
            assert (
                keyword_arguments(
                    last_input=last, first_input=first,
                )
            == (first, last)
            )
            assert (
                keyword_arguments(
                    last_input=0, first_input=1,
                )
            == (1, 0)
            )

  .. code-block:: python
    :lineno-start: 172
    :emphasize-lines: 1-9

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']
            assert (
                keyword_arguments(
                    first_input=a_tuple,
                    last_input=a_list,
                )
            == (a_tuple, a_list)
            )

  .. code-block:: python
    :lineno-start: 182
    :emphasize-lines: 1-12

            positional_arguments = (
                src.functions.positional_arguments
            )
            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}
            assert (
                positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                )
            == (a_set, a_dictionary)
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
  :lineno-start: 147
  :emphasize-lines: 1-2

      # def test_keyword_arguments():
      def test_keyword_arguments(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 14-19

        # def test_keyword_arguments():
        def test_keyword_arguments(self):
            keyword_arguments = (
                src.functions.keyword_arguments
            )
            first, last = 'first', 'last'

            assert (
                keyword_arguments(
                    first_input=first, last_input=last,
                )
            == (first, last)
            )
            self.assertNotEqual(
                keyword_arguments(
                    first_input=first, last_input=last,
                ),
                (first, last)
            )

  .. code-block:: python
    :lineno-start: 166
    :emphasize-lines: 7-12

            assert (
                keyword_arguments(
                    last_input=last, first_input=first,
                )
            == (first, last)
            )
            self.assertNotEqual(
                keyword_arguments(
                    last_input=last, first_input=first,
                ),
                (first, last)
            )

  .. code-block:: python
    :lineno-start: 178
    :emphasize-lines: 7-12

            assert (
                keyword_arguments(
                    last_input=0, first_input=1,
                )
            == (1, 0)
            )
            self.assertNotEqual(
                keyword_arguments(
                    last_input=0, first_input=1,
                ),
                (1, 0)
            )

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 10-16

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']
            assert (
                keyword_arguments(
                    first_input=a_tuple,
                    last_input=a_list,
                )
            == (a_tuple, a_list)
            )
            self.assertEqual(
                keyword_arguments(
                    first_input=a_tuple,
                    last_input=a_list,
                ),
                (a_tuple, a_list)
            )

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 13-19

            positional_arguments = (
                src.functions.positional_arguments
            )
            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}
            assert (
                positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                )
            == (a_set, a_dictionary)
            )
            self.assertNotEqual(
                positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                ),
                (a_set, a_dictionary)
            )


    def test_args_and_kwargs():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`.

* I change the :ref:`calls<how to call a function with input>` from :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 14-15

        # def test_keyword_arguments():
        def test_keyword_arguments(self):
            keyword_arguments = (
                src.functions.keyword_arguments
            )
            first, last = 'first', 'last'

            assert (
                keyword_arguments(
                    first_input=first, last_input=last,
                )
            == (first, last)
            )
            # self.assertNotEqual(
            self.assertEqual(
                keyword_arguments(
                    first_input=first, last_input=last,
                ),
                (first, last)
            )

  .. code-block:: python
    :lineno-start: 167
    :emphasize-lines: 7-8

            assert (
                keyword_arguments(
                    last_input=last, first_input=first,
                )
            == (first, last)
            )
            # self.assertNotEqual(
            self.assertEqual(
                keyword_arguments(
                    last_input=last, first_input=first,
                ),
                (first, last)
            )

  .. code-block:: python
    :lineno-start: 180
    :emphasize-lines: 7-8

            assert (
                keyword_arguments(
                    last_input=0, first_input=1,
                )
            == (1, 0)
            )
            # self.assertNotEqual(
            self.assertEqual(
                keyword_arguments(
                    last_input=0, first_input=1,
                ),
                (1, 0)
            )

  .. code-block:: python
    :lineno-start: 194
    :emphasize-lines: 10-11

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']
            assert (
                keyword_arguments(
                    first_input=a_tuple,
                    last_input=a_list,
                )
            == (a_tuple, a_list)
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
    :lineno-start: 212
    :emphasize-lines: 13-14

            positional_arguments = (
                src.functions.positional_arguments
            )
            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}
            assert (
                positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                )
            == (a_set, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                ),
                (a_set, a_dictionary)
            )


    def test_args_and_kwargs():

  the test passes.

* I add :ref:`variables<what is a variable?>` for the :ref:`calls<how to call a function with input>` to ``keyword_arguments``, ``positional_arguments`` and my expectations

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 8-11

        # def test_keyword_arguments():
        def test_keyword_arguments(self):
            keyword_arguments = (
                src.functions.keyword_arguments
            )
            first, last = 'first', 'last'

            reality = keyword_arguments(
                first_input=first, last_input=last,
            )
            my_expectation = (first, last)
            assert (
                keyword_arguments(
                    first_input=first, last_input=last,
                )
            == (first, last)
            )
            # self.assertNotEqual(

  .. code-block:: python
    :lineno-start: 165
    :emphasize-lines: 8-11

            self.assertEqual(
                keyword_arguments(
                    first_input=first, last_input=last,
                ),
                (first, last)
            )

            reality = keyword_arguments(
                last_input=last, first_input=first,
            )
            my_expectation = (first, last)
            assert (
                keyword_arguments(
                    last_input=last, first_input=first,
                )
            == (first, last)
            )
            # self.assertNotEqual(

  .. code-block:: python
    :lineno-start: 183
    :emphasize-lines: 8-11

            self.assertEqual(
                keyword_arguments(
                    last_input=last, first_input=first,
                ),
                (first, last)
            )

            reality = keyword_arguments(
                last_input=0, first_input=1,
            )
            my_expectation = (1, 0)
            assert (
                keyword_arguments(
                    last_input=0, first_input=1,
                )
            == (1, 0)
            )
            # self.assertNotEqual(
            self.assertEqual(
                keyword_arguments(
                    last_input=0, first_input=1,
                ),
                (1, 0)
            )

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 4-8

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']

            reality = keyword_arguments(
                first_input=a_tuple,
                last_input=a_list,
            )
            my_expectation = (a_tuple, a_list)
            assert (
                keyword_arguments(
                    first_input=a_tuple,
                    last_input=a_list,
                )
            == (a_tuple, a_list)
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
    :lineno-start: 232
    :emphasize-lines: 7-11

            positional_arguments = (
                src.functions.positional_arguments
            )
            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}

            reality = positional_arguments(
                last_input=a_dictionary,
                first_input=a_set,
            )
            my_expectation = (a_set, a_dictionary)
            assert (
                positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                )
            == (a_set, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                positional_arguments(
                    last_input=a_dictionary,
                    first_input=a_set,
                ),
                (a_set, a_dictionary)
            )


    def test_args_and_kwargs():

* I use the :ref:`variables<what is a variable?>` to remove repetition of the :ref:`calls<how to call a function with input>` to ``keyword_arguments``, ``positional_arguments`` and my expectations, from :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 12-17, 19-26

        # def test_keyword_arguments():
        def test_keyword_arguments(self):
            keyword_arguments = (
                src.functions.keyword_arguments
            )
            first, last = 'first', 'last'

            reality = keyword_arguments(
                first_input=first, last_input=last,
            )
            my_expectation = (first, last)
            # assert (
            #     keyword_arguments(
            #         first_input=first, last_input=last,
            #     )
            # == (first, last)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     keyword_arguments(
            #         first_input=first, last_input=last,
            #     ),
            #     (first, last)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 174
    :emphasize-lines: 5-10, 12-19

            reality = keyword_arguments(
                last_input=last, first_input=first,
            )
            my_expectation = (first, last)
            # assert (
            #     keyword_arguments(
            #         last_input=last, first_input=first,
            #     )
            # == (first, last)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     keyword_arguments(
            #         last_input=last, first_input=first,
            #     ),
            #     (first, last)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 194
    :emphasize-lines: 5-10, 12-19

            reality = keyword_arguments(
                last_input=0, first_input=1,
            )
            my_expectation = (1, 0)
            # assert (
            #     keyword_arguments(
            #         last_input=0, first_input=1,
            #     )
            # == (1, 0)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     keyword_arguments(
            #         last_input=0, first_input=1,
            #     ),
            #     (1, 0)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 214
    :emphasize-lines: 9-15, 17-25

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']

            reality = keyword_arguments(
                first_input=a_tuple,
                last_input=a_list,
            )
            my_expectation = (a_tuple, a_list)
            # assert (
            #     keyword_arguments(
            #         first_input=a_tuple,
            #         last_input=a_list,
            #     )
            # == (a_tuple, a_list)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     keyword_arguments(
            #         first_input=a_tuple,
            #         last_input=a_list,
            #     ),
            #     (a_tuple, a_list)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 240
    :emphasize-lines: 12-18, 20-28

            positional_arguments = (
                src.functions.positional_arguments
            )
            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}

            reality = positional_arguments(
                last_input=a_dictionary,
                first_input=a_set,
            )
            my_expectation = (a_set, a_dictionary)
            # assert (
            #     positional_arguments(
            #         last_input=a_dictionary,
            #         first_input=a_set,
            #     )
            # == (a_set, a_dictionary)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     positional_arguments(
            #         last_input=a_dictionary,
            #         first_input=a_set,
            #     ),
            #     (a_set, a_dictionary)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_args_and_kwargs():

  the test is still green.

* I remove the commented lines from :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 145

            self.assertEqual(reality, my_expectation)

        def test_keyword_arguments(self):
            keyword_arguments = (
                src.functions.keyword_arguments
            )
            first, last = 'first', 'last'

  .. code-block:: python
    :lineno-start: 153

            reality = keyword_arguments(
                first_input=first, last_input=last,
            )
            my_expectation = (first, last)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 160

            reality = keyword_arguments(
                last_input=last, first_input=first,
            )
            my_expectation = (first, last)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 167

            reality = keyword_arguments(
                last_input=0, first_input=1,
            )
            my_expectation = (1, 0)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 174

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']

            reality = keyword_arguments(
                first_input=a_tuple,
                last_input=a_list,
            )
            my_expectation = (a_tuple, a_list)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 185

            positional_arguments = (
                src.functions.positional_arguments
            )
            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}

  .. code-block:: python
    :lineno-start: 191

            reality = positional_arguments(
                last_input=a_dictionary,
                first_input=a_set,
            )
            my_expectation = (a_set, a_dictionary)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


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

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_args_and_kwargs` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 197
    :emphasize-lines: 3-4, 6-11

            self.assertEqual(reality, my_expectation)

        def test_args_and_kwargs(self):
            first, last = 'first', 'last'

            assert (
                src.functions.args_and_kwargs(
                    first, last_input=last,
                )
            == (first, last)
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
  :lineno-start: 199
  :emphasize-lines: 1-2

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
    :lineno-start: 199
    :emphasize-lines: 11-16

        # def test_args_and_kwargs():
        def test_args_and_kwargs(self):
            first, last = 'first', 'last'

            assert (
                src.functions.args_and_kwargs(
                    first, last_input=last,
                )
            == (first, last)
            )
            self.assertNotEqual(
                src.functions.args_and_kwargs(
                    first, last_input=last,
                ),
                (first, last)
            )


    def test_optional_arguments():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ('first', 'last') == ('first', 'last')

* I change the :ref:`call<how to call a function with input>` from :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 11-12

        # def test_args_and_kwargs():
        def test_args_and_kwargs(self):
            first, last = 'first', 'last'

            assert (
                src.functions.args_and_kwargs(
                    first, last_input=last,
                )
            == (first, last)
            )
            # self.assertNotEqual(
            self.assertNotEqual(
                src.functions.args_and_kwargs(
                    first, last_input=last,
                ),
                (first, last)
            )


    def test_optional_arguments():

  the test passes.

* I add :ref:`variables<what is a variable?>` for the :ref:`call<how to call a function with input>` to ``src.functions.args_and_kwargs`` and my expectation

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 5-8

        # def test_args_and_kwargs():
        def test_args_and_kwargs(self):
            first, last = 'first', 'last'

            reality = src.functions.args_and_kwargs(
                first, last_input=last,
            )
            my_expectation = (first, last)
            assert (
                src.functions.args_and_kwargs(
                    first, last_input=last,
                )
            == (first, last)
            )
            # self.assertNotEqual(
            self.assertNotEqual(
                src.functions.args_and_kwargs(
                    first, last_input=last,
                ),
                (first, last)
            )


    def test_optional_arguments():

* I use the :ref:`variables<what is a variable?>` to remove repetition of the :ref:`call<how to call a function with input>` to ``src.functions.args_and_kwargs`` and my expectation, from :ref:`test_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 9-15, 17-23

        # def test_args_and_kwargs():
        def test_args_and_kwargs(self):
            first, last = 'first', 'last'

            reality = src.functions.args_and_kwargs(
                first, last_input=last,
            )
            my_expectation = (first, last)
            # assert (
            #     src.functions.args_and_kwargs(
            #         first, last_input=last,
            #     )
            # == (first, last)
            # )
            # self.assertNotEqual(
            # self.assertNotEqual(
            #     src.functions.args_and_kwargs(
            #         first, last_input=last,
            #     ),
            #     (first, last)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_optional_arguments():

  the test is still green.

* I remove the commented lines from :ref:`test_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 197

            self.assertEqual(reality, my_expectation)

        def test_args_and_kwargs(self):
            first, last = 'first', 'last'

            reality = src.functions.args_and_kwargs(
                first, last_input=last,
            )
            my_expectation = (first, last)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


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

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_optional_arguments` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 207
    :emphasize-lines: 3-6, 8, 10-15

            self.assertEqual(reality, my_expectation)

        def test_optional_arguments():
            optional_arguments = (
                src.functions.optional_arguments
            )

            first_name, last_name = 'jane', 'doe'

            assert (
                optional_arguments(
                    first_name,
                )
            == (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 223
    :emphasize-lines: 1-7

            first_name, blow = 'joe', 'blow'
            assert (
                optional_arguments(
                    first_name, blow
                )
            == (first_name, blow)
            )

  .. code-block:: python
    :lineno-start: 231
    :emphasize-lines: 1-7

            first_name = 'john'
            assert (
                optional_arguments(
                    first_input=first_name
                )
            == (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 239
    :emphasize-lines: 1-8

            last_name = 'smith'
            assert (
                optional_arguments(
                    last_input=last_name,
                    first_input=first_name,
                )
            == (first_name, last_name)
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
  :lineno-start: 209
  :emphasize-lines: 1-2

      # def test_optional_arguments():
      def test_optional_arguments(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_optional_arguments`

  .. code-block:: python
    :lineno-start: 209
    :emphasize-lines: 15-20

        # def test_optional_arguments():
        def test_optional_arguments(self):
            optional_arguments = (
                src.functions.optional_arguments
            )

            first_name, last_name = 'jane', 'doe'

            assert (
                optional_arguments(
                    first_name,
                )
            == (first_name, last_name)
            )
            self.assertNotEqual(
                optional_arguments(
                    first_name,
                ),
                (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 230
    :emphasize-lines: 8-13

            first_name, blow = 'joe', 'blow'
            assert (
                optional_arguments(
                    first_name, blow
                )
            == (first_name, blow)
            )
            self.assertNotEqual(
                optional_arguments(
                    first_name, blow
                ),
                (first_name, blow)
            )

  .. code-block:: python
    :lineno-start: 244
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
    :lineno-start: 258
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
    :lineno-start: 209
    :emphasize-lines: 15-16

        # def test_optional_arguments():
        def test_optional_arguments(self):
            optional_arguments = (
                src.functions.optional_arguments
            )

            first_name, last_name = 'jane', 'doe'

            assert (
                optional_arguments(
                    first_name,
                )
            == (first_name, last_name)
            )
            # self.assertNotEqual(
            self.assertEqual(
                optional_arguments(
                    first_name,
                ),
                (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 231
    :emphasize-lines: 8-9

            first_name, blow = 'joe', 'blow'
            assert (
                optional_arguments(
                    first_name, blow
                )
            == (first_name, blow)
            )
            # self.assertNotEqual(
            self.assertEqual(
                optional_arguments(
                    first_name, blow
                ),
                (first_name, blow)
            )

  .. code-block:: python
    :lineno-start: 246
    :emphasize-lines: 8-9

            first_name = 'john'
            assert (
                optional_arguments(
                    first_input=first_name
                )
            == (first_name, last_name)
            )
            # self.assertNotEqual(
            self.assertEqual(
                optional_arguments(
                    first_input=first_name
                ),
                (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 261
    :emphasize-lines: 9-10

            last_name = 'smith'
            assert (
                optional_arguments(
                    last_input=last_name,
                    first_input=first_name,
                )
            == (first_name, last_name)
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

* I add :ref:`variables<what is a variable?>` for the :ref:`calls<how to call a function with input>` to ``src.functions.optional_arguments`` and my expectations

  .. code-block:: python
    :lineno-start: 209
    :emphasize-lines: 9-10

        # def test_optional_arguments():
        def test_optional_arguments(self):
            optional_arguments = (
                src.functions.optional_arguments
            )

            first_name, last_name = 'jane', 'doe'

            reality = optional_arguments(first_name)
            my_expectation = (first_name, last_name)
            assert (
                optional_arguments(
                    first_name,
                )
            == (first_name, last_name)
            )
            # self.assertNotEqual(
            self.assertEqual(
                optional_arguments(
                    first_name,
                ),
                (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 233
    :emphasize-lines: 3-6

            first_name, blow = 'joe', 'blow'

            reality = optional_arguments(
                first_name, blow
            )
            my_expectation = (first_name, blow)
            assert (
                optional_arguments(
                    first_name, blow
                )
            == (first_name, blow)
            )
            # self.assertNotEqual(
            self.assertEqual(
                optional_arguments(
                    first_name, blow
                ),
                (first_name, blow)
            )

  .. code-block:: python
    :lineno-start: 253
    :emphasize-lines: 3-6

            first_name = 'john'

            reality = optional_arguments(
                first_input=first_name
            )
            my_expectation = (first_name, last_name)
            assert (
                optional_arguments(
                    first_input=first_name
                )
            == (first_name, last_name)
            )
            # self.assertNotEqual(
            self.assertEqual(
                optional_arguments(
                    first_input=first_name
                ),
                (first_name, last_name)
            )

  .. code-block:: python
    :lineno-start: 273
    :emphasize-lines: 3-7

            last_name = 'smith'

            reality = optional_arguments(
                last_input=last_name,
                first_input=first_name,
            )
            my_expectation = (first_name, last_name)
            assert (
                optional_arguments(
                    last_input=last_name,
                    first_input=first_name,
                )
            == (first_name, last_name)
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

* I use the :ref:`variables<what is a variable?>` to remove repetition of the :ref:`calls<how to call a function with input>` to ``src.functions.optional_arguments`` and my expectations, from :ref:`test_optional_arguments`

  .. code-block:: python
    :lineno-start: 209
    :emphasize-lines: 11-16, 18-25

        # def test_optional_arguments():
        def test_optional_arguments(self):
            optional_arguments = (
                src.functions.optional_arguments
            )

            first_name, last_name = 'jane', 'doe'

            reality = optional_arguments(first_name)
            my_expectation = (first_name, last_name)
            # assert (
            #     optional_arguments(
            #         first_name,
            #     )
            # == (first_name, last_name)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     optional_arguments(
            #         first_name,
            #     ),
            #     (first_name, last_name)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 235
    :emphasize-lines: 7-12, 14-21

            first_name, blow = 'joe', 'blow'

            reality = optional_arguments(
                first_name, blow
            )
            my_expectation = (first_name, blow)
            # assert (
            #     optional_arguments(
            #         first_name, blow
            #     )
            # == (first_name, blow)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     optional_arguments(
            #         first_name, blow
            #     ),
            #     (first_name, blow)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 257
    :emphasize-lines: 7-12, 14-21

            first_name = 'john'

            reality = optional_arguments(
                first_input=first_name
            )
            my_expectation = (first_name, last_name)
            # assert (
            #     optional_arguments(
            #         first_input=first_name
            #     )
            # == (first_name, last_name)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     optional_arguments(
            #         first_input=first_name
            #     ),
            #     (first_name, last_name)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 279
    :emphasize-lines: 8-13, 15-24

            last_name = 'smith'

            reality = optional_arguments(
                last_input=last_name,
                first_input=first_name,
            )
            my_expectation = (first_name, last_name)
            # assert (
            #     optional_arguments(
            #         last_input=last_name,
            #         first_input=first_name,
            #     )
            # == (first_name, last_name)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     optional_arguments(
            #         last_input=last_name,
            #         first_input=first_name,
            #     ),
            #     (first_name, last_name)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_unknown_number_of_arguments():

  the test is still green.

* I remove the commented lines from :ref:`test_optional_arguments`

  .. code-block:: python
    :lineno-start: 207

            self.assertEqual(reality, my_expectation)

        def test_optional_arguments(self):
            optional_arguments = (
                src.functions.optional_arguments
            )

            first_name, last_name = 'jane', 'doe'

            reality = optional_arguments(first_name)
            my_expectation = (first_name, last_name)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 221

            first_name, blow = 'joe', 'blow'

            reality = optional_arguments(
                first_name, blow
            )
            my_expectation = (first_name, blow)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 230

            first_name = 'john'

            reality = optional_arguments(
                first_input=first_name
            )
            my_expectation = (first_name, last_name)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 239

            last_name = 'smith'

            reality = optional_arguments(
                last_input=last_name,
                first_input=first_name,
            )
            my_expectation = (first_name, last_name)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


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

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_unknown_number_of_arguments` to make it a :ref:`method<what is a method?>` of the :ref:`TestFunctions class<add TestFunctions class>`

  .. code-block:: python
    :lineno-start: 247
    :emphasize-lines: 3-6, 8-15

                self.assertEqual(reality, my_expectation)

        def test_unknown_number_of_arguments():
            unknown_number_of_arguments = (
                src.functions.unknown_number_of_arguments
            )

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3}
            assert (
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                )
            == (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 263
    :emphasize-lines: 1-8

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3, 'c': 4}
            assert (
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                )
            == (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 272
    :emphasize-lines: 1-8

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}
            assert (
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                )
            == (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 281
    :emphasize-lines: 1-5

            a_tuple = (1, 2, 3, 'n')
            assert (
                unknown_number_of_arguments(*a_tuple)
            == (a_tuple, {})
            )

  .. code-block:: python
    :lineno-start: 287
    :emphasize-lines: 1-5

            a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
            assert (
                unknown_number_of_arguments(**a_dictionary)
            == ((), a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 293
    :emphasize-lines: 1-4

            assert (
                unknown_number_of_arguments()
            == ((), {})
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
  :lineno-start: 249
  :emphasize-lines: 1-2

      # def test_unknown_number_of_arguments():
      def test_unknown_number_of_arguments(self):

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_unknown_number_of_arguments`

  .. code-block:: python
    :lineno-start: 249
    :emphasize-lines: 15-20

        # def test_unknown_number_of_arguments():
        def test_unknown_number_of_arguments(self):
            unknown_number_of_arguments = (
                src.functions.unknown_number_of_arguments
            )

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3}
            assert (
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                )
            == (a_tuple, a_dictionary)
            )
            self.assertNotEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 270
    :emphasize-lines: 9-14

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3, 'c': 4}
            assert (
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                )
            == (a_tuple, a_dictionary)
            )
            self.assertNotEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 285
    :emphasize-lines: 9-14

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}
            assert (
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                )
            == (a_tuple, a_dictionary)
            )
            self.assertNotEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 300
    :emphasize-lines: 6-9

            a_tuple = (1, 2, 3, 'n')
            assert (
                unknown_number_of_arguments(*a_tuple)
            == (a_tuple, {})
            )
            self.assertNotEqual(
                unknown_number_of_arguments(*a_tuple),
                (a_tuple, {})
            )

  .. code-block:: python
    :lineno-start: 310
    :emphasize-lines: 6-9

            a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
            assert (
                unknown_number_of_arguments(**a_dictionary)
            == ((), a_dictionary)
            )
            self.assertNotEqual(
                unknown_number_of_arguments(**a_dictionary),
                ((), a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 320
    :emphasize-lines: 5-8

            assert (
                unknown_number_of_arguments()
            == ((), {})
            )
            self.assertNotEqual(
                unknown_number_of_arguments(),
                ((), {})
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`.

* I change the :ref:`calls<how to call a function with input>` from :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_unknown_number_of_arguments`

  .. code-block:: python
    :lineno-start: 249
    :emphasize-lines: 15-16

        # def test_unknown_number_of_arguments():
        def test_unknown_number_of_arguments(self):
            unknown_number_of_arguments = (
                src.functions.unknown_number_of_arguments
            )

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3}
            assert (
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                )
            == (a_tuple, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 271
    :emphasize-lines: 9-10

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3, 'c': 4}
            assert (
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                )
            == (a_tuple, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 287
    :emphasize-lines: 9-10

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}
            assert (
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                )
            == (a_tuple, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 303
    :emphasize-lines: 6-7

            a_tuple = (1, 2, 3, 'n')
            assert (
                unknown_number_of_arguments(*a_tuple)
            == (a_tuple, {})
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(*a_tuple),
                (a_tuple, {})
            )

  .. code-block:: python
    :lineno-start: 314
    :emphasize-lines: 6-7

            a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
            assert (
                unknown_number_of_arguments(**a_dictionary)
            == ((), a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(**a_dictionary),
                ((), a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 271
    :emphasize-lines: 5-6

            assert (
                unknown_number_of_arguments()
            == ((), {})
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(),
                ((), {})
            )


    # Exceptions seen

  the test passes.

* I add :ref:`variables<what is a variable?>` for the :ref:`calls<how to call a function with input>` to ``src.functions.unknown_number_of_arguments`` and my expectations

  .. code-block:: python
    :lineno-start: 249
    :emphasize-lines: 10-13

        # def test_unknown_number_of_arguments():
        def test_unknown_number_of_arguments(self):
            unknown_number_of_arguments = (
                src.functions.unknown_number_of_arguments
            )

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3}

            reality = unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (a_tuple, a_dictionary)
            assert (
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                )
            == (a_tuple, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 276
    :emphasize-lines: 4-7

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3, 'c': 4}

            reality = unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (a_tuple, a_dictionary)
            assert (
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                )
            == (a_tuple, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 297
    :emphasize-lines: 4-7

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}

            reality = unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (a_tuple, a_dictionary)
            assert (
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                )
            == (a_tuple, a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(
                    *a_tuple, **a_dictionary
                ),
                (a_tuple, a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 318
    :emphasize-lines: 3-4

            a_tuple = (1, 2, 3, 'n')

            reality = unknown_number_of_arguments(*a_tuple)
            my_expectation = (a_tuple, {})
            assert (
                unknown_number_of_arguments(*a_tuple)
            == (a_tuple, {})
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(*a_tuple),
                (a_tuple, {})
            )

  .. code-block:: python
    :lineno-start: 332
    :emphasize-lines: 3-6

            a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}

            reality = unknown_number_of_arguments(
                **a_dictionary
            )
            my_expectation = ((), a_dictionary)
            assert (
                unknown_number_of_arguments(**a_dictionary)
            == ((), a_dictionary)
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(**a_dictionary),
                ((), a_dictionary)
            )

  .. code-block:: python
    :lineno-start: 348
    :emphasize-lines: 1-2

            reality = unknown_number_of_arguments()
            my_expectation = ((), {})
            assert (
                unknown_number_of_arguments()
            == ((), {})
            )
            # self.assertNotEqual(
            self.assertEqual(
                unknown_number_of_arguments(),
                ((), {})
            )


    # Exceptions seen

* I use the :ref:`variables<what is a variable?>` to remove repetition of the :ref:`calls<how to call a function with input>` to ``src.functions.unknown_number_of_arguments`` and my expectations, from :ref:`test_unknown_number_of_arguments`

  .. code-block:: python
    :lineno-start: 249
    :emphasize-lines: 14-19, 21-28

        # def test_unknown_number_of_arguments():
        def test_unknown_number_of_arguments(self):
            unknown_number_of_arguments = (
                src.functions.unknown_number_of_arguments
            )

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3}

            reality = unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (a_tuple, a_dictionary)
            # assert (
            #     unknown_number_of_arguments(
            #         *a_tuple, **a_dictionary
            #     )
            # == (a_tuple, a_dictionary)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     unknown_number_of_arguments(
            #         *a_tuple, **a_dictionary
            #     ),
            #     (a_tuple, a_dictionary)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 278
    :emphasize-lines: 8-13, 15-22

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3, 'c': 4}

            reality = unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (a_tuple, a_dictionary)
            # assert (
            #     unknown_number_of_arguments(
            #         *a_tuple, **a_dictionary
            #     )
            # == (a_tuple, a_dictionary)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     unknown_number_of_arguments(
            #         *a_tuple, **a_dictionary
            #     ),
            #     (a_tuple, a_dictionary)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 301
    :emphasize-lines: 8-13, 15-22

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}

            reality = unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (a_tuple, a_dictionary)
            # assert (
            #     unknown_number_of_arguments(
            #         *a_tuple, **a_dictionary
            #     )
            # == (a_tuple, a_dictionary)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     unknown_number_of_arguments(
            #         *a_tuple, **a_dictionary
            #     ),
            #     (a_tuple, a_dictionary)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 324
    :emphasize-lines: 5-8, 10-15

            a_tuple = (1, 2, 3, 'n')

            reality = unknown_number_of_arguments(*a_tuple)
            my_expectation = (a_tuple, {})
            # assert (
            #     unknown_number_of_arguments(*a_tuple)
            # == (a_tuple, {})
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     unknown_number_of_arguments(*a_tuple),
            #     (a_tuple, {})
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 340
    :emphasize-lines: 7-10, 12-19

            a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}

            reality = unknown_number_of_arguments(
                **a_dictionary
            )
            my_expectation = ((), a_dictionary)
            # assert (
            #     unknown_number_of_arguments(**a_dictionary)
            # == ((), a_dictionary)
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     unknown_number_of_arguments(**a_dictionary),
            #     ((), a_dictionary)
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 358
    :emphasize-lines: 3-6, 8-13

            reality = unknown_number_of_arguments()
            my_expectation = ((), {})
            # assert (
            #     unknown_number_of_arguments()
            # == ((), {})
            # )
            # self.assertNotEqual(
            # self.assertEqual(
            #     unknown_number_of_arguments(),
            #     ((), {})
            # )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green.

* I remove the commented lines from :ref:`test_unknown_number_of_arguments`

  .. code-block:: python
    :lineno-start: 247

            self.assertEqual(reality, my_expectation)

        def test_unknown_number_of_arguments(self):
            unknown_number_of_arguments = (
                src.functions.unknown_number_of_arguments
            )

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3}

            reality = unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (a_tuple, a_dictionary)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 264

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3, 'c': 4}

            reality = unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (a_tuple, a_dictionary)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 274

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}

            reality = unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (a_tuple, a_dictionary)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 284

            a_tuple = (1, 2, 3, 'n')

            reality = unknown_number_of_arguments(*a_tuple)
            my_expectation = (a_tuple, {})
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 291

            a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}

            reality = unknown_number_of_arguments(
                **a_dictionary
            )
            my_expectation = ((), a_dictionary)
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

  .. code-block:: python
    :lineno-start: 300

            reality = unknown_number_of_arguments()
            my_expectation = ((), {})
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # SyntaxError
    # ModuleNotFoundError
    # AttributeError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_unknown_number_of_arguments to TestFunctions'

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

I can use the :ref:`unittest library<another way to write tests>` to write tests with the :ref:`methods of the unittest.TestCase class<test_dir_unittest_testcase>` or I can write them with bare :ref:`assert statements<what is an assertion?>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test functions with unittest: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

So far, I know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what an assertion is<what is an assertion?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`
* :ref:`how to make functions that take input<functions that take input>`
* :ref:`what causes TypeError<what causes TypeError?>`
* :ref:`how to place values in strings<telephone>`
* :ref:`how to make a person say hello with f-strings<how to make a person with f-strings>`
* :ref:`how to separate tests from solutions<separate and equal>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to make a person with a class<how to make a person with a class>`
* :ref:`that everything in Python is an object<everything is an object>`
* :ref:`how to use the unittest library<another way to write tests>`

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