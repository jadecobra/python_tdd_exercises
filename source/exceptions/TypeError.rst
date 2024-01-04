
TypeError
=========

A `TypeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError>`_ can be raised when a function is called with the wrong number of inputs. This means the function call does not match the function signature.

* A function signature is the definition of the function which determines what inputs it accepts, for example

  .. code-block:: python

    def function(input_1, input_2, input_3, input_N):

  This function signature shows that ``function`` can take in four inputs

* Calling a function is using the function after it has been defined, by referencing the name with parentheses at the end, for example

  .. code-block:: python

    function(1, 2, 3, 4)

  is a call to ``function`` with ``1, 2, 3, 4`` as four inputs


RED: make it fail
-----------------


* I open a new file in the editor and save it as ``test_type_error.py`` in the ``tests`` folder created in :doc:`How to create a Test Driven Development Environment </how_to/create_tdd_environment>` and type the following in the file


  .. code-block:: python

    import unittest
    import functions


    class TestTypeErrors(unittest.TestCase):

        def test_function_signatures_solve_type_errors(self):
            self.assertIsNone(functions.function_a("a"))

  the terminal shows a :doc:`/exceptions/ModuleNotFoundError`

  .. code-block:: python

    import functions
    E  ModuleNotFoundError: No module called 'functions'

* I add it to the list of Exceptions encountered

  .. code-block:: python

      # Exceptions Encountered
      # AssertionError
      # ModuleNotFoundError

GREEN: make it pass
-------------------

* I have a lot of practice solving this error from :doc:`/exceptions/ModuleNotFoundError`. I create a file called ``functions.py`` and the terminal shows

  .. code-block:: python

    >    self.assertIsNone(functions.function_a("a"))
    E    AttributeError: module 'functions' has no attribute 'function_a'

  which I add to the list of Exceptions encountered

  .. code-block:: python

      # Exceptions Encountered
      # AssertionError
      # ModuleNotFoundError
      # AttributeError

* I add a name to ``functions.py``

  .. code-block:: python

    function_a = None

  the terminal shows

  .. code-block:: python

   >    self.assertIsNone(functions.function_a("a"))
   E    TypeError: 'NoneType' object is not callable

  A reminder of the first encounter with ``TypeError`` from `How to solve the AttributeError by defining a Function <./AttributeError.rst>`_
* I add it to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError

* I solve this ``TypeError`` by definining a ``callable``, in this case a function.

  .. code-block:: python

    def function_a():
        return None

  the terminal shows

  .. code-block:: python

    >    self.assertIsNone(functions.function_a("a"))
    E    TypeError: function_a() takes 0 positional arguments but 1 was given

  Another ``TypeError`` but with a new message. Reading the error from the bottom up

  * ``function_a() takes 0 positional arguments but 1 was given`` there was an expectation which was not met in how the function is called, it violates the defined signature
  * ``self.assertIsNone(functions.function_a("a"))`` I am checking if the call ``functions.function_a("a")`` is equal to :doc:`None </data_structures/none>`
  * ``functions.function_a("a")`` is the call. I think of it like an address

    - ``functions`` refers to ``functions.py`` which is a python module
    - ``function_a`` refers to the name ``function_a`` defined in ``functions.py``
    - ``()`` is how a function is called after it is defined
    - ``"a"`` is the value passed to ``function_a`` as input

  Imagine you have a telephone, it has a call function but to make a call you must provide a number then hit dial

  - ``call`` is like ``function_a``
  - the number you provide is like ``"a"``
  - hitting dial is like ``()``

  This is covered in more depth in :doc:`/functions/functions`


* I change ``function_a`` in ``functions.py``

  .. code-block:: python

    def function_a(data):
        return None

the terminal shows passing tests. BOOM!

REFACTOR: make it better
------------------------

There's not much to do here but add more tests for practice.


* I add a new test to ``test_function_signatures_solve_type_errors`` in ``test_type_error.py``

  .. code-block:: python

    self.assertIsNone(functions.function_b("a", "b"))

  the terminal shows

  .. code-block:: python

    AttributeError: module 'functions' has no attribute 'function_b'

* I add a name to ``functions.py``

  .. code-block:: python

    function_b = None

  the terminal shows

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I change ``function_b`` to a function

  .. code-block:: python

    def function_b():
        return None

  the terminal shows

  .. code-block:: python

   >    self.assertIsNone(functions.function_b("a", "b"))
   E    TypeError: function_b() takes 0 positional arguments but 2 were given

  the offending line ``functions.function_b("a", "b")`` called ``function_b`` with 2 parameters but the definition has the function taking no inputs

* I change ``function_b`` in ``functions.py``

  .. code-block:: python

    def function_b(positional_argument_1):
        return None

  and the terminal shows

  .. code-block:: python

    TypeError: function_b() takes 1 positional argument but 2 were given

  ah, the previous definition accepted no positional arguments, and now allows 1 positional argument but I called it with 2 positional arguments.

* I change ``function_b`` in ``functions.py`` to take in 2 positional arguments

  .. code-block:: python

    def function_b(positional_argument_1, positional_argument_2):
        return None

  the terminal shows all tests pass.
* Is there another solution to the above test? Can I define a function that takes in any number of parameters? see :doc:`/functions/functions`

More Tests
----------

RED: make it fail
~~~~~~~~~~~~~~~~~

I add a failing test to ``TestTypeErrors`` in ``test_type_error.py``

.. code-block:: python

  self.assertIsNone(functions.function_c("a", "b", "c"))

the terminal shows

.. code-block:: python

  AttributeError: module 'functions' has no attribute 'function_c'

GREEN: make it pass
~~~~~~~~~~~~~~~~~~~

* I add a name to ``functions.py``

  .. code-block:: python

    function_c = None

  the terminal shows

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I change ``function_c`` a function

  .. code-block:: python

    def function_c():
        return None

  the terminal shows

  .. code-block:: python

    TypeError: function_c() takes 0 positional arguments but 3 were given

* I change the function signature of ``function_c`` to accept one input argument

  .. code-block:: python

    def function_c(arg1):
        return None

  the terminal shows

  .. code-block:: python

    TypeError: function_c() takes 1 positional argument but 3 were given

* I change ``function_c`` in ``functions.py`` to take in another argument

  .. code-block:: python

    def function_c(arg1, arg2):
        return None

  the terminal shows

  .. code-block:: python

    TypeError: function_c() takes 2 positional arguments but 3 were given

* I change ``function_c`` in ``functions.py`` to take in one more argument

  .. code-block:: python

    def function_c(arg1, arg2, arg3):
        return None

  and the terminal shows all tests pass

REFACTOR: make it better
~~~~~~~~~~~~~~~~~~~~~~~~

* If you are not bored yet, I add a failing test to ``TestTypeErrors`` in ``test_type_error.py``

  .. code-block:: python

    self.assertIsNone(functions.function_d("a", "b", "c", "d"))

  the terminal shows

  .. code-block:: python

    AttributeError: module 'functions' has no attribute 'function_d'

* I add a name to ``functions.py``

  .. code-block:: python

    function_d = None

  the terminal shows

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I change ``function_d`` in ``functions.py`` to a :doc:`function </functions/functions>`

  .. code-block:: python

    def function_d():
        return None

  the terminal shows

  .. code-block::

    TypeError: function_d() takes 0 positional arguments but 4 were given

* What if I try the solution for the previous test? I change the signature of ``function_d`` in ``functions.py``

  .. code-block:: python

    def function_d(arg1, arg2, arg3):
        return None

  the terminal shows

  .. code-block:: python

    TypeError: function_d() takes 3 positional arguments but 4 were given

* I change ``function_d`` in ``functions.py`` to take 4 arguments

  .. code-block:: python

    def function_d(arg1, arg2, arg3, arg4):
        return None

  the terminal shows all tests pass...but wait! there's more. I can make this better.

* There's another solution to the above test. What if I can define a function that takes in any number of parameters, is there a signature in Python that allows a function to take 1 argument, 4 arguments, or any number of arguments? YES! I can use the starred expression ``*args`` to pass in any number of positional arguments to to ``function_d`` in ``functions.py``

  .. code-block:: python

    def function_d(*args):
        return None

  the terminal shows all tests still pass. FANTASTIC!!

What happens when you do this with ``function_a``, ``function_b``, ``function_c`` and ``function_d``?


You encountered the following exceptions

* :doc:`/exceptions/AssertionError`
* :doc:`/exceptions/ModuleNotFoundError`
* :doc:`/exceptions/AttributeError`
* :doc:`/exceptions/TypeError`

You now know

* How to solve a :doc:`/exceptions/ModuleNotFoundError`
* How to solve an :doc:`/exceptions/AssertionError`
* How to solve an :doc:`/exceptions/AttributeError`
* How to solve a `TypeError <https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#TypeError>`_ by matching function signatures and their calls
