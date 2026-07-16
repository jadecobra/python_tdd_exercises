.. meta::
  :description: Separate tests from solutions (keep them in different modules) in the functions project using TDD. Move every function (w_pass, w_return, return_leaves_the_function, constant, identity, positional_arguments, keyword_arguments, args_and_kwargs, optional_arguments, unknown_number_of_arguments) out of test_functions.py into src/functions.py. Use mkdir src, touch src/functions.py, import src.functions, reroute calls via local aliases like positional_arguments = src.functions.positional_arguments, then remove the commented lines (the local def left behind in the test). See real errors while separating: "NameError: name 'src' is not defined", "ModuleNotFoundError: No module named 'src'", "ModuleNotFoundError: No module named 'src.functions'", "AttributeError: module 'src.functions' has no attribute 'w_pass'". Practice bare assert is None / == , git commit -am after each move, uv run pytest-watcher. Reviews the functions that take input (positional/keyword order independence, optional defaults, *args **kwargs unpacking) as they get moved. Review lesson: I can write solutions in a different module from the tests. Part of Jacob Itegboje's Pumping Python TDD series for beginners.
  :keywords: Jacob Itegboje, Pumping Python, separate tests from solutions python, src folder functions, import src.functions, move function to src, ModuleNotFoundError No module named 'src', AttributeError module 'src.functions' has no attribute, remove the commented lines, test_functions.py to functions.py, functions separation TDD, bare assert in tests, uv run pytest-watcher, git commit -am move, w_pass w_return constant identity positional_arguments keyword_arguments, optional_arguments *args **kwargs, "NameError: name 'src' is not defined", "ModuleNotFoundError: No module named 'src.functions'", "I can write solutions in a different module from the tests", red green refactor separation, Python TDD separate module

.. include:: ../links.rst

#################################################################################
separate and equal functions
#################################################################################

All the :ref:`functions<what is a function?>` in :ref:`the functions project<what is a function?>` were written in ``test_functions.py``. I want to move them to ``functions.py`` in the ``src`` folder_ so that I can keep the tests and solutions separate.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/functions/tests/test_functions_w_separation.py
  :language: python
  :linenos:

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd functions

  the terminal_ shows I am in the ``functions`` folder_

  .. code-block:: python

    .../pumping_python/functions

* I open ``test_functions.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    test_functions.py ............                      [100%]

    =================== 12 passed in X.YZs ===================

----

*********************************************************************************
move w_pass
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the :ref:`call<how to call a function with input>` in the :ref:`assertion<what is an assertion?>` of :ref:`test_making_a_function_w_pass` to use the result of a :ref:`call<how to call a function with input>` to the :ref:`w_pass function<test_making_a_function_w_pass>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a :ref:`call<how to call a function with input>` to the :ref:`w_pass function<test_making_a_function_w_pass>` in ``test_functions.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 5-6

  def test_making_a_function_w_pass():
      def w_pass():
          pass

      # assert w_pass() is None
      assert src.functions.w_pass() is None


  def test_making_a_function_w_return():

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'src' is not defined

because ``src`` is not defined in ``test_functions.py``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ at the top of ``test_functions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.functions


    def test_making_a_function_w_pass():

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src'

  because there is nothing named ``src`` in this project.

* I add :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 230
    :emphasize-lines: 6
    :emphasize-text: ModuleNotFoundError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # SyntaxError
    # ModuleNotFoundError

* I open another terminal_ then make sure I am in the ``functions`` folder_

* I use mkdir_ to make a folder_ named ``src``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir src

* I go back to the terminal_ where the tests are running.

* I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) on the keyboard in ``test_functions.py`` to run the tests again and the terminal_ shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.functions'

  because there is nothing in the ``src`` folder_ named ``functions``.

* I go to the second terminal_ I opened, then use touch_ to make ``functions.py`` in the ``src`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    touch src/functions.py

* I add the new file_ to git_ for tracking

  .. code-block:: python

    git add src/functions.py

  the terminal_ goes back to the command line.

* I go back to the terminal_ where the tests are running and it shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions' has no attribute 'w_pass'

  because there is nothing in ``functions.py`` in the ``src`` folder_ with the name ``w_pass``.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen, in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 230
    :emphasize-lines: 7
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # SyntaxError
    # ModuleNotFoundError
    # AttributeError

* I open ``functions.py`` from the ``src`` folder.

* I add a copy of :ref:`the w_pass function<test_making_a_function_w_pass>` to ``functions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def w_pass():
        pass

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line and :ref:`the w_pass function<test_making_a_function_w_pass>` from :ref:`test_making_a_function_w_pass` in ``test_functions.py``

  .. code-block:: python
    :linenos:

    import src.functions


    def test_making_a_function_w_pass():
        assert src.functions.w_pass() is None


    def test_making_a_function_w_return():

  the test is still green because the :ref:`call<how to call a function with input>` that was made to :ref:`the w_pass function<test_making_a_function_w_pass>` that was in ``test_functions.py`` is now to :ref:`the w_pass function<test_making_a_function_w_pass>` in ``functions.py`` in the ``src`` folder_. When ``src.functions.w_pass`` is called, Python_ follows this path

  .. code-block:: shell

    src.functions.w_pass
    src
    └── functions.py
        └── def w_pass():
            └── pass

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move w_pass to functions.py'

:ref:`I can write solutions in a different module from the tests<separate and equal>`.

----

*********************************************************************************
move w_return
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I change the :ref:`call<how to call a function with input>` in the :ref:`assertion<what is an assertion?>` of :ref:`test_making_a_function_w_return` to use the result of a :ref:`call<how to call a function with input>` to the :ref:`w_return function<test_making_a_function_w_return>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a :ref:`call<how to call a function with input>` to the :ref:`w_return function<test_making_a_function_w_return>` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 5-6

    def test_making_a_function_w_return():
        def w_return():
            return

        # assert w_return() is None
        assert src.functions.w_return() is None


    def test_making_a_function_w_return_none():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'w_return'

  because ``functions.py`` in the ``src`` folder_ does not have anything named ``w_return`` in it.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a copy of :ref:`the w_return function<test_making_a_function_w_return>` to ``functions.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 5-6

  def w_pass():
      pass


  def w_return():
      return

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line and :ref:`the w_return function<test_making_a_function_w_return>` from :ref:`test_making_a_function_w_return` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 8

    def test_making_a_function_w_return():
        assert src.functions.w_return() is None


    def test_making_a_function_w_return_none():

  the test is still green because the :ref:`call<how to call a function with input>` that was made to :ref:`the w_return function<test_making_a_function_w_return>` that was in ``test_functions.py`` is now to :ref:`the w_return function<test_making_a_function_w_return>` in ``functions.py`` in the ``src`` folder_. When ``src.functions.w_return`` is called, Python_ follows this path

  .. code-block:: shell

    src.functions.w_return
    src
    └── functions.py
        └── def w_return():
            └── return

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move w_return to functions.py'

----

*********************************************************************************
move w_return_none
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I change the :ref:`call<how to call a function with input>` in the :ref:`assertion<what is an assertion?>` of :ref:`test_making_a_function_w_return_none` to use the result of a :ref:`call<how to call a function with input>` to the :ref:`w_return_none function<test_making_a_function_w_return_none>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a :ref:`call<how to call a function with input>` to the :ref:`w_return_none function<test_making_a_function_w_return_none>` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 5-6

    def test_making_a_function_w_return_none():
        def w_return_none():
            return None

        # assert w_return_none() is None
        assert src.functions.w_return_none() is None


    def test_what_happens_after_functions_return():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'w_return_none'

  because ``functions.py`` in the ``src`` folder_ does not have anything named ``w_return_none`` in it.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a copy of :ref:`the w_return_none function<test_making_a_function_w_return_none>` to ``functions.py``

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 5-6

  def w_return():
      return


  def w_return_none():
      return None

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line and :ref:`the w_return_none function<test_making_a_function_w_return_none>` from :ref:`test_making_a_function_w_return_none` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 12

    def test_making_a_function_w_return_none():
        assert src.functions.w_return_none() is None


    def test_what_happens_after_functions_return():

  the test is still green because the :ref:`call<how to call a function with input>` that was made to :ref:`the w_return_none function<test_making_a_function_w_return_none>` that was in ``test_functions.py`` is now to :ref:`the w_return_none function<test_making_a_function_w_return_none>` in ``functions.py`` in the ``src`` folder_. When ``src.functions.w_return_none`` is called, Python_ follows this path

  .. code-block:: shell

    src.functions.w_return_none
    src
    └── functions.py
        └── def w_return_none():
            └── return None

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move w_return_none to functions.py'

----

*********************************************************************************
move return_leaves_the_function
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I change the :ref:`call<how to call a function with input>` in the :ref:`assertion<what is an assertion?>` of :ref:`test_what_happens_after_functions_return` to use the result of a :ref:`call<how to call a function with input>` to :ref:`return_leaves_the_function<test_what_happens_after_functions_return>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a :ref:`call<how to call a function with input>` to :ref:`return_leaves_the_function<test_what_happens_after_functions_return>` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 6-10

    def test_what_happens_after_functions_return():
        def return_leaves_the_function():
            return None
            return 'only one way for this line to run'

        # assert return_leaves_the_function() is None
        assert (
            src.functions
               .return_leaves_the_function()
        ) is None


    def test_constant_function():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'return_leaves_the_function'

  because I have not added ``return_leaves_the_function`` to ``functions.py`` in the ``src`` folder_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a copy of :ref:`return_leaves_the_function<test_what_happens_after_functions_return>` to ``functions.py``

.. code-block:: python
  :lineno-start: 9
  :emphasize-lines: 5-7

  def w_return_none():
      return None


  def return_leaves_the_function():
      return None
      return 'only one way for this line to run'

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line and :ref:`return_leaves_the_function<test_what_happens_after_functions_return>` from :ref:`test_what_happens_after_functions_return` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 16

    def test_what_happens_after_functions_return():
        assert (
            src.functions
               .return_leaves_the_function()
        ) is None


    def test_constant_function():

  the test is still green because the :ref:`call<how to call a function with input>` that was made to :ref:`return_leaves_the_function<test_what_happens_after_functions_return>` that was in ``test_functions.py`` is now to :ref:`return_leaves_the_function<test_what_happens_after_functions_return>` in ``functions.py`` in the ``src`` folder_. When ``src.functions.return_leaves_the_function`` is called, Python_ follows this path

  .. code-block:: shell

    src.functions.return_leaves_the_function
    src
    └── functions.py
        └── def return_leaves_the_function():
            └── return None

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move return_leaves_the_function to functions.py'

----

*********************************************************************************
move constant function
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I change the :ref:`call<how to call a function with input>` in the :ref:`assertion<what is an assertion?>` of :ref:`test_constant_function` to use the result of a :ref:`call<how to call a function with input>` to the :ref:`constant function<test_constant_function>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a :ref:`call<how to call a function with input>` to the :ref:`constant function<test_constant_function>` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5-6

    def test_constant_function():
        def constant():
            return 'the same thing'

        # assert constant() == 'the same thing'
        assert src.functions.constant() == 'the same thing'


    def test_identity_function():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'constant'

  because there is nothing named ``constant`` in ``functions.py`` in the ``src`` folder_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a copy of :ref:`the constant function<test_constant_function>` to ``functions.py``

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 6-7

  def return_leaves_the_function():
      return None
      return 'only one way for this line to run'


  def constant():
      return 'the same thing'

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line and :ref:`the constant function<test_constant_function>` from :ref:`test_constant_function` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 23

    def test_constant_function():
        assert src.functions.constant() == 'the same thing'


    def test_identity_function():

  the test is still green because the :ref:`call<how to call a function with input>` that was made to :ref:`the constant function<test_constant_function>` that was in ``test_functions.py`` is now to :ref:`the constant function<test_constant_function>` in ``functions.py`` in the ``src`` folder_. When ``src.functions.constant`` is called, Python_ follows this path

  .. code-block:: shell

    src.functions.constant
    src
    └── functions.py
        └── def constant():
            └── return 'the same thing'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move constant function to functions.py'

----

*********************************************************************************
move identity function
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I change the calls in the :ref:`assertions<what is an assertion?>` of :ref:`test_identity_function` to use the results of calls to the :ref:`identity function<test_identity_function>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of calls to the :ref:`identity function<test_identity_function>` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 5-8

    def test_identity_function():
        def identity(the_input):
            return the_input

        # assert identity(None) == None
        # assert identity(object) == object
        assert src.functions.identity(None) == None
        assert src.functions.identity(object) == object


    def test_why_use_a_function():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'identity'

  because ``identity`` is not a name in ``functions.py`` in the ``src`` folder_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a copy of :ref:`the identity function<test_identity_function>` to ``functions.py``

.. code-block:: python
  :lineno-start: 18
  :emphasize-lines: 5-6

  def constant():
      return 'the same thing'


  def identity(the_input):
      return the_input

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line and :ref:`the identity function<test_identity_function>` from :ref:`test_identity_function` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 23

    def test_identity_function():
        assert src.functions.identity(None) == None
        assert src.functions.identity(object) == object


    def test_why_use_a_function():

  the test is still green because the :ref:`call<how to call a function with input>` that was made to :ref:`the identity function<test_identity_function>` that was in ``test_functions.py`` is now to :ref:`the identity function<test_identity_function>` in ``functions.py`` in the ``src`` folder_. When ``src.functions.identity`` is called, Python_ follows this path

  .. code-block:: shell

    src.functions.identity
    src
    └── functions.py
        └── def identity(the_input):
            └── return the_input

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move identity function to functions.py'

----

*********************************************************************************
move positional_arguments function
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I comment out the :ref:`positional_arguments function<test_positional_arguments>` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 17-18

    def test_why_use_a_function():
        def add_x(number):
            return 3 + number

        assert add_x(0) == 3
        assert add_x(1) == 4
        assert add_x(2) == 5
        assert add_x(3) == 6
        assert add_x(4) == 7
        assert add_x(5) == 8
        assert add_x(6) == 9
        assert add_x(7) == 10
        assert add_x(8) == 11
        assert add_x(9) == 12


    # def positional_arguments(first_input, last_input):
    #     return first_input, last_input


    def test_positional_arguments():

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'positional_arguments'
               is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use a :ref:`variable<what is a variable?>` to reroute the calls to the :ref:`positional_arguments function<test_positional_arguments>` from :ref:`test_positional_arguments` to the :ref:`positional_arguments function<test_positional_arguments>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2-4

    def test_positional_arguments():
        positional_arguments = (
            src.functions.positional_arguments
        )
        first, last = 'first', 'last'

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'positional_arguments' is not defined

  because :ref:`test_keyword_arguments` also calls :ref:`the positional_arguments function<test_positional_arguments>` of ``test_functions.py``. This is a risky change.

* I use a :ref:`variable<what is a variable?>` to reroute the :ref:`call<how to call a function with input>` to the :ref:`positional_arguments function<test_positional_arguments>` from :ref:`test_keyword_arguments` to the :ref:`positional_arguments function<test_positional_arguments>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 11-13

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert (
            keyword_arguments(
                first_input=a_tuple,
                last_input=a_list,
            )
          == (a_tuple, a_list)
        )

        positional_arguments = (
            src.functions.positional_arguments
        )
        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}
        assert (
            positional_arguments(
                last_input=a_dictionary,
                first_input=a_set,
            )
          == (a_set, a_dictionary)
        )


    def test_args_and_kwargs():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'positional_arguments'

  because ``positional_arguments`` does not exist in ``functions.py``.

* I add a copy of the :ref:`positional_arguments function<test_positional_arguments>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 5-6

    def identity(the_input):
        return the_input


    def positional_arguments(first_input, last_input):
        return first_input, last_input

  the tests pass because the calls that were made to the :ref:`positional_arguments function<test_positional_arguments>` that was in ``test_functions.py`` are now made to the :ref:`positional_arguments function<test_positional_arguments>` in ``functions.py`` in the ``src`` folder_.

  When ``positional_arguments`` is called in :ref:`test_positional_arguments` and :ref:`test_keyword_arguments`, Python_ follows this path

  .. code-block:: shell

    positional_arguments = src.functions.positional_arguments

    src
    └── functions.py
        └── def positional_arguments(first_input, last_input):
            └── return first_input, last_input

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented :ref:`positional_arguments function<test_positional_arguments>` from ``test_functions.py``

  .. code-block:: python
    :lineno-start: 32

    def test_why_use_a_function():
        def add_x(number):
            return 3 + number

        assert add_x(0) == 3
        assert add_x(1) == 4
        assert add_x(2) == 5
        assert add_x(3) == 6
        assert add_x(4) == 7
        assert add_x(5) == 8
        assert add_x(6) == 9
        assert add_x(7) == 10
        assert add_x(8) == 11
        assert add_x(9) == 12


    def test_positional_arguments():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move positional_arguments to functions.py'

----

*********************************************************************************
move keyword_arguments function
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I comment out the :ref:`keyword_arguments function<test_keyword_arguments>` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 11-12

        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}
        assert (
            keyword_arguments(
                a_set, a_dictionary,
            )
         == (a_set, a_dictionary)
        )


    # def keyword_arguments(first_input, last_input):
    #     return first_input, last_input


    def test_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'keyword_arguments' is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use a :ref:`variable<what is a variable?>` to reroute the calls to the :ref:`keyword_arguments function<test_keyword_arguments>` from :ref:`test_keyword_arguments` to the :ref:`keyword_arguments function<test_keyword_arguments>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 2-4

    def test_keyword_arguments():
        keyword_arguments = (
            src.functions.keyword_arguments
        )
        first, last = 'first', 'last'

        assert (
            keyword_arguments(
                first_input=first, last_input=last,
            )
         == (first, last)
        )
        assert (
            keyword_arguments(
                last_input=last, first_input=first,
            )
         == (first, last)
        )
        assert (
            keyword_arguments(
                last_input=0, first_input=1,
            )
         == (1, 0)
        )

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert (
            keyword_arguments(
                first_input=a_tuple,
                last_input=a_list,
            )
         == (a_tuple, a_list)
        )

        positional_arguments = (
            src.functions.positional_arguments
        )
        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}
        assert (
            positional_arguments(
                last_input=a_dictionary,
                first_input=a_set,
            )
         == (a_set, a_dictionary)
        )


    def test_args_and_kwargs():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'keyword_arguments'

  because I have not added ``keyword_arguments`` to ``functions.py``, yet.

* I add a copy of the :ref:`keyword_arguments function<test_keyword_arguments>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 5-6

    def positional_arguments(first_input, last_input):
        return first_input, last_input


    def keyword_arguments(first_input, last_input):
        return first_input, last_input


  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'keyword_arguments' is not defined

  because :ref:`test_positional_arguments` also calls :ref:`the keyword_arguments function<test_keyword_arguments>` of ``test_functions.py``. Risky business.

* I use a :ref:`variable<what is a variable?>` to reroute the calls to the :ref:`keyword_arguments function<test_keyword_arguments>` from :ref:`test_positional_arguments` to the :ref:`keyword_arguments function<test_keyword_arguments>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 8-10

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert (
            positional_arguments(a_tuple, a_list)
         == (a_tuple, a_list)
        )

        keyword_arguments = (
            src.functions.keyword_arguments
        )
        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}
        assert (
            keyword_arguments(
                a_set, a_dictionary,
            )
         == (a_set, a_dictionary)
        )


    # def keyword_arguments(first_input, last_input):
    #     return first_input, last_input


    def test_keyword_arguments():

  the tests pass because the calls that were made to :ref:`the keyword_arguments function<test_keyword_arguments>` that was in ``test_functions.py`` are now made to :ref:`the keyword_arguments function<test_keyword_arguments>` in ``functions.py`` in the ``src`` folder_.

  When ``keyword_arguments`` is called in :ref:`test_keyword_arguments` and :ref:`test_positional_arguments`, Python_ follows this path

  .. code-block:: shell

    keyword_arguments = src.functions.keyword_arguments

    src
    └── functions.py
        └── def keyword_arguments(first_input, last_input):
            └── return first_input, last_input

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented :ref:`keyword_arguments function<test_keyword_arguments>` from ``test_functions.py``

  .. code-block:: python
    :lineno-start: 48

    def test_positional_arguments():
        positional_arguments = (
            src.functions.positional_arguments
        )
        first, last = 'first', 'last'

        assert (
            positional_arguments(first, last)
         == (first, last)
        )
        assert (
            positional_arguments(last, first)
         == (last, first)
        )
        assert (
            positional_arguments(0, 1)
         == (0, 1)
        )

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert (
            positional_arguments(a_tuple, a_list)
         == (a_tuple, a_list)
        )

        keyword_arguments = (
            src.functions.keyword_arguments
        )
        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}
        assert (
            keyword_arguments(
                a_set, a_dictionary,
            )
         == (a_set, a_dictionary)
        )


    def test_keyword_arguments():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move keyword_arguments to functions.py'

----

*********************************************************************************
move args_and_kwargs function
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I change the :ref:`call<how to call a function with input>` in the :ref:`assertion<what is an assertion?>` of :ref:`test_args_and_kwargs` to use the result of a :ref:`call<how to call a function with input>` to the :ref:`args_and_kwargs function<test_args_and_kwargs>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of the result of a :ref:`call<how to call a function with input>` to the :ref:`args_and_kwargs function<test_args_and_kwargs>` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 8-9

    def test_args_and_kwargs():
        def args_and_kwargs(first_input, last_input):
            return first_input, last_input

        first, last = 'first', 'last'

        assert (
            # args_and_kwargs(
            src.functions.args_and_kwargs(
                first, last_input=last,
            )
         == (first, last)
        )


    def test_optional_arguments():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'args_and_kwargs'

  because ``args_and_kwargs`` is not a name in ``functions.py`` in the ``src`` folder_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a copy of :ref:`the args_and_kwargs function<test_args_and_kwargs>` to ``functions.py``

.. code-block:: python
  :lineno-start: 30
  :emphasize-lines: 5-6

  def keyword_arguments(first_input, last_input):
      return first_input, last_input


  def args_and_kwargs(first_input, last_input):
      return first_input, last_input
the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line and the :ref:`args_and_kwargs function<test_args_and_kwargs>` from :ref:`test_args_and_kwargs` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 136

    def test_args_and_kwargs():
        first, last = 'first', 'last'

        assert (
            src.functions.args_and_kwargs(
                first, last_input=last,
            )
         == (first, last)
        )


    def test_optional_arguments():

  the test is still green because the :ref:`call<how to call a function with input>` that was made to the :ref:`args_and_kwargs function<test_args_and_kwargs>` that was in ``test_functions.py`` is now to the :ref:`args_and_kwargs function<test_args_and_kwargs>` in ``functions.py`` in the ``src`` folder_. When ``src.functions.args_and_kwargs`` is called, Python_ follows this path

  .. code-block:: shell

    src.functions.args_and_kwargs
    src
    └── functions.py
        └── def args_and_kwargs(first_input, last_input):
            └── return first_input, last_input

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move args_and_kwargs to functions.py'

----

*********************************************************************************
move optional_arguments function
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I comment out the :ref:`optional_arguments function<test_optional_arguments>` in :ref:`test_optional_arguments` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 2-5

    def test_optional_arguments():
        # def optional_arguments(
        #     first_input, last_input='doe',
        # ):
        #     return first_input, last_input

        first_name, last_name = 'jane', 'doe'

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'optional_arguments'
               is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use a :ref:`variable<what is a variable?>` to reroute the calls to the :ref:`optional_arguments function<test_optional_arguments>` from :ref:`test_optional_arguments` to the :ref:`optional_arguments function<test_optional_arguments>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 6-8

    def test_optional_arguments():
        # def optional_arguments(
        #     first_input, last_input='doe',
        # ):
        #     return first_input, last_input
        optional_arguments = (
            src.functions.optional_arguments
        )

        first_name, last_name = 'jane', 'doe'

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions'
                    has no attribute 'optional_arguments'.
                    Did you mean: 'positional_arguments'?

  because ``optional_arguments`` does not exist in ``functions.py``.

* I add a copy of the :ref:`optional_arguments function<test_optional_arguments>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 5-8

    def args_and_kwargs(first_input, last_input):
        return first_input, last_input


    def optional_arguments(
        first_input, last_input='doe',
    ):
        return first_input, last_input

  the test passes because the calls that were made to the :ref:`optional_arguments function<test_optional_arguments>` that was in ``test_functions.py`` are now made to the :ref:`optional_arguments function<test_optional_arguments>` in ``functions.py`` in the ``src`` folder_.

  When ``optional_arguments`` is called in :ref:`test_optional_arguments`, Python_ follows this path

  .. code-block:: shell

    optional_arguments = src.functions.optional_arguments

    src
    └── functions.py
        └── def optional_arguments(
                first_input, last_input='doe',
            ):
            └── return first_input, last_input

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented :ref:`optional_arguments function<test_optional_arguments>` from :ref:`test_optional_arguments` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 147

    def test_optional_arguments():
        optional_arguments = (
            src.functions.optional_arguments
        )

        first_name, last_name = 'jane', 'doe'

        assert (
            optional_arguments(
                first_name,
            )
         == (first_name, last_name)
        )

        first_name, blow = 'joe', 'blow'
        assert (
            optional_arguments(
                first_name, blow
            )
         == (first_name, blow)
        )

        first_name = 'john'
        assert (
            optional_arguments(
                first_input=first_name
            )
         == (first_name, last_name)
        )

        last_name = 'smith'
        assert (
            optional_arguments(
                last_input=last_name,
                first_input=first_name,
            )
         == (first_name, last_name)
        )


    def test_unknown_number_of_arguments():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move optional_arguments to functions.py'

----

*********************************************************************************
move unknown_number_of_arguments function
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I comment out the :ref:`unknown_number_of_arguments function<test_unknown_number_of_arguments>` in :ref:`test_unknown_number_of_arguments` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 187
    :emphasize-lines: 2-5

    def test_unknown_number_of_arguments():
        # def unknown_number_of_arguments(
        #     *positional_arguments, **keyword_arguments
        # ):
        #     return positional_arguments, keyword_arguments

        a_tuple = (0, 1)

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'unknown_number_of_arguments'
              is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use a :ref:`variable<what is a variable?>` to reroute the calls to the :ref:`unknown_number_of_arguments function<test_unknown_number_of_arguments>` from :ref:`test_unknown_number_of_arguments` to the :ref:`unknown_number_of_arguments function<test_unknown_number_of_arguments>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 187
    :emphasize-lines: 6-8

    def test_unknown_number_of_arguments():
        # def unknown_number_of_arguments(
        #     *positional_arguments, **keyword_arguments
        # ):
        #     return positional_arguments, keyword_arguments
        unknown_number_of_arguments = (
            src.functions.unknown_number_of_arguments
        )

        a_tuple = (0, 1)

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions'
                    has no attribute 'unknown_number_of_arguments'

  because I have not yet added ``unknown_number_of_arguments`` to ``functions.py``.

* I add a copy of the :ref:`unknown_number_of_arguments function<test_unknown_number_of_arguments>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 5-8

    def optional_arguments(
        first_input, last_input='doe',
    ):
        return first_input, last_input


    def unknown_number_of_arguments(
        *positional_arguments, **keyword_arguments
    ):
        return positional_arguments, keyword_arguments

  the test passes because the calls that were made to the :ref:`unknown_number_of_arguments function<test_unknown_number_of_arguments>` that was in ``test_functions.py`` are now made to the :ref:`unknown_number_of_arguments function<test_unknown_number_of_arguments>` in ``functions.py`` in the ``src`` folder_.

  When ``unknown_number_of_arguments`` is called in :ref:`test_unknown_number_of_arguments`, Python_ follows this path

  .. code-block:: shell

    unknown_number_of_arguments = (
        src.functions.unknown_number_of_arguments
    )

    src
    └── functions.py
        └── def unknown_number_of_arguments(
                *positional_arguments, **keyword_arguments
            ):
            └── return positional_arguments, keyword_arguments

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented :ref:`unknown_number_of_arguments function<test_unknown_number_of_arguments>` from :ref:`test_unknown_number_of_arguments` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 187

    def test_unknown_number_of_arguments():
        unknown_number_of_arguments = (
            src.functions.unknown_number_of_arguments
        )

        a_tuple = (0, 1)
        a_dictionary = {'a': 2, 'b': 3}
        assert (
            unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            )
         == (a_tuple, a_dictionary)
        )

        a_tuple = (0, 1)
        a_dictionary = {'a': 2, 'b': 3, 'c': 4}
        assert (
            unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            )
         == (a_tuple, a_dictionary)
        )

        a_tuple = (0, 1, 2)
        a_dictionary = {'a': 3, 'b': 4, 'c': 5}
        assert (
            unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            )
         == (a_tuple, a_dictionary)
        )

        a_tuple = (0, 1, 2, 'n')
        assert (
            unknown_number_of_arguments(*a_tuple)
         == (a_tuple, {})
        )

        a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
        assert (
            unknown_number_of_arguments(**a_dictionary)
         == ((), a_dictionary)
        )

        assert (
            unknown_number_of_arguments()
         == ((), {})
        )


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # SyntaxError
    # ModuleNotFoundError
    # AttributeError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move unknown_number_of_arguments to functions.py'

----

*********************************************************************************
test_functions
*********************************************************************************

I can write the :ref:`functions<what is a function?>` that make the tests pass (except for :ref:`test_why_use_a_function` which I left alone) without looking at ``test_functions.py`` since the solutions are now separate from the tests.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I close ``test_functions.py``

* I delete all the text in ``functions.py`` and the terminal_ shows 11 failures. I start with the last :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    FAILED ...::test_making_a_function_w_pass -
        AttributeError: module 'src.functions'
                        has no attribute 'w_pass'
    FAILED ...::test_making_a_function_w_return -
        AttributeError: module 'src.functions'
                        has no attribute 'w_return'
    FAILED ...::test_making_a_function_w_return_none -
        AttributeError: module 'src.functions'
                        has no attribute 'w_return_none'
    FAILED ...::test_what_happens_after_functions_return -
        AttributeError: module 'src.functions'
                        has no attribute 'return_lea...
    FAILED ...::test_constant_function -
        AttributeError: module 'src.functions'
                        has no attribute 'constant'
    FAILED ...::test_identity_function -
        AttributeError: module 'src.functions'
                        has no attribute 'identity'
    FAILED ...::test_positional_arguments -
        AttributeError: module 'src.functions'
                        has no attribute 'positional_arguments'
    FAILED ...::test_keyword_arguments -
        AttributeError: module 'src.functions'
                        has no attribute 'keyword_arguments'
    FAILED ...::test_args_and_kwargs -
        AttributeError: module 'src.functions'
                        has no attribute 'args_and_kwargs'
    FAILED ...::test_optional_arguments -
        AttributeError: module 'src.functions'
                        has no attribute 'optional_arguments'
    FAILED ...::test_unknown_number_of_arguments -
        AttributeError: module 'src.functions'
                        has no attribute 'unknown_nu...
    ============= 11 failed, 1 passed in A.BCs ==============

  Can you make the tests pass without looking at how I solve it below? You can come back to compare solutions when you are done or if you get stuck.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* Starting with the last :ref:`Exception<errors>`, I add a :ref:`function definition<how to make a function>` for :ref:`unknown_number_of_arguments<test_unknown_number_of_arguments>` to ``functions.py`` in the ``src`` folder_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def unknown_number_of_arguments():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unknown_number_of_arguments() got an
               unexpected keyword argument 'a'

* I add ``a`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # def unknown_number_of_arguments():
    def unknown_number_of_arguments(a):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unknown_number_of_arguments() got
               multiple values for argument 'a'

  which means it got called with ``a`` as a :ref:`keyword argument<test_keyword_arguments>` and since I have it as the first position, Python_ reads it as two values for the same argument.

* I try another argument in the parentheses before ``a``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    # def unknown_number_of_arguments():
    # def unknown_number_of_arguments(a):
    def unknown_number_of_arguments(z, a):
        return None

  the terminal_ still shows :ref:`TypeError<what causes TypeError?>`

* I use a :ref:`starred expression<single starred expressions>` to make the :ref:`function<what is a function?>` any number of :ref:`positional_arguments<test_positional_arguments>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-6

    # def unknown_number_of_arguments():
    # def unknown_number_of_arguments(a):
    # def unknown_number_of_arguments(z, a):
    def unknown_number_of_arguments(
        *positional, a
    ):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unknown_number_of_arguments() got
               an unexpected keyword argument 'b'

* I add ``b`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    # def unknown_number_of_arguments():
    # def unknown_number_of_arguments(a):
    # def unknown_number_of_arguments(z, a):
    def unknown_number_of_arguments(
        # *positional, a
        *positional, a, b
    ):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == ((0, 1), {'a': 2, 'b': 3})

* I copy (:kbd:`ctrl/command+c`) the tuple_ from the right side in the terminal_ then paste it (:kbd:`ctrl/command+v`) to replace :ref:`the return statement`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9

    # def unknown_number_of_arguments():
    # def unknown_number_of_arguments(a):
    # def unknown_number_of_arguments(z, a):
    def unknown_number_of_arguments(
        # *positional, a
        *positional, a, b
    ):
        # return None
        return ((0, 1), {'a': 2, 'b': 3})

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unknown_number_of_arguments() got
               an unexpected keyword argument 'c'

* I add ``c`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    # def unknown_number_of_arguments():
    # def unknown_number_of_arguments(a):
    # def unknown_number_of_arguments(z, a):
    def unknown_number_of_arguments(
        # *positional, a
        # *positional, a, b
        *positional, a, b, c
    ):
        # return None
        return ((0, 1), {'a': 2, 'b': 3})

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unknown_number_of_arguments() missing
               1 required keyword-only argument: 'c'.

  because something called the :ref:`function<what is a function?>` without a value for ``c``

* I make ``c`` an :ref:`optional argument<test_optional_arguments>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    # def unknown_number_of_arguments():
    # def unknown_number_of_arguments(a):
    # def unknown_number_of_arguments(z, a):
    def unknown_number_of_arguments(
        # *positional, a
        # *positional, a, b
        # *positional, a, b, c
        *positional, a, b, c=None
    ):
        # return None
        return ((0, 1), {'a': 2, 'b': 3})

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ((0, 1), {'a': 2, 'b': 3})
                        == ((0, 1), {'a'...': 3, 'c': 4})

* I change the :ref:`return statement<the return statement>` to see the difference between the input and the expected output

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-12

    # def unknown_number_of_arguments():
    # def unknown_number_of_arguments(a):
    # def unknown_number_of_arguments(z, a):
    def unknown_number_of_arguments(
        # *positional, a
        # *positional, a, b
        # *positional, a, b, c
        *positional, a, b, c=None
    ):
        # return None
        # return ((0, 1), {'a': 2, 'b': 3})
        return positional, a, b, c

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ((0, 1), 2, 3, None)
                        == ((0, 1), {'a': 2, 'b': 3})

  - The test expects a tuple_ with a tuple_ and a :ref:`dictionary<what is a dictionary?>`.
  - The :ref:`function<what is a function?>` returns a tuple_ with a tuple_ and three values.

* I change :ref:`the return statement` back

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-12

    # def unknown_number_of_arguments():
    # def unknown_number_of_arguments(a):
    # def unknown_number_of_arguments(z, a):
    def unknown_number_of_arguments(
        # *positional, a
        # *positional, a, b
        # *positional, a, b, c
        *positional, a, b, c=None
    ):
        # return None
        return ((0, 1), {'a': 2, 'b': 3})
        # return positional, a, b, c

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ((0, 1), {'a': 2, 'b': 3})
                        == ((0, 1), {'a'...': 3, 'c': 4})

  the :ref:`dictionaries<what is a dictionary?>` are different.

* I use a :ref:`double starred expression<double starred expressions>` in the parentheses to make the :ref:`function<what is a function?>` take any number of :ref:`keyword_arguments<test_keyword_arguments>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9

    # def unknown_number_of_arguments():
    # def unknown_number_of_arguments(a):
    # def unknown_number_of_arguments(z, a):
    def unknown_number_of_arguments(
        # *positional, a
        # *positional, a, b
        # *positional, a, b, c
        # *positional, a, b, c=None
        *positional, **keyword
    ):
        # return None
        return ((0, 1), {'a': 2, 'b': 3})
        # return positional, a, b, c

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ((0, 1), {'a': 2, 'b': 3})
                        == ((0, 1), {'a'...': 3, 'c': 4})

* I return the inputs

  .. code-block:: python
    :linenos:
    :emphasize-lines: 12, 14

    # def unknown_number_of_arguments():
    # def unknown_number_of_arguments(a):
    # def unknown_number_of_arguments(z, a):
    def unknown_number_of_arguments(
        # *positional, a
        # *positional, a, b
        # *positional, a, b, c
        # *positional, a, b, c=None
        *positional, **keyword
    ):
        # return None
        # return ((0, 1), {'a': 2, 'b': 3})
        # return positional, a, b, c
        return positional, keyword

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'optional_arguments'

* I add a :ref:`function definition<how to make a function>` for :ref:`optional_arguments<test_optional_arguments>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4-5

        return positional, keyword


    def optional_arguments():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: optional_arguments() takes
               0 positional arguments but 1 was given

* I add a name to allow the :ref:`function<what is a function?>` take input

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1-2

    # def optional_arguments():
    def optional_arguments(argument):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == ('jane', 'doe')

* I copy (:kbd:`ctrl/command+c`) the value from the terminal_ and paste it (:kbd:`ctrl/command+v`) to replace :ref:`the return statement`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3-4

    # def optional_arguments():
    def optional_arguments(argument):
        # return None
        return ('jane', 'doe')

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: optional_arguments() takes
               1 positional argument but 2 were given

* I add another name to the parentheses

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2-3

    # def optional_arguments():
    # def optional_arguments(argument):
    def optional_arguments(argument, argument_b):
        # return None
        return ('jane', 'doe')

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: optional_arguments() missing
               1 required positional argument: 'argument_b'

* I make the argument :ref:`optional<test_optional_arguments>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3-4

    # def optional_arguments():
    # def optional_arguments(argument):
    # def optional_arguments(argument, argument_b):
    def optional_arguments(argument, argument_b=None):
        # return None
        return ('jane', 'doe')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('jane', 'doe')
                        == ('joe', 'blow')

* I change the :ref:`return statement<the return statement>` of :ref:`optional_arguments<test_optional_arguments>` to see the difference between the input and the expected output

  .. code-block:: python
    :lineno-start:

    # def optional_arguments():
    # def optional_arguments(argument):
    # def optional_arguments(argument, argument_b):
    def optional_arguments(argument, argument_b=None):
        # return None
        # return ('jane', 'doe')
        return argument, argument_b

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('jane', None) == ('jane', 'doe')

  the :ref:`function<what is a function?>` returned a tuple_ with the first argument and the :ref:`default value<test_optional_arguments>` of ``argument_b``.

* I change the :ref:`default value<test_optional_arguments>` to ``'doe'``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 4-5

    # def optional_arguments():
    # def optional_arguments(argument):
    # def optional_arguments(argument, argument_b):
    # def optional_arguments(argument, argument_b=None):
    def optional_arguments(argument, argument_b='doe'):
        # return None
        # return ('jane', 'doe')
        return argument, argument_b

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

     TypeError: optional_arguments() got
                an unexpected keyword argument 'first_input'

* I add the name in parentheses

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5-8

    # def optional_arguments():
    # def optional_arguments(argument):
    # def optional_arguments(argument, argument_b):
    # def optional_arguments(argument, argument_b=None):
    # def optional_arguments(argument, argument_b='doe'):
    def optional_arguments(
        argument, argument_b='doe', first_input
    ):
        # return None
        # return ('jane', 'doe')
        return argument, argument_b

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default
         follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I change the order of the arguments

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 7-9

    # def optional_arguments():
    # def optional_arguments(argument):
    # def optional_arguments(argument, argument_b):
    # def optional_arguments(argument, argument_b=None):
    # def optional_arguments(argument, argument_b='doe'):
    def optional_arguments(
        # argument, argument_b='doe', first_input
        argument, first_input,
        argument_b='doe',
    ):
        # return None
        # return ('jane', 'doe')
        return argument, argument_b

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: optional_arguments() missing
               1 required positional argument: 'first_input'

* I make ``first_input`` the first argument to see if the problem is the position it is in

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 8-9

    # def optional_arguments():
    # def optional_arguments(argument):
    # def optional_arguments(argument, argument_b):
    # def optional_arguments(argument, argument_b=None):
    # def optional_arguments(argument, argument_b='doe'):
    def optional_arguments(
        # argument, argument_b='doe', first_input
        # argument, first_input,
        first_input, argument,
        argument_b='doe',
    ):
        # return None
        # return ('jane', 'doe')
        return argument, argument_b

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: optional_arguments() missing
               1 required positional argument: 'argument'

* I make ``argument`` :ref:`optional<test_optional_arguments>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 9-10


    # def optional_arguments():
    # def optional_arguments(argument):
    # def optional_arguments(argument, argument_b):
    # def optional_arguments(argument, argument_b=None):
    # def optional_arguments(argument, argument_b='doe'):
    def optional_arguments(
        # argument, argument_b='doe', first_input
        # argument, first_input,
        # first_input, argument,
        first_input, argument=None,
        argument_b='doe',
    ):
        # return None
        # return ('jane', 'doe')
        return argument, argument_b

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert (None, 'doe')
                        == ('jane', 'doe')

  the :ref:`function<what is a function?>` returned a tuple_ with the :ref:`default value<test_optional_arguments>` of ``argument``

* I add ``first_input`` to :ref:`the return statement`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 15-16

    # def optional_arguments():
    # def optional_arguments(argument):
    # def optional_arguments(argument, argument_b):
    # def optional_arguments(argument, argument_b=None):
    # def optional_arguments(argument, argument_b='doe'):
    def optional_arguments(
        # argument, argument_b='doe', first_input
        # argument, first_input,
        # first_input, argument,
        first_input, argument=None,
        argument_b='doe',
    ):
        # return None
        # return ('jane', 'doe')
        # return argument, argument_b
        return first_input, argument, argument_b

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('jane', None, 'doe')
                        == ('jane', 'doe')

  it looks like I do not need the ``argument`` parameter.

* I remove ``argument`` from the parentheses and :ref:`return statement<the return statement>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 10-11, 17-18

    # def optional_arguments():
    # def optional_arguments(argument):
    # def optional_arguments(argument, argument_b):
    # def optional_arguments(argument, argument_b=None):
    # def optional_arguments(argument, argument_b='doe'):
    def optional_arguments(
        # argument, argument_b='doe', first_input
        # argument, first_input,
        # first_input, argument,
        # first_input, argument=None,
        first_input,
        argument_b='doe',
    ):
        # return None
        # return ('jane', 'doe')
        # return argument, argument_b
        # return first_input, argument, argument_b
        return first_input, argument_b

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: optional_arguments() got
               an unexpected keyword argument 'last_input'.
               Did you mean 'first_input'?

* I add the name in the parentheses

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 12-13

    # def optional_arguments():
    # def optional_arguments(argument):
    # def optional_arguments(argument, argument_b):
    # def optional_arguments(argument, argument_b=None):
    # def optional_arguments(argument, argument_b='doe'):
    def optional_arguments(
        # argument, argument_b='doe', first_input
        # argument, first_input,
        # first_input, argument,
        # first_input, argument=None,
        first_input,
        # argument_b='doe',
        argument_b='doe', last_input,
    ):
        # return None
        # return ('jane', 'doe')
        # return argument, argument_b
        # return first_input, argument, argument_b
        return first_input, argument_b

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default
         follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I give the argument a :ref:`default value<test_optional_arguments>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 13-14

    # def optional_arguments():
    # def optional_arguments(argument):
    # def optional_arguments(argument, argument_b):
    # def optional_arguments(argument, argument_b=None):
    # def optional_arguments(argument, argument_b='doe'):
    def optional_arguments(
        # argument, argument_b='doe', first_input
        # argument, first_input,
        # first_input, argument,
        # first_input, argument=None,
        first_input,
        # argument_b='doe',
        # argument_b='doe', last_input,
        argument_b='doe', last_input=None,
    ):
        # return None
        # return ('jane', 'doe')
        # return argument, argument_b
        # return first_input, argument, argument_b
        return first_input, argument_b

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('john', 'doe')
                        == ('john', 'smith')

  the last names are different.

* I add ``last_input`` to :ref:`the return statement`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 20-21

    # def optional_arguments():
    # def optional_arguments(argument):
    # def optional_arguments(argument, argument_b):
    # def optional_arguments(argument, argument_b=None):
    # def optional_arguments(argument, argument_b='doe'):
    def optional_arguments(
        # argument, argument_b='doe', first_input
        # argument, first_input,
        # first_input, argument,
        # first_input, argument=None,
        first_input,
        # argument_b='doe',
        # argument_b='doe', last_input,
        argument_b='doe', last_input=None,
    ):
        # return None
        # return ('jane', 'doe')
        # return argument, argument_b
        # return first_input, argument, argument_b
        # return first_input, argument_b
        return first_input, argument_b, last_input

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('jane', 'doe', None)
                        == ('jane', 'doe')

  I only need two inputs.

* I remove ``argument_b`` from the parentheses and :ref:`return statement<the return statement>`,  then change the :ref:`default value<test_optional_arguments>` of ``last_input`` to ``'doe'``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 14-15, 22-23

    # def optional_arguments():
    # def optional_arguments(argument):
    # def optional_arguments(argument, argument_b):
    # def optional_arguments(argument, argument_b=None):
    # def optional_arguments(argument, argument_b='doe'):
    def optional_arguments(
        # argument, argument_b='doe', first_input
        # argument, first_input,
        # first_input, argument,
        # first_input, argument=None,
        first_input,
        # argument_b='doe',
        # argument_b='doe', last_input,
        # argument_b='doe', last_input=None,
        last_input='doe',
    ):
        # return None
        # return ('jane', 'doe')
        # return argument, argument_b
        # return first_input, argument, argument_b
        # return first_input, argument_b
        # return first_input, argument_b, last_input
        return first_input, last_input

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'args_and_kwargs'

* I add a :ref:`function definition<how to make a function>` for :ref:`args_and_kwargs<test_args_and_kwargs>`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 4-5

        return first_input, last_input


    def args_and_kwargs():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: args_and_kwargs() got
               an unexpected keyword argument 'last_input'

* I add ``last_input`` in parentheses

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1-2

    # def args_and_kwargs():
    def args_and_kwargs(last_input):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: args_and_kwargs() got
               multiple values for argument 'last_input'

  which means it got called with ``last_input`` as a :ref:`positional <test_keyword_arguments>` and :ref:`keyword argument<test_keyword_arguments>`. Since I have it as the first position, Python_ reads it as two values for the same argument.

* I add another name before ``last_input``

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2-3

    # def args_and_kwargs():
    # def args_and_kwargs(last_input):
    def args_and_kwargs(argument, last_input):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == ('first', 'last')

* I :ref:`return<the return statement>` the inputs

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 4-5

    # def args_and_kwargs():
    # def args_and_kwargs(last_input):
    def args_and_kwargs(argument, last_input):
        # return None
        return argument, last_input

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'keyword_arguments'

* I add a :ref:`function definition<how to make a function>` for :ref:`keyword_arguments<test_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4-5

        return argument, last_input


    def keyword_arguments():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: keyword_arguments() got
               an unexpected keyword argument 'first_input'

* I add ``first_input`` to the parentheses

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 1-2

    # def keyword_arguments():
    def keyword_arguments(first_input):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: keyword_arguments() got
               an unexpected keyword argument 'last_input'.
               Did you mean 'first_input'?

* I add ``last_input`` to the parentheses

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-3

    # def keyword_arguments():
    # def keyword_arguments(first_input):
    def keyword_arguments(first_input, last_input):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == ('first', 'last')0

* I copy and paste the tuple_ from the terminal_ as :ref:`the return statement`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 4-5

    # def keyword_arguments():
    # def keyword_arguments(first_input):
    def keyword_arguments(first_input, last_input):
        # return None
        return ('first', 'last')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('first', 'last') == (1, 0)

* I change :ref:`the return statement` to see the difference between the inputs and the output

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 5-6

    # def keyword_arguments():
    # def keyword_arguments(first_input):
    def keyword_arguments(first_input, last_input):
        # return None
        # return ('first', 'last')
        return first_input, last_input

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions'
                    has no attribute 'positional_arguments'.
                    Did you mean: 'optional_arguments'?

* I add a :ref:`function definition<how to make a function>` for :ref:`positional_arguments<test_positional_arguments>`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 4-5

        return first_input, last_input


    def positional_arguments():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: positional_arguments() got
               an unexpected keyword argument 'last_input'

* I add the name to the parentheses in the :ref:`definition<how to make a function>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 1-2

    # def positional_arguments():
    def positional_arguments(last_input):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: positional_arguments() got
               an unexpected keyword argument 'first_input'.
               Did you mean 'last_input'?

* I add ``last_input`` to the parentheses

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 2-3

    # def positional_arguments():
    # def positional_arguments(last_input):
    def positional_arguments(last_input, first_input):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None
        == ({3, 1, 2, 'n'}, {'key': 'value'})

* I copy (:kbd:`ctrl/command+c`) and paste (:kbd:`ctrl/command+v`) the value from the terminal_ to change :ref:`the return statement`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 4-5

    # def positional_arguments():
    # def positional_arguments(last_input):
    def positional_arguments(last_input, first_input):
        # return None
        return ({3, 1, 2, 'n'}, {'key': 'value'})

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        assert ({1, 2, 3, 'n...ey': 'value'})
            == ('first', 'last')

* I change :ref:`the return statement` to see the difference between the inputs and output

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 5-6

    # def positional_arguments():
    # def positional_arguments(last_input):
    def positional_arguments(last_input, first_input):
        # return None
        # return ({3, 1, 2, 'n'}, {'key': 'value'})
        return last_input, first_input

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        assert ({'key': 'val...3, 1, 'n', 2})
            == ({3, 1, 'n', ...ey': 'value'})

  - The order is reversed.
  - :ref:`I want better error messages<another way to write tests>`.

* I change the order of the inputs in the :ref:`the return statement`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 6-7

    # def positional_arguments():
    # def positional_arguments(last_input):
    def positional_arguments(last_input, first_input):
        # return None
        # return ({3, 1, 2, 'n'}, {'key': 'value'})
        # return last_input, first_input
        return first_input, last_input

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('last', 'first')
                        == ('first', 'last')

  the order is reversed.

* I change the order of inputs in the parentheses

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 3-4

    # def positional_arguments():
    # def positional_arguments(last_input):
    # def positional_arguments(last_input, first_input):
    def positional_arguments(first_input, last_input):
        # return None
        # return ({3, 1, 2, 'n'}, {'key': 'value'})
        # return last_input, first_input
        return first_input, last_input

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'identity'

* I add a :ref:`function definition<how to make a function>` for :ref:`identity<test_identity_function>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 4-5

        return first_input, last_input


    def identity():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: identity() takes
               0 positional arguments but 1 was given

* I add a name to the :ref:`function definition<how to make a function>` to make it take input

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 1-2

    # def identity():
    def identity(argument):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == object

* I change :ref:`the return statement` to give the test what it wants

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 3-4

    # def identity():
    def identity(argument):
        # return None
        return object

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: assert <class 'object'> == None

* I :ref:`return<the return statement>` the input

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 4-5

    # def identity():
    def identity(argument):
        # return None
        # return object
        return argument

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'constant'

* I add a :ref:`function definition<how to make a function>` for :ref:`constant<test_constant_function>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 4-5

        return argument


    def constant():
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == 'the same thing'

* I copy and paste the value from the terminal_ as :ref:`the return statement`

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 2-3

    def constant():
        # return None
        return 'the same thing'

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'return_leaves_the_function'

* I add a :ref:`function definition<how to make a function>` for :ref:`return_leaves_the_function<test_what_happens_after_functions_return>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 4-5

        return 'the same thing'


    def return_leaves_the_function():
        return None

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'w_return_none'

* I add a :ref:`function definition<how to make a function>` for :ref:`w_return_none<test_making_a_function_w_return_none>`

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 5-6

    def return_leaves_the_function():
        return None


    def w_return_none():
        return None

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'w_return'

* I add a :ref:`function definition<how to make a function>` for :ref:`w_return<test_making_a_function_w_return>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 5-6

    def w_return_none():
        return None


    def w_return():
        return None

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'w_pass'

* I add a :ref:`function definition<how to make a function>` for :ref:`w_pass<test_making_a_function_w_pass>`

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 5-6

    def w_return():
        return None


    def w_pass():
        return None

  all tests are passing!

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
      :linenos:

    def unknown_number_of_arguments(
        *positional, **keyword
    ):
        return positional, keyword


    def optional_arguments(
        first_input, last_input='doe',
    ):
        return first_input, last_input


    def args_and_kwargs(argument, last_input):
        return argument, last_input


    def keyword_arguments(first_input, last_input):
        return first_input, last_input


    def positional_arguments(first_input, last_input):
        return first_input, last_input


    def identity(argument):
        return argument


    def constant():
        return 'the same thing'


    def return_leaves_the_function():
        return None


    def w_return_none():
        return None


    def w_return():
        return None


    def w_pass():
        return None

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'test functions'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``functions.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``functions``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

:ref:`I can write solutions in a different module from the tests<separate and equal>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<separate and equal functions: tests and solutions>`

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
* :ref:`I know how to separate tests from solutions<separate and equal>`.

:ref:`would you like to separate the tests from the solution in the telephone project?<separate and equal telephone>`

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