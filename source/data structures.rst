Data Structures
===============

Let us take a look at Data Structures in python using Test Driven Development. This chapter covers the null object ``None``

In programming we process input data of some form and output data in some form.
We can think of it as

.. code-block:: python

           input_data -> program -> output_data

you could be familiar with this from mathematics

.. code-block::

                 f(     x    ) -> y
           program(input_data) -> output_data


Prerequisites
-------------


:doc:`Setup a Test Driven Development Environment`

----


What are the data structures in python?
---------------------------------------

.. list-table::
   :header-rows: 1

   * - keyword
     - representation
     - examples
   * - None
     - no value
     - None
   * - bool
     - boolean
     - True / False
   * - int
     - integers
     - positive/negative whole numbers for example,  -1, 0, 1
   * - float
     - floats
     - floating point numbers for example,  -1.1, 0.1, 1.1
   * - str
     - string
     - any text in quotes for example,  "text", """text""", 'text', '''text'''
   * - tuple
     - tuples
     - immutable sequence of values in parentheses for example,  (1, 2.3, "three", (4, 5.6, 'seven'))
   * - list
     - lists/arrays
     - mutable sequence of values in square brackets for example,  [1, 2.3, "three", (4, 5.6, 'seven')]
   * - set
     - sets
     - sequence of values with in curly/squiggly braces with no duplicates for example,  {1, 2, 3}
   * - dict
     - dictionaries/mappings
     - mapping of key/value pairs in curly/squiggly braces for example,  {"a": "apple", "b": "ball", "c": "car", "d": "dog"}


The following chapters go into more detail about some of these data structures


* :doc:`None`
* :doc:`Booleans`
* :doc:`Lists`
* :doc:`data structures: dictionaries`
