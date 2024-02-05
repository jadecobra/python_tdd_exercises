
functions: passthrough
======================

A passthrough :doc:`function </functions/functions>` is one that returns the input it receives as output


RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test to the ``TestFunctions`` class in ``test_functions.py``

.. code-block:: python

    def test_passthrough_function(self):
        self.assertEqual(functions.passthrough(False), False)

the terminal shows an :ref:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I add a function definition to ``functions.py``

  .. code-block:: python

    def passthrough():
        return None

  the terminal shows a :doc:`/exceptions/TypeError` because the definition for ``passthrough`` does not allow ``inputs`` but the test sends :doc:`False </data_structures/booleans/booleans>` as input

  .. code-block:: python

    TypeError: passthrough() takes 0 positional arguments but 1 was given

* I add the new exception to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError

* then change ``passthrough`` in ``functions.py`` to take 1 positional argument

  .. code-block:: python

    def passthrough(input_data):
        return None

  and the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: None != False

  because the result of calling ``functions.passthrough`` with :doc:`False </data_structures/booleans/booleans>` as input is :ref:`None` which is not equal to the expected result (:doc:`False </data_structures/booleans/booleans>`)

* I change the definition of ``passthrough`` to make the test pass

  .. code-block:: python

    def passthrough(input_data):
        return False

  the terminal shows passing tests. I am genius!

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Wait a minute! Something is not quite right here. The definition for a ``passthrough`` function was that it returned the same thing it was given, the test passes when :doc:`False </data_structures/booleans/booleans>` is given as input, will it still pass when another value is given or will it always return :doc:`False </data_structures/booleans/booleans>`? Time to write a test


* RED: make it fail

  I add a new test to ``test_passthrough_function`` in ``TestFunctions`` in ``test_functions.py``

  .. code-block:: python

      def test_passthrough_function(self):
          self.assertEqual(functions.passthrough(False), False)
          self.assertEqual(functions.passthrough(True), True)

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: False != True

  the function returns :doc:`False </data_structures/booleans/booleans>` instead of :doc:`True </data_structures/booleans/booleans>` in the second case, confirming my suspicions, I am not all the way genius, yet

* GREEN: make it pass

  I  change the definition of ``passthrough`` in ``functions.py``

  .. code-block:: python

    def passthrough(input_data):
        return input_data

  the terminal shows passing tests. I have more confidence that the passthrough function will likely return the input data it is given. I will add more tests for good measure using the other python data structures

* REFACTOR: make it better

  I add more tests to ``test_passthrough_function``

  .. code-block:: python

      def test_passthrough_function(self):
          self.assertEqual(functions.passthrough(False), False)
          self.assertEqual(functions.passthrough(True), True)
          self.assertEqual(functions.passthrough(None), False)
          self.assertEqual(functions.passthrough(int), False)
          self.assertEqual(functions.passthrough(str), False)
          self.assertEqual(functions.passthrough(tuple), False)
          self.assertEqual(functions.passthrough(list), False)
          self.assertEqual(functions.passthrough(set), False)
          self.assertEqual(functions.passthrough(dict), False)

  the terminal shows an :doc:`/exceptions/AssertionError` for each line until I make the input match the output, proving that the passthrough function I have defined returns the input it is given. Hooray! I am genius again
