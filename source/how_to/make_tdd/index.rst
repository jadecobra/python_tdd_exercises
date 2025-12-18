.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watch for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

#################################################################################
how to make a test driven development environment
#################################################################################

*********************************************************************************
what is a Test Driven Development Environment?
*********************************************************************************

A `Test Driven Development`_ environment is a group of files_ and folders_ in a project where I can write tests and code and they automatically run so I see the results immediately.

*********************************************************************************
what is the Test Driven Development cycle?
*********************************************************************************

The `Test Driven Development`_ cycle is :red:`RED` :green:`GREEN` :yellow:`REFACTOR`

* :red:`RED`: make it :red:`fail` - write a test that :red:`fails` to make sure the test works
* :green:`GREEN`: make it :green:`pass` - write the simplest thing that will make the failing test :green:`pass`
* :yellow:`REFACTOR`: make it :yellow:`better` - write a :yellow:`better` solution, test or both, usually by `removing duplication`_

This process can be repeated as many times as needed until I get to my goal.

----

*********************************************************************************
preview
*********************************************************************************

I set up an environment for every Python_ project, this way I keep all the things that belong to the project in the same place. I can do this manually, which means I have to do the same exact steps for every project or I could do it automatically where I give the computer a command and it does all those steps for me.

Some things I think about when I want to start a project

* What name will I give the project? this is based on what the project will do. It's also one of the hardest things to do
* What is the structure of the project?
  - What files_ and folders_ does the project need?

* What other programs_ does my project need?
* What tests am I going to write for this project?

It turns out some of this is the same for every project

* I pick a name for the project
* I make a new folder_ for every project with the name I picked
* I place the code for the project in a ``src`` folder_
* I place the tests for the project in a ``tests`` folder_
* I try to name everything in the project with the name of the project or with something that describes what it does
* I write what programs the project needs (its dependencies) in a requirements file_
* I make a `virtual environment`_ to keep the dependencies separate from the rest of the computer
* I install what the project needs in the `virtual environment`_
* I work in the `virtual environment`_
* I run automated tests to make sure I have a `Test Driven Development`_ environment
* I start writing code for the project

Here is what that structure looks like if the name of the project is ``PROJECT_NAME``

.. code-block:: shell

  PROJECT_NAME
  ├── requirements.txt
  ├── src
  │   └── PROJECT_NAME.py
  └── tests
      └── PROJECT_NAME.py

----

These chapters show how I setup a project in Python_ on any computer (Linux_, Windows_, MacOS_) to help you get started with `Test Driven Development`_ right now

.. toctree::
  :titlesonly:

  make_tdd_environment
  install_wsl
  make_tdd_environment_no_wsl

they cover the following

* :ref:`Windows requirements`
* :ref:`Linux/Windows Subsystem for Linux requirements`

=================================================================================
on Linux, MacOS and Windows with `Window Subsystem for Linux computers
=================================================================================

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
* :ref:`how to make the tests a Python package`
* :ref:`how to manually run tests`
* :ref:`how to automatically run tests`
* :ref:`how to exit the automated tests`
* :ref:`how to make a virtual environment`
* :ref:`how to activate a virtual environment`
* :ref:`how to deactivate a virtual environment`
* :ref:`how to write text to a file`
* :ref:`how to install Python packages in a virtual environment`
* :ref:`how to see what packages are installed in a virtual environment`
* :ref:`how to view all the commands I typed in a terminal`
* :ref:`how to make a shell script`
* :ref:`how to run a shell script`
* :ref:`how to use a variable in a shell script`
* :ref:`how to make a shell script run as a command`
* :ref:`how to run a shell script`

=================================================================================
On Windows computers without Windows Subsystem for Linux
=================================================================================

* :ref:`how to manually make a python test driven development environment on Windows without Windows Subsystem for Linux`
* :ref:`how to automatically make a python test driven development environment on Windows without Windows Subsystem for Linux`
* :ref:`how to make an empty file on Windows without Windows Subsystem for Linux`
* :ref:`how to write text to a file on Windows without Windows Subsystem for Linux`
* :ref:`how to change the name of a file on Windows without WSL`
* :ref:`how to run a Python program on Windows without Windows Subsystem for Linux`
* :ref:`test_failure on Windows without WSL`
* :ref:`how to make the tests a Python package on Windows without WSL`
* :ref:`how to manually run tests on Windows without WSL`
* :ref:`how to automatically run tests on Windows without Windows Subsystem for Linux`
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
* :ref:`how to use a variable in a PowerShell script`
* :ref:`how to run a PowerShell script`
* :ref:`test_failure on Windows without WSL`

----

at the end of the chapter you will know how to make a Python_ `Test Driven Development`_ project for MacOS_, Linux_, `Windows Subsystem for Linux`_ and Windows_ without `Windows Subsystem for Linux`_

----

*********************************************************************************
what is next?
*********************************************************************************

* if you have MacOS_, Linux_ or successfully :ref:`installed Windows Subsystem for Linux<how to install Windows Subsystem for Linux on Windows>` you can do :ref:`how to make a python test driven development environment` or
* if you are not able to install `Windows Subsystem for Linux` check out :ref:`how to make a python test driven development environment on Windows without Windows Subsystem for Linux`

-----

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>