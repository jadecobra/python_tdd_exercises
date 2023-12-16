
#################################
Data Structures: Booleans: True
#################################

The tests in this chapter go over `booleans <https://docs.python.org/3/library/functions.html#bool>`_ by comparing them with other data structures in Python to learn what they are and what they are not.

There are two `boolean <https://docs.python.org/3/library/functions.html#bool>`_ values - `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ and `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

****************
What is True?
****************

**********************
is an integer True?
**********************

**********************
is a string True?
**********************

**********************
is a tuple True?
**********************

**********************
is a list True?
**********************

**********************
is a set True?
**********************

**********************
is a dictionary True?
**********************

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a similar series of failing tests for `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ to ``test_booleans.py``

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
          "c": 3,
          "n": "n"
      })
      self.assertNotIsInstance(True, bool)

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  >       self.assertFalse(True)
  E       AssertionError: True is not false

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I change all the ``self.assertFalse`` statements to ``self.assertTrue`` in ``test_what_is_true``

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
            "c": 3,
            "n": "n"
        })
        self.assertNotIsInstance(True, bool)

  and left with a failing test for the `self.assertNotIsInstance <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotIsInstance>`_ statement

  .. code-block:: python

    >       self.assertNotIsInstance(True, bool)
    E       AssertionError: True is an instance of <class 'bool'>

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

----

I can sum up my current knowledge of python from the tests so far as

- any value except empty objects, ``0`` and :doc:`None </data_structures/none>` are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
- empty `objects <https://docs.python.org/3/glossary.html#term-object>`_ including ``0`` and :doc:`None </data_structures/none>` are `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
- `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
- `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
- :doc:`None </data_structures/none>` is :doc:`None </data_structures/none>`

:doc:`/code/booleans`