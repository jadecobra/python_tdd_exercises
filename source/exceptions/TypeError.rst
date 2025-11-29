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

TypeError_ is raised when an :ref:`object<classes>` is used in a way that it should not be. This will help you understand how to use :ref:`functions` and :ref:`classes`

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``type_error`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh type_error

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: python

      ./makePythonTdd.ps1 type_error

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_type_error.py:7: AssertionError

* I hold ``ctrl`` (Windows/Linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_type_error.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change ``True`` to ``False`` to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestTypeError(unittest.TestCase):

*********************************************************************************
test_type_error_w_non_callables
*********************************************************************************

There are :ref:`objects<classes>` that can NOT be called

RED: make it fail
#################################################################################

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

* I add it to the list of :ref:`Exceptions<errors>` encountered

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # AttributeError

GREEN: make it pass
#################################################################################

* I click on ``type_error.py`` in the ``src`` folder_ to open it in the :ref:`editor<2 editors>` of my `Integrated Development Environment (IDE)`_, then add the name and point it to :ref:`None`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    none = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  the ``()`` to the right of ``src.type_error.none`` makes it a call, and the name ``none`` points to :ref:`None` which is NOT callable_

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

    # Exceptions Encountered
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

REFACTOR: make it better
#################################################################################

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

  the terminal_ shows :ref:`TypeError`

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

  the terminal_ shows :ref:`TypeError`

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

  the terminal_ shows :ref:`TypeError`

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


    # Exceptions Encountered

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

  the terminal_ shows :ref:`TypeError`

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

When I call a :ref:`function<functions>` I have to match its definition or I will have problems

RED: make it fail
#################################################################################

* I add a new test to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3-4

            src.type_error.a_dictionary()

        def test_type_error_w_function_signatures(self):
            src.type_error.function_00('a')


    # Exceptions Encountered

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'function_00'

GREEN: make it pass
#################################################################################

* I add the :ref:`function<functions>` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5-6

    def a_dictionary():
        return {'key': 'value'}


    def function_00():
        return None

  the terminal_ shows :ref:`TypeError`

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

REFACTOR: make it better
#################################################################################

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

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: function_01() takes 1 positional argument but 2 were given

* I add another name in parentheses so that the call to the :ref:`function<functions>` and its definition match

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 1

    def function_01(input_1, input_2):
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

    def function_01(input_1, input_2):
        return None


    def function_02(input_1, input_2):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: function_02() takes 2 positional arguments but 3 were given

* I add another name in parentheses to make the number of inputs match in ``type_error.p``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 1

    def function_02(input_1, input_2, input_3):
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

    def function_02(input_1, input_2, input_3):
        return None


    def function_03(input_1, input_2, input_3):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: function_03() takes 3 positional arguments but 4 were given

* I add a 4th name in parentheses to the definition

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 1

    def function_03(input_1, input_2, input_3, input_4):
        return None

  the test passes

I have to call a :ref:`function<functions>` with the same number of inputs its definition expects

----

*********************************************************************************
test_type_error_w_objects_that_do_not_mix
*********************************************************************************

Some operations do not work if the objects_ are not of the same type_

RED: make it fail
#################################################################################

I add a new test with a failing line in ``test_type_error.py``

.. code-block:: python
  :lineno-start: 18
  :emphasize-lines: 3-4

          src.type_error.function_03('a', 'b', 'c', 'd')

      def test_type_error_w_objects_that_do_not_mix(self):
          None + 1


  # Exceptions Encountered

the terminal_ shows TypeError_

.. code-block:: shell

  TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

I cannot do arithmetic_ with :ref:`None`

GREEN: make it pass
#################################################################################

I add the assertRaises_ :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 2-3

      def test_type_error_w_objects_that_do_not_mix(self):
          with self.assertRaises(TypeError):
              None + 1

the test passes

REFACTOR: make it better
#################################################################################

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

    # Exceptions Encountered

  the terminal_ shows all tests are passing

----

*********************************************************************************
test_calculator_raises_type_error
*********************************************************************************

requirements
#################################################################################

:ref:`the calculator<how to make a calculator>` is needed for this part

* I exit the tests by pressing ``ctrl+c`` on the keyboard in the terminal_
* I `change directory`_ to the ``calculator`` folder

  .. code-block:: shell
    :emphasize-lines: 1

    cd calculator

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/calculator

* I activate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    source .venv/bin/activate

  the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/calculator

* I run the tests with `pytest-watch`_

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: shell

    ======================== test session starts =========================
    platform linux -- Python 3.X.7, pytest-9.0.1, pluggy-1.6.0
    rootdir: /workspaces/pumping_python/pumping_python/calculator
    collected 4 items

    tests/test_calculator.py ....                                  [100%]

    ========================= 4 passed in 0.01s ==========================

* I hold ``ctrl`` (Windows/Linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

RED: make it fail
#################################################################################

I add a new failing test to show that I can NOT do an arithmetic_ operation with something that is not a number

.. code-block:: python
  :lineno-start: 33
  :emphasize-lines: 12-14

      def test_division(self):
          while self.y == 0:
              with self.assertRaises(ZeroDivisionError):
                  src.calculator.divide(self.x, self.y)
              self.y = a_random_number()
          else:
              self.assertEqual(
                  src.calculator.divide(self.x, self.y),
                  self.x/self.y
              )

      def test_calculator_raises_type_error(self):
          src.calculator.add(self.x, None)


  # Exceptions Encountered

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

GREEN: make it pass
#################################################################################

I add assertRaises_

.. code-block:: python
  :lineno-start: 44
  :emphasize-lines: 2-3

      def test_calculator_raises_type_error(self):
          with self.assertRaises(TypeError):
              src.calculator.add(self.x, None)

the test passes

REFACTOR: make it better
#################################################################################

* I add a failing line for :ref:`subtraction<test_subtraction>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 4

        def test_calculator_raises_type_error(self):
            with self.assertRaises(TypeError):
                src.calculator.add(self.x, None)
            src.calculator.subtract(self.x, None)

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 4-5

        def test_calculator_raises_type_error(self):
            with self.assertRaises(TypeError):
                src.calculator.add(self.x, None)
            with self.assertRaises(TypeError):
                src.calculator.subtract(self.x, None)

  the test passes

* I add another failing line, this time for :ref:`multiplication<test_multiplication>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 6

        def test_calculator_raises_type_error(self):
            with self.assertRaises(TypeError):
                src.calculator.add(self.x, None)
            with self.assertRaises(TypeError):
                src.calculator.subtract(self.x, None)
            src.calculator.multiply(self.x, None)

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 6-7

        def test_calculator_raises_type_error(self):
            with self.assertRaises(TypeError):
                src.calculator.add(self.x, None)
            with self.assertRaises(TypeError):
                src.calculator.subtract(self.x, None)
            with self.assertRaises(TypeError):
                src.calculator.multiply(self.x, None)

  the test passes

* I add another one for :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 8

        def test_calculator_raises_type_error(self):
            with self.assertRaises(TypeError):
                src.calculator.add(self.x, None)
            with self.assertRaises(TypeError):
                src.calculator.subtract(self.x, None)
            with self.assertRaises(TypeError):
                src.calculator.multiply(self.x, None)
            src.calculator.divide(self.x, None)

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: unsupported operand type(s) for /: 'int' and 'NoneType'

  I add the assertRaises_ :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 8-9

        def test_calculator_raises_type_error(self):
            with self.assertRaises(TypeError):
                src.calculator.add(self.x, None)
            with self.assertRaises(TypeError):
                src.calculator.subtract(self.x, None)
            with self.assertRaises(TypeError):
                src.calculator.multiply(self.x, None)
            with self.assertRaises(TypeError):
                src.calculator.divide(self.x, None)


    # Exceptions Encountered

  the test passes

----

*********************************************************************************
how to make the calculator check if its input is correct
*********************************************************************************

I want to add a :ref:`condition<booleans>` to the calculator to make sure that what the :ref:`functions` receive are numbers. I can do this with TypeError_

* I go to the :ref:`explorer<explorer on left>` in the `Integrated Development Environment (IDE)`_ to open the ``calculator`` folder_
* I open the ``src`` folder and click on ``calculator.py`` to open it in the :ref:`editor<2 editors>`

RED: make it fail
#################################################################################

I add an :ref:`exception handler<how to use try...except...else>` to the :ref:`add function<test_addition>` in ``calculator.py``

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 2-

  def add(input_1, input_2):
      try:
          return input_1 + input_2
      except TypeError:
          return 'Please give only numbers as input'

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: TypeError not raised

because the ``add`` :ref:`function<functions>` now sends a message when :ref:`TypeError` is raised

GREEN: make it pass
#################################################################################

I change the assertRaises_ to assertEqual_ in ``test_calculator.py``

.. code-block:: python
  :lineno-start: 44
  :emphasize-lines: 2-5

  def test_calculator_raises_type_error(self):
      self.assertEqual(
          src.calculator.add(self.x, None),
          'Please give only numbers as input'
      )
      with self.assertRaises(TypeError):
          src.calculator.subtract(self.x, None)
      with self.assertRaises(TypeError):
          src.calculator.multiply(self.x, None)
      with self.assertRaises(TypeError):
          src.calculator.divide(self.x, None)

the test passes

REFACTOR: make it better
#################################################################################

* I add an :ref:`exception handler<how to use try...except...else>` to the :ref:`divide function<test_division>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2-6

    def divide(input_1, input_2):
        try:
            return input_1 / input_2
        except TypeError:
            return 'Please give only numbers as input'


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
                src.calculator.add(self.x, None),
                'Please give only numbers as input'
            )
            self.assertEqual(
                src.calculator.divide(self.x, None),
                'Please give only numbers as input'
            )
            with self.assertRaises(TypeError):
                src.calculator.multiply(self.x, None)
            with self.assertRaises(TypeError):
                src.calculator.subtract(self.x, None)

* I have the same :ref:`exception handler<how to use try...except...else>` in both :ref:`functions` in ``calculator.py``. To follow `The Do Not Repeat Yourself (DRY) Principle`_ I can write a :ref:`function` that will handle TypeError_. The problem will be how it handles the lines that change

  - ``result = input_1 + input_2``
  - ``result = input_1 / input_2``

  I add a new :ref:`function<functions>` to ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-7

    def handle_type_error(function):
        def wrapper(input_1, input_2):
            try:
                return function(input_1, input_2)
            except TypeError:
                return 'Please give only numbers as input'
        return wrapper


    def subtract(input_1, input_2):

  this new :ref:`function<functions>` (``handle_type_error``) takes a :ref:`function<functions>` as input. It has a :ref:`function<functions>` inside it named ``wrapper``, which runs the input :ref:`function` and handles :ref:`TypeError` when raised

* I use the new :ref:`function<functions>` as a wrapper for the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 8-10

    def divide(input_1, input_2):
        try:
            return input_1 / input_2
        except TypeError:
            return 'Please give only numbers as input'


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
                src.calculator.add(self.x, None),
                'Please give only numbers as input'
            )
            self.assertEqual(
                src.calculator.divide(self.x, None),
                'Please give only numbers as input'
            )
            self.assertEqual(
                src.calculator.multiply(self.x, None),
                'Please give only numbers as input'
            )
            with self.assertRaises(TypeError):
                src.calculator.subtract(self.x, None)

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
                src.calculator.add(self.x, None),
                'Please give only numbers as input'
            )
            self.assertEqual(
                src.calculator.divide(self.x, None),
                'Please give only numbers as input'
            )
            self.assertEqual(
                src.calculator.multiply(self.x, None),
                'Please give only numbers as input'
            )
            self.assertEqual(
                src.calculator.subtract(self.x, None),
                'Please give only numbers as input'
            )


    # Exceptions Encountered

  the test passes

* I change the name of the test to be more descriptive

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 1

        def test_calculator_sends_a_message_when_inputs_are_not_numbers(self):
            self.assertEqual(

  The ``calculator`` now uses :ref:`TypeError` to send a message when bad inputs are passed, but there is a case I have not considered

* Python_ allows using the ``+`` operator with strings_ but it does not work for the other arithmetic_ operations

  .. code-block:: python

----

*********************************************************************************
review
*********************************************************************************

I ran tests for TypeError_ with
* objects_ that are not callable_
* :ref:`function<functions>` definitions and
* objects_ that do not mix.

Would you like to :ref:`test Lists?<lists>`

----

:ref:`TypeError: tests and solution`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->