.. include:: ../links.rst

functions: singleton
====================

A singleton function is a function that returns the same output every time it is called.

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test to ``test_functions.py``

.. code-block:: python

    def test_singleton_function(self):
        self.assertEqual(functions.singleton(), 'my_first_name')

the terminal shows an :ref:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change ``functions.py`` to make it pass

.. code-block:: python

  def singleton():
      return 'my_first_name'

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

I add a new test that checks if a singleton that accepts inputs returns the same value regardless of the inputs


* change ``test_functions.py``

  .. code-block:: python

      def test_singleton_function_with_input(self):
          self.assertEqual(
              functions.singleton_with_input('Bob', 'James', 'Frank'),
              'joe'
          )
          self.assertEqual(
              functions.singleton_with_input('a', 2, 'c', 3),
              'joe'
          )

  the terminal shows an :ref:`AttributeError`
* and I add a function for ``singleton_with_inputs`` to ``functions.py`` to make the test pass

  .. code-block:: python

    def singleton_with_inputs(*args):
        return 'joe'

From the tests I know

* that singleton functions return the same thing every time they are called
* that positional arguments are represented as `tuples <https://docs.python.org/3/library/stdtypes.html#tuple>`_ with parentheses - ``()``
* that keyword arguments are represented as :doc:`dictionaries </data_structures/dictionaries>`  with curly braces - ``{}``
* how to write functions in Python that can take in any number of positional or keyword arguments as inputs
* I can use ``*name`` to represent any number of positional arguments
* I can use ``**name`` to represent any number of keyword arguments
* I can define default values for arguments
* positional arguments must come before keyword arguments

Do you want to read more about functions?


* `functions <https://docs.python.org/3/glossary.html#term-function>`_
* `methods <https://docs.python.org/3/glossary.html#term-method>`_
* `parameters <https://docs.python.org/3/glossary.html#term-parameter>`_
* `function definitions <https://docs.python.org/3/reference/compound_stmts.html#function-definitions>`_
* `nested scope <https://docs.python.org/3/glossary.html#term-nested-scope>`_
