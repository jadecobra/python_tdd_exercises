
#####################################
How to handle Exceptions in programs
#####################################

:doc:`/how_to/exception_handling_tests` showed how to verify that an exception is raised when testing. This chapter shows how to handle exceptions when they are raised in programs

*************************
Prerequisites
*************************

* :doc:`How to create a Test Driven Development Environment </how_to/create_tdd_environment>`
* :doc:`/how_to/exception_handling_tests`

----

*************************
RED: make it fail
*************************

* I add a failing test to ``test_exception_handling.py`` and will cause an exception, then handle it.

  .. code-block:: python

    def test_catching_exceptions(self):
        exceptions.raises_exception_error()

  the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

* I add the error to the running list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError

*************************
GREEN: make it pass
*************************

* A `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ is raised when a name is used within a module with no definition for the name. In the test I call ``exceptions.raises_exception_error`` but there is no definition for ``exceptions``

* I add a new ``import`` statement

  .. code-block:: python

    import unittest
    import module
    import exceptions

  the terminal shows a :doc:`/exceptions/ModuleNotFoundError`

* I create a file called ``exceptions.py`` in the ``project_name`` folder, and the terminal shows an :doc:`/exceptions/AttributeError`
* I add a name for the attribute to ``exceptions.py`` and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ since I have not defined ``raises_exception_error`` in ``exceptions.py``

  .. code-block:: python

    raises_exception_error

* I assign ``raises_exception_error`` to the null value :doc:`None </data_structures/none>` and the terminal shows a :doc:`/exceptions/TypeError`

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

* When I define ``raises_exception_error`` as a function, the terminal shows passing tests

  .. code-block:: python

    def raises_exception_error():
        return None

* I use the `raise <https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement>`_ keyword to cause an exception when ``raises_exception_error`` is called

  .. code-block:: python

    def raises_exception_error():
        raise Exception

  the terminal shows the ``Exception`` is raised

  .. code-block:: python

    Exception

* I add a ``self.assertRaises`` to ``test_catching_exceptions`` in ``test_exception_handling.py`` to confirm that this exception is raised and allow the tests to continue

  .. code-block:: python

    def test_catching_exceptions(self):
        with self.assertRaises(Exception):
            exceptions.raises_exception_error()

  the terminal shows passing tests

*CONGRATULATIONS!*
You now know how to deliberately create an exception which means you have absolute power to reshape the universe to your will

*************************
REFACTOR: make it better
*************************

Time to add exception handling to the program so it returns a message when it encounters an exception instead of stopping


* RED: make it fail

  I add a new failing test to ``test_exception_handling``

  .. code-block:: python

    def test_catching_things_that_fail(self):
        self.assertEqual(
            exceptions.exception_handler(
                exceptions.raises_exception_error
            ),
            'failed'
        )

  the terminal shows an :doc:`/exceptions/AttributeError`

* GREEN: make it pass

  I add a name to ``exceptions.py`` and the terminal shows `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    exception_handler

  I assign ``exception_handler`` to the null value :doc:`None </data_structures/none>` and the terminal shows a :doc:`/exceptions/TypeError`

  .. code-block:: python

    exception_handler = None

  when I change ``exception_handler`` to a function the terminal shows a :doc:`/exceptions/TypeError` with a different message

  .. code-block:: python

    def exception_handler():
        return None

  I change the :doc:`function signature </functions/functions>` for ``exception_handler`` to accept a positional argument

  .. code-block:: python

    def exception_handler(argument):
        return None

  the terminal shows an :doc:`/exceptions/AssertionError` because the result of calling ``exceptions.exception_handler`` with ``exceptions.raises_exception_error`` as the input is currently :doc:`None </data_structures/none>` which is not equal to ``failed``

  .. code-block:: python

    AssertionError: None != 'failed'

  I change ``exception_handler`` to return ``failed`` and the terminal shows passing tests

  .. code-block:: python

    def exception_handler(argument):
        return 'failed'

* RED: make it fail

  the solution has a problem, the ``exception_handler`` always returns ``failed`` regardless of what I provide as an argument. It is a :doc:`singleton function </functions/functions_singleton>`.

  I should add a new test to ``test_exception_handling`` that provides a different input with an expectation of a different result

  .. code-block:: python

    def test_catching_things_that_succeed(self):
        self.assertEqual(
            exceptions.exception_handler(
                exceptions.does_not_raise_exception_error
            ),
            'succeeded'
        )

  the terminal shows an :doc:`/exceptions/AttributeError`

* GREEN: make it pass

  - I add ``does_not_raise_exception_error`` to ``exceptions.py`` and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

    .. code-block:: python

      does_not_raise_exception_error

  - I assign ``does_not_raise_exception_error`` to the null value :doc:`None </data_structures/none>`

    .. code-block:: python

      does_not_raise_exception_error = None

    and the terminal shows an :doc:`/exceptions/AssertionError` because the value returned by ``exceptions.exception_handler`` when given ``exceptions.does_not_raise_exception_error`` as input is ``failed`` which is not equal to ``succeeded``

    .. code-block::

      AssertionError: 'failed' != 'succeeded'

    To practice handling exceptions, I want the ``exception_handler`` function to return a different result based on the exceptions that occur within it

  - I change ``exception_handler`` in ``exceptions.py`` to call a function it receives as input

    .. code-block:: python

      def exception_handler(function):
          return function()

    the terminal shows a :doc:`/exceptions/TypeError` because ``does_not_raise_exception_error`` is not a function

    .. code-block:: python

          def exception_handler(function):
      >       return function()
      E    TypeError: 'NoneType' object is not callable

  - I change ``does_not_raise_exception_error`` to make it callable

    .. code-block:: python

      def does_not_raise_exception_error():
          return None

    the terminal shows

    .. code-block:: python

      AssertionError: None != 'succeeded'

    - The ``exception_handler`` :doc:`function </functions/functions>` returns the result of calling the :doc:`function </functions/functions>` it receives as input
    - When I call ``exceptions.exception_handler`` with ``exceptions.does_not_raise_exception_error`` as input, it calls the :doc:`function </functions/functions>` and returns the result
    - the result of calling ``exceptions.does_not_raise_exception_error`` is currently :doc:`None </data_structures/none>` which is not equal to ``succeeded`` so the expectation of the test is not met

*****************************************
How to use try...except...else
*****************************************

`try...except...else <https://docs.python.org/3/reference/compound_stmts.html#the-try-statement>`_ statements are used to catch/handle exceptions in Python. This allows the program to make a decision when it encounters an Exception.

I add a `try...except...else <https://docs.python.org/3/reference/compound_stmts.html#the-try-statement>`_ statement to ``exception_handler`` in ``exceptions.py`` to handle exceptions

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

* ``try`` **this**
* ``except Exception`` - when **this** raises an ``Exception`` do something
* ``else`` - when **this** does not raise an ``Exception`` do something else

In this case

* ``try`` **calling** ``function()``
* ``except Exception`` - when **calling** ``function()`` raises an ``Exception`` return ``failed``
* ``else`` - when **calling** ``function()`` does not raise an ``Exception`` return ``succeeded``


*****************************************
How to use try...except...else...finally
*****************************************

there is an extra clause in the `try <https://docs.python.org/3/reference/compound_stmts.html#the-try-statement>`_ statement called ``finally`` that is run no matter what happens in the ``try...except...else`` blocks

RED: make it fail
=========================

I add a failing test to ``test_exception_handling.py``

.. code-block:: python

  def test_finally_always_returns(self):
      self.assertEqual(
          exceptions.always_returns(
              exceptions.does_not_raise_exception_error
          ),
          "always_returns_this"
      )

the terminal shows an :doc:`/exceptions/AttributeError`

GREEN: make it pass
=========================

* I add a name to ``exceptions.py`` and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    always_returns

* I assign the name to :doc:`None </data_structures/none>` and get an :doc:`/exceptions/AttributeError`

  .. code-block:: python

    always_returns = None

* I redefine ``always_returns`` as a function and the terminal shows a :doc:`/exceptions/TypeError`

  .. code-block:: python

    def always_returns():
        return None

* I change the signature of ``always_returns`` to accept a function that it calls and returns its value

  .. code-block:: python

    def always_returns(function):
        return function()

  the terminal shows an :doc:`/exceptions/AssertionError` because ``exceptions.always_returns`` returns the value of ``does_not_raise_exception_error`` which is :doc:`None </data_structures/none>` and is not equal to the expectation in the test which is ``'always_returns_this'``

  .. code-block:: python

    AssertionError: None != 'always_returns_this'

* I add exception handling using ``try...except...else``

  .. code-block:: python

    def always_returns(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'

  the terminal shows an :doc:`/exceptions/AssertionError`. No exception is raised when ``does_not_raise_exception_error`` is called by ``always_returns_this``, it returns ``'succeeded'`` which is not equal to ``'always_returns_this'``

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

  no change, the terminal still has the same error. in Python the ``return`` statement is the last thing run in the function, anything written after a ``return`` statement is ignored

  The function returns ``succeeded`` from the ``else`` block and ignores the return statement below it

* I add a ``finally`` clause to force it to ignore the other return statements and only return what I want

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

* I will add one more test to show that the code in the ``finally`` block will always run

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
            'succeeded'
        )

  the terminal shows an :doc:`/exceptions/AssertionError`

* I change the ``succeeded`` to match the expected value

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
            "always_returns_this"
        )

  and the test passes

.. NOTE::

  ``always_returns`` could have been defined as a ``singleton`` :doc:`function </functions/functions>` and the tests would still pass, it  just would not show how to use ``try...except...else...finally`` ::

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

:doc:`/code/code_exception_handling`