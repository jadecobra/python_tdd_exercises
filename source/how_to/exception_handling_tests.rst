.. include:: ../links.rst

#################################################################################
how to test that an Exception is raised
#################################################################################

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/xAgoCiCZIt0?si=CKmBIYAZU71gk45I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

.. contents:: table of contents
  :local:
  :depth: 1

----

Exceptions_ are raised in Python when an error occurs and break execution of the program. When an exception is encountered no further instructions in the program will run.

This is useful because it means there is a problem that should be taken care of for the program to continue as expected.

It is also a pain when it causes the program to exit early. What if I want the program to run regardless of errors? I might want it to give messages to the user who may not care or understand the details that come with Exceptions_.

Exception Handling is a way to deal with Exceptions_, it allows programs to make decisions when an Exception is encountered.

.. _test_catching_module_not_found_error_in_tests:

*********************************************************************************
test_catching_module_not_found_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal and run :ref:`makePythonTdd.sh` with ``exceptions`` as the project name

  .. code-block:: python

    ./makePythonTdd.sh exceptions

  .. NOTE::

    If you are using Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 exceptions

  and it shows an :ref:`AssertionError` after making the files I need

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_exceptions.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_exceptions.py:7`` with the mouse to open it
* and change ``True`` to ``False`` to make ``test_failure`` pass
* then change ``test_failure`` to ``test_catching_module_not_found_error_in_tests``

  .. code-block:: python

    class TestException(unittest.TestCase):

        def test_catching_module_not_found_error_in_tests(self):
            import non_existent_module

  the terminal shows a :ref:`ModuleNotFoundError`

  .. code-block:: python

    ModuleNotFoundError: No module named 'non_existent_module'

green: make it pass
#################################################################################

* I add it to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

* I can take care of this error by making the module, but I want to catch or handle the exception in the test as a way to show that a ``ModuleNotFoundError`` was raised when I try to import ``non_existent_module``
* I add a ``self.assertRaises`` to ``test_catching_module_not_found_error_in_tests``

  .. code-block:: python

    def test_catching_module_not_found_error_in_tests(self):
        with self.assertRaises(ModuleNotFoundError):
            import non_existent_module

  and the terminal shows passing tests. How does all this work?

  - I use the `unittest.TestCase.assertRaises`_ :ref:`method<functions>` which takes a given `Exception <https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception>`_ as its input, in this case :ref:`ModuleNotFoundError` and checks if that error is raised by the statements given in the context below (the indented block after the ``with`` statement)
  - ``with`` - makes the context where I test that the exception is raised

    * `read more about the with statement <https://docs.python.org/3/reference/compound_stmts.html?highlight=statement#the-with-statement>`_
    * `read more about with statement context managers <https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers>`_
    * `read PEP 343 - The "with" Statement <https://peps.python.org/pep-0343/>`_

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

  A NameError_ is raised when a name is used within a :ref:`module<ModuleNotFoundError>` with no definition for the name. I call ``module.non_existent_attribute`` in the test and there is no definition for ``module``
* I add it to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError

* I add an `import statement`_ for ``module`` at the top of ``test_exceptions.py``

  .. code-block:: python

    import module
    import unittest

  the terminal shows a :ref:`ModuleNotFoundError`

  .. code-block:: python

    ModuleNotFoundError: No module named 'module'

* I make a file named ``module.py`` in the project folder and the terminal shows an :ref:`AttributeError` because the called attribute ``non_existent_attribute`` does not exist in ``module.py`` ::

    AttributeError: module 'module' has no attribute 'non_existent_attribute'

* I add the exception to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError

green: make it pass
#################################################################################

I add a ``with self.assertRaises`` context to ``test_catching_attribute_errors_in_tests``

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute

the terminal shows passing tests

refactor: make it better
#################################################################################

red: make it fail
---------------------------------------------------------------------------------

I do it again with :ref:`functions<functions>` for fun by adding a failing line that raises an :ref:`AttributeError` to ``test_catching_attribute_errors_in_tests``

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
      module.non_existent_function()

the terminal shows an :ref:`AttributeError` because ``non_existent_function`` does not exist in ``module.py``

.. code-block:: python

  AttributeError: module 'module' has no attribute 'non_existent_function'

green: make it pass
---------------------------------------------------------------------------------

I add an ``assertRaises`` context and indent the failing line to place it within the context to make the test pass

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
      with self.assertRaises(AttributeError):
          module.non_existent_function()

red: make it fail
---------------------------------------------------------------------------------

I add a failing line that raises an :ref:`AttributeError` for :doc:`classes </classes/classes>` to ``test_catching_attribute_errors_in_tests``

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

I put the failing line in an ``assertRaises`` context to make the test pass

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

I just made the same context 3 times. The ``self.assertRaises`` catches an :ref:`AttributeError` in each case. I only need to state it once and place all the lines that can raise the same error underneath it to remove the repetition

.. code-block:: python

  def test_catching_attribute_errors_in_tests(self):
      with self.assertRaises(AttributeError):
          module.non_existent_attribute
          module.non_existent_function()
          module.NonExistentClass()

Fantastic! all the tests still pass and I have a way to catch exceptions that are raised in programs I am testing. I also encountered the following exceptions

* :ref:`AssertionError`
* :ref:`ModuleNotFoundError`
* NameError_
* :ref:`AttributeError`

Would you like to look at :doc:`/how_to/exception_handling_programs`?

----

:doc:`/code/code_exception_handling`