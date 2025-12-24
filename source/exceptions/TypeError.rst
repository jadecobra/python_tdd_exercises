.. meta::
  :description: Facing a Python TypeError? Learn to fix common errors like 'unsupported operand type' and 'int object is not callable'. Watch the full tutorial to debug now.
  :keywords: Jacob Itegboje, python typeerror unsupported operand type, python typeerror 'int' object is not callable, python typeerror can only concatenate str, how to fix typeerror in python, python typeerror string and integer, python typeerror list indices must be integers, python typeerror 'str' object is not callable, python typeerror float object is not iterable

.. include:: ../links.rst

.. _TypeError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError

#################################################################################
TypeError
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/DdEmPvYaCEQ?si=ih9z9nUVSJnY4D0N" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
what causes TypeError?
*********************************************************************************

TypeError_ is raised when an :ref:`object<classes>` is used in a way that it should not be. This helps understand how to use :ref:`functions` and :ref:`classes`

----

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: ../code/tests/test_type_error.py
  :language: python
  :linenos:

----

*********************************************************************************
start the project
*********************************************************************************

* I open a terminal_
* I type pwd_ to make sure I am in the ``pumping_python`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python

  .. NOTE:: if you are not in the ``pumping_python`` folder_, try ``cd ~/pumping_python``

* I choose ``type_error`` as the name of this project
* I open ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` in the :ref:`editor<2 editors>`

  .. TIP:: Here is a quick way to open ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` if you are using `Visual Studio Code`_

    .. code-block:: shell
      :emphasize-lines: 1

      code makePythonTdd.sh

    on `Windows`_ without `Windows Subsystem for Linux`_ use

    .. code-block:: shell
      :emphasize-lines: 1

      code makePythonTdd.ps1

* I change everywhere I have ``exceptions`` in ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` to the name of this project

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 2, 3, 5, 12, 20

    #!/bin/bash
    mkdir type_error
    cd type_error
    mkdir src
    touch src/type_error.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestTypeError(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError
    " > tests/test_type_error.py

* I run the program_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``makePythonTdd.ps1`` instead of ``makePythonTdd.sh``

    .. code-block:: shell
      :emphasize-lines: 1

      ./makePythonTdd.ps1

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell
    :emphasize-lines: 10
    :emphasize-text: tests/test_type_error.py:7

    ======================================= FAILURES =======================================
    _____________________________ TestTypeError.test_failure ______________________________

    self = <tests.test_exceptions.TestTypeError testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_type_error.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_type_error.py::TestMagic::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

* I hold :kbd:`ctrl` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_type_error.py:7`` to open it in the :ref:`editor<2 editors>`
* I add :ref:`AssertionError` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4-5

    # Exceptions seen
    # AssertionError

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
test_type_error_w_non_callables
*********************************************************************************

There are :ref:`objects<classes>` that can NOT be called

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add an `import statement`_ at the top of ``test_type_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.type_error
    import unittest

* I change ``test_failure`` to ``test_type_error_w_non_callables``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-4

    class TestTypeError(unittest.TestCase):

        def test_type_error_w_non_callables(self):
            src.type_error.none()

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'none'

  there is nothing in ``type_error.py`` in the ``src`` folder_ yet

* I add :ref:`AttributeError` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

    # Exceptions seen
    # AssertionError
    # AttributeError

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I open ``type_error.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>` of my `Integrated Development Environment (IDE)`_, then add the name and point it to :ref:`None`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    none = None

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  - the ``()`` to the right of ``src.type_error.none`` makes it a call
  - the name ``none`` points to :ref:`None` which is NOT callable_

  I cannot call :ref:`None` like a :ref:`function<functions>`

* I add TypeError_ to the list of :ref:`Exceptions<errors>` seen in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

    # Exceptions seen
    # AssertionError
    # AttributeError
    # TypeError

* I make ``none`` a :ref:`function<functions>` in ``type_error.py`` to make it callable_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def none():
        return None

  the test passes

I can call a :ref:`function<functions>` but I cannot call :ref:`None`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3

        def test_type_error_w_non_callables(self):
            src.type_error.none()
            src.type_error.false()

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'false'

  nothing is named ``false`` in ``type_error.py``

* I add the name to ``type_error.py`` and point it to :ref:`False<test_what_is_false>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def none():
        return None


    false = False

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: 'bool' object is not callable

  I cannot call a :ref:`boolean<booleans>` they way I can call a :ref:`function<functions>`

* I make the variable_ a :ref:`function<functions>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def none():
        return None

    def false():
        return False

  the terminal_ shows green again

* I add a line to test the other :ref:`boolean<Booleans>` in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

        def test_type_error_w_non_callables(self):
            src.type_error.none()
            src.type_error.false()
            src.type_error.true()

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'true'

  there is nothing named ``true`` in ``type_error.py``

* I add the name and point it to :ref:`True<test_what_is_true>` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5

    def false():
        return False


    true = True

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: 'bool' object is not callable

* I make it a :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def false():
        return False


    def true():
        return True

  the test passes. I can call a :ref:`function<functions>`, I cannot call a :ref:`boolean<booleans>`

* I add another line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_type_error_w_non_callables(self):
            src.type_error.none()
            src.type_error.false()
            src.type_error.true()
            src.type_error.a_list()

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'a_list'

* I add the name and point it to a :ref:`list<lists>` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5

    def true():
        return True


    a_list = [1, 2, 3, 'n']

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: 'list' object is not callable

* I make ``a_list`` a :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def true():
        return True


    def a_list():
        return [1, 2, 3, 'n']

  the test passes. I can call a :ref:`function<functions>`, I cannot call a :ref:`list<lists>`

* I add a new failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4

          src.type_error.false()
          src.type_error.true()
          src.type_error.a_list()
          src.type_error.a_dictionary()


    # Exceptions seen

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'a_dictionary'

* I add the name to and point it to a :ref:`dictionary<dictionaries>` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5

    def a_list():
        return [1, 2, 3, 'n']


    a_dictionary = {'key': 'value'}

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: 'dict' object is not callable

* I change it to a :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5-6

    def a_list():
        return [1, 2, 3, 'n']


    def a_dictionary():
        return {'key': 'value'}

  the terminal_ shows green again.

It is safe to say that I cannot call :ref:`data structures`, they are not callable_. I can call :ref:`functions`

----

*********************************************************************************
test_type_error_w_function_signatures
*********************************************************************************

When I call a :ref:`function<functions>` I have to match its definition also known as its signature

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add a new test to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3-4

            src.type_error.a_dictionary()

        def test_type_error_w_function_signatures(self):
            src.type_error.function_00('a')


    # Exceptions seen

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'function_00'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add the :ref:`function<functions>` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5-6

    def a_dictionary():
        return {'key': 'value'}


    def function_00():
        return None

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: function_00() takes 0 positional arguments but 1 was given

  because ``function_00`` is called with ``'a'`` as input and the definition does not allow any inputs

* I add a name in parentheses to the :ref:`function<functions>` definition

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 1

    def function_00(the_input):
        return None

  the test passes

I have to call a :ref:`function<functions>` in a way that matches its definition or I get :ref:`TypeError`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add a new failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 14

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00('a')
        src.type_error.function_01('a', 'b')

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'function_01'. Did you mean: 'function_00'?

* I add the :ref:`function<functions>` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-6

    def function_00(the_input):
        return None


    def function_01(the_input):
        return None

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: function_01() takes 1 positional argument but 2 were given

  the definition only allows one input, and the test sent two

* I add another name in parentheses so that the call to the :ref:`function<functions>` and its definition match

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 1

    def function_01(first, second):
      return None

  the test passes

* I add another failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

        def test_type_error_w_function_signatures(self):
            src.type_error.function_00('a')
            src.type_error.function_01('a', 'b')
            src.type_error.function_02('a', 'b', 'c')

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'function_02'. Did you mean: 'function_00'?

* I add the :ref:`function<functions>` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5-6

    def function_01(first, second):
        return None


    def function_02(first, second):
        return None

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: function_02() takes 2 positional arguments but 3 were given

* I change the name of the first input, then add another name in parentheses to make the number of inputs match in ``type_error.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 1

    def function_02(first, second, third):
        return None

  the test passes

* I add one more failing line in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 5

        def test_type_error_w_function_signatures(self):
            src.type_error.function_00('a')
            src.type_error.function_01('a', 'b')
            src.type_error.function_02('a', 'b', 'c')
            src.type_error.function_03('a', 'b', 'c', 'd')

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'function_03'. Did you mean: 'function_00'?

* I add the :ref:`function<functions>` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 5-6

    def function_02(first, second, third):
        return None


    def function_03(first, second, third):
        return None

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: function_03() takes 3 positional arguments but 4 were given

* I add a 4th name in parentheses to the definition

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 1

    def function_03(first, second, third, fourth):
        return None

  the test passes

I have to call a :ref:`function<functions>` with the same number of inputs its definition expects

----

*********************************************************************************
test_type_error_w_objects_that_do_not_mix
*********************************************************************************

Some operations do not work if the objects_ are not of the same type_

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test with a failing line in ``test_type_error.py``

.. code-block:: python
  :lineno-start: 18
  :emphasize-lines: 3-4

          src.type_error.function_03('a', 'b', 'c', 'd')

      def test_type_error_w_objects_that_do_not_mix(self):
          None + 1


  # Exceptions seen

the terminal_ shows TypeError_

.. code-block:: shell

  TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

I cannot do arithmetic_ with :ref:`None`

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the `assertRaises method`_

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 2-3

      def test_type_error_w_objects_that_do_not_mix(self):
          with self.assertRaises(TypeError):
              None + 1

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another failing line to the test

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 4

        def test_type_error_w_objects_that_do_not_mix(self):
            with self.assertRaises(TypeError):
                None + 1
            'text' + 0.1

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: can only concatenate str (not "float") to str

  I cannot add something that is not a string_ to a string_. I use assertRaises_ to handle the :ref:`Exception<errors>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 4-5

        def test_type_error_w_objects_that_do_not_mix(self):
            with self.assertRaises(TypeError):
                None + 1
            with self.assertRaises(TypeError):
                'text' + 0.1

  the test passes

* I add another failing line

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 6

        def test_type_error_w_objects_that_do_not_mix(self):
            with self.assertRaises(TypeError):
                None + 1
            with self.assertRaises(TypeError):
                'text' + 0.1
            (1, 2, 3, 'n') - {1, 2, 3, 'n'}

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for -: 'tuple' and 'set'

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 6-7

        def test_type_error_w_objects_that_do_not_mix(self):
            with self.assertRaises(TypeError):
                None + 1
            with self.assertRaises(TypeError):
                'text' + 0.1
            with self.assertRaises(TypeError):
                (1, 2, 3, 'n') - {1, 2, 3, 'n'}

    # Exceptions seen

  the terminal_ shows all tests are passing

----

*********************************************************************************
close the project
*********************************************************************************

* I close the file(s) I had open in the :ref:`editor(s)<2 editors>`
* I exit the tests in the terminal_ with :kbd:`ctrl+c` on the keyboard
* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/type_error

* I `change directory`_ to the parent of ``type_error``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
test_calculator_raises_type_error
*********************************************************************************

I want to use :ref:`TypeError` with :ref:`exception handlers<how to use try...except...else>` to make sure that the :ref:`calculator program<how to make a calculator>` only works with numbers, just like it would in the real world

=================================================================================
open the project
=================================================================================

* I `change directory`_ to the ``calculator`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd calculator

  the terminal_ shows I am in the ``calculator`` folder_

  .. code-block:: shell

    .../pumping_python/calculator

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

    (.venv) .../pumping_python/calculator

* I use ``pytest-watch`` to run the tests

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4

    rootdir: .../pumping_python/calculator
    collected 4 items

    tests/test_calculator.py ....                                        [100%]

    ============================ 4 passed in X.YZs =============================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new failing test to show that I can NOT do arithmetic_ operations with something that is not a number

.. code-block:: python
  :lineno-start: 42
  :emphasize-lines: 16-17

      def test_division(self):
          try:
              self.assertEqual(
                  src.calculator.divide(
                      self.random_first_number,
                      self.random_second_number
                  ),
                  self.random_first_number/self.random_second_number
              )
          except ZeroDivisionError:
              self.assertEqual(
                  src.calculator.divide(self.random_first_number, 0),
                  'undefined: I cannot divide by 0'
              )

      def test_calculator_raises_type_error(self):
          src.calculator.add(None, None)


  # Exceptions seen

the terminal_ shows TypeError_

.. code-block:: shell

  TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add assertRaises_

.. code-block:: python
  :lineno-start: 57
  :emphasize-lines: 2-3

      def test_calculator_raises_type_error(self):
          with self.assertRaises(TypeError):
              src.calculator.add(None, None)

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add a failing line for :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 4

        def test_calculator_raises_type_error(self):
            with self.assertRaises(TypeError):
                src.calculator.add(None None)
            src.calculator.divide(None, None)

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for /: 'NoneType' and 'NoneType'

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 3-4

            with self.assertRaises(TypeError):
                src.calculator.add(self.random_first_number, None)
            with self.assertRaises(TypeError):
                src.calculator.divide(self.random_first_number, None)

  the test passes

* I add another failing line, this time for :ref:`multiplication<test_multiplication>`

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.divide(None, None)
            src.calculator.multiply(None, None)

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 3-4

            with self.assertRaises(TypeError):
                src.calculator.divide(None, None)
            with self.assertRaises(TypeError):
                src.calculator.multiply(None, None)

  the test passes

* I add another one for :ref:`subtraction<test_subtraction>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.multiply(self.random_first_number, None)
            src.calculator.subtract(self.random_first_number, None)

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'

  I add the `assertRaises method`_

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3-4

            with self.assertRaises(TypeError):
                src.calculator.multiply(self.random_first_number, None)
            with self.assertRaises(TypeError):
                src.calculator.subtract(self.random_first_number, None)


    # Exceptions seen

  the test passes

The ``calculator`` raises :ref:`TypeError` when given :ref:`None` as input, what does it do when the input is a boolean_, string_, tuple_, :ref:`list<lists>`, set_ or :ref:`a dictionary<dictionaries>`?

*********************************************************************************
test_calculator_with_strings
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test with an :ref:`assertion<AssertionError>` from :ref:`test_what_is_an_assertion`  to :ref:`test_addition`

.. code-block:: python
  :lineno-start: 64
  :emphasize-lines: 4-5

          with self.assertRaises(TypeError):
              src.calculator.subtract(None, None)

      def test_calculator_with_strings(self):
          self.assertEqual(src.calculator.add('1', '1'), '2')


  # Exceptions seen

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: '11' != '2'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the expectation to match reality

.. code-block:: python
  :lineno-start: 68
  :emphasize-lines: 1

          self.assertEqual(src.calculator.add('1', '1'), '11')

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add an :ref:`assertion<AssertionError>` for the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 3

        def test_calculator_with_strings(self):
            self.assertEqual(src.calculator.add('1', '1'), '11')
            self.assertEqual(src.calculator.divide('1', '1'), '11')

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for /: 'str' and 'str'

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 3-4

        def test_calculator_with_strings(self):
            self.assertEqual(src.calculator.add('1', '1'), '11')
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')

  the test passes

* I try it with the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')
            src.calculator.multiply('1', '1')

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: can't multiply sequence by non-int of type 'str'

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 3-4

            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`subtract function<test_subtraction>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')
            src.calculator.subtract('1', '1')

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 3-4

            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.subtract('1', '1')

  the test passes

---------------------------------------------------------------------------------
how to test if something is an instance of an object in a program
---------------------------------------------------------------------------------

I want the :ref:`add function<test_addition>` to raise TypeError_ when it is given a string_ like the other :ref:`functions`. I can do this with the `isinstance function`_ it is like the `assertIsInstance method`_ from when I tested :ref:`None`

* I add an :ref:`if statement<if statements>` to the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2-5

    def add(first, second):
        if isinstance(first, str) or isinstance(second, str):
            raise TypeError(
                'I am a calculator, I only work with numbers'
            )
        else:
            return first + second

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: I am a calculator, I only work with numbers

  the `isinstance function`_ like the `assertIsInstance method`_ checks if the first input it is given is an instance of the :ref:`object<classes>` it is given as the second input. It is part of `Python's Built-in Functions`_

* I change the assertEqual_ in ``test_calculator_with_strings`` to assertRaises_ in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2-3

        def test_calculator_with_strings(self):
            with self.assertRaises(TypeError):
                src.calculator.add('1', '1')

  the test passes

* I change the name of the test to be clearer

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 1

        def test_calculator_raises_type_error_when_given_strings(self):
            with self.assertRaises(TypeError):
                src.calculator.add('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.subtract('1', '1')


    # Exceptions seen

----

*********************************************************************************
test_calculator_sends_message_when_input_is_not_a_number
*********************************************************************************

I want the :ref:`calculator functions<how to make a calculator>` to send a message when the input is not a number, instead of just raising TypeError_ which causes the program to stop, I want the user to be able to try again with different input

=================================================================================
:red:`RED`: make it fail
=================================================================================

I change the assertRaises_ to assertEqual_ in ``test_calculator_raises_type_error`` in ``test_calculator.py``

.. code-block:: python
  :lineno-start: 57
  :emphasize-lines:

  def test_calculator_raises_type_error(self):
      self.assertEqual(
          src.calculator.add(None, None),
          'I am a calculator, I only work with numbers'
      )
      with self.assertRaises(TypeError):
          src.calculator.divide(None, None)
      with self.assertRaises(TypeError):
          src.calculator.multiply(None, None)
      with self.assertRaises(TypeError):
          src.calculator.subtract(None, None)

the terminal_ shows TypeError_

.. code-block:: shell

  TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add an :ref:`exception handler<how to use try...except...else>` to the :ref:`add function<test_addition>` in ``calculator.py``

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 7-10

  def add(first, second):
      if isinstance(first, str) or isinstance(second, str):
          raise TypeError(
              'I am a calculator, I only work with numbers'
          )
      else:
          try:
              return first + second
          except TypeError:
              return 'I am a calculator, I only work with numbers'

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I want the same thing to happen with the :ref:`divide function<test_division>`. I change assertRaises_ to assertEqual_ in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 6-9

        def test_calculator_raises_type_error(self):
            self.assertEqual(
                src.calculator.add(None, None),
                'I am a calculator, I only work with numbers'
            )
            self.assertEqual(
                src.calculator.divide(None, None),
                'I am a calculator, I only work with numbers'
            )

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for /: 'NoneType' and 'NoneType'

  I add an :ref:`except clause<how to use try...except...else>` to the :ref:`exception handler<how to use try...except...else>` in the :ref:`divide function<test_division>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 6-7

    def divide(first, second):
        try:
            return first / second
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'
        except TypeError:
            return 'I am a calculator, I only work with numbers'

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

  ``test_calculator_raises_type_error_when_given_strings`` fails because the :ref:`divide function<test_division>` now returns a message when TypeError_ is raised. I add the :ref:`if statement<if statements>` from the :ref:`add function<test_addition>` to the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2-12

    def divide(first, second):
        if isinstance(first, str) or isinstance(second, str):
            raise TypeError(
                'I am a calculator, I only work with numbers'
            )
        else:
            try:
                return first / second
            except ZeroDivisionError:
                return 'undefined: I cannot divide by 0'
            except TypeError:
                return 'I am a calculator, I only work with numbers'

  the test passes. I have some repetition to remove

* Both the :ref:`add<test_addition>` and :ref:`divide<test_division>` :ref:`functions` have the same error message twice

  .. code-block:: python

    'I am a calculator, I only work with numbers'

* I add a :ref:`variable<what_is_a_variable>` for the error message to the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 2, 4, 9

    def add(first, second):
        error_message = 'I am a calculator, I only work with numbers'
        if isinstance(first, str) or isinstance(second, str):
            raise TypeError(error_message)
        else:
            try:
                return first + second
            except TypeError:
                return error_message

  the test is still green

* I do the same thing with the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2, 4, 11

    def divide(first, second):
        error_message = 'I am a calculator, I only work with numbers'
        if isinstance(first, str) or isinstance(second, str):
            raise TypeError(error_message)
        else:
            try:
                return first / second
            except ZeroDivisionError:
                return 'undefined: I cannot divide by 0'
            except TypeError:
                return error_message

  the terminal_ shows all tests are still passing

* I do the same thing in ``test_calculator_raises_type_error`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 2, 5, 9

        def test_calculator_raises_type_error(self):
            error_message = 'I am a calculator, I only work with numbers'
            self.assertEqual(
                src.calculator.add(None, None),
                error_message
            )
            self.assertEqual(
                src.calculator.divide(None, None),
                error_message
            )
            with self.assertRaises(TypeError):
                src.calculator.multiply(None, None)
            with self.assertRaises(TypeError):
                src.calculator.subtract(None, None)

  still green

* The :ref:`add<test_addition>` and :ref:`divide<test_division>` :ref:`functions` have the same :ref:`if statement<if statements

  .. code-block:: python

    if isinstance(first, str) or isinstance(second, str):
        raise TypeError(
            'I am a calculator, I only work with numbers'
        )
    else:
        ...

---------------------------------------------------------------------------------
how to make a wrapper function
---------------------------------------------------------------------------------

I want a way to check if the input is a string for both :ref:`functions`. I can do this with a wrapper, which is a :ref:`function<functions>` that takes other :ref:`functions` as input.

* I add a :ref:`function<functions>` to ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-9

    def reject_strings(function):
        def wrapper(first, second):
            if isinstance(first, str) or isinstance(second, str):
                raise TypeError(
                    'I am a calculator, I only work with numbers'
                )
            else:
                return function(first, second)
        return wrapper


    def subtract(first, second):

* I use the new :ref:`function<functions>` to wrap the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 1


    @reject_strings
    def add(first, second):
        error_message = 'I am a calculator, I only work with numbers'
        if isinstance(first, str) or isinstance(second, str):
            raise TypeError(error_message)
        else:
            try:
                return first + second
            except TypeError:
                return error_message

  the test is still green.

  The ``reject_strings`` :ref:`function<functions>` takes a :ref:`function<functions>` as input

  - if any of the two inputs are strings_ it returns an error message
  - if none of the two inputs are strings_ it returns the result of the :ref:`function<functions>` working on the two inputs

* I remove the :ref:`if statement<if statements>` from the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 3-6

    @reject_strings
    def add(first, second):
        try:
            return first + second
        except TypeError:
            return 'I am a calculator, I only work with numbers'

  still green

* I use ``reject_strings`` with the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 1

    @reject_strings
    def divide(first, second):
        error_message = 'I am a calculator, I only work with numbers'
        if isinstance(first, str) or isinstance(second, str):
            raise TypeError(error_message)
        else:
            try:
                return first / second
            except ZeroDivisionError:
                return 'undefined: I cannot divide by 0'
            except TypeError:
                return error_message

  the test is still green

* I remove the :ref:`if statement<if statements>` from the :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 2-7

    @reject_strings
    def divide(first, second):
        try:
            return first / second
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'
        except TypeError:
            return 'I am a calculator, I only work with numbers'

  all tests are still passing

* both the :ref:`add<test_addition>` and :ref:`divide<test_division>` :ref:`function<functions>` have :ref:`exception handlers<how to use try...except...else>` that look the same

  .. code-block:: python
    :emphasize-lines: 1, 5-6, 8, 10-11

    try:
        return first / second
    except ZeroDivisionError:
        return 'undefined: I cannot divide by 0'
    except TypeError:
        return 'I am a calculator, I only work with numbers'

    try:
        return first + second
    except TypeError:
        return 'I am a calculator, I only work with numbers'

  the difference is in how they handle the inputs

  .. code-block:: python

        return first / second
        return first + second

  I add the :ref:`exception handlers<how to use try...except...else>` for TypeError_ to the ``reject_strings`` :ref:`function<functions>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3, 7-10

    def reject_strings(function):
        def wrapper(first, second):
            error_message = 'I am a calculator, I only work with numbers'
            if isinstance(first, str) or isinstance(second, str):
                raise TypeError(error_message)
            else:
                try:
                    return function(first, second)
                except TypeError:
                    return error_message
        return wrapper

  the tests are still green

* I remove the :ref:`except clause<how to use try...except...else>` from the :ref:`exception handler<how to use try...except...else>` in the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 22

    @reject_strings
    def divide(first, second):
        try:
            return first / second
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'

  the tests are still passing

* I do the same thing with the :ref:`add function<test_functions>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

    @reject_strings
    def add(first, second):
        return first + second

  still green

* I change the name of the :ref:`function<functions>` from ``reject_strings`` to ``take_numbers_only``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def take_numbers_only(function):
        def wrapper(first, second):

  and when wrapping the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 1

    @take_numbers_only
    def divide(first, second):

  I do the same thing with the :ref:`add function<test_division>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 1

    @take_numbers_only
    def add(first, second):

  .. TIP:: In `Visual Studio Code`_ I can change all the places that a name is in the file_, by using

    * Find and Replace - ``ctrl+H`` on Windows_ or ``option+command+F`` on MacOS_ or with
    * Rename Symbol

      - Right click on the name you want to change, for example ``the_input`` then select ``Rename Symbol`` or
      - Select the name you want to change then hit ``F2`` to rename it

  all tests are still passing.

* I use the ``takes_numbers_only`` :ref:`function<functions>` to wrap the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 1

    @take_numbers_only
    def multiply(first, second):
        return first * second

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

  the :ref:`multiply function<test_multiplication>` now returns a message and does not stop the program when it receives bad input. I change the assertRaises_ to assertEqual_ in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 5-8

                self.assertEqual(
                    src.calculator.divide(None, None),
                    error_message
                )
                self.assertEqual(
                    src.calculator.multiply(None, None),
                    error_message
                )

  the test is green again

* I do the same thing with the :ref:`subtract function<functions>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 1

    @take_numbers_only
    def subtract(first, second):
        return first - second

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: TypeError not raised

  I use assertEqual_ to change the expectation in ``test_calculator_raises_type_error`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 5-8


            self.assertEqual(
                src.calculator.multiply(None, None),
                error_message
            )
            self.assertEqual(
                src.calculator.subtract(None, None),
                error_message
            )

        def test_calculator_raises_type_error_when_given_strings(self):

  the test passes

* I change the name of the test to be clearer

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 1

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            error_message = 'I am a calculator, I only work with numbers'
            self.assertEqual(
                src.calculator.add(None, None),
                error_message
            )
            self.assertEqual(
                src.calculator.divide(None, None),
                error_message
            )
            self.assertEqual(
                src.calculator.multiply(None, None),
                error_message
            )
            self.assertEqual(
                src.calculator.subtract(None, None),
                error_message
            )

* The :ref:`calculator<how to make a calculator>` still raises TypeError_ for strings_, I want it to send a message like it does for :ref:`None`. I move the :ref:`assertion<what is an assertion?>` for the :ref:`add function<test_addition>` from ``test_calculator_raises_type_error_when_given_strings`` to ``test_calculator_sends_message_when_input_is_not_a_number``

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 5-6

            self.assertEqual(
                src.calculator.subtract(None, None),
                error_message
            )
            with self.assertRaises(TypeError):
                src.calculator.add('1', '1')

        def test_calculator_raises_type_error_when_given_strings(self):
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')

* I change the assertRaises_ to assertEqual_ with the expectation of a message

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 5, 7-8

            self.assertEqual(
                src.calculator.subtract(None, None),
                error_message
            )
            self.assertEqual(
                src.calculator.add('1', '1'),
                error_message
            )

        def test_calculator_raises_type_error_when_given_strings(self):
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: I am a calculator, I only work with numbers

* I change the `raise statement`_ in the `if statement<if statements>` of ``take_numbers_only`` in ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def take_numbers_only(function):
        def wrapper(first, second):
            error_message = 'I am a calculator, I only work with numbers'
            if isinstance(first, str) or isinstance(second, str):
                return error_message
            else:
                try:
                    return function(first, second)
                except TypeError:
                    return error_message
        return wrapper

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: TypeError not raised

  I have to make the same change for the other :ref:`assertions<what is an assertion?>` in ``test_calculator_raises_type_error_when_given_strings`` in ``test_calculator.py``

* I move the :ref:`assertion<what is an assertion?>` for the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 5-6

            self.assertEqual(
                src.calculator.add('1', '1'),
                error_message
            )
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')

        def test_calculator_raises_type_error_when_given_strings(self):
            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')

  then I change assertRaises_ to assertEqual_ with the error message

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 5, 7-8

            self.assertEqual(
                src.calculator.add('1', '1'),
                error_message
            )
            self.assertEqual(
                src.calculator.divide('1', '1'),
                error_message
            )

        def test_calculator_raises_type_error_when_given_strings(self):
            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

  for the next :ref:`assertion<what is an assertion?>`

* I move the :ref:`assertion<what is an assertion?>` to ``test_calculator_sends_message_when_input_is_not_a_number``

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 5-6

            self.assertEqual(
                src.calculator.divide('1', '1'),
                error_message
            )
            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')

        def test_calculator_raises_type_error_when_given_strings(self):
            with self.assertRaises(TypeError):
                src.calculator.subtract('1', '1')

  I change assertRaises_ to assertEqual_

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 5, 7-8

            self.assertEqual(
                src.calculator.divide('1', '1'),
                error_message
            )
            self.assertEqual(
                src.calculator.multiply('1', '1'),
                error_message
            )

        def test_calculator_raises_type_error_when_given_strings(self):
            with self.assertRaises(TypeError):
                src.calculator.subtract('1', '1')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

  one more :ref:`assertion<what is an assertion?>` to go

* I remove ``test_calculator_raises_type_error_when_given_strings``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 5-6

            self.assertEqual(
                src.calculator.multiply('1', '1'),
                error_message
            )
            with self.assertRaises(TypeError):
                src.calculator.subtract('1', '1')


    # Exceptions seen

  I change assertRaises_ to assertEqual_ with the expectation of the error message

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 5, 7-8

            self.assertEqual(
                src.calculator.multiply('1', '1'),
                error_message
            )
            self.assertEqual(
                src.calculator.subtract('1', '1'),
                error_message
            )


    # Exceptions seen

  the terminal_ shows green again

----

=================================================================================
close the project
=================================================================================

* I close the file(s) I had open in the :ref:`editor(s)<2 editors>`
* I exit the tests in the terminal_ with :kbd:`ctrl+c` on the keyboard
* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/calculator

* I `change directory`_ to the parent of ``calculator``

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

The :ref:`calculator program<how to make a calculator>` can take 2 inputs and :ref:`check if the inputs are numbers<test_calculator_sends_message_when_input_is_not_a_number>` then do
* :ref:`addition<test_addition>`
* :ref:`subtraction<test_subtraction>`
* :ref:`multiplication<test_multiplication>` and
* :ref:`division<test_division>`

Even though the program_ says it only works with numbers, I did not add tests for tuples_, :ref:`lists`, sets_, and :ref:`dictionaries`, though they are touched in :ref:`test_type_error_w_objects_that_do_not_mix` Do you want to add them?

I ran tests for TypeError_ with
* :ref:`objects that are not  callable<test_type_error_w_non_callables>`
* :ref:`function definitions<test_type_error_w_function_signatures>`
* :ref:`objects that do not mix<test_type_error_w_objects_that_do_not_mix>` and
* :ref:`used TypeError, an if statement, exception handler and wrapper function to make sure the calculator program only works with numbers<test_calculator_sends_message_when_input_is_not_a_number>`

Would you like to :ref:`test Lists?<lists>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<TypeError: tests and solution>`

----

*********************************************************************************
what is next?
*********************************************************************************

you know

* :ref:`how to make a test driven development environment`
* :ref:`how to raise AssertionError with assert methods<AssertionError>`
* :ref:`how to write functions<functions>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<None>`
* :ref:`what is True and False in Python<booleans>`
* :ref:`how to write programs that make decisions<booleans: truth table>`
* :ref:`how to make a calculator`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`how to make the calculator check if its inputs are numbers<test_calculator_sends_message_when_input_is_not_a_number>`

:ref:`Would you like to test Lists?<lists>`

-----

*********************************************************************************
please leave a review
*********************************************************************************

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 5 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->