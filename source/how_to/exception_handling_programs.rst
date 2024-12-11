.. include:: ../links.rst

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

  and the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.exceptions' has no attribute 'raise_exception'

green: make it pass
#################################################################################

* I add the name to ``exceptions.py``

  .. code-block:: python

    def function_name():
        return None


    raise_exception

  and get NameError_

  .. code-block:: python

    NameError: name 'raise_exception' is not defined

* I point it to :ref:`None`

  .. code-block:: python

    raise_exception = None

  and the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* When I make it a :ref:`function<functions>`

  .. code-block:: python

    def raise_exception():
        return None

  the terminal shows passing tests

* I want the :ref:`function<functions>` to raise an Exception_ when it is called

  .. code-block:: python

    def test_catching_exceptions_w_messages(self):
        with self.assertRaises(Exception):
            src.exceptions.raise_exception()

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Exception not raised

* I use the `raise statement`_

  .. code-block:: python

    def raise_exception():
        raise Exception

  and the test passes

* I can use the `unittest.TestCase.assertRaisesRegex`_ :ref:`method<functions>` to be more specific in tests, it checks that the code in its context raises the Exception_ it is given, with the message it is given, it uses `Regular Expressions`_ for this

  .. code-block:: python

    def test_catching_exceptions_w_messages(self):
        with self.assertRaisesRegex(
            Exception, 'BOOM!'
        ):
            src.exceptions.raise_exception()

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: "BOOM!" does not match ""

* the Exception_ is right, the message is not. I add it

  .. code-block:: python

    def raise_exception():
        raise Exception('BOOM!')

  and the test passes. Time to add an :doc:`exception handler</how_to/exception_handling_tests>` to the program

----

.. _test_catching_failure:

*********************************************************************************
test_catching_failure
*********************************************************************************

red: make it fail
#################################################################################

I add a new failing test

.. code-block:: python

  def test_catching_failure(self):
      self.assertEqual(
          src.exceptions.exception_handler(
              src.exceptions.raise_exception
          ),
          'failed'
      )

the terminal shows :ref:`AttributeError`

.. code-block::

  AttributeError: module 'src.exceptions' has no attribute 'exception_handler'

green: make it pass
#################################################################################

* When I add the name

  .. code-block:: python

    def raise_exception():
        raise Exception('BOOM')


    exception_handler

  I get NameError_

  .. code-block:: python

    NameError: name 'exception_handler' is not defined

* I point it to :ref:`None`

  .. code-block:: python

    exception_handler = None

  and get :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* then I make it a :ref:`function<functions>`

  .. code-block:: python

    def exception_handler():
        return None

  and get a different message for the :ref:`TypeError`

  .. code-block:: python

    TypeError: exception_handler() takes 0 positional arguments but 1 was given

* I make the :ref:`function<functions>` take input

  .. code-block:: python

    def exception_handler(argument):
        return None

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 'failed'

  because the result of calling ``src.exceptions.exception_handler`` is :ref:`None` and the test expects ``'failed'``

* I change the `return statement`_ to match the expectation

  .. code-block:: python

    def exception_handler(argument):
        return 'failed'

  and the test passes.

----

.. _test_catching_success:

*********************************************************************************
test_catching_success
*********************************************************************************

I want ``exception_handler`` to process the input and return ``failed`` when an Exception_ happens or ``success`` when it does not.

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

and get :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.exceptions' has no attribute 'does_not_raise_exception'

green: make it pass
#################################################################################

* I add the name to ``exceptions.py``

  .. code-block:: python

    def raise_exception():
        raise Exception('BOOM')


    does_not_raise_exception


    def exception_handler(argument):
        return 'failed'

  and the terminal shows NameError_

  .. code-block:: python

    NameError: name 'does_not_raise_exception' is not defined

* I point it to :ref:`None`

  .. code-block:: python

    does_not_raise_exception = None

  and get :ref:`AssertionError`

  .. code-block::

    AssertionError: 'failed' != 'succeeded'

  ``src.exceptions.exception_handler`` still returns ``'failed'`` and the test expects ``'succeeded'``

* I make ``exception_handler`` return its input

  .. code-block:: python

    def exception_handler(argument):
        return argument
        return 'failed'

  and two tests have :ref:`AssertionError`

  .. code-block:: python

    FAILED tests/test_exceptions.py::TestExceptions::test_catching_failure - AssertionError: <function raise_exception at 0xabcd12e34567> != 'failed'
    FAILED tests/test_exceptions.py::TestExceptions::test_catching_success - AssertionError: None != 'succeeded'

  - ``test_catching_failure`` fails - in this test ``exception_handler`` returns the name of the :ref:`function<functions>` it receives and its address in memory
  - ``test_catching_success`` still fails - in this test ``exception_handler`` returns ``does_not_raise_exception`` which points to :ref:`None`

* I rename the input parameter

  .. code-block:: python

    def exception_handler(a_function):
        return a_function
        return 'failed'

  then make ``exception_handler`` return the result of a call to its input as a :ref:`function<functions>`

  .. code-block:: python

    def exception_handler(a_function):
        return a_function()
        return 'failed'

  - and the terminal shows :ref:`TypeError`

    .. code-block:: python

      a_function = None

          def exception_handler(a_function):
      >       return a_function()
      E       TypeError: 'NoneType' object is not callable

    because ``does_not_raise_exception`` points to :ref:`None`, which is not callable_. I make it a :ref:`function<functions>` to fix this

    .. code-block:: python

      def does_not_raise_exception():
          return None

    and the terminal shows :ref:`AssertionError`

    .. code-block:: python

      AssertionError: None != 'succeeded'

  - the result of calling ``src.exceptions.raise_exception`` in ``test_catching_failure`` is an Exception_ with a message

    .. code-block:: python

      FAILED tests/test_exceptions.py::TestExceptions::test_catching_failure - Exception: 'BOOM!'

how to use try...except...else
---------------------------------------------------------------------------------

* when I add a `try statement`_ statement

  .. code-block:: python

    def exception_handler(a_function):
        try:
            a_function()
        except Exception:
            return 'failed'

  ``test_catching_failure`` passes and the terminal still shows :ref:`AssertionError`

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

  then change its `return statement`_

  .. code-block:: python

    def exception_handler(a_function):
        try:
            a_function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'

  and the terminal shows passing tests

  The `try statement`_ is used to catch/handle exceptions in Python. It allows the program to make a decision when it runs into an Exception_. I think of it as

  - ``try`` **this**
  - ``except Exception`` - when **this** raises ``Exception`` run the code in this block
  - ``else`` - when **this** does NOT raise ``Exception`` run the code in this block

  In this case

  - ``try`` **calling** ``a_function()``
  - ``except Exception`` - when **calling** ``a_function()`` raises ``Exception`` return ``'failed'``
  - ``else`` - when **calling** ``a_function()`` does NOT raise ``Exception`` return ``'succeeded'``

* I can be more specific with the Exception_ in the ``except`` block, for example

  .. code-block:: python

    def exception_handler(a_function):
        try:
            a_function()
        except ModuleNotFoundError:
            return 'failed'
        else:
            return 'succeeded'

  shows this in the terminal

  .. code-block:: python

    Exception: 'BOOM!'

  because it is not a :ref:`ModuleNotFoundError`, this `try statement`_ will only catch the Exception_ given in the ``except`` block, all others will be raised

* I change it back to what works

  .. code-block:: python

    def exception_handler(a_function):
        try:
            a_function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'

  and the terminal shows green again

----

.. _exception_handling_programs_review:

*********************************************************************************
review
*********************************************************************************

I ran tests to show how to cause Exceptions_, and catch or handle them in tests and programs. Would you like to test :doc:`measuring sleep duration?</how_to/sleep_duration>`

----

:doc:`/code/code_exception_handling`