
#####################################
How to handle Exceptions in programs
#####################################

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/tqMRKfPwDAc?si=UMy_NkJvL4Aql8Dq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

:doc:`/how_to/exception_handling_tests` showed how to verify that an exception is raised when testing. This chapter shows how to handle exceptions when they are raised in programs

*************************
Prerequisites
*************************

:doc:`/how_to/exception_handling_tests`

----

*************************
RED: make it fail
*************************

* I add a failing test to ``test_exceptions.py``

  .. code-block:: python

    def test_catching_exceptions(self):
        exceptions.raises_exception()

  the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    NameError: name 'exceptions' is not defined

*************************
GREEN: make it pass
*************************

* I add a new ``import`` statement

  .. code-block:: python

    import exceptions
    import module
    import unittest

  the terminal shows an :doc:`/exceptions/AttributeError`

  .. code-block:: python

    AttributeError: module 'exceptions' has no attribute 'raises_exception'

* I add a name for the attribute to ``exceptions.py``

  .. code-block:: python

    raises_exception

  and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ since I have not defined ``raises_exception`` in ``exceptions.py``

  .. code-block:: python

    NameError: name 'raises_exception' is not defined

* I assign ``raises_exception`` to the null value :doc:`None </data_structures/none>`

  .. code-block:: python

    raises_exception = None

  and the terminal shows a :doc:`/exceptions/TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError

* When I define ``raises_exception`` as a function, the terminal shows passing tests

  .. code-block:: python

    def raises_exception():
        return None

* I can use the `raise <https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement>`_ keyword to cause an exception when ``raises_exception`` is called

  .. code-block:: python

    def raises_exception():
        raise Exception('BOOM')

  the terminal shows the ``Exception`` is raised

  .. code-block:: python

    Exception: BOOM

* I add a ``with self.assertRaises`` context to ``test_catching_exceptions`` in ``test_exceptions.py`` to confirm that the exception is raised and allow the tests to continue

  .. code-block:: python

    def test_catching_exceptions(self):
        with self.assertRaises(Exception):
            exceptions.raises_exception()

  the terminal shows passing tests

*CONGRATULATIONS!*
You now know how to deliberately create an exception which means you have absolute power to reshape the universe to your will

*************************
REFACTOR: make it better
*************************

Time to add exception handling to the program so it returns a message when it encounters an exception instead of stopping


******************************
How to catch things that fail
******************************

RED: make it fail
==================

I add a new failing test to ``test_exceptions.py``

.. code-block:: python

  def test_catching_failures(self):
      self.assertEqual(
          exceptions.exception_handler(
              exceptions.raises_exception
          ),
          'failed'
      )

the terminal shows an :doc:`/exceptions/AttributeError`

.. code-block::

  AttributeError: module 'exceptions' has no attribute 'exception_handler'

GREEN: make it pass
====================

* I add a name to ``exceptions.py``

  .. code-block:: python

    exception_handler

  and the terminal shows `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    NameError: name 'exception_handler' is not defined

* I assign ``exception_handler`` to the null value :doc:`None </data_structures/none>`

  .. code-block:: python

    exception_handler = None

  and the terminal shows a :doc:`/exceptions/TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* When I change ``exception_handler`` to a function

  .. code-block:: python

    def exception_handler():
        return None

  the terminal shows a :doc:`/exceptions/TypeError` with a different message

  .. code-block:: python

    TypeError: exception_handler() takes 0 positional arguments but 1 was given

* I change the :doc:`function signature </functions/functions>` for ``exception_handler`` to accept a positional argument

  .. code-block:: python

    def exception_handler(argument):
        return None

  and the terminal shows an :doc:`/exceptions/AssertionError` because the result of calling ``exceptions.exception_handler`` with ``exceptions.raises_exception`` as the input is currently :doc:`None </data_structures/none>` which is not equal to ``'failed'``

  .. code-block:: python

    AssertionError: None != 'failed'

* I change ``exception_handler`` to return ``'failed'`` and the test passes

  .. code-block:: python

    def exception_handler(argument):
        return 'failed'

*********************************
How to catch things that succeed
*********************************

RED: make it fail
==================

the solution has a problem, the ``exception_handler`` always returns ``'failed'`` regardless of what I provide as an argument. It is a :doc:`singleton function </functions/functions_singleton>`.

I add a new test that provides a different input with an expectation of a different result

.. code-block:: python

  def test_catching_successes(self):
      self.assertEqual(
          exceptions.exception_handler(
              exceptions.does_not_raise_exception
          ),
          'succeeded'
      )

the terminal shows an :doc:`/exceptions/AttributeError`

.. code-block:: python

  AttributeError: module 'exceptions' has no attribute 'does_not_raise_exception'

GREEN: make it pass
====================

* I add ``does_not_raise_exception`` to ``exceptions.py``

  .. code-block:: python

    does_not_raise_exception

    def exception_handler(function):
        ...

  and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    NameError: name 'does_not_raise_exception' is not defined

* I assign ``does_not_raise_exception`` to the null value :doc:`None </data_structures/none>`

  .. code-block:: python

    does_not_raise_exception = None

  and the terminal shows an :doc:`/exceptions/AssertionError` because the value returned by ``exceptions.exception_handler`` when given ``exceptions.does_not_raise_exception`` as input is ``'failed'`` which is not equal to ``'succeeded'``

  .. code-block::

    AssertionError: 'failed' != 'succeeded'

  To practice handling exceptions, I want the ``exception_handler`` function to return a different result based on the exceptions that occur within it

* I make ``exception_handler`` in ``exceptions.py`` call a function it receives as input

  .. code-block:: python

    def exception_handler(function):
        return function()

  the terminal shows a :doc:`/exceptions/TypeError` because ``does_not_raise_exception`` is not  `callable <https://docs.python.org/3/glossary.html#term-callable>`_

  .. code-block:: python

    function = None

        def exception_handler(function):
    >       return function()
    E       TypeError: 'NoneType' object is not callable

* I change ``does_not_raise_exception`` to a function to make it `callable <https://docs.python.org/3/glossary.html#term-callable>`_

  .. code-block:: python

    def does_not_raise_exception():
        return None

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: None != 'succeeded'

  - The ``exception_handler`` :doc:`function </functions/functions>` returns the result of calling the :doc:`function </functions/functions>` it receives as input
  - When I call ``exceptions.exception_handler`` with ``exceptions.does_not_raise_exception`` as input, it calls the :doc:`function </functions/functions>` and returns the result
  - the result of calling ``exceptions.does_not_raise_exception`` is currently :doc:`None </data_structures/none>` which is not equal to ``'succeeded'`` and the result of calling ``exceptions.raises_exception`` is currently an Exception which is not equal to ``'failed'``

*****************************************
How to use try...except...else
*****************************************

`try...except...else <https://docs.python.org/3/reference/compound_stmts.html#the-try-statement>`_ statements are used to catch/handle exceptions in Python. This allows the program to make a decision when it encounters an Exception instead of ending execution.

I add a `try...except...else <https://docs.python.org/3/reference/compound_stmts.html#the-try-statement>`_ statement to ``exception_handler`` in ``exceptions.py`` to handle exceptions

.. code-block:: python

  def exception_handler(function):
      try:
          function()
      except Exception:
          return 'failed'
      else:
          return 'succeeded'

and the terminal shows passing tests

I think of the  `try...except...else <https://docs.python.org/3/reference/compound_stmts.html#the-try-statement>`_ statement as

* ``try`` **this**
* ``except Exception`` - when **this** raises an ``Exception`` do something
* ``else`` - when **this** does not raise an ``Exception`` do something else

In this case

* ``try`` **calling** ``function()``
* ``except Exception`` - when **calling** ``function()`` raises an ``Exception`` return ``'failed'``
* ``else`` - when **calling** ``function()`` does NOT raise an ``Exception`` return ``'succeeded'``


*****************************************
How to use try...except...else...finally
*****************************************

There is an extra clause in the `try <https://docs.python.org/3/reference/compound_stmts.html#the-try-statement>`_ statement called ``finally``. Anything in the ``finally`` clause is always run, regardless of what happens in the ``try...except...else`` blocks

RED: make it fail
=========================

I add a failing test to ``test_exceptions.py``

.. code-block:: python

  def test_finally_always_returns(self):
      self.assertEqual(
          exceptions.always_returns(
              exceptions.does_not_raise_exception
          ),
          "always returns this"
      )

the terminal shows an :doc:`/exceptions/AttributeError`

.. code-block:: python

  AttributeError: module 'exceptions' has no attribute 'always_returns'

GREEN: make it pass
=========================

* I add a name to ``exceptions.py``

  .. code-block:: python

    always_returns

  and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    NameError: name 'always_returns' is not defined

* I assign the name to :doc:`None </data_structures/none>`

  .. code-block:: python

    always_returns = None

  and the terminal shows a :doc:`/exceptions/TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I redefine ``always_returns`` as a function

  .. code-block:: python

    def always_returns():
        return None

  and the terminal shows another :doc:`/exceptions/TypeError` but with a different message

  .. code-block:: python

    TypeError: always_returns() takes 0 positional arguments but 1 was given

* I change the signature of ``always_returns`` to accept a function, and return the result of calling it

  .. code-block:: python

    def always_returns(function):
        return function()

  the terminal shows an :doc:`/exceptions/AssertionError` because ``exceptions.always_returns`` returns the value of calling ``does_not_raise_exception`` which is :doc:`None </data_structures/none>` and is not equal to the expectation in the test which is ``'always returns this'``

  .. code-block:: python

    AssertionError: None != 'always returns this'

* I add exception handling using ``try...except...else``

  .. code-block:: python

    def always_returns(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'

  the terminal shows an :doc:`/exceptions/AssertionError` with a different message. ``always_returns`` returns ``'succeeded'`` since no exception is raised when it calls ``does_not_raise_exception`` and ``'succeeded'`` is not equal to ``'always returns this'``

  .. code-block::

    AssertionError: 'succeeded' != 'always returns this'

* I can try adding another return statement to the function to see if that would work

  .. code-block:: python

    def always_returns(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'
        return 'always returns this'

  no change, the terminal still has the same error. In Python the ``return`` statement is the last thing run in the function. Anything written after a ``return`` statement is ignored, ``always_returns`` currently returns ``succeeded`` from the ``else`` block and ignores the return statement below it

* I have to add a ``finally`` clause to force it to ignore the other return statements and only return what I want

  .. code-block:: python

    def always_returns(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'
        finally:
            return 'always returns this'

  the terminal shows passing tests. The ``finally`` clause is always run regardless of what happens in the ``try..except..else`` blocks

* I add one more test to show that the code in the ``finally`` block will always run

  .. code-block:: python

    def test_finally_always_returns(self):
        self.assertEqual(
            exceptions.always_returns(
                exceptions.does_not_raise_exception
            ),
            "always returns this"
        )
        self.assertEqual(
            exceptions.always_returns(
                exceptions.raises_exception
            ),
            'succeeded'
        )

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: 'always returns this' != 'succeeded'

* I change ``'succeeded'`` to match the expected value

  .. code-block:: python

    def test_finally_always_returns(self):
        self.assertEqual(
            exceptions.always_returns(
                exceptions.does_not_raise_exception
            ),
            "always returns this"
        )
        self.assertEqual(
            exceptions.always_returns(
                exceptions.raises_exception
            ),
            "always returns this"
        )

  and the test passes

.. NOTE::

  ``always_returns`` could have been defined as a :doc:`singleton function </functions/functions_singleton>` and the tests would still pass, but it would not show how to use ``try...except...else...finally`` ::

      def always_returns(function):
          return 'always returns this'

----

CONGRATULATIONS
Your python powers are growing, you have seen

* how to deliberately raise exceptions
* how to verify that exceptions are raised
* how to handle exceptions when they occur

You also encountered the following exceptions

* :doc:`/exceptions/AssertionError`
* :doc:`/exceptions/ModuleNotFoundError`
* `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_
* :doc:`/exceptions/AttributeError`
* :doc:`/exceptions/TypeError`

.. admonition:: do you want to

Do you think you are ready to take on :doc:`/how_to/sleep_duration`?

----

:doc:`/code/code_exception_handling`