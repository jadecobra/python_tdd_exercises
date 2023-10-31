
Setup a Test Driven Development Environment
=================================================

`Test Driven Development <https://en.wikipedia.org/wiki/Test-driven_development>`_ is a way of developing software with a focus on tests where we come up with ideas to reach a goal and test them, the results of these tests tell us if we are closer or further away from the goal. We repeat the process until we reach the goal.

I learned Test Driven Development from reading `Kent Beck’s <https://en.wikipedia.org/wiki/Kent_Beck>`_ `Test Driven Development by Example <https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530/?_encoding=UTF8&pd_rd_w=dbNYL&content-id=amzn1.sym.579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_p=579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_r=133-9769820-0728336&pd_rd_wg=bMVBp&pd_rd_r=c84a5de8-ec36-4bd1-9196-8fa05de41794&ref_=aufs_ap_sc_dsk>`_ and `Martin Fowler’s <https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer)>`_ `Refactoring <https://www.amazon.com/Refactoring-Improving-Existing-Addison-Wesley-Signature/dp/0134757599/?_encoding=UTF8&pd_rd_w=dbNYL&content-id=amzn1.sym.579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_p=579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_r=133-9769820-0728336&pd_rd_wg=bMVBp&pd_rd_r=c84a5de8-ec36-4bd1-9196-8fa05de41794&ref_=aufs_ap_sc_dsk>`_, they both influenced me in a great way.

The Test Driven Development mantra paraphrased is ``RED GREEN REFACTOR``

* **RED**: make it fail - write a failing test to make sure the test works
* **GREEN**: make it pass - write only the code necessary to make the test pass
* **REFACTOR**: make it better

Here is a way to setup a Test Driven Development environment for Python projects.

Requirements
------------


* `download and install python <https://www.python.org/downloads/>`_
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


File Structure
^^^^^^^^^^^^^^


Open a terminal in your Interactive Development Environment (IDE) and type the following commands to setup the directory structure.

Note that ``{PROJECT_NAME}`` is a placeholder for the name of the project. For example if you are building a project called ``the_greatest_application`` replace ``{PROJECT_NAME}`` with ``the_greatest_application``

.. code-block:: shell

  mkdir -p {PROJECT_NAME}/tests
  cd {PROJECT_NAME}
  touch {PROJECT_NAME}.py
  touch tests/__init__.py
  touch tests/test_{PROJECT_NAME}.py

* ``mkdir -p {PROJECT_NAME}/tests`` creates a folder named ``tests`` in a folder named ``{PROJECT_NAME}``
* ``cd {PROJECT_NAME}`` changes the directory to ``{PROJECT_NAME}`` so we can work there
* we are going to place all our code for this project in the ``{PROJECT_NAME}`` folder
* tests will be stored in the ``tests`` folder to separate them from the source code (the actual program)
* ``touch`` is a program which creates an empty file with the name given after the command

  - ``touch __init__.py`` creates an empty file named ``__init__.py`` in the ``tests`` folder which tells python that the ``tests`` folder is a python package
  - ``touch test_{PROJECT_NAME}.py`` creates an empty file named ``test_{PROJECT_NAME}.py`` where we will write our tests
  - ``touch {PROJECT_NAME}.py`` creates an empty file named ``{PROJECT_NAME}.py`` which will contain the source code for our program


The folder structure should look like this

.. code-block::

  {PROJECT_NAME}
      |--tests
      |   |--__init__.py
      |   |--test_{PROJECT_NAME}.py
      |--{PROJECT_NAME}.py



RED: make it fail
-----------------


* We are ready to begin writing our first test. Open up ``{PROJECT_NAME}/tests/test_{PROJECT_NAME}.py`` in your Interactive Development Environment (IDE) and type the following text paying attention to spacing

  .. code-block:: python
    :linenos:

    import unittest


    class Test{PROJECT_NAME}(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code you just wrote

  - ``import unittest`` imports a module named ``unittest`` to use for testing
  - ``unittest`` is a module from the python standard library used for testing code
  - ``Test{PROJECT_NAME}`` is a :doc:`class <classes>` that will hold the tests we write
  - ``unittest.TestCase`` is a :doc:`class <classes>` defined in the ``unittest`` library which contains :doc:`methods/functions <functions>` for testing code that ``Test{PROJECT_NAME}`` inherits from
  - a simple way to think of inheritance is that ``Test{PROJECT_NAME}`` is a child of ``unittest.TestCase`` and can do the same things that its parent can do
  - ``def test_failure`` is the definition of a test :doc:`function <functions>` to test the program we are creating

    * ``self`` refers to the ``Test{PROJECT_NAME}`` class. To access ``methods`` and ``attributes`` within the ``Test{PROJECT_NAME}`` class we use ``self``. It avoids having to say ``Test{PROJECT_NAME}.assertFalse(True)``
    * ``self.assertFalse(True)`` is an assert statement that is a substitute for ``assert False == True`` which is similar to asking the question ``is False equal to True?``

* save the file
* turn on the ``Auto Save`` feature in your Interactive Development Environment (IDE)
* type the following in the terminal to test the code

  .. code-block:: python

    python3 -m unittest

  the terminal updates to show

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

*CONGRATULATIONS!* You have written your first test.

We are in the RED part of the Test Driven Development cycle. The error in the terminal gives us important information about the code which we can use to come up with a solution. Looking at it from the bottom


* ``FAILED (failures=1)`` There is a failure and the number of failures
* ``Ran 1 test in 0.000s`` how long it took the test took to run
* ``AssertionError: True is not false`` The error is an :doc:`AssertionError` which is raised by python when an assert statement is ``False``, in this case ``True is not false`` raises the error
* ``self.assertFalse(True)`` the line of code that caused the failure

  - the ``unittest.TestCase`` method ``assertFalse`` takes an input and checks if it is ``False``
  - ``True`` is given as input to ``assertFalse`` and the statement raises an error because ``True`` is not ``False``

* ``File "/<PATH_TO_PROJECT>/{PROJECT_NAME}/tests/test_{PROJECT_NAME}.py", line 7, in test_failure`` the line number and location of the file where the error occurred. Holding down ``Ctrl/option`` on your keyboard and clicking on this line will place your cursor at the position in the file where the error occurred
* ``Traceback (most recent call last):`` all the information returned by python after this line is the ``traceback`` showing the most recent call python made last
* ``FAIL: test_failure (tests.Test{PROJECT_NAME}.test_failure)`` a header with information about the test

  - ``tests.Test{PROJECT_NAME}.test_failure`` is the location of the failing test
  -  ``tests`` - refers to the tests folder
  - ``Test{PROJECT_NAME}`` - refers to the class defined on line 4
  - ``test_failure`` - refers to the function defined on line 6

* ``F`` indicates a failure
* ``python3 -m unittest`` is the command to run our tests using the ``unittest`` module

  - ``python3`` is the major version of python we are currently using
  - ``-m`` is an option passed to python to call the module given after the option
  - ``unittest`` is a module in the python standard library designed for testing


GREEN: make it pass
-------------------


* Create a list of Exceptions encountered as we go through our journey, to keep track of the cause and solutions we come up with. This will help us become more familiar with python's exceptions. Add :doc:`AssertionError` to the list

  .. code-block:: python
    :linenos:

    import unittest


    class Test{PROJECT_NAME}(unittest.TestCase):

        def test_failure(self):
           self.assertFalse(True)

    # Exceptions Encountered
    # AssertionError


* change line 7 to make the test pass. Which of these is a better solution?

  ``self.assertTrue(True)`` or ``self.assertFalse(False)``

  What was the deciding factor in picking one over the other?

* run the test again from the terminal

  .. code-block:: python

    python3 -m unittest

  the terminal updates to show

  .. code-block:: python

    .
    ------------------------------------------------------
    Ran 1 test in 0.000s

    OK

We are GREEN. *CONGRATULATIONS!* You have a passing test



REFACTOR: make it better
------------------------

We can make code better by using


* `The Abstraction Principle <https://en.wikipedia.org/wiki/Abstraction_principle_(computer_programming)>`_
* `The Do Not Repeat Yourself (DRY) Principle <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

Both of these can be summed up as ``remove duplication``. I ask two questions to help me remove duplication when I write code

* What is similar? this tells me what parts are common
* What is different? this tells me what parts are specific

Another way I think of it is to note which parts are ``fixed`` and which parts ``change``

So far there is not much to improve on what has been written but there has been duplication.

* we ran ``python3 -m unittest`` to see the test fail
* we ran ``python3 -m unittest`` to see the test pass
* we run ``python3 -m unittest`` again to make sure our improvements do not break previous passing tests

This means for every test introduced ``python3 -m unittest`` is run at least 3 times.
To avoid this repetition and focus on tests and solutions we can automate the repeating parts so you `Do Not Repeat Yourself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

How to Automatically Run Tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a Virtual Environment
++++++++++++++++++++++++++++

* create a file named ``requirements.txt`` in your editor in the ``{PROJECT_NAME}`` folder, then add this line

  .. code-block:: shell

    pytest-watch

* save the file and type the following in the terminal

  .. code-block:: python

      python3 -m venv .venv
      source .venv/bin/activate
      python3 -m pip install --upgrade pip
      pip install --requirement requirements.txt

  you will see a ``(.venv)`` at the far left of the command line in your terminal indicating that you are working in a virtual environment. Your folder structure should now look like this

  .. code-block::

      {PROJECT_NAME}
      |--.venv
      |--tests
      |   |--__init__.py
      |   |--test_{PROJECT_NAME}.py
      |--{PROJECT_NAME}.py
      |--requirements.txt

* You just created a `virtual environment <https://docs.python.org/3/library/venv.html>`_


  - ``python3 -m venv .venv`` creates a virtual environment named ``.venv`` - you can use any name you want
  - `venv <https://docs.python.org/3/library/venv.html#module-venv>`_ is a python standard library module for creating virtual environments
  - a virtual environment is an isolated folder to hold dependencies installed for the project where it resides. It helps keep dependencies for a specific project in the same place as the project, while isolating it from the source code and tests
  - ``source .venv/bin/activate`` activates the virtual environment, the ``(.venv)`` in the terminal indicates the virtual environment was activated
  - ``python3 -m pip install --upgrade pip`` upgrades ``pip`` the `python package manager <https://pypi.org/project/pip/>`_ to the latest version
  - ``pip install --requirement requirements.txt`` installs any python libraries listed in ``requirements.txt`` in the virtual environment, in this case ``pytest-watch``
  - ``pytest-watch`` is a program that automatically uses the `pytest <https://docs.pytest.org/>`_ library to runs tests when a change is made to python files in the project
  - `pytest <https://docs.pytest.org/>`_ is an external library for running tests in python

* type ``pytest-watch`` in the terminal to run the tests and the terminal displays

  .. code-block:: python

    [TODAYS_DATE] Running: py.test
    ================== test session starts===================
    platform <YOUR_OPERATING_SYSTEM> -- python <YOUR_python_VERSION >, pytest-<VERSION>, pluggy-<VERSION>
    rootdir: <YOUR_PATH>/project_name
    collected 1 item

    tests/test_<PROJECT_NAME>.py .                     [100%]

    =============== 1 passed in 0.00s =======================


Activate a Virtual Environment
++++++++++++++++++++++++++++++

If you already have a virtual environment setup in a project, you can activate it by following the steps below


* Open a terminal
* change directory to ``{PROJECT_NAME}``
* activate the virtual environment by typing ``source .venv/bin/activate`` in the terminal

-----


*CONGRATULATIONS!* You have successfully setup a Python Test Driven Environment and can build anything you want. Go forth and conquer the world



Automatically create a Python Test Driven Development Environment
-----------------------------------------------------------------

You made it this far and have become the greatest programmer in the world. Following the practice of removing duplication, I would write a program that contains all the steps above.

I can call the program any time I want to setup a Test Driven Development Environment instead of remembering and manually repeating each step


* open a new file in your Interactive Development Environment (IDE) then type the following

  .. code-block:: shell
   :linenos:

    project_name=$1
    mkdir -p $project_name/tests
    cd $project_name
    touch $project_name.py
    touch tests/__init__.py

    cat << DELIMITER > tests/test_$project_name.py
    import unittest


    class Test$project_name(unittest.TestCase):

        def test_failure(self):
            self.assertTrue(False)
    DELIMITER

    echo "pytest-watch" > requirements.txt

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    pytest-watch

* save the file with a name that describes what it does so you remember later, for example,  ``setupPythonTdd.sh`` in the folder that contains your ``{PROJECT_NAME}`` folder.

  .. caution::

    DO NOT SAVE the script in the ``{PROJECT_NAME}`` folder, save it in the parent

* open a new terminal
* make the program executable by typing this command in the terminal

  .. code-block:: python

    chmod +x setupPythonTdd.sh

* you can now create a Test Driven Development environment by giving a name you want for the ``$project_name`` variable when the program is called. For example,  typing this command in the terminal in the folder where ``setupTdd.sh`` is saved, will setup the environment for a project called ``the_greatest_application``

  .. code-block:: shell

    ./setupPythonTdd.sh the_greatest_application

This is one of the advantages of programming, we can take a series of steps and make them a one line command which the computer does on our behalf. Happy Trails!
