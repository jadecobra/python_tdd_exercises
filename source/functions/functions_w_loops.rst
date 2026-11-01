.. meta::
  :description: Pumping Python, by Johnny Blase. In the functions project, pytest-watcher reruns tests/test_functions.py while for loops and subTest replace repeated assertions. Four tests that assertIsNone on w_pass, w_return, w_return_none, and return_leaves_the_function become test_functions_return_none_by_default. The red step calls assertIsNotNone and the terminal shows AssertionError: unexpectedly None, then assertIsNone. test_identity_function loops None, object, the strings first and last, a tuple, a list, a set, and a dictionary. assertNotEqual on equal values shows AssertionError: None == None (and the same shape for the other objects) before assertEqual. test_why_use_a_for_loop loops add_x. A red expectation of 'BOOM!!!' shows AssertionError: 3 != 'BOOM!!!'. range(0, 10) and range(10) are the same numbers; range(1000) runs one thousand subtests and is slower. test_positional_arguments, test_keyword_arguments, and test_args_and_kwargs collapse into one loop over input pairs and four functions. A swapped tuple shows AssertionError: Tuples differ: ('first', 'last') != ('last', 'first'). args_and_kwargs still takes argument and last_input, so last_input= and first_input= raise TypeError: args_and_kwargs() got an unexpected keyword argument 'first_input'. Did you mean 'last_input'? The green step renames argument to first_input in the definition and the return, in src/functions/__init__.py. The review asks whether the loop still says what the test is checking.
  :keywords: for loop, subTest, range, assertIsNone, assertIsNotNone, assertEqual, assertNotEqual, unexpectedly None, Tuples differ, TypeError, first_input, args_and_kwargs, pytest-watcher, test_functions.py, Pumping Python, Johnny Blase

.. include:: ../links.rst

.. _range: https://docs.python.org/3/library/stdtypes.html?highlight=range#range
.. _range object: range_

#################################################################################
test functions with loops
#################################################################################

I want to use :ref:`for loops<what is a for loop?>` in the :ref:`functions<what is a function?>` project.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/functions/tests/test_functions_w_loops.py
  :caption: functions/tests/test_functions.py
  :language: python
  :linenos:
  :lines: 1-12

.. literalinclude:: ../code/functions/tests/test_functions_w_loops.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 14
  :lines: 14-27

.. literalinclude:: ../code/functions/tests/test_functions_w_loops.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 29
  :lines: 29-39

.. literalinclude:: ../code/functions/tests/test_functions_w_loops.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 41
  :lines: 41-49

.. literalinclude:: ../code/functions/tests/test_functions_w_loops.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 51
  :lines: 51-90

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd functions

* I open ``test_functions.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now

----

*********************************************************************************
extract test_functions_return_none_by_default
*********************************************************************************

:ref:`test_making_a_function_w_pass`, :ref:`test_making_a_function_w_return`, :ref:`test_making_a_function_w_return_none` and :ref:`test_what_happens_after_functions_return` all :ref:`assert<what is an assertion?>` that a :ref:`function<what is a function?>` returns :ref:`None<what is None?>` by default

.. code-block:: python

  self.assertIsNone(function())

I can make a :ref:`function<what is a function?>` with a :ref:`for loop<what is a for loop?>` to remove the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with a :ref:`for loop<what is a for loop?>` for what a :ref:`function<what is a function?>` returns by default

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 10
  :emphasize-lines: 5-13

        a_list = [0, 1, 2, 'n']
        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}

        def test_functions_return_none_by_default(self):
            for a_function in (
                src.functions.w_pass,
                src.functions.w_return,
                src.functions.w_return_none,
                src.functions.return_leaves_the_function,
            ):
                with self.subTest(a_function):
                    self.assertIsNotNone(a_function())

        def test_making_a_function_w_pass(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  SUBFAILED[<function w_pass at 0xffffa0b12345>] ...
      AssertionError: unexpectedly None
  SUBFAILED[<function w_return at 0xffffc6d78012>] ...
      AssertionError: unexpectedly None
  SUBFAILED[<function w_return_none at 0xffffe3f45678>] ...
      AssertionError: unexpectedly None
  SUBFAILED[<function return_leaves_the_function at 0xffffa01234b5>] ...
      AssertionError: unexpectedly None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertIsNotNone<another way to test if something is NOT None>` to :ref:`assertIsNone<another to test if something is None>`

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 21
  :emphasize-lines: 2

              with self.subTest(a_function):
                  self.assertIsNone(a_function())

      def test_making_a_function_w_pass(self):

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove :ref:`test_making_a_function_w_pass` because it is now covered by :ref:`test_functions_return_none_by_default<extract test_functions_return_none_by_default>`
* I remove :ref:`test_making_a_function_w_return` because it is now covered by :ref:`test_functions_return_none_by_default<extract test_functions_return_none_by_default>`
* I remove :ref:`test_making_a_function_w_return_none` because it is now covered by :ref:`test_functions_return_none_by_default<extract test_functions_return_none_by_default>`
* I remove :ref:`test_what_happens_after_functions_return` because it is now covered by :ref:`test_functions_return_none_by_default<extract test_functions_return_none_by_default>`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 21

                with self.subTest(a_function):
                    self.assertIsNone(a_function())

        def test_constant_function(self):

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'extract test_functions_return_none_by_default'

----

*********************************************************************************
test_identity_function with a loop
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`for loop<what is a for loop?>` to :ref:`test_identity_function`

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 29
  :emphasize-lines: 2-11

      def test_identity_function(self):
          for an_object in (
              None, object, self.first, self.last,
              self.a_tuple, self.a_list,
              self.a_set, self.a_dictionary,
          ):
              with self.subTest(an_object):
                  self.assertNotEqual(
                      src.functions.identity(an_object),
                      an_object
                  )

          self.assertIsNone(src.functions.identity(None))
          self.assertEqual(
              src.functions.identity(object), object
          )

      def test_why_use_a_function(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell
  :caption: terminal

  SUBFAILED[None] ...AssertionError: None == None
  SUBFAILED[<class 'object'>] ...
      AssertionError: <class 'object'> == <class 'object'>
  SUBFAILED[first] ...AssertionError: 'first' == 'first'
  SUBFAILED[last] ...AssertionError: 'last' == 'last'
  SUBFAILED[(0, 1, 2, 'n')] ...
      AssertionError: (0, 1, 2, 'n') == (0, 1, 2, 'n')
  SUBFAILED[[0, 1, 2, 'n']] ...
      AssertionError: [0, 1, 2, 'n'] == [0, 1, 2, 'n']
  SUBFAILED[{0, 1, 2, 'n'}] ...
      AssertionError: {0, 1, 2, 'n'} == {0, 1, 2, 'n'}
  SUBFAILED[{'key': 'value'}] ...
      AssertionError: {'key': 'value'} == {'key': 'value'}

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertNotEqual<test_assertNotEqual>` to :ref:`assertEqual<test_assertEqual>`

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 35
  :emphasize-lines: 2

              with self.subTest(an_object):
                  self.assertEqual(
                      src.functions.identity(an_object),
                      an_object
                  )

          self.assertIsNone(src.functions.identity(None))

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertions<what is an assertion?>` from :ref:`test_identity_function` because they are now covered by the :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 29

        def test_identity_function(self):
            for an_object in (
                None, object, self.first, self.last,
                self.a_tuple, self.a_list,
                self.a_set, self.a_dictionary,
            ):
                with self.subTest(an_object):
                    self.assertEqual(
                        src.functions.identity(an_object),
                        an_object
                    )

        def test_why_use_a_function(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'test_identity_function with a for loop'

----

*********************************************************************************
test_why_use_a_for_loop
*********************************************************************************

:ref:`test_why_use_a_function` makes ten :ref:`assertions<what is an assertion?>` that all look the same

.. code-block:: python

  self.assertEqual(add_x(a_number), result)

I can use a :ref:`for loop<what is a for loop?>` to remove the repetition

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`for loop<what is a for loop?>` to :ref:`test_why_use_a_function`

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 41
  :emphasize-lines: 5-7

      def test_why_use_a_function(self):
          def add_x(number):
              return 3 + number

          for a_number in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
              with self.subTest(a_number):
                  self.assertEqual(add_x(a_number), 'BOOM!!!')

          self.assertEqual(add_x(0), 3)
          self.assertEqual(add_x(1), 4)
          self.assertEqual(add_x(2), 5)

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  SUBFAILED[0] ...AssertionError: 3 != 'BOOM!!!'
  SUBFAILED[1] ...AssertionError: 4 != 'BOOM!!!'
  SUBFAILED[2] ...AssertionError: 5 != 'BOOM!!!'
  SUBFAILED[3] ...AssertionError: 6 != 'BOOM!!!'
  SUBFAILED[4] ...AssertionError: 7 != 'BOOM!!!'
  SUBFAILED[5] ...AssertionError: 8 != 'BOOM!!!'
  SUBFAILED[6] ...AssertionError: 9 != 'BOOM!!!'
  SUBFAILED[7] ...AssertionError: 10 != 'BOOM!!!'
  SUBFAILED[8] ...AssertionError: 11 != 'BOOM!!!'
  SUBFAILED[9] ...AssertionError: 12 != 'BOOM!!!'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``self.assertEqual(add_x(a_number), 'BOOM!!!')``

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 45
  :emphasize-lines: 3

          for a_number in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
              with self.subTest(a_number):
                  self.assertEqual(
                      add_x(a_number), a_number+3
                  )

          self.assertEqual(add_x(0), 3)

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertions<what is an assertion?>` from :ref:`test_why_use_a_function` because they are now covered by the :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 41

        def test_why_use_a_function(self):
            def add_x(number):
                return 3 + number

            for a_number in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                with self.subTest(a_number):
                    self.assertEqual(
                        add_x(a_number), a_number+3
                    )

        def test_positional_arguments(self):

----

*********************************************************************************
the range object
*********************************************************************************

Python_ has an :ref:`iterable<what is an iterable?>` I can use to make a sequence of numbers, it is called the `range object`_.

``range(0, a_number)`` makes a `range object`_ that goes from the first number in the parentheses to the second number minus ``1``


* I change the tuple_ in the :ref:`for loop<what is a for loop?>` to a `range object`_

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 41
    :emphasize-lines: 5, 7

        def test_why_use_a_function(self):
            def add_x(number):
                return 3 + number

            for a_number in range(0, 10):
                with self.subTest(a_number):
                    self.assertNotEqual(
                        add_x(a_number), a_number+3
                    )

        def test_positional_arguments(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    SUBFAILED[0] ...AssertionError: 3 == 3
    SUBFAILED[1] ...AssertionError: 4 == 4
    SUBFAILED[2] ...AssertionError: 5 == 5
    SUBFAILED[3] ...AssertionError: 6 == 6
    SUBFAILED[4] ...AssertionError: 7 == 7
    SUBFAILED[5] ...AssertionError: 8 == 8
    SUBFAILED[6] ...AssertionError: 9 == 9
    SUBFAILED[7] ...AssertionError: 10 == 10
    SUBFAILED[8] ...AssertionError: 11 == 11
    SUBFAILED[9] ...AssertionError: 12 == 12

* I can remove the ``0`` from the `range object`_

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 45
    :emphasize-lines: 1

            for a_number in range(10):

  the :ref:`AssertionError<what causes AssertionError?>` stays the same.

* I can use any number I want

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 45
    :emphasize-lines: 1

            for a_number in range(1000):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for one thousand sub tests and my tests run slower than before. What would happen if I changed the number to one million?

* I change :ref:`assertNotEqual<test_assertNotEqual>` to :ref:`assertEqual<test_assertEqual>`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 41
    :emphasize-lines: 7

        def test_why_use_a_function(self):
            def add_x(number):
                return 3 + number

            for a_number in range(1000):
                with self.subTest(a_number):
                    self.assertEqual(
                        add_x(a_number), a_number+3
                    )

        def test_positional_arguments(self):

  the test passes.

* I change the name of the test from :ref:`test_why_use_a_function` to :ref:`test_why_use_a_for_loop`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 35
    :emphasize-lines: 7

                with self.subTest(an_object):
                    self.assertEqual(
                        src.functions.identity(an_object),
                        an_object
                    )

        def test_why_use_a_for_loop(self):
            def add_x(number):
                return 3 + number

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'rename to test_why_use_a_for_loop'

----

*********************************************************************************
test_positional_arguments with for loops
*********************************************************************************

:ref:`test_positional_arguments` has :ref:`assertions<what is an assertion?>` that check what happens when a :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>` with :ref:`positional arguments<test_positional_arguments>`

.. code-block:: python

  self.assertEqual(
      function(position_0, position_1),
      (position_0, position_1)
  )

I can use a :ref:`for loop<what is a for loop?>` to remove repetition from the test.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`for loop<what is a for loop?>` for each one of the arguments used

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 51
  :emphasize-lines: 2-15

      def test_positional_arguments(self):
          for first, second in (
              (self.first, self.last),
              (self.last, self.first),
              (0, 1),
              (self.a_tuple, self.a_list),
              (self.a_set, self.a_dictionary),
          ):
              with self.subTest(inputs=(first, second)):
                  self.assertEqual(
                      src.functions.positional_arguments(
                          first, second
                      ),
                      (second, first)
                  )

          positional_arguments = (
              src.functions.positional_arguments
          )

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  SUBFAILED(inputs=('first', 'last')) ...
      AssertionError: Tuples differ:
          ('first', 'last') != ('last', 'first')
  SUBFAILED(inputs=('last', 'first')) ...
      AssertionError: Tuples differ:
          ('last', 'first') != ('first', 'last')
  SUBFAILED(inputs=(0, 1)) ...
      AssertionError: Tuples differ:
          (0, 1) != (1, 0)
  SUBFAILED(inputs=((0, 1, 2, 'n'), [0, 1, 2, 'n'])) ...
      AssertionError: Tuples differ:
          ((0, 1, 2, 'n'), [0, 1, 2, 'n'])
      !=  ([0, 1, 2, 'n'], (0, 1, 2, 'n'))
  SUBFAILED(inputs=({0, 1, 2, 'n'}, {'key': 'value'})) ...
      AssertionError: Tuples differ:
          ({0, 1, 2, 'n'}, {'key': 'value'})
       != ({'key': 'value'}, {0, 1, 2, 'n'})

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_positional_arguments`

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 59
  :emphasize-lines: 6

              with self.subTest(inputs=(first, second)):
                  self.assertEqual(
                      src.functions.positional_arguments(
                          first, second
                      ),
                      (first, second)
                  )

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`keyword_arguments<test_keyword_arguments>`, :ref:`args_and_kwargs<test_args_and_kwargs>` and :ref:`optional_arguments functions<test_optional_arguments>`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 51
    :emphasize-lines: 9-14

        def test_positional_arguments(self):
            for first, second in (
                (self.first, self.last),
                (self.last, self.first),
                (0, 1),
                (self.a_tuple, self.a_list),
                (self.a_set, self.a_dictionary),
            ):
                for a_function in (
                    src.functions.positional_arguments,
                    src.functions.keyword_arguments,
                    src.functions.args_and_kwargs,
                    src.functions.optional_arguments,
                ):

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 65
    :emphasize-lines: 1-7

                    with self.subTest(
                        a_function=a_function, inputs=(first, second)
                    ):
                        self.assertEqual(
                            a_function(first, second),
                            (second, first)
                        )

            positional_arguments = (
                src.functions.positional_arguments
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for twenty sub tests.

* I change the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_positional_arguments`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 68
    :emphasize-lines: 3

                        self.assertEqual(
                            a_function(first, second),
                            (first, second)
                        )

            positional_arguments = (
                src.functions.positional_arguments
            )

  the test passes.

* I remove the other statements from :ref:`test_positional_arguments` because they are now covered by the :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 68

                        self.assertEqual(
                            a_function(first, second),
                            (first, second)
                        )

        def test_keyword_arguments(self):

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_positional_arguments with for loops'

----

*********************************************************************************
test_keyword_arguments with for loops
*********************************************************************************

:ref:`test_keyword_arguments` has :ref:`assertions<what is an assertion?>` that check what happens when a :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>` with :ref:`keyword arguments<test_keyword_arguments>`

.. code-block:: python

  self.assertEqual(
      function(
          last_input=something,
          first_input=something_else),
      (something_else, something)
  )

I can use a :ref:`for loop<what is a for loop?>` to remove repetition from the test.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`for loop<what is a for loop?>` for each one of the arguments and the :ref:`positional_arguments<test_positional_arguments>`, :ref:`keyword_arguments<test_keyword_arguments>` and :ref:`optional_arguments functions<test_optional_arguments>` because they all have the same :ref:`signature<how to make a function that takes input>`

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 73
  :emphasize-lines: 2-13

      def test_keyword_arguments(self):
          for first, second in (
              (self.first, self.last),
              (self.last, self.first),
              (0, 1),
              (self.a_tuple, self.a_list),
              (self.a_set, self.a_dictionary),
          ):
              for a_function in (
                  src.functions.positional_arguments,
                  src.functions.keyword_arguments,
                  src.functions.optional_arguments,
              ):

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 86
  :emphasize-lines: 1-10

                  with self.subTest(
                      a_function=a_function, inputs=(first, second)
                  ):
                      self.assertEqual(
                          a_function(
                              last_input=first,
                              first_input=second
                          ),
                          (first, second)
                      )

          keyword_arguments = (
              src.functions.keyword_arguments
          )

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for fifteen sub tests.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_keyword_arguments`

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 89
  :emphasize-lines: 6

                      self.assertEqual(
                          a_function(
                              last_input=first,
                              first_input=second
                          ),
                          (second, first)
                      )

          keyword_arguments = (
              src.functions.keyword_arguments
          )

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the :ref:`args_and_kwargs function<test_args_and_kwargs>` to the :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 73
    :emphasize-lines: 12

        def test_keyword_arguments(self):
            for first, second in (
                (self.first, self.last),
                (self.last, self.first),
                (0, 1),
                (self.a_tuple, self.a_list),
                (self.a_set, self.a_dictionary),
            ):
                for a_function in (
                    src.functions.positional_arguments,
                    src.functions.keyword_arguments,
                    src.functions.args_and_kwargs,
                    src.functions.optional_arguments,
                ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell
    :caption: terminal

    SUBFAILED(
        a_function=<function args_and_kwargs at 0xffff01ab2c34>,
        inputs=('first', 'last')
    ) ...TypeError: args_and_kwargs()
                    got an unexpected keyword argument 'first_input'.
                    Did you mean 'last_input'?
    SUBFAILED(
        a_function=<function args_and_kwargs at 0xffff01ab2c34>,
        inputs=('last', 'first')
    ) ...TypeError: args_and_kwargs()
                    got an unexpected keyword argument 'first_input'.
                    Did you mean 'last_input'?
    SUBFAILED(
        a_function=<function args_and_kwargs at 0xffff01ab2c34>,
        inputs=(0, 1)
    ) ...TypeError: args_and_kwargs()
                    got an unexpected keyword argument 'first_input'.
                    Did you mean 'last_input'?
    SUBFAILED(
        a_function=<function args_and_kwargs at 0xffff01ab2c34>,
        inputs=((0, 1, 2, 'n'), [0, 1, 2, 'n'])
    ) ...TypeError: args_and_kwargs()
                    got an unexpected keyword argument 'first_input'.
                    Did you mean 'last_input'?
    SUBFAILED(
        a_function=<function args_and_kwargs at 0xffff01ab2c34>,
        inputs=({0, 1, 2, 'n'}, {'key': 'value'})
    ) ...TypeError: args_and_kwargs()
                    got an unexpected keyword argument 'first_input'.
                    Did you mean 'last_input'?

* I open ``__init__.py`` from the :ref:`functions folder<what is a function?>` in the ``src`` folder_
* I change ``argument`` to ``first_input`` in the :ref:`definition<how to make a function that can take input>` and the return of the :ref:`args_and_kwargs function<test_args_and_kwargs>`, in ``src/functions/__init__.py``

  .. code-block:: python
    :caption: functions/src/functions/__init__.py
    :lineno-start: 7
    :emphasize-lines: 7-8

    def optional_arguments(
            first_input, last_input='doe',
        ):
        return first_input, last_input


    def args_and_kwargs(first_input, last_input):
        return first_input, last_input


    def keyword_arguments(first_input, last_input):

  the test passes.

* I remove the other :ref:`assertions<what is an assertion?>` from :ref:`test_keyword_arguments` in ``tests/test_functions.py``

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 90

                        self.assertEqual(
                            a_function(
                                last_input=first,
                                first_input=second
                            ),
                            (second, first)
                        )

        def test_args_and_kwargs(self):

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_keyword_arguments with for loops'

----

*********************************************************************************
test_args_and_kwargs with for loops
*********************************************************************************

:ref:`test_positional_arguments` and :ref:`test_keyword_arguments` now look the same, one uses :ref:`for loops<what is a for loop?>`

.. code-block:: python

  self.assertEqual(
      function(
          last_input=something,
          first_input=something_else),
      (something_else, something)
  )

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add the :ref:`for loops<what is a for loop?>` for each one of the arguments and the :ref:`positional_arguments<test_positional_arguments>`, :ref:`keyword_arguments<test_keyword_arguments>`, :ref:`args_and_kwargs<test_args_and_kwargs>` and :ref:`optional_arguments functions<test_optional_arguments>`

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 98
  :emphasize-lines: 2-14

      def test_args_and_kwargs(self):
          for first, second in (
              (self.first, self.last),
              (self.last, self.first),
              (0, 1),
              (self.a_tuple, self.a_list),
              (self.a_set, self.a_dictionary),
          ):
              for a_function in (
                  src.functions.positional_arguments,
                  src.functions.keyword_arguments,
                  src.functions.args_and_kwargs,
                  src.functions.optional_arguments,
              ):

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 112
  :emphasize-lines: 1-14

                  with self.subTest(
                      a_function=a_function, inputs=(first, second)
                  ):
                      self.assertEqual(
                          a_function(first, second),
                          (second, first)
                      )
                      self.assertEqual(
                          a_function(
                              last_input=first,
                              first_input=second
                          ),
                          (first, second)
                      )

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 126
  :emphasize-lines: 1-12

                      self.assertEqual(
                          a_function(
                              first, last_input=second,
                          ),
                          (second, first)
                      )
                      self.assertEqual(
                          a_function(
                              second, last_input=first,
                          ),
                          (first, second)
                      )

          self.assertEqual(
              src.functions.args_and_kwargs(
                  self.first, last_input=self.last
              ),
              (self.first, self.last)
          )

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for twenty sub tests.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the expectation of the :ref:`assertion<what is an assertion?>` for :ref:`positional arguments<test_positional_arguments>`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 112
    :emphasize-lines: 6

                    with self.subTest(
                        a_function=a_function, inputs=(first, second)
                    ):
                        self.assertEqual(
                            a_function(first, second),
                            (first, second)
                        )
                        self.assertEqual(
                            a_function(
                                last_input=first,
                                first_input=second
                            ),
                            (first, second)
                        )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for twenty sub tests for the :ref:`assertion<what is an assertion?>` for :ref:`keyword arguments<test_keyword_arguments>`.

* I change the expectation of the :ref:`assertion<what is an assertion?>` for :ref:`keyword arguments<test_keyword_arguments>`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 119
    :emphasize-lines: 6

                        self.assertEqual(
                            a_function(
                                last_input=first,
                                first_input=second
                            ),
                            (second, first)
                        )
                        self.assertEqual(
                            a_function(
                                first, last_input=second,
                            ),
                            (second, first)
                        )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for twenty sub tests for the first :ref:`assertion<what is an assertion?>` for :ref:`positional and keyword arguments<test_args_and_kwargs>`.

* I change the expectation of the first :ref:`assertion<what is an assertion?>` for :ref:`positional and keyword arguments<test_args_and_kwargs>`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 126
    :emphasize-lines: 5

                        self.assertEqual(
                            a_function(
                                first, last_input=second,
                            ),
                            (first, second)
                        )
                        self.assertEqual(
                            a_function(
                                second, last_input=first,
                            ),
                            (first, second)
                        )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for twenty sub tests for the second :ref:`assertion<what is an assertion?>` for :ref:`positional and keyword arguments<test_args_and_kwargs>`.

* I change the expectation of the second :ref:`assertion<what is an assertion?>` for :ref:`positional and keyword arguments<test_args_and_kwargs>`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 132
    :emphasize-lines: 5

                        self.assertEqual(
                            a_function(
                                second, last_input=first,
                            ),
                            (second, first)
                        )

            self.assertEqual(
                src.functions.args_and_kwargs(
                    self.first, last_input=self.last
                ),
                (self.first, self.last)
            )

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertion<what is an assertion?>` from :ref:`test_args_and_kwargs`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 132

                        self.assertEqual(
                            a_function(
                                second, last_input=first,
                            ),
                            (second, first)
                        )

        def test_optional_arguments(self):

* I remove :ref:`test_positional_arguments` and :ref:`test_keyword_arguments` because they are now covered by :ref:`test_args_and_kwargs`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 41

        def test_why_use_a_for_loop(self):
            def add_x(number):
                return 3 + number

            for a_number in range(1000):
                with self.subTest(a_number):
                    self.assertEqual(
                        add_x(a_number), a_number+3
                    )

        def test_args_and_kwargs(self):

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_args_and_kwargs with for loops'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_functions.py`` and ``src/functions/__init__.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of ``functions``

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

----

*********************************************************************************
review
*********************************************************************************

* I used :ref:`for loops<what is a for loop?>` to remove repetition from the tests. If you did not go through this project and someone gave you this code, do you think you can tell what it is testing?

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test functions with loops: tests>`

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

:ref:`Would you like to test the microwave project with loops?<test microwave with loops>`

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