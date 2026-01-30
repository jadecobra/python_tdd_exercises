.. meta::
  :description: Facing a Python TypeError? Learn to fix common errors like 'unsupported operand type' and 'int object is not callable'. Watch the full tutorial to debug now.
  :keywords: Jacob Itegboje, python typeerror unsupported operand type, python typeerror 'int' object is not callable, python typeerror can only concatenate str, how to fix typeerror in python, python typeerror string and integer, python typeerror list indices must be integers, python typeerror 'str' object is not callable, python typeerror float object is not iterable

.. include:: ../../links.rst

.. _TypeError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError

#################################################################################
TypeError
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/DdEmPvYaCEQ?si=ih9z9nUVSJnY4D0N" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../../code/tests/test_type_error.py
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

* I change everywhere I have ``exceptions`` to the name of this project

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

    on Windows_ without `Windows Subsystem for Linux`_ use ``makePythonTdd.ps1`` NOT ``makePythonTdd.sh``

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

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``makePythonTdd.ps1`` NOT ``makePythonTdd.sh``

    .. code-block:: shell
      :emphasize-lines: 1

      ./makePythonTdd.ps1

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 10
    :emphasize-text: tests/test_type_error.py:7

    ================================= FAILURES =================================
    ______________________________ TestTypeError.test_failure ______________________________

    self = <tests.test_exceptions.TestTypeError testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_type_error.py:7: AssertionError
    ========================== short test summary info ============================
    FAILED tests/test_type_error.py::TestTypeError::test_failure - AssertionError: True is not false
    ============================ 1 failed in X.YZs =============================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_type_error.py:7`` to open it in the :ref:`editor<2 editors>`

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

There are :ref:`objects<what is a class?>` that can NOT be called

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

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

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'none'

  there is nothing in ``type_error.py`` in the ``src`` folder_ yet

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

    # Exceptions seen
    # AssertionError
    # AttributeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``type_error.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>` of my `Integrated Development Environment (IDE)`_, then add the name and point it to :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    none = None

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  - the ``()`` to the right of ``src.type_error.none`` makes it a call
  - the name ``none`` points to :ref:`None<what is None?>` which is NOT callable_

  I cannot call :ref:`None<what is None?>` like a :ref:`function<what is a function?>`

* I add TypeError_ to the list of :ref:`Exceptions<errors>` seen in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

    # Exceptions seen
    # AssertionError
    # AttributeError
    # TypeError

* I make ``none`` a :ref:`function<what is a function?>` in ``type_error.py`` to make it callable_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def none():
        return None

  the test passes

I can call a :ref:`function<what is a function?>`, I cannot call :ref:`None<what is None?>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3

        def test_type_error_w_the_uncallables(self):
            src.type_error.none()
            src.type_error.false()

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

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

  I cannot call a :ref:`boolean<what are booleans?>` the way I can call a :ref:`function<what is a function?>`

* I change the :ref:`variable<what is a variable?>` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    def none():
        return None

    def false():
        return False

  the terminal_ shows green again

* I add a line to test the other :ref:`boolean<what are booleans?>` in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

        def test_type_error_w_the_uncallables(self):
            src.type_error.none()
            src.type_error.false()
            src.type_error.true()

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

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

* I make it a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def false():
        return False


    def true():
        return True

  the test passes. I can call a :ref:`function<what is a function?>`, I cannot call a :ref:`boolean<what are booleans?>` or :ref:`None<what is None?>`

* I add a failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 4

            src.type_error.none()
            src.type_error.false()
            src.type_error.true()
            src.type_error.an_integer()

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

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

* I change the :ref:`variable<what is a variable?>` to a :ref:`funcion<what is a function?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def true():
        return True


    def an_integer():
        return 1234

  the test passes. I can call a :ref:`function<what is a function?>`, I cannot call an integer_, a :ref:`boolean<what are booleans?>` or :ref:`None<what is None?>`

* I add a line for a float_ in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4

            src.type_error.false()
            src.type_error.true()
            src.type_error.an_integer()
            src.type_error.a_float()

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

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

* I make ``a_float`` a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5-6

    def an_integer():
        return 1234


    def a_float():
        return 1.234

  the test passes. I can call a :ref:`function<what is a function?>`, I cannot call a float_, integer_, :ref:`boolean<what are booleans?>` or :ref:`None<what is None?>`

* I add a line for a string_ (anything in :ref:`quotes`) in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 4

            src.type_error.true()
            src.type_error.an_integer()
            src.type_error.a_float()
            src.type_error.a_string()

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

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

* I change ``a_string`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5-6

    def a_float():
        return 1.234


    def a_string():
        return 'a string'

  the test passes. I can call a :ref:`function<what is a function?>`. I cannot call a string_, a float_, integer_, :ref:`boolean<what are booleans?>` or :ref:`None<what is None?>`

* I add a failing line for a tuple_ (anything in parentheses ``()``, separated by a comma) in ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

            src.type_error.an_integer()
            src.type_error.a_float()
            src.type_error.a_string()
            src.type_error.a_tuple()

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

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

* I change it to a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-6

    def a_string():
        return 'a string'


    def a_tuple():
        return (1, 2, 3, 'n')

  the test passes. I can call a :ref:`function<what is a function?>`. I cannot call a tuple_, string_, float_, integer_ :ref:`boolean<what are booleans?>` or :ref:`None<what is None?>`

* I add another line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 4

            src.type_error.a_float()
            src.type_error.a_string()
            src.type_error.a_tuple()
            src.type_error.a_list()

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

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

* I change ``a_list`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5-6

    def a_tuple():
        return (1, 2, 3, 'n')


    def a_list():
        return [1, 2, 3, 'n']

  the test passes. I can call a :ref:`function<what is a function?>`, I cannot call a :ref:`list<lists>`, tuple_, string_, float_, integer_, :ref:`boolean<what are booleans?>` or :ref:`None<what is None?>`

* I add another failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4

            src.type_error.a_string()
            src.type_error.a_tuple()
            src.type_error.a_list()
            src.type_error.a_set()

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

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

* I make it a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 5-6

    def a_list():
        return [1, 2, 3, 'n']


    def a_set():
        return {1, 2, 3, 'n'}

  the test passes. I can call a :ref:`function<what is a function?>`, I cannot call a set_, :ref:`list<lists>`, tuple_, string_, float_, integer_, :ref:`boolean<what are booleans?>` or :ref:`None<what is None?>`

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

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

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

* I change it to a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5-6

    def a_set():
        return {1, 2, 3, 'n'}


    def a_dictionary():
        return {'key': 'value'}

  the terminal_ shows green again. I can call a :ref:`function<what is a function?>`, I cannot call a :ref:`dictionary<dictionaries>`, set_, :ref:`list<lists>`, tuple_, string_, float_, integer_, :ref:`boolean<what are booleans?>` or :ref:`None<what is None?>`

It is safe to say that I cannot call :ref:`data structures` because they are NOT callable_. I can call :ref:`functions<what is a function?>`, they are callable_

----

*********************************************************************************
test_type_error_w_function_signatures
*********************************************************************************

When I call a :ref:`function<what is a function?>` I have to match its definition also known as its signature or I get TypeError_

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a new test to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3-4

            src.type_error.a_dictionary()

        def test_type_error_w_function_signatures(self):
            src.type_error.function_00('a')


    # Exceptions seen

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'function_00'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the :ref:`function<what is a function?>` to ``type_error.py``

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

* I add a name in parentheses to the :ref:`function<what is a function?>` definition

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 1

    def function_00(the_input):
        return None

  the test passes

I have to call a :ref:`function<what is a function?>` in a way that matches its definition or I get TypeError_

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a new failing line to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 19

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00('a')
        src.type_error.function_01('a', 'b')

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'function_01'. Did you mean: 'function_00'?

* I add the :ref:`function<what is a function?>` to ``type_error.py``

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

* I change the first name, then add another name in parentheses so that the call to the :ref:`function<what is a function?>` and its definition match

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

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'function_02'. Did you mean: 'function_00'?

* I add the :ref:`function<what is a function?>` to ``type_error.py``

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

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'function_03'. Did you mean: 'function_00'?

* I add the :ref:`function<what is a function?>` to ``type_error.py``

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

I have to call a :ref:`function<what is a function?>` with the same number of inputs its definition expects

----

*********************************************************************************
test_type_error_w_objects_that_do_not_mix
*********************************************************************************

Some operations do not work if the :ref:`objects<what is a class?>` are NOT the same type_

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

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

I cannot do arithmetic_ with :ref:`None<what is None?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the `assertRaises method`_

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 2-3

      def test_type_error_w_objects_that_do_not_mix(self):
          with self.assertRaises(TypeError):
              None + False

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

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
review
*********************************************************************************

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

*************************************************************************************
what is next?
*************************************************************************************

you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to make a Python Test Driven Development environment automatically` or :ref:`how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`

:ref:`Would you like to use what you know so far with the Calculator?<how to make a calculator 3>`

-----

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