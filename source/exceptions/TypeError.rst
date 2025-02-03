.. include:: ../links.rst

#################################################################################
TypeError
#################################################################################

----

.. contents:: table of contents
  :local:
  :depth: 1

----

`TypeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError>`_ is raised when an object_ is used in a way that it is not meant to be used.

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
* and change ``test_failure`` to ``test_type_error_w_non_callables``

  .. code-block:: python

    import unittest
    import src.type_error


    class TestTypeError(unittest.TestCase):

        def test_type_error_w_non_callables(self):
            src.type_error.none()

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'none'

  which I add to the list of Exceptions_ encountered

  .. code-block:: python

      # Exceptions Encountered
      # AssertionError
      # AttributeError

green: make it pass
#################################################################################

I add the name to ``type_error.py`` and point it to :ref:`None`

.. code-block:: python

  none = None

and the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: 'NoneType' object is not callable

when I make it a :ref:`function<functions>`

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

  and the terminal shows :ref:`AttributeError`

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

* I change it to a :ref:`function<functions>`

  .. code-block:: python

    def none():
        return None


    def false():
        return False

  and the terminal shows green again

* I add a line to test the other :ref:`boolean<Booleans>`

  .. code-block:: python

    def test_type_error_w_non_callables(self):
        src.type_error.none()
        src.type_error.false()
        src.type_error.true()

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'true'

  then I add the name to ``type_error.py`` and point it to :ref:`True<test_what_is_true>`

  .. code-block:: python

    def false():
        return False


    true = True

  which gives me :ref:`TypeError`

  .. code-block:: python

    TypeError: 'bool' object is not callable

* I change it to a :ref:`function<functions>`

  .. code-block:: python

    def false():
        return False


    def true():
        return True

  and the test passes

* I add another line to the test

  .. code-block:: python

    def test_type_error_w_non_callables(self):
        src.type_error.none()
        src.type_error.false()
        src.type_error.true()
        src.type_error.a_list()

  and the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'a_list'

  I add a name to ``type_error.py`` and point it to a :ref:`list<lists>`

  .. code-block:: python

    def true():
        return True


    a_list = [1, 2, 3, 'n']

  and the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'list' object is not callable

* When I make it a :ref:`function<functions>`

  .. code-block:: python

    def true():
        return True


    def a_list():
        return [1, 2, 3, 'n']

  the test passes

* I add a new failing line to the test

  .. code-block:: python

    def test_type_error_w_non_callables(self):
        src.type_error.none()
        src.type_error.false()
        src.type_error.true()
        src.type_error.a_list()
        src.type_error.a_dictionary()

  and get :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'a_dictionary'

  I add the name and point it to a :ref:`dictionary<dictionaries>`

  .. code-block:: python

    def a_list():
        return [1, 2, 3, 'n']


    a_dictionary = {'key': 'value'}

  and the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'dict' object is not callable

* when I change it to a :ref:`function<functions>`

  .. code-block:: python

    def a_list():
        return [1, 2, 3, 'n']


    def a_dictionary():
        return {'key': 'value'}

  the terminal shows green again

----

*********************************************************************************
test_type_error_w_function_signatures
*********************************************************************************

`TypeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError>`_ is also raised when a :ref:`function<functions>` is called in a way that does not match its signature.

* I add a new test

  .. code-block:: python

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00('a')

  and the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'function_00'

  I add the name to ``type_error.py`` as a :ref:`function<functions>`

  .. code-block:: python

    def a_dictionary():
        return {'key': 'value'}


    def function_00():
        return None

  and get :ref:`TypeError`

  .. code-block:: python

   TypeError: function_00() takes 0 positional arguments but 1 was given

  because ``function_00`` is called in a way that is different from its signature or design

* I add an input argument to the :ref:`function<functions>` in ``type_error.py``

  .. code-block:: python

    def function_00(argument):
        return None

  and the terminal shows passing tests

* I add a new failing line

  .. code-block:: python

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00('a')
        src.type_error.function_01('a', 'b')

  the terminal shows

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'function_01'. Did you mean: 'function_00'?

  I add the name to ``type_error.py`` as a :ref:`function<functions>`

  .. code-block:: python

    def function_00(argument):
        return None


    def function_01(argument):
        return None

  and the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: function_01() takes 1 positional argument but 2 were given

* I make the number of inputs in the definition match the number of inputs in the call

  .. code-block:: python

    def function_01(
          argument_1, argument_2
      ):
      return None

  and the test passes

* I add another failing line

  .. code-block:: python

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00('a')
        src.type_error.function_01('a', 'b')
        src.type_error.function_02('a', 'b', 'c')

  the terminal shows

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'function_02'. Did you mean: 'function_00'?

* I add it as a :ref:`function<functions>` to ``type_error.py``

  .. code-block:: python

    def function_01(
            argument_1, argument_2
        ):
        return None


    def function_02(
            argument_1, argument_2
        ):
        return None

  the terminal shows

  .. code-block:: python

    TypeError: function_02() takes 2 positional arguments but 3 were given

* I make the number of inputs in the signature match the number of inputs given in the call

  .. code-block:: python

    def function_02(
            argument_1, argument_2,
            argument_3
        ):
        return None

  and the terminal shows green again

* I add one more failing line to the test

  .. code-block:: python

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00('a')
        src.type_error.function_01('a', 'b')
        src.type_error.function_02('a', 'b', 'c')
        src.type_error.function_03('a', 'b', 'c', 'd')

  the terminal shows

  .. code-block:: python

    AttributeError: module 'src.type_error' has no attribute 'function_03'. Did you mean: 'function_00'?

* I add the :ref:`function<functions>` to ``type_error.py``

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

  and get :ref:`TypeError`

  .. code-block:: python

    TypeError: function_03() takes 3 positional arguments but 4 were given

* I make the :ref:`function<functions>` take 4 arguments

  .. code-block:: python

    def function_03(
        argument_1, argument_2,
        argument_3, argument_4
    ):
        return None

  and the terminal shows both tests are passing

----

*********************************************************************************
test_type_error_w_function_signatures
*********************************************************************************

`TypeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError>`_ is raised when I try to do operations on objects_ that do not mix

red: make it fail
#################################################################################

I add a new test with a failing line

.. code-block:: python

  def test_type_error_w_types_that_do_not_mix(self):
      'text' + 1

the terminal shows `TypeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError>`_

.. code-block:: python

  TypeError: can only concatenate str (not "int") to str

I cannot add something that is not a string_ to a string_

green: make it pass
#################################################################################

I add the assertRaises_ :ref:`method<functions>`

.. code-block:: python

  def test_type_error_w_types_that_do_not_mix(self):
      with self.assertRaises(TypeError):
          'text' + 1

and the test passes

refactor: make it better
#################################################################################

* I add another line

  .. code-block:: python

    def test_type_error_w_types_that_do_not_mix(self):
        with self.assertRaises(TypeError):
            'text' + 1
        None + 2.3

  which gives me `TypeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError>`_

  .. code-block:: python

    TypeError: unsupported operand type(s) for +: 'NoneType' and 'float'

  I cannot do arithmetic with :ref:`None`, I add assertRaises_ to make the test pass

  .. code-block:: python

    def test_type_error_w_types_that_do_not_mix(self):
        with self.assertRaises(TypeError):
            'text' + 1
        with self.assertRaises(TypeError):
            None + 2.3

* One more example

  .. code-block:: python

    def test_type_error_w_types_that_do_not_mix(self):
        with self.assertRaises(TypeError):
            'text' + 1
        with self.assertRaises(TypeError):
            None + 2.3
        {1, 2, 3, 'n'} - {'key': 'value'}

  and I get `TypeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError>`_

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'set' and 'dict'

  I add assertRaises_

  .. code-block:: python

    def test_type_error_w_types_that_do_not_mix(self):
        with self.assertRaises(TypeError):
            'text' + 1
        with self.assertRaises(TypeError):
            None + 2.3
        with self.assertRaises(TypeError):
            {1, 2, 3, 'n'} - {'key': 'value'}

  and all tests are passing

*********************************************************************************
review
*********************************************************************************

I ran tests for `TypeError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#TypeError>`_ with objects that are not callable, :ref:`function<functions>` signatures and objects_ that do not mix.

----

:doc:`/code/code_type_error`