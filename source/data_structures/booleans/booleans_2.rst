.. meta::
  :description: Learn Python truthiness and falsiness using the bool() function and unittest. This TDD tutorial guides beginners through testing None, zero, empty lists, strings, and dictionaries using assertTrue and assertFalse. Understand how Python evaluates objects as True or False and see the internal logic of unittest assertion methods.
  :keywords: Jacob Itegboje, Python bool function tutorial, truthiness and falsiness in Python, unittest assertTrue vs assertFalse, TDD for beginners, python bool(None), is empty list false in python, python bool(0) vs bool(1), testing truthy values, python unittest internal logic, programming tutorials for beginners, python data structure truthiness, bool(str), bool(tuple), bool(dict), bool(set), python truth table tests

.. include:: ../../links.rst

.. _bool function: bool_

#################################################################################
booleans 2: test with bool
#################################################################################

I want to use the `bool built-in function`_ with the `assertFalse method`_ in :ref:`test_what_is_false` and the `assertTrue method`_ in :ref:`test_what_is_true`.


The `bool function`_ tells if Python_ groups the thing in parentheses as :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`. Which means the result of ``bool(something)`` is :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`.

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/booleans/test_booleans_truth_table.py
  :language: python
  :linenos:

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``booleans`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd booleans

  the terminal_ shows I am in the ``booleans`` folder_

  .. code-block:: shell

    .../pumping_python/booleans

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows

  .. code-block:: shell
    :emphasize-lines: 5

    rootdir: .../pumping_python/booleans
    configfile: pyproject.toml
    collected 2 items

    tests/test_booleans.py ..                                     [100%]

    ======================== 2 passed in X.YZs =========================

* I hold :kbd:`ctrl` on the keyboard, then click on ``tests/test_booleans.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
bool at work
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new :ref:`assertion<what is an assertion?>` to the ``test_what_is_false`` :ref:`method<what is a function?>`

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 5
  :emphasize-text: bool assertTrue

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)
          self.assertFalse(False)
          self.assertFalse(None)
          self.assertTrue(bool(None))
          self.assertFalse(0)
          self.assertFalse(0.0)
          self.assertFalse(str())
          self.assertFalse(tuple())
          self.assertFalse(list())
          self.assertFalse(set())
          self.assertFalse(dict())

      def test_what_is_true(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: False is not true

the result of ``bool(None)`` is :ref:`False<test_what_is_false>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertTrue_ to assertFalse_

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 1

          self.assertFalse(bool(None))

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` with bool_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 7
    :emphasize-text: bool assertTrue

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(bool(None))
            self.assertFalse(0)
            self.assertTrue(bool(0))
            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse(dict())

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the result of ``bool(0)`` is :ref:`False<test_what_is_false>`

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 1

            self.assertFalse(bool(0))

  the test passes

* I add a failing :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 9
    :emphasize-text: bool assertTrue

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(bool(None))
            self.assertFalse(0)
            self.assertFalse(bool(0))
            self.assertFalse(0.0)
            self.assertTrue(bool(0.0))
            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse(dict())

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the result of ``bool(0.0)`` is :ref:`False<test_what_is_false>`

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 1

            self.assertFalse(bool(0.0))

  the test passes

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 11
    :emphasize-text: bool assertTrue

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(bool(None))
            self.assertFalse(0)
            self.assertFalse(bool(0))
            self.assertFalse(0.0)
            self.assertFalse(bool(0.0))
            self.assertFalse(str())
            self.assertTrue(bool(str()))
            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse(dict())

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the result of ``bool(str())`` is :ref:`False<test_what_is_false>`

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1

            self.assertFalse(bool(str()))

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 4
    :emphasize-text: bool assertTrue

            self.assertFalse(str())
            self.assertFalse(bool(str()))
            self.assertFalse(tuple())
            self.assertTrue(bool(tuple()))
            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse(dict())

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the result of ``bool(tuple())`` is :ref:`False<test_what_is_false>`

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 1

            self.assertFalse(bool(tuple()))

  the test passes

* I add another failing :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 6
    :emphasize-text: bool assertTrue

            self.assertFalse(str())
            self.assertFalse(bool(str()))
            self.assertFalse(tuple())
            self.assertFalse(bool(tuple()))
            self.assertFalse(list())
            self.assertTrue(bool(list()))
            self.assertFalse(set())
            self.assertFalse(dict())

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the result of ``bool(list())`` is :ref:`False<test_what_is_false>`

* I make the :ref:`assertion<what is an assertion?>` :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 1

            self.assertFalse(bool(list()))

  the test passes

* I add another failing :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4
    :emphasize-text: bool assertTrue

            self.assertFalse(list())
            self.assertFalse(bool(list()))
            self.assertFalse(set())
            self.assertTrue(bool(set()))
            self.assertFalse(dict())

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the result of ``bool(set())`` is :ref:`False<test_what_is_false>`

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start:  22
    :emphasize-lines: 1

            self.assertFalse(bool(set()))

  the test passes

* One more

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 6
    :emphasize-text: bool assertTrue

            self.assertFalse(list())
            self.assertFalse(bool(list()))
            self.assertFalse(set())
            self.assertFalse(bool(set()))
            self.assertFalse(dict())
            self.assertTrue(bool(dict()))

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the result of ``bool(dict())`` is :ref:`False<test_what_is_false>`

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 19

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(bool(None))
            self.assertFalse(0)
            self.assertFalse(bool(0))
            self.assertFalse(0.0)
            self.assertFalse(bool(0.0))
            self.assertFalse(str())
            self.assertFalse(bool(str()))
            self.assertFalse(tuple())
            self.assertFalse(bool(tuple()))
            self.assertFalse(list())
            self.assertFalse(bool(list()))
            self.assertFalse(set())
            self.assertFalse(bool(set()))
            self.assertFalse(dict())
            self.assertFalse(bool(dict()))

        def test_what_is_true(self):

  the test passes

* The `assertFalse method`_ uses an :ref:`if statement<if statements>` to check if what it gets as input is :ref:`False<test_what_is_false>`, this is what the code looks like

  .. code-block:: python

    def assertFalse(self, something, message=None):
        """Check that something is false."""
        if something:
            raise AssertionError(message)

  here is what happens when the `assertFalse method`_ is called

  - it raises :ref:`AssertionError<what causes AssertionError?>` if ``something`` is :ref:`True<test_what_is_true>`, because ``if bool(something) == True`` is the same as ``if bool(something)`` is the same as ``if something``
  - it returns :ref:`None<what is None?>` if something is :ref:`False<test_what_is_false>` because :ref:`all functions return None by default, as if they have an invisible line that says return None<test_making_a_function_w_return_none>`

  - I do not have to give a value for the ``message`` parameter when I call `assertFalse`_ because

    .. code-block:: python

      self.assertFalse(something)

    is the same as

    .. code-block:: python

      self.assertFalse(something, None)

    is the same as

    .. code-block:: python

      self.assertFalse(
          something=something,
          message=None,
      )

    A :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without the parameter

  `click here to see the actual code for the assertFalse method <https://github.com/python/cpython/blob/2faceeec5c0fb06498a9654d429180ac4610c65a/Lib/unittest/case.py#L750>`_

----

*********************************************************************************
more bool at work
*********************************************************************************

Oh No! More of the same thing

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` with bool_ to :ref:`test_what_is_true`

.. code-block:: python
  :lineno-start: 26
  :emphasize-lines: 5
  :emphasize-text: bool assertFalse

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)
          self.assertTrue(True)
          self.assertTrue(-1)
          self.assertFalse(bool(-1))
          self.assertTrue(1)
          self.assertTrue(-0.1)
          self.assertTrue(0.1)
          self.assertTrue("text")
          self.assertTrue((1, 2, 3, 'n'))
          self.assertTrue([1, 2, 3, 'n'])
          self.assertTrue({1, 2, 3, 'n'})
          self.assertTrue({'key': 'value'})


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: True is not false

the result of ``bool(-1)`` is :ref:`True<test_what_is_true>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertFalse_ to assertTrue_

.. code-block:: python
  :lineno-start: 30
  :emphasize-lines: 1

          self.assertTrue(bool(-1))

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* on to the next one

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 7
    :emphasize-text: bool assertFalse

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(bool(-1))
            self.assertTrue(1)
            self.assertFalse(bool(1))
            self.assertTrue(-0.1)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the result of ``bool(1)`` is :ref:`True<test_what_is_true>`

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 1

            self.assertTrue(bool(1))

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 9
    :emphasize-text: bool assertFalse

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(bool(-1))
            self.assertTrue(1)
            self.assertTrue(bool(1))
            self.assertTrue(-0.1)
            self.assertFalse(bool(-0.1))
            self.assertTrue(0.1)
            self.assertTrue("text")
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue({1, 2, 3, 'n'})
            self.assertTrue({'key': 'value'})


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the result of ``bool(-0.1)`` is :ref:`True<test_what_is_true>`

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1

            self.assertTrue(bool(-0.1))

  the test passes

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 4
    :emphasize-text: bool assertFalse

            self.assertTrue(-0.1)
            self.assertTrue(bool(-0.1))
            self.assertTrue(0.1)
            self.assertFalse(bool(0.1))
            self.assertTrue("text")
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue({1, 2, 3, 'n'})
            self.assertTrue({'key': 'value'})

    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the result of ``bool(0.1)`` is :ref:`True<test_what_is_true>`

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 1

            self.assertTrue(bool(0.1))

  the test passes

* I add another one

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 6
    :emphasize-text: bool assertFalse

            self.assertTrue(-0.1)
            self.assertTrue(bool(-0.1))
            self.assertTrue(0.1)
            self.assertTrue(bool(0.1))
            self.assertTrue("text")
            self.assertFalse(bool("text"))
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue({1, 2, 3, 'n'})
            self.assertTrue({'key': 'value'})


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the result of ``bool("text")`` is :ref:`True<test_what_is_true>`

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 1

            self.assertTrue(bool("text"))

  the the test passes

* I add another :ref:`assertion<what is an assertion?>`, when is this going to end?

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4
    :emphasize-text: bool assertFalse

            self.assertTrue("text")
            self.assertTrue(bool("text"))
            self.assertTrue((1, 2, 3, 'n'))
            self.assertFalse(bool((1, 2, 3, 'n')))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue({1, 2, 3, 'n'})
            self.assertTrue({'key': 'value'})


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the result of ``bool((1, 2, 3, 'n'))`` is :ref:`True<test_what_is_true>`

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 1

            self.assertTrue(bool((1, 2, 3, 'n')))

  the test passes

* another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 6
    :emphasize-text: bool assertFalse

            self.assertTrue("text")
            self.assertTrue(bool("text"))
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue(bool((1, 2, 3, 'n')))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertFalse(bool([1, 2, 3, 'n']))
            self.assertTrue({1, 2, 3, 'n'})
            self.assertTrue({'key': 'value'})


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the result of ``bool([1, 2, 3, 'n'])`` is :ref:`True<test_what_is_true>`

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1

            self.assertTrue(bool([1, 2, 3, 'n']))

  the test passes

* I add the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 4
    :emphasize-text: bool assertFalse

            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue(bool([1, 2, 3, 'n']))
            self.assertTrue({1, 2, 3, 'n'})
            self.assertFalse(bool({1, 2, 3, 'n'}))
            self.assertTrue({'key': 'value'})


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not

  the result of ``bool({1, 2, 3, 'n'})`` is :ref:`True<test_what_is_true>`

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 1

            self.assertTrue(bool({1, 2, 3, 'n'}))

  the test passes

* I add the last one. Finally!

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 6
    :emphasize-text: bool assertFalse

            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue(bool([1, 2, 3, 'n']))
            self.assertTrue({1, 2, 3, 'n'})
            self.assertTrue(bool({1, 2, 3, 'n'}))
            self.assertTrue({'key': 'value'})
            self.assertFalse(bool({'key': 'value'}))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the result of ``bool({'key': 'value'})`` is :ref:`True<test_what_is_true>`

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 21

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(bool(-1))
            self.assertTrue(1)
            self.assertTrue(bool(1))
            self.assertTrue(-0.1)
            self.assertTrue(bool(-0.1))
            self.assertTrue(0.1)
            self.assertTrue(bool(0.1))
            self.assertTrue("text")
            self.assertTrue(bool("text"))
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue(bool((1, 2, 3, 'n')))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue(bool([1, 2, 3, 'n']))
            self.assertTrue({1, 2, 3, 'n'})
            self.assertTrue(bool({1, 2, 3, 'n'}))
            self.assertTrue({'key': 'value'})
            self.assertTrue(bool({'key': 'value'}))


    # NOTES

  the test passes

* The `assertTrue method`_ uses an :ref:`if statement<if statements>` to check if what it gets as input is :ref:`False<test_what_is_false>`, this is what the code looks like

  .. code-block:: python

    def assertTrue(self, something, message=None):
        """Check that something is true."""
        if not something:
            raise AssertionError(message)

  here is what happens when the `assertTrue method`_ is called

  - it raises :ref:`AssertionError<what causes AssertionError?>` if ``something`` is :ref:`False<test_what_is_false>`, because ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not bool(something)`` is the same as ``if not something``
  - it returns :ref:`None<what is None?>` if something is :ref:`True<test_what_is_true>` because :ref:`all functions return None by default, as if they have an invisible line that says return None<test_making_a_function_w_return_none>`

  - I do not have to give a value for the ``message`` parameter when I call `assertTrue`_ because

    .. code-block:: python

      self.assertTrue(something)

    is the same as

    .. code-block:: python

      self.assertTrue(something, None)

    is the same as

    .. code-block:: python

      self.assertTrue(
          something=something,
          message=None,
      )

    A :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without the parameter

  `click here to see the actual code for the assertTrue method <https://github.com/python/cpython/blob/2faceeec5c0fb06498a9654d429180ac4610c65a/Lib/unittest/case.py#L756>`_

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_booleans.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``booleans``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

* ``bool(anything)`` returns :green:`True` or :ref:`False<test_what_is_false>`
* ``assertFalse(anything) == assertFalse(bool(anything))``
* ``assertFalse(anything)`` checks if the result of ``bool(anything)`` is :ref:`True<test_what_is_true>` and raises :ref:`AssertionError<what causes AssertionError?>` if it is
* ``assertTrue(anything) == assertTrue(bool(anything))``
* ``assertTrue(anything)`` checks if the result of ``bool(anything)`` is :ref:`False<test_what_is_false>` and it raises :ref:`AssertionError<what causes AssertionError?>` if it is

`you can take a look at the source code here <https://github.com/python/cpython/blob/2faceeec5c0fb06498a9654d429180ac4610c65a/Lib/unittest/case.py#L750>`_

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed for the Truth Table?<truth table: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like to continue testing binary operations?<truth table: Binary Operations 2>`

-----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->