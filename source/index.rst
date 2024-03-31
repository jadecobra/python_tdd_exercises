.. pumping python documentation master file, made by
  sphinx-quickstart on Sun Oct 22 20:52:14 2023.
  You can adapt this file completely to your liking, but it should at least
  contain the root ``toctree`` directive.

.. include:: /links.rst

#############################################################################
pumping python: how to solve problems with test driven development
#############################################################################

I have put together what has worked for me over a decade of learning python and seeing other people use it into this book as exercises using `Test Driven Development <https://en.wikipedia.org/wiki/Test-driven_development>`_.

*****************************************************************************
who is this book for?
*****************************************************************************

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

*****************************************************************************
how can I use this book?
*****************************************************************************

You can choose how you go through the chapters by starting with what you like.

I suggest you

* start with :doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` because it is required by every chapter
* type out the code portions as you go through any chapter without copying and pasting the code
* repeat a chapter you like until you can do it from memory
* try remaking the tests from memory or write new tests for a concept you are working on
* try to write solutions using only the tests from the :ref:`catalog_of_tests` as your guide
* try adding tests for any ideas you get as you go through a chapter
* you can also go through the :ref:`how-tos` section sequentially
* work consistently at it, what can you sustainably do everyday for the next 10 years?
* do not quit until you get to the end, especially when it is hard, it is part of the experience when learning to solve problems, and there is a lot of failure. If you take it one small step at a time you eventually get there
* if you prefer videos, there is one for each chapter at `<https://www.youtube.com/@JacobItegboje>`_

.. _how-tos:

*****************************************************************************
howtos
*****************************************************************************

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

*****************************************************************************
table of contents
*****************************************************************************

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

----

:ref:`search`
