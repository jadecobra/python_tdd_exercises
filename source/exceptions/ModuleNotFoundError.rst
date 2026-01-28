.. meta::
  :description: Struggling with Python's ModuleNotFoundError? Learn to fix import errors from other `folders (directories)`_& get your code running. Watch the full tutorial to solve it now!
  :keywords: Jacob Itegboje, python ModuleNotFoundError no module named, how to fix ModuleNotFoundError in vscode, python import error from another folder, python relative import not working, ModuleNotFoundError: No module named 'src', python can't find module in same directory, pythonpath vscode setup, fix python import errors

.. include:: ../links.rst

.. _ModuleNotFoundError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError
.. _sys module: https://docs.python.org/3/library/sys.html#module-sys
.. _sys.path: https://docs.python.org/3/library/sys.html#sys.path

#################################################################################
what is a module?
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/IKb8uyhQPpc?si=XOtc-FDIPLWujM9v" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

A Python_ module_ is a file_ that ends in ``.py``. Any folder_ that contains an ``__init__.py`` is also a Python_ module_

*********************************************************************************
what causes ModuleNotFoundError?
*********************************************************************************

ModuleNotFoundError_ is raised when Python_ cannot find a module_ given in an `import statement`_

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/tests/test_module_not_found_error.py
  :language: python
  :linenos:

----

*********************************************************************************
start the project
*********************************************************************************

* I open a terminal_, it shows

  .. code-block:: shell

    .../pumping_python

  I am in the ``pumping_python`` directory_

  .. NOTE::

    if you are not in the ``pumping_python`` directory_, try

    .. code-block:: python
      :emphasize-lines: 1

      cd ~/pumping_python

    or the path to where you saved ``pumping_python`` to get back to it

* I make 2 new folders_

  .. code-block:: python
    :emphasize-lines: 1

    mkdir src tests

  the terminal_ goes back to the command line

  .. code-block:: python

    .../pumping_python

* I use touch_ to make an empty file_ for the program_ in the ``src`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    touch src/pumping_python.py

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item src/pumping_python.py`` instead of ``touch src/pumping_python.py``

    .. code-block:: Powershell
      :emphasize-lines: 1

      New-Item src/pumping_python.py

  the terminal_ goes back to the command line

  .. code-block:: python

    .../pumping_python/pumping_python

* I use touch_ to make an empty file_ in the ``tests`` folder_ to tell Python_ that it is a `Python package`_

  .. ATTENTION:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. code-block:: python
    :emphasize-lines: 1

    touch tests/__init__.py

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item tests/__init__.py`` instead of ``touch tests/__init__.py``

    .. code-block:: Powershell
      :emphasize-lines: 1

      New-Item tests/__init__.py

  the terminal_ goes back to the command line

* I make an empty file_ for the actual test

  .. code-block:: python
    :emphasize-lines: 1

    touch tests/test_pumping_python.py

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item tests/test_pumping_python.py`` NOT ``touch tests/test_pumping_python.py``

    .. code-block:: Powershell
      :emphasize-lines: 1

      New-Item tests/test_pumping_python.py

  the terminal_ goes back to the command line

* I open ``test_pumping_python.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP:: I can open a file_ from the terminal_ in `Visual Studio Code`_ by typing ``code`` and the name of the file_, for example

    .. code-block:: python
      :emphasize-lines: 1

      code tests/test_pumping_python.py

    ``test_pumping_python.py`` opens up in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_pumping_python.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestPumpingPython(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I make a `virtual environment`_ in the terminal_

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m venv .venv

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``python3 -m venv .venv`` instead of ``python3 -m venv .venv``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      python -m venv .venv

  the terminal_ takes some time then goes back to the command line

* I activate the `virtual environment`_

  .. code-block:: python
    :emphasize-lines: 1

    source .venv/bin/activate

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` NOT ``source .venv/bin/activate``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  the terminal_ shows

  .. code-block:: python

    (.venv) .../pumping_python

* I upgrade the `Python package manager (pip)`_ to the latest version

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m pip install --upgrade pip

  the terminal_ shows pip_ being uninstalled then installs the latest version or shows that it is already the latest version

* I make a ``requirements.txt`` file_ for the `Python programs`_ my project needs

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watch" > requirements.txt

  the terminal_ goes back to the command line

* I use pip_ to install ``pytest-watch`` with the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m pip install --requirement requirements.txt

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``python -m pip install --requirement requirements.txt`` instead of ``python3 -m pip install --requirement requirements.txt``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      python -m pip install --requirement requirements.txt

  the terminal_ shows pip_ downloading then installing the `Python programs`_ that `pytest-watch`_ needs to run

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I use `pytest-watch`_ to run the test

  .. code-block:: python
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows ModuleNotFoundError_ then goes back to the command line

  .. code-block:: shell
    :emphasize-lines: 1
    :emphasize-text: ModuleNotFoundError

    E   ModuleNotFoundError: No module named 'src.type_error'
    ======================= short test summary info ========================
    ERROR attribute_error/tests/test_attribute_error.py
    ERROR booleans/tests/test_booleans.py
    ERROR calculator/tests/test_calculator.py
    ERROR dictionaries/tests/test_dictionaries.py
    ERROR exceptions/tests/test_exceptions.py
    ERROR functions/tests/test_functions.py
    ERROR list_comprehensions/tests/test_list_comprehensions.py
    ERROR lists/tests/test_lists.py
    ERROR magic/tests/test_magic.py
    ERROR magic_again/tests/test_magic_again.py
    ERROR more_magic/tests/test_more_magic.py
    ERROR none/tests/test_none.py
    ERROR person/tests/test_classes.py
    ERROR person/tests/test_person.py
    ERROR pro_magic/tests/test_pro_magic.py
    ERROR pro_magic_plus/tests/test_pro_magic_plus.py
    ERROR telephone/tests/test_telephone.py
    ERROR truth_table/tests/test_truth_table.py
    ERROR type_error/tests/test_type_error.py
    !!!!!!!!!!!!!!! Interrupted: 19 errors during collection !!!!!!!!!!!!!!!
    ================ 2 tests collected, 19 errors in X.YZs =================

  because Python_ cannot find ``type_error.py`` in the ``src`` folder_, there eis only one file_ in it.

  I have to tell Python_ how to get to ``type_error.py`` in the ``src`` folder_ of ``type_error`` so it can run the tests from there :ref:`TypeError<what causes TypeError?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add an ``__init__.py`` file_ to the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    touch __init__.py

  the terminal_ goes back to the command line

* I open ``__init__.py`` in the :ref:`editor<2 editors>`

* I add an `import statement`_ for the `sys module`_ in ``__init__.py``

  .. code-block:: python
    :linenos:

    import sys

  the `sys module`_ is part of the `Python Standard Library`_, it has an :ref:`attribute<test_attribute_error_w_class_attributes>` that has a :ref:`list<what is a list?>` of places for Python_ to check for :ref:`modules<what is a module?>`

* I add ``type_error`` to the :ref:`attribute<test_attribute_error_w_class_attributes>` with the :ref:`append method<test_append_adds_item_to_end_of_a_list>`

  .. code-block:: python
    :linenos:

    import sys
    sys.path.append('type_error')

  `sys.path`_ is a :ref:`list<what is a list>` of strings_ that Python_ checks for :ref:`modules<what is a module?>`

* I try to run the test again

  .. code-block:: python
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows ModuleNotFoundError_

  .. code-block:: python

    ModuleNotFoundError: No module named 'tests.test_truth_table'

  progress

* I add ``truth_table`` to the `sys.path`_


*********************************************************************************
test_module_not_found_error
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

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

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``module_not_found_error.py`` in the ``src`` folder to ``module_00.py`` and the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

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

  I make a new file_ named ``module_01.py`` in the ``src`` folder and the test passes

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

* I add the file_ to the ``src`` folder_ and the test passes

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
* :ref:`how to make functions<what is a function?>`
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
* :ref:`how to raise ModuleNotFoundError<what is a module?>`

:ref:`Would you like to test AttributeError?<what causes AttributeError?>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->