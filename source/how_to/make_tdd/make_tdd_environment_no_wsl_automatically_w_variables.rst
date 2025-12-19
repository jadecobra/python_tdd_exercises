.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watch for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

########################################################################################################
how to make a python test driven development environment on Windows without Windows Subsystem for Linux with variables
########################################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

``makePythonTdd.ps1`` works and always makes a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` the way I want it, but there is a problem

--------------------------------------------------------------------------------------------
how to use a variable in a PowerShell script
--------------------------------------------------------------------------------------------

I changed ``magic`` to ``more_magic`` in 5 places in ``makePythonTdd.sh``. I would have to do the same change every time I have a new project, and I want to follow `The Do Not Repeat Yourself (DRY) Principle`_. I want the program_ to take a project name once and use that name when making the project to make the following

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

    $PROJECT_NAME="more_magic"
    mkdir more_magic
    cd more_magic
    mkdir src
    touch src/more_magic.py
    mkdir tests
    touch tests/__init__.py

    "import unittest


    class TestMagicAgain(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " | Out-File "tests/test_more_magic.py" - Encoding UTF8

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    "pytest-watch" | Out-File requirements.txt -Encoding UTF 8
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  a :ref:`variable<test_attribute_error_w_variables>` is a name that is used for a value that can change. For example, we use the word ``woman`` to represent any woman, ``man`` to represent any man, ``child`` to represent any child, and ``parent`` to represent anyone with a child. In this case I use ``$PROJECT_NAME`` to represent any name of a project

* I change every where I have ``more_magic`` in the program, to use the :ref:`variable<test_attribute_error_w_variables>` I just added so that I only have to make a change in one place

  .. NOTE:: The lines that are changing in the code are highlighted

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 2-3, 5, 12, 20

    $PROJECT_NAME="more_magic"
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
    ____________________________ Testmore_magic.test_failure ______________________________

    self = <tests.test_magic.Testmore_magic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_more_magic.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_more_magic.py::Testmore_magic::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in ``tests/test_more_magic.py`` to make the test pass

* I hit :kbd:`ctrl+c` in the terminal to stop the test
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
    ├── more_magic
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

* I change ``more_magic`` to ``$args[0]`` in ``makePythonTdd.ps1``

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
    ├── more_magic
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

* I can now make a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` with ``makePythonTdd.ps1`` when I give it a name for the ``PROJECT_NAME`` variable_. For example, when I type this in the terminal_

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

  the computer makes a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for a project called :ref:`assertion_error<AssertionError>` and runs :ref:`the first failing test<test_failure>`. I continue this in :ref:`AssertionError`

----

********************************************************************************************
review
********************************************************************************************

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen a way to make a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>`, and have a :ref:`program<makePythonTdd.ps1>` to do it for you on any Windows_ computer without `Windows Subsystem for Linux`_.

:ref:`How many questions can you answer after going through this chapter?<questions about making a Python Test Driven Development Environment on Windows without Windows Subsystem for Linux>`

:ref:`Would you like to test AssertionError?<AssertionError>`

----

:ref:`Click Here to see the code for the program to make a Python Test Driven Development environment for any Linux or MacOS computers<makePythonTdd.ps1>`

----

*********************************************************************************
please leave a review
*********************************************************************************

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 5 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->