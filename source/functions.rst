functions
=========

The focus of this chapter is on functions in python using Test Driven Development

A ``function`` is a `callable <https://docs.python.org/3/glossary.html#term-callable>`_ unit/block of code. It is a way to encapsulate statements that can be used after they are written to accomplish a task. With functions I make code modular which makes it easier to test and reuse.

In programming I process input data of some form and output data in some form. I can think of it as

.. code-block:: python

    input_data -> program -> output_data
    program(input_data) -> output_data

I can think of the ``program`` in this illustration as the ``function`` that carries out the processing of ``input_data`` to return ``output_data``



How to Define functions
-----------------------

``functions`` are defined using the `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword, a name, parentheses and a colon at the end

RED: make it fail
^^^^^^^^^^^^^^^^^

What if I a create a file called ``test_functions.py`` in the ``tests`` folder and add the following failing test

.. code-block:: python

  import unittest
  import functions


  class TestFunctions(unittest.TestCase):

    def test_functions_with_pass(self):
      self.assertIsNone(functions.function_with_pass())

the terminal displaysa :doc:`ModuleNotFoundError`\ , and I add it to the list of exceptions encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* create a file called ``functions.py`` in the project folder and the terminal updates to show an :doc:`AttributeError`\ , which I add to the running list of exceptions encountered
  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* update ``functions.py`` with a function definition
  .. code-block:: python

    def function_with_pass():
      pass
  and the terminal displays a passing test

  * the test checks if the value of the call to ``functions.function_with_pass`` is :doc:`None <data_structures_none>`
  * the function definition simply says `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ yet the test passes
  * `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a placeholder keyword which allows the function definition to follow python syntax rules
  * the test passes because in python all functions return :doc:`None <data_structures_none>` by default, I can imagine the function has an invisible line that says ``return None``

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

What if I test if functions really always return :doc:`None <data_structures_none>` by default


*
  RED: make it fail
  add a new failing test to ``TestFunctions`` in ``test_functions.py``

  .. code-block:: python

      def test_functions_with_return(self):
       self.assertIsNone(functions.function_with_return())

  the terminal updates to show an :doc:`AttributeError`

*
  GREEN: make it pass

  add a new function to ``functions.py`` to make the test pass, this time with a ``return`` statement instead of `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_

  .. code-block:: python

    def function_with_return(self):
      return

  the terminal shows this test is also passing. I have defined 2 functions with different statements in their body but they both return the same result, because "in python all functions return :doc:`None <data_structures_none>` by default, I can imagine the function has an invisible line that says ``return None``"

* RED: make it fail
  I can add one more test to the ``TestFunctions`` class in ``test_functions.py`` to help drive home the point
  .. code-block:: python

      def test_functions_with_return_none(self):
       self.assertIsNone(functions.function_with_return_none())
  the terminal updates to show an :doc:`AttributeError`
*
  GREEN: make it pass

  from the `Zen of Python <https://peps.python.org/pep-0020/>`_ - ``Explicit is better than implicit.`` Let us add a function definition to ``functions.py`` this time with an explicit ``return`` statement showing the value returned

  .. code-block:: python

    def function_with_return_none():
      return None

  and the terminal updates to show passing tests.

The 3 ways I have defined functions so far have the exact same outcome, they all ``return None``. If ``Explicit is better than implicit.`` I prefer to use ``return None`` telling anyone who reads the code exactly what the function returns.

Here is what I know so far about functions in python


* functions are defined using the `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword
* functions return :doc:`None <data_structures_none>` by default

Passthrough Functions
---------------------

A function returns ``output``, and can take :raw-html-m2r:`<code class="docutils literal"><span class="pre">&#96;(input)&#96;&#96;&#96;. As a simple test What if I create a</span></code>`\ passthrough function` which is a function that returns the input it receives as output

RED: make it fail
^^^^^^^^^^^^^^^^^

add a failing test to the ``TestFunctions`` class in ``test_functions.py``

.. code-block:: python

    def test_passthrough_function(self):
      self.assertEqual(functions.passthrough(False), False)

the terminal updates to show an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* update ``functions.py`` with a function definition
  .. code-block:: python

    def passthrough():
      return None
  the terminal updates to show a :doc:`TypeError` because the definition for ``passthrough`` does not allow ``inputs`` but the test sends :doc:`False <data_structures_booleans>` as input
  .. code-block:: python

    TypeError: passthrough() takes 0 positional arguments but 1 was given

* add the new exception to the list of exceptions encountered
  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError

* update ``passthrough`` in ``functions.py`` to take 1 positional argument
  .. code-block:: python

    def passthrough(input_data):
      return None
  the terminal updates to show an :doc:`AssertionError`
  .. code-block:: python

    AssertionError: None != False
  because the result of calling ``functions.passthrough`` with :doc:`False <data_structures_booleans>` as input is :doc:`None <data_structures_none>` which is not equal to :doc:`False <data_structures_booleans>` which is the expected result
* change the definition of ``passthrough`` to make the test pass
  .. code-block:: python

    def passthrough(input_data):
      return False
  the terminal updates to show passing tests. I am geniuses!

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Wait a minute! Something is not quite right here. The definition for a ``passthrough`` function was that it returned the same thing it was given, the test passes when :doc:`False <data_structures_booleans>` is given as input, will it still pass when another value is given or will it always return :doc:`False <data_structures_booleans>`? There is a way to find out, What if I test it


*
  RED: make it fail

  update ``test_passthrough_function`` in ``TestFunctions`` in ``test_functions.py``  with a new test

  .. code-block:: python

      def test_passthrough_function(self):
       self.assertEqual(functions.passthrough(False), False)
       self.assertEqual(functions.passthrough(True), True)

  the terminal shows an :doc:`AssertionError`

  .. code-block:: python

    AssertionError: False != True

  the function returns :doc:`False <data_structures_booleans>` instead of :doc:`True <data_structures_booleans>` in the second case, confirming the suspicions, I am not all the way geniuses, yet

*
  GREEN: make it pass

  change the definition of ``passthrough`` in ``functions.py``

  .. code-block:: python

    def passthrough(input_data):
      return input_data

  the terminal updates to show passing tests. I have more confidence that the passthrough function will likely return the input data it is given. Let us add more tests for good measure using the other python `Data Structures <./DATA_STRUCTURES.rst>`_

*
  REFACTOR: make it better

  update ``test_passthrough_function``

  .. code-block:: python

      def test_passthrough_function(self):
       self.assertEqual(functions.passthrough(False), False)
       self.assertEqual(functions.passthrough(True), True)
       self.assertEqual(functions.passthrough(None), False)
       self.assertEqual(functions.passthrough(int), False)
       self.assertEqual(functions.passthrough(str), False)
       self.assertEqual(functions.passthrough(tuple), False)
       self.assertEqual(functions.passthrough(list), False)
       self.assertEqual(functions.passthrough(set), False)
       self.assertEqual(functions.passthrough(dict), False)

  the terminal updates to show an :doc:`AssertionError` for each line until I make the input match the output, proving that the passthrough function I have defined returns the input it is given. Hooray! I am geniuses again

Functions with positional arguments
-----------------------------------

I can define the function to take in more than one input, For instance if I am writing a function to perform operations on 2 numbers as I do in :doc:`calculator`\ , the function has to be able to accept the 2 numbers it performs operations on

RED: make it fail
^^^^^^^^^^^^^^^^^

add a new test to ``test_functions.py``, replacing ``my_first_name`` and ``my_last_name`` with your first and last names

.. code-block:: python

    def test_functions_with_positional_arguments(self):
      self.assertEqual(
       functions.passthrough_with_positional_arguments(
         'my_first_name', 'my_last_name'
       ),
       ('my_first_name', 'my_last_name')
      )

the terminal updates to show an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* update ``functions.py`` with the solution I know works from ``test_passthrough_function``
  .. code-block:: python

    def passthrough_with_positional_arguments(input_data):
      return input_data
  the terminal updates to show a :doc:`TypeError`
* change the signature of ``passthrough_with_positional_arguments`` to take in more than one argument
  .. code-block:: python

    def passthrough_with_positional_arguments(input_data, second_argument):
      return input_data
  the terminal updates to show an :doc:`AssertionError`
* update ``passthrough_with_positional_arguments`` to return the two arguments it receives
  .. code-block:: python

    def passthrough_with_positional_arguments(input_data, second_argument):
      return input_data, second_argument
  the terminal displays passing tests

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

How can I make this better?


* I called the first argument ``input_data`` and the second argument ``second_argument``. Technically, both arguments are input data, so I need a better name that is more descriptive, How can I make this better?
* modify the signature of ``passthrough_with_positional_arguments`` to use more descriptive names
  .. code-block:: python

    def passthrough_with_positional_arguments(first_argument, second_argument):
      return first_argument, second_argument
  I still have passing tests
* add another test to ensure that ``passthrough_with_positional_arguments`` outputs data in the order given. update ``test_functions_with_positional_arguments``
  .. code-block:: python

      def test_functions_with_positional_arguments(self):
       self.assertEqual(
         functions.passthrough_with_positional_arguments(
           'my_first_name', 'my_last_name'
         ),
         ('my_first_name', 'my_last_name')
       )
       self.assertEqual(
         functions.passthrough_with_positional_arguments(
           'my_last_name', 'my_first_name'
         ),
         ('my_first_name', 'my_last_name')
       )
  the terminal updates to show an :doc:`AssertionError`
* update the test to the correct output
  .. code-block:: python

      def test_functions_with_positional_arguments(self):
       self.assertEqual(
         functions.passthrough_with_positional_arguments(
           'my_first_name', 'my_last_name'
         ),
         ('my_first_name', 'my_last_name')
       )
       self.assertEqual(
         functions.passthrough_with_positional_arguments(
           'my_last_name', 'my_first_name'
         ),
         ('my_last_name', 'my_first_name')
       )
  the terminal updates to show passing tests
* the function only takes in 2 positional arguments, though there are scenarios where a function needs to take in more arguments. For instance, if I do not know the number of positional arguments that will be given before hand
* update ``test_functions_with_positional_arguments`` with tests for cases where the number of positional arguments received is not known
  .. code-block:: python

      def test_functions_with_positional_arguments(self):
       self.assertEqual(
         functions.passthrough_with_positional_arguments(
           'my_first_name', 'my_last_name'
         ),
         ('my_first_name', 'my_last_name')
       )
       self.assertEqual(
         functions.passthrough_with_positional_arguments(
           'my_last_name', 'my_first_name'
         ),
         ('my_last_name', 'my_first_name')
       )
       self.assertEqual(
         functions.passthrough_with_positional_arguments(
           0, 1, 2, 3
         ),
         (0, 1, 2, 3)
       )
       self.assertEqual(
         functions.passthrough_with_positional_arguments(
           bool, int, float, str, tuple, list, set, dict
         ),
         (bool, int, float, str, tuple, list, set, dict)
       )
  the terminal updates to show a :doc:`TypeError` because 2 positional arguments were expected by the function but 4 were given
* In python I can represent multiple arguments using a starred expression `see arbitrary argument lists <https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists>`_. Let us update the signature of ``functions_with_positional_arguments`` with a starred expression to take in any number of arguments
  .. code-block:: python

    def passthrough_with_positional_arguments(*arguments):
      return arguments
  the terminal updates to show passing tests

Functions with keyword arguments
--------------------------------

There is an inherent problem with using positional arguments in functions. It requires the inputs to always be supplied in the correct sequence. If the program is dependent on that sequence, then it will behave in an unintended way when it receives input out of order. There is a way to ensure the function behaves correctly regardless of what order the user provides the input - Keyword Arguments

RED: make it fail
^^^^^^^^^^^^^^^^^

add a new test to ``test_functions.py``

.. code-block:: python

    def test_functions_with_keyword_arguments(self):
      self.assertEqual(
       functions.passthrough_with_keyword_arguments(
         first_name='my_first_name',
         last_name='my_last_name'
       ),
       ('my_first_name', 'my_last_name')
      )

the terminal updates to show an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add a function definition to ``functions.py``
  .. code-block:: python

    def passthrough_with_keyword_arguments():
      return None
  the terminal displays
  .. code-block:: python

    TypeError: passthrough_with_keyword_arguments() got an unexpected keyword argument 'first_name'

* alter the function signature to take in a positional argument
  .. code-block:: python

   def passthrough_with_keyword_arguments(first_name):
    return None
  the terminal prints out
  .. code-block:: python

   TypeError: passthrough_with_keyword_arguments() got an unexpected keyword argument 'last_name'

* update the function signature to take in another positional argument
  .. code-block:: python

    def passthrough_with_keyword_arguments(first_name, last_name):
      return None
  the terminal updates to show an :doc:`AssertionError`
* adjust the return statement to make the test pass
  .. code-block:: python

    def passthrough_with_keyword_arguments(first_name, last_name):
      return first_name, last_name
  Eureka! the terminal updates to show passing tests

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

So far ``passthrough_with_keyword_arguments`` looks the same as ``passthrough_with_positional_arguments`` did when it took in 2 positional arguments, I have not yet seen a difference between a ``positional argument`` and a ``keyword argument``


*
  add a test that puts the input data out of order to see if there is a difference

  .. code-block:: python

      def test_functions_with_keyword_arguments(self):
       self.assertEqual(
         functions.passthrough_with_keyword_arguments(
           first_name='my_first_name',
           last_name='my_last_name'
         ),
         ('my_first_name', 'my_last_name')
       )
       self.assertEqual(
         functions.passthrough_with_keyword_arguments(
           last_name='my_last_name',
           first_name='my_first_name'
         ),
         ('my_first_name', 'my_last_name')
       )

  the terminal updates to show passing tests. Unlike in ``test_functions_with_positional_arguments`` using the name when passing inputs, ensures the function always displays output in the right order regardless of the order in which the input data is given

  the function currently only takes in 2 keyword arguments. What if I wanted a function that can take in any number of keyword arguments? There is a starred expression for keyword arguments - ``**``.

*
  RED: make it fail
  add a test to ``test_functions_with_keyword_arguments``

  .. code-block:: python

      def test_functions_with_keyword_arguments(self):
       self.assertEqual(
         functions.passthrough_with_keyword_arguments(
           first_name='my_first_name',
           last_name='my_last_name'
         ),
         ('my_first_name', 'my_last_name')
       )
       self.assertEqual(
         functions.passthrough_with_keyword_arguments(
           last_name='my_last_name',
           first_name='my_first_name'
         ),
         ('my_first_name', 'my_last_name')
       )
       self.assertEqual(
         functions.passthrough_with_keyword_arguments(
           a=1, b=2, c=3, d=4
         ),
         {}
       )

  the terminal updates to show a :doc:`TypeError`

*
  GREEN: make it pass


  * change the signature of ``passthrough_with_keyword_arguments`` to accept any number of keyword arguments
  .. code-block:: python

    def passthrough_with_keyword_arguments(**keyword_arguments):
      return keyword_arguments
   the terminal updates to show an :doc:`AssertionError` for the previous test that was passing. I have introduced a regression - the new code has caused an old passing test to fail.
  * update the expected result of ``test_functions_with_keyword_arguments`` from the terminal's output
  .. code-block:: python

    def test_functions_with_keyword_arguments(self):
    self.assertEqual(
      functions.passthrough_with_keyword_arguments(
        first_name='my_first_name',
        last_name='my_last_name'
      ),
      {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
    )
   the terminal updates to show an :doc:`AssertionError` for the next test that was passing. I have another regression
  * change the next test to make the output match the expectation
  .. code-block:: python

      def test_functions_with_keyword_arguments(self):
        self.assertEqual(
          functions.passthrough_with_keyword_arguments(
            first_name='my_first_name',
            last_name='my_last_name'
          ),
          {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
        )
        self.assertEqual(
          functions.passthrough_with_keyword_arguments(
            last_name='my_last_name',
            first_name='my_first_name'
          ),
          {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
        )
   the terminal updates to show an :doc:`AssertionError` for the last test I added
  * time to match the last test to the expected value in the comparison
  .. code-block:: python

    def test_functions_with_keyword_arguments(self):
    self.assertEqual(
      functions.passthrough_with_keyword_arguments(
        first_name='my_first_name',
        last_name='my_last_name'
      ),
      {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
    )
    self.assertEqual(
      functions.passthrough_with_keyword_arguments(
        last_name='my_last_name',
        first_name='my_first_name'
      ),
      {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
    )
    self.assertEqual(
      functions.passthrough_with_keyword_arguments(
        a=1, b=2, c=3, d=4
      ),
      {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    )
   the terminal updates to show passing tests. From the tests I can see that keyword arguments are treated as :doc:`data structures: dictionaries` in python

*
  REFACTOR: make it better

  add one more test to ``test_functions_with_keyword_arguments`` to drill the lesson

  .. code-block:: python

      def test_functions_with_keyword_arguments(self):
       self.assertEqual(
         functions.passthrough_with_keyword_arguments(
           first_name='my_first_name',
           last_name='my_last_name'
         ),
         {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
       )
       self.assertEqual(
         functions.passthrough_with_keyword_arguments(
           last_name='my_last_name',
           first_name='my_first_name'
         ),
         {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
       )
       self.assertEqual(
         functions.passthrough_with_keyword_arguments(
           a=1, b=2, c=3, d=4
         ),
         {'a': 1, 'b': 2, 'c': 3, 'd': 4}
       )
       self.assertEqual(
         functions.passthrough_with_keyword_arguments(
           a_boolean=bool,
           an_integer=int,
           a_float=float,
           a_string=str,
           a_tuple=tuple,
           a_list=list,
           a_set=set,
           a_dictionary=dict
         ),
         {}
       )

  the terminal updates to show an :doc:`AssertionError` and I update the test with the right values to make the test pass

  .. code-block:: python

      self.assertEqual(
       functions.passthrough_with_keyword_arguments(
         a_boolean=bool,
         an_integer=int,
         a_float=float,
         a_string=str,
         a_tuple=tuple,
         a_list=list,
         a_set=set,
         a_dictionary=dict
       ),
       {
         'a_boolean': bool,
         'an_integer': int,
         'a_float': float,
         'a_string': str,
         'a_tuple': tuple,
         'a_list': list,
         'a_set': set,
         'a_dictionary': dict
       }
      )

Functions with positional and keyword arguments
-----------------------------------------------

I could also define functions to take in both positional arguments and keyword arguments

RED: make it fail
^^^^^^^^^^^^^^^^^

add a new failing test to ``test_functions.py``

.. code-block:: python

    def test_functions_with_positional_and_keyword_arguments(self):
      self.assertEqual(
       functions.accepts_positional_and_keyword_arguments(
         last_name='my_last_name', 'my_first_name'
       ),
       {}
      )

the terminal updates to show a ``SyntaxError`` because I put a positional argument after a keyword argument and I update the running list of exceptions encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError
  # AttributeError
  # TypeError
  # SyntaxError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* fix the order of arguments in ``test_functions_with_positional_and_keyword_arguments``
  .. code-block:: python

    def test_functions_with_positional_and_keyword_arguments(self):
      self.assertEqual(
       functions.accepts_positional_and_keyword_arguments('my_first_name', last_name='my_last_name'),
       {}
      )
  the terminal updates to show an :doc:`AttributeError`
* add a definition for the function to ``functions.py``
  .. code-block:: python

    def accepts_positional_and_keyword_arguments():
      return None
  the terminal updates to show a :doc:`TypeError`
  .. code-block:: python

    TypeError: accepts_positional_and_keyword_arguments() got an unexpected keyword argument 'last_name'

* modify the function signature to take in an argument
  .. code-block:: python

    def accepts_positional_and_keyword_arguments(last_name):
      return None
  the terminal updates to show another :doc:`TypeError`
  .. code-block:: python

    TypeError: accepts_positional_and_keyword_arguments() got multiple values for argument 'last_name'

* add another argument to the function signature
  .. code-block:: python

    def accepts_positional_and_keyword_arguments(last_name, first_name):
      return None
  the terminal shows the same error even though I have 2 different arguments. I need a way to let the program know which argument is positional and which is a keyword argument
* reorder the arguments in the signature
  .. code-block:: python

    def accepts_positional_and_keyword_arguments(first_name, last_name):
      return None
  the terminal updates to show an :doc:`AssertionError`
* edit the return statement to make the test pass
  .. code-block:: python

    def accepts_positional_and_keyword_arguments(first_name, last_name):
      return first_name, last_name
  the terminal updates the :doc:`AssertionError` with the values I just added
* modify ``test_functions_with_positional_and_keyword_arguments`` to make the results match the expectation
  .. code-block:: python

      def test_functions_with_positional_and_keyword_arguments(self):
       self.assertEqual(
         functions.accepts_positional_and_keyword_arguments(
           'my_first_name', last_name='my_last_name'
         ),
         ('my_first_name', 'my_last_name')
       )
  the terminal displays passing tests

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Hold on a second. This looks exactly like what I did in ``test_functions_with_positional_arguments``. I cannot tell from the function signature which argument is positional and which is a keyword argument and do not want to wait for the function to fail when I send in values to figure it out


* change the function signature of ``accepts_positional_and_keyword_arguments`` to have a default value for the keyword argument
  .. code-block:: python

    def accepts_positional_and_keyword_arguments(first_name, last_name=None):
      return first_name, last_name
  all tests are still passing
* I did not add a default argument for ``first_name``, What if I test What would happen if I did
  .. code-block:: python

    def accepts_positional_and_keyword_arguments(first_name=None, last_name=None):
      return first_name, last_name
  I still have passing tests. It looks like python lets us use default arguments with no issues, and I can provide keyword arguments positionally without using the name. add another test to prove this
* add a test to ``test_functions_with_positional_and_keyword_arguments``
  .. code-block:: python

      def test_functions_with_positional_and_keyword_arguments(self):
       self.assertEqual(
         functions.accepts_positional_and_keyword_arguments(
           'my_first_name', last_name='my_last_name'
         ),
         ('my_first_name', 'my_last_name')
       )
       self.assertEqual(
         functions.accepts_positional_and_keyword_arguments(
           'my_first_name', 'my_last_name'
         ),
         ('my_first_name', 'my_last_name')
       )
  all the tests are still passing. The problem here is without the names the program is going to take the input data in the order I provide it so it is better to be explicit with the names because from the `Zen of Python <https://peps.python.org/pep-0020/>`_ ``Explicit is better than implicit.``
* add 2 tests, this time for an unknown number of positional and keyword arguments
  .. code-block:: python

    def test_functions_with_positional_and_keyword_arguments(self):
      self.assertEqual(
       functions.accepts_positional_and_keyword_arguments(
         'my_first_name', last_name='my_last_name'
       ),
       ('my_first_name', 'my_last_name')
      )
      self.assertEqual(
       functions.accepts_positional_and_keyword_arguments(
         'my_first_name', 'my_last_name'
       ),
       ('my_first_name', 'my_last_name')
      )
      self.assertEqual(
       functions.accepts_positional_and_keyword_arguments(),
       (None, None)
      )
      self.assertEqual(
       functions.accepts_positional_and_keyword_arguments(
         bool, int, float, str, tuple, list, set, dict,
         a_boolean=bool, an_integer=int, a_float=float,
         a_string=str, a_tuple=tuple, a_list=list,
         a_set=set, a_dictionary=dict
       ),
       ()
      )
  the terminal updates to show a :doc:`TypeError` because the function signature specifically only has two keyword arguments which are not provided in the call
* using what I know from previous tests I can alter the function to use starred expressions
  .. code-block:: python

    def accepts_positional_and_keyword_arguments(*args, **kwargs):
      return args, kwargs
  the terminal updates to show a failure for a previous passing test
  .. code-block:: python

      def test_functions_with_positional_and_keyword_arguments(self):
    >    self.assertEqual(
         functions.accepts_positional_and_keyword_arguments('my_first_name', last_name='my_last_name'),
         ('my_first_name', 'my_last_name')
       )
    E    AssertionError: Tuples differ: (('my_first_name',), {'last_name': 'my_last_name'}) != ('my_first_name', 'my_last_name')

* I will comment out the other tests for a bit, so I can focus on the failing test
  .. code-block:: python

      def test_functions_with_positional_and_keyword_arguments(self):
       self.assertEqual(
         functions.accepts_positional_and_keyword_arguments(
           'my_first_name', last_name='my_last_name'
         ),
         ('my_first_name', 'my_last_name')
       )
       # self.assertEqual(
       #  functions.accepts_positional_and_keyword_arguments(
       #    'my_first_name', 'my_last_name'
       #  ),
       #   (('my_first_name', 'last_name'), {})
       # )
       # self.assertEqual(
       #   functions.accepts_positional_and_keyword_arguments(),
       #   (None, None)
       # )
       # self.assertEqual(
       # functions.accepts_positional_and_keyword_arguments(
       #   bool, int, float, str, tuple, list, set, dict,a_boolean=bool, an_integer=int, a_float=float,a_string=str, a_tuple=tuple, a_list=list, a_set=set,
       #   a_dictionary=dict
       #   ),
       #   ()
       # )

* update the expected values in the test to make it pass
  .. code-block:: python

       self.assertEqual(
         functions.accepts_positional_and_keyword_arguments(
           'my_first_name', last_name='my_last_name'
         ),
         (('my_first_name',), {'last_name': 'my_last_name'})
       )
  the terminal updates to show tests passing, with the positional argument in parentheses and the keyword argument in curly braces
* uncomment the next test
  .. code-block:: python

       self.assertEqual(
         functions.accepts_positional_and_keyword_arguments(
           'my_first_name', 'my_last_name'
         ),
         (('my_first_name', 'last_name'), {})
       )
  the terminal updates to show
  .. code-block:: python

    >    self.assertEqual(
         functions.accepts_positional_and_keyword_arguments('my_first_name', 'my_last_name'),
         (('my_first_name', 'last_name'), {})
       )
    E    AssertionError: Tuples differ: (('my_first_name', 'my_last_name'), {}) != (('my_first_name', 'last_name'), {})

* update the test to make it pass with both positional arguments in parentheses and empty curly braces since there are no keyword arguments
  .. code-block:: python

       self.assertEqual(
         functions.accepts_positional_and_keyword_arguments(
           'my_first_name', 'my_last_name'
         ),
         (('my_first_name', 'my_last_name'), {})
       )
  the terminal updates to show passing tests
* uncomment the next test to see it fail
  .. code-block:: python

       self.assertEqual(
         functions.accepts_positional_and_keyword_arguments(),
         (None, None)
       )
  the terminal updates to show an :doc:`AssertionError`
  .. code-block:: python

    AssertionError: Tuples differ: ((), {}) != (None, None)

* update the test to make it pass with empty parentheses and curly braces as the expectation since no positional or keyword arguments were provided as inputs
  .. code-block:: python

       self.assertEqual(
         functions.accepts_positional_and_keyword_arguments(),
         ((), {})
       )

* uncomment the last test to see it fail and the terminal updates to show an :doc:`AssertionError`
  .. code-block:: python

    AssertionError: Tuples differ: ((<class 'bool'>, <class 'int'>, <class 'f[307 chars]t'>}) != ()

* update the test to make it pass
  .. code-block:: python

       self.assertEqual(
         functions.accepts_positional_and_keyword_arguments(
           bool, int, float, str, tuple, list, set, dict,
           a_boolean=bool, an_integer=int, a_float=float,
           a_string=str, a_tuple=tuple, a_list=list,
           a_set=set, a_dictionary=dict
         ),
         (
           (bool, int, float, str, tuple, list, set, dict,),
           {
            'a_boolean': bool,
            'an_integer': int,
            'a_float': float,
            'a_string': str,
            'a_tuple': tuple,
            'a_list': list,
            'a_set': set,
            'a_dictionary': dict
           }
         )
       )
  the terminal updates to show passing tests
* From what I have seen so far, in python

  * positional arguments are represented as :doc:`tuples` with parentheses - ``()``
  * keyword arguments are represented as :doc:`data structures: dictionaries` with curly braces - ``{}``
  * I can use ``*name`` to represent any number of positional arguments
  * I can use ``**name`` to represent any number of keyword arguments
  * I can define default values for arguments
  * positional arguments must come before keyword arguments

Singleton Functions
-------------------

A singleton function is a function that returns the same thing every time it is called.

RED: make it fail
^^^^^^^^^^^^^^^^^

add a test to ``test_functions.py``

.. code-block:: python

    def test_singleton_function(self):
      self.assertEqual(functions.singleton(), 'my_first_name')

the terminal updates to show an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update ``functions.py`` to make it pass

.. code-block:: python

  def singleton():
    return 'my_first_name'

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

add a new test that checks if a singleton that accepts inputs returns the same value when it is given inputs


* update ``test_functions.py``
  .. code-block:: python

      def test_singleton_function_with_input(self):
       self.assertEqual(functions.singleton_with_input('Bob', 'James', 'Frank'), 'joe')
       self.assertEqual(functions.singleton_with_input('a', 2, 'c', 3), 'joe')
  the terminal updates to show an :doc:`AttributeError`
* add a function for ``singleton_with_inputs`` to ``functions.py`` to make the test pass
  .. code-block:: python

    def singleton_with_inputs(*args):
      return 'joe'

*WELL DONE!*
You now know


* that singleton functions return the same thing every time they are called
* that positional arguments are represented as :doc:`tuples` with parentheses - ``()``
* that keyword arguments are represented as :doc:`data structures: dictionaries` with curly braces - ``{}``
* how to write functions in python that can take in any number of positional or keyword arguments as inputs
* I can use ``*name`` to represent any number of positional arguments
* I can use ``**name`` to represent any number of keyword arguments
* I can define default values for arguments
* positional arguments must come before keyword arguments

Do you want to read more?


* `functions <https://docs.python.org/3/glossary.html#term-function>`_
* `methods <https://docs.python.org/3/glossary.html#term-method>`_
* `parameters <https://docs.python.org/3/glossary.html#term-parameter>`_
* `function definitions <https://docs.python.org/3/reference/compound_stmts.html#function-definitions>`_
* `nested scope <https://docs.python.org/3/glossary.html#term-nested-scope>`_
