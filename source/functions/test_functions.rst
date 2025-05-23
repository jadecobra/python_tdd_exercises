.. include:: ../links.rst

#################################################################################
test_functions
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----


*********************************************************************************
test_functions_w_pass
*********************************************************************************

red: make it fail
---------------------------------------------------------------------------------

* I open a terminal to run :ref:`makePythonTdd.sh` with ``functions`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh functions

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 functions

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_functions.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_functions.py:7`` to open it in the editor
* then change ``True`` to ``False``
* and change ``test_failure``

.. code-block:: python

  import unittest
  import functions


  class TestFunctions(unittest.TestCase):

      def test_functions_w_pass(self):
          self.assertIsNone(functions.function_w_pass())

the terminal shows :ref:`ModuleNotFoundError` , and I add it to the list of Exceptions_ encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError

green: make it pass
---------------------------------------------------------------------------------

* I make a file called ``functions.py`` in the project folder and the terminal shows :ref:`AttributeError`\ , which I add to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* I add a :ref:`function<functions>` definition to ``functions.py``

  .. code-block:: python

    def function_w_pass():
        pass

  and we have a passing test

  * the test checks if the value of the call to ``functions.function_w_pass`` is :ref:`None`
  * the :ref:`function<functions>` definition simply says `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ yet the test passes
  * `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a placeholder keyword which allows the :ref:`function<functions>` definition to follow Python syntax rules
  * the test passes because in Python all :ref:`functions` return :ref:`None` by default, like the :ref:`function<functions>` has an invisible line that says ``return None``

----

*********************************************************************************
test_functions_w_return
*********************************************************************************

red: make it fail
---------------------------------------------------------------------------------

I add a new failing test to ``TestFunctions`` in ``test_functions.py`` to check that :ref:`functions` always return :ref:`None`

.. code-block:: python

    def test_functions_w_return(self):
        self.assertIsNone(functions.function_w_return())

the terminal shows :ref:`AttributeError`

green: make it fail
---------------------------------------------------------------------------------

I add a new :ref:`function<functions>` to ``functions.py`` to make the test pass, this time with a ``return`` statement instead of `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_

.. code-block:: python

    def function_w_return(self):
        return

the terminal shows this test also passes

I defined 2 :ref:`functions` with different statements in their body but they both return the same result, because "in Python all :ref:`functions` return :ref:`None` by default, like the :ref:`function<functions>` has an invisible line that says ``return None``"

*********************************************************************************
test_functions_w_return_none
*********************************************************************************

red: make it fail
---------------------------------------------------------------------------------

I add one more test to the ``TestFunctions`` class in ``test_functions.py`` to help drive home the point

.. code-block:: python

    def test_functions_w_return_none(self):
        self.assertIsNone(
            functions.function_w_return_none()
        )

the terminal shows :ref:`AttributeError`

green: make it pass
---------------------------------------------------------------------------------

from the `Zen of Python`_: ``Explicit is better than implicit.`` I add a :ref:`function<functions>` definition to ``functions.py`` this time with an explicit ``return`` statement showing the value returned

.. code-block:: python

  def function_w_return_none():
      return None

and the terminal shows passing tests.

*********************************************************************************
review
*********************************************************************************

The 3 ways I have defined :ref:`functions` so far have the exact same outcome, they all ``return None``. If ``Explicit is better than implicit.`` then I prefer to use ``return None`` telling anyone who reads the code exactly what the :ref:`function<functions>` returns.

Here is what I know so far from the tests

* :ref:`functions` are defined using the def_ keyword
* :ref:`functions` return :ref:`None` by default

Would you like to :ref:`test singleton functions?<test_singleton_functions>`

----

:doc:`/code/code_functions`