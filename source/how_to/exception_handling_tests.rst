
How to test that an Exception is raised
========================================

`Exceptions <https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception>`_ are raised in Python when an error occurs and break execution of the program. When an exception is encountered no further instructions in the program will run.

This is useful because it means there is some violation that should be taken care of for the program to continue as expected.

It is also a pain when it causes the program to exit prematurely. What if I want the program to run regardless of errors? I might want it to give messages to the user who may not care or understand the details that come with Exceptions

Enter Exception Handling, a way to deal with exceptions, allowing programs to make decisions when an Exception is encountered. Enough words, time to write some code.

Prerequisites
^^^^^^^^^^^^^

:doc:`How to create a Test Driven Development Environment </how_to/create_tdd_environment>`

----

RED: make it fail
^^^^^^^^^^^^^^^^^

I create a file called ``test_exception_handling.py`` in the ``tests`` folder and add the following

.. code-block:: python

  import unittest
  import module


  class TestExceptionHandling(unittest.TestCase):

      def test_catching_module_not_found_error_in_tests(self):
          import non_existent_module

the terminal shows a :doc:`/exceptions/ModuleNotFoundError` and I add it to the list of exceptions encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I could take care of this error by creating the module, but in this case I want to catch or handle the exception in the test as a way to prove that a ``ModuleNotFoundError`` was raised when I refer to ``non_existent_module``

I add a ``self.assertRaises`` to ``test_catching_module_not_found_error_in_tests``

.. code-block:: python

  def test_catching_module_not_found_error_in_tests(self):
      with self.assertRaises(ModuleNotFoundError):
          import non_existent_module

and the terminal shows passing tests. How does all this work?


* I use the `self.assertRaises <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertRaises>`_ :doc:`method </functions/functions>` from the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ class which takes a given `Exception <https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception>`_ as its input, in this case :doc:`/exceptions/ModuleNotFoundError` and checks if that error is raised by the statements given in the context below (the indented block after the ``with`` statement)
* ``with`` - creates the context where I test that the exception is raised

  - `read more about the with statement <https://docs.python.org/3/reference/compound_stmts.html?highlight=statement#the-with-statement>`_
  - `read more about with statement context managers <https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers>`_
  - `read PEP 343 - The "with" Statement <https://peps.python.org/pep-0343/>`_


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

I can use this information to test that a particular exception is raised

* RED: make it fail

  I add a new test to ``TestExceptionHandling`` in ``test_exception_handling.py``

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        module.non_existent_attribute

  the terminal shows an :doc:`/exceptions/AttributeError` because the called attribute ``non_existent_attribute`` does not exist in ``module.py``

  .. code-block:: python

    E    AttributeError: module 'module' has no attribute 'non_existent_attribute'

  I add the exception to the running list or exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* GREEN: make it pass

  I add a ``self.assertRaises`` to ``test_catching_attribute_errors_in_tests``

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute

  the terminal shows passing tests. I will do it again with :doc:`methods </functions/functions>` for good measure

* RED: make it fail

  I add a failing line to ``test_catching_attribute_errors_in_tests``

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        module.non_existent_function()

  the terminal shows :doc:`/exceptions/AttributeError` because ``non_existent_function`` does not exist in ``module.py``

  .. code-block:: python

    E    AttributeError: module 'module' has no attribute 'non_existent_function'

* GREEN: make it pass

  I add ``self.assertRaises`` and indent the failing line to place it within the context

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()

  the terminal shows passing tests

* RED: make it fail

  I add another failing line to ``test_catching_attribute_errors_in_tests``, this time for :doc:`classes </classes/classes>`

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()
        module.NonExistentClass()

  the terminal shows an :doc:`/exceptions/AttributeError`

  .. code-block:: python

    E    AttributeError: module 'module' has no attribute 'NonExistentClass'

* GREEN: make it pass

  I add ``self.assertRaises`` to make it pass

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()
        with self.assertRaises(AttributeError):
            module.NonExistentClass()

  the terminal displays passing tests

* RED: make it fail

  I add a new failing line to test for a class attribute in ``test_catching_attribute_errors_in_tests``

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()
        with self.assertRaises(AttributeError):
            module.NonExistentClass()
        module.Class.non_existent_attribute

  the terminal shows an :doc:`/exceptions/AttributeError`

  .. code-block:: python

    E    AttributeError: type object 'Class' has no attribute 'non_existent_attribute'

* GREEN: make it pass

  I add ``self.assertRaises`` to catch the error

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()
        with self.assertRaises(AttributeError):
            module.NonExistentClass()
        with self.assertRaises(AttributeError):
            module.Class.non_existent_attribute

  the terminal shows passing tests

* RED: make it fail

  I trigger another attribute error, by adding a line to ``test_catching_attribute_errors_in_tests``

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()
        with self.assertRaises(AttributeError):
            module.NonExistentClass()
        with self.assertRaises(AttributeError):
            module.Class.non_existent_attribute
        module.Class.non_existent_method()

  the terminal shows another :doc:`/exceptions/AttributeError`

  .. code-block:: python

    E    AttributeError: type object 'Class' has no attribute 'non_existent_method'

* GREEN: make it pass

  I add ``self.assertRaises`` to make it pass

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()
        with self.assertRaises(AttributeError):
            module.NonExistentClass()
        with self.assertRaises(AttributeError):
            module.Class.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.Class.non_existent_method()

  the terminal shows passing tests

* REFACTOR: make it better

  I just created the same context 5 times, this is a good candidate for a rewrite. The ``self.assertRaises`` catches an :doc:`/exceptions/AttributeError` in each case, I only need to state it once and place all the lines that can raise the same error underneath it.

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
            module.non_existent_function()
            module.NonExistentClass()
            module.Class.non_existent_attribute
            module.Class.non_existent_method()

  Fantastic! all the tests still pass

:doc:`/code/code_exception_handling`