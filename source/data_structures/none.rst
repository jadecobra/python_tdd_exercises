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

`None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is an object used to represent the absence of a value

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``non`` as the name of the project

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

* When I use the assertIsNone_ :ref:`method<functions>` which checks that its input is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

  .. code-block:: python

    def test_what_is_none(self):
        self.assertIsNone(None)

  the test passes

* I add a note

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

* I add a failing test

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNone(False)

  the terminal responds with :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not None

* then I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # NOTES
    # False is NOT None
    # None is None

green: make it pass
#################################################################################

I change the :ref:`method`

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

  I add a note

  .. code-block:: python

    # NOTES
    # True is NOT None
    # False is NOT None
    # None is None

  when I change the :ref:`method`

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)

  the test passes

* the `unittest.TestCase`_ :ref:`class<classes>` has two :ref:`methods<functions>` I can use to test if an object_ is an instance of a :ref:`class<classes>`

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)
        self.assertNotIsInstance(False, bool)

  the assertNotIsInstance_ :ref:`method<functions>` checks if the object_ on the left in the parentheses is NOT an instance of the :ref:`class<classes>` on the right. The terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is an instance of <class 'bool'>

  :ref:`False<test_what_is_false>` is a boolean_. I change the :ref:`method<functions>` to assertIsInstance_ which checks that the object_ on the left in the parentheses is an instance of the :ref:`class<classes>` on the right

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)
        self.assertIsInstance(False, bool)

  and the test passes. I do it again with :ref:`True<test_what_is_true>`

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)
        self.assertIsInstance(False, bool)
        self.assertNotIsInstance(True, bool)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is an instance of <class 'bool'>

  :ref:`True<test_what_is_true>` is a boolean_. I use the assertIsInstance_ :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)
        self.assertIsInstance(False, bool)
        self.assertIsInstance(True, bool)

  and the test passes

* I add another line to test if :ref:`None` is a boolean_

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)
        self.assertIsInstance(False, bool)
        self.assertIsInstance(True, bool)
        self.assertIsInstance(None, bool)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not an instance of <class 'bool'>

  I change the :ref:`method<functions>` to make the test pass

  .. code-block:: python

      def test_is_none_a_boolean(self):
          self.assertNotIsInstance(None, bool)

* and change the last two notes

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

Time to test if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is an integer_

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertIsNone(-1)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: -1 is not None

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertIsNotNone(-1)

and the test passes

red: make it better
#################################################################################

* I add a new line

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNone(0)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0 is not None

  when I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)

  the test passes

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

* I add an instance test

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertNotIsInstance(-1, int)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: -1 is an instance of <class 'int'>

  - int_ is the :ref:`class<classes>` for integers_
  - ``-1`` is an integer_ representing positive integers_

  I make the test pass

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

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0 is an instance of <class 'int'>

  ``0`` is an integer_

  I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(-1, int)
        self.assertIsInstance(0, int)

  and the test passes

* I add an instance test again

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(-1, int)
        self.assertIsInstance(0, int)
        self.assertNotIsInstance(1, int)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 1 is an instance of <class 'int'>

  ``1`` is an integer_ representing the positive integers_

  when I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(-1, int)
        self.assertIsInstance(0, int)
        self.assertIsInstance(1, int)

  the terminal shows passing tests

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

  .. code-block:: python

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

I add a new test to see if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a float_

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

  I change the :ref:`method<functions>` to match

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)

  and the test passes

* I add a line again

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNone(0.1)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0.1 is not None

  after I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)

  the test passes

* time for the instance tests

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertNotIsInstance(-0.1, float)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: -0.1 is an instance of <class 'float'>

  ``-0.1`` is a float_ representing negative floating point numbers

  I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)

  and the test passes

* I add another instance test

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)
        self.assertNotIsInstance(0.0, float)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0.0 is an instance of <class 'float'>

  ``0.0`` is a float_

  I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)
        self.assertIsInstance(0.0, float)

  and the test passes

* I add another failing line

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)
        self.assertIsInstance(0.0, float)
        self.assertNotIsInstance(0.1, float)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0.1 is an instance of <class 'float'>

  ``0.1`` is a float_ representing positive floating point numbers

  I make the test pass

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)
        self.assertIsInstance(0.0, float)
        self.assertIsInstance(0.1, float)

* I add one more failing line

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

  .. code-block:: python

    AssertionError: None is not an instance of <class 'float'>

  then I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)
        self.assertIsInstance(0.0, float)
        self.assertIsInstance(0.1, float)
        self.assertNotIsInstance(None, float)

  and the test passes

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

the terminal shows :ref:`AssertionError`

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

* I add a line again

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertNotIsInstance('', str)

  str_ is the :ref:`class<classes>` for strings_, the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '' is an instance of <class 'str'>

  ``''`` is a string_, it is the empty string_. I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance('', str)

  the test passes

* I add another line

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance('', str)
        self.assertNotIsInstance("text", str)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'text' is an instance of <class 'str'>

  ``'text'`` is a string_, then I add a :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance('', str)
        self.assertIsInstance("text", str)

  and the test passes. A string_ is any character(s) inside single, double or triple quotes, for example
  * ``'single quotes'``
  * ``'''triple single quotes'''``
  * ``"double quotes"``
  * ``"""triple double quotes"""``

  see :ref:`quotes` for a more details

* I add one more instance test

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance('', str)
        self.assertIsInstance("text", str)
        self.assertIsInstance(None, str)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

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

* then I add a note

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
        self.assertIsInstance(None, tuple)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: None is not an instance of <class 'tuple'>

red: make it fail
#################################################################################

* then I change the :ref:`method<functions>` to make the test pass

  .. code-block:: python

    def test_is_none_a_tuple(self):
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

Based on what I have seen so far, I think it is safe to say that `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ and not anything else

----

*********************************************************************************
test_is_none_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a new test to see if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a :ref:`list <lists>`

.. code-block:: python

  def test_is_none_a_list(self):
      self.assertIsInstance(None, list)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: None is not an instance of <class 'list'>

green: make it pass
#################################################################################

* I change the line to make the test pass

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsInstance(None, list)

* then add a new note

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

I add a new failing test to see if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a set_

.. code-block:: python

  def test_is_none_a_set(self):
      self.assertIsInstance(None, set)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: None is not an instance of <class 'set'>

green: make it pass
#################################################################################

* I make it pass

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertNotIsInstance(None, set)

* then add another note

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

I add a new test to see if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a :ref:`<dictionary> dictionaries`

.. code-block:: python

  def test_is_none_a_dictionary(self):
      self.assertIsInstance(None, dict)

the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not an instance of <class 'dict'>

green: make it pass
#################################################################################

* I make the test pass

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertNotIsInstance(None, dict)

* and I add a note

  .. code-block:: python

    # NOTES
    # None is NOT a dictionary
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
