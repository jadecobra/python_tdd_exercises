
How I setup a Test Driven Development Environment
=================================================

`Test Driven Development <https://en.wikipedia.org/wiki/Test-driven_development>`_ is a way of developing software with a focus on tests. We come up with ideas to reach a goal and test the ideas, the results of the tests inform us about our direction in relation to the goal. We repeat this process until we reach the goal.

I learned Test Driven Development by reading `Kent Beck’s <https://en.wikipedia.org/wiki/Kent_Beck>`_ `Test Driven Development by Example <https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530/?_encoding=UTF8&pd_rd_w=dbNYL&content-id=amzn1.sym.579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_p=579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_r=133-9769820-0728336&pd_rd_wg=bMVBp&pd_rd_r=c84a5de8-ec36-4bd1-9196-8fa05de41794&ref_=aufs_ap_sc_dsk>`_ and `Martin Fowler’s <https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer)>`_ `Refactoring <https://www.amazon.com/Refactoring-Improving-Existing-Addison-Wesley-Signature/dp/0134757599/?_encoding=UTF8&pd_rd_w=dbNYL&content-id=amzn1.sym.579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_p=579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_r=133-9769820-0728336&pd_rd_wg=bMVBp&pd_rd_r=c84a5de8-ec36-4bd1-9196-8fa05de41794&ref_=aufs_ap_sc_dsk>`_, they both influenced me in a great way.

The Test Driven Development mantra paraphrased is ``RED GREEN REFACTOR``

* **RED**: make it fail - write a failing test to make sure the test works
* **GREEN**: make it pass - write only the code necessary to make the test pass
* **REFACTOR**: make it better

Here is how I setup a Test Driven Development environment for Python projects.

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


Open a terminal in the Interactive Development Environment (IDE) and type the following commands to setup the directory structure.

Note that ``{PROJECT_NAME}`` is a placeholder for the name of the project. For example if you are building a project called ``the_greatest_application`` replace ``{PROJECT_NAME}`` with ``the_greatest_application``

.. code-block:: shell

  mkdir -p {PROJECT_NAME}/tests
  cd {PROJECT_NAME}
  touch {PROJECT_NAME}.py
  touch tests/__init__.py
  touch tests/test_{PROJECT_NAME}.py

* We are going to place all our code for this project in the ``{PROJECT_NAME}`` folder
* Tests will be stored in the ``tests`` folder to separate them from the source code (the actual program)
* The ``__init__.py`` file in the ``tests`` folder tells python that the ``tests`` folder is a python package
* The test file is called ``test_{PROJECT_NAME}.py`` and is where we write our tests
* The source code for our program will be written in ``{PROJECT_NAME}.py``


Your folder structure should look like this

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

    import unittest


    class Test{PROJECT_NAME}(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code you just wrote

  - ``import unittest`` imports an existing module from the python standard library
  - ``unittest`` is a module that comes with python for testing code, earlier it was mentioned that a python module is any file that ends in ``.py`` so we can assume there is a file somewhere on the computer called ``unittest.py`` or a folder named ``unittest`` with an ``__init__.py`` the similar to  the setup for the ``tests`` folder, we could also confirm by taking a look at the `unittest source code <https://github.com/python/cpython/blob/3.11/Lib/unittest/__init__.py>`_
  - ``Test{PROJECT_NAME}`` is a :doc:`class <classes>` that will hold the tests we write
  - ``unittest.TestCase`` is a :doc:`class <classes>` defined in the ``unittest`` library which contains :doc:`methods/functions <functions>` for testing code that ``Test{PROJECT_NAME}`` inherits from
  - a simple way to think of inheritance is that ``Test{PROJECT_NAME}`` is a child of `unittest.TestCase` and can do the same things that its parent can do
  - ``def test_failure`` is the definition of a test function to test the program we are creating
  - ``self`` refers to the ``Test{PROJECT_NAME}`` class. To access ``methods`` and ``attributes`` within the ``Test{PROJECT_NAME}`` class we use ``self``. It avoids having to say ``Test{PROJECT_NAME}.assertFalse(True)``
  - ``self.assertFalse(True)`` is an assert statement that is a substitute for ``assert False == True`` which is similar to asking the question ``is False equal to True?``

* save the file
* turn on the ``Auto Save`` feature in your Interactive Development Environment (IDE)

* we are ready to test the code, write the following in the terminal

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


* ``FAILED (failures=1)`` The test failed - RED
* ``Ran 1 test in 0.000s`` tells us how long it took to run the test
* ``AssertionError: True is not false`` The error is an :doc:`AssertionError` which is raised by python when an assert statement is ``False``, in this case ``True is not false`` raises the error
* ``self.assertFalse(True)`` the line of code that caused the failure
* ``File "/<PATH_TO_PROJECT>/{PROJECT_NAME}/tests/test_{PROJECT_NAME}.py", line 7, in test_failure`` the line number and location of the file where the error occurred. Clicking on this line will place your cursor at the position in the file where the error occurred
* ``Traceback (most recent call last):`` all the information returned by python for the exception is the traceback, showing the most recent call python made last
* ``FAIL: test_failure (tests.Test{PROJECT_NAME}.test_failure)`` a header giving information about the test

  - ``tests.Test{PROJECT_NAME}.test_failure`` is the location of the failing test
  -  ``tests`` - our tests folder
  - ``Test{PROJECT_NAME}`` - the class defined on line 4
  - ``test_failure`` - the function defined on line 6

* ``F`` indicates a failure
* ``python3 -m unittest``

  - ``python3`` the major version of python we are currently using
  - ``-m`` an option given to python to call the module given after the option
  - ``unittest`` a python standard library module designed for testing


GREEN: make it pass
-------------------


* Let us keep a list of Exceptions we encounter as we go through our journey. Keeping track of the cause and solutions we come up with to these exceptions will help us become better programmers. Add :doc:`AssertionError` to the list

  .. code-block:: python

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

We can make code better by using the


* `Abstraction Principle <https://en.wikipedia.org/wiki/Abstraction_principle_(computer_programming)>`_
* `Do Not Repeat Yourself (DRY) Principle <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

Both of these can be summed up as ``remove duplication``. I ask two questions to help me remove duplication when I write code

* What is similar? this tells me what parts are common
* What is different? this tells me what parts are specific

Another way to think of it is to note which parts are ``constant`` and which parts are ``changing``

So far there is not much to improve on what has been written but there has been duplication.

* we ran ``python3 -m unittest`` to see the test fail
* we ran ``python3 -m unittest`` to see the test pass
* we run ``python3 -m unittest`` again to make sure our improvements do not break previous passing tests

This means for every test we introduce we have to run ``python3 -m unittest`` at least 3 times.
How do we avoid this repetition and focus on tests and solutions? We can automate the repeating parts so you `Do Not Repeat Yourself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

How to Automatically Run Tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a Virtual Environment
++++++++++++++++++++++++++++


.. admonition:: *Are you on a Windows machine?*

  If you are not using WSL make the following changes when you type the code below

  * replace ``python3`` with ``python``
  * replace ``source .venv/bin/activate`` with ``.venv/scripts/activate``


* create a file named ``requirements.txt`` in your editor then add this line

  .. code-block:: shell

    pytest-watch

* save the file and type the following in the terminal

  .. code-block:: python

      python3 -m venv .venv
      source .venv/bin/activate
      python3 -m pip install --upgrade pip
      pip install --requirement requirements.txt

  Your folder structure should now look like this

  .. code-block::

      project_name
      |--.venv
      |--tests
      |   |--__init__.py
      |   |--test_<PROJECT_NAME>.py
      |--<PROJECT_NAME>.py
      |--requirements.txt

  You just created a `virtual environment <https://docs.python.org/3/library/venv.html>`_


  - ``python3 -m venv .venv`` creates a virtual environment named ``.venv`` - you can use any name you want
  - `venv <https://docs.python.org/3/library/venv.html#module-venv>`_ is a python standard library module for creating virtual environments
  - a virtual environment is an isolated ``subfolder`` that holds any dependencies we install. It helps keep our dependencies for a specific project in the same place as the project, while isolating it from the source code and tests
  - ``source .venv/bin/activate`` or ``.venv/scripts/activate`` activates the virtual environment
  - ``python3 -m pip install --upgrade pip`` - upgrades ``pip`` the `python package manager <https://pypi.org/project/pip/>`_ to the latest version
  - ``pip install --requirement requirements.txt`` installs any python libraries listed in ``requirements.txt``
  - ``pytest-watch`` is a library that automatically runs tests when a change is made to python files in the project

* type ``pytest-watch`` in the terminal to run the tests and the terminal displays

  .. code-block:: python

    [TODAYS_DATE] Running: py.test
    ======================= test session starts==========================
    platform <YOUR_OPERATING_SYSTEM> -- python <YOUR_python_VERSION >, pytest-<VERSION>, pluggy-<VERSION>
    rootdir: <YOUR_PATH>/project_name
    collected 1 item

    tests/test_<PROJECT_NAME>.py .                                                                                                    [100%]

    ======================= 1 passed in 0.00s ============================


Activate a Virtual Environment
++++++++++++++++++++++++++++++

If you already have a virtual environment setup in a project, you can activate it by following the steps below


* Open a terminal
* change directory to ``{PROJECT_NAME}``
* activate the virtual environment by typing ``source .venv/bin/activate`` in the terminal

*CONGRATULATIONS!* You have successfully setup a python Test Driven Environment and can build anything you want. Go forth and conquer the world



Automatically create a Python Test Driven Development Environment
-----------------------------------------------------------------

You made it this far and have become the greatest programmer in the world. Following the practice of removing duplication, let us write a program that contains all the steps we did above.

Any time we want to setup a test driven development environment we can call the program instead of repeating and remembering each step


* open a new file in your Interactive Development Environment (IDE) then type the following

  .. code-block:: shell
   :linenos:

    project_name=$1
    mkdir -p $project_name/tests
    cd $project_name
    touch $project_name.py
    touch tests/__init__.py

    test_file=tests/test_$project_name.py

    cat << DELIMITER > $test_file
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

  .. warning::

    DO NOT SAVE the script in the ``{PROJECT_NAME}`` folder, save it in the parent

* make the program executable by typing this command in the terminal

  .. code-block:: python

    chmod +x setupPythonTdd.sh

* you can now create a Test Driven Development environment by giving a name you want for the ``$project_name`` variable when the program is called. For example,  typing this command in the terminal will setup the environment for a project called ``the_greatest_application``

  .. code-block:: shell

    ./setupPythonTdd.sh the_greatest_application

This is one of the advantages of programming, we can take a series of steps and make them a one line command which the computer does on our behalf. Happy Trails!
