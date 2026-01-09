.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watch for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

#################################################################################
how to make a test driven development environment
#################################################################################

*********************************************************************************
what is Test Driven Development (TDD)?
*********************************************************************************

This is a way to write software with a focus on tests. I write tests for ideas to reach a goal or meet a requirement, and the results tell me if I am closer to the goal or not. I repeat the process until I get to the goal.

*********************************************************************************
what is a Test Driven Development Environment?
*********************************************************************************

A :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` is a group of files_ and folders_ in a project where I can write tests and code and they automatically run so I see the results immediately.

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
what is covered?
*********************************************************************************

These chapters show how I setup a project in Python_ on any computer (Linux_, Windows_, MacOS_) to help you get started with `Test Driven Development`_ right now

.. toctree::
  :titlesonly:

  install_wsl
  make_tdd_manually
  make_tdd_environment_no_wsl
  make_tdd_automatically/index
  make_tdd_environment_no_wsl_automatically

they cover the following

* :ref:`Windows requirements`
* :ref:`Linux/Windows Subsystem for Linux requirements`

at the end of the chapters you will know how to make a :ref:`Python Test Driven Development project<what is a Test Driven Development Environment?>` for MacOS_, Linux_, `Windows Subsystem for Linux`_ or Windows_ without `Windows Subsystem for Linux`_

----

*********************************************************************************
what is next?
*********************************************************************************

* if you have a Windows_ computer :ref:`install Windows Subsystem for Linux<how to install Windows Subsystem for Linux on Windows>` then go to :ref:`how to make a python test driven development environment manually`
* if you have MacOS_, Linux_ or successfully :ref:`installed Windows Subsystem for Linux<how to install Windows Subsystem for Linux on Windows>` you can move on to :ref:`how to make a python test driven development environment manually` or
* if you are not able to install `Windows Subsystem for Linux`_ there is something for you in :ref:`how to make a python test driven development environment manually`

-----

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>