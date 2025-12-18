.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watch for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

#################################################################################
how to automatically make a python test driven development environment
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

You made it this far and have become `the greatest programmer in the world`_. To follow `The Do Not Repeat Yourself (DRY) Principle`_, I write a program_ with the commands to make  a Python_ `Test Driven Development`_ Environment anytime I want so I do not have to remember every step of the process or do them manually.

To review, here are steps I take to make the environment for every project

#. I pick a name for the project
#. :ref:`I make a directory for the project<how to make a directory for the project>`
#. :ref:`I change directory to the project<how to change directory to the project>`
#. :ref:`I make a directory for the source code<how to make a directory for the source code>`
#. :ref:`I make a Python file to hold the source code in the 'src' folder<how to make an empty file>`
#. :ref:`I make a directory for the tests<how to make a directory for the tests>`
#. :ref:`I make the 'tests' folder a Python package<how to make the tests a Python package>`
#. :ref:`I make a Python file to hold the tests in the 'tests' folder<test_failure>`
#. :ref:`I add the first failing test to the test file<test_failure>`
#. :ref:`I make a virtual environment<how to make a virtual environment>`
#. :ref:`I activate the virtual environment<how to activate a virtual environment>`
#. :ref:`I upgrade the Python package manager<how to upgrade the Python package manager in a virtual environment>`
#. :ref:`I make a requirements file for the needed Python packages<how to write text to a file>`
#. :ref:`I install the packages listed in the requirements file<how to install Python packages in a virtual environment>`
#. :ref:`I run the tests automatically<how to run the tests automatically in a virtual environment>`
#. :ref:`I open the test file in the editor from the terminal<how to open the test file in the editor from the terminal>`
#. I make the test pass
#. then I start working on the project

I want to give one command for the program to do every step except

* pick the name for the project
* make the test pass and
* work on the project, though I can now use an LLM_ to help with this

this way I only need to do 3 steps instead of 18

*********************************************************************************
preview
*********************************************************************************

Here is the program_ I have by the end of the chapter to :ref:`automatically make a python test driven development environment <how to automatically make a python test driven development environment>`, it is only 28 lines of code, with spaces

.. literalinclude:: ../../code/make_tdd/makePythonTdd.sh
  :language: shell
  :linenos:

*********************************************************************************
questions about automatically making a Python Test Driven Development Environment
*********************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`what is a Test Driven Development Environment?`
* :ref:`How can I make a Python Test Driven Development Environment manually?<how to manually make a python test driven development environment>`
* :ref:`How can I make a Python Test Driven Development Environment automatically?<how to automatically make a python test driven development environment>`
* :ref:`How can I change directories?<how to change directory>`
* :ref:`How can I make a directory?<how to make a directory>`
* :ref:`How can I see directory structure?<how to look at directory structure>`
* :ref:`How can I make an empty file?<how to make an empty file>`
* :ref:`How can I write text to a file?<how to write text to a file>`
* :ref:`How can I see what is inside a file?<how to see what is inside a file>`
* :ref:`How can I change the name of a file?<how to change the name of a file>`
* :ref:`How can I run a Python Program?<how to run a Python program>`
* :ref:`How can I test for failure?<test_failure>`
* :ref:`How can I make a Python package?<how to make the tests a Python package>`
* :ref:`How can I run tests manually?<how to manually run tests>`
* :ref:`How can I run tests automatically?<how to automatically run tests>`
* :ref:`How can I stop automated Python tests from running?<how to stop the automated tests>`
* :ref:`What is a Virtual Environment?<what is a virtual environment?>`
* :ref:`How can I make a Virtual Environment?<how to make a virtual environment>`
* :ref:`How can I activate a Virtual Environment?<how to activate a virtual environment>`
* :ref:`How can I deactivate a Virtual Environment?<how to deactivate a virtual environment>`
* :ref:`How can I document the Python programs my project needs?<how to write text to a file>`
* :ref:`How can I install the Python programs my project needs from a file?<how to install Python packages in a virtual environment>`
* :ref:`How can I install Python packages in a Virtual Environment?<how to install Python packages in a virtual environment>`
* :ref:`How can I see what Python packages are installed in a Virtual Environment?<how to see what packages are installed in a virtual environment>`
* :ref:`How can I view all the commands I type in a terminal?<how to view all the commands I typed in a terminal>`
* :ref:`How can I make a shell script?<how to make a shell script>`
* :ref:`What is a variable?<how to use a variable in a shell script>`
* :ref:`How can I use a variable in a shell script<how to use a variable in a shell script>`
* :ref:`How can I view the permissions of a file?<how to view the permissions of a file>`
* :ref:`How can I make a shell script run as a command<how to make a shell script run as a command>`
* :ref:`How can I run a shell script<how to run a shell script>`

----

*********************************************************************************
how to make a shell script
*********************************************************************************

* I go to the terminal_ and use touch_ to make an empty file_ with a name that is easy to remember later and describes the program_ that will automatically make a `Test Driven Development`_ environment for me

  .. code-block:: shell
    :emphasize-lines: 1

    touch makePythonTdd.sh

  the terminal_ goes back to the command line

* I open ``makePythonTdd.sh`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then add the commands I use to make the Python_ `Test Driven Development`_ environment

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 1-

    #!/bin/bash
    mkdir magic
    cd magic
    mkdir src
    touch src/magic.py
    mkdir tests
    touch tests/__init__.py
    touch tests/test_magic.py
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    echo "pytest-watch" > requirements.txt
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  ``#!/bin/bash`` is called a shebang_ line, it tells the computer to use bash_ to run this program_

* ``test_magic.py`` is an empty file_ because I used touch_. I want it to have the text for :ref:`the first failure<test_failure>` so I do not have to open the :ref:`editor<2 editors>` to add the text for each project. I use echo_ instead of touch_ to make the ``makePythonTdd.sh`` program_ add the text to ``test_magic.py`` when it makes the file in the ``tests`` folder_

  .. code-block:: shell
    :lineno-start: 6
    :emphasize-lines: 4

    mkdir tests
    touch tests/__init__.py

    echo "" > tests/test_magic.py

    python3 -m venv .venv
    source .venv/bin/activate

* I add the text for the test inside the :ref:`quotes ("")<quotes>`, the way I do with echo_ when I add ``"pytest-watch"`` as text in ``requirements.txt`` I just added to ``makePythonTdd.sh``

  .. CAUTION:: Indentation_ is important in Python_, I use 4 spaces as convention in this book, see the :PEP:`Python Style Guide <8>` for more

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 8-21

    #!/bin/bash
    mkdir magic
    cd magic
    mkdir src
    touch src/magic.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " > tests/test_magic.py

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    echo "pytest-watch" > requirements.txt
    python3 -m pip install --requirement requirements.txt
    pytest-watch

--------------------------------------------------------------------------------------------
how to run a shell script
--------------------------------------------------------------------------------------------

I go back to the terminal_ to run the program_

.. code-block:: shell
  :emphasize-lines: 1

  makePythonTdd.sh

the terminal_ shows

.. code-block:: shell

  command not found: makePythonTdd.sh

I have to tell the computer where the file_ is

.. code-block:: shell
  :emphasize-lines: 1

  ./makePythonTdd.sh

``./`` is shorthand for ``this directory`` which in this case is ``pumping_python`` where ``makePythonTdd.sh`` is saved. The computer checks a few directories_ when a command is given. Those directories are where commands like mkdir_, cd_, tree_ and echo_ are saved. The terminal_ shows

.. code-block:: shell

  permission denied: ./makePythonTdd.sh

I want to make sure the computer can run the program_. I have to make it executable

--------------------------------------------------------------------------------------------
how to view the permissions of a file
--------------------------------------------------------------------------------------------

I use ls_ to check the permissions of the file_

.. code-block:: shell
  :emphasize-lines: 1

  ls -l makePythonTdd.sh

``-l`` is the option to show the long listing format which includes permissions for the file_

the terminal_ shows

.. code-block:: shell

  -rw-r--r-- 1 abcdef ghijk XX Month  Y ZA:BC makePythonTdd.sh

here is what each one of the characters before the folder_ means

* ``-`` means this is a regular file_, it is not a directory_
* ``rw-`` means the owner of the file_ can read and write to the file_ but not execute it
* ``r--`` means the group on the computer the owner of the file_ belongs to can only read the file_, they cannot write to it or execute it, and the second
* ``r--`` means other users can only read the file_, they cannot write to it or execute it

I want to add execute permissions so I can run the file

--------------------------------------------------------------------------------------------
how to make a shell script run as a command
--------------------------------------------------------------------------------------------

* I change the mode of the file_ to add executable permissions

  .. code-block:: shell
    :emphasize-lines: 1

    chmod +x makePythonTdd.sh

  chmod_ is a program_ that changes the mode (permissions) of the given file_, the terminal_ goes back to the command line. I use chmod_ to make the file_ executable so the computer can run it

* I list the permissions again with ls_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -l makePythonTdd.sh

  the terminal_ shows

  .. code-block:: shell

    -rwxr-xr-x 1 abcdef ghijk XX Month  Y ZA:BC makePythonTdd.sh

  here is what each one of the characters before the folder_ means

  * ``-`` means this is a regular file_, it is not a directory_
  * ``rwx`` means the owner of the file_ has permissions to read, write to and execute it
  * ``r-x`` means the group the owner of the file_ belongs to has permissions to read and execute the file_ they cannot write to it, and the second
  * ``r-x`` means other users have permissions to read and execute the file_, they cannot write to it

* I try the command again

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 10

    ======================================= FAILURES =======================================
    ________________________________ TestMagic.test_failure ________________________________

    self = <tests.test_magic.TestMagic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_magic.py::TestMagic::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

  Success! I just made a program_ that can make the ``magic`` project anytime I want and it automatically does the steps I did manually.

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_magic.py`` to open it in the :ref:`editor<2 editors>` then make the test pass

* I hit :kbd:`ctrl+c` in the terminal_ to stop the test

* I want to use ``makePythonTdd.sh`` to make another project with a different name. I change ``magic`` to the name of the new project in the :ref:`editor<2 editors>`

  .. NOTE:: The lines that are changing in the code are highlighted

  .. code-block::
    :linenos:
    :emphasize-lines: 2, 3, 5, 12, 20

    #!/bin/bash
    mkdir magic_again
    cd magic_again
    mkdir src
    touch src/magic_again.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestMagicAgain(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " > tests/test_magic_again.py

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    echo "pytest-watch" > requirements.txt
    python3 -m pip install --requirement requirements.txt
    pytest-watch

* I run ``makePythonTdd.sh`` in the terminal_ to make a project named ``magic_again``

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell
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

    tree -a -L 2

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
how to use a variable in a shell script
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

* I add a name to represent any project name that I give to ``makePythonTdd.sh`` when I want it to make a project

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 2

    #!/bin/bash
    PROJECT_NAME="magic_again"
    mkdir magic_again
    cd magic_again
    mkdir src
    touch src/magic_again.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestMagicAgain(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " > tests/test_magic_again.py

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    echo "pytest-watch" > requirements.txt
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  a :ref:`variable<test_attribute_error_w_variables>` is a name that is used for a value that can change. For example, we use the word ``woman`` to represent any woman, ``man`` to represent any man, ``child`` to represent any child, and ``parent`` to represent anyone with a child. In this case I use ``$PROJECT_NAME`` to represent any name of a project

* I change every where I have ``magic_again`` in the program, to use the :ref:`variable<test_attribute_error_w_variables>` I just added so that I only have to make a change in one place

  .. NOTE:: The lines that are changing in the code are highlighted

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 3-4, 6, 13, 21

    #!/bin/bash
    PROJECT_NAME="magic_again"
    mkdir $PROJECT_NAME
    cd $PROJECT_NAME
    mkdir src
    touch src/$PROJECT_NAME.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class Test$PROJECT_NAME(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " > tests/test_$PROJECT_NAME.py

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    echo "pytest-watch" > requirements.txt
    python3 -m pip install --requirement requirements.txt
    pytest-watch

* I run the program_ again in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

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

* I run tree_ to see what I have in the ``pumping_python`` folder_ now

  .. code-block:: shell
    :emphasize-lines: 1

    tree -a -L 2

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

* The program_ works as expected, and I only need to give the project name in one place. It would be nice if I do not have to go into the file_ to give it the project name. I want to be able to just call the program_ and give it a name for the project from the command line. I can do this with ``$1`` in bash_, it represents the first argument given when a program_ is called. For example,

  .. code-block:: shell

    command argument

  in the code above, :kbd:`command` will be ``./makePythonTdd.sh`` and ``$1`` will be ``argument`` or whatever name I give.

  Here are a few other examples

  .. code-block:: shell

    mkdir name_of_folder

  ``mkdir`` is the command, and ``$1`` is ``name_of_folder``

  .. code-block:: shell

    touch name_of_file

  ``touch`` is the command, and ``$1`` is ``name_of_file``

  .. code-block:: shell

    echo "anything"

  ``echo`` is the command, and ``$1`` is ``"anything"``

  .. code-block:: shell

    tree -a

  ``tree`` is the command and ``$`` is ``-a``

* I change ``magic_again`` to ``$1`` in ``makePythonTdd.sh``

  .. code-block:: shell
    :lineno-start: 2
    :emphasize-lines: 1

    PROJECT_NAME=$1

* I try the program_ again, this time with a different name for the project in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh more_magic

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

* I run tree_ to see what I have in the ``pumping_python`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    tree -a -L 2

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

* I can now make a `Test Driven Development`_ environment with ``makePythonTdd.sh`` when I give it a name for the ``PROJECT_NAME`` variable_. For example, when I type this in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh assertion_error

  the terminal_ shows

  .. code-block:: shell

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

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen a way to make a Python_ `Test Driven Development`_ Environment, and have a :ref:`program<makePythonTdd.sh>` to do it for you on any Linux_, Windows_ or MacOS_ computers.

:ref:`How many questions can you answer after going through this chapter?<questions about making a Python Test Driven Development Environment>`

----

:ref:`Click Here to see the code for the program to make a Python Test Driven Development environment for any Linux or MacOS computers<makePythonTdd.sh>`

----

Would you like to :ref:`test AssertionError?<AssertionError>`

-----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->