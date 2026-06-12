.. meta::
  :description: Beginner tutorial on Python booleans: True and False as the two boolean values. Learn boolean operators (and, or, not), truthiness and falsiness (why 0, '', [], {}, None are falsy but not the same as False), and how booleans control if statements and program flow. Builds directly on the AssertionError TDD chapters that tested True/False identity with `is True` / `is not True`, `is False`, assertIs / assertIsNot, and the key lesson that 0 is not False, empty containers are not False, etc. even though they are falsy. Covers common beginner mistakes confusing truthiness with boolean identity or equality. Includes the full context from the red-green-refactor tests for None/True/False singletons.
  :keywords: Jacob Itegboje, Pumping Python, python booleans, what are booleans python, python True False, boolean operators python and or not, python truthiness, python falsiness, python if boolean, 0 is not False python, empty list is not False, None is not False, is True vs == True, python boolean identity, assertIs True, testing booleans unittest, python TDD booleans, boolean vs truthy, common python boolean mistakes, booleans in data structures, python True False tutorial beginners, bool() python, truth table python, python boolean best practices, falsy values are not False

.. include:: ../../links.rst

.. _True: https://docs.python.org/3/library/constants.html?highlight=true#True
.. _False: https://docs.python.org/3/library/constants.html?highlight=true#False

#################################################################################
what are booleans?
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/6r3QcYN0wxQ?si=cQaK63rwX3f9PGX6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

Imagine we have to divide everything into two and the options are things that are True_ and things that are False_. These are the booleans_: True_ and False_.

I used :ref:`assertIs<another way to test if something is the same object as True>` and :ref:`assertIsNot<another way to test if something is NOT the same object as True>` in :ref:`test_assertion_error_w_false` and :ref:`test_assertion_error_w_true` in :ref:`AssertionError<what causes AssertionError?>`, where I saw that

* True_ is NOT :ref:`None<what is None?>` and NOT equal to :ref:`None<what is None?>`
* :ref:False_ is NOT :ref:`None<what is None?>` and NOT equal to :ref:`None<what is None?>`
* :ref:`None is None<what is None?>` and equal to :ref:`None<what is None?>`

I test :ref:`booleans<what are booleans?>` in the chapters below

.. toctree::
  :titlesonly:
  :maxdepth: 1

  booleans_1
  ../../truth_table/index
  booleans_2
  booleans_3
  booleans_4

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`test booleans<booleans: only two>`
