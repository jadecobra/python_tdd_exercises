
AssertionError
==============

This chapter explores the `AssertionError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError>`_ exception in Python using Test Driven Development (TDD)

Prerequisites
-------------


:doc:`How to Setup a Test Driven Development Environment`


What is an AssertionError?
--------------------------

An ``AssertionError`` is an Exception that is raised when the result of an ``assert`` statement is ``False``. It was introduced in :doc:`How to Setup a Test Driven Development Environment` with the first failing test

.. code-block:: python

  self.assertFalse(True)

which is similar to

.. code-block:: python

  assert True is False

Why are asserts important?
--------------------------

When building a program we can add ``assert`` statements to the program to ensure that certain things are true before it proceeds past the statements, we can also test how the program behaves when it is given inputs. These assertions help catch bugs that break previous tested behavior when introduced, as well as answer the following questions


* What is similar?
* What is different?

A difference between our expectations and reality (the result of our programs) gives us a clue about what changes are needed to make them match

----

AssertionError with None
------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

* create a new file in the ``tests`` folder with the name ``test_assertion_error.py``
* add a test named ``test_assertion_errors_with_none`` with the python ``assert`` keyword to intentionally cause an ``AssertionError``

  .. code-block:: python

      import unittest


      class TestAssertionErrors(unittest.TestCase):

          def test_assertion_errors_with_none(self):
              assert False is None

  the terminal updates to show

  .. code-block:: python

    E       assert False is None

    tests/test_assertion_error.py:7: AssertionError

  - This ``AssertionError`` is raised by the line ``assert False is None`` which is similar to asking the question "is False the same as None?"
  - The difference is that the ``assert`` at the beginning of the line makes the statement more like "DO NOT PROCEED UNLESS ``False`` is ``None``"
  - Since ``None`` and ``False`` are different objects and not equal, the ``assert`` statement is ``False`` and python raises an ``AssertionError``

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

modify the failing line of ``test_assertion_errors_with_none`` in ``test_assertion_error.py`` to make the test pass

.. code-block:: python

  assert False is not None

the test passes because the assert statement is now true since `False` is not `None`

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

We can also make assertions with some methods from the ``unittest.TestCase`` class


* RED: make it fail

  add another line to ``test_assertion_errors_with_none`` using the ``unittest.TestCase.assertIsNone`` :doc:`method <functions>`

  .. code-block:: python

    self.assertIsNone(False)

  the terminal updates to show a more descriptive ``AssertionError`` since ``False is not None``

  .. code-block:: python

      E       AssertionError: False is not None

      tests/test_assertion_error.py:8: AssertionError

* GREEN: make it pass

  when we update the assert statement to

  .. code-block:: python

      self.assertIsNotNone(False)

  the terminal displays passing tests because the statement is ``True``, we can conclude that in python ``False`` is not ``None``

* RED: make it fail

  add another test to ``test_assertion_errors_with_none`` to find out the relation of ``None`` to ``True``

  .. code-block:: python

      assert True is None

  the terminal shows another ``AssertionError``

  .. code-block:: python

      E       assert True is None

* GREEN: make it pass

  update the failing line in ``test_assertion_errors_with_none`` to make the test pass

  .. code-block:: python

      assert True is not None

* RED: make it fail

  add a variation of the above statement using the ``unittest.TestCase.assertIsNone`` :doc:`method <functions>` to ``test_assertion_errors_with_none``

  .. code-block:: python

      self.assertIsNone(True)

  and the terminal displays

  .. code-block:: python

    E       AssertionError: True is not None

* GREEN: make it pass

  update the failing line in ``test_assertion_errors_with_none`` to make it pass

  .. code-block:: python

    self.assertIsNotNone(True)

  since all our tests are passing we can conclude that in python

  - ``True`` is not ``None``
  - ``False`` is not ``None``

* RED: make it fail

  add another test to ``test_assertion_errors_with_none``

  .. code-block:: python

      assert None is not None

  and the terminal displays

  .. code-block:: python

      E       assert None is not None

* GREEN: make it pass

  change the failing line in ``test_assertion_errors_with_none`` to make it pass

  .. code-block:: python

    assert None is None

* RED: make it fail

  add another test to ``test_assertion_errors_with_none`` using the ``unittest.TestCase`` method

  .. code-block:: python

      self.assertIsNotNone(None)

  and the terminal updates to show

  .. code-block:: python

      >       self.assertIsNotNone(None)
      E       AssertionError: unexpectedly None

* GREEN: make it pass

  update ``test_assertion_errors_with_none`` to make it pass

  .. code-block:: python

      self.assertIsNone(None)

Our knowledge of python has increased, we now know that

* ``None`` is ``None``
* ``True`` is not ``None``
* ``False`` is not ``None``

Which of these ``assert`` statements do you prefer when testing ``None``?

* ``assert x is None``
* ``self.assertIsNone(x)``

----

AssertionError with False
-------------------------

Can we raise an ``AssertionError`` for things that are ``False``?

RED: make it fail
^^^^^^^^^^^^^^^^^

update ``TestAssertionError`` in ``test_assertion_error.py`` with the following test to find out

.. code-block:: python

    def test_assertion_errors_with_false(self):
        assert True is False

the terminal updates to show

.. code-block:: python

   E       assert True is False

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update ``test_assertion_errors_with_false`` to make the test pass

.. code-block:: python

    assert False is False


RED: make it fail
^^^^^^^^^^^^^^^^^

What if we try the same test using the equivalent ``unittest.TestCase`` method by adding this line to ``test_assertion_errors_with_false``

.. code-block:: python

    self.assertFalse(True)

the terminal updates to show a failure

.. code-block:: python

   E       AssertionError: True is not false

this is familiar, it was the first failing test we wrote in :doc:`How to Setup a Test Driven Development Environment`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update ``test_assertion_errors_with_false`` to make it pass

.. code-block:: python

    self.assertFalse(False)

We now know that in python

* ``False`` is ``False``
* ``False`` is not ``True``
* ``None`` is ``None``
* ``True`` is not ``None``
* ``False`` is not ``None``

----

AssertionError with True
------------------------

Can we raise an ``AssertionError`` for things that are ``True``?

RED: make it fail
^^^^^^^^^^^^^^^^^

update ``TestAssertionError`` in ``test_assertion_error.py`` with the following test

.. code-block:: python

    def test_assertion_errors_with_true(self):
        assert False is True

the terminal updates to show

.. code-block:: python

  E       assert False is True

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update ``test_assertion_errors_with_true`` to make it pass

.. code-block:: python

    assert True is True

RED: make it fail
^^^^^^^^^^^^^^^^^

What if we try the above test with the ``unittest.TestCase`` equivalent method by updating ``test_assertion_errors_with_true``

.. code-block:: python

    self.assertTrue(False)

the terminal shows a failure

.. code-block:: python

    E       AssertionError: False is not true

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update ``test_assertion_errors_with_false`` to make it pass

.. code-block:: python

    self.assertTrue(True)

Our knowledge of python has grown, we now know that


* ``True`` is ``True``
* ``True`` is not ``False``
* ``False`` is ``False``
* ``False`` is not ``True``
* ``None`` is ``None``
* ``True`` is not ``None``
* ``False`` is not ``None``

We could sum up the above statements this way - in python ``True``, ``False`` and ``None`` are different. Understanding these differences helps us write useful programs. They show how python behaves and form our core truths, a foundation of predictable expectations of the language.

----

AssertionError with Equality
----------------------------

We can also make assertions of equality, where we compare if two things are the same

RED: make it fail
^^^^^^^^^^^^^^^^^

add a new test to ``TestAssertionError`` in ``test_assertion_error.py``

.. code-block:: python

    def test_assertion_errors_with_equality(self):
        assert False == None

the terminal displays

.. code-block:: python

  E       assert False == None

we could take this ``assert`` statement to mean ``DO NOT PROCEED UNLESS False is equal to None``

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

change ``test_assertion_errors_with_equality`` to make it pass

.. code-block:: python

    assert False != None

the tests pass because ``False`` is not equal to ``None``

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* RED: make it fail

  update ``test_assertion_errors_with_equality`` with the equivalent ``unittest.TestCase`` method

  .. code-block:: python

      self.assertEqual(False, None)

  the terminal outputs

  .. code-block:: python

      E       AssertionError: False != None

  The ``unittest.TestCase.assertEqual`` :doc:`method <functions>` checks if the two given inputs, ``False`` and ``None`` are equal. :doc:`TypeError` covers function signatures if you want a better understanding of passing inputs to functions.

  For now, we could imagine that in a file named ``unittest.py`` there is a definition which means something like the code below.

  .. code-block:: python

      class TestCase(object):

          def assertEqual(self, positional_argument_1, positional_argument_2):
              assert positional_argument_1 == positional_argument_2

  We could also `look at the real definition of the assertEqual method <https://github.com/python/cpython/blob/f1f85a42eafd31720cf905c5407ca3e043946698/Lib/unittest/case.py#L868>`_

* GREEN: make it pass

  change ``test_assertion_errors_with_equality`` to make it pass

  .. code-block:: python

      self.assertNotEqual(False, None)

  We have learned that in python

  * ``True`` is ``True``
  * ``True`` is not ``False``
  * ``False`` is ``False``
  * ``False`` is not ``True``
  * ``None`` is ``None``
  * ``True`` is not ``None``
  * ``False`` is not ``None`` and ``False`` is not equal to ``None``

* RED: make it fail

  add a new line to ``test_assertion_errors_with_equality``

  .. code-block:: python

      assert True == None

  and the terminal responds with a failure

  .. code-block:: python

      E       assert True == None

* GREEN: make it pass

  update the line in ``test_assertion_errors_with_equality`` to make it pass

  .. code-block:: python

      assert True != None

* RED: make it fail

  add the equivalent ``unittest.TestCase`` method to ``test_assertion_errors_with_equality``

  .. code-block:: python

      self.assertEqual(True, None)

  the terminal outputs

  .. code-block:: python

      E       AssertionError: True != None

* GREEN: make it pass

  update ``test_assertion_errors_with_equality`` to make it pass

  .. code-block:: python

      self.assertNotEqual(True, None)

  the terminal updates to show passing tests. We can now say that in python

  * ``True`` is ``True``
  * ``True`` is not ``False``
  * ``False`` is ``False``
  * ``False`` is not ``True``
  * ``None`` is ``None``
  * ``True`` is not ``None`` and ``True`` is not equal to ``None``
  * ``False`` is not ``None`` and ``False`` is not equal to ``None``

* RED: make it fail

    There is a pattern here, update ``test_assertion_errors_with_equality`` with the other cases from our statement above

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

  update ``test_assertion_errors_with_equality`` to make each test pass. Once all the tests pass we can conclude that in python

  * ``True`` is ``True`` and ``True`` is equal to ``True``
  * ``True`` is not ``False`` and ``True`` is not equal to ``False``
  * ``False`` is ``False`` and ``False`` is equal to ``False``
  * ``False`` is not ``True`` and ``False`` is not equal to ``True``
  * ``None`` is ``None`` and ``None`` is equal to ``None``
  * ``True`` is not ``None`` and ``True`` is not equal to ``None``
  * ``False`` is not ``None`` and ``False`` is not equal to ``None``

----


*WELL DONE!* Your magic powers are growing. From the experiments above you now know


* how to test for equality
* how to test if something is ``None`` or not
* how to test if something is ``False`` or not
* how to test if something is ``True`` or not
* how to use ``assert`` statements
* how to use the following ``unittest.TestCase.assert`` methods

  - ``assertIsNone``     - is this thing ``None``?
  - ``assertIsNotNone``  - is this thing not ``None``?
  - ``assertFalse``      - is this thing ``False``?
  - ``assertTrue``       - is this thing ``True``?
  - ``assertEqual``      - are these two things equal?
  - ``assertNotEqual``   - are these two things not equal?


.. admonition:: *FOOD FOR THOUGHT*


  * when x is y, is x also equal to y?
  * when x is not y, is x also not equal to y?
