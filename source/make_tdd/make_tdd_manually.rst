.. meta::
  :description: Build your first Python TDD project by hand with uv, the terminal, and unittest. Jacob Itegboje walks through pumping_python folder setup, uv init person, mkdir src and tests, mv main.py to src/person.py, touch tests/__init__.py, rename tests/person.py to test_person.py, and the first RED test with assert False is True raising AssertionError (FAILED errors=1, NO TESTS RAN until test_ prefix and package). Learn cd, mkdir, tree, cat, mv, touch, python3 -m unittest discovery, module-level assert gotchas, and why passing tests still show NO TESTS RAN before pytest-watcher. Pumping Python manual TDD environment chapter 1.
  :keywords: Jacob Itegboje, Pumping Python, manual python tdd setup, uv init project, python unittest first test, assert False is True AssertionError, NO TESTS RAN unittest, test_ prefix discovery, tests __init__.py package, mkdir src tests, mv main.py, tree cat touch terminal, python3 -m unittest, red green refactor first failure, test driven development environment manually, pumping_python person project, IDE auto save danger close file before mv

.. include:: ../links.rst

#################################################################################
how to make a Python test driven development environment manually
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
requirements
*********************************************************************************

* :ref:`start here`

----

*********************************************************************************
preview
*********************************************************************************

This is one way to make a :ref:`Python Test Driven Development project<what is a Test Driven Development Environment?>`. I walk through making the `folders (directories)`_ and files_ for the environment, including setting up :ref:`the first test<test_failure>`. By the end of the chapter you will know these commands better

.. code-block:: python

  cd
  tree
  mkdir
  touch
  echo
  cat
  mv
  python3 -m unittest
  history

----

*********************************************************************************
questions about making a Python Test Driven Development Environment
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`what is a Test Driven Development Environment?`
* :ref:`how can I make a Python Test Driven Development Environment manually?<how to make a Python Test Driven Development environment manually>`
* :ref:`how can I change directories?<how to change directory>`
* :ref:`how can I make a directory?<how to make a directory>`
* :ref:`how can I see directory structure?<how to look at directory relationships>`
* :ref:`how can I make an empty file?<how to make an empty file>`
* :ref:`how can I write text to a file?<how to write text to a file>`
* :ref:`how can I see what is inside a file?<how to see what is inside a file>`
* :ref:`how can I change the name of a file?<how to change the name of a file>`
* :ref:`how can I run a Python Program?<how to run a Python program>`
* :ref:`how can I test for failure?<test_failure>`
* :ref:`how can I make a Python package?<how to make the tests a Python package>`
* :ref:`how can I run tests manually?<how to manually run tests>`
* :ref:`how can I set up a project with uv?<how to setup a project with uv>`

----

********************************************************************************************
how to setup the project
********************************************************************************************

* I choose ``person`` as the name of this project

* I click ``Terminal`` in the menu bar at the top of the `Integrated Development Environment (IDE)`_, then click ``New Terminal`` to open a terminal_

* I `change directory`_ to where I will put all the projects from this book. I type cd_ in the terminal_

  .. note:: skip this step if you are already in the ``pumping_python`` directory_ or made it earlier

  .. code-block:: python
    :emphasize-lines: 1

    cd pumping_python

  - if the terminal_ shows

    .. code-block:: python

      cd: no such file or directory: pumping_python

    the `folder (directory)`_ does NOT exist. I need to make it. I use the `mkdir program`_ to make the ``pumping_python`` `folder (directory)`_

    .. code-block:: python
      :emphasize-lines: 1

      mkdir pumping_python

    the terminal_ goes back to the command line.

  - I try `changing directory`_ again

    .. code-block:: python
      :emphasize-lines: 1

      cd pumping_python

    the terminal_ shows I am in the ``pumping_python`` `folder (directory)`_

    .. code-block:: python

      .../pumping_python

* I type tree_ in the terminal_ to see what files_ and folders_ are in the ``pumping_python`` directory_

  .. code-block:: python
    :emphasize-lines: 1

    tree

  - if tree_ is not installed on the computer, the terminal_ shows

    .. code-block:: python

      tree: command not found

    :ref:`you can install it from here<what is covered?>`

  - if tree_ is installed on the computer, the terminal_ shows

    .. code-block:: python

      .

      0 directories, 0 files

    .. note:: If you have done other work in the ``pumping_python`` folder_ there will be files_ and folders_ not 0 directories_ and 0 files_

* I `change directory`_ to the ``person`` project in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd person

  the terminal_ is my friend, and shows

  .. code-block:: python

    cd: no such file or directory: person

  there is no folder_ with the name ``person`` in this folder_, time to make ``person``.

----

=====================================================================================================
how to setup a project with uv
=====================================================================================================

----

* I use the `uv Python Package Manager`_ to setup the project

  .. code-block:: python
    :emphasize-lines: 1

    uv init person

  the terminal_ shows

  .. code-block:: shell

    Initialized project `person` at `.../pumping_python/person`

  uv_ is a program_ that makes files_ and folders_ needed for a project. It also handles Python_ and `Python Packages`_.

----

=================================================================================
how to change directory to the project
=================================================================================

----

* I try to `change directory`_ to the ``person`` folder_ again

  .. code-block:: python
    :emphasize-lines: 1

    cd person

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/person

  uv_ made the directory_ for me.

* I use tree_ to see what uv_ added to the folder_

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ shows

  .. code-block:: shell

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
    ├── .python-version
    ├── README.md
    ├── main.py
    └── pyproject.toml

  it added a few files_ and folders_.

  - the ``-L`` option tells tree_ how deep to go when showing the folders_ and files_, I use ``2`` to make it show only the first level of contents of the child folders_
  - Here is what uv_ made for me

    - ``.git`` this folder_ makes the project a git_ repository, it makes it easy to keep track of changes I make, and if I publish the repository I can work on the project from any computer anywhere (as long as it is has access to the repository)
    - ``.gitignore`` is a file_ that tells git_ what files_ in the project to not keep track of, this is useful for things that I do not want or need to share
    - ``.python-version`` is a file_ that has the version of Python_ I am using, this helps if I do projects with different Python_ versions
    - ``README.md`` is a file_ that is used to describe the project
    - ``main.py`` is a :ref:`Python module<what is a module?>` for me to write the code for the project
    - ``pyproject.toml`` is a file_ that is used to configure Python_ projects for packaging see `pyproject.toml`_ for more

----

=====================================================================================================
how to see what is inside a file
=====================================================================================================

----

* I can use the `cat program`_ to look at what is inside ``.gitignore``

  .. code-block:: python
    :emphasize-lines: 1

    cat .gitignore

  the terminal_ shows

  .. code-block:: python

      # Python-generated files
      __pycache__/
      *.py[oc]
      build/
      dist/
      wheels/
      *.egg-info

      # Virtual environments
      .venv

* I use cat_ to see what is inside ``pyproject.toml``

  .. code-block:: python
    :emphasize-lines: 1

    cat pyproject.toml

  the terminal_ shows

  .. code-block:: python

    [project]
    name = "person"
    version = "0.1.0"
    description = "Add your description here"
    readme = "README.md"
    requires-python = ">=3.XY"
    dependencies = []

* I use cat_ to look at what is in ``.python-version``

  .. code-block:: python
    :emphasize-lines: 1

    cat .python-version

  the terminal_ is my friend, and shows

  .. code-block:: python

    3.XY

  where ``XY`` are numbers like ``13`` depending on what version of Python_ you have installed

* I use cat_ to show what is inside ``README.md``

  .. code-block:: python

    cat README.md

  the terminal_ goes back to the command line.

  .. code-block:: python

    .../pumping_python/person

  the file_ is empty

----

=================================================================================
how to run a Python program
=================================================================================

----

I use Python_ to run the ``person`` program_

.. code-block:: python
  :emphasize-lines: 1

  python3 src/person.py

the terminal_ is my friend, and shows

.. code-block:: text

  python3: can't open file
           '.../pumping_python/person/src/person.py':
           [Errno 2] No such file or directory

Python_ cannot find the file_ because it does not exist, and there is no folder_ named ``src``, yet.

----

=====================================================================================================
how to make a directory for the source code
=====================================================================================================

----

* I make a child folder_ in the ``person`` directory_ for the program_ because I want to keep the files_ separate from the other files_ in the project

  .. code-block:: python
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line.

* I use tree_ to see what changed in the ``person`` directory_

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 1

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 8

    .
    ├── .git
    ├── .gitignore
    ├── main.py
    ├── pyproject.toml
    ├── .python-version
    ├── README.md
    └── src

* I try to run the ``person`` program_ again

  .. code-block:: python
    :emphasize-lines: 1

    python3 src/person.py

  the terminal_ is my friend, and shows the same error from before because there is no file_ named ``person.py`` in the ``src`` folder_.

----

=====================================================================================================
how to change the name of a file
=====================================================================================================

----

* I use the `mv program`_ to change the name of ``main.py`` to ``person.py`` and move it to the ``src`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    mv main.py src/person.py

  the terminal_ goes back to the command line.

* I use tree_ to see what folders_ and files_ I now have

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 16

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
    ├── .python-version
    ├── README.md
    ├── pyproject.toml
    └── src
        └── person.py

  ``main.py`` is now ``person.py`` in the ``src`` folder_.

* I try to run the ``person`` program_ again

  .. code-block:: python
    :emphasize-lines: 1

    python3 src/person.py

  the terminal_ shows

  .. code-block:: shell

    Hello from person!

  Success! The `uv Python package manager`_ made the file_ with some Python_ code in it, I can successfully run it because the file_ is now in the folder_.

* I use cat_ to see what is in ``src/person.py``

  .. code-block:: python
    :emphasize-lines: 1

    cat src/person.py

  the terminal_ shows

  .. code-block:: python

    def main():
        print("Hello from person!")


    if __name__ == "__main__":
        main()

  magic!

----

********************************************************************************************
test_failure
********************************************************************************************

=================================================================================
how to manually run tests
=================================================================================

----

* I use the `unittest module`_ from `The Python Standard Library`_ that comes with Python_ to run tests. I type this in the terminal_

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ shows

  .. code-block:: python

    ------------------------------------------------------
    Ran 0 tests in 0.000s

    NO TESTS RAN

  because I do not have any tests, yet.

  - ``python3`` is the `Python program`_
  - ``-m`` is an option/switch passed when calling Python_ to run the :ref:`module<what is a module?>` ( :ref:`unittest<another way to write tests` in this case)
  - which leads to the question of :ref:`what is a module?<what is a module?>` Any file_ that ends in ``.py`` is a :ref:`Python module<what is a module?>`.

----

=====================================================================================================
how to make a directory for the tests
=====================================================================================================

----

* I make a child folder_ to keep the tests separate from the other files_

  .. code-block:: python
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line.

* I use tree_ to see what my project looks like

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 1

  the terminal_ is my friend, and shows

  .. code-block:: shell
    :emphasize-lines: 8

    .
    ├── .git
    ├── .gitignore
    ├── pyproject.toml
    ├── .python-version
    ├── README.md
    ├── src
    └── tests

----

=====================================================================================================
how to make a Python file for the tests in the 'tests' directory
=====================================================================================================

----

* I use touch_ to add an empty file_ to the ``tests`` directory_ for the actual test

  .. code-block:: python
    :emphasize-lines: 1

    touch tests/person.py

  the terminal_ goes back to the command line.

* I use tree_ to see what the project looks like now

  .. code-block:: python
    :emphasize-lines: 18

    tree -a -L 2

  the terminal_ is my friend, and shows

  .. code-block:: shell
    :emphasize-lines: 18

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
        └── person.py

* I run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ is my friend, and shows

  .. code-block:: python

    NO TESTS RAN

  because I have not set up the test correctly.

----

********************************************************************************************
:red:`RED`: make it fail
********************************************************************************************

* I open ``person.py`` from the ``tests`` folder_

  .. tip::

    I can open a file_ from the terminal_ with :kbd:`ctrl` (Windows_/Linux_) or :kbd:`command` (MacOS_) on the keyboard and a click with the mouse on the name of the file_

* I add the Python_ code below in ``tests/person.py``

  .. note:: the line numbers below are a guide, no need to copy them

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    False is True

  I expect this line to fail because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`.

* I turn on the ``Auto Save`` feature in the `Integrated Development Environment (IDE)`_ to automatically save files when I make a change so that `I do not repeat myself`_. I do not want to use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) on the keyboard every time I make a change, I want the computer to do that for me

  .. attention:: Turn on the ``Auto Save`` feature in the `Integrated Development Environment (IDE)`_

* I try the command again to run the tests in the terminal_

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ is my friend, and shows

  .. code-block:: python

    NO TESTS RAN

  because the ``tests`` folder_ is NOT a `Python package`_ and :ref:`unittest<another way to write tests` cannot find my test. I need to add a file_ named ``__init__.py`` to the ``tests`` folder, to make it a `Python package`_ for :ref:`unittest<another way to write tests` to find the test.

----

=====================================================================================================
how to make the tests a Python package
=====================================================================================================

----

* I use touch_ to add an empty file_ with the name ``__init__.py`` to the ``tests`` folder

  .. danger:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. code-block:: python
    :emphasize-lines: 1

    touch tests/__init__.py

  the terminal_ goes back to the command line.

* I run the tree_ command to see what changed

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ is my friend, and shows

  .. code-block:: shell
    :emphasize-lines: 18

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
        └── person.py

* I try to run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ does not feel like my friend, and shows

  .. code-block:: python

    NO TESTS RAN

  because :ref:`unittest<another way to write tests` does not know that ``person.py`` in the ``tests`` folder is a test file_. I did not start the name with ``test_``. I have to change the name.

* I close ``person.py``

  .. danger:: if you do not close ``person.py``, there will be 3 files in the ``tests`` folder after the next step (instead of 2), because the ``Auto Save`` feature (enabled earlier) will save the original file_ if it is still open after you change its name.

* I use the `mv program`_ to change the name of ``person.py`` in the ``tests`` folder_ to ``test_person.py``

  .. code-block:: python
    :emphasize-lines: 1

    mv tests/person.py tests/test_person.py

  the terminal_ goes back to the command line.

* I use tree_ with the ``-L`` option to see what I have so far

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ is my friend, and shows

  .. code-block:: shell
    :emphasize-lines: 20

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

  .. admonition:: if you do not see ``__pycache__`` in the tree do not worry,

    the important thing is that you renamed ``person.py`` to ``test_person.py`` for :ref:`unittest<another way to write tests` to find the test.

* I run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ still shows ``NO TESTS RAN``

* I add ``assert`` before ``False is True`` in ``tests/test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # False is True
    assert False is True

* I try to run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 9

    E
    ======================================================
    ERROR: tests.test_person (unittest.loader._FailedTest.tests.test_person)
    ------------------------------------------------------
    ImportError: Failed to import test module: tests.test_person
    Traceback (most recent call last):
      File "/usr/local/lib/python3.XY/unittest/loader.py",
        line 426, in _find_test_path
        module = self._get_module_from_name(name)
      File "/usr/local/lib/python3.XY/unittest/loader.py",
        line 367, in _get_module_from_name
        __import__(name)
        ~~~~~~~~~~^^^^^^
      File ".../pumping_python/person/tests/test_person.py",
        line 2, in <module>
        assert False is True
               ^^^^^^^^^^^^^
    AssertionError


    ------------------------------------------------------
    Ran 1 test in 0.001s

    FAILED (errors=1)

  Success! I have my first failure. I can use any name for the test file_. It must start with ``test_`` or :ref:`unittest<another way to write tests` will NOT run the tests in the file_.

  This is the :red:`RED` part of the :ref:`Test Driven Development Cycle<what is the Test Driven Development cycle?>`. The message in the terminal_ is about the failure, I like to read these from the bottom up. Here is an explanation of each line, starting from the last line on the screen

  - ``FAILED (errors=1)``: the number of failures or :ref:`errors`
  - ``Ran 1 test in A.XYZs``: the number of tests it ran and how long they took
  - ``AssertionError``: the :ref:`Error (Exception)<errors>` that happened. Since I used an :ref:`assert statement<what is an assertion?>` I get :ref:`AssertionError<what causes AssertionError?>` because the statement after ``assert`` is :ref:`False<test_what_is_false>` - :ref:`False<test_what_is_false>` is NOT :ref:`True<test_what_is_true>`
  - ``assert False is True``: the line of code that caused :ref:`AssertionError<what causes AssertionError?>`
  - the arrows (``^^^^^^^^^^^^^``): point to the part of the line above, that Python_ thinks caused the :ref:`error<errors>`
  - ``File ".../pumping_python/person/tests/test_person.py", line 2, in <module>``: the line number of the code that caused the :ref:`error<errors>` and the location of the file_ where the :ref:`error<errors>` happened and again the question - :ref:`what is a module?`
  - ``__import__(name)`` shows another :ref:`error<errors>` that is triggered by the one from ``assert False is True``
  - ``File "/usr/local/lib/python3.XY/unittest/loader.py", line 367, in _get_module_from_name`` shows the line, :ref:`method<what is a method?>` and file_ where the :ref:`error<errors>` triggered by my ``assert False is True`` happened
  - ``module = self._get_module_from_name(name)`` a failure triggered by the failure triggered by my ``assert False is True``
  - ``File "/usr/local/lib/python3.XY/unittest/loader.py", line 426, in _find_test_path`` shows the line, :ref:`method<what is a method?>` and file_ where the :ref:`error<errors>` triggered by the one triggered by my ``assert False is True`` happened
  - ``Traceback (most recent call last):``: all the information shown after this line that is indented to the right shows the calls that led to the failure. The last line is usually the most important one that points to what caused the failure, this is why I like to read it from the bottom up. In this case it is the only one I care about because it is the one I added to cause the failure.
  - ``ERROR: tests.test_person (unittest.loader._FailedTest.tests.test_person)`` is a header with information in :ref:`dot notation` about the failing test

    - I think of ``tests.test_person `` as an address

      *  ``tests`` is the ``tests`` folder_
      *  ``test_person`` is the ``test_person.py`` file_ in the ``tests`` folder_

----

********************************************************************************************
:green:`GREEN`: make it pass
********************************************************************************************

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``File ".../pumping_python/person/tests/test_person.py", line 2`` in the terminal_, and the `Integrated Development Environment (IDE)`_ opens the file_ with the cursor at the line where the failure happened.

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in ``test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    # False is True
    # assert False is True
    assert False is False

* I go back to the terminal_ to run the test

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the test passes! The terminal_ shows

  .. code-block:: none

    ------------------------------------------------------
    Ran 0 tests in 0.000s

    NO TESTS RAN

  this is confusing, since the only way I know the test passed, is because I saw it fail. Which is why the :red:`RED` part of the cycle is important, it shows that the test works. There has to be a better way. For now *cue CELEBRATION MUSIC AND DANCE!* I am :green:`GREEN!!`

----

********************************************************************************************
:yellow:`REFACTOR`: make it better
********************************************************************************************

* I keep a list of :ref:`Errors/Exceptions<errors>` that show up in the terminal_ as I go through this book to help me know them better, familiarity. I add :ref:`AssertionError<what causes AssertionError?>` to ``test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    # False is True
    # assert False is True
    assert False is False


    # Exceptions seen
    # AssertionError

  comments in Python_ are written with ``#`` at the beginning, they do not do anything, they are notes for me. Time to get some practice with :ref:`Python modules<what is a module?>`.

* I add the new files_ and folders_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

  the terminal_ goes back to the command line.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'setup project'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

********************************************************************************************
close the project
********************************************************************************************

* I close ``test_person.py``

* I click in the terminal and `change directory`_ to the parent of ``person``

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

  .. literalinclude:: ../code/make_tdd/makePythonTdd1History.sh
    :language: python
    :emphasize-lines: 2-3, 12, 14, 19, 21, 24, 27

  the `history program`_ shows all the commands I typed in the terminal_ so far.

* these are the commands I used to make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>`

  .. code-block:: python

    uv init NAME_OF_THE_PROJECT
    cd NAME_OF_THE_PROJECT
    mkdir src
    mv main.py src/NAME_OF_THE_PROJECT.py
    mkdir tests
    touch tests/__init__.py
    touch tests/test_NAME_OF_THE_PROJECT.py

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

----

*************************************************************************************
what is next?
*************************************************************************************

I know :ref:`how to make a Python test driven development environment manually`, :ref:`Would you like to find out what a module is?<what is a module?>`

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