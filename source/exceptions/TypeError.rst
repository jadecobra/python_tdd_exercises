.. include:: ../links.rst

#################################################################################
TypeError
#################################################################################

----

.. contents:: table of contents
  :local:
  :depth: 1

----

`TypeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError>`_ is raised when an object_ is called in a way that is different from its definition. For example when a :ref:`function<functions>` is called in a way that does not match its :ref:`function<functions>` signature.

*********************************************************************************
test_type_error_w_non_callables
*********************************************************************************

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

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_type_error.py:7`` with the mouse to open it in the editor
* then change ``True`` to ``False``
* and change ``test_failure`` to ``test_type_error_w_non_callables``

  .. code-block:: python

    import unittest
    import src.type_error


    class TestTypeErrors(unittest.TestCase):

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

  and the terminal shows 


*********************************************************************************
test_type_error_w_function_signatures
*********************************************************************************

  .. code-block:: python

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00()

* and the terminal shows :ref:`AttributeError`

  .. code-block:: python

    E    AttributeError: module 'functions' has no attribute 'function_00'




* I add a name to ``src.type_error.py``

  .. code-block:: python

    function_00 = None

  the terminal shows

  .. code-block:: python

   E    TypeError: 'NoneType' object is not callable

* I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # TypeError

* then change it to a callable_

  .. code-block:: python

    def function_00():
        return None

  and the test passes








  the terminal shows

  .. code-block:: python

    E    TypeError: function_00() takes 0 positional arguments but 1 was given

  same error, different message

  * ``function_00() takes 0 positional arguments but 1 was given`` there was an expectation which was not met in how the ``function_00`` is called, it violates the defined signature
  * ``src.type_error.function_00("a")`` I am checking if the call ``src.type_error.function_00("a")`` is equal to :ref:`None`
  * ``src.type_error.function_00("a")`` is the call. I think of it like an address

    - ``functions`` is to ``src.type_error.py`` which is a Python module
    - ``function_00`` is the name ``function_00`` defined in ``src.type_error.py``
    - ``()`` is how a function is called after it is defined
    - ``"a"`` is the value passed to ``function_00`` as input

  Imagine you have a telephone, it has a call function but to make a call you must provide a number then hit dial

  - ``call`` is like ``function_00``
  - the number you provide is like ``"a"``
  - hitting dial is like ``()``

  This is covered in more depth in :ref:`functions`


* I make ``function_00`` in ``src.type_error.py``

  .. code-block:: python

    def function_00(argument):
        return None

the terminal shows passing tests


There's not much to do here but add assertions for practice.

* I add a new test to ``test_type_error_w_function_signatures`` in ``test_type_error.py``

  .. code-block:: python

    src.type_error.function_01("a", "b")

  the terminal shows

  .. code-block:: python

    AttributeError: module 'functions' has no attribute 'function_01'

* I add a name to ``src.type_error.py``

  .. code-block:: python

    function_01 = None

  the terminal shows

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I make ``function_01`` to a function

  .. code-block:: python

    def function_01():
        return None

  the terminal shows

  .. code-block:: python

   E    TypeError: function_01() takes 0 positional arguments but 2 were given

  the offending line ``src.type_error.function_01("a", "b")`` called ``function_01`` with 2 parameters but the definition has the function taking no inputs

* I make ``function_01`` in ``src.type_error.py``

  .. code-block:: python

    def function_01(positional_argument_1):
        return None

  and the terminal shows

  .. code-block:: python

    TypeError: function_01() takes 1 positional argument but 2 were given

  ah, the previous definition took no positional arguments, and now allows 1 positional argument but I called it with 2 positional arguments.

* I make ``function_01`` in ``src.type_error.py`` to take in 2 positional arguments

  .. code-block:: python

    def function_01(positional_argument_1, positional_argument_2):
        return None

  the terminal shows all tests pass.
* Is there another solution to the above test? Can I define a function that takes in any number of parameters? see :ref:`test_functions_w_positional_arguments`

* I add a failing test to ``TestTypeErrors`` in ``test_type_error.py``

  .. code-block:: python

    src.type_error.function_02("a", "b", "c")

  the terminal shows

  .. code-block:: python

    AttributeError: module 'functions' has no attribute 'function_02'

* I add a name to ``src.type_error.py``

  .. code-block:: python

    function_02 = None

  the terminal shows

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I make ``function_02`` a function

  .. code-block:: python

    def function_02():
        return None

  the terminal shows

  .. code-block:: python

    TypeError: function_02() takes 0 positional arguments but 3 were given

* I make the signature of ``function_02`` take one input argument

  .. code-block:: python

    def function_02(argument_1):
        return None

  the terminal shows

  .. code-block:: python

    TypeError: function_02() takes 1 positional argument but 3 were given

* I make ``function_02`` in ``src.type_error.py`` to take in another argument

  .. code-block:: python

    def function_02(argument_1, argument_2):
        return None

  the terminal shows

  .. code-block:: python

    TypeError: function_02() takes 2 positional arguments but 3 were given

* I make ``function_02`` in ``src.type_error.py`` to take in one more argument

  .. code-block:: python

    def function_02(
        argument_1, argument_2
    ):
        return None

  and the terminal shows all tests pass

* If you are not bored yet, I add a failing test to ``TestTypeErrors`` in ``test_type_error.py``

  .. code-block:: python

    src.type_error.function_03("a", "b", "c", "d")

  the terminal shows

  .. code-block:: python

    AttributeError: module 'functions' has no attribute 'function_03'

* I add a name to ``src.type_error.py``

  .. code-block:: python

    function_03 = None

  the terminal shows

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I make ``function_03`` in ``src.type_error.py`` to a :ref:`function<functions>`

  .. code-block:: python

    def function_03():
        return None

  the terminal shows

  .. code-block::

    TypeError: function_03() takes 0 positional arguments but 4 were given

* What if I try the solution for the previous test? I make the signature of ``function_03`` in ``src.type_error.py``

  .. code-block:: python

    def function_03(
        argument_1, argument_2,
        argument_3
    ):
        return None

  the terminal shows

  .. code-block:: python

    TypeError: function_03() takes 3 positional arguments but 4 were given

* I make ``function_03`` in ``src.type_error.py`` to take 4 arguments

  .. code-block:: python

    def function_03(
        argument_1, argument_2,
        argument_3, argument_4
    ):
        return None

  the terminal shows all tests pass...but wait! there's more. I can make this better.

What happens when you do this with ``function_00``, ``function_01``, ``function_02`` and ``function_03``?


*********************************************************************************
review
*********************************************************************************

I can solve the `TypeError <https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#TypeError>`_ by matching function signatures and their calls

----

:doc:`/code/code_type_error`