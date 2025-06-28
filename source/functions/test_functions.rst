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
        self.assertEqual(functions.constant(), 'first_name')

the terminal shows :ref:`AttributeError`

green: make it pass
---------------------------------------------------------------------------------

I change the :ref:`function<functions>` to make it pass

.. code-block:: python

  def constant():
      return 'first_name'

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
test_identity_functions
*********************************************************************************

identity :ref:`functions` return their input as output

red: make it fail
---------------------------------------------------------------------------------

I add a failing test to the ``TestFunctions`` class in ``test_functions.py``

.. code-block:: python

    def test_identity_functions(self):
        self.assertEqual(functions.identity(False), False)

the terminal shows :ref:`AttributeError`

green: make it pass
---------------------------------------------------------------------------------

* I add a :ref:`function<functions>` definition to ``functions.py``

  .. code-block:: python

    def identity():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: identity() takes 0 positional arguments but 1 was given

  because the definition for ``identity`` does not allow inputs and the test sends :ref:`False<test_what_is_false>` as input

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError

* then I make ``identity`` in ``functions.py`` to take 1 positional argument

  .. code-block:: python

    def identity(argument):
        return None

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != False

  because the result of calling ``functions.identity`` with :ref:`False<test_what_is_false>` as input is :ref:`None` which is not equal to the expected result (:ref:`False<test_what_is_false>`)

* I change the definition of ``identity`` to make the test pass

  .. code-block:: python

    def identity(argument):
        return False

  the terminal shows passing tests. I am genius!

refactor: make it better
---------------------------------------------------------------------------------

Wait a minute! Something is not quite right here. The definition for a identity :ref:`function<functions>` was that it returned the same thing it was given, the test passes when :ref:`False<test_what_is_false>` is given as input, will it still pass when another value is given or will it always return :ref:`False<test_what_is_false>`? Time to write a test

* I add a new assertion to ``test_identity_functions``

  .. code-block:: python

    def test_identity_functions(self):
        self.assertEqual(functions.identity(False), False)
        self.assertEqual(functions.identity(True), True)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False != True

  the :ref:`function<functions>` returns :ref:`False<test_what_is_false>` instead of :ref:`True<test_what_is_true>` in the second case, I am not all the way genius, yet

* I change the definition of ``identity`` in ``functions.py``

  .. code-block:: python

    def identity(argument):
        return argument

  the terminal shows passing tests. I have more confidence that the identity :ref:`function<functions>` will return its input.

* I add more tests for good measure using the other Python data structures

  .. code-block:: python

    def test_identity_functions(self):
        self.assertEqual(functions.identity(False), False)
        self.assertEqual(functions.identity(True), True)
        self.assertEqual(functions.identity(None), False)
        self.assertEqual(functions.identity(int), False)
        self.assertEqual(functions.identity(str), False)
        self.assertEqual(functions.identity(tuple), False)
        self.assertEqual(functions.identity(list), False)
        self.assertEqual(functions.identity(set), False)
        self.assertEqual(functions.identity(dict), False)

  the terminal shows :ref:`AssertionError` for each line until I make the input match the output, proving that the identity :ref:`function<functions>` I have defined returns the input it is given. Hooray! I am genius again

----

*********************************************************************************
test_functions_w_positional_arguments
*********************************************************************************

I can make a :ref:`function<functions>` take more than one input

.. code-block:: python

    def test_functions_w_positional_arguments(self):
        self.assertEqual(
            functions.identity_w_positional_arguments(
                'first_name', 'last_name'
            ),
            ('first_name', 'last_name')
        )

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.functions' has no attribute 'identity_w_positional_arguments'

green: make it pass
---------------------------------------------------------------------------------

* I add a :ref:`function<functions>` to  ``functions.py``

  .. code-block:: python

    def identity_w_positional_arguments(argument):
        return argument

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: identity_w_positional_arguments() takes 1 positional argument but 2 were given

  I make the :ref:`function<functions>` take more than one argument

  .. code-block:: python

    def identity_w_positional_arguments(
        argument, second
    ):
        return argument

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != ('first', 'second')

  I make it return the 2 arguments it receives

  .. code-block:: python

    def identity_w_positional_arguments(
        argument, second
    ):
        return argument, second

  the test passes

refactor: make it better
---------------------------------------------------------------------------------

How can I make this better?

* I change the name of the first argument to be more descriptive

  .. code-block:: python

    def identity_w_positional_arguments(
            first, second
        ):
        return first, second

  I still have passing tests

* I add another assertion to make sure that ``identity_w_positional_arguments`` outputs data in the order given

  .. code-block:: python

      def test_functions_w_positional_arguments(self):
          self.assertEqual(
              functions.identity_w_positional_arguments(
                  'first_name', 'last_name'
              ),
              ('first_name', 'last_name')
          )
          self.assertEqual(
              functions.identity_w_positional_arguments(
                  'last_name', 'first_name'
              ),
              ('first_name', 'last_name')
          )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ('last_name', 'first_name') != ('first_name', 'last_name')

* I change the test so it has the right output

  .. code-block:: python

      def test_functions_w_positional_arguments(self):
          self.assertEqual(
              functions.identity_w_positional_arguments(
                  'first_name', 'last_name'
              ),
              ('first_name', 'last_name')
          )
          self.assertEqual(
              functions.identity_w_positional_arguments(
                  'last_name', 'first_name'
              ),
              ('last_name', 'first_name')
          )

  the terminal shows passing

* the :ref:`function<functions>` currently takes in 2 positional arguments.

*********************************************************************************
test_functions_w_unknown_positional_arguments
*********************************************************************************

* There are scenarios where a :ref:`function<functions>` needs to take in more arguments, like when I do not know the number of positional arguments that will be passed to the function, I add a test for the case where the number of positional arguments received is not known

  .. code-block:: python

    def test_functions_w_unknown_arguments(self):
        self.assertEqual(
            src.functions.identity_w_unknown_arguments(
                0, 1, 2, 3
            ),
            (0, 1, 2, 3)
        )

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.functions' has no attribute 'identity_w_unknown_arguments'. Did you mean: 'identity_w_positional_arguments'?

  I add the function with a `starred expression`_ like I did in :ref:`test_constant_functions`, to allow it take in any number of arguments

  .. code-block:: python

    def identity_w_unknown_arguments(*arguments):
        return arguments

  the test passes

* I add another assertion to show that this :ref:`function<functions>` never needs to know the number of inputs it is receiving

  .. code-block:: python

    self.assertEqual(
        src.functions.identity_w_unknown_arguments(
            0, 1, 2, 3
        ),
        (0, 1, 2, 3)
    )
    self.assertEqual(
        src.functions.identity_w_unknown_arguments(
            None, bool, int, float, str, tuple, list, set, dict
        ),
        None
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (None, <class 'bool'>, <class 'int'>, <cl[87 chars]ct'>) != None

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        src.functions.identity_w_unknown_arguments(
            None, bool, int, float, str, tuple, list, set, dict
        ),
        (None, bool, int, float, str, tuple, list, set, dict)
    )

  the test is green again

*********************************************************************************
review
*********************************************************************************

the tests show that

* I can use ``*name`` to represent any number of positional arguments
* positional arguments are represented as tuples_ with parentheses - ``()``
* :ref:`identity functions<test_identity_functions>` return their input
* :ref:`constant functions<test_constant_functions>` always return the same thing
* :ref:`functions` return :ref:`None` by default
* :ref:`functions` are defined using the def_ keyword

Would you like to :ref:`test constant functions?<test_constant_functions>`

----

:doc:`/code/code_functions`


# rename constant