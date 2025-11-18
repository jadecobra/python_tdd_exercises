.. meta::
  :description: Master Python's AssertionError for robust testing. Learn to use assert for debugging, handle exceptions, and see practical unittest examples. Watch the tutorial!
  :keywords: Jacob Itegboje, python AssertionError example, how to handle AssertionError in Python, python unittest assert examples, python assert for debugging, python assert best practices, python custom AssertionError message, python testing with pytest and assert

.. include:: ../links.rst

.. _AssertionError: https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError

#################################################################################
AssertionError
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/jxbttz7R0ho?si=Oiv1Y0WPwQhlw5i9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

AssertionError_ happens when a statement is :ref:`False<test_what_is_false>`. It was in :ref:`how to make a python test driven development environment` with :ref:`the first failing test<test_failure>`

.. code-block:: python

  self.assertFalse(True)

which is like an `assert statement`_

.. code-block:: python

  assert True is False

I think of the statement as "DO NOT CONTINUE, UNLESS :ref:`True<test_what_is_true>` is :ref:`False<test_what_is_false>`". The line stops the program_ because the statement is NOT :ref:`True<test_what_is_true>`, it is :ref:`False<test_what_is_false>`

I can use assertions_ when making a program_ to make sure something is :ref:`True<test_what_is_true>` before it continues. I can also use them to test how the program_ behaves, for example when it is given inputs.

Assertions_ can help catch things that break passing tests when I add new lines. They also help me answer 2 questions

* what is the same?
* what is different?

The difference between my expectations and reality (what happens when the program_ runs), tells me what to change to make them match.

----

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``assertion_error`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh assertion_error

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 assertion_error

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_assertion_error.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_assertion_error.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change ``True`` to ``False`` to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestAssertionError(unittest.TestCase):

*********************************************************************************
test_assertion_error_w_none
*********************************************************************************

red: make it fail
#################################################################################

* I change ``test_failure`` to ``test_assertion_error_w_none``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    import unittest


    class TestAssertionError(unittest.TestCase):

        def test_assertion_error_w_none(self):
            assert None is not None


    # Exceptions Encountered
    ...

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert None is not None

    tests/test_assertion_error.py:7: AssertionError

  the `assert statement`_ is :ref:`False<test_what_is_false>`, :ref:`None` is :ref:`None`

green: make it pass
#################################################################################

I change the line to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 2

      def test_assertion_error_w_none(self):
          assert None is None

the test passes

refactor: make it better
#################################################################################

I can also make assertions_ with some :ref:`methods<functions>` from the `unittest.TestCase`_ :ref:`class<classes>`

how to test if something is None
--------------------------------------------------------------------------------------------

* I add another failing line with the assertIsNotNone_ :ref:`method<functions>` which checks if the thing in parentheses (``()``) is NOT :ref:`None`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNotNone(None)

  the terminal_ shows a more descriptive message for the AssertionError_

  .. code-block:: python

    AssertionError: unexpectedly None

  I change the statement to use the assertIsNone_ :ref:`method<functions>` which checks if the thing in parentheses is :ref:`None`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

  the test passes

* I add a note

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1-2

    # NOTES
    # None is None


    # Exceptions Encountered
    # AssertionError

* I add a new :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is None

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert False is None

  I change the line to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1

            assert False is not None

  the test passes

* I add another line with assertIsNone_

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2

            assert False is not None
            self.assertIsNone(False)

  the terminal_ shows AssertionError_

  .. code-block:: python

    AssertionError: False is not None

  I use assertIsNotNone_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertIsNotNone(False)

  the test passes

* I add another note

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

    # NOTES
    # False is not None
    # None is None

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 4

            assert False is not None
            self.assertIsNotNone(False)

            assert True is None


    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert True is None

  I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 1

            assert True is not None

  the test passes

* I add a failing line with assertIsNone_

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNone(True)

  the terminal_ shows AssertionError_

  .. code-block:: python

    AssertionError: True is not None

  I make the statement :ref:`True<test_what_is_true>` with assertIsNotNone_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 9

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNotNone(True)


    # NOTES

  the test passes

* I add a note

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

    # NOTES
    # True is not None
    # False is not None
    # None is None

----

*********************************************************************************
test_assertion_error_w_false
*********************************************************************************

I can use assertions_ to test if something is :ref:`False<test_what_is_false>`

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 4-5

          assert True is not None
          self.assertIsNotNone(True)

      def test_assertion_error_w_false(self):
          assert True is False

  # NOTES

the terminal_ shows AssertionError_

.. code-block:: python

  E    assert True is False

green: make it pass
#################################################################################

I change the line to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 1

          assert True is not False

the test passes

refactor: make it better
#################################################################################

There is an assert_ :ref:`method<functions>` to check if something is :ref:`False<test_what_is_false>`, it is the one from :ref:`the first failing test<test_failure>`

how to test if something is False
--------------------------------------------------------------------------------------------

* I add a failing line with assertFalse_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3

        def test_assertion_error_w_false(self):
            assert True is not False
            self.assertFalse(True)

  the terminal_ shows AssertionError_

  .. code-block:: python

    AssertionError: True is not false

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3

        def test_assertion_error_w_false(self):
            assert True is not False
            self.assertFalse(False)

  the test passes

* I add notes

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-3

    # NOTES
    # False is False
    # True is not False
    # True is not None
    # False is not None
    # None is None

----

*********************************************************************************
test_assertion_error_w_true
*********************************************************************************

I can also use assertions_ to test if something is :ref:`True<test_what_is_true>`

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python
  :lineno-start: 18
  :emphasize-lines: 4

          self.assertFalse(False)

      def test_assertion_error_w_true(self):
          assert False is True


  # NOTES

the terminal_ shows AssertionError_

.. code-block:: python

  E    assert False is True

green: make it pass
#################################################################################

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 21
  :emphasize-lines: 1

          assert False is not True

the test passes

refactor: make it better
#################################################################################

There is an assert_ :ref:`method<functions>` to check if something is :ref:`True<test_what_is_true>`

how to test if something is True
--------------------------------------------------------------------------------------------

* I add a failing statement

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

            assert False is not True
            self.assertTrue(False)

  the terminal_ shows AssertionError_

  .. code-block:: python

    AssertionError: False is not true

* I change the failing line to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 3

        def test_assertion_error_w_true(self):
            assert False is not True
            self.assertTrue(True)


    # NOTES

  the test passes

* I add more notes

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2-3

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False
    # True is not None
    # False is not None
    # None is None

All the statements so far show that - :ref:`True<test_what_is_true>`, :ref:`False<test_what_is_false>` and :ref:`None` are different. They give me a basic expectation of Python_ because I can compare things with them.

----

*********************************************************************************
test_assertion_error_w_equality
*********************************************************************************

I can use assertions to test if 2 things are equal

red: make it fail
#################################################################################

I add a new failing test

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 3-4

          self.assertTrue(True)

      def test_assertion_error_w_equality(self):
          assert None != None


  # NOTES

the terminal_ shows AssertionError_

.. code-block:: python

  E    assert None != None

``!=`` is the symbol for ``NOT equal`` which makes this statement read as ``assert None is NOT equal to None``

green: make it pass
#################################################################################

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 24
  :emphasize-lines: 2

      def test_assertion_error_w_equality(self):
          assert None == None

the test passes.

``==`` is the symbol for ``is equal`` which makes this statement read as ``assert None is equal to None``

``=`` is the symbol for assignment, it's how to give a name to something in Python_

refactor: make it better
#################################################################################

There are assert_ :ref:`methods<functions>` to check if 2 things are equal or not.


how to test if two things are Equal
--------------------------------------------------------------------------------------------

* I add assertNotEqual_ which checks if the 2 things in the parentheses are NOT equal

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 3

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertNotEqual(None, None)

  the terminal_ shows AssertionError_

  .. code-block:: python

    AssertionError: None == None

  I change the :ref:`assertion<AssertionError>` to use the assertEqual_ :ref:`method<functions>` which checks if the 2 things in the parentheses are equal

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 1

            self.assertEqual(None, None)

  the test passes

* I add to the notes

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 8

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False
    # True is not None
    # False is not None
    # None is None and equal to None

* I add a new failing :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 5

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False == None


    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert False == None

  I change the line to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1

            assert False != None

  the test passes

* I add a failing line with assertEqual_

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 2

            assert False != None
            self.assertEqual(False, None)

  the terminal_ shows AssertionError_

  .. code-block:: python

    AssertionError: False != None

  I make the line :ref:`True<test_what_is_true>` with assertNotEqual_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 1

            self.assertNotEqual(False, None)

  the test passes

* I add to the notes

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 7

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False
    # True is not None
    # False is not None and not equal to None
    # None is None and equal to None

* I add the next failing :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 4

            assert False != None
            self.assertNotEqual(False, None)

            assert True == None

    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert True == None

  I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 1

            assert True != None

  the test passes

* I add a failing line with assertEqual_

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2

            assert True != None
            self.assertEqual(True, None)

  the terminal_ shows AssertionError_

  .. code-block:: python

    AssertionError: True != None

  I make the line :ref:`True<test_what_is_true>` with assertNotEqual_

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 1

            self.assertNotEqual(True, None)

  the test passes

* I add a note

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 6

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None

* I add another failing :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 4

            assert True != None
            self.assertNotEqual(True, None)

            assert True == False


    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert True == False

  I change the line to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1

            assert True != False

  the test passes

* I add a failing line with assertEqual_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2

            assert True != False
            self.assertEqual(True, False)

  the terminal_ shows AssertionError_

  .. code-block:: python

    AssertionError: True != False

  I change the assert_ :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2

            assert True != False
            self.assertNotEqual(True, False)

  the test passes

* I add a note

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 5

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False and not equal to False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None

* on to the next failing :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 4

            assert True != False
            self.assertNotEqual(True, False)

            assert False != False


    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert False != False

  I make the line :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

            assert False == False

  the test passes

* I add another failing line with assertNotEqual_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

            assert False == False
            self.assertNotEqual(False, False)

  the terminal_ shows AssertionError_

  .. code-block:: python

    AssertionError: False == False

  I change the line to use assertEqual_

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 1

            self.assertEqual(False, False)

  the test passes

* I add a note

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 4

    # NOTES
    # True is True
    # False is not True
    # False is False and equal to False
    # True is not False and not equal to False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None

* I add a failing :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4

            assert False == False
            self.assertEqual(False, False)

            assert False == True


    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert False == True

  I change the line to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 1

            assert False != True

  the test passes

* I add a failing line with assertEqual_

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 2

            assert False != True
            self.assertEqual(False, True)

  the terminal_ shows AssertionError_

  .. code-block:: python

    AssertionError: False != True

  I make the line :ref:`True<test_what_is_true>` with assertNotEqual_

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 2

            assert False != True
            self.assertNotEqual(False, True)

  the test passes

* I add another note

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 3

    # NOTES
    # True is True
    # False is not True and not equal to True
    # False is False and equal to False
    # True is not False and not equal to False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None

* time for the last statements

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 4

            assert False != True
            self.assertNotEqual(False, True)

            assert True != True


    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert True != True

  I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 1

              assert True == True

  the test passes

* I add a failing line with the assertNotEqual_ :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2

              assert True == True
              self.assertNotEqual(True, True)

  the terminal_ shows AssertionError_

  .. code-block:: python

    AssertionError: True == True

  I change the :ref:`method<functions>` to assertEqual_

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 21

          def test_assertion_error_w_equality(self):
              assert None == None
              self.assertEqual(None, None)

              assert False != None
              self.assertNotEqual(False, None)

              assert True != None
              self.assertNotEqual(True, None)

              assert True != False
              self.assertNotEqual(True, False)

              assert False == False
              self.assertEqual(False, False)

              assert False != True
              self.assertNotEqual(False, True)

              assert True == True
              self.assertEqual(True, True)


    # NOTES

  and all the tests are passing!

* I add a note for the last statement

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2

    # NOTES
    # True is True and equal to True
    # False is not True and not equal to True
    # False is False and equal to False
    # True is not False and not equal to False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None

----


*********************************************************************************
review
*********************************************************************************

I can use `assert statements`_ and :ref:`methods<functions>` to test if something is

* :ref:`None` or not
* :ref:`False<test_what_is_false>` or not
* :ref:`True<test_what_is_true>` or not
* :ref:`equal or not<test_assertion_error_w_equality>`

Here are questions you can answer after going through this chapter

:ref:`How can I test if something is None?<how to test if something is None>`
:ref:`How can I test if something is False?<how to test if something is False>`
:ref:`How can I test if something is True?<how to test if something is True>`
:ref:`How can I test if 2 things are Equal?<how to test if two things are Equal>`

Would you like to :ref:`test None?<None>`

----

:ref:`Click here for all the tests from this chapter<AssertionError: tests>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->