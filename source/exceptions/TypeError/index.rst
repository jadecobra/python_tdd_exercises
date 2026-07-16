.. meta::
  :description: What causes TypeError when calling Python functions? TDD tutorial in the type_error project (uv init, tests/test_type_error.py, uv run pytest-watcher . --now): match the call to the function definition (signature). Deliberately raise TypeError with wrong positional count ("takes 0 positional arguments but 1 was given", "missing 1 required positional argument: 'the_input'", "takes 2 positional arguments but 3 were given"), wrong keyword names ("got an unexpected keyword argument 'argument_0'. Did you mean 'argument'?"), and double-binding ("got multiple values for argument 'argument'"). Three tests: test_type_error_w_positional_arguments, test_type_error_w_keyword_arguments, test_type_error_w_args_and_kwargs. Nested defs are moved to module level so multiple tests can call the same functions; final snapshot only shows correct calls (the pedagogical problem that later separation/assertRaises work addresses). Side-effect NameError when a function name is not defined yet; initial AssertionError from test_failure. Jacob Itegboje Pumping Python TDD series.
  :keywords: Jacob Itegboje, Pumping Python, what causes TypeError, python TypeError function call, TypeError missing required positional argument, TypeError takes positional arguments but were given, TypeError got an unexpected keyword argument, TypeError Did you mean, TypeError got multiple values for argument, match function signature definition call, positional vs keyword arguments, test_type_error_w_positional_arguments, test_type_error_w_keyword_arguments, test_type_error_w_args_and_kwargs, NameError name is not defined, AssertionError True is not false, uv init type_error, uv run pytest-watcher . --now, red green refactor TypeError, remove the commented lines, nested function locals TypeError, module level functions for shared calls, how to call a function with input, python exceptions TDD tutorial

.. include:: ../../links.rst

.. _TypeError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError

#################################################################################
what causes TypeError?
#################################################################################

----

TypeError_ happens when an :ref:`object (everything in Python is an object)<everything is an object>` is used in a way that it should not be.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/type_error/tests/test_type_error.py
  :language: python
  :linenos:

*********************************************************************************
questions about TypeError
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`what causes TypeError?`
* :ref:`what happens when I call a function and do not send the right number of inputs?<test_type_error_w_positional_arguments>`
* :ref:`what happens when I call a function and do not use the right names?<test_type_error_w_keyword_arguments>`
* :ref:`what happens when I call a function with multiple values for the same argument?<test_type_error_w_args_and_kwargs>`

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``type_error``
* I open a terminal_
* I `change directory`_ to the ``type_error`` folder_ in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd type_error

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: type_error

  there is no folder_ with the name ``type_error`` in this folder_.

* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init type_error

  the terminal_ shows

  .. code-block:: shell

    Initialized project `type-error`
    at `.../pumping_python/type_error`

  then goes back to the command line.

* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd type_error

  the terminal_ shows I am in the ``type_error`` folder_

  .. code-block:: python

    .../pumping_python/type_error

* I `make a directory`_ for the tests

  .. code-block:: python
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

* I use the `mv program`_ to change the name of ``main.py`` to ``test_type_error.py`` and move it to the ``tests`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        mv main.py tests/test_type_error.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        Move-Item main.py tests/test_type_error.py

  the terminal_ goes back to the command line.

* I open ``test_type_error.py``

* I delete the text in the file_ then add :ref:`the first failing test<test_failure>` to ``test_type_error.py``

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

    git commit --all --message 'setup project'

  the terminal_ shows

  .. code-block:: python

    [main (root-commit) a0b12c3] setup project
     8 files changed, X insertions(+)
     create mode 100644 .gitignore
     create mode 100644 .python-version
     create mode 100644 README.md
     create mode 100644 pyproject.toml
     create mode 100644 requirements.txt
     create mode 100644 tests/__init__.py
     create mode 100644 tests/test_type_error.py
     create mode 100644 uv.lock

  then goes back to the command line.

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 5, 7

    ========================== ERRORS ==========================
    ______ ERROR collecting tests/test_type_error.py ______
    tests/test_type_error.py:2: in <module>
        assert False is True
    E   assert False is True
    ================= short test summary info ==================
    ERROR tests/test_type_error.py - assert False is True
    !!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!
    ===================== 1 error in L.MNs =====================

  because :ref:`False<test_what_is_false>` is NOT :ref:`True<test_what_is_true>`.

  .. admonition:: if the terminal_ does not show the same error, then check if

    * your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    and try ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_type_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6
    :emphasize-text: AssertionError

    def test_failure():
        assert False is True


    # Exceptions seen
    # AssertionError

* I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def test_failure():
        # assert False is True
        assert True is True


    # Exceptions seen
    # AssertionError

  the test passes.

----

*********************************************************************************
test_type_error_w_positional_arguments
*********************************************************************************

:ref:`TypeError<what causes TypeError?>` happens when I :ref:`call a function<how to call a function with input>` in a way that is different from its :ref:`signature<how to make a function that takes input>`. I have to match the number of arguments in the :ref:`function definition<how to make a function that takes input>` when I :ref:`call the function<how to call a function with input>` with :ref:`positional arguments<test_positional_arguments>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change ``test_failure`` to :ref:`test_type_error_w_positional_arguments`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def test_type_error_w_positional_arguments():
        function_00('a')


    # Exceptions seen
    # AssertionError

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_00' is not defined

  because there is nothing named ``function_00`` in ``test_type_error.py``.

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`definition for the function<how to make a function that takes input>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def test_type_error_w_positional_arguments():
        def function_00():
            return None

        function_00('a')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError:
        test_type_error_w_positional_arguments
            .<locals>.function_00()
        takes 0 positional arguments but 1 was given

  because

  - The :ref:`call<how to call a function with input>` to ``function_00`` which belongs to :ref:`test_type_error_w_positional_arguments` used one input (``'a'``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``function_00`` does not allow any inputs when it is called since the parentheses are empty.
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 4
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError

* I add a name in parentheses to the :ref:`function definition<how to make a function that takes input>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def test_type_error_w_positional_arguments():
        # def function_00():
        def function_00(the_input):
            return None

        function_00('a')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to ``function_01``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

        function_00('a')

        function_01('a', 'b')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_01' is not defined

  because there is nothing named ``function_01`` in ``test_type_error.py``.

* I add a :ref:`definition<how to make a function that takes input>` for ``function_01``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3-4

        function_00('a')

        def function_01(the_input):
            return None

        function_01('a', 'b')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError:
        test_type_error_w_positional_arguments
            .<locals>.function_01()
        takes 1 positional argument but 2 were given

  because

  - The :ref:`call<how to call a function with input>` to ``function_01`` which belongs to :ref:`test_type_error_w_positional_arguments` uses two :ref:`positional_arguments<test_positional_arguments>` (``'a'`` and ``'b'``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``function_01`` only allows one input.
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I change the name of the first input, then add another name in parentheses so that :ref:`the call to the function<how to call a function with input>` and its :ref:`definition<how to make a function that takes input>` match

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3-4

        function_00('a')

        # def function_01(the_input):
        def function_01(first, second):
            return None

        function_01('a', 'b')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_02``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3

        function_01('a', 'b')

        function_02('a', 'b', 'c')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_02' is not defined

  because there is nothing named ``function_02`` in ``test_type_error.py``.

* I add a :ref:`definition<how to make a function that takes input>` for ``function_02``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3-4

        function_01('a', 'b')

        def function_02(first, second):
            return None

        function_02('a', 'b', 'c')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError:
        test_type_error_w_positional_arguments
            .<locals>.function_02()
        takes 2 positional arguments but 3 were given

  because

  - The :ref:`call<how to call a function with input>` to ``function_02`` which belongs to :ref:`test_type_error_w_positional_arguments` uses three :ref:`positional arguments<test_positional_arguments>` (``'a'``, ``'b'`` and ``'c'``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``function_02`` only allows two inputs.
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I add a third name in parentheses so that :ref:`the call<how to call a function with input>` to ``function_02`` and its :ref:`definition<how to make a function that takes input>` match

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3-4

        function_01('a', 'b')

        # def function_02(first, second):
        def function_02(first, second, third):
            return None

        function_02('a', 'b', 'c')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_03``

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 3

        function_02('a', 'b', 'c')

        function_03('a', 'b', 'c', 'd')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_03' is not defined

  because there is nothing named ``function_03`` in ``test_type_error.py``.

* I add a :ref:`definition<how to make a function that takes input>` for ``function_03``

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 3-4

        function_02('a', 'b', 'c')

        def function_03(first, second, third):
            return None

        function_03('a', 'b', 'c', 'd')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError:
        test_type_error_w_positional_arguments
            .<locals>.function_03()
        takes 3 positional arguments but 4 were given

  because

  - The :ref:`call<how to call a function with input>` to ``function_03`` which belongs to :ref:`test_type_error_w_positional_arguments` uses four :ref:`positional arguments<test_positional_arguments>` (``'a'``, ``'b'``, ``'c'``, ``'d'``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``function_03`` only allows three inputs.
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I add a fourth name in parentheses so that :ref:`the call<how to call a function with input>` to ``function_03`` and its :ref:`definition<how to make a function that takes input>` match

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 3-4

        function_02('a', 'b', 'c')

        # def function_03(first, second, third):
        def function_03(first, second, third, fourth):
            return None

        function_03('a', 'b', 'c', 'd')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def test_type_error_w_positional_arguments():
        def function_00(the_input):
            return None

        function_00('a')

  .. code-block:: python
    :lineno-start: 7

        def function_01(first, second):
            return None

        function_01('a', 'b')

  .. code-block:: python
    :lineno-start: 12

        def function_02(first, second, third):
            return None

        function_02('a', 'b', 'c')

  .. code-block:: python
    :lineno-start: 17

        def function_03(first, second, third, fourth):
            return None

        function_03('a', 'b', 'c', 'd')


    # Exceptions seen

* I open a new terminal_ then change directories to ``type_error``

  .. code-block:: python
    :emphasize-lines: 1

    cd type_error

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_type_error_w_positional_arguments'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I have to call a function with the same number of inputs that are in its definition<test_type_error_w_positional_arguments>`.

----

*************************************************************************************
test_type_error_w_keyword_arguments
*************************************************************************************

:ref:`TypeError<what causes TypeError?>` happens when I :ref:`call a function<how to call a function with input>` in a way that is different from its :ref:`signature<how to make a function that takes input>`. I have to match the names of arguments in the :ref:`function definition<how to make a function that takes input>` when I :ref:`call the function<how to call a function with input>` with :ref:`keyword arguments<test_keyword_arguments>`.


----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with a call to ``function_04`` with a :ref:`keyword argument<test_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 4-5

        function_03('a', 'b', 'c', 'd')


    def test_type_error_w_keyword_arguments():
        function_04(argument='value')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_04' is not defined

  because there is nothing named ``function_04`` in ``test_type_error.py``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`definition<how to make a function that takes input>` for ``function_04``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 2-3

    def test_type_error_w_keyword_arguments():
        def function_04():
            return None

        function_04(argument='value')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_type_error_w_keyword_arguments
            .<locals>.function_04()
            got an unexpected keyword argument 'argument'

  because

  - The :ref:`call<how to call a function with input>` to ``function_04`` which belongs to :ref:`test_type_error_w_keyword_arguments` uses a :ref:`keyword argument<test_keyword_arguments>` (``argument='value'``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``function_04`` does not allow any inputs since the parentheses are empty.
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I add ``argument`` in the parentheses so that :ref:`the call<how to call a function with input>` to ``function_04`` and its :ref:`definition<how to make a function that takes input>` match

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 2-3

    def test_type_error_w_keyword_arguments():
        # def function_04():
        def function_04(argument):
            return None

        function_04(argument='value')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to ``function_05`` with :ref:`keyword arguments<test_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3-6

        function_04(argument='value')

        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_05' is not defined

* I add a :ref:`definition<how to make a function that takes input>` for ``function_05``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3-4

        function_04(argument='value')

        def function_05(argument):
            return None

        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError:
        test_type_error_w_keyword_arguments
            .<locals>.function_05()
        got an unexpected keyword argument 'argument_0'.
        Did you mean 'argument'?

  because

  - The :ref:`call<how to call a function with input>` to ``function_05`` which belongs to :ref:`test_type_error_w_keyword_arguments` uses :ref:`keyword arguments<test_keyword_arguments>` (``argument_0='value1'`` and ``argument_1=(0, 1, 2, 'n')``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``function_05`` only allows one input with the name ``argument``.
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I change the name of the input to match :ref:`the call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3-4

        function_04(argument='value')

        # def function_05(argument):
        def function_05(argument_0):
            return None

        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )


    # Exceptions seen

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError:
        test_type_error_w_keyword_arguments
            .<locals>.function_05()
        got an unexpected keyword argument 'argument_1'.
        Did you mean 'argument_0'?

* I add ``argument_0`` to the parentheses so that :ref:`the call<how to call a function with input>` to ``function_05`` and its :ref:`definition<how to make a function that takes input>` match

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4-5

        function_04(argument='value')

        # def function_05(argument):
        # def function_05(argument_0):
        def function_05(argument_0, argument_1):
            return None

        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_06`` with :ref:`keyword arguments<test_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 6-10

        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )

        function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_06' is not defined

* I add a :ref:`definition<how to make a function that takes input>` for ``function_06``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 6-7

        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )

        def function_06(argument_0, argument_1):
            return None

        function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError:
        test_type_error_w_keyword_arguments
            .<locals>.function_06()
        got an unexpected keyword argument 'argument_2'.
        Did you mean 'argument_0'?

  because

  - The :ref:`call<how to call a function with input>` to ``function_06`` which belongs to :ref:`test_type_error_w_keyword_arguments` uses :ref:`keyword arguments<test_keyword_arguments>` (``argument_0='value1'``, ``argument_1=(0, 1, 2, 'n')`` and ``argument_2=[0, 1, 2, 'n']``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``function_06`` only allows two inputs.
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I add ``argument_2`` to the parentheses so that :ref:`the call<how to call a function with input>` to ``function_06`` and its :ref:`definition<how to make a function that takes input>` match

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 6-7

        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )

        # def function_06(argument_0, argument_1):
        def function_06(argument_0, argument_1, argument_2):
            return None

        function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_07`` with :ref:`keyword arguments<test_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 7-12

        function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )

        function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_07' is not defined

* I add a :ref:`definition<how to make a function that takes input>` for ``function_07``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 7-11

        function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )

        def function_07(
            argument_0, argument_1,
            argument_2
        ):
            return None

        function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError:
        test_type_error_w_keyword_arguments
            .<locals>.function_07()
        got an unexpected keyword argument 'argument_n'.
        Did you mean 'argument_0'?

  because

  - The :ref:`call<how to call a function with input>` to ``function_07`` which belongs to :ref:`test_type_error_w_keyword_arguments` uses :ref:`keyword arguments<test_keyword_arguments>` (``argument_0=(0, 1, 2, 'n')``, ``argument_1=[0, 1, 2, 'n']``, ``argument_2={0, 1, 2, 'n'}`` and ``argument_n={'key': 'value'}``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``function_07`` only allows three inputs.
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I add ``argument_n`` to the parentheses so that :ref:`the call<how to call a function with input>` to ``function_07`` and its :ref:`definition<how to make a function that takes input>` match

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 9-10

        function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )

        def function_07(
            argument_0, argument_1,
            # argument_2
            argument_2, argument_n,
        ):
            return None

        function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 23

    def test_type_error_w_keyword_arguments():
        def function_04(argument):
            return None

        function_04(argument='value')

        def function_05(argument_0, argument_1):
            return None

        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )

        def function_06(argument_0, argument_1, argument_2):
            return None

        function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )

        def function_07(
            argument_0, argument_1,
            argument_2, argument_n,
        ):
            return None

        function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )


    # Exceptions seen

* I open a new terminal_ then change directories to ``type_error``

  .. code-block:: python
    :emphasize-lines: 1

    cd type_error

  the terminal_ shows I am in the ``type_error`` folder_

  .. code-block:: python

    .../pumping_python/type_error

* I add a git_ commit message in the other terminal

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_type_error_w_keyword_arguments'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I have to call a function with the same names that are in its definition<test_type_error_w_keyword_arguments>`.

----

*************************************************************************************
test_type_error_w_args_and_kwargs
*************************************************************************************

:ref:`TypeError<what causes TypeError?>` happens when I :ref:`call a function<how to call a function with input>` in a way that is different from its :ref:`signature<how to make a function that takes input>`. I cannot give two values for the same argument in the :ref:`function definition<how to make a function that takes input>` when I :ref:`call the function<how to call a function with input>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with a call to ``function_08`` with a :ref:`positional and keyword argument<test_args_and_kwargs>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 9-10

        function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )


    def test_type_error_w_args_and_kwargs():
        function_08('positional', argument='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_08' is not defined

  because there is no definition for ``function_08`` in the file_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function definition<how to make a function that takes input>` for ``function_08``

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2-3

    def test_type_error_w_args_and_kwargs():
        def function_08(argument):
            return None

        function_08('positional', argument='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_type_error_w_args_and_kwargs
            .<locals>.function_08()
        got multiple values for argument 'argument'

  because

  - The :ref:`call<how to call a function with input>` to ``function_08`` which belongs to :ref:`test_type_error_w_args_and_kwargs` uses :ref:`positional and keyword arguments<test_args_and_kwargs>` (``'positional'`` and ``argument='keyword'``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``function_08`` takes one argument (``argument``). How does Python_ know which value to use for ``argument`` if I use the :ref:`position<test_positional_arguments>` and the :ref:`name<test_keyword_arguments>`?
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I add another name to the parentheses

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2-3

    def test_type_error_w_args_and_kwargs():
        # def function_08(argument):
        def function_08(argument, name):
            return None

        function_08('positional', argument='keyword')


    # Exceptions seen

  the terminal_ still shows :ref:`TypeError<what causes TypeError?>` because the :ref:`call<how to call a function with input>` gives ``'positional'`` as the value for the first argument which is ``argument`` in the :ref:`definition<how to make a function that takes input>`, and it gives ``'keyword'`` as the value for ``argument`` as a :ref:`keyword argument<test_keyword_arguments>`.

* I change the order of the inputs

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 3-4

    def test_type_error_w_args_and_kwargs():
        # def function_08(argument):
        # def function_08(argument, name):
        def function_08(name, argument):
            return None

        function_08('positional', argument='keyword')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to ``function_08``

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 8

    def test_type_error_w_args_and_kwargs():
        # def function_08(argument):
        # def function_08(argument, name):
        def function_08(name, argument):
            return None

        function_08('positional', argument='keyword')
        function_08('positional', name='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_type_error_w_args_and_kwargs
            .<locals>.function_08()
        got multiple values for argument 'name'

  because

  - The :ref:`call<how to call a function with input>` to ``function_08`` which belongs to :ref:`test_type_error_w_args_and_kwargs` uses ``'positional'`` as the value for the first argument which is ``name`` in the :ref:`definition<how to make a function that takes input>`, and uses ``'keyword'`` as the value for ``name`` as a :ref:`keyword argument<test_keyword_arguments>`.
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``function_08`` takes two arguments (``name`` and ``argument``). How does Python_ know which value to use for ``name`` if I use the :ref:`position<test_positional_arguments>` and the :ref:`name<test_keyword_arguments>`?

* I use :ref:`keyword arguments<test_keyword_arguments>` in the :ref:`call<how to call a function with input>` to be clearer

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 8-9

    def test_type_error_w_args_and_kwargs():
        # def function_08(argument):
        # def function_08(argument, name):
        def function_08(name, argument):
            return None

        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_01`` with a :ref:`positional and keyword argument<test_args_and_kwargs>`

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 7

    def test_type_error_w_args_and_kwargs():
        # def function_08(argument):
        # def function_08(argument, name):
        def function_08(name, argument):
            return None

        function_01(1, first=0)
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_01' is not defined

  because ``function_01`` belongs to the :ref:`test_type_error_w_positional_arguments function<test_type_error_w_positional_arguments>` and I cannot reach it from outside.

* I move ``function_01`` out of :ref:`test_type_error_w_positional_arguments` so that it can be called from anywhere in the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2, 10

    def function_01(first, second):
        return None


    def test_type_error_w_positional_arguments():
        def function_00(the_input):
            return None

        function_00('a')
        function_01('a', 'b')

        def function_02(first, second, third):
            return None

        function_02('a', 'b', 'c')

        def function_03(first, second, third, fourth):
            return None

        function_03('a', 'b', 'c', 'd')


    def test_type_error_w_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_01() got
               multiple values for argument 'first'

  because the :ref:`call<how to call a function with input>` to ``function_01`` from :ref:`test_type_error_w_args_and_kwargs` uses ``1`` as the value for the first argument which is ``first`` in the :ref:`definition<how to make a function that takes input>`, and uses ``0`` as the value for ``first`` as a :ref:`keyword argument<test_keyword_arguments>`.

* I change the :ref:`call<how to call a function with input>` to only use :ref:`positional arguments<test_positional_arguments>` to make it clearer

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 7-8

    def test_type_error_w_args_and_kwargs():
        # def function_08(argument):
        # def function_08(argument, name):
        def function_08(name, argument):
            return None

        # function_01(1, first=0)
        function_01(1, 0)
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_02`` with arguments that are not clear

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 9

    def test_type_error_w_args_and_kwargs():
        # def function_08(argument):
        # def function_08(argument, name):
        def function_08(name, argument):
            return None

        # function_01(1, first=0)
        function_01(1, 0)
        function_02(False, first=None)
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_02' is not defined

  because ``function_02`` belongs to the :ref:`test_type_error_w_positional_arguments function<test_type_error_w_positional_arguments>` and I cannot reach it from outside.

* I move ``function_02`` out of :ref:`test_type_error_w_positional_arguments` so that it can be called from anywhere in the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6, 15

    def function_01(first, second):
        return None


    def function_02(first, second, third):
        return None


    def test_type_error_w_positional_arguments():
        def function_00(the_input):
            return None

        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')

        def function_03(first, second, third, fourth):
            return None

        function_03('a', 'b', 'c', 'd')


    def test_type_error_w_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_02() got
               multiple values for argument 'first'

  because the :ref:`call<how to call a function with input>` to ``function_02`` from :ref:`test_type_error_w_args_and_kwargs` uses ``False`` as the first :ref:`positional argument<test_positional_arguments>` which is named ``first`` in the :ref:`definition<how to make a function that takes input>`, and uses ``None`` as the value for ``first`` as a :ref:`keyword argument<test_keyword_arguments>`.

* I change the first value in the :ref:`call<how to call a function with input>` to a :ref:`keyword argument<test_keyword_arguments>` to make it clearer

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 9-10

    def test_type_error_w_args_and_kwargs():
        # def function_08(argument):
        # def function_08(argument, name):
        def function_08(name, argument):
            return None

        # function_01(1, first=0)
        function_01(1, 0)
        # function_02(False, first=None)
        function_02(second=False, first=None)
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_02() missing
               1 required positional argument: 'third'

  because

  - The :ref:`call<how to call a function with input>` to ``function_02`` from :ref:`test_type_error_w_args_and_kwargs` uses two arguments.
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``function_02`` takes three arguments (``first``, ``second`` and ``third``).

* I add a third argument to the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 10-11

    def test_type_error_w_args_and_kwargs():
        # def function_08(argument):
        # def function_08(argument, name):
        def function_08(name, argument):
            return None

        # function_01(1, first=0)
        function_01(1, 0)
        # function_02(False, first=None)
        # function_02(second=False, first=None)
        function_02(True, second=False, first=None)
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_02() got
               multiple values for argument 'first'

  because the :ref:`call<how to call a function with input>` to ``function_02`` from :ref:`test_type_error_w_args_and_kwargs` uses ``True`` as the first :ref:`positional argument<test_positional_arguments>` which is named ``first`` in the :ref:`definition<how to make a function that takes input>`, and uses ``None`` as the value for ``first`` as a :ref:`keyword argument<test_keyword_arguments>`.

* I change it to a :ref:`keyword argument<test_keyword_arguments>` to make it clearer

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 11-12

    def test_type_error_w_args_and_kwargs():
        # def function_08(argument):
        # def function_08(argument, name):
        def function_08(name, argument):
            return None

        # function_01(1, first=0)
        function_01(1, 0)
        # function_02(False, first=None)
        # function_02(second=False, first=None)
        # function_02(True, second=False, first=None)
        function_02(third=True, second=False, first=None)
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_03``

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 7-12

        # function_01(1, first=0)
        function_01(1, 0)
        # function_02(False, first=None)
        # function_02(second=False, first=None)
        # function_02(True, second=False, first=None)
        function_02(third=True, second=False, first=None)
        function_03(
            [0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_03' is not defined

  because ``function_03`` belongs to the :ref:`test_type_error_w_positional_arguments function<test_type_error_w_positional_arguments>` and I cannot reach it from outside.

* I move ``function_03`` out of :ref:`test_type_error_w_positional_arguments`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6, 16

    def function_02(first, second, third):
        return None


    def function_03(first, second, third, fourth):
        return None


    def test_type_error_w_positional_arguments():
        def function_00(the_input):
            return None

        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')


    def test_type_error_w_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_03() got
               multiple values for argument 'first'

  because the :ref:`call<how to call a function with input>` uses an argument in the first position and uses a :ref:`keyword argument<test_keyword_arguments>` with the name of the argument in the first position.

* I add a :ref:`keyword argument<test_keyword_arguments>` for the first value in the :ref:`call<how to call a function with input>` from :ref:`test_type_error_w_args_and_kwargs` to make it clearer

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 8-9

        # function_01(1, first=0)
        function_01(1, 0)
        # function_02(False, first=None)
        # function_02(second=False, first=None)
        # function_02(True, second=False, first=None)
        function_02(third=True, second=False, first=None)
        function_03(
            # [0, 1, 2, 'n'],
            second=[0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_07``

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 15-20

        # function_01(1, first=0)
        function_01(1, 0)
        # function_02(False, first=None)
        # function_02(second=False, first=None)
        # function_02(True, second=False, first=None)
        function_02(third=True, second=False, first=None)
        function_03(
            # [0, 1, 2, 'n'],
            second=[0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )

        function_07(
            {0, 1, 2, 'n'},
            {'key': 'value'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_07' is not defined

  because ``function_07`` belongs to the :ref:`test_type_error_w_keyword_arguments function<test_type_error_w_keyword_arguments>` and I cannot reach it from outside.

* I move ``function_07`` out of :ref:`test_type_error_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-9, 43-48

    def function_03(first, second, third, fourth):
        return None


    def function_07(
        argument_0, argument_1,
        argument_2, argument_n,
    ):
        return None


    def test_type_error_w_positional_arguments():
        def function_00(the_input):
            return None

        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')


    def test_type_error_w_keyword_arguments():
        def function_04(argument):
            return None

        function_04(argument='value')

        def function_05(argument_0, argument_1):
            return None

        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )

        def function_06(argument_0, argument_1, argument_2):
            return None

        function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )
        function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )

    def test_type_error_w_args_and_kwargs():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_07() got
               multiple values for argument 'argument_0'

  because

  - The :ref:`call<how to call a function with input>` to ``function_07`` from :ref:`test_type_error_w_args_and_kwargs` uses an argument in the first position and uses a :ref:`keyword argument<test_keyword_arguments>` with the name of the argument in the first position.
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``function_07`` takes four arguments. How does Python_ know which value to use for ``argument_0`` if I use both the :ref:`position<test_positional_arguments>` and the :ref:`name<test_keyword_arguments>` of the argument?
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I change the :ref:`call<how to call a function with input>` to use a :ref:`keyword argument<test_keyword_arguments>`, then change its position

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 2, 4

        function_07(
            # {0, 1, 2, 'n'},
            {'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the terminal_ still shows :ref:`TypeError<what causes TypeError?>` because the :ref:`call<how to call a function with input>` uses an argument in the first position and uses a :ref:`keyword argument<test_keyword_arguments>` with the name of the argument in the first position.

* I use a :ref:`keyword argument<test_keyword_arguments>` to make it clearer

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 3-4

        function_07(
            # {0, 1, 2, 'n'},
            # {'key': 'value'},
            argument_4={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: function_07() got
               an unexpected keyword argument 'argument_4'.
               Did you mean 'argument_0'?

  because

  - The :ref:`call<how to call a function with input>` to ``function_07`` from :ref:`test_type_error_w_args_and_kwargs` uses a :ref:`keyword argument<test_keyword_arguments>` that is not in the :ref:`function definition (signature)<how to make a function that takes input>`.
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I change the :ref:`keyword argument<test_keyword_arguments>` to match the :ref:`function definition<how to make a function that takes input>`

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 4-5

        function_07(
            # {0, 1, 2, 'n'},
            # {'key': 'value'},
            # argument_4={'key': 'value'},
            argument_n={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function>` to ``function_00``

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 7

    def test_type_error_w_args_and_kwargs():
        # def function_08(argument):
        # def function_08(argument, name):
        def function_08(name, argument):
            return None

        function_00()
        # function_01(1, first=0)
        function_01(1, 0)
        # function_02(False, first=None)
        # function_02(second=False, first=None)
        # function_02(True, second=False, first=None)
        function_02(third=True, second=False, first=None)
        function_03(
            # [0, 1, 2, 'n'],
            second=[0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_00' is not defined

  because ``function_00`` belongs to the :ref:`test_type_error_w_positional_arguments function<test_type_error_w_positional_arguments>` and I cannot reach it from outside.

* I move ``function_00`` out of :ref:`test_type_error_w_positional_arguments`

  .. code-block:: python
    :linenos: 1-2

    def function_00(the_input):
        return None


    def function_01(first, second):
        return None


    def function_02(first, second, third):
        return None


    def function_03(first, second, third, fourth):
        return None


    def function_07(
        argument_0, argument_1,
        argument_2, argument_n,
    ):
        return None


    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')


    def test_type_error_w_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_00() missing
               1 required positional argument: 'the_input'

  because the :ref:`function definition<how to make a function that takes input>` requires :ref:`calls<how to call a function with input>` with one input and it got :ref:`called<how to call a function with input>` with zero inputs.

* I change the :ref:`call<how to call a function with input>` to match the :ref:`signature<how to make a function that takes input>`

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 7-8

    def test_type_error_w_args_and_kwargs():
        # def function_08(argument):
        # def function_08(argument, name):
        def function_08(name, argument):
            return None

        # function_00()
        function_00('argument')
        # function_01(1, first=0)
        function_01(1, 0)
        # function_02(False, first=None)
        # function_02(second=False, first=None)
        # function_02(True, second=False, first=None)
        function_02(third=True, second=False, first=None)
        function_03(
            # [0, 1, 2, 'n'],
            second=[0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_04``

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 9

        function_02(third=True, second=False, first=None)
        function_03(
            # [0, 1, 2, 'n'],
            second=[0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )
        function_04('value1', 'value2')

        function_07(
            # {0, 1, 2, 'n'},
            # {'key': 'value'},
            # argument_4={'key': 'value'},
            argument_n={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_04' is not defined

  because ``function_04`` belongs to the :ref:`test_type_error_w_keyword_arguments function<test_type_error_w_keyword_arguments>` and I cannot reach it from outside.

* I move ``function_04`` out of :ref:`test_type_error_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5-6

    def function_03(first, second, third, fourth):
        return None


    def function_04(argument):
        return None


    def function_07(
        argument_0, argument_1,
        argument_2, argument_n,
    ):
        return None


    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')


    def test_type_error_w_keyword_arguments():
        function_04(argument='value')

        def function_05(argument_0, argument_1):
            return None

        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )

        def function_06(argument_0, argument_1, argument_2):
            return None

        function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )
        function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )

    def test_type_error_w_args_and_kwargs():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_04() takes
               1 positional argument but 2 were given

  because the :ref:`definition<how to make a function that takes input>` only allows it take one input, and it got :ref:`called<how to call a function with input>` with two.

* I change the :ref:`call<how to call a function with input>` to match the :ref:`signature<how to make a function that takes input>`

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 9-10

        function_02(third=True, second=False, first=None)
        function_03(
            # [0, 1, 2, 'n'],
            second=[0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )
        # function_04('value1', 'value2')
        function_04('value')

        function_07(
            # {0, 1, 2, 'n'},
            # {'key': 'value'},
            # argument_4={'key': 'value'},
            argument_n={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_05``

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 11

        function_02(third=True, second=False, first=None)
        function_03(
            # [0, 1, 2, 'n'],
            second=[0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )
        # function_04('value1', 'value2')
        function_04('value')
        function_05((0, 1, 2, 'n'))

        function_07(
            # {0, 1, 2, 'n'},
            # {'key': 'value'},
            # argument_4={'key': 'value'},
            argument_n={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_05' is not defined

* I move ``function_05`` out of :ref:`test_type_error_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5-6, 25-28

    def function_04(argument):
        return None


    def function_05(argument_0, argument_1):
        return None


    def function_07(
        argument_0, argument_1,
        argument_2, argument_n,
    ):
        return None


    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')


    def test_type_error_w_keyword_arguments():
        function_04(argument='value')
        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )

        def function_06(argument_0, argument_1, argument_2):
            return None

        function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )
        function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )

    def test_type_error_w_args_and_kwargs():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_05() missing
               1 required positional argument: 'argument_1'

  because the :ref:`definition<how to make a function that takes input>` expects a :ref:`call<how to call a function with input>` with two inputs and only got one input.

* I change the :ref:`call<how to call a function with input>` to match the :ref:`signature<how to make a function that takes input>`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 3-7

        # function_04('value1', 'value2')
        function_04('value')
        # function_05((0, 1, 2, 'n'))
        function_05(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
        )

        function_07(
            # {0, 1, 2, 'n'},
            # {'key': 'value'},
            # argument_4={'key': 'value'},
            argument_n={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_06``

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 8-13

        # function_04('value1', 'value2')
        function_04('value')
        # function_05((0, 1, 2, 'n'))
        function_05(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
        )
        function_06(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )

        function_07(
            # {0, 1, 2, 'n'},
            # {'key': 'value'},
            # argument_4={'key': 'value'},
            argument_n={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_06' is not defined

  because ``function_06`` belongs to the :ref:`test_type_error_w_keyword_arguments function<test_type_error_w_keyword_arguments>` and I cannot reach it from outside.

* I move ``function_06`` out of :ref:`test_type_error_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-6, 29-33

    def function_05(argument_0, argument_1):
        return None


    def function_06(argument_0, argument_1, argument_2):
        return None


    def function_07(
        argument_0, argument_1,
        argument_2, argument_n,
    ):
        return None


    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')


    def test_type_error_w_keyword_arguments():
        function_04(argument='value')
        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )
        function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )
        function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )

    def test_type_error_w_args_and_kwargs():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: function_06() got
               an unexpected keyword argument 'argument_n'.
               Did you mean 'argument_0'?

  because the :ref:`function got called<how to call a function with input>` with a :ref:`name (keyword)<test_keyword_arguments>` that is not in its :ref:`definition<how to make a function that takes input>`

* I remove ``argument_n={'key': 'value'}`` from the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 12

        # function_04('value1', 'value2')
        function_04('value')
        # function_05((0, 1, 2, 'n'))
        function_05(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
        )
        function_06(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            # argument_n={'key': 'value'},
        )

        function_07(
            # {0, 1, 2, 'n'},
            # {'key': 'value'},
            # argument_4={'key': 'value'},
            argument_n={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        function_08('positional', argument='keyword')
        # function_08('positional', name='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I remove the commented lines from :ref:`test_type_error_w_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 57

    def test_type_error_w_args_and_kwargs():
        def function_08(name, argument):
            return None

        function_00('argument')
        function_01(1, 0)
        function_02(third=True, second=False, first=None)
        function_03(
            second=[0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )
        function_04('value')
        function_05(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
        )
        function_06(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
        )
        function_07(
            argument_n={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        function_08('positional', argument='keyword')
        function_08(argument='positional', name='keyword')


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_type_error_w_args_and_kwargs'

----

* I add a :ref:`call<how to call a function with input>` to ``function_03`` from :ref:`test_type_error_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2-6

    def test_type_error_w_keyword_arguments():
        function_03(
            first=None,
            second=False,
            third=True,
        )
        function_04(argument='value')
        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )
        function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )
        function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )

    def test_type_error_w_args_and_kwargs():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_03() missing
               1 required positional argument: 'fourth'

  because the :ref:`signature<how to make a function that takes input>` only allows :ref:`calls<how to call a function with input>` with four inputs, and it got :ref:`called<how to call a function with input>` with three.

* I add ``fourth`` with a value to the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 6

    def test_type_error_w_keyword_arguments():
        function_03(
            first=None,
            second=False,
            third=True,
            fourth=4,
        )
        function_04(argument='value')

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_02`` from :ref:`test_type_error_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2-7

    def test_type_error_w_keyword_arguments():
        function_02(
            fourth=4.0,
            third=(0, 1, 2, 'n'),
            second=[0, 1, 2, 'n'],
            first={0, 1, 2, 'n'},
        )
        function_03(
            first=None,
            second=False,
            third=True,
            fourth=4,
        )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_02() got an unexpected keyword argument 'fourth'

  because the :ref:`signature<how to make a function that takes input>` only allows :ref:`calls<how to call a function with input>` with three inputs, and it got :ref:`called<how to call a function with input>` with four.

* I remove the unexpected :ref:`keyword argument<test_keyword_arguments>` from the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3

    def test_type_error_w_keyword_arguments():
        function_02(
            # fourth=4.0,
            third=(0, 1, 2, 'n'),
            second=[0, 1, 2, 'n'],
            first={0, 1, 2, 'n'},
        )
        function_03(
            first=None,
            second=False,
            third=True,
            fourth=4,
        )

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_01`` from :ref:`test_type_error_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2-4

    def test_type_error_w_keyword_arguments():
        function_01(
            second={'key': 'value'},
        )
        function_02(
            # fourth=4.0,
            third=(0, 1, 2, 'n'),
            second=[0, 1, 2, 'n'],
            first={0, 1, 2, 'n'},
        )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_01() missing
               1 required positional argument: 'first'

  because the :ref:`signature<how to make a function that takes input>` only allows :ref:`calls<how to call a function with input>` with two inputs, and it got :ref:`called<how to call a function with input>` with one.

* I change the :ref:`call<how to call a function with input>` to match the :ref:`signature<how to make a function that takes input>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3

    def test_type_error_w_keyword_arguments():
        function_01(
            first='first',
            second={'key': 'value'},
        )

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_00`` from :ref:`test_type_error_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2

    def test_type_error_w_keyword_arguments():
        function_00(second=1, first=0)
        function_01(
            first='first',
            second={'key': 'value'},
        )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_00() got
               an unexpected keyword argument 'second'

* I remove ``second`` from the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2-3

    def test_type_error_w_keyword_arguments():
        # function_00(second=1, first=0)
        function_00(first=0)
        function_01(
            first='first',
            second={'key': 'value'},
        )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_00() got
               an unexpected keyword argument 'first'

* I remove ``first`` from the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3-4

    def test_type_error_w_keyword_arguments():
        # function_00(second=1, first=0)
        # function_00(first=0)
        function_00()
        function_01(
            first='first',
            second={'key': 'value'},
        )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_00() missing
               1 required positional argument: 'the_input'

* I use the :ref:`name<test_keyword_arguments>` in the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3-4

    def test_type_error_w_keyword_arguments():
        # function_00(second=1, first=0)
        # function_00(first=0)
        # function_00()
        function_00(the_input=0)
        function_01(
            first='first',
            second={'key': 'value'},
        )

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I move the :ref:`call<how to call a function with input>` to ``function_08`` that uses :ref:`keyword arguments<test_keyword_arguments>` from :ref:`test_type_error_w_args_and_kwargs` to :ref:`test_type_error_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 7

        function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )
        function_08(argument='positional', name='keyword')


    def test_type_error_w_args_and_kwargs():
        def function_08(name, argument):
            return None

        function_00('argument')
        function_01(1, 0)
        function_02(third=True, second=False, first=None)
        function_03(
            second=[0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )
        function_04('value')
        function_05(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
        )
        function_06(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
        )
        function_07(
            argument_n={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        function_08('positional', argument='keyword')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'function_08' is not defined

* I move ``function_08`` out of :ref:`test_type_error_w_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 8-9

    def function_07(
        argument_0, argument_1,
        argument_2, argument_n,
    ):
        return None


    def function_08(name, argument):
        return None


    def test_type_error_w_positional_arguments():

  .. code-block:: python
    :lineno-start: 87

    def test_type_error_w_args_and_kwargs():
        function_00('argument')
        function_01(1, 0)
        function_02(third=True, second=False, first=None)
        function_03(
            second=[0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )
        function_04('value')
        function_05(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
        )
        function_06(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
        )
        function_07(
            argument_n={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        function_08('positional', argument='keyword')


    # Exceptions seen

  the test is green again.

* I remove the commented lines from :ref:`test_type_error_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 47

    def test_type_error_w_keyword_arguments():
        function_00(the_input=0)
        function_01(
            first='first',
            second={'key': 'value'},
        )
        function_02(
            third=(0, 1, 2, 'n'),
            second=[0, 1, 2, 'n'],
            first={0, 1, 2, 'n'},
        )
        function_03(
            first=None,
            second=False,
            third=True,
            fourth=4,
        )
        function_04(argument='value')
        function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )
        function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )
        function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )
        function_08(argument='positional', name='keyword')


    def test_type_error_w_args_and_kwargs():

* I add a :ref:`call<how to call a function with input>` to ``function_04`` from :ref:`test_type_error_w_positional_arguments`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 6

    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')
        function_04()


    def test_type_error_w_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_04() missing
               1 required positional argument: 'argument'

* I add a value to the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 6-7

    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')
        # function_04()
        function_04('a')


    def test_type_error_w_keyword_arguments():

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_05`` from :ref:`test_type_error_w_positional_arguments`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 8

    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')
        # function_04()
        function_04('a')
        function_05('a', 'b', 'c')


    def test_type_error_w_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_05() takes
               2 positional arguments but 3 were given

* I remove a value from the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 8-9

    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')
        # function_04()
        function_04('a')
        # function_05('a', 'b', 'c')
        function_05('a', 'b')


    def test_type_error_w_keyword_arguments():

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_06`` from :ref:`test_type_error_w_positional_arguments`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 10

    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')
        # function_04()
        function_04('a')
        # function_05('a', 'b', 'c')
        function_05('a', 'b')
        function_06('a', 'b')


    def test_type_error_w_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_06() missing
               1 required positional argument: 'argument_2'

* I add a value to the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 10-11

    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')
        # function_04()
        function_04('a')
        # function_05('a', 'b', 'c')
        function_05('a', 'b')
        # function_06('a', 'b')
        function_06('a', 'b', 'c')


    def test_type_error_w_keyword_arguments():

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_07`` from :ref:`test_type_error_w_positional_arguments`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 12

    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')
        # function_04()
        function_04('a')
        # function_05('a', 'b', 'c')
        function_05('a', 'b')
        # function_06('a', 'b')
        function_06('a', 'b', 'c')
        function_07('a', 'b', 'c', 'd', 'e')


    def test_type_error_w_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_07() takes
               4 positional arguments but 5 were given

* I remove a value from the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 12-13

    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')
        # function_04()
        function_04('a')
        # function_05('a', 'b', 'c')
        function_05('a', 'b')
        # function_06('a', 'b')
        function_06('a', 'b', 'c')
        # function_07('a', 'b', 'c', 'd', 'e')
        function_07('a', 'b', 'c', 'd')


    def test_type_error_w_keyword_arguments():

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I add a :ref:`call<how to call a function with input>` to ``function_08`` from :ref:`test_type_error_w_positional_arguments`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 14

    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')
        # function_04()
        function_04('a')
        # function_05('a', 'b', 'c')
        function_05('a', 'b')
        # function_06('a', 'b')
        function_06('a', 'b', 'c')
        # function_07('a', 'b', 'c', 'd', 'e')
        function_07('a', 'b', 'c', 'd')
        function_08('last')


    def test_type_error_w_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_08() missing
               1 required positional argument: 'argument'

* I add a value to the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 14-15

    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')
        # function_04()
        function_04('a')
        # function_05('a', 'b', 'c')
        function_05('a', 'b')
        # function_06('a', 'b')
        function_06('a', 'b', 'c')
        # function_07('a', 'b', 'c', 'd', 'e')
        function_07('a', 'b', 'c', 'd')
        # function_08('last')
        function_08('last', 'one')


    def test_type_error_w_keyword_arguments():

  the test passes because :ref:`the call to the function<how to call a function with input>` matches its :ref:`definition<how to make a function that takes input>`.

* I remove the commented lines from :ref:`test_type_error_w_positional_arguments`

  .. code-block:: python
    :lineno-start: 40

    def test_type_error_w_positional_arguments():
        function_00('a')
        function_01('a', 'b')
        function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')
        function_04('a')
        function_05('a', 'b')
        function_06('a', 'b', 'c')
        function_07('a', 'b', 'c', 'd')
        function_08('last', 'one')


    def test_type_error_w_keyword_arguments():

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit --all --message \
    'test with required and unexpected arguments'

:ref:`I have to call a function with the same number or names of arguments that are in its definition<test_type_error_w_args_and_kwargs>`.

----

*********************************************************************************
review
*********************************************************************************

I ran tests for :ref:`TypeError<what causes TypeError?>` with

* :ref:`positional arguments<test_type_error_w_positional_arguments>`
* :ref:`keyword arguments<test_type_error_w_keyword_arguments>`
* :ref:`positional and keyword arguments<test_type_error_w_args_and_kwargs>`

My problem with the tests is that they all show the correct way to call the :ref:`functions<what is a function?>` I made in the file_. If someone reads the file_ or runs it, there is no way for them to know how any of the :ref:`calls<how to call a function with input>` are related to :ref:`TypeError<what causes TypeError?>` unless they go through the process with me, there has to be a better way.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<TypeError: tests and solution>`

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

:ref:`Would you like to test using a function to make a string from input?<telephone>`

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