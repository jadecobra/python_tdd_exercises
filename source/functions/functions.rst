.. include:: ../links.rst

#################################################################################
functions
#################################################################################

A :ref:`function <test_functions>` is a unit or block of code that is callable_. I can write statements that I can used to do something and call it at different time from when I write it. They can make code smaller and easier to read, test, reuse, maintain and improve.

Programming involves providing a process with input data and the process returning output data

.. code-block:: python

    argument -> program -> output_data

I think of it mathematically as mapping a :ref:`function<test_functions>` ``f`` with inputs ``x`` and an output of ``y``

.. math::

  f(x) -> y

in other words

.. code-block:: python

  program(argument) -> output_data

``program`` is the :ref:`function <test_functions>` that processes ``argument`` to return ``output_data``

``functions`` are defined using the def_ keyword, a name, parentheses and a colon at the end

The following tests cover different ways to make a function

.. toctree::
  :titlesonly:
  :maxdepth: 1

  test_functions
  test_functions_w_positional_and_keyword_arguments<test_functions_w_positional_and_keyword>

----
