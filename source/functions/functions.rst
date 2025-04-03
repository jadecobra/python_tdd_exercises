.. include:: ../links.rst

#################################################################################
functions
#################################################################################

A ``function`` is a callable_ unit/block of code. It is a way to write statements that can be used to accomplish a task at a different time from when they are written. Using :ref:`functions` makes the code modular which makes it easier to read, test, reuse, maintain and improve.

Programming involves providing a process with input data and the process returning output data

.. code-block:: python

    argument -> program -> output_data

Which is like mathematics where a :ref:`function<functions>` is represented as ``f`` with inputs ``x`` and an output of ``y``

.. math::

  f(x) -> y

in other words

.. code-block:: python

  program(argument) -> output_data

``program`` is the ``function`` that carries out the processing of ``argument`` to return ``output_data``

``functions`` are defined using the def_ keyword, a name, parentheses and a colon at the end

The following tests cover different ways to make a function

.. toctree::
  :titlesonly:
  :maxdepth: 1

  test_functions
  test_singleton_functions<test_singleton_functions>
  test_passthrough_functions<test_passthrough_functions>
  test_functions_w_positional_arguments<test_functions_w_positional_arguments>
  test_functions_w_keyword_arguments<test_functions_w_keyword_arguments>
  test_functions_w_positional_and_keyword_arguments<test_functions_w_positional_and_keyword>

----
