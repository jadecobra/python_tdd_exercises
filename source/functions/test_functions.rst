.. include:: ../links.rst

#################################################################################
test_functions
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----


*********************************************************************************
test_functions_w_pass
*********************************************************************************

red: make it fail
---------------------------------------------------------------------------------

* I open a terminal to run :ref:`makePythonTdd.sh` with ``functions`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh functions

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 functions

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_functions.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_functions.py:7`` to open it in the editor
* then change ``True`` to ``False``
* and change ``test_failure``

.. code-block:: python

  import unittest
  import functions


  class TestFunctions(unittest.TestCase):

      def test_functions_w_pass(self):
          self.assertIsNone(functions.function_w_pass())

the terminal shows :ref:`ModuleNotFoundError` , and I add it to the list of Exceptions_ encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError

green: make it pass
---------------------------------------------------------------------------------

* I make a file called ``functions.py`` in the project folder and the terminal shows :ref:`AttributeError`\ , which I add to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* I add a :ref:`function<functions>` definition to ``functions.py``

  .. code-block:: python

    def function_w_pass():
        pass

  and we have a passing test

  * the test checks if the value of the call to ``functions.function_w_pass`` is :ref:`None`
  * the :ref:`function<functions>` definition simply says `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ yet the test passes
  * `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a placeholder keyword which allows the :ref:`function<functions>` definition to follow Python syntax rules
  * the test passes because in Python all :ref:`functions` return :ref:`None` by default, like the :ref:`function<functions>` has an invisible line that says ``return None``

----

*********************************************************************************
test_functions_w_return
*********************************************************************************

red: make it fail
---------------------------------------------------------------------------------

I add a new failing test to ``TestFunctions`` in ``test_functions.py`` to check that :ref:`functions` always return :ref:`None`

.. code-block:: python

    def test_functions_w_return(self):
        self.assertIsNone(functions.function_w_return())

the terminal shows :ref:`AttributeError`

green: make it fail
---------------------------------------------------------------------------------

I add a new :ref:`function<functions>` to ``functions.py`` to make the test pass, this time with a ``return`` statement instead of `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_

.. code-block:: python

    def function_w_return(self):
        return

the terminal shows this test also passes

I defined 2 :ref:`functions` with different statements in their body but they both return the same result, because "in Python all :ref:`functions` return :ref:`None` by default, like the :ref:`function<functions>` has an invisible line that says ``return None``"

*********************************************************************************
test_functions_w_return_none
*********************************************************************************

red: make it fail
---------------------------------------------------------------------------------

I add one more test to the ``TestFunctions`` class in ``test_functions.py`` to help drive home the point

.. code-block:: python

    def test_functions_w_return_none(self):
        self.assertIsNone(
            functions.function_w_return_none()
        )

the terminal shows :ref:`AttributeError`

green: make it pass
---------------------------------------------------------------------------------

from the `Zen of Python`_: ``Explicit is better than implicit.`` I add a :ref:`function<functions>` definition to ``functions.py`` this time with an explicit ``return`` statement showing the value returned

.. code-block:: python

  def function_w_return_none():
      return None

and the terminal shows passing tests.

*********************************************************************************
test_constant_functions
*********************************************************************************

constant :ref:`functions` always return the same thing when called

red: make it fail
---------------------------------------------------------------------------------

I add a test to ``test_functions.py``

.. code-block:: python

    def test_constant_functions(self):
        self.assertEqual(functions.constant(), 'my_first_name')

the terminal shows :ref:`AttributeError`

green: make it pass
---------------------------------------------------------------------------------

I change the :ref:`function<functions>` to make it pass

.. code-block:: python

  def constant():
      return 'my_first_name'

----

*********************************************************************************
test_constant_functions_w_inputs
*********************************************************************************

red: make it fail
---------------------------------------------------------------------------------

I add a new test that checks if a constant that takes inputs returns the same value regardless of the inputs

.. code-block:: python

  def test_constant_functions_w_inputs(self):
      self.assertEqual(
          functions.constant_w_inputs('Bob', 'James', 'Frank'),
          'joe'
      )
      self.assertEqual(
          functions.constant_w_inputs('a', 2, 'c', 3),
          'joe'
      )

the terminal shows :ref:`AttributeError`

green: make it pass
---------------------------------------------------------------------------------

and I add a :ref:`function <functions>` for ``constant_w_inputs`` to ``functions.py``

.. code-block:: python

  def constant_w_inputs(*args):
      return 'joe'

the terminal shows passing tests

----

*********************************************************************************
test_passthrough_functions
*********************************************************************************

Passthrough :ref:`functions` return their input as output

red: make it fail
---------------------------------------------------------------------------------

I add a failing test to the ``TestFunctions`` class in ``test_functions.py``

.. code-block:: python

    def test_passthrough_functions(self):
        self.assertEqual(functions.passthrough(False), False)

the terminal shows :ref:`AttributeError`

green: make it pass
---------------------------------------------------------------------------------

* I add a :ref:`function<functions>` definition to ``functions.py``

  .. code-block:: python

    def passthrough():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: passthrough() takes 0 positional arguments but 1 was given

  because the definition for ``passthrough`` does not allow inputs and the test sends :ref:`False<test_what_is_false>` as input

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError

* then I make ``passthrough`` in ``functions.py`` to take 1 positional argument

  .. code-block:: python

    def passthrough(argument):
        return None

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != False

  because the result of calling ``functions.passthrough`` with :ref:`False<test_what_is_false>` as input is :ref:`None` which is not equal to the expected result (:ref:`False<test_what_is_false>`)

* I change the definition of ``passthrough`` to make the test pass

  .. code-block:: python

    def passthrough(argument):
        return False

  the terminal shows passing tests. I am genius!

refactor: make it better
---------------------------------------------------------------------------------

Wait a minute! Something is not quite right here. The definition for a passthrough :ref:`function<functions>` was that it returned the same thing it was given, the test passes when :ref:`False<test_what_is_false>` is given as input, will it still pass when another value is given or will it always return :ref:`False<test_what_is_false>`? Time to write a test

* I add a new assertion to ``test_passthrough_functions``

  .. code-block:: python

    def test_passthrough_functions(self):
        self.assertEqual(functions.passthrough(False), False)
        self.assertEqual(functions.passthrough(True), True)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False != True

  the :ref:`function<functions>` returns :ref:`False<test_what_is_false>` instead of :ref:`True<test_what_is_true>` in the second case, I am not all the way genius, yet

* I change the definition of ``passthrough`` in ``functions.py``

  .. code-block:: python

    def passthrough(argument):
        return argument

  the terminal shows passing tests. I have more confidence that the passthrough :ref:`function<functions>` will return its input.

* I add more tests for good measure using the other Python data structures

  .. code-block:: python

    def test_passthrough_functions(self):
        self.assertEqual(functions.passthrough(False), False)
        self.assertEqual(functions.passthrough(True), True)
        self.assertEqual(functions.passthrough(None), False)
        self.assertEqual(functions.passthrough(int), False)
        self.assertEqual(functions.passthrough(str), False)
        self.assertEqual(functions.passthrough(tuple), False)
        self.assertEqual(functions.passthrough(list), False)
        self.assertEqual(functions.passthrough(set), False)
        self.assertEqual(functions.passthrough(dict), False)

  the terminal shows :ref:`AssertionError` for each line until I make the input match the output, proving that the passthrough :ref:`function<functions>` I have defined returns the input it is given. Hooray! I am genius again

----


*********************************************************************************
review
*********************************************************************************

The 3 ways I have defined :ref:`functions` so far have the exact same outcome, they all ``return None``. If ``Explicit is better than implicit.`` then I prefer to use ``return None`` telling anyone who reads the code exactly what the :ref:`function<functions>` returns.

Here is what I know so far from the tests

* :ref:`passthrough functions<test_passthrough_functions>` return their input
* :ref:`constant functions<test_constant_functions>` always return the same thing
* :ref:`functions` are defined using the def_ keyword
* :ref:`functions` return :ref:`None` by default

Would you like to :ref:`test constant functions?<test_constant_functions>`

----

:doc:`/code/code_functions`


# rename constant