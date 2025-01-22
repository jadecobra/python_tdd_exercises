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

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_none.py:7`` with the mouse to open it in the editor
* then change ``True`` to ``False`` to make the test pass

.. code-block:: python

  import unittest


  class TestNone(unittest.TestCase):

      def test_what_is_none(self):
          self.assertIsNotNone(None)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: unexpectedly None

assertIsNotNone_ checks that the input given is NOT `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

green: make it pass
#################################################################################

* When I use the assertIsNone_ :ref:`method<functions>` which checks that the given input is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

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

I add a new test with the assertNotIsInstance_ :ref:`method<functions>` from the `unittest.TestCase`_ :ref:`class<classes>` that checks if something is an instance of a given :ref:`class<classes>`

.. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsInstance(None, bool)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: None is not an instance of <class 'bool'>

green: make it pass
#################################################################################

* I use the assertIsInstance_ :ref:`method<functions>` to make the test pass

  .. code-block:: python

      def test_is_none_a_boolean(self):
          self.assertNotIsInstance(None, bool)

* then add a note

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

I add a new test to see if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is an integer_

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertIsInstance(None, int)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: None is not an instance of <class 'int'>

green: make it pass
#################################################################################

* I make the test pass

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertNotIsInstance(None, int)

* then add a new note

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
      self.assertIsInstance(None, float)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: None is not an instance of <class 'float'>

green: make it pass
#################################################################################

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

I add a test for to see if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a string_, which is any character(s) inside single, double or triple quotes, for example

* ``'single quotes'``
* ``'''triple single quotes'''``
* ``"double quotes"``
* ``"""triple double quotes"""``

see :ref:`quotes` for a more details

.. code-block:: python

  def test_is_none_a_string(self):
      self.assertIsInstance(None, str)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: None is not an instance of <class 'str'>

* I make the test pass

  .. code-block:: python

    def test_is_none_a_string(self):
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

I add a test to see if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a tuple_

.. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsInstance(None, tuple)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: None is not an instance of <class 'tuple'>

red: make it fail
#################################################################################

* I change the :ref:`method<functions>` to make the test pass

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

* I change the line to make the test pass

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertNotIsInstance(None, set)

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

*********************************************************************************
review
*********************************************************************************

I ran tests to show what `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is and what it is not

Would you like to test :ref:`booleans`?

----

:doc:`/code/code_none`
