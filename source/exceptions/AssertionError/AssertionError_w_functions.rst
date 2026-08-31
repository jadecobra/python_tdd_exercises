.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

#################################################################################
test AssertionError with functions
#################################################################################

----

I want to use the :ref:`assert_is_equal<extract assert_equal function>` and :ref:`assert_is_none functions<extract assert_is_none function>` in the :ref:`AssertionError project<what is an assertion?>`.

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
  :lines: 73-79

.. literalinclude:: ../../code/assertion_error/test_assertion_error_w_functions.py
  :language: python
  :lineno-start: 82
  :caption: assertion_error/tests/test_assertion_error.py
  :lines: 82-98

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
* I use the :ref:`assert_equal function<extract assert_equal function>` for the :ref:`assertions<what is an assertion?>` in :ref:`test_assert_keyword`

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
* I use the :ref:`assert_equal function<extract assert_equal function>` for three :ref:`assertions<what is an assertion?>` in :ref:`test_assertion_error_w_equality`

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
* I use the :ref:`assert_equal function<extract assert_equal function>` for the second :ref:`assertion<what is an assertion?>` in :ref:`test_assertion_error_w_is_vs_equal`

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
* I add a :ref:`function<what is a function?>` named ``assert_not_equal`` that takes two inputs and :ref:`asserts<what is an assertion?>` that they are NOT equal

  .. code-block:: python
    :emphasize-lines: 1-2

    def assert_not_equal(x, y):
        assert x != y


    def assert_equal(x, y):
        assert x == y


    def test_assert_keyword():

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

I can use :ref:`assertIsNone methods<another way to test if something is None>` and :ref:`assertIsNotNone<another way to test if something is NOT None>` for :ref:`assertions<what is an assertion?>` that test if something is :ref:`None<what is None?>` or not - ``assertIs(x, None)`` and ``assertIsNot(x, None)``.

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
* :ref:`I know how to place values in strings<telephone>`.
* :ref:`I know how to make a person say hello with f-strings<how to make a person with f-strings>`.
* :ref:`I know how to separate tests from solutions<separate and equal>`.
* :ref:`I know what causes AttributeError<what causes AttributeError?>`.
* :ref:`I know how to make a person with a class<how to make a person with a class>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.

:ref:`Would you like to use the assertIsNotNone and assertIsNone methods with the functions project?<test functions with assertIsNotNone and assertIsNone>`

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