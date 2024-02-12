.. pumping python documentation master file, created by
  sphinx-quickstart on Sun Oct 22 20:52:14 2023.
  You can adapt this file completely to your liking, but it should at least
  contain the root ``toctree`` directive.

.. include:: /links.rst

#####################################################################
Pumping Python: How to solve problems with Test Driven Development
#####################################################################

I have put together what has worked for me over a decade of learning python and seeing other people use it into this book as exercises using `Test Driven Development <https://en.wikipedia.org/wiki/Test-driven_development>`_.

**********************
Who is this book for?
**********************

* If you are interested in Python, this book is for you
* If you just started your journey, CONGRATULATIONS! You chose Python from the many available `programming languages <https://en.wikipedia.org/wiki/Programming_language>`_, Celebrate it, this book is for you
* If you are new to `Test Driven Development <https://en.wikipedia.org/wiki/Test-driven_development>`_ in Python, this book is for you
* If you use Python but do not know any of the errors below, this book is for you

  - :ref:`AssertionError`
  - :ref:`AttributeError`
  - IndexError_
  - KeyError_
  - :ref:`ModuleNotFoundError`
  - NameError_
  - :ref:`TypeError`
  - ValueError_

**********************
How to use this book
**********************

You can choose how you go through the chapters by starting with what you like.

My recommendation is to

* start with :doc:`How to create a Test Driven Development Environment </how_to/create_tdd_environment>` because it is required by every chapter
* type out the code portions as you go through any chapter without copying and pasting the code
* repeat a chapter you like until you can do it from memory
* try recreating the tests from memory or write new tests for a concept you are working on
* try to write solutions using only the tests from the :ref:`tests and solutions` sections as your guide
* try adding tests for any ideas you get as you go through a chapter
* you can also go through the :ref:`how-tos` section sequentially

If you prefer videos, there is one for each chapter at `<https://www.youtube.com/@JacobItegboje>`_

.. _how-tos:

*******
HOWTOs
*******
.. toctree::
  :maxdepth: 2
  :titlesonly:

  how_to/create_tdd_environment
  how_to/setup_my_ide
  how_to/calculator
  how_to/pass_values
  how_to/create_person
  how_to/exception_handling_tests
  how_to/exception_handling_programs
  how_to/sleep_duration
  learning_models

******************
Table of Contents
******************
.. toctree::
  :maxdepth: 2
  :titlesonly:

  conventions
  exceptions/ModuleNotFoundError
  exceptions/AssertionError
  exceptions/AttributeError
  exceptions/TypeError
  exceptions/IndentationError
  data_structures/none
  data_structures/booleans/booleans
  data_structures/booleans/truth_table/01
  data_structures/booleans/truth_table/02_logical_conjunction
  data_structures/booleans/truth_table/03_logical_disjunction
  data_structures/booleans/truth_table/04_logical_implication
  data_structures/booleans/truth_table/05_logical_equality
  data_structures/booleans/truth_table/06_exclusive_disjunction
  data_structures/booleans/truth_table/07_logical_nand
  data_structures/booleans/truth_table/08_logical_nor
  data_structures/booleans/truth_table/09_converse_non_implication
  data_structures/booleans/truth_table/10_material_non_implication
  data_structures/booleans/truth_table/11_negate
  data_structures/booleans/truth_table/12_project
  data_structures/booleans/truth_table/13_converse_implication
  data_structures/booleans/truth_table/14_true_lies
  data_structures/lists/lists
  data_structures/lists/list_comprehensions
  data_structures/dictionaries
  functions/functions
  functions/functions_passthrough
  functions/functions_positional
  functions/functions_keyword
  functions/functions_positional_and_keyword
  functions/functions_singleton
  classes/classes
  classes/classes_attributes_methods
  classes/classes_initializer

.. _tests-and-solutions:

*********************
tests and solutions
*********************
.. toctree::
  :maxdepth: 2
  :titlesonly:

  code/create_tdd/code_create_tdd_environment
  code/code_calculator
  code/code_pass_values
  code/code_person_factory
  code/code_sleep_duration
  code/code_exception_handling
  code/code_assertion_error
  code/code_attribute_error
  code/code_none
  code/code_booleans
  code/code_truth_table
  code/code_lists
  code/code_list_comprehensions
  code/code_dictionaries
  code/code_classes
  code/code_functions

:ref:`search`
