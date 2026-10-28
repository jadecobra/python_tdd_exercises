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

:ref:`test_assertion_error_w_true`, :ref:`test_assertion_error_w_false` and :ref:`test_assertion_error_w_none` all use a tuple_ with ``self.an_integer``, ``self.a_float``, ``self.a_string``, ``self.a_tuple``, ``self.a_list``, ``self.a_set`` and ``self.a_dictionary``.

I can use an :ref:`object attribute<what is an object attribute?>` with a :ref:`single starred expression<single starred expressions>` to remove the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add an :ref:`object attribute<what is an object attribute?>` to the :ref:`TestAssertionError object<add TestPerson object>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 10-14

    class TestAssertionError(unittest.TestCase):

        an_integer = 0
        a_float = 0.0
        a_string = ''
        a_tuple = ()
        a_list = []
        a_set = set()
        a_dictionary = {}
        basic_objects = (
            an_integer, a_float, a_string,
            a_tuple, a_list, a_set,
            a_dictionary,
        )

        def test_assert_keyword(self):

* I use the new :ref:`object attribute<what is an object attribute?>` with a :ref:`single starred expression<single starred expressions>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 7

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)
            self.assertIsNone(None)

            for an_object in (
                False, True, *self.basic_objects
            ):
                with self.subTest(object=an_object):
                    assert_is_not_none(an_object)
                    self.assertIsNot(an_object, None)
                    self.assertIsNotNone(an_object)

        def test_assertion_error_w_false(self):

  the test is still green.

* I change ``an_object`` to :ref:`None<what is None?>` in ``assert_is_not_none(an_object)`` to make sure the test still works as expected

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2

                with self.subTest(object=an_object):
                    assert_is_not_none(None)
                    self.assertIsNot(an_object, None)
                    self.assertIsNotNone(an_object)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(object=False) test_assertion_error_w_none -
        AssertionError: assert None is not None
    SUBFAILED(object=True) test_assertion_error_w_none -
        AssertionError: assert None is not None
    SUBFAILED(object=0) test_assertion_error_w_none -
        AssertionError: assert None is not None
    SUBFAILED(object=0.0) test_assertion_error_w_none -
        AssertionError: assert None is not None
    SUBFAILED(object='') test_assertion_error_w_none -
        AssertionError: assert None is not None
    SUBFAILED(object=()) test_assertion_error_w_none -
        AssertionError: assert None is not None
    SUBFAILED(object=[]) test_assertion_error_w_none -
        AssertionError: assert None is not None
    SUBFAILED(object=set()) test_assertion_error_w_none -
        AssertionError: assert None is not None
    SUBFAILED(object={}) test_assertion_error_w_none -
        AssertionError: assert None is not None

  it works.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I undo the change

.. code-block:: python
  :emphasize-lines: 2

              with self.subTest(object=an_object):
                  assert_is_not_none(an_object)
                  self.assertIsNot(an_object, None)
                  self.assertIsNotNone(an_object)

      def test_assertion_error_w_false(self):

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use the new :ref:`object attribute<what is an object attribute?>` with a :ref:`single starred expression<single starred expressions>` in :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 6

        def test_assertion_error_w_false(self):
            assert False is False
            self.assertIs(False, False)

            for an_object in (
                None, True, *self.basic_objects,
            ):
                with self.subTest(object=an_object):
                    assert_is_not_false(an_object)
                    self.assertIsNot(an_object, False)

        def test_assertion_error_w_true(self):

  the test is still green.

* I use the new :ref:`object attribute<what is an object attribute?>` with a :ref:`single starred expression<single starred expressions>` in :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 6

        def test_assertion_error_w_true(self):
            assert True is True
            self.assertIs(True, True)

            for an_object in (
                None, False, *self.basic_objects,
            ):
                with self.subTest(object=an_object):
                    assert_is_not_true(an_object)
                    self.assertIsNot(an_object, True)

        def test_assertion_error_w_equality(self):

  still green.

* I remove the other :ref:`object attributes<what is an object attribute?>` because they are only used by the ``basic_objects`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 3

    class TestAssertionError(unittest.TestCase):

        basic_objects = (0, 0.0, '', (), [], set(), {},)

        def test_assert_keyword(self):

  green.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract basic_objects object attribute'

----

*********************************************************************************
test_assertion_error_w_equality with a for loop
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add two :ref:`for loops<what is a for loop?>` to :ref:`test_assertion_error_w_equality`

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2-6

        def test_assertion_error_w_equality(self):
            objects = (None, False, True)
            for first in objects:
                for second in objects:
                    with self.subTest(pair=(first, second)):
                        self.assertEqual(first, second)

            assert_equal(None, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(pair=(None, False)) ...test_assertion_error_w_equality -
        AssertionError: None != False
    SUBFAILED(pair=(None, True)) ...test_assertion_error_w_equality -
        AssertionError: None != True
    SUBFAILED(pair=(False, None)) ...test_assertion_error_w_equality -
        AssertionError: False != None
    SUBFAILED(pair=(False, True)) ...test_assertion_error_w_equality -
        AssertionError: False != True
    SUBFAILED(pair=(True, None)) ...test_assertion_error_w_equality -
        AssertionError: True != None
    SUBFAILED(pair=(True, False)) ...test_assertion_error_w_equality -
        AssertionError: True != False

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I move ``self.assertEqual(first, second)`` into a :ref:`try statement<how to handle exceptions>` to handle the cases where the pairings are not equal

.. code-block:: python
  :lineno-start: 77
  :emphasize-lines: 6-9

      def test_assertion_error_w_equality(self):
          objects = (None, False, True)
          for first in objects:
              for second in objects:
                  with self.subTest(pair=(first, second)):
                      try:
                          self.assertEqual(first, second)
                      except AssertionError:
                          self.assertNotEqual(first, second)

          assert_equal(None, None)

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other statements from :ref:`test_assertion_error_w_equality` because they are now covered by the :ref:`for loops<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 77

        def test_assertion_error_w_equality(self):
            objects = (None, False, True)
            for first in objects:
                for second in objects:
                    with self.subTest(pair=(first, second)):
                        try:
                            self.assertEqual(first, second)
                        except AssertionError:
                            self.assertNotEqual(first, second)

        def test_assertion_error_w_is_vs_equal(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'test_assertion_error_w_equality with a for loop'

----

*********************************************************************************
add to basic_objects object attribute
*********************************************************************************

:ref:`test_assertion_error_w_true`, :ref:`test_assertion_error_w_false` and :ref:`test_assertion_error_w_none` look the same, the only difference is

.. code-block:: python

  False, True, *self.basic_objects  # test_assertion_error_w_none
  None, True, *self.basic_objects   # test_assertion_error_w_false
  None, False, *self.basic_objects  # test_assertion_error_w_true

which looks like some of the pairs from :ref:`test_assertion_error_w_equality`

.. code-block:: python
  :emphasize-lines: 1-2, 4

    SUBFAILED(pair=(None, False))
    SUBFAILED(pair=(None, True))
    SUBFAILED(pair=(False, None))
    SUBFAILED(pair=(False, True))
    SUBFAILED(pair=(True, None))
    SUBFAILED(pair=(True, False))

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add :ref:`True<test_what_is_true>` to the tuple_ in :ref:`test_assertion_error_w_true`

.. code-block:: python
  :lineno-start: 66
  :emphasize-lines: 6

        def test_assertion_error_w_true(self):
            assert True is True
            self.assertIs(True, True)

            for an_object in (
                None, False, True, *self.basic_objects,
            ):
                with self.subTest(object=an_object):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  SUBFAILED(object=True) ...
      AssertionError: assert True is not True

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I move ``assert_is_not_true(an_object)`` into a :ref:`try statement<how to handle Exceptions>` for the case where ``an_object`` is the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2-5

                with self.subTest(object=an_object):
                    try:
                        assert_is_not_true(an_object)
                    except AssertionError:
                        assert an_object is True

                    self.assertIsNot(an_object, True)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: True

* I move ``self.assertIsNot(an_object, True)`` into a :ref:`try statement<how to handle Exceptions>` for the case where ``an_object`` is the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 7-10

                with self.subTest(object=an_object):
                    try:
                        assert_is_not_true(an_object)
                    except AssertionError:
                        assert an_object is True

                    try:
                        self.assertIsNot(an_object, True)
                    except AssertionError:
                        self.assertIs(an_object, True)

        def test_assertion_error_w_equality(self):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the first :ref:`assertions<what is an assertion?>` from :ref:`test_assertion_error_w_true` because they are now covered by the :ref:`for loop<what is a for loop?>` and :ref:`try statements<how to handle Exceptions>`

  .. code-block:: python
    :lineno-start: 66

        def test_assertion_error_w_true(self):
            for an_object in (
                None, False, True, *self.basic_objects,
            ):
                with self.subTest(object=an_object):
                    try:
                        assert_is_not_true(an_object)
                    except AssertionError:
                        assert an_object is True

                    try:
                        self.assertIsNot(an_object, True)
                    except AssertionError:
                        self.assertIs(an_object, True)

        def test_assertion_error_w_equality(self):

* I add :ref:`False<test_what_is_false>` to the tuple_ in :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 6

        def test_assertion_error_w_false(self):
            assert False is False
            self.assertIs(False, False)

            for an_object in (
                None, False, True, *self.basic_objects,
            ):
                with self.subTest(object=an_object):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(object=False) ...
        AssertionError: assert False is not False

* I move ``assert_is_not_false(an_object)`` into a :ref:`try statement<how to handle Exceptions>` for the case where ``an_object`` is the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 2-5

                with self.subTest(object=an_object):
                    try:
                        assert_is_not_false(an_object)
                    except AssertionError:
                        assert an_object is False

                    self.assertIsNot(an_object, False)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: False

* I move ``self.assertIsNot(an_object, False)`` into a :ref:`try statement<how to handle Exceptions>` for the case where ``an_object`` is the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 7-10

                with self.subTest(object=an_object):
                    try:
                        assert_is_not_false(an_object)
                    except AssertionError:
                        assert an_object is False

                    try:
                        self.assertIsNot(an_object, False)
                    except AssertionError:
                        self.assertIs(an_object, False)

        def test_assertion_error_w_true(self):

  the test passes.

* I remove the first :ref:`assertions<what is an assertion?>` from :ref:`test_assertion_error_w_false` because they are now covered by the :ref:`for loop<what is a for loop?>` and :ref:`try statements<how to handle Exceptions>`

  .. code-block:: python
    :lineno-start: 55

        def test_assertion_error_w_false(self):
            for an_object in (
                None, False, True, *self.basic_objects,
            ):
                with self.subTest(object=an_object):
                    try:
                        assert_is_not_false(an_object)
                    except AssertionError:
                        assert an_object is False

                    try:
                        self.assertIsNot(an_object, False)
                    except AssertionError:
                        self.assertIs(an_object, False)

        def test_assertion_error_w_true(self):

* I add :ref:`None<what is None?>` to the tuple_ in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 7

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)
            self.assertIsNone(None)

            for an_object in (
                None, False, True, *self.basic_objects
            ):
                with self.subTest(object=an_object):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(object=None) ...
        AssertionError: assert None is not None

* I move ``assert_is_not_none(an_object)`` into a :ref:`try statement<how to handle Exceptions>` for the case where ``an_object`` is the same :ref:`object<everything is an object>` as :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 2-5

                with self.subTest(object=an_object):
                    try:
                        assert_is_not_none(an_object)
                    except AssertionError:
                        assert an_object is None

                    self.assertIsNot(an_object, None)
                    self.assertIsNotNone(an_object)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(object=None)...
        AssertionError: unexpectedly identical: None

* I move ``self.assertIsNot(an_object, None)`` into a :ref:`try statement<how to handle Exceptions>` for the case where ``an_object`` is the same :ref:`object<everything is an object>` as :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 7-10

                with self.subTest(object=an_object):
                    try:
                        assert_is_not_none(an_object)
                    except AssertionError:
                        assert an_object is None

                    try:
                        self.assertIsNot(an_object, None)
                    except AssertionError:
                        self.assertIs(an_object, None)

                    self.assertIsNotNone(an_object)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(object=None) ...
        AssertionError: unexpectedly None

* I move ``self.assertIsNotNone(an_object)`` into a :ref:`try statement<how to handle Exceptions>` for the case where ``an_object`` is the same :ref:`object<everything is an object>` as :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 6-9

                    try:
                        self.assertIsNot(an_object, None)
                    except AssertionError:
                        self.assertIs(an_object, None)

                    try:
                        self.assertIsNotNone(an_object)
                    except AssertionError:
                        self.assertIsNone(an_object)

        def test_assertion_error_w_false(self):

  the test passes.

* I remove the first :ref:`assertions<what is an assertion?>` from :ref:`test_assertion_error_w_none` because they are now covered by the :ref:`for loop<what is a for loop?>` and :ref:`try statements<how to handle Exceptions>`

  .. code-block:: python
    :lineno-start: 42

        def test_assertion_error_w_none(self):
            for an_object in (
                None, False, True, *self.basic_objects
            ):
                with self.subTest(object=an_object):
                    try:
                        assert_is_not_none(an_object)
                    except AssertionError:
                        assert an_object is None

                    try:
                        self.assertIsNot(an_object, None)
                    except AssertionError:
                        self.assertIs(an_object, None)

                    try:
                        self.assertIsNotNone(an_object)
                    except AssertionError:
                        self.assertIsNone(an_object)

        def test_assertion_error_w_false(self):

* I add :ref:`None<what is None?>`, :ref:`False<test_what_is_false>` and :ref:`True<test_what_is_true>` to the ``basic_objects`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 3-6

    class TestAssertionError(unittest.TestCase):

        basic_objects = (
            None, False, True,
            0, 0.0, '', (), [], set(), {},
        )

        def test_assert_keyword(self):

  the tests are still green.

* I remove :ref:`None<what is None?>`, :ref:`False<test_what_is_false>` and :ref:`True<test_what_is_true>` from :ref:`test_assertion_error_w_none` because they are now part of the ``basic_objects`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

        def test_assertion_error_w_none(self):
            for an_object in self.basic_objects:
                with self.subTest(object=an_object):

  still green.

* I make the same change to :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2

        def test_assertion_error_w_false(self):
            for an_object in self.basic_objects:
                with self.subTest(object=an_object):

  green.

* I do the same thing to :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 2

        def test_assertion_error_w_true(self):
            for an_object in self.basic_objects:
                with self.subTest(object=an_object):

  still green.

* I do the same thing to :ref:`test_assertion_error_w_equality`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 2-3

        def test_assertion_error_w_equality(self):
            for first in self.basic_objects:
                for second in self.basic_objects:
                    with self.subTest(pair=(first, second)):

  the tests are still green.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add to basic_objects object attribute'

*********************************************************************************
extract test_assertion_error
*********************************************************************************

:ref:`test_assertion_error_w_none`, :ref:`test_assertion_error_w_false` and :ref:`test_assertion_error_w_true` still look similar, they all have this :ref:`assertion<what is an assertion?>`

.. code-block:: python

  try:
      self.assertIsNot(an_object, something)
  except AssertionError:
      self.assertIs(an_object, something)

I can make a :ref:`function<what is a function?>` with a :ref:`for loop<what is a for loop?>` to remove the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`function<what is a function?>` with two :ref:`for loops<what is a for loop?>` like I did in :ref:`test_assertion_error_w_equality`

.. code-block:: python
  :lineno-start: 28
  :emphasize-lines: 8-12

  class TestAssertionError(unittest.TestCase):

      basic_objects = (
          None, False, True,
          0, 0.0, '', (), [], set(), {},
      )

      def test_assertion_error(self):
          for first in self.basic_objects:
              for second in self.basic_objects:
                  with self.subTest(pair=(first, second)):
                      self.assertIsNot(first, second)

      def test_assert_keyword(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what is AssertionError?>`

.. code-block:: python

  SUBFAILED(pair=(None, None)) ...test_assertion_error -
      AssertionError: unexpectedly identical: None
  SUBFAILED(pair=(False, False)) ...test_assertion_error -
      AssertionError: unexpectedly identical: False
  SUBFAILED(pair=(True, True)) ...test_assertion_error -
      AssertionError: unexpectedly identical: True
  SUBFAILED(pair=(0, 0)) ...test_assertion_error -
      AssertionError: unexpectedly identical: 0
  SUBFAILED(pair=(0.0, 0.0)) ...test_assertion_error -
      AssertionError: unexpectedly identical: 0.0
  SUBFAILED(pair=('', '')) ...test_assertion_error -
      AssertionError: unexpectedly identical: ''
  SUBFAILED(pair=((), ())) ...test_assertion_error -
      AssertionError: unexpectedly identical: ()
  SUBFAILED(pair=([], [])) ...test_assertion_error -
      AssertionError: unexpectedly identical: []
  SUBFAILED(pair=(set(), set())) ...test_assertion_error -
      AssertionError: unexpectedly identical: set()
  SUBFAILED(pair=({}, {})) ...test_assertion_error -
      AssertionError: unexpectedly identical: {}

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I move ``self.assertIsNot(first, second)`` into a :ref:`try statement<how to handle Exceptions>` for the cases where the first item is the same :ref:`object<everything is an object>` as the second one

.. code-block:: python
  :lineno-start: 35
  :emphasize-lines: 2-5

                  with self.subTest(pair=(first, second)):
                      try:
                          self.assertIsNot(first, second)
                      except AssertionError:
                          self.assertIs(first, second)

      def test_assert_keyword(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the :ref:`try statement<how to handle Exceptions>` for the :ref:`calls<how to call a function with input>` to the :ref:`assertIsNot<test_assertIsNot>` and :ref:`assertIs methods<test_assertIs>` in :ref:`test_assertion_error_w_none` since it is now covered by :ref:`test_assertion_error<extract test_assertion_error>`

  .. code-block:: python
    :lineno-start: 54

        def test_assertion_error_w_none(self):
            for an_object in self.basic_objects:
                with self.subTest(object=an_object):
                    try:
                        assert_is_not_none(an_object)
                    except AssertionError:
                        assert an_object is None

                    try:
                        self.assertIsNotNone(an_object)
                    except AssertionError:
                        self.assertIsNone(an_object)

        def test_assertion_error_w_false(self):

* I remove the :ref:`try statement<how to handle Exceptions>` for the :ref:`calls<how to call a function with input>` to the :ref:`assertIsNot<test_assertIsNot>` and :ref:`assertIs methods<test_assertIs>` in :ref:`test_assertion_error_w_false` since it is now covered by :ref:`test_assertion_error<extract test_assertion_error>`

  .. code-block:: python
    :lineno-start: 67

        def test_assertion_error_w_false(self):
            for an_object in self.basic_objects:
                with self.subTest(object=an_object):
                    try:
                        assert_is_not_false(an_object)
                    except AssertionError:
                        assert an_object is False

        def test_assertion_error_w_true(self):

* I remove the :ref:`try statement<how to handle Exceptions>` for the :ref:`calls<how to call a function with input>` to the :ref:`assertIsNot<test_assertIsNot>` and :ref:`assertIs methods<test_assertIs>` in :ref:`test_assertion_error_w_true` since it is now covered by :ref:`test_assertion_error<extract test_assertion_error>`

  .. code-block:: python
    :lineno-start: 75

        def test_assertion_error_w_true(self):
            for an_object in self.basic_objects:
                with self.subTest(object=an_object):
                    try:
                        assert_is_not_true(an_object)
                    except AssertionError:
                        assert an_object is True

        def test_assertion_error_w_equality(self):

* I add an :ref:`assertion<what is an assertion?>` for equality to :ref:`test_assertion_error<extract test_assertion_error>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 10

        def test_assertion_error(self):
            for first in self.basic_objects:
                for second in self.basic_objects:
                    with self.subTest(pair=(first, second)):
                        try:
                            self.assertIsNot(first, second)
                        except AssertionError:
                            self.assertIs(first, second)

                        self.assertEqual(first, second)

        def test_assert_keyword(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for eighty four sub tests

  .. code-block:: python

    ============ 84 failed, 8 passed in A.BCs ==============

  yikes!

* I move ``self.assertEqual(first, second)`` into a :ref:`try statement<how to handle Exceptions>` for the cases where the first item is equal to the second one

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 7-10

                    with self.subTest(pair=(first, second)):
                        try:
                            self.assertIsNot(first, second)
                        except AssertionError:
                            self.assertIs(first, second)

                        try:
                            self.assertEqual(first, second)
                        except AssertionError:
                            self.assertNotEqual(first, second)

        def test_assert_keyword(self):

  the test passes.

* I remove :ref:`test_assertion_error_w_equality` because it is now covered by :ref:`test_assertion_error<extract test_assertion_error>`
* I remove :ref:`test_assertion_error_w_is_vs_equal` because it is now covered by :ref:`test_assertion_error<extract test_assertion_error>`

  .. code-block:: python
    :lineno-start: 80

        def test_assertion_error_w_true(self):
            for an_object in self.basic_objects:
                with self.subTest(object=an_object):
                    try:
                        assert_is_not_true(an_object)
                    except AssertionError:
                        assert an_object is True

        def will_not_run():

----

:ref:`test_assertion_error_w_true`, :ref:`test_assertion_error_w_false` and :ref:`test_assertion_error_w_none` use helper :ref:`functions<what is a function?>` which hides their similarities

.. code-block:: python

  assert_is_not_true(an_object)   -> assert_is_not(x, True)
  assert_is_not_false(an_object)  -> assert_is_not(x, False)
  assert_is_not_none(an_object)   -> assert_is_not(x, None)

  assert_is_not(x, y)             -> assert x is not y

* I change the :ref:`call<how to call a function with input>` to :ref:`assert_is_not_true<extract assert_is_not_true function>` back to :ref:`the return statement` of the :ref:`assert_is_not function<extract assert_is_not function>`, in :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 5

        def test_assertion_error_w_true(self):
            for an_object in self.basic_objects:
                with self.subTest(object=an_object):
                    try:
                        assert an_object is not True
                    except AssertionError:
                        assert an_object is True

        def will_not_run():

  the test is still green.

* I change the :ref:`call<how to call a function with input>` to :ref:`assert_is_not_false<extract assert_is_not_false function>` back to :ref:`the return statement` of the :ref:`assert_is_not function<extract assert_is_not function>`, in :ref:`test_assertion_error_w_false`

  .. code-blok:: python
    :lineno-start: 72
    :emphasize-lines: 5

        def test_assertion_error_w_false(self):
            for an_object in self.basic_objects:
                with self.subTest(object=an_object):
                    try:
                        assert an_object is not False
                    except AssertionError:
                        assert an_object is False

        def test_assertion_error_w_true(self):

  still green.

* I change the :ref:`call<how to call a function with input>` to :ref:`assert_is_not_none<extract assert_is_not_none function>` back to :ref:`the return statement` of the :ref:`assert_is_not function<extract assert_is_not function>`, in :ref:`test_assertion_error_w_none`

  .. code-blok:: python
    :lineno-start: 59
    :emphasize-lines: 5

        def test_assertion_error_w_none(self):
            for an_object in self.basic_objects:
                with self.subTest(object=an_object):
                    try:
                        assert an_object is not None
                    except AssertionError:
                        assert an_object is None

  green.

* I add a simple :ref:`assert statement<what is an assertion?>` for when the first :ref:`object<everything is an object>` for the cases where the first item is the same :ref:`object<everything is an object>` as the second one

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 5

        def test_assertion_error(self):
            for first in self.basic_objects:
                for second in self.basic_objects:
                    with self.subTest(pair=(first, second)):
                        assert first is second

                        try:
                            self.assertIsNot(first, second)
                        except AssertionError:
                            self.assertIs(first, second)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for ninety sub tests

  .. code-block:: python

    ============ 90 failed, 6 passed in A.BCs ==============

  I do not think I would have written one hundred individual tests for :ref:`AssertionError<what causes AssertionError?>`

* I move ``assert first is second`` into a :ref:`try statement<how to handle Exceptions>` for the cases where the first item is NOT the same :ref:`object<everything is an object>` as the second one

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 5-8

        def test_assertion_error(self):
            for first in self.basic_objects:
                for second in self.basic_objects:
                    with self.subTest(pair=(first, second)):
                        try:
                            assert first is second
                        except AssertionError:
                            assert first is not second

                        try:
                            self.assertIsNot(first, second)
                        except AssertionError:
                            self.assertIs(first, second)

                        try:
                            self.assertEqual(first, second)
                        except AssertionError:
                            self.assertNotEqual(first, second)

        def test_assert_keyword(self):

  the test passes.

* I remove the :ref:`try statement<how to handle Exceptions>` for the simple :ref:`assert statements<what is an assertion?>` in :ref:`test_assertion_error_w_none` since it is now covered by :ref:`test_assertion_error<extract test_assertion_error>`

  .. code-block:: python
    :lineno-start: 64

        def test_assertion_error_w_none(self):
            for an_object in self.basic_objects:
                with self.subTest(object=an_object):
                    try:
                        self.assertIsNotNone(an_object)
                    except AssertionError:
                        self.assertIsNone(an_object)

        def test_assertion_error_w_false(self):

* I remove :ref:`test_assertion_error_w_false` because it is now covered by :ref:`test_assertion_error<extract test_assertion_error>`
* I remove :ref:`test_assertion_error_w_none` because it is now covered by :ref:`test_assertion_error<extract test_assertion_error>`

  .. code-block:: python
    :lineno-start: 64

        def test_assertion_error_w_none(self):
            for an_object in self.basic_objects:
                with self.subTest(object=an_object):
                    try:
                        self.assertIsNotNone(an_object)
                    except AssertionError:
                        self.assertIsNone(an_object)

        def will_not_run():

* I remove the :ref:`assert_is_not function<extract assert_is_not function>` because it is no longer used
* I remove the :ref:`assert_is_not_none<extract assert_is_not_none function>`, :ref:`assert_is_not_false<extract assert_is_not_false function>` and :ref:`assert_is_not_true functions<extract assert_is_not_true function>` because they are no longer used

  .. code-block:: python
    :linenos:

    import unittest


    def assert_not_equal(x, y):
        assert x != y

  the tests are still green.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract test_assertion_error'

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

----

*********************************************************************************
review
*********************************************************************************

I can use :ref:`for loops<what is a for loop?>`, :ref:`object attributes<what is an object attributes?>` and :ref:`functions<what is a function?>` to remove repetition. In this case I used them to make a test that has one hundred sub tests which would not have been fun to write one at a time, yet there is a problem. Can you tell just by looking at the code, that all :ref:`test_assertion_error` is doing is :ref:`asserting<what is an assertion?>` that

  - an item is the same :ref:`object<everything is an object>` as another, If this is :ref:`False<test_what_is_false>` then :ref:`assert<what is an assertion?>` that they are NOT the same :ref:`objects<everything is an object>`
  - an item is NOT the same :ref:`object<everything is an object>` as another, If this is :ref:`False<test_what_is_false>` then :ref:`assert<what is an assertion?>` that they are the same :ref:`objects<everything is an object>`
  - an item is equal to another, If this is :ref:`False<test_what_is_false>` then :ref:`assert<what is an assertion?>` that they are NOT equal

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
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`.
* :ref:`I know how to write programs that make decisions<truth table>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically with variables<how to make a Python Test Driven Development environment automatically with variables>`.
* :ref:`I know how to make a person with Exceptions<how to make a person with Exceptions>`.
* :ref:`I know how to test that an Exception is raised<how to test that an Exception is raised>`.
* :ref:`I know how to use Exception handlers in programs<how to handle Exceptions in programs>`.
* :ref:`I know how to make a person with loops<how to make a person with loops>`.

:ref:`Would you like to test the ATM project with loops?<test atm with loops>`

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