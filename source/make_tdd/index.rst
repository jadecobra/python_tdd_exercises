.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watcher for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../links.rst

#################################################################################
how to make a Python test driven development environment
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

*********************************************************************************
what is Test Driven Development (TDD)?
*********************************************************************************

`Test Driven Development`_ is a way to write software with a focus on tests. I write tests for ideas to reach a goal or meet a requirement, and the results tell me if I am closer to the goal or not. I repeat the process until I get to the goal.

----

*********************************************************************************
what is a Test Driven Development Environment?
*********************************************************************************


A :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` is a group of files_ and folders_ in a project where I can write tests and code and they automatically run so I see the results quickly.

----

*********************************************************************************
what is the Test Driven Development cycle?
*********************************************************************************


The `Test Driven Development`_ cycle is :red:`RED` :green:`GREEN` :yellow:`REFACTOR`

* :red:`RED`: make it :red:`fail` - I write a test that :red:`fails` to make sure the test works
* :green:`GREEN`: make it :green:`pass` - I write the simplest thing that will make the failing test :green:`pass`
* :yellow:`REFACTOR`: make it :yellow:`better` - I write a :yellow:`better` solution, test or both, usually by `removing duplication`_

This process can be repeated as many times as needed until I get to my goal.

----

*********************************************************************************
preview
*********************************************************************************

I set up an environment for every Python_ project, this way I keep all the things that belong to the project in the same place.

I can do this manually, which means I have to do the same steps for every project or I could do it automatically where I give the computer a command and it does all the steps for me.

Some things I think about when I want to start a project

* What name will I give the project? this is based on what the project will do. Naming things is its own challenge
* What is the structure of the project?
  - What files_ and folders_ does the project need?

* What other programs_ does my project need?
* What tests am I going to write for this project?

It turns out some of this is the same for every project

* I give the project a name
* I make a new folder_ for the project with the name I gave it
* I try to name everything in the project with the name of the project or with something that describes what it does
* I place the code for the project in a ``src`` folder_
* I place the tests for the project in a ``tests`` folder_
* I write what programs the project needs (its dependencies) in a requirements file_
* I make a `virtual environment`_ to keep the dependencies separate from the rest of the computer
* I install what the project needs in the `virtual environment`_
* I work in the `virtual environment`_
* I run automated tests to make sure I have a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>`
* I start writing code for the project

Here is what that structure looks like if the name of the project is ``PROJECT_NAME``

.. code-block:: shell

  PROJECT_NAME
  ├── .virtual_environment
  ├── requirements_file
  ├── src
  │   └── PROJECT_NAME.py
  └── tests
      └── test_PROJECT_NAME.py

----

*********************************************************************************
what is covered?
*********************************************************************************

This is one way to make a :ref:`Python Test Driven Development project<what is a Test Driven Development Environment?>`. I walk through making the `folders (directories)`_ and files_ for the environment, including setting up :ref:`the first test<test_failure>`.

.. toctree::
  :titlesonly:

  make TDD manually<make_tdd_manually>
  make TDD automatically<make_tdd_automatically>
  make TDD automatically with variables<make_tdd_automatically_w_variables/index>


*************************************************************************************
what is next?
*************************************************************************************

I made a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for a project called ``magic`` on any Linux_, MacOS_ and Windows_computers. :ref:`Would you like to test AssertionError next?<what causes AssertionError?>`

-----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->