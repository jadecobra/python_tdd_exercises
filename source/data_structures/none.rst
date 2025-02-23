.. include:: ../links.rst

#################################################################################
None
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/81afQTs6JH0?si=LAtEPEdDKutSOGw9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
test_what_is_none
*********************************************************************************

`None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is used when there is no value

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``none`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh none

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 none

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_none.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_none.py:7`` to open it in the editor
* then change ``True`` to ``False`` to make the test pass
* and change ``test_failure`` to ``test_what_is_none``

  .. code-block:: python

    import unittest


    class TestNone(unittest.TestCase):

        def test_what_is_none(self):
            self.assertIsNotNone(None)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: unexpectedly None

  assertIsNotNone_ checks that its input is NOT `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

green: make it pass
#################################################################################

When I use the assertIsNone_ :ref:`method<functions>` to check if the input is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

.. code-block:: python

  def test_what_is_none(self):
      self.assertIsNone(None)

the test passes, and I add a note

.. code-block:: python

  # NOTES
  # None is None


  # Exceptions Encountered
  # AssertionError

----

*********************************************************************************
test_is_none_a_boolean
*********************************************************************************

red: make it fail
#################################################################################

I add another failing test

.. code-block:: python

  def test_is_none_a_boolean(self):
      self.assertIsNone(False)

and the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: False is not None

green: make it pass
#################################################################################

I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # NOTES
    # False is NOT None
    # None is None


then I change the :ref:`method<functions>`

.. code-block:: python

  def test_is_none_a_boolean(self):
      self.assertIsNotNone(False)

and the test passes

refactor: make it better
#################################################################################

* I add another failing line

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNone(True)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not None

  then I add a note

  .. code-block:: python

    # NOTES
    # True is NOT None
    # False is NOT None
    # None is None

  I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)

  and the test passes

* The `unittest.TestCase`_ :ref:`class<classes>` has two :ref:`methods<functions>` I can use to test if an object_ is an instance of a :ref:`class<classes>` or not

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)
        self.assertNotIsInstance(False, bool)

  the assertNotIsInstance_ :ref:`method<functions>` checks if the object_ on the left in the parentheses is NOT an instance of the :ref:`class<classes>` on the right. The terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is an instance of <class 'bool'>

  :ref:`False<test_what_is_false>` is a boolean_. I change the :ref:`method<functions>` to assertIsInstance_ which checks if the object_ on the left of the parentheses is an instance of the :ref:`class<classes>` on the right

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)
        self.assertIsInstance(False, bool)

  the test passes. I do it again with :ref:`True<test_what_is_true>`

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)
        self.assertIsInstance(False, bool)
        self.assertNotIsInstance(True, bool)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is an instance of <class 'bool'>

  :ref:`True<test_what_is_true>` is a boolean_. I use the assertIsInstance_ :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)
        self.assertIsInstance(False, bool)
        self.assertIsInstance(True, bool)

  and the test passes

* then I add another line to test if :ref:`None` is a boolean_

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)
        self.assertIsInstance(False, bool)
        self.assertIsInstance(True, bool)
        self.assertIsInstance(None, bool)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'bool'>

  I change the :ref:`method<functions>` to make the test pass

  .. code-block:: python

      def test_is_none_a_boolean(self):
          self.assertNotIsInstance(None, bool)

* and change the last two notes I added

  .. code-block:: python

    # NOTES
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
test_is_none_an_integer
*********************************************************************************

red: make it fail
#################################################################################

I add a test to see if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is an integer_

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertIsNone(-1)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: -1 is not None

green: make it pass
#################################################################################

when I change the :ref:`method<functions>`

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertIsNotNone(-1)

the test passes

refactor: make it better
#################################################################################

* I add a new line

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNone(0)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0 is not None

  then I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)

  and the test passes

* I add another line

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNone(1)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 1 is not None

  I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)

  and the test passes

* then I add an instance test

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertNotIsInstance(-1, int)

  int_ is the :ref:`class<classes>` for integers_, the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: -1 is an instance of <class 'int'>

  ``-1`` is for positive integers_. I make the test pass

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(-1, int)
        self.assertIsInstance(0, int)

* then I add another instance test

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(-1, int)
        self.assertNotIsInstance(0, int)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0 is an instance of <class 'int'>

  ``0`` is an integer_. I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(-1, int)
        self.assertIsInstance(0, int)

  and the test passes

* I add another instance test

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(-1, int)
        self.assertIsInstance(0, int)
        self.assertNotIsInstance(1, int)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 1 is an instance of <class 'int'>

  ``1`` is for positive integers_. I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(-1, int)
        self.assertIsInstance(0, int)
        self.assertIsInstance(1, int)

  and the terminal shows passing tests

* one more instance test

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(-1, int)
        self.assertIsInstance(0, int)
        self.assertIsInstance(1, int)
        self.assertIsInstance(None, int)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'int'>

  I make the test pass

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(-1, int)
        self.assertIsInstance(0, int)
        self.assertIsInstance(1, int)
        self.assertNotIsInstance(None, int)

* then I add a new note

  .. code-block:: python

    # NOTES
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
test_is_none_a_float
*********************************************************************************

red: make it fail
#################################################################################

I add a test to see if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a float_

.. code-block:: python

  def test_is_none_a_float(self):
      self.assertIsNone(-0.1)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: -0.1 is not None

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  def test_is_none_a_float(self):
      self.assertIsNotNone(-0.1)

and the test passes

refactor: make it better
#################################################################################

* I add another line

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNone(0.0)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0.0 is not None

  when I change the :ref:`method<functions>` to match

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)

  the test passes

* I add a failing line

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNone(0.1)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0.1 is not None

  after I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)

  the test passes

* time for instance tests

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertNotIsInstance(-0.1, float)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: -0.1 is an instance of <class 'float'>

  ``-0.1`` is for negative floating point numbers. I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)

  and the test passes

* I add the next instance test

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)
        self.assertNotIsInstance(0.0, float)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0.0 is an instance of <class 'float'>

  ``0.0`` is a floating point number. I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)
        self.assertIsInstance(0.0, float)

  and the test passes

* I add another instance test

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)
        self.assertIsInstance(0.0, float)
        self.assertNotIsInstance(0.1, float)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0.1 is an instance of <class 'float'>

  ``0.1`` is for positive floating point numbers. I make the test pass

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)
        self.assertIsInstance(0.0, float)
        self.assertIsInstance(0.1, float)

* then I add one more line

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)
        self.assertIsInstance(0.0, float)
        self.assertIsInstance(0.1, float)
        self.assertIsInstance(None, float)

  and get :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'float'>

  when I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)
        self.assertIsInstance(0.0, float)
        self.assertIsInstance(0.1, float)
        self.assertNotIsInstance(None, float)

  the test passes

* time for a new note

  .. code-block:: python

    # NOTES
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
test_is_none_a_string
*********************************************************************************

red: make it fail
#################################################################################

I add a test to see if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a string_

.. code-block:: python

  def test_is_none_a_string(self):
      self.assertIsNone('')

and the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: '' is not None

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  def test_is_none_a_string(self):
      self.assertIsNotNone('')

and the test passes

refactor: make it better
#################################################################################

* then I add another line

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNone("text")

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'text' is not None

  I change the :ref:`method<functions>` to match

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")

  and the test passes

* I add a failing line for an instance test

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertNotIsInstance('', str)

  str_ is the :ref:`class<classes>` for strings_, the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '' is an instance of <class 'str'>

  ``''`` is the empty string_. I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance('', str)

  and the test passes

* I add another line

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance('', str)
        self.assertNotIsInstance("text", str)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'text' is an instance of <class 'str'>

  ``'text'`` is a string_, then I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance('', str)
        self.assertIsInstance("text", str)

  and the test passes. A string_ is any character(s) inside single, double or triple quotes, for example

  - ``'single quotes'``
  - ``'''triple single quotes'''``
  - ``"double quotes"``
  - ``"""triple double quotes"""``

  see :ref:`quotes` for more

* I add one more instance test

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance('', str)
        self.assertIsInstance("text", str)
        self.assertIsInstance(None, str)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'str'>

  when I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance('', str)
        self.assertIsInstance("text", str)
        self.assertNotIsInstance(None, str)

  the test passes

* and I add a note

  .. code-block:: python

    # NOTES
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
test_is_none_a_tuple
*********************************************************************************

red: make it fail
#################################################################################

I add a test to see if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a tuple_

.. code-block:: python

  def test_is_none_a_tuple(self):
      self.assertIsNone(())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: () is not None

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  def test_is_none_a_tuple(self):
      self.assertIsNotNone(())

and the test passes

refactor: make it better
#################################################################################

* I add a failing line

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNone((1, 2, 3, 'n'))

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (1, 2, 3, 'n') is not None

  I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))

  and the test passes

* I add an instance test

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))
        self.assertNotIsInstance((), tuple)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: () is an instance of <class 'tuple'>

  ``()`` is the empty tuple_. I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))
        self.assertIsInstance((), tuple)
        self.assertNotIsInstance((1, 2, 3, 'n'), tuple)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (1, 2, 3, 'n') is an instance of <class 'tuple'>

  ``(1, 2, 3, 'n')`` is a tuple_. I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))
        self.assertIsInstance((), tuple)
        self.assertIsInstance((1, 2, 3, 'n'), tuple)

  and the test passes

* I add one more instance test

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))
        self.assertIsInstance((), tuple)
        self.assertIsInstance((1, 2, 3, 'n'), tuple)
        self.assertIsInstance(None, tuple)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'tuple'>

  then I change the :ref:`method<functions>` to make the test pass

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))
        self.assertIsInstance((), tuple)
        self.assertIsInstance((1, 2, 3, 'n'), tuple)
        self.assertNotIsInstance(None, tuple)

* and I add a note

  .. code-block:: python

    # NOTES
    # None is NOT a tuple
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

  it is safe to say that so far it looks like `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ and not anything else

----

*********************************************************************************
test_is_none_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a new test for :ref:`lists`

.. code-block:: python

  def test_is_none_a_list(self):
      self.assertIsNone([])

and the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [] is not None

green: make it pass
#################################################################################


when I change the :ref:`method<functions>` to match

.. code-block:: python

  def test_is_none_a_list(self):
      self.assertIsNotNone([])

the test passes

refactor: make it better
#################################################################################

* I add another failing line

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNone([1, 2, 3, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: [1, 2, 3, 'n'] is not None

  I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])

  and the test passes

* I add an instance test

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])
        self.assertNotIsInstance([], list)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: [] is an instance of <class 'list'>

  ``[]`` is the empty list_. I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])
        self.assertIsInstance([], list)

  and the test passes

* then I add another instance test

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])
        self.assertIsInstance([], list)
        self.assertNotIsInstance([1, 2, 3, 'n'], list)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: [1, 2, 3, 'n'] is an instance of <class 'list'>

  ``[1, 2, 3, 'n']`` is a list_

  I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])
        self.assertIsInstance([], list)
        self.assertIsInstance([1, 2, 3, 'n'], list)

  and the test passes

* I add one more line

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])
        self.assertIsInstance([], list)
        self.assertIsInstance([1, 2, 3, 'n'], list)
        self.assertIsInstance(None, list)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'list'>

  I change the line to make the test pass

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])
        self.assertIsInstance([], list)
        self.assertIsInstance([1, 2, 3, 'n'], list)
        self.assertNotIsInstance(None, list)

  then add a new note

  .. code-block:: python

    # NOTES
    # None is NOT a list
    # None is NOT a tuple
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
test_is_none_a_set
*********************************************************************************

red: make it fail
#################################################################################

I add a new test to see if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a set_

.. code-block:: python

  def test_is_none_a_set(self):
      self.assertIsNone(set())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: set() is not None

green: make it pass
#################################################################################

I change the :ref:`method<functions>` to match the message

.. code-block:: python

  def test_is_none_a_set(self):
      self.assertIsNotNone(set())

and the test passes

refactor: make it better
#################################################################################

* I add another line

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNone({1, 2, 3, 'n'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {1, 2, 3, 'n'} is not NOne

  I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({1, 2, 3, 'n'})

  and the test passes

* then I add an instance test

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({1, 2, 3, 'n'})
        self.assertNotIsInstance({1, 2, 3, 'n'}, set)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {1, 2, 3, 'n'} is an instance of <class 'set'>

  I make the test pass

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({1, 2, 3, 'n'})
        self.assertIsInstance({1, 2, 3, 'n'}, set)

* then add another instance test

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({1, 2, 3, 'n'})
        self.assertIsInstance({1, 2, 3, 'n'}, set)
        self.assertIsInstance(None, set)

  which gives me :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'set'>

  I change the :ref:`method<functions>` to make it pass

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertNotIsInstance(None, set)

* then add a note

  .. code-block:: python

    # NOTES
    # None is NOT a set
    # None is NOT a list
    # None is NOT a tuple
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
test_is_none_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

One last test to see if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a :ref:`dictionary<dictionaries>`

.. code-block:: python

  def test_is_none_a_dictionary(self):
      self.assertIsNone(dict())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {} is not None

wait a minute! ``{}`` is how Python is for sets_, it also is for :ref:`dictionaries` this way, with a difference. I will show this in a little bit

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  def test_is_none_a_dictionary(self):
      self.assertIsNotNone(dict())

and the test passes

refactor: make it better
#################################################################################

* then I add another line

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNone({'key': 'value'})

  and get :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} is not None

  when I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})

  the terminal shows passing tests

* and I add an instance test

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})
        self.assertNotIsInstance({}, dict)

  dict_ is the :ref:`class<classes>` for :ref:`dictionaries`, the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {} is an instance of <class 'dict'>

  ``{}`` is the empty :ref:`dictionary<dictionaries>`. I change the :ref:`method<functions>` to make it pass

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})
        self.assertIsInstance({}, dict)

* then I add another instance test

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})
        self.assertIsInstance({}, dict)
        self.assertNotIsInstance({'key': 'value'}, dict)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'key': 'value'} is an instance of <class 'dict'>

  ``{'key': 'value'}`` is a :ref:`dictionary<dictionaries>` with ``:`` separating the key on the left from the value on the right, you can add more key-value pairs separating them with commas, there is more on this in the :ref:`dictionaries` chapter. I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})
        self.assertIsInstance({}, dict)
        self.assertIsInstance({'key': 'value'}, dict)

  and the test passes

* time for the last instance test

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})
        self.assertIsInstance({}, dict)
        self.assertIsInstance({'key': 'value'}, dict)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'dict'>

  I make the test pass

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertNotIsInstance(None, dict)

* then I add a note

  .. code-block:: python

    # NOTES
    # None is NOT a dictionary
    # None is NOt a set
    # None is NOT a list
    # None is NOT a tuple
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
review
*********************************************************************************

I ran tests to show what `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is and what it is not

Would you like to test :ref:`booleans`?

----

:doc:`/code/code_none`
