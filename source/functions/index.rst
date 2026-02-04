.. meta::
   :description: Learn Python functions with TDD! Explore arguments, defaults, and testing techniques in this practical guide. Start coding now!
   :keywords: Jacob Itegboje, Python functions, Test-Driven Development, Python programming, keyword arguments, positional arguments, coding tutorial

.. include:: ../links.rst

.. _function: https://docs.python.org/3/glossary.html#term-function
.. _functions: :ref:`function<what is a function?>`
.. _argument: https://docs.python.org/3/glossary.html#term-argument
.. _arguments: argument_
.. _keyword arguments: arguments_
.. _positional arguments: arguments_

#################################################################################
what is a function?
#################################################################################

A function_ is code that is callable_, this means I can write code to do something one time, and use it to do the thing at a different time from when I write it, by calling the name.

Using a function_ can make code simpler, easier to read, test, reuse, maintain and improve - all the good things.

Part of `Computer Programming`_ is sending input data to a process and getting output data back, you can think of it like this

.. code-block:: python

    input_data -> process -> output_data

I think of it like mapping a function ``f`` in Mathematics_ with inputs ``x`` and output ``y``

.. math::

  f(x) -> y

in other words

.. code-block:: python

                  f(x) -> y
  function(input_data) -> output_data

the :ref:`function<what is a function?>` does something (the process) with ``input_data`` and gives me ``output_data`` as the result.

functions_ are made with the def_ keyword in Python_, a name, parentheses and a colon at the end. The code that makes up the :ref:`function<what is a function?>` is indented to the right on the line after the colon.

.. code-block:: python

  def name_of_function():
      code indented to the right
      more code indented to the right
      ...

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/functions/test_functions_i.py
  :language: python
  :linenos:

*********************************************************************************
questions about functions
*********************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`what is a function?<what is a function?>`
* :ref:`what do functions return by default?<test_making_a_function_w_return_none>`
* :ref:`what happens after a function returns?<test_what_happens_after_a_function_returns>`
* :ref:`what is a constant function?<test_constant_function>`
* :ref:`what is the identity function?<test_identity_function>`
* :ref:`what is a positional argument?<test_functions_w_positional_arguments>`
* :ref:`what is a keyword argument?<test_functions_w_keyword_arguments>`
* :ref:`how can I make arguments a choice in a function?<test_functions_w_default_arguments>`
* :ref:`how can I make a function take any number of positional arguments?<test_functions_w_unknown_arguments>`
* :ref:`how can I make a function take any number of keyword arguments?<test_functions_w_unknown_arguments>`
* :ref:`how does Python read positional arguments in a function?<how Python reads positional arguments>`
* :ref:`how does Python read keyword arguments in a function?<how Python reads keyword arguments>`

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``functions``
* I open a terminal_
* I make a directory_ for the project

  .. code-block:: python
    :emphasize-lines: 1

    mkdir functions

  the terminal_ goes back to the command line

  .. code-block:: python

    .../pumping_python

* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd functions

  the terminal_ shows I am in the ``functions`` folder_

  .. code-block:: python

    .../pumping_python/functions

* I make a directory_ for the source code

  .. code-block:: python
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line

  .. code-block:: python

    .../pumping_python/functions

* I make a :ref:`Python file<what is a module?>` to hold the source code in the ``src`` directory_

  .. code-block:: python
    :emphasize-lines: 1

    touch src/functions.py

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item src/functions.py`` not ``touch src/functions.py``

    .. code-block:: Powershell
      :emphasize-lines: 1

      New-Item src/functions.py

  the terminal_ goes back to the command line

  .. code-block:: python

    .../pumping_python/functions

* I `make a directory`_ for the tests

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line

* I make the ``tests`` directory_ a `Python package`_

  .. DANGER:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/__init__.py

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item tests/__init__.py`` not ``touch tests/__init__.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/__init__.py

  the terminal_ goes back to the command line

* I make a :ref:`Python file<what is a module?>` for the tests in the ``tests`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/test_functions.py

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item tests/test_functions.py`` not ``touch tests/test_functions.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/test_functions.py

  the terminal_ goes back to the command line

* I open ``test_functions.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP::

    I can use the terminal_ to open a file_ in the `Integrated Development Environment (IDE)`_ by typing the name of the program and the name of the file_. That means when I type this in the terminal_

    .. code-block:: python
      :emphasize-lines: 1

      code tests/test_functions.py

    `Visual Studio Code`_ opens ``test_functions.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_functions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestFunctions(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I make a requirements file_ for the `Python packages`_ I need in the terminal_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

  the terminal_ goes back to the command line

* I add `pytest-watcher`_ to the file_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

  the terminal_ goes back to the command line

* I setup the project with uv_

  .. code-block:: python
    :emphasize-lines: 1

    uv init

  the terminal_ shows

  .. code-block:: shell

    Initialized project `functions`

  then goes back to the command line

* I remove ``main.py`` from the project

  .. code-block:: python
    :emphasize-lines: 1

    rm main.py

  the terminal_ goes back to the command line

* I install the Python packages listed in the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal shows it installed the `Python packages`_

* I run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 8, 10

    ================================ FAILURES ================================
    _______________________ TestFunctions.test_failure _______________________

    self = <tests.test_functions.TestFunctions testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_functions.py:7: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_functions.py::TestFunctions::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_functions.py:7`` to put the cursor on line 7 in the :ref:`editor<2 editors>`

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestFunctions(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
test_why_use_a_function
*********************************************************************************

Why use a :ref:`function<what is a function?>` when I can just write code to do the thing I want? Let's see

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change ``test_failure`` to ``test_why_use_a_function`` with an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-4

    class TestFunctions(unittest.TestCase):

        def test_why_use_a_function(self):
            self.assertEqual(1+0, 0)


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1 != 0

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation to match reality

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 1

          self.assertEqual(1+0, 1)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

        def test_why_use_a_function(self):
            self.assertEqual(1+0, 1)
            self.assertEqual(1+1, 1)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 2 != 1

* I change the expectation

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 1

            self.assertEqual(1+1, 2)

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_why_use_a_function(self):
            self.assertEqual(1+0, 1)
            self.assertEqual(1+1, 2)
            self.assertEqual(1+2, 2)

  the terminal_ shows :ref:`AssertionError<What causes AssertionError?>`

  .. code-block:: python

    AssertionError: 3 != 2

* I change the expectation

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

            self.assertEqual(1+2, 3)

  the test passes

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5

        def test_why_use_a_function(self):
            self.assertEqual(1+0, 1)
            self.assertEqual(1+1, 2)
            self.assertEqual(1+2, 3)
            self.assertEqual(1+3, 3)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 4 != 3

* I change the expectation

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1

            self.assertEqual(1+3, 4)

  the test passes

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3

            self.assertEqual(1+2, 3)
            self.assertEqual(1+3, 4)
            self.assertEqual(1+4, 4)


    # Exceptions seen
    # AssertionError

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 5 != 4

* I change the expectation

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertEqual(1+4, 5)

  the test passes

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3

            self.assertEqual(1+3, 4)
            self.assertEqual(1+4, 5)
            self.assertEqual(1+5, 5)


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 6 != 5

* I change the expectation

  .. code-block:: python
    :emphasize-lines: 1

            self.assertEqual(1+5, 6)

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

            self.assertEqual(1+4, 5)
            self.assertEqual(1+5, 6)
            self.assertEqual(1+6, 6)


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 7 != 6

* I change the expectation

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 1

            self.assertEqual(1+6, 7)

  the test passes

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3

            self.assertEqual(1+5, 6)
            self.assertEqual(1+6, 7)
            self.assertEqual(1+7, 7)


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 8 != 7

* I change the expectation

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 1

            self.assertEqual(1+7, 8)

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

            self.assertEqual(1+6, 7)
            self.assertEqual(1+7, 8)
            self.assertEqual(1+8, 8)


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 9 != 8

* I change the expectation

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertEqual(1+8, 9)

  the test passes

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3

            self.assertEqual(1+7, 8)
            self.assertEqual(1+8, 9)
            self.assertEqual(1+9, 9)


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 10 != 9

* I change the expectation

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 11

        def test_why_use_a_function(self):
            self.assertEqual(1+0, 1)
            self.assertEqual(1+1, 2)
            self.assertEqual(1+2, 3)
            self.assertEqual(1+3, 4)
            self.assertEqual(1+4, 5)
            self.assertEqual(1+5, 6)
            self.assertEqual(1+6, 7)
            self.assertEqual(1+7, 8)
            self.assertEqual(1+8, 9)
            self.assertEqual(1+9, 10)


    # Exceptions seen

  the test passes

* all those :ref:`assertions<what is an assertion?>` test what happens when I add a number to ``1``, what if I want to test what happens when I add a number to ``2``? I would have to   change ``1`` in 10 places. I change ``1`` to ``2`` in the calculation

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2-11
    :emphasize-text: 2

        def test_why_use_a_function(self):
            self.assertEqual(2+0, 1)
            self.assertEqual(2+1, 2)
            self.assertEqual(2+2, 3)
            self.assertEqual(2+3, 4)
            self.assertEqual(2+4, 5)
            self.assertEqual(2+5, 6)
            self.assertEqual(2+6, 7)
            self.assertEqual(2+7, 8)
            self.assertEqual(2+8, 9)
            self.assertEqual(2+9, 10)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 2 != 1

* I change the expectation of each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2-11
    :emphasize-text: 2 3 4 5 6 7 8 9 10 11

        def test_why_use_a_function(self):
            self.assertEqual(2+0, 2)
            self.assertEqual(2+1, 3)
            self.assertEqual(2+2, 4)
            self.assertEqual(2+3, 5)
            self.assertEqual(2+4, 6)
            self.assertEqual(2+5, 7)
            self.assertEqual(2+6, 8)
            self.assertEqual(2+7, 9)
            self.assertEqual(2+8, 10)
            self.assertEqual(2+9, 11)

  the test passes

* What if I want to test what happens when I add ``3`` to a number? Wait! No more, please, there has to be a better way. I can use a :ref:`function<what is a function?>` for the parts that repeat, I add one to the test

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    class TestFunctions(unittest.TestCase):

        def test_why_use_a_function(self):
            def add_x(x=2, y=0):
                return x + y

            self.assertEqual(2+0, 2)

* then I use it in the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-6
    :emphasize-text: add_x

        def test_why_use_a_function(self):
            def add_x(x=2, y=0):
                return x + y

            # self.assertEqual(2+0, 2)
            self.assertEqual(add_x(y=0), 2)
            self.assertEqual(2+1, 3)

  the test is still green

* I remove the comment and use the ``add_x`` :ref:`function<what is a function?>` in the other :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-14
    :emphasize-text: add_x

        def test_why_use_a_function(self):
            def add_x(x=2, y=0):
                return x + y

            self.assertEqual(add_x(y=0), 2)
            self.assertEqual(add_x(y=1), 3)
            self.assertEqual(add_x(y=2), 4)
            self.assertEqual(add_x(y=3), 5)
            self.assertEqual(add_x(y=4), 6)
            self.assertEqual(add_x(y=5), 7)
            self.assertEqual(add_x(y=6), 8)
            self.assertEqual(add_x(y=7), 9)
            self.assertEqual(add_x(y=8), 10)
            self.assertEqual(add_x(y=9), 11)

  still green

* Now if I want to test what happens when I add ``3`` to a number, I only have to make that change in one place, then change the results since those will change as well

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2
    :emphasize-text: 3

        def test_why_use_a_function(self):
            def add_x(x=3, y=0):
                return x + y

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 3 != 2

* I change the expectations for the :ref:`assertions<what is an assertion?>` one at a time

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-14

        def test_why_use_a_function(self):
            def add_x(x=3, y=0):
                return x + y

            self.assertEqual(add_x(y=0), 3)
            self.assertEqual(add_x(y=1), 4)
            self.assertEqual(add_x(y=2), 5)
            self.assertEqual(add_x(y=3), 6)
            self.assertEqual(add_x(y=4), 7)
            self.assertEqual(add_x(y=5), 8)
            self.assertEqual(add_x(y=6), 9)
            self.assertEqual(add_x(y=7), 10)
            self.assertEqual(add_x(y=8), 11)
            self.assertEqual(add_x(y=9), 12)


    # Exceptions seen
    # AssertionError

:ref:`I can use a function to remove repetition<test_why_use_a_function>`. Is there :ref:`a better way to handle the results changing?<a better way to handle the results changing>`

----

*********************************************************************************
test_making_a_function_w_pass
*********************************************************************************

I can make a :ref:`function<what is a function?>` with the pass_ keyword

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 16-17

      def test_why_use_a_function(self):
          def add_x(x=3, y=0):
              return x + y

          self.assertEqual(add_x(y=0), 3)
          self.assertEqual(add_x(y=1), 4)
          self.assertEqual(add_x(y=2), 5)
          self.assertEqual(add_x(y=3), 6)
          self.assertEqual(add_x(y=4), 7)
          self.assertEqual(add_x(y=5), 8)
          self.assertEqual(add_x(y=6), 9)
          self.assertEqual(add_x(y=7), 10)
          self.assertEqual(add_x(y=8), 11)
          self.assertEqual(add_x(y=9), 12)

      def test_making_a_function_w_pass(self):
          self.assertIsNone(src.functions.w_pass())


  # Exceptions seen

the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block::

  NameError: name 'src' is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 7
    :emphasize-text: NameError

        def test_making_a_function_w_pass(self):
            self.assertIsNone(src.functions.w_pass())


    # Exceptions seen
    # AssertionError
    # NameError

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.functions
    import unittest


    class TestFunctions(unittest.TestCase):

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions' has no attribute 'w_pass'

  ``functions.py`` in the ``src`` folder_ does not have anything named ``w_pass`` inside it

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* I open ``functions.py`` from the ``src`` folder in the :ref:`editor<2 editors>`

* I add a :ref:`function<what is a function?>` definition to ``functions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def w_pass():
        pass

  the test passes

  * the test checks if the result of the call to ``w_pass`` in ``functions.py`` in the ``src`` folder_ also known as ``src.functions.w_pass``, is :ref:`None<what is None?>`
  * the :ref:`function<what is a function?>` definition simply says pass_ and the test passes
  * pass_ is a special keyword that allows the :ref:`function<what is a function?>` definition to follow Python_ language rules
  * the test passes because all functions_ return :ref:`None<what is None?>` by default, as if they have an invisible line that says ``return None``, which leads me to the next test

:ref:`I can make a function with pass<test_making_a_function_w_pass>`

----

*********************************************************************************
test_making_a_function_w_return
*********************************************************************************

I can make a function with a `return statement`_

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new failing test in ``test_functions.py``

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 4-5

      def test_making_a_function_w_pass(self):
          self.assertIsNone(src.functions.w_pass())

      def test_making_a_function_w_return(self):
          self.assertIsNone(src.functions.w_return())


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_return'

``functions.py`` in the ``src`` folder_ does not have anything with the name ``w_return`` in it

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the new :ref:`function<what is a function?>` with the pass_ keyword to ``functions.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 5-6

  def w_pass():
      pass


  def w_return():
      pass

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

I change pass_ to a `return statement`_

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 2

  def w_return():
      return

the test is still green.

I have 2 functions_ with different statements and they both return :ref:`None<what is None?>`, because "all functions_ return :ref:`None<what is None?>` by default, as if they have an invisible line that says ``return None``", which leads me to the next test

:ref:`I can make a function with a return statement<test_making_a_function_w_return>`

----

*********************************************************************************
test_making_a_function_w_return_none
*********************************************************************************

I can make a :ref:`function<what is a function?>` with a `return statement`_ that says what the :ref:`function<what is a function?>` returns

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another failing test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 4-5

      def test_making_a_function_w_return(self):
          self.assertIsNone(src.functions.w_return())

      def test_making_a_function_w_return_none(self):
          self.assertIsNone(src.functions.w_return_none())


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_return_none'

``w_return_none`` is not defined in ``functions.py`` in the ``src`` folder_

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` definition to ``functions.py``

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 5-6

  def w_return():
      return


  def w_return_none():
      return

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`None<what is None?>` to the `return statement`_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2
    :emphasize-text: None

    def w_return_none():
        return None

  the test is still green

* I change :ref:`None<what is None?>` to ``something``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2
    :emphasize-text: something

    def w_return_none():
        return 'something'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'something' is not None

* I undo the change

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def w_return_none():
        return None

  the test is green again

I have 3 functions_ with different statements and they all return :ref:`None<what is None?>`, because "all functions_ return :ref:`None<what is None?>` by default, as if they have an invisible line that says ..." ah, the last :ref:`function<what is a function?>` has a line that clearly says ``return None`` for everyone to see.

I like to write my functions_ this way, so that anyone can see what the :ref:`function<what is a function?>` returns.

:ref:`I can make a function with return None<test_making_a_function_w_return_none>`

----

*********************************************************************************
test_what_happens_after_a_function_returns
*********************************************************************************

The `return statement`_ is the last thing that runs in a :ref:`function<what is a function?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 28
  :emphasize-lines: 4-5

      def test_making_a_function_w_return_none(self):
          self.assertIsNone(src.functions.w_return_none())

      def test_what_happens_after_a_function_returns(self):
          self.assertIsNone(src.functions.return_is_last())


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.functions' has no attribute 'return_is_last'

``functions.py`` does not have a definition for it yet

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` to ``functions.py``

.. code-block:: python
  :lineno-start: 9
  :emphasize-lines: 5-6

  def w_return_none():
      return None


  def return_is_last():
      return None

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def return_is_last():
        return 'something'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'something' is not None

* I add another `return statement`_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

    def return_is_last():
        return 'something'
        return None

  the terminal_ still shows the same :ref:`AssertionError<what causes AssertionError?>` because the `return statement`_ is the last thing to run in a :ref:`function<what is a function?>`, the second `return statement`_ will not run

  .. NOTE::

    The `Integrated Development Environment (IDE)`_ shows that the second return statement will not run by graying it out

* I make ``return None``, the first `return statement`_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2-3
    :emphasize-text: None

    def return_is_last():
        return None
        return 'something'

  the test is green again

* I change the second `return statement`_ as a reminder

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3
    :emphasize-text: will not run

    def return_is_last():
        return None
        return 'will not run'

  the second `return statement`_ is now like a comment, and the test is still green because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_a_function_returns>`

----

*********************************************************************************
test_constant_function
*********************************************************************************

constant functions_ always return the same thing when they are called

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 31
  :emphasize-lines: 4-8

      def test_what_happens_after_a_function_returns(self):
          self.assertIsNone(src.functions.return_is_last())

      def test_constant_function(self):
          self.assertEqual(
              src.functions.constant(),
              'the same thing'
          )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'constant'

I have not added a definition for ``constant`` in ``functions.py`` in the ``src`` folder_

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the :ref:`function<what is a function?>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 6-7

    def return_is_last():
        return None
        return 'will not run'


    def constant():
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != 'the same thing'

  what the ``constant`` :ref:`function<what is a function?>` returns and what the test expects are different

* I change the `return statement`_ to make them the same

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def constant():
        return 'the same thing'

  the test passes

A constant :ref:`function<what is a function?>` always returns the same thing when called, I can use them in place of :ref:`variables<what is a variable?>`, though the number of cases where they are faster than :ref:`variables<what is a variable?>` is pretty small. It is something like if the :ref:`function<what is a function?>` is called less than 10 times, but who's counting?

:ref:`a constant function always returns the same thing<test_constant_function>`

----

*********************************************************************************
test_identity_function
*********************************************************************************

The identity :ref:`function<what is a function?>` returns its input as output, it's also in the :ref:`Truth Table<truth table>` chapter in :ref:`test_logical_identity`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a failing test in ``test_functions.py``

.. code-block:: python
  :lineno-start: 34
  :emphasize-lines: 7-8

      def test_constant_function(self):
          self.assertEqual(
              src.functions.constant(),
              'the same thing'
          )

      def test_identity_function(self):
          self.assertIsNone(src.functions.identity(None))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'identity'

because ``functions.py`` has no ``identity``?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function<what is a function?>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 5-6

    def constant():
        return 'the same thing'


    def identity():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: identity() takes 0 positional arguments but 1 was given

  the definition for ``identity`` does not allow inputs and the test sends :ref:`None<what is None?>` as input

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add a name in parentheses for the ``identity`` :ref:`function<what is a function?>` to take input in ``functions.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 1

    def identity(the_input):
        return None

  the test passes. I am genius

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

The requirement for the :ref:`identity function<test_logical_identity>` is that it returns the same thing it is given, this test passes when :ref:`None<what is None?>` is given as input.

Does it pass when another value is given or does it always return :ref:`None<what is None?>`? Time to write a test

* I add a new :ref:`assertion<what is an assertion?>` to ``test_identity_function`` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 3

    def test_identity_function(self):
        self.assertIsNone(src.functions.identity(None))
        self.assertEqual(src.functions.identity(object), object)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != <class 'object'>

  the :ref:`function<what is a function?>` returns :ref:`None<what is None?>` not ``<class 'object'>`` in the second case. I am not all the way genius, yet

* When I make the ``identity`` :ref:`function<what is a function?>` in ``functions.py`` return what it gets

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2

    def identity(the_input):
        return the_input

  the test passes

I sometimes use the :ref:`Identity Function<test_identity_function>` when I am testing, to see if my test is connected to what I am testing. If I can send something and get it back, I can start making changes to see how it affects the output.

:ref:`The Identity Function returns its input as output<test_identity_function>`

So far, the :ref:`functions<what is a function?>` take no input or one input, the following tests use functions_ that take more than one input.

----

*********************************************************************************
test_functions_w_positional_arguments
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a failing test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 40
  :emphasize-lines: 5-9

      def test_identity_function(self):
          self.assertIsNone(src.functions.identity(None))
          self.assertEqual(src.functions.identity(object), object)

      def test_functions_w_positional_arguments(self):
          self.assertEqual(
              src.functions.w_positional_arguments('first', 'last'),
              ('first', 'last')
          )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_positional_arguments'

because ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function<what is a function?>` to  ``functions.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 5-6

    def identity(the_input):
        return the_input


    def w_positional_arguments():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_positional_arguments() takes 0 positional arguments but 2 were given

* I make the :ref:`function<what is a function?>` take input by adding a name in parentheses

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 1

    def w_positional_arguments(first_input):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_positional_arguments() takes 1 positional argument but 2 were given

* I make ``w_positional_arguments`` take another input by adding another name in parentheses

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 1

    def w_positional_arguments(first_input, last_input):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != ('first', 'last')

* I change the `return statement`_ to make the :ref:`function<what is a function?>` return what it gets

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2

    def w_positional_arguments(first_input, last_input):
        return first_input, last_input

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* The problem with giving arguments this way is that they always have to be in the order the :ref:`function<what is a function?>` expects or I get something different. I add a test to ``test_functions.py`` to show this

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 6-9

        def test_functions_w_positional_arguments(self):
            self.assertEqual(
                src.functions.w_positional_arguments('first', 'last'),
                ('first', 'last')
            )
            self.assertEqual(
                src.functions.w_positional_arguments('last', 'first'),
                ('first', 'last')
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: Tuples differ: ('last', 'first') != ('first', 'last')

* I change the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 8
    :emphasize-text: last

        def test_functions_w_positional_arguments(self):
            self.assertEqual(
                src.functions.w_positional_arguments('first', 'last'),
                ('first', 'last')
            )
            self.assertEqual(
                src.functions.w_positional_arguments('last', 'first'),
                ('last', 'first')
            )

  the test passes

  .. NOTE::

    - ``w_positional_arguments`` in ``functions.py`` in the ``src`` folder_ will always

      .. code-block:: python
        :emphasize-text: first_input last_input

        return first_input, last_input

    - ``src.functions.w_positional_arguments('first', 'last')`` calls ``w_positional_arguments`` in ``functions.py`` in the ``src`` folder_, with ``'first'`` and ``'last'`` as input, which is the same as

      .. code-block:: python

        return 'first', 'last'

      because ``first_input`` is ``'first'`` and ``last_input`` is ``'last'`` in the call to ``w_positional_arguments`` which will always

      .. code-block:: python
        :emphasize-text: first_input last_input

        return first_input, last_input

    - ``src.functions.w_positional_arguments('last', 'first')`` calls ``w_positional_arguments`` in ``functions.py`` in the ``src`` folder_, with ``'last'`` and ``'first'`` as input, which is the same as

      .. code-block:: python

        return 'last', 'first'

      because ``first_input`` is ``'last'`` and ``last_input`` is ``'first'`` in the call to ``w_positional_arguments`` which will always

      .. code-block:: python
        :emphasize-text: first_input last_input

        return first_input, last_input

    I must give input in the order a :ref:`function<what is a function?>` expects when I use `positional arguments`_, because it uses input in the order it gets them

:ref:`I can call functions with positional arguments<test_functions_w_positional_arguments>`

----

*********************************************************************************
test_functions_w_keyword_arguments
*********************************************************************************

There is a problem with using positional arguments, the inputs must always be given in the right order. This means the :ref:`function<what is a function?>` does something different when it gets input out of order.

I can use `Keyword Arguments`_ to make sure it does what I want even when I send input out of order.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 44
  :emphasize-lines: 11-17

      def test_functions_w_positional_arguments(self):
          self.assertEqual(
              src.functions.w_positional_arguments('first', 'last'),
              ('first', 'last')
          )
          self.assertEqual(
              src.functions.w_positional_arguments('last', 'first'),
              ('last', 'first')
          )

      def test_functions_w_keyword_arguments(self):
          self.assertEqual(
              src.functions.w_keyword_arguments(
                  first_input='first', last_input='last',
              ),
              ('first', 'last')
          )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_keyword_arguments'

``functions.py`` in the ``src`` folder_ is missing a definition for ``w_keyword_arguments``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function<what is a function?>` definition to ``functions.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 5-6

    def w_positional_arguments(first_input, last_input):
        return first_input, last_input


    def w_keyword_arguments():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_keyword_arguments() got an unexpected keyword argument 'first_input'

* I add the name of the unexpected argument_ in parentheses

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 1

    def w_keyword_arguments(first_input):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_keyword_arguments() got an unexpected keyword argument 'last_input'. Did you mean

* I add the name for the other unexpected argument_ in parentheses

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 1

    def w_keyword_arguments(first_input, last_input):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != ('first', 'last')

  I change the `return statement`_

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

    def w_keyword_arguments(first_input, last_input):
        return first_input, last_input

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another test with the `keyword arguments`_ given out of order in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 8-13

        def test_functions_w_keyword_arguments(self):
            self.assertEqual(
                src.functions.w_keyword_arguments(
                    first_input='first', last_input='last',
                ),
                ('first', 'last')
            )
            self.assertEqual(
                src.functions.w_keyword_arguments(
                    last_input='last', first_input='first',
                ),
                ('last', 'first')
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: Tuples differ: ('first', 'last') != ('last', 'first')

  the order stayed the same

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 12
    :emphasize-text: last

        def test_functions_w_keyword_arguments(self):
            self.assertEqual(
                src.functions.w_keyword_arguments(
                    first_input='first', last_input='last',
                ),
                ('first', 'last')
            )
            self.assertEqual(
                src.functions.w_keyword_arguments(
                    last_input='last', first_input='first',
                ),
                ('first', 'last')
            )

  the test passes. I can give the input in any order when I use `keyword arguments`_

* I can still call the :ref:`function<what is a function?>` the same way I did in :ref:`test_functions_w_positional_arguments` - without using the names. I add an :ref:`assertion<what is an assertion?>` to show this

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 7-10

            self.assertEqual(
                src.functions.w_keyword_arguments(
                    last_input='last', first_input='first',
                ),
                ('first', 'last')
            )
            self.assertEqual(
                src.functions.w_keyword_arguments('last', 'first'),
                ('first', 'last')
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: Tuples differ: ('last', 'first') != ('first', 'last')

  the :ref:`function<what is a function?>` uses the order (positions) when I do not use the names

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 16
    :emphasize-text: first

        def test_functions_w_keyword_arguments(self):
            self.assertEqual(
                src.functions.w_keyword_arguments(
                    first_input='first', last_input='last',
                ),
                ('first', 'last')
            )
            self.assertEqual(
                src.functions.w_keyword_arguments(
                    last_input='last', first_input='first',
                ),
                ('first', 'last')
            )
            self.assertEqual(
                src.functions.w_keyword_arguments('last', 'first'),
                ('last', 'first')
            )


    # Exceptions seen

  the test passes

.. NOTE::

  ``w_keyword_arguments`` and ``w_positional_arguments`` are the same functions_, they always

  .. code-block:: python

        return first_input, last_input

  Their names are different

  .. code-block:: python
    :emphasize-text: positional keyword

    def w_positional_arguments(first_input, last_input):
    def w_keyword_arguments(first_input, last_input):

  The difference that matters in the tests is how I call the functions_

  * I have to give the input in order when I use :ref:`positional arguments<test_functions_w_positional_arguments>`

    .. code-block:: python
      :emphasize-text: first

      w_positional_arguments('first', 'last') == return ('first', 'last')
      w_positional_arguments('last', 'first') == return ('last', 'first')
         w_keyword_arguments('last', 'first') == return ('last', 'first')

  * I can give the input in any order when I use `keyword arguments`_ because I give values for the names in parentheses from the :ref:`function<what is a function?>` definition when I call it

    .. code-block:: python
      :emphasize-text: first_input

      w_keyword_arguments(first_input='first', last_input='last')
      w_keyword_arguments(last_input='last', first_input='first')

    both of these statements are the same as

    .. code-block:: python

      return 'first', 'last'

    because ``first_input`` is ``'first'`` and ``last_input`` is ``'last'`` in the call to ``w_keyword_arguments`` which will always

    .. code-block:: python
      :emphasize-text: first_input last_input

      return first_input, last_input

:ref:`I can call a function with keyword arguments<test_functions_w_keyword_arguments>`

----

*********************************************************************************
test_functions_w_positional_and_keyword_arguments
*********************************************************************************

I can write functions_ that take both :ref:`positional<test_functions_w_positional_arguments>` and :ref:`keyword arguments<test_functions_w_keyword_arguments>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a failing test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 54
  :emphasize-lines: 19-25

        def test_functions_w_keyword_arguments(self):
            self.assertEqual(
                src.functions.w_keyword_arguments(
                    first_input='first', last_input='last',
                ),
                ('first', 'last')
            )
            self.assertEqual(
                src.functions.w_keyword_arguments(
                    last_input='last', first_input='first',
                ),
                ('first', 'last')
            )
            self.assertEqual(
                src.functions.w_keyword_arguments('last', 'first'),
                ('last', 'first')
            )

        def test_functions_w_positional_and_keyword_arguments(self):
            self.assertEqual(
                src.functions.w_positional_and_keyword_arguments(
                    last_input='last', 'first',
                ),
                ('first', 'last')
            )


    # Exceptions seen


the terminal_ shows SyntaxError_

.. code-block:: shell

  SyntaxError: positional argument follows keyword argument

I cannot put :ref:`keyword arguments<test_functions_w_keyword_arguments>` before :ref:`positional arguments<test_functions_w_positional_arguments>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I change the order of the arguments to follow Python_ rules

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 4

        def test_functions_w_positional_and_keyword_arguments(self):
            self.assertEqual(
                src.functions.w_positional_and_keyword_arguments(
                    'first', last_input='last',
                ),
                ('first', 'last')
            )

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions' has no attribute 'w_positional_and_keyword_arguments'

* I add a :ref:`function<what is a function?>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 5-6

      def w_keyword_arguments(first_input, last_input):
          return first_input, last_input


      def w_positional_and_keyword_arguments():
          return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_positional_and_keyword_arguments() got an unexpected keyword argument 'last_input'

* I add the name to the :ref:`function<what is a function?>` definition in parentheses in ``functions.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1
    :emphasize-text: last_input

    def w_positional_and_keyword_arguments(last_input):
        return None

  the terminal_ shows

  .. code-block:: shell

    TypeError: w_positional_and_keyword_arguments() got multiple values for argument 'last_input'

* I add another name in parentheses

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1
    :emphasize-text: first_input

    def w_positional_and_keyword_arguments(last_input, first_input):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_positional_and_keyword_arguments() got multiple values for argument 'last_input'

  I cannot put :ref:`positional arguments<test_functions_w_positional_arguments>` after :ref:`keyword arguments<test_functions_w_keyword_arguments>`. Python_ cannot tell the difference between the 2 values because ``last_input`` is both the second positional argument and passed in as a keyword argument

* I change the order of the names in parentheses

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1
    :emphasize-text: first_input

    def w_positional_and_keyword_arguments(first_input, last_input):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != ('first', 'last')

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2

    def w_positional_and_keyword_arguments(first_input, last_input):
        return first_input, last_input

  the test passes.

:ref:`I can call a function with positional and keyword arguments<test_functions_w_positional_and_keyword_arguments>`

----

*********************************************************************************
test_functions_w_default_arguments
*********************************************************************************

I can use :ref:`positional<test_functions_w_positional_arguments>` and :ref:`keyword arguments<test_functions_w_keyword_arguments>` when I want a :ref:`function<what is a function?>` to take inputs that are needed and inputs that are not

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a failing test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 72
  :emphasize-lines: 9-13

      def test_functions_w_positional_and_keyword_arguments(self):
          self.assertEqual(
              src.functions.w_positional_and_keyword_arguments(
                  'first', last_input='last',
              ),
              ('first', 'last')
          )

      def test_functions_w_default_arguments(self):
          self.assertEqual(
              src.functions.w_default_arguments('jane', last_name='doe'),
              ('jane', 'doe')
          )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_default_arguments'. Did you mean: 'w_keyword_arguments'?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` to ``functions.py``

.. code-block:: python
  :lineno-start: 34
  :emphasize-lines: 5-6

  def w_positional_and_keyword_arguments(first_input, last_input):
      return first_input, last_input


  def w_default_arguments(first_name, last_name):
      return first_name, last_name

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove ``, last_name='doe'`` from the call to ``w_default_arguments`` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 3

        def test_functions_w_default_arguments(self):
            self.assertEqual(
                src.functions.w_default_arguments('jane'),
                ('jane', 'doe')
            )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_default_arguments() missing 1 required positional argument: 'last_name'

  the ``last_name`` argument MUST be given when this :ref:`function<what is a function?>` is called

* I make the argument a choice by giving it a default value in ``functions.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 1

    def w_default_arguments(first_name, last_name='doe'):
        return first_name, last_name

  the test passes because the ``last_name`` argument no longer has to be given when this :ref:`function<what is a function?>` is called

  .. NOTE::

    If I call the :ref:`function<what is a function?>` without the ``last_name`` argument

    .. code-block:: python

      w_default_arguments('jane')

    it is the same as when I call it with the default value

    .. code-block:: python

      w_default_arguments('jane', last_name='doe')

    which is the same as

    .. code-block:: python

      return 'jane', 'doe'

    because ``w_default_arguments`` will always

    .. code-block:: python

      return first_name, last_name

* I add another :ref:`assertion<what is an assertion?>` to ``test_functions.py`` to show that I can still call the :ref:`function<what is a function?>` with different values

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 6-9

        def test_functions_w_default_arguments(self):
            self.assertEqual(
                src.functions.w_default_arguments('jane'),
                ('jane', 'doe')
            )
            self.assertEqual(
                src.functions.w_default_arguments('joe', 'blow'),
                ()
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: Tuples differ: ('joe', 'blow') != ()

  I change the expectation to match

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 8

        def test_functions_w_default_arguments(self):
            self.assertEqual(
                src.functions.w_default_arguments('jane'),
                ('jane', 'doe')
            )
            self.assertEqual(
                src.functions.w_default_arguments('joe', 'blow'),
                ('joe', 'blow')
            )


    # Exceptions seen

  the test passes

.. NOTE::

  ``w_keyword_arguments``, ``w_positional_arguments``,  ``w_positional_and_keyword_arguments`` and ``w_default_arguments`` are the same functions_, they always

  .. code-block:: python

    return first_input, last_input

  their names are different, ``w_default_arguments`` uses different names for the input and has a default value, it will always

  .. code-block:: python

    return first_name, last_name

  but ``first_input``, ``first_name``, ``last_input`` and ``last_name`` are just names, they could be any name

  .. code-block:: python
    :emphasize-text: positional keyword default

    def w_positional_arguments(first_input, last_input):
    def w_keyword_arguments(first_input, last_input):
    def w_positional_and_keyword_arguments(first_input, last_input):
    def w_default_arguments(first_name, last_name='doe'):

  The difference that matters in the tests is how I call the functions_

  .. code-block:: python
    :emphasize-text: last

                           w_positional_arguments('first', 'last') == return 'first', 'last'
                           w_positional_arguments('last', 'first') == return 'last',  'first'
       w_keyword_arguments(first_input='first', last_input='last') == return 'first', 'last'
       w_keyword_arguments(last_input='last', first_input='first') == return 'first', 'last'
                              w_keyword_arguments('last', 'first') == return 'last', 'first'
    w_positional_and_keyword_arguments('first', last_input='last') == return 'first', 'last'
                      w_default_arguments('jane', last_name='doe') == return 'jane', 'doe'
                                       w_default_arguments('jane') == return 'jane', 'doe'
                                w_default_arguments('joe', 'blow') == return 'joe', 'blow'

.. TIP::

  as a rule of thumb I use :ref:`keyword arguments<test_functions_w_keyword_arguments>` when I have 2 or more inputs so I do not have to remember the order

----

*********************************************************************************
test_functions_w_unknown_arguments
*********************************************************************************

I can make functions_ that take any number of :ref:`positional<test_functions_w_positional_arguments>` and :ref:`keyword<test_functions_w_keyword_arguments>` arguments. This means I do not need to know how many inputs are sent to the :ref:`function<what is a function?>` when it is called

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 80
  :emphasize-lines: 11-17

      def test_functions_w_default_arguments(self):
          self.assertEqual(
              src.functions.w_default_arguments('jane'),
              ('jane', 'doe')
          )
          self.assertEqual(
              src.functions.w_default_arguments('joe', 'blow'),
              ('joe', 'blow')
          )

      def test_functions_w_unknown_arguments(self):
          self.assertEqual(
              src.functions.w_unknown_arguments(
                  0, 1, 2, 3, a=4, b=5, c=6, d=7,
              ),
              None
          )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_unknown_arguments'. Did you mean: 'w_keyword_arguments'?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function<what is a function?>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 5-6

    def w_default_arguments(first_name, last_name='doe'):
        return first_name, last_name


    def w_unknown_arguments():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_unknown_arguments() got an unexpected keyword argument 'a'

* I add the name to the :ref:`function<what is a function?>` definition

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1

    def w_unknown_arguments(a):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_unknown_arguments() got multiple values for argument 'a'

  I had this same problem in :ref:`test_functions_w_positional_and_keyword_arguments`. Python_ cannot tell if ``a`` is a :ref:`positional<test_functions_w_positional_arguments>` or :ref:`keyword argument<test_functions_w_keyword_arguments>` in this case

* Python_ has a way for a :ref:`function<what is a function?>` to get any number of :ref:`keyword arguments<test_functions_w_keyword_arguments>` without knowing how many they are. I use it to replace ``a`` in the parentheses

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1

    def w_unknown_arguments(**kwargs):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_unknown_arguments() takes 0 positional arguments but 4 were given

* I add a name for the first :ref:`positional argument<test_functions_w_positional_arguments>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1
    :emphasize-text: x

    def w_unknown_arguments(**kwargs, x):
        return None

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: arguments cannot follow var-keyword argument

  a reminder that I cannot put :ref:`positional arguments<test_functions_w_positional_arguments>` after :ref:`keyword arguments<test_functions_w_keyword_arguments>`

* I change the order of the inputs in ``w_unknown_arguments`` in ``functions.py``

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1
    :emphasize-text: x

    def w_unknown_arguments(x, **kwargs):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_unknown_arguments() takes 1 positional argument but 4 were given

* I can add names for the other :ref:`positional arguments<test_functions_w_positional_arguments>`, or I can use what Python_ has to handle any number of :ref:`positional arguments<test_functions_w_positional_arguments>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1

    def w_unknown_arguments(*args, **kwargs):
        return None

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* ``*args, **kwargs`` is :ref:`Python convention<conventions>`. I change the names to be clearer

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1

    def w_unknown_arguments(*positional_arguments, **keyword_arguments):
        return None

  the test is still green

* I want the :ref:`function<what is a function?>` to return its input, remember the :ref:`identity function<test_identity_function>`? I change the `return statement`_

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2

    def w_unknown_arguments(*positional_arguments, **keyword_arguments):
        return positional_arguments, keyword_arguments

  the terminal_ shows

  .. code-block:: shell

    AssertionError: ((0, 1, 2, 3), {'a': 4, 'b': 5, 'c': 6, 'd': 7}) != None

  I get a tuple_ that has another tuple_ and a :ref:`dictionary<what is a dictionary?>`

* I copy the tuple_ from the terminal_ and use it to change the expectation in ``test_functions_w_unknown_arguments`` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 6

        def test_functions_w_unknown_arguments(self):
            self.assertEqual(
                src.functions.w_unknown_arguments(
                    0, 1, 2, 3, a=4, b=5, c=6, d=7,
                ),
                ((0, 1, 2, 3), {'a': 4, 'b': 5, 'c': 6, 'd': 7})
            )

  the test passes

----

*********************************************************************************
how Python reads positional arguments
*********************************************************************************

I want to see what happens when I call ``w_unknown_arguments`` with ONLY :ref:`positional arguments<test_functions_w_positional_arguments>`. I add an :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :lineno-start: 90
  :emphasize-lines: 8-11

      def test_functions_w_unknown_arguments(self):
          self.assertEqual(
              src.functions.w_unknown_arguments(
                  0, 1, 2, 3, a=4, b=5, c=6, d=7,
              ),
              ((0, 1, 2, 3, ), {'a': 4, 'b': 5, 'c': 6, 'd': 7})
          )
          self.assertEqual(
              src.functions.w_unknown_arguments(0, 1, 2, 3),
              ()
          )


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: Tuples differ: ((0, 1, 2, 3), {}) != ()

I change the expectation to match

.. code-block:: python
  :lineno-start: 97
  :emphasize-lines: 3

          self.assertEqual(
              src.functions.w_unknown_arguments(0, 1, 2, 3),
              ((0, 1, 2, 3), {})
          )


  # Exceptions seen

the test passes. The :ref:`function<what is a function?>` reads the :ref:`positional arguments<test_functions_w_positional_arguments>` as a tuple_ (things in parentheses (``()``) separated by commas)

----

*********************************************************************************
how Python reads keyword arguments
*********************************************************************************


I add another :ref:`assertion<what is an assertion?>` to see what happens when I call the :ref:`function<what is a function?>` with ONLY :ref:`keyword arguments<test_functions_w_keyword_arguments>`

.. code-block:: python
  :lineno-start: 97
  :emphasize-lines: 5-8

          self.assertEqual(
              src.functions.w_unknown_arguments(0, 1, 2, 3),
              ((0, 1, 2, 3))
          )
          self.assertEqual(
              src.functions.w_unknown_arguments(a=4, b=5, c=6, d=7),
              ()
          )


  # Exceptions seen

the terminal_ shows

.. code-block:: python

  AssertionError: Tuples differ: ((), {'a': 4, 'b': 5, 'c': 6, 'd': 7}) != ()

I change the expectation to match

.. code-block:: python
  :lineno-start: 101
  :emphasize-lines: 3

          self.assertEqual(
              src.functions.w_unknown_arguments(a=4, b=5, c=6, d=7),
              ((), dict(a=4, b=5, c=6, d=7))
          )


  # Exceptions seen

the test passes. The :ref:`function<what is a function?>` reads the :ref:`keyword arguments<test_functions_w_keyword_arguments>` as a :ref:`dictionary<dictionaries>` (:ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces (``{}``) separated by commas)

----

*********************************************************************************
how Python reads positional and keyword arguments
*********************************************************************************

I add one more :ref:`assertion<what is an assertion?>` to see what happens when I call the :ref:`function<what is a function?>` with no inputs

.. code-block:: python
  :lineno-start: 101
  :emphasize-lines: 5-8

          self.assertEqual(
              src.functions.w_unknown_arguments(a=4, b=5, c=6, d=7),
              ((), dict(a=4, b=5, c=6, d=7))
          )
          self.assertEqual(
              src.functions.w_unknown_arguments(),
              ()
          )


  # Exceptions seen

the terminal_ shows

.. code-block:: shell

  AssertionError: Tuples differ: ((), {}) != ()

I change the expectation to match

.. code-block:: python
  :lineno-start: 90
  :emphasize-lines: 18

      def test_functions_w_unknown_arguments(self):
          self.assertEqual(
              src.functions.w_unknown_arguments(
                  0, 1, 2, 3, a=4, b=5, c=6, d=7,
              ),
              ((0, 1, 2, 3, ), {'a': 4, 'b': 5, 'c': 6, 'd': 7})
          )
          self.assertEqual(
              src.functions.w_unknown_arguments(0, 1, 2, 3),
              ((0, 1, 2, 3), {})
          )
          self.assertEqual(
              src.functions.w_unknown_arguments(a=4, b=5, c=6, d=7),
              ((), dict(a=4, b=5, c=6, d=7))
          )
          self.assertEqual(
              src.functions.w_unknown_arguments(),
              ((), {})
          )


  # Exceptions seen

the test passes

.. NOTE::

  these statements are the same

  .. code-block:: python

    w_unknown_arguments(0, 1, 2, 3, a=4, b=5, c=6, d=7)
    w_unknown_arguments(*(0, 1, 2, 3), **dict(a=4, b=5, c=6, d=7))
    w_unknown_arguments(*(0, 1, 2, 3), **{'a': 4, 'b': 5, 'c': 6, 'd': 7})
    ((0, 1, 2, 3, ), {'a': 4, 'b': 5, 'c': 6, 'd': 7})

  because ``w_unknown_arguments`` in ``functions.py`` in the ``src`` folder will always

  .. code-block:: python

    return positional_arguments, keyword_arguments

  in this case

  .. code-block:: python

    0, 1, 2, 3
    *(0, 1, 2, 3)

  are :ref:`positional arguments<test_functions_w_positional_arguments>` which are taken as a tuple_ and

  .. code-block:: python

    a=4, b=5, c=6, d=7
    **dict(a=4, b=5, c=6, d=7)
    **{'a': 4, 'b': 5, 'c': 6, 'd': 7}

  are :ref:`keyword arguments<test_functions_w_keyword_arguments>` which are taken as a :ref:`dictionary<what is a dictionary?>`. The :ref:`function<what is a function?>` reads :ref:`positional arguments<test_functions_w_positional_arguments>` as tuples_, and :ref:`keyword arguments<test_functions_w_keyword_arguments>` as :ref:`dictionaries`, which is why the :ref:`update method of dictionaries<test_update_a_dictionary>` can take a :ref:`dictionary<dictionaries>` as input

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_functions.py`` and ``functions.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and use :kbd:`q` on the keyboard to leave the tests and the terminal_ goes back to the command line

* I `change directory`_ to the parent of ``functions``

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

I ran tests to show that I can make functions_ with

* the def_ keyword
* :ref:`positional arguments<test_functions_w_positional_arguments>`
* :ref:`keyword arguments<test_functions_w_keyword_arguments>`
* :ref:`positional and keyword arguments<test_functions_w_positional_and_keyword_arguments>`
* :ref:`default values<test_functions_w_default_arguments>`
* :ref:`can take any number of inputs<test_functions_w_unknown_arguments>`

as a reminder

* :ref:`I can use '*args' when I do not know how many positional arguments the function has to take<test_functions_w_unknown_arguments>`
* :ref:`positional arguments are taken as a tuple<how Python reads positional arguments>`
* :ref:`positional arguments must come before keyword arguments<test_functions_w_default_arguments>`
* :ref:`I can use '**kwargs' when I do not know how many keyword arguments the function<test_functions_w_unknown_arguments>`
* :ref:`keyword arguments are taken as a dictionary<how Python reads keyword arguments>`
* :ref:`the identity function returns its input<test_identity_function>`
* :ref:`constant functions always return the same thing<test_constant_function>`
* :ref:`nothing runs after the return statement in a function<test_what_happens_after_a_function_returns>`
* :ref:`functions return None by default<test_making_a_function_w_return_none>`

:ref:`How many questions can you answer about functions?<questions about functions>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<functions: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have covered a bit so far and know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>` and
* :ref:`how to make functions<what is a function?>`

:ref:`Would you like to know what causes AttributeError?<what causes AttributeError?>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->