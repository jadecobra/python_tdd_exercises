#############################################################################
functions
#############################################################################

A ``function`` is a callable_ unit/block of code. It is a way to write statements that can be used to accomplish a task at a different time from when they are written. Using functions makes the code modular which makes it easier to read, test, reuse, maintain and improve.

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

The following tests cover different ways to make a function

.. toctree::
  :titlesonly:
  :maxdepth: 1

  test_functions
  test_singleton_functions
  test_passthrough_functions
  test_functions_w_positional_arguments
  test_functions_w_keyword_arguments
  test_functions_w_positional_and_keyword_arguments

----
