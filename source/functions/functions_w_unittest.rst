.. meta::
  :description:
  :keywords:

.. include:: ../links.rst

#################################################################################
test functions with unittest
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

* I add a :ref:`class<what is a class?>` named ``Functions`` to ``test_functions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4, 6-7

    import src.functions


    class Functions(object):

        def test_failure(self):
            self.assertEqual(True, False)


    def test_making_a_function_w_pass():

  the test is still green.

* I change the name of the :ref:`class<what is a class?>` to ``TestFunctions``

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

* I add :ref:`unittest.TestCase<test_dir_unittest_testcase>` as the parent :ref:`class<what is a class?>` of ``TestFunctions``

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
            assert src.functions.w_pass() is None
            # self.assertIsNot(
            self.assertIs(
                src.functions.w_pass(), None
            )


    def test_making_a_function_w_return():

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
            assert src.functions.w_return() is None
            # self.assertIsNot(
            self.assertIs(
                src.functions.w_return(), None
            )


    def test_making_a_function_w_return_none():

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
close the project
*********************************************************************************

* I close ``functions.py``
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

So far, you know

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
* :ref:`how to separate tests from solutions<separate and equal functions>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to make a person with a class<how to make a person with a class>`
* :ref:`that everything in Python is an object<everything is an object>`
* :ref:`how to use the unittest library<another way to write tests>`

:ref:`Would you like to test the person project with the unittest library?<test telephone with unittest>`

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