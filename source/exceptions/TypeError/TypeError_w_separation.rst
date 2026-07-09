.. meta::
  :description: Separate tests from solutions (keep them "separate and equal") in the type_error project using TDD. Move the functions out of test_type_error.py into src/type_error.py. Use "import src.type_error" then reroute calls to src.type_error.function_00 etc, mkdir src, touch src/type_error.py, "remove the commented lines" (local defs left in test). See real errors while separating: "NameError: name 'src' is not defined", "ModuleNotFoundError: No module named 'src'", "ModuleNotFoundError: No module named 'src.type_error'", "AttributeError: module 'src.type_error' has no attribute 'function_00'". Finish with all 9 functions (function_00 through function_08 with special signatures for _02/_07/_08) in src/type_error.py and three tests calling exclusively via the src. prefix: test_type_error_w_positional_arguments, test_type_error_w_keyword_arguments, test_type_error_w_args_and_kwargs (including mixed positional+keyword calls like function_08('positional', argument='keyword')). uv run pytest-watcher . --now, git commits after each step. Review lesson: I can write solutions in a different module from the tests. Jacob Itegboje Pumping Python TDD series.
  :keywords: Jacob Itegboje, Pumping Python, separate and equal TypeError, separate tests from solutions, src/type_error.py, import src.type_error, src.type_error.function_00, "NameError: name 'src' is not defined", "ModuleNotFoundError: No module named 'src'", "ModuleNotFoundError: No module named 'src.type_error'", "AttributeError: module 'src.type_error' has no attribute 'function_00'", test_type_error_w_separation, test_type_error_w_positional_arguments, test_type_error_w_keyword_arguments, test_type_error_w_args_and_kwargs, remove the commented lines, move functions to src folder, function_00 to function_08, src package layout, TDD separation refactor, uv pytest-watcher, git commit, "I can write solutions in a different module from the tests", TypeError continuation chapter, python src type_error

.. include:: ../../links.rst

.. _TypeError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError

#################################################################################
separate and equal TypeError
#################################################################################

----

I want to move the :ref:`functions<what is a function?>` to ``type_error.py`` in the ``src`` folder_ so that I can keep the tests and solutions separate.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/type_error/tests/test_type_error_w_separation.py
  :language: python
  :linenos:

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`type_error folder<what causes TypeError?>` in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd type_error

  the terminal_ shows I am in the :ref:`type_error folder<what causes TypeError?>`

  .. code-block:: python

    .../pumping_python/type_error

* I open ``test_type_error.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    test_type_error.py ...                              [100%]

    =================== 3 passed in X.YZs ====================

----

*********************************************************************************
mass migration
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the :ref:`call<how to call a function with input>` to ``function_00`` in :ref:`test_type_error_w_positional_arguments` to a :ref:`call<how to call a function with input>` to ``function_00`` of ``type_error.py`` in the ``src`` folder_

.. code-block:: python
  :lineno-start: 40
  :emphasize-lines: 1-2

  def test_type_error_w_positional_arguments():
      # function_00('a')
      src.type_error.function_00('a')
      function_01('a', 'b')
      function_02('a', 'b', 'c')
      function_03('a', 'b', 'c', 'd')
      function_04('a')
      function_05('a', 'b')
      function_06('a', 'b', 'c')
      function_07('a', 'b', 'c', 'd')
      function_08('last', 'one')


  def test_type_error_w_keyword_arguments():

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'src' is not defined

because ``src`` is not defined in ``test_type_error.py``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ at the top of ``test_type_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.type_error


    def function_00(the_input):
        return None

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src'

  because there is nothing named ``src`` in this project.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 5
    :emphasize-text: ModuleNotFoundError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # ModuleNotFoundError

* I open another terminal_ then make sure I am in the :ref:`type_error folder<what causes TypeError?>`

* I use mkdir_ to make a folder_ named ``src``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir src

* I go back to the terminal_ where the tests are running.

* I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) on the keyboard in ``test_type_error.py`` to run the tests again and the terminal_ shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.type_error'

  because there is nothing in the ``src`` folder_ named ``type_error``.

* I go to the second terminal_ I opened, then use touch_ to make ``type_error.py`` in the ``src`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    touch src/type_error.py

* I go back to the terminal_ where the tests are running and it shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.type_error'
                    has no attribute 'function_00'

  because there is nothing in ``type_error.py`` in the ``src`` folder_ with the name ``function_00``.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 6
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # ModuleNotFoundError
    # AttributeError

* I open ``type_error.py`` from the ``src`` folder_

* I add a :ref:`definition<how to make a function>` for ``function_00`` to ``type_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def function_00():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_00() takes
               0 positional arguments but 1 was given

* I add a name to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    # def function_00():
    def function_00(one):
        return None

  the test passes because

  - When ``import src.type_error`` runs, Python_ brings in an :ref:`object<what is a class?>` for the ``type_error.py`` file_ from the ``src`` folder_ so I can use it in ``test_type_error.py`` as ``src.type_error``.
  - When ``src.type_error.function_00`` is :ref:`called<how to call a function with input>`, Python_ :ref:`calls<how to call a function with input>` the ``function_00`` :ref:`function<what is a function?>` from the :ref:`object<what is a class?>` it imported for the ``type_error.py`` file_ from the ``src`` folder_ (``src.type_error``).

  I think of ``src.type_error.function_00`` like an address

  .. code-block:: shell

    src.type_error.function_00
    src
    └── type_error.py
        └── def function_00(one):
            └── return None

  - ``function_00`` is something in ``type_error``, in this case it is a :ref:`function<what is a function?>` in ``type_error``
  - ``type_error`` is something in ``src``, in this case it is ``type_error.py`` (a :ref:`module<what is a module?>`) in the ``src`` folder_
  - ``src`` is something Python_ can import (a :ref:`module<what is a module?>`, `Python package`_ or folder_)
  - ``function_00`` is now an :ref:`attribute/property<what is a class attribute?>` of ``type_error.py`` in the ``src`` folder_. I can use it from outside the file_ with ``src.type_error.function_00``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to ``function_01`` in :ref:`test_type_error_w_positional_arguments` to a :ref:`call<how to call a function with input>` to ``function_01`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 4-5

    def test_type_error_w_positional_arguments():
        # function_00('a')
        src.type_error.function_00('a')
        # function_01('a', 'b')
        src.type_error.function_01('a', 'b')
        function_02('a', 'b', 'c')

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'function_01'.
                    Did you mean: 'function_00'?

* I add a :ref:`function definition<how to make a function>` for ``function_01`` to ``type_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    # def function_00():
    def function_00(one):
        return None


    def function_01():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_01() takes
               0 positional arguments but 2 were given

* I add two names in the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    # def function_00():
    def function_00(one):
        return None


    # def function_01():
    def function_01(one, two):
        return None

  the test passes because Python_ follows this path when ``src.type_error.function_01`` is :ref:`called<how to call a function with input>`

  .. code-block:: shell

    src.type_error.function_01
    src
    └── type_error.py
        └── def function_01(one, two):
            └── return None

* I change the :ref:`call<how to call a function with input>` to ``function_02`` in :ref:`test_type_error_w_positional_arguments` to a :ref:`call<how to call a function with input>` to ``function_02`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 6-7

    def test_type_error_w_positional_arguments():
        # function_00('a')
        src.type_error.function_00('a')
        # function_01('a', 'b')
        src.type_error.function_01('a', 'b')
        # function_02('a', 'b', 'c')
        src.type_error.function_02('a', 'b', 'c')
        function_03('a', 'b', 'c', 'd')

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'function_02'.
                    Did you mean: 'function_00'?

* I add a :ref:`function definition<how to make a function>` for ``function_02`` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 6-7

    # def function_01():
    def function_01(one, two):
        return None


    def function_02():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_02() takes
               0 positional arguments but 3 were given

* I add three names to the parentheses

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 6-7

    # def function_01():
    def function_01(one, two):
        return None


    # def function_02():
    def function_02(one, two, three):
        return None

  the test passes because Python_ follows this path when ``src.type_error.function_02`` is :ref:`called<how to call a function with input>`

  .. code-block:: shell

    src.type_error.function_02
    src
    └── type_error.py
        └── def function_02(one, two, three):
            └── return None

* I change the :ref:`call<how to call a function with input>` to ``function_03`` in :ref:`test_type_error_w_positional_arguments` to a :ref:`call<how to call a function with input>` to ``function_03`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 8-9

    def test_type_error_w_positional_arguments():
        # function_00('a')
        src.type_error.function_00('a')
        # function_01('a', 'b')
        src.type_error.function_01('a', 'b')
        # function_02('a', 'b', 'c')
        src.type_error.function_02('a', 'b', 'c')
        # function_03('a', 'b', 'c', 'd')
        src.type_error.function_03('a', 'b', 'c', 'd')
        function_04('a')

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'function_03'.
                    Did you mean: 'function_00'?

* I add a :ref:`function definition<how to make a function>` for ``function_03`` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 6-7

    # def function_02():
    def function_02(one, two, three):
        return None


    def function_03():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_03() takes
               0 positional arguments but 4 were given

* I add four names to the parentheses

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 6-7

    # def function_02():
    def function_02(one, two, three):
        return None


    # def function_03():
    def function_03(one, two, three, four):
        return None

  the test passes because Python_ follows this path when ``src.type_error.function_03`` is :ref:`called<how to call a function with input>`

  .. code-block:: shell

    src.type_error.function_03
    src
    └── type_error.py
        └── def function_03(one, two, three, four):
            └── return None

* I change the :ref:`call<how to call a function with input>` to ``function_04`` in :ref:`test_type_error_w_positional_arguments` to a :ref:`call<how to call a function with input>` to ``function_04`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 10-11

    def test_type_error_w_positional_arguments():
        # function_00('a')
        src.type_error.function_00('a')
        # function_01('a', 'b')
        src.type_error.function_01('a', 'b')
        # function_02('a', 'b', 'c')
        src.type_error.function_02('a', 'b', 'c')
        # function_03('a', 'b', 'c', 'd')
        src.type_error.function_03('a', 'b', 'c', 'd')
        # function_04('a')
        src.type_error.function_04('a')
        function_05('a', 'b')

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'function_04'.
                    Did you mean: 'function_00'?

* I add a :ref:`function definition<how to make a function>` for ``function_04`` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 6-7

    # def function_03():
    def function_03(one, two, three, four):
        return None


    def function_04():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_04() takes
               0 positional arguments but 1 was given

* I add ``one`` to the parentheses

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 6-7

    # def function_03():
    def function_03(one, two, three, four):
        return None


    # def function_04():
    def function_04(one):
        return None

  the test passes because Python_ follows this path when ``src.type_error.function_04`` is :ref:`called<how to call a function with input>`

  .. code-block:: shell

    src.type_error.function_04
    src
    └── type_error.py
        └── def function_04(one):
            └── return None

* I change the :ref:`call<how to call a function with input>` to ``function_05`` in :ref:`test_type_error_w_positional_arguments` to a :ref:`call<how to call a function with input>` to ``function_05`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 12-13

    def test_type_error_w_positional_arguments():
        # function_00('a')
        src.type_error.function_00('a')
        # function_01('a', 'b')
        src.type_error.function_01('a', 'b')
        # function_02('a', 'b', 'c')
        src.type_error.function_02('a', 'b', 'c')
        # function_03('a', 'b', 'c', 'd')
        src.type_error.function_03('a', 'b', 'c', 'd')
        # function_04('a')
        src.type_error.function_04('a')
        # function_05('a', 'b')
        src.type_error.function_05('a', 'b')
        function_06('a', 'b', 'c')

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'function_05'.
                    Did you mean: 'function_00'?

* I add a :ref:`function definition<how to make a function>` for ``function_05`` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 6-7

    # def function_04():
    def function_04(one):
        return None


    def function_05():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_05() takes
               0 positional arguments but 2 were given

* I add two names to the parentheses

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 6-7

    # def function_04():
    def function_04(one):
        return None


    # def function_05():
    def function_05(one, two):
        return None

  the test passes because Python_ follows this path when ``src.type_error.function_05`` is :ref:`called<how to call a function with input>`

  .. code-block:: shell

    src.type_error.function_05
    src
    └── type_error.py
        └── def function_05(one, two):
            └── return None

* I change the :ref:`call<how to call a function with input>` to ``function_06`` in :ref:`test_type_error_w_positional_arguments` to a :ref:`call<how to call a function with input>` to ``function_06`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 14-15

    def test_type_error_w_positional_arguments():
        # function_00('a')
        src.type_error.function_00('a')
        # function_01('a', 'b')
        src.type_error.function_01('a', 'b')
        # function_02('a', 'b', 'c')
        src.type_error.function_02('a', 'b', 'c')
        # function_03('a', 'b', 'c', 'd')
        src.type_error.function_03('a', 'b', 'c', 'd')
        # function_04('a')
        src.type_error.function_04('a')
        # function_05('a', 'b')
        src.type_error.function_05('a', 'b')
        # function_06('a', 'b', 'c')
        src.type_error.function_06('a', 'b', 'c')
        function_07('a', 'b', 'c', 'd')

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'function_06'.
                    Did you mean: 'function_00'?

* I add a :ref:`function definition<how to make a function>` for ``function_06`` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 6-7

    # def function_05():
    def function_05(one, two):
        return None


    def function_06():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_06() takes
               0 positional arguments but 3 were given

* I add three names to the parentheses

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 6-7

    # def function_05():
    def function_05(one, two):
        return None


    # def function_06():
    def function_06(one, two, three):
        return None

  the test passes because Python_ follows this path when ``src.type_error.function_06`` is :ref:`called<how to call a function with input>`

  .. code-block:: shell

    src.type_error.function_06
    src
    └── type_error.py
        └── def function_06(one, two, three):
            └── return None

* I change the :ref:`call<how to call a function with input>` to ``function_07`` in :ref:`test_type_error_w_positional_arguments` to a :ref:`call<how to call a function with input>` to ``function_07`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 16-17

    def test_type_error_w_positional_arguments():
        # function_00('a')
        src.type_error.function_00('a')
        # function_01('a', 'b')
        src.type_error.function_01('a', 'b')
        # function_02('a', 'b', 'c')
        src.type_error.function_02('a', 'b', 'c')
        # function_03('a', 'b', 'c', 'd')
        src.type_error.function_03('a', 'b', 'c', 'd')
        # function_04('a')
        src.type_error.function_04('a')
        # function_05('a', 'b')
        src.type_error.function_05('a', 'b')
        # function_06('a', 'b', 'c')
        src.type_error.function_06('a', 'b', 'c')
        # function_07('a', 'b', 'c', 'd')
        src.type_error.function_07('a', 'b', 'c', 'd')
        function_08('last', 'one')

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'function_07'.
                    Did you mean: 'function_00'?

* I add a :ref:`function definition<how to make a function>` for ``function_07`` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 6-7

    # def function_06():
    def function_06(one, two, three):
        return None


    def function_07():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_07() takes
               0 positional arguments but 4 were given

* I add four names to the parentheses

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 6-7

    # def function_06():
    def function_06(one, two, three):
        return None


    # def function_07():
    def function_07(one, two, three, four):
        return None

  the test passes because Python_ follows this path when ``src.type_error.function_07`` is :ref:`called<how to call a function with input>`

  .. code-block:: shell

    src.type_error.function_07
    src
    └── type_error.py
        └── def function_07(one, two, three, four):
            └── return None

* I change the :ref:`call<how to call a function with input>` to ``function_08`` in :ref:`test_type_error_w_positional_arguments` to a :ref:`call<how to call a function with input>` to ``function_08`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 18-19

    def test_type_error_w_positional_arguments():
        # function_00('a')
        src.type_error.function_00('a')
        # function_01('a', 'b')
        src.type_error.function_01('a', 'b')
        # function_02('a', 'b', 'c')
        src.type_error.function_02('a', 'b', 'c')
        # function_03('a', 'b', 'c', 'd')
        src.type_error.function_03('a', 'b', 'c', 'd')
        # function_04('a')
        src.type_error.function_04('a')
        # function_05('a', 'b')
        src.type_error.function_05('a', 'b')
        # function_06('a', 'b', 'c')
        src.type_error.function_06('a', 'b', 'c')
        # function_07('a', 'b', 'c', 'd')
        src.type_error.function_07('a', 'b', 'c', 'd')
        # function_08('last', 'one')
        src.type_error.function_08('last', 'one')


    def test_type_error_w_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'function_08'.
                    Did you mean: 'function_00'?

* I add a :ref:`function definition<how to make a function>` for ``function_08`` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 6-7

    # def function_07():
    def function_07(one, two, three, four):
        return None


    def function_08():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_08() takes
               0 positional arguments but 2 were given

* I add two names to the parentheses

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 6-7

    # def function_07():
    def function_07(one, two, three, four):
        return None


    # def function_08():
    def function_08(one, two):
        return None

  the test passes because Python_ follows this path when ``src.type_error.function_08`` is :ref:`called<how to call a function with input>`

  .. code-block:: shell

    src.type_error.function_08
    src
    └── type_error.py
        └── def function_08(one, two):
            └── return None

* I remove the commented lines from :ref:`test_type_error_w_positional_arguments` in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 43

    def test_type_error_w_positional_arguments():
        src.type_error.function_00('a')
        src.type_error.function_01('a', 'b')
        src.type_error.function_02('a', 'b', 'c')
        src.type_error.function_03('a', 'b', 'c', 'd')
        src.type_error.function_04('a')
        src.type_error.function_05('a', 'b')
        src.type_error.function_06('a', 'b', 'c')
        src.type_error.function_07('a', 'b', 'c', 'd')
        src.type_error.function_08('last', 'one')


    def test_type_error_w_keyword_arguments():

----

* I change the :ref:`call<how to call a function with input>` to ``function_00`` in :ref:`test_type_error_w_keyword_arguments` to a :ref:`call<how to call a function with input>` to ``function_00`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2-3

    def test_type_error_w_keyword_arguments():
        # function_00(the_input=0)
        src.type_error.function_00(the_input=0)
        function_01(
            first='first',
            second={'key': 'value'},
        )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_00() got
               an unexpected keyword argument 'the_input'

* I add ``the_input`` in the parentheses of the :ref:`definition<how to make a function that takes input>` of ``function_00`` in ``type_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    # def function_00():
    # def function_00(one):
    def function_00(one, the_input):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...::test_type_error_w_positional_arguments -
        TypeError: function_00() missing
                   1 required positional argument: 'the_input'
    FAILED ...::test_type_error_w_keyword_arguments -
        TypeError: function_00() missing
                   1 required positional argument: 'one'

  my change broke a test that was passing.

* I remove ``one`` from the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # def function_00():
    # def function_00(one):
    # def function_00(one, the_input):
    def function_00(the_input):
        return None

  the test passes.

* I change the :ref:`call<how to call a function with input>` to ``function_01`` in :ref:`test_type_error_w_keyword_arguments` to a :ref:`call<how to call a function with input>` to ``function_01`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 4-5

    def test_type_error_w_keyword_arguments():
        # function_00(the_input=0)
        src.type_error.function_00(the_input=0)
        # function_01(
        src.type_error.function_01(
            first='first',
            second={'key': 'value'},
        )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_01() got
               an unexpected keyword argument 'first'

* I add ``first`` in the parentheses of the :ref:`definition<how to make a function that takes input>` of ``function_01`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2-3

    # def function_01():
    # def function_01(one, two):
    def function_01(one, two, first):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...::test_type_error_w_positional_arguments -
        TypeError: function_01() missing
                   1 required positional argument: 'first'
    FAILED ...::test_type_error_w_keyword_arguments -
        TypeError: function_01() got
                   an unexpected keyword argument 'second'

  another change that broke a test that was passing.

* I add ``second`` to the parentheses

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3-4

    # def function_01():
    # def function_01(one, two):
    # def function_01(one, two, first):
    def function_01(one, two, first, second):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...::test_type_error_w_positional_arguments -
        TypeError: function_01() missing
                   2 required positional arguments:
                   'first' and 'second'
    FAILED ...::test_type_error_w_keyword_arguments -
        TypeError: function_01() missing
                   2 required positional arguments:
                   'one' and 'two'

* I remove ``one`` and ``two`` from the parentheses

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 4-5

    # def function_01():
    # def function_01(one, two):
    # def function_01(one, two, first):
    # def function_01(one, two, first, second):
    def function_01(first, second):
        return None

  the test passes.

* I change the :ref:`call<how to call a function with input>` to ``function_02`` in :ref:`test_type_error_w_keyword_arguments` to a :ref:`call<how to call a function with input>` to ``function_02`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 9-10

    def test_type_error_w_keyword_arguments():
        # function_00(the_input=0)
        src.type_error.function_00(the_input=0)
        # function_01(
        src.type_error.function_01(
            first='first',
            second={'key': 'value'},
        )
        # function_02(
        src.type_error.function_02(
            third=(0, 1, 2, 'n'),
            second=[0, 1, 2, 'n'],
            first={0, 1, 2, 'n'},
        )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_02() got
               an unexpected keyword argument 'third'

* I add ``third`` in the parentheses of the :ref:`definition<how to make a function that takes input>` of ``function_02`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2-3

    # def function_02():
    # def function_02(one, two, three):
    def function_02(one, two, three, third):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...::test_type_error_w_positional_arguments -
        TypeError: function_02() missing
                   1 required positional argument: 'third'
    FAILED ...::test_type_error_w_keyword_arguments -
        TypeError: function_02() got
                   an unexpected keyword argument 'second'

  I broke a test that was passing.

* I add ``second`` to the parentheses

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3-4

    # def function_02():
    # def function_02(one, two, three):
    # def function_02(one, two, three, third):
    def function_02(one, two, three, third, second):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...::test_type_error_w_positional_arguments -
        TypeError: function_02() missing
                   2 required positional arguments:
                   'third' and 'second'
    FAILED ...::test_type_error_w_keyword_arguments -
        TypeError: function_02() got
                   an unexpected keyword argument 'first'

* I add ``first`` to the parentheses

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4-8

    # def function_02():
    # def function_02(one, two, three):
    # def function_02(one, two, three, third):
    # def function_02(one, two, three, third, second):
    def function_02(
        one, two, three,
        third, second, first
    ):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...::test_type_error_w_positional_arguments -
        TypeError: function_02() missing
                   3 required positional arguments:
                   'third', 'second', and 'first'
    FAILED ...::test_type_error_w_keyword_arguments -
        TypeError: function_02() missing
                   3 required positional arguments:
                   'one', 'two', and 'three

* I remove ``one``, ``two`` and ``three`` from the parentheses

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 6

    # def function_02():
    # def function_02(one, two, three):
    # def function_02(one, two, three, third):
    # def function_02(one, two, three, third, second):
    def function_02(
        # one, two, three,
        third, second, first
    ):
        return None

  the test passes.

* I change the :ref:`call<how to call a function with input>` to ``function_03`` in :ref:`test_type_error_w_keyword_arguments` to a :ref:`call<how to call a function with input>` to ``function_03`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 15-16

    def test_type_error_w_keyword_arguments():
        # function_00(the_input=0)
        src.type_error.function_00(the_input=0)
        # function_01(
        src.type_error.function_01(
            first='first',
            second={'key': 'value'},
        )
        # function_03(
        src.type_error.function_03(
            third=(0, 1, 2, 'n'),
            second=[0, 1, 2, 'n'],
            first={0, 1, 2, 'n'},
        )
        # function_03(
        src.type_error.function_03(
            first=None,
            second=False,
            third=True,
            fourth=4,
        )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_03() got
               an unexpected keyword argument 'first'

* I add ``first`` in the parentheses of the :ref:`definition<how to make a function that takes input>` of ``function_03`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 2-3

    # def function_03():
    # def function_03(one, two, three, four):
    def function_03(one, two, three, four, first):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...::test_type_error_w_positional_arguments -
        TypeError: function_03() missing
                   1 required positional argument: 'first'
    FAILED ...::test_type_error_w_keyword_arguments -
        TypeError: function_03() got
                   an unexpected keyword argument 'second'

* I add ``second`` to the parentheses

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3-7

    # def function_03():
    # def function_03(one, two, three, four):
    # def function_03(one, two, three, four, first):
    def function_03(
        one, two, three, four,
        first, second
    ):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...::test_type_error_w_positional_arguments -
        TypeError: function_03() missing
                   2 required positional arguments:
                   'first' and 'second'
    FAILED ...::test_type_error_w_keyword_arguments -
        TypeError: function_03() got
                   an unexpected keyword argument 'third'

* I add ``third`` to the parentheses

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 6-7

    # def function_03():
    # def function_03(one, two, three, four):
    # def function_03(one, two, three, four, first):
    def function_03(
        one, two, three, four,
        # first, second
        first, second, third
    ):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    FAILED ...::test_type_error_w_positional_arguments -
        TypeError: function_03() missing
                   3 required positional arguments:
                   'first', 'second', and 'third'
    FAILED ...::test_type_error_w_keyword_arguments -
        TypeError: function_03() got
                   an unexpected keyword argument 'fourth'.
                   Did you mean 'four'?

* I add ``fourth`` to the parentheses

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 7-8

    # def function_03():
    # def function_03(one, two, three, four):
    # def function_03(one, two, three, four, first):
    def function_03(
        one, two, three, four,
        # first, second
        # first, second, third,
        first, second, third, fourth
    ):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...::test_type_error_w_positional_arguments -
        TypeError: function_03() missing
                   4 required positional arguments:
                   'first', 'second', 'third', and 'fourth'
    FAILED ...::test_type_error_w_keyword_arguments -
        TypeError: function_03() missing
                   4 required positional arguments:
                   'one', 'two', 'three', and 'four'

* I remove ``one``, ``two``, ``three`` and ``four`` from the parentheses

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 5

    # def function_03():
    # def function_03(one, two, three, four):
    # def function_03(one, two, three, four, first):
    def function_03(
        # one, two, three, four,
        # first, second
        # first, second, third,
        first, second, third, fourth
    ):
        return None

  the test passes.

* I change the :ref:`call<how to call a function with input>` to ``function_04`` in :ref:`test_type_error_w_keyword_arguments` to a :ref:`call<how to call a function with input>` to ``function_04`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 22-23

    def test_type_error_w_keyword_arguments():
        # function_00(the_input=0)
        src.type_error.function_00(the_input=0)
        # function_01(
        src.type_error.function_01(
            first='first',
            second={'key': 'value'},
        )
        # function_02(
        src.type_error.function_02(
            third=(0, 1, 2, 'n'),
            second=[0, 1, 2, 'n'],
            first={0, 1, 2, 'n'},
        )
        # function_03(
        src.type_error.function_03(
            first=None,
            second=False,
            third=True,
            fourth=4,
        )
        # function_04(argument='value')
        src.type_error.function_04(argument='value')

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_04() got
               an unexpected keyword argument 'argument'

* I change ``one`` to ``argument`` in the parentheses of the :ref:`definition<how to make a function that takes input>` of ``function_04`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 2-3

    # def function_04():
    # def function_04(one):
    def function_04(argument):
        return None

  the test passes.

* I change the :ref:`call<how to call a function with input>` to ``function_05`` in :ref:`test_type_error_w_keyword_arguments` to a :ref:`call<how to call a function with input>` to ``function_05`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 24-25

    def test_type_error_w_keyword_arguments():
        # function_00(the_input=0)
        src.type_error.function_00(the_input=0)
        # function_01(
        src.type_error.function_01(
            first='first',
            second={'key': 'value'},
        )
        # function_02(
        src.type_error.function_02(
            third=(0, 1, 2, 'n'),
            second=[0, 1, 2, 'n'],
            first={0, 1, 2, 'n'},
        )
        # function_03(
        src.type_error.function_03(
            first=None,
            second=False,
            third=True,
            fourth=4,
        )
        # function_04(argument='value')
        src.type_error.function_04(argument='value')
        # function_05(
        src.type_error.function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_05() got
               an unexpected keyword argument 'argument_0'

* I change ``one`` to ``argument_0`` in the parentheses of the :ref:`definition<how to make a function that takes input>` of ``function_05`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-3

    # def function_05():
    # def function_05(one, two):
    def function_05(argument_0, two):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

     TypeError: function_05() got
                an unexpected keyword argument 'argument_1'.
                Did you mean 'argument_0'?

* I change ``two`` to ``argument_1`` in the parentheses

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 3-4

    # def function_05():
    # def function_05(one, two):
    # def function_05(argument_0, two):
    def function_05(argument_0, argument_1):
        return None

  the test passes.

* I change the :ref:`call<how to call a function with input>` to ``function_06`` in :ref:`test_type_error_w_keyword_arguments` to a :ref:`call<how to call a function with input>` to ``function_06`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 6-7

        # function_05(
        src.type_error.function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )
        # function_06(
        src.type_error.function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_06() got
               an unexpected keyword argument 'argument_0'

* I change ``one`` to ``argument_0`` in the parentheses of the :ref:`definition<how to make a function that takes input>` of ``function_06`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2-3

    # def function_06():
    # def function_06(one, two, three):
    def function_06(argument_0, two, three):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

     TypeError: function_06() got
                an unexpected keyword argument 'argument_1'.
                Did you mean 'argument_0'?

* I change ``two`` to ``argument_1`` in the parentheses

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 3-4

    # def function_06():
    # def function_06(one, two, three):
    # def function_06(argument_0, two, three):
    def function_06(argument_0, argument_1, three):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

     TypeError: function_06() got
                an unexpected keyword argument 'argument_2'.
                Did you mean 'argument_0'?

* I change ``three`` to ``argument_2`` in the parentheses

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 3-4

    # def function_06():
    # def function_06(one, two, three):
    # def function_06(argument_0, two, three):
    # def function_06(argument_0, argument_1, three):
    def function_06(argument_0, argument_1, argument_2):
        return None

  the test passes.

* I change the :ref:`call<how to call a function with input>` to ``function_07`` in :ref:`test_type_error_w_keyword_arguments` to a :ref:`call<how to call a function with input>` to ``function_07`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 7-8

        # function_06(
        src.type_error.function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )
        # function_07(
        src.type_error.function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_07() got
               an unexpected keyword argument 'argument_0'

* I change ``one`` to ``argument_0`` in the parentheses of the :ref:`definition<how to make a function that takes input>` of ``function_07`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2-3

    # def function_07():
    # def function_07(one, two, three, four):
    def function_07(argument_0, two, three, four):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

     TypeError: function_07() got
                an unexpected keyword argument 'argument_1'.
                Did you mean 'argument_0'?

* I change ``two`` to ``argument_1`` in the parentheses

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 3-6

    # def function_07():
    # def function_07(one, two, three, four):
    # def function_07(argument_0, two, three, four):
    def function_07(
        argument_0, argument_1, three, four
    ):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

     TypeError: function_07() got
                an unexpected keyword argument 'argument_2'.
                Did you mean 'argument_0'?

* I change ``three`` to ``argument_2`` in the parentheses

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 5-7

    # def function_07():
    # def function_07(one, two, three, four):
    # def function_07(argument_0, two, three, four):
    def function_07(
        # argument_0, argument_1, three, four
        argument_0, argument_1,
        argument_2, four
    ):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

     TypeError: function_07() got
                an unexpected keyword argument 'argument_n'.
                Did you mean 'argument_0'?

* I change ``four`` to ``argument_n`` in the parentheses

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 7-8

    # def function_07():
    # def function_07(one, two, three, four):
    # def function_07(argument_0, two, three, four):
    def function_07(
        # argument_0, argument_1, three, four
        argument_0, argument_1,
        # argument_2, four
        argument_2, argument_n
    ):
        return None

  the test passes.

* I change the :ref:`call<how to call a function with input>` to ``function_08`` in :ref:`test_type_error_w_keyword_arguments` to a :ref:`call<how to call a function with input>` to ``function_08`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 8-11

        # function_07(
        src.type_error.function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )
        # function_08(argument='positional', name='keyword')
        src.type_error.function_08(
            argument='positional', name='keyword'
        )


    def test_type_error_w_args_and_kwargs():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_07() got
               an unexpected keyword argument 'argument'

* I change ``one`` to ``argument_0`` in the parentheses of the :ref:`definition<how to make a function that takes input>` of ``function_08`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 2-3

    # def function_08():
    # def function_08(one, two):
    def function_08(argument, two):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

     TypeError: function_08() got
                an unexpected keyword argument 'name'.

* I change ``two`` to ``name`` in the parentheses

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 3-4

    # def function_08():
    # def function_08(one, two):
    # def function_08(argument, two):
    def function_08(argument, name):
        return None

  the test passes.

* I remove the commented lines from :ref:`test_type_error_w_keyword_arguments` in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 55

    def test_type_error_w_keyword_arguments():
        src.type_error.function_00(the_input=0)
        src.type_error.function_01(
            first='first',
            second={'key': 'value'},
        )
        src.type_error.function_02(
            third=(0, 1, 2, 'n'),
            second=[0, 1, 2, 'n'],
            first={0, 1, 2, 'n'},
        )
        src.type_error.function_03(
            first=None,
            second=False,
            third=True,
            fourth=4,
        )
        src.type_error.function_04(argument='value')
        src.type_error.function_05(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
        )
        src.type_error.function_06(
            argument_0='value1',
            argument_1=(0, 1, 2, 'n'),
            argument_2=[0, 1, 2, 'n'],
        )
        src.type_error.function_07(
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
            argument_n={'key': 'value'},
        )
        src.type_error.function_08(
            argument='positional', name='keyword'
        )


    def test_type_error_w_args_and_kwargs():

----

* I change the :ref:`call<how to call a function with input>` to ``function_00`` in :ref:`test_type_error_w_args_and_kwargs` to a :ref:`call<how to call a function with input>` to ``function_00`` of ``type_error.py`` in the ``src`` folder_, in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 2-3

    def test_type_error_w_args_and_kwargs():
        # function_00('argument')
        src.type_error.function_00('argument')

  the test is still green.

* I change the :ref:`call<how to call a function with input>` to ``function_01`` to ``src.type_error.function_01``

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 4-5

    def test_type_error_w_args_and_kwargs():
        # function_00('argument')
        src.type_error.function_00('argument')
        # function_01(1, 0)
        src.type_error.function_01(1, 0)

  still green.

* I change the :ref:`call<how to call a function with input>` to ``function_02`` to ``src.type_error.function_02``

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 6-9

    def test_type_error_w_args_and_kwargs():
        # function_00('argument')
        src.type_error.function_00('argument')
        # function_01(1, 0)
        src.type_error.function_01(1, 0)
        # function_02(third=True, second=False, first=None)
        src.type_error.function_02(
            third=True, second=False, first=None
        )

  green.

* I change the :ref:`call<how to call a function with input>` to ``function_03`` to ``src.type_error.function_03``

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 5-6

        # function_02(third=True, second=False, first=None)
        src.type_error.function_02(
            third=True, second=False, first=None
        )
        # function_03(
        src.type_error.function_03(
            second=[0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )

  still green.

* I change the :ref:`call<how to call a function with input>` to ``function_04`` to ``src.type_error.function_04``

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 8-9

        # function_03(
        src.type_error.function_03(
            second=[0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )
        # function_04('value')
        src.type_error.function_04('value')

  the test is still green.

* I change the :ref:`call<how to call a function with input>` to ``function_05`` to ``src.type_error.function_05``

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 3-4

        # function_04('value')
        src.type_error.function_04('value')
        # function_05(
        src.type_error.function_05(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
        )

  still green.

* I change the :ref:`call<how to call a function with input>` to ``function_06`` to ``src.type_error.function_06``

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 6-7

        # function_05(
        src.type_error.function_05(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
        )
        # function_06(
        src.type_error.function_06(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
        )

  green.

* I change the :ref:`call<how to call a function with input>` to ``function_07`` to ``src.type_error.function_07``

  .. code-block:: python
    :lineno-start: 116
    :emphasize-lines: 7-8

        # function_06(
        src.type_error.function_06(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
        )
        # function_07(
        src.type_error.function_07(
            argument_n={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )

  still green.

* I change the :ref:`call<how to call a function with input>` to ``function_08`` to ``src.type_error.function_08``

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 8-11

        # function_07(
        src.type_error.function_07(
            argument_n={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        # function_08('positional', argument='keyword')
        src.type_error.function_08(
            'positional', argument='keyword'
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_08() got
               multiple values for argument 'argument'

* I change the order of the arguments in the :ref:`definition<how to make a function that takes input>` of ``function_08`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 72

    # def function_08():
    # def function_08(one, two):
    # def function_08(argument, two):
    # def function_08(argument, name):
    def function_08(name, argument):
        return None

  the test passes.

* I remove the commented lines from ``type_error.py``

  .. code-block:: python
    :linenos:

    def function_00(the_input):
        return None


    def function_01(first, second):
        return None


    def function_02(
        third, second, first
    ):
        return None


    def function_03(
        first, second, third, fourth
    ):
        return None


    def function_04(argument):
        return None


    def function_05(argument_0, argument_1):
        return None


    def function_06(argument_0, argument_1, argument_2):
        return None


    def function_07(
        argument_0, argument_1,
        argument_2, argument_n
    ):
        return None


    def function_08(name, argument):
        return None

* I remove the commented lines from :ref:`test_type_error_w_args_and_kwargs` in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 93

    def test_type_error_w_args_and_kwargs():
        src.type_error.function_00('argument')
        src.type_error.function_01(1, 0)
        src.type_error.function_02(
            third=True, second=False, first=None
        )
        src.type_error.function_03(
            second=[0, 1, 2, 'n'],
            first=(0, 1, 2, 'n'),
            third={0, 1, 2, 'n'},
            fourth={'key': 'value'}
        )
        src.type_error.function_04('value')
        src.type_error.function_05(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
        )
        src.type_error.function_06(
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
            argument_2={0, 1, 2, 'n'},
        )
        src.type_error.function_07(
            argument_n={'key': 'value'},
            argument_2={0, 1, 2, 'n'},
            argument_0=(0, 1, 2, 'n'),
            argument_1=[0, 1, 2, 'n'],
        )
        src.type_error.function_08(
            'positional', argument='keyword'
        )


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # ModuleNotFoundError
    # AttributeError

* I remove ``functions_00`` to ``functions_08`` from ``test_type_error.py`` because they are no longer :ref:`called<how to call a function with input>`

  .. code-block:: python
    :linenos:

    import src.type_error


    def test_type_error_w_positional_arguments():

  all the tests are passing because ``functions_00`` to ``functions_08`` are now :ref:`attributes<what is a class attribute?>` of ``type_error.py`` in the ``src`` folder_ and I can :ref:`call<how to call a function with input>` them from outside the file_ with ``src.type_error.function_name()``

  .. code-block:: shell

    src.type_error.function_name()
    src
    └── type_error.py
        └── def function_name(): return None

  where ``function_name`` is the name of the :ref:`function<what is a function?>`.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'move functions to type_error.py'

:ref:`I have to call a function with the same number or names of arguments that are in its definition<test_type_error_w_args_and_kwargs>`.

----

*********************************************************************************
review
*********************************************************************************

:ref:`I can write solutions in a different module from the tests<separate and equal>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<separate and equal TypeError: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

so far you know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what an assertion is<what is an assertion?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`
* :ref:`how to make functions that take input<functions that take input>`
* :ref:`what causes TypeError<what causes TypeError?>`
* :ref:`how to place values in strings<telephone>`
* :ref:`how to separate tests from solutions<separate and equal>`

:ref:`Would you like to test making a person with f-strings?<how to make a person with f-strings>`

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