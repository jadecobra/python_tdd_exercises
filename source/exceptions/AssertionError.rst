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

`AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_ is an Exception_ that is raised when the result of an ``assert`` statement is :ref:`False<test_what_is_false>`. It was introduced in :doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with the first failing test

.. code-block:: python

  self.assertFalse(True)

which is like

.. code-block:: python

  assert True is False

*********************************************************************************
why are asserts important?
*********************************************************************************

When building a program I can add ``assert`` statements to make sure something is :ref:`True<test_what_is_true>` before it continues. I can also use them to test how the program behaves when it is given inputs. This helps catch bugs that break previous tested behavior when introduced, as well as answer the following questions

* What is the same?
* What is different?

A difference between my expectations and reality, which is what happens when I run the program, gives me a clue about what to change to make them match

----

.. _test_assertion_error_w_none:

*********************************************************************************
test_assertion_error_w_none
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``assertion_error`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh assertion_error

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 assertion_error

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_assertion_error.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_assertion_error.py:7`` with the mouse to open it in the editor
* then change ``True`` to ``False`` to make the test pass
* and ``test_failure`` to ``test_assertion_error_w_none``

  .. code-block:: python

    import unittest


    class TestAssertionErrors(unittest.TestCase):

        def test_assertion_error_w_none(self):
            assert False is None

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert False is None

    tests/test_assertion_error.py:7: AssertionError

  - This `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_ is raised by the line ``assert False is None`` which is like asking the question "is False the same as None?"
  - The difference is that the ``assert`` at the beginning of the line makes the statement more like "DO NOT GO ON, UNLESS :ref:`False<test_what_is_false>` is :ref:`None`"
  - Since :ref:`None` and :ref:`False<test_what_is_false>` are not equal, the ``assert`` statement is :ref:`False<test_what_is_false>` and python raises an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

green: make it pass
#################################################################################

When I change the failing line

.. code-block:: python

  def test_assertion_error_w_none(self):
      assert False is not None

the test passes because the assert statement is now true since :ref:`False<test_what_is_false>` is not :ref:`None`

refactor: make it better
#################################################################################

I can also make assertions with some :ref:`methods<functions>` from the `unittest.TestCase`_ class

* I add another failing line using the `unittest.TestCase.assertIsNone`_ :ref:`method<functions>`

  .. code-block:: python

    def test_assertion_error_w_none(self):
        assert False is not None
        self.assertIsNone(False)

  the terminal shows a more descriptive `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: False is not None

* When I change the statement to use a different :ref:`method<functions>`

  .. code-block:: python

    def test_assertion_error_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

  the terminal shows a passing test because the statement is :ref:`True<test_what_is_true>`. I can now say that in Python :ref:`False<test_what_is_false>` is not :ref:`None`

* I add another test to find out how :ref:`None` is related to :ref:`True<test_what_is_true>`

  .. code-block:: python

    def test_assertion_error_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is None

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert True is None

* I change the failing line to a :ref:`True` statement

  .. code-block:: python

    def test_assertion_error_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None

  and the test passes

* I add a line using the `unittest.TestCase.assertIsNone`_ :ref:`method<functions>`

  .. code-block:: python

    def test_assertion_error_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNone(True)

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: True is not None

* when I change the statement

  .. code-block:: python

      assert True is not None
      self.assertIsNotNone(True)

  the test passes. I can now say that in Python

  - :ref:`True<test_what_is_true>` is not :ref:`None` and
  - :ref:`False<test_what_is_false>` is not :ref:`None`

* I add another failing line

  .. code-block:: python

    def test_assertion_error_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

        assert None is not None

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert None is not None

* when I change the statement to make it :ref:`True`

  .. code-block:: python

    assert None is None

  the terminal shows green again

* I add a failing line using an assert :ref:`method<functions>`

  .. code-block:: python

    def test_assertion_error_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

        assert None is None
        self.assertIsNotNone(None)

  and the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: unexpectedly None

* when I make the statement :ref:`True`

  .. code-block:: python

      assert None is None
      self.assertIsNone(None)

the test passes, and I can say that

* :ref:`None` is :ref:`None`
* :ref:`True<test_what_is_true>` is not :ref:`None`
* :ref:`False<test_what_is_false>` is not :ref:`None`

Which of these ``assert`` statements do you prefer when testing :ref:`None`?

* ``assert x is None``
* ``self.assertIsNone(x)``

----

.. _test_assertion_error_w_false:

*********************************************************************************
test_assertion_error_w_false
*********************************************************************************

Can I raise the `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_ for things that are :ref:`False<test_what_is_false>`?

red: make it fail
#################################################################################

I add a failing test to ``TestAssertionError`` in ``test_assertion_error.py`` to find out

.. code-block:: python

  def test_assertion_error_w_false(self):
      assert True is False

the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

.. code-block:: python

  E    assert True is False

green: make it pass
#################################################################################

I change the line to a :ref:`True` statement

.. code-block:: python

  def test_assertion_error_w_false(self):
      assert False is False

and the terminal shows passing tests

red: make it fail
#################################################################################

What if I try this with the `unittest.TestCase.assertFalse`_ :ref:`method<functions>`?

.. code-block:: python

  def test_assertion_error_w_false(self):
      assert False is False
      self.assertFalse(True)

the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

.. code-block:: python

  AssertionError: True is not false

this is familiar, it was the first failing test from :doc:`how to make a python test driven development environment </how_to/make_tdd_environment>`

green: make it pass
#################################################################################

I change the failing line to a :ref:`True` statement

.. code-block:: python

  def test_assertion_error_w_false(self):
      assert False is False
      self.assertFalse(False)

From the tests I can say that in Python

* :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`None` is :ref:`None`
* :ref:`True<test_what_is_true>` is not :ref:`None`
* :ref:`False<test_what_is_false>` is not :ref:`None`

----

.. _test_assertion_error_w_true:

*********************************************************************************
test_assertion_error_w_true
*********************************************************************************

Can I raise an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_ for things that are :ref:`True`?

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_assertion_error_w_true(self):
      assert False is True

the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

.. code-block:: python

  E    assert False is True

green: make it pass
#################################################################################

I change the failing line to a :ref:`True` statement

.. code-block:: python

  def test_assertion_error_w_true(self):
      assert True is True

and the test pases

red: make it fail
#################################################################################

What if I try the above test using the `unittest.TestCase.assertTrue` :ref:`method<functions>` ?

.. code-block:: python

  def test_assertion_error_w_true(self):
      assert True is True
      self.assertTrue(False)

the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

.. code-block:: python

  AssertionError: False is not true

green: make it pass
#################################################################################

I change the failing line to a :ref:`True` statement

.. code-block:: python

  def test_assertion_error_w_true(self):
      assert True is True
      self.assertTrue(True)

and the terminal shows passing tests. Which allows me to say that


* :ref:`False<test_what_is_false>` is not :ref:`True<test_what_is_true>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`
* :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`None` is :ref:`None`
* :ref:`True<test_what_is_true>` is not :ref:`None`
* :ref:`False<test_what_is_false>` is not :ref:`None`

I can sum up these statements as - in Python :ref:`True<test_what_is_true>`, :ref:`False<test_what_is_false>` and :ref:`None` are different, which helps me know how it behaves and gives me something to compare things with.

----

.. _test_assertion_error_w_equality:

*********************************************************************************
test_assertion_error_w_equality
*********************************************************************************

I can also make assertions where I check if two things are equal

red: make it fail
#################################################################################

I add a new test to ``TestAssertionError`` in ``test_assertion_error.py``

.. code-block:: python

  def test_assertion_error_w_equality(self):
      assert False == None

the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

.. code-block:: python

  E    assert False == None

green: make it pass
#################################################################################

I change the failing line to a :ref:`True` statement

.. code-block:: python

  def test_assertion_error_w_equality(self):
      assert False != None

the test passes because :ref:`False<test_what_is_false>` is not equal to :ref:`None`

refactor: make it better
#################################################################################

* red: make it fail

  I add a line with the `unittest.TestCase.assertEqual`_

  .. code-block:: python

    def test_assertion_error_w_equality(self):
        assert False != None
        self.assertEqual(False, None)

  and the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: False != None

  The `assertEqual`_ :ref:`method<functions>` checks if the two given inputs, :ref:`False<test_what_is_false>` and :ref:`None` are equal

* when I change the failing line to a :ref:`True` statement by using `unittest.TestCase.assertNotEqual`_

  .. code-block:: python

    def test_assertion_error_w_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

  the terminal shows passing tests. I have learned that in Python

  * :ref:`False<test_what_is_false>` is not :ref:`True<test_what_is_true>`
  * :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`
  * :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`
  * :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
  * :ref:`None` is :ref:`None`
  * :ref:`True<test_what_is_true>` is not :ref:`None`
  * :ref:`False<test_what_is_false>` is not :ref:`None` and :ref:`False<test_what_is_false>` is not equal to :ref:`None`

* I add a new failing line

  .. code-block:: python

    def test_assertion_error_w_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True == None

  and the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert True == None

* when I change the failing line to a :ref:`True` statement

  .. code-block:: python

    def test_assertion_error_w_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None

  the terminal shows passing tests

* I add the `unittest.TestCase.assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ :ref:`method<functions>`

  .. code-block:: python

    def test_assertion_error_w_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertEqual(True, None)

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: True != None

* I change the failing line to a :ref:`True` statement

  .. code-block:: python

    def test_assertion_error_w_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertNotEqual(True, None)

  and the terminal shows passing tests. I can now say that in Python

  * :ref:`False<test_what_is_false>` is not :ref:`True<test_what_is_true>`
  * :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`
  * :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`
  * :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
  * :ref:`None` is :ref:`None`
  * :ref:`True<test_what_is_true>` is not :ref:`None` and :ref:`True<test_what_is_true>` is not equal to :ref:`None`
  * :ref:`False<test_what_is_false>` is not :ref:`None` and :ref:`False<test_what_is_false>` is not equal to :ref:`None`

* red: make it fail

  There is a pattern here, so I add the other cases from the statements above to  ``test_assertion_error_w_equality``

  .. code-block:: python

    def test_assertion_error_w_equality(self):
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

* then I change each failing line until they all pass

  .. code-block:: python

    def test_assertion_error_w_equality(self):
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

  * :ref:`False<test_what_is_false>` is not :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>` is not equal to :ref:`True<test_what_is_true>`
  * :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>` and :ref:`True<test_what_is_true>` is equal to :ref:`True<test_what_is_true>`
  * :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>` and :ref:`True<test_what_is_true>` is not equal to :ref:`False<test_what_is_false>`
  * :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>` and :ref:`False<test_what_is_false>` is equal to :ref:`False<test_what_is_false>`
  * :ref:`None` is :ref:`None` and :ref:`None` is equal to :ref:`None`
  * :ref:`True<test_what_is_true>` is not :ref:`None` and :ref:`True<test_what_is_true>` is not equal to :ref:`None`
  * :ref:`False<test_what_is_false>` is not :ref:`None` and :ref:`False<test_what_is_false>` is not equal to :ref:`None`

----

.. _test_assertion_error_review:

*********************************************************************************
review
*********************************************************************************

If you have been typing along *WELL DONE!* Your magic powers are growing. From these tests you know

* how to test for equality
* how to test if something is :ref:`None` or not
* how to test if something is :ref:`False<test_what_is_false>` or not
* how to test if something is :ref:`True<test_what_is_true>` or not
* how to use ``assert`` statements
* how to use the following ``unittest.TestCase.assert`` methods

  - assertIsNone_ - is this thing :ref:`None`?
  - assertIsNotNone_ - is this thing not :ref:`None`?
  - assertFalse_ - is this thing :ref:`False<test_what_is_false>`?
  - assertTrue_ - is this thing :ref:`True<test_what_is_true>`?
  - assertEqual_ - are these two things equal?
  - assertNotEqual_ - are these two things not equal?

Would you like to test the :ref:`AttributeError`?

----

:doc:`/code/code_assertion_error`