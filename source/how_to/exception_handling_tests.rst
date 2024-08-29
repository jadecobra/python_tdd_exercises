.. include:: ../links.rst

#################################################################################
how to test that an Exception is raised
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/xAgoCiCZIt0?si=CKmBIYAZU71gk45I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

.. contents:: table of contents
  :local:
  :depth: 1

----

`Exceptions <https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception>`_ are raised in Python when an error occurs and break execution of the program. When an exception is encountered no further instructions in the program will run.

This is useful because it means there is a problem that should be taken care of for the program to continue as expected.

It is also a pain when it causes the program to exit early. What if I want the program to run regardless of errors? I might want it to give messages to the user who may not care or understand the details that come with `Exceptions <https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception>`_.

Exception Handling is a way to deal with `Exceptions <https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception>`_, it allows programs to make decisions when an Exception is encountered.

.. _test_catching_module_not_found_error_in_tests:

*********************************************************************************
test_catching_module_not_found_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``exceptions`` as the project name

  .. code-block:: python

    ./makePythonTdd.sh exceptions

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 exceptions

  and it shows an :ref:`AssertionError` after making the folders and files for the project

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_exceptions.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_exceptions.py:7`` with the mouse to open it
* then change ``True`` to ``False`` to make ``test_failure`` pass
* and change ``test_failure`` to ``test_catching_module_not_found_error_in_tests``

  .. code-block:: python

    class TestException(unittest.TestCase):

        def test_catching_module_not_found_error_in_tests(self):
            import non_existent_module

  the terminal shows a :ref:`ModuleNotFoundError`

  .. code-block:: python

    ModuleNotFoundError: No module named 'non_existent_module'

green: make it pass
#################################################################################

* I add it to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

* I can take care of this error by making the module, but I want to catch or handle the exception in the test
* I add the `unittest.TestCase.assertRaises`_ :ref:`method<functions>` to make sure that a :ref:`ModuleNotFoundError` is raised when I try to import ``non_existent_module``

  .. code-block:: python

    def test_catching_module_not_found_error_in_tests(self):
        with self.assertRaises(ModuleNotFoundError):
            import non_existent_module

  and the terminal shows passing tests

----

.. _test_catching_attribute_errors_in_tests:

*********************************************************************************
test_catching_attribute_errors_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add a new failing test

  .. code-block:: python

    def test_catching_attribute_errors_in_tests(self):
        module.non_existent_attribute

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'module' is not defined

* I add it to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError

* I add an `import statement`_

  .. code-block:: python

    import module
    import unittest

  the terminal shows a :ref:`ModuleNotFoundError`

  .. code-block:: python

    ModuleNotFoundError: No module named 'module'

* I make a file named ``module.py`` in the project folder and the terminal shows an :ref:`AttributeError` because ``non_existent_attribute`` does not exist in ``module.py`` ::

    AttributeError: module 'module' has no attribute 'non_existent_attribute'

* I add the exception to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError

green: make it pass
#################################################################################

I add a call to the `unittest.TestCase.assertRaises`_ :ref:`method<functions>`

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute

the terminal shows passing tests

refactor: make it better
#################################################################################

red: make it fail
---------------------------------------------------------------------------------

For fun I do it again with a :ref:`function<functions>` that does not exist

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
      module.non_existent_function()

the terminal shows an :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'module' has no attribute 'non_existent_function'

green: make it pass
---------------------------------------------------------------------------------

I add an `unittest.TestCase.assertRaises`_ :ref:`method<functions>` and indent the failing line to place it within the context to make the test pass

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
      with self.assertRaises(AttributeError):
          module.non_existent_function()

red: make it fail
---------------------------------------------------------------------------------

I add a failing line that raises an :ref:`AttributeError` for :ref:`classes` to ``test_catching_attribute_errors_in_tests``

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
      with self.assertRaises(AttributeError):
          module.non_existent_function()
      module.NonExistentClass()

the terminal shows an :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'module' has no attribute 'NonExistentClass'

green: make it pass
---------------------------------------------------------------------------------

I place the failing line in a `unittest.TestCase.assertRaises`_ context to make the test pass

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
      with self.assertRaises(AttributeError):
          module.non_existent_function()
      with self.assertRaises(AttributeError):
          module.NonExistentClass()

refactor: make it better
---------------------------------------------------------------------------------

I just made the same context 3 times. The `unittest.TestCase.assertRaises`_ :ref:`method<functions>` catches an :ref:`AttributeError` in each case. I only need to state it once and place all the lines that can raise the same error underneath it to remove the repetition

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
          module.non_existent_function()
          module.NonExistentClass()

Fantastic! all the tests still pass and I have a way to catch exceptions that are raised in programs I am testing. I also encountered the following :ref:`Exceptions<Exceptions>`

* :ref:`AssertionError`
* :ref:`ModuleNotFoundError`
* NameError_
* :ref:`AttributeError`

Would you like to look at :doc:`/how_to/exception_handling_programs`?

----

:doc:`/code/code_exception_handling`