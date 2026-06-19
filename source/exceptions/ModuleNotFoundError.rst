.. meta::
  :description: Struggling with Python's ModuleNotFoundError? Learn to fix import errors from other `folders (directories)`_& get your code running. Watch the full tutorial to solve it now!
  :keywords: Jacob Itegboje, python ModuleNotFoundError no module named, how to fix ModuleNotFoundError in vscode, python import error from another folder, python relative import not working, ModuleNotFoundError: No module named 'src', python can't find module in same directory, pythonpath vscode setup, fix python import errors

.. include:: ../links.rst

.. _ModuleNotFoundError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError
.. _sys.path: https://docs.python.org/3/library/sys.html#sys.path

#################################################################################
what is a module?
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/IKb8uyhQPpc?si=XOtc-FDIPLWujM9v" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

A Python_ module_ is any file_ that ends in ``.py``. Any folder_ that contains an ``__init__.py`` is also a Python_ module_.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/tests/test_module_not_found_error.py
  :language: python
  :linenos:

----

*********************************************************************************
start the project
*********************************************************************************

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

* I make a child folder_ in the ``module_not_found_error`` folder_ where I will keep the main :ref:`Python modules<what is a module?>` separate from the other files_

  .. code-block:: python
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line.

* I use the `mv program`_ to move``main.py`` to the ``src`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    mv main.py src/main.py

  the terminal_ goes back to the command line.

* I make a child folder_ to keep the tests separate from the other files_

  .. code-block:: python
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line.

* I use touch_ to add an empty file_ to the ``tests`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    touch tests/module_not_found_error.py

  the terminal_ goes back to the command line.

* I open ``module_not_found_error.py`` from the ``tests`` folder_

  .. tip::

    I can open a file_ from the terminal_ with :kbd:`ctrl` (Windows_/Linux_) or :kbd:`command` (MacOS_) on the keyboard and a click with the mouse on the name of the file_

* I add the :ref:`first failing test<test_failure>` to ``module_not_found_error.py`` in the ``tests`` folder_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    assert False is True

* I use the `unittest module`_ to run tests

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ shows

  .. code-block:: python

    ------------------------------------------------------
    Ran 0 tests in 0.000s

    NO TESTS RAN

* I close ``module_not_found_error.py``

  .. danger:: if you do not close ``magic.py``, there will be 3 files in the ``tests`` folder after the next step (instead of 2), because the ``Auto Save`` feature (enabled earlier) will save the original file_ if it is still open after you change its name.

* I use the `mv program`_ to change the name of ``module_not_found_error.py`` in the ``tests`` folder_ to ``test_module_not_found_error.py``

  .. code-block:: python
    :emphasize-lines: 1-2

    mv tests/module_not_found_error.py \
    tests/test_module_not_found_error.py

  the terminal_ goes back to the command line.

  .. tip::

    The ``\`` + :kbd:`enter/return` allows me to write one long line on multiple lines in the terminal_. Without it I have to write everything as one line because the terminal_ runs whatever line I have written when I hit :kbd:`enter/return` on the keyboard.

* I try to run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ still shows ``NO TESTS RAN``.

* I make the ``tests`` directory_ a `Python package`_

  .. danger:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/__init__.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/__init__.py

  the terminal_ goes back to the command line.

* I try to run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

      File ".../pumping_python/module_not_found_error/tests/test_module_not_found_error.py",
        line 1, in <module>
        assert False is True
               ^^^^^^^^^^^^^
    AssertionError


    ------------------------------------------------------
    Ran 1 test in 0.001s

    FAILED (errors=1)

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``File ".../pumping_python/module_not_found_error/tests/test_module_not_found_error.py", line 1`` in the terminal_, and the `Integrated Development Environment (IDE)`_ opens the file_ with the cursor at the line where the failure happened.

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen, in ``test_module_not_found_error.py``

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

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the test passes. Time to test :ref:`modules<what is a module?>`

----

*********************************************************************************
test_module_not_found_error
*********************************************************************************

----

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

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ is my friend, and shows ModuleNotFoundError_

  .. code-block:: shell
    :emphasize-lines: 4

      File ".../pumping_python/module_not_found_error/tests/test_module_not_found_error.py",
        line 1, in <module>
        import src.module_00
    ModuleNotFoundError: No module named 'src.module_00'


    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    FAILED (errors=1)

  because when ``import src.module_00`` runs, Python_ tries to bring in an :ref:`object (everything in Python is an object)<what is a class?>` for the ``module_00.py`` file_ from the ``src`` folder_.

* I add ModuleNotFoundError_ to the list of :ref:`Exceptions<errors>` seen in ``test_module_not_found_error.py``

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

ModuleNotFoundError_ is raised when Python_ cannot find a module_ (a file that ends in ``.py``) with the name given in an `import statement`_


----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I go back to the terminal_
* I use the `mv program`_ to change the name of ``main.py`` in the ``src`` folder_ to ``module_00.py``

  .. code-block:: python
    :emphasize-lines: 1

    mv src/main.py src/module_00.py

  the terminal_ goes back to the command line

* I run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  - the test passes because when ``import src.module_00`` runs, Python_ brings in an :ref:`object<what is a class?>` for the ``module_00.py`` file_ from the ``src`` folder_ so I can use it in ``test_module_not_found_error.py``
  - the terminal_ shows ``NO TESTS RAN`` which is confusing because the only way I know the test passed, is because I saw it fail

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an `import statement`_ for ``src.module_01`` to ``test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import src.module_00
    import src.module_01


    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError

* I run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_01'

* I make a new file_ named ``module_01.py`` in the ``src`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    touch src/module_01.py

  the terminal_ goes back to the command line.

* I run the test

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the test passes.

* I add an `import statement`_ for ``src.module_02`` to ``test_module_not_found_error.py``

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

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_02'

* I make a new file_ named ``module_02.py`` in the ``src`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    touch src/module_02.py

  the terminal_ goes back to the command line.

* I run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the test passes.

* I add an `import statement`_ for ``src.module_03`` to ``test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

    import src.module_00
    import src.module_01
    import src.module_02
    import src.module_03


    # Exceptions seen

* I go to the terminal_ to run the test

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_03'

* I make a new file_ named ``module_03.py`` in the ``src`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    touch src/module_03.py

  the terminal_ goes back to the command line.

* I run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the test passes.

* I add an `import statement`_ for ``src.module_04`` to ``test_module_not_found_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

    import src.module_00
    import src.module_01
    import src.module_02
    import src.module_04


    # Exceptions seen

* I go to the terminal_ to run the test

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_04'

* I make a new file_ named ``module_04.py`` in the ``src`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    touch src/module_04.py

  the terminal_ goes back to the command line.

* I run the test again

  .. code-block:: python
    :emphasize-lines: 1

    python3 -m unittest

  the test passes.

* I continue with another `import statement`_ in ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_module_not_found_error(self):
            import src.module_00
            import src.module_01
            import src.module_02

  the terminal_ is my friend, and shows ModuleNotFoundError_

  .. code-block:: shell

    ModuleNotFoundError: No module called 'src.module_02'

* I add ``module_02.py`` to the ``src`` folder and the test is green again, I close the file

* I add another `import statement`_ in ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5

        def test_module_not_found_error(self):
            import src.module_00
            import src.module_01
            import src.module_02
            import src.module_03

  the terminal_ is my friend, and shows

  .. code-block:: shell

    ModuleNotFoundError: No module called 'src.module_03'

* I add the file_ to the ``src`` folder_ and the test passes, I close the file_

* I add an `import statement`_ to ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2

            import src.module_03
            import src.module_04


    # Exceptions seen

  the terminal_ is my friend, and shows ModuleNotFoundError_

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_04'

* I add ``module_04.py`` to the ``src`` folder_, the test passes and I close the file_

* I add another `import statement`_ to ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2

            import src.module_04
            import src.module_05


    # Exceptions seen

  the terminal_ is my friend, and shows ModuleNotFoundError_

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_05'

* I add the file_ to the ``src`` folder_, the test passes and I close the file_

* another `import statement`_ in ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2

            import src.module_05
            import src.module_06


    # Exceptions seen

  the terminal_ is my friend, and shows ModuleNotFoundError_

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_06'

* I add ``module_06.py`` to the ``src`` folder_, the test passes, and I close the file_

* I add an `import statement`_ in ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

            import src.module_06
            import src.module_07


    # Exceptions seen

  the terminal_ is my friend, and shows ModuleNotFoundError_

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_07'

* I add the :ref:`module<what is a module?>` to the ``src`` folder_, the test passes and I close the file_

* I add an `import statement`_ to ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

            import src.module_07
            import src.module_08


    # Exceptions seen

  the test passes.

* I add ``module_08.py`` to the ``src`` folder_, the test passes.

* I add the last `import statement`_ to ``test_module_not_found_error.py``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2

            import src.module_08
            import src.module_09


    # Exceptions seen

  the terminal_ is my friend, and shows ModuleNotFoundError_

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_09'

* I add the file_ to the ``src`` folder_ and the test passes.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_module_not_found_error.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

  * I `change directory`_ to the parent of ``module_not_found_error``

    .. code-block:: python
      :emphasize-lines: 1

      cd ..

    the terminal_ is my friend, and shows

    .. code-block:: python

      ...\pumping_python

    I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I ran a test for ModuleNotFoundError_ to practice making :ref:`Python modules<what is a module?>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<ModuleNotFoundError: test>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have gone through a lot of information and know

* :ref:`how to make a Python test driven development environment manually<how to make a Python test driven development environment>`
* :ref:`what causes AssertionError?`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<list comprehensions>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`what you can do with dictionaries<dictionaries>`
* :ref:`what you can do with classes<what is a class?>`
* :ref:`how to raise ModuleNotFoundError<what is a module?>`

:ref:`Are you ready for a review, How many questions do you think you can answer?<pumping python review>`

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