.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): test telephone with unittest — move the telephone project's bare assert tests onto unittest.TestCase. Open telephone; uv run pytest-watcher . --now (10 passed). Add class Telephone then rename to TestTelephone → AttributeError: 'TestTelephone' object has no attribute 'assertEqual'. Parent unittest.TestCase → NameError name 'unittest' is not defined; import unittest → AssertionError: True != False then green with assertEqual(True, True). For each test (test_passing_none, booleans, int 1234, float 5.678, string 'hello', tuple/list/set/dict, classes object/bool/int/…): move into TestTelephone → TypeError takes 0 positional arguments but 1 was given (need self); add assertNotEqual → AssertionError e.g. 'I got: None' == 'I got: None' / "I got: [0, 1, 2, 'n']"; switch to assertEqual; keep bare assert + self.assertEqual; remove the commented lines; git commit. Ends with TestTelephone + 10 methods + # Exceptions seen AssertionError NameError TypeError ModuleNotFoundError AttributeError. Review: unittest.TestCase methods or bare assert statements.
  :keywords: Jacob Itegboje, Pumping Python, test telephone with unittest, telephone unittest, TestTelephone, unittest.TestCase, import unittest, AttributeError has no attribute assertEqual, NameError name 'unittest' is not defined, AssertionError True != False, TypeError takes 0 positional arguments but 1 was given, self first argument method, assertNotEqual, assertEqual, 'I got: None' == 'I got: None', I got: False, I got: True, an_integer 1234, a_float 5.678, hello, I got: [0, 1, 2, 'n'], I got: <class 'object'>, reality == my_expectation, bare assert and assertEqual, uv run pytest-watcher . --now, red green refactor, remove the commented lines, git commit -am, another way to write tests, test_telephone_w_unittest

.. include:: ../../links.rst

#################################################################################
test telephone with unittest
#################################################################################

I want to use the :ref:`unittest library<another way to write tests>` in the :ref:`telephone` project.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_unittest.py
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

    cd telephone

  the terminal_ shows I am in the ``telephone`` folder_

  .. code-block:: python

    .../pumping_python/telephone

* I open ``test_telephone.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    test_telephone.py ..........                        [100%]

    =================== 10 passed in D.EFs ===================

----

*********************************************************************************
add TestTelephone class
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a :ref:`class<what is a class?>` named ``Telephone`` to ``test_telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4, 6-7

    import src.telephone


    class Telephone(object):

        def test_failure(self):
            self.assertEqual(True, False)


    def test_passing_none():

  the test is still green.

* I change the name of the :ref:`class<what is a class?>` to ``TestTelephone``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import src.telephone


    # class Telephone(object):
    class TestTelephone(object):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'TestTelephone' object
                    has no attribute 'assertEqual'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`unittest.TestCase<test_dir_unittest_testcase>` as the parent :ref:`class<what is a class?>` of ``TestTelephone``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    import src.telephone


    # class Telephone(object):
    # class TestTelephone(object):
    class TestTelephone(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'unittest' is not defined.
               Did you forget to import 'unittest'?

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import src.telephone
    import unittest


    # class Telephone(object):
    # class TestTelephone(object):
    class TestTelephone(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

* I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-3

        def test_failure(self):
            # self.assertEqual(True, False)
            self.assertEqual(True, True)


    def test_passing_none():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :linenos:

    import src.telephone
    import unittest


    class TestTelephone(unittest.TestCase):

        def test_failure(self):
            self.assertEqual(True, True)


    def test_passing_none():

* I open a new terminal_ then make sure I am in the ``telephone`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd telephone

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add TestTelephone class'

----

*********************************************************************************
test_passing_none with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_passing_none` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>` and replace ``test_failure``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3-6

    class TestTelephone(unittest.TestCase):

        def test_passing_none():
            reality = src.telephone.text(None)
            my_expectation = 'I got: None'
            assert reality == my_expectation


    def test_passing_booleans():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestTelephone.test_passing_none()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_passing_none`

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 3-4

  class TestTelephone(unittest.TestCase):

      # def test_passing_none():
      def test_passing_none(self):

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_none`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 8

    class TestTelephone(unittest.TestCase):

        # def test_passing_none():
        def test_passing_none(self):
            reality = src.telephone.text(None)
            my_expectation = 'I got: None'
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    def test_passing_booleans():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I got: None' == 'I got: None'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_none`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 8-9

    class TestTelephone(unittest.TestCase):

        # def test_passing_none():
        def test_passing_none(self):
            reality = src.telephone.text(None)
            my_expectation = 'I got: None'
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_passing_booleans():

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 5

    class TestTelephone(unittest.TestCase):

        def test_passing_none(self):
            reality = src.telephone.text(None)
            my_expectation = 'I got: None'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_passing_booleans():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_passing_none to TestTelephone'

----

*********************************************************************************
test_passing_booleans with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_passing_booleans` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3-6, 8-10

            self.assertEqual(reality, my_expectation)

        def test_passing_booleans():
            reality = src.telephone.text(False)
            my_expectation = 'I got: False'
            assert reality == my_expectation

            reality = src.telephone.text(True)
            my_expectation = 'I got: True'
            assert reality == my_expectation


    def test_passing_an_integer():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestTelephone.test_passing_booleans()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_passing_booleans`

.. code-block:: python
  :lineno-start: 11
  :emphasize-lines: 3-4

          self.assertEqual(reality, my_expectation)

      # def test_passing_booleans():
      def test_passing_booleans(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the :ref:`assertions<what is an assertion?>` in :ref:`test_passing_booleans`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 8, 13

            self.assertEqual(reality, my_expectation)

        # def test_passing_booleans():
        def test_passing_booleans(self):
            reality = src.telephone.text(False)
            my_expectation = 'I got: False'
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)

            reality = src.telephone.text(True)
            my_expectation = 'I got: True'
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    def test_passing_an_integer():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I got: False' == 'I got: False'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the first :ref:`assertion<what is an assertion?>` in :ref:`test_passing_booleans`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 6-7

        # def test_passing_booleans():
        def test_passing_booleans(self):
            reality = src.telephone.text(False)
            my_expectation = 'I got: False'
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(True)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I got: True' == 'I got: True'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the second :ref:`assertion<what is an assertion?>` in :ref:`test_passing_booleans`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 4-5

            reality = src.telephone.text(True)
            my_expectation = 'I got: True'
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_passing_an_integer():

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 11

            self.assertEqual(reality, my_expectation)

        def test_passing_booleans(self):
            reality = src.telephone.text(False)
            my_expectation = 'I got: False'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(True)
            my_expectation = 'I got: True'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_passing_an_integer():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_passing_booleans to TestTelephone'

----

*********************************************************************************
test_passing_an_integer with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_passing_an_integer` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3-4, 6-8

            self.assertEqual(reality, my_expectation)

        def test_passing_an_integer():
            an_integer = 1234

            reality = src.telephone.text(an_integer)
            my_expectation = f'I got: {an_integer}'
            assert reality == my_expectation


    def test_passing_a_float():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestTelephone.test_passing_an_integer()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_passing_an_integer`

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 3-4

          self.assertEqual(reality, my_expectation)

      # def test_passing_an_integer():
      def test_passing_an_integer(self):

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_an_integer`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 10

            self.assertEqual(reality, my_expectation)

        # def test_passing_an_integer():
        def test_passing_an_integer(self):
            an_integer = 1234

            reality = src.telephone.text(an_integer)
            my_expectation = f'I got: {an_integer}'
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    def test_passing_a_float():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I got: 1234' == 'I got: 1234'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_an_integer`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 10-11

            self.assertEqual(reality, my_expectation)

        # def test_passing_an_integer():
        def test_passing_an_integer(self):
            an_integer = 1234

            reality = src.telephone.text(an_integer)
            my_expectation = f'I got: {an_integer}'
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_passing_a_float():

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 22

            self.assertEqual(reality, my_expectation)

        def test_passing_an_integer(self):
            an_integer = 1234

            reality = src.telephone.text(an_integer)
            my_expectation = f'I got: {an_integer}'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_passing_a_float():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_passing_an_integer to TestTelephone'

----

*********************************************************************************
test_passing_a_float with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_passing_a_float` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 3-4, 6-8

            self.assertEqual(reality, my_expectation)

        def test_passing_a_float():
            a_float = 5.678

            reality = src.telephone.text(a_float)
            my_expectation = f'I got: {a_float}'
            assert reality == my_expectation


    def test_passing_a_string():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestTelephone.test_passing_a_float()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_passing_a_float`

.. code-block:: python
  :lineno-start: 30
  :emphasize-lines: 3-4

          self.assertEqual(reality, my_expectation)

      # def test_passing_a_float():
      def test_passing_a_float(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_a_float`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 10

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_float():
        def test_passing_a_float(self):
            a_float = 5.678

            reality = src.telephone.text(a_float)
            my_expectation = f'I got: {a_float}'
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    def test_passing_a_string():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I got: 5.678' == 'I got: 5.678'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_a_float`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 10-11

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_float():
        def test_passing_a_float(self):
            a_float = 5.678

            reality = src.telephone.text(a_float)
            my_expectation = f'I got: {a_float}'
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_passing_a_string():

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 30

            self.assertEqual(reality, my_expectation)

        def test_passing_a_float(self):
            a_float = 5.678

            reality = src.telephone.text(a_float)
            my_expectation = f'I got: {a_float}'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_passing_a_string():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_passing_a_float to TestTelephone'

----

*********************************************************************************
test_passing_a_string with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_passing_a_string` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 3-4, 6-8

            self.assertEqual(reality, my_expectation)

        def test_passing_a_string():
            a_string = 'hello'

            reality = src.telephone.text(a_string)
            my_expectation = f'I got: {a_string}'
            assert reality == my_expectation


    def test_passing_a_tuple():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestTelephone.test_passing_a_string()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_passing_a_string`

.. code-block:: python
  :lineno-start: 38
  :emphasize-lines: 3-4

          self.assertEqual(reality, my_expectation)

      # def test_passing_a_string():
      def test_passing_a_string(self):

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_a_string`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 10

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_string():
        def test_passing_a_string(self):
            a_string = 'hello'

            reality = src.telephone.text(a_string)
            my_expectation = f'I got: {a_string}'
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    def test_passing_a_tuple():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I got: hello' == 'I got: hello'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_a_string`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 10-11

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_string():
        def test_passing_a_string(self):
            a_string = 'hello'

            reality = src.telephone.text(a_string)
            my_expectation = f'I got: {a_string}'
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_passing_a_tuple():

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 38

            self.assertEqual(reality, my_expectation)

        def test_passing_a_string(self):
            a_string = 'hello'

            reality = src.telephone.text(a_string)
            my_expectation = f'I got: {a_string}'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_passing_a_tuple():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_passing_a_string to TestTelephone'

----

*********************************************************************************
test_passing_a_tuple with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_passing_a_tuple` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3-4, 6-8

            self.assertEqual(reality, my_expectation)

        def test_passing_a_tuple():
            a_tuple = (0, 1, 2, 'n')

            reality = src.telephone.text(a_tuple)
            my_expectation = f'I got: {a_tuple}'
            assert reality == my_expectation


    def test_passing_a_list():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestTelephone.test_passing_a_tuple()
        takes 0 positional arguments but 1 was given

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_passing_a_tuple`

.. code-block:: python
  :lineno-start: 46
  :emphasize-lines: 3-4

          self.assertEqual(reality, my_expectation)

      # def test_passing_a_tuple():
      def test_passing_a_tuple(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_a_tuple`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 10

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_tuple():
        def test_passing_a_tuple(self):
            a_tuple = (0, 1, 2, 'n')

            reality = src.telephone.text(a_tuple)
            my_expectation = f'I got: {a_tuple}'
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    def test_passing_a_list():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: [0, 1, 2, 'n']"
                 == "I got: [0, 1, 2, 'n']"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_a_tuple`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 10-11

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_tuple():
        def test_passing_a_tuple(self):
            a_tuple = (0, 1, 2, 'n')

            reality = src.telephone.text(a_tuple)
            my_expectation = f'I got: {a_tuple}'
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_passing_a_list():

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 46

            self.assertEqual(reality, my_expectation)

        def test_passing_a_tuple(self):
            a_tuple = (0, 1, 2, 'n')

            reality = src.telephone.text(a_tuple)
            my_expectation = f'I got: {a_tuple}'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_passing_a_list():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_passing_a_tuple to TestTelephone'

----

*********************************************************************************
test_passing_a_list with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_passing_a_list` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 3-4, 6-8

            self.assertEqual(reality, my_expectation)

        def test_passing_a_list():
            a_list = [0, 1, 2, 'n']

            reality = src.telephone.text(a_list)
            my_expectation = f'I got: {a_list}'
            assert reality == my_expectation


    def test_passing_a_set():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestTelephone.test_passing_a_list()
        takes 0 positional arguments but 1 was given

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_passing_a_list`

.. code-block:: python
  :lineno-start: 54
  :emphasize-lines: 3-4

          self.assertEqual(reality, my_expectation)

      # def test_passing_a_list():
      def test_passing_a_list(self):

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_a_list`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 10

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_list():
        def test_passing_a_list(self):
            a_list = [0, 1, 2, 'n']

            reality = src.telephone.text(a_list)
            my_expectation = f'I got: {a_list}'
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    def test_passing_a_set():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: (0, 1, 2, 'n')"
                 == "I got: (0, 1, 2, 'n')"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_a_list`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 10-11

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_list():
        def test_passing_a_list(self):
            a_list = [0, 1, 2, 'n']

            reality = src.telephone.text(a_list)
            my_expectation = f'I got: {a_list}'
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_passing_a_set():

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 54

            self.assertEqual(reality, my_expectation)

        def test_passing_a_list(self):
            a_list = [0, 1, 2, 'n']

            reality = src.telephone.text(a_list)
            my_expectation = f'I got: {a_list}'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_passing_a_set():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_passing_a_list to TestTelephone'

----

*********************************************************************************
test_passing_a_set with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_passing_a_set` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3-4, 6-8

            self.assertEqual(reality, my_expectation)

        def test_passing_a_set():
            a_set = {0, 1, 2, 'n'}

            reality = src.telephone.text(a_set)
            my_expectation = f'I got: {a_set}'
            assert reality == my_expectation


    def test_passing_a_dictionary():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestTelephone.test_passing_a_set()
        takes 0 positional arguments but 1 was given

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_passing_a_set`

.. code-block:: python
  :lineno-start: 62
  :emphasize-lines: 3-4

          self.assertEqual(reality, my_expectation)

      # def test_passing_a_set():
      def test_passing_a_set(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_a_set`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 10

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_set():
        def test_passing_a_set(self):
            a_set = {0, 1, 2, 'n'}

            reality = src.telephone.text(a_set)
            my_expectation = f'I got: {a_set}'
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    def test_passing_a_dictionary():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: {0, 1, 2, 'n'}"
                 == "I got: {0, 1, 2, 'n'}"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_a_set`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 10-11

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_set():
        def test_passing_a_set(self):
            a_set = {0, 1, 2, 'n'}

            reality = src.telephone.text(a_set)
            my_expectation = f'I got: {a_set}'
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_passing_a_dictionary():

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 62

            self.assertEqual(reality, my_expectation)

        def test_passing_a_set(self):
            a_set = {0, 1, 2, 'n'}

            reality = src.telephone.text(a_set)
            my_expectation = f'I got: {a_set}'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_passing_a_dictionary():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_passing_a_set to TestTelephone'

----

*********************************************************************************
test_passing_a_dictionary with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_passing_a_dictionary` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 3-7, 9-11

            self.assertEqual(reality, my_expectation)

        def test_passing_a_dictionary():
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }

            reality = src.telephone.text(a_dictionary)
            my_expectation = f'I got: {a_dictionary}'
            assert reality == my_expectation


    def test_passing_a_class():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestTelephone.test_passing_a_dictionary()
        takes 0 positional arguments but 1 was given

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_passing_a_dictionary`

.. code-block:: python
  :lineno-start: 70
  :emphasize-lines: 3-4

          self.assertEqual(reality, my_expectation)

      # def test_passing_a_dictionary():
      def test_passing_a_dictionary(self):

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_a_dictionary`

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 13

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_dictionary():
        def test_passing_a_dictionary(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }

            reality = src.telephone.text(a_dictionary)
            my_expectation = f'I got: {a_dictionary}'
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    def test_passing_a_class():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        "I got: {'key0': 'value0', 'keyN': [0, 1, 2, 'n']}"
     == "I got: {'key0': 'value0', 'keyN': [0, 1, 2, 'n']}"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_a_dictionary`

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 13-14

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_dictionary():
        def test_passing_a_dictionary(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }

            reality = src.telephone.text(a_dictionary)
            my_expectation = f'I got: {a_dictionary}'
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_passing_a_class():

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 70

            self.assertEqual(reality, my_expectation)

        def test_passing_a_dictionary(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }

            reality = src.telephone.text(a_dictionary)
            my_expectation = f'I got: {a_dictionary}'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_passing_a_class():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_passing_a_dictionary to TestTelephone'

----

*********************************************************************************
test_passing_a_class with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_passing_a_class` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 3-6, 8-10, 12-14, 16-18, 20-22, 24-26, 28-30, 32-34, 36-38

            self.assertEqual(reality, my_expectation)

        def test_passing_a_class():
            reality = src.telephone.text(object)
            my_expectation = "I got: <class 'object'>"
            assert reality == my_expectation

            reality = src.telephone.text(bool)
            my_expectation = "I got: <class 'bool'>"
            assert reality == my_expectation

            reality = src.telephone.text(int)
            my_expectation = "I got: <class 'int'>"
            assert reality == my_expectation

            reality = src.telephone.text(float)
            my_expectation = "I got: <class 'float'>"
            assert reality == my_expectation

            reality = src.telephone.text(str)
            my_expectation = "I got: <class 'str'>"
            assert reality == my_expectation

            reality = src.telephone.text(tuple)
            my_expectation = "I got: <class 'tuple'>"
            assert reality == my_expectation

            reality = src.telephone.text(list)
            my_expectation = "I got: <class 'list'>"
            assert reality == my_expectation

            reality = src.telephone.text(set)
            my_expectation = "I got: <class 'set'>"
            assert reality == my_expectation

            reality = src.telephone.text(dict)
            my_expectation = "I got: <class 'dict'>"
            assert reality == my_expectation


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestTelephone.test_passing_a_class()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_passing_a_class`

.. code-block:: python
  :lineno-start: 81
  :emphasize-lines: 3-4

          self.assertEqual(reality, my_expectation)

      # def test_passing_a_class():
      def test_passing_a_class(self):

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the :ref:`assertions<what is an assertion?>` in :ref:`test_passing_a_class`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 8, 13, 18, 23, 28, 33, 38, 43, 48

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_class():
        def test_passing_a_class(self):
            reality = src.telephone.text(object)
            my_expectation = "I got: <class 'object'>"
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)

            reality = src.telephone.text(bool)
            my_expectation = "I got: <class 'bool'>"
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)

            reality = src.telephone.text(int)
            my_expectation = "I got: <class 'int'>"
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)

            reality = src.telephone.text(float)
            my_expectation = "I got: <class 'float'>"
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)

            reality = src.telephone.text(str)
            my_expectation = "I got: <class 'str'>"
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)

            reality = src.telephone.text(tuple)
            my_expectation = "I got: <class 'tuple'>"
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)

            reality = src.telephone.text(list)
            my_expectation = "I got: <class 'list'>"
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)

            reality = src.telephone.text(set)
            my_expectation = "I got: <class 'set'>"
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)

            reality = src.telephone.text(dict)
            my_expectation = "I got: <class 'dict'>"
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

     AssertionError: "I got: <class 'object'>"
                  == "I got: <class 'object'>"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`assertion<what is an assertion?>` for :ref:`object<everything is an object>`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 8-9

            self.assertEqual(reality, my_expectation)

        # def test_passing_a_class():
        def test_passing_a_class(self):
            reality = src.telephone.text(object)
            my_expectation = "I got: <class 'object'>"
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(bool)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: <class 'bool'>"
                 == "I got: <class 'bool'>"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`assertion<what is an assertion?>` for :ref:`bool<what are booleans?>`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 4-5

            reality = src.telephone.text(bool)
            my_expectation = "I got: <class 'bool'>"
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(int)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: <class 'int'>"
                 == "I got: <class 'int'>"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`assertion<what is an assertion?>` for int_

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 4-5

            reality = src.telephone.text(int)
            my_expectation = "I got: <class 'int'>"
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(float)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: <class 'float'>"
                 == "I got: <class 'float'>"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`assertion<what is an assertion?>` for float_

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 4-5

            reality = src.telephone.text(float)
            my_expectation = "I got: <class 'float'>"
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(str)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: <class 'str'>"
                 == "I got: <class 'str'>"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`assertion<what is an assertion?>` for str_

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 4-5

            reality = src.telephone.text(str)
            my_expectation = "I got: <class 'str'>"
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(tuple)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: <class 'tuple'>"
                 == "I got: <class 'tuple'>"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`assertion<what is an assertion?>` for tuple_

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 4-5

            reality = src.telephone.text(tuple)
            my_expectation = "I got: <class 'tuple'>"
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(list)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: <class 'list'>"
                 == "I got: <class 'list'>"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`assertion<what is an assertion?>` for :ref:`list<what is a list?>`

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 4-5

            reality = src.telephone.text(list)
            my_expectation = "I got: <class 'list'>"
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(set)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: <class 'set'>"
                 == "I got: <class 'set'>"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`assertion<what is an assertion?>` for set_

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 4-5

            reality = src.telephone.text(set)
            my_expectation = "I got: <class 'set'>"
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(dict)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: <class 'dict'>"
                 == "I got: <class 'dict'>"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`assertion<what is an assertion?>` for :ref:`dict<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 4-5

            reality = src.telephone.text(dict)
            my_expectation = "I got: <class 'dict'>"
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 81

            self.assertEqual(reality, my_expectation)

        def test_passing_a_class(self):
            reality = src.telephone.text(object)
            my_expectation = "I got: <class 'object'>"
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(bool)
            my_expectation = "I got: <class 'bool'>"
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(int)
            my_expectation = "I got: <class 'int'>"
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(float)
            my_expectation = "I got: <class 'float'>"
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(str)
            my_expectation = "I got: <class 'str'>"
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(tuple)
            my_expectation = "I got: <class 'tuple'>"
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(list)
            my_expectation = "I got: <class 'list'>"
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(set)
            my_expectation = "I got: <class 'set'>"
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(dict)
            my_expectation = "I got: <class 'dict'>"
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # ModuleNotFoundError
    # AttributeError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_passing_a_class to TestTelephone'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_telephone.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``telephone``

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

:ref:`Do you want to see all the CODE I typed in this chapter?<test telephone with unittest: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

You know:

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