.. include:: ../links.rst

#################################################################################
how to make a python test driven development environment
#################################################################################

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/QRIO98ofeFM?si=y4VchKPNr7mzeTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

This chapter covers one way to make a Python Test Driven Development environment

.. contents:: table of contents
  :local:
  :depth: 2

----

*********************************************************************************
requirements
*********************************************************************************

* download and install `Python <https://www.python.org/downloads/>`_
* An Integrated Development Environment (IDE). Here are a few options

  - `Visual Studio Code`_
  - `Other Integrated Development Environment (IDE) options <https://wiki.python.org/moin/IntegratedDevelopmentEnvironments>`_

windows requirements
#################################################################################

If you are using a Windows computer, try to install Linux_ with `Windows Subsystem Linux`_

* click ``start``
* then type ``PowerShell``
* right click and select ``Run as administrator`` to open a terminal
* then install `Windows Subsystem Linux`_ with

  .. code-block:: powershell

    wsl --install --distribution debian

  .. tip:: if you cannot install `Windows Subsystem Linux`_, do not worry, I show what you can do to get the same results


linux requirements
#################################################################################

run these commands in a terminal to install python on the Linux_ Operating System

.. code-block:: shell

  sudo apt update
  sudo apt full-upgrade --yes
  sudo apt install python3 python3-venv --yes

----

********************************************************************************************
how to manually make a python test driven development environment
********************************************************************************************

* I open a terminal in the Integrated Development Environment (IDE) then use mkdir_ to make a folder/directory for the project

  .. code-block:: shell

    mkdir magic

  then change directory to the project with the cd_ program

  .. code-block:: shell

    cd magic

  this is where all code for the project will stay

* I make child folders/directories for the source code and tests

  .. code-block:: shell

    mkdir src tests

* then add empty files for the project

  - I make an empty file that will hold the source code for the program

    .. code-block:: shell

      touch src/magic.py

    .. admonition:: on Windows without `Windows Subsystem Linux`_ use ``New-Item``

      .. code-block:: shell

        New-Item src/magic.py

    touch_/`New-Item`_ makes an empty file when given a name

  - tests will stay in the ``tests`` folder/directory to separate them from the source code (the actual program). I make an empty file called ``__init__.py`` in the ``tests`` folder/directory to tell Python that it is a `python package`_, this will help it find the tests later

    .. code-block:: shell

      touch tests/__init__.py

    .. WARNING:: make sure you use two underscores (__) for ``__init__.py``

    .. admonition:: on Windows without `Windows Subsystem Linux`_ use ``New-Item``

      .. code-block:: shell

        New-Item tests/__init__.py

  - then add one more empty file to the ``tests`` folder/directory for the actual test

    .. code-block:: shell

      touch tests/test_magic.py

    .. admonition:: on Windows without `Windows Subsystem Linux`_ use ``New-Item``

      .. code-block:: shell

        New-Item tests/test_magic.py

    you can use any name you like as long as it starts with ``test_``

* Here is what the folder/directory structure looks like

  .. code-block:: python

    magic
      ╰──src
      |  ╰──magic.py
      ╰──tests
         ╰──__init__.py
         ╰──test_magic.py

.. tip:: ``magic`` is a placeholder for the name of the project. For example, change ``magic`` to ``calculator`` to work on a ``calculator`` project

----

.. _test_failure:

********************************************************************************************
test_failure
********************************************************************************************

The Test Driven Development cycle is ``RED GREEN REFACTOR``

* **RED**: make it fail - write a failing test to make sure the test works
* **GREEN**: make it pass - write only what is needed to make the failing test pass
* **REFACTOR**: make it better - `remove duplication <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

.. _test_failure_red:

red: make it fail
############################################################################################

* I open up ``magic/tests/test_magic.py`` in the Integrated Development Environment (IDE) and type this

    you do not need to copy the line numbers below, they are a guide

  .. code-block:: python
    :linenos:

    import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code above

  - ``import unittest`` imports the unittest_ :ref:`module<ModuleNotFoundError>` which is used for testing, from the `python standard library`_
  - ``class TestMagic`` is the definition of a test :doc:`class </classes/classes>`

    * :doc:`class </classes/classes>` is the python keyword for making :doc:`/classes/classes`
    * ``TestMagic`` is the name given to the :doc:`class </classes/classes>` that will hold the tests, you can use any name you want as long as it starts with ``Test``
    * `unittest.TestCase`_ is a :doc:`class </classes/classes>` defined in the unittest_ :ref:`module<ModuleNotFoundError>` that contains :doc:`methods (functions) </functions/functions>` for testing
    * ``TestMagic`` inherits from `unittest.TestCase`_, it is a child or clone of `unittest.TestCase`_ and can do the same things. I can also change its behavior in the :doc:`class</classes/classes>` definition

  - ``def test_failure`` is the definition of a test :ref:`method<functions>` to test the program I am making

    * def_ is the python keyword for making :ref:`functions/methods<functions>`, a method is a function in a class
    * ``test_failure`` is the name of the :ref:`method<functions>`,  you can use any name you want as long as it starts with ``test_``
    * ``self`` is the ``TestMagic`` :ref:`class<classes>`. I use ``self`` to access :doc:`methods (functions) </functions/functions>` and :ref:`attributes<AttributeError>` of the ``TestMagic`` class and by extension `unittest.TestCase`_
    * ``self.assertFalse(True)`` is the actual test. I expect this line to fail because :doc:`True </data_structures/booleans/booleans>` is not :doc:`False </data_structures/booleans/booleans>`. If it passes then I have a problem

      - assertFalse_ is a :ref:`method<functions>` in the `unittest.TestCase`_ :doc:`class </classes/classes>` that checks if its input is :doc:`False </data_structures/booleans/booleans>`
      - :doc:`True </data_structures/booleans/booleans>` is given as input to ``assertFalse``

* I turn on the ``Auto Save`` feature in the Integrated Development Environment (IDE) to automatically save files when I make a change
* then type this in the terminal to run the test

  .. code-block:: python

    python3 -m unittest

  .. admonition:: on Windows without `Windows Subsystem Linux`_

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
    Ran 1 test in 0.000s

    FAILED (failures=1)

If you are typing along, *CONGRATULATIONS!* You just wrote a test.

This is the ``RED`` part of the Test Driven Development cycle. The error in the terminal has important information, here is an explanation from the bottom up

* ``FAILED (failures=1)`` the number of failures
* ``Ran 1 test in 0.000s`` the number of tests run and how long it took
* ``AssertionError: True is not false`` The error is an :ref:`AssertionError` which is raised because :doc:`True </data_structures/booleans/booleans>` is not :doc:`False </data_structures/booleans/booleans>`
* ``self.assertFalse(True)`` is the line of code that caused the failure
* ``File ".../magic/tests/test_magic.py", line 7, in test_failure`` is the line number and location of the file where the :ref:`AssertionError` happened

  .. tip::

    Hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click with your mouse on ``File ".../magic/tests/test_magic.py", line 7`` in the terminal, the Integrated Development Environment (IDE) will open the file in the editor with the cursor on the line where the error happened

* ``Traceback (most recent call last):`` all the indented information shown after this line is the ``traceback`` showing the calls that led to the error
* ``FAIL: test_failure (tests.test_magic.TestMagic.test_failure)`` is a header with information in :doc:`dot notation</dot_notation>` about the test

  - ``tests.test_magic.TestMagic.test_failure`` is the location of the failing test
  -  ``tests`` is the tests folder/directory
  -  ``test_magic`` is the ``test_magic.py`` file
  - ``TestMagic`` is the class defined on line 4
  - ``test_failure`` is the :ref:`method<functions>` defined on line 6

* ``F`` indicates a failure
* ``python3 -m unittest`` is the command to run tests with the ``unittest`` :ref:`module<ModuleNotFoundError>`

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to run the :ref:`module<ModuleNotFoundError>` given after the option as a script

* I recommend you write down :doc:`Exceptions </how_to/exception_handling_programs>` you meet to become familiar with them, it will help when you run into errors later. Time to add :ref:`AssertionError` to the list

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

I change the input on line 7 from :doc:`True </data_structures/booleans/booleans>` to :doc:`False </data_structures/booleans/booleans>`

.. code-block:: python

  self.assertFalse(False)

then run the test again in the terminal

.. code-block:: python

  python3 -m unittest

.. admonition:: on Windows without `Windows Subsystem Linux`_ use ``python`` instead of ``python3``

  .. code-block:: shell

    python -m unittest

and it shows a passing test

.. code-block:: python

  .
  ------------------------------------------------------
  Ran 1 test in 0.000s

  OK

*cue CELEBRATION MUSIC AND DANCE!* I am GREEN.

.. _test_failure_refactor:

refactor: make it better
############################################################################################

I ran ``python3 -m unittest`` to see the test fail, again to see the test pass, I will have to run it again anytime I change the code to make sure tests that were passing are not broken and the new code does what I expect.
This means it is run for each part of the Test Driven Development cycle or any time there is a code change. I do not want to type ``python3 -m unittest`` again, it is better for a program to run the tests so `I Do Not Repeat myself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

----

********************************************************************************************
how to automatically run tests
********************************************************************************************

how to make a virtual environment
############################################################################################

* I make a `virtual environment`_ with the venv_ :ref:`module<ModuleNotFoundError>` from the `python standard library`_

  .. code-block:: python

    python3 -m venv .venv

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use ``python`` instead of ``python3``

    .. code-block:: shell

      python -m venv .venv

  - ``python3`` is the major version of python being used
  - ``-m`` is the option passed to python to run the given :ref:`module<ModuleNotFoundError>` as a script
  - venv_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_ for making a `virtual environment`_ with a given name. A `virtual environment`_ is a separate folder/directory where packages that are dependencies of the project will be installed
  - ``.venv`` is the standard name for `virtual environments <https://docs.python.org/3/glossary.html#term-virtual-environment>`_ in Python, you can use any name you like

* I activate the `virtual environment`_ to use it ::

      source .venv/bin/activate

  .. admonition:: type this on Windows without `Windows Subsystem Linux`_

    .. code-block::

      .venv/scripts/activate

    or

    .. code-block::

      .venv/scripts/activate.ps1

  the ``(.venv)`` on the far left of the command line in the terminal shows that I am using the `virtual environment`_

  .. code-block:: shell

    (.venv) vscode ➜ .../magic $

* I upgrade pip_ the `python package manager`_ to the latest version

  .. code-block:: python

    pip install --upgrade pip

  - pip_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_ that installs `python packages`_
  - ``install`` is an argument given to pip_ to install a given package name
  - ``--upgrade`` is an option given to the ``install`` argument for pip_ to install the latest version of the name given
  - ``pip`` is the package name given for pip_ to install, in this case it upgrades itself

* After the upgrade, I can use pip_ to see the packages that are already installed in the virtual environment

  .. code-block:: python

    pip list

  and the terminal shows

  .. code-block:: shell

    Package Version
    ------- -------
    pip     24.1.1

  your versions may vary

* I make a file called ``requirements.txt`` in the ``magic`` folder/directory

  .. code-block:: shell

      echo "pytest-watch" > requirements.txt

  .. admonition:: type this on Windows without `Windows Subsystem Linux`_

    .. code-block::

      "pytest-watch" | Out-File requirements.txt

  - the command above makes a file named ``requirements.txt`` with `pytest-watch`_ as the text inside it
  - echo_ is a program that writes its given arguments to the `standard output (stdout)`_
  - ``>`` is an operator that is used to send output from a program to the file given
  - `pytest-watch`_ is a python program that automatically runs pytest_ when a python file in the folder/directory changes
  - pytest_ is a `python package`_ like unittest_ that is used for testing
  - ``requirements.txt`` is the name of a file where I can list `python packages`_ for pip_ the `python package manager`_ to install in the `virtual environment`_ later, you can use any name you like
  - ``|`` is an operator called a pipe that is used to send the result on the left to the program on the right
  - ``Out-File`` is a program that writes the input given to the file given

* I install the `pytest-watch`_ package and its dependencies from the ``requirements.txt`` file

  .. code-block:: python

      pip install --requirement requirements.txt

  - ``--requirement`` is another option that can be passed to the ``install`` argument to install `python packages`_ from a given file
  - ``requirements.txt`` is the file that contains a list of `python packages`_ for pip_ to install

* I use pip_ to see the packages that are now installed in the `virtual environment`_

  .. code-block:: python

    pip list

  and the terminal shows

  .. code-block:: python

    Package      Version
    ------------ -------
    colorama     0.4.6
    docopt       0.6.2
    iniconfig    2.0.0
    packaging    24.0
    pip          24.0
    pluggy       1.5.0
    pytest       8.2.2
    pytest-watch 4.2.0
    watchdog     4.0.1

  your versions may vary

* The folder/directory structure now looks like this

  .. code-block:: python

    magic
      ╰──.venv
      ╰──src
      | ╰──magic.py
      magic.py
      ╰──tests
      |  ╰──__pycache__
      |  ╰──__init__.py
      |  ╰──test_magic.py
      ╰──requirements.txt

* When I type ``pytest-watch`` in the terminal, the test runs and it shows results without going back to the command line

  .. code-block:: ruby

    [TODAYS_DATE] Running: py.test
    ================== test session starts===================
    ...
    rootdir: .../magic
    collected 1 item

    tests/test_magic.py .          [100%]

    =============== 1 passed in 0.00s =======================

* I change the input on line 7 in ``test_magic.py`` from :doc:`False </data_structures/booleans/booleans>` to :doc:`True </data_structures/booleans/booleans>` and it shows an :ref:`AssertionError`

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
    ================================= 1 failed in 0.05s ===================================

  then I change it back to :doc:`False </data_structures/booleans/booleans>` to make it pass with the terminal responding to each change

  .. tip:: press ``ctrl`` + ``c`` on the keyboard in the terminal when you want to stop the tests

----

how to deactivate a virtual environment
#################################################################################################

type the following in a terminal with an active `virtual environment`_

.. code-block::

  deactivate

----

how to activate a virtual environment
############################################################################################

Make sure you are in the folder/directory that contains the `virtual environment`_ for example ``magic``, and type the following in the terminal

.. code-block:: shell

  source .venv/bin/activate

.. admonition:: on Windows without `Windows Subsystem Linux`_

  You may need to Set the Execution Policy in Administrator mode first

  .. code-block:: PowerShell

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

  then activate the virtual environment

  .. code-block::

    .venv/scripts/activate

  or

  .. code-block:: PowerShell

    .venv/scripts/activate.ps1

-----

********************************************************************************************
how to automatically make a python test driven development environment
********************************************************************************************

You made it this far and have become the greatest programmer in the world. To follow `The Do Not Repeat Yourself (DRY) Principle`_, I would write a program that contains all the commands it took to get here, then I can use it to make a Test Driven Development Environment anytime I want and not have to remember each step of the process

* I exit the tests in the terminal by pressing ``ctrl`` + ``c`` on the keyboard
* then type ``deactivate`` to leave the `virtual environment`_
* and change directory to the parent of ``magic``

  .. code-block:: shell

    cd ..

* I use the history_ program to list the commands I typed in the terminal as a reference for the program

  .. code-block:: shell

    history

* then make an empty file with a name that describes what the program does so it is easy to remember later, for example :ref:`makePythonTdd.sh`

  .. code-block:: shell

    touch makePythonTdd.sh

* and open the file in the Integrated Development Environment (IDE), then copy each command I need to make a Test Driven Development Environment

  .. code-block:: ruby

    #!/bin/bash
    mkdir magic
    cd magic
    mkdir src tests
    touch src/magic.py
    touch tests/__init__.py
    touch tests/test_magic.py
    echo "pytest-watch" > requirements.txt
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  ``#!/bin/bash`` is a shebang_ line that tells the computer to use bash_ to run the program. You can change it to ``#!/bin/zsh`` if you have zsh_ installed

* This program will always make a project called ``magic``. I add a variable called ``PROJECT_NAME`` that is referenced with ``$PROJECT_NAME`` to make it possible to make any project name I give when the program is called

  .. code-block:: shell

    #!/bin/bash
    PROJECT_NAME=$1
    mkdir $PROJECT_NAME
    cd $PROJECT_NAME
    mkdir src tests
    touch $PROJECT_NAME.py
    touch tests/__init__.py
    touch tests/test_$PROJECT_NAME.py

    echo "pytest-watch" > requirements.txt

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  ``$1`` represents the first argument given when the program is called. You can use it in place of ``$PROJECT_NAME``

* I use the `cat <https://www.man7.org/linux/man-pages/man1/cat.1.html>`_ program to add text for the first failing test in ``test_$PROJECT_NAME.py``

    the line numbers below are a guide, you do not need to copy them

  .. literalinclude:: /code/make_tdd/makePythonTdd.sh
    :language: shell
    :linenos:

  all the text between the two ``DELIMITER`` words will be written to ``tests/test_$PROJECT_NAME.py``

* I use chmod_ to make the program executable

  .. code-block:: shell

    chmod +x makePythonTdd.sh

  chmod_ is a program that changes the mode of the file given

* I can now make a Test Driven Development environment by giving a name for the ``PROJECT_NAME`` variable when I call the program. For example, typing this command in the terminal in the folder/directory where ``makePythonTdd.sh`` is saved will make a Test Driven Development environment for a project called ``calculator``, you can continue this in :doc:`/how_to/calculator`

  .. code-block:: shell

    ./makePythonTdd.sh calculator

----

how to automatically make a python test driven development environment on windows without WSL
#################################################################################################

.. warning:: This is for Windows without `Windows Subsystem Linux`_

* I make a file named :ref:`makePythonTdd.ps1` by using the ``New-Item`` command in PowerShell

  .. code-block:: PowerShell

    New-Item makePythonTdd.ps1

* and open the file in the Integrated Development Environment's Editor then add the following code

    the line numbers below are a guide, you do not need to copy them

  .. literalinclude:: /code/make_tdd/makePythonTdd.ps1
    :linenos:
    :language: PowerShell

  - ``$args[0]`` represents the first argument given when the program is called. You can use it in place of ``$projectName`` and will get the same result
  - ``@""@`` is like ``DELIMITER`` it allows writing multiline text in PowerShell_
  - ``|`` is an operator that is used to send output from one program to another

* I can now make a Test Driven Development environment by giving a name for the ``$projectName`` variable when the program is called. For example, typing this command in the terminal in the folder/directory where ``makePythonTdd.ps1`` is saved will make a Test Driven Development environment for a project called ``calculator``, you can continue this in :doc:`/how_to/calculator`

  .. code-block:: PowerShell

    ./makePythonTdd.ps1 calculator

----

********************************************************************************************
review
********************************************************************************************

One of the advantages of programming is that I can take some steps and make them a one line command for the computer to do for me. You now know one way to make a Python Test Driven Development Environment, and have a program to do it for you anytime you want.

Would you like to test :doc:`/how_to/calculator`?

----

* :doc:`/code/make_tdd/code_make_python_tdd_sh`
* :doc:`/code/make_tdd/code_make_python_tdd_ps1`