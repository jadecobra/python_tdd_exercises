.. include:: ../links.rst

#################################################################################
functions: test_functions_w_keyword_arguments
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

There is an inherent problem with using positional arguments in functions. It requires the inputs to always be supplied in the right order. If the program is dependent on that order, then it will behave in an unintended way when it receives input out of order.

To ensure the :ref:`function<functions>` behaves right regardless of what order the user provides the input I can use Keyword Arguments

*********************************************************************************
test_functions_w_keyword_arguments
*********************************************************************************

red: make it fail
---------------------------------------------------------------------------------

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

the terminal shows :ref:`AttributeError`

green: make it pass
---------------------------------------------------------------------------------

* I add a :ref:`function<functions>` definition to ``functions.py``

  .. code-block:: python

    def passthrough_w_keyword_arguments():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: passthrough_w_keyword_arguments() got an unexpected keyword argument 'first_name'

* I make the :ref:`function<functions>` signature to make it take a positional argument

  .. code-block:: python

    def passthrough_w_keyword_arguments(first_name):
        return None

  the terminal shows :ref:`TypeError` with a different message

  .. code-block:: python

    TypeError: passthrough_w_keyword_arguments() got an unexpected keyword argument 'last_name'

* I make the :ref:`function<functions>` signature to take in another positional argument

  .. code-block:: python

    def passthrough_w_keyword_arguments(first_name, last_name):
        return None

  the terminal shows :ref:`AssertionError`
* I adjust the `return statement`_ to make the test pass

  .. code-block:: python

      def passthrough_w_keyword_arguments(first_name, last_name):
          return first_name, last_name

  Eureka! the terminal shows passing tests

refactor: make it better
---------------------------------------------------------------------------------

* So far ``passthrough_w_keyword_arguments`` looks the same as ``passthrough_w_positional_arguments`` did when it took in 2 positional arguments, I have not yet seen a difference between a ``positional argument`` and a ``keyword argument``. I add an assertion that puts the input data out of order to see if there is a difference

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

  the terminal shows passing tests. Unlike in ``test_functions_w_positional_arguments`` using the name when passing inputs, ensures the :ref:`function<functions>` always shows output in the right order regardless of the order in which the input data is given

* The :ref:`function<functions>` currently only takes in 2 keyword arguments. What if I want a :ref:`function<functions>` that can take in any number of keyword arguments? There is a starred expression for keyword arguments - ``**``. I add an assertion

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

  the terminal shows :ref:`TypeError`

* I make the signature of ``passthrough_w_keyword_arguments`` take any number of keyword arguments

  .. code-block:: python

    def passthrough_w_keyword_arguments(**keyword_arguments):
        return keyword_arguments

  the terminal shows :ref:`AssertionError` for the previous test that was passing. I have introduced a regression - the new code has caused an old passing test to fail.

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

  the terminal shows :ref:`AssertionError` for the next test that was passing. I have another regression

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

  and the terminal shows :ref:`AssertionError` for the last test I added

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

  the terminal shows passing tests. From these tests, I can say that keyword arguments are treated as :ref:`dictionaries`  in Python

* I add one more assertion to ``test_functions_w_keyword_arguments`` to drill the lesson

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

  the terminal shows :ref:`AssertionError` and I make the expected values match the values from the terminal

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

----

*********************************************************************************
review
*********************************************************************************

From the tests I know

* I can use ``**name`` to represent any number of keyword arguments
* that keyword arguments are represented as :ref:`dictionaries`  with curly braces - ``{}``
* I can use ``*name`` to represent any number of positional arguments
* that positional arguments are represented as tuples_ with parentheses - ``()``
* that passthrough :ref:`functions` return what they receive as input
* that constant :ref:`functions` return the same thing every time they are called
* :ref:`functions` are defined using the def_ keyword
* :ref:`functions` return :ref:`None` by default

Would you like to :ref:`test functions with positional and keyword arguments? <test_functions_w_positional_and_keyword_arguments>`

----

:doc:`/code/code_functions`
