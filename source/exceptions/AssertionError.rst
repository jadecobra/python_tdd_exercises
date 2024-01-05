
AssertionError
==============

An `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_ is an Exception that is raised when the result of an ``assert`` statement is :doc:`False </data_structures/booleans>`

It was introduced in :doc:`How to create a Test Driven Development Environment </how_to/create_tdd_environment>` with the first failing test

.. code-block:: python

  self.assertFalse(True)

which is similar to

.. code-block:: python

  assert True is False

Why are asserts important?
--------------------------

When building a program I can add ``assert`` statements to the program to ensure that certain things are :doc:`True </data_structures/booleans>` for it to proceed past the statements.

I can also test how the program behaves when it is given inputs using ``assert`` statements.

These assertions help catch bugs that break previous tested behavior when introduced, as well as answer the following questions


* What is similar?
* What is different?

A difference between my expectations and reality (what happens when I run the program) gives me a clue about what changes are needed to make them match

----

AssertionError with None
------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

* I create a new file in the ``tests`` folder with the name ``test_assertion_error.py``
* then add a test called ``test_assertion_errors_with_none`` using the python ``assert`` keyword to intentionally cause an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

    import unittest


    class TestAssertionErrors(unittest.TestCase):

        def test_assertion_errors_with_none(self):
            assert False is None

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

    E    assert False is None

    tests/test_assertion_error.py:7: AssertionError

  - This `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_ is raised by the line ``assert False is None`` which is similar to asking the question "is False the same as None?"
  - The difference is that the ``assert`` at the beginning of the line makes the statement more like "DO NOT PROCEED UNLESS :doc:`False </data_structures/booleans>` is :doc:`None </data_structures/none>`"
  - Since :doc:`None </data_structures/none>` and :doc:`False </data_structures/booleans>` are not equal, the ``assert`` statement is :doc:`False </data_structures/booleans>` and python raises an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

When I change the failing line to

.. code-block:: python

  def test_assertion_errors_with_none(self):
      assert False is not None

the test passes because the assert statement is now true since :doc:`False </data_structures/booleans>` is not :doc:`None </data_structures/none>`

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

I can also make assertions with some :doc:`methods </functions/functions>` from the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ class


* RED: make it fail

  I add another failing line using the `unittest.TestCase.assertIsNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNone>`_ :doc:`method </functions/functions>`

  .. code-block:: python

    def test_assertion_errors_with_none(self):
        assert False is not None
        self.assertIsNone(False)

  the terminal shows a more descriptive `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_ since ``False is not None``

  .. code-block:: python

    AssertionError: False is not None

* GREEN: make it pass

  when I change the assert statement to

  .. code-block:: python

    def test_assertion_errors_with_none(self):
        assert False is not None
        self.assertIsNotNone(False)

  the terminal shows passing tests because the statement is :doc:`True </data_structures/booleans>`. I can now say that in Python :doc:`False </data_structures/booleans>` is not :doc:`None </data_structures/none>`

* RED: make it fail

  I add another test to find out how :doc:`None </data_structures/none>` is related to :doc:`True </data_structures/booleans>`

  .. code-block:: python

    def test_assertion_errors_with_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is None

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

    E    assert True is None

* GREEN: make it pass

  I change the failing line to make the test pass

  .. code-block:: python

    def test_assertion_errors_with_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None

* RED: make it fail

  I add a line using the `unittest.TestCase.assertIsNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNone>`_ :doc:`method </functions/functions>`

  .. code-block:: python

    def test_assertion_errors_with_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNone(True)

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

    AssertionError: True is not None

* GREEN: make it pass

  I change the failing line to make the test pass

  .. code-block:: python

    def test_assertion_errors_with_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

  since all my tests are passing I can say that in Python

  - :doc:`True </data_structures/booleans>` is not :doc:`None </data_structures/none>`
  - :doc:`False </data_structures/booleans>` is not :doc:`None </data_structures/none>`

* RED: make it fail

  I add a failing line

  .. code-block:: python

    def test_assertion_errors_with_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

        assert None is not None

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

    E    assert None is not None

* GREEN: make it pass

  I change the failing line to make the test pass

  .. code-block:: python

    def test_assertion_errors_with_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

        assert None is None

* RED: make it fail

  I add a failing line using the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ method

  .. code-block:: python

    def test_assertion_errors_with_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

        assert None is None
        self.assertIsNotNone(None)

  and the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

    AssertionError: unexpectedly None

* GREEN: make it pass

  I change ``test_assertion_errors_with_none`` to make it pass

  .. code-block:: python

    def test_assertion_errors_with_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

        assert None is None
        self.assertIsNone(None)

From the tests I can see that

* :doc:`None </data_structures/none>` is :doc:`None </data_structures/none>`
* :doc:`True </data_structures/booleans>` is not :doc:`None </data_structures/none>`
* :doc:`False </data_structures/booleans>` is not :doc:`None </data_structures/none>`

Which of these ``assert`` statements do you prefer when testing :doc:`None </data_structures/none>`?

* ``assert x is None``
* ``self.assertIsNone(x)``

----

AssertionError with False
-------------------------

Can I raise an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_ for things that are :doc:`False </data_structures/booleans>`?

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test to ``TestAssertionError`` in ``test_assertion_error.py`` to find out

.. code-block:: python

  def test_assertion_errors_with_false(self):
      assert True is False

the terminal shows a failure

.. code-block:: python

  E    assert True is False

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the failing line to make the test pass

.. code-block:: python

  def test_assertion_errors_with_false(self):
      assert False is False


RED: make it fail
^^^^^^^^^^^^^^^^^

What if I try the same test using the `unittest.TestCase.assertFalse <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertFalse>`_ :doc:`method </functions/functions>` by adding this line to ``test_assertion_errors_with_false``?

.. code-block:: python

  def test_assertion_errors_with_false(self):
      assert False is False
      self.assertFalse(True)

the terminal shows a failure

.. code-block:: python

  AssertionError: True is not false

this is familiar, it was the first failing test from :doc:`How to create a Test Driven Development Environment </how_to/create_tdd_environment>`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the failing line to make the test pass

.. code-block:: python

  def test_assertion_errors_with_false(self):
      assert False is False
      self.assertFalse(False)

From the tests I can see that in Python

* :doc:`False </data_structures/booleans>` is :doc:`False </data_structures/booleans>`
* :doc:`False </data_structures/booleans>` is not :doc:`True </data_structures/booleans>`
* :doc:`None </data_structures/none>` is :doc:`None </data_structures/none>`
* :doc:`True </data_structures/booleans>` is not :doc:`None </data_structures/none>`
* :doc:`False </data_structures/booleans>` is not :doc:`None </data_structures/none>`

----

AssertionError with True
------------------------

Can I raise an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_ for things that are :doc:`True </data_structures/booleans>`?

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test to ``TestAssertionError`` in ``test_assertion_error.py``

.. code-block:: python

  def test_assertion_errors_with_true(self):
      assert False is True

the terminal shows a failure

.. code-block:: python

  E    assert False is True

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the failing line to make the test pass

.. code-block:: python

  def test_assertion_errors_with_true(self):
      assert True is True

RED: make it fail
^^^^^^^^^^^^^^^^^

What if I try the above test using the `unittest.TestCase.assertTrue <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertTrue>`_ :doc:`method </functions/functions>` ?

.. code-block:: python

  def test_assertion_errors_with_true(self):
      assert True is True
      self.assertTrue(False)

the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

.. code-block:: python

  AssertionError: False is not true

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the failing line to make the test pass

.. code-block:: python

  def test_assertion_errors_with_true(self):
      assert True is True
      self.assertTrue(True)

From the tests I can see that


* :doc:`True </data_structures/booleans>` is :doc:`True </data_structures/booleans>`
* :doc:`True </data_structures/booleans>` is not :doc:`False </data_structures/booleans>`
* :doc:`False </data_structures/booleans>` is :doc:`False </data_structures/booleans>`
* :doc:`False </data_structures/booleans>` is not :doc:`True </data_structures/booleans>`
* :doc:`None </data_structures/none>` is :doc:`None </data_structures/none>`
* :doc:`True </data_structures/booleans>` is not :doc:`None </data_structures/none>`
* :doc:`False </data_structures/booleans>` is not :doc:`None </data_structures/none>`

I could sum up the above statements this way - in Python :doc:`True </data_structures/booleans>`, :doc:`False </data_structures/booleans>` and :doc:`None </data_structures/none>` are different. My understanding of these differences helps me know how python behaves and gives a foundation of predictable expectations of the language.

----

AssertionError with Equality
----------------------------

I can also make assertions where I compare if two things are the same or equal

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test to ``TestAssertionError`` in ``test_assertion_error.py``

.. code-block:: python

  def test_assertion_errors_with_equality(self):
      assert False == None

the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

.. code-block:: python

  E    assert False == None


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the failing line to make the test pass

.. code-block:: python

  def test_assertion_errors_with_equality(self):
      assert False != None

the test passes because :doc:`False </data_structures/booleans>` is not equal to :doc:`None </data_structures/none>`

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* RED: make it fail

  I add a line with the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ method for equality testing

  .. code-block:: python

    def test_assertion_errors_with_equality(self):
        assert False != None
        self.assertEqual(False, None)

  and the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

    AssertionError: False != None

  The `unittest.TestCase.assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ :doc:`method </functions/functions>` checks if the two given inputs, :doc:`False </data_structures/booleans>` and :doc:`None </data_structures/none>` are equal

* GREEN: make it pass

  I change the failing line to make the test pass

  .. code-block:: python

    def test_assertion_errors_with_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

  I have learned that in Python

  * :doc:`True </data_structures/booleans>` is :doc:`True </data_structures/booleans>`
  * :doc:`True </data_structures/booleans>` is not :doc:`False </data_structures/booleans>`
  * :doc:`False </data_structures/booleans>` is :doc:`False </data_structures/booleans>`
  * :doc:`False </data_structures/booleans>` is not :doc:`True </data_structures/booleans>`
  * :doc:`None </data_structures/none>` is :doc:`None </data_structures/none>`
  * :doc:`True </data_structures/booleans>` is not :doc:`None </data_structures/none>`
  * :doc:`False </data_structures/booleans>` is not :doc:`None </data_structures/none>` and :doc:`False </data_structures/booleans>` is not equal to :doc:`None </data_structures/none>`

* RED: make it fail

  I add a new line to ``test_assertion_errors_with_equality``

  .. code-block:: python

    def test_assertion_errors_with_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True == None

  and the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

    E    assert True == None

* GREEN: make it pass

  I change the failing line to make the test pass

  .. code-block:: python

    def test_assertion_errors_with_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None

* RED: make it fail

  I add the `unittest.TestCase.assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ :doc:`method </functions/functions>` to ``test_assertion_errors_with_equality``

  .. code-block:: python

    def test_assertion_errors_with_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertEqual(True, None)

  the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

    AssertionError: True != None

* GREEN: make it pass

  I change the failing line to make the test pass

  .. code-block:: python

    def test_assertion_errors_with_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertNotEqual(True, None)

  and the terminal shows passing tests. I can now say that in Python

  * :doc:`True </data_structures/booleans>` is :doc:`True </data_structures/booleans>`
  * :doc:`True </data_structures/booleans>` is not :doc:`False </data_structures/booleans>`
  * :doc:`False </data_structures/booleans>` is :doc:`False </data_structures/booleans>`
  * :doc:`False </data_structures/booleans>` is not :doc:`True </data_structures/booleans>`
  * :doc:`None </data_structures/none>` is :doc:`None </data_structures/none>`
  * :doc:`True </data_structures/booleans>` is not :doc:`None </data_structures/none>` and :doc:`True </data_structures/booleans>` is not equal to :doc:`None </data_structures/none>`
  * :doc:`False </data_structures/booleans>` is not :doc:`None </data_structures/none>` and :doc:`False </data_structures/booleans>` is not equal to :doc:`None </data_structures/none>`

* RED: make it fail

  There is a pattern here, so I add the other cases from the statements above to  ``test_assertion_errors_with_equality``

  .. code-block:: python

    def test_assertion_errors_with_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertNotEqual(True, None)

        assert True != True
        self.assertNotEqual(True, True)

        assert True == False
        self.assertEqual(True, False)

        assert False != False
        self.assertNotEqual(False, False)

        assert False == True
        self.assertEqual(False, True)

        assert None != None
        self.assertNotEqual(None, None)

* GREEN: make it pass

  then I change each failing line until they all pass

  .. code-block:: python

    def test_assertion_errors_with_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertNotEqual(True, None)

        assert True == True
        self.assertEqual(True, True)

        assert True != False
        self.assertNotEqual(True, False)

        assert False == False
        self.assertEqual(False, False)

        assert False != True
        self.assertNotEqual(False, True)

        assert None == None
        self.assertEqual(None, None)

  and from the tests I can say that in Python

  * :doc:`True </data_structures/booleans>` is :doc:`True </data_structures/booleans>` and :doc:`True </data_structures/booleans>` is equal to :doc:`True </data_structures/booleans>`
  * :doc:`True </data_structures/booleans>` is not :doc:`False </data_structures/booleans>` and :doc:`True </data_structures/booleans>` is not equal to :doc:`False </data_structures/booleans>`
  * :doc:`False </data_structures/booleans>` is :doc:`False </data_structures/booleans>` and :doc:`False </data_structures/booleans>` is equal to :doc:`False </data_structures/booleans>`
  * :doc:`False </data_structures/booleans>` is not :doc:`True </data_structures/booleans>` and :doc:`False </data_structures/booleans>` is not equal to :doc:`True </data_structures/booleans>`
  * :doc:`None </data_structures/none>` is :doc:`None </data_structures/none>` and :doc:`None </data_structures/none>` is equal to :doc:`None </data_structures/none>`
  * :doc:`True </data_structures/booleans>` is not :doc:`None </data_structures/none>` and :doc:`True </data_structures/booleans>` is not equal to :doc:`None </data_structures/none>`
  * :doc:`False </data_structures/booleans>` is not :doc:`None </data_structures/none>` and :doc:`False </data_structures/booleans>` is not equal to :doc:`None </data_structures/none>`

----


If you have been typing along *WELL DONE!* Your magic powers are growing. From the experiments above you now know


* how to test for equality
* how to test if something is :doc:`None </data_structures/none>` or not
* how to test if something is :doc:`False </data_structures/booleans>` or not
* how to test if something is :doc:`True </data_structures/booleans>` or not
* how to use ``assert`` statements
* how to use the following ``unittest.TestCase.assert`` methods

  - `assertIsNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNone>`_ - is this thing :doc:`None </data_structures/none>`? (try saying that 10 times fast)
  - `assertIsNotNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNotNone>`_ - is this thing not :doc:`None </data_structures/none>`?
  - `assertFalse <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertFalse>`_ - is this thing :doc:`False </data_structures/booleans>`?
  - `assertTrue <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertTrue>`_ - is this thing :doc:`True </data_structures/booleans>`?
  - `assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ - are these two things equal?
  - `assertNotEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotEqual>`_ - are these two things not equal?