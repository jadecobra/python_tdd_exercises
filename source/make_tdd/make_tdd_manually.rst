.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watcher for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

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

  mkdir
  cd
  touch
  echo
  cat
  mv
  rm
  uv run pytest-watcher
  source .venv/bin/activate
  deactivate
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
* :ref:`how can I run tests automatically?<how to run the tests automatically>`
* :ref:`how can I stop automated Python tests from running?<how to stop the automated tests>`
* :ref:`how can I set up a project with uv?<how to setup a project with uv>`
* :ref:`what is a Virtual Environment?<what is a virtual environment?>`
* :ref:`how can I activate a Virtual Environment?<how to activate a virtual environment>`
* :ref:`how can I deactivate a Virtual Environment?<how to deactivate a virtual environment>`
* :ref:`how can I document the Python programs my project needs?<how to write text to a file>`
* :ref:`how can I install the Python programs my project needs from a file?<how to install Python packages with uv>`
* :ref:`how can I view all the commands I type in a terminal?<how to view all the commands typed in a terminal>`

----

********************************************************************************************
how to setup the project
********************************************************************************************

* I choose ``magic`` as the name of this project

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

* I `change directory`_ to the ``magic`` project in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd magic

  the terminal_ is my friend, and shows

  .. code-block:: python

    cd: no such file or directory: magic

  there is no folder_ with the name ``magic`` in this folder_, time to make ``magic``

----

=====================================================================================================
how to setup a project with uv
=====================================================================================================

----

* I use the `uv Python Package Manager`_ to setup the project

  .. code-block:: python
    :emphasize-lines: 1

    uv init magic

  the terminal_ shows

  .. code-block:: shell

    Initialized project `magic` at `.../pumping_python/magic`

  uv_ is a program_ that makes files_ and folders_ needed for a project. It also handles Python_ and `Python Packages`_

----

=================================================================================
how to change directory to the project
=================================================================================

----

* I try to `change directory`_ to the ``magic`` folder_ again

  .. code-block:: python
    :emphasize-lines: 1

    cd magic

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/magic

  uv_ made the directory_ for me

* I use tree_ to see what uv_ added to the folder_

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2-15

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

  the terminal_ and shows

  .. code-block:: python

    [project]
    name = "magic"
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

    .../pumping_python/magic

  the file_ is empty

----

=================================================================================
how to run a Python program
=================================================================================

----

I use Python_ to run the ``magic`` program_

.. code-block:: python
  :emphasize-lines: 1

  python3 src/magic.py

the terminal_ is my friend, and shows

.. code-block:: text

  python3: can't open file '.../pumping_python/magic/src/magic.py': [Errno 2] No such file or directory

Python_ cannot find the file_ because it does not exist, and there is no folder_ named ``src``, yet.

----

=====================================================================================================
how to make a directory for the source code
=====================================================================================================

----

* I make a child folder_ in the ``magic`` directory_ for the program_ because I want to keep the files_ separate from the other files_ in the project

  .. code-block:: python
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line.

* I use tree_ to see what changed in the ``magic`` directory_

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 1

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 16

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
    ├── main.py
    ├── pyproject.toml
    └── src

* I try to run the ``magic`` program_ again

  .. code-block:: python
    :emphasize-lines: 1

    python3 src/magic.py

  the terminal_ is my friend, and shows the same error from before because there is no file_ named ``magic.py`` in the ``src`` folder_

----

=====================================================================================================
how to change the name of a file
=====================================================================================================

----

* I use the `mv program`_ to change the name of ``main.py`` to ``magic.py`` and move it to the ``src`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    mv main.py src/magic.py

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
    └── src
        └── magic.py

  ``main.py`` is now ``magic.py`` in the ``src`` folder_

* I try to run the ``magic`` program_ again

  .. code-block:: python
    :emphasize-lines: 1

    python3 src/magic.py

  the terminal_ shows

  .. code-block:: shell

    Hello from magic!

  Success! The `uv Python package manager`_ made the file_ with some Python_ code in it, I can successfully run it because the file_ is now in the folder_.

* I use cat_ to see what is in ``src/magic.py``

  .. code-block:: python
    :emphasize-lines: 1

    cat src/magic.py

  the terminal_ shows

  .. code-block:: python

    def main():
        print("Hello from magic!")


    if __name__ == "__main__":
        main()

  magic!

----

********************************************************************************************
test_failure
********************************************************************************************

----

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
  - ``-m`` is an option/switch passed when calling Python_ to run the :ref:`module<what is a module?>` ( unittest_ in this case)
  - a :ref:`Python module<what is a module?>` is any file_ that ends with ``.py``, this means somewhere on the computer there is a file_ named ``unittest.py``, `click here to see the source code for unittest`_


----

=====================================================================================================
how to make a directory for the tests
=====================================================================================================

----

* I make a child folder_ to keep the tests in a different place from the actual program_

  .. code-block:: python
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line.

* I use tree_ to see what my project looks like

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ is my friend, and shows

  .. code-block:: shell
    :emphasize-lines: 17

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
    ├── src
    │   └── magic.py
    └── tests

----

=====================================================================================================
how to make a Python file for the tests in the 'tests' directory
=====================================================================================================

----

* I use touch_ to add an empty file_ to the ``tests`` directory_ for the actual test

  .. code-block:: python
    :emphasize-lines: 1

    touch tests/magic.py

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
    ├── src
    │   └── magic.py
    └── tests
        └── magic.py

* I run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ is my friend, and shows

  .. code-block:: python

    NO TESTS RAN

  because I have not set up the test correctly, yet

----

********************************************************************************************
:red:`RED`: make it fail
********************************************************************************************

* I use the `Integrated Development Environment (IDE)`_ to open ``tests/magic.py`` in the :ref:`editor<2 editors>`

  .. tip::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ by typing the name of the program and the name of the file_, for example with `Visual Studio Code`_ when I type this in the terminal_

    .. code-block:: python
      :emphasize-lines: 1

      code tests/magic.py

    ``magic.py`` from the ``tests`` folder_ opens in the :ref:`editor<2 editors>`.

    I can also open a file_ from the terminal_ with :kbd:`ctrl` (Windows_/Linux_) or :kbd:`command` (MacOS_) on the keyboard and a click with the mouse on the name of the file_

* I add the Python_ code below in ``tests/magic.py`` in the :ref:`editor<2 editors>`

  .. note:: the line numbers below are a guide, no need to copy them

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code I typed in the file_

  - ``import unittest`` imports the `unittest module`_ from `The Python Standard Library`_, this is what I am using for testing. It is like a toolbox that contains the tools I will use to test the code
  - ``class TestMagic``

    * ``class`` is the Python_ keyword for making :ref:`classes<what is a class?>` - a group of :ref:`attributes (values)<what causes AttributeError?>` and :ref:`methods (functions)<what is a function?>` that belong together, :ref:`see the classes chapter for more<what is a class?>`
    * ``TestMagic`` is the name I gave this :ref:`class <what is a class?>` and will hold the test

      .. tip:: I can use any name for the :ref:`test class<what is a class?>`, it MUST start with ``Test`` or unittest_ will NOT run the tests in it

    * `unittest.TestCase`_ is a :ref:`class <what is a class?>` from the `unittest module`_ that has :ref:`methods<what is a method?>` for , this is the tool that contains the :ref:`methods<what is a method?>` I will use to test code in this book
    * ``class TestMagic(unittest.TestCase)`` defines ``TestMagic`` as a "child" of `unittest.TestCase`_ which means I can use the :ref:`methods<what is a method?>` and :ref:`attributes<test_attribute_error_w_class_attributes>` of the `unittest.TestCase class`_, I do not have to make them because someone else already did

  - ``def test_failure``

    * def_ is the Python_ keyword for making :ref:`methods (functions) <what is a function?>`, see :ref:`functions<what is a function?>` for more
    * ``test_failure`` is the name of the :ref:`method<what is a method?>` I used for :ref:`this first test<test_failure>`

      .. tip:: I can use any name for the :ref:`test method<what is a function?>`, it MUST start with ``test_`` or unittest_ will NOT run the tests in it

    * ``self.`` lets me use :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a method?>` of the ``TestMagic`` :ref:`class<what is a class?>` which is a "child" of the `unittest.TestCase class`_, instead of using ``TestMagic().`` or ``unittest.TestCase().`` when I want to use something from the `unittest.TestCase class`_

      .. tip:: the name ``self`` is :ref:`Python convention<conventions>`. I can use any name though it is easier to stick with convention for this one

    * ``self.assertFalse(True)`` is an :ref:`assertion<what is an assertion?>` (a way to make sure something is :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`)

      - assertFalse_ is a :ref:`method<what is a method?>` in the `unittest.TestCase class`_ that checks if its input is :ref:`False<test_what_is_false>`
      - :ref:`True<test_what_is_true>` is given as the input

      I expect this line to fail because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`. If it does not fail, then Python_ and I have a problem

* I turn on the ``Auto Save`` feature in the `Integrated Development Environment (IDE)`_ to automatically save files when I make a change so that `I do not repeat myself`_. I do not want to use :kbd:`ctrl+s` ((Windows_/Linux_) or :kbd:`command+s` (MacOS_)) on the keyboard every time I make a change, I want the computer to do that for me

  .. attention:: Turn on the ``Auto Save`` feature in the `Integrated Development Environment (IDE)`_

    In `Visual Studio Code`_ it is under ``File`` in the menu

* I try the command again to run the tests in the terminal_

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ is my friend, and shows

  .. code-block:: python

    NO TESTS RAN

  because the ``tests`` folder_ is NOT a `Python package`_ and unittest_ cannot find my test. I need to add a file_ named ``__init__.py`` to the ``tests`` folder, to make it a `Python package`_ for unittest_ to find the test.

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
    ├── src
    │   └── magic.py
    └── tests
        ├── __init__.py
        └── magic.py

* I try to run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ does not feel like my friend, and shows

  .. code-block:: python

    NO TESTS RAN

  because unittest_ does not know that ``magic.py`` in the ``tests`` folder is a test file_. I did not start the name with ``test_``. I have to change the name

* I close ``magic.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. danger:: if you do not close ``magic.py`` in the :ref:`editor<2 editors>`, there will be 3 files in the ``tests`` folder after the next step (instead of 2), because the ``Auto Save`` feature (enabled earlier) will save the original file_ if it is still open in the :ref:`editor<2 editors>` after you change its name

* I use the `mv program`_ to change the name of ``magic.py`` in the ``tests`` folder_ to ``test_magic.py``

  .. code-block:: python
    :emphasize-lines: 1

    mv tests/magic.py tests/test_magic.py

  the terminal_ goes back to the command line.

* I use tree_ with the ``-L`` option to see what I have so far

  .. code-block:: python
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ is my friend, and shows

  .. code-block:: shell
    :emphasize-lines: 18

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
    ├── src
    │   └── magic.py
    └── tests
        ├── __init__.py
        ├── __pycache__
        └── test_magic.py

  .. admonition:: if you do not see ``__pycache__`` in the tree do not worry,

    the important thing is that you renamed ``magic.py`` to ``test_magic.py`` for unittest_ to find the test

* I run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 9

    F
    =========================================================
    FAIL: test_failure (tests.test_magic.TestMagic.test_failure)
    ---------------------------------------------------------
    Traceback (most recent call last):
      File "...pumping_python/magic/tests/test_magic.py", line 7, in test_failure
        self.assertFalse(True)
        ~~~~~~~~~~~~~~~~^^^^^^
    AssertionError: True is not false

    ---------------------------------------------------------
    Ran 1 test in A.XYZs

    FAILED (failures=1)

  .. tip:: I can use any name for the test file_. It must start with ``test_`` or unittest_ will NOT run the tests in the file_

  This is the :red:`RED` part of the :ref:`Test Driven Development Cycle<what is the Test Driven Development cycle?>`. The message in the terminal_ is about the failure, I like to read these from the bottom up. Here is an explanation of each line, starting from the last line on the screen

  - ``FAILED (failures=1)``: the number of failures
  - ``Ran 1 test in A.XYZs``: the number of tests it ran and how long they took
  - ``AssertionError: True is not false``: the :ref:`Error (Exception)<errors>` that happened and its message, in this case :ref:`AssertionError<what causes AssertionError?>` because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`
  - ``self.assertFalse(True)``: the line of code that caused :ref:`AssertionError<what causes AssertionError?>`
  - ``~~~~~~~~~~~~~~~~^^^^^^``: points to the part of the line above, that Python_ thinks caused the :ref:`error<errors>`
  - ``File ".../magic/tests/test_magic.py", line 7, in test_failure``: the line number of the code that caused the :ref:`error<errors>` and the location of the file where it is
  - ``Traceback (most recent call last):``: all the information shown after this line that is indented to the right shows the calls that led to the failure. The last line is usually the most important one that points to what caused the failure, this is why I like to read it from the bottom up
  - ``FAIL: test_failure (tests.test_magic.TestMagic.test_failure)`` is a header with information in :ref:`dot notation` about the failing :ref:`test method<what is a function?>`

    - ``tests.test_magic.TestMagic.test_failure`` is the location of the failing test

      *  ``tests`` is the ``tests`` folder_
      *  ``test_magic`` is the ``test_magic.py`` file_ in the ``tests`` folder_
      * ``TestMagic`` is the :ref:`class<what is a class?>` defined on line 4 in ``test_magic.py`` in the ``tests`` folder_
      * ``test_failure`` is the :ref:`method (function)<what is a function?>` defined in the ``TestMagic`` :ref:`class<what is a class?>`, on line 6 in ``test_magic.py`` in the ``tests`` folder_

  * ``F`` shows a failure

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``File ".../pumping_python/magic/tests/test_magic.py", line 7`` in the terminal_, and the `Integrated Development Environment (IDE)`_ opens the file_ in the :ref:`editor<2 editors>` with the cursor at the line where the failure happened

----

********************************************************************************************
:green:`GREEN`: make it pass
********************************************************************************************

I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` on line 7 of ``test_magic.py`` in the :ref:`editor<2 editors>`

.. code-block:: python
  :linenos:
  :emphasize-lines: 7

  import unittest


  class TestMagic(unittest.TestCase):

      def test_failure(self):
          self.assertFalse(False)

I run the test again in the terminal_

.. code-block:: python
  :emphasize-lines: 1

  python3 -m unittest

the test passes! the terminal_ is my friend, and shows

.. code-block:: none
  :emphasize-lines: 3, 5

  .
  ------------------------------------------------------
  Ran 1 test in A.XYZs

  OK

*cue CELEBRATION MUSIC AND DANCE!* I am :green:`GREEN!!`

----

********************************************************************************************
:yellow:`REFACTOR`: make it better
********************************************************************************************

I keep a list of :ref:`Errors/Exceptions<errors>` that show up in the terminal_ as I go through this book to help me know them better, it helps when I run into them later, because I will be more familiar with them. I add :ref:`AssertionError<what causes AssertionError?>` to ``test_magic.py`` in the :ref:`editor<2 editors>`

.. code-block:: python
  :linenos:
  :emphasize-lines: 10-11

  import unittest


  class TestMagic(unittest.TestCase):

      def test_failure(self):
          self.assertFalse(True)


  # Exceptions seen
  # AssertionError

.. note::

  comments in Python_ are written with ``#`` at the beginning, they do not do anything, they are notes for me

* I ran ``python3 -m unittest`` to see the test fail
* I ran ``python3 -m unittest`` every time I made a change until the test passed
* I will run ``python3 -m unittest`` again when I add any code, to make sure tests that passed before do not fail and that the new code I add does what I want

This means I have to run ``python3 -m unittest`` for each part of the :ref:`Test Driven Development Cycle<what is the Test Driven Development Cycle?>` or any time there is a code change.

I do not want to type ``python3 -m unittest`` again, I want the computer to do it for me.

----

=====================================================================================================
how to run the tests automatically
=====================================================================================================

----

I can use `pytest-watcher`_ to run tests automatically. It is a `Python program`_ that automatically runs pytest_ any time a :ref:`Python file<what is a module?>` changes in the folder_ it is looking at, this means it will run the tests for me every time I make a change.

pytest_ is a `Python package`_ like unittest_ that is used for testing. It is not part of `The Python Standard Library`_

I use uv_ to run `pytest-watcher`_ in the terminal_

.. code-block:: python
  :emphasize-lines: 1

  uv run pytest-watcher

the terminal_ is my friend, and shows

.. code-block:: shell

  Using CPython 3.13.13
  Creating virtual environment at: .venv
  error: Failed to spawn: `pytest-watcher`
    Caused by: No such file or directory (os error 2)

because `pytest-watcher`_ is not installed on the computer. I can install it with the `uv Python Package Manager`_.

----

=====================================================================================================
how to write text to a file
=====================================================================================================

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

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard, then click on ``tests/test_magic.py`` to place the cursor in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` on line 7

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

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard, then click on ``tests/test_magic.py:7`` to place the cursor in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then I change :ref:`True<test_what_is_true>` back to :ref:`False<test_what_is_false>` in ``test_magic.py``

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

* I close ``test_magic.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

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

You have seen me make a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for a project called ``magic`` on any Linux_, MacOS_ and Windows_computers. :ref:`Would you like to test AssertionError next?<what is an assertion?>`

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