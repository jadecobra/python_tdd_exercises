.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watcher for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../../links.rst

#################################################################################
how to make a Python Test Driven Development environment automatically
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
preview
*********************************************************************************

Here is the program_ I have by the end of the chapter to :ref:`automatically make a python test driven development environment <how to make a Python Test Driven Development environment automatically>`, it is only 27 lines of code, with spaces

.. literalinclude:: ../../code/make_tdd/makePythonTddNoVariables.sh
  :language: shell
  :linenos:

*********************************************************************************
questions about making a Python Test Driven Development Environment automatically
*********************************************************************************

Here are questions you can answer after going through this chapter


* :ref:`how can I make a shell script?<how to make a shell script>`
* :ref:`how can I view the permissions of a file?<how to view the permissions of a file>`
* :ref:`how can I make a shell script run as a command<how to make a shell script run as a command>`
* :ref:`how can I run a shell script<how to run a shell script>`

----

*********************************************************************************
how to make a shell script
*********************************************************************************

* I go to the terminal_ and use touch_ to make an empty file_ with a name that is easy to remember later. I want the name to also describe the program_ that will automatically make a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for me

  .. code-block:: shell
    :emphasize-lines: 1

    touch makePythonTdd.sh

  the terminal_ goes back to the command line

* I name this project ``magic_again``

* I open ``makePythonTdd.sh`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ with the name of the program and the name of the file_. That means if I type this in the terminal_

    .. code-block:: shell
      :emphasize-lines: 1

      code makePythonTdd.sh

    `Visual Studio Code`_ opens ``makePythonTdd.sh`` in the :ref:`editor<2 editors>`


* I add the commands I use to make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>` for a project in ``makePythonTdd.sh``

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
    echo "pytest" > requirements.txt
    echo "pytest-watcher" >> requirements.txt
    uv init
    rm main.py
    uv add --requirement requirements.txt
    uv run pytest-watcher . --now

  ``#!/bin/bash`` is called a shebang_ line, it tells the computer to use bash_ to run this program_

* ``test_magic_again.py`` is empty because I made it with touch_. I want the file_ to have the text for :ref:`the first failing test<test_failure>` so I do not have to open the :ref:`editor<2 editors>` to add the text for it in each project.

  I use echo_ in place of touch_ to make the ``makePythonTdd.sh`` program_ add the text to ``test_magic_again.py`` when it makes the file_ in the ``tests`` folder_, the same way I use echo_ to add text to the ``requirements.txt`` file_

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 8
    :emphasize-text: magic_again

    #!/bin/bash
    mkdir magic_again
    cd magic_again
    mkdir src
    touch src/magic_again.py
    mkdir tests
    touch tests/__init__.py
    echo "" > tests/test_magic_again.py
    echo "pytest" > requirements.txt
    echo "pytest-watcher" >> requirements.txt
    uv init
    rm main.py
    uv add --requirement requirements.txt
    uv run pytest-watcher . --now

* I add the text for the :ref:`the first failing test<test_failure>` inside the :ref:`quotes ("")<quotes>` I just added to ``makePythonTdd.sh``, the way I do with echo_ when I add ``"pytest"`` as text in ``requirements.txt``

  .. ATTENTION:: Indentation_ is important in Python_, I use 4 spaces as convention in this book, see the :PEP:`Python Style Guide <8>` for more

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 9-20

    #!/bin/bash
    mkdir magic_again
    cd magic_again
    mkdir src
    touch src/magic_again.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestMagicAgain(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError
    " > tests/test_magic_again.py

    echo "pytest" > requirements.txt
    echo "pytest-watcher" >> requirements.txt
    uv init
    rm main.py
    uv add --requirement requirements.txt
    uv run pytest-watcher . --now

----

*********************************************************************************
how to run a shell script
*********************************************************************************

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

I have to make the file executable for the computer to be be able to run the program_.

----

*********************************************************************************
how to view the permissions of a file
*********************************************************************************

I use ls_ to check the permissions of the file_

.. code-block:: shell
  :emphasize-lines: 1

  ls -l makePythonTdd.sh

``-l`` is the option to show the long listing format which includes permissions for the file_

the terminal_ shows

.. code-block:: shell

  -rw-r--r-- 1 abcdef ghijk XX Month  Y ZA:BC makePythonTdd.sh

.. NOTE:: the first 10 characters above (``-rw-r--r--``) are grouped

  .. code-block:: shell

    -    rw-    r--    r--

  the groups that have 3 characters show ``read``, ``write`` and ``execute`` permissions with

  - ``r`` for can ``read``
  - ``w`` for can ``write`` to, and
  - ``x`` for can ``execute``
  - ``-`` for CANNOT

  here is what it means for ``makePythonTdd.sh``

  * the first group with just 1 character tells if this is a file_ or directory_ : ``-`` means this is a file_, it is NOT a directory_
  * the second group has 3 characters, and is for the owner of the file_: ``rw-`` means the owner of the file_ can read (``r``), write to (``w``), and CANNOT (``-``) execute the file_
  * the next group also has 3 characters, and is for the group of the owner of the file_: ``r--`` means the group can read (``r``), CANNOT (``-``) write to, and CANNOT (``-``) execute the file_
  * the last group has 3 characters and is for other users: ``r--`` means other users can read (``r``), CANNOT (``-``) write to, and CANNOT (``-``) execute the file_

I want to add execute permissions so I can run (execute) the file_

----

*********************************************************************************
how to make a shell script run as a command
*********************************************************************************

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

  .. NOTE::

    * ``-`` means this is a file_, it is NOT a directory_
    * ``rwx`` means the owner of the file_ can read (``r``), write to (``w``) and execute (``x``) the file_
    * ``r-x`` means the group of the owner of the file_ can read (``r``), CANNOT (``-``) write to, and can execute (``x``) the file_
    * and the second ``r-x`` means other users can read (``r``), CANNOT (``-``) write to, and can execute (``x``) the file_

* I try the command again

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 10

    ============================== FAILURES ===============================
    ____________________ TestMagicAgain.test_failure ______________________

    self = <tests.test_magic_again.TestMagicAgain testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic_again.py:7: AssertionError
    ====================== short test summary info ========================
    FAILED tests/test_magic_again.py::TestMagicAgain::test_failure - AssertionError: True is not false
    ========================= 1 failed in X.YZs ===========================

  Success! I just made a program_ that can make the ``magic_again`` project anytime I want and it automatically does the steps I used to do.

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_magic_again.py`` to open it in the :ref:`editor<2 editors>` then make the test pass

* I click in the terminal_ and use :kbd:`q` on the keyboard to leave the tests, the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

* I close ``test_magic_again`` in the :ref:`editor<2 editors>`

----

*********************************************************************************
how to use makePythonTdd.sh to make a different project
*********************************************************************************

* I want to use ``makePythonTdd.sh`` to make another project with a different name. I change ``magic_again`` to the name of the new project in the :ref:`editor<2 editors>`

  .. NOTE:: The lines that are changing in the code are highlighted

  .. code-block::
    :linenos:
    :emphasize-lines: 2, 3, 5, 12, 20
    :emphasize-text: more_magic MoreMagic

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


    # Exceptions seen
    # AssertionError
    " > tests/test_more_magic.py

    echo "pytest" > requirements.txt
    echo "pytest-watcher" >> requirements.txt
    uv init
    rm main.py
    uv add --requirement requirements.txt
    uv run pytest-watcher . --now

* I run ``makePythonTdd.sh`` in the terminal_ to make a project named ``more_magic``

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 10

    ============================== FAILURES ===============================
    _____________________ TestMoreMagic.test_failure ______________________

    self = <tests.test_more_magic.TestMoreMagic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_more_magic.py:7: AssertionError
    ====================== short test summary info ========================
    FAILED tests/test_more_magic.py::TestMoreMagic::test_failure - AssertionError: True is not false
    ========================== 1 failed in X.YZs ==========================

  I make the test pass

* I click in the terminal_ and use :kbd:`q` on the keyboard to leave the tests, the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

* I close ``test_more_magic.py`` in the :ref:`editor<2 editors>`

:ref:`makePythonTdd.sh` works and can automatically make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>` the way I want every time. What a beautiful life.

----

********************************************************************************************
review
********************************************************************************************

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen a way I can make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>`, with a :ref:`program<makePythonTdd.sh>` to do it on any Linux_, Windows_ or MacOS_ computers.

:ref:`How many questions can you answer after going through this chapter?<questions about making a Python Test Driven Development Environment>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<makePythonTdd.sh with no variables>`

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
* :ref:`how to make a Python Test Driven Development environment automatically`

:ref:`Would you like to use makePythonTdd.sh to make a Python Test Driven Development environment to test that an Exception is raised?<how to test that an Exception is raised>`

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