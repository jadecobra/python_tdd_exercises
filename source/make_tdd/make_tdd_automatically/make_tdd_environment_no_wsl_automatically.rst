.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watcher for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

#######################################################################################################################
how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux
#######################################################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
preview
*********************************************************************************

Here is the program_ I have by the end of the chapter to :ref:`automatically make a python test driven development environment <how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux>`, it is only 27 lines of code, with spaces

.. literalinclude:: ../../code/make_tdd/makePythonTddNoVariables.ps1
  :language: PowerShell
  :linenos:

*************************************************************************************************************************************
questions about making a Python Test Driven Development Environment automatically on Windows without Windows Subsystem for Linux
*************************************************************************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`how can I make a PowerShell script?<how to make a PowerShell script>`
* :ref:`how can I run a PowerShell script?<how to run a PowerShell script>`

----

*********************************************************************************
how to make a PowerShell script
*********************************************************************************

* I go to the terminal_ and use `New-Item`_ to make an empty file_ with a name that is easy to remember later. I want the name to also describe the program_ that will automatically make a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for me

  .. code-block:: PowerShell
    :emphasize-lines: 1

    New-Item makePythonTdd.ps1

  the terminal_ goes back to the command line

* I open ``makePythonTdd.ps1`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then add the commands I use to make a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for a project

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
    "pytest-watcher" | Out-File requirements.txt -Encoding UTF8
    python -m pip install --requirement requirements.txt
    pytest-watcher

* ``test_magic_again.py`` is an empty file_ becuase I used `New-Item`_. I want it to have the text for :ref:`the first failure<test_failure on Windows without WSL>` so I do not have to open the :ref:`editor<2 editors>` to add the text for it in each project. I use `Out-File`_ to add the text to ``test_magic_again.py`` when it makes the file_ in the ``tests`` folder_, the same I do with the ``requirements.txt`` file_

  .. code-block:: shell
    :lineno-start: 5
    :emphasize-lines: 4

    mkdir tests
    New-Item tests/__init__.py

    "" | Out-File "tests/test_magic.py" -Encoding UTF8

    python -m venv .venv
    .venv/scripts/activate.ps1

* I add the text for the test inside the :ref:`quotes ("")<quotes>` I just added to ``makePythonTdd.sh``, the way I do with `Out-File`_ when I add ``"pytest-watcher"`` as text in ``requirements.txt``

  .. CAUTION:: Indentation_ is important in Python_, I use 4 spaces as convention in this book, see the :PEP:`Python Style Guide <8>` for more

  .. code-block:: PowerShell
    :lineno-start: 8
    :emphasize-lines: 1-12

    "import unittest


    class TestMagicAgain(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
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

    ================================= FAILURES =================================
    ________________________ TestMagicAgain.test_failure ________________________

    self = <tests.test_magic_again.TestMagicAgain testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic_again.py:7: AssertionError
    ====================== short test summary info ========================
    FAILED tests/test_magic_again.py::TestMagicAgain::test_failure - AssertionError: True is not false
    ============================ 1 failed in X.YZs =============================

  Success! I just made a program_ that can make the ``magic_again`` project anytime I want and it automatically does the steps I did manually.

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_magic_again.py`` to open it in the :ref:`editor<2 editors>` then make the test pass

* I click in the terminal_ and use :kbd:`q` on the keyboard to leave the tests and the terminal_ goes back to the command line
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

* I want to use ``makePythonTdd.ps1`` to make another project with a different name. I change ``magic_again`` to the name of the new project in the :ref:`editor<2 editors>`

  .. NOTE:: The lines that are changing in the code are highlighted

  .. code-block:: PowerShell
    :linenos:
    :emphasize-lines: 1, 2, 4, 11, 19

    mkdir more_magic
    cd more_magic
    mkdir src
    touch src/more_magic.py
    mkdir tests
    touch tests/__init__.py

    "import unittest


    class TestMoreMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError
    " | Out-File "tests/test_more_magic.py" - Encoding UTF8

* I run ``makePythonTdd.ps1`` in the terminal_ to make a project named ``more_magic``

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.ps1

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: PowerShell
    :emphasize-lines: 10

    ================================= FAILURES =================================
    ________________________ TestMoreMagic.test_failure _________________________

    self = <tests.test_more_magic.TestMoreMagic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_more_magic.py:7: AssertionError
    ====================== short test summary info ========================
    FAILED tests/test_more_magic.py::TestMoreMagic::test_failure - AssertionError: True is not false
    ============================ 1 failed in X.YZs =============================

  I make the test pass

* I click in the terminal_ and use :kbd:`q` on the keyboard to leave the tests and the terminal_ goes back to the command line

the program_ works and can make a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` automatically the way I want every time

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_more_magic.py`` in the :ref:`editor<2 editors>` I had open
* I click in the terminal_ and use :kbd:`ctrl+c` on the keyboard to leave the tests
* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    ...\pumping_python\more_magic

* I `change directory`_ to the parent of ``more_magic``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    ...\pumping_python

  I am back in the ``pumping_python`` directory_

----

********************************************************************************************
review
********************************************************************************************

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen a way I can make a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>`, with a :ref:`program<makePythonTdd.ps1>` to do it on any Windows_ computer without `Windows Subsystem for Linux`_.

:ref:`How many questions can you answer after going through this chapter?<questions about making a Python Test Driven Development Environment on Windows without Windows Subsystem for Linux>`

----

:ref:`Click Here to see the code for the program to make a Python Test Driven Development environment for any Linux or MacOS computers<makePythonTdd.ps1>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have gone through a few things

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux`

:ref:`Would you like to use makePythonTdd.ps1 to make a Python Test Driven Development environment to test that an Exception is raised?<how to test that an Exception is raised>`

-----

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