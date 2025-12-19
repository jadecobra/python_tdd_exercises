.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watch for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

########################################################################################################
how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux
########################################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

You made it this far and have become `the greatest programmer in the world`_. To follow `The Do Not Repeat Yourself (DRY) Principle`_, I write a program_ with the commands to make  a Python_ `Test Driven Development`_ Environment on a Windows_ Computer that does NOT have `Windows Subsystem for Linux`_ anytime I want so I do not have to remember every step of the process or do them manually.

To review, here are steps I take to make the environment for every project

#. I pick a name for the project
#. :ref:`I make a directory for the project<how to make a directory for the project on Windows without WSL>`
#. :ref:`I change directory to the project<how to change directory to the project on Windows without WSL>`
#. :ref:`I make a directory for the source code<how to make a directory for the source code on Windows without WSL>`
#. :ref:`I make a Python file to hold the source code in the 'src' folder<how to make an empty file on Windows without WSL>`
#. :ref:`I make a directory for the tests<how to make a directory for the tests on Windows without WSL>`
#. :ref:`I make the 'tests' folder a Python package<how to make the tests a Python package on Windows without WSL>`
#. :ref:`I make a Python file to hold the tests in the 'tests' folder<test_failure on Windows without WSL>`
#. :ref:`I add the first failing test to the test file<test_failure on Windows without WSL>`
#. :ref:`I make a virtual environment<how to make a virtual environment on Windows without WSL>`
#. :ref:`I activate the virtual environment<how to activate a virtual environment on Windows without WSL>`
#. :ref:`I upgrade the Python package manager<how to upgrade the Python package manager in a virtual environment on Windows without WSL>`
#. :ref:`I make a requirements file for the needed Python packages<how to write text to a file on Windows without WSL>`
#. :ref:`I install the packages listed in the requirements file<how to install Python packages in a virtual environment on Windows without WSL>`
#. :ref:`I run the tests automatically<how to run the tests automatically in a virtual environment on Windows without WSL>`
#. :ref:`I open the test file in the editor from the terminal<how to open the test file in the editor from the terminal on Windows without WSL>`
#. I make the test pass
#. then I start working on the project

I want to give one command for the program to do every step except

* pick the name for the project
* make the test pass and
* work on the project, though I can now use what is currently popularly called `Artificial Intelligence`_ to help with this

this way I only need to do 3 steps instead of 18

*********************************************************************************
preview
*********************************************************************************

Here is the program_ I have by the end of the chapter to :ref:`automatically make a python test driven development environment <how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux>`, it is only 27 lines of code, with spaces

.. literalinclude:: ../../code/make_tdd/makePythonTdd.ps1
  :language: PowerShell
  :linenos:

*************************************************************************************************************************
questions about making a Python Test Driven Development Environment automatically on Windows without Windows Subsystem for Linux
*************************************************************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`How can I make a PowerShell script?<how to make a PowerShell script>`
* :ref:`How can I run a PowerShell script<how to run a PowerShell script>`

----

*********************************************************************************
how to make a PowerShell script
*********************************************************************************

* I go to the terminal_ and use `New-Item`_ to make an empty file_ with a name that is easy to remember later. I want the name to also describe the program_ that will automatically make a `Test Driven Development`_ environment for me

  .. code-block:: PowerShell
    :emphasize-lines: 1

    New-Item makePythonTdd.ps1

  the terminal_ goes back to the command line

* I open ``makePythonTdd.ps1`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then add the commands I use to make a Python_ `Test Driven Development`_ environment for a project

  .. code-block:: PowerShell
    :linenos:
    :emphasize-lines: 1-

    mkdir magic_again
    cd magic_again
    mkdir src
    New-Item src/magic_again.py
    mkdir tests
    New-Item tests/__init__.py
    New-Item tests/test_magic_again.py
    python -m venv .venv
    .venv/scripts/activate.ps1
    python -m pip install --upgrade pip
    "pytest-watch" | Out-File requirements.txt -Encoding UTF8
    python -m pip install --requirement requirements.txt
    pytest-watch

* ``test_magic_again.py`` is an empty file_ becuase I used `New-Item`_. I want it to have the text for :ref:`the first failure<test_failure on Windows without WSL>` so I do not have to open the :ref:`editor<2 editors>` to add the text for it in each project. I use `Out-File`_ to add the text to ``test_magic_again.py`` when it makes the file_ in the ``tests`` folder_, the same I do with the ``requirements.txt`` file_

  .. code-block:: shell
    :lineno-start: 5
    :emphasize-lines: 4

    mkdir tests
    New-Item tests/__init__.py

    "" | Out-File "tests/test_magic.py" -Encoding UTF8

    python -m venv .venv
    .venv/scripts/activate.ps1

* I add the text for the test inside the :ref:`quotes ("")<quotes>` I just added to ``makePythonTdd.sh``, the way I do with `Out-File`_ when I add ``"pytest-watch"`` as text in ``requirements.txt``

  .. CAUTION:: Indentation_ is important in Python_, I use 4 spaces as convention in this book, see the :PEP:`Python Style Guide <8>` for more

  .. code-block:: PowerShell
    :lineno-start: 8
    :emphasize-lines: 1-11

    "import unittest


    class TestMagicAgain(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " | Out-File "tests/test_magic_again.py" -Encoding UTF8

--------------------------------------------------------------------------------------------
how to run a PowerShell script
--------------------------------------------------------------------------------------------

* I go back to the terminal_ to run the program_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    makePythonTdd.ps1

  the terminal_ shows

  .. code-block:: PowerShell

    command not found: makePythonTdd.ps1

  I have to tell the computer where the file_ is

  .. code-block:: PowerShell
    :emphasize-lines: 1

    .\makePythonTdd.ps1

  ``.\`` is shorthand for ``this directory`` which in this case is ``pumping_python`` where ``makePythonTdd.ps1`` is saved. The terminal_ shows


  .. code-block:: PowerShell
    :emphasize-lines: 10

    ======================================= FAILURES =======================================
    _____________________________ TestMagicAgain.test_failure _____________________________

    self = <tests.test_magic_again.TestMagicAgain testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic_again.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_magic_again.py::TestMagic::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

  Success! I just made a program_ that can make the ``magic_again`` project anytime I want and it automatically does the steps I did manually.

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_magic_again.py`` to open it in the :ref:`editor<2 editors>` then make the test pass

* I hit :kbd:`ctrl+c` in the terminal_ to stop the test
* I deactivate the `virtual environment`_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line

* I leave the ``magic`` folder to go back to the ``pumping_python`` folder_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: PowerShell

    ...\pumping_python >

* I want to use ``makePythonTdd.ps1`` to make another project with a different name. I change ``magic`` to the name of the new project in the :ref:`editor<2 editors>`

  .. NOTE:: The lines that are changing in the code are highlighted

  .. code-block:: PowerShell
    :linenos:
    :emphasize-lines: 1, 2, 4, 11, 19

    mkdir magic_again
    cd magic_again
    mkdir src
    touch src/magic_again.py
    mkdir tests
    touch tests/__init__.py

    "import unittest


    class TestMagicAgain(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " | Out-File "tests/test_magic_again.py" - Encoding UTF8

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    "pytest-watch" | Out-File requirements.txt -Encoding UTF 8
    python3 -m pip install --requirement requirements.txt
    pytest-watch

* I run ``makePythonTdd.ps1`` in the terminal_ to make a project named ``magic_again``

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.ps1

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: PowerShell
    :emphasize-lines: 10

    ======================================= FAILURES =======================================
    _____________________________ TestMagicAgain.test_failure ______________________________

    self = <tests.test_magic.TestMagicAgain testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic_again.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_magic_again.py::TestMagicAgain::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

  I make the test pass

* I hit :kbd:`ctrl+c` to exit the tests in the terminal_
* I run tree_ to see what I have in ``pumping_python`` now

  .. code-block:: shell
    :emphasize-lines: 1

    tree /F

  the terminal_ shows

  .. code-block::
    :emphasize-lines: 22-41

    .
    ├── magic
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    ├── magic_again
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    └── makePythonTdd.sh

  the program_ works and can reliably make a Python_ `Test Driven Development`_ environment the way I want it, but there is a problem

--------------------------------------------------------------------------------------------
how to use a variable in a PowerShell script
--------------------------------------------------------------------------------------------

I changed ``magic`` to ``magic_again`` in 5 places in ``makePythonTdd.sh``. I would have to do the same change every time I have a new project, and I want to follow `The Do Not Repeat Yourself (DRY) Principle`_. I want the program_ to take a project name once and use that name when making the project to make the following

- the project folder_
- the file_ for the program_ in the ``src`` folder_
- the file_ for the test in the ``tests`` folder_
- the :ref:`test class<classes>` in the test file_
- the `virtual environment`_ in the ``.venv`` folder_

The program_ should always make this structure

.. code-block:: shell

  PROJECT_NAME
  ├── requirements.txt
  ├── src
  │   └── PROJECT_NAME.py
  ├── tests
  │   ├── __init__.py
  │   └── test_PROJECT_NAME.py
  └── .venv

Time to use a variable_ for the name of the project

* I add a name to represent any project name that I give to ``makePythonTdd.ps1`` when I want it to make a project

  .. code-block:: PowerShell
    :linenos:
    :emphasize-lines: 1

    $PROJECT_NAME="magic_again"
    mkdir magic_again
    cd magic_again
    mkdir src
    touch src/magic_again.py
    mkdir tests
    touch tests/__init__.py

    "import unittest


    class TestMagicAgain(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " | Out-File "tests/test_magic_again.py" - Encoding UTF8

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    "pytest-watch" | Out-File requirements.txt -Encoding UTF 8
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  a :ref:`variable<test_attribute_error_w_variables>` is a name that is used for a value that can change. For example, we use the word ``woman`` to represent any woman, ``man`` to represent any man, ``child`` to represent any child, and ``parent`` to represent anyone with a child. In this case I use ``$PROJECT_NAME`` to represent any name of a project

* I change every where I have ``magic_again`` in the program, to use the :ref:`variable<test_attribute_error_w_variables>` I just added so that I only have to make a change in one place

  .. NOTE:: The lines that are changing in the code are highlighted

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 2-3, 5, 12, 20

    $PROJECT_NAME="magic_again"
    mkdir $PROJECT_NAME
    cd $PROJECT_NAME
    mkdir src
    touch src/$PROJECT_NAME.py
    mkdir tests
    touch tests/__init__.py

    "import unittest


    class Test$PROJECT_NAME(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " | Out-File "tests/test_$PROJECT_NAME.py" - Encoding UTF8

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    "pytest-watch" | Out-File requirements.txt -Encoding UTF 8
    python3 -m pip install --requirement requirements.txt
    pytest-watch

* I run the program_ again in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.ps1

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2, 4, 10, 12

    ======================================= FAILURES =======================================
    ____________________________ Testmagic_again.test_failure ______________________________

    self = <tests.test_magic.Testmagic_again testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic_again.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_magic_again.py::Testmagic_again::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in ``tests/test_magic_again.py`` to make the test pass

* I hit :kbd:`ctrl+c` in the terminal to stop the test
* I deactivate the `virtual environment`_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line

* I leave the ``magic_again`` folder to go back to the ``pumping_python`` folder_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: PowerShell

    ...\pumping_python

* I run tree_ to see what I have in the ``pumping_python`` folder_ now

  .. code-block:: shell
    :emphasize-lines: 1

    tree /F

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 8-13

    .
    ├── magic
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    ├── magic_again
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    └── makePythonTdd.sh

* The program_ works as expected, and I only need to give the project name in one place. It would be nice if I do not have to go into the file to give it the project name. I want to be able to just call the program_ and give it a name for the project from the command line. I can do this with ``$args[0]`` in PowerShell_, it represents the first argument given when a program_ is called. For example,

  .. code-block:: PowerShell

    command argument

  in the code above, :kbd:`command` will be ``makePythonTdd.ps1`` and ``$args[0]`` will be ``argument`` or whatever name I give.

  Here are a few other examples

  .. code-block:: PowerShell

    mkdir name_of_folder

  ``mkdir`` is the command, and ``$args[0]`` is ``name_of_folder``

  .. code-block:: PowerShell

    New-Item name_of_file

  ``New-Item`` is the command, and ``$args[0]`` is ``name_of_file``

  .. code-block:: PowerShell

    echo "anything"

  ``echo`` is the command, and ``$args[0]`` is ``"anything"``

  .. code-block:: PowerShell

    tree /F

  ``tree`` is the command and ``$args[0]`` is ``/F``

* I change ``magic_again`` to ``$args[0]`` in ``makePythonTdd.ps1``

  .. code-block:: shell
    :lineno-start: 1
    :emphasize-lines: 1

    $PROJECT_NAME=$args[0]

* I try the program_ again, this time with a different name for the project in the terminal_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    ./makePythonTdd.ps1 more_magic

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 10

    ======================================= FAILURES =======================================
    _____________________________ Testmore_magic.test_failure ______________________________

    self = <tests.test_more_magic.Testmore_magic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_more_magic.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_more_magic.py::Testmore_magic::test_failure - AssertionError: True is not false
    ================================== 1 failed in 0.04s ===================================

* I hold :kbd:`ctrl` on the keyboard in the terminal_ and click on ``tests/test_more_magic.py`` to open it in the :ref:`editor<2 editors>`, then make the test pass

* I use :kbd:`ctrl+c` on the keyboard in the terminal_ to stop the tests
* I deactivate the `virtual environment`_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line

* I leave the ``more_magic`` folder to go back to the ``pumping_python`` folder_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: PowerShell

    ...\pumping_python >

* I run tree_ to see what I have in the ``pumping_python`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    tree /F

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 15-20

    .
    ├── magic
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    ├── magic_again
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    ├── makePythonTdd.sh
    └── more_magic
        ├── .pytest_cache
        ├── requirements.txt
        ├── src
        ├── tests
        └── .venv

* I can now make a `Test Driven Development`_ environment with ``makePythonTdd.ps1`` when I give it a name for the ``PROJECT_NAME`` variable_. For example, when I type this in the terminal_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    ./makePythonTdd.ps1 assertion_error

  the terminal_ shows

  .. code-block:: PowerShell

    ====================================== FAILURES =======================================
    __________________________ Testassertion_error.test_failure ___________________________

    self = <tests.test_assertion_error.Testassertion_error testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_assertion_error.py:7: AssertionError
    =============================== short test summary info ===============================
    FAILED tests/test_assertion_error.py::Testassertion_error::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ==================================

  the computer makes a `Test Driven Development`_ environment for a project called :ref:`assertion_error<AssertionError>` and runs :ref:`the first failing test<test_failure>`. I continue this in :ref:`AssertionError`

----

********************************************************************************************
review
********************************************************************************************

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen a way to make a Python_ `Test Driven Development`_ Environment, and have a :ref:`program<makePythonTdd.ps1>` to do it for you on any Windows_ computer without `Windows Subsystem for Linux`_.

:ref:`How many questions can you answer after going through this chapter?<questions about making a Python Test Driven Development Environment on Windows without Windows Subsystem for Linux>`

Would you like to :ref:`test AssertionError?<AssertionError>`

----

:ref:`Click Here to see the code for the program to make a Python Test Driven Development environment for any Linux or MacOS computers<makePythonTdd.ps1>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->