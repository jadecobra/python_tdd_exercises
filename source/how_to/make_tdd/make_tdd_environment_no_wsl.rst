.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with a single script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watch for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

########################################################################################################
how to make a python test driven development environment on Windows without Windows Subsystem Linux
########################################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

This is one way to make a Python_ `Test Driven Development`_ project on a Windows_ Computer that does NOT have `Windows Subsystem Linux`_. First, :ref:`I do it manually<how to make a python test driven development environment manually on Windows without Windows SubSystem Linux>` where I make all the `folders (directories)`_ and files_ for the environment, including setting up :ref:`the first test<test_failure>`, then :ref:`I write a program to do it for me<how to make a python test driven development environment automatically on Windows without Windows SubSystem Linux>`

----

*********************************************************************************
requirements
*********************************************************************************

* `download and install Python <https://www.python.org/downloads/>`_
* get an `Integrated Development Environment (IDE)`_. Here are a few options

  - `Visual Studio Code`_
  - `Sublime Text`_
  - PyCharm_
  - `other Integrated Development Environment (IDE) options`_

----

****************************************************************************************************************
how to make a python test driven development environment manually on Windows without Windows Subsystem Linux
****************************************************************************************************************

I use ``magic`` as the name for this project

* I click on ``Terminal`` in the menu bar at the top of the `Integrated Development Environment (IDE)`_, then click ``New Terminal`` to open a terminal_

* I use the cd_ program_ to change `folder (directory)`_ to where I will put all the projects from this book. I type it in the terminal_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd pumping_python

  the terminal_ shows

  .. code-block:: PowerShell

    cd: no such file or directory: pumping_python

  the `folder (directory)`_ does NOT exist. I need to make it

* I use the mkdir_ program_ to make a `folder (directory)`_

  .. code-block:: PowerShell

    mkdir pumping_python

  the terminal_ goes back to the command line. I try `changing directory`_ again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd pumping_python

  the terminal_ shows I am now in the ``pumping_python`` `folder (directory)`_

  .. code-block:: shell

    .../pumping_python $

* I type tree_ in the terminal_ to see what files_ and folders_ are  in the ``pumping_python`` directory_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

* the terminal_ shows

  .. code-block:: shell

    .

    0 directories, 0 files

  .. NOTE:: You will see more files_ and folders_ if you have done other work in the ``pumping_python`` folder_

* I `change directory`_ to the ``magic`` project in the ``pumping_python`` folder_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd magic

  the terminal_ shows

  .. code-block:: PowerShell

    cd: no such file or directory: magic

  the ``magic`` folder does not yet exist. I `make the directory`_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    mkdir magic

  this makes a `folder (directory)`_ for the project where its files will stay

* I use cd_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd magic

  the terminal_ goes back to the command line

* I use tree_ again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    └── magic

    2 directories, 0 files

* I try cd_ again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd magic

  the terminal_ shows I am in the ``magic`` folder_ I just made in the ``pumping_python`` folder

  .. code-block:: shell

    .../pumping_python/magic $

how to run a Python program on Windows without Windows SubSystem Linux
#################################################################################################

* I use Python_ to run the ``magic`` program_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python src/magic.py

  the terminal_ shows

  .. code-block:: text
    :force:

    python: can't open file '.../pumping_python/magic/src/magic.py': [Errno 2] No such file or directory

  the computer cannot find the program_ because it does not exist.

* I make a child folder_ in the ``magic`` directory_ for the program_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    mkdir src

the terminal_ goes back to the command line

* I use tree_ to see what changed in the ``magic`` directory_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    └── src

    2 directories, 0 files

* I try to run the ``magic`` program_ again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python src/magic.py

  the terminal_ shows the same error from before. I have to make the file_

how to make an empty file on Windows without Windows SubSystem Linux
#################################################################################################

* I use `New-Item`_ to make an empty file in the ``src`` folder

  .. code-block:: PowerShell
    :emphasize-lines: 1

    New-Item src/magic.py

  the terminal_ goes back to the command line

* I use tree_ to see what folders_ and files_ I now have

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    └── src
        └── magic.py

    2 directories, 1 file

  `New-Item`_ is a command that makes an empty file_ with the name. I can give the directory_ I want to put the file_ in as part of the name, in this case ``New-Item src/magic.py`` makes a file named ``magic.py`` in the ``src`` folder_

* I try to run the ``magic`` program_ again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python src/magic.py

  the terminal_ goes back to the command line. Success! Even though ``magic.py`` does not do anything because there is no code in it, I can successfully run it.

********************************************************************************************
test_failure
********************************************************************************************

The `Test Driven Development`_ cycle is ``RED GREEN REFACTOR``

* **RED**: make it fail - write a failing test to make sure the test works
* **GREEN**: make it pass - write the simplest thing that will make the failing test pass
* **REFACTOR**: make it better - write a better solution, test or both. Usually by `removing duplication`_

this process can be repeated as many times as possible or until I get to my goal.

how to run tests manually on Windows without WSL
#################################################################################################

* I use the unittest_ :ref:`module<ModuleNotFoundError>` from the `Python standard library`_ that comes with Python_ to run tests. I type this in the terminal_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m unittest

  the terminal_ shows

  .. code-block:: PowerShell

    ----------------------------------------------------------------------
    Ran 0 tests in 0.000s

    NO TESTS RAN

  - ``python`` is the Python_ program_
  - ``-m`` is an option/switch passed when calling Python_ to run the :ref:`module<ModuleNotFoundError>` - unittest_ in this case
  - a Python_ :ref:`module<ModuleNotFoundError>` is any file that ends with ``.py``, this means somewhere on the computer there is a file named ``unittest.py``, `see the source code for unittest here <https://github.com/python/cpython/blob/3.14/Lib/unittest/__init__.py>`_

* I do not have any tests yet, that is why none ran. I make a child folder_ to keep the tests separate from the actual program_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line, I use tree_ to see what my project now looks like

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── src
    │   └── magic.py
    └── tests

    3 directories, 1 file


* I use `New-Item`_ to add an empty file to the ``tests`` directory for the actual test

  .. code-block:: PowerShell
    :emphasize-lines: 1

    New-Item tests/magic.py

  the terminal_ goes back to the command line

* I use tree_ to see what the project looks like so far

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── src
    │   └── magic.py
    └── tests
        └── magic.py

    3 directories, 2 files

* I run the test again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m unittest

  the terminal_ shows

  .. code-block:: PowerShell

    NO TESTS RAN

RED: make it fail
############################################################################################

* I click on ``magic/tests/test_magic.py`` in the `Integrated Development Environment (IDE)`_ to open it in the :ref:`editor<2 editors>`, then type the following

  .. NOTE:: the line numbers below are a guide, you do not need to copy them

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code in the file_

  - ``import unittest`` imports the unittest_ :ref:`module<ModuleNotFoundError>` from the `Python standard library`_, this is what I am using for testing
  - ``class TestMagic``

    * ``class`` is the Python_ keyword for making :ref:`classes` - a group of :ref:`attributes (values)<AttributeError>` and :ref:`methods (functions)<functions>` that belong together, see :ref:`classes` for more
    * ``TestMagic`` is the name I gave this :ref:`class <classes>` and will hold the test

      .. IMPORTANT:: I can use any name for the test :ref:`class<classes>`, it MUST start with ``Test`` or unittest_ will NOT run the tests in it

    * `unittest.TestCase`_ is a :ref:`class <classes>` from the unittest_ :ref:`module<ModuleNotFoundError>` that has :ref:`methods<functions>` for testing
    * ``class TestMagic(unittest.TestCase)`` defines ``TestMagic`` as a "child" of `unittest.TestCase`_ which means I can use its :ref:`methods<functions>` and :ref:`attributes<AttributeError>`

  - ``def test_failure``

    * def_ is the Python_ keyword for making :ref:`methods (functions) <functions>`, see :ref:`functions` for more
    * ``test_failure`` is the name I used :ref:`method<functions>` for :ref:`this first test<test_failure>`

      .. IMPORTANT:: I can use any name for the test :ref:`method<functions>`, it MUST start with ``test_`` or unittest_ will NOT run the tests in it

    * ``self.`` allows me to use :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of the ``TestMagic`` :ref:`class<classes>` which is a "child" of the `unittest.TestCase`_ :ref:`class<classes>`, instead of using ``TestMagic().`` or ``unittest.TestCase().``

      .. IMPORTANT:: the name ``self`` is Python_ convention. I can use any name but it is easier to stick with convention for this concept

    * ``self.assertFalse(True)`` is an :ref:`assertion<AssertionError>`

      - assertFalse_ is a :ref:`method<functions>` in the `unittest.TestCase`_ :ref:`class <classes>` that checks if its input is :ref:`False<test_what_is_false>`
      - :ref:`True<test_what_is_true>` is given as the input

      I expect this line to fail because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`. If it does not fail, then Python_ and I have a problem

* I turn on the ``Auto Save`` feature in the `Integrated Development Environment (IDE)`_ to automatically save files when I make a change so that `I do not repeat myself`_ by hitting save (``ctrl+s`` (Windows/Linux) or ``command+s`` (mac)) every time I make a change
* I try the command again to run the tests in the terminal_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m unittest

  the terminal_ shows

  .. code-block:: PowerShell

    NO TESTS RAN

  I need to tell Python_ that the ``tests`` folder is a `Python package`_, so it can find the tests

how to make a Python package
--------------------------------------------------------------------------------------------

* I use `New-Item`_ to add an empty file with the name ``__init__.py`` in the ``tests`` folder

  .. IMPORTANT:: make sure to use 2 underscores (__) for ``__init__.py``

  .. code-block:: PowerShell
    :emphasize-lines: 1

    New-Item tests/__init__.py

  the terminal_ goes back to the command line

* I run the tree_ command to see what changed

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── src
    │   └── magic.py
    └── tests
        ├── __init__.py
        └── magic.py

    3 directories, 3 files

* I try to run the tests again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m unittest

  the terminal_ shows

  .. code-block:: PowerShell

    NO TESTS RAN

  I need to tell Python_ that ``magic.py`` in the ``tests`` folder is a test file

* I close ``magic.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. CAUTION:: if you do not close ``magic.py`` you will have 3 files in the ``tests`` folder after the next step instead of 2 because you turned on the ``Auto Save`` feature earlier

how to rename a file on Windows without WSL
--------------------------------------------------------------------------------------------

* I use the `Rename-Item`_ command to change the name of ``magic.py`` in the ``tests`` folder_ to ``test_magic.py``

  .. code-block:: PowerShell
    :emphasize-lines: 1

    Rename-Item -Path tests/magic.py -NewName tests/test_magic.py

  the terminal_ goes back to the command line

* I use tree_ to see what I have so far

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── src
    │   └── magic.py
    └── tests
        ├── __init__.py
        ├── __pycache__
        └── test_magic.py

    4 directories, 3 files

* I run the tests again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m unittest

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: PowerShell

    F
    =============================================================
    FAIL: test_failure (tests.test_magic.TestMagic.test_failure)
    -------------------------------------------------------------
    Traceback (most recent call last):
      File "...pumping_python/magic/tests/test_magic.py", line 7, in test_failure
        self.assertFalse(True)
        ~~~~~~~~~~~~~~~~^^^^^^
    AssertionError: True is not false

    -------------------------------------------------------------
    Ran 1 test in A.XYZs

    FAILED (failures=1)

  .. IMPORTANT:: I can use any name for the test file but it must start with ``test_`` or unittest_ will NOT run the tests in the file

* This is the ``RED`` part of the `Test Driven Development`_ cycle. The message in the terminal_ is about the failure, I like to read these from the bottom up, here is an explanation of each line, starting from the last line on the screen

  * ``FAILED (failures=1)`` the number of failures
  * ``Ran 1 test in A.XYZs`` the number of tests it ran and how long they took
  * ``AssertionError: True is not false`` the :ref:`Error (Exception)<errors>` that happened and its message, in this case :ref:`AssertionError` because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`
  * ``self.assertFalse(True)`` the line of code that caused :ref:`AssertionError`
  * ``~~~~~~~~~~~~~~~~^^^^^^`` points to the part of the line above that Python_ thinks caused the :ref:`error<errors>`
  * ``File ".../magic/tests/test_magic.py", line 7, in test_failure`` the line number of the code that caused the :ref:`error<errors>` and the location of the file where it is
  * ``Traceback (most recent call last):`` all the information shown after this line that is indented to the right shows the calls that led to the failure, this is why I like to read it from the bottom up
  * ``FAIL: test_failure (tests.test_magic.TestMagic.test_failure)`` is a header with information in :ref:`dot notation` about the failing test :ref:`method<functions>`

    - ``tests.test_magic.TestMagic.test_failure`` is the location of the failing test
    -  ``tests`` is the ``tests`` folder_
    -  ``test_magic`` is the ``test_magic.py`` file_ in the ``tests`` directory_
    - ``TestMagic`` is the :ref:`class <classes>` defined on line 4 in ``test_magic.py``
    - ``test_failure`` is the :ref:`method (function)<functions>` defined on line 6 in ``test_magic.py``

  * ``F`` shows a failure

* I hold ``ctrl`` (Windows/Linux) or ``option`` (mac) or ``command`` (mac) on the keyboard and use the mouse to click on ``File ".../pumping_python/magic/tests/test_magic.py", line 7`` in the terminal_, and the `Integrated Development Environment (IDE)`_ opens the file in the :ref:`editor<2 editors>` with the cursor at the line where the failure happened

GREEN: make it pass
#################################################################################

I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` on line 7 of ``test_magic.py``

.. code-block:: PowerShell
  :lineno-start: 7
  :emphasize-lines: 1

          self.assertFalse(False)

I run the test again in the terminal_

.. code-block:: PowerShell
  :emphasize-lines: 1

  python -m unittest

the test passes! The terminal_ shows

.. code-block:: none

  .
  ------------------------------------------------------
  Ran 1 test in A.XYZs

  OK

*cue CELEBRATION MUSIC AND DANCE!* I am GREEN!!

REFACTOR: make it better
############################################################################################

I recommend keeping a list of :ref:`Errors/Exceptions<errors>` you meet as you go through this book to become familiar with them, it helps when you run into them later. I add a list with :ref:`AssertionError` in ``test_magic.py`` in the :ref:`editor<2 editors>`

.. code-block:: python
  :linenos:
  :emphasize-lines: 10-11

  import unittest


  class TestMagic(unittest.TestCase):

      def test_failure(self):
          self.assertFalse(True)


  # Exceptions Encountered
  # AssertionError

I ran ``python -m unittest`` a few times to see the test fail, I ran ``python -m unittest`` again to see the test pass. I will have to run ``python -m unittest`` again when I add any code, to make sure tests that were passing do not start failing and that the new code I add does what I want.

This means I have to run ``python -m unittest`` for each part of the `Test Driven Development`_ cycle or any time there is a code change. I do not want to type ``python -m unittest`` again, it is better for a `computer program`_ to run the tests so that `I do not repeat myself`_.

----

********************************************************************************************
how to run tests automatically on Windows without Windows SubSystem Linux
********************************************************************************************

I can use `pytest-watch`_ to run tests automatically. It is a Python_ program_ that automatically runs pytest_ any time a Python_ file in the folder it is watching changes, this means it will run the tests for me every time I make a change.

pytest_ is a `Python package`_ like unittest_, it is not part of the `Python standard library`_. I type it in the terminal_

.. code-block:: PowerShell
  :emphasize-lines: 1

  pytest-watch

the terminal_ shows

.. code-block:: PowerShell

  command not found: pytest-watch

I need to install `pytest-watch`_ for the computer to use it

how to make a virtual environment on Windows without WSL
############################################################################################

I can install `pytest-watch`_ globally (for the entire computer), which means it will always be available to any project on the computer, but a better way would be to put it in a `virtual environment`_ so that it is installed only for this project.

A `virtual environment`_ is a separate folder where I can install `Python packages`_ that my project needs. This helps me keep things that belong to the project in one place, separate from other things on the computer.

It means I can have a separate `virtual environment`_ for every project with only the programs_ that the project needs. This helps if I decide to package the program_ to send to someone else, because everything needed by the project is in one place.

* I make a `virtual environment`_ with the venv_ :ref:`module<ModuleNotFoundError>`

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m venv .venv

  the terminal_ goes back to the command line

  - ``python`` is the Python_ program_
  - ``-m`` is an option passed to Python_ to run the :ref:`module<ModuleNotFoundError>` given after the option
  - venv_ is a :ref:`module<ModuleNotFoundError>` from the `Python standard library`_, it is used to make a `virtual environment`_ with a given name
  - ``.venv`` is the name I am giving for this `virtual environment`_

    .. TIP:: ``.venv`` is Python_ convention, I can use any name I want for the virtual environment

* I run tree_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── src
    │   └── magic.py
    └── tests
        ├── __init__.py
        ├── __pycache__
        └── test_magic.py

    4 directories, 3 files

  it does not look like anything changed. This is because the ``.`` in front of ``.venv`` means the folder_ is hidden

* I try tree_ again with another option to see what changed

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── src
    │   └── magic.py
    ├── tests
    │   ├── __init__.py
    │   ├── __pycache__
    │   └── test_magic.py
    └── .venv
        ├── bin
        ├── .gitignore
        ├── include
        ├── lib
        ├── lib64 -> lib
        └── pyvenv.cfg

    9 directories, 5 files

  there is now a folder_ named ``.venv`` for the `virtual environment`_

how to activate a virtual environment on Windows without WSL
############################################################################################

* When I want to work in a `virtual environment`_, I make sure I am in the parent directory_ of it, for example, ``magic`` in this case. I activate the `virtual environment`_ in the terminal_ to use it

  .. code-block:: PowerShell
    :emphasize-lines: 1

    .venv/scripts/activate.ps1

  the terminal_ shows

    .. code-block:: PowerShell

      (.venv) .../magic $

the ``(.venv)`` on the far left of the command line in the terminal_ shows that I am in the `virtual environment`_

* I run `pytest-watch`_ again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: PowerShell

    command not found: pytest-watch

  I have to install `pytest-watch`_ in the `virtual environment`_ to use it in the `virtual environment`_

how to see what packages are installed in a virtual environment
--------------------------------------------------------------------------------------------

I use the `Python package manager (pip)`_ to see what `Python packages`_ are installed in the `virtual environment`_

.. code-block:: PowerShell
  :emphasize-lines: 1

  pip list

the terminal_ shows

.. code-block:: PowerShell

  Package Version
  ------- -------
  pip     x.y

- `pytest-watch`_ is not in the list
- pip_ is a :ref:`module<ModuleNotFoundError>` from the `Python standard library`_, it is used to install `Python packages`_

how to write text to a file on Windows without Windows SubSystem Linux
--------------------------------------------------------------------------------------------
I want to make a file where I can list all the `Python packages`_ for my project as a way to document it and have pip_ install the programs_ listed in the file_

* I can write text to a file_ with the echo_ program_, it shows whatever it is given as an argument, on the screen (`standard output (stdout)`_) for example

  .. code-block:: PowerShell
    :emphasize-lines: 1

    echo "pytest-watch"

  the terminal_ shows

  .. code-block:: PowerShell

    pytest-watch

* I can also use echo_ to add text to a file_, I use it to make the requirements file_ with `pytest-watch`_ as its text

  .. code-block:: PowerShell
    :emphasize-lines: 1

    echo "pytest-watch" > requirements.txt

  - ``>`` is an operator that is used to send output from a program_ to the given file_
  - `pytest-watch`_ is a Python_ program_ that automatically runs pytest_ when a Python_ file_ in the folder_ changes
  - pytest_ is a `Python package`_ like unittest_, that is used for testing
  - ``requirements.txt`` is the name of a file_ where I can list `Python packages`_ for pip_ to install. The name ``requirements.txt`` is Python_ convention, I can use any name I want for the requirements file

* I run tree_ to see what the project looks like now

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: PowerShell
    :force:

    .
    ├── requirements.txt
    ├── src
    │   └── magic.py
    ├── tests
    │   ├── __init__.py
    │   ├── __pycache__
    │   └── test_magic.py
    └── .venv
        ├── bin
        ├── .gitignore
        ├── include
        ├── lib
        ├── lib64 -> lib
        └── pyvenv.cfg

    9 directories, 6 files

  ``requirements.txt`` is now in the ``magic`` folder_

how to install Python packages in a virtual environment on Windows without WSL
---------------------------------------------------------------------------------------------------

* I use pip_ to install `pytest-watch`_ from the requirements file

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m pip install --requirement requirements.txt

  - ``--requirement`` is an option that can be passed to the ``install`` argument for `Python packages`_ in a given file_
  - ``requirements.txt`` is the name of the given file_

  the terminal_ shows a bunch or programs_ being installed, and when I do not have the latest version of pip_ installed, it shows

  .. code-block:: PowerShell

    [notice] A new release of pip is available: XY.Z -> AB.C
    [notice] To update, run: pip install --upgrade pip

  I upgrade pip_ to the latest version. I recommend you do this every time you are in a `virtual environment`_, it is good practice to update package managers to the latest version available

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m pip install --upgrade pip

  - ``install`` is an argument given to pip_ to install a given `Python package`_
  - ``--upgrade`` is an option that can be passed to the ``install`` argument, like ``--requirement`` from earlier, this one tells pip_ to upgrade the version of the given `Python package`_
  - ``pip`` is the Python_ package I am giving pip_ to install, in this case it upgrades itself to the latest version since I did not give a version number

  .. NOTE:: I can also tell pip_ to install `pytest-watch`_ directly without using a requirements file, the problem is it will not document what programs_ my project needs. I would either have to remember later or use ``pip list``. It also does not help someone else who is trying to run my project later, know what programs it needs without me

    .. code-block:: PowerShell
      :emphasize-lines: 1

      python -m pip install pytest-watch

* I check what `Python packages`_ are now installed in the `virtual environment`_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    pip list

  the terminal_ shows

  .. code-block:: PowerShell

    Package      Version
    ------------ -------
    colorama     x.y.z
    docopt       x.y.z
    iniconfig    x.y.z
    packaging    x.y
    pip          x.y
    pluggy       x.y.z
    Pygments     x.y.z
    pytest       x.y.z
    pytest-watch x.y.z
    watchdog     x.y.z

  `pytest-watch`_ is in the list. Yes!

* I try to run the tests again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    pytest-watch

  and it shows results without going back to the command line

  .. code-block:: PowerShell
    :emphasize-lines: 6

    ================== test session starts===================
    ...
    rootdir: .../magic
    collected 1 item

    tests/test_magic.py .                              [100%]

    =============== 1 passed in X.YZs =======================

  I hold ``ctrl`` (Windows) or ``option`` (mac) or ``command`` (mac) on the keyboard and click on ``tests/test_magic.py`` to place the cursor in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in ``test_magic.py``

  .. code-block:: PowerShell
    :lineno-start: 7
    :emphasize-lines: 1

          self.assertFalse(True)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: PowerShell
    :emphasize-lines: 10

    ====================================== FAILURES =======================================
    _______________________________ TestMagic.test_failure ________________________________

    self = <tests.test_magic.TestMagic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic.py:7: AssertionError
    ============================== short test summary info ================================
    FAILED tests/test_magic.py::TestMagic::test_failure - AssertionError: True is not false
    ================================= 1 failed in X.YZs ===================================

  I hold ``ctrl`` (Windows) or ``option`` (mac) or ``command`` (mac) on the keyboard and click on ``tests/test_magic.py:7`` to place the cursor in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then I change :ref:`True<test_what_is_true>` back to :ref:`False<test_what_is_false>` in ``test_magic.py``

  .. code-block:: PowerShell
    :lineno-start: 7
    :emphasize-lines: 1

          self.assertFalse(False)

  the test passes and I can write the rest of the code for the project as the tests run automatically in response to my changes

  .. TIP:: press ``ctrl+c`` on the keyboard in the terminal_ when you want to stop the tests to get back to the command line

----

*******************************************************************************************************************
how to make a python test driven development environment automatically on Windows without Windows SubSystem Linux
*******************************************************************************************************************

You made it this far and have become `the greatest programmer in the world`_. To follow `The Do Not Repeat Yourself (DRY) Principle`_, I write a program_ that has all the commands it took to get here, then I can use that program_ to make a `Test Driven Development`_ Environment anytime I want and not have to remember every step of the process

how to exit the automated tests
############################################################################################
I exit the tests in the terminal_ by pressing ``ctrl+c`` on the keyboard

how to deactivate a virtual environment
############################################################################################

* I leave the `virtual environment`_ by typing this in the terminal_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    deactivate

* I try `pytest-watch`_ again to show that I do not have it installed outside the `virtual environment`_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: PowerShell

    command not found: pytest-watch

* I `change directory`_ to the parent of ``magic``

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd ..

  ``..`` is shorthand for the parent of any directory_ you are in. The terminal_ shows

  .. code-block:: shell

    .../pumping_python $

  I am back in the ``pumping_python`` folder_

how to make a PowerShell script
############################################################################################

* I use `New-Item`_ to make an empty file_ with a name that is easy to remember later and describes the program_ that will make a `Test Driven Development`_ environment automatically

  .. code-block:: PowerShell
    :emphasize-lines: 1

    New-Item makePythonTdd.ps1
  the terminal_ goes back to the command line. I use tree_ to see what is in the ``pumping_python`` directory_

  .. code-block:: PowerShell

    tree

  the terminal_ shows my new file_ is in the same parent directory_ of the ``magic`` project

  .. code-block:: shell

    .
    ├── magic
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    └── makePythonTdd.ps1

    5 directories, 2 files

how to view all the commands I typed in a terminal
--------------------------------------------------------------------------------------------

* I type history_ in the terminal_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    history

  the terminal_ shows

  .. code-block:: PowerShell
    :emphasize-lines: 6, 8, 10, 13, 22, 29, 32, 35, 37, 38, 40

    cd pumping_python
    mkdir pumping_python
    cd pumping_python
    tree
    cd magic
    mkdir magic
    tree
    cd magic
    python src/magic.py
    mkdir src
    tree
    python src/magic.py
    New-Item src/magic.py
    tree
    python src/magic.py
    python -m unittest
    mkdir tests
    tree
    New-Item tests/magic.py
    tree
    python -m unittest
    New-Item tests/__init__.py
    tree
    python -m unittest
    mv tests/magic.py tests/test_magic.py
    tree
    python -m unittest
    pytest-watch
    python -m venv .venv
    tree
    tree
    .venv/scripts/activate.ps1
    pytest-watch
    pip list
    "pytest-watch" | Out-File requirements.txt -Encoding UTF8
    tree
    python -m pip install --requirement requirements.txt
    python -m pip install --upgrade pip
    pip list
    pytest-watch
    deactivate
    pytest-watch
    cd ..
    New-Item makePythonTdd.ps1
    tree

  the history_ program_ shows all the commands I typed in the terminal_ so far, and I use them to write the program_ that will automatically make a Python_ `Test Driven Development`_ environment for me

* I click on ``makePythonTdd.ps1`` to open it in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then add the commands I used to make the ``magic`` project to the file_

  .. NOTE:: the line numbers below are a guide, you do not need to copy them

  .. code-block:: PowerShell
    :linenos:
    :emphasize-lines: 1-

    mkdir magic
    cd magic
    mkdir src
    New-Item src/magic.py
    mkdir tests
    New-Item tests/__init__.py
    New-Item tests/test_magic.py
    python -m venv .venv
    .venv/scripts/activate.ps1
    python -m pip install --upgrade pip
    "pytest-watch" | Out-File requirements.txt -Encoding UTF8
    python -m pip install --requirement requirements.txt
    pytest-watch
how to run a PowerShell script
--------------------------------------------------------------------------------------------

I go back to the terminal_ to run the program_

.. code-block:: PowerShell
  :emphasize-lines: 1

  makePythonTdd.ps1

the terminal_ shows

.. code-block:: PowerShell

  command not found: makePythonTdd.ps1

I have to tell the computer exactly where the file_ is

.. code-block:: PowerShell
  :emphasize-lines: 1

  ./makePythonTdd.ps1

``./`` is shorthand for ``this directory`` which in this case is ``pumping_python`` where ``makePythonTdd.ps1`` is saved. The computer checks a few directories_ by default when a command is given. Those directories are where commands like mkdir_, cd_, tree_ and echo_ are saved. The terminal_ shows


.. code-block:: PowerShell
  :force:
  :emphasize-lines: 1-3

  mkdir: cannot create directory ‘magic’: File exists
  mkdir: cannot create directory ‘src’: File exists
  mkdir: cannot create directory ‘tests’: File exists
  Requirement already satisfied: pip in ./.venv/lib/python.13/site-packages (x.y)
  Collecting pip
  ...
  ================================= test session starts ==================================
  platform Linux -- Python 3.XY.Z, pytest-X.Y.Z, pluggy-X.Y.Z
  rootdir: .../pumping_python/magic
  collected 1 item

  tests/test_magic.py .                                                            [100%]

  ================================== 1 passed in X.YZs ===================================

This is a problem, ``makePythonTdd.ps1`` just made the same ``magic`` project I made earlier and so I get no failing test as my first test. It is repeating what I have already done, and `I do not repeat myself`_

.. NOTE:: the terminal_ might show a different result for you. You can keep going, the key thing is that the program does not yet do what I want

I want ``makePythonTdd.ps1`` to be able to make a project for any name I give. It should take a name and use it as the name for the project, then make the same structure I had for the ``magic`` project

how to use variables in a PowerShell script
--------------------------------------------------------------------------------------------

* I change ``magic`` to a :ref:`variable<test_attribute_error_w_variables>` in ``makePythonTdd.ps1`` so I can give it any name when I want to make a project

  .. NOTE:: the line numbers below are a guide, you do not need to copy them

  .. code-block:: PowerShell
    :linenos:
    :emphasize-lines: 1-3,5,8

    $PROJECT_NAME=$args[0]
    mkdir $PROJECT_NAME
    cd $PROJECT_NAME
    mkdir src
    New-Item "src/$PROJECT_NAME.py"
    mkdir tests
    New-Item tests/__init__.py
    New-Item tests/test_$PROJECT_NAME.py
    python -m venv .venv
    .venv/scripts/activate.ps1
    python -m pip install --upgrade pip
    "pytest-watch" | Out-File requirements.txt -Encoding UTF8
    python -m pip install --requirement requirements.txt
    pytest-watch

  a :ref:`variable<test_attribute_error_w_variables>` is a name that is used for a value that can change. For example in mathematics we can use ``x`` to represent any number. In this case I use ``PROJECT_NAME`` to represent any name of a project

  .. ADMONITION:: ``$args[0]`` is for the first argument given when the program is called, I can use it in place of ``$PROJECT_NAME`` for example

    .. code-block:: PowerShell

      command argument

    in the code above, ``command`` will be ``makePythonTdd.ps1`` and ``$args[0]`` will be the value of  ``argument``

* I use ``ctrl+c`` on the keyboard in the terminal_ to stop the test from running then I run the ``makePythonTdd.ps1`` again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    ./makePythonTdd.ps1

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1-4

    mkdir: missing operand
    Try 'mkdir --help' for more information.
    mkdir: cannot create directory ‘src’: File exists
    mkdir: cannot create directory ‘tests’: File exists
    Requirement already satisfied: pip in ./.venv/lib/python.13/site-packages (XY.Z)
    Collecting pip
      ...
    ================================= test session starts ==================================
    platform Linux -- Python 3.XY.Z, pytest-X.Y.Z, pluggy-X.Y.Z
    rootdir: ...
    collected 0 items

    ================================ no tests ran in 0.00s =================================

  it did not work. No tests ran and there were errors with making the folders_. I did not give ``./makePythonTdd.ps1`` a name for the project when I called it so mkdir_ and cd_ were tried with no name and did not work

* I stop `pytest-watch`_ from running by hitting ``ctrl+c`` on the keyboard in the terminal_. I run tree_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── magic
    │   ├── .pytest_cache
    │   │   ├── CACHEDIR.TAG
    │   │   ├── .gitignore
    │   │   ├── README.md
    │   │   └── v
    │   ├── requirements.txt
    │   ├── src
    │   │   └── magic.py
    │   ├── tests
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   └── test_magic.py
    │   └── .venv
    │       ├── bin
    │       ├── .gitignore
    │       ├── include
    │       ├── lib
    │       ├── lib64 -> lib
    │       └── pyvenv.cfg
    └── makePythonTdd.ps1

  I still have the same files_ and folders_ as before I ran the program_

* I run ``makePythonTdd.ps1`` with a project name this time

  .. code-block:: PowerShell
    :emphasize-lines: 1

    ./makePythonTdd.ps1 magic_again

  the terminal_ shows no errors because no tests ran

  .. code-block:: PowerShell

    ================================ no tests ran in X.YZs ================================

  I need to add code for :ref:`the first failing test<test_failure>` to the test file_

* I hit ``ctrl+c`` on the keyboard in the terminal_ to stop `pytest-watch`_ then check what is in the ``pumping_python`` folder_ now

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 22-41

    .
    ├── magic
    │   ├── .pytest_cache
    │   │   ├── CACHEDIR.TAG
    │   │   ├── .gitignore
    │   │   ├── README.md
    │   │   └── v
    │   ├── requirements.txt
    │   ├── src
    │   │   └── magic.py
    │   ├── tests
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   └── test_magic.py
    │   └── .venv
    │       ├── bin
    │       ├── .gitignore
    │       ├── include
    │       ├── lib
    │       ├── lib64 -> lib
    │       └── pyvenv.cfg
    ├── magic_again
    │   ├── .pytest_cache
    │   │   ├── CACHEDIR.TAG
    │   │   ├── .gitignore
    │   │   ├── README.md
    │   │   └── v
    │   ├── requirements.txt
    │   ├── src
    │   │   └── magic_again.py
    │   ├── tests
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   └── test_magic_again.py
    │   └── .venv
    │       ├── bin
    │       ├── .gitignore
    │       ├── include
    │       ├── lib
    │       ├── lib64 -> lib
    │       └── pyvenv.cfg
    └── makePythonTdd.ps1
* I use the `Out-File`_ program to add text for the first failing test to ``test_$PROJECT_NAME.py``

  .. literalinclude:: /code/make_tdd/makePythonTdd.ps1
    :linenos:
    :language: PowerShell
    :emphasize-lines: 9-20

* I try the program_ again in the terminal_ with a different name for the project

  .. code-block:: PowerShell
    :emphasize-lines: 1

    ./makePythonTdd.ps1 more_magic

  the terminal_ shows

  .. code-block:: PowerShell
    :emphasize-lines: 10

    ====================================== FAILURES =======================================
    __________________________ Testmore_magic.test_failure ___________________________

    self = <tests.test_more_magic.Testmore_magic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_more_magic.py:7: AssertionError
    ============================== short test summary info ================================
    FAILED tests/test_more_magic.py::Testmore_magic::test_failure - AssertionError: True is not false
    ================================= 1 failed in X.YZs ===================================

* I hit ``ctrl+c`` on the keyboard in the terminal_ to stop `pytest-watch`_ then check what is in the ``pumping_python`` folder now

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 43-

    .
    ├── magic
    │   ├── .pytest_cache
    │   │   ├── CACHEDIR.TAG
    │   │   ├── .gitignore
    │   │   ├── README.md
    │   │   └── v
    │   ├── requirements.txt
    │   ├── src
    │   │   └── magic.py
    │   ├── tests
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   └── test_magic.py
    │   └── .venv
    │       ├── bin
    │       ├── .gitignore
    │       ├── include
    │       ├── lib
    │       ├── lib64 -> lib
    │       └── pyvenv.cfg
    ├── magic_again
    │   ├── .pytest_cache
    │   │   ├── CACHEDIR.TAG
    │   │   ├── .gitignore
    │   │   ├── README.md
    │   │   └── v
    │   ├── requirements.txt
    │   ├── src
    │   │   └── magic_again.py
    │   ├── tests
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   └── test_magic_again.py
    │   └── .venv
    │       ├── bin
    │       ├── .gitignore
    │       ├── include
    │       ├── lib
    │       ├── lib64 -> lib
    │       └── pyvenv.cfg
    ├── makePythonTdd.ps1
    └── more_magic
        ├── .pytest_cache
        │   ├── CACHEDIR.TAG
        │   ├── .gitignore
        │   ├── README.md
        │   └── v
        ├── requirements.txt
        ├── src
        │   └── more_magic.py
        ├── tests
        │   ├── __init__.py
        │   ├── __pycache__
        │   └── test_more_magic.py
        └── .venv
            ├── bin
            ├── .gitignore
            ├── include
            ├── lib
            ├── lib64 -> lib
            └── pyvenv.cfg

* I can now make a `Test Driven Development`_ environment with ``makePythonTdd.ps1`` when I give it a name for the ``PROJECT_NAME`` variable_. For example, when I type this in the terminal_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    ./makePythonTdd.ps1 assertion_error

  the terminal_ shows

  .. code-block:: PowerShell

    ====================================== FAILURES =======================================
    __________________________ Testassertion_error.test_failure ___________________________

    self = <tests.test_assertion_error.Testassertion_error testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_assertion_error.py:7: AssertionError
    =============================== short test summary info ===============================
    FAILED tests/test_assertion_error.py::Testassertion_error::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ==================================

  the computer makes a `Test Driven Development`_ environment for a project called :ref:`assertion_error<AssertionError>` and runs :ref:`the first failing test<test_failure>`. I continue this in :ref:`AssertionError`

----

********************************************************************************************
review
********************************************************************************************

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen a way to make a Python_ `Test Driven Development`_ Environment, and have a :ref:`program<makePythonTdd.ps1>` to do it for you on any Windows_ computer without `Windows SubSystem Linux`_.

Here are questions you can answer after going through this chapter

* :ref:`How can I make a Python Test Driven Development Environment manually?<how to make a python test driven development environment manually on Windows without Windows SubSystem Linux>`
* :ref:`How can I make a Python Test Driven Development Environment automatically?<how to make a python test driven development environment automatically on Windows without Windows SubSystem Linux>`
* :ref:`How can I change directories?<how to change directory>`
* :ref:`How can I make a directory?<how to make a directory>`
* :ref:`How can I see directory structure?<how to look at directory structure>`
* :ref:`How can I make an empty file?<how to make an empty file on Windows without Windows SubSystem Linux>`
* :ref:`How can I write text to a file?<how to write text to a file on Windows without Windows SubSystem Linux>`
* :ref:`How can I rename a file?<how to rename a file on Windows without WSL>`
* :ref:`How can I run a Python Program?<how to run a Python program on Windows without Windows SubSystem Linux>`
* :ref:`How can I test for failure?<test_failure>`
* :ref:`How can I make a Python package?<how to make a Python package>`
* :ref:`How can I run tests manually?<how to run tests manually on Windows without WSL>`
* :ref:`How can I run tests automatically?<how to run tests automatically on Windows without Windows SubSystem Linux>`
* :ref:`How can I stop automated Python tests from running?<how to exit the automated tests>`
* :ref:`What is a Virtual Environment?<how to make a virtual environment on Windows without WSL>`
* :ref:`How can I make a Virtual Environment?<how to make a virtual environment on Windows without WSL>`
* :ref:`How can I activate a Virtual Environment?<how to activate a virtual environment on Windows without WSL>`
* :ref:`How can I deactivate a Virtual Environment?<how to deactivate a virtual environment>`
* :ref:`How can I document the Python programs my project needs?<how to write text to a file on Windows without Windows SubSystem Linux>`
* :ref:`How can I install the Python programs my project needs from a file?<how to install Python packages in a virtual environment on Windows without WSL>`
* :ref:`How can I install Python packages in a Virtual Environment?<how to install Python packages in a virtual environment on Windows without WSL>`
* :ref:`How can I see what Python packages are installed in a Virtual Environment?<how to see what packages are installed in a virtual environment>`
* :ref:`How can I view all the commands I type in a terminal?<how to view all the commands I typed in a terminal>`
* :ref:`How can I make a PowerShell script?<how to make a PowerShell script>`
* :ref:`How can I use a :ref:`variable<test_attribute_error_w_variables>` in a PowerShell script<how to use variables in a PowerShell script>`
* :ref:`What is a :ref:`variable<test_attribute_error_w_variables>`?<how to use variables in a PowerShell script>`
* :ref:`How can I run a PowerShell script<how to run a PowerShell script>`
* :ref:`What is the Test Driven Development Cycle?<test_failure>`

Would you like to test :ref:`test AssertionError?<AssertionError>`

----

:ref:`Click Here to see the code for the program to make a Python Test Driven Development environment for any Linux or MacOS computers<makePythonTdd.ps1>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->