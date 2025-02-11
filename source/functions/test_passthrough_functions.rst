.. include:: ../links.rst

.. _test_passthrough_functions:

#################################################################################
functions: test_passthrough_functions
#################################################################################

----

.. contents:: table of contents
  :local:
  :depth: 1

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

* I add a:ref:`function<functions>`definition to ``functions.py``

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

  the:ref:`function<functions>`returns :ref:`False<test_what_is_false>` instead of :ref:`True<test_what_is_true>` in the second case, I am not all the way genius, yet

* I change the definition of ``passthrough`` in ``functions.py``

  .. code-block:: python

    def passthrough(argument):
        return argument

  the terminal shows passing tests. I have more confidence that the passthrough:ref:`function<functions>`will return its input.

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

  the terminal shows :ref:`AssertionError` for each line until I make the input match the output, proving that the passthrough:ref:`function<functions>`I have defined returns the input it is given. Hooray! I am genius again

----

*********************************************************************************
review
*********************************************************************************

From the tests I know

* that passthrough :ref:`functions` return what they receive as input
* that singleton :ref:`functions` return the same thing every time they are called
* :ref:`functions` are defined using the def_ keyword
* :ref:`functions` return :ref:`None` by default

Would you like to :ref:`test_functions_w_positional_arguments`?

----

:doc:`/code/code_functions`