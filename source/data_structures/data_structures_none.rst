
Data Structures: None
=====================

What is None?
-------------

I will write some tests to explore `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ which is an object used to represent the absence of a value

RED: make it fail
^^^^^^^^^^^^^^^^^

I create a file called ``test_data_structures.py`` in the ``tests`` folder

.. code-block:: python

  import unittest


  class TestDataStructures(unittest.TestCase):

      def test_none_is_none(self):
          self.assertIsNotNone(None)

the terminal shows an :doc:`/exceptions/AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the ``assert`` statement in ``test_none_is_none`` to make it pass

.. code-block:: python

  class TestDataStructures(unittest.TestCase):

      def test_none_is_none(self):
          self.assertIsNone(None)

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

There are other python objects I can compare with `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ to learn more about what it is or is not

Is None a boolean?
------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with :doc:`booleans </data_structures/data_structures_booleans>`

.. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNone(True)
        self.assertIsNone(False)

the terminal shows an :doc:`/exceptions/AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change ``test_is_none_a_boolean`` to make the tests pass

.. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(True)
        self.assertIsNotNone(False)

From the tests I can see that

* :doc:`False </data_structures/data_structures_booleans>` is not `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
* :doc:`True </data_structures/data_structures_booleans>` is not `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

:doc:`booleans </data_structures/data_structures_booleans>` are instances of the `bool <https://docs.python.org/3/library/functions.html#bool>`_ :doc:`class </classes?>` in python so I can do an instance test using another `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ :doc:`method </functions/functions>` to check if an `object <https://docs.python.org/3/glossary.html#term-object>`_ is an instance of the `bool <https://docs.python.org/3/library/functions.html#bool>`_ :doc:`class </classes>`


* RED: make it fail

  I add a test with ``self.assertIsInstance`` to ``test_is_none_a_boolean``

  .. code-block:: python

      def test_is_none_a_boolean(self):
          self.assertIsNotNone(True)
          self.assertIsNotNone(False)
          self.assertIsInstance(None, bool)

  I now see an :doc:`/exceptions/AssertionError` in the terminal because `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an instance of a :doc:`boolean </data_structures/data_structures_booleans>`

  .. code-block:: python

    AssertionError: None is not an instance of <class 'bool'>

* GREEN: make it pass

  I change ``test_is_none_a_boolean`` to make the test pass

  .. code-block:: python

      def test_is_none_a_boolean(self):
          self.assertIsNotNone(True)
          self.assertIsNotNone(False)
          self.assertNotIsInstance(None, bool)

* I can summarize what I know about `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ from the tests as - it is not a :doc:`boolean </data_structures/data_structures_booleans>` and it is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

I want to know if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is equal to any of the other data types in python, i.e. `int <https://docs.python.org/3/library/functions.html#int>`_, `float <https://docs.python.org/3/library/functions.html#float>`_, `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_, `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_, :doc:`list </data_structures/data_structures_lists>`, `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ or :doc:`dict </data_structures/data_structures_dictionaries>`

Is None an integer?
-------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with `int <https://docs.python.org/3/library/functions.html#int>`_

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertIsNone(-1)
      self.assertIsNone(0)
      self.assertIsNone(1)

the terminal shows an :doc:`/exceptions/AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change ``test_is_none_an_integer`` to make it pass

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertIsNotNone(-1)
      self.assertIsNotNone(0)
      self.assertIsNotNone(1)

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

`integers <https://docs.python.org/3/library/functions.html#int>`_ are represented by the class `int <https://docs.python.org/3/library/functions.html#int>`_ in python so I can do an instance test like I did with :doc:`booleans </data_structures/data_structures_booleans>`


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

  I change ``test_is_none_an_integer`` to make the test pass

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertNotIsInstance(None, int)

* summarizing what I know about `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ so far from the tests

  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an integer
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/data_structures_booleans>`
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

Is None a string?
-----------------

I add a test for `strings <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_. A string is any character(s) that are enclosed by single, double or triple quotes for example

* ``'single quotes'``
* ``"double quotes"``
* ``'''triple single quotes'''``
* ``"""triple double quotes"""``

see :doc:`/conventions` for a little more details

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new failing test to ``test_data_structures.py`` to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_

.. code-block:: python

  def test_is_none_a_string(self):
      self.assertIsNone('')
      self.assertIsNone("text")

and the terminal shows an :doc:`/exceptions/AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change ``test_is_none_a_string`` to make it pass

.. code-block:: python

  def test_is_none_a_string(self):
      self.assertIsNotNone('')
      self.assertIsNotNone("text")

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

`strings <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ are represented by the `str <https://docs.python.org/3/library/stdtypes.html#str>`_ class keyword in python, I will add a test to check if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is an instance of the `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ class


* RED: make it fail

  I change ``test_is_none_a_string`` and the terminal shows a failing test

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance(None, str)

* GREEN: make it pass

  I change the failing line in the test to make it pass

  .. code-block:: python

      def test_is_none_a_string(self):
          self.assertIsNotNone('')
          self.assertIsNotNone("text")
          self.assertNotIsInstance(None, str)

* from the tests knowledge of `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ has grown to

  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a string
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an integer
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/data_structures_booleans>`
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

Is None a tuple?
----------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test to ``test_data_structures.py``

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

* I change the first line in ``test_is_none_a_tuple`` to make it pass

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())

  and the terminal displays an :doc:`/exceptions/AssertionError` for the second line

  .. code-block:: python

    AssertionError: (1, 2, 3, 'n') is not None

  because the `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ that contains the four elements ``1, 2, 3, 'n'`` is not `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
* I change the failing line in ``test_is_none_a_tuple``

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))

  the terminal now shows another :doc:`/exceptions/AssertionError` for the next line in the test but with a different message

  .. code-block:: python

    AssertionError: None is not an instance of <class 'tuple'>

* I change the failing line in the test to make it pass

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))
        self.assertNotIsInstance(None, tuple)

* From the tests I can see that in python

  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/data_structures_booleans>`
  * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Based on what I have seen so far, it is safe to assume that `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is only `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ and is not any other data structure, I want to test if this assumption is false.

Is None a list(array)?
----------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test to the series of tests

.. code-block:: python

  def test_is_none_a_list(self):
      self.assertIsNone([])
      self.assertIsNone([1, 2, 3, "n"])
      self.assertIsInstance(None, list)

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: [] is not None


``[]`` is how :doc:`lists` are represented in python


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I have done this dance a few times now so I can change ``test_is_none_a_list`` to make it pass. With the passing tests the knowledge of `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is changed to


* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`list </data_structures/data_structures_lists>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/data_structures_booleans>`
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

I change the tests to make them pass and I can change the knowledge of `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ to state that


* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`list </data_structures/data_structures_lists>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/data_structures_booleans>`
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


* ``dict()`` is one way to create an empty :doc:`dictionary </data_structures/data_structures_dictionaries>` in python
* ``{}`` is how :doc:`dictionaries </data_structures/data_structures_dictionaries>`  are represented in python. Wait a minute! sets are also represented with ``{}``, the difference is that dictionaries contain key/value pairs
* Do you want to :doc:`read more about dictionaries </data_structures/data_structures_dictionaries>`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the tests to make them pass and can state from the tests that


* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`dictionary </data_structures/data_structures_dictionaries>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`list </data_structures/data_structures_lists>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/data_structures_booleans>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
