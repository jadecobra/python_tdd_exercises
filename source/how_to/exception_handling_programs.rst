.. include:: ../links.rst

.. _Exceptions:

#################################################################################
how to handle Exceptions in programs
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/tqMRKfPwDAc?si=UMy_NkJvL4Aql8Dq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

This is a continuation of :doc:`exception_handling_tests`

.. contents:: table of contents
  :local:
  :depth: 1

----

.. _test_catching_exceptions:

*********************************************************************************
test_catching_exceptions_w_messages
*********************************************************************************

* I add a failing test to ``test_exceptions.py``

  .. code-block:: python

    def test_catching_exceptions_w_messages(self):
        src.exceptions.raise_exception()

  the terminal shows a :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.exceptions' has no attribute 'raise_exception'

green: make it pass
#################################################################################

* I add the name

  .. code-block:: python

    def function():
        return None

    raise_exception

  and the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'raise_exception' is not defined

* I assign it to :ref:`None`

  .. code-block:: python

    raise_exception = None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I make it a :ref:`function<functions>`

  .. code-block:: python

    def raise_exception():
        return None

  and the terminal shows passing tests

* I want the :ref:`function<functions>`  to raise an Exception_

  .. code-block:: python

    def test_catching_exceptions_w_messages(self):
        with self.assertRaises(Exception):
            src.exceptions.raise_exception()

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Exception not raised

* I can use the `raise <https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement>`_ keyword to cause one

  .. code-block:: python

    def raise_exception():
        raise Exception

  the terminal shows a passing test

* The problem with this is that this will catch any Exception_ I use, for example

  .. code-block:: python

    def raise_exception():
        raise AssertionError

  the terminal still shows a passing test

* I add the `unittest.TestCase.assertRaisesRegex`_ :ref:`method<functions>` which takes in two values, an Exception_ and a message

  .. code-block:: python

    def test_catching_exceptions_w_messages(self):
        with self.assertRaisesRegex(
            Exception, 'BOOM!'
        ):
            src.exceptions.raise_exception()

  which gives me an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: "BOOM!" does not match ""

  though the Exception_ is right, the message is not

* I add it to the :ref:`function<functions>`

  .. code-block:: python

    def raise_exception():
        raise Exception('BOOM!')

  and the test passes

* I can also replace the ``raise Exception`` line in the previous test

  .. code-block:: python

    def test_catching_exceptions_in_tests(self):
        with self.assertRaises(Exception):
            src.exceptions.raise_exception()

  and the terminal still shows passing tests

----

.. _test_catching_failure:

*********************************************************************************
test_catching_failure
*********************************************************************************

Next, I add exception handling for the program to send a message when an Exception_ happens

red: make it fail
#################################################################################

I add a new failing test to ``test_exceptions.py``

.. code-block:: python

  def test_catching_failure(self):
      self.assertEqual(
          src.exceptions.exception_handler(
              src.exceptions.raise_exception
          ),
          'failed'
      )

the terminal shows an :ref:`AttributeError`

.. code-block::

  AttributeError: module 'src.exceptions' has no attribute 'exception_handler'

green: make it pass
#################################################################################

* I add the name

  .. code-block:: python

    def raise_exception():
        raise Exception('BOOM')


    exception_handler

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'exception_handler' is not defined

* I assign it to :ref:`None`

  .. code-block:: python

    exception_handler = None

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* when I make it a :ref:`function<functions>`

  .. code-block:: python

    def exception_handler():
        return None

  the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: exception_handler() takes 0 positional arguments but 1 was given

* I make it take a positional argument

  .. code-block:: python

    def exception_handler(argument):
        return None

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 'failed'

  because the result of calling ``src.exceptions.exception_handler`` is :ref:`None` and the test expects ``'failed'``

* I change the `return statement`_ to match the exceptation

  .. code-block:: python

    def exception_handler(argument):
        return 'failed'

  and the test passes

----

.. _test_catching_success:

*********************************************************************************
test_catching_success
*********************************************************************************

the solution has a problem, the ``exception_handler`` is a :doc:`singleton function </functions/test_singleton_functions>` that always returns ``'failed'`` it does not care about the input. I want it to do something with the input and return ``failed`` only if an Exception_ happens or ``success`` if nothing happens

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_catching_success(self):
      self.assertEqual(
          src.exceptions.exception_handler(
              src.exceptions.does_not_raise_exception
          ),
          'succeeded'
      )

the terminal shows an :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.exceptions' has no attribute 'does_not_raise_exception'

green: make it pass
#################################################################################

* I add ``does_not_raise_exception`` to ``exceptions.py``

  .. code-block:: python

    def raise_exception():
        raise Exception('BOOM')


    does_not_raise_exception


    def exception_handler(argument):
        return 'failed'

  and the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'does_not_raise_exception' is not defined

* I assign ``does_not_raise_exception`` to :ref:`None`

  .. code-block:: python

    does_not_raise_exception = None

  and the terminal shows an :ref:`AssertionError`

  .. code-block::

    AssertionError: 'failed' != 'succeeded'

  ``src.exceptions.exception_handler`` still always returns ``'failed'`` and the test expects ``'succeeded'``

* I make ``exception_handler`` call its input as a :ref:`function<functions>`

  .. code-block:: python

    def exception_handler(function):
        return function()
        return 'failed'

  the terminal shows a :ref:`TypeError`

  .. code-block:: python

    function = None

        def exception_handler(function):
    >       return function()
    E       TypeError: 'NoneType' object is not callable

  because ``does_not_raise_exception`` is not callable_

* I make it a :ref:`function<functions>` to make it callable_

  .. code-block:: python

    def does_not_raise_exception():
        return None

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 'succeeded'

  - The ``exception_handler`` :ref:`function<functions>` returns the result of calling the :ref:`function<functions>` it receives as input
  - When I call ``src.exceptions.exception_handler`` with ``src.exceptions.does_not_raise_exception`` as input, it calls the :ref:`function<functions>` and returns the result which is :ref:`None` and is not equal to ``'succeeded'``
  - the result of calling ``src.exceptions.raise_exception`` is currently an Exception which is not equal to ``'failed'``

how to use try...except...else
---------------------------------------------------------------------------------

I add a `try statement`_ statement to handle exceptions

.. code-block:: python

  def exception_handler(function):
      try:
          function()
      except Exception:
          return 'failed'
      else:
          return 'succeeded'

and the terminal shows passing tests. The `try statement`_ is used to catch/handle exceptions in Python. It allows the program to make a decision when it encounters an Exception instead of ending execution

I think of the  `try statement`_ statement as

* ``try`` **this**
* ``except Exception`` - when **this** raises an ``Exception`` do something
* ``else`` - when **this** does not raise an ``Exception`` do something else

In this case

* ``try`` **calling** ``function()``
* ``except Exception`` - when **calling** ``function()`` raises an ``Exception`` return ``'failed'``
* ``else`` - when **calling** ``function()`` does NOT raise an ``Exception`` return ``'succeeded'``

----

.. _test_finally_always_returns:

*********************************************************************************
test_finally_always_returns
*********************************************************************************

There is an extra clause in the `try statement`_ statement called ``finally``. Anything in this clause always runs, regardless of what happens in the ``try...except...else`` blocks

red: make it fail
#################################################################################

I add a failing test to ``test_exceptions.py``

.. code-block:: python

  def test_finally_always_returns(self):
      self.assertEqual(
          src.exceptions.always_returns(
              src.exceptions.does_not_raise_exception
          ),
          'always returns this'
      )

the terminal shows an :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.exceptions' has no attribute 'always_returns'

green: make it pass
#################################################################################

* I make a copy of ``exception_handler`` and change the name of the copy to ``always_returns``

  .. code-block:: python

    def always_returns(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'

  the terminal shows an :ref:`AssertionError`

  .. code-block::

    AssertionError: 'succeeded' != 'always returns this'

  the :ref:`function<functions>` returns ``'succeeded'`` since no exception is raised when it calls ``does_not_raise_exception`` and ``'succeeded'`` is not equal to ``'always returns this'``

* I can try adding another `return statement`_ to the function to see if that would work

  .. code-block:: python

    def always_returns(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'
        return 'always returns this'

  no change, the terminal still has the same error. In Python the `return statement`_ is the last thing run in a :ref:`function<functions>`. Anything written after one will not run, ``always_returns`` currently returns ``succeeded`` from the ``else`` block and ignores the `return statement`_ below it

* I have to add a ``finally`` clause to force it to ignore any `return statement`_ and return only what I want

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

* I add another assertion to show that the code in the ``finally`` block will always run

  .. code-block:: python

    def test_finally_always_returns(self):
        self.assertEqual(
            src.exceptions.always_returns(
                src.exceptions.does_not_raise_exception
            ),
            'always returns this'
        )
        self.assertEqual(
            src.exceptions.always_returns(
                src.exceptions.raise_exception
            ),
            'failed'
        )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'always returns this' != 'failed'

* I change the expectation to match reality

  .. code-block:: python

    def test_finally_always_returns(self):
        self.assertEqual(
            src.exceptions.always_returns(
                src.exceptions.does_not_raise_exception
            ),
            'always returns this'
        )
        self.assertEqual(
            src.exceptions.always_returns(
                src.exceptions.raise_exception
            ),
            'always returns this'
        )

  and the test passes

* in this case, it would be the same as

  .. code-block:: python

    def always_returns(function):
        try:
            function()
        except Exception:
            return 'always returns this'
        else:
            return 'always returns this'

  which would be the same as defining ``always_returns`` as a :doc:`singleton function </functions/test_singleton_functions>`

  .. code-block:: python

      def always_returns(function):
          return 'always returns this'

  and the tests would still pass, but that would not show how to use ``try...except...else...finally``

----

.. _exception_handling_programs_review:

*********************************************************************************
review
*********************************************************************************

I ran tests to show how to cause Exceptions_, and catch/handle them in tests and programs. Would you like to test :doc:`how to measure sleep duration?</how_to/sleep_duration>`

----

:doc:`/code/code_exception_handling`