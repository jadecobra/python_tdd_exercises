.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watcher for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

#################################################################################
how to make a test driven development environment 3
#################################################################################

Since I am the greatest programmer in the world, I should not be doing as much repetition as I have done so far. I have to make it better

*********************************************************************************
review
*********************************************************************************

To review, here are steps I take to automate making the environment for every project

on a computer with MacOS_, Linux_ or `Windows`_ with `Windows Subsystem for Linux`_

#. I give the project a name
#. I open ``makePythonTdd.sh`` or ``makePythonTdd.ps1``
#. I change the name of the project to the new project name
#. I open the test file_ in the editor from the terminal_
#. I make the test pass
#. I start working on the project

I want to give one command for the program_ with the name of the project and have it do all the steps for me except

* give the project a name
* make the test pass and
* work on the project

this way I only need to do 2 or 3 steps instead of 6

As a reminder here is what the structure looks like if the name of the project is ``PROJECT_NAME``

.. code-block:: shell

  PROJECT_NAME
  ├── requirements.txt
  ├── src
  │   └── PROJECT_NAME.py
  ├── tests
  │   ├── __init__.py
  │   └── test_PROJECT_NAME.py
  └── .venv

----

*********************************************************************************
what is covered?
*********************************************************************************

These chapters show how I add a variable to a program_ so it makes a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` automatically on any computer (Linux_, Windows_, MacOS_) when I give it a name

.. toctree::
  :titlesonly:

  make TDD with name<make_tdd_environment_automatically_w_variables>
  make TDD no WSL with name<make_tdd_environment_no_wsl_automatically_w_variables>

they cover the following

----

=================================================================================
on Linux, MacOS and Windows with Window Subsystem for Linux computers
=================================================================================

----

* :ref:`how to use a variable in a shell script`
* :ref:`how to call a shell script with arguments`

----

=================================================================================
On Windows computers without Windows Subsystem for Linux
=================================================================================

----

* :ref:`how to use a variable in a PowerShell script`
* :ref:`how to call a PowerShell script with arguments`

----

at the end of the chapter you will know how to automatically make a :ref:`Python Test Driven Development project<what is a Test Driven Development Environment?>` for MacOS_, Linux_, `Windows Subsystem for Linux`_ and Windows_ without `Windows Subsystem for Linux`_ from the terminal_

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`how to make a Python Test Driven Development environment automatically with variables` or
* :ref:`how to make a python test driven development environment on Windows without Windows Subsystem for Linux with variables`

-----

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>