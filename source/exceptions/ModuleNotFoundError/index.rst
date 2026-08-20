.. meta::
  :description: What is a Python module? Fix ModuleNotFoundError by creating the missing .py files and folders. Jacob Itegboje uses TDD with unittest and import src.module_00 through src.doe.jane plus import magic to show ModuleNotFoundError No module named src.module_00, src.module_01, src.doe, src.doe.john, src.doe.jane, and magic until touch, New-Item, and mkdir make imports pass. Covers .py modules, tests/__init__.py so unittest discovers the file, a src/doe folder that imports without __init__.py, nested import src.doe.john, import magic from the project root, assert False is True setup AssertionError, NO TESTS RAN when imports-only pass, git add commit, and why you still run python3 -m unittest by hand until pytest-watcher. Pumping Python exceptions chapter after manual TDD setup.
  :keywords: Jacob Itegboje, Pumping Python, what is a python module, ModuleNotFoundError No module named, import src.module_00, python package __init__.py, namespace folder import without __init__.py, nested import src.doe.john, import magic project root, unittest import error, python3 -m unittest NO TESTS RAN, touch module_01.py New-Item mkdir src/doe, module not found error tdd, fix python import missing file, red green refactor imports, uv init module_not_found_error

.. include:: ../../links.rst

.. _ModuleNotFoundError: https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError
.. _sys.path: https://docs.python.org/3/library/sys.html#sys.path
.. _module: https://docs.python.org/3/glossary.html#term-module
.. _Python module: module_
.. _modules: module_

#################################################################################
what is a module?
#################################################################################

A `Python module`_ is any file_ that ends in ``.py``. Any folder_ that contains an ``__init__.py`` is also a Python_ module_.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/module_not_found_error/test_module_not_found_error.py
  :language: python
  :linenos:
  :caption: module_not_found_error/tests/test_module_not_found_error.py

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``module_not_found_error``
* I open a terminal_

* I `change directory`_ to the ``module_not_found_error`` project in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd module_not_found_error

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: module_not_found_error

  there is no folder_ with the name ``module_not_found_error`` in this folder_.

* I use the `uv Python Package Manager`_ to setup the project

  .. code-block:: python
    :emphasize-lines: 1

    uv init module_not_found_error

  the terminal_ shows

  .. code-block:: shell

    Initialized project `module-not-found-error`
    at `.../pumping_python/module_not_found_error`

* I `change directory`_ to the ``module_not_found_error`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd module_not_found_error

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/module_not_found_error

* I make a child folder_ to keep the tests separate from the other files_

  .. code-block:: python
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line.

* I add an empty file_ to the ``tests`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        touch tests/module_not_found_error.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        New-Item tests/module_not_found_error.py

* I open ``module_not_found_error.py`` from the ``tests`` folder_

  .. tip::

    I can open a file_ from the terminal_ with :kbd:`ctrl` (Windows_/Linux_) or :kbd:`command` (MacOS_) on the keyboard and a click with the mouse on the name of the file_

* I add the :ref:`first failing test<test_failure>` to ``module_not_found_error.py`` in the ``tests`` folder_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    assert False is True

* I use the :ref:`unittest module<another way to write tests>` to run tests

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the terminal_ shows

  .. code-block:: python

    ------------------------------------------------------
    Ran 0 tests in 0.000s

    NO TESTS RAN

* I close ``module_not_found_error.py``

  .. danger:: if you do not close ``module_not_found_error.py``, there will be 3 files in the ``tests`` folder after the next step (instead of 2), because the ``Auto Save`` feature (enabled earlier) will save the original file_ if it is still open after you change its name.

* I change the name of ``module_not_found_error.py`` in the ``tests`` folder_ to ``test_module_not_found_error.py``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1-2

        mv tests/module_not_found_error.py \
        tests/test_module_not_found_error.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1-2

        Move-Item tests/module_not_found_error.py \
        tests/test_module_not_found_error.py

  the terminal_ goes back to the command line.

  .. tip::

    The ``\`` + :kbd:`enter/return` allows me to write one long line on multiple lines in the terminal_. Without it I have to write everything as one line because the terminal_ runs whatever line I have written when I hit :kbd:`enter/return` on the keyboard.

* I try to run the test again

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the terminal_ still shows ``NO TESTS RAN``.

.. danger:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    * I make the ``tests`` directory_ a `Python package`_

      .. code-block:: python
        :emphasize-lines: 1

        touch tests/__init__.py

    * I try to run the test again

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

  .. tab-item:: no WSL
    :sync: no_wsl

    * I make the ``tests`` directory_ a `Python package`_

      .. code-block:: python
        :emphasize-lines: 1

        New-Item tests/__init__.py

    * I try to run the test again

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :emphasize-lines: 2, 4, 6

  ...
    File ".../pumping_python/module_not_found_error/tests/test_module_not_found_error.py",
      line 1, in <module>
      assert False is True
              ^^^^^^^^^^^^^
  AssertionError


  ------------------------------------------------------
  Ran 1 test in X.YZs

  FAILED (errors=1)

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``File ".../pumping_python/module_not_found_error/tests/test_module_not_found_error.py", line 1`` in the terminal_, and the `Integrated Development Environment (IDE)`_ opens the file_ with the cursor at the line where the failure happened.

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<how to test that an Exception is raised>` seen, in ``test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    assert False is True


    # Exceptions seen
    # AssertionError

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # assert False is True
    assert False is False


    # Exceptions seen
    # AssertionError

* I run the test again

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the test passes.

* I add the new files_ and folders_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

  the terminal_ goes back to the command line.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'setup project'

  the terminal_ shows a summary of the changes then goes back to the command line. Time to test :ref:`modules<what is a module?>`.

----

*********************************************************************************
test_module_not_found_error
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I remove the :ref:`assert statements<what is an assertion?>` then add an `import statement`_ for a :ref:`module<what is a module?>` at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.module_00


    # Exceptions seen
    # AssertionError

* I run the test again

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the terminal_ is my friend, and shows ModuleNotFoundError_

  .. code-block:: shell
    :emphasize-lines: 5

      File ".../pumping_python/module_not_found_error/
                tests/test_module_not_found_error.py",
        line 1, in <module>
        import src.module_00
    ModuleNotFoundError: No module named 'src.module_00'


    ----------------------------------------------------------------------
    Ran 1 test in X.YZAs

    FAILED (errors=1)

  because when ``import src.module_00`` runs, Python_ tries to bring in an :ref:`object (everything in Python is an object)<everything is an object>` for the ``module_00.py`` file_ from the ``src`` folder_.

* I add ModuleNotFoundError_ to the list of :ref:`Exceptions<how to test that an Exception is raised>` seen, in ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3
    :emphasize-text: ModuleNotFoundError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError

----

*********************************************************************************
what causes ModuleNotFoundError?
*********************************************************************************

ModuleNotFoundError_ is raised when Python_ cannot find a module_ (a file_ that ends in ``.py``) with the name given in an `import statement`_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I go back to the terminal_

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    * I use touch_ to make ``module_00.py`` in the ``src`` folder_

      .. code-block:: python
        :emphasize-lines: 1

        touch src/module_00.py

    * I run the test again

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

  .. tab-item:: no WSL
    :sync: no_wsl

    * I use `New-Item`_ to make ``module_00.py`` in the ``src`` folder_

      .. code-block:: python
        :emphasize-lines: 1

        New-Item src/module_00.py

    * I run the test again

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

- the test passes because when ``import src.module_00`` runs, Python_ brings in an :ref:`object<everything is an object>` for the ``module_00.py`` file_ from the ``src`` folder_ so I can use it in ``tests/test_module_not_found_error.py``

  .. code-block:: shell

    src.module_00
    └── src
        └── module_00.py

- the terminal_ shows ``NO TESTS RAN`` which is confusing since the only way I know the test passed, is because I saw it fail.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an `import statement`_ for ``src.module_01`` to ``tests/test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import src.module_00
    import src.module_01


    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError

* I run the test again

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_01'

* I make a new file_ named ``module_01.py`` in the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        touch src/module_01.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        New-Item src/module_01.py

  the terminal_ goes back to the command line.

* I run the test

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the test passes because ``import src.module_01`` brings in an :ref:`object<everything is an object>` for the ``module_01.py`` file_ from the ``src`` folder_ so I can use it in ``tests/test_module_not_found_error.py``.

  .. code-block:: shell

    src.module_01
    └── src
        └── module_01.py

* I add an `import statement`_ for ``src.module_02`` to ``tests/test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    import src.module_00
    import src.module_01
    import src.module_02


    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError

* I go to the terminal_ to run the test

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_02'

* I make a new file_ named ``module_02.py`` in the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        touch src/module_02.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        New-Item src/module_02.py

  the terminal_ goes back to the command line.

* I run the test again

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the test passes because ``import src.module_02`` brings in an :ref:`object<everything is an object>` for the ``module_02.py`` file_ from the ``src`` folder_ so I can use it in ``tests/test_module_not_found_error.py``.

  .. code-block:: shell

    src.module_02
    └── src
        └── module_02.py

* I add an `import statement`_ for ``src.module_03`` to ``tests/test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

    import src.module_00
    import src.module_01
    import src.module_02
    import src.module_03


    # Exceptions seen

* I go to the terminal_ to run the test

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_03'

* I make a new file_ named ``module_03.py`` in the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        touch src/module_03.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        New-Item src/module_03.py

  the terminal_ goes back to the command line.

* I run the test again

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the test passes because ``import src.module_03`` brings in an :ref:`object<everything is an object>` for the ``module_03.py`` file_ from the ``src`` folder_ so I can use it in ``tests/test_module_not_found_error.py``.

  .. code-block:: shell

    src.module_03
    └── src
        └── module_03.py

* I add an `import statement`_ for ``src.module_04`` to ``tests/test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.module_00
    import src.module_01
    import src.module_02
    import src.module_03
    import src.module_04


    # Exceptions seen

* I go to the terminal_ to run the test

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_04'

* I make a new file_ named ``module_04.py`` in the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        touch src/module_04.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        New-Item src/module_04.py

  the terminal_ goes back to the command line.

* I run the test again

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the test passes because ``import src.module_04`` brings in an :ref:`object<everything is an object>` for the ``module_04.py`` file_ from the ``src`` folder_ so I can use it in ``tests/test_module_not_found_error.py``.

  .. code-block:: shell

    src.module_04
    └── src
        └── module_04.py

* I add an `import statement`_ for ``src.module_05`` to ``tests/test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6

    import src.module_00
    import src.module_01
    import src.module_02
    import src.module_03
    import src.module_04
    import src.module_05


    # Exceptions seen

* I go to the terminal_ to run the test

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_05'

* I make a new file_ named ``module_05.py`` in the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        touch src/module_05.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        New-Item src/module_05.py

  the terminal_ goes back to the command line.

* I run the test again

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the test passes because ``import src.module_05`` brings in an :ref:`object<everything is an object>` for the ``module_05.py`` file_ from the ``src`` folder_ so I can use it in ``tests/test_module_not_found_error.py``.

  .. code-block:: shell

    src.module_05
    └── src
        └── module_05.py

* I add an `import statement`_ for ``src.module_not_found_error`` to ``tests/test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7

    import src.module_00
    import src.module_01
    import src.module_02
    import src.module_03
    import src.module_04
    import src.module_05
    import src.module_not_found_error


    # Exceptions seen

* I go to the terminal_ to run the test

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the terminal_ shows

  .. code-block:: python

    NO TESTS RAN

  the test passes because ``import src.module_not_found_error`` brings in an :ref:`object (everything is an object)<everything is an object>` for the ``module_not_found_error`` folder_ that is in the ``src`` folder_ so I can use it in ``tests/test_module_not_found_error.py``.

  .. code-block:: shell

    src.module_not_found_error
    └── src
        └── module_not_found_error
            └── __init__.py

* I add an `import statement`_ for ``src.doe`` to ``tests/test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8

    import src.module_00
    import src.module_01
    import src.module_02
    import src.module_03
    import src.module_04
    import src.module_05
    import src.module_not_found_error
    import src.doe


    # Exceptions seen

* I go to the terminal_ to run the test

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.doe'

* I make a new folder_ named ``doe`` in the ``src`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    mkdir src/doe

  the terminal_ goes back to the command line.

* I run the test again

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  - the test passes because ``import src.doe`` brings in an :ref:`object<everything is an object>` for the ``doe`` folder_ that is in the ``src`` folder_ so I can use it in ``tests/test_module_not_found_error.py``

    .. code-block:: shell

      src.doe
      └── src
          └── doe

  - this worked even though I did not add an ``__init__.py`` file_ to the folder_.

* I add an `import statement`_ for ``src.doe.john`` to ``tests/test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9

    import src.module_00
    import src.module_01
    import src.module_02
    import src.module_03
    import src.module_04
    import src.module_05
    import src.module_not_found_error
    import src.doe
    import src.doe.john


    # Exceptions seen

* I go to the terminal_ to run the test

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.doe.john'

* I make a new file_ named ``john.py`` in the ``doe`` folder_ in the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        touch src/doe/john.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        New-Item src/doe/john.py

  the terminal_ goes back to the command line.

* I run the test again

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the test passes because ``import src.doe.john`` brings in an :ref:`object<everything is an object>` for the ``john.py`` file_ from the ``doe`` folder_ that is in the ``src`` folder_ so I can use it in ``tests/test_module_not_found_error.py``.

  .. code-block:: shell

    src.doe.john
    └── src
        └── doe
            └── john.py

* I add an `import statement`_ for ``src.doe.jane`` to ``tests/test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10

    import src.module_00
    import src.module_01
    import src.module_02
    import src.module_03
    import src.module_04
    import src.module_05
    import src.module_not_found_error
    import src.doe
    import src.doe.john
    import src.doe.jane


    # Exceptions seen

* I go to the terminal_ to run the test

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.doe.jane'

* I make a new file_ named ``jane.py`` in the ``doe`` folder_ in the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        touch src/doe/jane.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        New-Item src/doe/jane.py

  the terminal_ goes back to the command line.

* I run the test again

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the test passes because ``import src.doe.jane`` brings in an :ref:`object<everything is an object>` for the ``jane.py`` file_ from the ``doe`` folder_ that is in the ``src`` folder_ so I can use it in ``tests/test_module_not_found_error.py``.

  .. code-block:: shell

    src.doe.jane
    └── src
        └── doe
            └── jane.py

* I add an `import statement`_ for ``magic`` to ``tests/test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11

    import src.module_00
    import src.module_01
    import src.module_02
    import src.module_03
    import src.module_04
    import src.module_05
    import src.module_not_found_error
    import src.doe
    import src.doe.john
    import src.doe.jane
    import magic


    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError

* I go to the terminal_ to run the test

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'magic'

* I make a new file_ named ``magic.py`` in the main folder_ of the project (``module_not_found_error``)

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        touch magic.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        New-Item magic.py

  the terminal_ goes back to the command line.

* I run the test again

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        python3 -m unittest

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        python -m unittest

  the test passes because ``import magic`` brings in an :ref:`object (everything is an object)<everything is an object>` for the ``magic.py`` that is in the ``module_not_found_error`` folder_ so I can use it in ``tests/test_module_not_found_error.py``.

  .. code-block:: shell

    magic
    └── magic.py

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

* I add a git_ commit message in the terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'test ModuleNotFoundError'

  the terminal_ shows a summary of the changes then goes back to the command line.

ModuleNotFoundError_ is raised when Python_ cannot find a module_ (a file_ that ends in ``.py``) with the name given in an `import statement`_.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_module_not_found_error.py``
* I go back to the terminal_
* I `change directory`_ to the parent of ``module_not_found_error``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ is my friend, and shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

* I ran a test for ModuleNotFoundError_ to practice making :ref:`Python modules<what is a module?>`.
* The terminal_ shows ``NO TESTS RAN`` when there is no test and when my test passes which is confusing since the only way I know the test passed, is because I saw it fail. :ref:`There has to be a better way<a better way to organize tests>`.

----

=====================================================================================================
how to view all the commands I typed to test ModuleNotFoundError
=====================================================================================================

----

I type history_ in the terminal_ to see all the commands I typed for this project

.. code-block:: python
  :emphasize-lines: 1

  history

the terminal_ shows

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    .. literalinclude:: ../../code/module_not_found_error/ModuleNotFoundErrorHistory.sh
      :language: python
      :emphasize-lines: 6, 8, 10-11, 14, 16-17, 19-20, 22-23, 25-26, 28-29, 31-33, 35-36, 38-39, 41-42, 44-45

    The `history program`_ shows all the commands I typed in the terminal_

    * I ran ``python3 -m unittest`` to see the test fail
    * I ran ``python3 -m unittest`` every time I made a change until the test passed
    * I will run ``python3 -m unittest`` again when I add any code, to make sure tests that passed before do not fail and that the new code I add does what I want

    This means I have to run ``python3 -m unittest`` for each part of the :ref:`Test Driven Development Cycle<what is the Test Driven Development Cycle?>` or any time there is a code change.

    I do not want to type ``python3 -m unittest`` ever again, I want the computer to do it for me.

  .. tab-item:: no WSL
    :sync: no_wsl

    .. literalinclude:: ../../code/module_not_found_error/ModuleNotFoundErrorHistory.ps1
      :language: python
      :emphasize-lines: 6, 8, 10-11, 14, 16-17, 19-20, 22-23, 25-26, 28-29, 31-33, 35-36, 38-39, 41-42, 44-45

    The `history program`_ shows all the commands I typed in the terminal_

    * I ran ``python -m unittest`` to see the test fail
    * I ran ``python -m unittest`` every time I made a change until the test passed
    * I will run ``python -m unittest`` again when I add any code, to make sure tests that passed before do not fail and that the new code I add does what I want

    This means I have to run ``python -m unittest`` for each part of the :ref:`Test Driven Development Cycle<what is the Test Driven Development Cycle?>` or any time there is a code change.

    I do not want to type ``python -m unittest`` ever again, I want the computer to do it for me.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<ModuleNotFoundError: test>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python Test Driven Development environment manually<how to make a Python Test Driven Development environment manually>`.
* :ref:`I know what a Python module is<what is a module?>`.

:ref:`Would you like to see how to run tests automatically?<how to run tests automatically>`

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