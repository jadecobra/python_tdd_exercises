.. meta::
   :description: Learn Python functions with TDD! Explore arguments, defaults, and testing techniques in this practical guide. Start coding now!
   :keywords: Jacob Itegboje, Python functions, Test-Driven Development, Python programming, keyword arguments, positional arguments, coding tutorial

.. include:: links.rst

.. _function: https://docs.python.org/3/glossary.html#term-function
.. _functions: function_

#################################################################################
functions
#################################################################################

A function_ is a unit or block of code that is callable_. This means I can write statements that I can use to do something at a different time from when I write them. They can make code smaller, easier to read, test, reuse, maintain and improve.

`Computer Programming` involves providing a process with input data and the process returning output data, for example

.. code-block:: python

    input_data -> program -> output_data

I think of it mathematically as mapping a :ref:`function<test_functions>` ``f`` with inputs ``x`` and an output of ``y``

.. math::

  f(x) -> y

in other words

.. code-block:: python

  function(input_data) -> output_data

the function_ processes ``input_data`` and returns ``output_data`` as the result

functions_ are made with the def_ keyword, a name, parentheses and a colon at the end

.. code-block:: python

  def name_of_function():

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with functions_ as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh functions

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: python

      ./makePythonTdd.ps1 functions

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_functions.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_functions.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change ``True`` to ``False`` to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestFunctions(unittest.TestCase):

*********************************************************************************
test_making_a_function_w_pass
*********************************************************************************

I can make a function_ with the pass_ keyword

red: make it fail
#################################################################################

* I change ``test_failure`` to ``test_making_a_function_w_pass``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    import unittest


    class TestFunctions(unittest.TestCase):

        def test_making_a_function_w_pass(self):
            self.assertIsNone(src.functions.w_pass())


    # Exceptions Encountered

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block::

    NameError: name 'src' is not defined

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # NameError

green: make it pass
#################################################################################

* I add an `import statement`_ at the top of the file

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.functions
    import unittest


    class TestFunctions(unittest.TestCase):

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.functions' has no attribute 'function_w_pass'

* I add to the list of :ref:`Exceptions<errors>` encountered

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* I click on ``functions.py`` in the ``src`` folder to open it in the :ref:`editor<2 editors>`, then I add a function_ definition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def w_pass():
        pass

  the test passes

  * the test checks if the result of the call to ``src.functions.w_pass`` is :ref:`None`
  * the function_ definition simply says pass_ and the test passes
  * pass_ is a placeholder keyword which allows the function_ definition to follow Python_ language rules
  * the test passes because all functions_ return :ref:`None` by default, as if the function_ has an invisible line that says ``return None``, which leads me to the next test

----

*********************************************************************************
test_making_a_function_w_return
*********************************************************************************

I can make a function with a `return statement`_

red: make it fail
#################################################################################

I add a new failing test in ``test_functions.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 4-5

      def test_making_a_function_w_pass(self):
          self.assertIsNone(src.functions.w_pass())

      def test_making_a_function_w_return(self):
          self.assertIsNone(src.functions.w_return())


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'function_w_return'

green: make it pass
#################################################################################

I add a new function_ to ``functions.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 5-6

  def w_pass():
      pass


  def w_return(self):
      pass

the test passes

refactor: make it better
#################################################################################

I change pass_ to a `return statement`_

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 2

  def w_return():
      return

the test is still green. I have 2 functions_ with different statements in their body but they both return :ref:`None`, because "all functions_ return :ref:`None` by default, as if the function_ has an invisible line that says ``return None``", which leads me to the next test

*********************************************************************************
test_making_a_function_w_return_none
*********************************************************************************

I can make a function_ with a `return statement`_ that says what the function_ returns

red: make it fail
################################################################################

I add another failing test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 4-5

      def test_making_a_function_w_return(self):
          self.assertIsNone(src.functions.w_return())

      def test_making_a_function_w_return_none(self):
          self.assertIsNone(src.functions.w_return_none())


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_return_none'

green: make it pass
################################################################################

I add a function_ definition to ``functions.py``

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 5-6

  def w_return():
      return


  def w_return_none():
      return

the test passes

refactor: make it better
################################################################################

I add :ref:`None` to the `return statement`_

.. code-block:: python

  def w_return_none():
      return None

From the :PEP:`Zen of Python <20>`: ``Explicit is better than implicit.``, I like to write my functions_ this way. Anyone can tell what the function_ returns without knowing what it does or even understanding Python_ code

----

*********************************************************************************
test_constant_function
*********************************************************************************

constant functions_ always return the same thing when called

red: make it fail
#################################################################################

I add a test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 4-5

    def test_making_a_function_w_return_none(self):
        self.assertIsNone(src.functions.w_return_none())

    def test_constant_function(self):
        self.assertEqual(
            src.functions.constant(),
            'the same thing'
        )

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'constant'

green: make it pass
#################################################################################

I add the function_ to ``functions.py``

.. code-block:: python
  :lineno-start: 9
  :emphasize-lines: 5-6

  def w_return_none():
      return None


  def constant():
      return None

the terminal shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: None != 'the same thing'

I change the `return statement`_

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 2

  def constant():
      return 'the same thing'

the test passes. A constant function_ always return the same thing when called, I can use them in place of variables_, though the number of cases where they are faster than variables_ for constants, is pretty small. It is something like if the function_ is only called less than 10 times, but who's counting?

----

*********************************************************************************
test_identity_function
*********************************************************************************

The identity function_ returns its input as output, it's also in the :ref:`Truth Table<booleans: truth table>` chapter in `test_logical_identity`

red: make it fail
################################################################################

I add a failing test in ``test_functions.py``

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 7-8

      def test_constant_function(self):
          self.assertEqual(
              src.functions.constant(),
              'the same thing'
          )

      def test_identity_function(self):
          self.assertIsNone(src.functions.identity(None))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'identity'

green: make it pass
################################################################################

* I add a function_ to ``functions.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5-6

    def constant():
        return 'the same thing'


    def identity():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: identity() takes 0 positional arguments but 1 was given

  the definition for ``identity`` does not allow inputs and the test sends :ref:`None` as input

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 5

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add a name in parentheses for the ``identity`` function_ to take input in ``functions.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1

    def identity(argument):
        return None

  the test passes. I am genius

refactor: make it better
################################################################################

The definition for the :ref:`identity function<test_logical_identity>` is that it returns the same thing it is given, the test passes when :ref:`None` is given as input, will it still pass when another value is given or will it always return :ref:`None`? Time to write a test

* I add a new :ref:`assertion<AssertionError>` to ``test_identity_function`` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3

    def test_identity_function(self):
        self.assertIsNone(src.functions.identity(None))
        self.assertEqual(src.functions.identity(object), object)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != <class 'object'>

  the function_ returns :ref:`None` instead of ``<class 'object'>`` in the second case, I am not all the way genius, yet

* I change the `return statement`_ of ``identity`` in ``functions.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

    def identity(argument):
        return argument

  the test passes

----

The :ref:`Identity Function<test_identity_function>` takes 1 argument, the following tests are for functions_ that take more than one input

*********************************************************************************
test_functions_w_positional_arguments
*********************************************************************************

red: make it fail
################################################################################

I add a failing test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 5-9

      def test_identity_function(self):
          self.assertIsNone(src.functions.identity(None))
          self.assertEqual(src.functions.identity(object), object)

      def test_functions_w_positional_arguments(self):
          self.assertEqual(
              src.functions.w_positional_arguments('first', 'last'),
              ('first', 'last')
          )


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_positional_arguments'

green: make it pass
################################################################################

* I add a function_ to  ``functions.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5-6

    def identity(argument):
        return argument


    def w_positional_arguments():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_positional_arguments() takes 0 positional arguments but 2 were given

* I make the function_ take input by adding a name in parentheses

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 1

    def w_positional_arguments(first):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: w_positional_arguments() takes 1 positional argument but 2 were given

* I make ``w_positional_arguments`` take another input by adding another name in parentheses

  .. code-block:: python

    def w_positional_arguments(first, last):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != ('first', 'last')

* I change the `return statement`_

  .. code-block:: python

    def w_positional_arguments(first, last):
        return first, last

  the test passes

refactor: make it better
################################################################################

* The problem with giving arguments this way is that they have to be in the order the function_ expects or I get a different behavior. I add a test to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 6-9

        def test_functions_w_positional_arguments(self):
            self.assertEqual(
                src.functions.w_positional_arguments('first', 'last'),
                ('first', 'last')
            )
            self.assertEqual(
                src.functions.w_positional_arguments('last', 'first'),
                ('first', 'last')
            )


    # Exceptions Encountered

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ('last', 'first') != ('first', 'last')

* I change the expectation of the test in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 3

          self.assertEqual(
              src.functions.w_positional_arguments('last', 'first'),
              ('last', 'first')
          )

  the test passes

----

*********************************************************************************
test_functions_w_keyword_arguments
*********************************************************************************

There is a problem with using positional arguments, the inputs must always be supplied in the right order. which means the program_ will behave in an unexpected way when it receives input out of order.

To make sure the function_ behaves how I want even when I send input out of order I can use Keyword Arguments

red: make it fail
################################################################################

I add a new test to ``test_functions.py``

.. code-block:: python
  :lineno-start: 31
  :emphasize-lines: 6-12

        self.assertEqual(
            src.functions.w_positional_arguments('last', 'first'),
            ('last', 'first')
        )

    def test_functions_w_keyword_arguments(self):
        self.assertEqual(
            src.functions.w_keyword_arguments(
                first='first', last='last',
            ),
            ('first', 'last')
        )

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.functions' has no attribute 'w_keyword_arguments'

green: make it pass
################################################################################

* I add a function_ definition to ``functions.py``

  .. code-block:: python

    def take_keyword_arguments():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: take_keyword_arguments() got an unexpected keyword argument 'first_name'

  I add the argument_ to the defintion

  .. code-block:: python

    def take_keyword_arguments(first_name):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python
    :force:

    TypeError: take_keyword_arguments() got an unexpected keyword argument 'last_name'. Did you mean 'first_name'?

  I add the argument

  .. code-block:: python

    def take_keyword_arguments(first_name, last_name):
        return None

  the terminal_ shows :ref:`AssertionError`

    AssertionError: None != ('first_name', 'last_name')

  I change the `return statement`_

  .. code-block:: python

    def take_keyword_arguments(first_name, last_name):
        return ('first_name', 'last_name')

  the test passes

refactor: make it better
################################################################################

* So far ``take_keyword_arguments`` looks the same as ``take_positional_arguments``, I have not yet seen a difference between a ``positional argument`` and a ``keyword argument``. I add an :ref:`assertion<AssertionError>` that puts the input data out of order to see if there is a difference

  .. code-block:: python

      def test_functions_w_keyword_arguments(self):
          self.assertEqual(
              functions.take_keyword_arguments(
                  first_name='first_name',
                  last_name='last_name'
              ),
              ('first_name', 'last_name')
          )
          self.assertEqual(
              src.functions.take_keyword_arguments(
                  last_name='last_name',
                  first_name='first_name',
              ),
              ('last_name', 'first_name')
          )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ('first_name', 'last_name') != ('last_name', 'first_name')

  the order stayed the same. I change the expectation to make the test pass

  .. code-block:: python

    self.assertEqual(
        src.functions.take_keyword_arguments(
            last_name='last_name',
            first_name='first_name',
        ),
        ('first_name', 'last_name')
    )

  the test passes. Keyword Arguments allow the input to be passed in any order


# ADD examples with dictionary as input

----

*********************************************************************************
test_functions_w_unknown_keyword_arguments
*********************************************************************************

* The function_ currently only takes in 2 keyword arguments. What if I want a function_ that can take in any number of keyword arguments? There is a starred expression for keyword arguments - ``**``. I add an :ref:`assertion<AssertionError>`

  .. code-block:: python

    def test_functions_w_unknown_keyword_arguments(self):
        self.assertEqual(
            src.functions.take_unknown_keyword_arguments(
                a=1, b=2, c=3, d=4
            ),
            None
        )

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.functions' has no attribute 'take_unknown_keyword_arguments'. Did you mean: 'take_keyword_arguments'?

  I add a function_ using a `starred expression`_

  .. code-block:: python

    def take_unknown_keyword_arguments(*arguments):
        return arguments

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: take_unknown_keyword_arguments() got an unexpected keyword argument 'a'

  the `starred expression`_ for keyword arguments is different, I change the function_

  .. code-block:: python

    def take_unknown_keyword_arguments(**keyword_arguments):
        return keyword_arguments

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'a': 1, 'b': 2, 'c': 3, 'd': 4} != None

  I change the expectation in the test to match

  .. code-block:: python

    def test_functions_w_unknown_keyword_arguments(self):
        self.assertEqual(
            src.functions.take_unknown_keyword_arguments(
                a=1, b=2, c=3, d=4
            ),
            {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        )

  the test passes

* I add another :ref:`assertion<AssertionError>` with a different number of inputs

  .. code-block:: python

    self.assertEqual(
        src.functions.take_unknown_keyword_arguments(
            a=1, b=2, c=3, d=4
        ),
        {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    )
    self.assertEqual(
        src.functions.take_unknown_keyword_arguments(
            none=None,
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

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python
    :force:

    AssertionError: {'none': None, 'a_boolean': <class 'bool'>[190 chars]ct'>} != {}

  I change the expectation to match the values in the terminal_

  .. code-block:: python

    self.assertEqual(
        src.functions.take_unknown_keyword_arguments(
            none=None,
            a_boolean=bool,
            an_integer=int,
            a_float=float,
            a_string=str,
            a_tuple=tuple,
            a_list=list,
            a_set=set,
            a_dictionary=dict
        ),
        dict(
            a_boolean=bool,
            a_dictionary=dict,
            a_float=float,
            a_list=list,
            a_set=set,
            a_string=str,
            a_tuple=tuple,
            an_integer=int,
            none=None,
        )
    )

  the test passes

# ADD examples with dictionary as input

----

*********************************************************************************
test_functions_w_positional_and_keyword_arguments
*********************************************************************************

red: make it fail
#################################################################################

I can also define functions_ to take both positional arguments and keyword arguments as inputs. I add a new failing test to ``test_functions.py``

.. code-block:: python

    def test_functions_w_positional_and_keyword_arguments(self):
        self.assertEqual(
        functions.take_positional_and_keyword_arguments(
            last_name='last_name', 'first_name'
        ),
        {}
      )

the terminal_ shows a SyntaxError_ because I put a positional argument
after a keyword argument. I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_functions.py``

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError
  # AttributeError
  # TypeError
  # SyntaxError

green: make it pass
#################################################################################

* I fix the order of arguments in ``test_functions_w_positional_and_keyword_arguments`` since keyword arguments come after positional arguments

  .. code-block:: python

    def test_functions_w_positional_and_keyword_arguments(self):
        self.assertEqual(
            functions.take_positional_and_keyword_arguments(
                'first_name', last_name='last_name'
            ),
            {}
        )

  the terminal_ shows :ref:`AttributeError`
* I add a definition for the function_ to ``functions.py``

  .. code-block:: python

    def take_positional_and_keyword_arguments():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: take_positional_and_keyword_arguments() got an unexpected keyword argument 'last_name'

* I make the function_ definition to take in an argument

  .. code-block:: python

    def take_positional_and_keyword_arguments(last_name):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: take_positional_and_keyword_arguments() got multiple values for argument 'last_name'

* I add another argument to the function_ definition

  .. code-block:: python

    def take_positional_and_keyword_arguments(last_name, first_name):
        return None

  the terminal_ shows the same error even though I have 2 different arguments. I need a way to let the ``take_positional_and_keyword_arguments`` know which argument is positional and which is a keyword argument
* I reorder the arguments in the definition

  .. code-block:: python

    def take_positional_and_keyword_arguments(first_name, last_name):
        return None

  the terminal_ shows :ref:`AssertionError`
* I edit the `return statement`_ to make the test pass

  .. code-block:: python

    def take_positional_and_keyword_arguments(first_name, last_name):
        return first_name, last_name

  the terminal_ shows :ref:`AssertionError` with the values I just added
* I make ``test_functions_w_positional_and_keyword_arguments`` to make the results match the expectation

  .. code-block:: python

      def test_functions_w_positional_and_keyword_arguments(self):
          self.assertEqual(
          functions.take_positional_and_keyword_arguments(
                  'first_name', last_name='last_name'
              ),
              ('first_name', 'last_name')
          )

  the test passes


refactor: make it better
#################################################################################

Hold on a second. This looks exactly like what I did in ``test_functions_w_positional_arguments``. I cannot tell from the function_ definition which argument is positional and which is a keyword argument and do not want to wait for the function_ to fail when I send in values to find out

* I make the definition of ``take_positional_and_keyword_arguments`` to have a default value for the keyword argument

  .. code-block:: python

    def take_positional_and_keyword_arguments(first_name, last_name=None):
        return first_name, last_name

  all tests are still passing

* I did not add a default argument for ``first_name``, what would happen if I did?

  .. code-block:: python

    def take_positional_and_keyword_arguments(first_name=None, last_name=None):
        return first_name, last_name

  I still have passing tests. It looks likelets us use default arguments with no issues, and I can provide keyword arguments positionally without using the name.

* I add another test to ``test_functions_w_positional_and_keyword_arguments`` to show this

  .. code-block:: python

      def test_functions_w_positional_and_keyword_arguments(self):
          self.assertEqual(
              functions.take_positional_and_keyword_arguments(
                  'first_name', last_name='last_name'
              ),
              ('first_name', 'last_name')
          )
          self.assertEqual(
              functions.take_positional_and_keyword_arguments(
                  'first_name', 'last_name'
              ),
              ('first_name', 'last_name')
          )

  all the tests are still passing. The problem here is without the names the program is going to take the input data in the order I provide it so it is better to be explicit with the names, from the :PEP:`Zen of Python <20>`: ``Explicit is better than implicit.``
* I add 2 tests, this time for an unknown number of positional and keyword arguments

  .. code-block:: python

    def test_functions_w_positional_and_keyword_arguments(self):
        self.assertEqual(
            functions.take_positional_and_keyword_arguments(
                'first_name', last_name='last_name'
            ),
            ('first_name', 'last_name')
        )
        self.assertEqual(
            functions.take_positional_and_keyword_arguments(
                'first_name', 'last_name'
            ),
            ('first_name', 'last_name')
        )
        self.assertEqual(
            functions.take_positional_and_keyword_arguments(),
            (None, None)
        )
        self.assertEqual(
            functions.take_positional_and_keyword_arguments(
                bool, int, float, str, tuple, list, set, dict,
                a_boolean=bool, an_integer=int, a_float=float,
                a_string=str, a_tuple=tuple, a_list=list,
                a_set=set, a_dictionary=dict
            ),
            ()
        )

  the terminal_ shows :ref:`TypeError` because the function_ definition only has 2 keyword arguments which are not provided in the call

* using what I know from previous tests I can alter the function_ to use starred expressions

  .. code-block:: python

    def take_positional_and_keyword_arguments(*args, **kwargs):
        return args, kwargs

  the terminal_ shows :ref:`AssertionError` for a previous passing test. I have introduced a regression

  .. code-block:: python

    E   AssertionError: Tuples differ: (('first_name',), {'last_name': 'last_name'}) != ('first_name', 'last_name')

* I comment out the other :ref:`assertions<AssertionError>` so I can focus on the failing test

  .. code-block:: python

      def test_functions_w_positional_and_keyword_arguments(self):
          self.assertEqual(
            functions.take_positional_and_keyword_arguments(
              'first_name', last_name='last_name'
            ),
            ('first_name', 'last_name')
          )
          # self.assertEqual(
          #    functions.take_positional_and_keyword_arguments(
          #        'first_name', 'last_name'
          #    ),
          #    (('first_name', 'last_name'), {})
          # )
          # self.assertEqual(
          #     functions.take_positional_and_keyword_arguments(),
          #     (None, None)
          # )
          # self.assertEqual(
          #    functions.take_positional_and_keyword_arguments(
          #        bool, int, float, str, tuple, list, set, dict,
          #        a_boolean=bool, an_integer=int, a_float=float,
          #        a_string=str, a_tuple=tuple, a_list=list,
          #        a_set=set, a_dictionary=dict
          #    ),
          #    ()
          # )

* I change the expected values in the test to make it pass

  .. code-block:: python

    self.assertEqual(
        functions.take_positional_and_keyword_arguments(
            'first_name', last_name='last_name'
        ),
        (('first_name',), {'last_name': 'last_name'})
    )

  the terminal_ shows tests passing, with the positional argument in parentheses and the keyword argument in curly braces
* I uncomment the next test

  .. code-block:: python

    self.assertEqual(
        functions.take_positional_and_keyword_arguments(
            'first_name', 'last_name'
        ),
        (('first_name', 'last_name'), {})
    )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E    AssertionError: Tuples differ: (('first_name', 'last_name'), {}) != (('first_name', 'last_name'), {})

* I make the test pass with both positional arguments in parentheses and empty curly braces since there are no keyword arguments

  .. code-block:: python

      self.assertEqual(
          functions.take_positional_and_keyword_arguments(
              'first_name', 'last_name'
          ),
          (('first_name', 'last_name'), {})
      )

  the test passes

* I uncomment the next test to see it fail

  .. code-block:: python

      self.assertEqual(
          functions.take_positional_and_keyword_arguments(),
          (None, None)
      )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ((), {}) != (None, None)

* I make the test pass with empty parentheses and curly braces as the expectation since no positional or keyword arguments were provided as inputs

  .. code-block:: python

    self.assertEqual(
        functions.take_positional_and_keyword_arguments(),
        ((), {})
    )

* I uncomment the last test to see it fail the terminal_ shows :ref:`AssertionError`

  .. code-block::

    AssertionError: Tuples differ: ((<class 'bool'>, <class 'int'>, <class 'f[307 chars]t'>}) != ()

* I make the test pass

  .. code-block:: python

      self.assertEqual(
          functions.take_positional_and_keyword_arguments(
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

----

*********************************************************************************
test_functions_w_unknown_positional_and_keyword_arguments
*********************************************************************************

red: make it fail
#################################################################################


green: make it pass
#################################################################################


refactor: make it better
#################################################################################


----

*********************************************************************************
test_functions_w_default_arguments
*********************************************************************************

red: make it fail
#################################################################################


green: make it pass
#################################################################################


refactor: make it better
#################################################################################

----

*********************************************************************************
test_functions_w_unknown_arguments
*********************************************************************************

red: make it fail
#################################################################################


green: make it pass
#################################################################################


refactor: make it better
#################################################################################

----

*********************************************************************************
review
*********************************************************************************

the tests show that

* I can define default values for arguments
* positional arguments must come before keyword arguments
* I can use ``**kwargs`` to represent any number of keyword arguments
* keyword arguments are represented as :ref:`dictionaries`
* I can use ``*args`` to represent any number of positional arguments
* positional arguments are represented as tuples_
* :ref:`identity functions<test_identity_function>` return their input
* :ref:`constant functions<test_constant_function>` always return the same thing
* functions_ return :ref:`None` by default
* functions_ are defined using the def_ keyword

Would you like to :ref:`test classes?<classes>`

----

:ref:`Click Here to see the code from this chapter<functions: tests and solutions>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->