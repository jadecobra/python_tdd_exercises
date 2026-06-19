.. meta::
  :description: Stop manually setting up Python TDD projects. Learn to automate your entire test-driven development environment with one script in just 5 minutes.
  :keywords: Jacob Itegboje, automate python tdd setup script, python test driven development workflow, how to structure a python project for testing, pytest-watcher for automatic testing, python virtual environment best practices, create python project from template, step-by-step python tdd tutorial, python project automation script

.. include:: ../links.rst

#################################################################################
how to make a Python Test Driven Development environment automatically
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/CLC1YAHHbjU?si=0agM3_IhWmUYpTln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
preview
*********************************************************************************

Here is the program_ I have by the end of the chapter to :ref:`automatically make a python test driven development environment <how to make a Python Test Driven Development environment automatically>`.

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    It is only 25 lines of code (with spaces)

    .. literalinclude:: ../code/make_tdd/makePythonTddNoVariables.sh
      :language: shell
      :linenos:

  .. tab-item:: no WSL
    :sync: no_wsl

    It is only 24 lines of code (with spaces)

    .. literalinclude:: ../code/make_tdd/makePythonTddNoVariables.ps1
      :language: Powershell
      :linenos:

*********************************************************************************
questions about making a Python Test Driven Development Environment automatically
*********************************************************************************

Questions to think about as I go through the chapter


* :ref:`how can I make a shell script?<how to make a shell script>`
* :ref:`how can I view the permissions of a file?<how to view the permissions of a file>`
* :ref:`how can I make a shell script run as a command<how to make a shell script run as a command>`
* :ref:`how can I run a shell script<how to run a shell script>`

----

*********************************************************************************
how to make a shell script
*********************************************************************************

* I go to the terminal_ and use touch_ to make an empty file_ with a name that is easy to remember later. I want the name to also describe the program_ that will automatically make a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for me

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item makePythonTdd.ps1

  the terminal_ goes back to the command line.

* I name this project ``magic_again``

* I open the file_ I just made of the `Integrated Development Environment (IDE)`_

  .. tip::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ with the name of the program_ and the name of the file_. That means if I type this in the terminal_

    .. tab-set::
      :sync-group: os

      .. tab-item:: WSL/Linux/Mac
        :sync: unix

        .. code-block:: shell
          :emphasize-lines: 1

          code makePythonTdd.sh

        `Visual Studio Code`_ opens ``makePythonTdd.sh``

      .. tab-item:: no WSL
        :sync: no_wsl

        .. code-block:: shell
          :emphasize-lines: 1

          code makePythonTdd.ps1

        `Visual Studio Code`_ opens ``makePythonTdd.ps1``

* I add the commands I use to make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>` for a project to the file_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :linenos:
        :emphasize-lines: 1-

        #!/bin/bash
        uv init magic_again
        cd magic_again
        mkdir src
        mv main.py src/magic_again.py
        mkdir tests
        touch tests/__init__.py
        touch tests/test_magic_again.py
        echo "pytest" > requirements.txt
        echo "pytest-watcher" >> requirements.txt
        uv add --requirement requirements.txt
        uv run pytest-watcher . --now

      ``#!/bin/bash`` is called a shebang_ line, it tells the computer to use bash_ to run this program_

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :linenos:
        :emphasize-lines: 1-

        uv init magic_again
        cd magic_again
        mkdir src
        mv main.py src/magic_again.py
        mkdir tests
        New-Item tests/__init__.py
        New-Item tests/test_magic_again.py
        "pytest" | requirements.txt -Encoding UTF8
        "pytest-watcher" >> requirements.txt
        uv add --requirement requirements.txt
        uv run pytest-watcher . --now

* ``test_magic_again.py`` will be empty if I make it this way. I want the file_ to have the text for :ref:`the first failing test<test_failure>` so I do not have to open the :ref:`editor<2 editors>` to add the text for it in each project.

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      I use echo_ in place of touch_ to make the ``makePythonTdd.sh`` program_ add text to ``test_magic_again.py`` when it makes the file_ in the ``tests`` folder_, the same way I use echo_ to add text to the ``requirements.txt`` file_

      .. code-block:: python
        :linenos:
        :emphasize-lines: 8
        :emphasize-text: magic_again

        #!/bin/bash
        uv init magic_again
        cd magic_again
        mkdir src
        mv main.py src/magic_again.py
        mkdir tests
        touch tests/__init__.py
        echo "" > tests/test_magic_again.py
        echo "pytest" > requirements.txt
        echo "pytest-watcher" >> requirements.txt
        uv add --requirement requirements.txt
        uv run pytest-watcher . --now

    .. tab-item:: no WSL
      :sync: no_wsl

      I use `Out-File`_ in place of `New-Item`_ to make the ``makePythonTdd.ps1`` program_ add text to ``test_magic_again.py`` when it makes the file_ in the ``tests`` folder_, the same way I use `Out-File`_ to add text to the ``requirements.txt`` file_

      .. code-block:: python
        :linenos:
        :emphasize-lines: 7
        :emphasize-text: magic_again

        uv init magic_again
        cd magic_again
        mkdir src
        Move-Item main.py src/magic_again.py
        mkdir tests
        New-Item tests/__init__.py
        "" | Out-File tests/test_magic_again.py -Encoding UTF8
        "pytest" | Out-File requirements.txt -Encoding UTF8
        "pytest-watcher" >> Out-File requirements.txt
        uv add --requirement requirements.txt
        uv run pytest-watcher . --now

* I add the text of :ref:`the first failing test<test_failure>` inside the :ref:`quotes ("")<quotes>` I just added to the files_, the way I do when I add ``"pytest"`` as text to ``requirements.txt``

  .. attention:: Indentation_ is important in Python_, I use 4 spaces as convention in this book, see the :PEP:`Python Style Guide <8>` for more

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :linenos:
        :emphasize-lines: 9-20

        #!/bin/bash
        uv init magic_again
        cd magic_again
        mkdir src
        mv main.py src/magic_again.py
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
        uv add --requirement requirements.txt
        uv run pytest-watcher . --now

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :linenos:
        :emphasize-lines: 8-19

        uv init magic_again
        cd magic_again
        mkdir src
        Move-Item main.py src/magic_again.py
        mkdir tests
        New-Item tests/__init__.py

        "import unittest


        class TestMagicAgain(unittest.TestCase):

            def test_failure(self):
                self.assertFalse(True)


        # Exceptions seen
        # AssertionError
        " | Out-File "tests/test_magic_again.py" - Encoding UTF8

        "pytest" | Out-File requirements.txt -Encoding UTF8
        "pytest-watcher" | Out-File requirements.txt -Encoding UTF8
        uv add --requirement requirements.txt
        uv run pytest-watcher . --now

----

*********************************************************************************
how to run a shell script
*********************************************************************************

I go back to the terminal_ to run the program_

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    .. code-block:: shell
      :emphasize-lines: 1

      makePythonTdd.sh

    the terminal_ is my friend, and shows

    .. code-block:: shell

      command not found: makePythonTdd.sh

    I have to tell the computer where the file_ is

    .. code-block:: shell
      :emphasize-lines: 1

      ./makePythonTdd.sh

    ``./`` is shorthand for ``this directory`` which in this case is ``pumping_python`` where ``makePythonTdd.sh`` is saved. The computer checks a few directories_ when a command is given. Those directories are where commands like mkdir_, cd_, tree_ and echo_ are saved. the terminal_ is my friend, and shows

    .. code-block:: shell

      permission denied: ./makePythonTdd.sh

    I have to make the file executable for the computer to be be able to run the program_.

  .. tab-item:: no WSL
    :sync: no_wsl

    .. code-block:: PowerShell
        :emphasize-lines: 1

        makePythonTdd.ps1

    the terminal_ is my friend, and shows

    .. code-block:: PowerShell

      command not found: makePythonTdd.ps1

    I have to tell the computer where the file_ is

    .. code-block:: PowerShell
      :emphasize-lines: 1

      .\makePythonTdd.ps1

    ``.\`` is shorthand for ``this directory`` which in this case is ``pumping_python`` where ``makePythonTdd.ps1`` is saved. the terminal_ is my friend, and shows

    .. code-block:: PowerShell
      :emphasize-lines: 10

      ========================= FAILURES =========================
      ___________________ TestMagicAgain.test_failure ____________________

      self = <tests.test_magic_again.TestMagicAgain testMethod=test_failure>

          def test_failure(self):
      >       self.assertFalse(True)
      E       AssertionError: True is not false

      tests/test_magic_again.py:7: AssertionError
      ================ short test summary info ===================
      FAILED tests/test_magic_again.py::TestMagicAgain::test_failure - AssertionError: True is not false
      ==================== 1 failed in X.YZs =====================

    Success! I just made a program_ that can make the ``magic_again`` project anytime I want and it automatically does the steps I did manually.

    :ref:`Click Here to skip to How to use makePythonTdd.ps1 to make a different project<how to use makePythonTdd to make a different project>`


----

*********************************************************************************
how to view the permissions of a file
*********************************************************************************

.. attention::

  This part is only for Computers with MacOS_, Linux_ or `Windows Subsystem for Linux`_. If you have Windows_ without `Windows Subsystem for Linux`_ :ref:`Click Here to skip to How to use makePythonTdd.ps1 to make a different project<how to use makePythonTdd to make a different project>`

I use ls_ to check the permissions of the file_

.. code-block:: shell
  :emphasize-lines: 1

  ls -l makePythonTdd.sh

``-l`` is the option to show the long listing format which includes permissions for the file_

the terminal_ is my friend, and shows

.. code-block:: shell

  -rw-r--r-- 1 abcdef ghijk XX Month  Y ZA:BC makePythonTdd.sh

.. note:: the first 10 characters above (``-rw-r--r--``) are grouped

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

  chmod_ is a program_ that changes the mode (permissions) of the given file_, the terminal_ goes back to the command line.

* I list the permissions again with ls_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -l makePythonTdd.sh

  the terminal_ is my friend, and shows

  .. code-block:: shell

    -rwxr-xr-x 1 abcdef ghijk XX Month  Y ZA:BC makePythonTdd.sh

  .. note::

    * ``-`` means this is a file_, it is NOT a directory_
    * ``rwx`` means the owner of the file_ can read (``r``), write to (``w``) and execute (``x``) the file_
    * ``r-x`` means the group of the owner of the file_ can read (``r``), CANNOT (``-``) write to, and can execute (``x``) the file_
    * and the second ``r-x`` means other users can read (``r``), CANNOT (``-``) write to, and can execute (``x``) the file_

* I try the command again

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  the terminal_ is my friend, and shows

  .. code-block:: shell
    :emphasize-lines: 10

    ========================== FAILURES ===========================
    ____________________ TestMagicAgain.test_failure ______________________

    self = <tests.test_magic_again.TestMagicAgain testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic_again.py:7: AssertionError
    ================== short test summary info ====================
    FAILED tests/test_magic_again.py::TestMagicAgain::test_failure - AssertionError: True is not false
    ===================== 1 failed in X.YZs =======================

  Success! I just made a program_ that can make the ``magic_again`` project anytime I want and it automatically does the steps I used to do.


----

*********************************************************************************
how to use makePythonTdd to make a different project
*********************************************************************************

* I hold :kbd:`ctrl` on the keyboard, and click on ``tests/test_magic_again.py`` to open it then make the test pass

* I close ``test_magic_again.py``

* I click in the terminal_, and use :kbd:`q` on the keyboard to leave the tests, the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

* I want to use ``makePythonTdd`` to make another project with a different name. I change ``magic_again`` to the name of the new project

  .. note:: The lines that are changing in the code are highlighted

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. literalinclude:: ../code/make_tdd/makePythonTddNoVariables.sh
        :language: python
        :linenos:
        :emphasize-lines: 2-3, 5, 12, 20

      * I run ``makePythonTdd.sh`` in the terminal_ to make a project named ``more_magic``

        .. code-block:: python
          :emphasize-lines: 1

          ./makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      .. literalinclude:: ../code/make_tdd/makePythonTddNoVariables.ps1
        :language: Powershell
        :linenos:
        :emphasize-lines: 1-2, 4, 11, 19

      * I run ``makePythonTdd.ps1`` in the terminal_ to make a project named ``more_magic``

        .. code-block:: python
          :emphasize-lines: 1

          ./makePythonTdd.ps1

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 10

    ======================== FAILURES =========================
    _______________ TestMoreMagic.test_failure ________________

    self = <tests.test_more_magic.TestMoreMagic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_more_magic.py:7: AssertionError
    ================ short test summary info ==================
    FAILED tests/test_more_magic.py::TestMoreMagic::test_failure - AssertionError: True is not false
    ==================== 1 failed in X.YZs ====================

  I make the test pass

* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests, the terminal_ is my friend, and shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

* I close ``test_more_magic.py``

The program_ works and can automatically make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>` the way I want every time. What a beautiful life.

----

********************************************************************************************
review
********************************************************************************************

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen one way I can make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>`, with a :ref:`program<makePythonTdd>` to do it on any Linux_, Windows_ or MacOS_ computers.

:ref:`How many questions can you answer after going through this chapter?<questions about making a Python Test Driven Development Environment>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<makePythonTdd with no variables>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have gone through a few things

:ref:`how to make a Python test driven development environment manually`
* :ref:`what causes AssertionError?`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<telephone>`
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

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->