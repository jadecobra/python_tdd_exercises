.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with a single script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watch for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

#################################################################################
What is a Test Driven Development Environment?
#################################################################################

A `Test Driven Development`_ environment is a collection of files_ and folders_ in a project where I can write automated tests and code and see the results of running them immediately.

#################################################################################
What is the Test Driven Development cycle?
#################################################################################

The `Test Driven Development`_ cycle is ``RED GREEN REFACTOR``

* **RED**: make it fail - write a test that fails to make sure the test works
* **GREEN**: make it pass - write the simplest thing that will make the failing test pass
* **REFACTOR**: make it better - write a better solution, test or both, usually by `removing duplication`_

This process can be repeated as many times as needed until I get to my goal.

#################################################################################
how to make a test driven development environment
#################################################################################

I set up an environment for every Python_ project, this way I keep all the things that belong to the project in the same place. I can do this manually, which means I have to do the same exact steps for every project or I could do it automatically where I give the computer a command and it does all those steps for me.

These chapters show how I setup a project in Python_ on any computer (Linux_, Windows_, MacOS_)to help you get started with `Test Driven Development`_ right now

.. toctree::
  :titlesonly:

  make_tdd_environment
  install_wsl
  make_tdd_environment_no_wsl

they cover the following

* :ref:`Windows requirements`
* :ref:`Linux/Windows Subsystem for Linux requirements`

on Linux_, MacOS_ and Windows_ with `Windows Subsystem for Linux`_

* :ref:`how to manually make a python test driven development environment`
* :ref:`how to automatically make a python test driven development environment`
* :ref:`how to change directory`
* :ref:`how to make a directory`
* :ref:`how to look at directory structure`
* :ref:`how to make an empty file`
* :ref:`how to write text to a file`
* :ref:`how to see what is inside a file`
* :ref:`how to change the name of a file`
* :ref:`how to run a Python program`
* :ref:`the first failing test<test_failure>`
* :ref:`how to make a Python package`
* :ref:`how to run tests manually`
* :ref:`how to run tests automatically`
* :ref:`how to exit the automated tests`
* :ref:`how to make a virtual environment`
* :ref:`how to activate a virtual environment`
* :ref:`how to deactivate a virtual environment`
* :ref:`how to write text to a file`
* :ref:`how to install Python packages in a virtual environment`
* :ref:`how to see what packages are installed in a virtual environment`
* :ref:`how to view all the commands I typed in a terminal`
* :ref:`how to make a shell script`
* :ref:`how to use variables in a shell script`
* :ref:`how to make a shell script run as a command`
* :ref:`how to run a shell script`

On Windows_ without `Windows Subsystem for Linux`

* :ref:`how to manually make a python test driven development environment on Windows without Windows Subsystem for Linux`
* :ref:`how to automatically make a python test driven development environment on Windows without Windows Subsystem for Linux`
* :ref:`how to make an empty file on Windows without Windows Subsystem for Linux`
* :ref:`how to write text to a file on Windows without Windows Subsystem for Linux`
* :ref:`how to change the name of a file on Windows without WSL`
* :ref:`how to run a Python program on Windows without Windows Subsystem for Linux`
* :ref:`test_failure on Windows without WSL`
* :ref:`how to make a Python package on Windows without WSL`
* :ref:`how to run tests manually on Windows without WSL`
* :ref:`how to run tests automatically on Windows without Windows Subsystem for Linux`
* :ref:`how to exit the automated tests on Windows without WSL`
* :ref:`how to make a virtual environment on Windows without WSL`
* :ref:`how to make a virtual environment on Windows without WSL`
* :ref:`how to activate a virtual environment on Windows without WSL`
* :ref:`how to deactivate a virtual environment on Windows without WSL`
* :ref:`how to write text to a file on Windows without Windows Subsystem for Linux`
* :ref:`how to install Python packages in a virtual environment on Windows without WSL`
* :ref:`how to see what packages are installed in a virtual environment on Windows without WSL`
* :ref:`how to view all the commands I typed in a terminal on Windows without WSL`
* :ref:`how to make a PowerShell script`
* :ref:`how to use variables in a shell script`
* :ref:`how to use variables in a PowerShell script`
* :ref:`how to use variables in a PowerShell script`
* :ref:`how to run a PowerShell script`
* :ref:`test_failure on Windows without WSL`

----

the programs to automatically setup a Python_ `Test Driven Development`_ project

* :ref:`makePythonTdd.sh` - for MacOS_, Linux_ and `Windows Subsystem for Linux`_
* :ref:`makePythonTdd.ps1` - for Windows_ without `Windows Subsystem for Linux`_
