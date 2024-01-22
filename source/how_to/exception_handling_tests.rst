
########################################
How to test that an Exception is raised
########################################

`Exceptions <https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception>`_ are raised in Python when an error occurs and break execution of the program. When an exception is encountered no further instructions in the program will run.

This is useful because it means there is a problem that should be taken care of for the program to continue as expected.

It is also a pain when it causes the program to exit early. What if I want the program to run regardless of errors? I might want it to give messages to the user who may not care or understand the details that come with Exceptions.

Exception Handling is a way to deal with exceptions, it allows programs to make decisions when an Exception is encountered.

*************************
Prerequisites
*************************

:doc:`Create a Test Driven Development Environment </how_to/create_tdd_environment>` with ``exceptions`` as the project name

----

************************************
How to handle a ModuleNotFoundError
************************************

RED: make it fail
==================

I create a file called ``test_exceptions.py`` in the ``tests`` folder and add the following

.. code-block:: python

  import unittest


  class TestExceptionHandling(unittest.TestCase):

      def test_catching_module_not_found_error_in_tests(self):
          import non_existent_module

the terminal shows a :doc:`/exceptions/ModuleNotFoundError`

.. code-block:: python

  ModuleNotFoundError: No module named 'non_existent_module'

I add it to the list of exceptions encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError

GREEN: make it pass
=====================

I can take care of this error by creating the module, but I want to catch or handle the exception in the test as a way to show that a ``ModuleNotFoundError`` was raised when I try to import ``non_existent_module``

I add a ``self.assertRaises`` to ``test_catching_module_not_found_error_in_tests``

.. code-block:: python

  def test_catching_module_not_found_error_in_tests(self):
      with self.assertRaises(ModuleNotFoundError):
          import non_existent_module

and the terminal shows passing tests. How does all this work?

* I use the `unittest.TestCase.assertRaises <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertRaises>`_ :doc:`method </functions/functions>` which takes a given `Exception <https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception>`_ as its input, in this case :doc:`/exceptions/ModuleNotFoundError` and checks if that error is raised by the statements given in the context below (the indented block after the ``with`` statement)
* ``with`` - creates the context where I test that the exception is raised

  - `read more about the with statement <https://docs.python.org/3/reference/compound_stmts.html?highlight=statement#the-with-statement>`_
  - `read more about with statement context managers <https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers>`_
  - `read PEP 343 - The "with" Statement <https://peps.python.org/pep-0343/>`_

REFACTOR: make it better
=========================

I can use this information to test that a particular exception is raised

************************************
How to handle an AttributeError
************************************

RED: make it fail
==================

* I add a new failing test

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        module.non_existent_attribute

  the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ ::

    NameError: name 'module' is not defined

  A `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ is raised when a name is used within a module with no definition for the name. In the test I call ``module.non_existent_attribute`` but there is no definition for ``module``
* I add it to the list of exceptions encountered ::

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError

* I add an import statement for ``module`` at the top of ``test_exceptions.py`` ::

    import module
    import unittest

  the terminal shows a :doc:`/exceptions/ModuleNotFoundError` ::

    ModuleNotFoundError: No module named 'module'

* I create a file named ``module.py`` in the project folder and the terminal shows an :doc:`/exceptions/AttributeError` because the called attribute ``non_existent_attribute`` does not exist in ``module.py`` ::

    AttributeError: module 'module' has no attribute 'non_existent_attribute'

* I add the exception to the list of exceptions encountered ::

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError

GREEN: make it pass
=====================

I add a ``with self.assertRaises`` context to ``test_catching_attribute_errors_in_tests``

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute

the terminal shows passing tests. I will do it again with :doc:`functions </functions/functions>` for fun

RED: make it fail
==================

I add a failing line that raises an :doc:`/exceptions/AttributeError` to ``test_catching_attribute_errors_in_tests``

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
      module.non_existent_function()

the terminal shows an :doc:`/exceptions/AttributeError` because ``non_existent_function`` does not exist in ``module.py``

.. code-block:: python

  AttributeError: module 'module' has no attribute 'non_existent_function'

GREEN: make it pass
====================

I add an ``assertRaises`` context and indent the failing line to place it within the context to make the test pass

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
      with self.assertRaises(AttributeError):
          module.non_existent_function()

RED: make it fail
==================

I add a failing line that raises an :doc:`/exceptions/AttributeError` for :doc:`classes </classes/classes>` to ``test_catching_attribute_errors_in_tests``

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
      with self.assertRaises(AttributeError):
          module.non_existent_function()
      module.NonExistentClass()

the terminal shows an :doc:`/exceptions/AttributeError`

.. code-block:: python

  AttributeError: module 'module' has no attribute 'NonExistentClass'

GREEN: make it pass
====================

I put the failing line in an ``assertRaises`` context to make the test pass

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
      with self.assertRaises(AttributeError):
          module.non_existent_function()
      with self.assertRaises(AttributeError):
          module.NonExistentClass()

REFACTOR: make it better
==========================

I just created the same context 3 times. The ``self.assertRaises`` catches an :doc:`/exceptions/AttributeError` in each case. I only need to state it once and place all the lines that can raise the same error underneath it to remove the repetition

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
          module.non_existent_function()
          module.NonExistentClass()

Fantastic! all the tests still pass and I have a way to catch exceptions that are raised in programs I am testing. I also encountered the following exceptions

* :doc:`/exceptions/AssertionError`
* :doc:`/exceptions/ModuleNotFoundError`
* `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_
* :doc:`/exceptions/AttributeError`

Time to look at :doc:`/how_to/exception_handling_programs`

----

:doc:`/code/code_exception_handling`