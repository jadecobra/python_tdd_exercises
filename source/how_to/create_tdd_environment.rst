
####################################################
How to create a Test Driven Development Environment
####################################################

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/QRIO98ofeFM?si=y4VchKPNr7mzeTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

`Test Driven Development <https://en.wikipedia.org/wiki/Test-driven_development>`_ is a way of developing software with a focus on tests. I write tests for ideas to reach a goal or meet a requirement, and the results of the tests tell me if I am closer or further away from the goal. The process is repeated until I reach the goal.

I recommend reading `Kent Beck’s <https://en.wikipedia.org/wiki/Kent_Beck>`_ `Test Driven Development by Example <https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530/?_encoding=UTF8&pd_rd_w=dbNYL&content-id=amzn1.sym.579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_p=579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_r=133-9769820-0728336&pd_rd_wg=bMVBp&pd_rd_r=c84a5de8-ec36-4bd1-9196-8fa05de41794&ref_=aufs_ap_sc_dsk>`_ and `Martin Fowler’s <https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer)>`_ `Refactoring <https://www.amazon.com/Refactoring-Improving-Existing-Addison-Wesley-Signature/dp/0134757599/?_encoding=UTF8&pd_rd_w=dbNYL&content-id=amzn1.sym.579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_p=579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_r=133-9769820-0728336&pd_rd_wg=bMVBp&pd_rd_r=c84a5de8-ec36-4bd1-9196-8fa05de41794&ref_=aufs_ap_sc_dsk>`_, they both influenced the way I write programs.

This chapter covers one way to create a Python Test Driven Development environment

***************
Requirements
***************

* download and install `Python <https://www.python.org/downloads/>`_
* An Interactive Development Environment (IDE). Here are a few options

  - `Visual Studio Code in a Browser <http://vscode.dev>`_
  - `Visual Studio Code <https://code.visualstudio.com/download>`_ on your computer
  - `PyCharm Community Edition <https://www.jetbrains.com/pycharm/download>`_
  - `Sublime <https://www.sublimetext.com>`_
  - `Other Interactive Development Environment (IDE) options <https://wiki.python.org/moin/IntegratedDevelopmentEnvironments>`_

.. admonition:: *are you on a windows computer?*

  * click ``start``
  * type ``PowerShell`` and click to open a terminal
  * install `Windows Subsystem for Linux <https://learn.microsoft.com/en-us/windows/wsl/install>`_ by typing the following in the terminal

    .. code-block:: powershell

      wsl --install

  * run subsequent commands in `Windows Subsystem for Linux <https://learn.microsoft.com/en-us/windows/wsl/install>`_
  * if you cannot use `Windows Subsystem for Linux <https://learn.microsoft.com/en-us/windows/wsl/install>`_, replace ``touch`` with ``New-Item``

*******
Setup
*******

I open a terminal in the Interactive Development Environment (IDE) and type the following commands to create the project

* I use `mkdir <https://man7.org/linux/man-pages/man1/mkdir.1.html>`_ with the ``--parents`` option to create a directory for the project with a child directory called ``tests`` inside it

  .. code-block:: shell

    mkdir --parents project_name/tests

* I change directory to ``project_name`` with the `cd <https://man7.org/linux/man-pages/man1/cd.1p.html>`_ program

  .. code-block:: shell

      cd project_name

  this is where all the code for the project will stay

* `touch <https://man7.org/linux/man-pages/man1/touch.1.html>`_ is a program which creates an empty file when given a name

  - I use it to create an empty file called ``project_name.py`` to hold the source code for the program

    .. code-block:: shell

        touch project_name.py

  - tests will be stored in the ``tests`` folder to separate them from the source code (the actual program)
  - I create an empty file called ``__init__.py`` in the ``tests`` folder to tell python that the ``tests`` folder is a python `package <https://docs.python.org/3/glossary.html#term-regular-package>`_

    .. code-block:: shell

        touch tests/__init__.py

    .. NOTE::

      make sure you use two underscores for ``__init__.py``

  - I create another empty file called ``test_project_name.py`` in the ``tests`` folder to hold the tests

    .. code-block:: shell

        touch tests/test_project_name.py

* Here is what the folder structure looks like

  .. code-block:: python

    project_name
      ╰──tests
      |  ╰──__init__.py
      |  ╰──test_project_name.py
      ╰──project_name.py

.. note::

  ``project_name`` is a placeholder for the name of the project. For example to create a project called ``calculator`` I would replace ``project_name`` with ``calculator``

----


The Test Driven Development cycle is ``RED GREEN REFACTOR``

* **RED**: make it fail - write a failing test to make sure the test works
* **GREEN**: make it pass - write only what is needed to make the test pass
* **REFACTOR**: make it better

******************
RED: make it fail
******************


* I open up ``project_name/tests/test_project_name.py`` in the Interactive Development Environment (IDE) and type the following

  .. code-block:: python
    :linenos:

    import unittest


    class TestProjectName(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code above

  - ``import unittest`` imports the `unittest <https://docs.python.org/3/library/unittest.html>`_ module
  - `unittest <https://docs.python.org/3/library/unittest.html>`_ is a module from the `python standard library <https://docs.python.org/3/tutorial/stdlib.html?highlight=standard%20library>`_ used for testing
  - ``TestProjectName`` is a :doc:`class </classes/classes>` that will hold tests

    * `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is the python keyword for creating :doc:`/classes/classes`

  - `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ is a :doc:`class </classes/classes>` defined in the `unittest <https://docs.python.org/3/library/unittest.html>`_ module which contains :doc:`methods (functions) </functions/functions>` for testing.
  - ``TestProjectName`` inherits from `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_. A simple way to think of inheritance is that ``TestProjectName`` is a child of `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ and can do the same things it can
  - ``def test_failure`` is the definition of a test :doc:`method </functions/functions>` to test the program I am creating

    * `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is the python keyword for creating :doc:`/functions/functions`
    * ``test_failure`` is the name of the :doc:`function </functions/functions>`
    * ``self`` is the ``TestProjectName`` class. I can use ``self`` to access :doc:`methods (functions) </functions/functions>` and ``attributes`` within the ``TestProjectName`` class, this avoids having to type ``TestProjectName().assertFalse(True)`` to access the ``assertFalse`` :doc:`method </functions/functions>`
    * ``self.assertFalse(True)`` is the actual test. I expect this line to fail because :doc:`True </data_structures/booleans>` is not :doc:`False </data_structures/booleans>`

      - ``assertFalse`` is a :doc:`method </functions/functions>` in the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ class which checks if its input is :doc:`False </data_structures/booleans>`
      - :doc:`True </data_structures/booleans>` is given as input to ``assertFalse``

* I save the file and turn on the ``Auto Save`` feature in the Interactive Development Environment (IDE) to automatically save a file when I make a change
* I type this in the terminal to test the code ::

    python3 -m unittest

  the terminal shows a failure ::

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

This is the ``RED`` part of the Test Driven Development cycle. The error in the terminal has important information. I read it from the bottom to the top


* ``FAILED (failures=1)`` there is one failure
* ``Ran 1 test in 0.000s`` how long it took the test to run
* ``AssertionError: True is not false`` The error is an :doc:`/exceptions/AssertionError` which is raised by python when an assert statement is :doc:`False </data_structures/booleans>`. In this case the error is raised because ``True is not false``
* ``self.assertFalse(True)`` is the line of code that caused the failure

  - ``assertFalse`` is a :doc:`method </functions/functions>` in the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ :doc:`class </classes/classes>` which checks if its input is :doc:`False </data_structures/booleans>`
  - :doc:`True </data_structures/booleans>` is given as input to ``assertFalse`` and the statement raises an :doc:`/exceptions/AssertionError` because :doc:`True </data_structures/booleans>` is not :doc:`False </data_structures/booleans>`

* ``File ".../project_name/tests/test_project_name.py", line 7, in test_failure`` is the line number and location of the file where the :doc:`/exceptions/AssertionError` occurred.

  .. tip::

    Hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click with your mouse on ``File ".../project_name/tests/test_project_name.py", line 7, in test_failure`` in the terminal and the Interactive Development Environment (IDE) will place the cursor at the position in the file where the error occurred

* ``Traceback (most recent call last):`` all the information shown indented after this line is the ``traceback`` showing the most recent call python made last
* ``FAIL: test_failure (tests.TestProjectName.test_failure)`` is a header with information about the test

  - ``tests.TestProjectName.test_failure`` is the location of the failing test
  -  ``tests`` is the tests folder
  - ``TestProjectName`` is the class defined on line 4
  - ``test_failure`` is the function defined on line 6

* ``F`` indicates a failure
* ``python3 -m unittest`` is the command to run tests with ``unittest``

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to call a module given after the option
  - `unittest <https://docs.python.org/3/library/unittest.html>`_ is a module from the `python standard library <https://docs.python.org/3/tutorial/stdlib.html?highlight=standard%20library>`_ used for testing

********************
GREEN: make it pass
********************


* I write down :doc:`Exceptions </how_to/exception_handling_programs>` I encounter to become more familiar with them. I add :doc:`/exceptions/AssertionError` to the list

  .. code-block:: python
    :linenos:

    import unittest


    class TestProjectName(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

    # Exceptions Encountered
    # AssertionError

* I change the input on line 7 to make the test pass

  .. code-block:: python

    self.assertFalse(False)

* then run the test again from the terminal

  .. code-block:: python

    python3 -m unittest

  and the terminal shows a passing test

  .. code-block:: python

    .
    ------------------------------------------------------
    Ran 1 test in 0.000s

    OK

  *cue CELEBRATION MUSIC AND DANCE!* I am GREEN.

*************************
REFACTOR: make it better
*************************

I can make code better by using

* `The Abstraction Principle <https://en.wikipedia.org/wiki/Abstraction_principle_(computer_programming)>`_ or
* `The Do Not Repeat Yourself (DRY) Principle <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

So far there is not much to improve on what has been written but there has been repetition

* ``python3 -m unittest`` was run to see the test fail
* ``python3 -m unittest`` was run to see the test pass
* ``python3 -m unittest`` will be run again to make sure changes do not break previous passing tests

This means ``python3 -m unittest`` is run for each part of the Test Driven Development cycle or each time there is a code change. I automate this so `I Do Not Repeat myself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_, it would be better for a program to automatically run the tests when there is a change to the code

*********************************
How to Automatically Run Tests
*********************************

How to create a Virtual Environment
====================================

* With the `echo <https://man7.org/linux/man-pages/man1/echo.1.html>`_ program I create a file called ``requirements.txt`` in the ``project_name`` folder with `pytest-watch <https://pypi.org/project/pytest-watch/>`_ as the text

  .. code-block:: shell

      echo "pytest-watch" > requirements.txt

  - the command above creates a file named ``requirements.txt`` with `pytest-watch <https://pypi.org/project/pytest-watch/>`_ as the text inside it
  - `echo <https://man7.org/linux/man-pages/man1/echo.1.html>`_ is a program that writes its given arguments to the standard output
  - ``>`` is an operator that is used to send output from a program to the file given
  - `pytest-watch <https://pypi.org/project/pytest-watch/>`_ is a python program that automatically runs the `pytest <https://docs.pytest.org/>`_ python package when a python file in the project changes
  - `pytest <https://docs.pytest.org/>`_ is a python package like `unittest <https://docs.python.org/3/library/unittest.html>`_ for running tests in Python
  - ``requirements.txt`` is the name of a file where I can list required python packages for `pip <https://pypi.org/project/pip/>`_ the `python package manager <https://pypi.org/project/pip/>`_ to install later, you can use any name you like

* I create a virtual environment with the `venv <https://docs.python.org/3/library/venv.html#module-venv>`_ module from the `python standard library <https://docs.python.org/3/tutorial/stdlib.html?highlight=standard%20library>`_

  .. code-block:: python

      python3 -m venv .venv

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to call the module given after the option
  - `venv <https://docs.python.org/3/library/venv.html#module-venv>`_ is a module from the `python standard library <https://docs.python.org/3/tutorial/stdlib.html?highlight=standard%20library>`_ for creating virtual environments when given a name
  - a virtual environment is a separate folder for dependencies of the project
  - ``.venv`` is the standard name for virtual environments in Python, you can use any name you like

* I activate the virtual environment to use it ::

      source .venv/bin/activate

  .. NOTE::

    if you are on a windows machine and not using `Windows Subsystem for Linux <https://learn.microsoft.com/en-us/windows/wsl/install>`_, use ::

      .venv/scripts/activate

  the ``(.venv)`` on the far left of the command line in the terminal indicates the virtual environment is activated ::

    (.venv) vscode ➜ .../project_name $

* I upgrade `pip <https://pypi.org/project/pip/>`_ the `python package manager <https://pypi.org/project/pip/>`_ to the latest version

  .. code-block:: python

      python3 -m pip install --upgrade pip

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to call the module given after the option
  - `pip <https://pypi.org/project/pip/>`_ is a module from the `python standard library <https://docs.python.org/3/tutorial/stdlib.html?highlight=standard%20library>`_ for installing python packages
  - ``install`` is an argument given to `pip <https://pypi.org/project/pip/>`_ to install a given package name
  - ``pip`` is the package name given for `pip <https://pypi.org/project/pip/>`_ to install, in this case  ``pip`` installs ``pip``
  - ``--upgrade`` is an option given to the ``install`` argument for `pip <https://pypi.org/project/pip/>`_ to install the latest version of the name given

* After upgrading, I use `pip <https://pypi.org/project/pip/>`_ to install any python packages listed in ``requirements.txt`` in the virtual environment. In this case `pip <https://pypi.org/project/pip/>`_ will install ``pytest-watch``

  .. code-block:: python

      pip install --requirement requirements.txt

  - ``--requirement`` is another option that can be passed to the ``install`` argument to install python packages from a given file
  - ``requirements.txt`` is the file that contains a list of libraries for `pip <https://pypi.org/project/pip/>`_ to install

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

* I type ``pytest-watch`` in the terminal to run the tests and it shows results without going back to the command line

  .. code-block:: ruby

    [TODAYS_DATE] Running: py.test
    ================== test session starts===================
    ...
    rootdir: .../project_name
    collected 1 item

    tests/test_project_name.py .          [100%]

    =============== 1 passed in 0.00s =======================

* I change the input on line 7 in ``test_project_name.py`` to :doc:`True </data_structures/booleans>` to make it fail and back to :doc:`False </data_structures/booleans>` to make it pass and the terminal responds to each change
* I can press ``ctrl`` + ``c`` on the keyboard in the terminal to stop the tests at anytime

How to Deactivate a Virtual Environment
========================================

type the following in a terminal with an active virtual environment ::

  deactivate

How to Activate a Virtual Environment
========================================

Make sure you are in the directory that contains the virtual environment for example ``project_name`` and type the following in the terminal::

  source .venv/bin/activate

on a windows computer that is not using `Windows Subsystem for Linux <https://learn.microsoft.com/en-us/windows/wsl/install>`_ ::

  .venv/scripts/activate

-----

******************************************************************************
BONUS: Automatically create a Python Test Driven Development Environment
******************************************************************************

You made it this far and have become the greatest programmer in the world. Following the `The Do Not Repeat Yourself (DRY) Principle <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_, I would write a program that contains all the steps above. I can then use it to create a Test Driven Development Environment any time I want without having to remember each step of the process

* I exit the tests in the terminal by pressing ``ctrl`` + ``c`` on the keyboard
* I type ``deactivate`` to deactivate the virtual environment
* I change directory to the parent of ``project_name`` ::

    cd ..

* I use the `history <https://man7.org/linux/man-pages/man3/history.3.html>`_ program to list the commands I typed earlier in the terminal as a reference for the program ::

    history

* I create an empty file with a name that describes what the program does so it is easy to remember later, for example ``createPythonTdd.sh`` ::

    touch createPythonTdd.sh

* I open ``createPythonTdd.sh`` in the Interactive Development Environment (IDE) and copy each command displayed in the terminal from ``history`` except ``python3 -m unittest`` since I want the tests to run automatically

  .. code-block:: ruby
    :linenos:

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

* This program will always create a project called ``project_name`` so I need to add a variable to make it create any project name I pass to the program as input. I add a variable called ``PROJECT_NAME`` which is referenced with ``$PROJECT_NAME``

  .. code-block:: shell
    :linenos:

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

* I use the `cat <https://www.man7.org/linux/man-pages/man1/cat.1.html>`_ program to add text for the failure test in ``test_$PROJECT_NAME.py``

  .. code-block:: shell
    :linenos:

    PROJECT_NAME=$1
    mkdir --parents $PROJECT_NAME/tests
    cd $PROJECT_NAME
    touch $PROJECT_NAME.py
    touch tests/__init__.py

    cat << DELIMITER > tests/test_$PROJECT_NAME.py
    import unittest


    class Test$PROJECT_NAME(unittest.TestCase):

      def test_failure(self):
          self.assertFalse(True)
    DELIMITER

    echo "pytest-watch" > requirements.txt

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  all the text between the two ``DELIMITER`` words will be written to ``tests/test_$PROJECT_NAME.py``

* I use `chmod <https://man7.org/linux/man-pages/man1/chmod.1.html>`_ to make the program executable ::

    chmod +x createPythonTdd.sh

* I can now create a Test Driven Development environment on demand by giving a name for the ``PROJECT_NAME`` variable when the program is called. For example, typing this command in the terminal in the folder where ``createPythonTdd.sh`` is saved will create a Test Driven Development environment for a project called ``calculator``, you can continue this in :doc:`/how_to/calculator` ::

    ./createPythonTdd.sh calculator



How to automatically create a Test Driven Development Environment on Windows without WSL
==========================================================================================
* I create a file named ``createPythonTdd.ps1`` by using the ``New-Item`` command in PowerShell ::

    New-Item createPythonTdd.ps1

* I open the file in the Interactive Development Editor and add the following code

  .. code-block:: powershell

    $projectName=$args[0]
    mkdir -p $projectName/tests
    Set-Location $projectName

    new-Item "$projectName.py"
    New-Item tests/__init__.py
    $testSetup = @"
    import unittest

    class Test$($projectName)(unittest.TestCase):

        def test_failure(self):
            self.assertTrue(False)
    "@
    $testSetup |  Out-File $("tests/test_$($projectName).py") -Encoding UTF8

    python -m venv .venv
    .venv/scripts/activate
    pip install --upgrade pip
    pip install pytest-watch
    pytest-watch

* I can now create a Test Driven Development environment on demand by giving a name for the ``PROJECT_NAME`` variable when the program is called. For example, typing this command in the terminal in the folder where ``createPythonTdd.sh`` is saved will create a Test Driven Development environment for a project called ``calculator``, you can continue this in :doc:`/how_to/calculator` ::

    ./createPythonTdd.ps1 calculator

----

One of the advantages of programming is that I can take a series of steps and make them a one line command which the computer does on my behalf.

You now know one way to create a Test Driven Development Environment for Python projects, and have a program to do it for you anytime you want

Happy Trails!

:doc:`/code/code_create_tdd_environment`

To see a project where you actually create a program using Test Driven Development, checkout :doc:`how_to/calculator`