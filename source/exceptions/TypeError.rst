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

*********************************************************************************
questions about TypeError
*********************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`what causes TypeError?`
* :ref:`are data structures callable?<test_type_error_w_the_uncallables>`
* :ref:`what happens when I call a function but do not send the right number of inputs?<test_type_error_w_function_signatures>`
* :ref:`what happens when I try objects that do not mix?<test_type_error_w_objects_that_do_not_mix>`
* :ref:`how can I make sure the calculator only takes numbers?<test_calculator_sends_message_when_input_is_not_a_number>`
* :ref:`how can I make a decorator function?<how to make a decorator function>`

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

* I name this project ``type_error``
* I open ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` in the :ref:`editor<2 editors>`

  .. TIP:: Here is a quick way to open ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` if you are using `Visual Studio Code`_

    .. code-block:: shell
      :emphasize-lines: 1

      code makePythonTdd.sh

    on `Windows`_ without `Windows Subsystem for Linux`_ use

    .. code-block:: shell
      :emphasize-lines: 1

      code makePythonTdd.ps1

* I change everywhere I have ``exceptions`` to the name of this project in ``makePythonTdd.sh``

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

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``makePythonTdd.ps1`` instead of ``makePythonTdd.sh``

    .. code-block:: PowerShell
      :linenos:
      :emphasize-lines: 1-2, 4, 11, 18

      mkdir type_error
      cd type_error
      mkdir src
      New-Item src/type_error.py
      mkdir tests
      New-Item tests/__init__.py

      "import unittest


      class TestTypeError(unittest.TestCase):

          def test_failure(self):
              self.assertFalse(True)

      # Exceptions seen
      # AssertionError
      " | Out-File tests/test_type_error.py

* I run the program_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``makePythonTdd.ps1`` instead of ``makePythonTdd.sh``

    .. code-block:: shell
      :emphasize-lines: 1

      ./makePythonTdd.ps1

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell
    :emphasize-lines: 10
    :emphasize-text: tests/test_type_error.py:7

    ======================================= FAILURES =======================================
    ______________________________ TestTypeError.test_failure ______________________________

    self = <tests.test_exceptions.TestTypeError testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_type_error.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_type_error.py::TestTypeError::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option` or :kbd:`command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_type_error.py:7`` to open it in the :ref:`editor<2 editors>`

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
test_type_error_w_the_uncallables
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

* I change ``test_failure`` to ``test_type_error_w_the_uncallables`` with a failing line

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-4

    class TestTypeError(unittest.TestCase):

        def test_type_error_w_the_uncallables(self):
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

I can call a :ref:`function<functions>`, I cannot call :ref:`None`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3

        def test_type_error_w_the_uncallables(self):
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

  I cannot call a :ref:`boolean<booleans>` the way I can call a :ref:`function<functions>`

* I change the :ref:`variable<what is a variable?>` to a :ref:`function<functions>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    def none():
        return None

    def false():
        return False

  the terminal_ shows green again

* I add a line to test the other :ref:`boolean<Booleans>` in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

        def test_type_error_w_the_uncallables(self):
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

  the test passes. I can call a :ref:`function<functions>`, I cannot call a :ref:`boolean<booleans>` or :ref:`None`

* I add a failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 4

            src.type_error.none()
            src.type_error.false()
            src.type_error.true()
            src.type_error.an_integer()

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'an_integer'

* I add the name and point it to an integer_ in ``type_error.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5

    def true():
        return True


    an_integer = 1234

  the terminal_ shows TypeError_

* I change the :ref:`variable<what is a variable?>` to a :ref:`funcion<functions>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def true():
        return True


    def an_integer():
        return 1234

  the test passes. I can call a :ref:`function<functions>`, I cannot call an integer_, a :ref:`boolean<booleans>` or :ref:`None`

* I add a line for a float_ in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4

            src.type_error.false()
            src.type_error.true()
            src.type_error.an_integer()
            src.type_error.a_float()

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'a_float'

* I add the name and point it to a float_ in ``type_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5

    def an_integer():
        return 1234


    a_float = 1.234

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: 'float' object is not callable

* I make ``a_float`` a :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5-6

    def an_integer():
        return 1234


    def a_float():
        return 1.234

  the test passes. I can call a :ref:`function<functions>`, I cannot call a float_, integer_, :ref:`boolean<booleans>` or :ref:`None`

* I add a line for a string_ (anything in :ref:`quotes`) in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 4

            src.type_error.true()
            src.type_error.an_integer()
            src.type_error.a_float()
            src.type_error.a_string()

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'a_string'

* I add the name and point it to a string_ in ``type_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5

    def a_float():
        return 1.234


    a_string = 'a string'

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: 'str' object is not callable

* I change ``a_string`` to a :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5-6

    def a_float():
        return 1.234


    def a_string():
        return 'a string'

  the test passes. I can call a :ref:`function<functions>`. I cannot call a string_, a float_, integer_, :ref:`boolean<booleans>` or :ref:`None`

* I add a failing line for a tuple_ (anything in parentheses ``()``, separated by a comma) in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

            src.type_error.an_integer()
            src.type_error.a_float()
            src.type_error.a_string()
            src.type_error.a_tuple()

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'a_tuple'

* I add the name and point it to a tuple_ in ``type_error.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5

    def a_string():
        return 'a string'


    a_tuple = (1, 2, 3, 'n')

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: 'tuple' object is not callable

* I change it to a :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-6

    def a_string():
        return 'a string'


    def a_tuple():
        return (1, 2, 3, 'n')

  the test passes. I can call a :ref:`function<functions>`. I cannot call a tuple_, string_, float_, integer_ :ref:`boolean<booleans>` or :ref:`None`

* I add another line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 4

            src.type_error.a_float()
            src.type_error.a_string()
            src.type_error.a_tuple()
            src.type_error.a_list()

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'a_list'

* I add the name and point it to a :ref:`list<lists>` (anything in square brackets (``[]``) in ``type_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5

    def a_tuple():
        return (1, 2, 3, 'n')


    a_list = [1, 2, 3, 'n']

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: 'list' object is not callable

* I change ``a_list`` to a :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5-6

    def a_tuple():
        return (1, 2, 3, 'n')


    def a_list():
        return [1, 2, 3, 'n']

  the test passes. I can call a :ref:`function<functions>`, I cannot call a :ref:`list<lists>`, tuple_, string_, float_, integer_, :ref:`boolean<booleans>` or :ref:`None`

* I add another failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4

            src.type_error.a_string()
            src.type_error.a_tuple()
            src.type_error.a_list()
            src.type_error.a_set()

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'a_set'

* I add the name and point it to a set_ in ``type_error.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 5

    def a_list():
        return [1, 2, 3, 'n']


    a_set = {1, 2, 3, 'n'}

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: 'set' object is not callable

* I make it a :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 5-6

    def a_list():
        return [1, 2, 3, 'n']


    def a_set():
        return {1, 2, 3, 'n'}

  the test passes. I can call a :ref:`function<functions>`, I cannot call a set_, :ref:`list<lists>`, tuple_, string_, float_, integer_, :ref:`boolean<booleans>` or :ref:`None`

* I add the last failing line for this test to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 11

        def test_type_error_w_the_uncallables(self):
            src.type_error.none()
            src.type_error.false()
            src.type_error.true()
            src.type_error.an_integer()
            src.type_error.a_float()
            src.type_error.a_string()
            src.type_error.a_tuple()
            src.type_error.a_list()
            src.type_error.a_set()
            src.type_error.a_dictionary()


    # Exceptions seen

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'a_dictionary'

* I add the name and point it to a :ref:`dictionary<dictionaries>` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5

    def a_set():
        return {1, 2, 3, 'n'}


    a_dictionary = {'key': 'value'}

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: 'dict' object is not callable

* I change it to a :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5-6

    def a_set():
        return {1, 2, 3, 'n'}


    def a_dictionary():
        return {'key': 'value'}

  the terminal_ shows green again. I can call a :ref:`function<functions>`, I cannot call a :ref:`dictionary<dictionaries>`, set_, :ref:`list<lists>`, tuple_, string_, float_, integer_, :ref:`boolean<booleans>` or :ref:`None`

It is safe to say that I cannot call :ref:`data structures` because they are NOT callable_. I can call :ref:`functions`, they are callable_

----

*********************************************************************************
test_type_error_w_function_signatures
*********************************************************************************

When I call a :ref:`function<functions>` I have to match its definition also known as its signature or I get TypeError_

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add a new test to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 17
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
    :lineno-start: 37
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
    :lineno-start: 41
    :emphasize-lines: 1

    def function_00(the_input):
        return None

  the test passes

I have to call a :ref:`function<functions>` in a way that matches its definition or I get TypeError_

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add a new failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 19

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00('a')
        src.type_error.function_01('a', 'b')

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'function_01'. Did you mean: 'function_00'?

* I add the :ref:`function<functions>` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 5-6

    def function_00(the_input):
        return None


    def function_01(the_input):
        return None

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: function_01() takes 1 positional argument but 2 were given

  the definition only allows one input, and the test sent two

* I change the first name, then add another name in parentheses so that the call to the :ref:`function<functions>` and its definition match

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 1

    def function_01(first, second):
        return None

  the test passes

* I add another failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 19
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
    :lineno-start: 45
    :emphasize-lines: 5-6

    def function_01(first, second):
        return None


    def function_02(first, second):
        return None

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: function_02() takes 2 positional arguments but 3 were given

* I change the name of the first input, then add another name in parentheses to make the number of inputs match

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 1

    def function_02(first, second, third):
        return None

  the test passes

* I add one more failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 19
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
    :lineno-start: 49
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
    :lineno-start: 53
    :emphasize-lines: 1

    def function_03(first, second, third, fourth):
        return None

  the test passes

I have to call a :ref:`function<functions>` with the same number of inputs its definition expects

----

*********************************************************************************
test_type_error_w_objects_that_do_not_mix
*********************************************************************************

Some operations do not work if the objects_ are NOT the same type_

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test with a failing line in ``test_type_error.py``

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 3-4

          src.type_error.function_03('a', 'b', 'c', 'd')

      def test_type_error_w_objects_that_do_not_mix(self):
          None + False


  # Exceptions seen

the terminal_ shows TypeError_

.. code-block:: shell

  TypeError: unsupported operand type(s) for +: 'NoneType' and 'bool'

I cannot do arithmetic_ with :ref:`None`

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the `assertRaises method`_

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 2-3

      def test_type_error_w_objects_that_do_not_mix(self):
          with self.assertRaises(TypeError):
              None + False

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another failing line to the test

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4

        def test_type_error_w_objects_that_do_not_mix(self):
            with self.assertRaises(TypeError):
                None + False
            True - 'text'

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for -: 'bool' and 'str'

* I use assertRaises_ to handle the :ref:`Exception<errors>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4-5

        def test_type_error_w_objects_that_do_not_mix(self):
            with self.assertRaises(TypeError):
                None + False
            with self.assertRaises(TypeError):
                True - 'text'

  the test passes

* I add another failing line

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 6

        def test_type_error_w_objects_that_do_not_mix(self):
            with self.assertRaises(TypeError):
                None + False
            with self.assertRaises(TypeError):
                True - 'text'
            (0, 1, 2, 'n') * [0, 1, 2, 'n']

  the terminal_ shows TypeError_

  .. code-block:: none

    TypeError: can't multiply sequence by non-int of type 'list'

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 6-7

        def test_type_error_w_objects_that_do_not_mix(self):
            with self.assertRaises(TypeError):
                None + False
            with self.assertRaises(TypeError):
                True - 'text'
            with self.assertRaises(TypeError):
                (0, 1, 2, 'n') * [0, 1, 2, 'n']

    # Exceptions seen

  the test passes

* I add another failing line

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 8

        def test_type_error_w_objects_that_do_not_mix(self):
            with self.assertRaises(TypeError):
                None + False
            with self.assertRaises(TypeError):
                True - 'text'
            with self.assertRaises(TypeError):
                (0, 1, 2, 'n') * [0, 1, 2, 'n']
            {0, 1, 2, 'n'} / {'key': 'value'}

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for /: 'set' and 'dict'

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 8-9


    def test_type_error_w_objects_that_do_not_mix(self):
        with self.assertRaises(TypeError):
            None + False
        with self.assertRaises(TypeError):
            True - 'text'
        with self.assertRaises(TypeError):
            (0, 1, 2, 'n') * [0, 1, 2, 'n']
        with self.assertRaises(TypeError):
            {0, 1, 2, 'n'} / {'key': 'value'}

  the terminal_ shows all tests are passing

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_type_error.py``  and ``type_error.py`` in the :ref:`editor<2 editors>`
* then I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard, the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

.. NOTE:: on Windows_ without `Windows Subsystem for Linux`_

  * the terminal_ shows

    .. code-block:: PowerShell

      (.venv) ...\pumping_python\type_error

  * I deactivate the `virtual environment`_

    .. code-block:: PowerShell
      :emphasize-lines: 1

      deactivate

    the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

    .. code-block:: PowerShell

      ...\pumping_python\type_error

  * I `change directory`_ to the parent of ``type_error``

    .. code-block:: shell
      :emphasize-lines: 1

      cd ..

    the terminal_ shows

    .. code-block:: PowerShell

      ...\pumping_python

    I am back in the ``pumping_python`` directory_

----

*********************************************************************************
test_calculator_raises_type_error
*********************************************************************************

I want to use TypeError_ with :ref:`exception handlers<how to use try...except...else>` to make sure that the :ref:`calculator program<how to make a calculator>` only works with numbers, the way a Calculator would in the real world.

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

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` instead of ``source .venv/bin/activate``

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

I add a new failing test to show that the :ref:`calculator<how to make a calculator>` raises TypeError_ when one of the inputs is :ref:`None`, just like in :ref:`test_type_error_w_objects_that_do_not_mix`

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

      def test_calculator_raises_type_error_w_none(self):
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

      def test_calculator_raises_type_error_w_none(self):
          with self.assertRaises(TypeError):
              src.calculator.add(None, None)

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add a failing line for :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 4

        def test_calculator_raises_type_error_w_none(self):
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
                src.calculator.multiply(None, None)
            src.calculator.subtract(None, None)

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'

  I add the `assertRaises method`_

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 8-9

        def test_calculator_raises_type_error_w_none(self):
            with self.assertRaises(TypeError):
                src.calculator.add(None, None)
            with self.assertRaises(TypeError):
                src.calculator.divide(None, None)
            with self.assertRaises(TypeError):
                src.calculator.multiply(None, None)
            with self.assertRaises(TypeError):
                src.calculator.subtract(None, None)


    # Exceptions seen

  the test passes

The ``calculator`` raises TypeError_ when given :ref:`None` as input. What does it do when the input is a :ref:`boolean<booleans>`, string_, tuple_, :ref:`list<lists>`, set_ or :ref:`a dictionary<dictionaries>`?

*********************************************************************************
test_calculator_raises_type_error_w_strings
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test with an :ref:`assertion<what is an assertion?>` from :ref:`test_what_is_an_assertion`  to test the :ref:`add function<test_addition>` with strings_

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

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 3

        def test_calculator_with_strings(self):
            self.assertEqual(src.calculator.add('1', '1'), '11')
            self.assertEqual(src.calculator.divide('1', '1'), '11')

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for /: 'str' and 'str'

  I change assertEqual_ to assertRaises_

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

  .. code-block:: none

    TypeError: can't multiply sequence by non-int of type 'str'

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 3-4

            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')

  the test passes

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
    :lineno-start: 57
    :emphasize-lines: 8-9

        def test_calculator_raises_type_error_w_none(self):
            with self.assertRaises(TypeError):
                src.calculator.add(None, None)
            with self.assertRaises(TypeError):
                src.calculator.divide(None, None)
            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.subtract('1', '1')

  the test passes

---------------------------------------------------------------------------------
how to test if something is an instance of an object in a program
---------------------------------------------------------------------------------

I want the :ref:`add function<test_addition>` to raise TypeError_ when it gets a string_, the same way the other :ref:`functions` raise TypeError_ when one of the inputs is a string_. I can use the `isinstance function`_ which is like the `assertIsInstance method`_ from when I tested :ref:`None`, it checks if one thing is an instance or child of a :ref:`class<classes>`

* I change the assertEqual_ to assertRaises_ in ``test_calculator_with_strings`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2-3

        def test_calculator_with_strings(self):
            with self.assertRaises(TypeError):
                src.calculator.add('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

* I open ``calculator.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* then I add an :ref:`if statement<if statements>` to the :ref:`add function<test_addition>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2-7

    def add(first_input, second_input):
        if isinstance(first_input, str) or isinstance(second_input, str):
            raise TypeError
        else:
            return first_input + second_input

  the test passes

  .. NOTE::

    - the `isinstance function`_ like the `assertIsInstance method`_ checks if the first input it is given is an instance (child) of the :ref:`class<classes>` it is given as the second input. It is part of `Python's Built-in Functions`_
    - the :ref:`if statement<if statements>` ``if isinstance(first_input, str) or isinstance(second_input, str):`` is :ref:`True<test_what_is_true>` if

      * ``first_input`` is a string_ and ``second_input`` is NOT a string_
      * ``first_input`` is NOT a string_ and ``second_input`` is a string_
      * ``first_input`` is a string_ and ``second_input`` is a string_

      the statement is only :ref:`False<test_what_is_false>` if ``first_input`` is NOT a string_ and ``second_input`` is NOT a string_. This is :ref:`Logical Disjunction from the Truth Table<test_logical_disjunction>`, which only returns :ref:`False<test_what_is_false>` when the two inputs are :ref:`False<test_what_is_false>`

* I change the name of the test to be clearer

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 1

        def test_calculator_raises_type_error_w_strings(self):
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

I want the :ref:`calculator functions<how to make a calculator>` to send a message when the input is not a number, not raise TypeError_ which causes the program to stop. I want the user to be able to try again with different input

=================================================================================
:red:`RED`: make it fail
=================================================================================

I change the assertRaises_ to assertEqual_ for the :ref:`add function<test_addition>` in ``test_calculator_raises_type_error_w_none``

.. code-block:: python
  :lineno-start: 57
  :emphasize-lines: 2-5

      def test_calculator_raises_type_error_w_none(self):
          self.assertEqual(
              src.calculator.add(None, None),
              'Excuse me?! I only work with numbers. Please try again...'
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

I add an :ref:`exception handler<how to use try...except...else>` to the `else clause`_ of the :ref:`add function<test_addition>` in ``calculator.py``

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 4-7

  def add(first_input, second_input):
      if isinstance(first_input, str) or isinstance(second_input, str):
          raise TypeError
      else:
          try:
              return first_input + second_input
          except TypeError:
              return 'Excuse me?! I only work with numbers. Please try again...'

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I want the same thing to happen when the :ref:`add function<test_addition>` gets a string_ as input. I change the assertRaises_ to assertEqual_ for the :ref:`add function<test_addition>` in ``test_calculator_raises_type_error_w_strings`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 2-5

        def test_calculator_raises_type_error_w_strings(self):
            self.assertEqual(
                src.calculator.add('1', '1'),
                'Excuse me?! I only work with numbers. Please try again...'
            )
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError

* I change the `raise statement`_ to a `return statement`_ in the :ref:`add function<test_addition>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3

    def add(first_input, second_input):
        if isinstance(first_input, str) or isinstance(second_input, str):
            return 'Excuse me?! I only work with numbers. Please try again...'
        else:
            try:
                return first_input + second_input
            except TypeError:
                return 'Excuse me?! I only work with numbers. Please try again...'

  the test passes

* I change the assertRaises_ to assertEqual_ for the :ref:`divide function<test_division>` in ``test_calculator_raises_type_error_w_strings`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 6-9

        def test_calculator_raises_type_error_w_strings(self):
            self.assertEqual(
                src.calculator.add('1', '1'),
                'Excuse me?! I only work with numbers. Please try again...'
            )
            self.assertEqual(
                src.calculator.divide('1', '1'),
                'Excuse me?! I only work with numbers. Please try again...'
            )

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for /: 'str' and 'str'

* I add another :ref:`except clause<how to use try...except...else>` to the :ref:`exception handler<how to use try...except...else>` in the :ref:`divide function<test_division>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 6-7

    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'
        except TypeError:
            return 'Excuse me?! I only work with numbers. Please try again...'

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

  ``test_calculator_raises_type_error_w_none`` fails because it expects TypeError_ when the inputs are not numbers

* I change the assertRaises_ to assertEqual_ for the :ref:`divide function<test_division>` in ``test_calculator_raises_type_error_w_none`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 6-9

    def test_calculator_raises_type_error_w_none(self):
        self.assertEqual(
            src.calculator.add(None, None),
            'Excuse me?! I only work with numbers. Please try again...'
        )
        self.assertEqual(
            src.calculator.divide(None, None),
            'Excuse me?! I only work with numbers. Please try again...'
        )

  the test passes

* I change the assertRaises_ to assertEqual_ for the :ref:`multiply function<test_multiplication>` in ``test_calculator_raises_type_error_w_none``

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 5-8


            self.assertEqual(
                src.calculator.divide(None, None),
                'Excuse me?! I only work with numbers. Please try again...'
            )
            self.assertEqual(
                src.calculator.multiply(None, None),
                'Excuse me?! I only work with numbers. Please try again...'
            )

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'

* I add an :ref:`exception handler<how to use try...except...else>` to the :ref:`multiply function<test_multiplication>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-5

    def multiply(first_input, second_input):
        try:
            return first_input * second_input
        except TypeError:
            return 'Excuse me?! I only work with numbers. Please try again...'

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

* I change the assertRaises_ to assertEqual_ for the :ref:`multiply function<test_multiplication>` in ``test_calculator_raises_type_error_w_strings`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.divide('1', '1'),
                'Excuse me?! I only work with numbers. Please try again...'
            )
            self.assertEqual(
                src.calculator.multiply('1', '1'),
                'Excuse me?! I only work with numbers. Please try again...'
            )

  the test passes

* I change the assertRaises_ to assertEqual_ for the :ref:`subtract function<test_subtraction>` in ``test_calculator_raises_type_error_w_strings``

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply('1', '1'),
                'Excuse me?! I only work with numbers. Please try again...'
            )
            self.assertEqual(
                src.calculator.subtract('1', '1'),
                'Excuse me?! I only work with numbers. Please try again...'
            )


    # Exceptions seen

  the terminal_ shows TypeError_

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

* I add an :ref:`exception handler<how to use try...except...else>` to the :ref:`subtract function<test_subtraction>` in ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-5

    def subtract(first_input, second_input):
        try:
            return first_input - second_input
        except TypeError:
            return 'Excuse me?! I only work with numbers. Please try again...'

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

* I change the assertRaises_ to assertEqual_ for the :ref:`subtract function<test_subtraction>` in ``test_calculator_raises_type_error_w_none`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply(None, None),
                'Excuse me?! I only work with numbers. Please try again...'
            )
            self.assertEqual(
                src.calculator.subtract(None, None),
                'Excuse me?! I only work with numbers. Please try again...'
            )


        def test_calculator_raises_type_error_w_strings(self):

  the test passes

  That was a lot of doing the same thing over and over again.

  - ``test_calculator_raises_type_error_w_none`` and ``test_calculator_raises_type_error_w_strings`` both look the same
  - the :ref:`calculator<how to make a calculator>` no longer raises TypeError_ when any of the inputs are NOT a number

* I remove the name of ``test_calculator_raises_type_error_w_strings`` to make its :ref:`assertions<what is an assertion?>` part of ``test_calculator_raises_type_error_w_none``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 5-20

            self.assertEqual(
                src.calculator.subtract(None, None),
                'Excuse me?! I only work with numbers. Please try again...'
            )
            self.assertEqual(
                src.calculator.add('1', '1'),
                'Excuse me?! I only work with numbers. Please try again...'
            )
            self.assertEqual(
                src.calculator.divide('1', '1'),
                'Excuse me?! I only work with numbers. Please try again...'
            )
            self.assertEqual(
                src.calculator.multiply('1', '1'),
                'Excuse me?! I only work with numbers. Please try again...'
            )
            self.assertEqual(
                src.calculator.subtract('1', '1'),
                'Excuse me?! I only work with numbers. Please try again...'
            )


    # Exceptions seen

* I change the name from ``test_calculator_raises_type_error_w_none`` to ``test_calculator_sends_message_when_input_is_not_a_number`` to be clearer

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 1

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            self.assertEqual(

  the tests are still green

* I have the same error message 8 times in this test. I use a :ref:`variable<what is a variable?>` to make it better

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 2, 6, 10, 14, 18, 22, 26, 30, 34

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            error_message = 'Excuse me?! I only work with numbers. Please try again...'

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
            self.assertEqual(
                src.calculator.add('1', '1'),
                error_message
            )
            self.assertEqual(
                src.calculator.divide('1', '1'),
                error_message
            )
            self.assertEqual(
                src.calculator.multiply('1', '1'),
                error_message
            )
            self.assertEqual(
                src.calculator.subtract('1', '1'),
                error_message
            )

  still green. All these :ref:`assertions<what is an assertion?>` look the same, they check that the :ref:`calculator<how to make a calculator>` :ref:`functions` return an error message when they get input that is NOT a number

  .. code-block:: python

    self.assertEqual(
        src.calculator.function(NOT_A_NUMBER, ALSO_NOT_A_NUMBER),
        error_message
    )

  there has to be :ref:`a better way to test the calculator with inputs that are NOT numbers`

----

*********************************************************************************
how to make a decorator function
*********************************************************************************

All the :ref:`functions` in the :ref:`calculator program<how to make a calculator>` have the same :ref:`exception handler<how to use try...except...else>`


.. code-block:: python

  try:
      something
  except TypeError:
      return 'Excuse me?! I only work with numbers. Please try again...'

the :ref:`divide function<test_division>` is different because it has another :ref:`except clause<how to use try...except...else>`

.. code-block:: python

  except ZeroDivisionError:
      return 'undefined: I cannot divide by 0'

the other part that is different for all the :ref:`functions` are the calculations

.. code-block:: python

  return first_input - second_input
  return first_input * second_input
  return first_input / second_input
  return first_input + second_input

=================================================================================
what is a decorator function?
=================================================================================

A decorator or wrapper :ref:`function<functions>` takes another :ref:`function<functions>` as input and returns a :ref:`function<functions>`. I can use it to remove the :ref:`exception handler<how to use try...except...else>` that is the same in all of the :ref:`calculator functions<how to make a calculator>`

* I add a new :ref:`function<functions>` add the top of ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-7

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            try:
                return function(first_input, second_input)
            except TypeError:
                return 'Excuse me?! I only work with numbers. Please try again...'
        return wrapper


    def subtract(first_input, second_input):

  The ``only_takes_numbers`` :ref:`function<functions>` takes a :ref:`function<functions>` as input

  - it tries to return the result of the :ref:`function<functions>` working on the two inputs
  - if TypeError_ is raised it returns the error message

* I use it to wrap the :ref:`subtract function<test_subtraction>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1

    @only_takes_numbers
    def subtract(first_input, second_input):
        try:

  the test is still green

* I remove the parts that are also in the ``only_takes_numbers`` :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3

    @only_takes_numbers
    def subtract(first_input, second_input):
        return first_input - second_input


    def multiply(first_input, second_input):

  still green

* I do the same thing with the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

    @only_takes_numbers
    def multiply(first_input, second_input):
        try:

  the terminal_ shows green

* I remove the parts that are also in the ``only_takes_numbers`` :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3

    @only_takes_numbers
    def multiply(first_input, second_input):
        return first_input * second_input


    def divide(first_input, second_input):

  the tests are still passing

* on to the :ref:`divide function<test_functions>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 1

    @only_takes_numbers
    def divide(first_input, second_input):
        try:

  still green

* I remove the :ref:`except clause<how to use try...except...else>` for TypeError_

  .. code-block:: python
    :lineno-start: 20

    @only_takes_numbers
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'


    def add(first_number, second_input):

  all the tests are still green

* one more to go, I wrap the :ref:`add function<test_addition>` with the ``only_takes_numbers`` :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1

    @only_takes_numbers
    def add(first_input, second_input):
        if isinstance(first_input, str) or isinstance(second_input, str):

  the test is still passing

* I remove the :ref:`exception handler<how to use try...except...else>` from the `else clause`_

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 6

    @only_takes_numbers
    def add(first_input, second_input):
        if isinstance(first_input, str) or isinstance(second_input, str):
            return 'Excuse me?! I only work with numbers. Please try again...'
        else:
            return first_input + second_input

  green! Lovely!

* I can make a :ref:`function<functions>` for the condition in the :ref:`if statement<if statements>` in the :ref:`add function<test_addition>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1-2, 7

    def is_string(something):
        return isinstance(something, str)


    @only_takes_numbers
    def add(first_input, second_input):
        if is_string(first_input) or is_string(second_input):
            return 'Excuse me?! I only work with numbers. Please try again...'
        else:
            return first_input + second_input

  the test is still green

  - This removes the duplication of ``str`` in the call to the `isinstance function`_

    .. code-block:: python

      isinstance(first_input, str)
      isinstance(second_input, str):

  - it also adds 2 lines of code to remove 6 characters. WOW!

* I can make a :ref:`function<functions>` for the whole :ref:`if statement<if statements>` in the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1-2, 7

    def one_input_is_a_string(first_input, second_input):
        return isinstance(first_input, str) or isinstance(second_input, str)


    @only_takes_numbers
    def add(first_input, second_input):
        if one_input_is_a_string(first_input, second_input):
            return 'Excuse me?! I only work with numbers. Please try again...'
        else:
            return first_input + second_input

  the test is still green.

  - the ``one_input_is_a_string`` :ref:`function<functions>` looks the same as :ref:`Logical Disjunction from the Truth Table<test_logical_disjunction>`
  - this makes it easier to change the :ref:`condition<if statements>` later without touching the :ref:`add function<test_addition>`
  - it still adds 2 lines of code

* I can also make a decorator :ref:`function<functions>` for the :ref:`if statement<if statements>` to practice making a decorator :ref:`function<functions>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-7

    def reject_strings(function):
        def wrapper(first_input, second_input):
            if isinstance(first_input, str) or isinstance(second_input, str):
                return 'Excuse me?! I only work with numbers. Please try again...'
            else:
                return function(first_input, second_input)
        return wrapper


    def only_takes_numbers(function):

* then use it to wrap the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 37

    @reject_strings
    @only_takes_numbers
    def add(first_input, second_input):

  the test is still green

* I remove the :ref:`if statement<if statements>` from the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4

    @reject_strings
    @only_takes_numbers
    def add(first_input, second_input):
        return first_input + second_input

  the test is still green

* the ``reject_strings`` and ``only_takes_numbers`` :ref:`functions` have parts that are the same

  .. code-block:: python

        def wrapper(first_input, second_input):
            ...
            return 'Excuse me?! I only work with numbers. Please try again...'
            ...
            return function(first_input, second_input)
        return wrapper

  I make a new :ref:`function<functions>` that has the :ref:`if statement<if statements>` from ``reject_strings`` and the :ref:`exception handler<how to use try...except...else>` from ``only_takes_numbers``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-10

    def only_takes_numbers_and_rejects_strings(function):
        def wrapper(first_input, second_input):
            if isinstance(first_input, str) or isinstance(second_input, str):
                return 'Excuse me?! I only work with numbers. Please try again...'
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return 'Excuse me?! I only work with numbers. Please try again...'
        return wrapper


    def reject_strings(function):

* I use the new :ref:`function<functions>` to wrap the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 1

    @only_takes_numbers_and_rejects_strings
    @reject_strings
    @only_takes_numbers
    def add(first_input, second_input):
        return first_input + second_input

  the test is still green

* I remove the other wrappers from the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 49

    @only_takes_numbers_and_rejects_strings
    def add(first_input, second_input):
        return first_input + second_input

  still green

* I wrap the other :ref:`functions<functions>` with ``only_takes_numbers_and_reject_strings``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 1, 7, 13

    @only_takes_numbers_and_rejects_strings
    @only_takes_numbers
    def subtract(first_input, second_input):
        return first_input - second_input


    @only_takes_numbers_and_rejects_strings
    @only_takes_numbers
    def multiply(first_input, second_input):
        return first_input * second_input


    @only_takes_numbers_and_rejects_strings
    @only_takes_numbers
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'


    @only_takes_numbers_and_rejects_strings
    def add(first_input, second_input):

  the terminal_ shows green

* I remove ``only_takes_numbers`` from each :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 31

    @only_takes_numbers_and_rejects_strings
    def subtract(first_input, second_input):
        return first_input - second_input


    @only_takes_numbers_and_rejects_strings
    def multiply(first_input, second_input):
        return first_input * second_input


    @only_takes_numbers_and_rejects_strings
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'


    @only_takes_numbers_and_rejects_strings
    def add(first_input, second_input):
        return first_input + second_input

  the test is still green

* I remove the ``reject_strings`` and ``only_takes_numbers`` :ref:`functions`

  .. code-block:: python
    :linenos:

    def only_takes_numbers_and_rejects_strings(function):
        def wrapper(first_input, second_input):
            if isinstance(first_input, str) or isinstance(second_input, str):
                return 'Excuse me?! I only work with numbers. Please try again...'
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return 'Excuse me?! I only work with numbers. Please try again...'
        return wrapper


    @only_takes_numbers_and_rejects_strings
    def subtract(first_input, second_input):
        return first_input - second_input


    @only_takes_numbers_and_rejects_strings
    def multiply(first_input, second_input):
        return first_input * second_input


    @only_takes_numbers_and_rejects_strings
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'


    @only_takes_numbers_and_rejects_strings
    def add(first_input, second_input):
        return first_input + second_input

* I change the name of the new decorator :ref:`function<functions>` to make it easier

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 13, 18, 23, 31

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            if isinstance(first_input, str) or isinstance(second_input, str):
                return 'Excuse me?! I only work with numbers. Please try again...'
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return 'Excuse me?! I only work with numbers. Please try again...'
        return wrapper


    @only_takes_numbers
    def subtract(first_input, second_input):
        return first_input - second_input


    @only_takes_numbers
    def multiply(first_input, second_input):
        return first_input * second_input


    @only_takes_numbers
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'


    @only_takes_numbers
    def add(first_input, second_input):
        return first_input + second_input

  still green

* There is also duplication of the error message. I add a :ref:`variable<what is a variable?>` to remove it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3, 6, 11

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            error_message = 'Excuse me?! I only work with numbers. Please try again...'

            if isinstance(first_input, str) or isinstance(second_input, str):
                return error_message
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return error_message
        return wrapper

  and all the tests are still passing. The world is my oyster!

----

=================================================================================
close the project
=================================================================================

* I close ``test_calculator.py`` and ``calculator.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard, the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/calculator

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

The :ref:`calculator program<how to make a calculator>` can take 2 inputs and :ref:`check if they are both numbers<test_calculator_sends_message_when_input_is_not_a_number>`, then :ref:`add<test_addition>`, :ref:`subtract<test_subtraction>`, :ref:`multiply<test_multiplication>` or :ref:`divide<test_division>` them

Even though the program_ says it only works with numbers, I did not add tests for tuples_, :ref:`lists`, sets_, and :ref:`dictionaries`, though they are touched in :ref:`test_type_error_w_objects_that_do_not_mix`, Do you want to add them or do we already have enough tests to know what would happen?

I ran tests for TypeError_ with

* :ref:`objects that are not  callable<test_type_error_w_the_uncallables>`
* :ref:`function definitions<test_type_error_w_function_signatures>`
* :ref:`objects that do not mix<test_type_error_w_objects_that_do_not_mix>` and
* :ref:`used TypeError, an if statement, exception handler and wrapper function to make sure the calculator program only works with numbers<test_calculator_sends_message_when_input_is_not_a_number>`

----

:ref:`How many questions can you answer after going through this chapter?<questions about TypeError>`

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
* :ref:`how to make a Python Test Driven Development environment automatically` or :ref:`how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux`
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