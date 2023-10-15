# How I setup a Test Driven Development Environment

We will step through creating a [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) Environment in python

The Test Driven Development mantra paraphrased is
    **RED** **GREEN** **REFACTOR**
- **RED**: make it fail - we write a failing test to make sure our test works
- **GREEN**: make it pass - we write only the code necessary to make the test pass
- **REFACTOR**: make it better - we make the code/tests better

# Table of Contents
1. [Requirements](#requirements)
2. [Setup](#setup)
3. [**RED**: make it fail](#red-make-it-fail)
4. [**GREEN**: make it pass](#green-make-it-pass)
5. [**REFACTOR**: make it better](#refactor-make-it-better)
    - [Automatically Run Tests](#how-to-automatically-run-tests)
        - [Create a Virtual Environment](#create-a-virtual-environment)
        - [Activate a Virtual Environment](#activate-a-virtual-environment)

## Requirements

- [download and install python](https://www.python.org/downloads/)
- download and install an Interactive Development Environment(IDE) - Here are a few options
    - [VSCode in a Browser](http://vscode.dev)
    - [Download VSCode](https://code.visualstudio.com/download)
    - [Download PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac)
    - [Download Sublime](https://www.sublimetext.com)
    - [Other Interactive Development Environment(IDE) options](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments)

## Setup

> *The following are required if you on a Windows machine*
> - [download and install Git](https://github.com/git-for-windows/git/releases/download/v2.41.0.windows.3/Git-2.41.0.3-32-bit.exe)
> - open a command line or PowerShell terminal and install WSLv2 by typing
>   ```shell
>   wsl --install`
>   ```
> - run subsequent commands in WSL

### Setup File Structure

- type the following in a terminal to setup the directory structure
    ```shell
    mkdir -p project_name/tests
    cd project_name
    touch <PROJECT_NAME>.py
    touch tests/__init__.py
    touch tests/test_<PROJECT_NAME>.py
    ```
- `project_name` is a placeholder for the name of the project e.g. if you are building a project called `the_greatest_application`, replace `project_name` with `the_greatest_application`. We are going to place all our code for this project in the `project_name` folder
- Tests are stored in the `tests` folder to separate them from the actual source code
- The `__init__.py` file in the `tests` folder tells python that it is a python package
- The actual test file is called `test_<PROJECT_NAME>.py`
- The python module we are creating is called `<PROJECT_NAME>.py`. A python module is any file that ends in `.py`
- Your folder structure should look like this
    ```
    project_name
    |--tests
    |   |--__init__.py
    |   |--test_<PROJECT_NAME>.py
    |--<PROJECT_NAME>.py
    ```

---

## **RED**: make it fail

- We are ready to begin writing our first test. Open up `project_name/tests/test_<PROJECT_NAME>.py` in your Interactive Development Environment(IDE) and type the following
    ```python
    import unittest


    class TestProjectName(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)
    ```
    Below is an explanation of the code you just wrote
    - `import unittest` imports an existing module from the python standard library that is used for testing.
    - `unittest` is a module/library/package that comes with python for testing code, earlier it was mentioned that a python module is any file that ends in `.py` so we can assume there is a file somewhere on the computer called `unittest.py` or a folder named `unittest` with an `__init__.py` like our `tests` folder, we can take a look at the [unittest source code](https://github.com/python/cpython/blob/3.11/Lib/unittest/__init__.py) to confirm
    - `TestProjectName` is a class, a "container" for the tests we are about to write
    - `unittest.TestCase` is a class defined in the `unittest` library which contains a bunch of `methods/functions` for testing code that `TestProjectName` inherits so they do not have to be rewritten
    - a simple way to think of inheritance is that `TestProjectName` is a child of `unittest.TestCase` and can do the same things that its parent can do
    - `def test_failure` is the definition of a test function to test the system being built
    - `self` refers to the `TestProjectName` class. To access `methods` and `attributes` within the `TestProjectName` class we use `self`. It avoids having to say `TestProjectName.assertFalse(True)`
    - `self.assertFalse(True)` is an assert statement that is a substitute for `assert False == True` which is similar to asking the question `is False equal to True?`
- to test the code, write the following in the terminal
    ```shell
    python3 -m unittest
    ```
    the terminal updates to show
    ```python
    F
    ======================================================
    FAIL: test_failure (tests.TestProjectName.test_failure)
    ------------------------------------------------------
    Traceback (most recent call last):
    File "/<PATH_TO_PROJECT>/<PROJECT_NAME>/tests/test_<PROJECT_NAME>.py", line 7, in test_failure
        self.assertFalse(True)
    AssertionError: True is not false

    ------------------------------------------------------
    Ran 1 test in 0.000s

    FAILED (failures=1)
    ```

*CONGRATULATIONS!* You have written your first test.

Following the iterative process of **RED** **GREEN** **REFACTOR**, we are currently **RED**.
The error provides important information about the code. Looking at it from the last line
- `FAILED (failures=1)` The test failed - **RED**
- `Ran 1 test in 0.000s` tells us how long it took to run the test
- `AssertionError: True is not false` The error is an [AssertionError](./ASSERTION_ERROR.md) which is raised by python when an assert statement is `False`, in this case `True is not false`
- `self.assertFalse(True)` the line of code that caused the failure
- `File "/<PATH_TO_PROJECT>/<PROJECT_NAME>/tests/test_<PROJECT_NAME>.py", line 7, in test_failure` the line number and location of the file where the error occurred. Clicking on this line will place your cursor at the position in the Interactive Development Environment(IDE)
- `Traceback (most recent call last):` all the information returned by python for the exception is the traceback, showing the most recent call python made last
- `FAIL: test_failure (tests.TestProjectName.test_failure)` a header giving information about the test
    - `tests.TestProjectName.test_failure` is the location of the failing test
      - `tests` - our tests folder
      - `TestProjectName` - the class defined on line 4
      - `test_failure` - the function defined on line 6
- `F` indicates a failure

---

## **GREEN**: make it pass

- as part of our practice we will keep a list of Errors/[Exceptions](https://docs.python.org/3/library/exceptions.html) encountered as we go through our python journey. This will help us become better python programmers as we will be familiar with the cause and solutions to these exceptions. Add [AssertionError](./ASSERTION_ERROR.md) to the list
    ```python
    import unittest


    class TestProjectName(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

    # Exceptions Encountered
    # AssertionError
    ```
- change line 7 to make the test pass. Which of these is a better solution? `self.assertTrue(True)` or `self.assertFalse(False)`
- What was the deciding factor in picking one over the other?
- run the test again from the terminal
    ```shell
    python3 -m unittest
    ```
    the terminal updates to show
    ```shell
    .
    ------------------------------------------------------
    Ran 1 test in 0.000s

    OK
    ```

*CONGRATULATIONS!* You have a passing test. We are **GREEN**

---

## **REFACTOR**: make it better

We can make code better by using the
- [Abstraction Principle](https://en.wikipedia.org/wiki/Abstraction_principle_(computer_programming))
- [Do Not Repeat Yourself (DRY) Principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)

So far there's not much to improve on what has been written but there has been duplication.
- we ran `python3 -m unittest` to see the test fail
- we ran `python3 -m unittest` to see the test pass
- we will run `python3 -m unittest` again to make sure our improvements do not break previous passing tests

This means for every test we introduce we have to run that command 3 times.
How do we avoid this repetition and focus on tests and solutions?

### How to Automatically Run Tests

#### Create a Virtual Environment

> *Are you on a Windows machine? If you are not using WSL*
> - replace `python3` in the examples with `python`
> - replace `source .venv/bin/activate` in the example below with `.venv/scripts/activate`

- in your editor create a file named `requirements.txt` and add this line
    ```python
    pytest-watch
    ```
- after saving the file, type the following in the terminal
    ```shell
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install --requirement requirements.txt
    ```
    Your folder structure should now look like this
    ```
    project_name
    |--.venv
    |--tests
    |   |--__init__.py
    |   |--test_<PROJECT_NAME>.py
    |--<PROJECT_NAME>.py
    |--requirements.txt
    ```

You just created a [virtual environment](https://docs.python.org/3/library/venv.html)
- `python3 -m venv .venv` creates a virtual environment named `.venv` - you can use any name you want
- [venv](https://docs.python.org/3/library/venv.html#module-venv) is a python module for creating virtual environments, which is an isolated `subfolder` that holds any dependencies we install. It helps keep our dependencies for a specific project in the same place as the project
- `source .venv/bin/activate` or `.venv/scripts/activate` activates the virtual environment
- `pip install --upgrade pip` - upgrades `pip` the [python package manager](https://pypi.org/project/pip/) to the latest version
- `pip install --requirement requirements.txt` installs any python libraries listed in `requirements.txt`
- `pytest-watch` is a library that automatically runs tests when a change is made to our python files in the project
- type `pytest-watch` in the terminal to run the tests and the terminal displays
    ```shell
    [TODAYS_DATE] Running: py.test
    ======================= test session starts==========================
    platform <YOUR_OPERATING_SYSTEM> -- python <YOUR_python_VERSION >, pytest-<VERSION>, pluggy-<VERSION>
    rootdir: <YOUR_PATH>/project_name
    collected 1 item

    tests/test_<PROJECT_NAME>.py .                                                                                                    [100%]

    ======================= 1 passed in 0.00s ============================
    ```

#### Activate a Virtual Environment

If you already have a virtual environment setup in a project, you can activate it by following the steps below
- Open your terminal
- change directory to <PROJECT_NAME>
- activate the virtual environment by typing `source .venv/bin/activate`

*CONGRATULATIONS!* You have successfully setup a python Test Driven Environment and can build anything you want. Go forth and conquer the world

---