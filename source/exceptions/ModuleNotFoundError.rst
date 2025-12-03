.. meta::
  :description: Struggling with Python's ModuleNotFoundError? Learn to fix import errors from other `folders (directories)`_& get your code running. Watch the full tutorial to solve it now!
  :keywords: Jacob Itegboje, python ModuleNotFoundError no module named, how to fix ModuleNotFoundError in vscode, python import error from another folder, python relative import not working, ModuleNotFoundError: No module named 'src', python can't find module in same directory, pythonpath vscode setup, fix python import errors

.. include:: ../links.rst

.. _ModuleNotFoundError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError

#################################################################################
ModuleNotFoundError
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/IKb8uyhQPpc?si=XOtc-FDIPLWujM9v" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

ModuleNotFoundError_ is raised when Python_ cannot find a module_ that is given in an `import statement`_. A Python_ module_ is a file that ends in ``.py``. Any folder_ that contains an ``__init__.py`` is also a Python_ module_

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``module_not_found_error`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh module_not_found_error

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: python

      ./makePythonTdd.ps1 module_not_found_error

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_module_not_found_error.py:7: AssertionError

* I hold ``ctrl`` (Windows/Linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_module_not_found_error.py:7`` to open it in the :ref:`editor<2 editors>`,
* then I change ``True`` to ``False`` to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestModuleNotFoundError(unittest.TestCase):

*********************************************************************************
test_module_not_found_error
*********************************************************************************

RED: make it fail
#################################################################################

* I change ``test_failure`` to ``test_module_not_found_error``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    import unittest


    class TestModuleNotFoundError(unittest.TestCase):

        def test_module_not_found_error(self):
            import src.module_00

  the terminal_ shows ModuleNotFoundError_

  .. code-block:: shell

    ModuleNotFoundError: No module called 'src.module_00'

  because Python_ cannot find ``module_00.py`` in the ``src`` folder

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

GREEN: make it pass
#################################################################################

I change ``module_not_found_error.py`` in the ``src`` folder to ``module_00.py`` and the test passes

REFACTOR: make it better
#################################################################################
* I add another `import statement`_ to ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

        def test_module_not_found_error(self):
            import src.module_00
            import src.module_01

  the terminal_ shows ModuleNotFoundError_

  .. code-block:: shell

    ModuleNotFoundError: No module named 'src.module_01'

  I make a new file named ``module_01.py`` in the ``src`` folder and the test passes

* I close the file

* I continue with another `import statement`_ in ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_module_not_found_error(self):
            import src.module_00
            import src.module_01
            import src.module_02

  the terminal_ shows ModuleNotFoundError_

  .. code-block:: shell

    ModuleNotFoundError: No module called 'src.module_02'

  I add ``module_02.py`` to the ``src`` folder and the terminal_ shows green again

* I close the file

* I add one last failing `import statement`_ for practice in ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5

        def test_module_not_found_error(self):
            import src.module_00
            import src.module_01
            import src.module_02
            import src.module_03

  the terminal_ shows

  .. code-block:: shell

    ModuleNotFoundError: No module called 'src.module_03'

* I add the file to the ``src`` folder_ and the test passes

* I close the file

----

*********************************************************************************
review
*********************************************************************************

I ran a test for ModuleNotFoundError_ to practice making Python_ modules_. Would you like to :ref:`test AttributeError?<AttributeError>`

----

:ref:`Click Here for the code I wrote in this chapter<ModuleNotFoundError: test>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->