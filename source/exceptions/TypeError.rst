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

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``type_error`` as the name of the project

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh type_error

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: shell

      ./makePythonTdd.ps1 type_error

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_type_error.py:7: AssertionError

* I hold :kbd:`ctrl` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_type_error.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format to follow Python_ :ref:`convention<conventions>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestTypeError(unittest.TestCase):

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
    :emphasize-lines: 2

    import unittest
    import src.type_error

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

* I add it to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

    # Exceptions seen
    # AssertionError
    # AttributeError

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I open ``type_error.py`` from the ``src`` folder_ to open it in the :ref:`editor<2 editors>` of my `Integrated Development Environment (IDE)`_, then add the name and point it to :ref:`None`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    none = None

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  the ``()`` to the right of ``src.type_error.none`` makes it a call, and the name ``none`` points to :ref:`None` which is NOT callable_

* I add the error to the list of :ref:`Exceptions<errors>` seen in ``test_type_error.py``

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

  the test passes. I can call a :ref:`function<functions>` but I cannot call a :ref:`boolean<booleans>`

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

* I make `a_list` a :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def true():
        return True


    def a_list():
        return [1, 2, 3, 'n']

  the test passes. I can call a :ref:`function<functions>` but I cannot call a :ref:`list<lists>`

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

It is safe to say that I cannot call :ref:`data structures` but I can call :ref:`functions`

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

  because ``function_00`` is called with ``'a'`` as input but the definition does not accept any inputs

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

* I add another name in parentheses so that the call to the :ref:`function<functions>` and its definition match

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 1

    def function_01(first_input, second_input):
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

    def function_01(first_input, second_input):
        return None


    def function_02(first_input, second_input):
        return None

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: function_02() takes 2 positional arguments but 3 were given

* I add another name in parentheses to make the number of inputs match in ``type_error.p``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 1

    def function_02(first_input, second_input, input_3):
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

    def function_02(first_input, second_input, input_3):
        return None


    def function_03(first_input, second_input, input_3):
        return None

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: function_03() takes 3 positional arguments but 4 were given

* I add a 4th name in parentheses to the definition

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 1

    def function_03(first_input, second_input, input_3, input_4):
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

    def add(first_input, second_input):
        if isinstance(first_input, str) or isinstance(second_input, str):
            raise TypeError(
                'I am a calculator, I only work with numbers'
            )
        else:
            return first_input + second_input

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
how to use TypeError to check input
*********************************************************************************

I want the :ref:`calculator functions<how to make a calculator>` to send a message when input is bad, instead of just raising TypeError_ which causes the program to stop, I want the user to be able to try again with different input

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

  def add(first_input, second_input):
      if isinstance(first_input, str) or isinstance(second_input, str):
          raise TypeError(
              'I am a calculator, I only work with numbers'
          )
      else:
          try:
              return first_input + second_input
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

    def divide(first_input, second_input):
        try:
            return first_input / second_input
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

    def divide(first_input, second_input):
        if isinstance(first_input, str) or isinstance(second_input, str):
            raise TypeError(
                'I am a calculator, I only work with numbers'
            )
        else:
            try:
                return first_input / second_input
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

    def add(first_input, second_input):
        error_message = 'I am a calculator, I only work with numbers'
        if isinstance(first_input, str) or isinstance(second_input, str):
            raise TypeError(error_message)
        else:
            try:
                return first_input + second_input
            except TypeError:
                return error_message

  the test is still green

* I do the same thing with the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2, 4, 11

    def divide(first_input, second_input):
        error_message = 'I am a calculator, I only work with numbers'
        if isinstance(first_input, str) or isinstance(second_input, str):
            raise TypeError(error_message)
        else:
            try:
                return first_input / second_input
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

    if isinstance(first_input, str) or isinstance(second_input, str):
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
        def wrapper(first_input, second_input):
            if isinstance(first_input, str) or isinstance(second_input, str):
                raise TypeError(
                    'I am a calculator, I only work with numbers'
                )
            else:
                return function(first_input, second_input)
        return wrapper


    def subtract(first_input, second_input):

* I use the new :ref:`function<functions>` to wrap the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 1


    @reject_strings
    def add(first_input, second_input):
        error_message = 'I am a calculator, I only work with numbers'
        if isinstance(first_input, str) or isinstance(second_input, str):
            raise TypeError(error_message)
        else:
            try:
                return first_input + second_input
            except TypeError:
                return error_message

  the test is still green.

  The ``reject_strings`` :ref:`function<functions>` takes a :ref:`function<functions>` as input

  - if any of the two inputs are strings_ it returns an error message
  - if none of the two inputs are strings_ it returns the result of the :ref:`function<functions>` working on the two inputs

* I remove the :ref:`if statement<if statements (conditions)>` from the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 3-6

    @reject_strings
    def add(first_input, second_input):
        try:
            return first_input + second_input
        except TypeError:
            return 'I am a calculator, I only work with numbers'

  still green

* I use ``reject_strings`` with the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 1

    @reject_strings
    def divide(first_input, second_input):
        error_message = 'I am a calculator, I only work with numbers'
        if isinstance(first_input, str) or isinstance(second_input, str):
            raise TypeError(error_message)
        else:
            try:
                return first_input / second_input
            except ZeroDivisionError:
                return 'undefined: I cannot divide by 0'
            except TypeError:
                return error_message

  the test is still green

* I remove the :ref:`if statement<if statements (conditions)>` from the :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 2-7

    @reject_strings
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'
        except TypeError:
            return 'I am a calculator, I only work with numbers'

  all tests are still passing

* both the :ref:`add<test_addition>` and :ref:`divide<test_division>` :ref:`function<functions>` have :ref:`exception handlers<how to use try...except...else>` that look the same

  .. code-block:: python
    :emphasize-lines: 1, 5-6, 8, 10-11

    try:
        return first_input / second_input
    except ZeroDivisionError:
        return 'undefined: I cannot divide by 0'
    except TypeError:
        return 'I am a calculator, I only work with numbers'

    try:
        return first_input + second_input
    except TypeError:
        return 'I am a calculator, I only work with numbers'

  the difference is in how they handle the inputs

  .. code-block:: python

    return first_input / second_input
    return first_input + second_input

  I add the :ref:`exception handlers<how to use try...except...else>` for TypeError_ to the ``reject_strings`` :ref:`function<functions>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3, 7-10

    def reject_strings(function):
        def wrapper(first_input, second_input):
            error_message = 'I am a calculator, I only work with numbers'
            if isinstance(first_input, str) or isinstance(second_input, str):
                raise TypeError(error_message)
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return error_message
        return wrapper

  the tests are still green

* I remove the :ref:`except clause<how to use try...except...else>` from the :ref:`exception handler<how to use try...except...else>` in the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 22

    @reject_strings
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'

  the tests are still passing

* I do the same thing with the :ref:`add function<test_functions>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

    @reject_strings
    def add(first_input, second_input):
        return first_input + second_input

  still green

* I change the name of the :ref:`function<functions>` from ``reject_strings`` to ``take_numbers_only``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def take_numbers_only(function):
        def wrapper(first_input, second_input):

  and when wrapping the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 1

    @take_numbers_only
    def divide(first_input, second_input):

  I do the same thing with the :ref:`add function<test_division>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 1

    @take_numbers_only
    def add(first_input, second_input):

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
    def multiply(first_input, second_input):
        return first_input * second_input

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
    def subtract(first_input, second_input):
        return first_input - second_input

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

    def test_calculator_sends_message_when_inputs_are_not_numbers(self):
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

* The :ref:`calculator<how to make a calculator>` still raises TypeError_ for strings_, I want it to send a message like it does for :ref:`None`. I change assertRaises_ to assertEqual_ for the first :ref:`assertion<what is an assertion?>` in ``test_calculator_raises_type_error_when_given_strings``

  .. code-block:: python



* I change the `raise statement`_ in the `if statement<if statements>` of ``take_numbers_only``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def take_numbers_only(function):
        def wrapper(first_input, second_input):
            error_message = 'I am a calculator, I only work with numbers'
            if isinstance(first_input, str) or isinstance(second_input, str):
                return error_message
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return error_message
        return wrapper

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: TypeError not raised




There is a problem, the test uses random numbers, which means at some point ``random_second_number`` will have a value of ``0`` and the first part of ``test_division`` will raise :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`


* I add a `return statement`_ to the ``a_random_number`` :ref:`function` in ``test_calculator.py`` to make it happen

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return 0
        return random.triangular(-1000.0, 1000.0)

  the terminal_ shows :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

  .. code-block:: shell
    :emphasize-lines: 1

    >           self.random_first_number/self.random_second_number
            )
    E       ZeroDivisionError: division by zero

  the expectation calculation in ``test_division`` divides by ``0`` when ``random_second_number`` is ``0`` but the result should be ``'undefined: I cannot divide by 0'``

* I add an :ref:`exception handler<how to use try...except...else>` to the test

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2-14

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

  the test passes

* I remove the `return statement`_ from ``a_random_number`` to go back to testing with a range of numbers

  .. code-block:: python
    :linenos:

    import random
    import src.calculator
    import unittest


    def a_random_number():
        return random.triangular(-1000.0, 1000.0)


    class TestCalculator(unittest.TestCase):

  the test is still green










I add an :ref:`exception handler<how to use try...except...else>` to the :ref:`add function<test_addition>` in ``calculator.py``

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 2-

  def add(input_1, input_2):
      try:
          return input_1 + input_2
      except TypeError:
          return 'I only work with numbers'

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: TypeError not raised

because the ``add`` :ref:`function<functions>` now sends a message when :ref:`TypeError` is raised

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the assertRaises_ to assertEqual_ in ``test_calculator.py``

.. code-block:: python
  :lineno-start: 44
  :emphasize-lines: 2-5

  def test_calculator_raises_type_error(self):
      self.assertEqual(
          src.calculator.add(self.random_first_number, None),
          'I only work with numbers'
      )
      with self.assertRaises(TypeError):
          src.calculator.divide(self.random_first_number, None)
      with self.assertRaises(TypeError):
          src.calculator.multiply(self.random_first_number, None)
      with self.assertRaises(TypeError):
          src.calculator.subtract(self.random_first_number, None)

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add an :ref:`exception handler<how to use try...except...else>` to the :ref:`divide function<test_division>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2-6

    def divide(input_1, input_2):
        try:
            return input_1 / input_2
        except TypeError:
            return 'I only work with numbers'


    def add(input_1, input_2):

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

  because the ``add`` :ref:`function<functions>` now sends a message when :ref:`TypeError` is raised

* I change assertRaises_ to assertEqual_ in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 6-9

        def test_calculator_raises_type_error(self):
            self.assertEqual(
                src.calculator.add(self.random_first_number, None),
                'I only work with numbers'
            )
            self.assertEqual(
                src.calculator.divide(self.random_first_number, None),
                'I only work with numbers'
            )
            with self.assertRaises(TypeError):
                src.calculator.multiply(self.random_first_number, None)
            with self.assertRaises(TypeError):
                src.calculator.subtract(self.random_first_number, None)

* I have the same :ref:`exception handler<how to use try...except...else>` in both :ref:`functions` in ``calculator.py``. To follow `The Do Not Repeat Yourself (DRY) Principle`_ I can write a :ref:`function<functions>` that handles TypeError_. The problem is how it takes care of the lines that change, that is

  - ``result = input_1 + input_2``
  - ``result = input_1 / input_2``

  I add a new :ref:`function<functions>` to ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    def handle_type_error(function):
        def wrapper(input_1, input_2):
            try:
                return function(input_1, input_2)
            except TypeError:
                return 'I only work with numbers'
        return wrapper


    def subtract(input_1, input_2):

  this new :ref:`function<functions>` (``handle_type_error``) takes a :ref:`function<functions>` as input. It has a :ref:`function<functions>` inside it named ``wrapper``, which runs the input :ref:`function<functions>` and handles :ref:`TypeError` when raised

* I use the new :ref:`function<functions>` as a wrapper for the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 8-10

    def divide(input_1, input_2):
        try:
            return input_1 / input_2
        except TypeError:
            return 'I only work with numbers'


    @handle_type_error
    def add(input_1, input_2):
        return input_1 + input_2

  the test is still green

* I wrap the :ref:`divide function<test_division>` as well

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 1-3

    @handle_type_error
    def divide(input_1, input_2):
        return input_1 / input_2


    @handle_type_error
    def add(input_1, input_2):
        return input_1 + input_2

  the test is still green

* I use the wrapper with the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 1-3

    @handle_type_error
    def multiply(input_1, input_2):
        return input_1 * input_2

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

  I change the assertRaises_ to assertEqual_ in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 10-13

        def test_calculator_raises_type_error(self):
            self.assertEqual(
                src.calculator.add(self.random_first_number, None),
                'I only work with numbers'
            )
            self.assertEqual(
                src.calculator.divide(self.random_first_number, None),
                'I only work with numbers'
            )
            self.assertEqual(
                src.calculator.multiply(self.random_first_number, None),
                'I only work with numbers'
            )
            with self.assertRaises(TypeError):
                src.calculator.subtract(self.random_first_number, None)

  the test passes

* I add the wrapper to the :ref:`subtract function<test_subtraction>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1

    @handle_type_error
    def subtract(input_1, input_2):
        return input_1 - input_2


    @handle_type_error
    def multiply(input_1, input_2):
        return input_1 * input_2

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

  I change assertRaises_ to assertEqual_ in ``calculator.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 14-17

        def test_calculator_raises_type_error(self):
            self.assertEqual(
                src.calculator.add(self.random_first_number, None),
                'I only work with numbers'
            )
            self.assertEqual(
                src.calculator.divide(self.random_first_number, None),
                'I only work with numbers'
            )
            self.assertEqual(
                src.calculator.multiply(self.random_first_number, None),
                'I only work with numbers'
            )
            self.assertEqual(
                src.calculator.subtract(self.random_first_number, None),
                'I only work with numbers'
            )


    # Exceptions seen

  the test passes

* I change the name of the test to be clearer

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 1

        def test_calculator_sends_a_message_when_inputs_are_not_numbers(self):
            self.assertEqual(

  The ``calculator`` now uses :ref:`TypeError` to send a message when bad inputs are passed, but there is a case I have not considered

* Python_ allows using the ``+`` operator with strings_ but it does not work for the other arithmetic_ operations. I add a test to show this with the :ref:`addition function<test_addition>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 6-10

            self.assertEqual(
                src.calculator.subtract(self.random_first_number, None),
                'I only work with numbers'
            )

        def test_calculator_with_strings(self):
            self.assertEqual(
                src.calculator.add('hello ', 'world'),
                None
            )


    # Exceptions seen

  the terminal_ shows

  .. code-block:: shell

    AssertionError: 'hello world' != None

  I change the expectation to match

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 4

        def test_calculator_with_strings(self):
            self.assertEqual(
                src.calculator.add('hello ', 'world'),
                'hello world'
            )

  the test passes

* I add another :ref:`assertion<AssertionError>` for :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 6-9

        def test_calculator_with_strings(self):
            self.assertEqual(
                src.calculator.add('hello ', 'world'),
                'hello world'
            )
            self.assertEqual(
                src.calculator.divide('hello ', 'world'),
                'hello world'
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'I only work with numbers' != 'hello world'

  the :ref:`divide function<test_division>` raised TypeError_ which was handled by ``handle_type_error`` so I get a message back

* I change the expectation in ``test_calculator.py``

  .. code-block:: python
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.divide('hello ', 'world'),
                'I only work with numbers'
            )

  the test passes

* I want the :ref:`add function<test_addition>` to show the same message when it gets a string_. I add a :ref:`condition<if statements>` to ``handle_type_error`` in ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def handle_type_error(function):
        def wrapper(input_1, input_2):
            if isinstance(input_1, str) or isinstance(input_2, str):
                return 'I only work with numbers'
            try:
                return function(input_1, input_2)
            except TypeError:
                return 'I only work with numbers'
        return wrapper

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'I only work with numbers' != 'hello world'

  that's more like it. The condition I added uses the isinstance_ :ref:`function<functions>` to check if ``input_1`` and ``input_2`` are strings_

* I change the expectation in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 4

        def test_calculator_with_strings(self):
            self.assertEqual(
                src.calculator.add('hello ', 'world'),
                'I only work with numbers'
            )
            self.assertEqual(
                src.calculator.divide('hello ', 'world'),
                'I only work with numbers'
            )

  the test passes

* The message in ``handle_type_error`` is a duplication which means if I would have to change it in two places if needed. I use a variable_ instead so that any changes would only need to happen in one place

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3, 5, 9

    def handle_type_error(function):
        def wrapper(input_1, input_2):
            error_message = 'I only work with numbers'
            if isinstance(input_1, str) or isinstance(input_2, str):
                return error_message
            try:
                return function(input_1, input_2)
            except TypeError:
                return error_message
        return wrapper

  the test is still green

* I change the name from ``handle_type_error`` to be clearer in ``calculator.py``

  .. TIP:: you can use the ``Rename Symbol`` function of the `Integrated Development Environment (IDE)`_ to change everywhere ``handle_type_error`` is at once

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 13, 18, 23, 28

    def check_input(function):
        def wrapper(input_1, input_2):
            error_message = 'I only work with numbers'
            if isinstance(input_1, str) or isinstance(input_2, str):
                return error_message
            try:
                return function(input_1, input_2)
            except TypeError:
                return error_message
        return wrapper


    @check_input
    def subtract(input_1, input_2):
        return input_1 - input_2


    @check_input
    def multiply(input_1, input_2):
        return input_1 * input_2


    @check_input
    def divide(input_1, input_2):
        return input_1 / input_2


    @check_input
    def add(input_1, input_2):
        return input_1 + input_2

  the terminal still shows green

* I add another :ref:`assertion<AssertionError>` for :ref:`multiplication<test_multiplication>` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.divide('hello ', 'world'),
                'I only work with numbers'
            )
            self.assertEqual(
                src.calculator.multiply('hello', 'world'),
                None
            )

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'I only work with numbers' != None

  I change the expectation to match

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.multiply('hello', 'world'),
                'I only work with numbers'
            )

  the test passes

* I add another one for :ref:`subtraction<test_subtraction>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply('hello', 'world'),
                'I only work with numbers'
            )
            self.assertEqual(
                src.calculator.subtract('hello', 'world'),
                None
            )

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'I only work with numbers' != None

  I make the expectation match

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.subtract('hello', 'world'),
                'I only work with numbers'
            )


    # Exceptions seen

  the test passes




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

The :ref:`calculator program<how to make a calculator>` can take 2 inputs and :ref:`check if the inputs are good<how to check if input is good>` then do
* :ref:`addition<test_addition>`
* :ref:`subtraction<test_subtraction>`
* :ref:`multiplication<test_multiplication>` and
* :ref:`division<test_division>`

Even though the program_ claims to only work with numbers, I did not add a test for floats_, do you want to add those tests?

I ran tests for TypeError_ with
* objects_ that are not callable_
* :ref:`function<functions>` definitions and
* objects_ that do not mix
* and the :ref:`calculator program<how to make a calculator>` to use TypeError_ to make sure it gets the right inputs

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