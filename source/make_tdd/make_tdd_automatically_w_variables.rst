.. meta::
  :description: Automate makePythonTdd with a PROJECT_NAME variable, then pass the project name as $1 (bash) or $args[0] (PowerShell). Jacob Itegboje edits makePythonTdd.sh and makePythonTdd.ps1 so one command builds uv init, tests package, first unittest test_failure with assertFalse(True), pytest and pytest-watcher, and pytest-watcher . --now. Covers pro_magic then pro_magic_plus CLI args, AssertionError True is not false, Testpro_magic snake_case vs CapWords TestProMagic, tree after setup, and an exceptions project demo. Pumping Python TDD environment with variables chapter.
  :keywords: Jacob Itegboje, Pumping Python, makePythonTdd.sh, makePythonTdd.ps1, PROJECT_NAME variable shell script, bash $1 first argument, PowerShell $args[0], uv init project name, assertFalse True AssertionError, Testpro_magic snake_case CapWords, pro_magic pro_magic_plus, pytest-watcher --now, make Python Test Driven Development environment automatically with variables

.. include:: ../links.rst

##############################################################################################
how to make a Python Test Driven Development environment automatically with variables
##############################################################################################

Since I am the greatest programmer in the world, I should not be doing as much repetition as I have done so far. I have to make it better.

Here are steps I take with ``makePythonTdd`` to make the environment for every project on a computer with MacOS_, Linux_ or `Windows`_ with `Windows Subsystem for Linux`_

#. I give the project a name
#. I open ``makePythonTdd``
#. I change the name of the project to the new project name
#. I run ``makePythonTdd``
#. I open the test file_ in the editor from the terminal_
#. I make the test pass
#. I start working on the project

----

*********************************************************************************
preview
*********************************************************************************

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    .. literalinclude:: ../code/make_tdd/makePythonTdd.sh
      :language: shell
      :linenos:
      :caption: makePythonTdd.sh

  .. tab-item:: no WSL
    :sync: no_wsl

    .. literalinclude:: ../code/make_tdd/makePythonTdd.ps1
      :language: shell
      :linenos:
      :caption: makePythonTdd.ps1

----

********************************************************************************************
how to use a variable in a shell script
********************************************************************************************

The ``makePythonTdd`` works and always makes a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>` the way I want it. The problem is I have to change the name of the project in a few places every time I use the program to make a project.

I want the program_ to take the name of the project once and use the name to make the

- project folder_
- file_ for the program_ in the ``src`` folder_
- file_ for the test in the ``tests`` folder_
- :ref:`test class<everything is an object>` in the test file_
- :ref:`virtual environment<what is a virtual environment?>` in the ``.venv`` folder_
- install dependencies
- automatically run tests

This way I give one command for the program_ with the name of the project and have it do all the steps for me except

* give the project a name
* make the test pass and
* work on the project

As a reminder, it will always make this structure

.. code-block:: shell
  :emphasize-text: PROJECT_NAME
  :emphasize-lines: 8-14

  PROJECT_NAME
  ├── .git
  ├── .gitignore
  ├── pyproject.toml
  ├── .pytest_cache
  ├── .python-version
  ├── README.md
  ├── requirements.txt
  ├── src
  │   └── PROJECT_NAME
  │       └── __init__.py
  ├── tests
  │   ├── __init__.py
  │   └── test_PROJECT_NAME.py
  ├── uv.lock
  └── .venv

I can use a :ref:`variable<what is a variable?>` for the name of the project

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    * I open ``makePythonTdd.sh``

    * I add ``PROJECT_NAME`` to represent any project name I use to make a project

      .. code-block:: shell
        :linenos:
        :emphasize-lines: 2
        :emphasize-text: PROJECT_NAME

        #!/bin/bash
        PROJECT_NAME="pro_magic"

  .. tab-item:: no WSL
    :sync: no_wsl

    * I open ``makePythonTdd.ps1``

    * I add ``$PROJECT_NAME`` to represent any project name I use to make a project

      .. code-block:: shell
        :linenos:
        :emphasize-lines: 1
        :emphasize-text: PROJECT_NAME

        $PROJECT_NAME="pro_magic"

* A :ref:`variable<what is a variable?>` is a name used for a value that can change. For example, we use the word

  * ``woman`` to represent any woman
  * ``man`` to represent any man
  * ``child`` to represent any child
  * ``parent`` to represent anyone with a child.

* I use ``PROJECT_NAME`` to represent any project name
* I name this project ``pro_magic`` because I am a professional

* I change the name of the project to the :ref:`variable<what is a variable?>` (``PROJECT_NAME``) I just added so that I only have to make a change in one place

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    .. literalinclude:: ../code/make_tdd/makePythonTddVariables.sh
      :language: shell
      :linenos:
      :emphasize-lines: 3-4, 11, 19

    * I run ``makePythonTdd.sh`` in the terminal_ to make the ``pro_magic`` project

      .. code-block:: python
        :emphasize-lines: 1

        ./makePythonTdd.sh

  .. tab-item:: no WSL
    :sync: no_wsl

    .. literalinclude:: ../code/make_tdd/makePythonTddVariables.ps1
      :language: Powershell
      :linenos:
      :emphasize-lines: 2-3, 10, 18

    * I run ``makePythonTdd.ps1`` in the terminal_ to make the ``pro_magic`` project

      .. code-block:: python
        :emphasize-lines: 1

        .\makePythonTdd.ps1

* the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 4, 10, 12
    :emphasize-text: pro_magic

    ========================= FAILURES =========================
    _______________ Testpro_magic.test_failure _________________

    self = <tests.test_pro_magic.Testpro_magic testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_pro_magic.py:7: AssertionError
    ================= short test summary info =================
    FAILED tests/test_pro_magic.py::Testpro_magic::test_failure - AssertionError: True is not false
    =================== 1 failed in X.YZs =====================

  this program_ does not make the class name in the :ref:`CapWords format<CapWords>` (``TestProMagic``) so it is in :ref:`snake_case` (``Testpro_magic``), :ref:`there has to be a better way<BONUS: makePythonTdd.sh Pro>`.

* I hold :kbd:`ctrl` on the keyboard, then click on ``tests/test_pro_magic.py`` in the terminal_ to open it

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes.

* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I run tree_ to see what I have in the ``pro_magic`` folder_

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    .. code-block:: python
      :emphasize-lines: 1

      tree -a -L 1 pro_magic

  .. tab-item:: no WSL
    :sync: no_wsl

    .. code-block:: python
      :emphasize-lines: 1

      tree pro_magic

* the terminal_ shows

  .. code-block:: shell

    pro_magic
    ├── .git
    ├── .gitignore
    ├── pyproject.toml
    ├── .pytest_cache
    ├── .python-version
    ├── README.md
    ├── requirements.txt
    ├── src
    ├── tests
    ├── uv.lock
    └── .venv

The program_ does what I want, and I only need to give the project name in one place. It would be nice if I do not have to go into the file_ to give it the project name.

----

********************************************************************************************
how to call a shell script with arguments
********************************************************************************************

I want to be able to call the program_ and give it a name for the project from the command line.

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    I can do this with ``$1`` in bash_. ``$1`` is for the first argument given after the name of a program_ when it is called. For example

  .. tab-item:: no WSL
    :sync: no_wsl

    I can do this with ``$args[0]`` in PowerShell_. ``$args[0]`` is for the first argument given after the name of a program_ when it is called. For example

.. code-block:: shell

  command argument

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    in the code above, ``command`` is the name of the program_ and ``$1`` is ``argument``


  .. tab-item:: no WSL
    :sync: no_wsl

    in the code above, ``command`` is the name of the program_ ``$args[0]`` is ``argument``

Here are a few other examples

.. code-block:: shell

  mkdir folder_name
  touch file_name
  echo "echo"

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    * ``mkdir`` is the command, and ``$1`` is ``folder_name``
    * ``touch`` is the command, and ``$1`` is ``file_name``
    * ``echo`` is the command, and ``$1`` is ``"echo"``

  .. tab-item:: no WSL
    :sync: no_wsl

    * ``mkdir`` is the command, and ``$args[0]`` is ``folder_name``
    * ``touch`` is the command, and ``$args[0]`` is ``file_name``
    * ``echo`` is the command, and ``$args[0]`` is ``"echo"``

----

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    * I change ``pro_magic`` to ``$1`` in ``makePythonTdd.sh``

      .. code-block:: shell
        :linenos:
        :emphasize-lines: 2
        :emphasize-text: 1

        #!/bin/bash
        PROJECT_NAME=$1
        uv init $PROJECT_NAME

    * I try the program_ again, this time with a name for the project in the terminal_

      .. code-block:: python
        :emphasize-lines: 1

        ./makePythonTdd.sh pro_magic_plus

  .. tab-item:: no WSL
    :sync: no_wsl

    * I change ``pro_magic`` to ``$args[0]`` in ``makePythonTdd.ps1``

      .. code-block:: shell
        :linenos:
        :emphasize-lines: 1
        :emphasize-text: args

        $PROJECT_NAME=$args[0]
        uv init $PROJECT_NAME

    * I try the program_ again, this time with a name for the project in the terminal_

      .. code-block:: python
        :emphasize-lines: 1

        .\makePythonTdd.ps1 pro_magic_plus

* the terminal_ is my friend, and shows

  .. code-block:: shell
    :emphasize-lines: 10
    :emphasize-text: pro_magic_plus

    ========================= FAILURES =========================
    ____________ Testpro_magic_plus.test_failure _______________

    self = <tests.test_pro_magic_plus.Testpro_magic_plus testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_pro_magic_plus.py:7: AssertionError
    ================= short test summary info ==================
    FAILED tests/test_pro_magic_plus.py::Testpro_magic_plus::test_failure - AssertionError: True is not false
    ==================== 1 failed in X.YZs =====================

* I hold :kbd:`ctrl` on the keyboard in the terminal_ and click on ``tests/test_pro_magic_plus.py`` to open it, then make the test pass

* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I run tree_ to see what I have in the ``pro_magic_plus`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree -aL 1 pro_magic_plus

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        tree pro_magic_plus

  the terminal_ is my friend, and shows

  .. code-block:: shell

    pro_magic_plus
    ├── .git
    ├── .gitignore
    ├── pyproject.toml
    ├── .pytest_cache
    ├── .python-version
    ├── README.md
    ├── requirements.txt
    ├── src
    ├── tests
    ├── uv.lock
    └── .venv

* I can now make a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` with ``makePythonTdd`` when I give it a name for the ``PROJECT_NAME`` :ref:`variable<what is a variable?>`. For example, when I type this in the terminal_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        ./makePythonTdd.sh exceptions

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        .\makePythonTdd.ps1 exceptions

  it does all the steps then shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    ======================== FAILURES ==========================
    ______________ Testexceptions.test_failure _________________

    self = <tests.test_exceptions.Testexceptions testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_exceptions.py:7: AssertionError
    ================== short test summary info ==================
    FAILED tests/test_exceptions.py::Testexceptions::test_failure - AssertionError: True is not false
    ===================== 1 failed in X.YZs =====================

the computer makes a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>` for a project called :ref:`exceptions<how to test that an Exception is raised>` and runs :ref:`the first failing test<test_failure>`. I continue this in :ref:`how to test that an Exception is raised`

----

********************************************************************************************
review
********************************************************************************************

`Computer Programming`_ allows me to take some steps and make them a one line command for the computer to do for me. You have seen a way to make a :ref:`Python Test Driven Development environment<what is a Test Driven Development Environment?>`, and have a :ref:`program<makePythonTdd>` to do it for you on any Linux_, Windows_ or MacOS_ computers.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see the CODE for makePythonTdd.sh?<makePythonTdd with variables>`

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
* :ref:`I know how Python groups objects into False or True<what are booleans?>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`.
* :ref:`I know how to write programs that make decisions<truth table>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically with variables<how to make a Python Test Driven Development environment automatically with variables>`.

:ref:`Would you like to test making a person with Exceptions?<how to test that an Exception is raised>`

----

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