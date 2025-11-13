.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with a single script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watch for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

########################################################################################################
how to make a python test driven development environment on Windows without Windows Subsystem Linux
########################################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

This is one way to make a Python_ `Test Driven Development`_ environment on a Windows Computer that does NOT have `Windows Subsystem Linux`_

----

*********************************************************************************
requirements
*********************************************************************************

* `download and install Python <https://www.python.org/downloads/>`_
* get an Integrated Development Environment (IDE). Here are a few options

  - `Visual Studio Code`_
  - `Sublime Text`_
  - PyCharm_
  - `other Integrated Development Environment (IDE) options`_

----

****************************************************************************************************************
how to manually make a python test driven development environment on Windows without Windows Subsystem Linux
****************************************************************************************************************

* Imagine I have to work on a project and its name is ``magic``. I open a terminal in the `Integrated Development Environment (IDE)`_ and use mkdir_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir magic

  this makes a `folder/directory`_ for the project where its files will stay

* I use cd_

  .. code-block:: shell
    :emphasize-lines: 1

    cd magic

  this changes directory to the ``magic`` `folder/directory`_ I just made

* I make a child `folder/directory`_ for the source code (the actual program)

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  I use `New-Item`_

  .. code-block:: shell
    :emphasize-lines: 1

    New-Item src/magic.py

  this makes an empty file for the source code (the actual program)

* I make a child `folder/directory`_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  this is where I will add tests for the project

* I use `New-Item`_ to add an empty file called ``__init__.py`` in the ``tests`` folder

  .. attention:: make sure to use 2 underscores (__) for ``__init__.py``

  .. code-block:: shell
    :emphasize-lines: 1

    New-Item tests/__init__.py

  this tells Python_ that ``tests`` is a `python package`_, it will help it find the tests I write later

* I use `New-Item`_ to add one more empty file in the ``tests`` directory for the actual test

  .. code-block:: shell
    :emphasize-lines: 1

    New-Item tests/test_magic.py

  .. TIP:: I can use any name for the test file as long as it starts with ``test_``

* these are the folders/directories and files in the project

  .. code-block:: none
    :force:

    magic
    ├── src
    │   └── magic.py
    └── tests
        ├── __init__.py
        └── test_magic.py

  ``.py`` at the end of a file name shows it is a Python_ :ref:`module<ModuleNotFoundError>`

----

********************************************************************************************
test_failure
********************************************************************************************

The `Test Driven Development`_ cycle is ``RED GREEN REFACTOR``

* **RED**: make it fail - write a failing test to make sure the test works
* **GREEN**: make it pass - write only what is needed to make the failing test pass
* **REFACTOR**: make it better - `remove duplication`_

red: make it fail
############################################################################################

* I click on ``magic/tests/test_magic.py`` in the `Integrated Development Environment (IDE)`_ to open it in the editor, then type the following

  .. NOTE:: the line numbers below are a guide, you do not need to copy them

  .. code-block:: python
    :linenos:

    import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

  Here is an explanation of the code in the file

  - ``import unittest`` imports the unittest_ :ref:`module<ModuleNotFoundError>` from the `python standard library`_, it is used for testing
  - ``class TestMagic``

    * ``class`` is the Python_ keyword for making :ref:`classes`, which are a group of :ref:`attributes<AttributeError>` and :ref:`methods<functions>` that belong together, see :ref:`classes` for more
    * ``TestMagic`` is the name of this :ref:`class <classes>` and will hold the test

      .. TIP:: I can use any name for the test class as long as it starts with ``Test``

    * `unittest.TestCase`_ is a :ref:`class <classes>` from the unittest_ :ref:`module<ModuleNotFoundError>` which has :ref:`methods<functions>` for testing
    * ``class TestMagic(unittest.TestCase)`` defines ``TestMagic`` as a "child" of `unittest.TestCase`_ which means I can use its :ref:`methods<functions>` and :ref:`attributes<AttributeError>`

  - ``def test_failure``

    * def_ is the Python_ keyword for making :ref:`methods (functions) <functions>`, see :ref:`functions` for more
    * ``test_failure`` is the name of this :ref:`method<functions>` for my tests

      .. TIP:: I can use any name for the test method as long as it starts with ``test_``

    * ``self.`` allows me to use :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of the ``TestMagic`` :ref:`class<classes>` which is a "child" of the `unittest.TestCase`_ :ref:`class<classes>`, instead of using ``TestMagic().`` or ``unittest.TestCase().``
    * ``self.assertFalse(True)`` is an :ref:`assertion<AssertionError>`

      - assertFalse_ is a :ref:`method<functions>` in the `unittest.TestCase`_ :ref:`class <classes>` that checks if its input is :ref:`False<test_what_is_false>`
      - :ref:`True<test_what_is_true>` is given as the input

      I expect this line to fail because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`. If it does not fail, then Python_ and I have a problem

* I turn on the ``Auto Save`` feature in the `Integrated Development Environment (IDE)`_ to automatically save files when I make a change so `I do not repeat myself`_ by hitting save (``ctrl+s`` (windows/linux) or ``command+s`` (mac)) every time
* I type this in the terminal to run the test

  .. code-block:: python

    python -m unittest

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    F
    =============================================================
    FAIL: test_failure (tests.test_magic.TestMagic.test_failure)
    -------------------------------------------------------------
    Traceback (most recent call last):
      File ".../magic/tests/test_magic.py", line 7, in test_failure
        self.assertFalse(True)
        ~~~~~~~~~~~~~~~~^^^^^^
    AssertionError: True is not false

    -------------------------------------------------------------
    Ran 1 test in A.XYZs

    FAILED (failures=1)

If you are typing along, *CONGRATULATIONS!* You just wrote a test.

This is the ``RED`` part of the `Test Driven Development`_ cycle. The message in the terminal is about the failure, I like to read these from the bottom up, here is an explanation of each line

* ``FAILED (failures=1)`` the number of failures
* ``Ran 1 test in A.XYZs`` the number of tests it ran and how long they took
* ``AssertionError: True is not false`` the :ref:`Error/Exception<errors>` raised and its message, in this case :ref:`AssertionError` is raised because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`
* ``~~~~~~~~~~~~~~~~^^^^^^`` points to the part of the line above it that it thinks caused the :ref:`error<errors>`
* ``self.assertFalse(True)`` the line of code that caused the failure
* ``File ".../magic/tests/test_magic.py", line 7, in test_failure`` the line number of the code that caused the failure and the location of the file where it is

  .. TIP:: Hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``File ".../magic/tests/test_magic.py", line 7`` in the terminal, and the `Integrated Development Environment (IDE)`_ will open the file in the editor with the cursor at the line where the failure happened

* ``Traceback (most recent call last):`` all the information shown after this line that is indented to the right shows the calls that led to the failure, this is why I like to read it from the bottom up
* ``FAIL: test_failure (tests.test_magic.TestMagic.test_failure)`` is a header with information in :ref:`dot notation` about the failing test :ref:`method<functions>`

  - ``tests.test_magic.TestMagic.test_failure`` is the location of the failing test
  -  ``tests`` is the ``tests`` folder
  -  ``test_magic`` is the ``test_magic.py`` file
  - ``TestMagic`` is the :ref:`class <classes>` defined on line 4
  - ``test_failure`` is the :ref:`method<functions>` defined on line 6

* ``F`` shows a failure
* ``python -m unittest`` is the command to run tests with the ``unittest`` :ref:`module<ModuleNotFoundError>`

  - ``python`` is the Python_ program
  - ``-m`` is an option/switch passed to Python_ to run the :ref:`module<ModuleNotFoundError>` given after it

* I recommend you keep a list of :ref:`Errors/Exceptions<errors>` you meet to become familiar with them, it helps when you run into them later. I add :ref:`AssertionError` to the list

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11

    import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError

green: make it pass
#################################################################################

I change the input on line 7 from :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>`

.. code-block:: python

  self.assertFalse(False)

then I run the test again in the terminal

.. code-block:: python

  python -m unittest

and the test passes! The terminal shows

.. code-block:: none

  .
  ------------------------------------------------------
  Ran 1 test in A.XYZs

  OK

*cue CELEBRATION MUSIC AND DANCE!* I am GREEN.

refactor: make it better
############################################################################################

I ran ``python -m unittest`` to see the test fail, I ran ``python -m unittest`` again to see the test pass. I will have to run ``python -m unittest`` again when I make a code change, to make sure tests that were passing are not failing and that the new code I add does what I expect.

This means I have to run ``python -m unittest`` for each part of the `Test Driven Development`_ cycle or any time there is a code change. I do not want to type ``python -m unittest`` again, it is better for a program to run the tests so `I do not repeat myself`_.

----

********************************************************************************************
how to automatically run tests on Windows without Windows Subsystem Linux
********************************************************************************************

how to make a virtual environment
############################################################################################

* I make a `virtual environment`_ with the venv_ :ref:`module<ModuleNotFoundError>`

  .. code-block:: shell

    python -m venv .venv

  - ``python`` is the Python_ program
  - ``-m`` is an option passed to Python_ to run the :ref:`module<ModuleNotFoundError>` given after the option as a script
  - venv_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_, it is used to make a `virtual environment`_ with a given name.
  - A `virtual environment`_ is a separate folder where `python packages`_ needed by the project will be installed, this helps me keep things that belong to the project in one place separate from other things on the computer
  - ``.venv`` is the name given

    .. NOTE:: ``.venv`` is Python_ convention, I can use any name I want for the virtual environment

* I run PowerShell_ in Administrator mode and set the Execution Policy for the activation script to work

  .. code-block:: PowerShell

    Set-ExecutionPolicy RemoteSigned

  the terminal may show the following message if you have never run this command before

  .. code-block:: text

    The execution policy helps protect you from scripts that you do not trust.
    Changing the execution policy might expose you to the security risks
    described in the about_Execution_Policies help topic at
    https:/go.microsoft.com/fwlink/?LinkID=135170.
    Do you want to change the execution policy?

    [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"):

  Type ``Y`` to accept the change and it will enable scripts that have been signed by a verified publisher to run on your computer, you can read more at `Set-ExecutionPolicy`_

  To activate the virtual environment, go back to the terminal you were working in before the Execution Policy change and type

  .. code-block::

    .venv/scripts/activate

  or

  .. code-block:: PowerShell

    .venv/scripts/activate.ps1

  .. ADMONITION:: the ``(.venv)`` on the far left of the command line in the terminal shows that I am in the `virtual environment`_, for example

    .. code-block:: shell

      (.venv) .../magic $

* I upgrade pip_ the `python package manager`_ to the latest version

  .. code-block:: shell

    python -m pip install --upgrade pip

  - pip_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_, it is used to install `python packages`_
  - ``install`` is an argument given to pip_ to install a given package name
  - ``--upgrade`` is an option/switch given to the ``install`` argument for pip_ to upgrade the version of the given `python package`_
  - ``pip`` is the package name I am giving pip_ to install, in this case it upgrades itself

* I use pip_ to see what packages are installed in the virtual environment

  .. code-block:: python

    pip list

  the terminal shows

  .. code-block:: shell

    Package Version
    ------- -------
    pip     x.y

* I use `Out-File`_ to make a file in the ``magic`` directory with `pytest-watch`_ as its text

  .. code-block:: PowerShell

    "pytest-watch" | Out-File requirements.txt -Encoding UTF8

  - ``|`` is an operator that is used to send output from the left of it as input to the right of it
  - `Out-File`_ is a program that writes input text to a given file
  - `pytest-watch`_ is a Python_ program that automatically runs pytest_ when a Python_ file in the folder changes
  - pytest_ is a `python package`_ like unittest_, that is used for testing
  - ``requirements.txt`` is the name of a file where I can list `python packages`_ for pip_ to install

    .. NOTE:: ``requirements.txt`` is Python_ convention, I can use any name I want for the file

* I install `pytest-watch`_ and the programs it needs

  .. code-block:: python

      pip install --requirement requirements.txt

  - ``--requirement`` is another option that can be passed to the ``install`` argument for `python packages`_ in a given file
  - ``requirements.txt`` is the name of the file given

    .. NOTE:: ``requirements.txt`` is Python_ convention, I can use any name I want for the file

* I use pip_ to see what packages are now installed in the `virtual environment`_

  .. code-block:: python

    pip list

  the terminal shows

  .. code-block:: python

    Package      Version
    ------------ -------
    colorama     x.y.z
    docopt       x.y.z
    iniconfig    x.y.z
    packaging    x.y
    pip          x.y
    pluggy       x.y.z
    Pygments     x.y.z
    pytest       x.y.z
    pytest-watch x.y.z
    watchdog     x.y.z

* I now have these folders/directories and files in the project

  .. code-block:: shell
    :force:

    magic
    ├── .venv
    ├── src
    │   └── magic.py
    └── tests
    │   ├── __init__.py
    │   ├── __pycache__
    │   └── test_magic.py
    └── requirements.txt

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

* when I change the input on line 7 in ``test_magic.py`` from :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>`, the terminal shows :ref:`AssertionError`

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

  I change :ref:`True<test_what_is_true>` back to :ref:`False<test_what_is_false>` in ``test_magic.py`` to make it pass. I can now write the rest of the code for the project while the tests run automatically

  .. TIP:: press ``ctrl`` + ``c`` on the keyboard in the terminal when you want to stop the tests

----

how to deactivate a virtual environment
#################################################################################################

When I want to leave a `virtual environment`_, I type this in the terminal to deactivate it

.. code-block::

  deactivate

----

how to activate a virtual environment
############################################################################################

When I want to work in a `virtual environment`_, I `change directory`_ to the `folder/directory`_ that has the `virtual environment`_ for example ``magic``, and type this in the terminal

.. code-block:: PowerShell

  .venv/scripts/activate

or

.. code-block:: PowerShell

  .venv/scripts/activate.ps1

.. ADMONITION:: the ``(.venv)`` on the far left of the command line in the terminal shows that I am in the `virtual environment`_, for example

  .. code-block:: shell

    (.venv) .../magic $

-----

*******************************************************************************************************************
how to automatically make a python test driven development environment on Windows without Windows Subsystem Linux
*******************************************************************************************************************

You made it this far and have become the greatest programmer in the world. To follow `The Do Not Repeat Yourself (DRY) Principle`_, I write a program that has all the commands it took to get here, then I can use it to make a `Test Driven Development`_ Environment anytime I want and not have to remember every step of the process

* I exit the tests in the terminal by pressing ``ctrl`` + ``c`` on the keyboard
* I leave the `virtual environment`_

  .. code-block:: shell

    deactivate

* I use cd_ to `change directory`_ to the parent of ``magic``

  .. code-block:: shell

    cd ..

* I use `New-Item`_ to make an empty file with a name that describes what the program does so it is easy to remember later, for example :ref:`makePythonTdd.sh`

  .. code-block:: shell

    New-Item makePythonTdd.ps1

* I use history_

  .. code-block:: shell

    history

  the history_ program shows all the commands I have typed in the terminal so far, and I use them to write the program

* I click on ``makePythonTdd.ps1`` to open it in the Integrated Development Environment (IDE), then type the commands I need to make a `Test Driven Development`_ Environment in the editor

  .. NOTE:: the line numbers below are a guide, you do not need to copy them

  .. code-block:: PowerShell
    :linenos:

    mkdir magic
    cd magic
    mkdir src
    New-Item src/magic.py
    mkdir tests
    New-Item tests/__init__.py
    New-Item tests/test_magic.py
    python -m venv .venv
    .venv/scripts/activate.ps1
    python -m pip install --upgrade pip
    "pytest-watch" | Out-File requirements.txt -Encoding UTF8
    python -m pip install --requirement requirements.txt
    pytest-watch

* The problem with this program is it will always make a project called ``magic``. I need it to be able to make any project I want. I add a variable to replace ``magic`` so I can give it any name when I want to make a project

  .. NOTE:: the line numbers below are a guide, you do not need to copy them

  .. code-block:: PowerShell
    :linenos:
    :emphasize-lines: 1-3,5,8

    $PROJECT_NAME=$args[0]
    mkdir $PROJECT_NAME
    cd $PROJECT_NAME
    mkdir src
    New-Item "src/$PROJECT_NAME.py"
    mkdir tests
    New-Item tests/__init__.py
    New-Item tests/test_$PROJECT_NAME.py
    python -m venv .venv
    source .venv/bin/activate.ps1
    python -m pip install --upgrade pip
    "pytest-watch" | Out-File requirements.txt -Encoding UTF8
    python -m pip install --requirement requirements.txt
    pytest-watch

  .. ADMONITION:: ``$args[0]`` is for the first argument given when the program is called, I can use it in place of ``$PROJECT_NAME`` for example

    .. code-block:: shell

      command argument

    in the code above, ``command`` will be ``makePythonTdd.ps1`` and ``$args[0]`` will be the value of  ``argument``

* I use the `Out-File`_ program to add text for the first failing test to ``test_$PROJECT_NAME.py``

  .. literalinclude:: /code/make_tdd/makePythonTdd.ps1
    :linenos:
    :language: PowerShell
    :emphasize-lines: 9-20

* I can make a `Test Driven Development`_ environment when I call the program with a name for the ``PROJECT_NAME`` variable. For example, when I type this in the terminal in the folder where ``makePythonTdd.ps1`` is saved

  .. code-block:: PowerShell

    ./makePythonTdd.ps1 calculator

  the terminal shows

  .. code-block:: python

    ====================================== FAILURES =======================================
    _____________________________ Testcalculator.test_failure _____________________________

    self = <tests.test_calculator.Testcalculator testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_calculator.py:7: AssertionError
    =============================== short test summary info ===============================
    FAILED tests/test_calculator.py::Testcalculator::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ==================================

  the computer made a `Test Driven Development`_ environment for a project called :ref:`calculator<how to make a calculator>`, you can continue this in :ref:`how to make a calculator`

----

********************************************************************************************
review
********************************************************************************************

One of the advantages of programming is that I can take some steps and make them a one line command for the computer to do for me.

You have seen a way to make a Python_ `Test Driven Development`_ Environment, and have a :ref:`program<makePythonTdd.sh>` to do it for you on any Windows_ computers without having to install `Windows Subsystem Linux`_.

Would you like to test :ref:`test AssertionError?<AssertionError>`

----

the program to make a Python_ `Test Driven Development`_ Environment for any Windows_ computers without `Windows Subsystem Linux`_

:ref:`Click Here to see the code for the program to make a Python Test Driven Development environment for any Windows computers without Windows Subsystem Linux<makePythonTdd.ps1>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->