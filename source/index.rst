.. pumping python documentation master file, created by
  sphinx-quickstart on Sun Oct 22 20:52:14 2023.
  You can adapt this file completely to your liking, but it should at least
  contain the root ``toctree`` directive.

#####################################################################
Pumping Python: How to use Test Driven Development to solve problems
#####################################################################

This book is a collection of exercises to get you writing programs with python using `Test Driven Development <https://en.wikipedia.org/wiki/Test-driven_development>`_.

I have put together what has worked for me over the past 10 years of learning the language and watching how other people use it.

**********************
Who is this book for?
**********************

* are you just starting your journey? congratulations! You made a decision from the many choices of programming languages available. Celebrate it. This book is for you
* are you new to Test Driven Development in Python? This book is for you
* do you use Python but are unfamiliar with any of the errors below? This book is for you

  - :doc:`/exceptions/AssertionError`
  - :doc:`/exceptions/AttributeError`
  - `IndexError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#IndexError>`_
  - `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_
  - :doc:`/exceptions/ModuleNotFoundError`
  - `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_
  - :doc:`/exceptions/TypeError`
  - `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_

It will show you how to cause errors and use them, there are also a few drills

**********************
How to use this book
**********************

You can choose how you go through the chapters by starting with what like or looks interesting.

Here is how I recommend you use the book

* start with  :doc:`How to create a Test Driven Development Environment </how_to/create_tdd_environment>` because it is required by every other chapter
* type out the code portions as you go through each chapter - do not copy and paste
* repeat a chapter you like until you can do it from memory
* try recreating the tests from memory or write new tests for a concept you are learning
* try writing the solutions for the tests in chapters like the ``HOWTOs``
* try adding tests for any ideas you get as you go through a chapter

*******
HOWTOs
*******
.. toctree::
  :maxdepth: 2
  :titlesonly:

  how_to/setup_my_ide
  how_to/create_tdd_environment
  how_to/calculator
  how_to/passing_values
  how_to/person_factory
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

  exceptions/ModuleNotFoundError
  exceptions/AssertionError
  exceptions/AttributeError
  exceptions/TypeError
  exceptions/IndentationError
  how_to/exception_handling_tests
  how_to/exception_handling_programs
  conventions
  classes/classes
  classes/classes_attributes_methods
  classes/classes_initializer
  functions/functions
  functions/functions_passthrough
  functions/functions_positional
  functions/functions_keyword
  functions/functions_positional_and_keyword
  functions/functions_singleton
  data_structures/none
  data_structures/booleans
  data_structures/lists
  data_structures/list_comprehensions
  data_structures/dictionaries
  truth_table/01
  truth_table/02_logical_conjunction
  truth_table/03_logical_disjunction
  truth_table/04_logical_implication
  truth_table/05_logical_equality
  truth_table/06_exclusive_disjunction
  truth_table/07_logical_nand
  truth_table/08_logical_nor
  truth_table/09_converse_non_implication
  truth_table/10_material_non_implication
  truth_table/11_negate
  truth_table/12_project
  truth_table/13_converse_implication
  truth_table/14_true_lies

*********************
tests and solutions
*********************
.. toctree::
  :maxdepth: 2
  :titlesonly:

  code/code_create_tdd_environment
  code/code_assertion_error
  code/code_attribute_error
  code/code_none
  code/code_booleans
  code/code_lists
  code/code_list_comprehensions
  code/code_dictionaries
  code/code_functions
  code/code_classes
  code/code_truth_table
  code/code_exception_handling
  code/code_calculator
  code/code_passing_values
  code/code_person_factory
  code/code_sleep_duration

:ref:`search`
