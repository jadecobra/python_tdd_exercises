.. include:: ../links.rst

#################################################################################
how to make a python test driven development environment
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

This is one way to make a Python Test Driven Development environment

.. contents:: table of contents
  :local:
  :depth: 2

----

*********************************************************************************
requirements
*********************************************************************************

* download and install `Python <https://www.python.org/downloads/>`_
* get an Integrated Development Environment (IDE). Here are a few options

  - `Visual Studio Code`_
  - `Sublime Text`_
  - PyCharm_
  - `other Integrated Development Environment (IDE) options <https://wiki.python.org/moin/IntegratedDevelopmentEnvironments>`_

windows requirements
#################################################################################

If you are using a Windows computer, try to install Linux_ with `Windows Subsystem Linux`_

* click ``start``
* then type ``PowerShell``
* right click and select ``Run as administrator``
* then install `Windows Subsystem Linux`_ in the terminal

  .. code-block:: powershell

    wsl --install --distribution debian

  .. tip:: do not worry if you cannot install `Windows Subsystem Linux`_, I have you covered


linux requirements
#################################################################################

run these commands in a terminal to install Python in Linux_

.. code-block:: shell

  sudo apt update
  sudo apt install python3 python3-venv --yes

----

********************************************************************************************
how to manually make a python test driven development environment
********************************************************************************************

* Imagine I have to work on a project called ``magic``. I open a terminal in the Integrated Development Environment (IDE) and use mkdir_ to make a folder/directory for the project

  .. code-block:: shell

    mkdir magic

  then change directory to the project with the cd_ program

  .. code-block:: shell

    cd magic

  this is where all code for the project will stay

* I make a child folder for the source code

  .. code-block:: shell

    mkdir src

  then add an empty file for the source code (the actual program)

  .. code-block:: shell

    touch src/magic.py

  .. admonition:: on Windows_ without `Windows Subsystem Linux`_ use ``New-Item``

    .. code-block:: shell

      New-Item src/magic.py

  touch_/`New-Item`_ makes an empty file when given a name

* I make a child directory for the tests

  .. code-block:: shell

    mkdir tests

  then an empty file called ``__init__.py`` in the ``tests`` folder to tell Python that it is a `python package`_, this will help it find the tests later

  .. code-block:: shell

    touch tests/__init__.py

  .. WARNING:: make sure to use two underscores (__) for ``__init__.py``

  .. admonition:: on Windows_ without `Windows Subsystem Linux`_ use ``New-Item``

    .. code-block:: shell

      New-Item tests/__init__.py

  I add  one more empty file in the ``tests`` directory for the actual test

  .. code-block:: shell

    touch tests/test_magic.py

  .. admonition:: on Windows_ without `Windows Subsystem Linux`_ use ``New-Item``

    .. code-block:: shell

      New-Item tests/test_magic.py

  you can use any name as long as it starts with ``test_``

* these are the folders/directories and files in the project

  .. code-block:: python

    magic
      ╰──src
      |  ╰──magic.py
      ╰──tests
         ╰──__init__.py
         ╰──test_magic.py

  ``py`` at the end of a file name shows it is a Python :ref:`module<ModuleNotFoundError>`

----

********************************************************************************************
test_failure
********************************************************************************************

The `Test Driven Development`_ cycle is ``RED GREEN REFACTOR``

* **RED**: make it fail - write a failing test to make sure the test works
* **GREEN**: make it pass - write only what is needed to make the failing test pass
* **REFACTOR**: make it better - `remove duplication`_

.. _test_failure_red:

red: make it fail
############################################################################################

* I open ``magic/tests/test_magic.py`` in the Integrated Development Environment (IDE) and type the following

    the line numbers below are a guide, you do not need to copy them

  .. code-block:: python
    :linenos:

    import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code in the file

  - ``import unittest`` imports the unittest_ :ref:`module<ModuleNotFoundError>` from the `python standard library`_, it is used for testing
  - ``class TestMagic``

    * ``class`` is the Python keyword for making :ref:`classes`, which are a collection of :ref:`attributes<AttributeError>` and :ref:`methods<functions>` for a purpose
    * ``TestMagic`` is the name of this :ref:`class <classes>` and will hold the test. You can use any name as long as it starts with ``Test``
    * `unittest.TestCase`_ is a :ref:`class <classes>` defined in the unittest_ :ref:`module<ModuleNotFoundError>` which has :ref:`methods<functions>` for testing
    * ``class TestMagic(unittest.TestCase)`` defines that ``TestMagic`` inherits from `unittest.TestCase`_ which allows me use its :ref:`methods<functions>`

  - ``def test_failure``

    * def_ is the Python keyword for making :ref:`methods and functions<functions>`, a method is a function in a class
    * ``test_failure`` is the name of this :ref:`method<functions>`, you can use any name as long as it starts with ``test_``
    * ``self`` is used to access :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of the ``TestMagic`` class and by extension the `unittest.TestCase`_ class instead of using ``TestMagic().`` or ``unittest.TestCase().``
    * ``self.assertFalse(True)`` is an assertion

      - assertFalse_ is a :ref:`method<functions>` in the `unittest.TestCase`_ :ref:`class <classes>` that checks if its input is :ref:`False<test_what_is_false>`
      - :ref:`True<test_what_is_true>` is given as the input
      - I expect this line to fail because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`, there is a problem if it does not fail

* I turn on the ``Auto Save`` feature in the Integrated Development Environment (IDE) to automatically save files when I make a change so `I do not repeat myself`_ by manually saving every time there is a change
* then type this in the terminal to run the test

  .. code-block:: python

    python3 -m unittest

  .. admonition:: on Windows_ without `Windows Subsystem Linux`_

    use ``python`` instead of ``python3``

    .. code-block:: shell

      python -m unittest

  and it shows a failure

  .. code-block:: python

    F
    =============================================================
    FAIL: test_failure (tests.test_magic.TestMagic.test_failure)
    -------------------------------------------------------------
    Traceback (most recent call last):
    File ".../magic/tests/test_magic.py", line 7, in test_failure
        self.assertFalse(True)
    AssertionError: True is not false

    -------------------------------------------------------------
    Ran 1 test in A.XYZs

    FAILED (failures=1)

If you are typing along, *CONGRATULATIONS!* You just wrote a test.

This is the ``RED`` part of the `Test Driven Development`_ cycle. The message in the terminal is about the failure, here is an explanation from the bottom up

* ``FAILED (failures=1)`` the number of failures
* ``Ran 1 test in A.XYZs`` the number of tests run and how long it took
* ``AssertionError: True is not false`` the :ref:`Exception<Exceptions>` raised and its message, in this case :ref:`AssertionError` is raised because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`
* ``self.assertFalse(True)`` the line of code that caused the failure
* ``File ".../magic/tests/test_magic.py", line 7, in test_failure`` the line number and location of the file where the failure happened

  .. tip:: Hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``File ".../magic/tests/test_magic.py", line 7`` with your mouse in the terminal, and the Integrated Development Environment (IDE) will open the file in the editor with the cursor at the line where the failure happened

* ``Traceback (most recent call last):`` all the information shown after this line that is indented to the right shows the calls that led to the failure
* ``FAIL: test_failure (tests.test_magic.TestMagic.test_failure)`` is a header with information in :doc:`dot notation</dot_notation>` about the failing test :ref:`method<functions>`

  - ``tests.test_magic.TestMagic.test_failure`` is the location of the failing test
  -  ``tests`` is the ``tests`` folder
  -  ``test_magic`` is the ``test_magic.py`` file
  - ``TestMagic`` is the :ref:`class <classes>` defined on line 4
  - ``test_failure`` is the :ref:`method<functions>` defined on line 6

* ``F`` indicates a failure
* ``python3 -m unittest`` is the command to run tests with the ``unittest`` :ref:`module<ModuleNotFoundError>`

  - ``python3`` is the major version of Python being used
  - ``-m`` is an option passed to Python to run the :ref:`module<ModuleNotFoundError>` given after the option as a script

* I recommend you keep a list of :ref:`Exceptions<Exceptions>` you meet to become familiar with them, it helps when you run into failures later. Time to add :ref:`AssertionError` to the list

  .. code-block:: python

    import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

    # Exceptions Encountered
    # AssertionError

.. _test_failure_green:

green: make it pass
#################################################################################

I change the input on line 7 from :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>`

.. code-block:: python

  self.assertFalse(False)

then run the test again in the terminal

.. code-block:: python

  python3 -m unittest

.. admonition:: on Windows_ without `Windows Subsystem Linux`_ use ``python`` instead of ``python3``

  .. code-block:: shell

    python -m unittest

and it shows a passing test

.. code-block:: python

  .
  ------------------------------------------------------
  Ran 1 test in A.XYZs

  OK

*cue CELEBRATION MUSIC AND DANCE!* I am GREEN.

.. _test_failure_refactor:

refactor: make it better
############################################################################################

I ran ``python3 -m unittest`` to see the test fail, ran it again to see the test pass. I will have to run it again when I make a code change, to make sure tests that were passing are not failing and the new code does what I expect.
This means it is run for each part of the `Test Driven Development`_ cycle or any time there is a code change. I do not want to type ``python3 -m unittest`` again, it is better for a program to run the tests so `I do not repeat myself`_.

----

********************************************************************************************
how to automatically run tests
********************************************************************************************

how to make a virtual environment
############################################################################################

* I make a `virtual environment`_ with the venv_ :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

    python3 -m venv .venv

  .. admonition:: on Windows_ without `Windows Subsystem Linux`_ use ``python`` instead of ``python3``

    .. code-block:: shell

      python -m venv .venv

  - ``python3`` is the major version of Python being used
  - ``-m`` is an option passed to Python to run the :ref:`module<ModuleNotFoundError>` given after the option as a script
  - venv_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_, it is used to make a `virtual environment`_ with a given name. A `virtual environment`_ is a separate folder where `python packages`_ needed by the project will be installed
  - ``.venv`` is the name given, you can use any name

* I activate the `virtual environment`_ to use it

  .. code-block:: shell

    source .venv/bin/activate

  .. admonition:: on Windows_ without `Windows Subsystem Linux`_ run PowerShell_ in Administrator mode and set the Execution Policy for the activation script to work

    .. code-block:: PowerShell

      Set-ExecutionPolicy RemoteSigned

    the terminal shows

    .. code-block:: text

      The execution policy helps protect you from scripts that you do not trust.
      Changing the execution policy might expose you to the security risks
      described in the about_Execution_Policies help topic at
      https:/go.microsoft.com/fwlink/?LinkID=135170.
      Do you want to change the execution policy?

      [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"):

    Type ``Y`` to confirm the change and it will enable scripts that have been signed by a verified publisher to run on your computer, you can read more at `Set-ExecutionPolicy`_

    To activate the virtual environment, go back to the terminal you were working in before the Execution Policy change and type

    .. code-block::

      .venv/scripts/activate

    or

    .. code-block:: PowerShell

      .venv/scripts/activate.ps1

  the ``(.venv)`` on the far left of the command line in the terminal shows that I am in the `virtual environment`_

  .. code-block:: shell

    (.venv) .../magic $

* I upgrade pip_ the `python package manager`_ to the latest version

  .. code-block:: python

    python3 -m pip install --upgrade pip

  .. admonition:: on Windows_ without `Windows Subsystem Linux`_ use ``python`` instead of ``python3``

    .. code-block:: shell

      python -m pip install --upgrade pip

  - pip_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_, it is used to install `python packages`_
  - ``install`` is an argument given to pip_ to install a given package name
  - ``--upgrade`` is an option given to the ``install`` argument for pip_ to upgrade the version of the `python package`_ given
  - ``pip`` is the package name given for pip_ to install, in this case it upgrades itself

* I can use pip_ to see what packages are installed in the virtual environment

  .. code-block:: python

    pip list

  and the terminal shows

  .. code-block:: shell

    Package Version
    ------- -------
    pip     x.y.z

* I make a file in the ``magic`` directory with `pytest-watch`_ as its text

  .. code-block:: shell

      echo pytest-watch > requirements.txt

  .. admonition:: on Windows_ without `Windows Subsystem Linux`_ type this

    .. code-block::

      "pytest-watch" | Out-File requirements.txt -Encoding UTF8

  - echo_ is a program that writes its given arguments to the `standard output (stdout)`_
  - ``>`` is an operator that is used to send output from a program to the given file
  - ``|`` is an operator that is used to send output from the left as input to the right
  - `Out-File`_ writes input text to a given file
  - `pytest-watch`_ is a Python program that automatically runs pytest_ when a Python file in the folder changes
  - pytest_ is a `python package`_ like unittest_ that is used for testing
  - ``requirements.txt`` is the name of a file where I can list `python packages`_ for pip_ to install, you can use any name

* I install `pytest-watch`_ and its dependencies

  .. code-block:: python

      pip install --requirement requirements.txt

  - ``--requirement`` is another option that can be passed to the ``install`` argument for `python packages`_ in a given file
  - ``requirements.txt`` is the name of the file given

* I use pip_ to see the packages that are now installed in the `virtual environment`_

  .. code-block:: python

    pip list

  and the terminal shows

  .. code-block:: python

    Package      Version
    ------------ -------
    colorama     x.y.z
    docopt       x.y.z
    iniconfig    x.y.z
    packaging    x.y
    pip          x.y
    pluggy       x.y.z
    pytest       x.y.z
    pytest-watch x.y.z
    watchdog     x.y.z

* The folder/directory structure now looks like this

  .. code-block:: python

    magic
      ╰──.venv
      ╰──src
      | ╰──magic.py
      ╰──tests
      |  ╰──__pycache__
      |  ╰──__init__.py
      |  ╰──test_magic.py
      ╰──requirements.txt

* I run the tests from the terminal

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

* when I change the input on line 7 in ``test_magic.py`` from :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` it shows :ref:`AssertionError`

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

  then I change it back to :ref:`False<test_what_is_false>` to make it pass and can write the rest of the code for the project while the tests run automatically

  .. tip:: press ``ctrl`` + ``c`` on the keyboard in the terminal to stop the tests at anytime

----

how to deactivate a virtual environment
#################################################################################################

type this in a terminal with an active `virtual environment`_

.. code-block::

  deactivate

----

how to activate a virtual environment
############################################################################################

Make sure you are in the folder/directory that has the `virtual environment`_ for example ``magic``, and type this in the terminal

.. code-block:: shell

  source .venv/bin/activate

.. admonition:: on Windows_ without `Windows Subsystem Linux`_

  .. code-block::

    .venv/scripts/activate

  or

  .. code-block:: PowerShell

    .venv/scripts/activate.ps1

the ``(.venv)`` on the far left of the command line in the terminal shows that I am in the `virtual environment`_

.. code-block:: shell

  (.venv) .../magic $

-----

********************************************************************************************
how to automatically make a python test driven development environment
********************************************************************************************

You made it this far and have become the greatest programmer in the world. To follow `The Do Not Repeat Yourself (DRY) Principle`_, I would write a program that has all the commands it took to get here, then I can use it to make a `Test Driven Development`_ Environment anytime I want and not have to remember each step of the process

* I exit the tests in the terminal by pressing ``ctrl`` + ``c`` on the keyboard
* and leave the `virtual environment`_

  .. code-block:: shell

    deactivate

* then change directory to the parent of ``magic``

  .. code-block:: shell

    cd ..

* and make an empty file with a name that describes what the program does so it is easy to remember later, for example :ref:`makePythonTdd.sh`

  .. code-block:: shell

    touch makePythonTdd.sh

* I use the history_ program to list the commands I typed and use them as a reference for the program

  .. code-block:: shell

    history

* then open the file in the Integrated Development Environment (IDE), and copy the commands I need to make a `Test Driven Development`_ Environment

  .. code-block:: ruby

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
    echo pytest-watch > requirements.txt
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  ``#!/bin/bash`` is a shebang_ line that tells the computer to use bash_ to run the program. You can change it to ``#!/bin/zsh`` if you have zsh_ installed

* This program will always make a project called ``magic``. I add a variable to make it possible to make a project for any name I give when the program is called and use it to replace ``magic`` in the program

  .. code-block:: shell

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

  ``$1`` represents the first argument given when the program is called, you can use it in place of ``$PROJECT_NAME``

* I use the echo_ program to add text for the first failing test to ``test_$PROJECT_NAME.py``

    the line numbers below are a guide, you do not need to copy them

  .. literalinclude:: /code/make_tdd/makePythonTdd.sh
    :language: shell
    :linenos:

* then make the program executable

  .. code-block:: shell

    chmod +x makePythonTdd.sh

  chmod_ is a program that changes the mode of the given file

* I can make a `Test Driven Development`_ environment when I call the program with a name for the ``PROJECT_NAME`` variable. For example, when I type

  .. code-block:: shell

    ./makePythonTdd.sh calculator

  in the terminal in the folder where ``makePythonTdd.sh`` is saved, the computer will make a `Test Driven Development`_ environment for a project called ``calculator``, you can continue this in :doc:`/how_to/calculator`

----

how to automatically make a python test driven development environment on Windows_ without WSL
#################################################################################################

.. warning:: This is for Windows_ without `Windows Subsystem Linux`_

* I make a file called :ref:`makePythonTdd.ps1` by using the ``New-Item`` command in PowerShell

  .. code-block:: PowerShell

    New-Item makePythonTdd.ps1

* and open the file in the Integrated Development Environment's Editor then add the following

    the line numbers below are a guide, you do not need to copy them

  .. literalinclude:: /code/make_tdd/makePythonTdd.ps1
    :linenos:
    :language: PowerShell

  - ``$args[0]`` is the first argument given when the program is called. You can use it in place of ``$PROJECT_NAME``
  - `Out-File`_ writes input text to a given file

* I can make a `Test Driven Development`_ environment when I call the program with a name for the ``$PROJECT_NAME`` variable. For example, when I type

  .. code-block:: PowerShell

    ./makePythonTdd.ps1 calculator

  in the terminal in the directory where ``makePythonTdd.ps1`` is saved, the computer will make a `Test Driven Development`_ environment for a project called ``calculator``, you can continue this in :doc:`/how_to/calculator`


----

.. _make_tdd_environment_review:

********************************************************************************************
review
********************************************************************************************

One of the advantages of programming is that I can take some steps and make them a one line command for the computer to do for me. You have seen a way to make a Python Test Driven Development Environment, and have a program to do it for you on any Linux_, Windows_ or MacOS_ computers.

Would you like to test :doc:`making a calculator?</how_to/calculator>`

----

* :doc:`/code/make_tdd/code_make_python_tdd_sh`
* :doc:`/code/make_tdd/code_make_python_tdd_ps1`