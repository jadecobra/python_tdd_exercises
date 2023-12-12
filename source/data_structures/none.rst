
Data Structures: None
=====================

What is None?
-------------

The tests in this chapter explore `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_, which is an object used to represent the absence of a value

RED: make it fail
^^^^^^^^^^^^^^^^^

I create a file called ``test_none.py`` in the ``tests`` folder

.. code-block:: python

  import unittest


  class TestDataStructures(unittest.TestCase):

      def test_none_is_none(self):
          self.assertIsNotNone(None)

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  E       AssertionError: unexpectedly None


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

When I change the ``assert`` statement in ``test_none_is_none`` to ``self.assertIsNone`` which compares the given input with `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

.. code-block:: python

  class TestDataStructures(unittest.TestCase):

      def test_none_is_none(self):
          self.assertIsNone(None)

the test passes

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

There are other python objects I can compare with `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ to learn more about what it is or is not

Is None a boolean?
------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with :doc:`booleans </data_structures/booleans>`

.. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNone(True)
        self.assertIsNone(False)

the terminal shows an :doc:`/exceptions/AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change ``test_is_none_a_boolean`` using ``self.assertIsNotNone`` to make the tests pass

.. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(True)
        self.assertIsNotNone(False)

- `unittest.TestCase.assertIsNotNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNotNone>`_ checks that the object provided as input is not `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

From the tests I can see that

* :doc:`False </data_structures/booleans>` is not `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
* :doc:`True </data_structures/booleans>` is not `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

:doc:`booleans </data_structures/booleans>` are instances of the `bool <https://docs.python.org/3/library/functions.html#bool>`_ :doc:`class </classes/classes>` in Python so I can do an instance test using another `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ :doc:`method </functions/functions>` to check if an `object <https://docs.python.org/3/glossary.html#term-object>`_ is an instance of the `bool <https://docs.python.org/3/library/functions.html#bool>`_ :doc:`class </classes/classes>`


* RED: make it fail

  I add a test with ``self.assertIsInstance`` to ``test_is_none_a_boolean``

  .. code-block:: python

      def test_is_none_a_boolean(self):
          self.assertIsNotNone(True)
          self.assertIsNotNone(False)
          self.assertIsInstance(None, bool)

  I now see an :doc:`/exceptions/AssertionError` in the terminal because `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an instance of a :doc:`boolean </data_structures/booleans>`

  .. code-block:: python

    AssertionError: None is not an instance of <class 'bool'>

* GREEN: make it pass

  I change ``test_is_none_a_boolean`` to make the test pass

  .. code-block:: python

      def test_is_none_a_boolean(self):
          self.assertIsNotNone(True)
          self.assertIsNotNone(False)
          self.assertNotIsInstance(None, bool)

From the tests I can summarize what I know as `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans>` and it is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

I want to know if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is equal to any of the other data types in Python like `int <https://docs.python.org/3/library/functions.html#int>`_, `float <https://docs.python.org/3/library/functions.html#float>`_, `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_, `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_, :doc:`list </data_structures/lists>`, `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ or :doc:`dict </data_structures/dictionaries>`

Is None an integer?
-------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with `integers <https://docs.python.org/3/library/functions.html#int>`_

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertIsNone(-1)
      self.assertIsNone(0)
      self.assertIsNone(1)

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block::

  E       AssertionError: -1 is not None


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change ``test_is_none_an_integer`` using ``self.assertIsNotNone`` to make it pass

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertIsNotNone(-1)
      self.assertIsNotNone(0)
      self.assertIsNotNone(1)

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

`integers <https://docs.python.org/3/library/functions.html#int>`_ are represented by the class `int <https://docs.python.org/3/library/functions.html#int>`_ in python so I can do an instance test like I did with :doc:`booleans </data_structures/booleans>`


* RED: make it fail

  I add a new line to ``test_is_none_an_integer`` with ``self.assertIsInstance``

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(None, int)

  an :doc:`/exceptions/AssertionError` is displayed in the terminal because `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an instance of `int <https://docs.python.org/3/library/functions.html#int>`_

  .. code-block:: python

    AssertionError: None is not an instance of <class 'int'>

* GREEN: make it pass

  I change ``test_is_none_an_integer`` using ``self.assertNotIsInstance`` to make the test pass

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertNotIsInstance(None, int)

* summarizing what I know about `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ so far from the tests

  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an integer
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans>`
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

Is None a string?
-----------------

I add a test for `strings <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_. A string is any character(s) surrounded by single, double or triple quotes for example

* ``'single quotes'``
* ``"double quotes"``
* ``'''triple single quotes'''``
* ``"""triple double quotes"""``

see :doc:`/conventions` for a little more detail

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new failing test to ``test_none.py`` to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_

.. code-block:: python

  def test_is_none_a_string(self):
      self.assertIsNone('')
      self.assertIsNone("text")

and the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  E       AssertionError: '' is not None


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change ``test_is_none_a_string`` using ``self.assertIsNotNone`` to make it pass

.. code-block:: python

  def test_is_none_a_string(self):
      self.assertIsNotNone('')
      self.assertIsNotNone("text")

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

`strings <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ are represented by the `str <https://docs.python.org/3/library/stdtypes.html#str>`_ class keyword in python, I will add a test to check if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is an instance of the `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ class


* RED: make it fail

  I add a failing test to ``test_is_none_a_string`` with a ``self.assertIsInstance`` statement

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance(None, str)

  and the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    E       AssertionError: None is not an instance of <class 'str'>

* GREEN: make it pass

  To make it pass I replace the failing line with a ``self.assertNotIsInstance`` statement

  .. code-block:: python

      def test_is_none_a_string(self):
          self.assertIsNotNone('')
          self.assertIsNotNone("text")
          self.assertNotIsInstance(None, str)

* from the tests I know that

  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a string
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an integer
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans>`
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

Is None a tuple?
----------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test to ``test_none.py`` to find out if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a `tuple <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_

.. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNone(())
        self.assertIsNone((1, 2, 3, 'n'))
        self.assertIsInstance(None, tuple)

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: () is not None


``()`` is how `tuples <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_ are represented in python

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^^

* I change the failing lines in ``test_is_none_a_tuple`` with ``self.assertIsNotNone`` to make them pass

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))
        self.assertIsInstance(None, tuple)

  and the terminal displays an :doc:`/exceptions/AssertionError` for the instance test

  .. code-block:: python

    AssertionError: None is not an instance of <class 'tuple'>

* I change the failing line using ``self.assertNotIsInstance``  to make it pass

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))
        self.assertNotIsInstance(None, tuple)

* From the tests I can see that in python

  - `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_
  - `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
  - `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
  - `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans>`
  - `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Based on what I have seen so far, it is safe to assume that `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is only `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ and is not any other data structure

Is None a list?
----------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test to the series of tests to check if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a :doc:`list </data_structures/lists>`

.. code-block:: python

  def test_is_none_a_list(self):
      self.assertIsNone([])
      self.assertIsNone([1, 2, 3, "n"])
      self.assertIsInstance(None, list)

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: [] is not None


``[]`` is how :doc:`lists </data_structures/lists>` are represented in python


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I have done this dance a few times now so I can change ``test_is_none_a_list`` with ``self.assertIsNotNone`` and ``self.assertNotIsInstance`` to make it pass.

With the passing tests I know that

* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`list </data_structures/lists>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

Is None a set?
--------------

RED: make it fail
^^^^^^^^^^^^^^^^^

following the same pattern from earlier, I add a new failing test, this time for sets

.. code-block:: python

  def test_is_none_a_set(self):
      self.assertIsNone({})
      self.assertIsNone({1, 2, 3, "n"})
      self.assertIsInstance(None, set)

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: {} is not None

``{}`` is how ``sets`` are represented in python


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the tests to make them pass using ``self.assertIsNotNone`` and ``self.assertNotIsInstance`` and I now know that

* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`list </data_structures/lists>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

Is None a dictionary?
---------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test

.. code-block:: python

  def test_is_none_a_dictionary(self):
      self.assertIsNone(dict())
      self.assertIsNone({
          "a": 1,
          "b": 2,
          "c":  3,
          "n": "n"
      })
      self.assertIsInstance(None, dict)

the terminal displays an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: {} is not None


* ``dict()`` is one way to create an empty :doc:`dictionary </data_structures/dictionaries>` in python
* ``{}`` is how :doc:`dictionaries </data_structures/dictionaries>`  are represented in python. Wait a minute! `sets <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ are also represented with ``{}``, the difference is that :doc:`dictionaries </data_structures/dictionaries>` contain key/value pairs
* Do you want to :doc:`read more about dictionaries </data_structures/dictionaries>`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the tests to make them pass and can see from the tests that

* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`dictionary </data_structures/dictionaries>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`list </data_structures/lists>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_


You now know what `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is and what it is not


:doc:`code/none`