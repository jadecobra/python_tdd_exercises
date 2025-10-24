.. meta::
  :description: Facing a Python TypeError? Learn to fix common errors like 'unsupported operand type' and 'int object is not callable'. Watch the full tutorial to debug now.
  :keywords: Jacob Itegboje, python typeerror unsupported operand type, python typeerror 'int' object is not callable, python typeerror can only concatenate str, how to fix typeerror in python, python typeerror string and integer, python typeerror list indices must be integers, python typeerror 'str' object is not callable, python typeerror float object is not iterable

.. include:: ../links.rst

#################################################################################
TypeError
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/DdEmPvYaCEQ?si=ih9z9nUVSJnY4D0N" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

The `TypeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError>`_ is raised when an :ref:`object<classes>` is used in a way that it should not be.

*********************************************************************************
test_type_error_w_non_callables
*********************************************************************************

There are objects that cannot be called

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``type_error`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh type_error

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 type_error

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_type_error.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_type_error.py:7`` to open it in the editor
* then change ``True`` to ``False``
* I add an `import statement`_

  .. code-block:: python

    import unittest
    import src.type_error

* and change ``test_failure`` to ``test_type_error_w_non_callables``

  .. code-block:: python

    class TestTypeError(unittest.TestCase):

        def test_type_error_w_non_callables(self):
            src.type_error.none()

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'none'

  I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError

green: make it pass
#################################################################################

* then I add the name to ``type_error.py`` and point it to :ref:`None`

  .. code-block:: python

    none = None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  the ``()`` to the right of ``src.type_error.none`` makes it a call, and the name ``none`` points to :ref:`None` which is not callable_

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # TypeError

* and I make ``none`` a :ref:`function<functions>` to make it callable_

  .. code-block:: python

    def none():
        return None

  the test passes

refactor: make it better
#################################################################################

* I add another line to the test

  .. code-block:: python

    def test_type_error_w_non_callables(self):
        src.type_error.none()
        src.type_error.false()

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'false'

  when I add the name to ``type_error.py`` and point it to :ref:`False<test_what_is_false>`

  .. code-block:: python

    def none():
        return None


    false = False

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'bool' object is not callable

  I make it a :ref:`function<functions>`

  .. code-block:: python

    def none():
        return None

    def false():
        return False

  the terminal shows green again

* I add a line to test the other :ref:`boolean<Booleans>`

  .. code-block:: python

    def test_type_error_w_non_callables(self):
        src.type_error.none()
        src.type_error.false()
        src.type_error.true()

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'true'

  I add the name to ``type_error.py`` and point it to :ref:`True<test_what_is_true>`

  .. code-block:: python

    def false():
        return False


    true = True

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'bool' object is not callable

  when I make it a :ref:`function<functions>`

  .. code-block:: python

    def false():
        return False


    def true():
        return True

  the test passes

* I add another line to the test

  .. code-block:: python

    def test_type_error_w_non_callables(self):
        src.type_error.none()
        src.type_error.false()
        src.type_error.true()
        src.type_error.a_list()

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'a_list'

  I add the name and point it to a :ref:`list<lists>`

  .. code-block:: python

    def true():
        return True


    a_list = [1, 2, 3, 'n']

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'list' object is not callable

  then I make it a :ref:`function<functions>`

  .. code-block:: python

    def true():
        return True


    def a_list():
        return [1, 2, 3, 'n']

  and the test passes

* I add a new failing line

  .. code-block:: python

    def test_type_error_w_non_callables(self):
        src.type_error.none()
        src.type_error.false()
        src.type_error.true()
        src.type_error.a_list()
        src.type_error.a_dictionary()

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'a_dictionary'

  I add the name and point it to a :ref:`dictionary<dictionaries>`

  .. code-block:: python

    def a_list():
        return [1, 2, 3, 'n']


    a_dictionary = {'key': 'value'}

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'dict' object is not callable

  then I change it to a :ref:`function<functions>`

  .. code-block:: python

    def a_list():
        return [1, 2, 3, 'n']


    def a_dictionary():
        return {'key': 'value'}

  the terminal shows green again. It is safe to say that I cannot call :ref:`data structures`.

----

*********************************************************************************
test_type_error_w_function_signatures
*********************************************************************************

Calls to a :ref:`function<functions>` have to match its signature

red: make it fail
#################################################################################

* I add a new test

  .. code-block:: python

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00('a')

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'function_00'

  then I add the :ref:`function<functions>` to ``type_error.py``

  .. code-block:: python

    def a_dictionary():
        return {'key': 'value'}


    def function_00():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: function_00() takes 0 positional arguments but 1 was given

  because ``function_00`` is called with ``'a'`` as input but the definition does not accept any inputs

green: make it pass
#################################################################################

* I add an input parameter to the :ref:`function<functions>` definition

  .. code-block:: python

    def function_00(argument):
        return None

  the terminal shows passing tests

refactor: make it better
#################################################################################

* I add a new failing line

  .. code-block:: python

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00('a')
        src.type_error.function_01('a', 'b')

  the terminal shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.type_error' has no attribute 'function_01'. Did you mean: 'function_00'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def function_00(argument):
        return None


    def function_01(argument):
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: function_01() takes 1 positional argument but 2 were given

  when I make the number of inputs in the definition match the number of inputs in the call

  .. code-block:: python

    def function_01(
          argument_1, argument_2
      ):
      return None

  the test passes

* I add another failing line

  .. code-block:: python

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00('a')
        src.type_error.function_01('a', 'b')
        src.type_error.function_02('a', 'b', 'c')

  the terminal shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.type_error' has no attribute 'function_02'. Did you mean: 'function_00'?

  I add the :ref:`function<functions>` to ``type_error.py``

  .. code-block:: python

    def function_01(
            argument_1, argument_2
        ):
        return None


    def function_02(
            argument_1, argument_2
        ):
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: function_02() takes 2 positional arguments but 3 were given

  then I make the number of inputs match

  .. code-block:: python

    def function_02(
            argument_1, argument_2,
            argument_3
        ):
        return None

  the terminal shows green again

* I add one more failing line to the test

  .. code-block:: python

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00('a')
        src.type_error.function_01('a', 'b')
        src.type_error.function_02('a', 'b', 'c')
        src.type_error.function_03('a', 'b', 'c', 'd')

  the terminal shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.type_error' has no attribute 'function_03'. Did you mean: 'function_00'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def function_02(
            argument_1, argument_2,
            argument_3
        ):
        return None


    def function_03(
            argument_1, argument_2,
            argument_3
        ):
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: function_03() takes 3 positional arguments but 4 were given

  I add a 4th parameter to the definition

  .. code-block:: python

    def function_03(
        argument_1, argument_2,
        argument_3, argument_4
    ):
        return None

  the terminal shows both tests are passing.

----

*********************************************************************************
test_type_error_w_objects_that_do_not_mix
*********************************************************************************

Some operations do not work if the objects_ are not the same type_

red: make it fail
#################################################################################

I add a new test with a failing line

.. code-block:: python

  def test_type_error_w_objects_that_do_not_mix(self):
      None + 1

the terminal shows `TypeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError>`_

.. code-block:: python

  TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

I cannot do arithmetic_ with :ref:`None`

green: make it pass
#################################################################################

I add the assertRaises_ :ref:`method<functions>`

.. code-block:: python

  def test_type_error_w_objects_that_do_not_mix(self):
      with self.assertRaises(TypeError):
          None + 1

and the test passes

refactor: make it better
#################################################################################

* I add another line

  .. code-block:: python

    def test_type_error_w_objects_that_do_not_mix(self):
        with self.assertRaises(TypeError):
            None + 1
        'text' + 0.1

  the terminal shows `TypeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError>`_

  .. code-block:: python

    TypeError: can only concatenate str (not "float") to str

  I cannot add something that is not a string_ to a string_. I add assertRaises_

  .. code-block:: python

    def test_type_error_w_objects_that_do_not_mix(self):
        with self.assertRaises(TypeError):
            None + 1
        with self.assertRaises(TypeError):
            'text' + 0.1

  and the test passes

* then I add one more line

  .. code-block:: python

    def test_type_error_w_objects_that_do_not_mix(self):
        with self.assertRaises(TypeError):
            None + 1
        with self.assertRaises(TypeError):
            'text' + 0.1
        (1, 2, 3, 'n') - {1, 2, 3, 'n'}

  the terminal shows `TypeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError>`_

  .. code-block:: python

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

  the terminal shows all tests are passing.

----

*********************************************************************************
review
*********************************************************************************

I ran tests for `TypeError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#TypeError>`_ with objects_ that are not callable_, :ref:`function<functions>` signatures and objects_ that do not mix. Would you like to :ref:`test data structures?<data structures>`

----

:doc:`/code/code_type_error`