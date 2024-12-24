.. include:: ../links.rst

.. _ModuleNotFoundError:

#################################################################################
ModuleNotFoundError
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/IKb8uyhQPpc?si=XOtc-FDIPLWujM9v" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

.. contents:: table of contents
  :local:
  :depth: 1

----

``ModuleNotFoundError`` is raised when Python cannot find a module from an `import statement`_. A Python :ref:`module<ModuleNotFoundError>` has a filename that ends in ``.py``

*********************************************************************************
test_module_not_found_error
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``module_not_found_error`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh module_not_found_error

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 module_not_found_error

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_module_not_found_error.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_module_not_found_error.py:7`` with the mouse to open it in the editor, then change ``test_failure`` to ``test_module_not_found_error``

  .. code-block:: python

    import unittest


    class TestModuleNotFoundError(unittest.TestCase):

        def test_module_not_found_error(self):
            import src.module_00

  and the terminal shows `ModuleNotFoundError <https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError>`_

  .. code-block:: python

    ModuleNotFoundError: No module called 'src.module_00'

  because Python cannot find ``module_00.py`` in the ``src`` folder

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

green: make it pass
#################################################################################

* then I rename ``module_not_found_error.py`` in the ``src`` folder to ``module_00.py`` and the terminal shows a passing test
* I add another `import statement`_

  .. code-block:: python

    def test_module_not_found_error(self):
        import src.module_00
        import src.module_01

  which gives me `ModuleNotFoundError <https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError>`_

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_01'

* When I make a new file named ``module_01.py`` in the ``src`` folder, the terminal shows a passing test
* I continue with another `import statement`_

  .. code-block:: python

    def test_module_not_found_error(self):
        import src.module_00
        import src.module_01
        import src.module_02

  and get `ModuleNotFoundError <https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError>`_

  .. code-block:: python

    ModuleNotFoundError: No module called 'src.module_02'

* I add ``module_02.py`` to the ``src`` folder, and the terminal shows green again
* One last failing `import statement`_

  .. code-block:: python

    def test_module_not_found_error(self):
        import src.module_00
        import src.module_01
        import src.module_02
        import src.module_03

  and the terminal shows

  .. code-block:: python

    ModuleNotFoundError: No module called 'src.module_03'

* I add the file to the ``src`` folder and the test passes

----

*********************************************************************************
review
*********************************************************************************

I ran a test for the `ModuleNotFoundError <https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError>`_ and Python modules. Would you like to test the :ref:`AssertionError?<AssertionError>`

----

:doc:`/code/code_module_not_found_error`