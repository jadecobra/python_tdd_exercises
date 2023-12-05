.. pumping python documentation master file, created by
  sphinx-quickstart on Sun Oct 22 20:52:14 2023.
  You can adapt this file completely to your liking, but it should at least
  contain the root ``toctree`` directive.

Welcome to pumping python
==========================
This book is a collection of exercises to get you writing python code immediately using Test Driven Development.

It is a culmination of what has worked for me over the past 10 years learning the language and observing other people use it.

Who is this book for?
---------------------
* If you are just starting your journey, congratulations! You made a decision from the many choices of programming languages available. Celebrate it. This book is for you
* If you are new to Test Driven Development in python, this book is for you
* If you already use python but are unfamiliar with any of the errors below, this book is for you

  - :doc:`/exceptions/ModuleNotFoundError`
  - :doc:`/exceptions/AssertionError`
  - :doc:`/exceptions/AttributeError`
  - :doc:`/exceptions/TypeError`

It will show you how to trigger errors and resolve them, there are also a few drills that will get you used to certain concepts

How to use this book
--------------------

You can choose how you go through the chapters by starting with any you like or that looks like it could solve your current problem.

Here is how I recommend you use the book

* start with  :doc:`How to Setup a Test Driven Development Environment </how_to/setup_tdd_environment>` because it is required by every other chapter
* type out the code portions as you go through each chapter - do not copy and paste
* repeat a chapter you like until you can do it from memory
* try recreating the tests from memory or write new tests for a concept you are learning
* try writing the solutions for the tests in chapters like the ``HOW TOs``
* try adding tests for any ideas you get as you go through a chapter

Table of Contents
-----------------
.. toctree::
  :maxdepth: 2
  :titlesonly:

  exceptions/AssertionError
  exceptions/ModuleNotFoundError
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
  data_structures/data_structures_none
  data_structures/data_structures_booleans
  data_structures/data_structures_lists
  data_structures/list_comprehensions
  data_structures/data_structures_dictionaries
  truth_table/truth_table_01
  truth_table/truth_table_02_logical_conjunction
  truth_table/truth_table_03_logical_disjunction
  truth_table/truth_table_04_logical_implication
  truth_table/truth_table_05_logical_equality
  truth_table/truth_table_06_exclusive_disjunction
  truth_table/truth_table_07_logical_nand
  truth_table/truth_table_08_logical_nor
  truth_table/truth_table_09_converse_non_implication
  truth_table/truth_table_10_material_non_implication
  truth_table/truth_table_11_negate
  truth_table/truth_table_12_project
  truth_table/truth_table_13_converse_implication
  truth_table/truth_table_14_true_lies

HOW TOs
--------
.. toctree::
  :maxdepth: 2
  :titlesonly:

  how_to/setup_tdd_environment
  how_to/setup_my_ide
  how_to/calculator
  how_to/passing_values
  how_to/person_factory
  how_to/sleep_duration
  how_to/exception_handling_tests
  how_to/exception_handling_programs
  learning_models

code
----
.. toctree::
  :maxdepth: 2
  :titlesonly:

  code/code_setup_tdd_environment
  code/code_assertion_error
  code/code_attribute_error
  code/code_calculator
  code/code_classes
  code/code_dictionaries
  code/code_exception_handling
  code/code_functions
  code/code_passing_values
  code/code_person_factory
  code/code_sleep_duration
  code/code_truth_table


:ref:`search`
