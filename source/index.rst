.. pumping python documentation master file, made by
  sphinx-quickstart on Sun Oct 22 20:52:14 2023.
  You can adapt this file completely to your liking, but it should at least
  contain the root ``toctree`` directive.

.. include:: /links.rst

#################################################################################
pumping python: how I solve problems with test driven development
#################################################################################


My name is Jacob Itegboje and I have been a Python Programmer in roles as a Developer, Platform Engineer, DevOps Engineer and Solutions Architect. This is a collection of `Test Driven Development`_ exercises that helped me understand and use the language for over a decade.
`Test Driven Development`_ is a way to write software with a focus on tests. I write tests for ideas to reach a goal or meet a requirement, and the results tell me if I am closer or further away from the goal. The process is repeated until I get to the goal.

I recommend reading `Kent Beck’s <https://en.wikipedia.org/wiki/Kent_Beck>`_ `Test Driven Development by Example`_ and `Martin Fowler’s <https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer)>`_ `Refactoring`_, they both influenced the way I write programs.

*********************************************************************************
who is this book for?
*********************************************************************************

* If you are interested in Python, this book is for you
* If you just started your journey, CONGRATULATIONS! You chose Python from the many available `programming languages <https://en.wikipedia.org/wiki/Programming_language>`_, Celebrate it, this book is for you
* If you are new to `Test Driven Development`_ in Python, this book is for you
* If you use Python but do not know any of the :ref:`Exceptions` below, this book is for you

  - :ref:`AssertionError`
  - :ref:`AttributeError`
  - IndexError_
  - KeyError_
  - :ref:`ModuleNotFoundError`
  - NameError_
  - :ref:`TypeError`
  - ValueError_

*********************************************************************************
how can I use this book?
*********************************************************************************

Start with :doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` because it is required by every chapter,  then you can choose how you go through the chapters based on what you like, or you could go through the :ref:`how-tos` section in order

My recommendations are that you

* type out the code portions as you go through a chapter without copying and pasting the code
* repeat a chapter you like until you can do it from memory
* at the end of a chapter, delete the tests then try to write them from memory or use the solution as a guide
* at the end of a chapter, close the tests, then delete the solution and try to write a solution with the terminal response as your guide
* try to write solutions using only the tests from the :ref:`catalog_of_tests` as your guide
* try adding tests for any ideas you get as you go through a chapter, the sooner you start writing tests the better you will get at doing it since it requires a little bit of a shift in thinking
* do not quit until you get to the end of a chapter, especially when it gets hard, it is part of the experience when learning to solve problems, because there is a lot of failure. You can always walk away from the chapter to do something that is not related for a while, then come back to it. If you take one small step at a time you eventually get where you want to go

If you like videos, there is one for each chapter at `<https://www.youtube.com/@JacobItegboje>`_

.. _how-tos:

*********************************************************************************
howtos
*********************************************************************************

.. toctree::
  :maxdepth: 1
  :titlesonly:

  how_to/make_tdd_environment
  how_to/setup_my_ide
  how_to/calculator
  how_to/pass_values
  how_to/make_person
  how_to/exception_handling_tests
  how_to/exception_handling_programs
  how_to/sleep_duration

*********************************************************************************
table of contents
*********************************************************************************

.. toctree::
  :maxdepth: 1
  :titlesonly:

  conventions
  exceptions/exceptions
  data_structures/data_structures
  functions/functions
  classes/classes
  tests<catalog_of_tests>
  solutions<catalog_of_solutions>
  learning_models
  dot_notation
  review

----

:ref:`search`
