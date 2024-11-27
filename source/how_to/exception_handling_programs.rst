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

    def function_name():
        return None

    raise_exception

  and the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'raise_exception' is not defined

* I point it to :ref:`None`

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

* I want the :ref:`function<functions>` to raise an Exception_ when called

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

* I can use the `unittest.TestCase.assertRaisesRegex`_ :ref:`method<functions>` which takes in two values, an Exception_ and a message to be more specific when catching Exceptions_

  .. code-block:: python

    def test_catching_exceptions_w_messages(self):
        with self.assertRaisesRegex(
            Exception, 'BOOM!'
        ):
            src.exceptions.raise_exception()

  this gives me an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: "BOOM!" does not match ""

  the Exception_ is right, the message is not

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

Time to add exception handling for the program to send a message when an Exception_ happens

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

* I point it to :ref:`None`

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

* I change the `return statement`_ to match the expectation

  .. code-block:: python

    def exception_handler(argument):
        return 'failed'

  and the test passes

----

.. _test_catching_success:

*********************************************************************************
test_catching_success
*********************************************************************************

the solution has a problem, the ``exception_handler`` is a :doc:`singleton function </functions/test_singleton_functions>`, it does not care about the input and always returns ``'failed'``. I want it to do something with the input and return ``failed`` if an Exception_ happens or ``success`` if an Exception_ does not happen

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

* I point ``does_not_raise_exception`` to :ref:`None`

  .. code-block:: python

    does_not_raise_exception = None

  and the terminal shows an :ref:`AssertionError`

  .. code-block::

    AssertionError: 'failed' != 'succeeded'

  ``src.exceptions.exception_handler`` still returns ``'failed'`` and the test expects ``'succeeded'``

* I make ``exception_handler`` return its input

  .. code-block:: python

    def exception_handler(argument):
        return argument
        return 'failed'

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    REPLACE_ME!!!!!!!

* I rename the input parameter and make it return the result of a call to it as a :ref:`function<functions>`

  .. code-block:: python

    def exception_handler(a_function):
        return a_function()
        return 'failed'

  the terminal shows a :ref:`TypeError`

  .. code-block:: python

    a_function = None

        def exception_handler(a_function):
    >       return a_function()
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

* I add a `try statement`_ statement to handle Exceptions_

  .. code-block:: python

    def exception_handler(a_function):
        try:
            a_function()
        except Exception:
            return 'failed'

  the terminal still shows the :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 'succeeded'

* I add an ``else`` clause

  .. code-block:: python

    def exception_handler(a_function):
        try:
            a_function()
        except Exception:
            return 'failed'
        else:
            return None

  still an :ref:`AssertionError`

* I change the `return statement`_

  .. code-block:: python

    def exception_handler(a_function):
        try:
            a_function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'

  and the terminal shows passing tests

The `try statement`_ is used to catch/handle exceptions in Python. It allows the program to make a decision when it encounters an Exception instead of ending execution

I think of the  `try statement`_ statement as

* ``try`` **this**
* ``except Exception`` - when **this** raises this ``Exception`` run the code in this block
* ``else`` - when **this** does NOT raise the ``Exception`` in the ``except`` block, run the code in this block

In this case

* ``try`` **calling** ``a_function()``
* ``except Exception`` - when **calling** ``a_function()`` raises an ``Exception`` return ``'failed'``
* ``else`` - when **calling** ``a_function()`` does NOT raise the ``Exception`` return ``'succeeded'``

----

.. _exception_handling_programs_review:

*********************************************************************************
review
*********************************************************************************

I ran tests to show how to cause Exceptions_, and catch or handle them in tests and programs. Would you like to test :doc:`measuring sleep duration?</how_to/sleep_duration>`

----

:doc:`/code/code_exception_handling`