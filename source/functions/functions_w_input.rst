.. meta::
  :description: Master Python functions that take input step-by-step using Test-Driven Development (TDD) in the functions project. Learn def with parameters, the identity/passthrough function, positional vs keyword arguments (order independence via names, swap examples like last_input=0 first_input=1), optional/default values, *args and **kwargs plus unpacking (*a_tuple, **a_dict), moving helpers out of tests for cross-calls, and bare assert == / is. See real errors: "NameError: name 'identity' is not defined", "TypeError: ... takes 0 positional arguments but 1 was given", "got an unexpected keyword argument", "SyntaxError: positional argument follows keyword argument", "SyntaxError: duplicate argument", AssertionError on wrong returns or order. Practice constant functions "assert constant() == 'the same thing'", unknown_number_of_arguments(*a_tuple, **a_dictionary) == (tuple, dict), uv run pytest-watcher, red green refactor. Builds directly on the prior functions chapter. Part of Jacob Itegboje's Pumping Python TDD series for beginners.
  :keywords: Jacob Itegboje, Pumping Python, Python functions that take input, TDD functions with parameters, positional vs keyword arguments, keyword arguments order independence, identity function return the_input, *args **kwargs unpacking, optional default arguments, bare assert in tests, "NameError: name 'identity' is not defined", "TypeError: takes 0 positional arguments but 1 was given", "got an unexpected keyword argument", "SyntaxError: positional argument follows keyword argument", constant function "the same thing", swap last_input first_input, functions red green refactor, uv run pytest-watcher functions, test_identity_function, test_positional_arguments, test_keyword_arguments, test_args_and_kwargs, test_optional_arguments, test_unknown_number_of_arguments, argument unpacking python

.. include:: ../links.rst

.. _argument: https://docs.python.org/3/glossary.html#term-argument
.. _arguments: argument_
.. _keyword argument: arguments_
.. _keyword arguments: arguments_
.. _positional arguments: arguments_

#################################################################################
functions that take input
#################################################################################

A :ref:`function<what is a function?>` is code that is callable_, which means I can write code to do something one time, and call the name for it to do that thing at a different time from when I write it.

:ref:`functions<what is a function?>` can make code simpler, easier to read, test, reuse, maintain and improve - all the good things.

Part of `Computer Programming`_ is sending :ref:`input data<basic objects>` to a process and getting :ref:`output data<basic objects>` back

.. code-block:: python

    input_object -> process -> output_object

where ``process`` is the :ref:`function<what is a function?>`. I think of it like mapping a function ``f`` in Mathematics_ with inputs ``x`` and output ``y``

A :ref:`function<what is a function?>` does something (the process) with ``input_object`` and returns ``output_object`` as the result. For example

.. code-block:: python

                    f(x) -> y
  function(input_object) -> output_object
   solar_panel(sunlight) -> electricity
      factory(materials) -> product
       chef(ingredients) -> food
           stomach(food) -> poop


----

*********************************************************************************
how to make a function that takes input
*********************************************************************************

:ref:`functions<what is a function?>` that take input are made with

* the def_ keyword
* a name
* parentheses with the inputs allowed
* a colon after the parentheses
* the code that makes up the :ref:`function<what is a function?>` (its body) comes after the colon
* a :ref:`return statement<the return statement>`

.. code-block:: python

  def name_of_function(input_object):
      the body of the function
      return output_object

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/functions/tests/test_functions_w_input.py
  :language: python
  :linenos:
  :caption: functions/tests/test_functions.py
  :lines: 1-20

.. literalinclude:: ../code/functions/tests/test_functions_w_input.py
  :language: python
  :lineno-start: 23
  :caption: functions/tests/test_functions.py
  :lines: 23-42

.. literalinclude:: ../code/functions/tests/test_functions_w_input.py
  :language: python
  :lineno-start: 45
  :caption: functions/tests/test_functions.py
  :lines: 45-66

.. literalinclude:: ../code/functions/tests/test_functions_w_input.py
  :language: python
  :lineno-start: 69
  :caption: functions/tests/test_functions.py
  :lines: 69-103

.. literalinclude:: ../code/functions/tests/test_functions_w_input.py
  :language: python
  :lineno-start: 106
  :caption: functions/tests/test_functions.py
  :lines: 106-151

.. literalinclude:: ../code/functions/tests/test_functions_w_input.py
  :language: python
  :lineno-start: 154
  :caption: functions/tests/test_functions.py
  :lines: 154-165

.. literalinclude:: ../code/functions/tests/test_functions_w_input.py
  :language: python
  :lineno-start: 168
  :caption: functions/tests/test_functions.py
  :lines: 168-205

.. literalinclude:: ../code/functions/tests/test_functions_w_input.py
  :language: python
  :lineno-start: 208
  :caption: functions/tests/test_functions.py
  :lines: 208-

*********************************************************************************
questions about functions that take input
*********************************************************************************

* :ref:`how can I make a function take input?<how to make a function that takes input>`
* :ref:`how can I use a function to remove repetition?<test_why_use_a_function>`
* :ref:`how can I call a function with input?<how to call a function with input>`
* :ref:`what is the identity function?<test_identity_function>`
* :ref:`what is a positional argument?<test_positional_arguments>`
* :ref:`what is a keyword argument?<test_keyword_arguments>`
* :ref:`how can I make arguments a choice in a function?<test_optional_arguments>`
* :ref:`how can I make a function take any number of positional arguments?<test_unknown_number_of_arguments>`
* :ref:`how can I make a function take any number of keyword arguments?<test_unknown_number_of_arguments>`
* :ref:`what can I do with single starred expressions?<single starred expressions>`
* :ref:`what can I do with double starred expressions?<double starred expressions>`
* :ref:`how does Python read starred expressions?<how Python treats starred expressions>`
* :ref:`how does Python read double starred expressions?<how Python treats double starred expressions>`

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd functions

  the terminal_ shows I am in the ``functions`` folder_

  .. code-block:: python

    .../pumping_python/functions

* I open ``test_functions.py`` from the ``tests`` folder_

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    test_functions.py .....                             [100%]

    =================== 5 passed in X.YZs ====================

----

*********************************************************************************
test_identity_function
*********************************************************************************

A :ref:`function<what is a function?>` can take input and it :ref:`returns None by default<test_making_a_function_w_return_none>`. The :ref:`Identity or Passthrough function<test_logical_identity>` returns the input it gets as output.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 30
  :emphasize-lines: 8-9

  def test_constant_function():
      def constant():
          return 'the same thing'

      assert constant() == 'the same thing'


  def test_identity_function():
      assert identity() == None


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

.. code-block:: python

  NameError: name 'identity' is not defined

is it because ``test_functions.py`` has no ``identity``?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` for ``identity``

.. code-block:: python
  :lineno-start: 37
  :emphasize-lines: 2-3

  def test_identity_function():
      def identity():
          return None

      assert identity() == None


  # Exceptions seen

the test passes because I get :ref:`None<what is None?>` when I :ref:`call<how to call a function with input>` ``identity``

.. code-block:: shell

  identity() -> None
  └── def identity():
      └── return None

----

*********************************************************************************
how to call a function with input
*********************************************************************************

I can call a :ref:`function<what is a function?>` with input by placing an :ref:`object<everything is an object>` in parentheses (``()``) when I use the name after it is defined.

.. code-block:: python

  name_of_function(input_object)

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add input to the :ref:`function call<how to call a function>`

.. code-block:: python
  :lineno-start: 37
  :emphasize-lines: 5-6

  def test_identity_function():
      def identity():
          return None

      # assert identity() == None
      assert identity(None) == None


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError:
      test_identity_function.<locals>.identity()
      takes 0 positional arguments but 1 was given

because

- the :ref:`call<how to call a function>` to ``identity`` which belongs to :ref:`test_identity_function` uses one input (:ref:`None<what is None?>`).
- The :ref:`function definition (signature)<how to make a function that takes input>` of ``identity`` does not allow any inputs when it is called, since the parentheses are empty.
- :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a name in parentheses for the ``identity`` :ref:`function<what is a function?>` to take input

.. code-block:: python
  :lineno-start: 37
  :emphasize-lines: 2-3

  def test_identity_function():
      # def identity():
      def identity(the_input):
          return None

      # assert identity() == None
      assert identity(None) == None


  # Exceptions seen

the test passes. I am genius.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

The description for the :ref:`identity function<test_logical_identity>` is that it returns the same thing it is given, this test passes when :ref:`None<what is None?>` is given as input.

Does it pass when another value is given or does it always return :ref:`None<what is None?>`? There is one way to find out

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_identity_function` in

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 6-8

    def test_identity_function():
        # def identity():
        def identity(the_input):
            return None

        # assert identity() == None
        assert identity(None) == None
        assert identity(object) == object


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None == object

  - looks like I am not all the way genius, yet. When I :ref:`call<how to call a function with input>` ``identity`` it returns :ref:`None<what is None?>`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

    .. code-block:: python

      assert identity(object) == object
      assert None             == object

    I get :ref:`AssertionError<what causes AssertionError?>` since :ref:`None is only equal to None<what is None?>`.

  - :ref:`object<everything is an object>` is the mother of everything in Python_ - :ref:`everything in Python is an object (they inherit from it)<everything is an object>`.



* I make the ``identity`` :ref:`function<what is a function?>` return what it gets

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4-5

    def test_identity_function():
        # def identity():
        def identity(the_input):
            # return None
            return the_input

        # assert identity() == None
        assert identity(None) == None
        assert identity(object) == object


    # Exceptions seen

  the test passes.

  .. code-block:: shell

    identity(None  ) -> None
    └── def identity(the_input):
        ├── the_input = None
        └── return the_input

  .. code-block:: shell

    identity(object) -> object
    └── def identity(the_input):
        ├── the_input = object
        └── return the_input

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 37

    def test_identity_function():
        def identity(the_input):
            return the_input

        assert identity(None) == None
        assert identity(object) == object


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_identity_function'

  the terminal_ shows a summary of the changes then goes back to the command line.


I sometimes use the :ref:`Identity Function<test_identity_function>` when I am testing, to check connections. If I can send something (input) and get it back, I can start making changes to see how it affects the output.

:ref:`The Identity Function returns its input as output.<test_identity_function>`

----

*********************************************************************************
test_why_use_a_function
*********************************************************************************

Why would I use a :ref:`function<what is a function?>` when I can just write code to do the thing I want? Let us assume I am writing a program to add up numbers.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 9-10

    def test_identity_function():
        def identity(the_input):
            return the_input

        assert identity(None) == None
        assert identity(object) == object


    def test_why_use_a_function():
        assert 1 + 0 == 0


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (1 + 0) == 0

  because ``1 + 0`` is NOT equal to ``0``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 45
  :emphasize-lines: 2-3

  def test_why_use_a_function():
      # assert 1 + 0 == 0
      assert 1 + 0 == 1


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for ``1 + 1``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        assert 1 + 1 == 1


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (1 + 1) == 1

  because ``1 + 1`` is NOT equal to ``1``.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4-5

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``1 + 2``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 6

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        assert 1 + 2 == 2


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (1 + 2) == 2

  because ``1 + 2`` is NOT equal to ``2``.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 6-7

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``1 + 3``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 8

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        assert 1 + 3 == 3


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (1 + 3) == 3

  because ``1 + 3`` is NOT equal to ``3``.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 8-9

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        # assert 1 + 3 == 3
        assert 1 + 3 == 4


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``1 + 4``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 10

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        # assert 1 + 3 == 3
        assert 1 + 3 == 4
        assert 1 + 4 == 4


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (1 + 4) == 4

  because ``1 + 4`` is NOT equal to ``4``.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 10-11

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        # assert 1 + 3 == 3
        assert 1 + 3 == 4
        # assert 1 + 4 == 4
        assert 1 + 4 == 5


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``1 + 5``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 12

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        # assert 1 + 3 == 3
        assert 1 + 3 == 4
        # assert 1 + 4 == 4
        assert 1 + 4 == 5
        assert 1 + 5 == 5


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (1 + 5) == 5

  because ``1 + 5`` is NOT equal to ``5``.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 12-13

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        # assert 1 + 3 == 3
        assert 1 + 3 == 4
        # assert 1 + 4 == 4
        assert 1 + 4 == 5
        # assert 1 + 5 == 5
        assert 1 + 5 == 6


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``1 + 6``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 14

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        # assert 1 + 3 == 3
        assert 1 + 3 == 4
        # assert 1 + 4 == 4
        assert 1 + 4 == 5
        # assert 1 + 5 == 5
        assert 1 + 5 == 6
        assert 1 + 6 == 6


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (1 + 6) == 6

  because ``1 + 6`` is NOT equal to ``6``.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 14-15

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        # assert 1 + 3 == 3
        assert 1 + 3 == 4
        # assert 1 + 4 == 4
        assert 1 + 4 == 5
        # assert 1 + 5 == 5
        assert 1 + 5 == 6
        # assert 1 + 6 == 6
        assert 1 + 6 == 7


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``1 + 7``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 16

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        # assert 1 + 3 == 3
        assert 1 + 3 == 4
        # assert 1 + 4 == 4
        assert 1 + 4 == 5
        # assert 1 + 5 == 5
        assert 1 + 5 == 6
        # assert 1 + 6 == 6
        assert 1 + 6 == 7
        assert 1 + 7 == 7


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (1 + 7) == 7

  because ``1 + 7`` is NOT equal to ``7``.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 16-17

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        # assert 1 + 3 == 3
        assert 1 + 3 == 4
        # assert 1 + 4 == 4
        assert 1 + 4 == 5
        # assert 1 + 5 == 5
        assert 1 + 5 == 6
        # assert 1 + 6 == 6
        assert 1 + 6 == 7
        # assert 1 + 7 == 7
        assert 1 + 7 == 8


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``1 + 8``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 18

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        # assert 1 + 3 == 3
        assert 1 + 3 == 4
        # assert 1 + 4 == 4
        assert 1 + 4 == 5
        # assert 1 + 5 == 5
        assert 1 + 5 == 6
        # assert 1 + 6 == 6
        assert 1 + 6 == 7
        # assert 1 + 7 == 7
        assert 1 + 7 == 8
        assert 1 + 8 == 8


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (1 + 8) == 8

  because ``1 + 8`` is NOT equal to ``8``.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 18-19

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        # assert 1 + 3 == 3
        assert 1 + 3 == 4
        # assert 1 + 4 == 4
        assert 1 + 4 == 5
        # assert 1 + 5 == 5
        assert 1 + 5 == 6
        # assert 1 + 6 == 6
        assert 1 + 6 == 7
        # assert 1 + 7 == 7
        assert 1 + 7 == 8
        # assert 1 + 8 == 8
        assert 1 + 8 == 9


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``1 + 9``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 20

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        # assert 1 + 3 == 3
        assert 1 + 3 == 4
        # assert 1 + 4 == 4
        assert 1 + 4 == 5
        # assert 1 + 5 == 5
        assert 1 + 5 == 6
        # assert 1 + 6 == 6
        assert 1 + 6 == 7
        # assert 1 + 7 == 7
        assert 1 + 7 == 8
        # assert 1 + 8 == 8
        assert 1 + 8 == 9
        assert 1 + 9 == 9


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (1 + 9) == 9

  because ``1 + 9`` is NOT equal to ``9``.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 20-21

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        assert 1 + 0 == 1
        # assert 1 + 1 == 1
        assert 1 + 1 == 2
        # assert 1 + 2 == 2
        assert 1 + 2 == 3
        # assert 1 + 3 == 3
        assert 1 + 3 == 4
        # assert 1 + 4 == 4
        assert 1 + 4 == 5
        # assert 1 + 5 == 5
        assert 1 + 5 == 6
        # assert 1 + 6 == 6
        assert 1 + 6 == 7
        # assert 1 + 7 == 7
        assert 1 + 7 == 8
        # assert 1 + 8 == 8
        assert 1 + 8 == 9
        # assert 1 + 9 == 9
        assert 1 + 9 == 10


    # Exceptions seen

  the test passes.

* all these :ref:`assertions<what is an assertion?>` test what happens when I add a number to ``1``. If I want to test what happens when I add a number to ``2``, I would have to change ``1`` in 10 places. I change ``1`` to ``2`` for the calculation part of the :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 3-4, 6-7, 9-10, 12-13, 15-16, 18-19, 21-22, 24-25, 27-28, 30-31
    :emphasize-text: 2

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        # assert 1 + 0 == 1
        assert 2 + 0 == 1
        # assert 1 + 1 == 1
        # assert 1 + 1 == 2
        assert 2 + 1 == 2
        # assert 1 + 2 == 2
        # assert 1 + 2 == 3
        assert 2 + 2 == 3
        # assert 1 + 3 == 3
        # assert 1 + 3 == 4
        assert 2 + 3 == 4
        # assert 1 + 4 == 4
        # assert 1 + 4 == 5
        assert 2 + 4 == 5
        # assert 1 + 5 == 5
        # assert 1 + 5 == 6
        assert 2 + 5 == 6
        # assert 1 + 6 == 6
        # assert 1 + 6 == 7
        assert 2 + 6 == 7
        # assert 1 + 7 == 7
        # assert 1 + 7 == 8
        assert 2 + 7 == 8
        # assert 1 + 8 == 8
        # assert 1 + 8 == 9
        assert 2 + 8 == 9
        # assert 1 + 9 == 9
        # assert 1 + 9 == 10
        assert 2 + 9 == 10


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (2 + 0) == 1

* I change the result side of each :ref:`assertion<what is an assertion?>` to make them :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4-5, 8-9, 12-13, 16-17, 20-21, 24-25, 28-29, 32-33, 36-37, 40-41

    def test_why_use_a_function():
        # assert 1 + 0 == 0
        # assert 1 + 0 == 1
        # assert 2 + 0 == 1
        assert 2 + 0 == 2
        # assert 1 + 1 == 1
        # assert 1 + 1 == 2
        # assert 2 + 1 == 2
        assert 2 + 1 == 3
        # assert 1 + 2 == 2
        # assert 1 + 2 == 3
        # assert 2 + 2 == 3
        assert 2 + 2 == 4
        # assert 1 + 3 == 3
        # assert 1 + 3 == 4
        # assert 2 + 3 == 4
        assert 2 + 3 == 5
        # assert 1 + 4 == 4
        # assert 1 + 4 == 5
        # assert 2 + 4 == 5
        assert 2 + 4 == 6
        # assert 1 + 5 == 5
        # assert 1 + 5 == 6
        # assert 2 + 5 == 6
        assert 2 + 5 == 7
        # assert 1 + 6 == 6
        # assert 1 + 6 == 7
        # assert 2 + 6 == 7
        assert 2 + 6 == 8
        # assert 1 + 7 == 7
        # assert 1 + 7 == 8
        # assert 2 + 7 == 8
        assert 2 + 7 == 9
        # assert 1 + 8 == 8
        # assert 1 + 8 == 9
        # assert 2 + 8 == 9
        assert 2 + 8 == 10
        # assert 1 + 9 == 9
        # assert 1 + 9 == 10
        # assert 2 + 9 == 10
        assert 2 + 9 == 11


    # Exceptions seen

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_why_use_a_function'

  the terminal_ shows a summary of the changes then goes back to the command line.

* I go back to the terminal_ where the tests are running

-----

* What if I want to test what happens when I add ``3`` to a number? Wait! No more, please! I do not want to have to make a change for each new number, there has to be a better way. I can use a :ref:`function<what is a function?>` for the parts that repeat. I add a :ref:`function<what is a function?>` to :ref:`test_why_use_a_function`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-3

    def test_why_use_a_function():
        def add_x(number):
            return 2 + number

        # assert 1 + 0 == 0
        # assert 1 + 0 == 1
        # assert 2 + 0 == 1
        assert 2 + 0 == 2

* I use the new :ref:`function<what is a function?>` for the calculation in the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 8-9
    :emphasize-text: add_x

    def test_why_use_a_function():
        def add_x(number):
            return 2 + number

        # assert 1 + 0 == 0
        # assert 1 + 0 == 1
        # assert 2 + 0 == 1
        # assert 2 + 0 == 2
        assert add_x(0) == 2
        # assert 1 + 1 == 1
        # assert 1 + 1 == 2
        # assert 2 + 1 == 2
        assert 2 + 1 == 3

  the test is still green because when I :ref:`call<how to call a function with input>` ``add_x`` with a number as input, it returns ``2`` plus the number as output.

  .. code-block:: shell

    add_x(number) -> 2 + number
    └── def add_x(number):
        └── return 2 + number

  When ``add_x(0)`` runs

  .. code-block:: shell

    add_x(0) -> 2
    └── def add_x(number):
        ├── number = 0
        └── return 2 + number
            return 2 + 0
            return 2

  Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assert add_x(0) == 2
    assert 2        == 2

  ``2 + 0`` is equal to ``2``.

* I use the ``add_x`` :ref:`function<what is a function?>` for the other :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 13-14, 18-19, 23-24, 28-29, 33-34, 38-39, 43-44, 48-49, 53-54
    :emphasize-text: add_x

    def test_why_use_a_function():
        def add_x(number):
            return 2 + number

        # assert 1 + 0 == 0
        # assert 1 + 0 == 1
        # assert 2 + 0 == 1
        # assert 2 + 0 == 2
        assert add_x(0) == 2
        # assert 1 + 1 == 1
        # assert 1 + 1 == 2
        # assert 2 + 1 == 2
        # assert 2 + 1 == 3
        assert add_x(1) == 3
        # assert 1 + 2 == 2
        # assert 1 + 2 == 3
        # assert 2 + 2 == 3
        # assert 2 + 2 == 4
        assert add_x(2) == 4
        # assert 1 + 3 == 3
        # assert 1 + 3 == 4
        # assert 2 + 3 == 4
        # assert 2 + 3 == 5
        assert add_x(3) == 5
        # assert 1 + 4 == 4
        # assert 1 + 4 == 5
        # assert 2 + 4 == 5
        # assert 2 + 4 == 6
        assert add_x(4) == 6
        # assert 1 + 5 == 5
        # assert 1 + 5 == 6
        # assert 2 + 5 == 6
        # assert 2 + 5 == 7
        assert add_x(5) == 7
        # assert 1 + 6 == 6
        # assert 1 + 6 == 7
        # assert 2 + 6 == 7
        # assert 2 + 6 == 8
        assert add_x(6) == 8
        # assert 1 + 7 == 7
        # assert 1 + 7 == 8
        # assert 2 + 7 == 8
        # assert 2 + 7 == 9
        assert add_x(7) == 9
        # assert 1 + 8 == 8
        # assert 1 + 8 == 9
        # assert 2 + 8 == 9
        # assert 2 + 8 == 10
        assert add_x(8) == 10
        # assert 1 + 9 == 9
        # assert 1 + 9 == 10
        # assert 2 + 9 == 10
        # assert 2 + 9 == 11
        assert add_x(9) == 11


    # Exceptions seen

  still green.

* Now I only have to make a change in one place if I want to test what happens if I add ``3`` to a number

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 3-4

    def test_why_use_a_function():
        def add_x(number):
            # return 2 + number
            return 3 + number

        # assert 1 + 0 == 0
        # assert 1 + 0 == 1
        # assert 2 + 0 == 1
        # assert 2 + 0 == 2
        assert add_x(0) == 2

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 3 == 2

  because

  .. code-block:: shell

    add_x(number) -> 3 + number
    └── def add_x(number):
        └── return 3 + number

* I change the results part of the :ref:`assertions<what is an assertion?>` one at a time

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 10-11, 16-17, 22-23, 28-29, 34-35, 40-41, 46-47, 52-53, 58-59, 64-65

    def test_why_use_a_function():
        def add_x(number):
            # return 2 + number
            return 3 + number

        # assert 1 + 0 == 0
        # assert 1 + 0 == 1
        # assert 2 + 0 == 1
        # assert 2 + 0 == 2
        # assert add_x(0) == 2
        assert add_x(0) == 3
        # assert 1 + 1 == 1
        # assert 1 + 1 == 2
        # assert 2 + 1 == 2
        # assert 2 + 1 == 3
        # assert add_x(1) == 3
        assert add_x(1) == 4
        # assert 1 + 2 == 2
        # assert 1 + 2 == 3
        # assert 2 + 2 == 3
        # assert 2 + 2 == 4
        # assert add_x(2) == 4
        assert add_x(2) == 5
        # assert 1 + 3 == 3
        # assert 1 + 3 == 4
        # assert 2 + 3 == 4
        # assert 2 + 3 == 5
        # assert add_x(3) == 5
        assert add_x(3) == 6
        # assert 1 + 4 == 4
        # assert 1 + 4 == 5
        # assert 2 + 4 == 5
        # assert 2 + 4 == 6
        # assert add_x(4) == 6
        assert add_x(4) == 7
        # assert 1 + 5 == 5
        # assert 1 + 5 == 6
        # assert 2 + 5 == 6
        # assert 2 + 5 == 7
        # assert add_x(5) == 7
        assert add_x(5) == 8
        # assert 1 + 6 == 6
        # assert 1 + 6 == 7
        # assert 2 + 6 == 7
        # assert 2 + 6 == 8
        # assert add_x(6) == 8
        assert add_x(6) == 9
        # assert 1 + 7 == 7
        # assert 1 + 7 == 8
        # assert 2 + 7 == 8
        # assert 2 + 7 == 9
        # assert add_x(7) == 9
        assert add_x(7) == 10
        # assert 1 + 8 == 8
        # assert 1 + 8 == 9
        # assert 2 + 8 == 9
        # assert 2 + 8 == 10
        # assert add_x(8) == 10
        assert add_x(8) == 11
        # assert 1 + 9 == 9
        # assert 1 + 9 == 10
        # assert 2 + 9 == 10
        # assert 2 + 9 == 11
        # assert add_x(9) == 11
        assert add_x(9) == 12


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 45

    def test_why_use_a_function():
        def add_x(number):
            return 3 + number

        assert add_x(0) == 3
        assert add_x(1) == 4
        assert add_x(2) == 5
        assert add_x(3) == 6
        assert add_x(4) == 7
        assert add_x(5) == 8
        assert add_x(6) == 9
        assert add_x(7) == 10
        assert add_x(8) == 11
        assert add_x(9) == 12


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'extract add_x function'

  the terminal_ shows a summary of the changes then goes back to the command line.

* :ref:`I can use a function to organize tests<a better way to organize tests>`
* :ref:`I can use a function to remove repetition<test_why_use_a_function>`.
* Is there :ref:`a better way to handle the changing results?<a better way to handle the results changing>`

:ref:`test_identity_function` used one input, these next tests use :ref:`functions<what is a function?>` that take more than one input.

----

*********************************************************************************
test_positional_arguments
*********************************************************************************

:ref:`I can call functions with positional arguments<test_positional_arguments>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 4-5

        assert add_x(9) == 12


    def test_positional_arguments():
        assert positional_arguments() == None


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'positional_arguments' is not defined

  because ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the :ref:`function<what is a function?>`

.. code-block:: python
  :lineno-start: 61
  :emphasize-lines: 2-3

  def test_positional_arguments():
      def positional_arguments():
          return None

      assert positional_arguments() == None


  # Exceptions seen

the test passes.

.. code-block:: shell

  positional_arguments() -> None
  └── def positional_arguments():
      └── return None

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add input to the :ref:`function call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 5-6

    def test_positional_arguments():
        def positional_arguments():
            return None

        # assert positional_arguments() == None
        assert positional_arguments('first') == None


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_positional_arguments.<locals>.positional_arguments()
        takes 0 positional arguments but 1 was given

  because

  - the :ref:`call<how to call a function>` to ``positional_arguments`` which belongs to :ref:`test_positional_arguments` uses one input (``'first'``).
  - the :ref:`function definition (signature)<how to make a function that takes input>` of ``positional_arguments`` does not allow any inputs when it is called since the parentheses are empty.
  - :ref:`the call to a function must match its signature (definition)<what causes TypeError?>`.

* I add a name in parentheses to make the :ref:`function<what is a function?>` take input

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2-3

    def test_positional_arguments():
        # def positional_arguments():
        def positional_arguments(the_input):
            return None

        # assert positional_arguments() == None
        assert positional_arguments('first') == None


    # Exceptions seen

  the test passes because

  .. code-block:: shell

    positional_arguments(the_input) -> None
    └── def positional_arguments(the_input):
        └── return None

* I add another input to the :ref:`function call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 7-8

    def test_positional_arguments():
        # def positional_arguments():
        def positional_arguments(the_input):
            return None

        # assert positional_arguments() == None
        # assert positional_arguments('first') == None
        assert positional_arguments('first', 'last') == None


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_positional_arguments.<locals>.positional_arguments()
        takes 1 positional arguments but 2 was given

  because

  - the :ref:`call<how to call a function>` to ``positional_arguments`` which belongs to :ref:`test_positional_arguments` uses two inputs(``'first'` and ``'last'``).
  - the :ref:`function definition (signature)<how to make a function that takes input>` of ``positional_arguments`` only allows one input.
  - :ref:`the call to a function must match its signature (definition)<what causes TypeError?>`.

* I make the :ref:`function<what is a function?>` take two inputs by changing the name of the first input to be clearer, then I add a another name to the parentheses

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 3-4

    def test_positional_arguments():
        # def positional_arguments():
        # def positional_arguments(the_input):
        def positional_arguments(first_input, last_input):
            return None

        # assert positional_arguments() == None
        # assert positional_arguments('first') == None
        assert positional_arguments('first', 'last') == None


    # Exceptions seen

  the test passes.

* I change the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 9-13

    def test_positional_arguments():
        # def positional_arguments():
        # def positional_arguments(the_input):
        def positional_arguments(first_input, last_input):
            return None

        # assert positional_arguments() == None
        # assert positional_arguments('first') == None
        # assert positional_arguments('first', 'last') == None
        assert (
            positional_arguments('first', 'last')
         == ('first', 'last')
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == ('first', 'last')

  because when I :ref:`call<how to call a function with input>` ``positional_arguments`` with ``'first'`` and ``'last'`` as inputs, it returns :ref:`None<what is None?>`

  .. code-block:: shell

    positional_arguments(first_input, last_input) -> None
    └── def positional_arguments(first_input, last_input):
        └── return None

  Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assert positional_arguments('first', 'last') == ('first', 'last')
    assert None                                  == ('first', 'last')

  I get :ref:`AssertionError<what causes AssertionError?>` since :ref:`None<what is None?>` is NOT equal to a tuple_.

* I change :ref:`the return statement` to make the :ref:`function<what is a function?>` return its inputs as output (like :ref:`the identity function<test_identity_function>`)

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 5-6

    def test_positional_arguments():
        # def positional_arguments():
        # def positional_arguments(the_input):
        def positional_arguments(first_input, last_input):
            # return None
            return first_input, last_input

        # assert positional_arguments() == None
        # assert positional_arguments('first') == None
        # assert positional_arguments('first', 'last') == None
        assert (
            positional_arguments('first', 'last')
         == ('first', 'last')
        )


    # Exceptions seen

  the test passes, because the :ref:`function<what is a function?>` always returns ``first_input, last_input`` and the :ref:`call<how to call a function with input>` in the test sends ``'first'`` as ``first_input`` and ``'last'`` as ``last_input``

  When ``positional_arguments('first', 'last')`` runs

  .. code-block:: shell

    positional_arguments('first', 'last') -> ('first', 'last')
    └── def positional_arguments(first_input, last_input)
        ├── first_input = 'first'
        ├── last_input  = 'last'
        └── return first_input, last_input
            return 'first'    , 'last'

* The bad thing about giving arguments this way, is I must use the exact same order in the :ref:`function definition<how to make a function that takes input>` when I make a :ref:`call a function<how to call a function with input>` or I get something different. The good thing about giving arguments this way is I do not need to know the names of the arguments. I add an :ref:`assertion<what is an assertion?>` to show this

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 15-18

    def test_positional_arguments():
        # def positional_arguments():
        # def positional_arguments(the_input):
        def positional_arguments(first_input, last_input):
            # return None
            return first_input, last_input

        # assert positional_arguments() == None
        # assert positional_arguments('first') == None
        # assert positional_arguments('first', 'last') == None
        assert (
            positional_arguments('first', 'last')
         == ('first', 'last')
        )
        assert (
            positional_arguments('last', 'first')
         == ('first', 'last')
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('last', 'first') == ('first', 'last')

  because the :ref:`function<what is a function?>` always returns ``first_input, last_input`` and this test :ref:`calls the function<how to call a function with input>` with ``'last'`` as ``first_input`` and ``'first'`` as ``last_input``.

  When ``positional_arguments('last', 'first')`` runs

  .. code-block:: shell

    positional_arguments('last', 'first') -> ('last', 'first')
    └── def positional_arguments(first_input, last_input)
        ├── first_input = 'last'
        ├── last_input  = 'first'
        └── return first_input, last_input
            return 'last'     , 'first'

  Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assert positional_arguments('last', 'first') == ('first', 'last')
    assert ('last', 'first')                     == ('first', 'last')

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 17-18
    :emphasize-text: last

    def test_positional_arguments():
        # def positional_arguments():
        # def positional_arguments(the_input):
        def positional_arguments(first_input, last_input):
            # return None
            return first_input, last_input

        # assert positional_arguments() == None
        # assert positional_arguments('first') == None
        # assert positional_arguments('first', 'last') == None
        assert (
            positional_arguments('first', 'last')
         == ('first', 'last')
        )
        assert (
            positional_arguments('last', 'first')
        #  == ('first', 'last')
         == ('last', 'first')
        )


    # Exceptions seen

  the test passes.

* I add :ref:`variables<what is a variable?>` for ``'first'`` and ``'last'`` in :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 12

    def test_positional_arguments():
        # def positional_arguments():
        # def positional_arguments(the_input):
        def positional_arguments(first_input, last_input):
            # return None
            return first_input, last_input

        # assert positional_arguments() == None
        # assert positional_arguments('first') == None
        # assert positional_arguments('first', 'last') == None

        first, last = 'first', 'last'

        assert (
            positional_arguments('first', 'last')
         == ('first', 'last')
        )
        assert (
            positional_arguments('last', 'first')
        #  == ('first', 'last')
         == ('last', 'first')
        )


    # Exceptions seen

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``'first'`` and ``'last'`` from :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 15-18, 21, 23-25

    def test_positional_arguments():
        # def positional_arguments():
        # def positional_arguments(the_input):
        def positional_arguments(first_input, last_input):
            # return None
            return first_input, last_input

        # assert positional_arguments() == None
        # assert positional_arguments('first') == None
        # assert positional_arguments('first', 'last') == None

        first, last = 'first', 'last'

        assert (
        #     positional_arguments('first', 'last')
        #  == ('first', 'last')
            positional_arguments(first, last)
         == (first, last)
        )
        assert (
            # positional_arguments('last', 'first')
        #  == ('first', 'last')
        #  == ('last', 'first')
            positional_arguments(last, first)
         == (last, first)
        )


    # Exceptions seen

  the test is still green.

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 9-12

        assert (
            # positional_arguments('last', 'first')
        #  == ('first', 'last')
        #  == ('last', 'first')
            positional_arguments(last, first)
         == (last, first)
        )

        assert (
            positional_arguments(0, 1)
         == (1, 0)
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (0, 1) == (1, 0)

  because the :ref:`function<what is a function?>` always returns ``first_input, last_input`` and this test :ref:`calls the function<how to call a function with input>` with ``0`` as ``first_input`` and ``1`` as ``last_input``.

  Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assert positional_arguments(0, 1) == (1, 0)
    assert (0, 1)                     == (1, 0)

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 3-4

        assert (
            positional_arguments(0, 1)
        #  == (1, 0)
         == (0, 1)
        )


    # Exceptions seen

  the test passes.

  .. code-block:: shell

    positional_arguments(0, 1) -> (0, 1)
    └── def positional_arguments(first_input, last_input)
        ├── first_input = 0
        ├── last_input  = 1
        └── return first_input, last_input
            return 0          , 1

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_positional_arguments` with a tuple_ (anything in parentheses ``( )`` separated by a comma) and a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``)

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 7-12

        assert (
            positional_arguments(0, 1)
        #  == (1, 0)
         == (0, 1)
        )

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert (
            positional_arguments(a_list, a_tuple)
         == (a_tuple, a_list)
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

      AssertionError:
          assert ([1, 2, 3, 'n...0, 1, 2, 'n'))
              == ((1, 2, 3, 'n...0, 1, 2, 'n'])

  because the :ref:`function<what is a function?>` always returns ``first_input, last_input`` and the :ref:`call<how to call a function with input>` in this test sends ``(0, 1, 2, 'n')`` as ``first_input`` and ``[0, 1, 2, 'n']`` as ``last_input``.

  Using substitution

  .. code-block:: python

    assert positional_arguments(a_list, a_tuple)
                            == (a_tuple, a_list)
    assert ([0, 1, 2, 'n'], (0, 1, 2, 'n'))
        == ((0, 1, 2, 'n'), [0, 1, 2, 'n'])

* I change reality to match my expectation

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 4-5

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert (
            # positional_arguments(a_list, a_tuple)
            positional_arguments(a_tuple, a_list)
         == (a_tuple, a_list)
        )


    # Exceptions seen

  the test passes.

  .. code-block:: shell

    ├── a_tuple = (0, 1, 2, 'n')
    ├── a_list = [0, 1, 2, 'n']
    └── positional_arguments(a_tuple, a_list) -> (a_tuple, a_list)
        └── def positional_arguments(first_input, last_input)
            ├── first_input = a_tuple
            ├── last_input  = a_list
            └── return first_input, last_input
                return a_tuple    , a_list

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 61

    def test_positional_arguments():
        def positional_arguments(first_input, last_input):
            return first_input, last_input

        first, last = 'first', 'last'

        assert (
            positional_arguments(first, last)
         == (first, last)
        )
        assert (
            positional_arguments(last, first)
         == (last, first)
        )

        assert (
            positional_arguments(0, 1)
         == (0, 1)
        )

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert (
            positional_arguments(a_tuple, a_list)
         == (a_tuple, a_list)
        )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_positional_arguments'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can call functions with positional arguments<test_positional_arguments>`.


----

*********************************************************************************
extract assert_equal function
*********************************************************************************

The :ref:`assertions<what is an assertion?>` in :ref:`test_positional_arguments`, :ref:`test_why_use_a_function`, :ref:`test_identity_function` and :ref:`test_constant_function` are the same, they check if the result of a :ref:`function call<how to call a function with input>` is equal to something.

.. code-block:: python

  assert function() == something

I can use a :ref:`function<what is a function?>` to :ref:`assert<what is an assertion?>` if two things are equal.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a :ref:`function<what is a function?>` named ``assert_equal`` that takes two inputs and :ref:`asserts<what is an assertion?>` that they are equal

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def assert_equal(input_1, input_2):
        assert input_1 == input_2


    def test_making_a_function_w_pass():

* I use the new :ref:`function<what is a function?>` for the first :ref:`assertion<what is an assertion?>` in :ref:`test_positional_arguments`

  .. code-block::
    :lineno-start: 65
    :emphasize-lines: 7-14

    def test_positional_arguments():
        def positional_arguments(first_input, last_input):
            return first_input, last_input

        first, last = 'first', 'last'

        # assert (
        #     positional_arguments(first, last)
        #  == (first, last)
        # )
        assert_equal(
            positional_arguments(first, last),
            (last, first)
        )
        assert (
            positional_arguments(last, first)
         == (last, first)
        )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('first', 'last') == ('last', 'first')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation to match reality

.. code-block:: python
  :lineno-start: 75
  :emphasize-lines: 3-4

      assert_equal(
          positional_arguments(first, last),
          # (last, first)
          (first, last)
      )
      assert (
          positional_arguments(last, first)
       == (last, first)
      )

the test passes.

.. code-block:: shell

  ├── first = 'first'
  ├── last  = 'last'
  └── assert_equal(
          positional_arguments(first, last),
          (first, last)
      ) -> None
      └── def assert_equal(input_1, input_2):
          ├── input_1 = positional_arguments(first, last)
          │             └── def positional_arguments(
          │                     first_input, last_input
          │                 ):
          │                 ├── first_input = first
          │                 ├── last_input  = last
          │                 └── return first_input, last_input
          │                     return first      , last
          ├── input_2 = (first, last)
          └── assert input_1       == input_2
              assert (first, last) == (first, last)

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use the :ref:`assert_equal function<extract assert_equal function>` for the second :ref:`assertion<what is an assertion?>` in :ref:`test_positional_arguments`

  .. code-block::
    :lineno-start: 80
    :emphasize-lines: 1-8

        # assert (
        #     positional_arguments(last, first)
        #  == (last, first)
        # )
        assert_equal(
            positional_arguments(last, first),
            (first, last)
        )

        assert (
            positional_arguments(0, 1)
         == (0, 1)
        )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('last', 'first') == ('first', 'last')

* I change the expectation to match reality

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 3-4

        assert_equal(
            positional_arguments(last, first),
            # (first, last)
            (last, first)
        )

        assert (
            positional_arguments(0, 1)
         == (0, 1)
        )

  the test passes.

  .. code-block:: shell

    ├── first = 'first'
    ├── last  = 'last'
    └── assert_equal(
            positional_arguments(last, first),
            (last, first)
        ) -> None
        └── def assert_equal(input_1, input_2):
            ├── input_1 = positional_arguments(last, first)
            │             └── def positional_arguments(
            │                     first_input, last_input
            │                 ):
            │                 ├── first_input = last
            │                 ├── last_input  = first
            │                 └── return first_input, last_input
            │                     return last       , first
            ├── input_2 = (last, first)
            └── assert input_1       == input_2
                assert (last, first) == (last, first)

* I :ref:`call the assert_equal function<extract assert_equal function>` for the third :ref:`assertion<what is an assertion?>` in :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 1-7

        # assert (
        #     positional_arguments(0, 1)
        #  == (0, 1)
        # )
        assert_equal(
            positional_arguments(0, 1), (1, 0)
        )

        a_tuple = (0, 1, 2, 'n')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (0, 1) == (1, 0)

* I change the expectation to match reality for the third :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 2-3

        assert_equal(
            # positional_arguments(0, 1), (1, 0)
            positional_arguments(0, 1), (0, 1)
        )

        a_tuple = (0, 1, 2, 'n')

  the test passes.

  .. code-block:: shell

    assert_equal(
        positional_arguments(0, 1),
        (0, 1)
    ) -> None
    └── def assert_equal(input_1, input_2):
        ├── input_1 = positional_arguments(0, 1)
        │             └── def positional_arguments(
        │                     first_input, last_input
        │                 ):
        │                 ├── first_input = 0
        │                 ├── last_input  = 1
        │                 └── return first_input, last_input
        │                     return 0          , 1
        ├── input_2 = (0, 1)
        └── assert input_1 == input_2
            assert (0, 1)  == (0, 1)

* I use the :ref:`assert_equal function<extract assert_equal function>` for the fourth :ref:`assertion<what is an assertion?>` in :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 3-10

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        # assert (
        #     positional_arguments(a_tuple, a_list)
        #  == (a_tuple, a_list)
        # )
        assert_equal(
            positional_arguments(a_list, a_tuple),
            (a_tuple, a_list)
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ([0, 1, 2, 'n...0, 1, 2, 'n'))
                        == ((0, 1, 2, 'n...0, 1, 2, 'n']

* I change the :ref:`call<how to call a function with input>` to ``positional_arguments`` to match the expectation of the fourth :ref:`assertion<what is an assertion?>` in :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 8-9

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        # assert (
        #     positional_arguments(a_tuple, a_list)
        #  == (a_tuple, a_list)
        # )
        assert_equal(
            # positional_arguments(a_list, a_tuple),
            positional_arguments(a_tuple, a_list),
            (a_tuple, a_list)
        )


    # Exceptions seen

  the test passes.

  .. code-block:: shell

    ├── a_tuple = (0, 1, 2, 'n')
    ├── a_list = [0, 1, 2, 'n']
    └── assert_equal(
            positional_arguments(a_tuple, a_list),
            (a_tuple, a_list)
        ) -> None
        └── def assert_equal(input_1, input_2):
            ├── input_1 = positional_arguments(a_tuple, a_list)
            │             └── def positional_arguments(
            │                     first_input, last_input
            │                 ):
            │                 ├── first_input = a_tuple
            │                 ├── last_input  = a_list
            │                 └── return first_input, last_input
            │                     return a_tuple    , a_list
            ├── input_2 = (a_tuple, a_list)
            └── assert input_1            == input_2
                assert (a_tuple, a_list)  == (a_tuple, a_list)

* I remove the commented lines from :ref:`test_positional_arguments`

  .. code-block:: python
    :lineno-start: 65

    def test_positional_arguments():
        def positional_arguments(first_input, last_input):
            return first_input, last_input

        first, last = 'first', 'last'

        assert_equal(
            positional_arguments(first, last),
            (first, last)
        )
        assert_equal(
            positional_arguments(last, first),
            (last, first)
        )

  .. code-block:: python
    :lineno-start: 80

        assert_equal(
            positional_arguments(0, 1), (0, 1)
        )

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert_equal(
            positional_arguments(a_tuple, a_list),
            (a_tuple, a_list)
        )


    # Exceptions

* I use the :ref:`assert_equal function<extract assert_equal function>` for the :ref:`assertions<what is an assertion?>` in :ref:`test_why_use_a_function`

  .. code-block::
    :lineno-start: 49
    :emphasize-lines: 5-25

    def test_why_use_a_function():
        def add_x(number):
            return 3 + number

        # assert add_x(0) == 3
        assert_equal(add_x(0), 2)
        # assert add_x(1) == 4
        assert_equal(add_x(1), 3)
        # assert add_x(2) == 5
        assert_equal(add_x(2), 4)
        # assert add_x(3) == 6
        assert_equal(add_x(3), 5)
        # assert add_x(4) == 7
        assert_equal(add_x(4), 6)
        # assert add_x(5) == 8
        assert_equal(add_x(5), 7)
        # assert add_x(6) == 9
        assert_equal(add_x(6), 8)
        # assert add_x(7) == 10
        assert_equal(add_x(7), 9)
        # assert add_x(8) == 11
        assert_equal(add_x(8), 10)
        # assert add_x(9) == 12
        assert_equal(add_x(9), 11)


    def test_positional_arguments():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 3 == 2

* I change the expectations of the :ref:`assertions<what is an assertion?>` of :ref:`test_why_use_a_function`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 6-7, 9-10, 12-13, 15-16, 18-19, 21-22, 24-25, 27-28, 30-31, 33-34

    def test_why_use_a_function():
        def add_x(number):
            return 3 + number

        # assert add_x(0) == 3
        # assert_equal(add_x(0), 2)
        assert_equal(add_x(0), 3)
        # assert add_x(1) == 4
        # assert_equal(add_x(1), 3)
        assert_equal(add_x(1), 4)
        # assert add_x(2) == 5
        # assert_equal(add_x(2), 4)
        assert_equal(add_x(2), 5)
        # assert add_x(3) == 6
        # assert_equal(add_x(3), 5)
        assert_equal(add_x(3), 6)
        # assert add_x(4) == 7
        # assert_equal(add_x(4), 6)
        assert_equal(add_x(4), 7)
        # assert add_x(5) == 8
        # assert_equal(add_x(5), 7)
        assert_equal(add_x(5), 8)
        # assert add_x(6) == 9
        # assert_equal(add_x(6), 8)
        assert_equal(add_x(6), 9)
        # assert add_x(7) == 10
        # assert_equal(add_x(7), 9)
        assert_equal(add_x(7), 10)
        # assert add_x(8) == 11
        # assert_equal(add_x(8), 10)
        assert_equal(add_x(8), 11)
        # assert add_x(9) == 12
        # assert_equal(add_x(9), 11)
        assert_equal(add_x(9), 12)


    def test_positional_arguments():

  the test passes.

  .. code-block:: shell

    assert_equal(add_x(0), 3) -> None
    └── def assert_equal(input_1, input_2):
        ├── input_1 = add_x(0)
        │             └── def add_x(number):
        │                 ├── number = 0
        │                 └── return 3 + number
        │                     return 3 + 0
        │                     return 3
        ├── input_2 = 3
        └── assert input_1 == input_2
            assert 3       == 3

* I remove the commented lines from :ref:`test_why_use_a_function`

  .. code-block:: python
    :lineno-start: 49

    def test_why_use_a_function():
        def add_x(number):
            return 3 + number

        assert_equal(add_x(0), 3)
        assert_equal(add_x(1), 4)
        assert_equal(add_x(2), 5)
        assert_equal(add_x(3), 6)
        assert_equal(add_x(4), 7)
        assert_equal(add_x(5), 8)
        assert_equal(add_x(6), 9)
        assert_equal(add_x(7), 10)
        assert_equal(add_x(8), 11)
        assert_equal(add_x(9), 12)


    def test_positional_arguments():

* I use the :ref:`assert_equal function<extract assert_equal function>` for the :ref:`assertions<what is an assertion?>` in :ref:`test_identity_function`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 5-8

    def test_identity_function():
        def identity(the_input):
            return the_input

        # assert identity(None) == None
        assert_equal(identity(None), object)
        # assert identity(object) == object
        assert_equal(identity(object), None)


    def test_why_use_a_function():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: assert None == <class 'object'>

* I change the expectation of the first :ref:`assertion<what is an assertion?>` in :ref:`test_identity_function`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 6-7

    def test_identity_function():
        def identity(the_input):
            return the_input

        # assert identity(None) == None
        # assert_equal(identity(None), object)
        assert_equal(identity(None), None)
        # assert identity(object) == object
        assert_equal(identity(object), None)


    def test_why_use_a_function():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: assert <class 'object'> == None

* I change the expectation of the second :ref:`assertion<what is an assertion?>` in :ref:`test_identity_function`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 9-10

    def test_identity_function():
        def identity(the_input):
            return the_input

        # assert identity(None) == None
        # assert_equal(identity(None), object)
        assert_equal(identity(None), None)
        # assert identity(object) == object
        # assert_equal(identity(object), None)
        assert_equal(identity(object), object)


    def test_why_use_a_function():

  the test passes.

  .. code-block:: shell

    assert_equal(identity(object), object) -> None
    └── def assert_equal(input_1, input_2):
        ├── input_1 = identity(object)
        │             └── def identity(the_input):
        │                 ├── the_input = object
        │                 └── return the_input
        │                     return object
        ├── input_2 = object
        └── assert input_1 == input_2
            assert object  == object

* I remove the commented lines from :ref:`test_identity_function`

  .. code-block:: python
    :lineno-start: 41

    def test_identity_function():
        def identity(the_input):
            return the_input

        assert_equal(identity(None), None)
        assert_equal(identity(object), object)


    def test_why_use_a_function():

* I use the :ref:`assert_equal function<extract assert_equal function>` in :ref:`test_constant_function`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 5-6

    def test_constant_function():
        def constant():
            return 'the same thing'

        # assert constant() == 'the same thing'
        assert_equal(constant(), 'not the same thing')


    def test_identity_function():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'the same thing'
                        == 'not the same thing'

* I change the expectation to match reality in :ref:`test_constant_function`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 6-7

    def test_constant_function():
        def constant():
            return 'the same thing'

        # assert constant() == 'the same thing'
        # assert_equal(constant(), 'not the same thing')
        assert_equal(constant(), 'the same thing')


    def test_identity_function():

  the test passes.

  .. code-block:: shell

    assert_equal(constant(), 'the same thing') -> None
    └── def assert_equal(input_1, input_2):
        ├── input_1 = constant()
        │             └── def constant():
        │                 └── return 'the same thing'
        ├── input_2 = 'the same thing'
        └── assert input_1          == input_2
            assert 'the same thing' == 'the same thing'

* I remove the commented lines from :ref:`test_identity_function`

  .. code-block:: python
    :lineno-start: 34

    def test_constant_function():
        def constant():
            return 'the same thing'

        assert_equal(constant(), 'the same thing')


    def test_identity_function():

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'extract assert_equal function'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use a function to assert if two things are equal<extract assert_equal function>`.

----

*********************************************************************************
extract assert_is_none function
*********************************************************************************

The :ref:`assertions<what is an assertion?>` in :ref:`test_what_happens_after_functions_return`, :ref:`test_making_a_function_w_return_none`, :ref:`test_making_a_function_w_return` and :ref:`test_making_a_function_w_pass` are the same, they check if the result of a :ref:`function call<how to call a function with input>` is the same :ref:`object<everything is an object>` as :ref:`None<what is None?>`.

.. code-block:: python

  assert function() is None

I can use a :ref:`function<what is a function?>` to :ref:`assert<what is an assertion?>` if something is :ref:`None<what is None?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a :ref:`function<what is a function?>` named ``assert_is_none`` that takes one input and :ref:`asserts<what is an assertion?>` if the input is :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def assert_equal(input_1, input_2):
        assert input_1 == input_2


    def assert_is_none(something):
        assert something is None


    def test_making_a_function_w_pass():

* I use the new :ref:`function<what is a function?>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_making_a_function_w_pass`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def test_making_a_function_w_pass():
        def w_pass():
            pass

        # assert w_pass() is None
        assert_is_none(w_pass)


    def test_making_a_function_w_return():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    assert <function test_making_a_function_w_pass
                .<locals>.w_pass
            at 0xffffa76b5432>
        is None

  because I just passed the :ref:`function<what is a function?>`, I did not :ref:`call it<how to call a function with input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I :ref:`call<how to call a function with input>` the :ref:`w_pass function<test_making_a_function_w_pass>` in the :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :lineno-start: 9
  :emphasize-lines: 6-7

    def test_making_a_function_w_pass():
        def w_pass():
            pass

        # assert w_pass() is None
        # assert_is_none(w_pass)
        assert_is_none(w_pass())


    def test_making_a_function_w_return():

the test passes.

.. code-block:: shell

  assert_is_none(w_pass()) -> None
  └── def assert_is_none(something):
          ├── something = w_pass()
          │               └── def w_pass():
          │                   └── pass
          │                       return None
          └── assert something is None
              assert None      is None

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_making_a_function_w_pass`

  .. code-block:: python
    :lineno-start: 9

    def test_making_a_function_w_pass():
        def w_pass():
            pass

        assert_is_none(w_pass())


    def test_making_a_function_w_return():

* I use the :ref:`assert_is_none function<extract assert_is_none function>` for the :ref:`assertion<what is an assertion?>` in :ref:`test_making_a_function_w_return`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5-6

    def test_making_a_function_w_return():
        def w_return():
            return

        # assert w_return() is None
        assert_is_none(w_return)


    def test_making_a_function_w_return_none():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    assert <function test_making_a_function_w_return
                .<locals>.w_return
            at 0xffff7e654321>
        is None

* I :ref:`call<how to call a function with input>` the :ref:`w_return function<test_making_a_function_w_return>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 6-7

    def test_making_a_function_w_return():
        def w_return():
            return

        # assert w_return() is None
        # assert_is_none(w_return)
        assert_is_none(w_return())


    def test_making_a_function_w_return_none():

  the test passes.

  .. code-block:: shell

    assert_is_none(w_return()) -> None
    └── def assert_is_none(something):
            ├── something = w_return()
            │               └── def w_return():
            │                   └── return
            │                       return None
            └── assert something is None
                assert None      is None

* I remove the commented lines from :ref:`test_making_a_function_w_return`

  .. code-block:: python
    :lineno-start: 16

    def test_making_a_function_w_return():
        def w_return():
            return

        assert_is_none(w_return())


    def test_making_a_function_w_return_none():

* I use the :ref:`assert_is_none function<extract assert_is_none function>` in :ref:`test_making_a_function_w_return_none`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5-6

    def test_making_a_function_w_return_none():
        def w_return_none():
            return None

        # assert w_return_none() is None
        assert_is_none(w_return_none)


    def test_what_happens_after_functions_return():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    assert <function test_making_a_function_w_return_none
                .<locals>.w_return_none
            at 0xffffa1234567>
          is None

* I :ref:`call<how to call a function with input>` the :ref:`w_return_none function<test_making_a_function_w_return_none>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6-7

    def test_making_a_function_w_return_none():
        def w_return_none():
            return None

        # assert w_return_none() is None
        # assert_is_none(w_return_none)
        assert_is_none(w_return_none())


    def test_what_happens_after_functions_return():

  the test passes.

  .. code-block:: shell

    assert_is_none(w_return_none()) -> None
    └── def assert_is_none(something):
            ├── something = w_return_none()
            │               └── def w_return_none():
            │                   └── return None
            └── assert something is None
                assert None      is None

* I remove the commented lines from :ref:`test_making_a_function_w_return_none`

  .. code-block:: python
    :lineno-start: 23

    def test_making_a_function_w_return_none():
        def w_return_none():
            return None

        assert_is_none(w_return_none())


    def test_what_happens_after_functions_return():

* I use the :ref:`assert_is_none function<extract assert_is_none function>` in :ref:`test_what_happens_after_functions_return`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 6-7

    def test_what_happens_after_functions_return():
        def return_leaves_the_function():
            return None
            return 'only one way for this line to run'

        # assert return_leaves_the_function() is None
        assert_is_none(return_leaves_the_function)


    def test_constant_function():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    assert <function test_what_happens_after_functions_return
                .<locals>.return_leaves_the_function
            at 0xffffa01b2345>
        is None

* I :ref:`call<how to call a function with input>` the :ref:`return_leaves_the_function function<test_what_happens_after_functions_return>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 7-8

    def test_what_happens_after_functions_return():
        def return_leaves_the_function():
            return None
            return 'only one way for this line to run'

        # assert return_leaves_the_function() is None
        # assert_is_none(return_leaves_the_function)
        assert_is_none(return_leaves_the_function())


    def test_constant_function():

  the test passes.

  .. code-block:: shell

    assert_is_none(return_leaves_the_function()) -> None
    └── def assert_is_none(something):
            ├── something = return_leaves_the_function()
            │               └── def return_leaves_the_function():
            │                   └── return None
            └── assert something is None
                assert None      is None

* I remove the commented lines from :ref:`test_what_happens_after_functions_return`

  .. code-block:: python
    :lineno-start: 30

    def test_what_happens_after_functions_return():
        def return_leaves_the_function():
            return None
            return 'only one way for this line to run'

        assert_is_none(return_leaves_the_function())


    def test_constant_function():

* I use the :ref:`assert_is_none function<extract assert_is_none function>` in :ref:`test_identity_function` for the :ref:`assertion<what is an assertion?>` that has :ref:`None<what is None?>` as its expectation

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 5-6

    def test_identity_function():
        def identity(the_input):
            return the_input

        # assert_equal(identity(None), None)
        assert_is_none(identity(object))
        assert_equal(identity(object), object)


    def test_why_use_a_function():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: assert <class 'object'> is None

* I change the input in :ref:`call<how to call a function with input>` to the :ref:`identity function<test_identity_function>` from :ref:`object<everything is an object>` to :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 6-7

    def test_identity_function():
        def identity(the_input):
            return the_input

        # assert_equal(identity(None), None)
        # assert_is_none(identity(object))
        assert_is_none(identity(None))
        assert_equal(identity(object), object)


    def test_why_use_a_function():

  the test passes.

  .. code-block:: shell

    assert_is_none(identity(None)) -> None
    └── def assert_is_none(something):
            ├── something = identity(None)
            │               └── def identity(the_input):
            │                   ├── the_input = None
            │                   └── return the_input
            └── assert something is None
                assert None      is None

* I remove the commented lines from :ref:`test_identity_function`

  .. code-block:: python
    :lineno-start: 45

    def test_identity_function():
        def identity(the_input):
            return the_input

        assert_is_none(identity(None))
        assert_equal(identity(object), object)


    def test_why_use_a_function():

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'extract assert_is_none function'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use a function to assert if something is None<extract assert_is_none function>`.

----

*********************************************************************************
test_keyword_arguments
*********************************************************************************

:ref:`test_positional_arguments` shows that :ref:`positional arguments<test_positional_arguments>` must always be given in the right order which is a problem if I forget the order, especially if there are many inputs.

Another way to :ref:`call a function<how to call a function with input>` is to use `Keyword Arguments`_ to make sure the :ref:`function<what is a function?>` always gets the values for the inputs it expects without worrying about the order.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test for `keyword arguments`_ to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 9-10

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert_equal(
            positional_arguments(a_tuple, a_list),
            (a_tuple, a_list)
        )


    def test_keyword_arguments():
        assert_equal(keyword_arguments(), None)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'keyword_arguments' is not defined

  because there is no definition for ``keyword_arguments`` in this file_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function definition<how to make a function that takes input>`

.. code-block:: python
  :lineno-start: 96
  :emphasize-lines: 2-3

    def test_keyword_arguments():
        def keyword_arguments():
            return None

        assert_equal(keyword_arguments(), None)


    # Exceptions seen

the test passes.

.. code-block:: shell

  keyword_arguments() -> None
  └── def keyword_arguments():
      └── return None

----

*********************************************************************************
what is a keyword argument?
*********************************************************************************

A `keyword argument`_ is a key-value pair that is used to pass input in a :ref:`function call<how to call a function>`. Where key is a name, and the value is any :ref:`object<everything is an object>` the :ref:`function<what is a function?>` accepts.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add input to the :ref:`function call<how to call a function with input>` with a name

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 5-8

    def test_keyword_arguments():
        def keyword_arguments():
            return None

        # assert_equal(keyword_arguments(), None)
        assert_equal(
            keyword_arguments(first_input='first'), None
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_keyword_arguments.<locals>.keyword_arguments()
        got an unexpected keyword argument 'first_input'

  because

  - the :ref:`call<how to call a function>` to ``keyword_arguments`` which belongs to :ref:`test_keyword_arguments` uses a name (``first_input``) and a value for the name (``'first'``).
  - the :ref:`function definition (signature)<how to make a function that takes input>` of ``keyword_arguments`` does not allow any inputs when it is called since the parentheses are empty.
  - :ref:`the call to a function must match its signature (definition)<what causes TypeError?>`.

* I add a name in parentheses to make the :ref:`function<what is a function?>` take input

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 2-3

    def test_keyword_arguments():
        # def keyword_arguments():
        def keyword_arguments(the_input):
            return None

        # assert_equal(keyword_arguments(), None)
        assert_equal(
            keyword_arguments(first_input='first'), None
        )


    # Exceptions seen

  the terminal_ still shows :ref:`TypeError<what causes TypeError?>` because the names in the :ref:`function call<how to call a function with input>` and :ref:`function definition<how to make a function that takes input>` are different.

* I change the name of the input in the :ref:`function definition<how to make a function that takes input>` (``the_input``) to match the name used in the :ref:`function call<how to call a function with input>` (``first_input``)

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 3-4

    def test_keyword_arguments():
        # def keyword_arguments():
        # def keyword_arguments(the_input):
        def keyword_arguments(first_input):
            return None

        # assert_equal(keyword_arguments(), None)
        assert_equal(
            keyword_arguments(first_input='first'), None
        )


    # Exceptions seen

  the test passes because the :ref:`keyword<test_keyword_arguments>` I used to :ref:`call the function<how to call a function with input>` matches the name in the :ref:`function definition<how to make a function that takes input>`.

  .. code-block:: shell

    keyword_arguments(first_input='first') -> None
    └── def keyword_arguments(first_input):
        └── return None

* I add another :ref:`keyword argument<test_keyword_arguments>` to the :ref:`function call<how to call a function with input>` in :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 9-13

    def test_keyword_arguments():
        # def keyword_arguments():
        # def keyword_arguments(the_input):
        def keyword_arguments(first_input):
            return None

        # assert_equal(keyword_arguments(), None)
        assert_equal(
            # keyword_arguments(first_input='first'), None
            keyword_arguments(
                first_input='first', last_input='last',
            ),
            None
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError:
        test_keyword_arguments.<locals>.keyword_arguments()
        got an unexpected keyword argument 'last_input'.
        Did you mean 'first_input'?

  because

  - the :ref:`call<how to call a function>` to ``keyword_arguments`` which belongs to :ref:`test_keyword_arguments` uses two names (``first_input`` and ``last_input``) and values for the names (``'first'`` and ``'last'``).
  - the :ref:`function definition (signature)<how to make a function that takes input>` of ``keyword_arguments`` only allows one input when it is :ref:`called<how to call a function with input>`.
  - :ref:`the call to a function must match its signature (definition)<what causes TypeError?>`.

* I make the :ref:`function<what is a function?>` take two inputs by adding another name in parentheses

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 4-5

    def test_keyword_arguments():
        # def keyword_arguments():
        # def keyword_arguments(the_input):
        # def keyword_arguments(first_input):
        def keyword_arguments(first_input, second_input):
            return None

        # assert_equal(keyword_arguments(), None)
        assert_equal(
            # keyword_arguments(first_input='first'), None
            keyword_arguments(
                first_input='first', last_input='last',
            ),
            None
        )


    # Exceptions seen

  the terminal_ still shows :ref:`TypeError<what causes TypeError?>` because the names in the :ref:`function call<how to call a function with input>` and :ref:`function definition<how to make a function that takes input>` are different.

* I change the name of the input in the :ref:`function definition<how to make a function that takes input>` (``second_input``) to match the name used in the :ref:`function call<how to call a function with input>` (``last_input``)

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 5-6

    def test_keyword_arguments():
        # def keyword_arguments():
        # def keyword_arguments(the_input):
        # def keyword_arguments(first_input):
        # def keyword_arguments(first_input, second_input):
        def keyword_arguments(first_input, last_input):
            return None

        # assert_equal(keyword_arguments(), None)
        assert_equal(
            # keyword_arguments(first_input='first'), None
            keyword_arguments(
                first_input='first', last_input='last',
            ),
            None
        )


    # Exceptions seen

  the test passes because the :ref:`keywords<test_keyword_arguments>` I used to :ref:`call the function<how to call a function with input>` match the names in the :ref:`function definition<how to make a function that takes input>`.

  .. code-block:: shell

    keyword_arguments(
        first_input='first', last_input='last'
    ) -> None
    └── def keyword_arguments(first_input, last_input):
        └── return None

* I change the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 15-16

    def test_keyword_arguments():
        # def keyword_arguments():
        # def keyword_arguments(the_input):
        # def keyword_arguments(first_input):
        # def keyword_arguments(first_input, second_input):
        def keyword_arguments(first_input, last_input):
            return None

        # assert_equal(keyword_arguments(), None)
        assert_equal(
            # keyword_arguments(first_input='first'), None
            keyword_arguments(
                first_input='first', last_input='last',
            ),
            # None
            ('first', 'last')
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == ('first', 'last')

  because when I :ref:`call<how to call a function with input>` ``keyword_arguments`` with ``first_input='first'`` and ``last_input='last'`` as inputs, it returns :ref:`None<what is None?>`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`.

  .. code-block:: shell

    assert_equal(
        keyword_arguments(
            first_input='first', last_input='last',
        ),
        ('first', 'last')
    ) -> None
    └── def assert_equal(input_1, input_2):
        ├── input_1 = keyword_arguments(
        │                 first_input='first', last_input='last',
        │             )
        │             └── def keyword_arguments(
        │                     first_input, last_input
        │                 ):
        │                 └── return None
        ├── input_2 = ('first', 'last')
        └── assert input_1 == input_2
            assert None    == ('first', 'last')

  which raises :ref:`AssertionError<what causes AssertionError?>` since :ref:`None<what is None?>` is NOT equal to a tuple_.

* I change :ref:`the return statement` to make the :ref:`function<what is a function?>` return its inputs as output (like :ref:`the identity function<test_identity_function>`)

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 7-8

    def test_keyword_arguments():
        # def keyword_arguments():
        # def keyword_arguments(the_input):
        # def keyword_arguments(first_input):
        # def keyword_arguments(first_input, second_input):
        def keyword_arguments(first_input, last_input):
            # return None
            return first_input, last_input

        # assert_equal(keyword_arguments(), None)
        assert_equal(
            # keyword_arguments(first_input='first'), None
            keyword_arguments(
                first_input='first', last_input='last',
            ),
            # None
            ('first', 'last')
        )


    # Exceptions seen

  the test passes, because the :ref:`function<what is a function?>` always returns ``first_input, last_input`` and the :ref:`call<how to call a function with input>` in the test sends ``first_input='first'`` and ``last_input='last'``

  .. code-block:: shell

    keyword_arguments(
        first_input='first', last_input='last'
    ) -> ('first', 'last')
    └── def keyword_arguments(first_input, last_input):
        ├── first_input = 'first'
        ├── last_input  = 'last'
        └── return first_input, last_input
            return 'first'    , 'last'

* The bad thing about giving arguments this way, is I must use the exact names in the :ref:`function definition<how to make a function that takes input>` when I make a :ref:`call to the function<how to call a function with input>`. The good thing about giving arguments this way is that the names do not have to match the order in the :ref:`function definition<how to make a function that takes input>`. I add an :ref:`assertion<what is an assertion?>` with the `keyword arguments`_ given out of order

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 10-15

        # assert_equal(keyword_arguments(), None)
        assert_equal(
            # keyword_arguments(first_input='first'), None
            keyword_arguments(
                first_input='first', last_input='last',
            ),
            # None
            ('first', 'last')
        )
        assert_equal(
            keyword_arguments(
                last_input='last', first_input='first',
            ),
            ('last', 'first')
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('first', 'last') == ('last', 'first')

  because the :ref:`function<what is a function?>` always returns ``first_input, last_input`` and this test :ref:`calls the function<how to call a function with input>` with ``'last'`` as ``last_input`` and ``'first'`` as ``first_input``, the order does not matter because I used the names.

  .. code-block:: shell

    assert_equal(
        keyword_arguments(
            last_input='last', first_input='first',
        ),
        ('last', 'first')
    ) -> None
    └── def assert_equal(input_1, input_2):
        ├── input_1 = keyword_arguments(
        │                 last_input='last', first_input='first',
        │             )
        │             └── def keyword_arguments(
        │                     first_input, last_input
        │                 ):
        │                 ├── first_input = 'first'
        │                 ├── last_input  = 'last'
        │                 └── return first_input, last_input
        │                     return 'first'    , 'last'
        ├── input_2 = ('last', 'first')
        └── assert input_1           == input_2
            assert ('first', 'last') == ('last', 'first')

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 14-15

        # assert_equal(keyword_arguments(), None)
        assert_equal(
            # keyword_arguments(first_input='first'), None
            keyword_arguments(
                first_input='first', last_input='last',
            ),
            # None
            ('first', 'last')
        )
        assert_equal(
            keyword_arguments(
                last_input='last', first_input='first',
            ),
            # ('last', 'first')
            ('first', 'last')
        )


    # Exceptions seen

  the test passes.

  .. code-block:: shell

    keyword_arguments(
        last_input='last', first_input='first'
    ) -> ('first', 'last')
    └── def keyword_arguments(first_input, last_input):
        ├── first_input = 'first'
        ├── last_input  = 'last'
        └── return first_input, last_input
            return 'first'    , 'last'

* I add :ref:`variables<what is a variable?>` for ``'first'`` and ``'last'`` in :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 10

    def test_keyword_arguments():
        # def keyword_arguments():
        # def keyword_arguments(the_input):
        # def keyword_arguments(first_input):
        # def keyword_arguments(first_input, second_input):
        def keyword_arguments(first_input, last_input):
            # return None
            return first_input, last_input

        first, last = 'first', 'last'

        # assert_equal(keyword_arguments(), None)

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``'first'`` and ``'last'`` from :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 9-10, 14-15, 18-19

        # assert_equal(keyword_arguments(), None)
        assert_equal(
            # keyword_arguments(first_input='first'), None
            keyword_arguments(
                # first_input='first', last_input='last',
                first_input=first, last_input=last,
            ),
            # None
            # ('first', 'last')
            (first, last)
        )
        assert_equal(
            keyword_arguments(
                # last_input='last', first_input='first',
                last_input=last, first_input=first,
            ),
            # ('last', 'first')
            # ('first', 'last')
            (first, last)
        )


    # Exceptions seen

  the test is still green.

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 11-16

        assert_equal(
            keyword_arguments(
                # last_input='last', first_input='first',
                last_input=last, first_input=first,
            ),
            # ('last', 'first')
            # ('first', 'last')
            (first, last)
        )

        assert_equal(
            keyword_arguments(
                last_input=0, first_input=1,
            ),
            (0, 1)
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert (1, 0) == (0, 1)

  because the :ref:`function<what is a function?>` always returns ``first_input, last_input`` and this test :ref:`calls the function<how to call a function with input>` with ``0`` as ``last_input`` and ``1`` as ``first_input``, the order does not matter because I used the :ref:`names<test_keyword_arguments>`.

  .. code-block:: shell

    assert_equal(
        keyword_arguments(
            last_input=0, first_input=1,
        ),
        (0, 1)
    ) -> None
    └── def assert_equal(input_1, input_2):
        ├── input_1 = keyword_arguments(
        │                 last_input=0, first_input=1,
        │             )
        │             └── def keyword_arguments(
        │                     first_input, last_input
        │                 ):
        │                 ├── first_input = 1
        │                 ├── last_input  = 0
        │                 └── return first_input, last_input
        │                     return 1          , 0
        ├── input_2 = (0, 1)
        └── assert input_1 == input_2
            assert (1, 0)  == (0, 1)

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 15-16

        assert_equal(
            keyword_arguments(
                # last_input='last', first_input='first',
                last_input=last, first_input=first,
            ),
            # ('last', 'first')
            # ('first', 'last')
            (first, last)
        )

        assert_equal(
            keyword_arguments(
                last_input=0, first_input=1,
            ),
            # (0, 1)
            (1, 0)
        )


    # Exceptions seen

  the test passes.

  .. code-block:: shell

    keyword_arguments(
        last_input=0, first_input=1
    ) -> (1, 0)
    def keyword_arguments(first_input, last_input):
    ├── first_input = 1
    ├── last_input  = 0
    └── return first_input, last_input
        return 1          , 0

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_keyword_arguments` with a tuple_ and a :ref:`list<what is a list?>`

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 9-17

        assert_equal(
            keyword_arguments(
                last_input=0, first_input=1,
            ),
            # (0, 1)
            (1, 0)
        )

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert_equal(
            keyword_arguments(
                first_input=a_list,
                last_input=a_tuple,
            ),
            (a_tuple, a_list)
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        assert ([1, 2, 3, 'n...0, 1, 2, 'n'))
            == ((1, 2, 3, 'n...0, 1, 2, 'n'])

  because the :ref:`function<what is a function?>` always returns ``first_input, last_input`` and this test :ref:`calls the function<how to call a function with input>` with ``[0, 1, 2, 'n']`` as ``first_input`` and ``(0, 1, 2, 'n')`` as ``last_input``, the order does not matter because I used the :ref:`names<test_keyword_arguments>`

  .. code-block:: shell

    ├── a_tuple = (0, 1, 2, 'n')
    ├── a_list = [0, 1, 2, 'n']
    └── assert_equal(
            keyword_arguments(
                first_input=a_list, last_input=a_tuple,
            ),
            (a_tuple, a_list)
        ) -> None
        └── def assert_equal(input_1, input_2):
            ├── input_1 = keyword_arguments(
            │                 first_input=a_list,
            │                 last_input=a_tuple,
            │             )
            │             └── def keyword_arguments(
            │                     first_input, last_input
            │                 ):
            │                 ├── first_input = a_list
            │                 ├── last_input  = a_tuple
            │                 └── return first_input, last_input
            │                     return a_list     , a_tuple
            ├── input_2 = (a_tuple, a_list)
            └── assert input_1            == input_2
                assert (a_list, a_tuple)  == (a_tuple, a_list)

* I change reality to match my expectation

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 13-16

        assert_equal(
            keyword_arguments(
                last_input=0, first_input=1,
            ),
            # (0, 1)
            (1, 0)
        )

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert_equal(
            keyword_arguments(
                # first_input=a_list,
                # last_input=a_tuple,
                first_input=a_tuple,
                last_input=a_list,
            ),
            (a_tuple, a_list)
        )


    # Exceptions seen

  the test passes.

  .. code-block:: shell

    ├── a_tuple = (0, 1, 2, 'n')
    ├── a_list = [0, 1, 2, 'n']
    └── keyword_arguments(
            first_input=a_list,
            last_input=a_tuple,
        ) -> (a_tuple, a_list)
        └── def keyword_arguments(first_input, last_input):
            ├── first_input = a_list
            ├── last_input  = a_tuple
            └── return first_input, last_input
                return a_tuple    , a_list

* ``keyword_arguments`` and ``positional_arguments`` are the same :ref:`function<what is a function?>` in ``test_functions.py``, they always

  .. code-block:: python

        return first_input, last_input

  Their names are different

  .. code-block:: python
    :emphasize-text: positional keyword

    def positional_arguments(first_input, last_input):
    def keyword_arguments(first_input, last_input):

  The difference that matters in the tests is how I :ref:`call<how to call a function with input>` them

  - I have to give the input in order when I use :ref:`positional arguments<test_positional_arguments>` because I do NOT use the names from the :ref:`function definition<how to make a function that takes input>` when I :ref:`call<how to call a function with input>` it

    .. code-block:: python
      :emphasize-text: first

      positional_arguments('first', 'last')
                -> return ('first', 'last')

    .. code-block:: python
      :emphasize-text: first

      positional_arguments('last', 'first')
                -> return ('last', 'first')

    .. code-block:: python
      :emphasize-text: first

      positional_arguments(0, 1)
                -> return (0, 1)

    .. code-block:: python
      :emphasize-text: first

      positional_arguments((0, 1, 2, 'n'), [0, 1, 2, 'n'])
                -> return ((0, 1, 2, 'n'), [0, 1, 2, 'n'])

    .. code-block:: python
      :emphasize-text: first

      keyword_arguments('last', 'first')
             -> return ('last', 'first')

  - I can give the input in any order when I use `keyword arguments`_ because I use the names from the :ref:`function definition<how to make a function that takes input>` when I :ref:`call<how to call a function with input>` it

    .. code-block:: python
      :emphasize-text: first

      keyword_arguments(
          first_input='first', last_input='last',
      )
      -> return ('first', 'last')

    .. code-block:: python
      :emphasize-text: first

      keyword_arguments(
          last_input='last', first_input='first',
      )
      -> return ('first', 'last')

    .. code-block:: python
      :emphasize-text: first

      keyword_arguments(last_input=0, first_input=1)
      -> return (1, 0)

    .. code-block:: python
      :emphasize-text: first

      keyword_arguments(
          first_input=(0, 1, 2, 'n'),
          last_input=[0, 1, 2, 'n'],
      )
      -> return ((0, 1, 2, 'n'), [0, 1, 2, 'n'])

  I :ref:`call<how to call a function with input>` the :ref:`positional_arguments function<test_positional_arguments>` with :ref:`keyword arguments<test_keyword_arguments>` to show that the two :ref:`functions<what is a function?>` are the same

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 13-21
    :emphasize-text: positional

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert_equal(
            keyword_arguments(
                # first_input=a_list,
                # last_input=a_tuple,
                first_input=a_tuple,
                last_input=a_list,
            ),
            (a_tuple, a_list)
        )

        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}
        assert_equal(
            positional_arguments(
                last_input=a_dictionary,
                first_input=a_set,
            ),
            (a_set, a_dictionary)
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'positional_arguments' is not defined

  because the :ref:`positional_arguments function<test_positional_arguments>`  belongs to the :ref:`test_positional_arguments function<test_positional_arguments>` and I cannot reach it from outside :ref:`test_positional_arguments`.

* I move the :ref:`positional_arguments function<test_positional_arguments>` out of :ref:`test_positional_arguments` so that it can be :ref:`called<how to call a function with input>` from anywhere in the file_

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 4-5, 9

        assert_equal(add_x(9), 12)


    def positional_arguments(first_input, last_input):
        return first_input, last_input


    def test_positional_arguments():
        first, last = 'first', 'last'

        assert_equal(
            positional_arguments(first, last),
            (first, last)
        )
        assert_equal(
            positional_arguments(last, first),
            (last, first)
        )

        assert_equal(
            positional_arguments(0, 1), (0, 1)
        )

        a_tuple = (0, 1, 2, 'n')

  the test passes because these two :ref:`calls<how to call a function with input>` are the same

  .. code-block:: python

    positional_arguments(
        last_input=a_dictionary,
        first_input=a_set,
    )

    positional_arguments(
        a_set, a_dictionary,
    )

  - When ``positional_arguments(last_input=a_dictionary, first_input=a_set)`` runs

    .. code-block:: shell

      positional_arguments(
          last_input=a_dictionary,
          first_input=a_set,
      ) -> (a_set, a_dictionary)
      └── def positional_arguments(first_input, last_input):
          ├── first_input = a_set
          ├── last_input = a_dictionary
          └── return first_input, last_input
              return a_set      , a_dictionary

  - When ``positional_arguments(a_set, a_dictionary)`` runs

    .. code-block:: shell

      positional_arguments(
          a_set, a_dictionary
      ) -> (a_set, a_dictionary)
      └── def positional_arguments(first_input, last_input):
          ├── first_input = a_set
          ├── last_input = a_dictionary
          └── return first_input, last_input
              return a_set      , a_dictionary

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_positional_arguments` to show that I can :ref:`call<how to call a function with input>` the :ref:`keyword_arguments function<test_keyword_arguments>` with :ref:`positional arguments<test_positional_arguments>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 8-15
    :emphasize-text: keyword

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert_equal(
            positional_arguments(a_tuple, a_list),
            (a_tuple, a_list)
        )

        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}
        assert_equal(
            keyword_arguments(
                a_set, a_dictionary,
            ),
            (a_set, a_dictionary)
        )


    def test_keyword_arguments():

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'keyword_arguments' is not defined

  because the :ref:`keyword_arguments function<test_keyword_arguments>` belongs to the :ref:`test_keyword_arguments function<test_keyword_arguments>` and I cannot reach it from outside :ref:`test_keyword_arguments`, yet.

* I move the :ref:`keyword_arguments function<test_keyword_arguments>` out of :ref:`test_keyword_arguments` so that it can be :ref:`called<how to call a function with input>` from anywhere in the file_

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 11-12

        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}
        assert_equal(
            keyword_arguments(
                a_set, a_dictionary,
            ),
            (a_set, a_dictionary)
        )


    def keyword_arguments(first_input, last_input):
        return first_input, last_input


    def test_keyword_arguments():
        # def keyword_arguments():
        # def keyword_arguments(the_input):
        # def keyword_arguments(first_input):
        # def keyword_arguments(first_input, second_input):
            # return None

  the test passes because these two :ref:`calls<how to call a function with input>` are the same

  .. code-block:: python

    keyword_arguments(
        a_set, a_dictionary,
    )

    keyword_arguments(
        last_input=a_dictionary,
        first_input=a_set,
    )

  - When ``keyword_arguments(a_set, a_dictionary)`` runs

    .. code-block:: shell

      keyword_arguments(
          a_set, a_dictionary
      ) -> (a_set, a_dictionary)
      └── def keyword_arguments(first_input, last_input):
          ├── first_input = a_set
          ├── last_input  = a_dictionary
          └── return first_input, last_input
              return a_set      , a_dictionary

  - When ``keyword_arguments(last_input=a_dictionary, first_input=a_set)`` runs

    .. code-block:: shell

      keyword_arguments(
          last_input=a_dictionary,
          first_input=a_set,
      ) -> (a_set, a_dictionary)
      └── def keyword_arguments(first_input, last_input):
          ├── first_input = a_set
          ├── last_input  = a_dictionary
          └── return first_input, last_input
              return a_set      , a_dictionary

* I remove the commented lines from :ref:`test_keyword_arguments`

  .. code-block:: python
    :lineno-start: 110

    def test_keyword_arguments():
        first, last = 'first', 'last'

        assert_equal(
            keyword_arguments(
                first_input=first, last_input=last,
            ),
            (first, last)
        )
        assert_equal(
            keyword_arguments(
                last_input=last, first_input=first,
            ),
            (first, last)
        )

  .. code-block:: python
    :lineno-start: 126

        assert_equal(
            keyword_arguments(
                last_input=0, first_input=1,
            ),
            (1, 0)
        )

  .. code-block:: python
    :lineno-start: 133

        a_tuple = (0, 1, 2, 'n')
        a_list = [0, 1, 2, 'n']
        assert_equal(
            keyword_arguments(
                first_input=a_tuple,
                last_input=a_list,
            ),
            (a_tuple, a_list)
        )

  .. code-block:: python
    :lineno-start: 143

        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}
        assert_equal(
            positional_arguments(
                last_input=a_dictionary,
                first_input=a_set,
            ),
            (a_set, a_dictionary)
        )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_keyword_arguments'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can call a function with keyword arguments<test_keyword_arguments>`.

----

*********************************************************************************
test_args_and_kwargs
*********************************************************************************

Can I :ref:`call a function<how to call a function with input>` with both :ref:`positional<test_positional_arguments>` and :ref:`keyword arguments<test_keyword_arguments>`?

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 12-18
    :emphasize-text: first

        a_set = {0, 1, 2, 'n'}
        a_dictionary = {'key': 'value'}
        assert_equal(
            positional_arguments(
                last_input=a_dictionary,
                first_input=a_set,
            ),
            (a_set, a_dictionary)
        )


    def test_args_and_kwargs():
        assert_equal(
            args_and_kwargs(
                last_input='last', 'first',
            ),
            ('first', 'last')
        )


    # Exceptions seen

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: positional argument follows keyword argument

  because I cannot put :ref:`keyword arguments<test_keyword_arguments>` before :ref:`positional arguments<test_positional_arguments>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add SyntaxError_ to the list of :ref:`Exceptions<how to test that an Exception is raised>` seen, in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 163
    :emphasize-lines: 5
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # SyntaxError

* I change the order of the arguments to follow Python_ rules

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 4-5
    :emphasize-text: first

    def test_args_and_kwargs():
        assert_equal(
            args_and_kwargs(
                # last_input='last', 'first',
                'first', last_input='last'
            ),
            ('first', 'last')
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'args_and_kwargs' is not defined

  because I have not given a definition for the name yet.

* I add a :ref:`function definition<how to make a function that takes input>` for ``args_and_kwargs``

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 2-3

    def test_args_and_kwargs():
        def args_and_kwargs():
            return None

        assert_equal(
            args_and_kwargs(
                # last_input='last', 'first',
                'first', last_input='last'
            ),
            ('first', 'last')
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_args_and_kwargs.<locals>.args_and_kwargs()
        got an unexpected keyword argument 'last_input'

  because

  - the :ref:`call<how to call a function>` to ``args_and_kwargs`` which belongs to :ref:`test_args_and_kwargs` uses a :ref:`keyword argument<test_keyword_arguments>` (``last_input='last'``).
  - the :ref:`function definition (signature)<how to make a function that takes input>` of ``args_and_kwargs`` does not allow any inputs when it is :ref:`called<how to call a function>` since the parentheses are empty.
  - :ref:`the call to a function must match its signature (definition)<what causes TypeError?>`.

* I add ``last_input`` to the parentheses of ``args_and_kwargs``

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 2-3

    def test_args_and_kwargs():
        # def args_and_kwargs():
        def args_and_kwargs(last_input):
            return None

        assert_equal(
            args_and_kwargs(
                # last_input='last', 'first',
                'first', last_input='last'
            ),
            ('first', 'last')
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_args_and_kwargs.<locals>.args_and_kwargs()
        got multiple values for argument 'last_input'

  because

  - the :ref:`call<how to call a function>` to ``args_and_kwargs`` which belongs to :ref:`test_args_and_kwargs` uses both :ref:`positional<test_positional_arguments>` and :ref:`keyword arguments<test_keyword_arguments>` for the same parameter (``'first'`` and ``last_input='last'``).
  - the :ref:`function definition (signature)<how to make a function that takes input>` of ``args_and_kwargs`` takes one argument (``last_input``). How does Python_ know which value to use for ``last_input`` if I use the :ref:`position<test_positional_arguments>` and the :ref:`name<test_keyword_arguments>`?

    .. code-block:: shell

      args_and_kwargs_arguments('first', last_input='last',)
      └── def args_and_kwargs_arguments(last_input):
          ├── last_input = 'first' ?
          └── last_input = 'last'  ?

  - :ref:`the call to a function must match its signature (definition)<what causes TypeError?>`.

* I add ``first_input`` to the parentheses of ``args_and_kwargs`` to make it clearer

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 3-4
    :emphasize-text: first_input

    def test_args_and_kwargs():
        # def args_and_kwargs():
        # def args_and_kwargs(last_input):
        def args_and_kwargs(last_input, first_input):
            return None

        assert_equal(
            args_and_kwargs(
                # last_input='last', 'first',
                'first', last_input='last'
            ),
            ('first', 'last')
        )


    # Exceptions seen

  the terminal_ still shows :ref:`TypeError<what causes TypeError?>` because I have not fixed the problem, the :ref:`call<how to call a function with input>` has confusing values. Python_ cannot tell the difference between the two values because I gave a :ref:`positional argument<test_positional_arguments>` (``first``), the :ref:`function definition<how to make a function that takes input>` has the ``last_input`` parameter in the first position, and I gave a value with the name ``last_input``.

  .. code-block:: shell

    args_and_kwargs_arguments('first', last_input='last',)
    └── def args_and_kwargs_arguments(last_input, first_input):
        ├── last_input = 'first' ?
        ├── last_input = 'last'  ?
        └── first_input = ?

* The :ref:`call<how to call a function with input>` gives the values for ``last_input`` as both ``'first'`` and ``'last'``, it would be like defining the :ref:`function<what is a function?>` with the same name twice

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 4-5

    def test_args_and_kwargs():
        # def args_and_kwargs():
        # def args_and_kwargs(last_input):
        # def args_and_kwargs(last_input, first_input):
        def args_and_kwargs(last_input, last_input):
            return None

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: duplicate argument 'last_input'
                 in function definition

* I use the right names and put them in the right order

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 5-6
    :emphasize-text: first_input

    def test_args_and_kwargs():
        # def args_and_kwargs():
        # def args_and_kwargs(last_input):
        # def args_and_kwargs(last_input, first_input):
        # def args_and_kwargs(last_input, last_input):
        def args_and_kwargs(first_input, last_input):
            return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == ('first', 'last')

  because when I :ref:`call<how to call a function with input>` ``args_and_kwargs`` with ``'first'`` and ``last_input='last'`` as inputs, it returns :ref:`None<what is None?>` which raises :ref:`AssertionError<what causes AssertionError?>` since :ref:`None<what is None?>` is NOT equal to a tuple_.

  .. code-block:: shell

    ├── a_tuple = (0, 1, 2, 'n')
    ├── a_list = [0, 1, 2, 'n']
    └── assert_equal(
            args_and_kwargs(
                'first', last_input='last'
            ),
            ('first', 'last')
        ) -> None
        └── def assert_equal(input_1, input_2):
            ├── input_1 = args_and_kwargs(
            │                 'first', last_input='last'
            │             )
            │             └── def args_and_kwargs(
            │                     first_input, last_input
            │                 ):
            │                 └── return None
            ├── input_2 = ('first', 'last')
            └── assert input_1 == input_2
                assert None    == ('first', 'last')

* I change :ref:`the return statement` to give the test what it wants

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 7-8

    def test_args_and_kwargs():
        # def args_and_kwargs():
        # def args_and_kwargs(last_input):
        # def args_and_kwargs(last_input, first_input):
        # def args_and_kwargs(last_input, last_input):
        def args_and_kwargs(first_input, last_input):
            # return None
            return first_input, last_input

  the test passes.

  .. code-block:: shell

    args_and_kwargs(
        'first', last_input='last',
    ) -> ('first', 'last')
    └── def args_and_kwargs(first_input, last_input):
        └── return first_input, last_input
            return 'first'    , 'last'

* I add :ref:`variables<what is a variable?>` for ``'first'`` and ``'last'`` in :ref:`test_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 10

    def test_args_and_kwargs():
        # def args_and_kwargs():
        # def args_and_kwargs(last_input):
        # def args_and_kwargs(last_input, first_input):
        # def args_and_kwargs(last_input, last_input):
        def args_and_kwargs(first_input, last_input):
            # return None
            return first_input, last_input

        first, last = 'first', 'last'

        assert_equal(
            args_and_kwargs(
                # last_input='last', 'first',
                'first', last_input='last'
            ),
            ('first', 'last')
        )


    # Exceptions seen

* I use the new :ref:`variables<what is a variable?>` to remove repetition of ``'first'`` and ``'last'`` from :ref:`test_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 163
    :emphasize-lines: 6-7, 9-10

        first, last = 'first', 'last'

        assert_equal(
            args_and_kwargs(
                # last_input='last', 'first',
                # 'first', last_input='last'
                first, last_input=last
            ),
            # ('first', 'last')
            (first, last)
        )


    # Exceptions seen

  the test is still green.

* I remove the commented lines from :ref:`test_args_and_kwargs`

  .. code-block:: python
    :lineno-start: 154

    def test_args_and_kwargs():
        def args_and_kwargs(first_input, last_input):
            return first_input, last_input

        first, last = 'first', 'last'

        assert_equal(
            args_and_kwargs(
                first, last_input=last
            ),
            (first, last)
        )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_args_and_kwargs'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can call a function with positional and keyword arguments<test_args_and_kwargs>`.

----

*********************************************************************************
test_optional_arguments
*********************************************************************************

I can make an argument_ of a :ref:`function<what is a function?>` optional, which means a value does not need to be given for it when the :ref:`function is called<how to call a function with input>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 160
    :emphasize-lines: 9-16

        assert_equal(
            args_and_kwargs(
                first, last_input=last
            ),
            (first, last)
        )


    def test_optional_arguments():
        first_name, last_name = 'jane', 'doe'
        assert_equal(
            optional_arguments(
                first_name, last_input=last_name,
            ),
            (first_name, last_name)
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'optional_arguments' is not defined

  because ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the :ref:`function definition<how to make a function that takes input>` for ``optional_arguments``

.. code-block:: python
  :lineno-start: 168
  :emphasize-lines: 2-3

  def test_optional_arguments():
      def optional_arguments(first_input, last_input):
          return first_input, last_input

      first_name, last_name = 'jane', 'doe'
      assert_equal(
          optional_arguments(
              first_name, last_input=last_name,
          ),
          (first_name, last_name)
      )


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove ``last_input=last_name`` from the :ref:`call<how to call a function with input>` to ``optional_arguments`` to show that it is a required argument

  .. code-block:: python
    :lineno-start: 168
    :emphasize-lines: 8-9

    def test_optional_arguments():
        def optional_arguments(first_input, last_input):
            return first_input, last_input

        first_name, last_name = 'jane', 'doe'
        assert_equal(
            optional_arguments(
                # first_name, last_input=last_name,
                first_name,
            ),
            (first_name, last_name)
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_optional_arguments.<locals>.optional_arguments()
        missing 1 required positional argument: 'last_input'

  because the ``last_input`` argument MUST be given when this :ref:`function is called<how to call a function with input>` (it is required).

* I give the argument a :ref:`default value<test_optional_arguments>` to make it optional

  .. code-block:: python
    :lineno-start: 168
    :emphasize-lines: 2-5

    def test_optional_arguments():
        # def optional_arguments(first_input, last_input):
        def optional_arguments(
            first_input, last_input='doe'
        ):
            return first_input, last_input

        first_name, last_name = 'jane', 'doe'
        assert_equal(
            optional_arguments(
                # first_name, last_input=last_name,
                first_name,
            ),
            (first_name, last_name)
        )


    # Exceptions seen

  the test passes because I do not need to give a value for the ``last_input`` parameter when I :ref:`call the function<how to call a function with input>` since there is a :ref:`default value<test_optional_arguments>` for the ``last_input`` parameter of the :ref:`function<what is a function?>` (``doe``).

  These two :ref:`calls<how to call a function with input>` are the same

  .. code-block:: python

    optional_arguments('jane')
    optional_arguments('jane', last_input='doe')

  - When ``optional_arguments('jane')`` runs

    .. code-block:: shell

      optional_arguments('jane') -> ('jane', 'doe')
      └── def optional_arguments(first_input, last_input='doe'):
          ├── first_input = 'jane'
          ├── last_input  = 'doe' # use default value
          └── return first_input, last_input
              return 'jane'     , 'doe'

  - When ``optional_arguments(first_input, last_input='doe')`` runs

    .. code-block:: shell

      optional_arguments(
          'jane', last_input='doe'
      ) -> ('jane', 'doe')
      └── def optional_arguments(first_input, last_input='doe'):
          ├── first_input = 'jane'
          ├── last_input  = 'doe' # use given value
          └── return first_input, last_input
              return 'jane'     , 'doe'

  :ref:`A function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I add another :ref:`assertion<what is an assertion?>` to show that I can still :ref:`call the function<how to call a function with input>` with different values

  .. code-block:: python
    :lineno-start: 175
    :emphasize-lines: 10-16

        first_name, last_name = 'jane', 'doe'
        assert_equal(
            optional_arguments(
                # first_name, last_input=last_name,
                first_name,
            ),
            (first_name, last_name)
        )

        first_name, blow = 'joe', 'blow'
        assert_equal(
            optional_arguments(
                first_name, blow
            ),
            ()
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('joe', 'blow') == ()

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 184
    :emphasize-lines: 6-7

        first_name, blow = 'joe', 'blow'
        assert_equal(
            optional_arguments(
                first_name, blow
            ),
            # ()
            (first_name, blow)
        )


    # Exceptions seen

  the test passes.

  .. code-block:: shell

    ├── first_name = 'joe'
    ├── blow       = 'blow'
    └── optional_arguments(
            first_name, blow
        ) -> ('joe', 'blow')
        └── def optional_arguments(first_input, last_input='doe'):
            ├── first_input = first_name
            ├── last_input  = blow # use given value
            └── return first_input, last_input
                return 'joe'     , 'blow'

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_optional_arguments`

  .. code-block:: python
    :lineno-start: 184
    :emphasize-lines: 10-16

        first_name, blow = 'joe', 'blow'
        assert_equal(
            optional_arguments(
                first_name, blow
            ),
            # ()
            (first_name, blow)
        )

        first_name = 'john'
        assert_equal(
            optional_arguments(
                first_input=first_name,
            ),
            ()
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('john', 'doe') == ()

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 193
    :emphasize-lines: 5-6

        first_name = 'john'
        assert_equal(
            optional_arguments(
                first_input=first_name,
            ),
            # ()
            (first_name, last_name)
        )


    # Exceptions seen

  the test passes because I do not need to give a value for the ``last_input`` parameter in the call to ``optional_arguments`` since there is a :ref:`default value<test_optional_arguments>` for the ``last_input`` parameter of the ``optional_arguments`` :ref:`function<what is a function?>` (``doe``). This means that

  .. code-block:: python

    optional_arguments('john')

  is the same as

  .. code-block:: python

    optional_arguments('john', last_input='doe')

  .. code-block:: shell

    ├── first_name = 'john'
    └── optional_arguments(
            first_input=first_name
        ) -> ('john', 'doe')
        └── def optional_arguments(first_input, last_input='doe'):
            ├── first_input = first_name
            ├── last_input  = 'doe' # use default value
            └── return first_input, last_input
                return 'john'     , 'doe'

  :ref:`A function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I add one more :ref:`assertion<what is an assertion?>` to :ref:`test_optional_arguments`

  .. code-block:: python
    :lineno-start: 193
    :emphasize-lines: 10-17

        first_name = 'john'
        assert_equal(
            optional_arguments(
                first_input=first_name,
            ),
            # ()
            (first_name, last_name)
        )

        last_name = 'smith'
        assert_equal(
            optional_arguments(
                last_input=last_name,
                first_input=first_name,
            ),
            (last_name, first_name)
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('john', 'smith')
                        == ('smith', 'john')

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 202
    :emphasize-lines: 7-8

        last_name = 'smith'
        assert_equal(
            optional_arguments(
                last_input=last_name,
                first_input=first_name,
            ),
            # (last_name, first_name)
            (first_name, last_name)
        )


    # Exceptions seen

  the test passes.

  .. code-block:: shell

    ├── first_name = 'john'
    ├── last_name  = 'smith'
    └── optional_arguments(
            last_input=last_name,
            first_input=first_name,
        ) -> ('john', 'smith')
        └── def optional_arguments(first_input, last_input='doe'):
            ├── first_input = first_name
            ├── last_input  = smith # use given value
            └── return first_input, last_input
                return 'john'     , 'smith'

* I remove the commented lines from :ref:`test_optional_arguments`

  .. code-block:: python
    :lineno-start: 168

    def test_optional_arguments():
        def optional_arguments(
            first_input, last_input='doe'
        ):
            return first_input, last_input

        first_name, last_name = 'jane', 'doe'
        assert_equal(
            optional_arguments(
                first_name,
            ),
            (first_name, last_name)
        )

  .. code-block:: python
    :lineno-start: 174

        first_name, blow = 'joe', 'blow'
        assert_equal(
            optional_arguments(
                first_name, blow
            ),
            (first_name, blow)
        )

  .. code-block:: python
    :lineno-start: 190

        first_name = 'john'
        assert_equal(
            optional_arguments(
                first_input=first_name,
            ),
            (first_name, last_name)
        )

  .. code-block:: python
    :lineno-start: 198

        last_name = 'smith'
        assert_equal(
            optional_arguments(
                last_input=last_name,
                first_input=first_name,
            ),
            (first_name, last_name)
        )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_optional_arguments'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can make a function with optional and required arguments<test_optional_arguments>`.

----

These four :ref:`functions<what is a function?>` - :ref:`keyword_arguments<test_keyword_arguments>`, :ref:`positional_arguments<test_positional_arguments>`, :ref:`args_and_kwargs<test_args_and_kwargs>` and :ref:`optional_arguments<test_optional_arguments>` are the same, they always ``return first_input, last_input``, their names are different.

.. code-block:: python
  :emphasize-text: positional keyword default kwargs optional

  def positional_arguments(first_input, last_input):
  def keyword_arguments(first_input, last_input):
  def args_and_kwargs(first_input, last_input):
  def optional_arguments(first_input, last_input='doe'):

``first_input`` and ``last_input`` are also names (:ref:`variables<what is a variable?>`), they can be any names. The difference that matters in the tests is how I :ref:`call<how to call a function with input>` the :ref:`functions<what is a function?>`

.. code-block:: python
  :emphasize-text: last

  positional_arguments('first', 'last')
             -> return 'first', 'last'

.. code-block:: python
  :emphasize-text: last

  positional_arguments('last', 'first')
             -> return 'last', 'first'

.. code-block:: python
  :emphasize-text: last

  positional_arguments(
      first_input=[0, 1, 2, 'n'],
      last_input=(0, 1, 2, 'n')
  ) -> return [0, 1, 2, 'n'], (0, 1, 2, 'n')

.. code-block:: python
  :emphasize-text: last

  keyword_arguments(
      first_input='first', last_input='last'
  ) -> return 'first', 'last'

.. code-block:: python
  :emphasize-text: last

  keyword_arguments(
      last_input='last', first_input='first'
  ) -> return 'first', 'last'

.. code-block:: python
  :emphasize-text: last

  keyword_arguments('last', 'first')
          -> return 'last', 'first'

.. code-block:: python
  :emphasize-text: last

  args_and_kwargs('first', last_input='last')
        -> return 'first', 'last'

.. code-block:: python
  :emphasize-text: last

  optional_arguments('jane', last_input='doe')
           -> return 'jane', 'doe'

.. code-block:: python
  :emphasize-text: last

  optional_arguments('jane')
           -> return 'jane', 'doe'

.. code-block:: python
  :emphasize-text: last

  optional_arguments('joe', 'blow')
           -> return 'joe', 'blow'

.. code-block:: python
  :emphasize-text: last

  optional_arguments(
      first_input='john', last_input='smith'
  ) -> return 'john', 'smith'

.. tip::

  As a rule of thumb I use :ref:`keyword arguments<test_keyword_arguments>` when the :ref:`function<what is a function?>` takes two or more inputs so I do not have to remember the order.

----

*********************************************************************************
test_unknown_number_of_arguments
*********************************************************************************

I can make :ref:`functions<what is a function?>` that take any number of :ref:`positional<test_positional_arguments>` and :ref:`keyword<test_keyword_arguments>` arguments. This means I do not need to know how many inputs the :ref:`function<what is a function?>` should take when it is :ref:`called<how to call a function with input>`, it can handle whatever I give it.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add :ref:`test_unknown_number_of_arguments` to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 198
    :emphasize-lines: 11-17

        last_name = 'smith'
        assert_equal(
            optional_arguments(
                last_input=last_name,
                first_input=first_name,
            ),
            (first_name, last_name)
        )


    def test_unknown_number_of_arguments():
        assert_equal(
            unknown_number_of_arguments(
                0, 1, a=2, b=3,
            ),
            None
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'unknown_number_of_arguments' is not defined

  because ``test_functions.py`` does not have ``unknown_number_of_arguments``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 2-3

    def test_unknown_number_of_arguments():
        def unknown_number_of_arguments():
            return None

        assert_equal(
            unknown_number_of_arguments(
                0, 1, a=2, b=3,
            ),
            None
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_unknown_number_of_arguments
              .<locals>.unknown_number_of_arguments()
        got an unexpected keyword argument 'a'

  because the :ref:`assertion<what is an assertion?>` called ``unknown_number_of_arguments`` with a :ref:`keyword argument<test_keyword_arguments>` named ``a`` and the :ref:`function definition<how to make a function that takes input>` does not allow any inputs, the parentheses are empty.

* I add ``a`` to the :ref:`function definition<how to make a function that takes input>`

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 2-3

    def test_unknown_number_of_arguments():
        # def unknown_number_of_arguments():
        def unknown_number_of_arguments(a):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_unknown_number_of_arguments
            .<locals>.unknown_number_of_arguments()
        got multiple values for argument 'a'

  I had this same problem in :ref:`test_args_and_kwargs`. Python_ cannot tell if ``a`` is a :ref:`positional<test_positional_arguments>` or :ref:`keyword argument<test_keyword_arguments>` based on my :ref:`function definition<how to make a function that takes input>`. It cannot tell if ``0`` or ``2`` is the value for ``a``.

  .. code-block:: shell

    unknown_number_of_arguments(0, 1, a=2, b=3,)
    └── def unknown_number_of_arguments(a):
        ├── a = 0 ?
        └── a = 2 ?

----

*********************************************************************************
double starred expressions
*********************************************************************************

Python_ has a way for a :ref:`function<what is a function?>` to take any number of :ref:`keyword arguments<test_keyword_arguments>` without knowing how many they are. It is the double starred expression (``**``).

* I use a double starred expression to replace ``a`` in the parentheses

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 3-4

    def test_unknown_number_of_arguments():
        # def unknown_number_of_arguments():
        # def unknown_number_of_arguments(a):
        def unknown_number_of_arguments(**kwargs):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_unknown_number_of_arguments
            .<locals>.unknown_number_of_arguments()
        takes 0 positional arguments but 2 were given

* I add ``x`` as the name of the first :ref:`positional argument<test_positional_arguments>`

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 4-5
    :emphasize-text: x

    def test_unknown_number_of_arguments():
        # def unknown_number_of_arguments():
        # def unknown_number_of_arguments(a):
        # def unknown_number_of_arguments(**kwargs):
        def unknown_number_of_arguments(**kwargs, x):
            return None

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: arguments cannot follow var-keyword argument

  a reminder that :ref:`I cannot put positional arguments after keyword arguments<test_args_and_kwargs>`.

* I change the order of the inputs in ``unknown_number_of_arguments``

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 5-6
    :emphasize-text: x

    def test_unknown_number_of_arguments():
        # def unknown_number_of_arguments():
        # def unknown_number_of_arguments(a):
        # def unknown_number_of_arguments(**kwargs):
        # def unknown_number_of_arguments(**kwargs, x):
        def unknown_number_of_arguments(x, **kwargs):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_unknown_number_of_arguments
            .<locals>.unknown_number_of_arguments()
        takes 1 positional argument but 2 were given

* I add ``y`` as the name of the other :ref:`positional argument<test_positional_arguments>`

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 6-7

    def test_unknown_number_of_arguments():
        # def unknown_number_of_arguments():
        # def unknown_number_of_arguments(a):
        # def unknown_number_of_arguments(**kwargs):
        # def unknown_number_of_arguments(**kwargs, x):
        # def unknown_number_of_arguments(x, **kwargs):
        def unknown_number_of_arguments(x, y, **kwargs):
            return None

        assert_equal(
            unknown_number_of_arguments(
                0, 1, a=2, b=3,
            ),
            None
        )


    # Exceptions seen

  the test passes.

  .. code-block:: shell

    unknown_number_of_arguments(0, 1, a=2, b=3,) -> None
    └── def unknown_number_of_arguments(x, y, **kwargs):
        └── return None

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to see what happens if I :ref:`call the function<how to call a function with input>` with three :ref:`keyword arguments<test_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 217
    :emphasize-lines: 8-13

        assert_equal(
            unknown_number_of_arguments(
                0, 1, a=2, b=3,
            ),
            None
        )

        assert_equal(
            unknown_number_of_arguments(
                0, 1, a=2, b=3, c=4,
            ),
            ()
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None == ()

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 224
    :emphasize-lines: 5-6

        assert_equal(
            unknown_number_of_arguments(
                0, 1, a=2, b=3, c=4,
            ),
            # ()
            None
        )


    # Exceptions seen

  the test passes because the :ref:`function<what is a function?>` can take any number of :ref:`keyword arguments<test_keyword_arguments>` without knowing how many are in the :ref:`call<how to call a function with input>`.

  .. code-block:: shell

    unknown_number_of_arguments(0, 1, a=2, b=3, c=4,) -> None
    └── def unknown_number_of_arguments(x, y, **kwargs):
        └── return None

* I add an :ref:`assertion<what is an assertion?>` to see what happens when I :ref:`call the function<how to call a function with input>` with three :ref:`positional arguments<test_positional_arguments>`

  .. code-block:: python
    :lineno-start: 224
    :emphasize-lines: 9-14

        assert_equal(
            unknown_number_of_arguments(
                0, 1, a=2, b=3, c=4,
            ),
            # ()
            None
        )

        assert_equal(
            unknown_number_of_arguments(
                0, 1, 2, a=3, b=4, c=5,
            ),
            None
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_unknown_number_of_arguments
            .<locals>.unknown_number_of_arguments()
        takes 2 positional arguments but 3 were given

  the :ref:`function definition<how to make a function that takes input>` only allows two :ref:`positional arguments<test_positional_arguments>` not three.

* I change the definition of the ``unknown_number_of_arguments`` :ref:`function<what is a function?>` to make it take three :ref:`positional arguments<test_positional_arguments>`

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 7-8
    :emphasize-text: z

    def test_unknown_number_of_arguments():
        # def unknown_number_of_arguments():
        # def unknown_number_of_arguments(a):
        # def unknown_number_of_arguments(**kwargs):
        # def unknown_number_of_arguments(**kwargs, x):
        # def unknown_number_of_arguments(x, **kwargs):
        # def unknown_number_of_arguments(x, y, **kwargs):
        def unknown_number_of_arguments(x, y, z, **kwargs):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        test_unknown_number_of_arguments
            .<locals>.unknown_number_of_arguments()
        missing 1 required positional argument: 'z'

  because the previous :ref:`call to the function<how to call a function with input>` uses two :ref:`positional arguments<test_positional_arguments>` and the :ref:`function<what is a function?>` now requires three.

----

*********************************************************************************
single starred expressions
*********************************************************************************

Python_ also has a way for a :ref:`function<what is a function?>` to take any number of :ref:`positional arguments<test_positional_arguments>` without knowing how many they are. It is the single starred expression (``*``).

* I use a single starred expression (``*``) to replace the :ref:`positional arguments<test_positional_arguments>`

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 8-9

    def test_unknown_number_of_arguments():
        # def unknown_number_of_arguments():
        # def unknown_number_of_arguments(a):
        # def unknown_number_of_arguments(**kwargs):
        # def unknown_number_of_arguments(**kwargs, x):
        # def unknown_number_of_arguments(x, **kwargs):
        # def unknown_number_of_arguments(x, y, **kwargs):
        # def unknown_number_of_arguments(x, y, z, **kwargs):
        def unknown_number_of_arguments(*args, **kwargs):
            return None

  the test passes.

  .. code-block:: shell

    unknown_number_of_arguments(0, 1, 2, a=3, b=4, c=5,) -> None
    └── def unknown_number_of_arguments(*args, **kwargs):
        └── return None

* ``*args, **kwargs`` is :ref:`Python convention<conventions>`. I change the names to make it clearer

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 9-12

    def test_unknown_number_of_arguments():
        # def unknown_number_of_arguments():
        # def unknown_number_of_arguments(a):
        # def unknown_number_of_arguments(**kwargs):
        # def unknown_number_of_arguments(**kwargs, x):
        # def unknown_number_of_arguments(x, **kwargs):
        # def unknown_number_of_arguments(x, y, **kwargs):
        # def unknown_number_of_arguments(x, y, z, **kwargs):
        # def unknown_number_of_arguments(*args, **kwargs):
        def unknown_number_of_arguments(
            *positional_arguments, **keyword_arguments
        ):
            return None

  the test is still green.

----

*********************************************************************************
how Python treats starred and double starred expressions
*********************************************************************************

* I change :ref:`the return statement` because I want the :ref:`function<what is a function?>` to return its input (remember the :ref:`identity function<test_identity_function>`?)

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 13-14

    def test_unknown_number_of_arguments():
        # def unknown_number_of_arguments():
        # def unknown_number_of_arguments(a):
        # def unknown_number_of_arguments(**kwargs):
        # def unknown_number_of_arguments(**kwargs, x):
        # def unknown_number_of_arguments(x, **kwargs):
        # def unknown_number_of_arguments(x, y, **kwargs):
        # def unknown_number_of_arguments(x, y, z, **kwargs):
        # def unknown_number_of_arguments(*args, **kwargs):
        def unknown_number_of_arguments(
            *positional_arguments, **keyword_arguments
        ):
            return positional_arguments, keyword_arguments
            # return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ((0, 1), {'a': 2, 'b': 3})
                        == None

  I get a tuple_ that has

  - a tuple_ (anything in parentheses ``( )`` separated by a comma) for the :ref:`positional arguments<test_positional_arguments>`
  - a :ref:`dictionary<what is a dictionary?>` (any key-value pairs in curly braces ``{ }`` separated by commas) for the :ref:`keyword arguments<test_keyword_arguments>`

  When ``unknown_number_of_arguments(0, 1, a=2, b=3)`` runs

  .. code-block:: shell

    unknown_number_of_arguments(
        0, 1, a=2, b=3
    ) -> ((0, 1), {'a': 2, 'b': 3})
    └── def unknown_number_of_arguments(
            *positional_arguments, **keyword_arguments
        ):
        ├── positional_arguments = (0, 1)
        ├── keyword_arguments    = {'a': 2, 'b': 3}
        └── return  positional_arguments, keyword_arguments
            return ((0, 1              ), {'a': 2, 'b': 3  })

  - If I use ``*something`` in a :ref:`function definition<how to make a function that takes input>`, it takes any number of :ref:`positional arguments<test_positional_arguments>` as a tuple_.
  - If I use ``**something`` in a :ref:`function definition<how to make a function that takes input>`, it takes any number of :ref:`keyword arguments<test_keyword_arguments>` as a :ref:`dictionary<what is a dictionary?>`.

* I change my expectation to match reality in the first :ref:`assertion<what is an assertion?>` of :ref:`test_unknown_number_of_arguments`

  .. code-block:: python
    :lineno-start: 217
    :emphasize-lines: 11-12

        def unknown_number_of_arguments(
            *positional_arguments, **keyword_arguments
        ):
            return positional_arguments, keyword_arguments
            # return None

        assert_equal(
            unknown_number_of_arguments(
                0, 1, a=2, b=3,
            ),
            # None
            ((0, 1), {'a': 2, 'b': 3})
        )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ((0, 1), {'a': 2, 'b': 3, 'c': 4})
                        == None

  I get a tuple_ that has

  - a tuple_ (anything in parentheses ``( )`` separated by a comma) for the :ref:`positional arguments<test_positional_arguments>`.
  - a :ref:`dictionary<what is a dictionary?>` (any key-value pairs in curly braces ``{ }`` separated by commas) for the :ref:`keyword arguments<test_keyword_arguments>`.

  When ``unknown_number_of_arguments(0, 1, a=2, b=3, c=4)`` runs

  .. code-block:: shell

    unknown_number_of_arguments(
        0, 1, a=2, b=3, c=4
    ) -> ((0, 1), {'a': 2, 'b': 3, 'c': 4})
    └── def unknown_number_of_arguments(
            *positional_arguments, **keyword_arguments
        ):
        ├── positional_arguments = (0, 1)
        ├── keyword_arguments    = {'a': 2, 'b': 3, 'c': 4}
        └── return  positional_arguments, keyword_arguments
            return ((0, 1              ), {'a': 2, 'b': 3, 'c':4})

  - If I use ``*something`` in a :ref:`function definition<how to make a function that takes input>`, it takes any number of :ref:`positional arguments<test_positional_arguments>` as a tuple_ (anything in parentheses ``( )`` separated by a comma).
  - If I use ``**something`` in a :ref:`function definition<how to make a function that takes input>`, it takes any number of :ref:`keyword arguments<test_keyword_arguments>` as a :ref:`dictionary<what is a dictionary?>` (any key-value pairs in curly braces ``{ }`` separated by commas).

* I change my expectation to match reality in the second :ref:`assertion<what is an assertion?>` of :ref:`test_unknown_number_of_arguments`

  .. code-block:: python
    :lineno-start: 223
    :emphasize-lines: 14-15

        assert_equal(
            unknown_number_of_arguments(
                0, 1, a=2, b=3,
            ),
            # None
            ((0, 1), {'a': 2, 'b': 3})
        )

        assert_equal(
            unknown_number_of_arguments(
                0, 1, a=2, b=3, c=4,
            ),
            # ()
            # None
            ((0, 1), {'a': 2, 'b': 3, 'c': 4})
        )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        assert ((0, 1, 2), {'a': 3, 'b': 4, 'c': 5})
            == None

  I get a tuple_ that has

  - a tuple_ for the :ref:`positional arguments<test_positional_arguments>`
  - a :ref:`dictionary<what is a dictionary?>` for the :ref:`keyword arguments<test_keyword_arguments>`

  .. code-block:: shell

    unknown_number_of_arguments(
        0, 1, 2, a=3, b=4, c=5
    ) -> ((0, 1, 2), {'a': 3, 'b': 4, 'c': 5})
    └── def unknown_number_of_arguments(
            *positional_arguments, **keyword_arguments
        ):
        ├── positional_arguments = (0, 1, 2)
        ├── keyword_arguments    = {'a': 3, 'b': 4, 'c':5}
        └── return  positional_arguments, keyword_arguments
            return ((0, 1, 2           ), {'a': 3, 'b': 4, 'c':5})

  - If I use ``*something`` in a :ref:`function definition<how to make a function that takes input>`, it takes any number of :ref:`positional arguments<test_positional_arguments>` as a tuple_ (anything in parentheses ``( )`` separated by a comma).
  - If I use ``**something`` in a :ref:`function definition<how to make a function that takes input>`, it takes any number of :ref:`keyword arguments<test_keyword_arguments>` as a :ref:`dictionary<what is a dictionary?>` (any key-value pairs in curly braces ``{ }`` separated by commas).

* I change my expectation to match reality in the last :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 231
    :emphasize-lines: 14-15

        assert_equal(
            unknown_number_of_arguments(
                0, 1, a=2, b=3, c=4,
            ),
            # ()
            # None
            ((0, 1), {'a': 2, 'b': 3, 'c': 4})
        )

        assert_equal(
            unknown_number_of_arguments(
                0, 1, 2, a=3, b=4, c=5,
            ),
            # None
            ((0, 1, 2), {'a': 3, 'b': 4, 'c': 5})
        )


    # Exceptions seen
  the test passes.

----

=================================================================================
how Python treats starred expressions
=================================================================================

----

* I add :ref:`variables<what is a variable?>` for the tuple_ and :ref:`dictionary<what is a dictionary?>` of the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 16-17

    def test_unknown_number_of_arguments():
        # def unknown_number_of_arguments():
        # def unknown_number_of_arguments(a):
        # def unknown_number_of_arguments(**kwargs):
        # def unknown_number_of_arguments(**kwargs, x):
        # def unknown_number_of_arguments(x, **kwargs):
        # def unknown_number_of_arguments(x, y, **kwargs):
        # def unknown_number_of_arguments(x, y, z, **kwargs):
        # def unknown_number_of_arguments(*args, **kwargs):
        def unknown_number_of_arguments(
            *positional_arguments, **keyword_arguments
        ):
            return positional_arguments, keyword_arguments
            # return None

        a_tuple = (0, 1)
        a_dictionary = {'a': 2, 'b': 3}
        assert_equal(
            unknown_number_of_arguments(
                0, 1, a=2, b=3,
            ),
            # None
            ((0, 1), {'a': 2, 'b': 3})
        )

* I use the :ref:`variables<what is a variable?>` to remove repetition of the tuple_ and :ref:`dictionary<what is a dictionary?>` from the first :ref:`assertion<what is an assertion?>` in :ref:`test_unknown_number_of_arguments`

  .. code-block:: python
    :lineno-start: 223
    :emphasize-lines: 5-6, 9-10

        a_tuple = (0, 1)
        a_dictionary = {'a': 2, 'b': 3}
        assert_equal(
            unknown_number_of_arguments(
                # 0, 1, a=2, b=3,
                a_tuple, a_dictionary
            ),
            # None
            # ((0, 1), {'a': 2, 'b': 3})
            (a_tuple, a_dictionary)
        )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert (((0, 1), {'a... 'b': 3}), {})
                        == ((0, 1), {'a': 2, 'b': 3})

  because passing in the values this way means I am sending in two :ref:`positional arguments<test_positional_arguments>` (``a_tuple`` and ``a_dictionary``) so I get a tuple_ with

  - a tuple_ of the arguments_ since they are both :ref:`positional<test_positional_arguments>`.
  - an empty :ref:`dictionary<what is a dictionary?>` since there are no :ref:`keyword arguments<test_keyword_arguments>`.

  .. code-block:: shell

    ├── a_tuple = (0, 1)
    ├── a_dictionary = {'a': 2, 'b': 3}
    └── unknown_number_of_arguments(
            a_tuple, a_dictionary
        ) -> ((0, 1), {'a': 2, 'b': 3}), {})
        └── def unknown_number_of_arguments(
                *positional_arguments, **keyword_arguments
            ):
            ├── positional_arguments = (a_tuple, a_dictionary)
            ├── keyword_arguments    = {}
            └── return   positional_arguments    , keyword_arguments
                return ((a_tuple, a_dictionary)  , {})
                return ((0, 1), {'a': 2, 'b': 3}), {})

* I change the tuple_ with ``*`` so that Python_ breaks up its contents, allowing them to be used as separate arguments

  .. code-block:: python
    :lineno-start: 223
    :emphasize-lines: 6-7

        a_tuple = (0, 1)
        a_dictionary = {'a': 2, 'b': 3}
        assert_equal(
            unknown_number_of_arguments(
                # 0, 1, a=2, b=3,
                # a_tuple, a_dictionary
                *a_tuple, a_dictionary
            ),
            # None
            # ((0, 1), {'a': 2, 'b': 3})
            (a_tuple, a_dictionary)
        )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ((0, 1, {'a': 2, 'b': 3}), {})
                        == ((0, 1), {'a': 2, 'b': 3})

  I still get a tuple_ of the arguments since they are both :ref:`positional arguments<test_positional_arguments>`, the difference is that the items of the tuple_ appear separately not as another tuple_.

----

=================================================================================
how Python treats double starred expressions
=================================================================================

----

* I change the :ref:`dictionary<what is a dictionary?>` with ``**`` so that Python_ breaks up the contents, allowing them to be used as :ref:`keyword arguments<test_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 223
    :emphasize-lines: 7-8

        a_tuple = (0, 1)
        a_dictionary = {'a': 2, 'b': 3}
        assert_equal(
            unknown_number_of_arguments(
                # 0, 1, a=2, b=3,
                # a_tuple, a_dictionary
                # *a_tuple, a_dictionary
                *a_tuple, **a_dictionary
            ),
            # None
            # ((0, 1), {'a': 2, 'b': 3})
            (a_tuple, a_dictionary)
        )

  the test passes

  .. code-block:: shell

    ├── a_tuple = (0, 1)
    ├── a_dictionary = {'a': 2, 'b': 3}
    └── unknown_number_of_arguments(
            *a_tuple, **a_dictionary
        ) -> ((0, 1), {'a': 2, 'b': 3})
        └── def unknown_number_of_arguments(
                *positional_arguments, **keyword_arguments
            ):
            ├── positional_arguments = a_tuple
            ├── keyword_arguments    = a_dictionary
            └── return  positional_arguments, keyword_arguments
                return (a_tuple             , a_dictionary     )
                return ((0, 1)              , {'a': 2, 'b': 3} )

  these three statements are the same

  .. code-block:: python

    unknown_number_of_arguments(*a_tuple, **a_dictionary  )
    unknown_number_of_arguments(*(0, 1) , **{'a':2, 'b':3})
    unknown_number_of_arguments(0, 1    , a=2, b=3        )

  - If I use ``*something`` in a :ref:`function call<how to call a function>`, it sends the things in ``something`` as :ref:`positional arguments<test_positional_arguments>`.
  - If I use ``**something`` in a :ref:`function call<how to call a function>`, it sends the :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` of ``something`` as :ref:`keyword arguments<test_keyword_arguments>`.

* I add a :ref:`variable<what is a variable?>` for the :ref:`dictionary<what is a dictionary?>` of the second :ref:`assertion<what is an assertion?>` in :ref:`test_unknown_number_of_arguments`

  .. code-block:: python
    :lineno-start: 223
    :emphasize-lines: 15

        a_tuple = (0, 1)
        a_dictionary = {'a': 2, 'b': 3}
        assert_equal(
            unknown_number_of_arguments(
                # 0, 1, a=2, b=3,
                # a_tuple, a_dictionary
                # *a_tuple, a_dictionary
                *a_tuple, **a_dictionary
            ),
            # None
            # ((0, 1), {'a': 2, 'b': 3})
            (a_tuple, a_dictionary)
        )

        a_dictionary = {'a': 2, 'b': 3, 'c': 4}
        assert_equal(
            unknown_number_of_arguments(
                0, 1, a=2, b=3, c=4,
            ),
            # ()
            # None
            ((0, 1), {'a': 2, 'b': 3, 'c': 4})
        )

* I use the ``a_tuple`` and new ``a_dictionary`` :ref:`variables<what is a variable?>` to remove repetition of the tuple_ and :ref:`dictionary<what is a dictionary?>` from the second :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 237
    :emphasize-lines: 4-5, 9-10

        a_dictionary = {'a': 2, 'b': 3, 'c': 4}
        assert_equal(
            unknown_number_of_arguments(
                # 0, 1, a=2, b=3, c=4,
                a_tuple, a_dictionary,
            ),
            # ()
            # None
            # ((0, 1), {'a': 2, 'b': 3, 'c': 4})
            (a_tuple, a_dictionary)
        )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        assert (((0, 1), {'a... 'c': 4}), {})
            == ((0, 1), {'a'...': 3, 'c': 4})

  because passing in the values this way means I am sending in two :ref:`positional arguments<test_positional_arguments>` (``a_tuple`` and ``a_dictionary``) so I get a tuple_ with

  - a tuple_ of the arguments_ since they are both :ref:`positional<test_positional_arguments>`
  - an empty :ref:`dictionary<what is a dictionary?>` since there are no :ref:`keyword arguments<test_keyword_arguments>`

  .. code-block:: shell

    ├── a_tuple = (0, 1)
    ├── a_dictionary = {'a': 2, 'b': 3, 'c': 4}
    └── unknown_number_of_arguments(
            a_tuple, a_dictionary
        ) -> ((0, 1), {'a': 2, 'b': 3, 'c': 4}), {})
        └── def unknown_number_of_arguments(
                *positional_arguments, **keyword_arguments
            )
            ├── positional_arguments = (a_tuple, a_dictionary)
            ├── keyword_arguments    = {}
            └── return positional_arguments, keyword_arguments
                return ((a_tuple, a_dictionary), {})
                return ((0, 1), {'a': 2, 'b': 3, 'c': 4}), {})

* I change the :ref:`dictionary<what is a dictionary?>` with ``**`` so that Python_ breaks up the contents, allowing them to be used as :ref:`keyword arguments<test_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 237
    :emphasize-lines: 5-6

        a_dictionary = {'a': 2, 'b': 3, 'c': 4}
        assert_equal(
            unknown_number_of_arguments(
                # 0, 1, a=2, b=3, c=4,
                # a_tuple, a_dictionary,
                a_tuple, **a_dictionary,
            ),
            # ()
            # None
            # ((0, 1), {'a': 2, 'b': 3, 'c': 4})
            (a_tuple, a_dictionary)
        )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert (((0, 1),), {...': 3, 'c': 4})
                        == ((0, 1), {'a'...': 3, 'c': 4})

  The tuple_ I get no longer has an empty :ref:`dictionary<what is a dictionary?>`, values from the input :ref:`dictionary<what is a dictionary?>`.

* I change the tuple_ with ``*`` so that Python_ breaks up the contents, allowing them to be used as separate arguments

  .. code-block:: python
    :lineno-start: 237
    :emphasize-lines: 6-7

        a_dictionary = {'a': 2, 'b': 3, 'c': 4}
        assert_equal(
            unknown_number_of_arguments(
                # 0, 1, a=2, b=3, c=4,
                # a_tuple, a_dictionary,
                # a_tuple, **a_dictionary,
                *a_tuple, **a_dictionary,
            ),
            # ()
            # None
            # ((0, 1), {'a': 2, 'b': 3, 'c': 4})
            (a_tuple, a_dictionary)
        )

  the test passes.

  .. code-block:: shell

    ├── a_tuple = (0, 1)
    ├── a_dictionary = {'a': 2, 'b': 3, 'c': 4}
    └── unknown_number_of_arguments(
            *a_tuple, **a_dictionary
        ) -> (0, 1), {'a': 2, 'b': 3, 'c': 4})
        └── def unknown_number_of_arguments(
                *positional_arguments, **keyword_arguments
            )
            ├── positional_arguments = a_tuple
            ├── keyword_arguments    = a_dictionary
            └── return positional_arguments, keyword_arguments
                return (a_tuple            , a_dictionary)
                return (0, 1), {'a': 2, 'b': 3, 'c': 4})

  these three statements are the same

  .. code-block:: python

    unknown_number_of_arguments(*a_tuple, **a_dictionary            )
    unknown_number_of_arguments(*(0, 1) , **{'a': 2, 'b': 3, 'c': 4})
    unknown_number_of_arguments(0, 1    , a=2, b=3, c=4             )

  - If I use ``*something`` in a :ref:`function call<how to call a function>`, it sends the things in ``something`` as :ref:`positional arguments<test_positional_arguments>`.
  - If I use ``**something`` in a :ref:`function call<how to call a function>`, it sends the :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` of ``something`` as :ref:`keyword arguments<test_keyword_arguments>`.

* I add :ref:`variables<what is a variable?>` for the tuple_ and :ref:`dictionary<what is a dictionary?>` of the third :ref:`assertion<what is an assertion?>` in :ref:`test_unknown_number_of_arguments`

  .. code-block:: python
    :lineno-start: 237
    :emphasize-lines: 15-16

        a_dictionary = {'a': 2, 'b': 3, 'c': 4}
        assert_equal(
            unknown_number_of_arguments(
                # 0, 1, a=2, b=3, c=4,
                # a_tuple, a_dictionary,
                # a_tuple, **a_dictionary,
                *a_tuple, **a_dictionary,
            ),
            # ()
            # None
            # ((0, 1), {'a': 2, 'b': 3, 'c': 4})
            (a_tuple, a_dictionary)
        )

        a_tuple = (0, 1, 2)
        a_dictionary = {'a': 3, 'b': 4, 'c': 5}
        assert_equal(
            unknown_number_of_arguments(
                0, 1, 2, a=3, b=4, c=5,
            ),
            # None
            ((0, 1, 2), {'a': 3, 'b': 4, 'c': 5})
        )


    # Exceptions seen

* I use the :ref:`variables<what is a variable?>` to remove repetition of the tuple_ and :ref:`dictionary<what is a dictionary?>` from the third :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 251
    :emphasize-lines: 4-5, 9-10

        a_tuple = (0, 1, 2)
        a_dictionary = {'a': 3, 'b': 4, 'c': 5}
        assert_equal(
            unknown_number_of_arguments(
                # 0, 1, 2, a=3, b=4, c=5,
                a_tuple, a_dictionary
            ),
            # None
            # ((0, 1, 2), {'a': 3, 'b': 4, 'c': 5})
            (a_tuple, a_dictionary)
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert (((0, 1, 2), ... 'c': 5}), {})
                        == ((0, 1, 2), {...': 4, 'c': 5})

  because passing in the values this way means I am sending in two :ref:`positional arguments<test_positional_arguments>` (``a_tuple`` and ``a_dictionary``) so I get a tuple_ with

  - a tuple_ of the arguments_ since they are both :ref:`positional<test_positional_arguments>`
  - an empty :ref:`dictionary<what is a dictionary?>` since there are no :ref:`keyword arguments<test_keyword_arguments>`

  .. code-block:: shell

    ├── a_tuple = (0, 1, 2)
    ├── a_dictionary = {'a': 3, 'b': 4, 'c': 5}
    └── unknown_number_of_arguments(
            a_tuple, a_dictionary
        ) -> ((0, 1, 2), {'a': 3, 'b': 4, 'c': 5}), {})
        └── def unknown_number_of_arguments(
                *positional_arguments, **keyword_arguments
            ):
            ├── positional_arguments = (a_tuple, a_dictionary)
            ├── keyword_arguments    = {}
            └── return   positional_arguments, keyword_arguments
                return ((a_tuple, a_dictionary)             , {})
                return ((0, 1, 2), {'a': 3, 'b': 4, 'c': 5}), {})

* I change the inputs with ``*`` and ``**`` so that Python_ breaks up the contents, allowing them to be used as separate arguments

  .. code-block:: python
    :lineno-start: 251
    :emphasize-lines: 6-7

        a_tuple = (0, 1, 2)
        a_dictionary = {'a': 3, 'b': 4, 'c': 5}
        assert_equal(
            unknown_number_of_arguments(
                # 0, 1, 2, a=3, b=4, c=5,
                # a_tuple, a_dictionary
                *a_tuple, **a_dictionary
            ),
            # None
            # ((0, 1, 2), {'a': 3, 'b': 4, 'c': 5})
            (a_tuple, a_dictionary)
        )


    # Exceptions seen

  the test passes.

  .. code-block:: shell

    ├── a_tuple = (0, 1, 2)
    ├── a_dictionary = {'a': 3, 'b': 4, 'c': 5}
    └── unknown_number_of_arguments(
            *a_tuple, **a_dictionary
        ) -> ((0, 1, 2), {'a': 3, 'b': 4, 'c': 5})
        └── def unknown_number_of_arguments(
                *positional_arguments, **keyword_arguments
            ):
            ├── positional_arguments = a_tuple
            ├── keyword_arguments    = a_dictionary
            └── return   positional_arguments, keyword_arguments
                return ( a_tuple , a_dictionary            )
                return ((0, 1, 2), {'a': 3, 'b': 4, 'c': 5})

  these three statements are the same

  .. code-block:: python

    unknown_number_of_arguments(
        *a_tuple  , **a_dictionary
    )
    unknown_number_of_arguments(
        *(0, 1, 2), **{'a': 2, 'b': 3, 'c': 4}
    )
    unknown_number_of_arguments(
        0, 1, 2, a=3, b=4, c=5
    )

  - If I use ``*something`` in a :ref:`function call<how to call a function>`, it sends the things in ``something`` as :ref:`positional arguments<test_positional_arguments>`.
  - If I use ``**something`` in a :ref:`function call<how to call a function>`, it sends the :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` of ``something`` as :ref:`keyword arguments<test_keyword_arguments>`.

* I add an :ref:`assertion<what is an assertion?>` with a :ref:`call<how to call a function with input>` to ``unknown_number_of_arguments`` using only :ref:`positional arguments<test_positional_arguments>`

  .. code-block:: python
    :lineno-start: 251
    :emphasize-lines: 14-18

        a_tuple = (0, 1, 2)
        a_dictionary = {'a': 3, 'b': 4, 'c': 5}
        assert_equal(
            unknown_number_of_arguments(
                # 0, 1, 2, a=3, b=4, c=5,
                # a_tuple, a_dictionary
                *a_tuple, **a_dictionary
            ),
            # None
            # ((0, 1, 2), {'a': 3, 'b': 4, 'c': 5})
            (a_tuple, a_dictionary)
        )

        a_tuple = (0, 1, 2, 'n')
        assert_equal(
            unknown_number_of_arguments(*a_tuple),
            ()
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ((0, 1, 2, 'n'), {}) == ()

  because passing in the values this way means I am sending in only :ref:`positional arguments<test_positional_arguments>` (``*a_tuple``) so I get a tuple_ with

  - a tuple_ of the :ref:`positional arguments<test_positional_arguments>`.
  - an empty :ref:`dictionary<what is a dictionary?>` since there are no :ref:`keyword arguments<test_keyword_arguments>`.

  .. code-block:: shell

    ├── a_tuple = (0, 1, 2, 'n')
    └── unknown_number_of_arguments(
            *a_tuple
        ) -> ((0, 1, 2, 'n'), {})
        └── def unknown_number_of_arguments(
                *positional_arguments, **keyword_arguments
            ):
            ├── positional_arguments = a_tuple
            ├── keyword_arguments    = {}
            └── return   positional_arguments, keyword_arguments
                return ( a_tuple             , {}               )
                return ((0, 1, 2, 'n')       , {}               )

  these three statements are the same

  .. code-block:: python

    unknown_number_of_arguments(*a_tuple       )
    unknown_number_of_arguments(*(0, 1, 2, 'n'))
    unknown_number_of_arguments(0, 1, 2, 'n'   )

  - If I use ``*something`` in a :ref:`function call<how to call a function>`, it sends the things in ``something`` as :ref:`positional arguments<test_positional_arguments>`.
  - If I use ``*something`` in a :ref:`function definition<how to make a function that takes input>`, it takes any number of :ref:`positional arguments<test_positional_arguments>` as a tuple_ (anything in parentheses ``( )`` separated by a comma).

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 264
    :emphasize-lines: 4-5

        a_tuple = (0, 1, 2, 'n')
        assert_equal(
            unknown_number_of_arguments(*a_tuple),
            # ()
            (a_tuple, {})
        )


    # Exceptions seen

  the test passes.

* I add another :ref:`assertion<what is an assertion?>` to see what happens when I :ref:`call the function<how to call a function with input>` with ONLY :ref:`keyword arguments<test_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 264
    :emphasize-lines: 8-12

        a_tuple = (0, 1, 2, 'n')
        assert_equal(
            unknown_number_of_arguments(*a_tuple),
            # ()
            (a_tuple, {})
        )

        a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
        assert_equal(
            unknown_number_of_arguments(**a_dictionary),
            ()
        )


    # Exceptions seen

  the terminal_ is my friend, and shows

  .. code-block:: python

    AssertionError: assert ((), {'a': 1,... 3, 'd': 'n'}) == ()

  because passing in the values this way means I am sending in only :ref:`keyword arguments<test_keyword_arguments>` (``**a_dictionary``) so I get a tuple_ with

  - an empty tuple_ since there are no :ref:`positional arguments<test_positional_arguments>`
  - a :ref:`dictionary<what is a dictionary?>` of the :ref:`keyword arguments<test_keyword_arguments>`

  .. code-block:: shell

    ├── a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
    └── unknown_number_of_arguments(
            **a_dictionary
        ) -> ((), {'a': 1, 'b': 2, 'c': 3, 'd': 'n'})
        └── def unknown_number_of_arguments(
                *positional_arguments, **keyword_arguments
            ):
            ├── positional_arguments = ()
            ├── keyword_arguments    = {
            │       'a': 1, 'b': 2, 'c': 3, 'd': 'n'
            │   }
            └── return  positional_arguments, keyword_arguments
                return ((), {'a': 1, 'b': 2, 'c': 3, 'd': 'n'})

  these three statements are the same

  .. code-block:: python

    unknown_number_of_arguments(**a_dictionary                    )
    unknown_number_of_arguments({'a': 1, 'b': 2, 'c': 3, 'd': 'n'})
    unknown_number_of_arguments(  a = 1,  b = 2,  c = 3,  d = 'n' )

  - If I use ``**something`` in a :ref:`function call<how to call a function>`, it sends the :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` of ``something`` as :ref:`keyword arguments<test_keyword_arguments>`.
  - If I use ``**something`` in a :ref:`function definition<how to make a function that takes input>`, it takes any number of :ref:`keyword arguments<test_keyword_arguments>` as a :ref:`dictionary<what is a dictionary?>` (any key-value pairs in curly braces ``{ }`` separated by commas).

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 271
    :emphasize-lines: 4-5

        a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
        assert_equal(
            unknown_number_of_arguments(**a_dictionary),
            # ()
            ((), a_dictionary)
        )


    # Exceptions seen

  the test passes.

* I add one more :ref:`assertion<what is an assertion?>` to see what happens when I :ref:`call<how to call a function with input>` the :ref:`unknown_number_of_arguments function<test_unknown_number_of_arguments>` with no inputs

  .. code-block:: python
    :lineno-start: 271
    :emphasize-lines: 8-10

        a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
        assert_equal(
            unknown_number_of_arguments(**a_dictionary),
            # ()
            ((), a_dictionary)
        )

        assert_equal(
            unknown_number_of_arguments(), TypeError
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: assert ((), {}) == <class 'TypeError'>

  because ``unknown_number_of_arguments`` gets called with no arguments_ so I get a tuple_ with

  - an empty tuple_ since there are no :ref:`positional arguments<test_positional_arguments>`.
  - an empty :ref:`dictionary<what is a dictionary?>` since there are no :ref:`keyword arguments<test_keyword_arguments>`.

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 278
    :emphasize-lines: 2-3

        assert_equal(
            # unknown_number_of_arguments(), TypeError
            unknown_number_of_arguments(), ((), {})
        )


    # Exceptions seen

  the test passes.

  .. code-block:: shell

    unknown_number_of_arguments() -> ((), {})
    └── def unknown_number_of_arguments(
            *positional_arguments, **keyword_arguments
        ):
        ├── positional_arguments = ()
        ├── keyword_arguments    = {}
        └── return  positional_arguments, keyword_arguments
            return (()                  , {}               )

  - If I use ``*something`` in a :ref:`function definition<how to make a function that takes input>`, it takes any number of :ref:`positional arguments<test_positional_arguments>` as a tuple_ (anything in parentheses ``( )`` separated by a comma).
  - If I use ``**something`` in a :ref:`function definition<how to make a function that takes input>`, it takes any number of :ref:`keyword arguments<test_keyword_arguments>` as a :ref:`dictionary<what is a dictionary?>` (any key-value pairs in curly braces ``{ }`` separated by commas).

* I remove the commented lines from :ref:`test_unknown_number_of_arguments`

  .. code-block:: python
    :lineno-start: 208

    def test_unknown_number_of_arguments():
        def unknown_number_of_arguments(
            *positional_arguments, **keyword_arguments
        ):
            return positional_arguments, keyword_arguments

        a_tuple = (0, 1)
        a_dictionary = {'a': 2, 'b': 3}
        assert_equal(
            unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            ),
            (a_tuple, a_dictionary)
        )

  .. code-block:: python
    :lineno-start: 223

        a_dictionary = {'a': 2, 'b': 3, 'c': 4}
        assert_equal(
            unknown_number_of_arguments(
                *a_tuple, **a_dictionary,
            ),
            (a_tuple, a_dictionary)
        )


  .. code-block:: python
    :lineno-start: 231

        a_tuple = (0, 1, 2)
        a_dictionary = {'a': 3, 'b': 4, 'c': 5}
        assert_equal(
            unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            ),
            (a_tuple, a_dictionary)
        )

  .. code-block:: python
    :lineno-start: 240

        a_tuple = (0, 1, 2, 'n')
        assert_equal(
            unknown_number_of_arguments(*a_tuple),
            (a_tuple, {})
        )

  .. code-block:: python
    :lineno-start: 246

        a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
        assert_equal(
            unknown_number_of_arguments(**a_dictionary),
            ((), a_dictionary)
        )

        assert_equal(
            unknown_number_of_arguments(), ((), {})
        )


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # SyntaxError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_unknown_number_of_arguments'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can make a function that can take any number of positional or keyword arguments<test_unknown_number_of_arguments>`.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_functions.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``functions``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

I ran tests to show that I can make :ref:`functions<what is a function?>` that take input

* :ref:`I can use a function to remove repetition<test_why_use_a_function>`.
* :ref:`I can call a function with input by placing an input in parentheses when I call it<how to call a function with input>`.
* :ref:`The identity or passthrough function returns its input as output<test_identity_function>`.
* :ref:`I can call a function with positional arguments<test_positional_arguments>`.
* :ref:`I can call a function with keyword arguments<test_keyword_arguments>`.
* :ref:`I can call a function with positional and keyword arguments<test_args_and_kwargs>`.
* :ref:`I can make a function with optional arguments<test_optional_arguments>`.
* :ref:`I can make a function that can take any number of positional or keyword arguments<test_unknown_number_of_arguments>`

  - If I use ``*something`` in a :ref:`function call<how to call a function>`, it sends the things in ``something`` as :ref:`positional arguments<test_positional_arguments>`.
  - If I use ``**something`` in a :ref:`function call<how to call a function>`, it sends the :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` of ``something`` as :ref:`keyword arguments<test_keyword_arguments>`.
  - If I use ``*something`` in a :ref:`function definition<how to make a function that takes input>`, it takes any number of :ref:`positional arguments<test_positional_arguments>` as a tuple_ (anything in parentheses ``( )`` separated by a comma).
  - If I use ``**something`` in a :ref:`function definition<how to make a function that takes input>`, it takes any number of :ref:`keyword arguments<test_keyword_arguments>` as a :ref:`dictionary<what is a dictionary?>` (any key-value pairs in curly braces ``{ }`` separated by commas).

:ref:`How many questions can you answer about functions?<questions about functions that take input>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<functions that take input: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python Test Driven Development environment manually<how to make a Python Test Driven Development environment manually>`.
* :ref:`I know what a Python module is<what is a module?>`.
* :ref:`I know how to run tests automatically<how to run tests automatically>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`I know how to make a person with strings<how to make a person with strings>`.
* :ref:`I know how to make functions that take input<functions that take input>`.

I am going for a walk.

.. toctree::
  :titlesonly:
  :maxdepth: 1

  ../exceptions/TypeError/index
  ../exceptions/AssertionError/AssertionError_w_functions
  ../how_to/telephone/index
  ../exceptions/ModuleNotFoundError/separate_and_equal

:ref:`Would you like to test TypeError?<what causes TypeError?>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->