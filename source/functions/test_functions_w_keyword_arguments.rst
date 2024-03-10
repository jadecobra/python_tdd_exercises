.. include:: ../links.rst

.. _test_functions_w_keyword_arguments:

#############################################################################
functions: test_functions_w_keyword_arguments
#############################################################################

----

.. contents:: table of contents
  :local:
  :depth: 1

----

There is an inherent problem with using positional arguments in functions. It requires the inputs to always be supplied in the correct order. If the program is dependent on that order, then it will behave in an unintended way when it receives input out of order.

To ensure the function behaves correctly regardless of what order the user provides the input I can use Keyword Arguments

.. _test_functions_w_keyword_arguments_red:

*****************************************************************************
red: make it fail
*****************************************************************************

I add a new test to ``test_functions.py``

.. code-block:: python

    def test_functions_w_keyword_arguments(self):
        self.assertEqual(
            functions.passthrough_w_keyword_arguments(
                first_name='my_first_name',
                last_name='my_last_name'
            ),
            ('my_first_name', 'my_last_name')
        )

the terminal shows an :ref:`AttributeError`

.. _test_functions_w_keyword_arguments_green:

*****************************************************************************
green: make it pass
*****************************************************************************


* I add a function definition to ``functions.py``

  .. code-block:: python

    def passthrough_w_keyword_arguments():
        return None

  the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: passthrough_w_keyword_arguments() got an unexpected keyword argument 'first_name'

* I make the :doc:`function</functions/functions>` signature to make it accept a positional argument

  .. code-block:: python

    def passthrough_w_keyword_arguments(first_name):
        return None

  the terminal shows a :ref:`TypeError` with a different message

  .. code-block:: python

    TypeError: passthrough_w_keyword_arguments() got an unexpected keyword argument 'last_name'

* I make the :doc:`function</functions/functions>` signature to take in another positional argument

  .. code-block:: python

    def passthrough_w_keyword_arguments(first_name, last_name):
        return None

  the terminal shows an :ref:`AssertionError`
* I adjust the return statement to make the test pass

  .. code-block:: python

      def passthrough_w_keyword_arguments(first_name, last_name):
          return first_name, last_name

  Eureka! the terminal shows passing tests

.. _test_functions_w_keyword_arguments_refactor:

*****************************************************************************
refactor: make it better
*****************************************************************************

So far ``passthrough_w_keyword_arguments`` looks the same as ``passthrough_w_positional_arguments`` did when it took in 2 positional arguments, I have not yet seen a difference between a ``positional argument`` and a ``keyword argument``


* I add an assertion that puts the input data out of order to see if there is a difference

  .. code-block:: python

      def test_functions_w_keyword_arguments(self):
          self.assertEqual(
              functions.passthrough_w_keyword_arguments(
                  first_name='my_first_name',
                  last_name='my_last_name'
              ),
              ('my_first_name', 'my_last_name')
          )
          self.assertEqual(
              functions.passthrough_w_keyword_arguments(
                  last_name='my_last_name',
                  first_name='my_first_name'
              ),
              ('my_first_name', 'my_last_name')
          )

  the terminal shows passing tests. Unlike in ``test_functions_w_positional_arguments`` using the name when passing inputs, ensures the function always displays output in the right order regardless of the order in which the input data is given

The function currently only takes in 2 keyword arguments. What if I want a function that can take in any number of keyword arguments? There is a starred expression for keyword arguments - ``**``.

.. _test_functions_w_keyword_arguments_refactor_red:

red: make it fail
#############################################################################

I add an assertion

.. code-block:: python

    def test_functions_w_keyword_arguments(self):
        self.assertEqual(
            functions.passthrough_w_keyword_arguments(
                first_name='my_first_name',
                last_name='my_last_name'
            ),
            ('my_first_name', 'my_last_name')
        )
        self.assertEqual(
            functions.passthrough_w_keyword_arguments(
                last_name='my_last_name',
                first_name='my_first_name'
            ),
            ('my_first_name', 'my_last_name')
        )
        self.assertEqual(
            functions.passthrough_w_keyword_arguments(
                a=1, b=2, c=3, d=4
            ),
            {}
        )

the terminal shows a :ref:`TypeError`

.. _test_functions_w_keyword_arguments_refactor_green:

green: make it pass
#############################################################################

* I make the signature of ``passthrough_w_keyword_arguments`` accept any number of keyword arguments

  .. code-block:: python

    def passthrough_w_keyword_arguments(**keyword_arguments):
        return keyword_arguments

  the terminal shows an :ref:`AssertionError` for the previous test that was passing. I have introduced a regression - the new code has caused an old passing test to fail.

* so I change the expectation

  .. code-block:: python

    def test_functions_w_keyword_arguments(self):
        self.assertEqual(
            functions.passthrough_w_keyword_arguments(
                first_name='my_first_name',
                last_name='my_last_name'
            ),
            {
                'first_name': 'my_first_name',
                'last_name': 'my_last_name'
            }
        )

  the terminal shows an :ref:`AssertionError` for the next test that was passing. I have another regression

* I make the expectation match the output

  .. code-block:: python

    def test_functions_w_keyword_arguments(self):
        self.assertEqual(
            functions.passthrough_w_keyword_arguments(
                first_name='my_first_name',
                last_name='my_last_name'
            ),
            {
                'first_name': 'my_first_name',
                'last_name': 'my_last_name'
            }
        )
        self.assertEqual(
            functions.passthrough_w_keyword_arguments(
                last_name='my_last_name',
                first_name='my_first_name'
            ),
            {
                'first_name': 'my_first_name',
                'last_name': 'my_last_name'
            }
        )

  and the terminal shows an :ref:`AssertionError` for the last test I added

* time to match the last test to the expected value in the comparison

  .. code-block:: python

    def test_functions_w_keyword_arguments(self):
        self.assertEqual(
            functions.passthrough_w_keyword_arguments(
                first_name='my_first_name',
                last_name='my_last_name'
            ),
            {
                'first_name': 'my_first_name',
                'last_name': 'my_last_name'
            }
        )
        self.assertEqual(
            functions.passthrough_w_keyword_arguments(
                last_name='my_last_name',
                first_name='my_first_name'
            ),
            {
                'first_name': 'my_first_name',
                'last_name': 'my_last_name'
            }
        )
        self.assertEqual(
            functions.passthrough_w_keyword_arguments(
              a=1, b=2, c=3, d=4
            ),
            {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        )

  the terminal shows passing tests. From the tests I can see that keyword arguments are treated as :doc:`dictionaries </data_structures/dictionaries>`  in Python

.. _test_functions_w_keyword_arguments_refactor_refactor:

refactor: make it better
#############################################################################

I add one more assertion to ``test_functions_w_keyword_arguments`` to drill the lesson

.. code-block:: python

  def test_functions_w_keyword_arguments(self):
      self.assertEqual(
          functions.passthrough_w_keyword_arguments(
              first_name='my_first_name',
              last_name='my_last_name'
          ),
          {
              'first_name': 'my_first_name',
              'last_name': 'my_last_name'
          }
      )
      self.assertEqual(
          functions.passthrough_w_keyword_arguments(
              last_name='my_last_name',
              first_name='my_first_name'
          ),
          {
              'first_name': 'my_first_name',
              'last_name': 'my_last_name'
          }
      )
      self.assertEqual(
          functions.passthrough_w_keyword_arguments(
              a=1, b=2, c=3, d=4
          ),
          {'a': 1, 'b': 2, 'c': 3, 'd': 4}
      )
      self.assertEqual(
          functions.passthrough_w_keyword_arguments(
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

the terminal shows an :ref:`AssertionError` and I make the expected values match the values from the terminal

.. code-block:: python

  self.assertEqual(
      functions.passthrough_w_keyword_arguments(
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

All tests are passing!


*****************************************************************************
review
*****************************************************************************

From the tests I know

* I can use ``**name`` to represent any number of keyword arguments
* that keyword arguments are represented as :doc:`dictionaries </data_structures/dictionaries>`  with curly braces - ``{}``
* I can use ``*name`` to represent any number of positional arguments
* that positional arguments are represented as `tuples <https://docs.python.org/3/library/stdtypes.html#tuple>`_ with parentheses - ``()``
* that passthrough functions return what they receive as input
* that singleton functions return the same thing every time they are called
* functions are defined using the `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword
* functions return :ref:`None` by default

Would you like to :ref:`test_functions_w_positional_and_keyword_arguments`?

----

:doc:`/code/code_functions`
