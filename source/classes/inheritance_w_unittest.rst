.. meta::
  :description:
  :keywords:

.. include:: ../links.rst

#################################################################################
test objects with unittest
#################################################################################

I want to use the :ref:`unittest library<another way to write tests>` in the :ref:`class<everything is an object>` project.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/person/tests/test_classes.py
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

    cd classes

  the terminal_ shows I am in the ``classes`` folder_

  .. code-block:: python

    .../pumping_python/classes

* I open ``test_classes.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    test_classes.py .............                       [100%]

    =================== 13 passed in J.KLs ===================

----

*********************************************************************************
add TestClasses class
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a :ref:`class<what is a class?>` named ``Classes`` to ``test_classes.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10, 13-14

    class WPass: pass


    class WParentheses(): pass


    class WObject(object): pass


    class Classes(object):

        def test_failure(self):
            self.assertEqual(True, False)


    def test_making_a_class_w_pass():

  the test is still green.

* I change the name of the :ref:`class<what is a class?>` to ``TestClasses``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4-5

    class WObject(object): pass


    # class Class(object):
    class TestClasses(object):

        def test_failure(self):
            self.assertEqual(True, False)

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'TestClasses' object
                    has no attribute 'assertEqual'

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 5
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`unittest.TestCase<test_dir_unittest_testcase>` as the parent :ref:`class<what is a class?>` of ``TestClasses``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5-6

    class WObject(object): pass


    # class Class(object):
    # class TestClasses(object):
    class TestClasses(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'unittest' is not defined.
               Did you forget to import 'unittest'?

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import unittest


    class WPass: pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

* I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 6-7

    # class Class(object):
    # class TestClasses(object):
    class TestClasses(unittest.TestCase):

        def test_failure(self):
            # self.assertEqual(True, False)
            self.assertEqual(True, True)


    def test_making_a_class_w_pass():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 10

    class WObject(object): pass


    class TestClasses(unittest.TestCase):

        def test_failure(self):
            self.assertEqual(True, True)


    def test_making_a_class_w_pass():

* I open a new terminal_ then make sure I am in the ``classes`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd classes

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add TestClasses class'

----

*********************************************************************************
test_making_a_class_w_pass with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_making_a_class_w_pass` to make it a :ref:`method<what is a method?>` of the :ref:`TestClasses class<add TestClasses class>` and replace ``test_failure``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3-5

    class TestClasses(unittest.TestCase):

        def test_making_a_class_w_pass():
            assert isinstance(WPass(), object)
            assert issubclass(WPass, object)


    def test_making_a_class_w_parentheses():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestClasses.test_making_a_class_w_pass()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_making_a_class_w_pass`

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 1-2

      # def test_making_a_class_w_pass():
      def test_making_a_class_w_pass(self):

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsInstance method<test_assert_not_is_instance>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 4

        # def test_making_a_class_w_pass():
        def test_making_a_class_w_pass(self):
            assert isinstance(WPass(), object)
            self.assertNotIsInstance(WPass(), object)

            assert issubclass(WPass, object)


    def test_making_a_class_w_parentheses():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <tests.test_classes.WPass object at 0xffff01234a567>
        is an instance of <class 'object'>

* I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to :ref:`assertIsInstance<test_assert_is_instance>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 4-5

        # def test_making_a_class_w_pass():
        def test_making_a_class_w_pass(self):
            assert isinstance(WPass(), object)
            # self.assertNotIsInstance(WPass(), object)
            self.assertIsInstance(WPass(), object)

            assert issubclass(WPass, object)


    def test_making_a_class_w_parentheses():

  the test passes.

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsSubclass method<test_assert_not_is_subclass>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 8

        # def test_making_a_class_w_pass():
        def test_making_a_class_w_pass(self):
            assert isinstance(WPass(), object)
            # self.assertNotIsInstance(WPass(), object)
            self.assertIsInstance(WPass(), object)

            assert issubclass(WPass, object)
            self.assertNotIsSubclass(WPass, object)


    def test_making_a_class_w_parentheses():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'tests.test_classes.WPass'>
        is a subclass of <class 'object'>

* I change :ref:`assertNotIsSubclass<test_assert_not_is_subclass>` to :ref:`assertIsSubclass<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 8-9

        # def test_making_a_class_w_pass():
        def test_making_a_class_w_pass(self):
            assert isinstance(WPass(), object)
            # self.assertNotIsInstance(WPass(), object)
            self.assertIsInstance(WPass(), object)

            assert issubclass(WPass, object)
            # self.assertNotIsSubclass(WPass, object)
            self.assertIsSubclass(WPass, object)


    def test_making_a_class_w_parentheses():

  the test passes.

* I remove the commented lines from :ref:`test_making_a_class_w_pass`

  .. code-block:: python
    :lineno-start: 13

    class TestClasses(unittest.TestCase):

        def test_making_a_class_w_pass(self):
            assert isinstance(WPass(), object)
            self.assertIsInstance(WPass(), object)

            assert issubclass(WPass, object)
            self.assertIsSubclass(WPass, object)


    def test_making_a_class_w_parentheses():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_making_a_class_w_pass to TestClasses'

----

*********************************************************************************
test_making_a_class_w_parentheses with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_making_a_class_w_parentheses` to make it a :ref:`method<what is a method?>` of the :ref:`TestClasses class<add TestClasses class>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 3-5

            self.assertIsSubclass(WPass, object)

        def test_making_a_class_w_parentheses():
            assert isinstance(WParentheses(), object)
            assert issubclass(WParentheses, object)


    def test_making_a_class_w_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestClasses.test_making_a_class_w_parentheses()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_making_a_class_w_parentheses`

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 1-2

      # def test_making_a_class_w_parentheses():
      def test_making_a_class_w_parentheses(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsInstance method<test_assert_not_is_instance>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4-6

        # def test_making_a_class_w_parentheses():
        def test_making_a_class_w_parentheses(self):
            assert isinstance(WParentheses(), object)
            self.assertNotIsInstance(
                WParentheses(), object
            )

            assert issubclass(WParentheses, object)


    def test_making_a_class_w_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <tests.test_classes.WPass object at 0xffff56789b123>
        is an instance of <class 'object'>

* I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to :ref:`assertIsInstance<test_assert_is_instance>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4-5

        # def test_making_a_class_w_parentheses():
        def test_making_a_class_w_parentheses(self):
            assert isinstance(WParentheses(), object)
            # self.assertNotIsInstance(
            self.assertIsInstance(
                WParentheses(), object
            )

            assert issubclass(WParentheses, object)


    def test_making_a_class_w_object():

  the test passes.

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsSubclass method<test_assert_not_is_subclass>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 10-12

        # def test_making_a_class_w_parentheses():
        def test_making_a_class_w_parentheses(self):
            assert isinstance(WParentheses(), object)
            # self.assertNotIsInstance(
            self.assertIsInstance(
                WParentheses(), object
            )

            assert issubclass(WParentheses, object)
            self.assertNotIsSubclass(
                WParentheses, object
            )


    def test_making_a_class_w_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'tests.test_classes.WParentheses'>
        is a subclass of <class 'object'>

* I change :ref:`assertNotIsSubclass<test_assert_not_is_subclass>` to :ref:`assertIsSubclass<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 10-11

        # def test_making_a_class_w_parentheses():
        def test_making_a_class_w_parentheses(self):
            assert isinstance(WParentheses(), object)
            # self.assertNotIsInstance(
            self.assertIsInstance(
                WParentheses(), object
            )

            assert issubclass(WParentheses, object)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                WParentheses, object
            )


    def test_making_a_class_w_object():

  the test passes.

* I remove the commented lines from :ref:`test_making_a_class_w_parentheses`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 5, 8

            self.assertIsSubclass(WPass, object)

        def test_making_a_class_w_parentheses(self):
            assert isinstance(WParentheses(), object)
            self.assertIsInstance(WParentheses(), object)

            assert issubclass(WParentheses, object)
            self.assertIsSubclass(WParentheses, object)


    def test_making_a_class_w_object():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_making_a_class_w_parentheses to TestClasses'

----

*********************************************************************************
test_making_a_class_w_object with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_making_a_class_w_object` to make it a :ref:`method<what is a method?>` of the :ref:`TestClasses class<add TestClasses class>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3-5

            self.assertIsSubclass(WParentheses, object)

        def test_making_a_class_w_object():
            assert isinstance(WObject(), object)
            assert issubclass(WObject, object)


    def test_is_none_an_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestClasses.test_making_a_class_w_object()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_making_a_class_w_object`

.. code-block:: python
  :lineno-start: 29
  :emphasize-lines: 1-2

      # def test_making_a_class_w_object():
      def test_making_a_class_w_object(self):

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsInstance method<test_assert_not_is_instance>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 4

        # def test_making_a_class_w_object():
        def test_making_a_class_w_object(self):
            assert isinstance(WObject(), object)
            self.assertNotIsInstance(WObject(), object)

            assert issubclass(WObject, object)


    def test_is_none_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <tests.test_classes.WPass object at 0xffffabcde0f12>
        is an instance of <class 'object'>

* I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to :ref:`assertIsInstance<test_assert_is_instance>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 4-5

        # def test_making_a_class_w_object():
        def test_making_a_class_w_object(self):
            assert isinstance(WObject(), object)
            # self.assertNotIsInstance(WObject(), object)
            self.assertIsInstance(WObject(), object)

            assert issubclass(WObject, object)


    def test_is_none_an_object():

  the test passes.

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsSubclass method<test_assert_not_is_subclass>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 8

        # def test_making_a_class_w_object():
        def test_making_a_class_w_object(self):
            assert isinstance(WObject(), object)
            # self.assertNotIsInstance(WObject(), object)
            self.assertIsInstance(WObject(), object)

            assert issubclass(WObject, object)
            self.assertNotIsSubclass(WObject, object)


    def test_is_none_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'tests.test_classes.WObject'>
        is a subclass of <class 'object'>

* I change :ref:`assertNotIsSubclass<test_assert_not_is_subclass>` to :ref:`assertIsSubclass<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 8-9

        # def test_making_a_class_w_object():
        def test_making_a_class_w_object(self):
            assert isinstance(WObject(), object)
            # self.assertNotIsInstance(WObject(), object)
            self.assertIsInstance(WObject(), object)

            assert issubclass(WObject, object)
            # self.assertNotIsSubclass(WObject, object)
            self.assertIsSubclass(WObject, object)


    def test_is_none_an_object():

  the test passes.

* I remove the commented lines from :ref:`test_making_a_class_w_object`

  .. code-block:: python
    :lineno-start: 27

            self.assertIsSubclass(WParentheses, object)

        def test_making_a_class_w_object(self):
            assert isinstance(WObject(), object)
            self.assertIsInstance(WObject(), object)

            assert issubclass(WObject, object)
            self.assertIsSubclass(WObject, object)


    def test_is_none_an_object():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_making_a_class_w_object to TestClasses'

----

*********************************************************************************
test_is_none_an_object with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_is_none_an_object` to make it a :ref:`method<what is a method?>` of the :ref:`TestClasses class<add TestClasses class>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 3-6

            self.assertIsSubclass(WObject, object)

        def test_is_none_an_object():
            assert isinstance(None, object)
            # fails because None is not a class
            # assert issubclass(None, object)


    def test_is_a_boolean_an_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestClasses.test_is_none_an_object()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_is_none_an_object`

.. code-block:: python
  :lineno-start: 36
  :emphasize-lines: 1-2

      # def test_is_none_an_object():
      def test_is_none_an_object(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsInstance method<test_assert_not_is_instance>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 4

        # def test_is_none_an_object():
        def test_is_none_an_object(self):
            assert isinstance(None, object)
            self.assertNotIsInstance(None, object)

            # fails because None is not a class
            # assert issubclass(None, object)


    def test_is_a_boolean_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        None is an instance of <class 'object'>

* I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to :ref:`assertIsInstance<test_assert_is_instance>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 4-5

        # def test_is_none_an_object():
        def test_is_none_an_object(self):
            assert isinstance(None, object)
            # self.assertNotIsInstance(None, object)
            self.assertIsInstance(None, object)

            # fails because None is not a class
            # assert issubclass(None, object)


    def test_is_a_boolean_an_object():

  the test passes.

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertIsSubclass method<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 9

        # def test_is_none_an_object():
        def test_is_none_an_object(self):
            assert isinstance(None, object)
            # self.assertNotIsInstance(None, object)
            self.assertIsInstance(None, object)

            # fails because None is not a class
            # assert issubclass(None, object)
            self.assertIsSubclass(None, object)


    def test_is_a_boolean_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not a class

* I comment out the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 9

        # def test_is_none_an_object():
        def test_is_none_an_object(self):
            assert isinstance(None, object)
            # self.assertNotIsInstance(None, object)
            self.assertIsInstance(None, object)

            # fails because None is not a class
            # assert issubclass(None, object)
            # self.assertIsSubclass(None, object)


    def test_is_a_boolean_an_object():

  the test passes.

* I remove the other commented lines from :ref:`test_is_none_an_object`

  .. code-block:: python
    :lineno-start: 34

            self.assertIsSubclass(WObject, object)

        def test_is_none_an_object(self):
            assert isinstance(None, object)
            self.assertIsInstance(None, object)

            # fails because None is not a class
            # assert issubclass(None, object)
            # self.assertIsSubclass(None, object)


    def test_is_a_boolean_an_object():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_is_none_an_object to TestClasses'

----

*********************************************************************************
test_is_a_boolean_an_object with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_is_a_boolean_an_object` to make it a :ref:`method<what is a method?>` of the :ref:`TestClasses class<add TestClasses class>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 3-5

            # self.assertIsSubclass(None, object)

        def test_is_a_boolean_an_object():
            assert isinstance(bool, object)
            assert issubclass(bool, object)


    def test_is_an_integer_an_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestClasses.test_is_a_boolean_an_object()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_is_a_boolean_an_object`

.. code-block:: python
  :lineno-start: 44
  :emphasize-lines: 1-2

      # def test_is_a_boolean_an_object():
      def test_is_a_boolean_an_object(self):

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsInstance<test_assert_not_is_instance>` and :ref:`assertNotIsSubclass methods<test_assert_not_is_subclass>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 4, 7

        # def test_is_a_boolean_an_object():
        def test_is_a_boolean_an_object(self):
            assert isinstance(bool, object)
            self.assertNotIsInstance(bool, object)

            assert issubclass(bool, object)
            self.assertNotIsSubclass(bool, object)


    def test_is_an_integer_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'bool'>
        is an instance of <class 'object'>

* I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to :ref:`assertIsInstance<test_assert_is_instance>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 4-5

        # def test_is_a_boolean_an_object():
        def test_is_a_boolean_an_object(self):
            assert isinstance(bool, object)
            # self.assertNotIsInstance(bool, object)
            self.assertIsInstance(bool, object)

            assert issubclass(bool, object)
            self.assertNotIsSubclass(bool, object)


    def test_is_an_integer_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'bool'>
        is a subclass of <class 'object'>

* I change :ref:`assertNotIsSubclass<test_assert_not_is_subclass>` to :ref:`assertIsSubclass<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 8-9

        # def test_is_a_boolean_an_object():
        def test_is_a_boolean_an_object(self):
            assert isinstance(bool, object)
            # self.assertNotIsInstance(bool, object)
            self.assertIsInstance(bool, object)

            assert issubclass(bool, object)
            # self.assertNotIsSubclass(bool, object)
            self.assertIsSubclass(bool, object)


    def test_is_an_integer_an_object():

  the test passes.

* I remove the commented lines from :ref:`test_is_a_boolean_an_object`

  .. code-block:: python
    :lineno-start: 42

            # self.assertIsSubclass(None, object)

        def test_is_a_boolean_an_object(self):
            assert isinstance(bool, object)
            self.assertIsInstance(bool, object)

            assert issubclass(bool, object)
            self.assertIsSubclass(bool, object)


    def test_is_an_integer_an_object():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_is_a_boolean_an_object to TestClasses'

----

*********************************************************************************
test_is_an_integer_an_object with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_is_an_integer_an_object` to make it a :ref:`method<what is a method?>` of the :ref:`TestClasses class<add TestClasses class>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 3-5

            self.assertIsSubclass(bool, object)

        def test_is_an_integer_an_object():
            assert isinstance(int, object)
            assert issubclass(int, object)


    def test_is_a_float_an_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestClasses.test_is_an_integer_an_object()
        takes 0 positional arguments but 1 was given

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_is_an_integer_an_object`

.. code-block:: python
  :lineno-start: 51
  :emphasize-lines: 1-2

      # def test_is_an_integer_an_object():
      def test_is_an_integer_an_object(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsInstance<test_assert_not_is_instance>` and :ref:`assertNotIsSubclass methods<test_assert_not_is_subclass>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 4, 7

        # def test_is_an_integer_an_object():
        def test_is_an_integer_an_object(self):
            assert isinstance(int, object)
            self.assertNotIsInstance(int, object)

            assert issubclass(int, object)
            self.assertNotIsSubclass(int, object)


    def test_is_a_float_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'int'>
        is an instance of <class 'object'>

* I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to :ref:`assertIsInstance<test_assert_is_instance>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 4-5

        # def test_is_an_integer_an_object():
        def test_is_an_integer_an_object(self):
            assert isinstance(int, object)
            # self.assertNotIsInstance(int, object)
            self.assertIsInstance(int, object)

            assert issubclass(int, object)
            self.assertNotIsSubclass(int, object)


    def test_is_a_float_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'int'>
        is a subclass of <class 'object'>

* I change :ref:`assertNotIsSubclass<test_assert_not_is_subclass>` to :ref:`assertIsSubclass<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 8-9

        # def test_is_an_integer_an_object():
        def test_is_an_integer_an_object(self):
            assert isinstance(int, object)
            # self.assertNotIsInstance(int, object)
            self.assertIsInstance(int, object)

            assert issubclass(int, object)
            # self.assertNotIsSubclass(int, object)
            self.assertIsSubclass(int, object)


    def test_is_a_float_an_object():

  the test passes.

* I remove the commented lines from :ref:`test_is_an_integer_an_object`

  .. code-block:: python
    :lineno-start: 49

            self.assertIsSubclass(bool, object)

        def test_is_an_integer_an_object(self):
            assert isinstance(int, object)
            self.assertIsInstance(int, object)

            assert issubclass(int, object)
            self.assertIsSubclass(int, object)


    def test_is_a_float_an_object():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_is_an_integer_an_object to TestClasses'

----

*********************************************************************************
test_is_a_float_an_object with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_is_a_float_an_object` to make it a :ref:`method<what is a method?>` of the :ref:`TestClasses class<add TestClasses class>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 3-5

            self.assertIsSubclass(int, object)

        def test_is_a_float_an_object():
            assert isinstance(float, object)
            assert issubclass(float, object)


    def test_is_a_string_an_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestClasses.test_is_a_float_an_object()
        takes 0 positional arguments but 1 was given

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_is_a_float_an_object`

.. code-block:: python
  :lineno-start: 58
  :emphasize-lines: 1-2

      # def test_is_a_float_an_object():
      def test_is_a_float_an_object(self):

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsInstance<test_assert_not_is_instance>` and :ref:`assertNotIsSubclass methods<test_assert_not_is_subclass>`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 4, 7

        # def test_is_a_float_an_object():
        def test_is_a_float_an_object(self):
            assert isinstance(float, object)
            self.assertNotIsInstance(float, object)

            assert issubclass(float, object)
            self.assertNotIsSubclass(float, object)


    def test_is_a_string_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'float'>
        is an instance of <class 'object'>

* I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to :ref:`assertIsInstance<test_assert_is_instance>`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 4-5

        # def test_is_a_float_an_object():
        def test_is_a_float_an_object(self):
            assert isinstance(float, object)
            # self.assertNotIsInstance(float, object)
            self.assertIsInstance(float, object)

            assert issubclass(float, object)
            self.assertNotIsSubclass(float, object)


    def test_is_a_string_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'float'>
        is a subclass of <class 'object'>

* I change :ref:`assertNotIsSubclass<test_assert_not_is_subclass>` to :ref:`assertIsSubclass<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 8-9

        # def test_is_a_float_an_object():
        def test_is_a_float_an_object(self):
            assert isinstance(float, object)
            # self.assertNotIsInstance(float, object)
            self.assertIsInstance(float, object)

            assert issubclass(float, object)
            # self.assertNotIsSubclass(float, object)
            self.assertIsSubclass(float, object)


    def test_is_a_string_an_object():

  the test passes.

* I remove the commented lines from :ref:`test_is_a_float_an_object`

  .. code-block:: python
    :lineno-start: 56

            self.assertIsSubclass(int, object)

        def test_is_a_float_an_object(self):
            assert isinstance(float, object)
            self.assertIsInstance(float, object)

            assert issubclass(float, object)
            self.assertIsSubclass(float, object)


    def test_is_a_string_an_object():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_is_a_float_an_object to TestClasses'

----

*********************************************************************************
test_is_a_string_an_object with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_is_a_string_an_object` to make it a :ref:`method<what is a method?>` of the :ref:`TestClasses class<add TestClasses class>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3-5

            self.assertIsSubclass(float, object)

        def test_is_a_string_an_object():
            assert isinstance(str, object)
            assert issubclass(str, object)


    def test_is_a_tuple_an_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestClasses.test_is_a_string_an_object()
        takes 0 positional arguments but 1 was given

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_is_a_string_an_object`

.. code-block:: python
  :lineno-start: 65
  :emphasize-lines: 1-2

      # def test_is_a_string_an_object():
      def test_is_a_string_an_object(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsInstance<test_assert_not_is_instance>` and :ref:`assertNotIsSubclass methods<test_assert_not_is_subclass>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 4, 7

        # def test_is_a_string_an_object():
        def test_is_a_string_an_object(self):
            assert isinstance(str, object)
            self.assertNotIsInstance(str, object)

            assert issubclass(str, object)
            self.assertNotIsSubclass(str, object)


    def test_is_a_tuple_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'str'>
        is an instance of <class 'object'>

* I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to :ref:`assertIsInstance<test_assert_is_instance>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 4-5

        # def test_is_a_string_an_object():
        def test_is_a_string_an_object(self):
            assert isinstance(str, object)
            # self.assertNotIsInstance(str, object)
            self.assertIsInstance(str, object)

            assert issubclass(str, object)
            self.assertNotIsSubclass(str, object)


    def test_is_a_tuple_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'str'>
        is a subclass of <class 'object'>

* I change :ref:`assertNotIsSubclass<test_assert_not_is_subclass>` to :ref:`assertIsSubclass<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 8-9

        # def test_is_a_string_an_object():
        def test_is_a_string_an_object(self):
            assert isinstance(str, object)
            # self.assertNotIsInstance(str, object)
            self.assertIsInstance(str, object)

            assert issubclass(str, object)
            # self.assertNotIsSubclass(str, object)
            self.assertIsSubclass(str, object)


    def test_is_a_tuple_an_object():

  the test passes.

* I remove the commented lines from :ref:`test_is_a_string_an_object`

  .. code-block:: python
    :lineno-start: 63

            self.assertIsSubclass(float, object)

        def test_is_a_string_an_object(self):
            assert isinstance(str, object)
            self.assertIsInstance(str, object)

            assert issubclass(str, object)
            self.assertIsSubclass(str, object)


    def test_is_a_tuple_an_object():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_is_a_string_an_object to TestClasses'

----

*********************************************************************************
test_is_a_tuple_an_object with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_is_a_tuple_an_object` to make it a :ref:`method<what is a method?>` of the :ref:`TestClasses class<add TestClasses class>`

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 3-5

            self.assertIsSubclass(str, object)

        def test_is_a_tuple_an_object():
            assert isinstance(tuple, object)
            assert issubclass(tuple, object)


    def test_is_a_list_an_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestClasses.test_is_a_tuple_an_object()
        takes 0 positional arguments but 1 was given

  because ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_is_a_tuple_an_object`

.. code-block:: python
  :lineno-start: 72
  :emphasize-lines: 1-2

      # def test_is_a_tuple_an_object():
      def test_is_a_tuple_an_object(self):

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsInstance<test_assert_not_is_instance>` and :ref:`assertNotIsSubclass methods<test_assert_not_is_subclass>`

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 4, 7

        # def test_is_a_tuple_an_object():
        def test_is_a_tuple_an_object(self):
            assert isinstance(tuple, object)
            self.assertNotIsInstance(tuple, object)

            assert issubclass(tuple, object)
            self.assertNotIsSubclass(tuple, object)


    def test_is_a_list_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'tuple'>
        is an instance of <class 'object'>

* I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to :ref:`assertIsInstance<test_assert_is_instance>`

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 4-5

        # def test_is_a_tuple_an_object():
        def test_is_a_tuple_an_object(self):
            assert isinstance(tuple, object)
            # self.assertNotIsInstance(tuple, object)
            self.assertIsInstance(tuple, object)

            assert issubclass(tuple, object)
            self.assertNotIsSubclass(tuple, object)


    def test_is_a_list_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'tuple'>
        is a subclass of <class 'object'>

* I change :ref:`assertNotIsSubclass<test_assert_not_is_subclass>` to :ref:`assertIsSubclass<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 8-9

        # def test_is_a_tuple_an_object():
        def test_is_a_tuple_an_object(self):
            assert isinstance(tuple, object)
            # self.assertNotIsInstance(tuple, object)
            self.assertIsInstance(tuple, object)

            assert issubclass(tuple, object)
            # self.assertNotIsSubclass(tuple, object)
            self.assertIsSubclass(tuple, object)


    def test_is_a_list_an_object():

  the test passes.

* I remove the commented lines from :ref:`test_is_a_tuple_an_object`

  .. code-block:: python
    :lineno-start: 70

            self.assertIsSubclass(str, object)

        def test_is_a_tuple_an_object(self):
            assert isinstance(tuple, object)
            self.assertIsInstance(tuple, object)

            assert issubclass(tuple, object)
            self.assertIsSubclass(tuple, object)


    def test_is_a_list_an_object():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_is_a_tuple_an_object to TestClasses'

----

*********************************************************************************
test_is_a_list_an_object with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_is_a_list_an_object` to make it a :ref:`method<what is a method?>` of the :ref:`TestClasses class<add TestClasses class>`

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 3-5

            self.assertIsSubclass(tuple, object)

        def test_is_a_list_an_object():
            assert isinstance(list, object)
            assert issubclass(list, object)


    def test_is_a_set_an_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestClasses.test_is_a_list_an_object()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_is_a_list_an_object`

.. code-block:: python
  :lineno-start: 79
  :emphasize-lines: 1-2

      # def test_is_a_list_an_object():
      def test_is_a_list_an_object(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsInstance<test_assert_not_is_instance>` and :ref:`assertNotIsSubclass methods<test_assert_not_is_subclass>`

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 4, 7

        # def test_is_a_list_an_object():
        def test_is_a_list_an_object(self):
            assert isinstance(list, object)
            self.assertNotIsInstance(list, object)

            assert issubclass(list, object)
            self.assertNotIsSubclass(list, object)


    def test_is_a_set_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'list'>
        is an instance of <class 'object'>

* I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to :ref:`assertIsInstance<test_assert_is_instance>`

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 4-5

        # def test_is_a_list_an_object():
        def test_is_a_list_an_object(self):
            assert isinstance(list, object)
            # self.assertNotIsInstance(list, object)
            self.assertIsInstance(list, object)

            assert issubclass(list, object)
            self.assertNotIsSubclass(list, object)


    def test_is_a_set_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'list'>
        is a subclass of <class 'object'>

* I change :ref:`assertNotIsSubclass<test_assert_not_is_subclass>` to :ref:`assertIsSubclass<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 8-9

        # def test_is_a_list_an_object():
        def test_is_a_list_an_object(self):
            assert isinstance(list, object)
            # self.assertNotIsInstance(list, object)
            self.assertIsInstance(list, object)

            assert issubclass(list, object)
            # self.assertNotIsSubclass(list, object)
            self.assertIsSubclass(list, object)


    def test_is_a_set_an_object():

  the test passes.

* I remove the commented lines from :ref:`test_is_a_list_an_object`

  .. code-block:: python
    :lineno-start: 77

            self.assertIsSubclass(tuple, object)

        def test_is_a_list_an_object(self):
            assert isinstance(list, object)
            self.assertIsInstance(list, object)

            assert issubclass(list, object)
            self.assertIsSubclass(list, object)


    def test_is_a_set_an_object():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_is_a_list_an_object to TestClasses'

----

*********************************************************************************
test_is_a_set_an_object with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_is_a_set_an_object` to make it a :ref:`method<what is a method?>` of the :ref:`TestClasses class<add TestClasses class>`

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 3-5

            self.assertIsSubclass(list, object)

        def test_is_a_set_an_object():
            assert isinstance(set, object)
            assert issubclass(set, object)


    def test_is_a_dictionary_an_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestClasses.test_is_a_set_an_object()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_is_a_set_an_object`

.. code-block:: python
  :lineno-start: 86
  :emphasize-lines: 1-2

      # def test_is_a_set_an_object():
      def test_is_a_set_an_object(self):

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsInstance<test_assert_not_is_instance>` and :ref:`assertNotIsSubclass methods<test_assert_not_is_subclass>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 4, 7

        # def test_is_a_set_an_object():
        def test_is_a_set_an_object(self):
            assert isinstance(set, object)
            self.assertNotIsInstance(set, object)

            assert issubclass(set, object)
            self.assertNotIsSubclass(set, object)


    def test_is_a_dictionary_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'set'>
        is an instance of <class 'object'>

* I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to :ref:`assertIsInstance<test_assert_is_instance>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 4-5

        # def test_is_a_set_an_object():
        def test_is_a_set_an_object(self):
            assert isinstance(set, object)
            # self.assertNotIsInstance(set, object)
            self.assertIsInstance(set, object)

            assert issubclass(set, object)
            self.assertNotIsSubclass(set, object)


    def test_is_a_dictionary_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'set'>
        is a subclass of <class 'object'>

* I change :ref:`assertNotIsSubclass<test_assert_not_is_subclass>` to :ref:`assertIsSubclass<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 8-9

        # def test_is_a_set_an_object():
        def test_is_a_set_an_object(self):
            assert isinstance(set, object)
            # self.assertNotIsInstance(set, object)
            self.assertIsInstance(set, object)

            assert issubclass(set, object)
            # self.assertNotIsSubclass(set, object)
            self.assertIsSubclass(set, object)


    def test_is_a_dictionary_an_object():

  the test passes.

* I remove the commented lines from :ref:`test_is_a_set_an_object`

  .. code-block:: python
    :lineno-start: 84

            self.assertIsSubclass(list, object)

        def test_is_a_set_an_object(self):
            assert isinstance(set, object)
            self.assertIsInstance(set, object)

            assert issubclass(set, object)
            self.assertIsSubclass(set, object)


    def test_is_a_dictionary_an_object():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_is_a_set_an_object to TestClasses'

----

*********************************************************************************
test_is_a_dictionary_an_object with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_is_a_dictionary_an_object` to make it a :ref:`method<what is a method?>` of the :ref:`TestClasses class<add TestClasses class>`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 3-5

            self.assertIsSubclass(set, object)

        def test_is_a_dictionary_an_object():
            assert isinstance(dict, object)
            assert issubclass(dict, object)


    def test_dir_of_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestClasses.test_is_a_dictionary_an_object()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_is_a_dictionary_an_object`

.. code-block:: python
  :lineno-start: 93
  :emphasize-lines: 1-2

      # def test_is_a_dictionary_an_object():
      def test_is_a_dictionary_an_object(self):

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsInstance<test_assert_not_is_instance>` and :ref:`assertNotIsSubclass methods<test_assert_not_is_subclass>`

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 4, 7

        # def test_is_a_dictionary_an_object():
        def test_is_a_dictionary_an_object(self):
            assert isinstance(dict, object)
            self.assertNotIsInstance(dict, object)

            assert issubclass(dict, object)
            self.assertNotIsSubclass(dict, object)


    def test_dir_of_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'dict>
        is an instance of <class 'object'>

* I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to :ref:`assertIsInstance<test_assert_is_instance>`

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 4-5

        # def test_is_a_dictionary_an_object():
        def test_is_a_dictionary_an_object(self):
            assert isinstance(dict, object)
            # self.assertNotIsInstance(dict, object)
            self.assertIsInstance(dict, object)

            assert issubclass(dict, object)
            self.assertNotIsSubclass(dict, object)


    def test_dir_of_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'dict'>
        is a subclass of <class 'object'>

* I change :ref:`assertNotIsSubclass<test_assert_not_is_subclass>` to :ref:`assertIsSubclass<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 8-9

        # def test_is_a_dictionary_an_object():
        def test_is_a_dictionary_an_object(self):
            assert isinstance(dict, object)
            # self.assertNotIsInstance(dict, object)
            self.assertIsInstance(dict, object)

            assert issubclass(dict, object)
            # self.assertNotIsSubclass(dict, object)
            self.assertIsSubclass(dict, object)


    def test_dir_of_object():

  the test passes.

* I remove the commented lines from :ref:`test_is_a_dictionary_an_object`

  .. code-block:: python
    :lineno-start: 91

            self.assertIsSubclass(set, object)

        def test_is_a_dictionary_an_object(self):
            assert isinstance(dict, object)
            self.assertIsInstance(dict, object)

            assert issubclass(dict, object)
            self.assertIsSubclass(dict, object)


    def test_dir_of_object():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_is_a_dictionary_an_object to TestClasses'

----

*********************************************************************************
review
*********************************************************************************

I can use the :ref:`unittest library<another way to write tests>` to write tests with the :ref:`methods of the unittest.TestCase class<test_dir_unittest_testcase>` or I can write them with bare :ref:`assert statements<what is an assertion?>`.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_classes.py`` and ``classes.py`` in the :ref:`editor(s)<2 editors>`
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``classes``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test objects with unittest: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

You know

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

:ref:`Would you like to test the classes project with the unittest library?<test classes with unittest>`

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