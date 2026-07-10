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

    TypeError: TestClasses.test_making_a_class_w_pass() takes
               0 positional arguments but 1 was given

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
    :emphasize-lines: 4-6

        # def test_making_a_class_w_pass():
        def test_making_a_class_w_pass(self):
            assert isinstance(WPass(), object)
            self.assertNotIsInstance(
                WPass(), object
            )
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
            # self.assertNotIsInstance(
            self.assertIsInstance(
                WPass(), object
            )
            assert issubclass(WPass, object)


    def test_making_a_class_w_parentheses():

  the test passes.

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsSubclass method<test_assert_not_is_subclass>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 9-11

        # def test_making_a_class_w_pass():
        def test_making_a_class_w_pass(self):
            assert isinstance(WPass(), object)
            # self.assertNotIsInstance(
            self.assertIsInstance(
                WPass(), object
            )
            assert issubclass(WPass, object)
            self.assertNotIsSubclass(
                WPass, object
            )


    def test_making_a_class_w_parentheses():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'tests.test_classes.WPass'>
        is a subclass of <class 'object'>

* I change :ref:`assertNotIsSubclass<test_assert_not_is_subclass>` to :ref:`assertIsSubclass<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 9-10

        # def test_making_a_class_w_pass():
        def test_making_a_class_w_pass(self):
            assert isinstance(WPass(), object)
            # self.assertNotIsInstance(
            self.assertIsInstance(
                WPass(), object
            )
            assert issubclass(WPass, object)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                WPass, object
            )


    def test_making_a_class_w_parentheses():

  the test passes.

* I remove the commented lines from :ref:`test_making_a_class_w_pass`

  .. code-block:: python
    :lineno-start: 13

    class TestClasses(unittest.TestCase):

        def test_making_a_class_w_pass(self):
            assert isinstance(WPass(), object)
            self.assertIsInstance(
                WPass(), object
            )

            assert issubclass(WPass, object)
            self.assertIsSubclass(
                WPass, object
            )


    def test_making_a_class_w_parentheses():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_making_a_class_w_pass to TestClasses'

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

    TypeError: TestClasses.test_making_a_class_w_pass() takes
               0 positional arguments but 1 was given

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
    :emphasize-lines: 4-6

        # def test_making_a_class_w_pass():
        def test_making_a_class_w_pass(self):
            assert isinstance(WPass(), object)
            self.assertNotIsInstance(
                WPass(), object
            )
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
            # self.assertNotIsInstance(
            self.assertIsInstance(
                WPass(), object
            )
            assert issubclass(WPass, object)


    def test_making_a_class_w_parentheses():

  the test passes.

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotIsSubclass method<test_assert_not_is_subclass>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 9-11

        # def test_making_a_class_w_pass():
        def test_making_a_class_w_pass(self):
            assert isinstance(WPass(), object)
            # self.assertNotIsInstance(
            self.assertIsInstance(
                WPass(), object
            )
            assert issubclass(WPass, object)
            self.assertNotIsSubclass(
                WPass, object
            )


    def test_making_a_class_w_parentheses():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'tests.test_classes.WPass'>
        is a subclass of <class 'object'>

* I change :ref:`assertNotIsSubclass<test_assert_not_is_subclass>` to :ref:`assertIsSubclass<test_assert_is_subclass>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 9-10

        # def test_making_a_class_w_pass():
        def test_making_a_class_w_pass(self):
            assert isinstance(WPass(), object)
            # self.assertNotIsInstance(
            self.assertIsInstance(
                WPass(), object
            )
            assert issubclass(WPass, object)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                WPass, object
            )


    def test_making_a_class_w_parentheses():

  the test passes.

* I remove the commented lines from :ref:`test_making_a_class_w_pass`

  .. code-block:: python
    :lineno-start: 13

    class TestClasses(unittest.TestCase):

        def test_making_a_class_w_pass(self):
            assert isinstance(WPass(), object)
            self.assertIsInstance(
                WPass(), object
            )

            assert issubclass(WPass, object)
            self.assertIsSubclass(
                WPass, object
            )


    def test_making_a_class_w_parentheses():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_making_a_class_w_pass to TestClasses'

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