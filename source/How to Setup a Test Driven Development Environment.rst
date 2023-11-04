
How to Setup a Test Driven Development Environment
==================================================

`Test Driven Development <https://en.wikipedia.org/wiki/Test-driven_development>`_ is a way of developing software with a focus on tests where we come up with ideas to reach a goal and test them, the results of these tests tell us if we are closer or further away from the goal. We repeat the process until we reach the goal.

I learned Test Driven Development from reading `Kent Beck’s <https://en.wikipedia.org/wiki/Kent_Beck>`_ `Test Driven Development by Example <https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530/?_encoding=UTF8&pd_rd_w=dbNYL&content-id=amzn1.sym.579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_p=579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_r=133-9769820-0728336&pd_rd_wg=bMVBp&pd_rd_r=c84a5de8-ec36-4bd1-9196-8fa05de41794&ref_=aufs_ap_sc_dsk>`_ and `Martin Fowler’s <https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer)>`_ `Refactoring <https://www.amazon.com/Refactoring-Improving-Existing-Addison-Wesley-Signature/dp/0134757599/?_encoding=UTF8&pd_rd_w=dbNYL&content-id=amzn1.sym.579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_p=579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_r=133-9769820-0728336&pd_rd_wg=bMVBp&pd_rd_r=c84a5de8-ec36-4bd1-9196-8fa05de41794&ref_=aufs_ap_sc_dsk>`_, they both influenced me in a great way.

Here is a way to setup a Test Driven Development environment for Python projects.


Requirements
------------


* `download and install Python <https://www.python.org/downloads/>`_
* download and install an Interactive Development Environment (IDE) - Here are a few options

  * `VSCode in a Browser <http://vscode.dev>`_
  * `VSCode <https://code.visualstudio.com/download>`_
  * `PyCharm <https://www.jetbrains.com/pycharm/download/#section=mac>`_
  * `Sublime <https://www.sublimetext.com>`_
  * `Other Interactive Development Environment (IDE) options <https://wiki.python.org/moin/IntegratedDevelopmentEnvironments>`_

Setup
-----

.. admonition:: *If you are on a windows machine*

  * `download and install Git <https://github.com/git-for-windows/git/releases>`_
  * open a terminal and install WSLv2 by typing ``wsl --install``
  * run subsequent commands in WSL


Project Structure
^^^^^^^^^^^^^^^^^


Open a terminal in your Interactive Development Environment (IDE) and type the following commands to setup the project

Note that ``{PROJECT_NAME}`` is a placeholder for the name of the project. For example if I were building a project called ``magic`` I would replace ``{PROJECT_NAME}`` with ``magic``

* I first create a directory for the project named ``{PROJECT_NAME}`` and a folder named ``tests`` folder within the project

  .. code-block:: shell

    mkdir -p {PROJECT_NAME}/tests

* Then I change directory to ``{PROJECT_NAME}`` so I can work in there, it is where all the code for this project will reside, keeping things in a separate dedicated workspace

  .. code-block:: shell

    cd {PROJECT_NAME}

* ``touch`` is a program which creates an empty file with the name you give it, I will use it to create empty files for the project

  - I create an empty file named ``{PROJECT_NAME}.py`` which will contain the source code for the program

    .. code-block:: shell

      touch {PROJECT_NAME}.py

  - Tests will be stored in the ``tests`` folder to separate them from the source code (the actual program). I create an empty file named ``__init__.py`` in the ``tests`` folder to tell python that the ``tests`` folder is a python package, this helps python find the tests

    .. code-block:: shell

      touch tests/__init__.py

  - I also create an empty file named ``test_{PROJECT_NAME}.py`` in the ``tests`` folder where I will write tests

    .. code-block:: shell

      touch tests/test_{PROJECT_NAME}.py

* The folder structure should look like this

  .. code-block::

    {PROJECT_NAME}
        ╰──tests
        |   ╰──__init__.py
        |   ╰──test_{PROJECT_NAME}.py
        ╰──{PROJECT_NAME}.py


The Test Driven Development cycle paraphrased is ``RED GREEN REFACTOR``

* **RED**: make it fail - write a failing test to make sure the test works
* **GREEN**: make it pass - write only the code necessary to make the test pass
* **REFACTOR**: make it better


RED: make it fail
-----------------


* We are ready to begin writing our first test. Open up ``{PROJECT_NAME}/tests/test_{PROJECT_NAME}.py`` in your Interactive Development Environment (IDE) and type the following text paying attention to spacing, the line numbers are given here as a guide

  .. code-block:: python
    :linenos:

    import unittest


    class Test{PROJECT_NAME}(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code above

  - ``import unittest`` imports the `unittest <https://docs.python.org/3/library/unittest.html>`_ module
  - `unittest <https://docs.python.org/3/library/unittest.html>`_ is a module from the python standard library used for testing
  - ``Test{PROJECT_NAME}`` is a :doc:`class <classes>` that will hold the tests we write
  - ``unittest.TestCase`` is a :doc:`class <classes>` defined in the `unittest <https://docs.python.org/3/library/unittest.html>`_ library which contains :doc:`methods (functions) <functions>` for testing and ``Test{PROJECT_NAME}`` inherits from it
  - a simple way to think of inheritance is that ``Test{PROJECT_NAME}`` is a child of ``unittest.TestCase`` and can do the same things it can do
  - ``def test_failure`` is the definition of a test :doc:`method (function) <functions>` to test the program we are creating

    * ``self`` is the ``Test{PROJECT_NAME}`` class. To access ``methods`` and ``attributes`` within the ``Test{PROJECT_NAME}`` class we use ``self``. It avoids having to say ``Test{PROJECT_NAME}().assertFalse(True)``
    * ``self.assertFalse(True)`` is a statement that is a substitute for ``assert False == True`` which is similar to asking the question ``is False equal to True?``

* save the file
* turn on the ``Auto Save`` feature in your Interactive Development Environment (IDE) to avoid having to repeat saving a file each time you make a change
* type this in the terminal to test the code

  .. code-block:: python

    python3 -m unittest

  the terminal updates to show a failure

  .. code-block:: python

    F
    ======================================================
    FAIL: test_failure (tests.Test{PROJECT_NAME}.test_failure)
    ------------------------------------------------------
    Traceback (most recent call last):
    File "/<PATH_TO_PROJECT>/{PROJECT_NAME}/tests/test_{PROJECT_NAME}.py", line 7, in test_failure
        self.assertFalse(True)
    AssertionError: True is not false

    ------------------------------------------------------
    Ran 1 test in 0.000s

    FAILED (failures=1)

If you are typing along *CONGRATULATIONS!* You have written your first test.

We are in the RED part of the Test Driven Development cycle. The error in the terminal gives us important information. Looking at it from the bottom


* ``FAILED (failures=1)`` there is one failure
* ``Ran 1 test in 0.000s`` how long it took the test to run
* ``AssertionError: True is not false`` The error is an :doc:`AssertionError` which is raised by python when an assert statement is ``False``, in this case the error is raised because ``True is not false``
* ``self.assertFalse(True)`` the line of code that caused the failure

  - ``assertFalse`` is a :doc:`method (function) <functions>` in the ``unittest.TestCase`` class which checks if its input is ``False``
  - ``True`` is given as input to ``assertFalse`` and the statement raises an error because ``True`` is not ``False``

* ``File "/<PATH_TO_PROJECT>/{PROJECT_NAME}/tests/test_{PROJECT_NAME}.py", line 7, in test_failure`` is the line number and location of the file where the error occurred. Holding down ``ctrl`` (windows/linux ) or ``option`` (mac) on the keyboard and clicking on this line will place the cursor at the position in the file where the error occurred
* ``Traceback (most recent call last):`` all the information returned by python after this line is the ``traceback`` showing the most recent call python made last
* ``FAIL: test_failure (tests.Test{PROJECT_NAME}.test_failure)`` a header with information about the test

  - ``tests.Test{PROJECT_NAME}.test_failure`` is the location of the failing test
  -  ``tests`` - is the tests folder
  - ``Test{PROJECT_NAME}`` - is the class defined on line 4
  - ``test_failure`` - is the function defined on line 6

* ``F`` indicates a failure
* ``python3 -m unittest`` is the command to run our tests using the `unittest`_ module

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to call the module given after the option
  - `unittest <https://docs.python.org/3/library/unittest.html>`_ is a module from the python standard library used for testing


GREEN: make it pass
-------------------


* I keep track of Exceptions encountered to help become more familiar with python's exceptions. Let us add :doc:`AssertionError` to the list

  .. code-block:: python
    :linenos:

    import unittest


    class Test{PROJECT_NAME}(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

    # Exceptions Encountered
    # AssertionError

* changing the input on line 7 makes the test pass

  .. code-block:: python

    self.assertFalse(False)

* I run the test again from the terminal

  .. code-block:: python

    python3 -m unittest

  and we get

  .. code-block:: python

    .
    ------------------------------------------------------
    Ran 1 test in 0.000s

    OK

The test passes. *CELEBRATION DANCE!* We are GREEN.


REFACTOR: make it better
------------------------

We can make code better by using


* `The Abstraction Principle <https://en.wikipedia.org/wiki/Abstraction_principle_(computer_programming)>`_
* `The Do Not Repeat Yourself (DRY) Principle <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

Both of these can be summed up as ``remove duplication``

So far there is not much to improve on what has been written but there has been duplication.

* ``python3 -m unittest`` was run to see the test fail
* ``python3 -m unittest`` was run to see the test pass
* ``python3 -m unittest`` will be run to make sure changes do not break previous passing tests

This means ``python3 -m unittest`` is run for each part of the Test Driven Development cycle. To avoid this repetition, I automate the repeating parts so I `Do Not Repeat Myself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

How to Automatically Run Tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

How to Create a Virtual Environment
+++++++++++++++++++++++++++++++++++

* Using ``echo`` I create a file named ``requirements.txt`` in the ``{PROJECT_NAME}`` folder with ``pytest-watch`` as the text

  .. code-block:: shell

    echo "pytest-watch" > requirements.txt

  - ``pytest-watch`` is a program that automatically uses the `pytest <https://docs.pytest.org/>`_ library to run tests when a python file in the project changes
  - `pytest <https://docs.pytest.org/>`_ is a library like `unittest <https://docs.python.org/3/library/unittest.html>`_ for running tests in python
  - ``requirements.txt`` is a file where we can list required dependencies of a project for `pip <https://pypi.org/project/pip/>`_ to install later, you can use any name you like

* I create a virtual environment using the `venv <https://docs.python.org/3/library/venv.html#module-venv>`_ module from the python standard library

  .. code-block:: python

      python3 -m venv .venv

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to call the module given after the option
  - `venv <https://docs.python.org/3/library/venv.html#module-venv>`_ is a module from the python library for creating virtual environments a given name
  - a virtual environment is an isolated folder that holds dependencies. It helps keep dependencies for a specific project separate from other python dependencies you install on the computer, source code and tests
  - ``.venv`` is the standard name for virtual environments in python, you can use any name you want

* after creating the virtual environment, I activate it to use it

  .. code-block:: python

      source .venv/bin/activate

  the ``(.venv)`` on the far left of the command line in the terminal indicates the virtual environment successfully activated

* I upgrade `pip <https://pypi.org/project/pip/>`_ the `python package manager <https://pypi.org/project/pip/>`_ to the latest version

  .. code-block:: python

      python3 -m pip install --upgrade pip

* I can now use `pip <https://pypi.org/project/pip/>`_ to install any python libraries listed in ``requirements.txt`` in the virtual environment, in this case ``pytest-watch``

  .. code-block:: python

      pip install --requirement requirements.txt

* The folder structure now looks like this

  .. code-block:: ruby

      {PROJECT_NAME}
          ╰──.venv
          ╰──tests
          |   ╰──__init__.py
          |   ╰──test_{PROJECT_NAME}.py
          ╰──{PROJECT_NAME}.py
          ╰──requirements.txt

* typing ``pytest-watch`` in the terminal runs the tests and the terminal displays

  .. code-block:: ruby

    [TODAYS_DATE] Running: py.test
    ================== test session starts===================
    platform <YOUR_OPERATING_SYSTEM> -- python <YOUR_python_VERSION >, pytest-<VERSION>, pluggy-<VERSION>
    rootdir: <YOUR_PATH>/project_name
    collected 1 item

    tests/test_<PROJECT_NAME>.py .                     [100%]

    =============== 1 passed in 0.00s =======================

* to verify that the terminal now responds to my changes I can modify the input on line 7 in ``test_{PROJECT_NAME}.py`` to ``True`` to see it fail and back to ``False`` to see it pass
* hit `ctrl` + `c` in the terminal to stop the tests at anytime

How to Deactivate a Virtual Environment
+++++++++++++++++++++++++++++++++++++++

type ``deactivate`` in the terminal

How to Activate a Virtual Environment
+++++++++++++++++++++++++++++++++++++

Make sure you are in the directory that contains the virtual environment for example ``{PROJECT_NAME}`` and type ``source .venv/bin/activate`` in the terminal



BONUS: Automatically create a Python Test Driven Development Environment
-------------------------------------------------------------------------

You made it this far and have become the greatest programmer in the world. Following the practice of removing duplication, I would write a program that contains all the steps above following `The Do Not Repeat Yourself (DRY) Principle <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_. I can then call the program any time I want to setup a Test Driven Development Environment

* exit the tests in the terminal by hitting ``ctrl`` + ``c`` on the keyboard
* type ``deactivate`` to deactivate the virtual environment if you have not already
* change directory to the parent of ``{PROJECT_NAME}``

  .. code-block:: shell

      cd ..

* type ``history`` in the terminal to see the commands typed in this session as a reference for the program
* create an empty file with a name that describes what it does so it is easy to remember later, for example, ``setupPythonTdd.sh``

  .. code-block:: shell

      touch setupPythonTdd.sh

* and open it in the Interactive Development Environment (IDE), adding each command we added earlier

  .. code-block:: shell
   :linenos:

    mkdir -p {PROJECT_NAME}/tests
    cd {PROJECT_NAME}
    touch {PROJECT_NAME}.py
    touch tests/__init__.py
    touch tests/test_{PROJECT_NAME}.py

    echo "pytest-watch" > requirements.txt

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    pytest-watch

* If we run this program as is it will always create a project named ``{PROJECT_NAME}`` so we need to add a variable to make it create any project name we pass to the program as input. I will update the program with a variable named ``PROJECT_NAME`` which is referenced with ``$PROJECT_NAME``

  .. code-block:: shell
    :linenos:

    PROJECT_NAME=$1
    mkdir -p $PROJECT_NAME/tests
    cd $PROJECT_NAME
    touch $PROJECT_NAME.py
    touch tests/__init__.py
    touch tests/test_$PROJECT_NAME.py

    echo "pytest-watch" > requirements.txt

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    pytest-watch

* The only thing missing now is the test for failure in ``test_$PROJECT_NAME.py``, I will use the concatenate program to add the text for .. important:: text

  .. code-block:: shell
    :linenos:

    PROJECT_NAME=$1
    mkdir -p $PROJECT_NAME/tests
    cd $PROJECT_NAME
    touch $PROJECT_NAME.py
    touch tests/__init__.py

    cat << DELIMITER > touch tests/test_$PROJECT_NAME.py
    import unittest


    class Test$PROJECT_NAME(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)
    DELIMITER

    echo "pytest-watch" > requirements.txt

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    pytest-watch

* to make the program executable I use ``chmod``

  .. code-block:: python

    chmod +x setupPythonTdd.sh

* I can now create a Test Driven Development environment on demand by giving a name for the ``{PROJECT_NAME}`` variable when the program is called. For example, typing this command in the terminal in the folder where ``setupPythonTdd.sh`` is saved will setup a Test Driven Development environment for a project called ``magic``

  .. code-block:: shell

    ./setupPythonTdd.sh magic

This is one of the advantages of programming, we can take a series of steps and make them a one line command which the computer does on our behalf

There you have it. You now know one way to Setup a Test Driven Development Environmnet for Python projects, and have a program to do it for you anytime you want

Happy Trails!
