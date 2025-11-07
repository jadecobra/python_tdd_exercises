.. meta::
   :description: Learn Python functions with TDD! Explore arguments, defaults, and testing techniques in this practical guide. Start coding now!
   :keywords: Jacob Itegboje, Python functions, Test-Driven Development, Python programming, keyword arguments, positional arguments, coding tutorial

.. include:: links.rst

.. danger:: DANGER WILL ROBINSON! Though the code works, this chapter is still UNDER CONSTRUCTION it may look completely different when I am done


#################################################################################
functions
#################################################################################

----

A :ref:`function <test_functions>` is a unit or block of code that is callable_. I can write statements that I can used to do something and call it at different time from when I write it. They can make code smaller and easier to read, test, reuse, maintain and improve.

Programming involves providing a process with input datand the process returning output data

.. code-block:: python

    argument -> program -> output_data

I think of it mathematically as mapping a :ref:`function<test_functions>` ``f`` with inputs ``x`` and an output of ``y``

.. math::

  f(x) -> y

in other words

.. code-block:: python

  program(argument) -> output_data

``program`` is the :ref:`function <test_functions>` that processes ``argument`` to return ``output_data``

``functions`` are defined using the def_ keyword, a name, parentheses and a colon at the end

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal to run :ref:`makePythonTdd.sh` with ``functions`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh functions

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 functions

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python
    :emphasize-lines: 1

    E       AssertionError: True is not false

    tests/test_functions.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_functions.py:7`` to open it in the editor
* then I change ``True`` to ``False`` to make the test pass

  .. code-block:: python
    :lineno-start: 7

            self.assertFalse(False)

*********************************************************************************
test_making_a_function_w_pass
*********************************************************************************

red: make it fail
#################################################################################

* I change ``test_failure`` to ``test_making_a_function_w_pass``

  .. code-block:: python

    import unittest


    class TestFunctions(unittest.TestCase):

        def test_making_a_function_w_pass(self):
            self.assertIsNone(src.functions.function_w_pass())

  the terminal shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

  I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_functions.py``

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

green: make it pass
#################################################################################

* I make a file called ``functions.py`` in the project folder the terminal shows :ref:`AttributeError` , which I add to the list of :ref:`Exceptions<errors>` encountered in ``test_functions.py``

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* I add a :ref:`function<functions>` definition to ``functions.py``

  .. code-block:: python

    def function_w_pass():
        pass

  and we have a passing test

  * the test checks if the value of the call to ``functions.function_w_pass`` is :ref:`None`
  * the :ref:`function<functions>` definition simply says pass_ and the test passes
  * pass_ is a placeholder keyword which allows the :ref:`function<functions>` definition to followsyntax rules
  * the test passes because inall :ref:`functions` return :ref:`None` by default, as if the :ref:`function<functions>` has an invisible line that says ``return None``

----

*********************************************************************************
test_making_a_function_w_return
*********************************************************************************

red: make it fail
#################################################################################

I add a new failing test to ``TestFunctions`` in ``test_functions.py`` to check that :ref:`functions` always return :ref:`None`

.. code-block:: python

    def test_making_a_function_w_return(self):
        self.assertIsNone(functions.function_w_return())

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

I add a new :ref:`function<functions>` to ``functions.py`` to make the test pass, this time with a ``return`` statement instead of pass_

.. code-block:: python

    def function_w_return(self):
        return

the terminal shows this test also passes

I defined 2 :ref:`functions` with different statements in their body but they both return the same result, because "inall :ref:`functions` return :ref:`None` by default, like the :ref:`function<functions>` has an invisible line that says ``return None``"

*********************************************************************************
test_making_a_function_w_return_none
*********************************************************************************

red: make it fail
################################################################################

I add one more test to the ``TestFunctions`` class in ``test_functions.py`` to help drive home the point

.. code-block:: python

    def test_making_a_function_w_return_none(self):
        self.assertIsNone(
            functions.function_w_return_none()
        )

the terminal shows :ref:`AttributeError`

green: make it pass
################################################################################

from the :PEP:`Zen of Python <20>`: ``Explicit is better than implicit.`` I add a :ref:`function<functions>` definition to ``functions.py`` this time with an explicit ``return`` statement showing the value returned

.. code-block:: python

  def function_w_return_none():
      return None

the test passes.

----

*********************************************************************************
test_constant_function
*********************************************************************************

constant :ref:`functions` always return the same thing when called

red: make it fail
#################################################################################

I add a test to ``test_functions.py``

.. code-block:: python

    def test_constant_function(self):
        self.assertEqual(functions.constant(), 'first_name')

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

I change the :ref:`function<functions>` to make it pass

.. code-block:: python

  def constant():
      return 'first_name'

*********************************************************************************
test_constant_function_w_inputs
*********************************************************************************

red: make it fail
#################################################################################

I add a new test for a :ref:`constant function<test_constant_function>` that takes input

.. code-block:: python

  def test_constant_function_w_inputs(self):
      self.assertEqual(
          src.functions.constant_w_inputs('Bob', 'James', 'Frank'),
          src.functions.constant()
      )
      self.assertEqual(
          functions.constant_w_inputs('a', 2, 'c', 3),
          src.functions.constant()
      )

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

and I add a definition for it

.. code-block:: python

  def constant_w_inputs(*arguments):
      return constant()

the test passes

----

*********************************************************************************
test_identity_function
*********************************************************************************

identity :ref:`functions` return their input as output

red: make it fail
################################################################################

I add a failing test to the ``TestFunctions`` class in ``test_functions.py``

.. code-block:: python

    def test_identity_function(self):
        self.assertEqual(functions.identity(False), False)

the terminal shows :ref:`AttributeError`

green: make it pass
################################################################################

* I add a :ref:`function<functions>` definition to ``functions.py``

  .. code-block:: python

    def identity():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: identity() takes 0 positional arguments but 1 was given

  because the definition for ``identity`` does not allow inputs and the test sends :ref:`False<test_what_is_false>` as input

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_functions.py``

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError

* then I make ``identity`` in ``functions.py`` to take 1 positional argument

  .. code-block:: python

    def identity(argument):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != False

  because the result of calling ``functions.identity`` with :ref:`False<test_what_is_false>` as input is :ref:`None` which is not equal to the expected result (:ref:`False<test_what_is_false>`)

* I change the definition of ``identity`` to make the test pass

  .. code-block:: python

    def identity(argument):
        return False

  the test passes. I am genius!

refactor: make it better
################################################################################

Wait a minute! Something is not quite right here. The definition for a identity :ref:`function<functions>` was that it returned the same thing it was given, the test passes when :ref:`False<test_what_is_false>` is given as input, will it still pass when another value is given or will it always return :ref:`False<test_what_is_false>`? Time to write a test

* I add a new :ref:`assertion<AssertionError>` to ``test_identity_function``

  .. code-block:: python

    def test_identity_function(self):
        self.assertEqual(functions.identity(False), False)
        self.assertEqual(functions.identity(True), True)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False != True

  the :ref:`function<functions>` returns :ref:`False<test_what_is_false>` instead of :ref:`True<test_what_is_true>` in the second case, I am not all the way genius, yet

* I change the definition of ``identity`` in ``functions.py``

  .. code-block:: python

    def identity(argument):
        return argument

  the test passes. I have more confidence that the identity :ref:`function<functions>` will return its input.

* I add more tests using the other data structures

  .. code-block:: python

    def test_identity_function(self):
        self.assertEqual(functions.identity(False), False)
        self.assertEqual(functions.identity(True), True)
        self.assertEqual(functions.identity(None), False)
        self.assertEqual(functions.identity(int), False)
        self.assertEqual(functions.identity(str), False)
        self.assertEqual(functions.identity(tuple), False)
        self.assertEqual(functions.identity(list), False)
        self.assertEqual(functions.identity(set), False)
        self.assertEqual(functions.identity(dict), False)

  the terminal shows :ref:`AssertionError` for each line until I make the input match the output, proving that the identity :ref:`function<functions>` I have defined returns the input it is given. Hooray! I am genius again

----

*********************************************************************************
test_functions_w_positional_arguments
*********************************************************************************

I can make a :ref:`function<functions>` take more than one input

.. code-block:: python

    def test_functions_w_positional_arguments(self):
        self.assertEqual(
            functions.take_positional_arguments(
                'first_name', 'last_name'
            ),
            ('first_name', 'last_name')
        )

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.functions' has no attribute 'take_positional_arguments'

green: make it pass
################################################################################

* I add a :ref:`function<functions>` to  ``functions.py``

  .. code-block:: python

    def take_positional_arguments(argument):
        return argument

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: take_positional_arguments() takes 1 positional argument but 2 were given

  I make the :ref:`function<functions>` take more than one argument

  .. code-block:: python

    def take_positional_arguments(
        argument, second
    ):
        return argument

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != ('first', 'second')

  I make it return the 2 arguments it receives

  .. code-block:: python

    def take_positional_arguments(
        argument, second
    ):
        return argument, second

  the test passes

refactor: make it better
################################################################################

How can I make this better?

* I change the name of the first argument to be more descriptive

  .. code-block:: python

    def take_positional_arguments(
            first, second
        ):
        return first, second

  I still have passing tests

* I add another :ref:`assertion<AssertionError>` to make sure that ``take_positional_arguments`` outputs data in the order given

  .. code-block:: python

      def test_functions_w_positional_arguments(self):
          self.assertEqual(
              functions.take_positional_arguments(
                  'first_name', 'last_name'
              ),
              ('first_name', 'last_name')
          )
          self.assertEqual(
              functions.take_positional_arguments(
                  'last_name', 'first_name'
              ),
              ('first_name', 'last_name')
          )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ('last_name', 'first_name') != ('first_name', 'last_name')

* I change the test so it has the right output

  .. code-block:: python

      def test_functions_w_positional_arguments(self):
          self.assertEqual(
              functions.take_positional_arguments(
                  'first_name', 'last_name'
              ),
              ('first_name', 'last_name')
          )
          self.assertEqual(
              functions.take_positional_arguments(
                  'last_name', 'first_name'
              ),
              ('last_name', 'first_name')
          )

  the terminal shows passing

* the :ref:`function<functions>` currently takes in 2 positional arguments.

*********************************************************************************
test_functions_w_unknown_positional_arguments
*********************************************************************************

* There are scenarios where a :ref:`function<functions>` needs to take in more arguments, like when I do not know the number of positional arguments that will be passed to the function, I add a test for the case where the number of positional arguments received is not known

  .. code-block:: python

    def test_functions_w_unknown_positional_arguments(self):
        self.assertEqual(
            src.functions.take_unknown_positional_arguments(
                0, 1, 2, 3
            ),
            (0, 1, 2, 3)
        )

  the terminal shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.functions' has no attribute 'take_unknown_positional_arguments'. Did you mean: 'take_positional_arguments'?

  I add the function with a `starred expression`_ like I did in :ref:`test_constant_function`, to allow it take in any number of arguments

  .. code-block:: python

    def take_unknown_positional_arguments(*arguments):
        return arguments

  the test passes

* I add another :ref:`assertion<AssertionError>` to show that this :ref:`function<functions>` never needs to know the number of inputs it is receiving

  .. code-block:: python

    self.assertEqual(
        src.functions.take_unknown_positional_arguments(
            0, 1, 2, 3
        ),
        (0, 1, 2, 3)
    )
    self.assertEqual(
        src.functions.take_unknown_positional_arguments(
            None, bool, int, float, str, tuple, list, set, dict
        ),
        None
    )

  the terminal shows :ref:`AssertionError`

  .. code-block::
    :force:

    AssertionError: (None, <class 'bool'>, <class 'int'>, <cl[87 chars]ct'>) != None

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        src.functions.take_unknown_positional_arguments(
            None, bool, int, float, str, tuple, list, set, dict
        ),
        (None, bool, int, float, str, tuple, list, set, dict)
    )

  the test is green again

----

*********************************************************************************
test_functions_w_keyword_arguments
*********************************************************************************

There is a problem with using positional arguments, the inputs must always be supplied in the right order. which means the program will behave in an unexpected way when it receives input out of order.

To make sure the :ref:`function<functions>` behaves how we want regardless of what order the user gives the input I can use Keyword Arguments

red: make it fail
################################################################################

I add a new test to ``test_functions.py``

.. code-block:: python

  def test_functions_w_keyword_arguments(self):
      self.assertEqual(
          src.functions.take_keyword_arguments(
              first_name='first_name',
              last_name='last_name',
          ),
          ('first_name', 'last_name')
      )

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.functions' has no attribute 'take_keyword_arguments'. Did you mean: 'take_unknown_positional_arguments'?

green: make it pass
################################################################################

* I add a :ref:`function<functions>` definition to ``functions.py``

  .. code-block:: python

    def take_keyword_arguments():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: take_keyword_arguments() got an unexpected keyword argument 'first_name'

  I add the argument to the defintion

  .. code-block:: python

    def take_keyword_arguments(first_name):
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python
    :force:

    TypeError: take_keyword_arguments() got an unexpected keyword argument 'last_name'. Did you mean 'first_name'?

  I add the argument

  .. code-block:: python

    def take_keyword_arguments(first_name, last_name):
        return None

  the terminal shows :ref:`AssertionError`

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

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

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

* The :ref:`function<functions>` currently only takes in 2 keyword arguments. What if I want a :ref:`function<functions>` that can take in any number of keyword arguments? There is a starred expression for keyword arguments - ``**``. I add an :ref:`assertion<AssertionError>`

  .. code-block:: python

    def test_functions_w_unknown_keyword_arguments(self):
        self.assertEqual(
            src.functions.take_unknown_keyword_arguments(
                a=1, b=2, c=3, d=4
            ),
            None
        )

  the terminal shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.functions' has no attribute 'take_unknown_keyword_arguments'. Did you mean: 'take_keyword_arguments'?

  I add a :ref:`function<functions>` using a `starred expression`_

  .. code-block:: python

    def take_unknown_keyword_arguments(*arguments):
        return arguments

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: take_unknown_keyword_arguments() got an unexpected keyword argument 'a'

  the `starred expression`_ for keyword arguments is different, I change the :ref:`function<functions>`

  .. code-block:: python

    def take_unknown_keyword_arguments(**keyword_arguments):
        return keyword_arguments

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

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

  the terminal shows :ref:`AssertionError`

  .. code-block:: python
    :force:

    AssertionError: {'none': None, 'a_boolean': <class 'bool'>[190 chars]ct'>} != {}

  I change the expectation to match the values in the terminal

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

I can also define :ref:`functions` to take both positional arguments and keyword arguments as inputs. I add a new failing test to ``test_functions.py``

.. code-block:: python

    def test_functions_w_positional_and_keyword_arguments(self):
        self.assertEqual(
        functions.take_positional_and_keyword_arguments(
            last_name='last_name', 'first_name'
        ),
        {}
      )

the terminal shows a SyntaxError_ because I put a positional argument
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

  the terminal shows :ref:`AttributeError`
* I add a definition for the :ref:`function<functions>` to ``functions.py``

  .. code-block:: python

    def take_positional_and_keyword_arguments():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: take_positional_and_keyword_arguments() got an unexpected keyword argument 'last_name'

* I make the :ref:`function<functions>` definition to take in an argument

  .. code-block:: python

    def take_positional_and_keyword_arguments(last_name):
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: take_positional_and_keyword_arguments() got multiple values for argument 'last_name'

* I add another argument to the :ref:`function<functions>` definition

  .. code-block:: python

    def take_positional_and_keyword_arguments(last_name, first_name):
        return None

  the terminal shows the same error even though I have 2 different arguments. I need a way to let the ``take_positional_and_keyword_arguments`` know which argument is positional and which is a keyword argument
* I reorder the arguments in the definition

  .. code-block:: python

    def take_positional_and_keyword_arguments(first_name, last_name):
        return None

  the terminal shows :ref:`AssertionError`
* I edit the `return statement`_ to make the test pass

  .. code-block:: python

    def take_positional_and_keyword_arguments(first_name, last_name):
        return first_name, last_name

  the terminal shows :ref:`AssertionError` with the values I just added
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

Hold on a second. This looks exactly like what I did in ``test_functions_w_positional_arguments``. I cannot tell from the :ref:`function<functions>` definition which argument is positional and which is a keyword argument and do not want to wait for the :ref:`function<functions>` to fail when I send in values to find out

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

  the terminal shows :ref:`TypeError` because the :ref:`function<functions>` definition only has 2 keyword arguments which are not provided in the call

* using what I know from previous tests I can alter the :ref:`function<functions>` to use starred expressions

  .. code-block:: python

    def take_positional_and_keyword_arguments(*args, **kwargs):
        return args, kwargs

  the terminal shows :ref:`AssertionError` for a previous passing test. I have introduced a regression

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

  the terminal shows tests passing, with the positional argument in parentheses and the keyword argument in curly braces
* I uncomment the next test

  .. code-block:: python

    self.assertEqual(
        functions.take_positional_and_keyword_arguments(
            'first_name', 'last_name'
        ),
        (('first_name', 'last_name'), {})
    )

  the terminal shows :ref:`AssertionError`

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

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ((), {}) != (None, None)

* I make the test pass with empty parentheses and curly braces as the expectation since no positional or keyword arguments were provided as inputs

  .. code-block:: python

    self.assertEqual(
        functions.take_positional_and_keyword_arguments(),
        ((), {})
    )

* I uncomment the last test to see it fail the terminal shows :ref:`AssertionError`

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
* :ref:`functions` return :ref:`None` by default
* :ref:`functions` are defined using the def_ keyword

Would you like to :ref:`test classes?<classes>`

----

:ref:`Click Here to see the code from this chapter<functions: tests and solutions>`
