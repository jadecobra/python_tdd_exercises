.. include:: ../links.rst

.. _AssertionError:

#################################################################################
AssertionError
#################################################################################

----

.. contents:: table of contents
  :local:
  :depth: 1

----

An `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_ is an Exception that is raised when the result of an ``assert`` statement is :ref:`False <test_what_is_false>`

It was introduced in :doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with the first failing test

.. code-block:: python

  self.assertFalse(True)

which is like

.. code-block:: python

  assert True is False

*********************************************************************************
why are asserts important?
*********************************************************************************

When building a program I can add ``assert`` statements to the program to ensure that certain things are :ref:`True <test_what_is_true>` for it to proceed past the statements.

I can also test how the program behaves when it is given inputs using ``assert`` statements.

These assertions help catch bugs that break previous tested behavior when introduced, as well as answer the following questions

* what is the same?
* What is different?

A difference between my expectations and reality (what happens when I run the program) gives me a clue about what changes are needed to make them match

----

.. _test_assertion_errors_w_none:

*********************************************************************************
test_assertion_errors_w_none
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``assertion_error`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh assertion_error

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 assertion_error

  it makes the folders and files that are needed, installs packages, runs the first test and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_assertion_error.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_assertion_error.py:7`` with the mouse to open it
* then change ``True`` to ``False`` to make the test pass
* and change ``test_failure``

  .. code-block:: python

    import unittest


    class TestAssertionErrors(unittest.TestCase):

        def test_assertion_errors_w_none(self):
            assert False is None

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert False is None

    tests/test_assertion_error.py:7: AssertionError

  - This `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_ is raised by the line ``assert False is None`` which is like asking the question "is False the same as None?"
  - The difference is that the ``assert`` at the beginning of the line makes the statement more like "DO NOT PROCEED UNLESS :ref:`False <test_what_is_false>` is :ref:`None`"
  - Since :ref:`None` and :ref:`False <test_what_is_false>` are not equal, the ``assert`` statement is :ref:`False <test_what_is_false>` and python raises an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

green: make it pass
#################################################################################

When I make the failing line to

.. code-block:: python

  def test_assertion_errors_w_none(self):
      assert False is not None

the test passes because the assert statement is now true since :ref:`False <test_what_is_false>` is not :ref:`None`

refactor: make it better
#################################################################################

I can also make assertions with some :ref:`methods<functions>` from the `unittest.TestCase`_ class


* red: make it fail

  I add another failing line using the `unittest.TestCase.assertIsNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNone>`_ :ref:`method<functions>`

  .. code-block:: python

    def test_assertion_errors_w_none(self):
        assert False is not None
        self.assertIsNone(False)

  the terminal shows a more descriptive `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_ since ``False is not None``

  .. code-block:: python

    AssertionError: False is not None

* green: make it pass

  when I make the assert statement to

  .. code-block:: python

    def test_assertion_errors_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

  the terminal shows passing tests because the statement is :ref:`True <test_what_is_true>`. I can now say that in Python :ref:`False <test_what_is_false>` is not :ref:`None`

* red: make it fail

  I add another test to find out how :ref:`None` is related to :ref:`True <test_what_is_true>`

  .. code-block:: python

    def test_assertion_errors_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is None

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert True is None

* green: make it pass

  I make the failing line to make the test pass

  .. code-block:: python

    def test_assertion_errors_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None

* red: make it fail

  I add a line using the `unittest.TestCase.assertIsNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNone>`_ :ref:`method<functions>`

  .. code-block:: python

    def test_assertion_errors_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNone(True)

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: True is not None

* green: make it pass

  I make the failing line to make the test pass

  .. code-block:: python

    def test_assertion_errors_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

  since all my tests are passing I can say that in Python

  - :ref:`True <test_what_is_true>` is not :ref:`None`
  - :ref:`False <test_what_is_false>` is not :ref:`None`

* red: make it fail

  I add a failing line

  .. code-block:: python

    def test_assertion_errors_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

        assert None is not None

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert None is not None

* green: make it pass

  I make the failing line to make the test pass

  .. code-block:: python

    def test_assertion_errors_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

        assert None is None

* red: make it fail

  I add a failing line using the `unittest.TestCase`_ method

  .. code-block:: python

    def test_assertion_errors_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

        assert None is None
        self.assertIsNotNone(None)

  and the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: unexpectedly None

* green: make it pass

  I make ``test_assertion_errors_w_none`` to make it pass

  .. code-block:: python

    def test_assertion_errors_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

        assert None is None
        self.assertIsNone(None)

From the tests I can see that

* :ref:`None` is :ref:`None`
* :ref:`True <test_what_is_true>` is not :ref:`None`
* :ref:`False <test_what_is_false>` is not :ref:`None`

Which of these ``assert`` statements do you prefer when testing :ref:`None`?

* ``assert x is None``
* ``self.assertIsNone(x)``

----

.. _test_assertion_errors_w_false:

*********************************************************************************
test_assertion_errors_w_false
*********************************************************************************

Can I raise an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_ for things that are :ref:`False <test_what_is_false>`?

red: make it fail
#################################################################################

I add a failing test to ``TestAssertionError`` in ``test_assertion_error.py`` to find out

.. code-block:: python

  def test_assertion_errors_w_false(self):
      assert True is False

the terminal shows a failure

.. code-block:: python

  E    assert True is False

green: make it pass
#################################################################################

I make the failing line to make the test pass

.. code-block:: python

  def test_assertion_errors_w_false(self):
      assert False is False

red: make it fail
#################################################################################

What if I try the same test using the `unittest.TestCase.assertFalse <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertFalse>`_ :ref:`method<functions>` by adding this line to ``test_assertion_errors_w_false``?

.. code-block:: python

  def test_assertion_errors_w_false(self):
      assert False is False
      self.assertFalse(True)

the terminal shows a failure

.. code-block:: python

  AssertionError: True is not false

this is familiar, it was the first failing test from :doc:`how to make a python test driven development environment </how_to/make_tdd_environment>`

green: make it pass
#################################################################################

I make the failing line to make the test pass

.. code-block:: python

  def test_assertion_errors_w_false(self):
      assert False is False
      self.assertFalse(False)

From the tests I can see that in Python

* :ref:`False <test_what_is_false>` is :ref:`False <test_what_is_false>`
* :ref:`False <test_what_is_false>` is not :ref:`True <test_what_is_true>`
* :ref:`None` is :ref:`None`
* :ref:`True <test_what_is_true>` is not :ref:`None`
* :ref:`False <test_what_is_false>` is not :ref:`None`

----

.. _test_assertion_errors_w_true:

*********************************************************************************
test_assertion_errors_w_true
*********************************************************************************

Can I raise an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_ for things that are :ref:`True <test_what_is_true>`?

red: make it fail
#################################################################################

I add a failing test to ``TestAssertionError`` in ``test_assertion_error.py``

.. code-block:: python

  def test_assertion_errors_w_true(self):
      assert False is True

the terminal shows a failure

.. code-block:: python

  E    assert False is True

green: make it pass
#################################################################################

I make the failing line to make the test pass

.. code-block:: python

  def test_assertion_errors_w_true(self):
      assert True is True

red: make it fail
#################################################################################

What if I try the above test using the `unittest.TestCase.assertTrue <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertTrue>`_ :ref:`method<functions>` ?

.. code-block:: python

  def test_assertion_errors_w_true(self):
      assert True is True
      self.assertTrue(False)

the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

.. code-block:: python

  AssertionError: False is not true

green: make it pass
#################################################################################

I make the failing line to make the test pass

.. code-block:: python

  def test_assertion_errors_w_true(self):
      assert True is True
      self.assertTrue(True)

From the tests I can see that


* :ref:`True <test_what_is_true>` is :ref:`True <test_what_is_true>`
* :ref:`True <test_what_is_true>` is not :ref:`False <test_what_is_false>`
* :ref:`False <test_what_is_false>` is :ref:`False <test_what_is_false>`
* :ref:`False <test_what_is_false>` is not :ref:`True <test_what_is_true>`
* :ref:`None` is :ref:`None`
* :ref:`True <test_what_is_true>` is not :ref:`None`
* :ref:`False <test_what_is_false>` is not :ref:`None`

I could sum up the above statements this way - in Python :ref:`True <test_what_is_true>`, :ref:`False <test_what_is_false>` and :ref:`None` are different. My understanding of these differences helps me know howPython behaves and gives a foundation of predictable expectations of the language.

----

.. _test_assertion_errors_w_equality:

*********************************************************************************
test_assertion_errors_w_equality
*********************************************************************************

I can also make assertions where I compare if two things are the same or equal

red: make it fail
#################################################################################

I add a new test to ``TestAssertionError`` in ``test_assertion_error.py``

.. code-block:: python

  def test_assertion_errors_w_equality(self):
      assert False == None

the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

.. code-block:: python

  E    assert False == None

green: make it pass
#################################################################################

I make the failing line to make the test pass

.. code-block:: python

  def test_assertion_errors_w_equality(self):
      assert False != None

the test passes because :ref:`False <test_what_is_false>` is not equal to :ref:`None`

refactor: make it better
#################################################################################

* red: make it fail

  I add a line with the `unittest.TestCase`_ method for equality testing

  .. code-block:: python

    def test_assertion_errors_w_equality(self):
        assert False != None
        self.assertEqual(False, None)

  and the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: False != None

  The `unittest.TestCase.assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ :ref:`method<functions>` checks if the two given inputs, :ref:`False <test_what_is_false>` and :ref:`None` are equal

* green: make it pass

  I make the failing line to make the test pass

  .. code-block:: python

    def test_assertion_errors_w_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

  I have learned that in Python

  * :ref:`True <test_what_is_true>` is :ref:`True <test_what_is_true>`
  * :ref:`True <test_what_is_true>` is not :ref:`False <test_what_is_false>`
  * :ref:`False <test_what_is_false>` is :ref:`False <test_what_is_false>`
  * :ref:`False <test_what_is_false>` is not :ref:`True <test_what_is_true>`
  * :ref:`None` is :ref:`None`
  * :ref:`True <test_what_is_true>` is not :ref:`None`
  * :ref:`False <test_what_is_false>` is not :ref:`None` and :ref:`False <test_what_is_false>` is not equal to :ref:`None`

* red: make it fail

  I add a new line to ``test_assertion_errors_w_equality``

  .. code-block:: python

    def test_assertion_errors_w_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True == None

  and the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert True == None

* green: make it pass

  I make the failing line to make the test pass

  .. code-block:: python

    def test_assertion_errors_w_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None

* red: make it fail

  I add the `unittest.TestCase.assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ :ref:`method<functions>` to ``test_assertion_errors_w_equality``

  .. code-block:: python

    def test_assertion_errors_w_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertEqual(True, None)

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: True != None

* green: make it pass

  I make the failing line to make the test pass

  .. code-block:: python

    def test_assertion_errors_w_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertNotEqual(True, None)

  and the terminal shows passing tests. I can now say that in Python

  * :ref:`True <test_what_is_true>` is :ref:`True <test_what_is_true>`
  * :ref:`True <test_what_is_true>` is not :ref:`False <test_what_is_false>`
  * :ref:`False <test_what_is_false>` is :ref:`False <test_what_is_false>`
  * :ref:`False <test_what_is_false>` is not :ref:`True <test_what_is_true>`
  * :ref:`None` is :ref:`None`
  * :ref:`True <test_what_is_true>` is not :ref:`None` and :ref:`True <test_what_is_true>` is not equal to :ref:`None`
  * :ref:`False <test_what_is_false>` is not :ref:`None` and :ref:`False <test_what_is_false>` is not equal to :ref:`None`

* red: make it fail

  There is a pattern here, so I add the other cases from the statements above to  ``test_assertion_errors_w_equality``

  .. code-block:: python

    def test_assertion_errors_w_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertNotEqual(True, None)

        assert True != True
        self.assertNotEqual(True, True)

        assert True == False
        self.assertEqual(True, False)

        assert False != False
        self.assertNotEqual(False, False)

        assert False == True
        self.assertEqual(False, True)

        assert None != None
        self.assertNotEqual(None, None)

* green: make it pass

  then I make each failing line until they all pass

  .. code-block:: python

    def test_assertion_errors_w_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertNotEqual(True, None)

        assert True == True
        self.assertEqual(True, True)

        assert True != False
        self.assertNotEqual(True, False)

        assert False == False
        self.assertEqual(False, False)

        assert False != True
        self.assertNotEqual(False, True)

        assert None == None
        self.assertEqual(None, None)

  and from the tests I can say that in Python

  * :ref:`True <test_what_is_true>` is :ref:`True <test_what_is_true>` and :ref:`True <test_what_is_true>` is equal to :ref:`True <test_what_is_true>`
  * :ref:`True <test_what_is_true>` is not :ref:`False <test_what_is_false>` and :ref:`True <test_what_is_true>` is not equal to :ref:`False <test_what_is_false>`
  * :ref:`False <test_what_is_false>` is :ref:`False <test_what_is_false>` and :ref:`False <test_what_is_false>` is equal to :ref:`False <test_what_is_false>`
  * :ref:`False <test_what_is_false>` is not :ref:`True <test_what_is_true>` and :ref:`False <test_what_is_false>` is not equal to :ref:`True <test_what_is_true>`
  * :ref:`None` is :ref:`None` and :ref:`None` is equal to :ref:`None`
  * :ref:`True <test_what_is_true>` is not :ref:`None` and :ref:`True <test_what_is_true>` is not equal to :ref:`None`
  * :ref:`False <test_what_is_false>` is not :ref:`None` and :ref:`False <test_what_is_false>` is not equal to :ref:`None`

----

.. _test_assertion_errors_review:

*********************************************************************************
review
*********************************************************************************

If you have been typing along *WELL DONE!* Your magic powers are growing. From the tests above you now know

* how to test for equality
* how to test if something is :ref:`None` or not
* how to test if something is :ref:`False <test_what_is_false>` or not
* how to test if something is :ref:`True <test_what_is_true>` or not
* how to use ``assert`` statements
* how to use the following ``unittest.TestCase.assert`` methods

  - `assertIsNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNone>`_ - is this thing :ref:`None`? (try saying that 10 times fast)
  - `assertIsNotNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNotNone>`_ - is this thing not :ref:`None`?
  - `unittest.TestCase.assertFalse`_ - is this thing :ref:`False <test_what_is_false>`?
  - `assertTrue <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertTrue>`_ - is this thing :ref:`True <test_what_is_true>`?
  - assertEqual_ - are these two things equal?
  - `assertNotEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotEqual>`_ - are these two things not equal?

Would you like to test :ref:`AttributeErrors<AttributeError>`?

----

:doc:`/code/code_assertion_error`