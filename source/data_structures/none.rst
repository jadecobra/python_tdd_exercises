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

.. _test_none_is_none:

test_none_is_none
*********************************************************************************

`None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is an object used to represent the absence of a value

red: make it fail
#################################################################################

I make a file called ``test_none.py`` in the ``tests`` folder with the following text

.. code-block:: python

  import unittest


  class TestNone(unittest.TestCase):

      def test_none_is_none(self):
          self.assertIsNotNone(None)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: unexpectedly None

`unittest.TestCase.assertIsNotNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNotNone>`_ checks that the input given is not `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

green: make it pass
#################################################################################

When I make the ``assertIsNotNone`` to ``assertIsNone`` in ``test_none_is_none``

.. code-block:: python

  class TestNone(unittest.TestCase):

      def test_none_is_none(self):
          self.assertIsNone(None)

the test passes

`unittest.TestCase.assertIsNone`_ checks that the given input is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

refactor: make it better
#################################################################################

There are otherPython `objects <https://docs.python.org/3/glossary.html#term-object>`_ I can compare with `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ to learn more about what it is or is not

----

.. _test_is_none_a_boolean:

test_is_none_a_boolean
*********************************************************************************

red: make it fail
#################################################################################

I add a new test to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with :doc:`booleans </data_structures/booleans/booleans>`

.. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNone(True)
        self.assertIsNone(False)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: True is not None

green: make it pass
#################################################################################

I make ``assertIsNone`` to ``assertIsNotNone`` in ``test_is_none_a_boolean`` to make the tests pass

.. code-block:: python

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(True)
        self.assertIsNotNone(False)

From the tests I see that

* :ref:`False<test_what_is_false>` is not `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
* :ref:`True<test_what_is_true>` is not `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

refactor: make it better
#################################################################################

:doc:`booleans </data_structures/booleans/booleans>` are represented by the `bool <https://docs.python.org/3/library/functions.html#bool>`_ :ref:`class <classes>` in Python. I can add a test with `unittest.TestCase.assertIsInstance <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsInstance>`_ to check if an object_ is an instance of a :ref:`class <classes>`


* red: make it fail

  I add a test with ``self.assertIsInstance`` to ``test_is_none_a_boolean``

  .. code-block:: python

      def test_is_none_a_boolean(self):
          self.assertIsNotNone(True)
          self.assertIsNotNone(False)
          self.assertIsInstance(None, bool)

  the terminal shows :ref:`AssertionError` because `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an instance of a :doc:`boolean </data_structures/booleans/booleans>`

  .. code-block:: python

    AssertionError: None is not an instance of <class 'bool'>

* green: make it pass

  I make ``assertIsInstance`` to ``assertNotIsInstance`` in ``test_is_none_a_boolean`` to make the test pass

  .. code-block:: python

      def test_is_none_a_boolean(self):
          self.assertIsNotNone(True)
          self.assertIsNotNone(False)
          self.assertNotIsInstance(None, bool)

  `unittest.TestCase.assertNotIsInstance <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotIsInstance>`_ checks that a given object_ is NOT an instance of the given :ref:`class <classes>`

From the tests I see that

* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans/booleans>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

refactor: make it better
#################################################################################

I want to know if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is equal to any of the other data types in Python

* is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ an `int <https://docs.python.org/3/library/functions.html#int>`_?
* is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ a `float <https://docs.python.org/3/library/functions.html#float>`_?
* is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_?
* is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_?
* is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ a :doc:`list </data_structures/lists/lists>`?
* is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ a set_?
* is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ a :doc:`dict </data_structures/dictionaries>`?

----

.. _test_is_none_an_integer:

test_is_none_an_integer
*********************************************************************************

red: make it fail
#################################################################################

I add a new test to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with an integer_

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertIsNone(-1)
      self.assertIsNone(0)
      self.assertIsNone(1)

the terminal shows :ref:`AssertionError`

.. code-block::

  AssertionError: -1 is not None


green: make it pass
#################################################################################

I make ``assertIsNone`` to ``assertIsNotNone`` in ``test_is_none_an_integer`` to make it pass

.. code-block:: python

  def test_is_none_an_integer(self):
      self.assertIsNotNone(-1)
      self.assertIsNotNone(0)
      self.assertIsNotNone(1)

refactor: make it better
#################################################################################

:ref:`integers<int>`_ are represented by the `int <https://docs.python.org/3/library/functions.html#int>`_ :ref:`class <classes>` in Python, I can add an instance test like I did with :doc:`booleans </data_structures/booleans/booleans>`


* red: make it fail

  I add a ``self.assertIsInstance`` test to ``test_is_none_an_integer``

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(None, int)

  the terminal shows :ref:`AssertionError` because `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an instance of `int <https://docs.python.org/3/library/functions.html#int>`_

  .. code-block:: python

    AssertionError: None is not an instance of <class 'int'>

* green: make it pass

  I make ``assertIsInstance`` to ``assertNotIsInstance`` in ``test_is_none_an_integer`` to make the test pass

  .. code-block:: python

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertNotIsInstance(None, int)

From the tests I see that

* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans/booleans>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

----

.. _test_is_none_a_float:

test_is_none_a_float
*********************************************************************************

red: make it fail
#################################################################################

I add a new test to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with floats_

.. code-block:: python

  def test_is_none_a_float(self):
      self.assertIsNone(-1.1)
      self.assertIsNone(0.2)

the terminal shows :ref:`AssertionError`

.. code-block::

  AssertionError: -1.1 is not None


green: make it pass
#################################################################################

I make ``assertIsNone`` to ``assertIsNotNone`` in ``test_is_none_a_float`` to make the test pass

.. code-block:: python

  def test_is_none_a_float(self):
      self.assertIsNotNone(-1.1)
      self.assertIsNotNone(0.2)

refactor: make it better
#################################################################################

floats_ are represented by the `float <https://docs.python.org/3/library/functions.html#float>`_ :ref:`class <classes>` in Python, I can do an instance test


* red: make it fail

  I add a ``self.assertIsInstance`` line to ``test_is_none_a_float``

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-1.1)
        self.assertIsNotNone(0.2)
        self.assertIsInstance(None, float)

  the terminal shows :ref:`AssertionError` because `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an instance of `float <https://docs.python.org/3/library/functions.html#float>`_

  .. code-block:: python

    AssertionError: None is not an instance of <class 'float'>

* green: make it pass

  I make ``assertIsInstance`` to ``assertNotIsInstance`` in ``test_is_none_a_float`` to make the test pass

  .. code-block:: python

    def test_is_none_a_float(self):
        self.assertIsNotNone(-1.1)
        self.assertIsNotNone(0.2)
        self.assertNotIsInstance(None, float)

From the tests I see that

- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `float <https://docs.python.org/3/library/functions.html#float>`_
- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans/booleans>`
- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

----

.. _test_is_none_a_string:

test_is_none_a_string
*********************************************************************************

I add a test for `strings <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_. A string is any character(s) inside single, double or triple quotes for example

* ``'single quotes'``
* ``'''triple single quotes'''``
* ``"double quotes"``
* ``"""triple double quotes"""``

see :doc:`/conventions` for a little more detail

red: make it fail
#################################################################################

I add a new failing test to ``test_none.py`` to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_

.. code-block:: python

  def test_is_none_a_string(self):
      self.assertIsNone('')
      self.assertIsNone("text")

and the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: '' is not None


green: make it pass
#################################################################################

I make ``assertIsNone`` to ``assertIsNotNone`` in ``test_is_none_a_string`` to make it pass

.. code-block:: python

  def test_is_none_a_string(self):
      self.assertIsNotNone('')
      self.assertIsNotNone("text")

refactor: make it better
#################################################################################

`strings <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ are represented by the str_ class in Python, I add an instance test


* red: make it fail

  I add a failing test to ``test_is_none_a_string`` with a ``self.assertIsInstance`` statement

  .. code-block:: python

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance(None, str)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not an instance of <class 'str'>

* green: make it pass

  To make it pass I make ``assertIsInstance`` to ``assertNotIsInstance``

  .. code-block:: python

      def test_is_none_a_string(self):
          self.assertIsNotNone('')
          self.assertIsNotNone("text")
          self.assertNotIsInstance(None, str)

From the tests I see that

- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `float <https://docs.python.org/3/library/functions.html#float>`_
- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans/booleans>`
- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

----

.. _test_is_none_a_tuple:

test_is_none_a_tuple
*********************************************************************************

red: make it fail
#################################################################################

I add a new test to ``test_none.py`` to find out if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a `tuple <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_

.. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNone(())
        self.assertIsNone((1, 2, 3, 'n'))
        self.assertIsInstance(None, tuple)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: () is not None


``()`` is how `tuples <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_ are represented in Python

green: make it pass
#################################################################################^

* I make ``assertIsNone`` to ``assertIsNotNone`` in ``test_is_none_a_tuple`` to make the first two lines pass

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))
        self.assertIsInstance(None, tuple)

  and the terminal shows :ref:`AssertionError` for the instance test

  .. code-block:: python

    AssertionError: None is not an instance of <class 'tuple'>

* I make ``assertIsInstance`` to ``assertNotIsInstance`` to make it pass

  .. code-block:: python

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))
        self.assertNotIsInstance(None, tuple)

From the tests I see that

- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_
- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `float <https://docs.python.org/3/library/functions.html#float>`_
- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans/booleans>`
- `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

refactor: make it better
#################################################################################

Based on what I have seen so far, it is safe to assume that `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is only `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ and is not any other data structure

----

.. _test_is_none_a_list:

test_is_none_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a new test to the series of tests to check if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is a :doc:`list </data_structures/lists/lists>`

.. code-block:: python

  def test_is_none_a_list(self):
      self.assertIsNone([])
      self.assertIsNone([1, 2, 3, "n"])
      self.assertIsInstance(None, list)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [] is not None


``[]`` is how :doc:`lists </data_structures/lists/lists>` are represented in Python

green: make it pass
#################################################################################

I have done this dance a few times. I make ``assertIsNone`` to ``assertIsNotNone`` and ``assertIsInstance`` to ``assertNotIsInstance`` in ``test_is_none_a_list`` to make it pass.

With the passing tests I see that

* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`list </data_structures/lists/lists>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `float <https://docs.python.org/3/library/functions.html#float>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans/booleans>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

----

.. _test_is_none_a_set:

test_is_none_a_set
*********************************************************************************

red: make it fail
#################################################################################

following the same pattern from earlier, I add a new failing test for `sets <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_

.. code-block:: python

  def test_is_none_a_set(self):
      self.assertIsNone(set())
      self.assertIsNone({1, 2, 3, "n"})
      self.assertIsInstance(None, set)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: set() is not None


green: make it pass
#################################################################################

I make ``assertIsNone`` to ``assertIsNotNone`` and ``assertIsInstance`` to ``assertNotIsInstance`` in ``test_is_none_a_set`` to make it pass.

From the tests I see that

* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a set_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`list </data_structures/lists/lists>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `float <https://docs.python.org/3/library/functions.html#float>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans/booleans>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

----

.. _test_is_none_a_dictionary:

test_is_none_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add a new test to compare `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ with :doc:`dictionaries </data_structures/dictionaries>`

.. code-block:: python

  def test_is_none_a_dictionary(self):
      self.assertIsNone(dict())
      self.assertIsNone({
          "a": 1,
          "b": 2,
          "c": 3,
          "n": "n"
      })
      self.assertIsInstance(None, dict)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {} is not None

* ``dict()`` is one way to make an empty :doc:`dictionary </data_structures/dictionaries>` in Python
* ``{}`` is how :doc:`dictionaries </data_structures/dictionaries>`  are represented in Python. Wait a minute! `sets <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ are also represented with ``{}``. The difference is that :doc:`dictionaries </data_structures/dictionaries>` hold key-value pairs
* Do you want to :doc:`read more about dictionaries </data_structures/dictionaries>`?

green: make it pass
#################################################################################
I make the tests to make them pass and can see from the tests that

* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`dictionary </data_structures/dictionaries>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a set_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`list </data_structures/lists/lists>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a `float <https://docs.python.org/3/library/functions.html#float>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not an `integer <https://docs.python.org/3/library/functions.html#int>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is not a :doc:`boolean </data_structures/booleans/booleans>`
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_

You now know what `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is and what it is not

Would you like to test :ref:`booleans`?

----

:doc:`/code/code_none`
