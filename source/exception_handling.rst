
How to handle Exceptions (Errors)
=================================

Exceptions are raised in python when an error occurs and break execution of the program. When an exception is encountered no further instructions in the program will run.

This is useful because it means there is some violation that should be taken care of for the program to proceed as intended.

It also a pain when it causes the program to exit prematurely. What if I want the program to run regardless of errors? I might want it to give messages to the user who may not care or understand the details that come with Exceptions

Enter Exception Handling, a way to deal with exceptions, allowing programs to make decisions when an Exception is encountered. Enough words, time to write some code.


How to test that an Exception is raised
---------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I create a file called ``test_exception_handling.py`` in the ``tests`` folder and add the following

.. code-block:: python

  import unittest
  import module


  class TestExceptionHandling(unittest.TestCase):

      def test_catching_module_not_found_error_in_tests(self):
          import non_existent_module

the terminal shows a :doc:`ModuleNotFoundError` and I add it to the list of exceptions encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I could take care of this error by creating the module, but in this case I want to catch or handle the exception in the test as a way to prove that a ``ModuleNotFoundError`` was raised when I refer to ``non_existent_module``

I add a ``self.assertRaises`` to ``test_catching_module_not_found_error_in_tests``

.. code-block:: python

  def test_catching_module_not_found_error_in_tests(self):
      with self.assertRaises(ModuleNotFoundError):
          import non_existent_module

and the terminal shows passing tests. How does all this work?


* I use the ``self.assertRaises`` :doc:`method <functions>` from the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ class which takes a given exception as its input, in this case ``ModuleNotFoundError`` and checks if that error is raised by the statements given in the context below (the indented block after the ``with`` statement)
* ``with`` - creates the context where I test that the exception is raised

  - `read more about the with statement <https://docs.python.org/3/reference/compound_stmts.html?highlight=statement#the-with-statement>`_
  - `read more about with statement context managers <https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers>`_
  - `read PEP 343 - The "with" Statement <https://peps.python.org/pep-0343/>`_


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

I can use this information to test that a particular exception is raised

* RED: make it fail

  I add a new test to ``TestExceptionHandling`` in ``test_exception_handling.py``

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        module.non_existent_attribute

  the terminal shows an :doc:`AttributeError` because the called attribute ``non_existent_attribute`` does not exist in ``module.py``

  .. code-block:: python

    E    AttributeError: module 'module' has no attribute 'non_existent_attribute'

  I add the exception to the running list or exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* GREEN: make it pass

  I add a ``self.assertRaises`` to ``test_catching_attribute_errors_in_tests``

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute

  the terminal shows passing tests. Let's do it again with ``methods`` for good measure

* RED: make it fail

  I add a failing line to ``test_catching_attribute_errors_in_tests``

  .. code-block:: python

   def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
      module.non_existent_function()

  the terminal shows :doc:`AttributeError` because ``non_existent_function`` does not exist in ``module.py``

  .. code-block:: python

    E    AttributeError: module 'module' has no attribute 'non_existent_function'

* GREEN: make it pass

  I add ``self.assertRaises`` and indent the failing line to place it within the context

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()

  the terminal shows passing tests

* RED: make it fail

  I add another failing line to ``test_catching_attribute_errors_in_tests``

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()
        module.NonExistentClass()

  the terminal shows an :doc:`AttributeError`

  .. code-block:: python

    E    AttributeError: module 'module' has no attribute 'NonExistentClass'

* GREEN: make it pass

  I add ``self.assertRaises`` to make it pass

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()
        with self.assertRaises(AttributeError):
            module.NonExistentClass()

  the terminal displays passing tests

* RED: make it fail

  I change ``test_catching_attribute_errors_in_tests`` with a new failing line

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()
        with self.assertRaises(AttributeError):
            module.NonExistentClass()
        module.Class.non_existent_attribute

  the terminal shows an :doc:`AttributeError`

  .. code-block:: python

    E    AttributeError: type object 'Class' has no attribute 'non_existent_attribute'

* GREEN: make it pass

  I add ``self.assertRaises`` to catch the error

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()
        with self.assertRaises(AttributeError):
            module.NonExistentClass()
        with self.assertRaises(AttributeError):
            module.Class.non_existent_attribute

  the terminal shows passing tests

* RED: make it fail

  I trigger another attribute error, by adding a line to ``test_catching_attribute_errors_in_tests``

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()
        with self.assertRaises(AttributeError):
            module.NonExistentClass()
        with self.assertRaises(AttributeError):
            module.Class.non_existent_attribute
        module.Class.non_existent_method()

  the terminal shows another :doc:`AttributeError`

  .. code-block:: python

    E    AttributeError: type object 'Class' has no attribute 'non_existent_method'

* GREEN: make it pass

  I add ``self.assertRaises`` to make it pass

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()
        with self.assertRaises(AttributeError):
            module.NonExistentClass()
        with self.assertRaises(AttributeError):
            module.Class.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.Class.non_existent_method()

  the terminal shows passing tests

* REFACTOR: make it better

  I just created the same context 5 times, this is a good candidate for a rewrite. The ``self.assertRaises`` catches an :doc:`AttributeError` in each case, I only need to state it once and place all the lines that raise the error underneath it.

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
            module.non_existent_function()
            module.NonExistentClass()
            module.Class.non_existent_attribute
            module.Class.non_existent_method()

  Fantastic! all the tests still pass

----

How to handle Exceptions in programs
------------------------------------

Earlier on I showed how to verify that an exception is raised, I will now show how to handle exceptions when they are raised

RED: make it fail
^^^^^^^^^^^^^^^^^

I will deliberately trigger an exception in the code and then handle it. Add a failing test to ``test_exception_handling.py`` with a new test

.. code-block:: python

  def test_catching_exceptions(self):
      exceptions.raises_exception_error()

the terminal displays a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I add it to the running list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError

* A `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ is raised when a name is used within a module with no definition for the name. In the test I call ``exceptions.raises_exception_error`` but there is no definition for ``exceptions``

* I add a new ``import`` statement

  .. code-block:: python

    import unittest
    import module
    import exceptions

  the terminal shows a :doc:`ModuleNotFoundError`

* I create a file called ``exceptions.py`` in the ``{PROJECT_NAME}`` folder, and the terminal shows an :doc:`AttributeError`
* I add a name for the attribute called in the test to ``exceptions.py`` and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ since I have not defined ``raises_exception_error`` in ``exceptions.py``

  .. code-block:: python

    raises_exception_error

* I assign ``raises_exception_error`` a value and the terminal shows a :doc:`TypeError`

  .. code-block:: python

    raises_exception_error = None

  which I add to the running list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError
    # TypeError

* When I define ``raises_exception_error`` as a function and the terminal shows passing tests

  .. code-block:: python

    def raises_exception_error():
        return None

* I use the `raise <https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement>`_ keyword to cause an exception when ``raises_exception_error`` is called

  .. code-block:: python

    def raises_exception_error():
        raise Exception

  the terminal shows the ``Exception`` is raised

  .. code-block:: python

    E    Exception

* I add a ``self.assertRaises`` to ``test_catching_exceptions`` in ``test_exception_handling.py`` to confirm that this exception is raised and allow the tests to continue even though there is a failure

  .. code-block:: python

    def test_catching_exceptions(self):
        with self.assertRaises(Exception):
            exceptions.raises_exception_error()

  the terminal shows passing tests

*CONGRATULATIONS!*
You now know how to deliberately create an exception which means you have absolute power to reshape the universe to your will


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Let us add exception handling to the program so it does not end when it encounters an exception but instead gives a message


* RED: make it fail

  add a new test to ``test_exception_handling``

  .. code-block:: python

    def test_catching_things_that_fail(self):
        self.assertEqual(
            exceptions.exception_handler(
                exceptions.raises_exception_error
            ),
            'failed'
        )

  the terminal shows an :doc:`AttributeError`

* GREEN: make it pass

  I add a name to ``exceptions.py`` and the terminal shows `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    exception_handler

  I define ``exception_handler`` and the terminal displays a :doc:`TypeError`

  .. code-block:: python

    exception_handler = None

  when I change ``exception_handler`` to a function the terminal displays a :doc:`TypeError` with a different message

  .. code-block:: python

    def exception_handler():
        return None

  I change the signature for ``exception_handler`` to accept a positional argument

  .. code-block:: python

    def exception_handler(argument):
        return None

  the terminal shows an :doc:`/AssertionError` because the result of calling ``exceptions.exception_handler`` with ``exceptions.raises_exception_error`` as the input is currently :doc:`None <data_structures_none>` which is not equal to ``failed``

  .. code-block:: python

    E    AssertionError: None != 'failed'

  I change ``exception_handler`` to return ``failed`` and the terminal shows passing tests

  .. code-block:: python

    def exception_handler(argument):
        return 'failed'

* RED: make it fail

  the solution has a problem, the ``exception_handler`` always returns ``failed`` regardless of what I provide as an argument

  I should add a new test to ``test_exception_handling`` that provides a different input with an expectation of a different result

  .. code-block:: python

    def test_catching_things_that_succeed(self):
        self.assertEqual(
            exceptions.exception_handler(
                exceptions.does_not_raise_exception_error
            ),
            'succeeded'
        )

  the terminal shows an :doc:`AttributeError`

* GREEN: make it pass

  - I add ``does_not_raise_exception_error`` to ``exceptions.py`` and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

    .. code-block:: python

      does_not_raise_exception_error

  - I assign ``does_not_raise_exception_error`` to the null value :doc:`None <data_structures_none>`

    .. code-block:: python

      does_not_raise_exception_error = None

    and the terminal shows an :doc:`/AssertionError` because the value returned by ``exceptions.exception_handler`` when given ``exceptions.does_not_raise_exception_error`` as input is ``failed`` which is not equal to ``succeeded``

    .. code-block::

      E    AssertionError: 'failed' != 'succeeded'

    I want the ``exception_handler`` function to return a different input based on the exceptions that occur within the function to practice handling exceptions.

  - I change ``exception_handler`` in ``exceptions.py`` to call a function it receives as input

    .. code-block:: python

      def exception_handler(function):
          return function()

    the terminal shows a :doc:`TypeError` because ``does_not_raise_exception_error`` is not a function

  - I change ``does_not_raise_exception_error`` to make it callable

    .. code-block:: python

      def does_not_raise_exception_error():
          return None

    the terminal shows

    .. code-block:: python

      AssertionError: None != 'succeeded'

    - The ``exception_handler`` function returns the result of calling the function it receives as input
    - When I call ``exceptions.exception_handler(exceptions.does_not_raise_exception_error)`` it in turn calls ``does_not_raise_exception_error`` and returns the result of the call which is currently defined as :doc:`None <data_structures_none>`
    - Since the result is not equal to ``succeeded``, the expectation is not met.

  - `try...except...else <https://docs.python.org/3/reference/compound_stmts.html#the-try-statement>`_ statements are used to catch/handle exceptions in python. This allows the program to make a decision when it encounters an Exception.

    I add it to ``exception_handler`` in ``exceptions.py`` to handle exceptions

    .. code-block:: python

      def exception_handler(function):
          try:
              function()
          except Exception:
              return 'failed'
          else:
              return 'succeeded'

    the terminal shows passing tests

I think of the  `try...except...else <https://docs.python.org/3/reference/compound_stmts.html#the-try-statement>`_ statement as
* ``try`` something
* if it raises an ``Exception`` do something
* if it does not raise an exception do something else

In this case

* ``try`` calling ``function()``
* ``except Exception`` - if ``function()`` raises an Exception return ``failed``
* ``else`` - if ``function()`` does not raise an Exception return ``succeeded``


How to use try...except...else...finally
----------------------------------------

there is an extra clause in the `try <https://docs.python.org/3/reference/compound_stmts.html#the-try-statement>`_ statement called ``finally`` that is run no matter what happens in the `try...except...else` blocks

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test to ``test_exception_handling.py``

.. code-block:: python

  def test_finally_always_returns(self):
      self.assertEqual(
          exceptions.always_returns(
              exceptions.does_not_raise_exception_error
          ),
          "always_returns_this"
      )

the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I add a name to ``exceptions.py`` and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    always_returns

* I assign the name to :doc:`None </data_structures_none>` and get an :doc:`AttributeError`

  .. code-block:: python

    always_returns = None

* I redefine ``always_returns`` as a function and the terminal displays a :doc:`TypeError`

  .. code-block:: python

    def always_returns():
        return None

* I change the signature of ``always_returns`` to accept a function that it calls and returns its value

  .. code-block:: python

    def always_returns(function):
        return function()

  the terminal shows

  .. code-block:: python

  AssertionError: None != 'always_returns_this'

  because ``exceptions.always_returns`` returns the value of ``does_not_raise_exception_error`` which is :doc:`None <data_structures_none>` and is not equal to the expectation in the test which is ``always_returns_this``

* I add exception handling with using ``try...except...else``

  .. code-block:: python

    def always_returns(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'

  the terminal displays an :doc:`/AssertionError` since no exception is raised when ``does_not_raise_exception_error`` is called by ``always_returns_this``, it returns ``succeeded`` which is not equal to ``always_returns_this``

* I can try adding another return statement to the function to see if that would work

  .. code-block:: python

    def always_returns(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'
        return 'always_returns_this'

  no change, the terminal still has the same error. In python the ``return`` statement is the last thing run in the function, anything written after a ``return`` statement is ignored

  Since the function returns ``succeeded`` it ignores the return statement below it.

* I can add a clause to force it to ignore the other return statements and only return what I want. I add a ``finally`` clause to the ``try...except...else`` block

  .. code-block:: python

    def always_returns(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'
        finally:
            return 'always_returns_this'

  the terminal shows passing tests. the ``finally`` clause is always run regardless of what happens in the ``try..except..else`` parts

* I will add one more test to verify that the code in the ``finally`` block will always run

  .. code-block:: python

    def test_finally_always_returns(self):
        self.assertEqual(
            exceptions.always_returns(
                exceptions.does_not_raise_exception_error
            ),
            "always_returns_this"
        )
        self.assertEqual(
            exceptions.always_returns(
                exceptions.raises_exception_error
            ),
            'always_returns_this'
        )


* ``always_returns`` could have been defined as a ``singleton`` :doc:`function <functions>` and the tests would still pass, but that would not illustrate how to use ``try...except...else...finally``

  .. code-block:: python

    def always_returns(function):
      return 'always_returns_this`

----

CONGRATULATIONS
Your python powers are growing, you now know

* how to deliberately raise exceptions
* how to verify that exceptions are raised
* how to handle exceptions when they occur

.. admonition:: do you want to

  * `read more about the try statement <https://docs.python.org/3/reference/compound_stmts.html#the-try-statement>`_
  *  `read more about exception handling <https://docs.python.org/3/tutorial/errors.html?highlight=try%20except#handling-exceptions>`_