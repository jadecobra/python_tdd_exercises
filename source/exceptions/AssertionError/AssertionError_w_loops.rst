.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

#################################################################################
test AssertionError with loops
#################################################################################

----

I want to use :ref:`for loops<what is a for loop?>` in the :ref:`assertion_error<what is an assertion?>` project.

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

----

*********************************************************************************
test_assert_keyword with for loop
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a tuple_ with a :ref:`for loop<what is a for loop?>` for the items in :ref:`test_assert_keyword`

.. code-block:: python
  :lineno-start: 38
  :emphasize-lines: 2-9

      def test_assert_keyword(self):
          for reality, my_expectation in (
              (1 + 1, 2),
              ('1' + '1', '11'),
              ('I am' + ' alive', 'I am alive')
          ):
              with self.subTest((reality, my_expectation)):
                  assert_equal(reality, 'BOOM!!!')
                  self.assertEqual(reality, 'BAP!!!')

          reality = 1 + 1

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  SUBFAILED[(2, 2)] ...test_assert_keyword -
      AssertionError: assert 2 == 'BOOM!!!'
  SUBFAILED[('11', '11')] ...test_assert_keyword -
      AssertionError: assert '11' == 'BOOM!!!'
  SUBFAILED[('I am alive', 'I am alive')] ...test_assert_keyword -
      AssertionError: assert 'I am alive' == 'BOOM!!!'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the expectation of ``assert_equal(reality, 'BOOM!!!')``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2

                with self.subTest((reality, my_expectation)):
                    assert_equal(reality, my_expectation)
                    self.assertEqual(reality, 'BAP!!!')

            reality = 1 + 1

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED[(2, 2)] ...test_assert_keyword -
        AssertionError: 2 != 'BAP!!!'
    SUBFAILED[('11', '11')] ...test_assert_keyword -
        AssertionError: '11' != 'BAP!!!'
    SUBFAILED[('I am alive', 'I am alive')] ...test_assert_keyword -
        AssertionError: 'I am alive' != 'BAP!!!'

* I change the expectation of ``self.assertEqual(reality, 'BAP!!!')``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 3

                with self.subTest((reality, my_expectation)):
                    assert_equal(reality, my_expectation)
                    self.assertEqual(reality, my_expectation)

            reality = 1 + 1

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other statements from :ref:`test_assert_keyword` because they are now covered by the :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 38

        def test_assert_keyword(self):
            for reality, my_expectation in (
                (1 + 1, 2),
                ('1' + '1', '11'),
                ('I am' + ' alive', 'I am alive')
            ):
                with self.subTest((reality, my_expectation)):
                    assert_equal(reality, my_expectation)
                    self.assertEqual(reality, my_expectation)

        def test_assertion_error_w_none(self):

* I open a new terminal_ then make sure I am in the ``assertion_error`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'test_assert_keyword with a for loop'

----

*********************************************************************************
test_assertion_error_w_none with for loop
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`for loop<what is a for loop?>` to :ref:`test_assertion_error_w_none`

.. code-block:: python
  :lineno-start: 48
  :emphasize-lines: 6-15

      def test_assertion_error_w_none(self):
          assert None is None
          self.assertIs(None, None)
          self.assertIsNone(None)

          for an_object in (
              False, True, self.an_integer,
              self.a_float, self.a_string,
              self.a_tuple, self.a_list,
              self.a_set, self.a_dictionary,
          ):
              with self.subTest(object=an_object):
                  assert_is_not_none(None)
                  self.assertIsNot(an_object, object)
                  self.assertIsNotNone(None)

          assert_is_not_none(False)

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

    AssertionError: assert None is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`None<what is None?>` to ``an_object`` in ``assert_is_not_none(None)``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 2

                with self.subTest(object=an_object):
                    assert_is_not_none(an_object)
                    self.assertIsNot(an_object, an_object)
                    self.assertIsNotNone(None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(object=False) ::test_assertion_error_w_none -
        AssertionError: unexpectedly identical: False
    SUBFAILED(object=True) ::test_assertion_error_w_none -
         AssertionError: unexpectedly identical: True
    SUBFAILED(object=0) ::test_assertion_error_w_none -
        AssertionError: unexpectedly identical: 0
    SUBFAILED(object=0.0) ::test_assertion_error_w_none -
        AssertionError: unexpectedly identical: 0.0
    SUBFAILED(object='') ::test_assertion_error_w_none -
        AssertionError: unexpectedly identical: ''
    SUBFAILED(object=()) ::test_assertion_error_w_none -
        AssertionError: unexpectedly identical: ()
    SUBFAILED(object=[]) ::test_assertion_error_w_none -
        AssertionError: unexpectedly identical: []
    SUBFAILED(object=set()) ::test_assertion_error_w_none -
        AssertionError: unexpectedly identical: set()
    SUBFAILED(object={}) ::test_assertion_error_w_none -
        AssertionError: unexpectedly identical: {}

* I change the second ``an_object`` to :ref:`None<what is None?>` in ``self.assertIsNot(an_object, an_object)``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 3

                with self.subTest(object=an_object):
                    assert_is_not_none(an_object)
                    self.assertIsNot(an_object, None)
                    self.assertIsNotNone(None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly None

* I change :ref:`None<what is None?>` to ``an_object``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 4

                with self.subTest(object=an_object):
                    assert_is_not_none(an_object)
                    self.assertIsNot(an_object, None)
                    self.assertIsNotNone(an_object)

            assert_is_not_none(False)

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other statements from :ref:`test_assertion_error_w_none` because they are now covered by the :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 48

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)
            self.assertIsNone(None)

            for an_object in (
                False, True, self.an_integer,
                self.a_float, self.a_string,
                self.a_tuple, self.a_list,
                self.a_set, self.a_dictionary,
            ):
                with self.subTest(object=an_object):
                    assert_is_not_none(an_object)
                    self.assertIsNot(an_object, None)
                    self.assertIsNotNone(an_object)

        def test_assertion_error_w_false(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'test_assertion_error_w_none with a for loop'

----

*********************************************************************************
test_assertion_error_w_false with a for loop
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`for loop<what is a for loop?>` to :ref:`test_assertion_error_w_false`

.. code-block:: python
  :lineno-start: 64
  :emphasize-lines: 5-13

        def test_assertion_error_w_false(self):
            assert False is False
            self.assertIs(False, False)

            for an_object in (
                None, True, self.an_integer,
                self.a_float, self.a_string,
                self.a_tuple, self.a_list,
                self.a_set, self.a_dictionary,
            ):
                with self.subTest(object=an_object):
                    assert_is_not_false(False)
                    self.assertIsNot(an_object, True)

            assert_is_not_false(None)

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: assert False is not False

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`False<test_what_is_false>` to ``an_object`` in ``assert_is_not_false(False)``

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 2

                with self.subTest(object=an_object):
                    assert_is_not_false(an_object)
                    self.assertIsNot(an_object, True)

            assert_is_not_false(None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(object=True) test_assertion_error_w_false -
        AssertionError: unexpectedly identical: True

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in ``self.assertIsNot(an_object, True)``

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 3

            with self.subTest(object=an_object):
                assert_is_not_false(an_object)
                self.assertIsNot(an_object, False)

        assert_is_not_false(None)

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other statements from :ref:`test_assertion_error_w_false` because they are now covered by the :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 64

        def test_assertion_error_w_false(self):
            assert False is False
            self.assertIs(False, False)

            for an_object in (
                None, True, self.an_integer,
                self.a_float, self.a_string,
                self.a_tuple, self.a_list,
                self.a_set, self.a_dictionary,
            ):
                with self.subTest(object=an_object):
                    assert_is_not_false(an_object)
                    self.assertIsNot(an_object, False)

        def test_assertion_error_w_true(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'test_assertion_error_w_false with a for loop'

----

*********************************************************************************
test_assertion_error_w_true with a for loop
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`for loop<what is a for loop?>` to :ref:`test_assertion_error_w_true`

.. code-block:: python
  :lineno-start: 78
  :emphasize-lines: 5-13

      def test_assertion_error_w_true(self):
          assert True is True
          self.assertIs(True, True)

          for an_object in (
              None, False, self.an_integer,
              self.a_float, self.a_string,
              self.a_tuple, self.a_list,
              self.a_set, self.a_dictionary,
          ):
              with self.subTest(object=an_object):
                  assert_is_not_true(True)
                  self.assertIsNot(an_object, False)

          assert_is_not_true(None)

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert True is not True

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`True<test_what_is_true>` to ``an_object`` in ``assert_is_not_true(True)``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 2

                with self.subTest(object=an_object):
                    assert_is_not_true(an_object)
                    self.assertIsNot(an_object, False)

            assert_is_not_true(None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(object=False) ...test_assertion_error_w_true -
        AssertionError: unexpectedly identical: False

* I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in ``self.assertIsNot(an_object, False)``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 3

            with self.subTest(object=an_object):
                assert_is_not_true(an_object)
                self.assertIsNot(an_object, True)

        assert_is_not_true(None)

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other statements from :ref:`test_assertion_error_w_false` because they are now covered by the :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 78

        def test_assertion_error_w_true(self):
            assert True is True
            self.assertIs(True, True)

            for an_object in (
                None, False, self.an_integer,
                self.a_float, self.a_string,
                self.a_tuple, self.a_list,
                self.a_set, self.a_dictionary,
            ):
                with self.subTest(object=an_object):
                    assert_is_not_true(an_object)
                    self.assertIsNot(an_object, True)

        def test_assertion_error_w_equality(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'test_assertion_error_w_true w a for loop'

----

*********************************************************************************
extract basic_objects object attribute
*********************************************************************************

:ref:`test_assertion_error_w_true`, :ref:`test_assertion_error_w_false` and :ref:`test_assertion_error_w_none` all use a tuple_ with ``self.an_integer``, ``self.a_float``, ``self.a_string``, ``self.a_tuple``, ``self.a_list``, ``self.a_set`` and ``self.a_dictionary``. I can use an :ref:`object attribute<what is an object attribute?>` with a :ref:`single starred expression<single starred expressions>` to remove the repetition

* I add an :ref:`object attribute<what is an object attribute?>` to the :ref:`TestAssertionError object<add TestPerson object>`


----

*********************************************************************************
test_assertion_error_w_equality with a for loop
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----



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

* I add :ref:`calls<how to call a function with input>` to :ref:`assertNotEqual<test_assertNotEqual>` and :ref:`assertEqual<test_assertEqual>` to :ref:`test_assertion_error_w_equality`

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

* I change :ref:`assertNotEqual<test_assertNotEqual>` to :ref:`assertEqual<test_assertEqual>` for ``(None, None)``

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

* I change :ref:`assertNotEqual<test_assertNotEqual>` to :ref:`assertEqual<test_assertEqual>` for ``(False, False)``

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

* I change :ref:`assertNotEqual<test_assertNotEqual>` to :ref:`assertEqual<test_assertEqual>` for ``(True, True)``

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

* I change :ref:`assertEqual<test_assertEqual>` to :ref:`assertNotEqual<test_assertNotEqual>` for ``(False, None)``

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

* I change :ref:`assertEqual<test_assertEqual>` to :ref:`assertNotEqual<test_assertNotEqual>` for ``(False, True)``

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

* I change :ref:`assertEqual<test_assertEqual>` to :ref:`assertNotEqual<test_assertNotEqual>` for ``(True, None)``

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

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_assertion_error_w_equality to TestAssertionError'

----

*********************************************************************************
test_assertion_error_w_is_vs_equal with a for loop
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----



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

* I add a :ref:`call<how to call a function with input>` to :ref:`assertIs<test_assertIs>` for ``assert 0 is not 0.0``

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

* I change :ref:`assertIs<test_assertIs>` to :ref:`assertIsNot<test_assertIsNot>`

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

* I add a :ref:`call<how to call a function with input>` to :ref:`assertNotEqual<test_assertNotEqual>` for ``assert 0 == 0.0``

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

* I change :ref:`assertNotEqual<test_assertNotEqual>` to :ref:`assertEqual<test_assertEqual>`

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

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_assertion_error_w_is_vs_equal to TestAssertionError'

----

*********************************************************************************
will_not_run with a for loop
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----



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

* I add a :ref:`call<how to call a function with input>` to :ref:`test_assertEqual`

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

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move will_not_run to TestAssertionError'

----

*********************************************************************************
test_failure with a for loop
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----



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

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assertNotEqual>`

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

* I change :ref:`assertNotEqual<test_assertNotEqual>` to :ref:`assertEqual<test_assertEqual>`

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

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_failure to TestAssertionError'

----

*********************************************************************************
remove repetition with object attributes
*********************************************************************************

Three of the tests have the exact same :ref:`variables<what is a variable?>`. I can make them :ref:`object attributes<what is an object attribute?>` to remove repetition of making the same :ref:`variables<what is a variable?>` in the tests.

* I add an :ref:`object attribute<what is an object attribute?>` for ``an_integer = 0`` to :ref:`TestAssertionError<add TestAssertionError class>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 3

    class TestAssertionError(unittest.TestCase):

        an_integer = 0

        def test_assert_keyword(self):

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``an_integer = 0`` from :ref:`test_assertion_error_w_none`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``an_integer = 0`` from :ref:`test_assertion_error_w_false`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``an_integer = 0`` from :ref:`test_assertion_error_w_true`

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

* I add an :ref:`object attribute<what is an object attribute?>` for ``a_float = 0.0``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 4

    class TestAssertionError(unittest.TestCase):

        an_integer = 0
        a_float = 0.0

        def test_assert_keyword(self):

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_float = 0.0`` from :ref:`test_assertion_error_w_none`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_float = 0.0`` from :ref:`test_assertion_error_w_false`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_float = 0.0`` from :ref:`test_assertion_error_w_true`

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

* I add an :ref:`object attribute<what is an object attribute?>` for ``a_string = ''``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 5

    class TestAssertionError(unittest.TestCase):

        an_integer = 0
        a_float = 0.0
        a_string = ''

        def test_assert_keyword(self):

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_string = ''`` from :ref:`test_assertion_error_w_none`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_string = ''`` from :ref:`test_assertion_error_w_false`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_string = ''`` from :ref:`test_assertion_error_w_true`

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

* I add an :ref:`object attribute<what is an object attribute?>` for ``a_tuple = ()``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 6

    class TestAssertionError(unittest.TestCase):

        an_integer = 0
        a_float = 0.0
        a_string = ''
        a_tuple = ()

        def test_assert_keyword(self):

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_tuple = ()`` from :ref:`test_assertion_error_w_none`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_tuple = ()`` from :ref:`test_assertion_error_w_false`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_tuple = ()`` from :ref:`test_assertion_error_w_true`

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

* I add an :ref:`object attribute<what is an object attribute?>` for ``a_list = []``

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_list = []`` from :ref:`test_assertion_error_w_none`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_list = []`` from :ref:`test_assertion_error_w_false`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_list = []`` from :ref:`test_assertion_error_w_true`

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

* I add an :ref:`object attribute<what is an object attribute?>` for ``a_set = set()``

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_set = set()`` from :ref:`test_assertion_error_w_none`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_set = set()`` from :ref:`test_assertion_error_w_false`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_set = set()`` from :ref:`test_assertion_error_w_true`

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

* I add an :ref:`object attribute<what is an object attribute?>` for ``a_dictionary = {}``

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_dictionary = {}`` from :ref:`test_assertion_error_w_none`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_dictionary = {}`` from :ref:`test_assertion_error_w_false`

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

* I use the :ref:`object attribute<what is an object attribute?>` to remove repetition of ``a_dictionary = {}`` from :ref:`test_assertion_error_w_true`

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

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract object attributes'

:ref:`I can use object attributes to remove repetition<remove repetition with object attributes>`. I make them once and other things in the :ref:`object<everything is an object>` can reference them.

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
* I can use :ref:`object attributes<what is an object attribute?>` for things that repeat, which allows :ref:`methods<what is a method?>` of the same :ref:`object<everything is an object>` to use them.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test AssertionError with a for loop: tests>`

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