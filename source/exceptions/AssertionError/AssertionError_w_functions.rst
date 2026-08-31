.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

#################################################################################
test AssertionError with functions
#################################################################################

----

I want to use the :ref:`assert_is_equal<extract assert_equal function>` and make other :ref:`functions<what is a function?>` like it in the :ref:`AssertionError project<what is an assertion?>`.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_functions.py
  :language: python
  :linenos:
  :caption: assertion_error/tests/test_assertion_error.py
  :lines: 1-10

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_functions.py
  :language: python
  :lineno-start: 13
  :caption: assertion_error/tests/test_assertion_error.py
  :lines: 13-22

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_functions.py
  :language: python
  :lineno-start: 25
  :caption: assertion_error/tests/test_assertion_error.py
  :lines: 25-28

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_functions.py
  :language: python
  :lineno-start: 31
  :caption: assertion_error/tests/test_assertion_error.py
  :lines: 31-42

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_functions.py
  :language: python
  :lineno-start: 45
  :caption: assertion_error/tests/test_assertion_error.py
  :lines: 45-56

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_functions.py
  :language: python
  :lineno-start: 59
  :caption: assertion_error/tests/test_assertion_error.py
  :lines: 59-70

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_functions.py
  :language: python
  :lineno-start: 73
  :caption: assertion_error/tests/test_assertion_error.py
  :lines: 73-80

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_functions.py
  :language: python
  :lineno-start: 83
  :caption: assertion_error/tests/test_assertion_error.py
  :lines: 83-99

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`assertion_error folder<what is an assertion?>` in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

* I open ``test_assertion_error.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows

  .. code-block:: shell

    tests/test_assertion_error.py .......             [100%]

    ================== 7 passed in D.EFs ===================

* I add the :ref:`assert_equal function<extract assert_equal function>` to ``test_assertion_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def assert_equal(x, y):
        assert x == y


    def test_assert_keyword():

* I open another terminal_
* I `change directory`_ to the :ref:`assertion_error folder<what is an assertion?>` in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add assert_equal function'

----

*********************************************************************************
test_assert_keyword with assert_equal
*********************************************************************************

=================================================================================
:RED:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I use the :ref:`assert_equal function<extract assert_equal function>` for the :ref:`assertions<what is an assertion?>` in :ref:`test_assert_keyword`, in ``test_assertion_error.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-3, 5-6, 8-9

    def test_assert_keyword():
        # assert 1 + 1 == 2
        assert_equal(1+1, 3)

        # assert '1' + '1' == '11'
        assert_equal('1'+'1', '2')

        # assert 'I am' + ' alive' == 'I am alive'
        assert_equal('I am'+' alive', 'I am a ghost')


    def test_assertion_error_w_none():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 2 == 3

  .. code-block:: shell

    assert_equal(1+1, 3) -> None
    └── def assert_equal(x, y):
        ├── x = 1 + 1
        │     = 2
        ├── y = 3
        └── assert x == y
            assert 1 == 3

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the expectation from ``3`` to ``2`` to match reality for the first :ref:`assertion<what is an assertion?>` in :ref:`test_assert_keyword`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-4

    def test_assert_keyword():
        # assert 1 + 1 == 2
        # assert_equal(1+1, 3)
        assert_equal(1+1, 2)

        # assert '1' + '1' == '11'
        assert_equal('1'+'1', '2')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert '11' == '2'

  .. code-block:: shell

    assert_equal('1'+'1', '2') -> None
    └── def assert_equal(x, y):
        ├── x = '1' + '1'
        │     = '11'
        ├── y = '2'
        └── assert x    == y
            assert '11' == '2'

* I change the expectation from ``'2'`` to ``'11'`` to match reality for the second :ref:`assertion<what is an assertion?>` in :ref:`test_assert_keyword`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2-3

        # assert '1' + '1' == '11'
        # assert_equal('1'+'1', '2')
        assert_equal('1'+'1', '11')

        # assert 'I am' + ' alive' == 'I am alive'
        assert_equal('I am'+' alive', 'I am a ghost')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'I am alive' == 'I am a ghost'

  .. code-block:: shell

    assert_equal('I am'+' alive', 'I am a ghost') -> None
    └── def assert_equal(x, y):
        ├── x = 'I am' + ' alive'
        │     = 'I am alive'
        ├── y = 'I am a ghost'
        └── assert x            == y
            assert 'I am alive' == 'I am a ghost'

* I change the expectation from ``'I am a ghost'`` to ``'I am alive'`` for the third :ref:`assertion<what is an assertion?>` in :ref:`test_assert_keyword`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2-3

        # assert 'I am' + ' alive' == 'I am alive'
        # assert_equal('I am'+' alive', 'I am a ghost')
        assert_equal('I am'+' alive', 'I am alive')


    def test_assertion_error_w_none():

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_assert_keyword`

  .. code-block:: python
    :lineno-start: 5

    def test_assert_keyword():
        assert_equal(1+1, 2)
        assert_equal('1'+'1', '11')
        assert_equal('I am'+' alive', 'I am alive')


    def test_assertion_error_w_none():

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'test_assert_keyword with assert_equal'

----

*********************************************************************************
test_assertion_error_w_equality with assert_equal
*********************************************************************************

=================================================================================
:RED:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I use the :ref:`assert_equal function<extract assert_equal function>` for three :ref:`assertions<what is an assertion?>` in :ref:`test_assertion_error_w_equality`, in ``test_assertion_error.py``

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2-3, 9-10, 14-15

      def test_assertion_error_w_equality():
          # assert None == None
          assert_equal(False, None)

          assert False != None

          assert False != True

          # assert False == False
          assert_equal(True, False)

          assert True != None

          # assert True == True
          assert_equal(False, True)


      def test_assertion_error_w_is_vs_equal():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert False == None

  .. code-block:: shell

    assert_equal(False, None) -> None
    └── def assert_equal(x, y):
        ├── x = False
        ├── y = None
        └── assert x     == y
            assert False == None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`False<test_what_is_false>` to :ref:`None<what is None?>` in the first :ref:`assertion<what is an assertion?>` of :ref:`test_assertion_error_w_equality`

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 3-4

    def test_assertion_error_w_equality():
        # assert None == None
        # assert_equal(False, None)
        assert_equal(None, None)

        assert False != None

        assert False != True

        # assert False == False
        assert_equal(True, False)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert True == False

  .. code-block:: shell

    assert_equal(True, False) -> None
    └── def assert_equal(x, y):
        ├── x = True
        ├── y = False
        └── assert x   == y
            assert True == False

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the fourth :ref:`assertion<what is an assertion?>` of :ref:`test_assertion_error_w_equality`

  .. code-block:: python
    :lineno-start:86
    :emphasize-lines: 2-3

        # assert False == False
        # assert_equal(True, False)
        assert_equal(False, False)

        assert True != None

        # assert True == True
        assert_equal(False, True)


    def test_assertion_error_w_is_vs_equal():

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: python

    E       assert False == True

  .. code-block:: shell

    assert_equal(False, True) -> None
    └── def assert_equal(x, y):
        ├── x = False
        ├── y = True
        └── assert x     == y
            assert False == True

* I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the last :ref:`assertion<what is an assertion?>` of :ref:`test_assertion_error_w_equality`

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 2-3

        # assert True == True
        # assert_equal(False, True)
        assert_equal(True, True)


    def test_assertion_error_w_is_vs_equal():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_assertion_error_w_equality` since they are now repetitions

  .. code-block:: python
    :lineno-start: 778
    :emphasize-lines: 3-4, 7-7

    def test_assertion_error_w_equality():
        assert_equal(None, None)
        assert_equal(False, False)
        assert_equal(True, True)

        assert False != None
        assert False != True
        assert True != None



    def test_assertion_error_w_is_vs_equal():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'test_assertion_error_w_equality with assert_equal'

----

*********************************************************************************
test_assertion_error_w_is_vs_equal with assert_equal
*********************************************************************************

=================================================================================
:RED:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I use the :ref:`assert_equal function<extract assert_equal function>` for the second :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_is_vs_equal`, in ``test_assertion_error.py``

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 4-5

      def test_assertion_error_w_is_vs_equal():
          assert 0 is not 0.0

          # assert 0 == 0.0
          assert_equal(1, 0.0)


      def will_not_run():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 1 == 0.0

  .. code-block:: shell

    assert_equal(1, 0.0) -> None
    └── def assert_equal(x, y):
        ├── x = 1
        ├── y = 0.0
        └── assert x == y
            assert 1 == 0.0

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`False<test_what_is_false>` to :ref:`None<what is None?>` in the second :ref:`assertion<what is an assertion?>` of :ref:`test_assertion_error_w_is_vs_equal`

.. code-block:: python
  :lineno-start: 87
  :emphasize-lines: 5-6

  def test_assertion_error_w_is_vs_equal():
      assert 0 is not 0.0

      # assert 0 == 0.0
      # assert_equal(1, 0.0)
      assert_equal(0, 0.0)


  def will_not_run():

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line from :ref:`test_assertion_error_w_is_vs_equal`

  .. code-block:: python
    :lineno-start: 87

    def test_assertion_error_w_is_vs_equal():
        assert 0 is not 0.0
        assert_equal(0, 0.0)


    def will_not_run():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'test_assertion_error_w_is_vs_equal with assert_equal'

----

*********************************************************************************
extract assert_not_equal function
*********************************************************************************

The remaining :ref:`assertions<what is an assertion?>` in :ref:`test_assertion_error_w_equality` and  :ref:`assertion<what is an assertion?>` in :ref:`test_failure` are the same, they check if something is not equal to something else.

.. code-block:: python

  assert something != something_else

I can use a :ref:`function<what is a function?>` to :ref:`assert<what is an assertion?>` if two things are NOT equal.

----

=================================================================================
:RED:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a :ref:`function<what is a function?>` named ``assert_not_equal`` that takes two inputs and :ref:`asserts<what is an assertion?>` that they are NOT equal, in ``test_assertion_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def assert_not_equal(x, y):
        assert x != y


    def assert_equal(x, y):

* I use the new :ref:`function<what is a function?>` for the remaining :ref:`assertions<what is an assertion?>` in :ref:`test_assertion_error_w_equality`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 6-11

    def test_assertion_error_w_equality():
        assert_equal(None, None)
        assert_equal(False, False)
        assert_equal(True, True)

        # assert False != None
        assert_not_equal(None, None)
        # assert False != True
        assert_not_equal(True, True)
        # assert True != None
        assert_not_equal(None, None)


    def test_assertion_error_w_is_vs_equal():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None != None

  .. code-block:: shell

    assert_not_equal(None, None) -> None
    └── def assert_not_equal(x, y):
        ├── x = None
        ├── y = None
        └── assert x    != y
            assert None != None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the first :ref:`None<what is None?>` in the parentheses to :ref:`False<test_what_is_false>` for the first :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_equality`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 2-3

        # assert False != None
        # assert_not_equal(None, None)
        assert_not_equal(False, None)
        # assert False != True
        assert_not_equal(True, True)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`\

  .. code-block:: python

    E       assert True != True

  .. code-block:: shell

    assert_not_equal(True, True) -> None
    └── def assert_not_equal(x, y):
        ├── x = True
        ├── y = True
        └── assert x    != y
            assert True != True

* I change the first :ref:`True<test_what_is_true>` in the parentheses to :ref:`False<test_what_is_false>` for the second :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_equality`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 2-3

        # assert False != True
        # assert_not_equal(True, True)
        assert_not_equal(False, True)
        # assert True != None
        assert_not_equal(None, None)


    def test_assertion_error_w_is_vs_equal():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None != None

* I change the first :ref:`None<what is None?>` in the parentheses to :ref:`True<test_what_is_true>` for the third :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_equality`

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 2-3

        # assert True != None
        # assert_not_equal(None, None)
        assert_not_equal(True, None)


    def test_assertion_error_w_is_vs_equal():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_assertion_error_w_equality`

  .. code-block:: python
    :lineno-start: 81

    def test_assertion_error_w_equality():
        assert_equal(None, None)
        assert_equal(False, False)
        assert_equal(True, True)

        assert_not_equal(False, None)
        assert_not_equal(False, True)
        assert_not_equal(True, None)


    def test_assertion_error_w_is_vs_equal():

* I use the :ref:`assert_not_equal function<extract assert_not_equal function>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_failure<pytest only calls the function if the name starts with test>`

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 3-4

    def test_failure():
        # assert False == True
        # assert False != True
        assert_not_equal(True, True)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert True != True

* I change the first :ref:`True<test_what_is_true>` in the parentheses of the :ref:`assertion<what is an assertion?>` to :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 4-5

    def test_failure():
        # assert False == True
        # assert False != True
        # assert_not_equal(True, True)
        assert_not_equal(False, True)


    # NOTES

  the test passes.

* I remove the commented lines from :ref:`test_failure<pytest only calls the function if the name starts with test>`

  .. code-block:: python
    :lineno-start: 102

    def test_failure():
        # assert False == True
        assert_not_equal(False, True)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract assert_not_equal function'

----

*********************************************************************************
extract assert_is_not function
*********************************************************************************

The other :ref:`assertions<what is an assertion?>` in ``test_assertion_error.py`` are the same, they check if something is NOT the same :ref:`object<everything is an object>` as something else

.. code-block:: python

  assert something is not something_else

three of the :ref:`assertions<what is an assertion?>` are the same, they check if something is the same :ref:`object<everything is an object>` as something else

.. code-block:: python

  assert something is something_else

I can use a :ref:`function<what is a function?>` to :ref:`assert<what is an assertion?>` if one :ref:`object<everything is an object>` is NOT the same :ref:`object<everything is an object>` as another.

----

=================================================================================
:RED:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a :ref:`function<what is a function?>` named ``assert_is_not`` that takes two inputs and :ref:`asserts<what is an assertion?>`  that they are not the same :ref:`object<everything is an object>`, in ``test_assertion_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def assert_is_not(x, y):
        assert x is not y


    def assert_not_equal(x, y):

* I use the :ref:`assert_is_not function<extract assert_is_not function>` for the :ref:`assertions<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4-5, 7-8, 10-11

    def test_assertion_error_w_none():
        assert None is None

        # assert False is not None
        assert_is_not(None, None)

        # assert True is not None
        assert_is_not(None, None)

        # assert 0 is not None
        assert_is_not(None, None)

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 1-2, 4-5, 7-8

        # assert 0.0 is not None
        assert_is_not(None, None)

        # assert '' is not None
        assert_is_not(None, None)

        # assert () is not None
        assert_is_not(None, None)

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 1-2, 4-5, 7-8

        # assert [] is not None
        assert_is_not(None, None)

        # assert set() is not None
        assert_is_not(None, None)

        # assert {} is not None
        assert_is_not(None, None)


    def test_assertion_error_w_false():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is not None

  .. code-block:: shell

    assert_is_not(None, None) -> None
    └── def assert_is_not(x, y):
        ├── x = None
        ├── y = None
        └── assert x    is not y
            assert None is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the first :ref:`None<what is None?>` in the parentheses to :ref:`False<test_what_is_false>` for the second :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5-6

    def test_assertion_error_w_none():
        assert None is None

        # assert False is not None
        # assert_is_not(None, None)
        assert_is_not(False, None)

        # assert True is not None
        assert_is_not(None, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is not None

* I change the first :ref:`None<what is None?>` in the parentheses to :ref:`True<test_what_is_true>` for the third :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2-3

        # assert True is not None
        # assert_is_not(None, None)
        assert_is_not(True, None)

        # assert 0 is not None
        assert_is_not(None, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is not None

* I change the first :ref:`None<what is None?>` in the parentheses to ``0`` for the fourth :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2-3

        # assert 0 is not None
        # assert_is_not(None, None)
        assert_is_not(0, None)

        # assert 0.0 is not None
        assert_is_not(None, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is not None

* I change the first :ref:`None<what is None?>` in the parentheses to ``0.0`` for the fifth :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2-3

        # assert 0.0 is not None
        # assert_is_not(None, None)
        assert_is_not(0.0, None)

        # assert '' is not None
        assert_is_not(None, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is not None

* I change the first :ref:`None<what is None?>` in the parentheses to ``''`` for the sixth :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2-3

        # assert '' is not None
        # assert_is_not(None, None)
        assert_is_not('', None)

        # assert () is not None
        assert_is_not(None, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is not None

* I change the first :ref:`None<what is None?>` in the parentheses to ``()`` for the seventh :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2-3

        # assert () is not None
        # assert_is_not(None, None)
        assert_is_not((), None)

        # assert [] is not None
        assert_is_not(None, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is not None

* I change the first :ref:`None<what is None?>` in the parentheses to ``[]`` for the eighth :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 2-3

        # assert [] is not None
        # assert_is_not(None, None)
        assert_is_not([], None)

        # assert set() is not None
        assert_is_not(None, None)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is not None

* I change the first :ref:`None<what is None?>` in the parentheses to ``[]`` for the ninth :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 2-3

        # assert set() is not None
        # assert_is_not(None, None)
        assert_is_not(set(), None)

        # assert {} is not None
        assert_is_not(None, None)


    def test_assertion_error_w_false():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is not None

* I change the first :ref:`None<what is None?>` in the parentheses to ``{}`` for the tenth :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 2-3

        # assert {} is not None
        # assert_is_not(None, None)
        assert_is_not({}, None)


    def test_assertion_error_w_false():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is not None

  the test passes.

* I use the :ref:`assert_is_not function<extract assert_is_not function>` for the first :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_is_vs_equal`

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 2-3

    def test_assertion_error_w_is_vs_equal():
        # assert 0 is not 0.0
        assert_is_not(0.0, 0.0)
        assert_equal(0, 0.0)


    def will_not_run():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0.0 is not 0.0

  .. code-block:: shell

    assert_is_not(0.0, 0.0) -> None
    └── def assert_is_not(x, y):
        ├── x = 0.0
        ├── y = 0.0
        └── assert x   is not y
            assert 0.0 is not 0.0

* I change the first ``0.0`` to ``0`` in the parentheses

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 3-4

    def test_assertion_error_w_is_vs_equal():
        # assert 0 is not 0.0
        # assert_is_not(0.0, 0.0)
        assert_is_not(0, 0.0)
        assert_equal(0, 0.0)


    def will_not_run():

  the test passes.

* I remove the commented lines from :ref:`test_assertion_error_w_is_vs_equal`

  .. code-block:: python
    :lineno-start: 113

    def test_assertion_error_w_is_vs_equal():
        assert_is_not(0, 0.0)
        assert_equal(0, 0.0)


    def will_not_run():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract assert_is_not function'

----

*********************************************************************************
extract assert_is_not_none function
*********************************************************************************

All the :ref:`assertions<what is an assertion?>` in :ref:`test_assertion_error_w_none` except the first one, use the :ref:`assert_is_not function<extract assert_is_not function>` to :ref:`assert<what is an assertion?>` that something is NOT the same :ref:`object<everything is an object>` as :ref:`None<what is None?>`

.. code-block:: python

  assert something is not None

I can use a :ref:`function<what is a function?>` to remove repetition of :ref:`None<what is None?>` from the :ref:`call<how to call a function with input>` to the :ref:`assert_is_not function<extract assert_is_not function>` to :ref:`assert<what is an assertion?>` that something is NOT the same :ref:`object<everything is an object>` as :ref:`None<what is None?>`.

----

=================================================================================
:RED:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a :ref:`function<what is a function?>` named ``assert_is_not_none`` that takes one input and :ref:`calls the assert_is_not function<extract assert_is_not function>` to :ref:`assert<what is an assertion?>` that the input is NOT the same :ref:`object<everything is an object>` as :ref:`None<what is None?>`, in ``test_assertion_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def assert_is_not(x, y):
        assert x is not y


    def assert_is_not_none(x):
        assert_is_not(x, None)


    def assert_not_equal(x, y):

* I use the :ref:`assert_is_not_none function<extract assert_is_not_none function>` for the second :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6-7

    def test_assertion_error_w_none():
        assert None is None

        # assert False is not None
        # assert_is_not(None, None)
        # assert_is_not(False, None)
        assert_is_not_none(None)

        # assert True is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is not None

  .. code-block:: shell

    assert_is_not_none(None) -> None
    └── def assert_is_not_none(x):
        ├── x = None
        └── assert_is_not(x, None)
            └── def assert_is_not(x, y):
                ├── x = None
                ├── y = None
                └── assert x    is not y
                    assert None is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`None<what is None?>` to :ref:`False<test_what_is_false>` for the second :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_none`

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 7-8

    def test_assertion_error_w_none():
        assert None is None

        # assert False is not None
        # assert_is_not(None, None)
        # assert_is_not(False, None)
        # assert_is_not_none(None)
        assert_is_not_none(False)

        # assert True is not None

the test passes.

.. code-block:: shell

  assert_is_not_none(False) -> None
  └── def assert_is_not_none(x):
      ├── x = False
      └── assert_is_not(x, None)
          └── def assert_is_not(x, y):
              ├── x = False
              ├── y = None
              └── assert x     is not y
                  assert False is not None

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use the :ref:`assert_is_not_none function<extract assert_is_not_none function>` for the remaining :ref:`assertions<what is an assertion?>` in :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 3-4, 8-9, 13-14

        # assert True is not None
        # assert_is_not(None, None)
        # assert_is_not(True, None)
        assert_is_not_none(True)

        # assert 0 is not None
        # assert_is_not(None, None)
        # assert_is_not(0, None)
        assert_is_not_none(0)

        # assert 0.0 is not None
        # assert_is_not(None, None)
        # assert_is_not(0.0, None)
        assert_is_not_none(0.0)

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 3-4, 8-9, 13-14

        # assert '' is not None
        # assert_is_not(None, None)
        # assert_is_not('', None)
        assert_is_not_none('')

        # assert () is not None
        # assert_is_not(None, None)
        # assert_is_not((), None)
        assert_is_not_none(())

        # assert [] is not None
        # assert_is_not(None, None)
        # assert_is_not([], None)
        assert_is_not_none([])

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3-4, 8-9

        # assert set() is not None
        # assert_is_not(None, None)
        # assert_is_not(set(), None)
        assert_is_not_none(set())

        # assert {} is not None
        # assert_is_not(None, None)
        # assert_is_not({}, None)
        assert_is_not_none({})


    def test_assertion_error_w_false():

  the test is still green.

* I remove the commented lines from :ref:`test_assertion_error_w_none`

  .. code-block:: python
    :lineno-start: 23

    def test_assertion_error_w_none():
        assert None is None

        assert_is_not_none(False)
        assert_is_not_none(True)
        assert_is_not_none(0)
        assert_is_not_none(0.0)
        assert_is_not_none('')
        assert_is_not_none(())
        assert_is_not_none([])
        assert_is_not_none(set())
        assert_is_not_none({})


    def test_assertion_error_w_false():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract assert_is_not_none function'

----

*********************************************************************************
extract assert_is_not_false function
*********************************************************************************

The :ref:`assertions<what is an assertion?>` in :ref:`test_assertion_error_w_false` except ``assert False is False`` are the same, they check if something is NOT the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>`

.. code-block:: python

  assert something is not False

I can use a :ref:`function<what is a function?>` to :ref:`assert<what is an assertion?>` that something is NOT the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>`.

----

=================================================================================
:RED:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a :ref:`function<what is a function?>` named ``assert_is_not_false`` that takes one input and :ref:`calls the assert_is_not function<extract assert_is_not function>` to :ref:`assert<what is an assertion?>` that the input is NOT the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>`, in ``test_assertion_error.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def assert_is_not_none(x):
        assert_is_not(x, None)


    def assert_is_not_false(x):
        assert_is_not(x, False)


    def assert_not_equal(x, y):

* I use the :ref:`assert_is_not_false function<extract assert_is_not_false function>` for the first :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2-3

    def test_assertion_error_w_false():
        # assert None is not False
        assert_is_not_false(False)

        assert False is False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert False is not False

  .. code-block:: shell

    assert_is_not_false(False) -> None
    └── def assert_is_not_false(x):
        ├── x = False
        └── assert_is_not(x, False)
            └── def assert_is_not(x, y):
                ├── x = False
                ├── y = False
                └── assert x     is not y
                    assert False is not False

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`False<test_what_is_false>` to :ref:`None<what is None?>` for the first :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_false`

.. code-block:: python
  :lineno-start: 41
  :emphasize-lines: 3-4

  def test_assertion_error_w_false():
      # assert None is not False
      # assert_is_not_false(False)
      assert_is_not_false(None)

      assert False is False

the test passes.

.. code-block:: shell

  assert_is_not_false(None) -> None
  └── def assert_is_not_false(x):
      ├── x = None
      └── assert_is_not(x, False)
          └── def assert_is_not(x, y):
              ├── x = None
              ├── y = False
              └── assert x    is not y
                  assert None is not False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use the :ref:`assert_is_not_false function<extract assert_is_not_false function>` for the remaining :ref:`assertions<what is an assertion?>` in :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3-4, 6-7, 9-10

        assert False is False

        # assert True is not False
        assert_is_not_false(True)

        # assert 0 is not False
        assert_is_not_false(0)

        # assert 0.0 is not False
        assert_is_not_false(0.0)

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 1-2, 4-5, 7-8

        # assert '' is not False
        assert_is_not_false('')

        # assert () is not False
        assert_is_not_false(())

        # assert [] is not False
        assert_is_not_false([])

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 1-2, 4-5

        # assert set() is not False
        assert_is_not_false(set())

        # assert {} is not False
        assert_is_not_false({})


    def test_assertion_error_w_true():

  the test is still green.

* I remove the commented lines from :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2, 4

    def test_assertion_error_w_false():
        assert False is False

        assert_is_not_false(None)
        assert_is_not_false(True)
        assert_is_not_false(0)
        assert_is_not_false(0.0)
        assert_is_not_false('')
        assert_is_not_false(())
        assert_is_not_false([])
        assert_is_not_false(set())
        assert_is_not_false({})


    def test_assertion_error_w_true():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract assert_is_not_false function'

----

*********************************************************************************
extract assert_is_not_true function
*********************************************************************************

The :ref:`assertions<what is an assertion?>` in :ref:`test_assertion_error_w_true` except ``assert True is True`` are the same, they check if something is NOT the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`

.. code-block:: python

  assert something is not True

I can use a :ref:`function<what is a function?>` to :ref:`assert<what is an assertion?>` that something is NOT the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`.

----

=================================================================================
:RED:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a :ref:`function<what is a function?>` named ``assert_is_not_true`` that takes one input and :ref:`calls the assert_is_not function<extract assert_is_not function>` to :ref:`assert<what is an assertion?>` that the input is NOT the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`, in ``test_assertion_error.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def assert_is_not_false(x):
        assert_is_not(x, False)


    def assert_is_not_true(x):
        assert_is_not(x, True)


    def assert_not_equal(x, y):

* I use the :ref:`assert_is_not_true function<extract assert_is_not_true function>` for the first :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 2-3

    def test_assertion_error_w_true():
        # assert None is not True
        assert_is_not_true(True)

        assert False is not True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert True is not True

  .. code-block:: shell

    assert_is_not_true(True) -> None
    └── def assert_is_not_true(x):
        ├── x = True
        └── assert_is_not(x, True)
            └── def assert_is_not(x, y):
                ├── x = True
                ├── y = True
                └── assert x    is not y
                    assert True is not True

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`True<test_what_is_true>` to :ref:`None<what is None?>` for the first :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_true`

.. code-block:: python
  :lineno-start: 59
  :emphasize-lines: 3-4

  def test_assertion_error_w_true():
      # assert None is not True
      # assert_is_not_true(True)
      assert_is_not_true(None)

      assert False is not True

the test passes.

.. code-block:: shell

  assert_is_not_true(None) -> None
  └── def assert_is_not_true(x):
      ├── x = None
      └── assert_is_not(x, True)
          └── def assert_is_not(x, y):
              ├── x = None
              ├── y = True
              └── assert x    is not y
                  assert None is not True

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use the :ref:`assert_is_not_true function<extract assert_is_not_true function>` for the remaining :ref:`assertions<what is an assertion?>` in :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 1-2, 6-7

        # assert False is not True
        assert_is_not_true(False)

        assert True is True

        # assert 0 is not True
        assert_is_not_true(0)

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 1-2, 4-5, 7-8

        # assert 0.0 is not True
        assert_is_not_true(0.0)

        # assert '' is not True
        assert_is_not_true('')

        # assert () is not True
        assert_is_not_true(())

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 1-2, 4-5, 7-8

        # assert [] is not True
        assert_is_not_true([])

        # assert set() is not True
        assert_is_not_true(set())

        # assert {} is not True
        assert_is_not_true({})


    def test_assertion_error_w_equality():

  the test is still green.

* I remove the commented lines from :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 2

    def test_assertion_error_w_true():
        assert True is True

        assert_is_not_true(None)
        assert_is_not_true(False)
        assert_is_not_true(0)
        assert_is_not_true(0.0)
        assert_is_not_true('')
        assert_is_not_true(())
        assert_is_not_true([])
        assert_is_not_true(set())
        assert_is_not_true({})


    def test_assertion_error_w_equality():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract assert_is_not_true function'

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

I can use :ref:`functions<what is a function?>` to make :ref:`assertions<what is an assertion?>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test AssertionError with assertIsNotNone and assertIsNone: tests>`

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

:ref:`Would you like to test using a function to make a string from input?<telephone>`

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