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

  - `Visual Studio Code <https://code.visualstudio.com/download>`_
  - `PyCharm Community Edition <https://www.jetbrains.com/pycharm/download>`_
  - `Sublime Text <https://www.sublimetext.com>`_
  - `Other Integrated Development Environment (IDE) options <https://wiki.python.org/moin/IntegratedDevelopmentEnvironments>`_

windows requirements
#################################################################################

If the operating system of your computer is Windows, use `Windows Subsystem Linux`_

* click ``start``
* type ``PowerShell`` and click to open a terminal
* install `Windows Subsystem Linux`_ by typing the following in a PowerShell_ terminal

  .. code-block:: powershell

    wsl --install --distribution debian

* after installation run the following in a bash_ terminal to install python

  .. code-block:: shell

    sudo apt update
    sudo apt full-upgrade --yes
    sudo apt install python3 python3-venv --yes

* run the rest of the commands in this chapter in a bash_ terminal

----

********************************************************************************************
setup
********************************************************************************************

I open a terminal in the Integrated Development Environment (IDE) and type the following commands to make the project

* I use mkdir_ with the ``-p/--parents`` option to make a directory for the project with a child directory called ``tests`` inside it

  .. code-block:: shell

    mkdir --parents project_name/tests

  NOTE::

    if ``--parents`` does not work, try ``-p`` instead

* I change directory to ``project_name`` with the cd_ program

  .. code-block:: shell

      cd project_name

  this is where all the code for the project will stay

* touch_ is a program which makes an empty file when given a name

  .. admonition:: If you are using Windows without `Windows Subsystem Linux`_

    change ``touch`` to ``New-Item``

  - I make an empty file called ``project_name.py`` to hold the source code for the program

    .. code-block:: shell

        touch project_name.py

    tests will be stored in the ``tests`` folder to separate them from the source code (the actual program)

  - I make another empty file called ``__init__.py`` in the ``tests`` folder to tell Python that the ``tests`` folder is a python package_

    .. code-block:: shell

        touch tests/__init__.py

    .. WARNING:: make sure you use two underscores for ``__init__.py``

  - I make one more empty file called ``test_project_name.py`` in the ``tests`` folder

    .. code-block:: shell

        touch tests/test_project_name.py

* Here is what the folder structure looks like

  .. code-block:: python

    project_name
      ╰──tests
      |  ╰──__init__.py
      |  ╰──test_project_name.py
      ╰──project_name.py

.. tip:: ``project_name`` is a placeholder for the name of the project. For example to make a project called ``magic``, I would change ``project_name`` to ``magic``

----

.. _test_failure:

********************************************************************************************
test_failure
********************************************************************************************

The Test Driven Development cycle is ``RED GREEN REFACTOR``

* **RED**: make it fail - write a failing test to make sure the test works
* **GREEN**: make it pass - write only what is needed to make the test pass
* **REFACTOR**: make it better

.. _test_failure_red:

red: make it fail
############################################################################################

* I open up ``project_name/tests/test_project_name.py`` in the Integrated Development Environment (IDE) and type the following

    the line numbers below are a guide, you do not need to copy them

  .. code-block:: python
    :linenos:

    import unittest


    class TestProjectName(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code above

  - ``import unittest`` imports unittest_ which is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_ used for testing
  - ``TestProjectName`` is a :doc:`class </classes/classes>` that will hold tests
  - :doc:`class </classes/classes>` is the python keyword for making :doc:`/classes/classes`
  - `unittest.TestCase`_ is a :doc:`class </classes/classes>` defined in the unittest_ :ref:`module<ModuleNotFoundError>` which contains :doc:`methods (functions) </functions/functions>` for testing
  - ``TestProjectName`` inherits from `unittest.TestCase`_, it is a child or clone of `unittest.TestCase`_ that can do the same things as `unittest.TestCase`_
  - ``def test_failure`` is the definition of a test :ref:`method<functions>` to test the program I am making

    * def_ is the python keyword for making :ref:`functions (methods)<functions>`
    * ``test_failure`` is the name of the :ref:`method<functions>`
    * ``self`` is the ``TestProjectName`` :ref:`class<classes>`. I can use ``self`` to access :doc:`methods (functions) </functions/functions>` and :ref:`attributes<AttributeError>` of the ``TestProjectName`` class, without having to type ``TestProjectName().assertFalse(True)`` to access the ``assertFalse`` :ref:`method<functions>`
    * ``self.assertFalse(True)`` is the actual test. I expect this line to fail because :doc:`True </data_structures/booleans/booleans>` is not :doc:`False </data_structures/booleans/booleans>`

      - assertFalse_ is a :ref:`method<functions>` in the `unittest.TestCase`_ :doc:`class </classes/classes>` that checks if its input is :doc:`False </data_structures/booleans/booleans>` and raises an :ref:`AssertionError` when it is not
      - :doc:`True </data_structures/booleans/booleans>` is given as input to ``assertFalse``

* I save the file and turn on the ``Auto Save`` feature in the Integrated Development Environment (IDE) to automatically save files when I make a change
* I type this in the terminal to test the code

  .. code-block:: python

    python3 -m unittest

  the terminal shows a failure

  .. code-block:: python

    F
    ======================================================
    FAIL: test_failure (tests.TestProjectName.test_failure)
    ------------------------------------------------------
    Traceback (most recent call last):
    File ".../project_name/tests/test_project_name.py", line 7, in test_failure
        self.assertFalse(True)
    AssertionError: True is not false

    ------------------------------------------------------
    Ran 1 test in 0.000s

    FAILED (failures=1)

If you are typing along, *CONGRATULATIONS!* You have written your first test.

This is the ``RED`` part of the Test Driven Development cycle. The error in the terminal has important information. I like to read it from the bottom to the top

* ``FAILED (failures=1)`` there is one failure
* ``Ran 1 test in 0.000s`` how long it took the test to run
* ``AssertionError: True is not false`` The error is an :ref:`AssertionError` which is raised by python when an assert statement is :doc:`False </data_structures/booleans/booleans>`. In this case the error is raised because ``True is not false``
* ``self.assertFalse(True)`` is the line of code that caused the failure

  - ``assertFalse`` is a :ref:`method<functions>` in the `unittest.TestCase`_ :doc:`class </classes/classes>` which checks if its input is :doc:`False </data_structures/booleans/booleans>`
  - :doc:`True </data_structures/booleans/booleans>` is given as input to ``assertFalse`` and the statement raises an :ref:`AssertionError` because :doc:`True </data_structures/booleans/booleans>` is not :doc:`False </data_structures/booleans/booleans>`

* ``File ".../project_name/tests/test_project_name.py", line 7, in test_failure`` is the line number and location of the file where the :ref:`AssertionError` occurred.

  .. tip::

    Hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click with your mouse on ``File ".../project_name/tests/test_project_name.py", line 7, in test_failure`` in the terminal and the Integrated Development Environment (IDE) will place the cursor at the position in the file where the error occurred

* ``Traceback (most recent call last):`` all the indented information shown after this line is the ``traceback`` showing the most recent call python made last
* ``FAIL: test_failure (tests.TestProjectName.test_failure)`` is a header with information about the test

  - ``tests.TestProjectName.test_failure`` is the location of the failing test
  -  ``tests`` is the tests folder
  - ``TestProjectName`` is the class defined on line 4
  - ``test_failure`` is the function defined on line 6

* ``F`` indicates a failure
* ``python3 -m unittest`` is the command to run tests with ``unittest``

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to call a :ref:`module<ModuleNotFoundError>` given after the option
  - unittest_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_ used for testing

* I write down :doc:`Exceptions </how_to/exception_handling_programs>` I encounter to become more familiar with them. Time to add :ref:`AssertionError` to the list

  .. code-block:: python

    import unittest


    class TestProjectName(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

    # Exceptions Encountered
    # AssertionError

.. _test_failure_green:

green: make it pass
#################################################################################

I change the input on line 7 to :doc:`False </data_structures/booleans/booleans>`

.. code-block:: python

  self.assertFalse(False)

then run the test again from the terminal

.. code-block:: python

  python3 -m unittest

and the terminal shows a passing test

.. code-block:: python

  .
  ------------------------------------------------------
  Ran 1 test in 0.000s

  OK

*cue CELEBRATION MUSIC AND DANCE!* I am GREEN.

.. _test_failure_refactor:

refactor: make it better
#################################################################################

I can make code better by using

* `The Abstraction Principle`_ or
* `The Do Not Repeat Yourself (DRY) Principle`_

So far there is not much to improve on what has been written but there has been repetition

* ``python3 -m unittest`` was run to see the test fail
* ``python3 -m unittest`` was run to see the test pass
* ``python3 -m unittest`` will be run anytime I make a change to make sure it does not break tests that already passed

This means ``python3 -m unittest`` is run for each part of the Test Driven Development cycle or each time there is a code change. I automate this so `I Do Not Repeat myself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_, it would be better for a program to automatically run the tests when there is a change to the code

----

********************************************************************************************
how to automatically run tests
********************************************************************************************

how to make a Virtual Environment
############################################################################################

* I make a file called ``requirements.txt`` in the ``project_name``

  .. code-block:: shell

      echo "pytest-watch" > requirements.txt

  - the command above makes a file named ``requirements.txt`` with `pytest-watch`_ as the text inside it
  - echo_ is a program that writes its given arguments to the standard output
  - ``>`` is an operator that is used to send output from a program to the file given
  - `pytest-watch`_ is a python program that automatically runs the pytest_ python package when a python file in the project changes
  - pytest_ is a python package like unittest_ for running tests in Python
  - ``requirements.txt`` is the name of a file where I list required python packages for pip_ the `python package manager`_ to install later, you can use any name you like

* I make a `virtual environment`_ with the venv_ :ref:`module<ModuleNotFoundError>` from the `python standard library`_

  .. code-block:: python

      python3 -m venv .venv

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to call the :ref:`module<ModuleNotFoundError>` given after the option
  - venv_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_ for making a `virtual environment`_ when given a name
  - a `virtual environment`_ is a separate folder for dependencies of the project
  - ``.venv`` is the standard name for `virtual environments <https://docs.python.org/3/glossary.html#term-virtual-environment>`_ in Python, you can use any name you like

* I activate the `virtual environment`_ to use it ::

      source .venv/bin/activate

  .. admonition:: If you are using Windows without `Windows Subsystem Linux`_ type this instead

    .. code-block::

      .venv/scripts/activate

  the ``(.venv)`` on the far left of the command line in the terminal shows that the `virtual environment`_ is activated

  .. code-block:: shell

    (.venv) vscode ➜ .../project_name $

* I upgrade pip_ the `python package manager`_ to the latest version

  .. code-block:: python

      python3 -m pip install --upgrade pip

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to call the :ref:`module<ModuleNotFoundError>` given after the option
  - pip_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_ for installing python packages
  - ``install`` is an argument given to pip_ to install a given package name
  - ``pip`` is the package name given for pip_ to install, in this case  ``pip`` installs ``pip``
  - ``--upgrade`` is an option given to the ``install`` argument for pip_ to install the latest version of the name given

* After upgrading, I use pip_ to see the packages that are already installed in the virtual environment

  .. code-block:: python

    python3 -m pip list

  and the terminal shows

  .. code-block:: shell

    Package Version
    ------- -------
    pip     24.0

  you versions may vary

* then I install the `pytest-watch`_ from the ``requirements.txt`` in the `virtual environment`_

  .. code-block:: python

      python3 -m pip install --requirement requirements.txt

  - ``--requirement`` is another option that can be passed to the ``install`` argument to install python packages from a given file
  - ``requirements.txt`` is the file that contains a list of libraries for pip_ to install

* I use pip_ to see the packages that are now installed

  .. code-block:: python

    pip list

  and the terminal shows this

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

* The folder structure now looks like this

  .. code-block:: python

    project_name
      ╰──.venv
      ╰──tests
      |  ╰──__pycache__
      |  ╰──__init__.py
      |  ╰──test_project_name.py
      ╰──project_name.py
      ╰──requirements.txt

* When I type ``pytest-watch`` in the terminal, the test runs and it shows results without going back to the command line

  .. code-block:: ruby

    [TODAYS_DATE] Running: py.test
    ================== test session starts===================
    ...
    rootdir: .../project_name
    collected 1 item

    tests/test_project_name.py .          [100%]

    =============== 1 passed in 0.00s =======================

* I make the input on line 7 in ``test_project_name.py`` to :doc:`True </data_structures/booleans/booleans>` to make it fail and back to :doc:`False </data_structures/booleans/booleans>` to make it pass with the terminal responding to each change
* I can press ``ctrl`` + ``c`` on the keyboard in the terminal to stop the tests at anytime

----

how to deactivate a virtual environment
############################################################################################

type the following in a terminal with an active `virtual environment`_ ::

  deactivate

----

how to activate a virtual environment
############################################################################################

Make sure you are in the directory that contains the `virtual environment`_ for example ``project_name`` and type the following in the terminal::

  source .venv/bin/activate

.. admonition:: If you are using Windows without `Windows Subsystem Linux`_

  .. code-block::

    .venv/scripts/activate

-----

********************************************************************************************
how to automatically make a python test driven development environment
********************************************************************************************

You made it this far and have become the greatest programmer in the world. Following the `The Do Not Repeat Yourself (DRY) Principle`_, I would write a program that contains all the steps above. I can then use it to make a Test Driven Development Environment any time I want without having to remember each step of the process

* I exit the tests in the terminal by pressing ``ctrl`` + ``c`` on the keyboard
* I type ``deactivate`` to deactivate the `virtual environment`_
* I change directory to the parent of ``project_name`` ::

    cd ..

* I use the history_ program to list the commands I typed earlier in the terminal as a reference for the program ::

    history

* I make an empty file with a name that describes what the program does so it is easy to remember later, for example :ref:`makePythonTdd.sh` ::

    touch makePythonTdd.sh

* I open the file in the Integrated Development Environment (IDE) and copy each command shown in the terminal from ``history`` except ``python3 -m unittest`` since I want the tests to run automatically

  .. code-block:: ruby

    #!/bin/bash
    mkdir --parents project_name/tests
    cd project_name
    touch project_name.py
    touch tests/__init__.py
    touch tests/test_project_name.py
    echo "pytest-watch" > requirements.txt
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  ``#!/bin/bash`` is a shebang_ line that tells the computer to use bash_ to run the program

* This program will always make a project called ``project_name`` so I need to add a variable to make any project name I pass to the program as input. I add a variable called ``PROJECT_NAME`` which is referenced with ``$PROJECT_NAME``

  .. code-block:: shell

    #!/bin/bash
    PROJECT_NAME=$1
    mkdir --parents $PROJECT_NAME/tests
    cd $PROJECT_NAME
    touch $PROJECT_NAME.py
    touch tests/__init__.py
    touch tests/test_$PROJECT_NAME.py

    echo "pytest-watch" > requirements.txt

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install --requirement requirements.txt
    pytest-watch

* I use the `cat <https://www.man7.org/linux/man-pages/man1/cat.1.html>`_ program to add text for the first failing test in ``test_$PROJECT_NAME.py``

    the line numbers below are a guide, you do not need to copy them

  .. literalinclude:: /code/make_tdd/makePythonTdd.sh
    :language: shell
    :linenos:

  all the text between the two ``DELIMITER`` words will be written to ``tests/test_$PROJECT_NAME.py``

* I use `chmod <https://man7.org/linux/man-pages/man1/chmod.1.html>`_ to make the program executable ::

    chmod +x makePythonTdd.sh

* I can make a Test Driven Development environment any time I want by giving a name for the ``PROJECT_NAME`` variable when the program is called. For example, typing this command in the terminal in the folder where ``makePythonTdd.sh`` is saved will make a Test Driven Development environment for a project called ``calculator``, you can continue this in :doc:`/how_to/calculator` ::

    ./makePythonTdd.sh calculator

----

how to automatically make a python test driven development environment on windows without WSL
###################################################################################################

.. warning::

  This section only applies if you are using Windows without `Windows Subsystem Linux`_

* I make a file named :ref:`makePythonTdd.ps1` by using the ``New-Item`` command in PowerShell ::

    New-Item makePythonTdd.ps1

* I open the file in the Interactive Development Editor then add the following code

    the line numbers below are a guide, you do not need to copy them

  .. literalinclude:: /code/make_tdd/makePythonTdd.ps1
    :linenos:
    :language: PowerShell

  ``#!/usr/bin/pwsh`` is a shebang_ line that tells the computer to use the PowerShell_ shell to run the program

* I can make a Test Driven Development environment anytime I want by giving a name for the ``PROJECT_NAME`` variable when the program is called. For example, typing this command in the terminal in the folder where ``makePythonTdd.ps1`` is saved will make a Test Driven Development environment for a project called ``calculator``, you can continue this in :doc:`/how_to/calculator` ::

    ./makePythonTdd.ps1 calculator

----

********************************************************************************************
review
********************************************************************************************

One of the advantages of programming is that I can take a series of steps and make them a one line command which the computer does for me.

You now know one way to make a Test Driven Development Environment for Python projects, and have a program to do it for you anytime you want

Would you like to test :doc:`/how_to/calculator`?

----

* :doc:`/code/make_tdd/code_make_python_tdd_sh`
* :doc:`/code/make_tdd/code_make_python_tdd_ps1`