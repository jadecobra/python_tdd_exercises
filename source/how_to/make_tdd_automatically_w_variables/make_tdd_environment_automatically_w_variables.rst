:orphan:

.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watch for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

##############################################################################################
how to make a Python Test Driven Development environment automatically w/ variables
##############################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

********************************************************************************************
how to use a variable in a shell script
********************************************************************************************

``makePythonTdd.sh`` works and always makes a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` the way I want it, but there is a problem

I change the name of the project in 5 places every time I use the program to make a project. I want the program_ to take a project name once and use that name when making the project to make the following

- the project folder_
- the file_ for the program_ in the ``src`` folder_
- the file_ for the test in the ``tests`` folder_
- the :ref:`test class<what is a class?>` in the test file_
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

Time to use a :ref:`variable<what is a variable?>` for the name of the project

* I open ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` in the :ref:`editor<2 editors>`

  .. TIP:: Here is a quick way to open ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` if you are using `Visual Studio Code`_

    .. code-block:: python
      :emphasize-lines: 1

      code makePythonTdd.sh

* I add a name to represent any project name that I give to ``makePythonTdd.sh`` when I want it to make a project

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 2

    #!/bin/bash
    PROJECT_NAME="dictionaries"
    mkdir dictionaries
    cd dictionaries
    mkdir src
    touch src/dictionaries.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestDictionaries(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError
    " > tests/test_dictionaries.py

  a :ref:`variable<test_attribute_error_w_variables>` is a name that is used for a value that can change. For example, we use the word

  * ``woman`` to represent any woman
  * ``man`` to represent any man
  * ``child`` to represent any child
  * ``parent`` to represent anyone with a child.

  In this case I use ``$PROJECT_NAME`` to represent any name of a project

* I change every where I have ``dictionaries`` in the program_, to use the :ref:`variable<test_attribute_error_w_variables>` I just added so that I only have to make a change in one place

  .. NOTE:: The lines that are changing in the code are highlighted

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 3-4, 6, 13, 21

    #!/bin/bash
    PROJECT_NAME="dictionaries"
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


    # Exceptions seen
    # AssertionError
    " > tests/test_$PROJECT_NAME.py

* I change the name of the project to 

* I run the program_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2, 4, 10, 12

    ======================================= FAILURES =======================================
    ____________________________ Testdictionaries.test_failure ______________________________

    self = <tests.test_magic_again.Testdictionaries testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_dictionaries.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_dictionaries.py::Testdictionaries::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in ``tests/test_dictionaries.py`` to make the test pass

* I hit :kbd:`ctrl+c` in the terminal_ to stop the test

* I run tree_ to see what I have in the ``pumping_python`` folder_ now

  .. code-block:: shell
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 8-13

    .
    ├── magic_again
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    ├── dictionaries
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

* I change ``dictionaries`` to ``$1`` in ``makePythonTdd.sh``

  .. code-block:: shell
    :lineno-start: 2
    :emphasize-lines: 1

    PROJECT_NAME=$1

* I try the program_ again, this time with a different name for the project in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh dictionaries_again

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 10

    ======================================= FAILURES =======================================
    _____________________________ Testdictionaries_again.test_failure ______________________________

    self = <tests.test_dictionaries_again.Testdictionaries_again testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_dictionaries_again.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_dictionaries_again.py::Testdictionaries_again::test_failure - AssertionError: True is not false
    ================================== 1 failed in 0.04s ===================================

* I hold :kbd:`ctrl` on the keyboard in the terminal_ and click on ``tests/test_dictionaries_again.py`` to open it in the :ref:`editor<2 editors>`, then make the test pass

* I use :kbd:`ctrl+c` on the keyboard in the terminal_ to stop the tests

* I run tree_ to see what I have in the ``pumping_python`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    tree -a -L 2

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 15-20

    .
    ├── magic_again
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    ├── dictionaries
    │   ├── .pytest_cache
    │   ├── requirements.txt
    │   ├── src
    │   ├── tests
    │   └── .venv
    ├── makePythonTdd.sh
    └── dictionaries_again
        ├── .pytest_cache
        ├── requirements.txt
        ├── src
        ├── tests
        └── .venv

* I can now make a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` with ``makePythonTdd.sh`` when I give it a name for the ``PROJECT_NAME`` variable_. For example, when I type this in the terminal_

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

  the computer makes a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for a project called :ref:`assertion_error<what causes AssertionError?>` and runs :ref:`the first failing test<test_failure>`. I continue this in :ref:`AssertionError<what causes AssertionError?>`

----

********************************************************************************************
review
********************************************************************************************

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen a way to make a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>`, and have a :ref:`program<makePythonTdd.sh>` to do it for you on any Linux_, Windows_ or MacOS_ computers.

:ref:`How many questions can you answer after going through this chapter?<questions about making a Python Test Driven Development Environment>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<makePythonTdd.sh>`

----

:ref:`Would you like to test AssertionError?<what causes AssertionError?>`

-----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please leave a 5 star review. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->