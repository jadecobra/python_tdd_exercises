
How to Setup a Test Driven Development Environment
==================================================

`Test Driven Development <https://en.wikipedia.org/wiki/Test-driven_development>`_ is a way of developing software with a focus on tests.  I come up with ideas to reach a goal and test those ideas, the results of these tests tell me if I am closer or further away from the goal and I repeat the process until I reach the goal.

I recommend reading `Kent Beck’s <https://en.wikipedia.org/wiki/Kent_Beck>`_ `Test Driven Development by Example <https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530/?_encoding=UTF8&pd_rd_w=dbNYL&content-id=amzn1.sym.579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_p=579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_r=133-9769820-0728336&pd_rd_wg=bMVBp&pd_rd_r=c84a5de8-ec36-4bd1-9196-8fa05de41794&ref_=aufs_ap_sc_dsk>`_ and `Martin Fowler’s <https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer)>`_ `Refactoring <https://www.amazon.com/Refactoring-Improving-Existing-Addison-Wesley-Signature/dp/0134757599/?_encoding=UTF8&pd_rd_w=dbNYL&content-id=amzn1.sym.579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_p=579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_r=133-9769820-0728336&pd_rd_wg=bMVBp&pd_rd_r=c84a5de8-ec36-4bd1-9196-8fa05de41794&ref_=aufs_ap_sc_dsk>`_, they both influenced the way I write programs.

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

.. admonition:: *are you on a windows computer?*

  * open PowerShell and install `Windows Subsystem for Linux <https://learn.microsoft.com/en-us/windows/wsl/install>`_ by typing ``wsl --install``
  * run subsequent commands in `Windows Subsystem for Linux <https://learn.microsoft.com/en-us/windows/wsl/install>`_


Setup
-----

I open a terminal in the Interactive Development Environment (IDE) and type the following commands to setup the project

.. note::

  ``{PROJECT_NAME}`` is a placeholder for the name of the project. For example to setup a project called ``magic`` I would replace ``{PROJECT_NAME}`` with ``magic``

* I create a directory for the project with a folder called ``tests`` inside it

  .. code-block:: shell

    mkdir -p {PROJECT_NAME}/tests

* I change directory to ``{PROJECT_NAME}``

  .. code-block:: shell

    cd {PROJECT_NAME}

  this is where all the code for the project will reside to keep things in a separate dedicated workspace

* ``touch`` is a program which creates an empty file with the name it is given

  - I create an empty file called ``{PROJECT_NAME}.py`` to hold the source code for the program

    .. code-block:: shell

      touch {PROJECT_NAME}.py

  - tests will be stored in the ``tests`` folder to separate them from the source code (the actual program)
  - I create an empty file called ``__init__.py`` in the ``tests`` folder to tell python that the ``tests`` folder is a python `package <https://docs.python.org/3/glossary.html#term-regular-package>`_, so it can find the tests later

    .. code-block:: shell

      touch tests/__init__.py

  - I create an empty file called ``test_{PROJECT_NAME}.py`` in the ``tests`` folder to hold the testing code

    .. code-block:: shell

      touch tests/test_{PROJECT_NAME}.py

* The folder structure now looks like this

  .. code-block:: ruby

    {PROJECT_NAME}
        ╰──tests
        |   ╰──__init__.py
        |   ╰──test_{PROJECT_NAME}.py
        ╰──{PROJECT_NAME}.py


----


The Test Driven Development cycle paraphrased is ``RED GREEN REFACTOR``

* **RED**: make it fail - write a failing test to make sure the test works
* **GREEN**: make it pass - write only the code necessary to make the test pass
* **REFACTOR**: make it better


RED: make it fail
-----------------


* I open up ``{PROJECT_NAME}/tests/test_{PROJECT_NAME}.py`` in the Interactive Development Environment (IDE) and type the following

  .. code-block:: python
    :linenos:

    import unittest


    class Test{PROJECT_NAME}(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code above

  - ``import unittest`` imports the `unittest <https://docs.python.org/3/library/unittest.html>`_ module
  - `unittest <https://docs.python.org/3/library/unittest.html>`_ is a module from the python standard library used for testing
  - ``Test{PROJECT_NAME}`` is a :doc:`class <classes>` that will hold the tests I write
  - `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ is a :doc:`class <classes>` defined in the `unittest <https://docs.python.org/3/library/unittest.html>`_ module which contains :doc:`methods (functions) <functions>` for testing and ``Test{PROJECT_NAME}`` inherits from it. A simple way to think of inheritance is that ``Test{PROJECT_NAME}`` is a child of `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ and can do the same things it can
  - ``def test_failure`` is the definition of a test :doc:`method <functions>` to test the program I am creating

    * ``def`` is the python keyword for creating :doc:`functions`
    * ``test_failure`` is the name of the :doc:`function <functions>`
    * ``self`` is the ``Test{PROJECT_NAME}`` class. I can use ``self`` to access ``methods`` and ``attributes`` within the ``Test{PROJECT_NAME}`` class, this avoids having to type ``Test{PROJECT_NAME}().assertFalse(True)`` to access the ``assertFalse`` :doc:`method <functions>` for instance
    * ``self.assertFalse(True)`` the actual test

      - ``assertFalse`` is a :doc:`method <functions>` in the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ class which checks if its input is ``False``
      - ``True`` is given as input to ``assertFalse``

      I expect this line to fail because ``True`` is not ``False``

* I save the file and turn on the ``Auto Save`` feature in the Interactive Development Environment (IDE) to avoid manually saving a file each time a change is made
* I type this in the terminal to test the code

  .. code-block:: python

    python3 -m unittest

  the terminal updates to show a failure as expected

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

If you are typing along, *CONGRATULATIONS!* You have written the first test.

This is the `RED` part of the Test Driven Development cycle. The error in the terminal has important information. Looking at it from the bottom


* ``FAILED (failures=1)`` there is one failure
* ``Ran 1 test in 0.000s`` how long it took the test to run
* ``AssertionError: True is not false`` The error is an :doc:`AssertionError` which is raised by python when an assert statement is ``False``, in this case the error is raised because ``True is not false``
* ``self.assertFalse(True)`` the line of code that caused the failure

  - ``assertFalse`` is a :doc:`method <functions>` in the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ class which checks if its input is ``False``
  - ``True`` is given as input to ``assertFalse`` and the statement raises an error because ``True`` is not ``False``

* ``File "/<PATH_TO_PROJECT>/{PROJECT_NAME}/tests/test_{PROJECT_NAME}.py", line 7, in test_failure`` is the line number and location of the file where the error occurred. Hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on this line with the mouse to place the cursor at the position in the file where the error occurred
* ``Traceback (most recent call last):`` all the information returned by python after this line is the ``traceback`` showing the most recent call python made last
* ``FAIL: test_failure (tests.Test{PROJECT_NAME}.test_failure)`` a header with information about the test

  - ``tests.Test{PROJECT_NAME}.test_failure`` is the location of the failing test
  -  ``tests`` is the tests folder
  - ``Test{PROJECT_NAME}`` is the class defined on line 4
  - ``test_failure`` is the function defined on line 6

* ``F`` indicates a failure
* ``python3 -m unittest`` is the command to run tests with `unittest`_

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to call a module given after the option
  - `unittest <https://docs.python.org/3/library/unittest.html>`_ is a module from the python standard library used for testing


GREEN: make it pass
-------------------


* I write down Exceptions I encounter to help become more familiar with errors in python. I add :doc:`AssertionError` to the list

  .. code-block:: python
    :linenos:

    import unittest


    class Test{PROJECT_NAME}(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

    # Exceptions Encountered
    # AssertionError

* I change the input on line 7 to make the test pass

  .. code-block:: python

    self.assertFalse(False)

* I run the test again from the terminal

  .. code-block:: python

    python3 -m unittest

  and the terminal updates to show a passing test

  .. code-block:: python

    .
    ------------------------------------------------------
    Ran 1 test in 0.000s

    OK

  *cue CELEBRATION MUSIC AND DANCE!* I am GREEN.


REFACTOR: make it better
------------------------

I can make code better by using


* `The Abstraction Principle <https://en.wikipedia.org/wiki/Abstraction_principle_(computer_programming)>`_ or
* `The Do Not Repeat Yourself (DRY) Principle <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

Both of these can be summed up as ``remove duplication``

So far there is not much to improve on what has been written but there has been duplication.

* ``python3 -m unittest`` was run to see the test fail
* ``python3 -m unittest`` was run to see the test pass
* ``python3 -m unittest`` will be run to make sure changes do not break previous passing tests

This means ``python3 -m unittest`` is run for each part of the Test Driven Development cycle or each time there is a code change. I automate this so I `Do Not Repeat myself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_, it would be better for a program to automatically run the tests when there is a change to the code

How to Automatically Run Tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

How to create a Virtual Environment
+++++++++++++++++++++++++++++++++++

* Using ``echo`` I create a file called ``requirements.txt`` in the ``{PROJECT_NAME}`` folder with ``pytest-watch`` as the text

  .. code-block:: shell

    echo "pytest-watch" > requirements.txt

  - ``pytest-watch`` is a python program that automatically uses the `pytest <https://docs.pytest.org/>`_ python package to run tests when a python file in the project changes
  - `pytest <https://docs.pytest.org/>`_ is a python package like `unittest <https://docs.python.org/3/library/unittest.html>`_ for running tests in python
  - ``requirements.txt`` is a file where I can list required python packages for `pip <https://pypi.org/project/pip/>`_ the `python package manager <https://pypi.org/project/pip/>`_ to install later, you can use any name you like

* I create a virtual environment using the `venv <https://docs.python.org/3/library/venv.html#module-venv>`_ module from the python standard library

  .. code-block:: python

      python3 -m venv .venv

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to call the module given after the option
  - `venv <https://docs.python.org/3/library/venv.html#module-venv>`_ is a module from the python standard library for creating virtual environments when given a name
  - a virtual environment is an isolated folder that holds dependencies, it keeps the dependencies for a specific project separate
  - ``.venv`` is the standard name for virtual environments in python, you can use any name you like

* I activate the virtual environment to use it

  .. code-block:: python

      source .venv/bin/activate

  the ``(.venv)`` on the far left of the command line in the terminal indicates the virtual environment is activated

* I upgrade `pip <https://pypi.org/project/pip/>`_ the `python package manager <https://pypi.org/project/pip/>`_ to the latest version

  .. code-block:: python

      python3 -m pip install --upgrade pip

  - ``python3`` is the major version of python being used
  - ``-m`` is an option passed to python to call the module given after the option
  - `pip <https://pypi.org/project/pip/>`_ is a module from the python standard library for installing python packages
  - ``install`` is an argument given to `pip <https://pypi.org/project/pip/>`_ to install a given package name
  - ``pip`` is the given package name for `pip <https://pypi.org/project/pip/>`_ to install, in this case  ``pip`` installs ``pip``
  - ``--upgrade`` is an option given to the ``install`` argument for `pip <https://pypi.org/project/pip/>`_ to install the latest version of the name given

* I can now use `pip <https://pypi.org/project/pip/>`_ to install any python packages listed in ``requirements.txt`` in the virtual environment. In this case `pip <https://pypi.org/project/pip/>`_ will install ``pytest-watch``

  .. code-block:: python

      pip install --requirement requirements.txt

  - ``--requirement`` is another option that can be passed to the ``install`` argument to install python packages from a given file name
  - ``requirements.txt`` is the file that contains a list of libraries for `pip <https://pypi.org/project/pip/>`_ to install

* The folder structure now looks like this

  .. code-block:: ruby

      {PROJECT_NAME}
          ╰──.venv
          ╰──tests
          |   ╰──__init__.py
          |   ╰──test_{PROJECT_NAME}.py
          ╰──{PROJECT_NAME}.py
          ╰──requirements.txt

* I type ``pytest-watch`` in the terminal to run the tests and it displays information about the test without going back to the command line

  .. code-block:: ruby

    [TODAYS_DATE] Running: py.test
    ================== test session starts===================
    platform <YOUR_OPERATING_SYSTEM> -- python <YOUR_python_VERSION >, pytest-<VERSION>, pluggy-<VERSION>
    rootdir: <YOUR_PATH>/project_name
    collected 1 item

    tests/test_<PROJECT_NAME>.py .                     [100%]

    =============== 1 passed in 0.00s =======================

* to verify that the terminal now responds to changes, I modify the input on line 7 in ``test_{PROJECT_NAME}.py`` to ``True`` to see it fail and back to ``False`` to see it pass
* I can press ``ctrl`` + ``c`` on the keyboard in the terminal to stop the tests at anytime

How to Deactivate a Virtual Environment
+++++++++++++++++++++++++++++++++++++++

type ``deactivate`` in the terminal

How to Activate a Virtual Environment
+++++++++++++++++++++++++++++++++++++

Make sure you are in the directory that contains the virtual environment for example ``{PROJECT_NAME}`` and type ``source .venv/bin/activate`` in the terminal



BONUS: Automatically create a Python Test Driven Development Environment
-------------------------------------------------------------------------

You made it this far and have become the greatest programmer in the world. Following the `The Do Not Repeat Yourself (DRY) Principle <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_, I would write a program that contains all the steps above. I can then use it to setup a Test Driven Development Environment any time I want without having to remember each step of the process

* I exit the tests in the terminal by pressing ``ctrl`` + ``c`` on the keyboard
* I type ``deactivate`` to deactivate the virtual environment
* I change directory to the parent of ``{PROJECT_NAME}``

  .. code-block:: shell

      cd ..

* I type ``history`` in the terminal to list the commands typed in this session so far as a reference for the program

  .. code-block:: shell

    history

* I create an empty file with a name that describes what the program does so it is easy to remember later, for example ``setupPythonTdd.sh``

  .. code-block:: shell

      touch setupPythonTdd.sh

* I open ``setupPythonTdd.sh`` in the Interactive Development Environment (IDE) and copy each command displayed in the terminal from ``history``

  .. code-block:: ruby
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
    python3 -m pip install --requirement requirements.txt
    pytest-watch

* There is a problem with the program, it will always create a project called ``{PROJECT_NAME}`` so I need to add a variable to make it create any project name I pass to the program as input. I update the program with a variable called ``PROJECT_NAME`` which is referenced with ``$PROJECT_NAME``

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
    python3 -m pip install --requirement requirements.txt
    pytest-watch

* to add the test for failure in ``test_$PROJECT_NAME.py``, I use the ``concatenate`` program to add the text

  .. code-block:: shell
    :linenos:

    PROJECT_NAME=$1
    mkdir -p $PROJECT_NAME/tests
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

* I use ``chmod`` to make the program executable

  .. code-block:: python

    chmod +x setupPythonTdd.sh

* I can now create a Test Driven Development environment on demand by giving a name for the ``{PROJECT_NAME}`` variable when the program is called. For example, typing this command in the terminal in the folder where ``setupPythonTdd.sh`` is saved will setup a Test Driven Development environment for a project called ``magic``

  .. code-block:: shell

    ./setupPythonTdd.sh magic

This is one of the advantages of programming, I can take a series of steps and make them a one line command which the computer does on my behalf

You now know one way to Setup a Test Driven Development Environment for Python projects, and have a program to do it for you anytime you want

Happy Trails!
