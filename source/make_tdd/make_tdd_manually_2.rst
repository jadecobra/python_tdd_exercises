.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watcher for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../links.rst

#################################################################################
how to run the tests automatically
#################################################################################

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``magic`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd magic

  the terminal_ shows I am in the ``magic`` folder_

  .. code-block:: python

    .../pumping_python/magic

* I can use `pytest-watcher`_ to run tests automatically. It is a `Python program`_ that automatically runs pytest_ any time a :ref:`Python file<what is a module?>` changes in the folder_ it is looking at, this means it will run the tests for me every time I make a change.

  pytest_ is a `Python package`_ like unittest_ that is used for testing. It is not part of `The Python Standard Library`_.

  I use uv_ to run `pytest-watcher`_ in the terminal_

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher

  the terminal_ is my friend, and shows

  .. code-block:: shell

    Using CPython 3.X.Y
    Creating virtual environment at: .venv
    error: Failed to spawn: `pytest-watcher`
      Caused by: No such file or directory (os error 2)

  because `pytest-watcher`_ is not installed on the computer. I can install it with the `uv Python Package Manager`_.

----

*********************************************************************************
how to write text to a file
*********************************************************************************

----

I want to make a file_ where I list all the `Python packages`_ that my project needs as a way to document it and have uv_ install the programs_ listed in the file_

* I can write text to a file_ with the `echo program`_, it shows whatever it is given as an argument, on the screen (`standard output (stdout)`_) for example, if I type this in the terminal_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest"

  it shows

  .. code-block:: python

    pytest

* I can also use echo_ to add text to a file_. I use it to make the requirements file_ with pytest_ as what is inside it

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

  - ``>`` is an operator that is used to send output from a program_ to the given file_
  - pytest_ is a `Python package`_ like unittest_, that is used for testing
  - ``requirements.txt`` is the name of the file_ where I am adding `Python packages`_ for the `uv Python Package Manager`_ to install. The name ``requirements.txt`` is Python_ convention, I can use any name I want for the requirements file_

* I add `pytest-watcher`_ to the requirements file_ as well

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

  - ``>>`` is an operator that is used to send output from a program_ to the given file_, it adds to what is in the file without writing over it
  - `pytest-watcher`_ is a `Python program`_ that automatically runs pytest_ when I change code in the project

* I use tree_ to see what the project looks like now

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 15

    .
    ├── .git
    │   ├── HEAD
    │   ├── branches
    │   ├── config
    │   ├── description
    │   ├── hooks
    │   ├── info
    │   ├── objects
    │   └── refs
    ├── .gitignore
    ├── .python-version
    ├── README.md
    ├── pyproject.toml
    ├── requirements.txt
    ├── src
    │   └── magic.py
    └── tests
        ├── __init__.py
        ├── __pycache__
        └── test_magic.py

  ``requirements.txt`` is now in the ``magic`` folder_

* I use cat_ to make sure ``requirements.txt`` has ``pytest`` and ``pytest-watcher`` inside it

  .. code-block:: python
    :emphasize-lines: 1

    cat requirements.txt

  the terminal_ shows

  .. code-block:: python

    pytest
    pytest-watcher

  life is good!

----

=====================================================================================================
how to install Python packages with uv
=====================================================================================================

----

* I use uv_ to install `pytest-watcher`_ from the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  - ``--requirement`` is an option that can be given to the ``add`` argument for `Python packages`_ in a given file_
  - ``requirements.txt`` is the name of the given file_. It helps to manage `Python programs`_ that are needed by the project. In this case I only have two programs_. A project can have a big number of programs it needs and using one file_ with one command is easier than one command for each program_

  the terminal_ is my friend, and shows setup and installation

  .. code-block:: shell

    Resolved 9 packages in GHIms
    ░░░░░░░░░░░░░░░░░░░░ [0/7] Installing wheels...
    ...
    Installed 7 packages in JKLms
     + iniconfig==A.B.C
     + packaging==DE.F
     + pluggy==G.H.I
     + pygments==J.K.L
     + pytest==M.N.O
     + pytest-watcher==P.Q.R
     + watchdog==S.T.U

* I run tree_ to see what changed in the project

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 1

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 5, 11

    .
    ├── .git
    ├── .gitignore
    ├── .python-version
    ├── .venv
    ├── README.md
    ├── pyproject.toml
    ├── requirements.txt
    ├── src
    ├── tests
    └── uv.lock

  uv_ added 2 things

  - ``.venv`` a folder_ for a :ref:`Virtual Environment<what is a virtual environment?>`
  - ``uv.lock`` a file_ that has the exact versions of the `Python programs`_ that were installed

* I use cat_ to show what is now in ``pyproject.toml``

  .. code-block:: python

    cat pyproject.toml

  the terminal_ is my friend, and shows

  .. code-block:: python
    :emphasize-lines: 8-9

    [project]
    name = "magic"
    version = "0.1.0"
    description = "Add your description here"
    readme = "README.md"
    requires-python = ">=3.XY"
    dependencies = [
        "pytest>=M.N.O",
        "pytest-watcher>=P.Q.R",
    ]

  it added `pytest`_ and `pytest-watcher`_ to the dependencies of the project

----

=====================================================================================================
what is a virtual environment?
=====================================================================================================

----

A `virtual environment`_ is a separate folder_ where I can install `Python packages`_ that my project needs. This helps me keep things that belong to the project in one place, separate from other things on the computer.

It means I can have a separate `virtual environment`_ for every project with only the programs_ that the project needs. I do not have to keep every program_ I have ever used for projects that do not need them.

----

=====================================================================================================
how to activate a virtual environment
=====================================================================================================

----

* When I want to work in a `virtual environment`_, I make sure I am in the parent directory_ of it, for example, ``magic`` in this case. I activate the `virtual environment`_ in the terminal_ to use it

  .. code-block:: python
    :emphasize-lines: 1

    source .venv/bin/activate

  the terminal_ is my friend, and shows

  .. code-block:: python

    (magic) .../magic

  ``(magic)`` on the far left of the command line in the terminal_ shows that I am in the `virtual environment`_

----

=====================================================================================================
how to deactivate a virtual environment
=====================================================================================================

----

* I leave the `virtual environment`_ by typing ``deactivate`` in the terminal_

  .. code-block:: python
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(magic)`` is no longer on the left side

  .. code-block:: python

    .../pumping_python/magic

----

=====================================================================================================
how to run the tests automatically with uv and pytest-watcher
=====================================================================================================

----

* I try to run the test again, this time with uv_

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows results without going back to the command line

  .. code-block:: python
    :emphasize-lines: 10

    pytest-watcher version X.Y.Z
    Runner command: pytest
    Waiting for file changes in .../pumping_python/magic
    =================== test session starts ====================
    platform ____ -- Python 3.A.B, pytest-C.D.E, pluggy-F.G.H
    rootdir: .../pumping_python/magic
    configfile: pyproject.toml
    collected 1 item

    tests/test_magic.py .                                 [100%]

    ==================== 1 passed in X.YZs =====================
    [pytest-watcher]
    Current runner args: []
    Press w to show menu

----

=====================================================================================================
how to open the test file in the editor from the terminal
=====================================================================================================

----

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard, then click on ``tests/test_magic.py`` to place the cursor of the `Integrated Development Environment (IDE)`_, then I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` on line 7

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7

    import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 10

    ======================== FAILURES ==========================
    _________________ TestMagic.test_failure ___________________

    self = <tests.test_magic.TestMagic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic.py:7: AssertionError
    =============== short test summary info ====================
    FAILED tests/test_magic.py::TestMagic::test_failure - AssertionError: True is not false
    =================== 1 failed in X.YZs ======================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard, then click on ``tests/test_magic.py:7`` to place the cursor of the `Integrated Development Environment (IDE)`_, then I change :ref:`True<test_what_is_true>` back to :ref:`False<test_what_is_false>` in ``test_magic.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

          self.assertFalse(False)

  the test passes. I can write the rest of the code for the project and get results back quickly because the tests run when I change the code

----

=====================================================================================================
how to stop the automated tests
=====================================================================================================

----

I go to the terminal_ and use :kbd:`q` on the keyboard to stop the tests, the terminal_ goes back to the command line.

.. code-block:: python

  .../pumping_python/magic

----

********************************************************************************************
close the project
********************************************************************************************

* I close ``test_magic.py``

* I click in the terminal and `change directory`_ to the parent of ``magic``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  ``..`` is for the parent of any directory_ I am in. the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` folder_

----

********************************************************************************************
review
********************************************************************************************

* I gave the computer some commands to make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>`
* I made some folders_
* I made some files_
* I made a :ref:`failing test<test_failure>`
* I made the failing test pass
* I made the test run automatically with `pytest-watcher`_

----

=====================================================================================================
how to view all the commands typed in a terminal
=====================================================================================================

----

* I type history_ in the terminal_ to see all the commands I have typed so far

  .. code-block:: python
    :emphasize-lines: 1

    history

  the terminal_ shows

  .. literalinclude:: ../code/make_tdd/makePythonTddHistory.sh
    :language: shell
    :emphasize-lines: 1-2, 10, 14, 19, 21, 24, 33-34, 37, 41, 52

  the `history program`_ shows all the commands I typed in the terminal_ so far, and I use them to write the program_ that will :ref:`automatically make a Python Test Driven Development environment<how to make a Python test driven development environment 2>` for me

* these are the commands I used to make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>`

  .. code-block:: python

    uv init NAME_OF_THE_PROJECT
    cd NAME_OF_THE_PROJECT
    mkdir src
    mv main.py src/NAME_OF_THE_PROJECT.py
    mkdir tests
    touch tests/__init__.py
    touch tests/test_NAME_OF_THE_PROJECT.py
    echo "pytest" > requirements.txt
    echo "pytest-watcher" >> requirements.txt
    uv add --requirement requirements.txt
    uv run pytest-watcher . --now

  where ``NAME_OF_THE_PROJECT`` is the name I give the project

* these are the steps I took to make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>`

  - give the project a name
  - :ref:`make a directory for the project<how to setup a project with uv>`
  - :ref:`change directory to the project<how to change directory to the project>`
  - :ref:`make a directory for the source code<how to make a directory for the source code>`
  - :ref:`make a Python file to hold the source code in the 'src' folder<how to make an empty file>`
  - :ref:`make a directory for the tests<how to make a directory for the tests>`
  - :ref:`make the 'tests' directory a Python package<how to make the tests a Python package>`
  - :ref:`make a Python file for the tests in the 'tests' directory<how to make a Python file for the tests in the 'tests' directory>`
  - :ref:`add the first failing test to the test file<test_failure>`
  - :ref:`make a requirements file for the Python packages I need<how to write text to a file>`
  - :ref:`install the Python packages I gave in the requirements file<how to install Python packages with uv>`
  - :ref:`run the tests automatically<how to run the tests automatically with uv and pytest-watcher>`
  - :ref:`open the test file in the editor from the terminal<how to open the test file in the editor from the terminal>`
  - make the test pass

----

:ref:`How many questions can you answer after going through this chapter?<questions about making a Python Test Driven Development Environment>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like to find out what a module is?<what is a module?>`

-----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->