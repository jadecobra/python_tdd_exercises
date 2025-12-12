.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watch for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

#################################################################################
how to make a python test driven development environment
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

This is one way to make a Python_ `Test Driven Development`_ project. First, :ref:`I do it manually<how to manually make a python test driven development environment>`, where I make all the `folders (directories)`_ and files_ for the environment, including setting up :ref:`the first test<test_failure>`, then :ref:`I write a program to do it for me<how to automatically make a python test driven development environment>`

*********************************************************************************
preview
*********************************************************************************

Here is the program_ I have by the end of the chapter to :ref:`automatically make a python test driven development environment <how to automatically make a python test driven development environment>`, it is only 28 lines of code, with spaces

.. literalinclude:: ../../code/make_tdd/makePythonTdd.sh
  :language: shell
  :linenos:

*********************************************************************************
questions about making a Python Test Driven Development Environment
*********************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`what is a Test Driven Development Environment?`
* :ref:`How can I make a Python Test Driven Development Environment manually?<how to manually make a python test driven development environment>`
* :ref:`How can I make a Python Test Driven Development Environment automatically?<how to automatically make a python test driven development environment>`
* :ref:`How can I change directories?<how to change directory>`
* :ref:`How can I make a directory?<how to make a directory>`
* :ref:`How can I see directory structure?<how to look at directory structure>`
* :ref:`How can I make an empty file?<how to make an empty file>`
* :ref:`How can I write text to a file?<how to write text to a file>`
* :ref:`How can I see what is inside a file?<how to see what is inside a file>`
* :ref:`How can I change the name of a file?<how to change the name of a file>`
* :ref:`How can I run a Python Program?<how to run a Python program>`
* :ref:`How can I test for failure?<test_failure>`
* :ref:`How can I make a Python package?<how to make a Python package>`
* :ref:`How can I run tests manually?<how to manually run tests>`
* :ref:`How can I run tests automatically?<how to automatically run tests>`
* :ref:`How can I stop automated Python tests from running?<how to exit the automated tests>`
* :ref:`What is a Virtual Environment?<what is a virtual environment?>`
* :ref:`How can I make a Virtual Environment?<how to make a virtual environment>`
* :ref:`How can I activate a Virtual Environment?<how to activate a virtual environment>`
* :ref:`How can I deactivate a Virtual Environment?<how to deactivate a virtual environment>`
* :ref:`How can I document the Python programs my project needs?<how to write text to a file>`
* :ref:`How can I install the Python programs my project needs from a file?<how to install Python packages in a virtual environment>`
* :ref:`How can I install Python packages in a Virtual Environment?<how to install Python packages in a virtual environment>`
* :ref:`How can I see what Python packages are installed in a Virtual Environment?<how to see what packages are installed in a virtual environment>`
* :ref:`How can I view all the commands I type in a terminal?<how to view all the commands I typed in a terminal>`
* :ref:`How can I make a shell script?<how to make a shell script>`
* :ref:`What is a variable?<how to use a variable in a shell script>`
* :ref:`How can I use a variable in a shell script<how to use a variable in a shell script>`
* :ref:`How can I view the permissions of a file?<how to view the permissions of a file>`
* :ref:`How can I make a shell script run as a command<how to make a shell script run as a command>`
* :ref:`How can I run a shell script<how to run a shell script>`

----

*********************************************************************************
requirements
*********************************************************************************

* `download and install Python <https://www.python.org/downloads/>`_
* get an `Integrated Development Environment (IDE)`_. Here are a few options

  - `Visual Studio Code`_

    - If you are on MacOS_ and using `Visual Studio Code`_, `Configure the path <https://code.visualstudio.com/docs/setup/mac#_configure-the-path-with-vs-code>`_ so you can open `Visual Studio Code`_ from the command line later

  - `Sublime Text`_
  - PyCharm_
  - `other Integrated Development Environment (IDE) options`_

=================================================================================
Windows requirements
=================================================================================


* If you are using a Windows_ computer, :ref:`install Windows Subsystem for Linux<how to install Windows Subsystem for Linux on Windows>`
* If you cannot :ref:`install Windows Subsystem for Linux<how to install Windows Subsystem for Linux on Windows>`, you can :ref:`make a Python Test Driven Development Environment on Windows without Windows Subsystem for Linux<how to make a python test driven development environment on Windows without Windows Subsystem for Linux>` instead of this chapter

=================================================================================
Linux/Windows Subsystem for Linux requirements
=================================================================================

.. ATTENTION:: Do this only if you are using Linux_ or `Windows Subsystem for Linux`_. MacOS_ users should not do this section

* Open a terminal_ then type this to update the `Linux package manager`_

  .. code-block:: shell
    :emphasize-lines: 1

    sudo apt update

  .. TIP:: you can do a full upgrade if you want

  .. code-block:: shell

    sudo apt full-upgrade --yes

* type this in the terminal_ to install Python_

  .. code-block:: shell
    :emphasize-lines: 1

    sudo apt install python3 python3-venv --yes

----

********************************************************************************************
how to manually make a python test driven development environment
********************************************************************************************

I pick ``magic`` as the name for this project

* I open ``Terminal`` in the menu bar at the top of the `Integrated Development Environment (IDE)`_, then click ``New Terminal`` to open a terminal_

* I `change directory`_ to where I will put all the projects from this book. I type cd_ in the terminal_

  .. NOTE:: You can skip this step if you are already in the ``pumping_python`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    cd pumping_python

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: pumping_python

  the `folder (directory)`_ does NOT exist. I need to make it

* I use the `mkdir program`_ to make the ``pumping_python`` `folder (directory)`_

  .. code-block:: shell

    mkdir pumping_python

  the terminal_ goes back to the command line

* I try `changing directory`_ again

  .. code-block:: shell
    :emphasize-lines: 1

    cd pumping_python

  the terminal_ shows I am now in the ``pumping_python`` `folder (directory)`_

  .. code-block:: shell

    .../pumping_python $

* I type tree_ in the terminal_ to see what files_ and folders_ are in the ``pumping_python`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  when tree_ is not installed on the computer, the terminal_ shows

  .. code-block:: shell

    tree: command not found

  I need to install tree_ to use it

  .. admonition:: if you are using MacOS_ type this in the terminal_

    first install brew_ (The Missing Package Manager for MacOS), if you do not have it already

    .. code-block:: shell
      :emphasize-lines: 1

      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    then use brew_ to install tree_

    .. code-block:: shell
      :emphasize-lines: 1

      brew install tree

  or

  .. admonition:: if you are using Linux_ or `Windows Subsystem for Linux`_ type this in the terminal_

    .. code-block:: shell
      :emphasize-lines: 1

      sudo apt install tree --yes

  after the computer installs tree_, I run the command again

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  when tree_ is installed on the computer, the terminal_ shows

  .. code-block:: shell

    .

    0 directories, 0 files

  .. NOTE:: You will see more files_ and folders_ if you have done other work in the ``pumping_python`` folder_

* I `change directory`_ to the ``magic`` project in the ``pumping_python`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd magic

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: magic

  the ``magic`` folder does NOT exist yet

* I make the ``magic`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir magic

  this makes a `folder (directory)`_ for the project where its files_ will stay

* I use tree_ again

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2

    .
    └── magic

* I try cd_ again

  .. code-block:: shell
    :emphasize-lines: 1

    cd magic

  the terminal_ shows I am now in the ``magic`` folder_ I just made in the ``pumping_python`` folder

  .. code-block:: shell

    .../pumping_python/magic

=================================================================================
how to run a Python program
=================================================================================

* I use Python_ to run the ``magic`` program_

  .. code-block:: shell
    :emphasize-lines: 1

    python3 src/magic.py

  the terminal_ shows

  .. code-block:: text

    python3: can't open file '.../pumping_python/magic/src/magic.py': [Errno 2] No such file or directory

  the computer cannot find the program_ because it does not exist, yet

* I make a child folder_ in the ``magic`` directory_ for the program_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line

* I use tree_ to see what changed in the ``magic`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2

    .
    └── src

* I try to run the ``magic`` program_ again

  .. code-block:: shell
    :emphasize-lines: 1

    python3 src/magic.py

  the terminal_ shows the same error from before. I have to make the file_

=================================================================================
how to make an empty file
=================================================================================

* I use touch_ to make an empty file_ in the ``src`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    touch src/magic.py

  the terminal_ goes back to the command line

* I use tree_ to see what folders_ and files_ I now have

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 3

    .
    └── src
        └── magic.py

  touch_ is a program_ that makes an empty file_ with the name. I can give it the directory_ I want to put the file_ in as part of the name, in this case ``touch src/magic.py`` makes a file named ``magic.py`` in the ``src`` folder_

* I try to run the ``magic`` program_ again

  .. code-block:: shell
    :emphasize-lines: 1

    python3 src/magic.py

  the terminal_ goes back to the command line. Success! Even though ``magic.py`` does not do anything because there is no code in it, I can successfully run it because it exists.

********************************************************************************************
test_failure
********************************************************************************************

=================================================================================
how to manually run tests
=================================================================================

* I use the unittest_ :ref:`module<ModuleNotFoundError>` from the `Python standard library`_ that comes with Python_ to run tests. I type this in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ shows

  .. code-block:: shell

    ----------------------------------------------------------------------
    Ran 0 tests in 0.000s

    NO TESTS RAN

  - ``python3`` is the `Python program`_
  - ``-m`` is an option/switch passed when calling Python_ to run the :ref:`module<ModuleNotFoundError>` - unittest_ in this case
  - a Python_ :ref:`module<ModuleNotFoundError>` is any file_ that ends with ``.py``, this means somewhere on the computer there is a file_ named ``unittest.py``, `see the source code for unittest here`_

* I do not have any tests yet, so there is nothing to run. I make a child folder_ to keep the tests separate from the actual program_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line

* I use tree_ to see what my project looks like

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4

    .
    ├── src
    │   └── magic.py
    └── tests

* I use touch_ to add an empty file_ to the ``tests`` directory_ for the actual test

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/magic.py

  the terminal_ goes back to the command line

* I use tree_ to see what the project looks like so far

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 5

    .
    ├── src
    │   └── magic.py
    └── tests
        └── magic.py

* I run the test again

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ shows

  .. code-block:: shell

    NO TESTS RAN

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I open ``tests/magic.py`` with the `Integrated Development Environment (IDE)`_ to open it in the :ref:`editor<2 editors>`

  .. TIP:: I can open a file_ from the terminal_ in `Visual Studio Code`_ by typing ``code`` and the name of the file_, for example

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/magic.py

    I can also open a file_ by using ``ctrl`` (Windows_/Linux_) or ``command`` (MacOS_) on the keyboard and clicking with the mouse on the name of the file_

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

  - ``import unittest`` imports the unittest_ :ref:`module<ModuleNotFoundError>` from the `Python standard library`_, this is what I am using for testing
  - ``class TestMagic``

    * ``class`` is the Python_ keyword for making :ref:`classes` - a group of :ref:`attributes (values)<AttributeError>` and :ref:`methods (functions)<functions>` that belong together, I cover this in more detail in the :ref:`classes chapter<classes>`
    * ``TestMagic`` is the name I gave this :ref:`class <classes>` and will hold the test

      .. IMPORTANT:: I can use any name for the test :ref:`class<classes>`, it MUST start with ``Test`` or unittest_ will NOT run the tests in it

    * `unittest.TestCase`_ is a :ref:`class <classes>` from the unittest_ :ref:`module<ModuleNotFoundError>` that has :ref:`methods<functions>` for testing
    * ``class TestMagic(unittest.TestCase)`` defines ``TestMagic`` as a "child" of `unittest.TestCase`_ which means I can use its :ref:`methods<functions>` and :ref:`attributes<AttributeError>`

  - ``def test_failure``

    * def_ is the Python_ keyword for making :ref:`methods (functions) <functions>`, see :ref:`functions` for more
    * ``test_failure`` is the name I used :ref:`method<functions>` for :ref:`this first test<test_failure>`

      .. IMPORTANT:: I can use any name for the test :ref:`method<functions>`, it MUST start with ``test_`` or unittest_ will NOT run the tests in it

    * ``self.`` lets me use :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of the ``TestMagic`` :ref:`class<classes>` which is a "child" of the `unittest.TestCase class`_, instead of using ``TestMagic().`` or ``unittest.TestCase().``

      .. IMPORTANT:: the name ``self`` is Python_ convention. I can use any name but it is easier to stick with convention for this concept

    * ``self.assertFalse(True)`` is an :ref:`assertion<AssertionError>`

      - assertFalse_ is a :ref:`method<functions>` in the `unittest.TestCase`_ :ref:`class <classes>` that checks if its input is :ref:`False<test_what_is_false>`
      - :ref:`True<test_what_is_true>` is given as the input

      I expect this line to fail because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`. If it does not fail, then Python_ and I have a problem

* I turn on the ``Auto Save`` feature in the `Integrated Development Environment (IDE)`_ to automatically save files when I make a change so that `I do not repeat myself`_ by hitting save (``ctrl+s`` (Windows/Linux) or ``command+s`` (mac)) every time I make a change

  .. ATTENTION:: Turn on the ``Auto Save`` feature in your `Integrated Development Environment (IDE)`_

* I try the command again to run the tests in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ shows

  .. code-block:: shell

    NO TESTS RAN

  I need to tell Python_ that the ``tests`` folder is a `Python package`_, so it can find the tests

--------------------------------------------------------------------------------------------
how to make a Python package
--------------------------------------------------------------------------------------------

* I use touch_ to add an empty file with the name ``__init__.py`` in the ``tests`` folder

  .. ATTENTION:: make sure to use 2 underscores (__) before and after ``init`` for ``__init__.py``

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/__init__.py

  the terminal_ goes back to the command line

* I run the tree_ command to see what changed

  .. code-block:: shell
    :emphasize-lines: 1

    tree

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

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ shows

  .. code-block:: shell

    NO TESTS RAN

  I need to tell Python_ that ``magic.py`` in the ``tests`` folder is a test file

* I close ``magic.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. CAUTION:: if you do not close ``magic.py`` you will end up with 3 files in the ``tests`` folder after the next step (instead of 2), because the ``Auto Save`` feature (enabled earlier) will save the original file after you change its name

--------------------------------------------------------------------------------------------
how to change the name of a file
--------------------------------------------------------------------------------------------

* I use the `mv program`_ to change the name of ``magic.py`` in the ``tests`` folder_ to ``test_magic.py``

  .. code-block:: shell
    :emphasize-lines: 1

    mv tests/magic.py tests/test_magic.py

  the terminal_ goes back to the command line

* I use tree_ with the ``-L`` option to see what I have so far

  .. code-block:: shell
    :emphasize-lines: 1

    tree -L 2

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

  the ``-L`` option tells tree_ how deep to go when showing the folders_ and files_, I use ``2`` to make it show only the first level of contents of the child folders_

* I run the tests again

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ shows :ref:`AssertionError`

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

  .. IMPORTANT:: I can use any name for the test file but it must start with ``test_`` or unittest_ will NOT run the tests in the file

* This is the ``RED`` part of the `Test Driven Development`_ cycle. The message in the terminal_ is about the failure, I like to read these from the bottom up, here is an explanation of each line, starting from the last line on the screen

  - ``FAILED (failures=1)`` the number of failures
  - ``Ran 1 test in A.XYZs`` the number of tests it ran and how long they took
  - ``AssertionError: True is not false`` the :ref:`Error (Exception)<errors>` that happened and its message, in this case :ref:`AssertionError` because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`
  - ``self.assertFalse(True)`` the line of code that caused :ref:`AssertionError`
  - ``~~~~~~~~~~~~~~~~^^^^^^`` points to the part of the line above that Python_ thinks caused the :ref:`error<errors>`
  - ``File ".../magic/tests/test_magic.py", line 7, in test_failure`` the line number of the code that caused the :ref:`error<errors>` and the location of the file where it is
  - ``Traceback (most recent call last):`` all the information shown after this line that is indented to the right shows the calls that led to the failure, this is why I like to read it from the bottom up
  - ``FAIL: test_failure (tests.test_magic.TestMagic.test_failure)`` is a header with information in :ref:`dot notation` about the failing test :ref:`method<functions>`

    - ``tests.test_magic.TestMagic.test_failure`` is the location of the failing test
    -  ``tests`` is the ``tests`` folder_
    -  ``test_magic`` is the ``test_magic.py`` file_ in the ``tests`` directory_
    - ``TestMagic`` is the :ref:`class <classes>` defined on line 4 in ``test_magic.py``
    - ``test_failure`` is the :ref:`method (function)<functions>` defined on line 6 in ``test_magic.py``

  * ``F`` shows a failure

* I hold ``ctrl`` (Windows_/Linux_) or (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``File ".../pumping_python/magic/tests/test_magic.py", line 7`` in the terminal_, and the `Integrated Development Environment (IDE)`_ opens the file_ in the :ref:`editor<2 editors>` with the cursor at the line where the failure happened

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` on line 7 of ``test_magic.py`` in the :ref:`editor<2 editors>`

.. code-block:: shell
  :lineno-start: 7
  :emphasize-lines: 1

          self.assertFalse(False)

I run the test again in the terminal_

.. code-block:: shell
  :emphasize-lines: 1

  python3 -m unittest

the test passes! The terminal_ shows

.. code-block:: none

  .
  ------------------------------------------------------
  Ran 1 test in A.XYZs

  OK

*cue CELEBRATION MUSIC AND DANCE!* I am GREEN!!


=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

Keep a list of :ref:`Errors/Exceptions<errors>` that show up in the terminal_ as you go through this book to know them better, it helps when you run into them later. I add a list with :ref:`AssertionError` in ``test_magic.py`` in the :ref:`editor<2 editors>`

.. code-block:: python
  :linenos:
  :emphasize-lines: 10-11

  import unittest


  class TestMagic(unittest.TestCase):

      def test_failure(self):
          self.assertFalse(True)


  # Exceptions Encountered
  # AssertionError

I ran ``python3 -m unittest`` a few times to see the test fail, I ran ``python3 -m unittest`` again to see the test pass. I will have to run ``python3 -m unittest`` again when I add any code, to make sure tests that were passing do not start failing and that the new code I add does what I want.

This means I have to run ``python3 -m unittest`` for each part of the `Test Driven Development`_ cycle or any time there is a code change.

I do not want to type ``python3 -m unittest`` again, it is better for a `computer program`_ to run the tests so that `I do not repeat myself`_.

----

********************************************************************************************
how to automatically run tests
********************************************************************************************

I can use `pytest-watch`_ to run tests automatically. It is a `Python program`_ that automatically runs pytest_ any time a Python_ file_ changes in the folder_ it is looking at, this means it will run the tests for me every time I make a change.

pytest_ is a `Python package`_ like unittest_, it is not first_inputart of the `Python standard library`_

I type it in the terminal_

.. code-block:: shell
  :emphasize-lines: 1

  pytest-watch

the terminal_ shows

.. code-block:: shell

  command not found: pytest-watch

I need to install `pytest-watch`_ for the computer to use it. Next, I set up a `virtual environment`_ to keep programs_ my project needs in one place

=================================================================================
how to make a virtual environment
=================================================================================

I can install `pytest-watch`_ globally (for the entire computer), which means it will always be available to any project on the computer, but a better way would be to put it in a `virtual environment`_ so that it is installed only for this project.

---------------------------------------------------------------------------------
what is a virtual environment?
---------------------------------------------------------------------------------

A `virtual environment`_ is a separate folder_ where I can install `Python packages`_ that my project needs. This helps me keep things that belong to the project in one place, separate from other things on the computer.

It means I can have a separate `virtual environment`_ for every project with only the programs_ that the project needs. This helps if I decide to package the program_ to send to someone else, because everything needed by the project is in one place.

* I make a `virtual environment`_ with the venv_ :ref:`module<ModuleNotFoundError>` from the `Python standard library`_

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m venv .venv

  the terminal_ goes back to the command line

  - ``python3`` is the `Python program`_
  - ``-m`` is an option passed to Python_ to run the :ref:`module<ModuleNotFoundError>` given after the option
  - venv_ is a :ref:`module<ModuleNotFoundError>` from the `Python standard library`_, it is used to make a `virtual environment`_ with a given name
  - ``.venv`` is the name I am giving for this `virtual environment`_

    .. IMPORTANT:: ``.venv`` is Python_ convention, I can use any name I want for the virtual environment

* I run tree_

  .. code-block:: shell
    :emphasize-lines: 1

    tree -L 2

  the terminal_ shows

  .. code-block:: shell

    .
    ├── src
    │   └── magic.py
    └── tests
        ├── __init__.py
        ├── __pycache__
        └── test_magic.py

  it does not look like anything changed. This is because the ``.`` in front of ``.venv`` means the folder_ is hidden

* I try tree_ again with another option to see what changed

  .. code-block:: shell
    :emphasize-lines: 1

    tree -a -L 2

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

  - the ``-a`` option makes tree_ show all files that are listed including hidden files_ and folders_
  - the ``-L`` option tells tree_ how deep to go when showing the folders_ and files_, I use ``2`` to keep it to the first level of what is in the children folders_ of ``magic``

=================================================================================
how to activate a virtual environment
=================================================================================

* When I want to work in a `virtual environment`_, I make sure I am in the parent directory_ of it, for example, ``magic`` in this case. I activate the `virtual environment`_ in the terminal_ to use it

  .. code-block:: shell
    :emphasize-lines: 1

    source .venv/bin/activate

  the terminal_ shows

  .. code-block:: shell

    (.venv) .../magic $

  the ``(.venv)`` on the far left of the command line in the terminal_ shows that I am in the `virtual environment`_

* I run `pytest-watch`_ again

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: shell

    command not found: pytest-watch

  I have to install `pytest-watch`_ in the `virtual environment`_ to use it in the `virtual environment`_

--------------------------------------------------------------------------------------------
how to see what packages are installed in a virtual environment
--------------------------------------------------------------------------------------------

I use the `Python package manager (pip)`_ to see what `Python packages`_ are installed in the `virtual environment`_ I just made

.. code-block:: shell
  :emphasize-lines: 1

  pip list

the terminal_ shows

.. code-block:: shell

  Package Version
  ------- -------
  pip     x.y

- `pytest-watch`_ is not in the list
- pip_ is a :ref:`module<ModuleNotFoundError>` from the `Python standard library`_, it is used to install `Python packages`_

--------------------------------------------------------------------------------------------
how to write text to a file
--------------------------------------------------------------------------------------------
I want to make a file where I can list all the `Python packages`_ for my project as a way to document it and have pip_ install the programs_ listed in the file_

* I can write text to a file_ with the `echo program`_, it shows whatever it is given as an argument, on the screen (`standard output (stdout)`_) for example

  .. code-block:: shell
    :emphasize-lines: 1

    echo "pytest-watch"

  the terminal_ shows

  .. code-block:: shell

    pytest-watch

* I can also use echo_ to add text to a file_, I use it to make the requirements file_ with `pytest-watch`_ as what is inside it

  .. code-block:: shell
    :emphasize-lines: 1

    echo "pytest-watch" > requirements.txt

  - ``>`` is an operator that is used to send output from a program_ to the given file_
  - `pytest-watch`_ is a `Python program`_ that automatically runs pytest_ when a Python_ file_ in the folder_ changes
  - pytest_ is a `Python package`_ like unittest_, that is used for testing
  - ``requirements.txt`` is the name of a file_ where I can list `Python packages`_ for pip_ to install. The name ``requirements.txt`` is Python_ convention, I can use any name I want for the requirements file

* I run tree_ to see what the project looks like now

  .. code-block:: shell
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ shows

  .. code-block:: shell
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

--------------------------------------------------------------------------------------------
how to see what is inside a file
--------------------------------------------------------------------------------------------

I can use the `cat program`_ to see what is inside a file_. I use it to make sure my ``requirements.txt`` has ``pytest-watch`` inside it

.. code-block:: shell
  :emphasize-lines: 1

  cat requirements.txt

the terminal_ shows

.. code-block:: shell

  pytest-watch

life is good!

--------------------------------------------------------------------------------------------
how to install Python packages in a virtual environment
--------------------------------------------------------------------------------------------

* I use pip_ to install `pytest-watch`_ from the requirements file

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m pip install --requirement requirements.txt

  - ``--requirement`` is an option that can be given to the ``install`` argument for `Python packages`_ in a given file_
  - ``requirements.txt`` is the name of the given file_

  the terminal_ shows programs_ being downloaded and installed, and when I do not have the latest version of pip_ installed, it shows this at the end

  .. code-block:: shell

    [notice] A new release of pip is available: XY.Z -> AB.C
    [notice] To update, run: pip install --upgrade pip

* I upgrade pip_ to the latest version. I recommend you do this every time you are in a `virtual environment`_, it is good practice to update package managers to the latest version available

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m pip install --upgrade pip

  - ``install`` is an argument given to pip_ to install a given `Python package`_
  - ``--upgrade`` is an option that can be passed to the ``install`` argument, like ``--requirement`` from earlier, this one tells pip_ to upgrade the version of the given `Python package`_
  - ``pip`` is the Python_ package I am giving pip_ to install, in this case it upgrades itself to the latest version since I did not give a version number

  .. NOTE:: I can also tell pip_ to install `pytest-watch`_ directly without using a requirements file, the problem is it will not document what programs_ my project needs. I would either have to remember later or use ``pip list``. It also does not help someone else who is trying to run my project later, know what programs it needs without me

    .. code-block:: shell

      python3 -m pip install pytest-watch

* I check what `Python packages`_ are now installed in the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    pip list

  the terminal_ shows

  .. code-block:: shell

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

  .. TIP:: imagine that the `pytest-watch`_ project also has a requirements file_ with ``colorama``, ``docopt``, ``iniconfig``, ``packaging``, ``pluggy``, ``Pygments``, ``pytest`` and ``watchdog`` as programs that it needs to run and they got installed when I asked pip_ to install `pytest-watch`_ from the ``requirements.txt`` file_

* I try to run the tests again

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

  and it shows results without going back to the command line

  .. code-block:: shell
    :emphasize-lines: 6

    ================== test session starts===================
    ...
    rootdir: .../magic
    collected 1 item

    tests/test_magic.py .                              [100%]

    =============== 1 passed in X.YZs =======================

* I hold ``ctrl`` (Windows_/Linux_) or (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and click on ``tests/test_magic.py`` to place the cursor in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` on line 7

  .. code-block:: shell
    :lineno-start: 7
    :emphasize-lines: 1

          self.assertFalse(True)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell
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

  I hold ``ctrl`` (Windows_/Linux_) or (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and click on ``tests/test_magic.py:7`` to place the cursor in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then I change :ref:`True<test_what_is_true>` back to :ref:`False<test_what_is_false>` in ``test_magic.py``

  .. code-block:: shell
    :lineno-start: 7
    :emphasize-lines: 1

          self.assertFalse(False)

  the test passes and I can write the rest of the code for the project as the tests run automatically in response to any change I make

=================================================================================
how to exit the automated tests
=================================================================================

I exit the tests in the terminal_ by pressing ``ctrl+c`` on the keyboard

=================================================================================
how to deactivate a virtual environment
=================================================================================

* I leave the `virtual environment`_ by typing this in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

* I try `pytest-watch`_ again to show that I do not have it installed outside the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: shell

    command not found: pytest-watch

* I `change directory`_ to the parent of ``magic``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  ``..`` is shorthand for the parent of any directory_ you are in. The terminal_ shows

  .. code-block:: shell

    .../pumping_python $

  I am back in the ``pumping_python`` folder_

----

********************************************************************************************
how to automatically make a python test driven development environment
********************************************************************************************

You made it this far and have become `the greatest programmer in the world`_. To follow `The Do Not Repeat Yourself (DRY) Principle`_, I write a program_ that has all the commands it took to get here, then I can use that program_ to make a `Test Driven Development`_ Environment anytime I want and not have to remember every step of the process

=================================================================================
how to make a shell script
=================================================================================

* I use touch_ to make an empty file_ with a name that is easy to remember later and describes the program_ that will automatically make a `Test Driven Development`_ environment for me

  .. code-block:: shell
    :emphasize-lines: 1

    touch makePythonTdd.sh

  the terminal_ goes back to the command line

* I use tree_ to see what is in the ``pumping_python`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ shows my new file_ is in the same parent directory_ of the ``magic`` project

  .. code-block:: shell
    :emphasize-lines: 8

    .
    ├── magic
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    └── makePythonTdd.sh

--------------------------------------------------------------------------------------------
how to view all the commands I typed in a terminal
--------------------------------------------------------------------------------------------

* I type history_ in the terminal_ to see all the commands I have typed so far

  .. code-block:: shell
    :emphasize-lines: 1

    history

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 8, 10, 12, 15, 19, 21, 24, 31, 34, 38, 41, 42, 44

    cd pumping_python
    mkdir pumping_python
    cd pumping_python
    tree
    sudo apt install tree --yes
    tree
    cd magic
    mkdir magic
    tree
    cd magic
    python3 src/magic.py
    mkdir src
    tree
    python3 src/magic.py
    touch src/magic.py
    tree
    python3 src/magic.py
    python3 -m unittest
    mkdir tests
    tree
    touch tests/magic.py
    tree
    python3 -m unittest
    touch tests/__init__.py
    tree
    python3 -m unittest
    mv tests/magic.py tests/test_magic.py
    tree -L 2
    python3 -m unittest
    pytest-watch
    python3 -m venv .venv
    tree
    tree -a -L 2
    source .venv/bin/activate
    pytest-watch
    pip list
    echo "pytest-watch"
    echo "pytest-watch" > requirements.txt
    tree -a -L 2
    cat requirements.txt
    python3 -m pip install --requirement requirements.txt
    python3 -m pip install --upgrade pip
    pip list
    pytest-watch
    deactivate
    pytest-watch
    cd ..
    touch makePythonTdd.sh
    tree -a -L 2

  the `history program`_ shows all the commands I typed in the terminal_ so far, and I use them to write the program_ that will automatically make a Python_ `Test Driven Development`_ environment for me

* I open ``makePythonTdd.sh`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then add the commands I used to make the ``magic`` project to the file_

  .. NOTE:: the line numbers below are a guide, you do not need to copy them

  .. code-block:: shell
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

* I change touch_ then use echo_ to add text for the first failing test to ``test_magic.py`` in ``makePythonTdd.sh``

  .. code-block:: shell
    :lineno-start: 8
    :emphasize-lines: 1

    echo "" > tests/test_magic.py

* I add the text for the test like I did with ``test_magic.py`` inside the :ref:`quotes ("")<quotes>` I just added to ``makePythonTdd.sh``

  .. CAUTION:: Indentation_ is important in Python_, I use 4 spaces as convention in this book, see the :PEP:`Python Style Guide <8>` for more

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 8-21

    #!/bin/bash
    mkdir magic
    cd magic
    mkdir src
    touch src/magic.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " > tests/test_magic.py

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    echo "pytest-watch" > requirements.txt
    python3 -m pip install --requirement requirements.txt
    pytest-watch

--------------------------------------------------------------------------------------------
how to run a shell script
--------------------------------------------------------------------------------------------

I go back to the terminal_ to run the program_

.. code-block:: shell
  :emphasize-lines: 1

  makePythonTdd.sh

the terminal_ shows

.. code-block:: shell

  command not found: makePythonTdd.sh

I have to tell the computer where the file_ is

.. code-block:: shell
  :emphasize-lines: 1

  ./makePythonTdd.sh

``./`` is shorthand for ``this directory`` which in this case is ``pumping_python`` where ``makePythonTdd.sh`` is saved. The computer checks a few directories_ when a command is given. Those directories are where commands like mkdir_, cd_, tree_ and echo_ are saved. The terminal_ shows

.. code-block:: shell

  permission denied: ./makePythonTdd.sh

I want to make sure the computer can run the program_. I have to make it executable

--------------------------------------------------------------------------------------------
how to view the permissions of a file
--------------------------------------------------------------------------------------------

I use ls_ to check the permissions of the file_

.. code-block:: shell
  :emphasize-lines: 1

  ls -l makePythonTdd.sh

``-l`` is the option to show the long listing format which includes permissions for the file_

the terminal_ shows

.. code-block:: shell

  -rw-r--r-- 1 abcdef ghijk XX Month  Y ZA:BC makePythonTdd.sh

here is what each one of the characters before the folder_ means

* ``-`` means this is a regular file_, it is not a directory_
* ``rw-`` means the owner of the file_ can read and write to the file_ but not execute it
* ``r--`` means the group on the computer the owner of the file_ belongs to can only read the file_, they cannot write to it or execute it, and the second
* ``r--`` means other users can only read the file_, they cannot write to it or execute it

I want to add execute permissions so I can run the file

--------------------------------------------------------------------------------------------
how to make a shell script run as a command
--------------------------------------------------------------------------------------------

* I change the mode of the file_ to add executable permissions

  .. code-block:: shell
    :emphasize-lines: 1

    chmod +x makePythonTdd.sh

  chmod_ is a program_ that changes the mode (permissions) of the given file_, the terminal_ goes back to the command line. I use chmod_ to make the file_ executable so the computer can run it

* I list the permissions again with ls_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -l makePythonTdd.sh

  the terminal_ shows

  .. code-block:: shell

    -rwxr-xr-x 1 abcdef ghijk XX Month  Y ZA:BC makePythonTdd.sh

  here is what each one of the characters before the folder_ means

  * ``-`` means this is a regular file_, it is not a directory_
  * ``rwx`` means the owner of the file_ has permissions to read, write to and execute it
  * ``r-x`` means the group the owner of the file_ belongs to has permissions to read and execute the file_ they cannot write to it, and the second
  * ``r-x`` means other users have permissions to read and execute the file_, they cannot write to it

* I try the command again

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 10

    ======================================= FAILURES =======================================
    ________________________________ TestMagic.test_failure ________________________________

    self = <tests.test_magic.TestMagic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_magic.py::TestMagic::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

  Success! I just made a program_ that can make the ``magic`` project anytime I want and it automatically does the steps I did manually.

* I hold ``ctrl`` on the keyboard and click on ``tests/test_magic.py`` to open it in the :ref:`editor<2 editors>` then make the test pass

* I hit ``ctrl+c`` in the terminal_ to stop the test

* I want to use ``makePythonTdd.sh`` to make another project with a different name. I change ``magic`` to the name of the new project in the :ref:`editor<2 editors>`

  .. NOTE:: The lines that are changing in the code are highlighted

  .. code-block::
    :linenos:
    :emphasize-lines: 2, 3, 5, 12, 20

    #!/bin/bash
    mkdir magic_again
    cd magic_again
    mkdir src
    touch src/magic_again.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestMagicAgain(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " > tests/test_magic_again.py

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    echo "pytest-watch" > requirements.txt
    python3 -m pip install --requirement requirements.txt
    pytest-watch

* I run ``makePythonTdd.sh`` in the terminal_ to make a project named ``magic_again``

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell
    :emphasize-lines: 10

    ======================================= FAILURES =======================================
    _____________________________ TestMagicAgain.test_failure ______________________________

    self = <tests.test_magic.TestMagicAgain testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic_again.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_magic_again.py::TestMagicAgain::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

  I make the test pass

* I hit ``ctrl+c`` to exit the tests in the terminal_
* I run tree_ to see what I have in ``pumping_python`` now

  .. code-block:: shell
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ shows

  .. code-block::
    :emphasize-lines: 22-41

    .
    ├── magic
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    ├── magic_again
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    └── makePythonTdd.sh

  the program_ works and can reliably make a Python_ `Test Driven Development`_ environment the way I want it, but there is a problem

--------------------------------------------------------------------------------------------
how to use a variable in a shell script
--------------------------------------------------------------------------------------------

I changed ``magic`` to ``magic_again`` in 4 places in ``makePythonTdd.sh``. I would have to do the same change every time I have a new project, and I want to follow `The Do Not Repeat Yourself (DRY) Principle`_. I want the program_ to take a project name once and use that name when making the project to make the following

- the project folder_
- the file_ for the program_ in the ``src`` folder_
- the file_ for the test in the ``tests`` folder_
- the test :ref:`class<classes>` in the test file_
- the `virtual environment`_ in the ``.venv`` folder_

The program_ should always make this structure

.. code-block:: shell

  PROJECT_NAME
  ├── requirements.txt
  ├── src
  │   └── PROJECT_NAME.py
  ├── tests
  │   ├── __init__.py
  │   └── test_PROJECT_NAME.py
  └── .venv

Time to use a variable_ for the name of the project

* I add a name to represent any project name that I give to ``makePythonTdd.sh`` when I want it to make a project

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 2

    #!/bin/bash
    PROJECT_NAME="magic_again"
    mkdir magic_again
    cd magic_again
    mkdir src
    touch src/magic_again.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestMagicAgain(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " > tests/test_magic_again.py

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    echo "pytest-watch" > requirements.txt
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  a :ref:`variable<test_attribute_error_w_variables>` is a name that is used for a value that can change. For example, we use the word ``woman`` to represent any woman, ``man`` to represent any man, ``child`` to represent any child, and ``parent`` to represent anyone with a child. In this case I use ``$PROJECT_NAME`` to represent any name of a project

* I change every where I have ``magic_again`` in the program, to use the :ref:`variable<test_attribute_error_w_variables>` I just added so that I only have to make a change in one place

  .. NOTE:: The lines that are changing in the code are highlighted

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 3-4, 6, 13, 21

    #!/bin/bash
    PROJECT_NAME="magic_again"
    mkdir $PROJECT_NAME
    cd $PROJECT_NAME
    mkdir src
    touch src/$PROJECT_NAME.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class Test$PROJECT_NAME(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " > tests/test_$PROJECT_NAME.py

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    echo "pytest-watch" > requirements.txt
    python3 -m pip install --requirement requirements.txt
    pytest-watch

* I run the program_ again in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2, 4, 10, 12

    ======================================= FAILURES =======================================
    ____________________________ Testmagic_again.test_failure ______________________________

    self = <tests.test_magic.Testmagic_again testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic_again.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_magic_again.py::Testmagic_again::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in ``tests/test_magic_again.py`` to make the test pass

* I hit ``ctrl+c`` in the terminal to stop the test

* I run tree_ to see what I have in the ``pumping_python`` folder_ now

  .. code-block:: shell
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 8-13

    .
    ├── magic
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    ├── magic_again
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    └── makePythonTdd.sh

* The program_ works as expected, and I only need to give the project name in one place. It would be nice if I do not have to go into the file_ to give it the project name. I want to be able to just call the program_ and give it a name for the project from the command line. I can do this with ``$1`` in bash_, it represents the first argument given when a program_ is called. For example,

  .. code-block:: shell

    command argument

  in the code above, ``command`` will be ``./makePythonTdd.sh`` and ``$1`` will be ``argument`` or whatever name I give.

  Here are a few other examples

  .. code-block:: shell

    mkdir name_of_folder

  ``mkdir`` is the command, and ``$1`` is ``name_of_folder``

  .. code-block:: shell

    touch name_of_file

  ``touch`` is the command, and ``$1`` is ``name_of_file``

  .. code-block:: shell

    echo "anything"

  ``echo`` is the command, and ``$1`` is ``"anything"``

  .. code-block:: shell

    tree -a

  ``tree`` is the command and ``$`` is ``-a``

* I change ``magic_again`` to ``$1`` in ``makePythonTdd.sh``

  .. code-block:: shell
    :lineno-start: 2
    :emphasize-lines: 1

    PROJECT_NAME=$1

* I try the program_ again, this time with a different name for the project in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh more_magic

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 10

    ======================================= FAILURES =======================================
    _____________________________ Testmore_magic.test_failure ______________________________

    self = <tests.test_more_magic.Testmore_magic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_more_magic.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_more_magic.py::Testmore_magic::test_failure - AssertionError: True is not false
    ================================== 1 failed in 0.04s ===================================

* I hold ``ctrl`` on the keyboard in the terminal_ and click on ``tests/test_more_magic.py`` to open it in the :ref:`editor<2 editors>`, then make the test pass

* I use ``ctrl+c`` on the keyboard in the terminal_ to stop the tests

* I run tree_ to see what I have in the ``pumping_python`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 15-20

    .
    ├── magic
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    ├── magic_again
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    ├── makePythonTdd.sh
    └── more_magic
        ├── .pytest_cache
        ├── requirements.txt
        ├── src
        ├── tests
        └── .venv

* I can now make a `Test Driven Development`_ environment with ``makePythonTdd.sh`` when I give it a name for the ``PROJECT_NAME`` variable_. For example, when I type this in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh assertion_error

  the terminal_ shows

  .. code-block:: shell

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

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen a way to make a Python_ `Test Driven Development`_ Environment, and have a :ref:`program<makePythonTdd.sh>` to do it for you on any Linux_, Windows_ or MacOS_ computers.

:ref:`How many questions can you answer after going through this chapter?<questions about making a Python Test Driven Development Environment>`

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