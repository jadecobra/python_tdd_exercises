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

*********************************************************************************
what causes ModuleNotFoundError?
*********************************************************************************

ModuleNotFoundError_ is raised when Python_ cannot find a module_ that is given in an `import statement`_. A Python_ module_ is a file that ends in ``.py``. Any folder_ that contains an ``__init__.py`` is also a Python_ module_

----

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: ../code/tests/test_module_not_found_error.py
  :language: python
  :linenos:

----

*********************************************************************************
start the project
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``module_not_found_error`` as the name of the project

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh module_not_found_error

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: shell

      ./makePythonTdd.ps1 module_not_found_error

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_module_not_found_error.py:7: AssertionError

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option` or :kbd:`command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_module_not_found_error.py:7`` to open it in the :ref:`editor<2 editors>`
  
* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

* I change the name of the :ref:`class<what is a class?>` to match the :ref:`CapWords format<CapWords>` to follow :ref:`Python convention<conventions>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestModuleNotFoundError(unittest.TestCase):

*********************************************************************************
test_module_not_found_error
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

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

* I add the error to the list of :ref:`Exceptions<errors>` seen in ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change ``module_not_found_error.py`` in the ``src`` folder to ``module_00.py`` and the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================
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
close the project
*********************************************************************************

* I close the file(s) I have open in the :ref:`editor(s)<2 editors>`
* I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard
* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/module_not_found_error

* I `change directory`_ to the parent of ``module_not_found_error``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I ran a test for ModuleNotFoundError_ to practice making Python_ modules_

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<ModuleNotFoundError: test>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have gone through a lot of information and know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to write functions<what is a function?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<list comprehensions>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`what you can do with dictionaries<dictionaries>`
* :ref:`what you can do with classes<what is a class?>`
* :ref:`how to raise ModuleNotFoundError<ModuleNotFoundError>`

:ref:`Would you like to test AttributeError?<AttributeError>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please leave a 5 star review. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->