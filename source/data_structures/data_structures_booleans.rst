
Data Structures: Booleans
=========================

The tests in this chapter cover `booleans <https://docs.python.org/3/library/functions.html#bool>`_ by comparing them with other data structures in python to learn what they are and what they are not. There are only two `boolean <https://docs.python.org/3/library/functions.html#bool>`_ values - `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ and `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

What is False?
--------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I create a failing test in ``test_data_structures.py`` called ``test_what_is_false``

.. code-block:: python

  def test_what_is_false(self):
      self.assertTrue(None)
      self.assertTrue(False)
      self.assertTrue(0)
      self.assertTrue("")
      self.assertTrue(())
      self.assertTrue([])
      self.assertTrue({})
      self.assertTrue(dict())
      self.assertNotIsInstance(False, bool)

the `unittest.TestCase.assertTrue <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertTrue>`_ :doc:`method </functions>` checks if a given input is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_, the terminal shows an :doc:`/exceptions/AssertionError` indicating that the given input is not `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* when I change the ``self.assertTrue`` statements in ``test_what_is_false`` to ``self.assertFalse`` I am left with one failing test

  .. code-block:: python

    def test_what_is_false(self):
        self.assertFalse(None)
        self.assertFalse(False)
        self.assertFalse(0)
        self.assertFalse("")
        self.assertFalse(())
        self.assertFalse([])
        self.assertFalse({})
        self.assertFalse(dict())
        self.assertNotIsInstance(False, bool)

  the `unittest.TestCase.assertNotIsInstance <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotIsInstance>`_ :doc:`method </functions>` checks that the first input given is not an instance of the :doc:`class </classes/classes>` given as the second input in other words, it is asking the question ``is False not an instance of bool?``

* When I change ``self.assertNotIsInstance`` to ``self.assertIsInstance`` the last test passes

  .. code-block:: python

    def test_what_is_false(self):
        self.assertFalse(None)
        self.assertFalse(False)
        self.assertFalse(0)
        self.assertFalse("")
        self.assertFalse(())
        self.assertFalse([])
        self.assertFalse({})
        self.assertFalse(dict())
        self.assertIsInstance(False, bool)

From the tests I can say that in python

* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
* ``dict()`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ which means an empty :doc:`dictionary <data_structures_dictionaries>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``{}`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ which means an empty `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_/\ :doc:`dictionary </data_structures/data_structures_dictionaries>`   is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``[]`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ which means an empty :doc:`list <data_structures_lists>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``()`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ which means an empty `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``""`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ which means an empty `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

I can sum this up as


* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
* empty `objects <https://docs.python.org/3/glossary.html#term-object>`_ including ``0`` and :doc:`None <data_structures_none>` are `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

What is True?
-------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a similar series of failing tests for `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ to ``test_data_structures.py``

.. code-block:: python

  def test_what_is_true(self):
      self.assertFalse(True)
      self.assertFalse(1)
      self.assertFalse(-1)
      self.assertFalse("text")
      self.assertFalse((1, 2, 3, "n"))
      self.assertFalse([1, 2, 3, 'n'])
      self.assertFalse({1, 2, 3, "n"})
      self.assertFalse({
          "a": 1,
          "b": 2,
          "c":  3,
          "n": "n"
      })
      self.assertNotIsInstance(True, bool)

the terminal shows an :doc:`/exceptions/AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* When I change all the ``self.assertFalse`` statements to ``self.assertTrue`` in ``test_what_is_true`` I am left with a failing test for the `unittest.TestCase.assertNotIsInstance <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotIsInstance>`_ statement

  .. code-block:: python

    def test_what_is_true(self):
        self.assertTrue(True)
        self.assertTrue(1)
        self.assertTrue(-1)
        self.assertTrue("text")
        self.assertTrue((1, 2, 3, "n"))
        self.assertTrue([1, 2, 3, 'n'])
        self.assertTrue({1, 2, 3, "n"})
        self.assertTrue({
            "a": 1,
            "b": 2,
            "c":  3,
            "n": "n"
        })
        self.assertNotIsInstance(True, bool)

* I change ``self.assertNotIsInstance`` to ``self.assertIsInstance`` and all the tests pass, confirming that `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is an instance of the `boolean <https://docs.python.org/3/library/functions.html#bool>`_ object

  .. code-block:: python

    def test_what_is_true(self):
        self.assertTrue(True)
        self.assertTrue(1)
        self.assertTrue(-1)
        self.assertTrue("text")
        self.assertTrue((1, 2, 3, "n"))
        self.assertTrue([1, 2, 3, 'n'])
        self.assertTrue({1, 2, 3, "n"})
        self.assertTrue({
            "a": 1,
            "b": 2,
            "c":  3,
            "n": "n"
        })
        self.assertIsInstance(True, bool)

* I can sum up my current knowledge of python from the tests so far as

  - any value except ``0``, empty objects and :doc:`None <data_structures_none>` are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
  - empty `objects <https://docs.python.org/3/glossary.html#term-object>`_ including ``0`` and :doc:`None <data_structures_none>` are `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
  - `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
  - `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
  - :doc:`None <data_structures_none>` is :doc:`None <data_structures_none>`
