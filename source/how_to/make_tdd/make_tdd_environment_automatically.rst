.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watch for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

#################################################################################
how to make a Python Test Driven Development environment automatically
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

You made it this far and have become `the greatest programmer in the world`_. To follow `The Do Not Repeat Yourself (DRY) Principle`_, I write a program_ with the commands to make  a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` anytime I want so I do not have to remember every step of the process or do them manually.

To review, here are steps I take to make the environment for every project

#. I pick a name for the project
#. :ref:`I make a directory for the project<how to make a directory for the project>`
#. :ref:`I change directory to the project<how to change directory to the project>`
#. :ref:`I make a directory for the source code<how to make a directory for the source code>`
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

I want to give one command for the program to do every step except

* pick the name for the project
* make the test pass and
* work on the project, though I can now use an `Artificial Intelligence Large Language Model`_ to help with this

this way I only need to do 3 steps instead of 18

*********************************************************************************
preview
*********************************************************************************

Here is the program_ I have by the end of the chapter to :ref:`automatically make a python test driven development environment <how to make a Python Test Driven Development environment automatically>`, it is only 28 lines of code, with spaces

.. literalinclude:: ../../code/make_tdd/makePythonTdd.sh
  :language: shell
  :linenos:

*********************************************************************************
questions about making a Python Test Driven Development Environment automatically
*********************************************************************************

Here are questions you can answer after going through this chapter


* :ref:`How can I make a shell script?<how to make a shell script>`
* :ref:`How can I view the permissions of a file?<how to view the permissions of a file>`
* :ref:`How can I make a shell script run as a command<how to make a shell script run as a command>`
* :ref:`How can I run a shell script<how to run a shell script>`

----

*********************************************************************************
how to make a shell script
*********************************************************************************

* I go to the terminal_ and use touch_ to make an empty file_ with a name that is easy to remember later. I want the name to also describe the program_ that will automatically make a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for me

  .. code-block:: shell
    :emphasize-lines: 1

    touch makePythonTdd.sh

  the terminal_ goes back to the command line

* I open ``makePythonTdd.sh`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_, then add the commands I use to make a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for a project

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 1-

    #!/bin/bash
    mkdir magic_again
    cd magic_again
    mkdir src
    touch src/magic_again.py
    mkdir tests
    touch tests/__init__.py
    touch tests/test_magic_again.py
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    echo "pytest-watch" > requirements.txt
    python3 -m pip install --requirement requirements.txt
    pytest-watch

  ``#!/bin/bash`` is called a shebang_ line, it tells the computer to use bash_ to run this program_

* ``test_magic_again.py`` is an empty file_ because I used touch_. I want it to have the text for :ref:`the first failure<test_failure>` so I do not have to open the :ref:`editor<2 editors>` to add the text for it in each project. I use echo_ instead of touch_ to make the ``makePythonTdd.sh`` program_ add the text to ``test_magic_again.py`` when it makes the file_ in the ``tests`` folder_, the same I do with the ``requirements.txt`` file_

  .. code-block:: shell
    :lineno-start: 6
    :emphasize-lines: 4

    mkdir tests
    touch tests/__init__.py

    echo "" > tests/test_magic_again.py

    python3 -m venv .venv
    source .venv/bin/activate

* I add the text for the test inside the :ref:`quotes ("")<quotes>` I just added to ``makePythonTdd.sh``, the way I do with echo_ when I add ``"pytest-watch"`` as text in ``requirements.txt``

  .. CAUTION:: Indentation_ is important in Python_, I use 4 spaces as convention in this book, see the :PEP:`Python Style Guide <8>` for more

  .. code-block:: shell
    :lineno-start: 9
    :emphasize-lines: 1-12

    echo "import unittest


    class TestMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " > tests/test_magic_again.py

--------------------------------------------------------------------------------------------
how to run a shell script
--------------------------------------------------------------------------------------------

I go back to the terminal_ to run the program_

.. code-block:: shell
  :emphasize-lines: 1

  makePythonTdd.sh

the terminal_ shows

.. code-block:: shell

  command not found: makePythonTdd.sh

I have to tell the computer where the file_ is

.. code-block:: shell
  :emphasize-lines: 1

  ./makePythonTdd.sh

``./`` is shorthand for ``this directory`` which in this case is ``pumping_python`` where ``makePythonTdd.sh`` is saved. The computer checks a few directories_ when a command is given. Those directories are where commands like mkdir_, cd_, tree_ and echo_ are saved. The terminal_ shows

.. code-block:: shell

  permission denied: ./makePythonTdd.sh

I want to make sure the computer can run the program_. I have to make it executable

--------------------------------------------------------------------------------------------
how to view the permissions of a file
--------------------------------------------------------------------------------------------

I use ls_ to check the permissions of the file_

.. code-block:: shell
  :emphasize-lines: 1

  ls -l makePythonTdd.sh

``-l`` is the option to show the long listing format which includes permissions for the file_

the terminal_ shows

.. code-block:: shell

  -rw-r--r-- 1 abcdef ghijk XX Month  Y ZA:BC makePythonTdd.sh

the first 10 characters above are grouped

.. code-block:: shell

  -    rw-    r--    r--

the groups that have 3 characters show ``read``, ``write`` and ``execute`` permissions with

- ``r`` for ``read``
- ``w`` for ``write`` and
- ``x`` for ``execute``

here is what it means for ``makePythonTdd.sh``

* the first group tells if this is file_ or directory_ : ``-`` means this is a regular file_, it is not a directory_
* this group shows permissions for the owner of the thing: ``rw-`` means the owner of the file_ can read and write to the file_ but NOT execute it
* this group shows permissions for the group of the owner of the thing: ``r--`` means the group can read the file_, NOT write to it or execute it
* this group is for other users: ``r--`` means other users can read the file_, NOT write to it or execute it

I want to add execute permissions so I can run the file

--------------------------------------------------------------------------------------------
how to make a shell script run as a command
--------------------------------------------------------------------------------------------

* I change the mode of the file_ to add executable permissions

  .. code-block:: shell
    :emphasize-lines: 1

    chmod +x makePythonTdd.sh

  chmod_ is a program_ that changes the mode (permissions) of the given file_, the terminal_ goes back to the command line

* I list the permissions again with ls_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -l makePythonTdd.sh

  the terminal_ shows

  .. code-block:: shell

    -rwxr-xr-x 1 abcdef ghijk XX Month  Y ZA:BC makePythonTdd.sh

  here is what each one of the characters before the folder_ means

  * ``-`` means this is a regular file_, it is not a directory_
  * ``rwx`` means the owner of the file_ has permissions to read, write to and execute it
  * ``r-x`` means the group the owner of the file_ belongs to has permissions to read and execute the file_ they cannot write to it, and the second
  * ``r-x`` means other users have permissions to read and execute the file_, they cannot write to it

* I try the command again

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 10

    ======================================= FAILURES =======================================
    _____________________________ TestMagicAgain.test_failure ______________________________

    self = <tests.test_magic_again.TestMagicAgain testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic_again.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_magic_again.py::TestMagic::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

  Success! I just made a program_ that can make the ``magic_again`` project anytime I want and it automatically does the steps I did manually.

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_magic_again.py`` to open it in the :ref:`editor<2 editors>` then make the test pass

* I hit :kbd:`ctrl+c` in the terminal_ to stop the test

* I want to use ``makePythonTdd.sh`` to make another project with a different name. I change ``magic_again`` to the name of the new project in the :ref:`editor<2 editors>`

  .. NOTE:: The lines that are changing in the code are highlighted

  .. code-block::
    :linenos:
    :emphasize-lines: 2, 3, 5, 12, 20

    #!/bin/bash
    mkdir more_magic
    cd more_magic
    mkdir src
    touch src/more_magic.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestMoreMagic(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " > tests/test_more_magic.py

* I run ``makePythonTdd.sh`` in the terminal_ to make a project named ``more_magic``

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell
    :emphasize-lines: 10

    ======================================= FAILURES =======================================
    ______________________________ TestMoreMagic.test_failure ______________________________

    self = <tests.test_more_magic.TestMoreMagic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_more_magic.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_more_magic.py::TestMoreMagic::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

  I make the test pass

* I hit :kbd:`ctrl+c` to exit the tests in the terminal_

the program_ works and can make a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` automatically the way I want every time

----

*********************************************************************************
close the project
*********************************************************************************

* I close the ``test_more_magic.py`` in the :ref:`editor<2 editors>` I had open
* I exit the tests in the terminal_ with :kbd:`Ctrl+C` on the keyboard
* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/more_magic

* I `change directory`_ to the parent of ``more_magic``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

********************************************************************************************
review
********************************************************************************************

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen a way I can make a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>`, with a :ref:`program<makePythonTdd.sh>` to do it on any Linux_, Windows_ or MacOS_ computers.

:ref:`How many questions can you answer after going through this chapter?<questions about making a Python Test Driven Development Environment>`

----

:ref:`Click Here to see the code for the program to make a Python Test Driven Development environment for any Linux or MacOS computers<makePythonTdd.sh>`

----

*********************************************************************************
what is next?
*********************************************************************************

Here is what we have gone through together so far

* :ref:`how to make a test driven development environment`
* :ref:`how to raise AssertionError with assert methods<AssertionError>`
* :ref:`how to write functions<functions>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<None>`
* :ref:`what is True and False in Python<booleans>`
* :ref:`how to write programs that make decisions<booleans: truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to make a Python Test Driven Development environment automatically`

:ref:`Would you like to use makePythonTdd.sh to make a Python Test Driven Development environment to test that an Exception is raised?<how to test that an Exception is raised>`

-----

*********************************************************************************
please leave a review
*********************************************************************************

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 5 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->