.. meta::
  :description: Learn Python functions with TDD: use def + pass, return, and explicit "return None". Discover that every function returns None by default (as if it has an invisible "return None"), that a return statement exits immediately (dead code after it never runs), and build constant functions that always return the exact same object. Practice bare "assert ... is None" and "is 'value'" inside tests; encounter real errors including "name 'w_pass' is not defined" (NameError), "TypeError: 'NoneType' object is not callable" when calling before defining, and AssertionError like "assert None is 0" or "assert 'the same thing' is None". Step-by-step RED/GREEN/REFACTOR with unittest and pytest-watcher. Part of Jacob Itegboje's Pumping Python series.
  :keywords: Jacob Itegboje, Pumping Python, python functions for beginners, learn functions with TDD, def pass return python, functions return None by default, return statement exits immediately, constant function python, return None invisible, bare assert is None, NameError name 'w_pass' is not defined, TypeError NoneType object is not callable, AssertionError assert None is 0, what does a python function return, test function syntax unittest, red green refactor functions, python TDD def keyword, how to make a function python, constant functions always return the same, uv pytest-watcher functions project

.. include:: ../links.rst

.. _function: https://docs.python.org/3/glossary.html#term-function
.. _functions: :ref:`function<what is a function?>`
.. _arguments: argument_
.. _return: https://docs.python.org/3/reference/simple_stmts.html#the-return-statement
.. _return statement: return_
.. _return statements: return_

#################################################################################
what is a function?
#################################################################################

A function_ is code that is callable_, this means I can write code to do something one time, and call the name for it to do that thing at a different time from when I write it.

functions_ can make code simpler, easier to read, test, reuse, maintain and improve - all the good things.

----

*********************************************************************************
how to make a function
*********************************************************************************

functions_ are made with

* the def_ keyword
* a name
* parentheses and a colon at the end
* the code that makes up the :ref:`function<what is a function?>` (its body) comes after the colon

.. code-block:: python

  def name_of_function():
      the body of the function
      ...

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/functions/test_functions.py
  :language: python
  :linenos:

*********************************************************************************
questions about functions
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`what is a function?<what is a function?>`
* :ref:`what do functions return by default?<test_making_a_function_w_return_none>`
* :ref:`what happens after a function returns?<test_what_happens_after_functions_return>`
* :ref:`what is a constant function?<test_constant_function>`

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``functions``
* I open a terminal_
* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init functions

  the terminal_ shows

  .. code-block:: shell

    Initialized project `functions`
    at `.../pumping_python/functions`

  then goes back to the command line.

* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd functions

  the terminal_ shows I am in the ``functions`` folder_

  .. code-block:: python

    .../pumping_python/functions

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

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/__init__.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/__init__.py

  the terminal_ goes back to the command line.

* I use the `mv program`_ to change the name of ``main.py`` to ``test_functions.py`` and move it to the ``tests`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        mv main.py tests/test_functions.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        Move-Item main.py tests/test_functions.py

  the terminal_ goes back to the command line.

* I open ``test_functions.py``

* I delete all the text then add :ref:`the first failing test<test_failure>` to ``test_functions.py``

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

* I add the new files_ and folders_ to git_ for tracking

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
     create mode 100644 tests/test_functions.py
     create mode 100644 uv.lock

  then goes back to the command line.

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

    test_functions.py:2: AssertionError
    ================ short test summary info =================
    FAILED test_functions.py::test_failure - assert False is True
    =================== 1 failed in X.YZs ====================

  because :ref:`False<test_what_is_false>` is NOT :ref:`True<test_what_is_true>`

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors and try to run ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_functions.py``

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

----

*********************************************************************************
test_making_a_function_w_pass
*********************************************************************************

The simplest :ref:`function<what is a function?>` I can make is with the pass_ keyword.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change ``test_failure`` to :ref:`test_making_a_function_w_pass`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def test_making_a_function_w_pass():
        w_pass


    # Exceptions seen
    # AssertionError

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    >       w_pass
    E       NameError: name 'w_pass' is not defined

  because Python_ does not know what I mean by ``w_pass`` since I do not have a definition for it in ``test_functions.py``.

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

----

*********************************************************************************
what is a variable?
*********************************************************************************

I can define a name in Python with a variable. It is a name that is used for any :ref:`object<what is a class?>`. For example, in Mathematics_ we use ``x`` to represent any number.

Every time I use the name, Python_ "knows" that I am referring to the :ref:`object<what is a class?>` pointed the name to.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``w_pass`` to a :ref:`variable<what is a variable?>` by pointing it to :ref:`None (the simplest object)<what is None?>`

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-3

  def test_making_a_function_w_pass():
      # w_pass
      w_pass = None


  # Exceptions seen
  # AssertionError
  # NameError

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

    def test_making_a_function_w_pass():
        # w_pass
        w_pass = None
        assert w_pass is 0


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is 0

  because ``w_pass`` points to :ref:`None<what is None?>`. Using substitution

  .. code-block:: python

    w_pass = None
    assert w_pass is 0
    assert None   is 0

  which raises :ref:`AssertionError<what causes AssertionError?>` since :ref:`None is not the same object as an integer (whole number without decimals)<test_assertion_error_w_none>`.

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    def test_making_a_function_w_pass():
        # w_pass
        w_pass = None
        # assert w_pass is 0
        assert w_pass is None


    # Exceptions seen

  the test passes.

----

*********************************************************************************
how to call a function
*********************************************************************************

Right now, ``w_pass`` is just a name. To use a :ref:`function<what is a function?>` I have to call it, like a telephone number. The way to do that is with parentheses (``()``) after the name.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add parentheses to the :ref:`assertion<what is an assertion?>` to call ``w_pass`` inside :ref:`test_making_a_function_w_pass`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6

    def test_making_a_function_w_pass():
        # w_pass
        w_pass = None
        # assert w_pass is 0
        # assert w_pass is None
        assert w_pass() is None


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``w_pass`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    w_pass = None # point the name to the object
    w_pass()      # call the name
    None()        # substitute the value for the name

  ``None()`` raises :ref:`TypeError<what causes TypeError?>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use the def_ and pass_ keywords to make ``w_pass`` the simplest :ref:`function<what is a function?>` I can make

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3, 6-7

    def test_making_a_function_w_pass():
        # w_pass
        # w_pass = None
        # assert w_pass is 0
        # assert w_pass is None
        def w_pass():
            pass

        assert w_pass() is None


    # Exceptions seen

  - The test passes because I get :ref:`None<what is None?>` when I call ``w_pass``.
  - The :ref:`assertion<what is an assertion?>` - ``assert w_pass() is None`` checks if the result of a call to ``w_pass``, is the same :ref:`object<everything is an object>` as :ref:`None<what is None?>`.
  - The :ref:`function definition<how to make a function>` simply says pass_ and the test passes.
  - pass_ is a keyword that allows the :ref:`function definition<how to make a function>` to follow Python_ language rules (the :ref:`function<what is a function?>` must have a body).
  - The test passes because :ref:`all functions return None by default, as if they have an invisible line that says return None<test_making_a_function_w_return_none>`, which leads me to the next test, but first cleanup time.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def test_making_a_function_w_pass():
        def w_pass():
            pass

        assert w_pass() is None


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError

* I open another terminal_ then add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_making_a_function_w_pass'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can make a function with pass.<test_making_a_function_w_pass>`.

----

*********************************************************************************
test_making_a_function_w_return
*********************************************************************************

I can also make a function with a `return statement`_.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a new test with a name

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9

    def test_making_a_function_w_pass():
        def w_pass():
            pass

        assert w_pass() is None


    def test_making_a_function_w_return():
        w_return


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    >       w_return
    E       NameError: name 'w_return' is not defined

  because Python_ does not know what I mean by ``w_return`` since I do not have a definition for it in ``test_functions.py``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``w_return`` to a :ref:`variable<what is a variable?>` by pointing it to :ref:`None (the simplest object)<what is None?>`

.. code-block:: python
  :lineno-start: 8
  :emphasize-lines: 2-3

  def test_making_a_function_w_return():
      # w_return
      w_return = None


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for ``w_return``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 4

    def test_making_a_function_w_return():
        # w_return
        w_return = None
        assert w_return is 1


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is 1

  because ``w_return`` points to :ref:`None<what is None?>`. Using substitution

  .. code-block:: python

    w_return = None
    assert w_return is 1
    assert None     is 1

  which raises :ref:`AssertionError<what causes AssertionError?>` since :ref:`None is not the same object as an integer (whole number without decimals)<test_assertion_error_w_none>`.

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 4-5

    def test_making_a_function_w_return():
        # w_return
        w_return = None
        # assert w_return is 1
        assert w_return is None


    # Exceptions seen

  the test passes.

* I add parentheses to call ``w_return`` inside :ref:`test_making_a_function_w_return`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 6

    def test_making_a_function_w_return():
        # w_return
        w_return = None
        # assert w_return is 1
        # assert w_return is None
        assert w_return() is None


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``w_return`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    w_return = None # point the name to the object
    w_return()      # call the name
    None()          # substitute the value for the name

  ``None()`` raises :ref:`TypeError<what causes TypeError?>`.

* I use the def_ and pass_ keywords to change ``w_return`` to the simplest :ref:`function<what is a function?>` I can make

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3, 6-7

    def test_making_a_function_w_return():
        # w_return
        # w_return = None
        # assert w_return is 1
        # assert w_return is None
        def w_return():
            pass

        assert w_return() is None


    # Exceptions seen

  the test passes.

----

*********************************************************************************
the return statement
*********************************************************************************

The return_ keyword is used to define what a :ref:`function<what is a function?>` gives as output when it is called.

* I change pass_ to a `return statement`_ with the return_ keyword

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 7-8

    def test_making_a_function_w_return():
        # w_return
        # w_return = None
        # assert w_return is 1
        # assert w_return is None
        def w_return():
            # pass
            return

        assert w_return() is None


    # Exceptions seen

  - The test is still green because I get :ref:`None<what is None?>` when I call ``w_return``.
  - The :ref:`assertion<what is an assertion?>` - ``assert w_return() is None`` checks if the result of a call to ``w_return``, is the same :ref:`object<everything is an object>` as :ref:`None<what is None?>`.
  - The :ref:`function definition<how to make a function>` simply says return_ and the test passes.
  - return_ is a keyword that defines what the :ref:`function<what is a function?>` gives as output.

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def test_making_a_function_w_pass():
        def w_pass():
            pass

        assert w_pass() is None


    def test_making_a_function_w_return():
        def w_return():
            return

        assert w_return() is None


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_making_a_function_w_return'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can make a function with a return statement<test_making_a_function_w_return>`.

I have two :ref:`functions<what is a function?>` with different statements, and the tests show that they both return :ref:`None<what is None?>`

.. code-block:: python

  def w_pass():
      pass

.. code-block:: python

  def w_return():
      return

their contents are different, their results are the same because ":ref:`all functions return None by default, as if they have an invisible line that says return None<test_making_a_function_w_return_none>`", which leads me to the next test.


----

*********************************************************************************
test_making_a_function_w_return_none
*********************************************************************************

I can make a :ref:`function<what is a function?>` with a `return statement`_ that says exactly what the :ref:`function<what is a function?>` returns.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with a name

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 8-9

    def test_making_a_function_w_return():
        def w_return():
            return

        assert w_return() is None


    def test_making_a_function_w_return_none():
        w_return_none


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'w_return_none' is not defined

  because Python_ does not know what I mean by ``w_return_none`` since I do not have a definition for it in this file_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``w_return_none`` to a :ref:`variable<what is a variable?>` by pointing it to :ref:`None (the simplest object)<what is None?>`

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 2-3

  def test_making_a_function_w_return_none():
      # w_return_none
      w_return_none = None


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for ``w_return_none``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 4

    def test_making_a_function_w_return_none():
        # w_return_none
        w_return_none = None
        assert w_return_none is 2


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is 2

  because ``w_return_none`` points to :ref:`None<what is None?>`. Using substitution

  .. code-block:: python

    w_return_none = None
    assert w_return_none is 2
    assert None          is 2

  which raises :ref:`AssertionError<what causes AssertionError?>` since :ref:`None is not the same object as an integer (whole number without decimals)<test_assertion_error_w_none>`.

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 4-5

    def test_making_a_function_w_return_none():
        # w_return_none
        w_return_none = None
        # assert w_return_none is 2
        assert w_return_none is None


    # Exceptions seen

  the test passes.

* I add parentheses to call ``w_return_none`` inside :ref:`test_making_a_function_w_return_none`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 6

    def test_making_a_function_w_return_none():
        # w_return_none
        w_return_none = None
        # assert w_return_none is 2
        # assert w_return_none is None
        assert w_return_none() is None


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``w_return_none`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    w_return_none = None # point the name to the object
    w_return_none()      # call the name
    None()               # substitute the value for the name

  ``None()`` raises :ref:`TypeError<what causes TypeError?>`.

* I change ``w_return_none`` to a :ref:`function<what is a function?>` with the def_ and return_ keywords

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3, 6-7

    def test_making_a_function_w_return_none():
        # w_return_none
        # w_return_none = None
        # assert w_return_none is 2
        # assert w_return_none is None
        def w_return_none():
            return

        assert w_return_none() is None


    # Exceptions seen

  the test passes.

* I add :ref:`None<what is None?>` to the `return statement`_ of ``w_return_none``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 7-8

    def test_making_a_function_w_return_none():
        # w_return_none
        # w_return_none = None
        # assert w_return_none is 2
        # assert w_return_none is None
        def w_return_none():
            # return
            return None

        assert w_return_none() is None


    # Exceptions seen

  the test is still green.

* I change :ref:`None<what is None?>` to ``'something'``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 8-9
    :emphasize-text: something

    def test_making_a_function_w_return_none():
        # w_return_none
        # w_return_none = None
        # assert w_return_none is 2
        # assert w_return_none is None
        def w_return_none():
            # return
            # return None
            return 'something'

        assert w_return_none() is None


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'something' is None

  because when I call ``w_return_none`` I get ``'something'``. Using substitution

  .. code-block:: python

    assert w_return_none() is None
    assert 'something'     is None

  which raises :ref:`AssertionError<what causes AssertionError?>` because :ref:`a string (anything in quotes) is not None<test_assertion_error_w_none>`.

* I undo the change

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 8-9

    def test_making_a_function_w_return_none():
        # w_return_none
        # w_return_none = None
        # assert w_return_none is 2
        # assert w_return_none is None
        def w_return_none():
            # return
            return None
            # return 'something'

        assert w_return_none() is None


    # Exceptions seen

  - The test is green again because I get :ref:`None<what is None?>` when I call ``w_return_none``.
  - The :ref:`assertion<what is an assertion?>` - ``assert w_return_none() is None`` checks if the result of a call to ``w_return_none``, is the same :ref:`object<everything is an object>` as :ref:`None<what is None?>`.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 8

    def test_making_a_function_w_return():
        def w_return():
            return

        assert w_return() is None


    def test_making_a_function_w_return_none():
        def w_return_none():
            return None

        assert w_return_none() is None


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_making_a_function_w_return_none'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can make a function with return None.<test_making_a_function_w_return_none>`.

I have three :ref:`functions<what is a function?>` with different statements, and the tests show that they all return :ref:`None<what is None?>`

.. code-block:: python

  def w_pass():
      pass

.. code-block:: python

  def w_return():
      return

.. code-block:: python

  def w_return_none():
      return None

their contents are different, their results are the same because ":ref:`all functions return None by default, as if they have an invisible line that says ...<test_making_a_function_w_return_none>`"

I like to write my :ref:`functions<what is a function?>` with explicit `return statements`_, so that anyone can see what the :ref:`function<what is a function?>` returns without having to think about it.

----

*********************************************************************************
test_what_happens_after_functions_return
*********************************************************************************

The `return statement`_ is the last thing to run in a :ref:`function<what is a function?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 8-9

    def test_making_a_function_w_return_none():
        def w_return_none():
            return None

        assert w_return_none() is None


    def test_what_happens_after_functions_return():
        return_leaves_the_function


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'return_leaves_the_function'
               is not defined

  because Python_ does not know what I mean by ``return_leaves_the_function`` since I do not have a definition for it in this file_, yet.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``return_leaves_the_function`` to a :ref:`variable<what is a variable?>` by pointing it to :ref:`None (the simplest object)<what is None?>`

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 2-3

  def test_what_happens_after_functions_return():
      # return_leaves_the_function
      return_leaves_the_function = None


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4

    def test_what_happens_after_functions_return():
        # return_leaves_the_function
        return_leaves_the_function = None
        assert return_leaves_the_function is 'something'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None is 'something'

  because ``return_leaves_the_function`` points to :ref:`None<what is None?>`. Using substitution

  .. code-block:: python

    return_leaves_the_function = None
    assert return_leaves_the_function is 'something'
    assert None                       is 'something'

  which raises :ref:`AssertionError<what causes AssertionError?>` since :ref:`None is not the same object as a string<test_assertion_error_w_none>`.

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4-5

    def test_what_happens_after_functions_return():
        # return_leaves_the_function
        return_leaves_the_function = None
        # assert return_leaves_the_function is 'something'
        assert return_leaves_the_function is None


    # Exceptions seen

  the test passes.

* I add parentheses to call ``return_leaves_the_function`` inside :ref:`test_making_a_function_w_return_none`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 6

    def test_what_happens_after_functions_return():
        # return_leaves_the_function
        return_leaves_the_function = None
        # assert return_leaves_the_function is 'something'
        # assert return_leaves_the_function is None
        assert return_leaves_the_function() is None


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``return_leaves_the_function`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    return_leaves_the_function = None # point the name to the object
    return_leaves_the_function()      # call the name
    None()                            # substitute the value for the name

  ``None()`` raises :ref:`TypeError<what causes TypeError?>`.

* I change ``return_leaves_the_function`` to a :ref:`function<what is a function?>` with the def_ and return_ keywords

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3, 6-7

    def test_what_happens_after_functions_return():
        # return_leaves_the_function
        # return_leaves_the_function = None
        # assert return_leaves_the_function is 'something'
        # assert return_leaves_the_function is None
        def return_leaves_the_function():
            return None

        assert return_leaves_the_function() is None


    # Exceptions seen

  the test passes.

* I add a `return statement`_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 7

    def test_what_happens_after_functions_return():
        # return_leaves_the_function
        # return_leaves_the_function = None
        # assert return_leaves_the_function is 'something'
        # assert return_leaves_the_function is None
        def return_leaves_the_function():
            return 'something'
            return None

        assert return_leaves_the_function() is None


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert 'something' is None

  because when I call ``return_leaves_the_function`` I get ``'something'``. Using substitution

  .. code-block:: python

    assert return_leaves_the_function() is None
    assert 'something'                  is None

  - which raises :ref:`AssertionError<what causes AssertionError?>` because :ref:`a string is not None<test_assertion_error_w_none>`.
  - The `return statement`_ is the last thing to run in a :ref:`function<what is a function?>`, it exits after the `return statement`_.
  - It never gets to ``return None`` because it leaves after ``return 'something'``.
  - The second `return statement`_ will never run. It is not reachable (this is called dead code).
  - This means I can treat a :ref:`call to a function<how to call a function>` as the :ref:`object<what is a class?>` it returns.

  .. tip::

    The `Integrated Development Environment (IDE)`_ shows that the second return statement will not run by graying it out.

* I move ``return None``, to make it the first `return statement`_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 7-8

    def test_what_happens_after_functions_return():
        # return_leaves_the_function
        # return_leaves_the_function = None
        # assert return_leaves_the_function is 'something'
        # assert return_leaves_the_function is None
        def return_leaves_the_function():
            return None
            return 'something'

        assert return_leaves_the_function() is None


    # Exceptions seen

  the test is green again.

* I change the second `return statement`_ as a reminder

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 8-9

    def test_what_happens_after_functions_return():
        # return_leaves_the_function
        # return_leaves_the_function = None
        # assert return_leaves_the_function is 'something'
        # assert return_leaves_the_function is None
        def return_leaves_the_function():
            return None
            # return 'something'
            return 'only one way for this line to run'

        assert return_leaves_the_function() is None


    # Exceptions seen

  the second `return statement`_ is now like a comment, and the test is still green because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 15

    def test_making_a_function_w_return_none():
        def w_return_none():
            return None

        assert w_return_none() is None


    def test_what_happens_after_functions_return():
        def return_leaves_the_function():
            return None
            return 'only one way for this line to run'

        assert return_leaves_the_function() is None


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_what_happens_after_functions_return'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test_constant_function
*********************************************************************************

There are :ref:`functions<what is a function?>` that always return the same thing when they are called. They are singletons or constant :ref:`functions<what is a function?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 9-10

    def test_what_happens_after_functions_return():
        def return_leaves_the_function():
            return None
            return 'only one way for this line to run'

        assert return_leaves_the_function() is None


    def test_constant_function():
        constant


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'constant' is not defined

  because Python_ does not know what I mean by ``constant`` since I do not have a definition for it in this file_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``constant`` to a :ref:`variable<what is a variable?>` by pointing it to :ref:`None<what is None?>`

.. code-block:: python
  :lineno-start: 30
  :emphasize-lines: 2-3

  def test_constant_function():
      # constant
      constant = None


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4

    def test_constant_function():
        # constant
        constant = None
        assert constant is 'the same thing'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None is 'the same thing'

  because ``constant`` points to :ref:`None<what is None?>`. Using substitution

  .. code-block:: python

    constant = None
    assert constant is 'the same thing'
    assert None     is 'the same thing'

  which raises :ref:`AssertionError<what causes AssertionError?>` since :ref:`None is not the same object as a string(anything in quotes)<test_assertion_error_w_none>`.

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4-5

    def test_constant_function():
        # constant
        constant = None
        # assert constant is 'the same thing'
        assert constant is None


    # Exceptions seen

  the test passes.

* I add parentheses to call ``constant``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 6

    def test_constant_function():
        # constant
        constant = None
        # assert constant is 'the same thing'
        # assert constant is None
        assert constant() is None


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``constant`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    constant = None # point the name to the object
    constant()      # call the name
    None()          # substitute the value for the name

  ``None()`` raises :ref:`TypeError<what causes TypeError?>`.

* I change ``constant`` to a :ref:`function<what is a function?>` with the def_ and return_ keywords

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 3, 6-7

    def test_constant_function():
        # constant
        # constant = None
        # assert constant is 'the same thing'
        # assert constant is None
        def constant():
            return None

        assert constant() is None


    # Exceptions seen

  the test passes.

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 7-8

    def test_constant_function():
        # constant
        # constant = None
        # assert constant is 'the same thing'
        # assert constant is None
        def constant():
            # return None
            return 'the same thing'

        assert constant() is None


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'the same thing' is None

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 10-11

    def test_constant_function():
        # constant
        # constant = None
        # assert constant is 'the same thing'
        # assert constant is None
        def constant():
            # return None
            return 'the same thing'

        # assert constant() is None
        assert constant() is 'the same thing'


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 22

    def test_what_happens_after_functions_return():
        def return_leaves_the_function():
            return None
            return 'only one way for this line to run'

        assert return_leaves_the_function() is None


    def test_constant_function():
        def constant():
            return 'the same thing'

        assert constant() is 'the same thing'


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_constant_function'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`A constant function always returns the same thing.<test_constant_function>` when called, I can use them in place of :ref:`variables<what is a variable?>`. The number of cases where they are faster than :ref:`variables<what is a variable?>` is pretty small. It is something like if the :ref:`function<what is a function?>` is called less than 10 times (who's counting?)

All the :ref:`functions<what is a function?>` I have written so far return the same value every time they are called.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_functions.py`` and ``functions.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``functions``

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

I ran tests to show that I can make functions_ with the def_, :ref:`pass<test_making_a_function_w_pass>` and :ref:`return<test_making_a_function_w_return>` keywords.

:ref:`How many questions can you answer about functions?<questions about functions>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<what is a function?: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have covered a bit so far and know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what causes AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`

:ref:`Would you like to use variables to make a person?<how to make a person with strings>`

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