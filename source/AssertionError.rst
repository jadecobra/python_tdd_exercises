
AssertionError
==============

I will go through the `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_ in Python using Test Driven Development (TDD) in this chapter

Prerequisites
-------------


:doc:`How to Setup a Test Driven Development Environment <setup_tdd_environment>`


What is an AssertionError?
--------------------------

An `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_ is an Exception that is raised when the result of an ``assert`` statement is :doc:`False <data_structures_booleans>`

It was introduced in :doc:`How to Setup a Test Driven Development Environment <setup_tdd_environment>` with the first failing test

.. code-block:: python

  self.assertFalse(True)

which is similar to

.. code-block:: python

  assert True is False

Why are asserts important?
--------------------------

When building a program I can add ``assert`` statements to the program to ensure that certain things are true before it proceeds past the statements.

I can also test how the program behaves when it is given inputs using ``assert`` statements.

These assertions help catch bugs that break previous tested behavior when introduced, as well as answer the following questions


* What is similar?
* What is different?

A difference between my expectations and reality (the result of my programs) gives me a clue about what changes I need to make them match

----

AssertionError with None
------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

* I create a new file in the ``tests`` folder with the name ``test_assertion_error.py``
* and add a test called ``test_assertion_errors_with_none`` using the python ``assert`` keyword to intentionally cause an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

   import unittest


   class TestAssertionErrors(unittest.TestCase):

     def test_assertion_errors_with_none(self):
       assert False is None

  the terminal updates to show an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

  E    assert False is None

  tests/test_assertion_error.py:7: AssertionError

  - This `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_ is raised by the line ``assert False is None`` which is similar to asking the question "is False the same as None?"
  - The difference is that the ``assert`` at the beginning of the line makes the statement more like "DO NOT PROCEED UNLESS :doc:`False <data_structures_booleans>` is :doc:`None <data_structures_none>`"
  - Since :doc:`None <data_structures_none>` and :doc:`False <data_structures_booleans>` are different objects and not equal, the ``assert`` statement is :doc:`False <data_structures_booleans>` and python raises an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I modify the failing line of ``test_assertion_errors_with_none`` in ``test_assertion_error.py`` to make the test pass

.. code-block:: python

  assert False is not None

the test passes because the assert statement is now true since :doc:`False <data_structures_booleans>` is not :doc:`None <data_structures_none>`

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

I can also make assertions with some :doc:`methods <functions>` from the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ class


* RED: make it fail

  I add another line to ``test_assertion_errors_with_none`` using the `unittest.TestCase.assertIsNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNone>`_ :doc:`method <functions>`

  .. code-block:: python

  self.assertIsNone(False)

  the terminal updates to show a more descriptive `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_ since ``False is not None``

  .. code-block:: python

   E    AssertionError: False is not None

   tests/test_assertion_error.py:8: AssertionError

* GREEN: make it pass

  when I update the assert statement to

  .. code-block:: python

   self.assertIsNotNone(False)

  the terminal displays passing tests because the statement is :doc:`True <data_structures_booleans>`. I can now say that in python :doc:`False <data_structures_booleans>` is not :doc:`None <data_structures_none>`

* RED: make it fail

  I add another test to ``test_assertion_errors_with_none`` to find out how :doc:`None <data_structures_none>` is related to :doc:`True <data_structures_booleans>`

  .. code-block:: python

   assert True is None

  the terminal shows another `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

   E    assert True is None

* GREEN: make it pass

  I update the failing line in ``test_assertion_errors_with_none`` to make the test pass

  .. code-block:: python

   assert True is not None

* RED: make it fail

  I add a variation of the above statement using the `unittest.TestCase.assertIsNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNone>`_ :doc:`method <functions>` to ``test_assertion_errors_with_none``

  .. code-block:: python

   self.assertIsNone(True)

  and the terminal displays an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

  E    AssertionError: True is not None

* GREEN: make it pass

  I update the failing line in ``test_assertion_errors_with_none`` to make it pass

  .. code-block:: python

  self.assertIsNotNone(True)

  since all my tests are passing I can say that in python

  - :doc:`True <data_structures_booleans>` is not :doc:`None <data_structures_none>`
  - :doc:`False <data_structures_booleans>` is not :doc:`None <data_structures_none>`

* RED: make it fail

  I add another test to ``test_assertion_errors_with_none``

  .. code-block:: python

   assert None is not None

  and the terminal displays a failure

  .. code-block:: python

   E    assert None is not None

* GREEN: make it pass

  I change the failing line in ``test_assertion_errors_with_none`` to make it pass

  .. code-block:: python

  assert None is None

* RED: make it fail

  I add another test to ``test_assertion_errors_with_none`` using the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ method

  .. code-block:: python

   self.assertIsNotNone(None)

  and the terminal updates to show an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

   >    self.assertIsNotNone(None)
   E    AssertionError: unexpectedly None

* GREEN: make it pass

  I update ``test_assertion_errors_with_none`` to make it pass

  .. code-block:: python

   self.assertIsNone(None)

My knowledge of python has increased, From the tests I can see that

* :doc:`None <data_structures_none>` is :doc:`None <data_structures_none>`
* :doc:`True <data_structures_booleans>` is not :doc:`None <data_structures_none>`
* :doc:`False <data_structures_booleans>` is not :doc:`None <data_structures_none>`

Which of these ``assert`` statements do you prefer when testing :doc:`None <data_structures_none>`?

* ``assert x is None``
* ``self.assertIsNone(x)``

----

AssertionError with False
-------------------------

Can I raise an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_ for things that are :doc:`False <data_structures_booleans>`?

RED: make it fail
^^^^^^^^^^^^^^^^^

I update ``TestAssertionError`` in ``test_assertion_error.py`` with the following test to find out

.. code-block:: python

  def test_assertion_errors_with_false(self):
    assert True is False

the terminal updates to show a failure

.. code-block:: python

  E    assert True is False

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I update ``test_assertion_errors_with_false`` to make the test pass

.. code-block:: python

  assert False is False


RED: make it fail
^^^^^^^^^^^^^^^^^

What if I try the same test using the `unittest.TestCase.assertFalse <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertFalse>`_ :doc:`method <functions>` by adding this line to ``test_assertion_errors_with_false``

.. code-block:: python

  self.assertFalse(True)

the terminal updates to show a failure

.. code-block:: python

  E    AssertionError: True is not false

this is familiar, it was the first failing test I wrote in :doc:`How to Setup a Test Driven Development Environment <setup_tdd_environment>`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I update ``test_assertion_errors_with_false`` to make it pass

.. code-block:: python

  self.assertFalse(False)

From the tests I can see that in python

* :doc:`False <data_structures_booleans>` is :doc:`False <data_structures_booleans>`
* :doc:`False <data_structures_booleans>` is not :doc:`True <data_structures_booleans>`
* :doc:`None <data_structures_none>` is :doc:`None <data_structures_none>`
* :doc:`True <data_structures_booleans>` is not :doc:`None <data_structures_none>`
* :doc:`False <data_structures_booleans>` is not :doc:`None <data_structures_none>`

----

AssertionError with True
------------------------

Can I raise an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_ for things that are :doc:`True <data_structures_booleans>`?

RED: make it fail
^^^^^^^^^^^^^^^^^

I update ``TestAssertionError`` in ``test_assertion_error.py`` with the following test

.. code-block:: python

  def test_assertion_errors_with_true(self):
    assert False is True

the terminal updates to show a failure

.. code-block:: python

  E    assert False is True

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I update ``test_assertion_errors_with_true`` to make it pass

.. code-block:: python

  assert True is True

RED: make it fail
^^^^^^^^^^^^^^^^^

What if I try the above test using the `unittest.TestCase.assertTrue <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertTrue>`_ :doc:`method <functions>` ?

.. code-block:: python

  self.assertTrue(False)

the terminal shows an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

.. code-block:: python

  E    AssertionError: False is not true

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I update ``test_assertion_errors_with_false`` to make it pass

.. code-block:: python

  self.assertTrue(True)

My knowledge of python has grown, From the tests I can see that


* :doc:`True <data_structures_booleans>` is :doc:`True <data_structures_booleans>`
* :doc:`True <data_structures_booleans>` is not :doc:`False <data_structures_booleans>`
* :doc:`False <data_structures_booleans>` is :doc:`False <data_structures_booleans>`
* :doc:`False <data_structures_booleans>` is not :doc:`True <data_structures_booleans>`
* :doc:`None <data_structures_none>` is :doc:`None <data_structures_none>`
* :doc:`True <data_structures_booleans>` is not :doc:`None <data_structures_none>`
* :doc:`False <data_structures_booleans>` is not :doc:`None <data_structures_none>`

I could sum up the above statements this way - in python :doc:`True <data_structures_booleans>`, :doc:`False <data_structures_booleans>` and :doc:`None <data_structures_none>` are different. My understanding of these differences helps me shows how python behaves and give a foundation of predictable expectations of the language.

----

AssertionError with Equality
----------------------------

I can also make assertions of equality, where I compare if two things are the same

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test to ``TestAssertionError`` in ``test_assertion_error.py``

.. code-block:: python

  def test_assertion_errors_with_equality(self):
    assert False == None

the terminal displays an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

.. code-block:: python

  E    assert False == None


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change ``test_assertion_errors_with_equality`` to make it pass

.. code-block:: python

  assert False != None

the test passes because :doc:`False <data_structures_booleans>` is not equal to :doc:`None <data_structures_none>`

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* RED: make it fail

  I update ``test_assertion_errors_with_equality`` with the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ method for equality testing

  .. code-block:: python

   self.assertEqual(False, None)

  the terminal outputs an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

   E    AssertionError: False != None

  The `unittest.TestCase.assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ :doc:`method <functions>` checks if the two given inputs, :doc:`False <data_structures_booleans>` and :doc:`None <data_structures_none>` are equal

* GREEN: make it pass

  I change ``test_assertion_errors_with_equality`` to make it pass

  .. code-block:: python

   self.assertNotEqual(False, None)

  I have learned that in python

  * :doc:`True <data_structures_booleans>` is :doc:`True <data_structures_booleans>`
  * :doc:`True <data_structures_booleans>` is not :doc:`False <data_structures_booleans>`
  * :doc:`False <data_structures_booleans>` is :doc:`False <data_structures_booleans>`
  * :doc:`False <data_structures_booleans>` is not :doc:`True <data_structures_booleans>`
  * :doc:`None <data_structures_none>` is :doc:`None <data_structures_none>`
  * :doc:`True <data_structures_booleans>` is not :doc:`None <data_structures_none>`
  * :doc:`False <data_structures_booleans>` is not :doc:`None <data_structures_none>` and :doc:`False <data_structures_booleans>` is not equal to :doc:`None <data_structures_none>`

* RED: make it fail

  I add a new line to ``test_assertion_errors_with_equality``

  .. code-block:: python

   assert True == None

  and the terminal responds with an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

   E    assert True == None

* GREEN: make it pass

  I update the line in ``test_assertion_errors_with_equality`` to make it pass

  .. code-block:: python

   assert True != None

* RED: make it fail

  I add the `unittest.TestCase.assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ :doc:`method <functions>` to ``test_assertion_errors_with_equality``

  .. code-block:: python

   self.assertEqual(True, None)

  the terminal outputs an `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_

  .. code-block:: python

   E    AssertionError: True != None

* GREEN: make it pass

  I update ``test_assertion_errors_with_equality`` to make it pass

  .. code-block:: python

   self.assertNotEqual(True, None)

  the terminal updates to show passing tests. I can now say that in python

  * :doc:`True <data_structures_booleans>` is :doc:`True <data_structures_booleans>`
  * :doc:`True <data_structures_booleans>` is not :doc:`False <data_structures_booleans>`
  * :doc:`False <data_structures_booleans>` is :doc:`False <data_structures_booleans>`
  * :doc:`False <data_structures_booleans>` is not :doc:`True <data_structures_booleans>`
  * :doc:`None <data_structures_none>` is :doc:`None <data_structures_none>`
  * :doc:`True <data_structures_booleans>` is not :doc:`None <data_structures_none>` and :doc:`True <data_structures_booleans>` is not equal to :doc:`None <data_structures_none>`
  * :doc:`False <data_structures_booleans>` is not :doc:`None <data_structures_none>` and :doc:`False <data_structures_booleans>` is not equal to :doc:`None <data_structures_none>`

* RED: make it fail

  There is a pattern here, I update ``test_assertion_errors_with_equality`` with the other cases from my statement above

  .. code-block:: python

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

  I update ``test_assertion_errors_with_equality`` to make each test pass

  .. code-block:: python

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

  I can now say that in python

  * :doc:`True <data_structures_booleans>` is :doc:`True <data_structures_booleans>` and :doc:`True <data_structures_booleans>` is equal to :doc:`True <data_structures_booleans>`
  * :doc:`True <data_structures_booleans>` is not :doc:`False <data_structures_booleans>` and :doc:`True <data_structures_booleans>` is not equal to :doc:`False <data_structures_booleans>`
  * :doc:`False <data_structures_booleans>` is :doc:`False <data_structures_booleans>` and :doc:`False <data_structures_booleans>` is equal to :doc:`False <data_structures_booleans>`
  * :doc:`False <data_structures_booleans>` is not :doc:`True <data_structures_booleans>` and :doc:`False <data_structures_booleans>` is not equal to :doc:`True <data_structures_booleans>`
  * :doc:`None <data_structures_none>` is :doc:`None <data_structures_none>` and :doc:`None <data_structures_none>` is equal to :doc:`None <data_structures_none>`
  * :doc:`True <data_structures_booleans>` is not :doc:`None <data_structures_none>` and :doc:`True <data_structures_booleans>` is not equal to :doc:`None <data_structures_none>`
  * :doc:`False <data_structures_booleans>` is not :doc:`None <data_structures_none>` and :doc:`False <data_structures_booleans>` is not equal to :doc:`None <data_structures_none>`

----


If you have been typing along *WELL DONE!* Your magic powers are growing. From the experiments above you now know


* how to test for equality
* how to test if something is :doc:`None <data_structures_none>` or not
* how to test if something is :doc:`False <data_structures_booleans>` or not
* how to test if something is :doc:`True <data_structures_booleans>` or not
* how to use ``assert`` statements
* how to use the following ``unittest.TestCase.assert`` methods

  - `assertIsNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNone>`_ - is this thing :doc:`None <data_structures_none>`?
  - `assertIsNotNone <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNotNone>`_ - is this thing not :doc:`None <data_structures_none>`?
  - `assertFalse <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertFalse>`_ - is this thing :doc:`False <data_structures_booleans>`?
  - `assertTrue <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertTrue>`_ - is this thing :doc:`True <data_structures_booleans>`?
  - `assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ - are these two things equal?
  - `assertNotEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotEqual>`_ - are these two things not equal?