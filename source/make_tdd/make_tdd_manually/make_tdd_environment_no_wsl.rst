.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watcher for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

########################################################################################################
how to make a python test driven development environment on Windows without Windows Subsystem for Linux
########################################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

********************************************************************************************
preview
********************************************************************************************

This is one way to make a :ref:`Python Test Driven Development project<what is a Test Driven Development Environment?>` on a Windows_ Computer that does NOT have `Windows Subsystem for Linux`_.

I walk through making the `folders (directories)`_ and files_ for the environment, including setting up :ref:`the first test<test_failure on Windows without WSL>`

By the end of the chapter you will know these commands better

.. code-block:: PowerShell

  mkdir
  cd
  touch
  echo
  cat
  mv
  Remove-Item
  uv run pytest-watcher
  source .venv/bin/activate
  deactivate
  history

----

*************************************************************************************************************************
questions about making a Python Test Driven Development Environment on Windows without Windows Subsystem for Linux
*************************************************************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`what is a Test Driven Development Environment?`
* :ref:`how can I make a Python Test Driven Development Environment manually?<how to make a Python Test Driven Development environment manually on Windows without Windows Subsystem for Linux>`
* :ref:`how can I change directories?<how to change directory>`
* :ref:`how can I make a directory?<how to make a directory>`
* :ref:`how can I see directory structure?<how to look at directory structure>`
* :ref:`how can I make an empty file?<how to make an empty file on Windows without Windows Subsystem for Linux>`
* :ref:`how can I write text to a file?<how to write text to a file on Windows without Windows Subsystem for Linux>`
* :ref:`how can I change the name of a file?<how to change the name of a file on Windows without WSL>`
* :ref:`how can I run a Python Program?<how to run a Python program on Windows without Windows Subsystem for Linux>`
* :ref:`how can I test for failure?<test_failure on Windows without WSL>`
* :ref:`how can I make a Python package?<how to make the tests a Python package on Windows without WSL>`
* :ref:`how can I run tests manually?<how to manually run tests on Windows without WSL>`
* :ref:`how can I run tests automatically?<how to run the tests automatically on Windows without Windows Subsystem for Linux>`
* :ref:`how can I stop automated Python tests from running?<how to stop the automated tests on Windows without WSL>`
* :ref:`what is a Virtual Environment?<what is a virtual environment?>`
* :ref:`how can I make a Virtual Environment?<how to make a virtual environment on Windows without WSL>`
* :ref:`how can I activate a Virtual Environment?<how to activate a virtual environment on Windows without WSL>`
* :ref:`how can I deactivate a Virtual Environment?<how to deactivate a virtual environment on Windows without WSL>`
* :ref:`how can I document the Python programs my project needs?<how to write text to a file on Windows without Windows Subsystem for Linux>`
* :ref:`how can I install the Python programs my project needs from a file?<how to install Python packages with uv on Windows without WSL>`
* :ref:`how can I install Python packages in a Virtual Environment?<how to install Python packages with uv on Windows without WSL>`
* :ref:`how can I see what Python packages are installed in a Virtual Environment?<how to see what packages are installed in a virtual environment on Windows without WSL>`
* :ref:`how can I view all the commands I type in a terminal?<how to view all the commands typed in a terminal on Windows without WSL>`

----

********************************************************************************************
requirements
********************************************************************************************

* `download and install Python <https://www.python.org/downloads/>`_
* get an `Integrated Development Environment (IDE)`_. Here are a few options

  - `Visual Studio Code`_
  - `Sublime Text`_
  - PyCharm_
  - `other Integrated Development Environment (IDE) options`_

----

****************************************************************************************************************
how to make a Python Test Driven Development environment manually on Windows without Windows Subsystem for Linux
****************************************************************************************************************

I choose ``magic`` as the name of this project

* I open ``Terminal`` in the menu bar at the top of the `Integrated Development Environment (IDE)`_, then click ``New Terminal`` to open a terminal_

* I `change directory`_ to where I will put all the projects from this book. I type cd_ in the terminal_

  .. NOTE:: You can skip this step if you are already in the ``pumping_python`` directory_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd pumping_python

  the terminal_ shows

  .. code-block:: PowerShell

    cd: no such file or directory: pumping_python

  the `folder (directory)`_ does NOT exist. I need to make it

* I use the `mkdir program`_ to make the ``pumping_python`` `folder (directory)`_

  .. code-block:: PowerShell

    mkdir pumping_python

the terminal_ goes back to the command line

* I try `changing directory`_ again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd pumping_python

  the terminal_ shows I am in the ``pumping_python`` `folder (directory)`_

  .. code-block:: shell

    ...\pumping_python >

* I type tree_ in the terminal_ to see what files_ and folders_ are in the ``pumping_python`` directory_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree /F

* the terminal_ shows

  .. code-block:: shell

    C:.
    No subfolders exist

  .. NOTE:: If you have done other work in the ``pumping_python`` folder_ there will be files_ and folders_ not 0 directories_ and 0 files_

----

=====================================================================================================
how to make a directory for the project on Windows without WSL
=====================================================================================================

----

* I `change directory`_ to the ``magic`` project in the ``pumping_python`` folder_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd magic

  the terminal_ shows

  .. code-block:: PowerShell

    cd: no such file or directory: magic

  the ``magic`` folder does NOT exist yet

* I make the ``magic`` directory_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    mkdir magic

  this makes a `folder (directory)`_ for the project where its files_ will stay

* I use tree_ again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree /F

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2

    .
    └── magic

----

=====================================================================================================
how to change directory to the project on Windows without WSL
=====================================================================================================

----

I try cd_ again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd magic

  the terminal_ shows I am in the ``magic`` folder_ I just made in the ``pumping_python`` folder

  .. code-block:: PowerShell

    ...\pumping_python\magic >

----

=====================================================================================================
how to run a Python program on Windows without Windows Subsystem for Linux
=====================================================================================================

----

* I use Python_ to run the ``magic`` program_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python src/magic.py

  the terminal_ shows

  .. code-block:: text

    python: can't open file '...\pumping_python\magic\src\magic.py': [Errno 2] No such file or directory

  the computer cannot find the program_ because it does not exist, yet

----

=====================================================================================================
how to make a directory for the source code on Windows without WSL
=====================================================================================================

----

* I make a child folder_ in the ``magic`` directory_ for the program_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line

* I use tree_ to see what changed in the ``magic`` directory_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree /F

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2

    .
    └── src

* I try to run the ``magic`` program_ again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python src/magic.py

  the terminal_ shows the same error from before. I have to make the file_

----

=====================================================================================================
how to make an empty file on Windows without Windows Subsystem for Linux
=====================================================================================================

----

* I use `New-Item`_ to make an empty file_ in the ``src`` folder_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    New-Item src/magic.py

  the terminal_ goes back to the command line

* I use tree_ to see what folders_ and files_ I now have

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree /F

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 3

    .
    └── src
        └── magic.py

  `New-Item`_ is a command that makes an empty file_ with the name. I can give it the directory_ I want to put the file_ in as part of the name, in this case ``New-Item src/magic.py`` makes a file_ named ``magic.py`` in the ``src`` folder_

* I try to run the ``magic`` program_ again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python src/magic.py

  the terminal_ goes back to the command line. Success! Even though ``magic.py`` does not do anything because there is no code in it, I can successfully run it because it is a Python_ file_.

----

********************************************************************************************
test_failure on Windows without WSL
********************************************************************************************

----

=====================================================================================================
how to manually run tests on Windows without WSL
=====================================================================================================

----

* I use the `unittest module`_ from the `Python standard library`_ that comes with Python_ to run tests. I type this in the terminal_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m unittest

  the terminal_ shows

  .. code-block:: PowerShell

    ----------------------------------------------------------------------
    Ran 0 tests in 0.000s

    NO TESTS RAN

  - ``python`` is the `Python program`_
  - ``-m`` is an option/switch passed when calling Python_ to run the :ref:`module<what is a module?>`, unittest_ in this case
  - a Python_ :ref:`module<what is a module?>` is any file_ that ends with ``.py``, this means somewhere on the computer there is a file_ named ``unittest.py``, `click here to see the source code for unittest`_

* I do not have any tests yet, so there is nothing to run

----

=====================================================================================================
how to make a directory for the tests on Windows without WSL
=====================================================================================================

----

* I make a child folder_ to keep the tests separate from the actual program_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    mkdir tests

the terminal_ goes back to the command line

* I use tree_ to see what my project looks like

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree /F

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4

    .
    ├── src
    │   └── magic.py
    └── tests

----

=====================================================================================================
how to make a Python file for the tests in the 'tests' directory on Windows without WSL
=====================================================================================================

----

* I use `New-Item`_ to add an empty file_ to the ``tests`` directory for the actual test

  .. code-block:: PowerShell
    :emphasize-lines: 1

    New-Item tests/magic.py

  the terminal_ goes back to the command line

* I use tree_ to see what the project looks like so far

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree /F

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 5

    .
    ├── src
    │   └── magic.py
    └── tests
        └── magic.py

* I run the test again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m unittest

  the terminal_ shows

  .. code-block:: PowerShell

    NO TESTS RAN

----

********************************************************************************************
:red:`RED`: make it fail
********************************************************************************************

* I open ``tests/magic.py`` with the `Integrated Development Environment (IDE)`_ to open it in the :ref:`editor<2 editors>`

  .. TIP::

    I can use the terminal_ to open a file_ in the `Integrated Development Environment (IDE)`_ by typing the name of the program and the name of the file_. That means when I type this in the terminal_

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/magic.py

    I can also open a file_ by using :kbd:`ctrl` on the keyboard and clicking with the mouse on the name of the file_

* I add the Python_ code below in ``tests/magic.py`` in the :ref:`editor<2 editors>`

  .. NOTE:: the line numbers below are a guide, you do not need to copy them

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code I typed in the file_

  - ``import unittest`` imports the `unittest module`_ from the `Python standard library`_, this is what I am using for testing
  - ``class TestMagic``

    * ``class`` is the Python_ keyword for making :ref:`classes<what is a class?>` - a group of :ref:`attributes (values)<what causes AttributeError?>` and :ref:`methods (functions)<what is a function?>` that belong together, I cover this in more detail in the :ref:`classes chapter<what is a class?>`
    * ``TestMagic`` is the name I gave this :ref:`class <what is a class?>` and will hold the test

      .. IMPORTANT:: I can use any name for the :ref:`test class<what is a class?>`, it MUST start with ``Test`` or unittest_ will NOT run the tests in it

    * `unittest.TestCase`_ is a :ref:`class <what is a class?>` from the `unittest module`_ that has :ref:`methods<what is a function?>` for testing
    * ``class TestMagic(unittest.TestCase)`` defines ``TestMagic`` as a "child" of `unittest.TestCase`_ which means I can use its :ref:`methods<what is a function?>` and :ref:`attributes<test_attribute_error_w_class_attributes>`

  - ``def test_failure``

    * def_ is the Python_ keyword for making :ref:`methods (functions) <what is a function?>`, see :ref:`functions<what is a function?>` for more
    * ``test_failure`` is the name I used :ref:`method<what is a function?>` for :ref:`this first test<test_failure>`

      .. IMPORTANT:: I can use any name for the :ref:`test method<what is a function?>`, it MUST start with ``test_`` or unittest_ does NOT run the tests in it

    * ``self.`` lets me use :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a function?>` of the ``TestMagic`` :ref:`class<what is a class?>` which is a "child" of the `unittest.TestCase class`_, instead of using ``TestMagic().`` or ``unittest.TestCase().``

      .. IMPORTANT:: the name ``self`` is Python_ convention. I can use any name but it is easier to stick with convention for this concept

    * ``self.assertFalse(True)`` is an :ref:`assertion<what is an assertion?>`

      - assertFalse_ is a :ref:`method<what is a function?>` in the `unittest.TestCase`_ :ref:`class <what is a class?>` that checks if its input is :ref:`False<test_what_is_false>`
      - :ref:`True<test_what_is_true>` is given as the input

      I expect this line to fail because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`. If it does not fail, then Python_ and I have a problem

* I turn on the ``Auto Save`` feature in the `Integrated Development Environment (IDE)`_ to automatically save files when I make a change so that `I do not repeat myself`_ by saving (:kbd:`ctrl+s` (Windows_/Linux_) or :kbd:`command+s` (MacOS_)) every time I make a change

  .. ATTENTION:: Turn on the ``Auto Save`` feature in your `Integrated Development Environment (IDE)`_

* I try the command again to run the tests in the terminal_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m unittest

  the terminal_ shows

  .. code-block:: PowerShell

    NO TESTS RAN

  I need to tell Python_ that the ``tests`` folder is a `Python package`_, so it can find the tests

----

=====================================================================================================
how to make the tests a Python package on Windows without WSL
=====================================================================================================

----

* I use `New-Item`_ to add an empty file_ with the name ``__init__.py`` in the ``tests`` folder

  .. ATTENTION:: make sure to use 2 underscores (__) before and after ``init`` for ``__init__.py``

  .. code-block:: PowerShell
    :emphasize-lines: 1

    New-Item tests/__init__.py

  the terminal_ goes back to the command line

* I run the tree_ command to see what changed

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree /F

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 5

    .
    ├── src
    │   └── magic.py
    └── tests
        ├── __init__.py
        └── magic.py

* I try to run the tests again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m unittest

  the terminal_ shows

  .. code-block:: PowerShell

    NO TESTS RAN

  I need to tell Python_ that ``magic.py`` in the ``tests`` folder is a test file

* I close ``magic.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. CAUTION:: if you do not close ``magic.py`` you will end up with 3 files in the ``tests`` folder after the next step (instead of 2), because the ``Auto Save`` feature (enabled earlier) will save the original file_ after you change its name

----

=====================================================================================================
how to change the name of a file on Windows without WSL
=====================================================================================================

----

* I use the `Move-Item`_ command to change the name of ``magic.py`` in the ``tests`` folder_ to ``test_magic.py``

  .. code-block:: PowerShell
    :emphasize-lines: 1

    Move-Item tests/magic.py tests/test_magic.py

  the terminal_ goes back to the command line

* I use tree_ to see what I have so far

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree /F

  the terminal_ shows

  .. NOTE:: if you do not see ``__pycache__`` in the list do not worry, the important thing is that you renamed ``magic.py`` to ``test_magic.py`` for unittest_ to find the test

  .. code-block:: shell
    :emphasize-lines: 7

    .
    ├── src
    │   └── magic.py
    └── tests
        ├── __init__.py
        ├── __pycache__
        └── test_magic.py

* I run the tests again

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m unittest

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 9

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

  .. IMPORTANT:: I can use any name for the test file_ but it must start with ``test_`` or unittest_ will NOT run the tests in the file

* This is the ``RED`` part of the `Test Driven Development`_ cycle. The message in the terminal_ is about the failure, I like to read these from the bottom up, here is an explanation of each line, starting from the last line on the screen

  - ``FAILED (failures=1)`` the number of failures
  - ``Ran 1 test in A.XYZs`` the number of tests it ran and how long they took
  - ``AssertionError: True is not false`` the :ref:`Error (Exception)<errors>` that happened and its message, in this case :ref:`AssertionError<what causes AssertionError?>` because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`
  - ``self.assertFalse(True)`` the line of code that caused :ref:`AssertionError<what causes AssertionError?>`
  - ``~~~~~~~~~~~~~~~~^^^^^^`` points to the part of the line above that Python_ thinks caused the :ref:`error<errors>`
  - ``File ".../magic/tests/test_magic.py", line 7, in test_failure`` the line number of the code that caused the :ref:`error<errors>` and the location of the file where it is
  - ``Traceback (most recent call last):`` all the information shown after this line that is indented to the right shows the calls that led to the failure, this is why I like to read it from the bottom up
  - ``FAIL: test_failure (tests.test_magic.TestMagic.test_failure)`` is a header with information in :ref:`dot notation` about the failing :ref:`test method<what is a function?>`

    - ``tests.test_magic.TestMagic.test_failure`` is the location of the failing test
    -  ``tests`` is the ``tests`` folder_
    -  ``test_magic`` is the ``test_magic.py`` file_ in the ``tests`` directory_
    - ``TestMagic`` is the :ref:`class <what is a class?>` defined on line 4 in ``test_magic.py``
    - ``test_failure`` is the :ref:`method (function)<what is a function?>` defined on line 6 in ``test_magic.py``

  * ``F`` shows a failure

* I hold :kbd:`ctrl` on the keyboard and use the mouse to click on ``File ".../pumping_python/magic/tests/test_magic.py", line 7`` in the terminal_, and the `Integrated Development Environment (IDE)`_ opens the file_ in the :ref:`editor<2 editors>` with the cursor at the line where the failure happened

----

********************************************************************************************
:green:`GREEN`: make it pass
********************************************************************************************

I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` on line 7 of ``test_magic.py`` in the :ref:`editor<2 editors>`

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

----

********************************************************************************************
:yellow:`REFACTOR`: make it better
********************************************************************************************

Keep a list of :ref:`Errors/Exceptions<errors>` that show up in the terminal_ as you go through this book to know them better, it helps when you run into them later. I add a list with :ref:`AssertionError<what causes AssertionError?>` in ``test_magic.py`` in the :ref:`editor<2 editors>`

.. code-block:: python
  :linenos:
  :emphasize-lines: 10-11

  import unittest


  class TestMagic(unittest.TestCase):

      def test_failure(self):
          self.assertFalse(True)


  # Exceptions seen
  # AssertionError

I ran ``python -m unittest`` a few times to see the test fail, I ran ``python -m unittest`` again to see the test pass. I will have to run ``python -m unittest`` again when I add any code, to make sure tests that were passing do not start failing and that the new code I add does what I want.

This means I have to run ``python -m unittest`` for each part of the `Test Driven Development`_ cycle or any time there is a code change.

I do not want to type ``python -m unittest`` again, it is better for a `computer program`_ to run the tests so that `I do not repeat myself`_.

----

=====================================================================================================
how to run the tests automatically on Windows without Windows Subsystem for Linux
=====================================================================================================

----

I can use `pytest-watcher`_ to run tests automatically. It is a `Python program`_ that automatically runs pytest_ any time a Python_ file_ changes in the folder_ it is looking at, this means it will run the tests for me every time I make a change.

pytest_ is a `Python package`_ like unittest_, it is not part of the `Python standard library`_

I type it in the terminal_

.. code-block:: PowerShell
  :emphasize-lines: 1

  pytest-watcher

the terminal_ shows

.. code-block:: PowerShell

  command not found: pytest-watcher

I need to install `pytest-watcher`_ for the computer to use it. Next, I set up a `virtual environment`_ to keep programs_ my project needs in one place

----

=====================================================================================================
what is a virtual environment?
=====================================================================================================

----

I can install `pytest-watcher`_ globally (for the entire computer), which means it will always be available to any project on the computer, but a better way would be to put it in a `virtual environment`_ so that it is installed only for this project.

A `virtual environment`_ is a separate folder_ where I can install `Python packages`_ that my project needs. This helps me keep things that belong to the project in one place, separate from other things on the computer.

It means I can have a separate `virtual environment`_ for every project with only the programs_ that the project needs. This helps if I decide to package the program_ to send to someone else, because everything needed by the project is in one place.

----

=====================================================================================================
how to make a virtual environment on Windows without WSL
=====================================================================================================

----

* I make a `virtual environment`_ with the venv_ :ref:`module<what is a module?>` from the `Python standard library`_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m venv .venv

  the terminal_ goes back to the command line

  - ``python`` is the `Python program`_
  - ``-m`` is an option passed to Python_ to run the :ref:`module<what is a module?>` given after the option
  - venv_ is a :ref:`module<what is a module?>` from the `Python standard library`_, it is used to make a `virtual environment`_ with a given name
  - ``.venv`` is the name I am giving for this `virtual environment`_

    .. IMPORTANT:: ``.venv`` is Python_ convention, I can use any name I want for the virtual environment

* I run tree_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree /F


  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 8

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

  there is now a folder_ named ``.venv`` for the `virtual environment`_

----

=====================================================================================================
how to activate a virtual environment on Windows without WSL
=====================================================================================================

----

* I run PowerShell_ in Administrator mode and set the Execution Policy for the activation script to work

  .. code-block:: PowerShell
    :emphasize-lines: 1

    Set-ExecutionPolicy RemoteSigned

  the terminal_ may show the following message if you have never run this command before

  .. code-block:: text
    :emphasize-lines: 7

    The execution policy helps protect you from scripts that you do not trust.
    Changing the execution policy might expose you to the security risks
    described in the about_Execution_Policies help topic at
    https:/go.microsoft.com/fwlink/?LinkID=135170.
    Would you like to change the execution policy?

    [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"):

  Type ``A`` to accept the change and it enables scripts that have been signed by a verified publisher to run on your computer, you can read more at `Set-ExecutionPolicy`_

* When I want to work in a `virtual environment`_, I make sure I am in the parent directory_ of it, for example, ``magic`` in this case. I activate the `virtual environment`_ in the terminal_ to use it

  .. code-block:: PowerShell
    :emphasize-lines: 1

    .venv/scripts/activate.ps1

  the terminal_ shows

    .. code-block:: PowerShell

      (.venv) .../magic

  the ``(.venv)`` on the far left of the command line in the terminal_ shows that I am in the `virtual environment`_

* I use `pytest-watcher`_ to run the test again

  .. code-block:: PowerShell
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: PowerShell

    command not found: pytest-watcher

  I have to install `pytest-watcher`_ in the `virtual environment`_ to use it in the `virtual environment`_

----

=====================================================================================================
how to see what packages are installed in a virtual environment on Windows without WSL
=====================================================================================================

----

I use the `Python package manager (pip)`_ to see what `Python packages`_ are installed in the `virtual environment`_ I just made

.. code-block:: PowerShell
  :emphasize-lines: 1

  pip list

the terminal_ shows

.. code-block:: PowerShell

  Package Version
  ------- -------
  pip     x.y

- `pytest-watcher`_ is not in the list
- pip_ is a :ref:`module<what is a module?>` from the `Python standard library`_, it is used to install `Python packages`_

----

=====================================================================================================
how to write text to a file on Windows without Windows Subsystem for Linux
=====================================================================================================

----

I want to make a file_ where I can list all the `Python packages`_ for my project as a way to document it and have pip_ install the programs_ listed in the file_

* I can write text to a file_ with the `echo program`_, it shows whatever it is given as an argument, on the screen (`standard output (stdout)`_) for example

  .. code-block:: PowerShell
    :emphasize-lines: 1

    echo "pytest-watcher"

  the terminal_ shows

  .. code-block:: PowerShell

    pytest-watcher

  I can use it to write text to a file_ by giving the file_ name with an operator

  .. code-block:: PowerShell

    echo "pytest-watcher" > requirements.txt

  ``>`` is an operator that is used to send output from a program_ to the given file_

* I can also use `Out-File`_ to add text to a file_, I use it to make the requirements file_ with `pytest-watcher`_ as its text

  .. code-block:: PowerShell
    :emphasize-lines: 1

    "pytest-watcher" | Out-File requirements.txt

  - ``|`` is an operator that is used to send output to a program_
  - `Out-File`_ is a program_ that can be used to write text to a file_
  - `pytest-watcher`_ is a `Python program`_ that automatically runs pytest_ when I change code in the project
  - pytest_ is a `Python package`_ like unittest_, that is used for testing
  - ``requirements.txt`` is the name of a file_ where I can list `Python packages`_ for pip_ to install. The name ``requirements.txt`` is Python_ convention, I can use any name I want for the requirements file

* I run tree_ to see what the project looks like now

  .. code-block:: PowerShell
    :emphasize-lines: 1

    tree /F

  the terminal_ shows

  .. code-block:: shell
    :force:
    :emphasize-lines: 2

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

  ``requirements.txt`` is now in the ``magic`` folder_

----

=====================================================================================================
how to see what is inside a file on Windows without WSL
=====================================================================================================

----

I can use the `cat program`_ to see what is inside a file_. I use it to make sure my ``requirements.txt`` has ``pytest-watcher`` inside it

.. code-block:: shell
  :emphasize-lines: 1

  cat requirements.txt

the terminal_ shows

.. code-block:: shell

  pytest-watcher

life is good!

----

=====================================================================================================
how to install Python packages with uv on Windows without WSL
=====================================================================================================

----

* I use pip_ to install `pytest-watcher`_ from the requirements file

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m pip install --requirement requirements.txt

  - ``--requirement`` is an option that can be passed to the ``install`` argument for `Python packages`_ in a given file_
  - ``requirements.txt`` is the name of the given file_

  the terminal_ shows programs_ being downloaded and installed, and when I do not have the latest version of pip_ installed, it shows this at the end

  .. code-block:: PowerShell

    [notice] A new release of pip is available: XY.Z -> AB.C
    [notice] To update, run: pip install --upgrade pip

----

=====================================================================================================
how to upgrade the Python package manager in a virtual environment on Windows without WSL
=====================================================================================================

----

* I upgrade pip_ to the latest version. I recommend you do this every time you are in a `virtual environment`_, it is good practice to update package managers to the latest version available

  .. code-block:: PowerShell
    :emphasize-lines: 1

    python -m pip install --upgrade pip

  - ``install`` is an argument given to pip_ to install a given `Python package`_
  - ``--upgrade`` is an option that can be passed to the ``install`` argument, like ``--requirement`` from earlier, this one tells pip_ to upgrade the version of the given `Python package`_
  - ``pip`` is the `Python package`_ I am giving pip_ to install, in this case it upgrades itself to the latest version since I did not give a version number

  .. NOTE:: I can also tell pip_ to install `pytest-watcher`_ directly without using a requirements file, the problem is it will not document what programs_ my project needs. I would either have to remember later or use ``pip list``. It also does not help someone else who is trying to run my project later, know what programs it needs without me

    .. code-block:: PowerShell

      python -m pip install pytest-watcher

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
    pytest-watcher x.y.z
    watchdog     x.y.z

  `pytest-watcher`_ is in the list. Yes!

  .. TIP:: imagine that the `pytest-watcher`_ project also has a requirements file_ with ``colorama``, ``docopt``, ``iniconfig``, ``packaging``, ``pluggy``, ``Pygments``, ``pytest`` and ``watchdog`` as programs that it needs to run and they got installed when I asked pip_ to install `pytest-watcher`_ from the ``requirements.txt`` file_

----

=====================================================================================================
how to run the tests automatically with uv and pytest-watcher
=====================================================================================================

----

I try to run the tests again

.. code-block:: PowerShell
  :emphasize-lines: 1

  pytest-watcher

and it shows results without going back to the command line

.. code-block:: PowerShell
  :emphasize-lines: 6

  ================== test session starts===================
  ...
  rootdir: .../magic
  collected 1 item

  tests/test_magic.py .                              [100%]

  =============== 1 passed in X.YZs =======================

----

=====================================================================================================
how to open the test file in the editor from the terminal on Windows without WSL
=====================================================================================================

----

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_magic.py`` to place the cursor in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` on line 7

  .. code-block:: PowerShell
    :lineno-start: 7
    :emphasize-lines: 1

          self.assertFalse(True)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: PowerShell
    :emphasize-lines: 10

    ============================ FAILURES ==============================
    __________________________ TestMagic.test_failure ___________________________

    self = <tests.test_magic.TestMagic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic.py:7: AssertionError
    ===================== short test summary info ========================
    FAILED tests/test_magic.py::TestMagic::test_failure - AssertionError: True is not false
    ======================= 1 failed in X.YZs ==========================

  I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_magic.py:7`` to place the cursor in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then I change :ref:`True<test_what_is_true>` back to :ref:`False<test_what_is_false>` in ``test_magic.py``

  .. code-block:: PowerShell
    :lineno-start: 7
    :emphasize-lines: 1

          self.assertFalse(False)

  the test passes and I can write the rest of the code for the project as the tests run automatically in response to any change I make

----

=====================================================================================================
how to stop the automated tests on Windows without WSL
=====================================================================================================

----

I exit the tests in the terminal_ with :kbd:`ctrl+c` on the keyboard

----

=====================================================================================================
how to deactivate a virtual environment on Windows without WSL
=====================================================================================================

----

* I leave the `virtual environment`_ by typing this in the terminal_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: PowerShell

    ...\pumping_python\magic

* I try `pytest-watcher`_ again to show that I do not have it installed outside the `virtual environment`_

  .. code-block:: PowerShell
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: PowerShell

    command not found: pytest-watcher

* I `change directory`_ to the parent of ``magic``

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd ..

  ``..`` is shorthand for the parent of any directory_ you are in. The terminal_ shows

  .. code-block:: PowerShell

    ...\pumping_python >

  I am back in the ``pumping_python`` folder_

----

********************************************************************************************
review
********************************************************************************************

I gave the computer some commands to make a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>`. I made some folders_ and files_, successfully wrote a :ref:`failing test<test_failure>`, made it pass, then made the tests run automatically

----

============================================================================================
how to view all the commands typed in a terminal on Windows without WSL
============================================================================================

----

* I type history_ in the terminal_ to see all the commands I have typed so far

  .. code-block:: PowerShell
    :emphasize-lines: 1

    history

  the terminal_ shows

  .. code-block:: PowerShell
    :emphasize-lines: 6, 8, 10, 13, 19, 22, 29, 32, 37, 39-40, 44

    cd pumping_python
    mkdir pumping_python
    cd pumping_python
    tree /F
    cd magic
    mkdir magic
    tree /F
    cd magic
    python src/magic.py
    mkdir src
    tree /F
    python src/magic.py
    New-Item src/magic.py
    tree /F
    python src/magic.py
    python -m unittest
    mkdir tests
    tree /F
    New-Item tests/magic.py
    tree /F
    python -m unittest
    New-Item tests/__init__.py
    tree /F
    python -m unittest
    mv tests/magic.py tests/test_magic.py
    tree /F
    python -m unittest
    pytest-watcher
    python -m venv .venv
    tree /F
    tree /F
    .venv/scripts/activate.ps1
    pytest-watcher
    pip list
    echo "pytest-watcher"
    echo "pytest-watcher" > requirements.txt
    "pytest-watcher" | Out-File requirements.txt -Encoding UTF8
    tree /F
    python -m pip install --requirement requirements.txt
    python -m pip install --upgrade pip
    pip list
    pytest-watcher
    deactivate
    pytest-watcher
    cd ..
    New-Item makePythonTdd.ps1
    tree /F

  the `history program`_ shows all the commands I typed in the terminal_ so far, and I use them to write the program_ that will automatically make a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for me

* these are the commands I used to help make a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>`

  .. code-block:: shell

    mkdir NAME_OF_THE_PROJECT
    cd NAME_OF_THE_PROJECT
    mkdir src
    New-Item src/NAME_OF_THE_PROJECT.py
    mkdir tests
    New-Item tests/__init__.py
    New-Item tests/test_NAME_OF_THE_PROJECT.py
    python3 -m venv .venv
    source .venv/bin/activate
    echo "pytest-watcher" > requirements.txt
    python3 -m pip install --upgrade pip
    python3 -m pip install --requirement requirements.txt
    pytest-watcher

  where ``NAME_OF_THE_PROJECT`` is the name I give the project

* these are the steps I took to make a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>`

  - give the project a name
  - :ref:`make a directory for the project<how to make a directory for the project on Windows without WSL>`
  - :ref:`change directory to the project<how to change directory to the project on Windows without WSL>`
  - :ref:`make a directory for the source code<how to make a directory for the source code on Windows without WSL>`
  - :ref:`make a Python file to hold the source code in the 'src' folder<how to make an empty file on Windows without Windows Subsystem for Linux>`
  - :ref:`make a directory for the tests<how to make a directory for the tests on Windows without WSL>`
  - :ref:`make the 'tests' folder a Python package<how to make the tests a Python package on Windows without WSL>`
  - :ref:`make a Python file to hold the tests in the 'tests' folder on Windows without WSL<how to make a Python file for the tests in the 'tests' directory on Windows without WSL>`
  - :ref:`add the first failing test to the test file<test_failure on Windows without WSL>`
  - :ref:`make a virtual environment<how to make a virtual environment on Windows without WSL>`
  - :ref:`activate the virtual environment<how to activate a virtual environment on Windows without WSL>`
  - :ref:`upgrade the Python package manager<how to upgrade the Python package manager in a virtual environment on Windows without WSL>`
  - :ref:`make a requirements file for the needed Python packages<how to write text to a file on Windows without Windows Subsystem for Linux>`
  - :ref:`install the packages listed in the requirements file_<how to install Python packages with uv on Windows without WSL>`
  - :ref:`run the tests automatically<how to run the tests automatically on Windows without Windows Subsystem for Linux>`
  - :ref:`open the test file in the editor from the terminal<how to open the test file in the editor from the terminal on Windows without WSL>`
  - make the test pass

----

:ref:`How many questions can you answer after going through this chapter?<questions about making a Python Test Driven Development Environment>`

----

************************************************************************************************
what is next?
************************************************************************************************

You have seen me make a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for a project called ``magic`` on any Windows_ computer that does NOT have `Windows Subsystem for Linux`_. :ref:`Would you like to test AssertionError next?<what causes AssertionError?>`

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