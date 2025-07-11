.. include:: ../links.rst

#################################################################################
AssertionError
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/jxbttz7R0ho?si=Oiv1Y0WPwQhlw5i9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

.. contents:: table of contents
  :local:
  :depth: 1

----

The `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_ is raised to show that a statement is :ref:`False<test_what_is_false>`. It was introduced in :doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with the first failing test

.. code-block:: python

  self.assertFalse(True)

which is like

.. code-block:: python

  assert True is False

When building a program I can use assert_ methods to make sure something is :ref:`True<test_what_is_true>` before it continues, I can also use them to test how the program behaves, for example when it is given inputs, which can help catch things that break previous tested behavior when added. They also help me answer 2 questions

* what is the same?
* what is different?

The difference between my expectations and reality (what happens when the program runs), gives me a clue about what to change to make them match.

----

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

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_assertion_error.py:7`` to open it in the editor
* then change ``True`` to ``False`` to make the test pass
* and change ``test_failure`` to ``test_assertion_error_w_none``

  .. code-block:: python

    import unittest


    class TestAssertionError(unittest.TestCase):

        def test_assertion_error_w_none(self):
            assert None is not None

  the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert None is not None

    tests/test_assertion_error.py:7: AssertionError

  the assert_ at the beginning of the line makes the statement something like "DO NOT CONTINUE, UNLESS :ref:`None` is NOT :ref:`None`". The `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_ is raised to break execution of the program because the statement is :ref:`False<test_what_is_false>`

green: make it pass
#################################################################################

When I change the failing line

.. code-block:: python

  def test_assertion_error_w_none(self):
      assert None is None

the test passes because this statement is :ref:`True<test_what_is_true>`

refactor: make it better
#################################################################################

I can also make assertions with some :ref:`methods<functions>` from the `unittest.TestCase`_ class

* I add another failing line using the assertIsNotNone_ :ref:`method<functions>` which checks if something is NOT :ref:`None`

  .. code-block:: python

    def test_assertion_error_w_none(self):
        assert None is None
        self.assertIsNotNone(None)

  the terminal shows a more descriptive message for the `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: unexpectedly None

  when I change the statement to use the assertIsNone_ :ref:`method<functions>` which checks if something is :ref:`None`

  .. code-block:: python

    def test_assertion_error_w_none(self):
        assert None is None
        self.assertIsNone(None)

  the test passes and I add a note

  .. code-block:: python

    # NOTES
    # None is None


    # Exceptions Encountered
    # AssertionError

* then I add a new failing line

  .. code-block:: python

    def test_assertion_error_w_none(self):
        assert None is None
        self.assertIsNone(None)

        assert False is None

  the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert False is None

  I change the line to make it :ref:`True<test_what_is_true>`

  .. code-block:: python

    assert False is not None

  and the test passes. I add another line with the assertIsNone_ :ref:`method<functions>` which checks if something is :ref:`None`

  .. code-block:: python

    def test_assertion_error_w_none(self):
        assert None is None
        self.assertIsNone(None)

        assert False is not None
        self.assertIsNone(False)

  the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: False is not None

  I change the statement

  .. code-block:: python

    assert False is None
    self.assertIsNotNone(False)

  and the test passes. I add another note

  .. code-block:: python

    # NOTES
    # False is not None
    # None is None

* then I add a failing line

  .. code-block:: python

    def test_assertion_error_w_none(self):
        assert None is None
        self.assertIsNone(None)

        assert False is not None
        self.assertIsNotNone(False)

        assert True is None

  the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert True is None

  I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python

    assert True is not None

  and the terminal shows green again. I add a failing line using the assertIsNone_ :ref:`method<functions>`

  .. code-block:: python

    def test_assertion_error_w_none(self):
        assert None is None
        self.assertIsNone(None)

        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNone(True)

  the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: True is not None

  when I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python

      assert True is not None
      self.assertIsNotNone(True)

  the test passes and I add a note

  .. code-block:: python

    # NOTES
    # True is not None
    # False is not None
    # None is None

----


*********************************************************************************
test_assertion_error_w_false
*********************************************************************************

I can test if something is :ref:`False<test_what_is_false>`

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_assertion_error_w_false(self):
      assert True is False

the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

.. code-block:: python

  E    assert True is False

green: make it pass
#################################################################################

I change the line to make it :ref:`True<test_what_is_true>`

.. code-block:: python

  def test_assertion_error_w_false(self):
      assert True is not False

and the terminal shows all tests are passing

red: make it fail
#################################################################################

There is a :ref:`method<functions>` for this, it is the one from the first failing test which checks if something is :ref:`False<test_what_is_false>`

.. code-block:: python

  def test_assertion_error_w_false(self):
      assert True is not False
      self.assertFalse(True)

the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

.. code-block:: python

  AssertionError: True is not false

green: make it pass
#################################################################################

I change the failing line

.. code-block:: python

  def test_assertion_error_w_false(self):
      assert True is not False
      self.assertFalse(False)

and the test passes. Time to add notes

.. code-block:: python

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

I can test if something is :ref:`True<test_what_is_true>`

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_assertion_error_w_true(self):
      assert False is True

and the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

.. code-block:: python

  E    assert False is True

green: make it pass
#################################################################################

then I make the statement :ref:`True<test_what_is_true>`

.. code-block:: python

  def test_assertion_error_w_true(self):
      assert False is not True

and the terminal shows green again

red: make it fail
#################################################################################

there is also a :ref:`method<functions>` to check if something is :ref:`True<test_what_is_true>`

.. code-block:: python

  def test_assertion_error_w_true(self):
      assert False is not True
      self.assertTrue(False)

the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

.. code-block:: python

  AssertionError: False is not true

green: make it pass
#################################################################################

I change the failing line to a :ref:`True<test_what_is_true>` statement

.. code-block:: python

  def test_assertion_error_w_true(self):
      assert False is not True
      self.assertTrue(True)

and all tests are passing. I add more notes

.. code-block:: python

  # NOTES
  # True is True
  # False is not True
  # False is False
  # True is not False
  # True is not None
  # False is not None
  # None is None

These statements can be summed up as - :ref:`True<test_what_is_true>`, :ref:`False<test_what_is_false>` and :ref:`None` are different. They set up a basic expectation because I can compare things to them.

----


*********************************************************************************
test_assertion_error_w_equality
*********************************************************************************

I can also test if 2 things are equal

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_assertion_error_w_equality(self):
      assert None != None

the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

.. code-block:: python

  E    assert None != None

``!=`` is the symbol for ``NOT equal`` which makes this statement read as ``assert None is NOT equal to None``

green: make it pass
#################################################################################

I change the failing line and the test passes

.. code-block:: python

  def test_assertion_error_w_equality(self):
      assert None == None

``==`` is the symbol for ``is equal`` which makes this statement read as ``assert None is equal to None``

refactor: make it better
#################################################################################

* there is a :ref:`method<functions>` for this

  .. code-block:: python

    def test_assertion_error_w_equality(self):
        assert None == None
        self.assertNotEqual(None, None)

  `unittest.TestCase.assertNotEqual`_ checks if the 2 things given are NOT equal, and the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: None == None

  when I use the `unittest.TestCase.assertEqual`_ :ref:`method<functions>` to make the failing line :ref:`True<test_what_is_true>`

  .. code-block:: python

    def test_assertion_error_w_equality(self):
        assert None == None
        self.assertEqual(None, None)

  the terminal shows passing tests and I update the notes

  .. code-block:: python

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False
    # True is not None
    # False is not None
    # None is None and equal to None

* then I add a new failing line

  .. code-block:: python

    def test_assertion_error_w_equality(self):
        assert None == None
        self.assertEqual(None, None)

        assert False == None

  and the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert False == None

  when I change the failing line to a :ref:`True<test_what_is_true>` statement

  .. code-block:: python

    assert False != None

  the terminal shows passing tests. I add the `unittest.TestCase.assertEqual`_ :ref:`method<functions>`

  .. code-block:: python

    assert False != None
    self.assertEqual(False, None)

  and the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: False != None

  I change the failing line to a :ref:`True<test_what_is_true>` statement

  .. code-block:: python

    assert False != None
    self.assertNotEqual(False, None)

  and the test passes. I update the notes to say that

  .. code-block:: python

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False
    # True is not None
    # False is not None and not equal to None
    # None is None and equal to None

* I add the next failing line

  .. code-block:: python

    def test_assertion_error_w_equality(self):
        assert None == None
        self.assertEqual(None, None)

        assert False != None
        self.assertNotEqual(False, None)

        assert True == None

  and get `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert True == None

  I change the statement

  .. code-block:: python

    assert True != None

  and the test passes. I do the same thing with an assert :ref:`method<functions>`

  .. code-block:: python

    assert True != None
    self.assertEqual(True, None)

  the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: True != None

  I change the :ref:`method<functions>`

  .. code-block:: python

    assert True != None
    self.assertNotEqual(True, None)

  and the test is green again. I add a note

  .. code-block:: python

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None

* then I add another failing line

  .. code-block:: python

    def test_assertion_error_w_equality(self):
        assert None == None
        self.assertEqual(None, None)

        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertNotEqual(True, None)

        assert True == False

  the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert True == False

  I change the failing line

  .. code-block:: python

    assert True != False

  and the test passes. I add a call to assertEqual_

  .. code-block:: python

    assert True != False
    self.assertEqual(True, False)

  and get `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: True != False

  then I change the :ref:`method<functions>`

  .. code-block:: python

    assert True != False
    self.assertNotEqual(True, False)

  and the test passes. I add a note

  .. code-block:: python

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False and not equal to False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None

* on to the next line

  .. code-block:: python

    def test_assertion_error_w_equality(self):
        assert None == None
        self.assertEqual(None, None)

        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertNotEqual(True, None)

        assert True != False
        self.assertNotEqual(True, False)

        assert False != False

  which gives me `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert False != False

  I make the line :ref:`True<test_what_is_true>`

  .. code-block:: python

    assert False == False

  and the test passes. I add another failing line

  .. code-block:: python

    assert False == False
    self.assertNotEqual(False, False)

  the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: False == False

  when I change the :ref:`method<functions>`

  .. code-block:: python

    assert False == False
    self.assertEqual(False, False)

  the test passes and I add a note

  .. code-block:: python

    # NOTES
    # True is True
    # False is not True
    # False is False and equal to False
    # True is not False and not equal to False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None

* I add another failing line

  .. code-block:: python

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

        assert False == True

  the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert False == True

  I change the line

  .. code-block:: python

    assert False != True

  and the terminal shows passing tests. I add another failing line

  .. code-block:: python

    assert False != True
    self.assertEqual(False, True)

  and get `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: False != True

  then I change the :ref:`method<functions>`

  .. code-block:: python

    assert False != True
    self.assertNotEqual(False, True)

  and the test passes. I add another note

  .. code-block:: python

    # NOTES
    # True is True
    # False is not True and not equal to True
    # False is False and equal to False
    # True is not False and not equal to False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None

* time for the last statement

  .. code-block:: python

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

        assert True != True

  the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    E    assert True != True

  when I make the line :ref:`True<test_what_is_true>`

  .. code-block:: python

    assert True == True

  the test passes. I add a line with the assert_ :ref:`method<functions>`

  .. code-block:: python

    assert True == True
    self.assertNotEqual(True, True)

  and the terminal shows `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError>`_

  .. code-block:: python

    AssertionError: True == True

  I change the :ref:`method<functions>`

  .. code-block:: python

    assert True == True
    self.assertEqual(True, True)

  and all tests are passing. I add a note for the last statement

  .. code-block:: python

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

With `assert statements`_ and :ref:`methods<functions>` I can test if something is

* :ref:`None` or not
* :ref:`False<test_what_is_false>` or not
* :ref:`True<test_what_is_true>` or not
* equal or not

Would you like to test the :ref:`AttributeError`?

----

:doc:`/code/code_assertion_error`