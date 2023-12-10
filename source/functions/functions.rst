
functions
=========

A ``function`` is a `callable <https://docs.python.org/3/glossary.html#term-callable>`_ unit/block of code. It is a way to write statements that can be used to accomplish a task at a different time from when they are written. Using functions makes the code modular which makes it easier to read, test, reuse, maintain and improve.

Programming involves providing a process with input data and the process returning output data

.. code-block:: python

    input_data -> program -> output_data

Which is similar to functions in mathematics where a function is represented as ``f`` with inputs ``x`` and an output of ``y``

.. code-block:: python

  f(x) -> y

in other words

.. code-block:: python

  program(input_data) -> output_data

``program`` is the ``function`` that carries out the processing of ``input_data`` to return ``output_data``

``functions`` are defined using the `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword, a name, parentheses and a colon at the end

RED: make it fail
^^^^^^^^^^^^^^^^^

I create a file called ``test_functions.py`` in the ``tests`` folder and add the following failing test

.. code-block:: python

  import unittest
  import functions


  class TestFunctions(unittest.TestCase):

      def test_functions_with_pass(self):
          self.assertIsNone(functions.function_with_pass())

the terminal displays a :doc:`/exceptions/ModuleNotFoundError`\ , and I add it to the list of exceptions encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I create a file called ``functions.py`` in the project folder and the terminal shows an :doc:`/exceptions/AttributeError`\ , which I add to the running list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* I add a function definition to ``functions.py``

  .. code-block:: python

    def function_with_pass():
        pass

  and we have a passing test

  * the test checks if the value of the call to ``functions.function_with_pass`` is :doc:`None </data_structures/none>`
  * the function definition simply says `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ yet the test passes
  * `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a placeholder keyword which allows the function definition to follow python syntax rules
  * the test passes because in python all functions return :doc:`None </data_structures/none>` by default, like the function has an invisible line that says ``return None``

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

* RED: make it fail

  I add a new failing test to ``TestFunctions`` in ``test_functions.py`` to check that functions always return :doc:`None </data_structures/none>`

  .. code-block:: python

      def test_functions_with_return(self):
          self.assertIsNone(functions.function_with_return())

  the terminal shows an :doc:`/exceptions/AttributeError`

* GREEN: make it pass

  I add a new function to ``functions.py`` to make the test pass, this time with a ``return`` statement instead of `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_

  .. code-block:: python

      def function_with_return(self):
          return

  the terminal shows this test also passes

  I defined 2 functions with different statements in their body but they both return the same result, because "in python all functions return :doc:`None </data_structures/none>` by default, like the function has an invisible line that says ``return None``"

* RED: make it fail

  I add one more test to the ``TestFunctions`` class in ``test_functions.py`` to help drive home the point

  .. code-block:: python

      def test_functions_with_return_none(self):
          self.assertIsNone(
              functions.function_with_return_none()
          )

  the terminal shows an :doc:`/exceptions/AttributeError`
* GREEN: make it pass

  from the `Zen of Python <https://peps.python.org/pep-0020/>`_ - ``Explicit is better than implicit.`` I add a function definition to ``functions.py`` this time with an explicit ``return`` statement showing the value returned

  .. code-block:: python

    def function_with_return_none():
        return None

  and the terminal shows passing tests.

The 3 ways I have defined functions so far have the exact same outcome, they all ``return None``. If ``Explicit is better than implicit.`` then I prefer to use ``return None`` telling anyone who reads the code exactly what the function returns.

Here is what I know so far from the tests

* functions are defined using the `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword
* functions return :doc:`None </data_structures/none>` by default