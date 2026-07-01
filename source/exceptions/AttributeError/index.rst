.. meta::
  :description: What causes AttributeError in Python? Step-by-step TDD tutorial that deliberately triggers AttributeError: module 'src.attribute_error' has no attribute 'variable_00' (and with "Did you mean" suggestions in later steps), plus side-effect ModuleNotFoundError: No module named 'src.attribute_error', NameError during bare name assignment in GREEN steps, and TypeError: 'NoneType' object is not callable (when a name assigned None is called as a function). Fix by adding 10 module variables (chained = None) then 10 functions (each returning the previous) in src/attribute_error.py; tests use bare attribute access and calls (no assert statement needed for the main tests; the access itself must not raise). Demonstrates that variables and functions are attributes of the module and "in Python everything is an object". Re-uses the initial test_failure from AssertionError. Covers uv init attribute_error, mkdir tests + src, tests/__init__.py, mv main.py, requirements.txt with pytest + pytest-watcher, uv add --requirement requirements.txt, uv run pytest-watcher . --now, git commit after every RED/GREEN/REFACTOR (including "remove the commented lines" on the impl), src package layout for "import src.attribute_error". Part of the Pumping Python TDD book by Jacob Itegboje.
  :keywords: Jacob Itegboje, Pumping Python, python AttributeError, what causes AttributeError, AttributeError: module 'src.attribute_error' has no attribute, AttributeError Did you mean, python AttributeError fix, TDD AttributeError, red green refactor attributes, uv init attribute_error, src.attribute_error, bare attribute access unittest, no assert needed for AttributeError test, python module has no attribute, variables are attributes of modules, functions are attributes of modules, python everything is an object, python TDD src layout, pytest-watcher AttributeError, AssertionError True is not false, 'NoneType' object is not callable, ModuleNotFoundError No module named src, NameError name is not defined, 10 variables 10 functions, uv add --requirement, uv run pytest-watcher . --now, git commit after each step, remove the commented lines, Pumping Python exceptions, python TDD for beginners AttributeError, src package layout

.. include:: ../../links.rst

.. _AttributeError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError

#################################################################################
what causes AttributeError?
#################################################################################

----

AttributeError_ happens when a name that is NOT in an :ref:`object (everything in Python is an object)<everything is an object>` is used.

----

*********************************************************************************
what is an attribute?
*********************************************************************************

An :ref:`attribute<what causes AttributeError?>` is a :ref:`name (variable?)<what is a variable?>` for something that belongs to :ref:`an object (a class)<what is a class?>`, for example, a human being has attributes like height, weight, sex and color, they are also known as properties.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/attribute_error/tests/test_attribute_error.py
  :language: python
  :linenos:

*********************************************************************************
questions about AttributeError
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`what causes AttributeError?`
* :ref:`what is an attribute?`

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``attribute_error``
* I open a terminal_
* I `change directory`_ to the ``attribute_error`` folder_ in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd attribute_error

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: attribute_error

  there is no folder_ with the name ``attribute_error`` in this folder_.

* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init attribute_error

  the terminal_ shows

  .. code-block:: shell

    Initialized project `attribute-error`
    at `.../pumping_python/attribute_error`

  then goes back to the command line.

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd attribute_error

  the terminal_ shows I am in the ``attribute_error`` folder_

  .. code-block:: shell

    .../pumping_python/attribute_error

* I `make a directory`_ for the tests

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line.

* I make the ``tests`` directory_ a `Python package`_

  .. danger:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        touch tests/__init__.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        New-Item tests/__init__.py

  the terminal_ goes back to the command line.

* I make a :ref:`Python file<what is a module?>` for the tests in the ``tests`` directory_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        touch tests/test_attribute_error.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        New-Item tests/test_attribute_error.py

  the terminal_ goes back to the command line.

* I use the `mv program`_ to change the name of ``main.py`` to ``test_attribute_error.py`` and move it to the ``tests`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        mv main.py tests/test_attribute_error.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        Move-Item main.py tests/test_attribute_error.py

  the terminal_ goes back to the command line.

* I open ``test_attribute_error.py``

* I delete all the text then add :ref:`the first failing test<test_failure>` to ``test_attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def test_failure():
        assert False is True

* I go back to the terminal_ to make a requirements file_ for the `Python packages`_ I need

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

  the terminal_ goes back to the command line.

* I add `pytest-watcher`_ to the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

  the terminal_ goes back to the command line.

* I use uv_ to install `pytest-watcher`_ with the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal_ shows that it installed `pytest-watcher`_ and its dependencies.

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

  the terminal_ goes back to the command line.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'setup project'

  the terminal_ shows a summary of the changes then goes back to the command line.

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 6, 8, 10

    ======================== FAILURES ========================
    ______________________ test_failure ______________________

        def test_failure():
    >       assert False is True
    E       assert False is True

    test_attribute_error.py:2: AssertionError
    ================ short test summary info =================
    FAILED test_attribute_error.py::test_failure - assert False is True
    =================== 1 failed in X.YZs ====================

  because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors and try to run ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6
    :emphasize-text: AssertionError

    def test_failure():
        assert False is True


    # Exceptions seen
    # AssertionError

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def test_failure():
        # assert False is True
        assert False is False


    # Exceptions seen
    # AssertionError

  the test passes.

* I add an `import statement`_ at the top of  ``test_attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.attribute_error

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src'

  because Python_ cannot find anything named ``src`` in this project.

* I add :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3
    :emphasize-text: ModuleNotFoundError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError

* I open a new terminal_ then `change directories`_ to ``attribute_error``

  .. code-block:: python
    :emphasize-lines: 1

    cd attribute_error

* I use mkdir_ to make a folder_ named ``src`` in the project

  .. code-block:: python
    :emphasize-lines: 1

    mkdir src

* I go back to the terminal_ where the tests are running
* I go to ``test_attribute_error.py`` and use :kbd:`ctrl/command+s` on the keyboard to run the test again. The terminal_ shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.attribute_error'

  because there is nothing named ``attribute_error`` in the ``src`` folder_

* I go to the second terminal_
* I use touch_ to make ``attribute_error.py`` in the ``src`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    touch src/attribute_error.py

* I go to the terminal_ where the tests are running and it shows the test is green again.

----

*********************************************************************************
test_attribute_error_w_variables
*********************************************************************************

:ref:`AttributeError<what causes AttributeError?>` happens when I use a :ref:`variable<what is a variable?>` that does not exist in an :ref:`object<what is a class?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change :ref:`test_failure` to ``test_attribute_error_w_variables``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import src.attribute_error


    def test_attribute_error_w_variables():
        src.attribute_error.variable_00


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.attribute_error'
                    has no attribute 'variable_00'

  because when ``src.attribute.variable_00`` runs, Python_ follows this path

  .. code-block:: shell

      src
      └── attribute_error.py
          └── variable_00 # does not exist in attribute_error.py

  which raises :ref:`AttributeError<what causes AttributeError?>` since there is nothing named ``variable_00`` in ``attribute_error.py`` in the ``src`` folder_, it is empty.

* I add AttributeError_ to the list of :ref:`Exceptions<errors>` seen in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``attribute_error.py`` from the ``src`` folder_

* I add ``variable_00`` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    variable_00

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'variable_00' is not defined

  because I used a name that is not defined in this file_

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 5
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError

* I point ``variable_00`` to :ref:`None<what is None?>` to define it, in ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # variable_00
    variable_00 = None

  the test passes because

  - When ``import src.attribute_error`` runs, Python_ brings in an :ref:`object<what is a class?>` for the ``attribute_error.py`` file_ from the ``src`` folder_ so I can use it in ``test_attribute_error.py`` as ``src.attribute_error``.
  - When ``src.attribute_error.variable_00`` runs, Python_ looks at what the ``variable_00`` :ref:`variable<what is a variable?>` from the :ref:`object<what is a class?>` it imported for the ``attribute_error.py`` file_ from the ``src`` folder_ (``src.attribute_error``) points to.

  I think of ``src.attribute_error.variable_00`` like an address

  .. code-block:: shell

    src
    └── attribute_error.py
        └── variable_00 = None

  - ``variable_00`` is something in ``attribute_error``, in this case it is a :ref:`variable<what is a variable?>` in ``attribute_error``
  - ``attribute_error`` is something in ``src``, in this case it is ``attribute_error.py`` (a :ref:`module<what is a module?>`) in the ``src`` folder_
  - ``src`` is something Python_ can import (a :ref:`module<what is a module?>`, `Python package`_ or folder_)
  - ``variable_00`` is now an :ref:`attribute/property<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_. I can use it from outside the file_ with ``src.attribute_error.variable_00``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a statement for ``variable_01`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    def test_attribute_error_w_variables():
        src.attribute_error.variable_00
        src.attribute_error.variable_01


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'variable_01'.
                    Did you mean: 'variable_00'?

* I add ``variable_01`` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    # variable_00
    variable_00 = None
    variable_01

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'variable_01' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # variable_00
    variable_00 = None
    # variable_01
    variable_01 = variable_00

  the test passes because ``variable_01`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.variable_01``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── variable_01 = variable_00

* I add a statement for ``variable_02`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4

    def test_attribute_error_w_variables():
        src.attribute_error.variable_00
        src.attribute_error.variable_01
        src.attribute_error.variable_02


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell
    :force:

    AttributeError: module 'src.attribute_error'
                    has no attribute 'variable_02'.
                    Did you mean: 'variable_00'?

* I add ``variable_02`` and point it to :ref:`None<what is None?>` in ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    # variable_00
    variable_00 = None
    # variable_01
    variable_01 = variable_00
    variable_02 = variable_01

  the test passes because ``variable_02`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.variable_02``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── variable_02 = variable_01

* I add a line for ``variable_03`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5


    def test_attribute_error_w_variables():
        src.attribute_error.variable_00
        src.attribute_error.variable_01
        src.attribute_error.variable_02
        src.attribute_error.variable_03


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'variable_03'.
                    Did you mean: 'variable_00'?

* I add ``variable_03`` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6

    # variable_00
    variable_00 = None
    # variable_01
    variable_01 = variable_00
    variable_02 = variable_01
    variable_03 = variable_02

  the test passes because ``variable_03`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.variable_03``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── variable_03 = variable_02

* I add a line for ``variable_04`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 6


    def test_attribute_error_w_variables():
        src.attribute_error.variable_00
        src.attribute_error.variable_01
        src.attribute_error.variable_02
        src.attribute_error.variable_03
        src.attribute_error.variable_04


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'variable_04'.
                    Did you mean: 'variable_00'?

* I add ``variable_04`` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7

    # variable_00
    variable_00 = None
    # variable_01
    variable_01 = variable_00
    variable_02 = variable_01
    variable_03 = variable_02
    variable_04 = variable_03

  the test passes because ``variable_04`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.variable_04``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── variable_04 = variable_03

* I add a line for ``variable_05`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7


    def test_attribute_error_w_variables():
        src.attribute_error.variable_00
        src.attribute_error.variable_01
        src.attribute_error.variable_02
        src.attribute_error.variable_03
        src.attribute_error.variable_04
        src.attribute_error.variable_05


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'variable_05'.
                    Did you mean: 'variable_00'?

* I add ``variable_05`` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8

    # variable_00
    variable_00 = None
    # variable_01
    variable_01 = variable_00
    variable_02 = variable_01
    variable_03 = variable_02
    variable_04 = variable_03
    variable_05 = variable_04

  the test passes because ``variable_05`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.variable_05``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── variable_05 = variable_04

* I add a line for ``variable_06`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 8

    def test_attribute_error_w_variables():
        src.attribute_error.variable_00
        src.attribute_error.variable_01
        src.attribute_error.variable_02
        src.attribute_error.variable_03
        src.attribute_error.variable_04
        src.attribute_error.variable_05
        src.attribute_error.variable_06


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'variable_06'.
                    Did you mean: 'variable_00'?

* I add ``variable_06`` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9

    # variable_00
    variable_00 = None
    # variable_01
    variable_01 = variable_00
    variable_02 = variable_01
    variable_03 = variable_02
    variable_04 = variable_03
    variable_05 = variable_04
    variable_06 = variable_05

  the test passes because ``variable_06`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.variable_06``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── variable_06 = variable_05

* I add a line for ``variable_07`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 9

    def test_attribute_error_w_variables():
        src.attribute_error.variable_00
        src.attribute_error.variable_01
        src.attribute_error.variable_02
        src.attribute_error.variable_03
        src.attribute_error.variable_04
        src.attribute_error.variable_05
        src.attribute_error.variable_06
        src.attribute_error.variable_07


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'variable_07'.
                    Did you mean: 'variable_00'?

* I add ``variable_07`` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10

    # variable_00
    variable_00 = None
    # variable_01
    variable_01 = variable_00
    variable_02 = variable_01
    variable_03 = variable_02
    variable_04 = variable_03
    variable_05 = variable_04
    variable_06 = variable_05
    variable_07 = variable_06

  the test passes because ``variable_07`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.variable_07``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── variable_07 = variable_06

* I add a line for ``variable_08`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 10

    def test_attribute_error_w_variables():
        src.attribute_error.variable_00
        src.attribute_error.variable_01
        src.attribute_error.variable_02
        src.attribute_error.variable_03
        src.attribute_error.variable_04
        src.attribute_error.variable_05
        src.attribute_error.variable_06
        src.attribute_error.variable_07
        src.attribute_error.variable_08


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'variable_08'.
                    Did you mean: 'variable_00'?

* I add ``variable_08`` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11

    # variable_00
    variable_00 = None
    # variable_01
    variable_01 = variable_00
    variable_02 = variable_01
    variable_03 = variable_02
    variable_04 = variable_03
    variable_05 = variable_04
    variable_06 = variable_05
    variable_07 = variable_06
    variable_08 = variable_07

  the test passes because ``variable_08`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.variable_08``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── variable_08 = variable_07

* I add a line for ``variable_09`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 11

    def test_attribute_error_w_variables():
        src.attribute_error.variable_00
        src.attribute_error.variable_01
        src.attribute_error.variable_02
        src.attribute_error.variable_03
        src.attribute_error.variable_04
        src.attribute_error.variable_05
        src.attribute_error.variable_06
        src.attribute_error.variable_07
        src.attribute_error.variable_08
        src.attribute_error.variable_09


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'variable_09'.
                    Did you mean: 'variable_00'?

* I add ``variable_09`` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 12

    # variable_00
    variable_00 = None
    # variable_01
    variable_01 = variable_00
    variable_02 = variable_01
    variable_03 = variable_02
    variable_04 = variable_03
    variable_05 = variable_04
    variable_06 = variable_05
    variable_07 = variable_06
    variable_08 = variable_07
    variable_09 = variable_08

  the test passes because ``variable_09`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.variable_09``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── variable_09 = variable_08

* I remove the commented lines

  .. code-block:: python
    :linenos:

    variable_00 = None
    variable_01 = variable_00
    variable_02 = variable_01
    variable_03 = variable_02
    variable_04 = variable_03
    variable_05 = variable_04
    variable_06 = variable_05
    variable_07 = variable_06
    variable_08 = variable_07
    variable_09 = variable_08

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_attribute_error_w_variables'

:ref:`A variable in a module is an attribute of the module<test_attribute_error_w_variables>`.

----

*********************************************************************************
test_attribute_error_w_functions
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with a :ref:`function call<how to call a function>`, to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4-5

        src.attribute_error.variable_09


    def test_attribute_error_w_functions():
        src.attribute_error.function_00()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: python

    AttributeError: module 'src.attribute_error'
                    has no attribute 'function_00'

  because there is nothing named ``function_00`` in ``attribute_error.py`` in the ``src`` folder_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name and point it to :ref:`None<what is None?>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 4

    variable_09 = variable_08


    function_00 = variable_09

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  because :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 6
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError
    # TypeError

* I change the :ref:`variable<what is a variable?>` to a :ref:`function<what is a function?>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 4-5

    variable_09 = variable_08


    # function_00 = variable_09
    def function_00(): return variable_09

  the test passes because ``function_00`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can :ref:`call it<how to call a function>` from outside the file_ with ``src.attribute_error.function_00()``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── def function_00(): return variable_09

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line

  .. code-block:: python
    :linenos:

    variable_09 = variable_08


    def function_00(): return variable_09

  time to make it a drill.

* I add a :ref:`call<how to call a function>` to ``function_01`` from :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3

    def test_attribute_error_w_functions():
        src.attribute_error.function_00()
        src.attribute_error.function_01()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'function_01'.
                    Did you mean: 'function_00'?

* I add a :ref:`definition<how to make a function>` for ``function_01`` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def function_00(): return variable_09
    def function_01(): return function_00()

  the test passes because ``function_01`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can :ref:`call it<how to call a function>` from outside the file_ with ``src.attribute_error.function_01()``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── def function_01(): return function_00()

* I add a :ref:`call<how to call a function>` to ``function_02`` from :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 4

    def test_attribute_error_w_functions():
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'function_02'.
                    Did you mean: 'function_00'?

* I add a :ref:`definition<how to make a function>` for ``function_02`` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

    def function_00(): return variable_09
    def function_01(): return function_00()
    def function_02(): return function_01()

  the test passes because ``function_02`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can :ref:`call it<how to call a function>` from outside the file_ with ``src.attribute_error.function_02()``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── def function_02(): return function_01()

* I add a :ref:`call<how to call a function>` to ``function_03`` from :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5

    def test_attribute_error_w_functions():
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()
        src.attribute_error.function_03()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'function_03'.
                    Did you mean: 'function_00'?

* I add a :ref:`definition<how to make a function>` for ``function_03`` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4

    def function_00(): return variable_09
    def function_01(): return function_00()
    def function_02(): return function_01()
    def function_03(): return function_02()

  the test passes because ``function_03`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can :ref:`call it<how to call a function>` from outside the file_ with ``src.attribute_error.function_03()``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── def function_03(): return function_02()

* I add a :ref:`call<how to call a function>` to ``function_04`` from :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 6

    def test_attribute_error_w_functions():
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()
        src.attribute_error.function_03()
        src.attribute_error.function_04()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'function_04'.
                    Did you mean: 'function_00'?

* I add a :ref:`definition<how to make a function>` for ``function_04`` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5

    def function_00(): return variable_09
    def function_01(): return function_00()
    def function_02(): return function_01()
    def function_03(): return function_02()
    def function_04(): return function_03()

  the test passes because ``function_04`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can :ref:`call it<how to call a function>` from outside the file_ with ``src.attribute_error.function_04()``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── def function_04(): return function_03()

* I add a :ref:`call<how to call a function>` to ``function_05`` from :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 7

    def test_attribute_error_w_functions():
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()
        src.attribute_error.function_03()
        src.attribute_error.function_04()
        src.attribute_error.function_05()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'function_05'.
                    Did you mean: 'function_00'?

* I add a :ref:`definition<how to make a function>` for ``function_05`` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 6

    def function_00(): return variable_09
    def function_01(): return function_00()
    def function_02(): return function_01()
    def function_03(): return function_02()
    def function_04(): return function_03()
    def function_05(): return function_04()

  the test passes because ``function_05`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can :ref:`call it<how to call a function>` from outside the file_ with ``src.attribute_error.function_05()``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── def function_05(): return function_04()

* I add a :ref:`call<how to call a function>` to ``function_06`` from :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 8

    def test_attribute_error_w_functions():
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()
        src.attribute_error.function_03()
        src.attribute_error.function_04()
        src.attribute_error.function_05()
        src.attribute_error.function_06()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'function_06'.
                    Did you mean: 'function_00'?

* I add a :ref:`definition<how to make a function>` for ``function_06`` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 7

    def function_00(): return variable_09
    def function_01(): return function_00()
    def function_02(): return function_01()
    def function_03(): return function_02()
    def function_04(): return function_03()
    def function_05(): return function_04()
    def function_06(): return function_05()

  the test passes because ``function_06`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can :ref:`call it<how to call a function>` from outside the file_ with ``src.attribute_error.function_06()``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── def function_06(): return function_05()

* I add a :ref:`call<how to call a function>` to ``function_07`` from :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 9

    def test_attribute_error_w_functions():
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()
        src.attribute_error.function_03()
        src.attribute_error.function_04()
        src.attribute_error.function_05()
        src.attribute_error.function_06()
        src.attribute_error.function_07()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'function_07'.
                    Did you mean: 'function_00'?

* I add a :ref:`definition<how to make a function>` for ``function_07`` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 8

    def function_00(): return variable_09
    def function_01(): return function_00()
    def function_02(): return function_01()
    def function_03(): return function_02()
    def function_04(): return function_03()
    def function_05(): return function_04()
    def function_06(): return function_05()
    def function_07(): return function_06()

  the test passes because ``function_07`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can :ref:`call it<how to call a function>` from outside the file_ with ``src.attribute_error.function_07()``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── def function_07(): return function_06()

* I add a :ref:`call<how to call a function>` to ``function_08`` from :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 10

    def test_attribute_error_w_functions():
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()
        src.attribute_error.function_03()
        src.attribute_error.function_04()
        src.attribute_error.function_05()
        src.attribute_error.function_06()
        src.attribute_error.function_07()
        src.attribute_error.function_08()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'function_08'.
                    Did you mean: 'function_00'?

* I add a :ref:`definition<how to make a function>` for ``function_08`` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 9

    def function_00(): return variable_09
    def function_01(): return function_00()
    def function_02(): return function_01()
    def function_03(): return function_02()
    def function_04(): return function_03()
    def function_05(): return function_04()
    def function_06(): return function_05()
    def function_07(): return function_06()
    def function_08(): return function_07()

  the test passes because ``function_08`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can :ref:`call it<how to call a function>` from outside the file_ with ``src.attribute_error.function_08()``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── def function_08(): return function_07()

* I add a :ref:`call<how to call a function>` to ``function_09`` from :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 11

    def test_attribute_error_w_functions():
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()
        src.attribute_error.function_03()
        src.attribute_error.function_04()
        src.attribute_error.function_05()
        src.attribute_error.function_06()
        src.attribute_error.function_07()
        src.attribute_error.function_08()
        src.attribute_error.function_09()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'function_09'.
                    Did you mean: 'function_00'?

* I add a :ref:`definition<how to make a function>` for ``function_09`` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 10

    def function_00(): return variable_09
    def function_01(): return function_00()
    def function_02(): return function_01()
    def function_03(): return function_02()
    def function_04(): return function_03()
    def function_05(): return function_04()
    def function_06(): return function_05()
    def function_07(): return function_06()
    def function_08(): return function_07()
    def function_09(): return function_08()

  the test passes because ``function_09`` is now an :ref:`attribute<what is a class attribute?>` of ``attribute_error.py`` in the ``src`` folder_, and I can :ref:`call it<how to call a function>` from outside the file_ with ``src.attribute_error.function_09()``.

  .. code-block:: shell

    src
    └── attribute_error.py
        └── def function_09(): return function_08()

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_attribute_error_w_functions'

:ref:`A function in a module is an attribute of the module<test_attribute_error_w_functions>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``attribute_error.py`` and ``test_attribute_error.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``attribute_error``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

I ran tests for :ref:`AttributeError<what causes AttributeError?>` that showed

* :ref:`A function in a module is an attribute of the module<test_attribute_error_w_functions>`.
* :ref:`A variable in a module is an attribute of the module<test_attribute_error_w_variables>`.

I also saw these :ref:`Exceptions<errors>`

* :ref:`AssertionError<what causes AssertionError?>`
* :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`TypeError<what causes TypeError?>`

My problem with the tests is that they all show the correct way to use :ref:`attributes<what is a class attribute?>` I made in ``attribute_error.py``. If someone reads the file_ or runs it, there is no way for them to know how the code relates to :ref:`AttributeError<what causes AttributeError?>` unless they go through the process with me, there has to be a better way.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<AttributeError: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

You know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what causes AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`
* :ref:`how to make functions that take input<functions that take input>`
* :ref:`what causes TypeError?`
* :ref:`how to place values in strings<telephone>`
* :ref:`how to make a person say hi with f-strings<how to make a person with f-strings>`
* :ref:`how to separate tests from solutions<separate and equal functions>`
* :ref:`what causes AttributeError?`

:ref:`Would you like to test using a class to remove repetition of inputs from functions?<how to make a person with a class>`

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