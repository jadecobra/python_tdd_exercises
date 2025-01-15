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
test_none_is_none
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

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_none.py:7`` with the mouse to open it in the editor
* then change ``True`` to ``False`` to make the test pass

.. code-block:: python

  import unittest


  class TestNone(unittest.TestCase):

      def test_none_is_none(self):
          self.assertIsNotNone(None)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: unexpectedly None

assertIsNotNone_ checks that the input given is NOT `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

green: make it pass
#################################################################################

* When I use the assertIsNone_ :ref:`method<functions>` which checks that the given input is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

  .. code-block:: python

    def test_none_is_none(self):
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

I add a new test to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with :ref:`booleans`

.. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNone(True)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: True is not None

green: make it pass
#################################################################################

I make the test pass

.. code-block:: python

  def test_is_none_a_boolean(self):
      self.assertIsNotNone(True)

then add a note

.. code-block:: python

  # NOTES
  # True is not None
  # None is None

refactor: make it better
#################################################################################

* I add another failing line

  .. code-block:: python

      def test_is_none_a_boolean(self):
          self.assertIsNotNone(True)
          self.assertIsNone(False)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not None

* then I add another note

  .. code-block:: python

    # NOTES
    # False is not None
    # True is not None
    # None is None

* :ref:`booleans` are represented by the bool_ :ref:`class <classes>` Python. I can add a test with the `unittest.TestCase.assertIsInstance`_ :ref:`method<functions>` to check if something is is an instance of a :ref:`class<classes>`

  .. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(True)
        self.assertIsNotNone(False)
        self.assertIsInstance(None, bool)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not an instance of <class 'bool'>

* I change the :ref:`method<functions>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python

      def test_is_none_a_boolean(self):
          self.assertIsNotNone(True)
          self.assertIsNotNone(False)
          self.assertNotIsInstance(None, bool)

  `unittest.TestCase.assertNotIsInstance`_ checks if something is NOT an instance of the given :ref:`class <classes>`

* I change the notes

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

I add a new test to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with an integer_

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertIsNone(-1)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: -1 is not None

green: make it pass
#################################################################################

I use assertIsNotNone_

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertIsNotNone(-1)

and the test passes

refactor: make it better
#################################################################################

* I add another failing line

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNone(0)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0 is not None

  and I change the line to make the test pass

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)

  then add another failing line

  .. code-block:: python

    def test_is_none_an_integer(self):
      self.assertIsNotNone(-1)
      self.assertIsNotNone(0)
      self.assertIsNone(1)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 1 is not None

  when I change the :ref:`method<functions>`

  .. code-block:: python

    def test_is_none_an_integer(self):
      self.assertIsNotNone(-1)
      self.assertIsNotNone(0)
      self.assertIsNotNone(1)

  the test passes

* integers_ are represented by the int_ :ref:`class <classes>`, I can add an instance test like I did with :ref:`booleans`

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
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
        self.assertNotIsInstance(None, int)

* then add a note

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

I add a new test to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with floats_

.. code-block:: python

  def test_is_none_a_float(self):
      self.assertIsNone(-1.2)

the terminal shows :ref:`AssertionError`

.. code-block::

  AssertionError: -1.2 is not None

green: make it pass
#################################################################################

I change the line to make the test pass

.. code-block:: python

  def test_is_none_a_float(self):
      self.assertIsNotNone(-1.2)

refactor: make it better
#################################################################################

* then I add a new failing line

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-1.2)
        self.assertIsNone(0.3)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0.3 is not None

* floats_ are represented by the float_ :ref:`class <classes>` in Python, I can do an instance test

  .. code-block:: python

      def test_is_none_a_float(self):
          self.assertIsNotNone(-1.1)
          self.assertIsNotNone(0.2)
          self.assertIsInstance(None, float)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not an instance of <class 'float'>

* I change the line to make the test pass

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-1.2)
        self.assertIsNotNone(0.3)
        self.assertNotIsInstance(None, float)

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

I add a test for to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with a string_, which is any character(s) inside single, double or triple quotes, for example

* ``'single quotes'``
* ``'''triple single quotes'''``
* ``"double quotes"``
* ``"""triple double quotes"""``

see :ref:`quotes` for a more details

.. code-block:: python

  def test_is_none_a_string(self):
      self.assertIsNone('')

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: '' is not None

green: make it pass
#################################################################################

I change the :ref:`method<functions>` to make the test pass

.. code-block:: python

  def test_is_none_a_string(self):
      self.assertIsNotNone('')

refactor: make it better
#################################################################################

* then add a new line

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNone("text")

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: "text" is not None

  I make the test pass

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")

* strings_ are represented by the str_, time for an instance test

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance(None, str)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not an instance of <class 'str'>

  I make the test pass

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertNotIsInstance(None, str)

* then add a note

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

I add a new test to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with a tuple_

.. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNone(())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: () is not None

``()`` is how tuples_ are represented in Python

green: make it pass
##################################################################################

I make the test pass

.. code-block:: python

  def test_is_none_a_tuple(self):
      self.assertIsNotNone(())

refactor: make it better
##################################################################################

* then I add a failing line

  .. code-block:: python

      def test_is_none_a_tuple(self):
          self.assertIsNotNone(())
          self.assertIsNone((1, 2, 3, 'n'))

  the terminal shows :ref:`AssertionError`

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
        self.assertIsInstance(None, tuple)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not an instance of <class 'tuple'>

  I make the test pass

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))
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

Based on what I have seen so far, it is safe to assume that `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ and is not anything else

----

*********************************************************************************
test_is_none_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a new test to check if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a :ref:`list <lists>`

.. code-block:: python

  def test_is_none_a_list(self):
      self.assertIsNone([])
      self.assertIsNone([1, 2, 3, "n"])
      self.assertIsInstance(None, list)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [] is not None

``[]`` is how :ref:`lists` are represented in Python

green: make it pass
#################################################################################

* I have done this dance a few times, I change the :ref:`method<functions>` to make it pass

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])

  refactor: make it better


  then I add another line
  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNone([1, 2, 3, "n"])

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: [1, 2, 3, 'n'] is not None

* I add an instance test

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, "n"])
        self.assertIsInstance(None, list)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not an instance of <class 'list'>

  I change the line to make the test pass

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, "n"])
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

following the same pattern from earlier, I add a new failing test for sets_

.. code-block:: python

  def test_is_none_a_set(self):
      self.assertIsNone(set())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: set() is not None


green: make it pass
#################################################################################

I make the test pass

.. code-block:: python

  def test_is_none_a_set(self):
      self.assertIsNotNone(set())

refactor: make it better

* then add another line

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNone({1, 2, 3, "n"})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {1, 2, 3, "n"} is not None

  I change it to make it pass

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({1, 2, 3, "n"})

* I add an instance test

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({1, 2, 3, "n"})
        self.assertIsInstance(None, set)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not an instance of <class 'set'>

  I change the line to make the test pass

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({1, 2, 3, "n"})
        self.assertIsNotInstance(None, set)

* then I add a note

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

I add a new test to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with :ref:`dictionaries`

.. code-block:: python

  def test_is_none_a_dictionary(self):
      self.assertIsNone(dict())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {} is not None

* ``dict()`` is one way to make an empty :ref:`dictionary <dictionaries>` in Python
* ``{}`` is how :ref:`dictionaries`  are represented in Python. Wait a minute! sets_ are also represented with ``{}``. The difference is that :ref:`dictionaries` hold key-value pairs
* do you want to :ref:`read more about dictionaries? <dictionaries>`

green: make it pass
#################################################################################

I make the test pass

.. code-block:: python

  def test_is_none_a_dictionary(self):
      self.assertIsNotNone(dict())

refactor: make it better

* then I add another line

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNoneNone(dict())
        self.assertIsNone({
            "a": 1,
            "b": 2,
            "c": 3,
            "n": "n"
        })

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: { "a": 1, "b": 2, "c": 3, "n": "n" } is not None

  I make the test pass

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({
            "a": 1,
            "b": 2,
            "c": 3,
            "n": "n"
        })

* then add an instance test

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({
            "a": 1,
            "b": 2,
            "c": 3,
            "n": "n"
        })
        self.assertIsInstance(None, dict)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not an instance of <class 'dict'>

  I make the test pass

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({
            "a": 1,
            "b": 2,
            "c": 3,
            "n": "n"
        })
        self.assertIsNotInstance(None, dict)

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

I ran tests to show what `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is and what it is not

Would you like to test :ref:`booleans`?

----

:doc:`/code/code_none`
