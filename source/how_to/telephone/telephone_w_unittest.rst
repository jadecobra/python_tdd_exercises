.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): test telephone with unittest — move the telephone project's tests onto unittest.TestCase and drop the unused assert_equal helper. Open telephone; uv run pytest-watcher . --now (10 passed). Add class Telephone then rename to TestTelephone → AttributeError: 'TestTelephone' object has no attribute 'assertEqual'. Parent unittest.TestCase → NameError name 'unittest' is not defined (pytest: Did you forget to import 'unittest'?); import unittest → AssertionError: True != False then green with assertEqual(True, True). For each of 10 tests (test_passing_none, booleans, int 1234, float 5.678, string 'hello', tuple/list/set, dict with reality/my_expectation, objects object/bool/int/…): move into TestTelephone → TypeError takes 0 positional arguments but 1 was given (need self); add assertNotEqual → AssertionError e.g. 'I got: None' == 'I got: None', "I got: (0, 1, 2, 'n')" == "I got: (0, 1, 2, 'n')", "I got: [0, 1, 2, 'n']"; switch to assertEqual; remove the commented lines; git commit. Ends with TestTelephone + 10 methods all self.assertEqual + # Exceptions seen AssertionError NameError TypeError AttributeError. Review: unittest.TestCase methods or bare assert statements. What is next: test person with datetime.
  :keywords: Jacob Itegboje, Pumping Python, test telephone with unittest, telephone unittest, TestTelephone, unittest.TestCase, import unittest, AttributeError has no attribute assertEqual, NameError name 'unittest' is not defined, Did you forget to import unittest, AssertionError True != False, TypeError takes 0 positional arguments but 1 was given, self first argument method, assertNotEqual, assertEqual, 'I got: None' == 'I got: None', I got: False, I got: True, an_integer 1234, a_float 5.678, hello, I got: (0, 1, 2, 'n'), I got: [0, 1, 2, 'n'], I got: <class 'object'>, reality == my_expectation, remove unused assert_equal, uv run pytest-watcher . --now, red green refactor, remove the commented lines, git commit -am, another way to write tests, test_telephone_w_unittest

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
  :caption: telephone/tests/test_telephone.py
  :language: python
  :linenos:
  :lines: 1-15

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_unittest.py
  :caption: telephone/tests/test_telephone.py
  :language: python
  :lineno-start: 17
  :lines: 17-27

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_unittest.py
  :caption: telephone/tests/test_telephone.py
  :language: python
  :lineno-start: 29
  :lines: 29-39

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_unittest.py
  :caption: telephone/tests/test_telephone.py
  :language: python
  :lineno-start: 41
  :lines: 41-49

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_unittest.py
  :caption: telephone/tests/test_telephone.py
  :language: python
  :lineno-start: 51
  :lines: 51-58

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_unittest.py
  :caption: telephone/tests/test_telephone.py
  :language: python
  :lineno-start: 60
  :lines: 60-

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

* I add an :ref:`object<everything is an object>` named ``Telephone`` to ``test_telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11, 13-14

    import src.telephone


    text = src.telephone.text


    def assert_equal(a, b):
        assert a == b


    class Telephone(object):

        def test_failure(self):
            self.assertEqual(True, False)


    def test_passing_none():

  the test is still green.

* I change the name of the :ref:`object<everything is an object>` to ``TestTelephone``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5-6

    def assert_equal(a, b):
        assert a == b


    # class Telephone(object):
    class TestTelephone(object):

        def test_failure(self):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'TestTelephone' object
                    has no attribute 'assertEqual'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`unittest.TestCase<test_dir_unittest_testcase>` as the parent :ref:`object<everything is an object>` of ``TestTelephone``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2-3

    # class Telephone(object):
    # class TestTelephone(object):
    class TestTelephone(unittest.TestCase):

        def test_failure(self):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell

    NameError: name 'unittest' is not defined.
               Did you forget to import 'unittest'?

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import src.telephone
    import unittest


    text = src.telephone.text

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

* I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in :ref:`test_failure`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 6-7

    # class Telephone(object):
    # class TestTelephone(object):
    class TestTelephone(unittest.TestCase):

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

    def assert_equal(a, b):
        assert a == b


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

* I go back to the terminal_ where the tests are running

* I remove :ref:`test_failure`
* I move :ref:`test_passing_none` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3-4

    class TestTelephone(unittest.TestCase):

        def test_passing_none():
            assert_equal(text(None), 'I got: None')


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
  :lineno-start: 12
  :emphasize-lines: 3-4

  class TestTelephone(unittest.TestCase):

      # def test_passing_none():
      def test_passing_none(self):
          assert_equal(text(None), 'I got: None')

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_none`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 3-4

        # def test_passing_none():
        def test_passing_none(self):
            # assert_equal(text(None), 'I got: None')
            self.assertNotEqual(text(None), 'I got: None')


    def test_passing_booleans():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I got: None' == 'I got: None'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_none`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4-5

        # def test_passing_none():
        def test_passing_none(self):
            # assert_equal(text(None), 'I got: None')
            # self.assertNotEqual(text(None), 'I got: None')
            self.assertEqual(text(None), 'I got: None')


    def test_passing_booleans():

  the test passes.

* I remove the commented lines from :ref:`test_passing_none`

  .. code-block:: python
    :lineno-start: 12

    class TestTelephone(unittest.TestCase):

        def test_passing_none(self):
            self.assertEqual(text(None), 'I got: None')


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

* I go back to the terminal_ where the tests are running

* I move :ref:`test_passing_booleans` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4-6

        def test_passing_none(self):
            self.assertEqual(text(None), 'I got: None')

        def test_passing_booleans():
            assert_equal(text(False), 'I got: False')
            assert_equal(text(True), 'I got: True')


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
  :lineno-start: 14
  :emphasize-lines: 4-5

      def test_passing_none(self):
          self.assertEqual(text(None), 'I got: None')

      # def test_passing_booleans():
      def test_passing_booleans(self):
          assert_equal(text(False), 'I got: False')
          assert_equal(text(True), 'I got: True')

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`calls<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` for the :ref:`assertions<what is an assertion?>` in :ref:`test_passing_booleans`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3-6

        # def test_passing_booleans():
        def test_passing_booleans(self):
            # assert_equal(text(False), 'I got: False')
            self.assertNotEqual(text(False), 'I got: False')
            # assert_equal(text(True), 'I got: True')
            self.assertNotEqual(text(True), 'I got: True')


    def test_passing_an_integer():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I got: False' == 'I got: False'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the first :ref:`assertion<what is an assertion?>` in :ref:`test_passing_booleans`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 4-5

        # def test_passing_booleans():
        def test_passing_booleans(self):
            # assert_equal(text(False), 'I got: False')
            # self.assertNotEqual(text(False), 'I got: False')
            self.assertEqual(text(False), 'I got: False')
            # assert_equal(text(True), 'I got: True')
            self.assertNotEqual(text(True), 'I got: True')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I got: True' == 'I got: True'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the second :ref:`assertion<what is an assertion?>` in :ref:`test_passing_booleans`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 7-8

        # def test_passing_booleans():
        def test_passing_booleans(self):
            # assert_equal(text(False), 'I got: False')
            # self.assertNotEqual(text(False), 'I got: False')
            self.assertEqual(text(False), 'I got: False')
            # assert_equal(text(True), 'I got: True')
            # self.assertNotEqual(text(True), 'I got: True')
            self.assertEqual(text(True), 'I got: True')


    def test_passing_an_integer():

  the test passes.

* I remove the commented lines from :ref:`test_passing_booleans`

  .. code-block:: python
    :lineno-start: 14

        def test_passing_none(self):
            self.assertEqual(text(None), 'I got: None')

        def test_passing_booleans(self):
            self.assertEqual(text(False), 'I got: False')
            self.assertEqual(text(True), 'I got: True')


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

* I go back to the terminal_ where the tests are running

* I move :ref:`test_passing_an_integer` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5-7

        def test_passing_booleans(self):
            self.assertEqual(text(False), 'I got: False')
            self.assertEqual(text(True), 'I got: True')

        def test_passing_an_integer():
            an_integer = 1234
            assert_equal(text(an_integer), f'I got: {an_integer}')


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
  :lineno-start: 17
  :emphasize-lines: 5-6

        def test_passing_booleans(self):
            self.assertEqual(text(False), 'I got: False')
            self.assertEqual(text(True), 'I got: True')

        # def test_passing_an_integer():
        def test_passing_an_integer(self):
            an_integer = 1234
            assert_equal(text(an_integer), f'I got: {an_integer}')

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_an_integer`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 4-7

        # def test_passing_an_integer():
        def test_passing_an_integer(self):
            an_integer = 1234
            # assert_equal(text(an_integer), f'I got: {an_integer}')
            self.assertNotEqual(
                text(an_integer), f'I got: {an_integer}'
            )


    def test_passing_a_float():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I got: 1234' == 'I got: 1234'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_an_integer`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-6

        # def test_passing_an_integer():
        def test_passing_an_integer(self):
            an_integer = 1234
            # assert_equal(text(an_integer), f'I got: {an_integer}')
            # self.assertNotEqual(
            self.assertEqual(
                text(an_integer), f'I got: {an_integer}'
            )

  the test passes.

* I remove the commented lines from :ref:`test_passing_an_integer`

  .. code-block:: python
    :lineno-start: 17

        def test_passing_booleans(self):
            self.assertEqual(text(False), 'I got: False')
            self.assertEqual(text(True), 'I got: True')

        def test_passing_an_integer(self):
            an_integer = 1234
            self.assertEqual(
                text(an_integer), f'I got: {an_integer}'
            )


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

* I go back to the terminal_ where the tests are running

* I move :ref:`test_passing_a_float` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 7-9

        def test_passing_an_integer(self):
            an_integer = 1234
            self.assertEqual(
                text(an_integer), f'I got: {an_integer}'
            )

        def test_passing_a_float():
            a_float = 5.678
            assert_equal(text(a_float), f'I got: {a_float}')


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
  :lineno-start: 21
  :emphasize-lines: 7-8

      def test_passing_an_integer(self):
          an_integer = 1234
          self.assertEqual(
              text(an_integer), f'I got: {an_integer}'
          )

      # def test_passing_a_float():
      def test_passing_a_float(self):
          a_float = 5.678
          assert_equal(text(a_float), f'I got: {a_float}')

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_a_float`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4-7

        # def test_passing_a_float():
        def test_passing_a_float(self):
            a_float = 5.678
            # assert_equal(text(a_float), f'I got: {a_float}')
            self.assertNotEqual(
                text(a_float), f'I got: {a_float}'
            )


    def test_passing_a_string():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I got: 5.678' == 'I got: 5.678'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_a_float`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 5-6

        # def test_passing_a_float():
        def test_passing_a_float(self):
            a_float = 5.678
            # assert_equal(text(a_float), f'I got: {a_float}')
            # self.assertNotEqual(
            self.assertEqual(
                text(a_float), f'I got: {a_float}'
            )

  the test passes.

* I remove the commented lines from :ref:`test_passing_a_float`

  .. code-block:: python
    :lineno-start: 21

        def test_passing_an_integer(self):
            an_integer = 1234
            self.assertEqual(
                text(an_integer), f'I got: {an_integer}'
            )

        def test_passing_a_float(self):
            a_float = 5.678
            self.assertEqual(
                text(a_float), f'I got: {a_float}'
            )


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

* I go back to the terminal_ where the tests are running

* I move :ref:`test_passing_a_string` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 7-9

        def test_passing_a_float(self):
            a_float = 5.678
            self.assertEqual(
                text(a_float), f'I got: {a_float}'
            )

        def test_passing_a_string():
            a_string = 'hello'
            assert_equal(text('hello'), f'I got: {a_string}')


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
  :lineno-start: 27
  :emphasize-lines: 7-8

      def test_passing_a_float(self):
          a_float = 5.678
          self.assertEqual(
              text(a_float), f'I got: {a_float}'
          )

      # def test_passing_a_string():
      def test_passing_a_string(self):
          a_string = 'hello'
          assert_equal(text('hello'), f'I got: {a_string}')

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_a_string`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 4-7

        # def test_passing_a_string():
        def test_passing_a_string(self):
            a_string = 'hello'
            # assert_equal(text('hello'), f'I got: {a_string}')
            self.assertNotEqual(
                text('hello'), f'I got: {a_string}'
            )


    def test_passing_a_tuple():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I got: hello' == 'I got: hello'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_a_string`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5-6

        # def test_passing_a_string():
        def test_passing_a_string(self):
            a_string = 'hello'
            # assert_equal(text('hello'), f'I got: {a_string}')
            # self.assertNotEqual(
            self.assertEqual(
                text('hello'), f'I got: {a_string}'
            )

  the test passes.

* I remove the commented lines from :ref:`test_passing_a_string`

  .. code-block:: python
    :lineno-start: 27

        def test_passing_a_float(self):
            a_float = 5.678
            self.assertEqual(
                text(a_float), f'I got: {a_float}'
            )

        def test_passing_a_string(self):
            a_string = 'hello'
            self.assertEqual(
                text('hello'), f'I got: {a_string}'
            )


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

* I go back to the terminal_ where the tests are running

* I move :ref:`test_passing_a_tuple` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 7-9

        def test_passing_a_string(self):
            a_string = 'hello'
            self.assertEqual(
                text('hello'), f'I got: {a_string}'
            )

        def test_passing_a_tuple():
            a_tuple = (0, 1, 2, 'n')
            assert_equal(text(a_tuple), f"I got: {a_tuple}")


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
  :lineno-start: 33
  :emphasize-lines: 7-8

      def test_passing_a_string(self):
          a_string = 'hello'
          self.assertEqual(
              text('hello'), f'I got: {a_string}'
          )

      # def test_passing_a_tuple():
      def test_passing_a_tuple(self):
          a_tuple = (0, 1, 2, 'n')
          assert_equal(text(a_tuple), f"I got: {a_tuple}")

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_a_tuple`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 4-7

        # def test_passing_a_tuple():
        def test_passing_a_tuple(self):
            a_tuple = (0, 1, 2, 'n')
            # assert_equal(text(a_tuple), f"I got: {a_tuple}")
            self.assertNotEqual(
                text(a_tuple), f"I got: {a_tuple}"
            )


    def test_passing_a_list():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: (0, 1, 2, 'n')"
                 == "I got: (0, 1, 2, 'n')"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_a_tuple`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 5-6

        # def test_passing_a_tuple():
        def test_passing_a_tuple(self):
            a_tuple = (0, 1, 2, 'n')
            # assert_equal(text(a_tuple), f"I got: {a_tuple}")
            # self.assertNotEqual(
            self.assertEqual(
                text(a_tuple), f"I got: {a_tuple}"
            )

  the test passes.

* I remove the commented lines from :ref:`test_passing_a_tuple`

  .. code-block:: python
    :lineno-start: 33

        def test_passing_a_string(self):
            a_string = 'hello'
            self.assertEqual(
                text('hello'), f'I got: {a_string}'
            )

        def test_passing_a_tuple(self):
            a_tuple = (0, 1, 2, 'n')
            self.assertEqual(
                text(a_tuple), f"I got: {a_tuple}"
            )


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

* I go back to the terminal_ where the tests are running

* I move :ref:`test_passing_a_list` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 7-9

        def test_passing_a_tuple(self):
            a_tuple = (0, 1, 2, 'n')
            self.assertEqual(
                text(a_tuple), f"I got: {a_tuple}"
            )

        def test_passing_a_list():
            a_list = [0, 1, 2, 'n']
            assert_equal(text(a_list), f'I got: {a_list}')


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
  :lineno-start: 39
  :emphasize-lines: 7-8

      def test_passing_a_tuple(self):
          a_tuple = (0, 1, 2, 'n')
          self.assertEqual(
              text(a_tuple), f"I got: {a_tuple}"
          )

      # def test_passing_a_list():
      def test_passing_a_list(self):
          a_list = [0, 1, 2, 'n']
          assert_equal(text(a_list), f'I got: {a_list}')


  def test_passing_a_set():

green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_a_list`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4-7

        # def test_passing_a_list():
        def test_passing_a_list(self):
            a_list = [0, 1, 2, 'n']
            # assert_equal(text(a_list), f'I got: {a_list}')
            self.assertNotEqual(
                text(a_list), f'I got: {a_list}'
            )


    def test_passing_a_set():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: [0, 1, 2, 'n']"
                 == "I got: [0, 1, 2, 'n']"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_a_list`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 5-6

        # def test_passing_a_list():
        def test_passing_a_list(self):
            a_list = [0, 1, 2, 'n']
            # assert_equal(text(a_list), f'I got: {a_list}')
            # self.assertNotEqual(
            self.assertEqual(
                text(a_list), f'I got: {a_list}'
            )

  the test passes.

* I remove the commented lines from :ref:`test_passing_a_list`

  .. code-block:: python
    :lineno-start: 39

        def test_passing_a_tuple(self):
            a_tuple = (0, 1, 2, 'n')
            self.assertEqual(
                text(a_tuple), f"I got: {a_tuple}"
            )

        def test_passing_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertEqual(
                text(a_list), f'I got: {a_list}'
            )


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

* I go back to the terminal_ where the tests are running

* I move :ref:`test_passing_a_set` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 7-9

        def test_passing_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertEqual(
                text(a_list), f'I got: {a_list}'
            )

        def test_passing_a_set():
            a_set = {0, 1, 2, 'n'}
            assert_equal(text(a_set), f'I got: {a_set}')


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
  :lineno-start: 45
  :emphasize-lines: 7-8

      def test_passing_a_list(self):
          a_list = [0, 1, 2, 'n']
          self.assertEqual(
              text(a_list), f'I got: {a_list}'
          )

      # def test_passing_a_set():
      def test_passing_a_set(self):
          a_set = {0, 1, 2, 'n'}
          assert_equal(text(a_set), f'I got: {a_set}')

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_a_set`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 4-5

        # def test_passing_a_set():
        def test_passing_a_set(self):
            a_set = {0, 1, 2, 'n'}
            # assert_equal(text(a_set), f'I got: {a_set}')
            self.assertNotEqual(text(a_set), f'I got: {a_set}')


    def test_passing_a_dictionary():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: "I got: {0, 1, 2, 'n'}"
                 == "I got: {0, 1, 2, 'n'}"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_a_set`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 5-6

        # def test_passing_a_set():
        def test_passing_a_set(self):
            a_set = {0, 1, 2, 'n'}
            # assert_equal(text(a_set), f'I got: {a_set}')
            # self.assertNotEqual(text(a_set), f'I got: {a_set}')
            self.assertEqual(text(a_set), f'I got: {a_set}')


    def test_passing_a_dictionary():

  the test passes.

* I remove the commented lines from :ref:`test_passing_a_set`

  .. code-block:: python
    :lineno-start: 45

        def test_passing_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertEqual(
                text(a_list), f'I got: {a_list}'
            )

        def test_passing_a_set(self):
            a_set = {0, 1, 2, 'n'}
            self.assertEqual(text(a_set), f'I got: {a_set}')


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

* I go back to the terminal_ where the tests are running

* I move :ref:`test_passing_a_dictionary` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 5-12

        def test_passing_a_set(self):
            a_set = {0, 1, 2, 'n'}
            self.assertEqual(text(a_set), f'I got: {a_set}')

        def test_passing_a_dictionary():
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            reality = text(a_dictionary)
            my_expectation = f'I got: {a_dictionary}'
            assert_equal(reality, my_expectation)


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
  :lineno-start: 51
  :emphasize-lines: 5-6

      def test_passing_a_set(self):
          a_set = {0, 1, 2, 'n'}
          self.assertEqual(text(a_set), f'I got: {a_set}')

      # def test_passing_a_dictionary():
      def test_passing_a_dictionary(self):
          a_dictionary = {
              'key0': 'value0',
              'keyN': [0, 1, 2, 'n'],
          }

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_a_dictionary`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 9-10

        # def test_passing_a_dictionary():
        def test_passing_a_dictionary(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            reality = text(a_dictionary)
            my_expectation = f'I got: {a_dictionary}'
            # assert_equal(reality, my_expectation)
            self.assertNotEqual(reality, my_expectation)


    def test_passing_a_class():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        "I got: {'key0': 'value0', 'keyN': [0, 1, 2, 'n']}"
     == "I got: {'key0': 'value0', 'keyN': [0, 1, 2, 'n']}"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_a_dictionary`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 10-11

        # def test_passing_a_dictionary():
        def test_passing_a_dictionary(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            reality = text(a_dictionary)
            my_expectation = f'I got: {a_dictionary}'
            # assert_equal(reality, my_expectation)
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_passing_a_class():

  the test passes.

* I remove the commented lines from :ref:`test_passing_a_dictionary`

  .. code-block:: python
    :lineno-start: 51

        def test_passing_a_set(self):
            a_set = {0, 1, 2, 'n'}
            self.assertEqual(text(a_set), f'I got: {a_set}')

        def test_passing_a_dictionary(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            reality = text(a_dictionary)
            my_expectation = f'I got: {a_dictionary}'
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

* I go back to the terminal_ where the tests are running

* I move :ref:`test_passing_a_class` to make it a :ref:`method<what is a method?>` of the :ref:`TestTelephone class<add TestTelephone class>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3-14

            self.assertEqual(reality, my_expectation)

        def test_passing_a_class():
            assert_equal(
                text(object), "I got: <class 'object'>"
            )
            assert_equal(text(bool), "I got: <class 'bool'>")
            assert_equal(text(int), "I got: <class 'int'>")
            assert_equal(text(float), "I got: <class 'float'>")
            assert_equal(text(str), "I got: <class 'str'>")
            assert_equal(text(tuple), "I got: <class 'tuple'>")
            assert_equal(text(list), "I got: <class 'list'>")
            assert_equal(text(set), "I got: <class 'set'>")
            assert_equal(text(dict), "I got: <class 'dict'>")


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
  :lineno-start: 62
  :emphasize-lines: 3-4

          self.assertEqual(reality, my_expectation)

      # def test_passing_a_class():
      def test_passing_a_class(self):
          assert_equal(
              text(object), "I got: <class 'object'>"
          )

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`calls<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` for the :ref:`assertions<what is an assertion?>` in :ref:`test_passing_a_class`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 3-10

        # def test_passing_a_class():
        def test_passing_a_class(self):
            # assert_equal(
            self.assertNotEqual(
                text(object), "I got: <class 'object'>"
            )
            # assert_equal(text(bool), "I got: <class 'bool'>")
            self.assertNotEqual(
                text(bool), "I got: <class 'bool'>"
            )

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 1-12

            # assert_equal(text(int), "I got: <class 'int'>")
            self.assertNotEqual(text(int), "I got: <class 'int'>")
            # assert_equal(text(float), "I got: <class 'float'>")
            self.assertNotEqual(
                text(float), "I got: <class 'float'>"
            )
            # assert_equal(text(str), "I got: <class 'str'>")
            self.assertNotEqual(text(str), "I got: <class 'str'>")
            # assert_equal(text(tuple), "I got: <class 'tuple'>")
            self.assertNotEqual(
                text(tuple), "I got: <class 'tuple'>"
            )

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 1-10

            # assert_equal(text(list), "I got: <class 'list'>")
            self.assertNotEqual(
                text(list), "I got: <class 'list'>"
            )
            # assert_equal(text(set), "I got: <class 'set'>")
            self.assertNotEqual(text(set), "I got: <class 'set'>")
            # assert_equal(text(dict), "I got: <class 'dict'>")
            self.assertNotEqual(
                text(dict), "I got: <class 'dict'>"
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

     AssertionError: "I got: <class 'object'>"
                  == "I got: <class 'object'>"

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` in :ref:`test_passing_a_class`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 4-5, 9-10

        # def test_passing_a_class():
        def test_passing_a_class(self):
            # assert_equal(
            # self.assertNotEqual(
            self.assertEqual(
                text(object), "I got: <class 'object'>"
            )
            # assert_equal(text(bool), "I got: <class 'bool'>")
            # self.assertNotEqual(
            self.assertEqual(
                text(bool), "I got: <class 'bool'>"
            )

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 2-3, 5-6

            # assert_equal(text(int), "I got: <class 'int'>")
            # self.assertNotEqual(text(int), "I got: <class 'int'>")
            self.assertEqual(text(int), "I got: <class 'int'>")
            # assert_equal(text(float), "I got: <class 'float'>")
            # self.assertNotEqual(
            self.assertEqual(
                text(float), "I got: <class 'float'>"
            )

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2-3, 5-6

            # assert_equal(text(str), "I got: <class 'str'>")
            # self.assertNotEqual(text(str), "I got: <class 'str'>")
            self.assertEqual(text(str), "I got: <class 'str'>")
            # assert_equal(text(tuple), "I got: <class 'tuple'>")
            # self.assertNotEqual(
            self.assertEqual(
                text(tuple), "I got: <class 'tuple'>"
            )

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 2-3, 7-8, 10-11

            # assert_equal(text(list), "I got: <class 'list'>")
            # self.assertNotEqual(
            self.assertEqual(
                text(list), "I got: <class 'list'>"
            )
            # assert_equal(text(set), "I got: <class 'set'>")
            # self.assertNotEqual(text(set), "I got: <class 'set'>")
            self.assertEqual(text(set), "I got: <class 'set'>")
            # assert_equal(text(dict), "I got: <class 'dict'>")
            # self.assertNotEqual(
            self.assertEqual(
                text(dict), "I got: <class 'dict'>"
            )


    # Exceptions seen

  the test passes.

* I remove the commented lines from :ref:`test_passing_a_class`

  .. code-block:: python
    :lineno-start: 62

            self.assertEqual(reality, my_expectation)

        def test_passing_a_class(self):
            self.assertEqual(
                text(object), "I got: <class 'object'>"
            )
            self.assertEqual(
                text(bool), "I got: <class 'bool'>"
            )
            self.assertEqual(text(int), "I got: <class 'int'>")
            self.assertEqual(
                text(float), "I got: <class 'float'>"
            )
            self.assertEqual(text(str), "I got: <class 'str'>")

  .. code-block:: python
    :lineno-start: 76

            self.assertEqual(
                text(tuple), "I got: <class 'tuple'>"
            )
            self.assertEqual(
                text(list), "I got: <class 'list'>"
            )
            self.assertEqual(text(set), "I got: <class 'set'>")
            self.assertEqual(
                text(dict), "I got: <class 'dict'>"
            )


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError

* I remove my :ref:`assert_equal function<extract assert_equal function>` since it is no longer used

  .. code-block:: python
    :linenos:

    import src.telephone
    import unittest


    text = src.telephone.text


    class TestTelephone(unittest.TestCase):

  all tests are still green.

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
* :ref:`I know how to make a person with an object<how to make a person with an object>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.

:ref:`Would you like to make sure the person project always calculates the correct age?<test person with datetime>`

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