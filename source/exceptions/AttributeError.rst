.. meta::
  :description: Getting an AttributeError in Python? Learn to fix the common 'NoneType' object and other attribute errors with our step-by-step guide and video tutorial.
  :keywords: Jacob Itegboje, python AttributeError 'NoneType' object has no attribute, how to fix AttributeError in python, python 'int' object has no attribute 'append', python AttributeError 'str' object has no attribute, AttributeError: 'list' object has no attribute 'add', python check if attribute exists before access, python debug AttributeError in class, python common causes of AttributeError, AttributeError vs TypeError in Python

.. include:: ../links.rst

.. _AttributeError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError

#################################################################################
what causes AttributeError?
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/4-KGDO3zMYk?si=TdPbniUMkoz0M7CI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

So far, all the tests show that I get AttributeError_ when I use a name that is NOT in an :ref:`object<what is a class?>`.

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

.. literalinclude:: ../code/tests/test_attribute_error.py
  :language: python
  :linenos:

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``attribute_error``
* I open a terminal_
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

* I make a directory_ for the source code

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line.

* I use the `mv program`_ to change the name of ``main.py`` to ``attribute_error.py`` and move it to the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        mv main.py src/attribute_error.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        Move-Item main.py src/attribute_error.py

  the terminal_ goes back to the command line.

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

* I make a :ref:`Python file<what is a module?>` for the tests in the ``tests`` directory_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/test_attribute_error.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/test_attribute_error.py

  the terminal_ goes back to the command line.

* I open ``test_attribute_error.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

* I add :ref:`the first failing test<test_failure>` to ``test_attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestAttributeError(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I go back to the terminal_ to make a requirements file_ for the `Python packages`_ I need

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" > requirements.txt

  the terminal_ goes back to the command line.

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

* I use uv_ to install `pytest-watcher`_ with the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal_ shows that it installed `pytest-watcher`_ and its dependencies

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 8, 10

    ============================ FAILURES ============================
    ________________ TestAttributeError.test_failure _________________

    self = <tests.test_attribute_error.AttributeError testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_attribute_error.py:7: AssertionError
    ==================== short test summary info =====================
    FAILED tests/test_attribute_error.py::TestAttributeError::test_failure - AssertionError: True is not false
    ======================= 1 failed in X.YZs ========================

  because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors and try to run ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_attribute_error.py`` in the :ref:`editor<2 editors>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestAttributeError(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes.

----

*********************************************************************************
test_attribute_error_w_variables
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add an `import statement`_ at the top of  ``test_attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.attribute_error
    import unittest

* I change ``test_failure`` to ``test_attribute_error_w_variables``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-4

    class TestAttributeError(unittest.TestCase):

        def test_attribute_error_w_variables(self):
            src.attribute_error.variable_00


    # Exceptions seen

  I think of ``src.attribute_error.variable_00`` as an address

  - ``src`` is the ``src`` folder_
  - ``src.attribute_error`` points to ``attribute_error.py`` in the ``src`` folder_
  - ``src.attribute_error.variable_00`` points to ``variable_00`` in ``attribute_error.py`` in the ``src`` folder_
  - since there is nothing in ``attribute_error.py`` named ``variable_00``, Python_ cannot find ``variable_00`` inside ``attribute_error.py`` and raises AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'variable_00'

  ``variable_00`` is NOT an attribute of ``attribute_error.py`` in the ``src`` folder_

* I add AttributeError_ to the list of :ref:`Exceptions<errors>` seen in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # AttributeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``attribute_error.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>` of my `Integrated Development Environment (IDE)`_

* I delete all the text in the file_, then add the name to ``attribute_error.py``

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
    :lineno-start: 11
    :emphasize-lines: 4
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # AttributeError
    # NameError

* I point ``variable_00`` to :ref:`None<what is None?>`, in ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    variable_00 = None

  - the test passes because ``variable_00`` is now an :ref:`attribute<what is a class attribute?>` or property of ``attribute_error.py`` in the ``src`` folder_
  - I can use it from outside the file_ with ``src.attribute_error.variable_00``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I do the same test a few more times as a drill in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3

        def test_attribute_error_w_variables(self):
            src.attribute_error.variable_00
            src.attribute_error.variable_01


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'variable_01'.
                    Did you mean: 'variable_00'?

* I add the name to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    variable_00 = None
    variable_01

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'variable_01' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    variable_00 = None
    variable_01 = None

  the test passes.

* I add another statement to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

        def test_attribute_error_w_variables(self):
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

* I add the name and point it to :ref:`None<what is None?>` in ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    variable_00 = None
    variable_01 = None
    variable_02 = None

  the test passes.

* I add a line for ``src.attribute_error.variable_03`` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5


        def test_attribute_error_w_variables(self):
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

* I add the :ref:`variable<what is a variable?>` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None

  the test passes.

* I add a line for ``src.attribute_error.variable_04`` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6


        def test_attribute_error_w_variables(self):
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

* I add the :ref:`variable<what is a variable?>` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None
    variable_04 = None

  the test passes.

* I add a line for ``src.attribute_error.variable_05`` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 7


        def test_attribute_error_w_variables(self):
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

* I add the :ref:`variable<what is a variable?>` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None
    variable_04 = None
    variable_05 = None

  the test passes.

* I add a line for ``src.attribute_error.variable_06`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 8


        def test_attribute_error_w_variables(self):
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

* I add the :ref:`variable<what is a variable?>` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None
    variable_04 = None
    variable_05 = None
    variable_06 = None

  the test passes.

* I add a line for ``src.attribute_error.variable_07`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9


        def test_attribute_error_w_variables(self):
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

* I add the :ref:`variable<what is a variable?>` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None
    variable_04 = None
    variable_05 = None
    variable_06 = None
    variable_07 = None

  the test passes.

* I add a line for ``src.attribute_error.variable_08`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10

        def test_attribute_error_w_variables(self):
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

* I add the :ref:`variable<what is a variable?>` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None
    variable_04 = None
    variable_05 = None
    variable_06 = None
    variable_07 = None
    variable_08 = None

  the test passes.

* I add a line for ``src.attribute_error.variable_09`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 11


        def test_attribute_error_w_variables(self):
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

* I add the :ref:`variable<what is a variable?>` to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None
    variable_04 = None
    variable_05 = None
    variable_06 = None
    variable_07 = None
    variable_08 = None
    variable_09 = None

  the test passes.

* I open a new terminal_ then change directories to ``assertion_error``

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

  the terminal_ shows I am in the ``assertion_error`` folder_

  .. code-block:: python

    .../pumping_python/assertion_error

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_what_is_an_assertion'

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

I add a test for :ref:`functions<what is a function?>` to ``test_attribute_error.py``

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 5-6

          src.attribute_error.variable_07
          src.attribute_error.variable_08
          src.attribute_error.variable_09

      def test_attribute_error_w_functions(self):
          src.attribute_error.function_00()


  # Exceptions seen

the terminal_ is my friend, and shows AttributeError_

.. code-block:: python

  AttributeError: module 'src.attribute_error'
                  has no attribute 'function_00'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name and point it to :ref:`None<what is None?>` in ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 13

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None
    variable_04 = None
    variable_05 = None
    variable_06 = None
    variable_07 = None
    variable_08 = None
    variable_09 = None


    function_00 = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  because :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # AttributeError
    # NameError
    # TypeError

* I change the :ref:`variable<what is a variable?>` to a :ref:`function<what is a function?>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 1-3

    # function_00 = None
    def function_00():
        return None

  - the test passes because ``function_00`` is now an :ref:`attribute<what is a class attribute?>` or property of ``attribute_error.py`` in the ``src`` folder_
  - I can call it from outside the file_ with ``src.attribute_error.function_00()``


----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line

  .. code-block:: python
    :linenos:

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None
    variable_04 = None
    variable_05 = None
    variable_06 = None
    variable_07 = None
    variable_08 = None
    variable_09 = None


    def function_00():
        return None

  time to make it a drill.

* I add a call to ``src.attribute_error.function_01`` in :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3

        def test_attribute_error_w_functions(self):
            src.attribute_error.function_00()
            src.attribute_error.function_01()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'function_01'.
                    Did you mean: 'function_00'?

* I add the :ref:`function<what is a function?>` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5-6

    def function_00():
        return None


    def function_01():
        return None

  the test passes.

* I add a line for ``src.attribute_error.function_02`` to :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4

        def test_attribute_error_w_functions(self):
            src.attribute_error.function_00()
            src.attribute_error.function_01()
            src.attribute_error.function_02()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error'
                    has no attribute 'function_02'.
                    Did you mean: 'function_00'?

* I add a :ref:`function<what is a function?>` for it in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5-6

    def function_01():
        return None


    def function_02():
        return None

  the test passes.

* I add a line for ``src.attribute_error.function_03`` to :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5

        def test_attribute_error_w_functions(self):
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

* I add a :ref:`function<what is a function?>` for it in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-6

    def function_02():
        return None


    def function_03():
        return None

  the test passes.

* I add a line for ``src.attribute_error.function_04`` to :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 6

        def test_attribute_error_w_functions(self):
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

* I add a :ref:`function<what is a function?>` for it in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5-6

    def function_03():
        return None


    def function_04():
        return None

  the test passes.

* I add a line for ``src.attribute_error.function_05`` to :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 7

        def test_attribute_error_w_functions(self):
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

* I add a :ref:`function<what is a function?>` for it in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 5-6

    def function_04():
        return None


    def function_05():
        return None

  the test passes.

* I add a line for ``src.attribute_error.function_06`` to :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 8

        def test_attribute_error_w_functions(self):
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

* I add a :ref:`function<what is a function?>` for it in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5-6

    def function_05():
        return None


    def function_06():
        return None

  the test passes.

* I add a line for ``src.attribute_error.function_07`` to :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 9

        def test_attribute_error_w_functions(self):
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

* I add a :ref:`function<what is a function?>` for it in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 5-6

    def function_06():
        return None


    def function_07():
        return None

  the test passes.

* I add a line for ``src.attribute_error.function_08`` to :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 10

        def test_attribute_error_w_functions(self):
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

* I add a :ref:`function<what is a function?>` for it in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 5-6

    def function_07():
        return None


    def function_08():
        return None

  the test passes.

* I add a line for ``src.attribute_error.function_09`` to :ref:`test_attribute_error_w_functions` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 11

        def test_attribute_error_w_functions(self):
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

* I add a :ref:`function<what is a function?>` for it in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 5-6

    def function_08():
        return None


    def function_09():
        return None

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_attribute_error_w_functions'


* :ref:`A function in a module is an attribute of the module<test_attribute_error_w_functions>`
* :ref:`A variable in a module is an attribute of the module<test_attribute_error_w_variables>`

----

*********************************************************************************
test_attribute_error_w_class_attributes
*********************************************************************************

I know that :ref:`variables<what is a variable?>` and :ref:`functions<what is a function?>` in a :ref:`module<what is a module?>` are attributes of the :ref:`module<what is a module?>`.

A :ref:`class<what is a class?>` in a :ref:`module<what is a module?>` is also an attribute of the :ref:`module<what is a module?>`, and :ref:`variables<what is a variable?>` in the :ref:`class<what is a class?>` are attributes of the :ref:`class<what is a class?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

I add a new test to ``test_attribute_error.py``

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 7-8

      def test_attribute_error_w_functions(self):
          src.attribute_error.function_00()
          src.attribute_error.function_01()
          src.attribute_error.function_02()
          src.attribute_error.function_03()

      def test_attribute_error_w_class_attributes(self):
          src.attribute_error.AClass.attribute_00


  # Exceptions seen

the terminal_ is my friend, and shows AttributeError_

.. code-block:: shell

  AttributeError: module 'src.attribute_error' has no attribute 'AClass'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function<what is a function?>` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5-6

    def function_03():
        return None


    def AClass():
        return None

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: 'function' object has no attribute 'attribute_00'

* I add a :ref:`variable<what is a variable?>` inside the :ref:`function <what is a function?>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-4

    def AClass():

        attribute_00 = None
        return None

  the terminal_ still shows the same :ref:`Exception<errors>` because I cannot get to a :ref:`variable<what is a variable?>` inside a :ref:`function<what is a function?>` from outside the :ref:`function<what is a function?>`

* I use the :ref:`class<what is a class?>` keyword instead of the def_ keyword to make ``AClass`` a :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 1

    class AClass():

        attribute_00 = None
        return None

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    E    return None
    E    ^^^^^^^^^^^
    E  SyntaxError: 'return' outside function

  I cannot use a `return statement`_ outside a :ref:`function<what is a function?>`

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError

* I remove the `return statement`_ from ``AClass`` in ``attribute_error.py`` since it is no longer a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 23

    class AClass():

        attribute_00 = None

  the test passes.

``attribute_00`` is now an attribute of the ``AClass`` :ref:`class<what is a class?>` which is an attribute of ``attribute_error.py`` in the ``src`` folder_ and I can get to it with ``src.attribute_error.AClass.attribute_00``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another failing line for practice to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: type object 'AClass' has no attribute 'attribute_01'. Did you mean: 'attribute_00'?

* I add the name to the :ref:`class<what is a class?>` definition in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 4

    class AClass():

        attribute_00 = None
        attribute_01 = None

  the test passes.

* I add another line to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01
            src.attribute_error.AClass.attribute_02

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: type object 'AClass' has no attribute 'attribute_02'. Did you mean: 'attribute_00'?

* I add the :ref:`variable<what is a variable?>` to ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

    class AClass():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None

  the test passes.

* I add another line to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01
            src.attribute_error.AClass.attribute_02
            src.attribute_error.AClass.attribute_03


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: type object 'AClass' has no attribute 'attribute_03'. Did you mean: 'attribute_00'?

* I add the name to ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6

    class AClass():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add '


* :ref:`A variable in a class is an attribute of the class<test_attribute_error_w_class_attributes>`
* :ref:`A class in a module is an attribute of the module<test_attribute_error_w_class_attributes>`
* :ref:`A function in a module is an attribute of the module<test_attribute_error_w_functions>`
* :ref:`A variable in a module is an attribute of the module<test_attribute_error_w_variables>`

----

*********************************************************************************
test_attribute_error_w_class_methods
*********************************************************************************

I know that :ref:`variables<what is a variable?>`, :ref:`functions<what is a function?>` and :ref:`classes<what is a class?>` in a :ref:`module<what is a module?>` are attributes of the :ref:`module<what is a module?>`.

I also know that :ref:`variables<what is a variable?>` in a :ref:`class<what is a class?>` are attributes of the :ref:`class<what is a class?>`.

:ref:`functions<what is a function?>` in a :ref:`class<what is a class?>` are also attributes, they are called :ref:`methods<what is a method?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests
* I add a new test to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 7-8

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01
            src.attribute_error.AClass.attribute_02
            src.attribute_error.AClass.attribute_03

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: type object 'AClass' has no attribute 'method_00'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name to ``AClass`` and point it to :ref:`None<what is None?>`, in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 8

    class AClass():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None

        method_00 = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  ``method_00`` points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`

* I make it a :ref:`method<what is a method?>` with the def_ keyword

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 8-9

    class AClass():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None

        def method_00():
            return None

  the test passes.

``method_00`` is now an attribute of ``AClass`` which is an attribute of ``attribute_error.py`` in the ``src`` folder_ and I can call it with ``src.attribute_error.AClass.method_00()``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* You know the "drill", I add a new failing line to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01()

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: type object 'AClass' has no attribute 'method_01'. Did you mean: 'method_00'?

* I add a definition for it in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4-5

        def method_00():
            return None

        def method_01():
            return None

  the test passes.

* I add another failing line to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01()
            src.attribute_error.AClass.method_02()

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: type object 'AClass' has no attribute 'method_02'. Did you mean: 'method_00'?

* I add the :ref:`method<what is a method?>` to ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 7-8

        def method_00():
            return None

        def method_01():
            return None

        def method_02():
            return None

  the test passes.

* I add the last line to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01()
            src.attribute_error.AClass.method_02()
            src.attribute_error.AClass.method_03()


    # Exceptions seen

  the terminal_ is my friend, and shows AttributeError_

  .. code-block:: shell

    AttributeError: type object 'AClass' has no attribute 'method_03'. Did you mean: 'method_00'?

* I add the :ref:`method<what is a method?>` to ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 17-18

    class AClass():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None

        def method_00():
            return None

        def method_01():
            return None

        def method_02():
            return None

        def method_03():
            return None

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add '


* :ref:`A function in a class is an attribute of the class and is called a method<test_attribute_error_w_class_methods>`
* :ref:`A variable in a class is an attribute of the class<test_attribute_error_w_class_attributes>`
* :ref:`A class in a module is an attribute of the module<test_attribute_error_w_class_attributes>`
* :ref:`A function in a module is an attribute of the module<test_attribute_error_w_functions>`
* :ref:`A variable in a module is an attribute of the module<test_attribute_error_w_variables>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``attribute_error.py`` and ``test_attribute_error.py``  in the :ref:`editors<2 editors>`
* I go back to the terminal_ that is running the tests
* I click in the terminal_ where the tests are running, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``attribute_error``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I ran tests for AttributeError_ with

* :ref:`variables<what is a variable?>`
* :ref:`functions<test_attribute_error_w_functions>`
* :ref:`variables in classes also known as class attributes<test_attribute_error_w_class_attributes>`
* :ref:`functions in classes also known as methods<test_attribute_error_w_class_methods>`

I also saw these :ref:`Exceptions<errors>`

* :ref:`AssertionError<what causes AssertionError?>`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`TypeError<what causes TypeError?>` and
* SyntaxError_

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<AttributeError: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know

* :ref:`how to make a Python test driven development environment manually<how to make a Python test driven development environment>`
* :ref:`what causes AssertionError?`
* :ref:`how to make functions<what is a function?>` and
* :ref:`what causes AttributeError<what causes AttributeError?>`

:ref:`Would you like to test how to pass values from tests to functions with assert methods?<telephone>`

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