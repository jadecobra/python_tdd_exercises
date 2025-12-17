.. meta::
   :description: Learn Python functions with TDD! Explore arguments, defaults, and testing techniques in this practical guide. Start coding now!
   :keywords: Jacob Itegboje, Python functions, Test-Driven Development, Python programming, keyword arguments, positional arguments, coding tutorial

.. include:: links.rst

.. _function: https://docs.python.org/3/glossary.html#term-function
.. _functions: function_
.. _argument: https://docs.python.org/3/glossary.html#term-argument
.. _arguments: argument_
.. _keyword arguments: arguments_
.. _positional arguments: arguments_

#################################################################################
functions
#################################################################################

A function_ is a unit or block of code that is callable_. This means I can write statements that I can use to do something at a different time from when I write them. They can make code smaller, easier to read, test, reuse, maintain and improve.

`Computer Programming`_ involves providing a process with input data and the process returning output data, for example

.. code-block:: none

    input_data -> program -> output_data

I think of it mathematically as mapping a :ref:`function<test_functions>` ``f`` with inputs ``x`` and an output of ``y``

.. math::

  f(x) -> y

in other words

.. math:

  function(input_data) -> output_data

the function_ processes ``input_data`` and returns ``output_data`` as the result

functions_ are made with the def_ keyword, a name, parentheses and a colon at the end

.. code-block:: python

  def name_of_function():

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: code/tests/test_functions.py
  :language: python
  :linenos:

*********************************************************************************
questions about functions
*********************************************************************************

Here are the questions you can answer after going through this chapter

* :ref:`What is a Function?<functions>`
* :ref:`What do functions return by default?<test_making_a_function_w_return_none>`
* :ref:`What is a constant function?<test_constant_function>`
* :ref:`What is the identity function?<test_identity_function>`
* :ref:`What is a positional argument?<test_functions_w_positional_arguments>`
* :ref:`What is a keyword argument?<test_functions_w_keyword_arguments>`
* :ref:`How can I make arguments optional in a function?<test_functions_w_default_arguments>`
* :ref:`How can I make a function take an unknown number of positional arguments?<test_functions_w_unknown_arguments>`
* :ref:`How can I make a function take an unknown number of keyword arguments?<test_functions_w_unknown_arguments>`
* :ref:`How are positional arguments represented in a function?<test_functions_w_unknown_arguments>`
* :ref:`How are keyword arguments represented in a function?<test_functions_w_unknown_arguments>`

----

*********************************************************************************
requirements
*********************************************************************************

* I pick ``functions`` as the name of this project
* I open a terminal_
* then I `make a directory`_ for the project

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir functions

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python

* I `change directory`_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd functions

  the terminal_ shows I am now in the ``functions`` folder_

  .. code-block:: shell

    .../pumping_python/functions

* I `make a folder`_ for the source code

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/functions

* I use touch_ to make an empty file_ for the program_ in the ``src`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    touch src/functions.py

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``New-Item src/functions.py`` instead of ``touch src/functions.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item src/functions.py

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/functions

* I `make a directory`_ for the tests

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line

* I use touch_ to make an empty file_ in the ``tests`` folder_ to tell Python_ that it is a `Python package`_

  .. ATTENTION:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/__init__.py

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``New-Item tests/__init__.py`` instead of ``touch tests/__init__.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/__init__.py

  the terminal_ goes back to the command line

* I make an empty file_ for the actual test

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/test_functions.py

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``New-Item tests/test_functions.py`` instead of ``touch tests/test_functions.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/test_functions.py

  the terminal_ goes back to the command line

* I click on ``test_functions.py`` in the `Integrated Development Environment (IDE)`_ to open it in the :ref:`editor<2 editors>`

  .. TIP:: I can open a file_ from the terminal_ in `Visual Studio Code`_ by typing ``code`` and the name of the file_ with

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_functions.py

  ``test_functions.py`` opens up in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_functions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-11

    import unittest


    class TestFunctions(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError

* I make a `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m venv .venv

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``python3 -m venv .venv`` instead of ``python3 -m venv .venv``

    .. code-block:: shell
      :emphasize-lines: 1

      python -m venv .venv

  the terminal_ takes some time then goes back to the command line

* I activate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    source .venv/bin/activate

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` instead of ``source .venv/bin/activate``

    .. code-block:: shell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/functions

* I upgrade the `Python package manager (pip)`_ to the latest version

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m pip install --upgrade pip

  the terminal_ shows pip_ being uninstalled then installs the latest version or shows that it is already the latest version

* I make a ``requirements.txt`` file for the `Python programs`_ my project needs

  .. code-block:: shell
    :emphasize-lines: 1

    echo "pytest-watch" > requirements.txt

  the terminal_ goes back to the command line

* I use pip_ to use the requirements file_ to install ``pytest-watch``

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m pip install --requirement requirements.txt

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``python -m pip install --requirement requirements.txt`` instead of ``python3 -m pip install --requirement requirements.txt``

    .. code-block:: shell
      :emphasize-lines: 1

      python -m pip install --requirement requirements.txt

  the terminal_ shows pip_ downloads and installs the `Python programs`_ that `pytest-watch`_ needs to run

* I run the tests

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 8, 10

    ================================ FAILURES ================================
    _______________________ TestFunctions.test_failure _______________________

    self = <tests.test_functions.TestFunctions testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       Functions: True is not false

    tests/test_functions.py:7: Functions
    ======================== short test summary info =========================
    FAILED tests/test_functions.py::TestFunctions::test_failure - Functions: True is not false
    =========================== 1 failed in X.YZs ============================

* I hold ``ctrl`` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_functions.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
test_making_a_function_w_pass
*********************************************************************************

I can make a function_ with the pass_ keyword

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I change ``test_failure`` to ``test_making_a_function_w_pass``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    import unittest


    class TestFunctions(unittest.TestCase):

        def test_making_a_function_w_pass(self):
            self.assertIsNone(src.functions.w_pass())


    # Exceptions Encountered

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block::

    NameError: name 'src' is not defined

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # NameError

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add an `import statement`_ at the top of the file

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.functions
    import unittest


    class TestFunctions(unittest.TestCase):

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.functions' has no attribute 'w_pass'

  ``functions.py`` in the ``src`` folder_ does not have anything named ``w_pass`` inside it

* I add to the list of :ref:`Exceptions<errors>` encountered

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* I open ``functions.py`` from the ``src`` folder in the :ref:`editor<2 editors>`, then I add a function_ definition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def w_pass():
        pass

  the test passes

  * the test checks if the result of the call to ``src.functions.w_pass`` is :ref:`None`
  * the function_ definition simply says pass_ and the test passes
  * pass_ is a placeholder keyword which allows the function_ definition to follow Python_ language rules
  * the test passes because all functions_ return :ref:`None` by default, as if the function_ has an invisible line that says ``return None``, which leads me to the next test

----

*********************************************************************************
test_making_a_function_w_return
*********************************************************************************

I can make a function with a `return statement`_

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new failing test in ``test_functions.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 4-5

      def test_making_a_function_w_pass(self):
          self.assertIsNone(src.functions.w_pass())

      def test_making_a_function_w_return(self):
          self.assertIsNone(src.functions.w_return())


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_return'

``functions.py`` in the ``src`` folder_ does not have ``w_return`` in it

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a new function_ with pass_ to ``functions.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 5-6

  def w_pass():
      pass


  def w_return():
      pass

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

I change pass_ to a `return statement`_

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 2

  def w_return():
      return

the test is still green.

I have 2 functions_ with different statements in their body but they both return :ref:`None`, because "all functions_ return :ref:`None` by default, as if the function_ has an invisible line that says ``return None``", which leads me to the next test

*********************************************************************************
test_making_a_function_w_return_none
*********************************************************************************

I can make a function_ with a `return statement`_ that says what the function_ returns

*********************************************************************************
:red:`RED`: make it fail
*********************************************************************************

I add another failing test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 4-5

      def test_making_a_function_w_return(self):
          self.assertIsNone(src.functions.w_return())

      def test_making_a_function_w_return_none(self):
          self.assertIsNone(src.functions.w_return_none())


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_return_none'

``w_return_none`` is not defined in ``functions.py`` in the ``src`` folder_

*********************************************************************************
:green:`GREEN`: make it pass
*********************************************************************************

I add a function_ definition to ``functions.py``

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 5-6

  def w_return():
      return


  def w_return_none():
      return

the test passes

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

I add :ref:`None` to the `return statement`_

.. code-block:: python
  :lineno-start: 9
  :emphasize-lines: 2

  def w_return_none():
      return None

I like to write my functions_ this way, saying exactly what it returns, that way anyone can tell what the function_ returns without knowing what it does or even understanding Python_ code

----

*********************************************************************************
test_constant_function
*********************************************************************************

constant functions_ always return the same thing when they are called

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 4-8

      def test_making_a_function_w_return_none(self):
          self.assertIsNone(src.functions.w_return_none())

      def test_constant_function(self):
          self.assertEqual(
              src.functions.constant(),
              'the same thing'
          )


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'constant'

I have not added a definition for ``constant`` in ``functions.py`` in the ``src`` folder_

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the function_ to ``functions.py``

.. code-block:: python
  :lineno-start: 9
  :emphasize-lines: 5-6

  def w_return_none():
      return None


  def constant():
      return None

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: None != 'the same thing'

what the ``constant`` function_ returns and what the test expects are different. I change the `return statement`_ to make them match

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 2

  def constant():
      return 'the same thing'

the test passes.

A constant function_ always return the same thing when called, I can use them in place of variables_, though the number of cases where they are faster than :ref:`variables<test_attribute_error_w_variables>` is pretty small. It is something like if the function_ is called less than 10 times, but who's counting?

----

*********************************************************************************
test_identity_function
*********************************************************************************

The identity function_ returns its input as output, it's also in the :ref:`Truth Table<booleans: truth table>` chapter in :ref:`test_logical_identity`

*********************************************************************************
:red:`RED`: make it fail
*********************************************************************************

I add a failing test in ``test_functions.py``

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 7-8

      def test_constant_function(self):
          self.assertEqual(
              src.functions.constant(),
              'the same thing'
          )

      def test_identity_function(self):
          self.assertIsNone(src.functions.identity(None))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'identity'

*********************************************************************************
:green:`GREEN`: make it pass
*********************************************************************************

* I add a function_ to ``functions.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5-6

    def constant():
        return 'the same thing'


    def identity():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: identity() takes 0 positional arguments but 1 was given

  the definition for ``identity`` does not allow inputs and the test sends :ref:`None` as input

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 5

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add a name in parentheses for the ``identity`` function_ to take input in ``functions.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1

    def identity(the_input):
        return None

  the test passes. I am genius

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

The requirement for the :ref:`identity function<test_logical_identity>` is that it returns the same thing it is given, the test is currently passing when :ref:`None` is given as input. Does it pass when another value is given or does it always return :ref:`None`? Time to write a test

* I add a new :ref:`assertion<AssertionError>` to ``test_identity_function`` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3

    def test_identity_function(self):
        self.assertIsNone(src.functions.identity(None))
        self.assertEqual(src.functions.identity(object), object)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != <class 'object'>

  the function_ returns :ref:`None` instead of ``<class 'object'>`` in the second case, I am not all the way genius, yet

* I change the `return statement`_ of ``identity`` in ``functions.py`` to match the expectation

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

    def identity(the_input):
        return the_input

  the test passes

I sometimes use the :ref:`Identity Function<test_identity_function>` when I am testing connections to see if my test is connected to what I am testing. If I can send input and received the same input back then I can start making changes to see what results I get.

The :ref:`Identity Function<test_identity_function>` takes one input, the following tests are for functions_ that take more than one.

----

*********************************************************************************
test_functions_w_positional_arguments
*********************************************************************************

*********************************************************************************
:red:`RED`: make it fail
*********************************************************************************

I add a failing test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 5-9

      def test_identity_function(self):
          self.assertIsNone(src.functions.identity(None))
          self.assertEqual(src.functions.identity(object), object)

      def test_functions_w_positional_arguments(self):
          self.assertEqual(
              src.functions.w_positional_arguments('first', 'last'),
              ('first', 'last')
          )


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_positional_arguments'

*********************************************************************************
:green:`GREEN`: make it pass
*********************************************************************************

* I add a function_ to  ``functions.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5-6

    def identity(the_input):
        return the_input


    def w_positional_arguments():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_positional_arguments() takes 0 positional arguments but 2 were given

* I make the function_ take input by adding a name in parentheses

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 1

    def w_positional_arguments(first_input):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_positional_arguments() takes 1 positional argument but 2 were given

* I make ``w_positional_arguments`` take another input by adding another name in parentheses

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 1

    def w_positional_arguments(first_input, last_input):
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != ('first', 'last')

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def w_positional_arguments(first_input, last_input):
        return first_input, last_input

  the test passes

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

* The problem with giving arguments this way is that they have to be in the order the function_ expects or I get a different behavior. I add a test to ``test_functions.py`` to show this

  .. code-block:: python
    :lineno-start: 26
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


    # Exceptions Encountered

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ('last', 'first') != ('first', 'last')

* I change the expectation of the test in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 3

          self.assertEqual(
              src.functions.w_positional_arguments('last', 'first'),
              ('last', 'first')
          )

  the test passes.

The order matters when passing `positional arguments`_ to a function_, because they are processed based on the position or in the order they are given to the function_

----

*********************************************************************************
test_functions_w_keyword_arguments
*********************************************************************************

There is a problem with using positional arguments, the inputs must always be supplied in the right order, which means the function_ behaves in an unexpected way when it gets input out of order.

I can use `Keyword Arguments`_ to make sure it behaves how I want even when I send input out of order

*********************************************************************************
:red:`RED`: make it fail
*********************************************************************************

I add a new test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 31
  :emphasize-lines: 6-12

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


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_keyword_arguments'

``functions.py`` in the ``src`` folder_ is missing a definition for ``w_keyword_arguments``

*********************************************************************************
:green:`GREEN`: make it pass
*********************************************************************************

* I add a function_ definition to ``functions.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-6

    def w_positional_arguments(first_input, last_input):
        return first_input, last_input


    def w_keyword_arguments():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_keyword_arguments() got an unexpected keyword argument 'first_input'

* I add the name for the argument_ in parentheses

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 1

    def w_keyword_arguments(first_input):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_keyword_arguments() got an unexpected keyword argument 'last_input'. Did you mean

* I add the name in parentheses

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 1

    def w_keyword_arguments(first_input, last_input):
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != ('first', 'last')

  I change the `return statement`_

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

    def w_keyword_arguments(first_input, last_input):
        return first_input, last_input

  the test passes

``w_keyword_arguments`` and ``w_positional_arguments`` are the same functions_. The only difference in the definitions is their names. The difference that matters in the tests is in how I call the functions_.

In the first case I use :ref:`positional arguments<test_functions_w_positional_arguments>` which have to be given in order

.. code-block:: python

  w_positional_arguments('first', 'last')
  w_positional_arguments('last', 'first')

in the second case I use `keyword arguments`_ which use the names of the :ref:`variables<test_attribute_error_w_variables>` in parentheses in the function_ definition when calling the it

.. code-block:: python

  w_keyword_arguments(first_input='first', last_input='last')

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

* I add another test with the `keyword arguments`_ given out of order in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 36
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

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ('first', 'last') != ('last', 'first')

  the order stayed the same

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 5

            self.assertEqual(
                src.functions.w_keyword_arguments(
                    last_input='last', first_input='first',
                ),
                ('first', 'last')
            )

  the test passes. `Keyword Arguments`_ allow the input to be passed in any order

* I can still call the function_ without using the names, the same way I did in :ref:`test_functions_w_positional_arguments`. I add an :ref:`assertion<AssertionError>` to show this

  .. code-block:: python
    :lineno-start: 43
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

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ('last', 'first') != ('first', 'last')

  I change the expectation to match

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 3

          self.assertEqual(
              src.functions.w_keyword_arguments('last', 'first'),
              ('last', 'first')
          )


    # Exceptions Encountered

  the test passes

:ref:`Positional Arguments<test_functions_w_positional_arguments>` MUST be given in the expected order, `Keyword Arguments`_ can be given in any order

----

*********************************************************************************
test_functions_w_positional_and_keyword_arguments
*********************************************************************************

I can write functions_ that take both :ref:`positional<test_functions_w_positional_arguments>` and `keyword arguments<test_functions_w_keyword_arguments>`

*********************************************************************************
:red:`RED`: make it fail
*********************************************************************************

I add a failing test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 49
  :emphasize-lines: 6-12

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


  # Exceptions Encountered


the terminal_ shows SyntaxError_

.. code-block:: shell

  SyntaxError: positional argument follows keyword argument

I cannot put a :ref:`keyword argument<test_functions_w_keyword_arguments>` before a :ref:`positional argument<test_functions_w_positional_arguments>` in Python_

*********************************************************************************
:green:`GREEN`: make it pass
*********************************************************************************

* I change the order of the arguments to follow Python_ rules

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 4

        def test_functions_w_positional_and_keyword_arguments(self):
            self.assertEqual(
                src.functions.w_positional_and_keyword_arguments(
                    'first', last_input='last',
                ),
                ('first', 'last')
            )

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.functions' has no attribute 'w_positional_and_keyword_arguments'

* I add a function_ to ``functions.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5-6

      def w_keyword_arguments(first_input, last_input):
          return first_input, last_input


      def w_positional_and_keyword_arguments():
          return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_positional_and_keyword_arguments() got an unexpected keyword argument 'last_input'

* I add the name to the function_ definition in parentheses in ``functions.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 1

    def w_positional_and_keyword_arguments(last_input):
        return None

  the terminal_ shows

  .. code-block:: shell

    TypeError: w_positional_and_keyword_arguments() got multiple values for argument 'last_input'

* I add another name in parentheses

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 1

    def w_positional_and_keyword_arguments(last_input, first_input):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_positional_and_keyword_arguments() got multiple values for argument 'last_input'

  Python_ cannot tell the difference between the 2 values since ``last_input`` is both the second positional argument and passed in as a keyword argument

* I change the order of the names in parentheses

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 1

    def w_positional_and_keyword_arguments(first_input, last_input):
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != ('first', 'last')

  I cannot put :ref:`positional arguments<test_functions_w_positional_arguments>` after :ref:`keyword arguments<test_functions_w_keyword_arguments>`

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    def w_positional_and_keyword_arguments(first_input, last_input):
        return first_input, last_input

  the test passes.

There is no difference between the last 3 functions except their names, they all have this pattern

.. code-block:: python

  def a_name(first_input, last_input):
      return first_input, last_input

what is different is the way I called them in the tests

.. code-block:: python

  w_positional_arguments('first', 'last')
  w_positional_arguments('first', 'last')
  w_keyword_arguments(first_input='first', last_input='last')
  w_keyword_arguments(last_input='last', first_input='first')
  w_keyword_arguments('last', 'first')
  w_positional_and_keyword_arguments('first', last_input='last')

----

*********************************************************************************
test_functions_w_default_arguments
*********************************************************************************

I can use :ref:`positional<test_functions_w_positional_arguments>` and :ref:`keyword arguments<test_functions_w_keyword_arguments>` when I want a function_ to take inputs that are needed and inputs that are NOT needed

*********************************************************************************
:red:`RED`: make it fail
*********************************************************************************

I add a failing test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 54
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


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_default_arguments'. Did you mean: 'w_keyword_arguments'?

*********************************************************************************
:green:`GREEN`: make it pass
*********************************************************************************

I add a function_ to ``functions.py``

.. code-block:: python
  :lineno-start: 29
  :emphasize-lines: 5-6

  def w_positional_and_keyword_arguments(first_input, last_input):
      return first_input, last_input


  def w_default_arguments(first_name, last_name):
      return first_name, last_name

the test passes

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

* I remove ``last_name='doe'`` from the call to ``w_default_arguments`` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3

        def test_functions_w_default_arguments(self):
            self.assertEqual(
                src.functions.w_default_arguments('jane'),
                ('jane', 'doe')
            )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_default_arguments() missing 1 required positional argument: 'last_name'

  the ``last_name`` argument is needed when the function_ is called

* I make the argument a choice by giving it a default value in ``functions.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 1

    def w_default_arguments(first_name, last_name='doe'):
        return first_name, last_name

  the test passes.

* Calling the function_ without the ``last_name`` argument

  .. code-block:: python

    w_default_arguments('jane')

  is now the same as calling it with the default value

  .. code-block:: python

    w_default_arguments('jane', last_name='doe')

  I add another :ref:`assertion<AssertionError>` to ``test_functions.py`` to show that I can still call the function_ with different values

  .. code-block:: python
    :lineno-start: 62
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


    # Exceptions Encountered

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ('joe', 'blow') != ()

  I change the expectation to match

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 3

            self.assertEqual(
                src.functions.w_default_arguments('joe', 'blow'),
                ('joe', 'blow')
            )

  the test passes

----

*********************************************************************************
test_functions_w_unknown_arguments
*********************************************************************************

I can make functions_ that take any number of :ref:`positional<test_functions_w_positional_arguments>` and :ref:`keyword<test_functions_w_keyword_arguments>` arguments. This means I do not need to know how many inputs are sent to the function_ when it is called

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 67
  :emphasize-lines: 6-12

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


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_unknown_arguments'. Did you mean: 'w_keyword_arguments'?

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add a function_ to ``functions.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5-6

    def w_default_arguments(first_name, last_name='doe'):
        return first_name, last_name


    def w_unknown_arguments():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_unknown_arguments() got an unexpected keyword argument 'a'

* I add the name to the function_ definition

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

    def w_unknown_arguments(a):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_unknown_arguments() got multiple values for argument 'a'

  I had this same problem in :ref:`test_functions_w_positional_and_keyword_arguments`, Python_ cannot tell which arguments are :ref:`positional<test_functions_w_positional_arguments>` or :ref:`keyword arguments<test_functions_w_keyword_arguments>` yet

* Python_ has a way to allow passing any number of :ref:`keyword arguments<test_functions_w_keyword_arguments>` without knowing how many they are. I use it to replace ``a`` in the parentheses

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

    def w_unknown_arguments(**kwargs):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_unknown_arguments() takes 0 positional arguments but 4 were given

* I add a name for the first :ref:`positional argument<test_functions_w_positional_arguments>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

    def w_unknown_arguments(**kwargs, x):
        return None

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: arguments cannot follow var-keyword argument

  a reminder that I cannot put :ref:`positional arguments<test_functions_w_positional_arguments>` after :ref:`keyword arguments<test_functions_w_keyword_arguments>`

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` encountered in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 6

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I change the order of the inputs in ``w_unknown_arguments`` in ``functions.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

    def w_unknown_arguments(x, **kwargs):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_unknown_arguments() takes 1 positional argument but 4 were given

* I can add names for the other :ref:`positional arguments<test_functions_w_positional_arguments>`, or I can do something like what I did with the :ref:`keyword arguments<test_functions_w_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

    def w_unknown_arguments(*args, **kwargs):
        return None

  the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* ``*args, **kwargs`` is Python_ convention. I change the names to be more descriptive

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

    def w_unknown_arguments(*arguments, **keyword_arguments):
        return None

  the test is still green

* I want the function_ to return its input, I change the `return statement`_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

    def w_unknown_arguments(*arguments, **keyword_arguments):
        return arguments, keyword_arguments

  the terminal_ shows

  .. code-block:: shell

    AssertionError: ((0, 1, 2, 3), {'a': 4, 'b': 5, 'c': 6, 'd': 7}) != None

* I copy the tuple_ from the terminal_ and use it to change the expectation in ``test_functions_w_unknown_arguments`` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 6

        def test_functions_w_unknown_arguments(self):
            self.assertEqual(
                src.functions.w_unknown_arguments(
                    0, 1, 2, 3, a=4, b=5, c=6, d=7,
                ),
                ((0, 1, 2, 3), {'a': 4, 'b': 5, 'c': 6, 'd': 7})
            )

  the test passes

* I want to see what happens when I call the function_ without :ref:`keyword arguments<test_functions_w_keyword_arguments>`. I add a new :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 7-10

            self.assertEqual(
                src.functions.w_unknown_arguments(
                    0, 1, 2, 3, a=4, b=5, c=6, d=7,
                ),
                ((0, 1, 2, 3), {'a': 4, 'b': 5, 'c': 6, 'd': 7})
            )
            self.assertEqual(
                src.functions.w_unknown_arguments(0, 1, 2, 3),
                ()
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ((0, 1, 2, 3), {}) != ()

  I change the expectation to match

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 3

            self.assertEqual(
                src.functions.w_unknown_arguments(0, 1, 2, 3),
                ((0, 1, 2, 3), {})
            )


    # Exceptions Encountered

  the test passes

* I add another :ref:`assertion<AssertionError>` to see what happens when I call the function_ without :ref:`positional arguments<test_functions_w_positional_arguments>`

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 5-8

            self.assertEqual(
                src.functions.w_unknown_arguments(0, 1, 2, 3),
                ((0, 1, 2, 3), {})
            )
            self.assertEqual(
                src.functions.w_unknown_arguments(a=4, b=5, c=6, d=7),
                ()
            )

  the terminal_ shows

  .. code-block:: shell

    AssertionError: Tuples differ: ((), {'a': 4, 'b': 5, 'c': 6, 'd': 7}) != ()

  I change the expectation to match

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 3

            self.assertEqual(
                src.functions.w_unknown_arguments(a=4, b=5, c=6, d=7),
                ((), dict(a=4, b=5, c=6, d=7))
            )


    # Exceptions Encountered

  the test passes

* I add one more :ref:`assertion<AssertionError>` to see what happens when I call the function_ with no inputs

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 5-8

          self.assertEqual(
              src.functions.w_unknown_arguments(a=4, b=5, c=6, d=7),
              ((), dict(a=4, b=5, c=6, d=7))
          )
          self.assertEqual(
              src.functions.w_unknown_arguments(),
              ()
          )

  the terminal_ shows

  .. code-block:: shell

    AssertionError: Tuples differ: ((), {}) != ()

  I change the expectation to match

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 3

            self.assertEqual(
                src.functions.w_unknown_arguments(),
                ((), {})
            )


    # Exceptions Encountered


  the test passes

The function_ reads

* :ref:`positional arguments<test_functions_w_positional_arguments>` as tuples_ and
* :ref:`keyword arguments<test_functions_w_keyword_arguments>` as :ref:`dictionaries`.

This is why the :ref:`update method of dictionaries<test_update_a_dictionary>` can take a :ref:`dictionary<dictionaries>` as input

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

* :ref:`positional arguments<test_functions_w_positional_arguments>` must come before :ref:`keyword arguments<test_functions_w_keyword_arguments>`
* I can use ``**kwargs`` when I do not know how many :ref:`keyword arguments<test_functions_w_keyword_arguments>` the function_ has to take
* :ref:`keyword arguments<test_functions_w_keyword_arguments>` are represented as :ref:`dictionaries`
* I can use ``*args`` when I do not know how many :ref:`positional arguments<test_functions_w_positional_arguments>` the function_ has to take
* :ref:`positional arguments<test_functions_w_positional_arguments>` are represented as tuples_
* the :ref:`identity function<test_identity_function>` returns its input
* :ref:`constant functions<test_constant_function>` always return the same thing
* functions_ return :ref:`None` by default

:ref:`How many questions can you answer after going through this chapter?<questions about functions>`

----

:ref:`Click Here to see the code from this chapter<functions: tests and solutions>`

----

*********************************************************************************
what is next?
*********************************************************************************

you have covered a bit so far and know

* :ref:`how to make a test driven development environment`
* :ref:`how to raise AssertionError with assert methods<AssertionError>` and
* :ref:`how to write functions<functions>`

Would you like to :ref:`test how to pass values from tests to functions with assert methods?<how to pass values>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->