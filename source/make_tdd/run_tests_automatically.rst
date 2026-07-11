.. meta::
  :description: Run Python tests automatically with pytest-watcher and uv on the person project from manual TDD setup. Jacob Itegboje adds requirements.txt with pytest and pytest-watcher, uv add --requirement requirements.txt, uv run pytest-watcher . --now, source .venv/bin/activate and deactivate, code tests/test_person.py from terminal, assert False is True collection error E assert False is True, fix to no tests ran on pass, Press q to stop watcher. Covers virtual environment .venv, pyproject.toml dependencies, uv.lock, NO TESTS RAN vs pytest collected 0 items, and why manual python3 -m unittest is replaced. Pumping Python make TDD project 1 part 2 after what is a module.
  :keywords: Jacob Itegboje, Pumping Python, pytest-watcher automatic tests, uv add requirement requirements.txt, uv run pytest-watcher --now, python virtual environment activate deactivate, source .venv/bin/activate, echo pytest requirements.txt, NO TESTS RAN unittest, collected 0 items pytest, assert False is True collection error, person project pumping_python, automate python3 -m unittest, test driven development environment manually part 2, pyproject.toml dependencies pytest-watcher, Press q stop pytest-watcher, code tests/test_person.py terminal

.. include:: ../links.rst

#################################################################################
how to run tests automatically
#################################################################################

In the previous chapters

* I ran ``python3 -m unittest`` to see the test fail
* I ran ``python3 -m unittest`` every time I made a change until the test passed

I run ``python3 -m unittest`` for each part of the :ref:`Test Driven Development Cycle<what is the Test Driven Development Cycle?>` or any time there is a code change. I want the computer to automatically run the tests for me.

----

*********************************************************************************
preview
*********************************************************************************

This is one way to automatically run tests in a :ref:`Python Test Driven Development project<what is a Test Driven Development Environment?>`. By the end of the chapter you will know these commands better

.. code-block:: python

  cd
  echo
  tree
  cat
  uv run pytest-watcher
  source .venv/bin/activate
  deactivate
  history

----

*********************************************************************************
questions about how to run tests automatically
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`how can I run tests automatically?<how to run tests automatically>`
* :ref:`how can I stop automated Python tests from running?<how to stop the automated tests>`
* :ref:`what is a Virtual Environment?<what is a virtual environment?>`
* :ref:`how can I activate a Virtual Environment?<how to activate a virtual environment>`
* :ref:`how can I deactivate a Virtual Environment?<how to deactivate a virtual environment>`
* :ref:`how can I document the Python programs my project needs?<how to write text to a file>`
* :ref:`how can I install the Python programs my project needs from a file?<how to install Python packages with uv>`
* :ref:`how can I view all the commands I type in a terminal?<how to view all the commands typed in a terminal>`

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``person`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd person

  the terminal_ shows I am in the ``person`` folder_

  .. code-block:: python

    .../pumping_python/person

* I use tree_ to see what the project looks like, as a reminder

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 15

    .
    ├── .git
    │   ├── config
    │   ├── description
    │   ├── FETCH_HEAD
    │   ├── HEAD
    │   ├── hooks
    │   ├── info
    │   ├── objects
    │   └── refs
    ├── .gitignore
    ├── pyproject.toml
    ├── .python-version
    ├── README.md
    ├── src
    │   └── person.py
    └── tests
        ├── __init__.py
        ├── __pycache__
        └── test_person.py

* I can use `pytest-watcher`_ to run tests automatically. It is a `Python program`_ that automatically runs pytest_ any time a :ref:`Python file<what is a module?>` changes in the folder_ it is looking at, this means it will run the tests for me every time I make a change.

  pytest_ is a `Python package`_ like :ref:`unittest<another way to write tests` that is used for testing. It is not part of `The Python Standard Library`_.

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

  - because `pytest-watcher`_ is not installed on the computer. I can install `pytest-watcher`_ with the `uv Python Package Manager`_
  - the message also shows ``Creating virtual environment at: .venv``

* I use tree_ to see what the project looks like now

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 15

    .
    ├── .git
    │   ├── config
    │   ├── description
    │   ├── FETCH_HEAD
    │   ├── HEAD
    │   ├── hooks
    │   ├── info
    │   ├── objects
    │   └── refs
    ├── .gitignore
    ├── pyproject.toml
    ├── .python-version
    ├── README.md
    ├── src
    │   └── person.py
    ├── tests
    │   ├── __init__.py
    │   ├── __pycache__
    │   └── test_person.py
    └── .venv
        ├── bin
        ├── CACHEDIR.TAG
        ├── .gitignore
        ├── lib
        ├── lib64 -> lib
        ├── .lock
        └── pyvenv.cfg

  uv_ made a :ref:`virtual environment<what is a virtual environment?>` in a folder_ named ``.venv`` with files_ and folders_.

----

*********************************************************************************
what is a virtual environment?
*********************************************************************************

A `virtual environment`_ is a separate folder_ where I can install `Python packages`_ that my project needs. This helps me keep things that belong to the project in one place, separate from other things on the computer.

It means I can have a separate `virtual environment`_ for every project with only the programs_ that the project needs. I do not have to keep every program_ I have ever used for projects that do not need them.


----

*********************************************************************************
how to write text to a file
*********************************************************************************

I want to make a file_ where I list all the `Python packages`_ that my project needs as a way to document it and have uv_ install the programs_ listed in the file_

* I can write text to a file_ with the `echo program`_, it shows whatever it is given as an argument, on the screen. For example, if I type this in the terminal_

  .. code-block:: python
    :emphasize-lines: 1

    echo "Hello, my name is Jacob"

  it shows

  .. code-block:: python

    Hello, my name is Jacob

* I can also use echo_ to add text to a file_. I use it to make the requirements file_ with pytest_ as what is inside it

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

  - ``>`` is an operator that is used to send output from a program_ to the given file_
  - pytest_ is a `Python package`_ like :ref:`unittest<another way to write tests`, that is used for testing
  - ``requirements.txt`` is the name of the file_ where I add names of `Python packages`_ for the `uv Python Package Manager`_ to install. The name ``requirements.txt`` is Python_ convention, I can use any name I want for the requirements file_.

* I use tree_ to see what the project looks like now

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 1

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 7

    .
    ├── .git
    ├── .gitignore
    ├── pyproject.toml
    ├── .python-version
    ├── README.md
    ├── requirements.txt
    ├── src
    ├── tests
    └── .venv

  ``requirements.txt`` is now in the ``person`` folder_

* I use the `cat program`_ to look at what is in ``requirements.txt``

  .. code-block:: python
    :emphasize-lines: 1

    cat requirements.txt

  the terminal_ shows

  .. code-block:: python

    pytest

* I add `pytest-watcher`_ to the requirements file_ as well

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

  - ``>>`` is an operator that is used to send output from a program_ to the given file_, it adds to what is in the file without writing over it
  - `pytest-watcher`_ is a `Python program`_ that automatically runs pytest_ when I change code in the project

* I use cat_ to look at what is in ``requirements.txt`` now

  .. code-block:: python
    :emphasize-lines: 1

    cat requirements.txt

  the terminal_ shows

  .. code-block:: python

    pytest
    pytest-watcher

  life is good!

----

*********************************************************************************
how to install Python packages with uv
*********************************************************************************

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
    :emphasize-lines: 10

    .
    ├── .git
    ├── .gitignore
    ├── pyproject.toml
    ├── .python-version
    ├── README.md
    ├── requirements.txt
    ├── src
    ├── tests
    ├── uv.lock
    └── .venv

  uv_ added ``uv.lock`` a file_ that has the exact versions of the `Python programs`_ that were installed.

* I use cat_ to show what is now in ``pyproject.toml``

  .. code-block:: python

    cat pyproject.toml

  the terminal_ is my friend, and shows

  .. code-block:: python
    :emphasize-lines: 8-9

    [project]
    name = "person"
    version = "0.1.0"
    description = "Add your description here"
    readme = "README.md"
    requires-python = ">=3.XY"
    dependencies = [
        "pytest>=M.N.O",
        "pytest-watcher>=P.Q.R",
    ]

  it added `pytest`_ and `pytest-watcher`_ to the dependencies of the project.

----

*********************************************************************************
how to activate a virtual environment
*********************************************************************************


When I want to work in a `virtual environment`_, I make sure I am in the parent folder_ of the `virtual environment`. In this case ``person`` is the parent. I activate the `virtual environment`_ in the terminal_ to use it

.. code-block:: python
  :emphasize-lines: 1

  source .venv/bin/activate

the terminal_ is my friend, and shows

.. code-block:: python

  (person) .../pumping_python/person

``(person)`` on the far left of the command line in the terminal_ shows that I am working in the `virtual environment`_.

----

*********************************************************************************
how to deactivate a virtual environment
*********************************************************************************

I can leave the `virtual environment`_ by typing ``deactivate`` in the terminal_

.. code-block:: python
  :emphasize-lines: 1

  deactivate

the terminal_ goes back to the command line

.. code-block:: python

  .../pumping_python/person

``(person)`` is no longer on the left side.

----

*********************************************************************************
how to run tests automatically with uv and pytest-watcher
*********************************************************************************

* I open ``test_person.py`` from the ``tests`` folder_
* I change ``assert False is False`` to ``assert False is True`` in ``test_person.py``

  .. code-block:: python
    :emphasize-lines: 2-3

    # False is True
    assert False is True
    # assert False is False


    # Exceptions seen
    # AssertionError

* I go back to the terminal_ to run the test again

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows an error without going back to the command line

  .. code-block:: shell
    :emphasize-lines: 14

    pytest-watcher version X.Y.Z
    Runner command: pytest
    Waiting for file changes in .../pumping_python/person
    =================== test session starts ====================
    platform ____ -- Python 3.A.B, pytest-C.D.E, pluggy-F.G.H
    rootdir: .../pumping_python/person
    configfile: pyproject.toml
    collected 0 items / 1 error

    ========================== ERRORS ==========================
    ___________ ERROR collecting tests/test_person.py ___________
    tests/test_person.py:2: in <module>
        assert False is True
    E   assert False is True
    ================= short test summary info ==================
    ERROR tests/test_person.py - assert False is True
    !!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!
    ===================== 1 error in I.JKs =====================
    [pytest-watcher]
    Current runner args: []
    Press w to show menu

  better!

----

*********************************************************************************
how to open the test file in the editor from the terminal
*********************************************************************************

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard, then click on ``tests/test_person.py`` to go back to ``test_person.py``. I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    # False is True
    # assert False is True
    assert False is False


    # Exceptions seen
    # AssertionError

  the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 8

    [ptw] Detected modified: ./tests/test_person.py ->
    =================== test session starts ====================
    platform ____ -- Python 3.A.B, pytest-C.D.E, pluggy-F.G.H
    rootdir: .../pumping_python/person
    configfile: pyproject.toml
    collecting ... [ptw] Detected modified: ./tests/test_person.py ->
    [ptw] Detected modified: ./tests/test_person.py ->
    collected 0 items

    ================== no tests ran in 0.01s ===================

    [pytest-watcher]
    Current runner args: []
    Press w to show menu

  - `pytest-watcher`_ "saw" the change I made to ``test_person.py`` and ran the test again
  - the terminal_ shows ``no tests ran`` which is confusing since the only way I know the test passed, is because I saw it fail

I can write the rest of the code for the project and get results back quickly because the tests run when I change the code.

I want to write code that represents a person, after :ref:`I learn what an assertion is<what is an assertion?>`.

----

*********************************************************************************
how to stop the automated tests
*********************************************************************************

I go to the terminal_ and use :kbd:`q` on the keyboard to stop the tests, the terminal_ goes back to the command line.

.. code-block:: python

  .../pumping_python/person

----

********************************************************************************************
close the project
********************************************************************************************

* I click in the terminal_ then add the new files_ and folders_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

  the terminal_ goes back to the command line.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'automate tests'

  the terminal_ shows a summary of the changes then goes back to the command line.

* I close ``test_person.py``

* I `change directory`_ to the parent of ``person``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  ``..`` is for the parent of any directory_ I am in. the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` folder_.

----

********************************************************************************************
review
********************************************************************************************

* I gave the computer some commands to :ref:`automate running tests for my Python Test Driven Development environment<how to run tests automatically>`
* I used uv_ to make a :ref:`virtual environment<what is a virtual environment?>`
* :ref:`I made a requirements file_ for my project dependencies<how to write text to a file>`
* :ref:`I installed pytest-watcher from the requirements file<how to install Python packages with uv>`
* :ref:`I ran the test automatically with uv and pytest-watcher<how to run tests automatically with uv and pytest-watcher>`

----

=====================================================================================================
how to view all the commands I typed to automate running tests
=====================================================================================================

----

* I type history_ in the terminal_ to see all the commands I typed in this chapter

  .. code-block:: python
    :emphasize-lines: 1

    history

  the terminal_ shows

  .. literalinclude:: ../code/make_tdd/makePythonTdd2History.sh
    :language: python
    :emphasize-lines: 4, 7, 9, 14

  the `history program`_ shows all the commands I typed in the terminal_

* these are the commands I used to make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>` then :ref:`run the tests automatically<how to run tests automatically>`

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

* these are the steps I took to make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>` then :ref:`run the tests automatically<how to run tests automatically>`

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
  - :ref:`run the tests automatically<how to run tests automatically with uv and pytest-watcher>`
  - :ref:`open the test file in the editor from the terminal<how to open the test file in the editor from the terminal>`
  - make the test pass

----

:ref:`How many questions can you answer after going through this chapter?<questions about how to run tests automatically>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python test driven development environment manually<how to make a Python test driven development environment manually>`.
* :ref:`I know what a Python module is<what is a module?>`.
* :ref:`I know how to run tests automatically<how to run tests automatically>`.

:ref:`Would you like to know what causes AssertionError<what causes AssertionError?>`

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