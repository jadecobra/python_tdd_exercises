.. meta::
  :description: Automate a Python TDD project setup with one shell script. Jacob Itegboje builds makePythonTdd.sh and makePythonTdd.ps1 from the manual uv init steps (src, tests package, first unittest AssertionError with assertFalse(True), requirements.txt with pytest and pytest-watcher). Covers shebang, touch/New-Item, echo/Out-File for the first failing test, ./ vs .\ run paths, permission denied and chmod +x on WSL/Linux/Mac, then rename magic to more_magic and re-run. Pumping Python automatic TDD environment chapter.
  :keywords: Jacob Itegboje, Pumping Python, makePythonTdd.sh, makePythonTdd.ps1, automate python tdd setup, shell script shebang, chmod +x executable, permission denied shell script, PowerShell Out-File UTF8, uv init project, pytest-watcher --now, assertFalse True AssertionError, TestMagic test_failure, more_magic project rename, make Python Test Driven Development environment automatically

.. include:: ../links.rst

#################################################################################
how to make a Python Test Driven Development environment automatically
#################################################################################

So far I do the same steps to make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>` then :ref:`run the tests automatically<how to run tests automatically>`

- give the project a name
- :ref:`make a directory for the project<how to setup a project with uv>`
- :ref:`change directory to the project<how to change directory to the project>`
- :ref:`make a directory for the source code<how to make a directory for the source code>`
- :ref:`make a Python file to hold the source code in the 'src' folder<how to make a35n empty file>`
- :ref:`make a directory for the tests<how to make a directory for the tests>`
- :ref:`make the 'tests' directory a Python package<how to make the tests a Python package>`
- :ref:`make a Python file for the tests in the 'tests' directory<how to make a Python file for the tests in the 'tests' directory>`
- :ref:`add the first failing test to the test file<test_failure>`
- :ref:`make a requirements file for the Python packages I need<how to write text to a file>`
- :ref:`install the Python packages I gave in the requirements file<how to install Python packages with uv>`
- add the files_ and folders_ to git_ for tracking
- :ref:`run the tests automatically<how to run tests automatically with uv and pytest-watcher>`
- :ref:`open the test file in the editor from the terminal<how to open the test file in the editor from the terminal>`
- make the test pass

with these commands

.. code-block:: python
  :emphasize-text: NAME_OF_THE_PROJECT

  uv init NAME_OF_THE_PROJECT
  cd NAME_OF_THE_PROJECT
  mkdir src
  mkdir tests
  touch tests/__init__.py
  mv main.py tests/test_NAME_OF_THE_PROJECT.py
  echo "pytest" > requirements.txt
  echo "pytest-watcher" >> requirements.txt
  uv add --requirement requirements.txt
  uv run pytest-watcher . --now

where ``NAME_OF_THE_PROJECT`` is the name I give the project.

I want to automate those steps so that I can give the computer one command and it will do all the steps for me.



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

I make a new file_ with a name that describes automatically making a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` and is easy to remember later.

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    * I use touch_ to make ``makePythonTdd.sh``

      .. code-block:: python
        :emphasize-lines: 1

        touch makePythonTdd.sh

    * I open ``makePythonTdd.sh``

  .. tab-item:: no WSL
    :sync: no_wsl

    * I use New-Item_ to make ``makePythonTdd.ps1``

      .. code-block:: python
        :emphasize-lines: 1

        New-Item makePythonTdd.ps1

    * I open ``makePythonTdd.ps1``

* I name this project ``magic``

* I add the commands I use to make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>` for a project to the file_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :linenos:
        :emphasize-lines: 1-

        #!/bin/bash
        uv init magic
        cd magic
        mkdir src
        mv main.py src/magic.py
        mkdir tests
        touch tests/__init__.py
        touch tests/test_magic.py
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

        uv init magic
        cd magic
        mkdir src
        Move-Item main.py src/magic.py
        mkdir tests
        New-Item tests/__init__.py
        New-Item tests/test_magic.py
        "pytest" | Out-File requirements.txt -Encoding UTF8
        "pytest-watcher" >> requirements.txt
        uv add --requirement requirements.txt
        uv run pytest-watcher . --now

* ``test_magic.py`` will be empty if I run these commands. I want the file_ to have the text for :ref:`the first failing test<test_failure>` so I do not have to add the text for it every time I start a project.

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      I use echo_ in place of touch_ to make the ``makePythonTdd.sh`` program_ add text to ``test_magic.py`` when it makes the file_ in the ``tests`` folder_, the same way I use echo_ to add text to the ``requirements.txt`` file_

      .. code-block:: python
        :linenos:
        :emphasize-lines: 8
        :emphasize-text: magic

        #!/bin/bash
        uv init magic
        cd magic
        mkdir src
        mv main.py src/magic.py
        mkdir tests
        touch tests/__init__.py
        echo "" > tests/test_magic.py
        echo "pytest" > requirements.txt
        echo "pytest-watcher" >> requirements.txt
        uv add --requirement requirements.txt
        uv run pytest-watcher . --now

    .. tab-item:: no WSL
      :sync: no_wsl

      I use `Out-File`_ in place of `New-Item`_ to make the ``makePythonTdd.ps1`` program_ add text to ``test_magic.py`` when it makes the file_ in the ``tests`` folder_, the same way I use `Out-File`_ to add text to the ``requirements.txt`` file_

      .. code-block:: python
        :linenos:
        :emphasize-lines: 7
        :emphasize-text: magic

        uv init magic
        cd magic
        mkdir src
        Move-Item main.py src/magic.py
        mkdir tests
        New-Item tests/__init__.py
        "" | Out-File tests/test_magic.py -Encoding UTF8
        "pytest" | Out-File requirements.txt -Encoding UTF8
        "pytest-watcher" >> requirements.txt
        uv add --requirement requirements.txt
        uv run pytest-watcher . --now

* I add the text of :ref:`the first failing test<test_failure>` inside the :ref:`quotes ("")<quotes>` I just added to the file_, the way I do when I add ``"pytest"`` as text to ``requirements.txt``

  .. attention:: Indentation_ is important in Python_, I use 4 spaces as convention in this book, see the :PEP:`Python Style Guide <8>` for more

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :linenos:
        :emphasize-lines: 9-20

        #!/bin/bash
        uv init magic
        cd magic
        mkdir src
        mv main.py src/magic.py
        mkdir tests
        touch tests/__init__.py

        echo "import unittest


        class TestMagic(unittest.TestCase):

            def test_failure(self):
                self.assertFalse(True)


        # Exceptions seen
        # AssertionError
        " > tests/test_magic.py

        echo "pytest" > requirements.txt
        echo "pytest-watcher" >> requirements.txt
        uv add --requirement requirements.txt
        uv run pytest-watcher . --now

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :linenos:
        :emphasize-lines: 8-19

        uv init magic
        cd magic
        mkdir src
        Move-Item main.py src/magic.py
        mkdir tests
        New-Item tests/__init__.py

        "import unittest


        class TestMagic(unittest.TestCase):

            def test_failure(self):
                self.assertFalse(True)


        # Exceptions seen
        # AssertionError
        " | Out-File "tests/test_magic.py" -Encoding UTF8

        "pytest" | Out-File requirements.txt -Encoding UTF8
        "pytest-watcher" >> requirements.txt
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

    .. code-block:: python
      :emphasize-lines: 1

      makePythonTdd.sh

    the terminal_ is my friend, and shows

    .. code-block:: python

      command not found: makePythonTdd.sh

    I have to tell the computer where the file_ is

    .. code-block:: python
      :emphasize-lines: 1

      ./makePythonTdd.sh

    ``./`` is shorthand for ``this directory`` which in this case is ``pumping_python`` where ``makePythonTdd.sh`` is saved.

    The computer checks a few directories_ when a command is given. Those directories are where commands like mkdir_, cd_, tree_ and echo_ are saved.

    The terminal_ is my friend, and shows

    .. code-block:: python

      permission denied: ./makePythonTdd.sh

    I have to make the ``makePythonTdd.sh`` executable for the computer to be able to run the program_.

  .. tab-item:: no WSL
    :sync: no_wsl

    .. code-block:: python
        :emphasize-lines: 1

        makePythonTdd.ps1

    the terminal_ is my friend, and shows

    .. code-block:: python

      command not found: makePythonTdd.ps1

    I have to tell the computer where the file_ is

    .. code-block:: python
      :emphasize-lines: 1

      .\makePythonTdd.ps1

    ``.\`` is shorthand for ``this directory`` which in this case is ``pumping_python`` where ``makePythonTdd.ps1`` is saved. the terminal_ is my friend, and shows

    .. code-block:: python
      :emphasize-lines: 10

      ========================= FAILURES =========================
      _________________ TestMagic.test_failure ___________________

      self = <tests.test_magic.TestMagic testMethod=test_failure>

          def test_failure(self):
      >       self.assertFalse(True)
      E       AssertionError: True is not false

      tests/test_magic.py:7: AssertionError
      ================ short test summary info ===================
      FAILED tests/test_magic.py::TestMagic::test_failure - AssertionError: True is not false
      ==================== 1 failed in X.YZs =====================

    Success! I just made a program_ that can make the ``magic`` project anytime I want and it automatically does the steps I did manually.

    :ref:`Click Here to skip to How to use makePythonTdd.ps1 to make a different project<how to use makePythonTdd to make a different project>`

----

*********************************************************************************
how to view the permissions of a file
*********************************************************************************

.. attention::

  This part is only for Computers with MacOS_, Linux_ or `Windows Subsystem for Linux`_.

  :ref:`Click Here to skip to How to use makePythonTdd.ps1 to make a different project if you have Windows without Windows Subsystem for Linux<how to use makePythonTdd to make a different project>`.

I use ls_ to check the permissions of the file_

.. code-block:: python
  :emphasize-lines: 1

  ls -l makePythonTdd.sh

``-l`` is the option to show the long listing format which includes permissions for the file_

The terminal_ shows

.. code-block:: python

  -rw-r--r-- 1 abcdef ghijk XX Month  Y ZA:BC makePythonTdd.sh

.. note:: the first 10 characters above (``-rw-r--r--``) are grouped into four

  .. code-block:: python

    -    rw-    r--    r--

  the groups that have three characters show ``read``, ``write`` and ``execute`` permissions with

  - ``r`` for can ``read``
  - ``w`` for can ``write`` to
  - ``x`` for can ``execute``
  - ``-`` for CANNOT

  here is what it means for ``makePythonTdd.sh``

  * The first group with just one character tells if this is a file_ or directory_ : ``-`` means this is a file_, it is NOT a directory_.
  * The second group has three characters, and is for the owner of the file_: ``rw-`` means the owner of the file_ can read (``r``), write to (``w``), and CANNOT (``-``) execute the file_.
  * The next group also has three characters, and is for the group the owner of the file_ belongs to: ``r--`` means the group can read (``r``), CANNOT (``-``) write to, and CANNOT (``-``) execute the file_.
  * The last group has three characters and is for other users: ``r--`` means other users can read (``r``), CANNOT (``-``) write to, and CANNOT (``-``) execute the file_.

I want to add execute permissions so I can run (execute) the file_.

----

*********************************************************************************
how to make a shell script run as a command
*********************************************************************************

* I change the mode of the file_ to add executable permissions

  .. code-block:: python
    :emphasize-lines: 1

    chmod +x makePythonTdd.sh

  chmod_ is a program_ that changes the mode (permissions) of the given file_, the terminal_ goes back to the command line.

* I list the permissions again with ls_

  .. code-block:: python
    :emphasize-lines: 1

    ls -l makePythonTdd.sh

  the terminal_ is my friend, and shows

  .. code-block:: python

    -rwxr-xr-x 1 abcdef ghijk XX Month  Y ZA:BC makePythonTdd.sh

  .. note::

    * ``-`` means this is a file_, it is NOT a directory_.
    * ``rwx`` means the owner of the file_ can read (``r``), write to (``w``) and execute (``x``) the file_.
    * ``r-x`` means the group of the owner of the file_ can read (``r``), CANNOT (``-``) write to, and can execute (``x``) the file_.
    * The second ``r-x`` means other users can read (``r``), CANNOT (``-``) write to, and can execute (``x``) the file_.

* I try the command again

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh

  the terminal_ is my friend, and shows

  .. code-block:: python
    :emphasize-lines: 10

    ========================== FAILURES ===========================
    __________________ TestMagic.test_failure _____________________

    self = <tests.test_magic.TestMagic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_magic.py:7: AssertionError
    ================== short test summary info ====================
    FAILED tests/test_magic.py::TestMagic::test_failure - AssertionError: True is not false
    ===================== 1 failed in X.YZs =======================

  Success! I just made a program_ that can make the ``magic`` project anytime I want and it automatically does the steps I used to do manually.


----

*********************************************************************************
how to use makePythonTdd to make a different project
*********************************************************************************

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_magic.py:7`` to open it and place the cursor on line 7
* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in ``test_magic.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    class TestMagic(unittest.TestCase):

        def test_failure(self):
            # self.assertFalse(True)
            self.assertFalse(False)


    # Exceptions seen

  the test passes.

* I close ``test_magic.py``

* I click in the terminal_, and use :kbd:`q` on the keyboard to leave the tests, the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

* I want to use ``makePythonTdd`` to make another project with a different name. I change ``magic`` to the name of the new project

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. literalinclude:: ../code/make_tdd/makePythonTddNoVariables.sh
        :language: python
        :linenos:
        :emphasize-lines: 2-3, 5, 12, 20

      I run ``makePythonTdd.sh`` in the terminal_ to make a project named ``more_magic``

      .. code-block:: python
        :emphasize-lines: 1

        ./makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      .. literalinclude:: ../code/make_tdd/makePythonTddNoVariables.ps1
        :language: Powershell
        :linenos:
        :emphasize-lines: 1-2, 4, 11, 19

      I run ``makePythonTdd.ps1`` in the terminal_ to make a project named ``more_magic``

      .. code-block:: python
        :emphasize-lines: 1

        .\makePythonTdd.ps1

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
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

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_more_magic.py:7`` to open it
* I change :ref:`assertFalse<another way to test if something is grouped as False>` to :ref:`assertTrue<another way to test if something is grouped as True>` in ``test_more_magic.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    class TestMoreMagic(unittest.TestCase):

        def test_failure(self):
            # self.assertFalse(True)
            self.assertTrue(True)


    # Exceptions seen

  the test passes.

* I close ``test_more_magic.py``

* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests, the terminal_ is my friend, and shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

The program_ works and can automatically make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>` the way I want every time. What a beautiful life.

----

********************************************************************************************
review
********************************************************************************************

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen one way I can make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>`, with a :ref:`program<makePythonTdd>` to do it on any Linux_, Windows_ or MacOS_ computers.

:ref:`How many questions can you answer after going through this chapter?<questions about making a Python Test Driven Development Environment automatically>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<makePythonTdd with no variables>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python Test Driven Development environment manually<how to make a Python Test Driven Development environment manually>`.
* :ref:`I know what a Python module is<what is a module?>`.
* :ref:`I know how to run tests automatically<how to run tests automatically>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`I know how to make a person with strings<how to make a person with strings>`.
* :ref:`I know how to make functions that take input<functions that take input>`.
* :ref:`I know what causes TypeError<what causes TypeError?>`.
* :ref:`I know how to place values in strings<telephone>`.
* :ref:`I know how to make a person say hello with f-strings<how to make a person with f-strings>`.
* :ref:`I know how to separate tests from solutions<separate and equal>`.
* :ref:`I know what causes AttributeError<what causes AttributeError?>`.
* :ref:`I know how to make a person with a class<how to make a person with a class>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`

:ref:`Would you like to test the truth table?<truth table>` It helps understand writing programs_ that make decisions based on :ref:`conditions<if statements>`.

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