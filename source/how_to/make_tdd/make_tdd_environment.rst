.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with a single script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watch for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

#################################################################################
how to make a python test driven development environment
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

This chapter shows one way to make a Python_ `Test Driven Development`_ environment, first I do it manually where I make all the `folders/directories`_ and files needed, including setting up :ref:`the first test<test_failure>`, then :ref:`I write a program to do it for me<how to make a python test driven development environment automatically>`

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

windows requirements
#################################################################################

If you are using a Windows_ computer, try :ref:`how to install Windows Subsystem Linux on Windows`. If installing `Windows Subsystem Linux`_ does not work, use :ref:`how to make a python test driven development environment on Windows without Windows Subsystem Linux` instead of this chapter

linux/Windows Subsystem Linux requirements
#################################################################################

.. ATTENTION:: Do this only if you are using Linux_ or `Windows Subsystem Linux`_, no need to do it on a MacOS_ computer

Open a terminal_ then type this to update the `linux package manager`_

.. code-block:: shell

  sudo apt update

optionally, you can do a full upgrade if you want

.. code-block:: shell

  sudo apt full-upgrade --yes

type this in the terminal_ to install Python_

.. code-block:: shell

  sudo apt install python3 python3-venv --yes

----

********************************************************************************************
how to make a python test driven development environment manually
********************************************************************************************

* Let us say I have to work on a project and its name is ``magic``. I click on ``terminal_`` in the menu bar at the top of the `Integrated Development Environment (IDE)`_, then click ``New terminal_`` to open a terminal_
* I can use the cd_ program_ to change `folder/directory`_ to where I will store all the projects from this book. I type it in the terminal_

  .. code-block:: shell

    cd pumping_python

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: pumping_python

  the `folder/directory`_ does NOT exist. I need to make it

* I use the mkdir_ program_ to make a `folder/directory`_

  .. code-block:: shell

    mkdir pumping_python

  the terminal_ shows nothing. I try `changing directory`_ again

  .. code-block:: python

    cd pumping_python

  the terminal_ shows I am now in the ``pumping_python`` `folder/directory`_

  .. code-block:: shell

    .../pumping_python $

  - a `folder/directory`_ is a container for files_. It helps to organize things, just like a folder in a file cabinet is used to organize files that belong together. I keep every project I work on in its own `folder/directory`_ which makes them easy to find later. For example all the code from this book will be kept in ``pumping_python``
  - a `file`_ is a collection or container for text, like paper we write or print on and keep in a folder. Their names usually end with an  extension to show the type of file_ for example

    - ``.txt`` for a `plain text`_ file_
    - ``.sh`` for a bash_ file_
    - ``.ps1`` for a PowerShell_ file_
    -  ``.py`` for a :ref:`Python module<ModuleNotFoundError>`

  .. TIP:: to make sure I can see the ``pumping_python`` folder_ in my `Integrated Development Environment (IDE)`_ I have to open the folder. Here's how to do that with `Visual Studio Code`_

    .. code-block:: shell

      code .

    a new `Visual Studio Code`_ window opens in the ``pumping_python`` directory_

* I can use the tree_ program_ to see what files and folders are in a directory_. I type it in the terminal_ to see what is in the ``pumping_python`` directory_

  .. code-block:: shell

    tree

  - when tree_ is not installed on the computer the terminal_ shows

    .. code-block:: shell

      tree: command not found

    I need to install tree_ to use it

    .. admonition:: if you are using MacOS_ type this in the terminal_

      first install brew_ (The Missing Package Manager for macOS), if you do not have it already

      .. code-block:: shell

        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

      then use brew_ to install tree_

      .. code-block:: shell

        brew install tree

    or

    .. admonition:: if you are using Linux_ or `Windows Subsystem Linux`_ type this in the terminal_

      .. code-block:: shell

        sudo apt install tree --yes

    after the computer installs tree_, I run the command again

    .. code-block:: shell

      tree

  - when tree_ is installed on the computer, the terminal_ shows

    .. code-block:: shell

      .

      0 directories, 0 files

* I `change directory`_ to the ``magic`` project in the ``pumping_python`` folder_ with cd_

  .. code-block:: shell

    cd magic

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: magic

  the ``magic`` folder does not exist yet, ``pumping_python`` is empty. I make the directory_ with mkdir_

  .. code-block:: shell

    mkdir magic

  the terminal_ shows nothing. I use tree_ again

  .. code-block:: shell

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    └── magic

    2 directories, 0 files

  I try cd_ again

  .. code-block:: shell

    cd magic

  the terminal_ shows I am in the ``magic`` folder_ I just made in the ``pumping_python`` folder

  .. code-block:: shell

    .../pumping_python/magic

* I use Python_ to run the ``magic`` program_

  .. code-block:: shell

    python3 src/magic.py

  the terminal_ shows

  .. code-block:: text
    :force:

    python3: can't open file '.../pumping_python/magic/src/magic.py': [Errno 2] No such file or directory

  the computer cannot find the program_ because it does not exist yet. I make a child folder_ in the ``magic`` directory_ for it

  .. code-block:: shell

    mkdir src

  the terminal_ shows nothing. I use tree_ to see what changed in the ``magic`` directory_

  .. code-block:: shell

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    └── src

    2 directories, 0 files

  I try to run the ``magic`` program_ again

  .. code-block:: shell

    python3 src/magic.py

  the terminal_ shows the same error from before. I have to make the file_. I use touch_ to make an empty file in the ``src`` folder

  .. code-block:: shell

    touch src/magic.py

  the terminal_ shows nothing

* I use tree_ to see what folders_ and files_ I have now

  .. code-block:: shell

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    └── src
        └── magic.py

    2 directories, 1 file

  touch_ is a program_ that makes an empty file with whatever name it is given in whatever directory_ is given in the name, in this case ``touch src/magic.py`` makes a file named ``magic.py`` in the ``src`` folder_

* I try to run the ``magic`` program_ again

  .. code-block:: shell

    python3 src/magic.py

  the terminal_ shows nothing. Success! Even though this ``magic.py`` does not do anything because there is no code in it, I can successfully run it.

********************************************************************************************
test_failure
********************************************************************************************

The `Test Driven Development`_ cycle is ``RED GREEN REFACTOR``

* **RED**: make it fail - write a failing test to make sure the test works
* **GREEN**: make it pass - write the simplest thing that will make the failing test pass
* **REFACTOR**: make it better - write a better solution, test or both. Usually by `removing duplication`_

this process can be repeated as many times as possible

red: make it fail
############################################################################################

* Since this books is about `Test Driven Development`_ I use the unittest_ :ref:`module<ModuleNotFoundError>` from the `python standard library`_ that comes with Python_ to run tests. I type it in the terminal_

  .. code-block:: python

    python3 -m unittest

  the terminal_ shows

  .. code-block:: python

    ----------------------------------------------------------------------
    Ran 0 tests in 0.000s

    NO TESTS RAN

  - ``python3`` is the Python_ program_
  - ``-m`` is an option/switch passed when calling Python_ to run the :ref:`module<ModuleNotFoundError>` - unittest_ in this case
  - a Python_ :ref:`module<ModuleNotFoundError>` is any file that ends in ``.py``, this means somewhere on the computer there is a file named ``unittest.py``, `see the source code for unittest here <https://github.com/python/cpython/blob/3.14/Lib/unittest/__init__.py>`_

* I do not have any tests yet, that is why none ran. I make a child folder_ to keep the tests separate from the actual program_ (`source code`_)

  .. code-block:: shell

    mkdir tests

  the terminal_ shows nothing, I use tree_ to see what my project looks like now

  .. code-block:: shell

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── src
    │   └── magic.py
    └── tests

    3 directories, 1 file

* I use touch_ to add an empty file in the ``tests`` directory for the actual test

  .. code-block:: shell

    touch tests/magic.py

  the terminal_ shows nothing. I use tree_ to see what the project looks like so far

  .. code-block:: shell

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

  .. code-block:: shell

    python3 -m unittest

  the terminal_ shows

  .. code-block:: shell

    NO TESTS RAN

* I click on ``magic/tests/magic.py`` in the `Integrated Development Environment (IDE)`_ to open it in the editor, then type the following Python_ code in the file

  .. TIP:: I can open a file from the terminal_ in `Visual Studio Code`_ by typing ``code`` and the name of the file, for example

    .. code-block:: shell

      code tests/magic.py

  .. NOTE:: the line numbers below are a guide, you do not need to copy them

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code in the file

  - ``import unittest`` imports the unittest_ :ref:`module<ModuleNotFoundError>` from the `python standard library`_, this is what I am using for testing
  - ``class TestMagic``

    * ``class`` is the Python_ keyword for making :ref:`classes` - a group of :ref:`attributes (values)<AttributeError>` and :ref:`methods (functions)<functions>` that belong together, see :ref:`classes` for more
    * ``TestMagic`` is the name of this :ref:`class <classes>` and will hold the test

      .. IMPORTANT:: I can use any name for the test :ref:`class<classes>`, it MUST start with ``Test`` or unittest_ will not run the tests in it

    * `unittest.TestCase`_ is a :ref:`class <classes>` from the unittest_ :ref:`module<ModuleNotFoundError>` that has :ref:`methods<functions>` I will use for testing
    * ``class TestMagic(unittest.TestCase)`` defines ``TestMagic`` as a "child" of `unittest.TestCase`_ which means I can use its :ref:`methods<functions>` and :ref:`attributes<AttributeError>`

  - ``def test_failure``

    * def_ is the Python_ keyword for making :ref:`methods (functions) <functions>`, see :ref:`functions` for more
    * ``test_failure`` is the name of this :ref:`method<functions>` for :ref:`this first test<test_failure>`

      .. IMPORTANT:: I can use any name for the test :ref:`method<functions>`, it MUST start with ``test_`` or unittest_ will not run the tests in it

    * ``self.`` allows me to use :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of the ``TestMagic`` :ref:`class<classes>` which is a "child" of the `unittest.TestCase`_ :ref:`class<classes>`, instead of using ``TestMagic().`` or ``unittest.TestCase().``
    * ``self.assertFalse(True)`` is an :ref:`assertion<AssertionError>`

      - assertFalse_ is a :ref:`method<functions>` in the `unittest.TestCase`_ :ref:`class <classes>` that checks if its input is :ref:`False<test_what_is_false>`
      - :ref:`True<test_what_is_true>` is given as the input

      I expect this line to fail because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`. If it does not fail, then Python_ and I have a problem

* I turn on the ``Auto Save`` feature in the `Integrated Development Environment (IDE)`_ to automatically save files when I make a change so `I do not repeat myself`_ by hitting save (``ctrl+s`` (windows/linux) or ``command+s`` (mac)) every time I make a change
* I run the command again

  .. code-block:: shell

    python3 -m unittest

  the terminal_ shows

  .. code-block:: shell

    NO TESTS RAN

  I need to tell Python_ that the ``tests`` folder is a `python package`_, so it can find the tests

* then I use touch_ to add an empty file called ``__init__.py`` in the ``tests`` folder

  .. IMPORTANT:: make sure to use 2 underscores (__) for ``__init__.py``

  .. code-block:: shell

    touch tests/__init__.py

  the terminal_ shows nothing. I run the tree_ command to see what changed

  .. code-block:: shell

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

  I run the command again

  .. code-block:: shell

    python3 -m unittest

  the terminal_ shows

  .. code-block:: shell

    NO TESTS RAN

  I need to tell Python_ that ``magic.py`` in the ``tests`` folder is a test file

* I close ``magic.py`` in the editor of the `Integrated Development Environment (IDE)`_

  .. CAUTION:: if you do not close ``magic.py`` you will have 3 files in the ``tests`` folder after the next step instead of 2 because you turned on the ``Auto Save`` feature earlier

* then I use the mv_ program_ to change the name of the file to ``test_magic.py``

  .. code-block:: shell

    mv tests/magic.py tests/test_magic.py

  the terminal_ shows nothing. I use tree_ to see what I have so far

  .. code-block:: shell

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── src
    │   └── magic.py
    └── tests
        ├── __init__.py
        ├── __pycache__
        │   └── __init__.cpython-313.pyc
        └── test_magic.py

    4 directories, 4 files

* I run the command again

  .. code-block:: shell

    python3 -m unittest

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

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

  .. IMPORTANT:: I can use any name for the test file but it must start with ``test_`` or unittest_ will not run the tests in the file

* This is the ``RED`` part of the `Test Driven Development`_ cycle. The message in the terminal_ is about the failure, I like to read these from the bottom up, here is an explanation of each line

  * ``FAILED (failures=1)`` the number of failures
  * ``Ran 1 test in A.XYZs`` the number of tests it ran and how long they took
  * ``AssertionError: True is not false`` the :ref:`Error (Exception)<errors>` that happened and its message, in this case :ref:`AssertionError` because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`
  * ``self.assertFalse(True)`` the line of code that caused :ref:`AssertionError`
  * ``~~~~~~~~~~~~~~~~^^^^^^`` points to the part of the line above that Python_ thinks caused the :ref:`error<errors>`
  * ``File ".../magic/tests/test_magic.py", line 7, in test_failure`` the line number of the code that caused the :ref:`error<errors>` and the location of the file where it is

    .. TIP:: Hold ``ctrl`` (windows/linux) or ``option`` (mac) or ``command`` (mac) on the keyboard and use the mouse to click on ``File ".../pumping_python/magic/tests/test_magic.py", line 7`` in the terminal_, and the `Integrated Development Environment (IDE)`_ will open the file in the editor with the cursor at the line where the failure happened

  * ``Traceback (most recent call last):`` all the information shown after this line that is indented to the right shows the calls that led to the failure, this is why I like to read it from the bottom up
  * ``FAIL: test_failure (tests.test_magic.TestMagic.test_failure)`` is a header with information in :ref:`dot notation` about the failing test :ref:`method<functions>`

    - ``tests.test_magic.TestMagic.test_failure`` is the location of the failing test
    -  ``tests`` is the ``tests`` folder_
    -  ``test_magic`` is the ``test_magic.py`` file_ in the ``tests`` directory_
    - ``TestMagic`` is the :ref:`class <classes>` defined on line 4 in ``test_magic.py``
    - ``test_failure`` is the :ref:`method (function)<functions>` defined on line 6 in ``test_magic.py``

  * ``F`` shows a failure

* I recommend keeping a list of :ref:`Errors/Exceptions<errors>` you meet as you go through this book to become familiar with them, it helps when you run into them later. I add :ref:`AssertionError` to the list

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11

    import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError

green: make it pass
#################################################################################

I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` on line 7

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 1

          self.assertFalse(False)

then I run the test again in the terminal_

.. code-block:: python

  python3 -m unittest

and the test passes! The terminal_ shows

.. code-block:: none

  .
  ------------------------------------------------------
  Ran 1 test in A.XYZs

  OK

*cue CELEBRATION MUSIC AND DANCE!* I am GREEN.

refactor: make it better
############################################################################################

I ran ``python3 -m unittest`` a few times to see the test fail, I ran ``python3 -m unittest`` again to see the test pass. I will have to run ``python3 -m unittest`` again when I add any code, to make sure tests that were passing do not start failing and that the new code I add does what I want.

This means I have to run ``python3 -m unittest`` for each part of the `Test Driven Development`_ cycle or any time there is a code change. I do not want to type ``python3 -m unittest`` again, it is better for a `computer program`_ to run the tests so `I do not repeat myself`_.

----

********************************************************************************************
how to run tests automatically
********************************************************************************************

I can use `pytest-watch`_ to run tests automatically. It is a Python_ program_ that automatically runs pytest_ any time a Python_ file in the folder it is watching changes, this means it will run the tests for me every time I make a change.

pytest_ is a `python package`_ like unittest_, it is not part of the `python standard library`_. I type it in the terminal_

.. code-block:: shell

  pytest-watch

the terminal_ shows

.. code-block:: shell

  command not found: pytest-watch

I need to install it for the computer to use it

how to make a virtual environment
############################################################################################

I can install it globally, which means it will always be available to any project on the computer, but a better way would be to put it in a `virtual environment`_ so that it is installed specifically for this project.

A `virtual environment`_ is a separate folder where I can install `python packages`_ that my project needs. This helps me keep things that belong to the project in one place separate from other things on the computer. It means I can have a separate `virtual environment`_ for every project with only the programs_ that the project needs

* I make a `virtual environment`_ with the venv_ :ref:`module<ModuleNotFoundError>`

  .. code-block:: shell

    python3 -m venv .venv

  the terminal_ shows nothing

  - ``python3`` is the Python_ program_
  - ``-m`` is an option passed to Python_ to run the :ref:`module<ModuleNotFoundError>` given after the option
  - venv_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_, it is used to make a `virtual environment`_ with a given name
  - ``.venv`` is the name I am giving for this `virtual environment`_

    .. TIP:: ``.venv`` is Python_ convention, I can use any name I want for the virtual environment

* I run tree_

  .. code-block:: shell

    tree

  the terminal shows

  .. code-block:: shell

    .
    ├── src
    │   └── magic.py
    └── tests
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-313.pyc
        │   └── test_magic.cpython-313.pyc
        └── test_magic.py

  it does not look like anything changed. This is because the ``.`` in front of ``.venv`` means the folder_ is hidden

* I try tree_ again with a few options to see what changed

  .. code-block:: shell

    tree -a -L 2

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

  there is now a folder_ named ``.venv``

  - the ``-a`` option makes tree_ show all files that are listed including hidden files_ and folders_
  - the ``-L`` option tells tree_ how deep to go with showing the folders_ and files_, I use ``2`` to keep it only to the first level of  contents of the child folders_

* I have to activate the `virtual environment`_ to use it

  .. code-block:: shell

    source .venv/bin/activate

  the terminal shows

  .. code-block:: shell

    (.venv) .../magic $

  the ``(.venv)`` on the far left of the command line in the terminal_ shows that I am in the `virtual environment`_, for example

* I run `pytest-watch`_ again

  .. code-block:: shell

    pytest-watch

  the terminal_ shows

  .. code-block:: shell

    command not found: pytest-watch

  I have to install it in the `virtual environment`_ to use it in the `virtual environment`_

* I use the `python package manager (pip)`_ to see what `python packages`_ are already installed in the `virtual environment`_

  .. code-block:: python

    pip list

  the terminal_ shows

  .. code-block:: shell

    Package Version
    ------- -------
    pip     x.y

  - `pytest-watch`_ is not in the list
  - pip_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_, it is the package manager used to install `python packages`_

* I want to make a file where I can list all the Python_ packages for my project as a way to document it and have pip_ install the programs_ listed in the file. I can use echo_ to do this, it is a program_ that shows whatever it is given on the screen (`standard output (stdout)`_) for example

  .. code-block:: shell

    echo "pytest-watch"

  the terminal shows

  .. code-block:: shell

    pytest-watch

  I can also use echo_ to add text to a file_, I use it to make the requirements file_ with `pytest-watch`_ as its text

  .. code-block:: shell

    echo "pytest-watch" > requirements.txt

  - ``>`` is an operator that is used to send output from a program_ to the given file_
  - `pytest-watch`_ is a Python_ program_ that automatically runs pytest_ when a Python_ file_ in the folder_ changes
  - pytest_ is a `python package`_ like unittest_, that is used for testing
  - ``requirements.txt`` is the name of a file_ where I can list `python packages`_ for pip_ to install. The name ``requirements.txt`` is Python_ convention, I can use any name I want for the requirements file

* I run tree_ to see what the project looks like now

  .. code-block:: shell

    tree -a -L 2

  the terminal_ shows

  .. code-block:: shell
    :force:

    .
    ├── requirements.txt
    ├── src
    │   └── magic.py
    ├── tests
    │   ├── __init__.py
    │   ├── magic.py
    │   ├── __pycache__
    │   └── test_magic.py
    └── .venv
        ├── bin
        ├── .gitignore
        ├── include
        ├── lib
        ├── lib64 -> lib
        └── pyvenv.cfg

  there is a requirements file as part of the project

* I use pip_ to install `pytest-watch`_ from the requirements file

  .. code-block:: python

    python3 -m pip install --requirement requirements.txt

  - ``--requirement`` is another option that can be passed to the ``install`` argument for `python packages`_ in a given file_
  - ``requirements.txt`` is the name of the given file_

  when I do not have the latest version of pip_, the terminal_ shows

  .. code-block:: python

    [notice] A new release of pip is available: XY.Z -> AB.C
    [notice] To update, run: pip install --upgrade pip

  I upgrade pip_ to the latest version (this is good practice)

  .. code-block:: shell

    python3 -m pip install --upgrade pip

  - ``install`` is an argument given to pip_ to install a given Python_ package
  - ``--upgrade`` is an option/switch given to the ``install`` argument for pip_ to upgrade the version of the given `python package`_
  - ``pip`` is the Python_ package I am giving pip_ to install, in this case it upgrades itself

  .. NOTE:: I can also tell pip_ to install `pytest-watch`_ directly without using a requirements file, the problem is it will not document what programs_ my project needs. I would either have to remember later or use ``pip list`` and it does not help someone else who is trying to run my project later

    .. code-block:: shell

      python3 -m pip install pytest-watch

* I use pip_ to see what packages are now installed in the `virtual environment`_

  .. code-block:: python

    pip list

  the terminal_ shows

  .. code-block:: python

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

  .. code-block:: shell

    pytest-watch

  and it shows results without going back to the command line

  .. code-block:: ruby

    [TODAYS_DATE] Running: py.test
    ================== test session starts===================
    ...
    rootdir: .../magic
    collected 1 item

    tests/test_magic.py .                              [100%]

    =============== 1 passed in X.YZs =======================

  I hold ``ctrl`` (windows) or ``option`` (mac) or ``command`` (mac) on the keyboard and click on ``tests/test_magic.py`` to place the cursor in the editor of the `Integrated Development Environment (IDE)`_, then I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in ``test_magic.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

          self.assertFalse(True)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

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

  I hold ``ctrl`` (windows) or ``option`` (mac) or ``command`` (mac) on the keyboard and click on ``tests/test_magic.py:7`` to place the cursor in the editor of the `Integrated Development Environment (IDE)`_, then I change :ref:`True<test_what_is_true>` back to :ref:`False<test_what_is_false>` in ``test_magic.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

          self.assertFalse(False)

  the test passes. I can now write the rest of the code for the project while the tests run automatically

  .. TIP:: press ``ctrl+c`` on the keyboard in the terminal_ when you want to stop the tests to get back control of the terminal

----

********************************************************************************************
how to make a python test driven development environment automatically
********************************************************************************************

You made it this far and have become `the greatest programmer in the world`_. To follow `The Do Not Repeat Yourself (DRY) Principle`_, I write a program_ that has all the commands it took to get here, then I can use it to make a `Test Driven Development`_ Environment anytime I want and not have to remember every step of the process

* I exit the tests in the terminal_ by pressing ``ctrl+c`` on the keyboard
* I leave the `virtual environment`_

  .. code-block:: shell

    deactivate

  I try `pytest-watch`_ again to show that it only works inside the `virtual environment`_

  .. code-block:: shell

    pytest-watch

  the terminal_ shows

  .. code-block:: shell

    command not found: pytest-watch

* I use cd_ to `change directory`_ to the parent of ``magic``

  .. code-block:: shell

    cd ..

  ``..`` is shorthand for the parent of any directory_ you are in. The terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory

* I use touch_ to make an empty file with a name that describes the program_ to make a `Test Driven Development` environment automatically, this will make it is easy to remember later

  .. code-block:: shell

    touch makePythonTdd.sh

  the terminal_ shows nothing. I use tree_ to see what is in the ``pumping_python`` directory_

  .. code-block:: shell

    tree

  the terminal_ shows my new file is in the directory_

  .. code-block:: shell

    .
    ├── magic
    │   ├── requirements.txt
    │   ├── src
    │   │   └── magic.py
    │   └── tests
    │       ├── __init__.py
    │       ├── __pycache__
    │       │   ├── __init__.cpython-313.pyc
    │       │   ├── test_magic.cpython-313.pyc
    │       │   └── test_magic.cpython-313-pytest-9.0.1.pyc
    │       └── test_magic.py
    └── makePythonTdd.sh

* I type history_ in the terminal_

  .. code-block:: shell

    history

  the history_ program_ shows all the commands I typed in the terminal_ so far, and I use them to write the program_ that will automatically make a Python_ `Test Driven Development`_ environment for me

* I click on ``makePythonTdd.sh`` to open it in the editor of the `Integrated Development Environment (IDE)`_, then I add these commands to it

  .. NOTE:: the line numbers below are a guide, you do not need to copy them

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-

    #!/bin/bash
    mkdir magic
    cd magic
    mkdir src
    touch src/magic.py
    mkdir tests
    touch tests/__init__.py
    touch tests/test_magic.py
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    echo "pytest-watch" > requirements.txt
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  ``#!/bin/bash`` is called a shebang_ line, it tells the computer to use bash_ to run this program_

* I go back to the terminal_ to run the program_

  .. code-block:: shell

    makePythonTdd.sh

  the terminal_ shows

  .. code-block:: shell

    command not found: makePythonTdd.sh

  I have to tell the computer exactly where the file is

  .. code-block:: shell

    ./makePythonTdd.sh

  ``./`` is shorthand for ``this directory`` which in this case is ``pumping_python`` where ``makePythonTdd.sh`` is saved. The computer checks a few directories_ by default when a command is given. Those directories are where commands like mkdir_, cd_, tree_ and echo_ are saved. The terminal_ shows

  .. code-block:: shell

    permission denied: ./makePythonTdd.sh

  I need to make the program_ executable so the computer can run it

* I change the mode of the file_

  .. code-block:: shell

    chmod +x makePythonTdd.sh

  chmod_ is a program_ that changes the mode of the given file_, the terminal_ shows nothing

* I try the command again

  .. code-block:: shell

    ./makePythonTdd.sh

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1-3

    mkdir: cannot create directory ‘magic’: File exists
    mkdir: cannot create directory ‘src’: File exists
    mkdir: cannot create directory ‘tests’: File exists
    Requirement already satisfied: pip in ./.venv/lib/python3.13/site-packages (x.y)
    Collecting pip
    ...
    Successfully installed pip-X.Y
    Requirement already satisfied: pytest-watch in ./.venv/lib/python3.13/site-packages (from -r requirements.txt (line 1)) (X.Y.Z)
    Requirement already satisfied: docopt>=X.Y.Z in ./.venv/lib/python3.13/site-packages (from pytest-watch->-r requirements.txt (line 1)) (X.Y.Z)
    Requirement already satisfied: colorama>=X.Y.Z in ./.venv/lib/python3.13/site-packages (from pytest-watch->-r requirements.txt (line 1)) (X.Y.Z)
    Requirement already satisfied: watchdog>=X.Y.Z in ./.venv/lib/python3.13/site-packages (from pytest-watch->-r requirements.txt (line 1)) (X.Y.Z)
    Requirement already satisfied: pytest>=X.Y.Z in ./.venv/lib/python3.13/site-packages (from pytest-watch->-r requirements.txt (line 1)) (X.Y.Z)
    Requirement already satisfied: iniconfig>=X.Y.Z in ./.venv/lib/python3.13/site-packages (from pytest>=X.Y.Z->pytest-watch->-r requirements.txt (line 1)) (X.Y.Z)
    Requirement already satisfied: packaging>=XX in ./.venv/lib/python3.13/site-packages (from pytest>=X.Y.Z->pytest-watch->-r requirements.txt (line 1)) (X.Y)
    Requirement already satisfied: pluggy<X,>=X.Y in ./.venv/lib/python3.13/site-packages (from pytest>=X.Y.Z->pytest-watch->-r requirements.txt (line 1)) (X.Y.Z)
    Requirement already satisfied: pygments>=X.Y.Z in ./.venv/lib/python3.13/site-packages (from pytest>=X.Y.Z->pytest-watch->-r requirements.txt (line 1)) (X.Y.Z)

    [today's date] Running: py.test
    ================================= test session starts ==================================
    platform linux -- Python 3.XY.Z, pytest-X.Y.Z, pluggy-X.Y.Z
    rootdir: .../pumping_python/magic
    collected 1 item

    tests/test_magic.py .                                                            [100%]

    ================================== 1 passed in X.YZs ===================================

  This is a problem, the ``makePythonTdd.sh`` just made the ``magic`` project which already exists and so I get no failing test as my first test. It is repeating what I have already done.

* I want it to be able to make any project I want. It should take a name use it as the name for the project, then make the same structure I had for the ``magic`` project. I add a name as a variable_ to change ``magic`` in ``makePythonTdd.sh`` so I can give it any name when I want to make a project

  .. NOTE:: the line numbers below are a guide, you do not need to copy them. The lines that are changing in the code are highlighted

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 2-4,6,9

    #!/bin/bash
    PROJECT_NAME=$1
    mkdir $PROJECT_NAME
    cd $PROJECT_NAME
    mkdir src
    touch src/$PROJECT_NAME.py
    mkdir tests
    touch tests/__init__.py
    touch tests/test_$PROJECT_NAME.py
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    echo pytest-watch > requirements.txt
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  .. NOTE:: ``$1`` represents the first argument given when a program_ is called, I can use it in place of ``$PROJECT_NAME`` for example,

    .. code-block:: shell

      command argument

    in the code above, ``command`` will be ``./makePythonTdd.sh`` and ``$1`` will be the value of  ``argument``

* I use ``ctrl+c`` to stop the test from running then I run the ``makePythonTdd.sh`` again

  .. code-block:: python

    ./makePythonTdd.sh

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1-4

    mkdir: missing operand
    Try 'mkdir --help' for more information.
    mkdir: cannot create directory ‘src’: File exists
    mkdir: cannot create directory ‘tests’: File exists
    Requirement already satisfied: pip in ./.venv/lib/python3.13/site-packages (XY.Z)
    Collecting pip
      ...

    ================================= test session starts ==================================
    platform linux -- Python 3.XY.Z, pytest-X.Y.Z, pluggy-X.Y.Z
    rootdir: ...
    collected 0 items

    ================================ no tests ran in 0.00s =================================

  it did not work. No tests ran and there were errors with making the folders. I did not give ``./makePythonTdd.sh`` a name for the project when I called it so mkdir_ and cd_ did not work

* I stop `pytest-watch`_ from running by hitting ``ctrl+c`` on the keyboard in the terminal_, then I run ``makePythonTdd.sh`` with a project name this time

  .. code-block:: python

    ./makePythonTdd.sh a_project

  the terminal_ shows no errors but no tests ran

  .. code-block:: python

    ================================ no tests ran in X.YZs ================================

  I need to add code for :ref:`the first failing test<test_failure>` to the test file

* I use echo_ instead of touch_ to add text for the first failing test to ``test_$PROJECT_NAME.py``

  .. code-block:: shell
    :lineno-start: 9
    :emphasize-lines: 1

    echo "" > tests/test_$PROJECT_NAME.py

  then I add the text for the test like I did with ``test_magic.py`` in the :ref:`quotes ("")<quotes>`

  .. CAUTION:: Indentation_ matters in Python_, I use 4 spaces as convention in this book, see :PEP:`Python Style Guide <8>` for more

  .. literalinclude:: /code/make_tdd/makePythonTdd.sh
    :language: shell
    :linenos:
    :emphasize-lines: 10-21

* I hit ``ctrl+c`` on the keyboard in the terminal_ to stop `pytest-watch`_, then I try the program_ again with a different name for the project

  .. code-block:: shell

    ./makePythonTdd.sh another_project

  the terminal_ shows

  .. code-block:: shell

    ====================================== FAILURES =======================================
    __________________________ Testanother_project.test_failure ___________________________

    self = <tests.test_another_project.Testanother_project testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_another_project.py:7: AssertionError
    ============================== short test summary info ================================
    FAILED tests/test_another_project.py::Testanother_project::test_failure - AssertionError: True is not false
    ================================= 1 failed in X.YZs ===================================

  I hit ``ctrl+c`` on the keyboard in the terminal_ to stop the test

* I can now make a `Test Driven Development`_ environment with ``makePythonTdd.sh`` when I give it a name for the ``PROJECT_NAME`` variable. For example, when I type this in the terminal_

  .. code-block:: shell

    ./makePythonTdd.sh assertion_error

  the terminal_ shows

  .. code-block:: python

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

how to deactivate a virtual environment
#################################################################################################

When I want to leave a `virtual environment`_, I type this in the terminal_ to deactivate it

.. code-block::

  deactivate

----

how to activate a virtual environment
############################################################################################

When I want to work in a `virtual environment`_, I `change directory`_ to the `folder/directory`_ that has the `virtual environment`_ for example ``magic``, and type this in the terminal_

.. code-block:: shell

  source .venv/bin/activate

the ``(.venv)`` on the far left of the command line in the terminal_ shows that I am in the `virtual environment`_, for example

.. code-block:: shell

  (.venv) .../magic $

-----

********************************************************************************************
review
********************************************************************************************

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen a way to make a Python_ `Test Driven Development`_ Environment, and have a :ref:`program<makePythonTdd.sh>` to do it for you on any Linux_, Windows_ or MacOS_ computers.

Would you like to test :ref:`test AssertionError?<AssertionError>`

----

:ref:`Click Here to see the code for the program to make a Python Test Driven Development environment for any Linux or MacOS computers<makePythonTdd.sh>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->