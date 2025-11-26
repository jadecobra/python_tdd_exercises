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

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_type_error.py:7`` to open it in the :ref:`editor<2 editors>`
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

red: make it fail
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

green: make it pass
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

refactor: make it better
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

red: make it fail
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

green: make it pass
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

refactor: make it better
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

red: make it fail
#################################################################################

I add a new test with a failing line

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

green: make it pass
#################################################################################

I add the assertRaises_ :ref:`method<functions>`

.. code-block:: python

  def test_type_error_w_objects_that_do_not_mix(self):
      with self.assertRaises(TypeError):
          None + 1

the test passes

refactor: make it better
#################################################################################

* I add another line

  .. code-block:: python

    def test_type_error_w_objects_that_do_not_mix(self):
        with self.assertRaises(TypeError):
            None + 1
        'text' + 0.1

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: can only concatenate str (not "float") to str

  I cannot add something that is not a string_ to a string_. I add assertRaises_

  .. code-block:: python

    def test_type_error_w_objects_that_do_not_mix(self):
        with self.assertRaises(TypeError):
            None + 1
        with self.assertRaises(TypeError):
            'text' + 0.1

  the test passes

* then I add one more line

  .. code-block:: python

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

    def test_type_error_w_objects_that_do_not_mix(self):
        with self.assertRaises(TypeError):
            None + 1
        with self.assertRaises(TypeError):
            'text' + 0.1
        with self.assertRaises(TypeError):
            (1, 2, 3, 'n') - {1, 2, 3, 'n'}

  the terminal_ shows all tests are passing.

----

*********************************************************************************
review
*********************************************************************************

I ran tests for TypeError_ with objects_ that are not callable_, :ref:`function<functions>` definitions and objects_ that do not mix.

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