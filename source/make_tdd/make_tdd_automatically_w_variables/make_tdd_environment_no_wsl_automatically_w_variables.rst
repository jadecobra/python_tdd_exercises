:orphan:

.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watcher for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

############################################################################################################################
how to make a python test driven development environment on Windows without Windows Subsystem for Linux with variables
############################################################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

********************************************************************************************
how to use a variable in a PowerShell script
********************************************************************************************

``makePythonTdd.ps1`` works and always makes a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>` the way I want it, but there is a problem


I change the name of the project in 5 places every time I use the program to make a project. I want the program_ to take a project name once and use that name when making the project to make the following

- the project folder_
- the file_ for the program_ in the ``src`` folder_
- the file_ for the test in the ``tests`` folder_
- the :ref:`test class<what is a class?>` in the test file_
- the `virtual environment`_ in the ``.venv`` folder_

The program_ should always make this structure

.. code-block:: shell
  :emphasize-text: PROJECT_NAME

  PROJECT_NAME
  ├── requirements.txt
  ├── src
  │   └── PROJECT_NAME.py
  ├── tests
  │   ├── __init__.py
  │   └── test_PROJECT_NAME.py
  └── .venv

Time to use a :ref:`variable<what is a variable?>` for the name of the project

* I open ``makePythonTdd.ps1`` in the :ref:`editor<2 editors>`

  .. TIP:: Here is a quick way to open ``makePythonTdd.ps1`` if you are using `Visual Studio Code`_

    .. code-block:: python
      :emphasize-lines: 1

      code makePythonTdd.ps1

* I add a name to represent any project name that I give to ``makePythonTdd.ps1`` when I want it to make a project

  .. code-block:: PowerShell
    :linenos:
    :emphasize-lines: 1

    $PROJECT_NAME="dictionaries"
    mkdir dictionaries
    cd dictionaries

  a :ref:`variable<what is a variable?>` is a name that is
  used for a value that can change. For example, we use the word

  * ``woman`` to represent any woman
  * ``man`` to represent any man
  * ``child`` to represent any child
  * ``parent`` to represent anyone with a child.

  In this case I use ``$PROJECT_NAME`` to represent any name of a project

* I change every where I have ``dictionaries`` in the program, to use the :ref:`variable<what is a variable?>` I just added so that I only have to make a change in one place

  .. NOTE:: The lines that are changing in the code are highlighted

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 2-3, 5, 12, 20

    $PROJECT_NAME="dictionaries"
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


    # Exceptions seen
    # AssertionError
    " | Out-File "tests/test_$PROJECT_NAME.py" - Encoding UTF8

* Since I already did some work in the :ref:`dictionaries<what is a dictionary?>` project. I do not want the program_ to write over it. I change the name of the project to ``pro_magic`` because I am a professional

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 1
    :emphasize-text: pro_magic

    $PROJECT_NAME="pro_magic"
    mkdir $PROJECT_NAME
    cd $PROJECT_NAME

* I run the program_ again in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.ps1

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2, 4, 10, 12

    ================================= FAILURES =================================
    _______________________ Testpro_magic.test_failure _________________________

    self = <tests.test_pro_magic.Testpro_magic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_pro_magic.py:7: AssertionError
    ========================= short test summary info ==========================
    FAILED tests/test_pro_magic.py::Testpro_magic::test_failure - AssertionError: True is not false
    ============================ 1 failed in X.YZs =============================

this program_ does not make the class names in the :ref:`CapWords format<CapWords>` so they are in :ref:`snake_case` when made but :ref:`there is a better way<BONUS: makePythonTdd.sh Plus>`

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/pro_magic.py`` in the terminal_ to open it in the :ref:`editor<2 editors>`

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

* I use :kbd:`ctrl+c` in the terminal_ to stop the test
* I deactivate the `virtual environment`_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line

* I leave the ``pro_magic`` folder to go back to the ``pumping_python`` folder_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: PowerShell

    ...\pumping_python

The program_ does what I want, and I only need to give the project name in one place. It would be nice if I do not have to go into the file_ to give it the project name.

----

********************************************************************************************
how to call a PowerShell script with arguments
********************************************************************************************

I want to be able to call the program_ and give it a name for the project from the command line. I can do this with ``$[args]`` in PowerShell_, it represents the first argument given when a program_ is called. For example

.. code-block:: PowerShell

    command argument

  in the code above, :kbd:`command` is the name of the program_ and ``$args[0]`` is ``argument``

Here are a few other examples

.. code-block:: PowerShell

  mkdir folder_name

``mkdir`` is the command, and ``$args[0]`` is ``folder_name``

.. code-block:: PowerShell

  New-Item file_name

``New-Item`` is the command, and ``$args[0]`` is ``file_name``

.. code-block:: PowerShell

  echo "echo"

``echo`` is the command, and ``$args[0]`` is ``"echo"``

.. code-block:: PowerShell

  tree /F

``tree`` is the command ``$args[0]`` is ``/F``

----

* I change ``pro_magic`` to ``$args[0]`` in ``makePythonTdd.ps1``

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 1
    :emphasize-text: args

    $PROJECT_NAME=$args[0]

* I try the program_ again, this time with a different name for the project in the terminal_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    ./makePythonTdd.ps1 pro_magic_plus

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 10

    ================================= FAILURES =================================
    ____________________ Testpro_magic_plus.test_failure _______________________

    self = <tests.test_pro_magic_plus.Testpro_magic_plus testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_pro_magic_plus.py:7: AssertionError
    ========================= short test summary info ==========================
    FAILED tests/test_pro_magic_plus.py::Testpro_magic_plus::test_failure - AssertionError: True is not false
    ============================ 1 failed in X.YZs =============================

* I hold :kbd:`ctrl` on the keyboard in the terminal_ and click on ``tests/test_pro_magic_plus.py`` to open it in the :ref:`editor<2 editors>`, then make the test pass

* I use :kbd:`ctrl+c` on the keyboard in the terminal_ to stop the tests
* I deactivate the `virtual environment`_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line

* I leave the ``pro_magic_plus`` folder to go back to the ``pumping_python`` folder_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: PowerShell

    ...\pumping_python >

* I can now make a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` with ``makePythonTdd.ps1`` when I give it a name for the ``PROJECT_NAME`` variable_. For example, when I type this in the terminal_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    ./makePythonTdd.ps1 person

  the terminal_ shows

  .. code-block:: PowerShell

    ============================ FAILURES ==============================

    _________________________ Testperson.test_failure ___________________________

    self = <tests.test_person.Testperson testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_person.py:7: AssertionError
    =========================== short test summary info ===========================
    FAILED tests/test_person.py::Testperson::test_failure - AssertionError: True is not false
    ============================= 1 failed in X.YZs =============================

  the computer makes a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>` for a project called :ref:`person<how to make a person>` and runs :ref:`the first failing test<test_failure>`. I continue this in :ref:`how to make a person`

----

********************************************************************************************
review
********************************************************************************************

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen a way to make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>`, and have a :ref:`program<makePythonTdd.sh>` to do it for you on any Windows_ computer without `Windows Subsystem for Linux`_.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see the CODE for makePythonTdd.ps1?<makePythonTdd.ps1>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<list comprehensions>`
* :ref:`what you can do with dictionaries<dictionaries>`
* :ref:`how to make a Python Test Driven Development environment automatically with variables<how to make a test driven development environment 3>`

:ref:`would you like to test using dictionaries and functions to make a person?<how to make a person>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->