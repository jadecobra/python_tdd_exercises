.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watch for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

#################################################################################
how to make a test driven development environment part 2
#################################################################################

You made it this far and have become `the greatest programmer in the world`_. To follow `The Do Not Repeat Yourself (DRY) Principle`_, I write a program_ with the commands to make  a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` automatically anytime I want on a

* :ref:`Windows Computer that does NOT have Windows Subsystem for Linux<how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux>`
* :ref:`computer with MacOS, Linux or Windows with Windows Subsystem for Linux<how to make a Python Test Driven Development environment automatically>`

*********************************************************************************
review
*********************************************************************************

To review, here are steps I take to make the environment for every project

on a computer with MacOS_, Linux_ or `Windows`_ with `Windows Subsystem for Linux`_

#. I give the project a name
#. :ref:`I make a directory for the project<how to make a directory for the project>`
#. :ref:`I change directory to the project<how to change directory to the project>`
#. :ref:`I make a directory for the source code named 'src'<how to make a directory for the source code>`
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

on a Windows_ computer without `Windows Subsystem for Linux`_

#. I give the project a name
#. :ref:`I make a directory for the project<how to make a directory for the project on Windows without WSL>`
#. :ref:`I change directory to the project<how to change directory to the project on Windows without WSL>`
#. :ref:`I make a directory for the source code named 'src'<how to make a directory for the source code on Windows without WSL>`
#. :ref:`I make a Python file to hold the source code in the 'src' folder<how to make an empty file on Windows without Windows Subsystem for Linux>`
#. :ref:`I make a directory for the tests<how to make a directory for the tests on Windows without WSL>`
#. :ref:`I make the 'tests' folder a Python package<how to make the tests a Python package on Windows without WSL>`
#. :ref:`I make a Python file to hold the tests in the 'tests' folder<test_failure on Windows without WSL>`
#. :ref:`I add the first failing test to the test file<test_failure on Windows without WSL>`
#. :ref:`I make a virtual environment<how to make a virtual environment on Windows without WSL>`
#. :ref:`I activate the virtual environment<how to activate a virtual environment on Windows without WSL>`
#. :ref:`I upgrade the Python package manager<how to upgrade the Python package manager in a virtual environment on Windows without WSL>`
#. :ref:`I make a requirements file for the needed Python packages<how to write text to a file on Windows without Windows Subsystem for Linux>`
#. :ref:`I install the packages listed in the requirements file<how to install Python packages in a virtual environment on Windows without WSL>`
#. :ref:`I run the tests automatically<how to run the tests automatically on Windows without Windows Subsystem for Linux>`
#. :ref:`I open the test file in the editor from the terminal<how to open the test file in the editor from the terminal_ on Windows without WSL>`
#. I make the test pass
#. then I start working on the project

I want to give one command for the program_, the only steps I want to do are

* give the project a name
* make the test pass and
* work on the project (though I can now use `Artificial Intelligence`_ to help with all of them)

this way I only need to do 3 steps instead of 18

As a reminder here is what the structure looks like if the name of the project is ``PROJECT_NAME``

.. code-block:: shell

  PROJECT_NAME
  ├── requirements.txt
  ├── src
  │   └── PROJECT_NAME.py
  └── tests
      └── test_PROJECT_NAME.py

----

*********************************************************************************
what is covered?
*********************************************************************************

These chapters show how I setup a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` automatically on any computer (Linux_, Windows_, MacOS_)

.. toctree::
  :titlesonly:

  make_tdd_environment_automatically
  make_tdd_environment_no_wsl_automatically

they cover the following

=================================================================================
on Linux, MacOS and Windows with Window Subsystem for Linux computers
=================================================================================

* :ref:`how to make a shell script`
* :ref:`how to view the permissions of a file`
* :ref:`how to make a shell script run as a command`
* :ref:`how to run a shell script`

=================================================================================
On Windows computers without Windows Subsystem for Linux
=================================================================================

* :ref:`How can I make a PowerShell script?<how to make a PowerShell script>`
* :ref:`How can I run a PowerShell script<how to run a PowerShell script>`

----

at the end of the chapter you will know how to automatically make a :ref:`Python Test Driven Development project<what is a Test Driven Development Environment?>` for MacOS_, Linux_, `Windows Subsystem for Linux`_ and Windows_ without `Windows Subsystem for Linux`_

----

*********************************************************************************
what is next?
*********************************************************************************

* :ref:`how to make a Python Test Driven Development environment automatically` or
* :ref:`how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux`

-----

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>