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

If you are using a Windows computer, install `Windows Subsystem Linux`_

* click ``start``
* type ``PowerShell``, right click and select ``Run as administrator`` to open a terminal
* install `Windows Subsystem Linux`_ by typing

  .. code-block:: powershell

    wsl --install --distribution debian

* run these commands in a bash_ terminal to install python after installing Debian_ or any of the `Linux distributions`_

  .. code-block:: shell

    sudo apt update
    sudo apt full-upgrade --yes
    sudo apt install python3 python3-venv --yes

  run the rest of the commands in this chapter in a bash_ terminal

----

********************************************************************************************
setup
********************************************************************************************

* I open a terminal in the Integrated Development Environment (IDE) then use mkdir_ to make a directory for the project

  .. code-block:: shell

    mkdir magic

* and change directory to the project with the cd_ program

  .. code-block:: shell

    cd magic

  this is where all code for the project will stay

* I make child directories for the source code and tests

  .. code-block:: shell

    mkdir src tests

* then add empty files for the project

  .. admonition:: If you are using Windows without `Windows Subsystem Linux`_

    change ``touch`` to ``New-Item``

  - I make an empty file that will hold the source code for the program

    .. code-block:: shell

      touch src/magic.py

    touch_ is a program that makes an empty file when given a name

  - tests will stay in the ``tests`` folder to separate them from the source code (the actual program). I make an empty file called ``__init__.py`` in the ``tests`` folder to tell Python that it is a `python package`_

    .. code-block:: shell

      touch tests/__init__.py

    .. WARNING:: make sure you use two underscores for ``__init__.py``

  - then add one more empty file to the ``tests`` folder for the actual test

    .. code-block:: shell

      touch tests/test_magic.py

* Here is what the folder structure looks like

  .. code-block:: python

    magic
      ╰──src
        ╰──magic.py
      ╰──tests
      |  ╰──__init__.py
      |  ╰──test_magic.py

.. tip:: ``magic`` is a placeholder for the name of the project. For example, change ``magic`` to ``calculator`` to work on a ``calculator`` project

----

.. _test_failure:

********************************************************************************************
test_failure
********************************************************************************************

The Test Driven Development cycle is ``RED GREEN REFACTOR``

* **RED**: make it fail - write a failing test to make sure the test works
* **GREEN**: make it pass - write only what is needed to make the failing test pass
* **REFACTOR**: make it better

.. _test_failure_red:

red: make it fail
############################################################################################

* I open up ``magic/tests/test_magic.py`` in the Integrated Development Environment (IDE) and type this

    the line numbers below are a guide, you do not need to copy them

  .. code-block:: python
    :linenos:

    import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code above

  - ``import unittest`` imports the unittest_ :ref:`module<ModuleNotFoundError>` from the `python standard library`_. This :ref:`module<ModuleNotFoundError>` is used for testing
  - ``class TestMagic`` is the definition of a test :doc:`class </classes/classes>`

    * :doc:`class </classes/classes>` is the python keyword for making :doc:`/classes/classes`
    * ``TestMagic`` is the name given to the :doc:`class </classes/classes>` that will hold the tests, you can use any name you want as long as it starts with ``Test``
    * `unittest.TestCase`_ is a :doc:`class </classes/classes>` defined in the unittest_ :ref:`module<ModuleNotFoundError>` that contains :doc:`methods (functions) </functions/functions>` for testing
    * ``TestMagic`` inherits from `unittest.TestCase`_, it is a child or clone of `unittest.TestCase`_ that can do the same things it can

  - ``def test_failure`` is the definition of a test :ref:`method<functions>` to test the program I am making

    * def_ is the python keyword for making :ref:`functions (methods)<functions>`
    * ``test_failure`` is the name of the :ref:`method<functions>`,  you can use any name you want as long as it starts with ``test_``
    * ``self`` is the ``TestMagic`` :ref:`class<classes>`. I use ``self`` to access :doc:`methods (functions) </functions/functions>` and :ref:`attributes<AttributeError>` of the ``TestMagic`` class and by extension `unittest.TestCase`_, without having to type ``TestMagic().`` or ``unittest.TestCase().``
    * ``self.assertFalse(True)`` is the actual test. I expect this line to fail because :doc:`True </data_structures/booleans/booleans>` is not :doc:`False </data_structures/booleans/booleans>`

      - assertFalse_ is a :ref:`method<functions>` in the `unittest.TestCase`_ :doc:`class </classes/classes>` that checks if its input is :doc:`False </data_structures/booleans/booleans>`
      - :doc:`True </data_structures/booleans/booleans>` is given as input to ``assertFalse``

* I turn on the ``Auto Save`` feature in the Integrated Development Environment (IDE) to automatically save files when I make a change
* then type this in the terminal to run the test

  .. code-block:: python

    python3 -m unittest

  and the terminal shows a failure

  .. code-block:: python

    F
    ======================================================
    FAIL: test_failure (tests.TestMagic.test_failure)
    ------------------------------------------------------
    Traceback (most recent call last):
    File ".../magic/tests/test_magic.py", line 7, in test_failure
        self.assertFalse(True)
    AssertionError: True is not false

    ------------------------------------------------------
    Ran 1 test in 0.000s

    FAILED (failures=1)

If you are typing along, *CONGRATULATIONS!* You have written your first test.

This is the ``RED`` part of the Test Driven Development cycle. The error in the terminal has important information, reading from the bottom

* ``FAILED (failures=1)`` there is one failure
* ``Ran 1 test in 0.000s`` how long the test ran
* ``AssertionError: True is not false`` The error is an :ref:`AssertionError` which is raised because :doc:`True </data_structures/booleans/booleans>` is not :doc:`False </data_structures/booleans/booleans>`
* ``self.assertFalse(True)`` is the line of code that caused the failure
* ``File ".../magic/tests/test_magic.py", line 7, in test_failure`` is the line number and location of the file where the :ref:`AssertionError` happened

  .. tip::

    Hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click with your mouse on ``File ".../magic/tests/test_magic.py", line 7`` in the terminal and the Integrated Development Environment (IDE) will open the file in the editor and place the cursor on the line in the file where the error happened

* ``Traceback (most recent call last):`` all the indented information shown after this line is the ``traceback`` showing the calls python made that led to the error
* ``FAIL: test_failure (tests.TestMagic.test_failure)`` is a header with information in :doc:`dot notation</dot_notation>` about the test

  - ``tests.TestMagic.test_failure`` is the location of the failing test
  -  ``tests`` is the tests folder
  - ``TestMagic`` is the class defined on line 4
  - ``test_failure`` is the function defined on line 6

* ``F`` indicates a failure
* ``python3 -m unittest`` is the command to run tests with ``unittest``

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to run the :ref:`module<ModuleNotFoundError>` given after the option as a script
  - unittest_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_ used for testing

* I recommend you write down :doc:`Exceptions </how_to/exception_handling_programs>` you meet on this journey to become more familiar with them, it will help when you run into errors later. Time to add :ref:`AssertionError` to the list

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

I change the input on line 7 to :doc:`False </data_structures/booleans/booleans>`

.. code-block:: python

  self.assertFalse(False)

then run the test again from the terminal

.. code-block:: python

  python3 -m unittest

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

How can I make this better? I ran ``python3 -m unittest`` to see the test fail, again to see the test pass and will have to run it again anytime I change the code, to make sure tests that were passing are not broken and the new code does what I expect.
This means it is run for each part of the Test Driven Development cycle or any time there is a code change. I do not want to type ``python3 -m unittest`` again, it would be better for a program to run the tests so `I Do Not Repeat myself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

----

********************************************************************************************
how to automatically run tests
********************************************************************************************

how to make a Virtual Environment
############################################################################################

* I make a `virtual environment`_ with the venv_ :ref:`module<ModuleNotFoundError>` from the `python standard library`_

  .. code-block:: python

      python3 -m venv .venv

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to run the :ref:`module<ModuleNotFoundError>` given after the option as a script
  - venv_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_ for making a `virtual environment`_ with a given name
  - a `virtual environment`_ is a separate folder for dependencies of the project
  - ``.venv`` is the standard name for `virtual environments <https://docs.python.org/3/glossary.html#term-virtual-environment>`_ in Python, you can use any name you like

* I activate the `virtual environment`_ to use it ::

      source .venv/bin/activate

  .. admonition:: If you are using Windows without `Windows Subsystem Linux`_ type this instead

    .. code-block::

      .venv/scripts/activate.ps1

  the ``(.venv)`` on the far left of the command line in the terminal shows that the `virtual environment`_ is activated

  .. code-block:: shell

    (.venv) vscode ➜ .../magic $

* I upgrade pip_ the `python package manager`_ to the latest version

  .. code-block:: python

    pip install --upgrade pip

  - pip_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_ that installs `python packages`_
  - ``install`` is an argument given to pip_ to install a given package name
  - ``pip`` is the package name given for pip_ to install, in this case  ``pip`` installs ``pip``
  - ``--upgrade`` is an option given to the ``install`` argument for pip_ to install the latest version of the name given

* After upgrading, I use pip_ to see the packages that are already installed in the virtual environment

  .. code-block:: python

    pip list

  and the terminal shows

  .. code-block:: shell

    Package Version
    ------- -------
    pip     24.0

  your versions may vary

* I make a file called ``requirements.txt`` in the ``magic`` folder

  .. code-block:: shell

      echo "pytest-watch" > requirements.txt

  - the command above makes a file named ``requirements.txt`` with `pytest-watch`_ as the text inside it
  - echo_ is a program that writes its given arguments to the `standard output (stdout)`_
  - ``>`` is an operator that is used to send output from a program to the file given
  - `pytest-watch`_ is a python program that automatically runs pytest_ when a python file in the directory changes
  - pytest_ is a `python package`_ like unittest_ used for testing
  - ``requirements.txt`` is the name of a file where I can list `python packages`_ for pip_ the `python package manager`_ to install later, you can use any name you like

* then I install the `pytest-watch`_ package and its dependencies from the ``requirements.txt`` in the `virtual environment`_

  .. code-block:: python

      pip install --requirement requirements.txt

  - ``--requirement`` is another option that can be passed to the ``install`` argument to install `python packages`_ from a given file
  - ``requirements.txt`` is the file that contains a list of `python packages`_ for pip_ to install

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

    magic
      ╰──.venv
      ╰──tests
      |  ╰──__pycache__
      |  ╰──__init__.py
      |  ╰──test_magic.py
      ╰──magic.py
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

* I change the input on line 7 in ``test_magic.py`` to :doc:`True </data_structures/booleans/booleans>` to make it fail and back to :doc:`False </data_structures/booleans/booleans>` to make it pass with the terminal responding to each change
* I can press ``ctrl`` + ``c`` on the keyboard in the terminal to stop the tests at anytime

----

how to deactivate a virtual environment
#################################################################################################

type the following in a terminal with an active `virtual environment`_ ::

  deactivate

----

how to activate a virtual environment
############################################################################################

Make sure you are in the directory that contains the `virtual environment`_ for example ``magic`` and type the following in the terminal::

  source .venv/bin/activate

.. admonition:: If you are using Windows without `Windows Subsystem Linux`_

  You may need to Set the Execution Policy in Administrator mode first

  .. code-block:: PowerShell

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

  then activate the virtual environment

  .. code-block:: PowerShell

    .venv/scripts/activate.ps1

-----

********************************************************************************************
how to automatically make a python test driven development environment
********************************************************************************************

You made it this far and have become the greatest programmer in the world. To follow `The Do Not Repeat Yourself (DRY) Principle`_, I would write a program that contains all the steps it took to get here, then I can use it anytime I want to make a Test Driven Development Environment without having to remember each step

* I exit the tests in the terminal by pressing ``ctrl`` + ``c`` on the keyboard
* then type ``deactivate`` to leave the `virtual environment`_
* and change directory to the parent of ``magic`` ::

    cd ..

* I use the history_ program to list the commands I typed earlier in the terminal as a reference for the program ::

    history

* and make an empty file with a name that describes what the program does so it is easy to remember later, for example :ref:`makePythonTdd.sh` ::

    touch makePythonTdd.sh

* then open the file in the Integrated Development Environment (IDE) and copy each command I need to set up a Test Driven Environment

  .. code-block:: ruby

    #!/bin/bash
    mkdir --parents magic/tests
    cd magic
    touch magic.py
    touch tests/__init__.py
    touch tests/test_magic.py
    echo "pytest-watch" > requirements.txt
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  ``#!/bin/bash`` is a shebang_ line that tells the computer to use bash_ to run the program. You can change it to ``#!/bin/zsh`` if you have zsh_ installed

* This program will always make a project called ``magic``. I add a variable called ``PROJECT_NAME`` that is referenced with ``$PROJECT_NAME`` to make it possible to make any project name I give

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

  ``$1`` represents the first argument given when the program is called. You can use it in place of ``$PROJECT_NAME`` and will get the same result

* I use the `cat <https://www.man7.org/linux/man-pages/man1/cat.1.html>`_ program to add text for the first failing test in ``test_$PROJECT_NAME.py``

    the line numbers below are a guide, you do not need to copy them

  .. literalinclude:: /code/make_tdd/makePythonTdd.sh
    :language: shell
    :linenos:

  all the text between the two ``DELIMITER`` words will be written to ``tests/test_$PROJECT_NAME.py``

* I use chmod_ to make the program executable ::

    chmod +x makePythonTdd.sh

  chmod_ is a program that changes the mode of the file given

* I can make a Test Driven Development environment any time I want by giving a name for the ``PROJECT_NAME`` variable when the program is called. For example, typing this command in the terminal in the folder where ``makePythonTdd.sh`` is saved will make a Test Driven Development environment for a project called ``calculator``, you can continue this in :doc:`/how_to/calculator` ::

    ./makePythonTdd.sh calculator

----

how to automatically make a python test driven development environment on windows without WSL
#################################################################################################

.. warning::

  This section only applies if you are using Windows without `Windows Subsystem Linux`_

* I make a file named :ref:`makePythonTdd.ps1` by using the ``New-Item`` command in PowerShell ::

    New-Item makePythonTdd.ps1

* and open the file in the Integrated Development Environment's Editor then add the following code

    the line numbers below are a guide, you do not need to copy them

  .. literalinclude:: /code/make_tdd/makePythonTdd.ps1
    :linenos:
    :language: PowerShell

* I can make a Test Driven Development environment anytime I want by giving a name for the ``PROJECT_NAME`` variable when the program is called. For example, typing this command in the terminal in the folder where ``makePythonTdd.ps1`` is saved will make a Test Driven Development environment for a project called ``calculator``, you can continue this in :doc:`/how_to/calculator` ::

    ./makePythonTdd.ps1 calculator

----

********************************************************************************************
review
********************************************************************************************

One of the advantages of programming is that I can take some steps and make them a one line command that the computer does for me.

You now know one way to make a Python Test Driven Development Environment, and have a program to do it for you anytime you want.

Would you like to test :doc:`/how_to/calculator`?

----

* :doc:`/code/make_tdd/code_make_python_tdd_sh`
* :doc:`/code/make_tdd/code_make_python_tdd_ps1`