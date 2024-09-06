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
test_catching_exceptions
*********************************************************************************

* I add a failing test to ``test_exceptions.py``

  .. code-block:: python

    def test_catching_exceptions(self):
        src.exceptions.raises_exception()

  the terminal shows a :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.exceptions' has no attribute 'raises_exception'

green: make it pass
#################################################################################

* I add the name

  .. code-block:: python

    def function():
        return None

    raises_exception

  and the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'raises_exception' is not defined

* I assign it to :ref:`None`

  .. code-block:: python

    raises_exception = None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

*  I make it a :ref:`function<functions>`

  .. code-block:: python

    def raises_exception():
        return None

  and the terminal shows passing tests

* I can use the `raise <https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement>`_ keyword to cause an exception when ``raises_exception`` is called

  .. code-block:: python

    def raises_exception():
        raise Exception('BOOM')

  the terminal shows the ``Exception`` is raised

  .. code-block:: python

    Exception: BOOM

* I add the `unittest.TestCase.assertRaisesRegex`_ :ref:`method<functions>` to show that this specific Exception_ is raised

  .. code-block:: python

    def test_catching_exceptions(self):
        with self.assertRaisesRegex(
            Exception,
            'BOOM'
        ):
            src.exceptions.raises_exception()

  the terminal shows passing tests

refactor: make it better
#################################################################################

Time to add exception handling to the program so it returns a message when it encounters an Exception_ instead of stopping

----

.. _test_catching_failures:

*********************************************************************************
test_catching_failures
*********************************************************************************

red: make it fail
#################################################################################

I add a new failing test to ``test_exceptions.py``

.. code-block:: python

  def test_catching_failures(self):
      self.assertEqual(
          src.exceptions.exception_handler(
              src.exceptions.raises_exception
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

    def raises_exception():
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

* when I make a :ref:`function<functions>`

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

  and the terminal shows an :ref:`AssertionError` because the result of calling ``src.exceptions.exception_handler`` with ``src.exceptions.raises_exception`` as the input is currently :ref:`None` which is not equal to ``'failed'``

  .. code-block:: python

    AssertionError: None != 'failed'

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

red: make it fail
#################################################################################

the solution has a problem, the ``exception_handler`` always returns ``'failed'`` regardless of what I provide as an argument. It is a :doc:`singleton function </functions/test_singleton_functions>`.

I add a new test that provides a different input with an expectation of a different result

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

    def raises_exception():
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

  and the terminal shows an :ref:`AssertionError` because the value returned by ``src.exceptions.exception_handler`` when given ``src.exceptions.does_not_raise_exception`` as input is ``'failed'`` which is not equal to ``'succeeded'``

  .. code-block::

    AssertionError: 'failed' != 'succeeded'

  To practice handling exceptions, I want the ``exception_handler`` :ref:`function<functions>` to return a different result based on the exceptions that happen inside it

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
  - the result of calling ``src.exceptions.raises_exception`` is currently an Exception which is not equal to ``'failed'``

how to use try...except...else
---------------------------------------------------------------------------------

I add a `try statement`_statement to ``exception_handler`` in ``exceptions.py`` to handle exceptions

.. code-block:: python

  def exception_handler(function):
      try:
          function()
      except Exception:
          return 'failed'
      else:
          return 'succeeded'

and the terminal shows passing tests. The `try statement`_ is used to catch/handle exceptions in Python. It allows the program to make a decision when it encounters an Exception instead of ending execution

I think of the  `try statement`_statement as

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

There is an extra clause in the `try statement`_ statement called ``finally``. Anything in the ``finally`` clause always runs, regardless of what happens in the ``try...except...else`` blocks

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

* I add the name

  .. code-block:: python

    def exception_handler(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'


    always_returns

  and the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'always_returns' is not defined

* I assign the name to :ref:`None`

  .. code-block:: python

    always_returns = None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I make it a :ref:`function<functions>`

  .. code-block:: python

    def always_returns():
        return None

  and the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: always_returns() takes 0 positional arguments but 1 was given

* I make it return the result of calling the input

  .. code-block:: python

    def always_returns(function):
        return function()

  the terminal shows an :ref:`AssertionError` because ``src.exceptions.always_returns`` returns the value of calling ``does_not_raise_exception`` which is :ref:`None` and is not equal to the expectation in the test which is ``'always returns this'``

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

  the terminal shows another :ref:`AssertionError`

  .. code-block::

    AssertionError: 'succeeded' != 'always returns this'

  ``always_returns`` returns ``'succeeded'`` since no exception is raised when it calls ``does_not_raise_exception`` and ``'succeeded'`` is not equal to ``'always returns this'``

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

  no change, the terminal still has the same error. In Python the `return statement`_ is the last thing run in the :ref:`function<functions>`. Anything written after one will not run, ``always_returns`` currently returns ``succeeded`` from the ``else`` block and ignores the `return statement`_ below it

* I have to add a ``finally`` clause to force it to ignore any `return statement`_ and only return what I want

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
                src.exceptions.raises_exception
            ),
            'succeeded'
        )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'always returns this' != 'succeeded'

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
                src.exceptions.raises_exception
            ),
            'always returns this'
        )

  and the test passes

.. NOTE::

  I could have defined ``always_returns`` as a :doc:`singleton function </functions/test_singleton_functions>` and the tests would still pass, but it would not show how to use ``try...except...else...finally`` ::

      def always_returns(function):
          return 'always returns this'

----

.. _exception_handling_programs_review:

*********************************************************************************
review
*********************************************************************************

CONGRATULATIONS
Your Python powers are growing, you have seen

* how to deliberately raise exceptions
* how to verify that exceptions are raised
* how to handle exceptions when they occur

I also encountered the following :ref:`Exceptions<Exceptions>`

Would you like to test :doc:`/how_to/sleep_duration`?

----

:doc:`/code/code_exception_handling`