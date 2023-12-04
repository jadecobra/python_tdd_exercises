
functions: keyword arguments
============================

There is an inherent problem with using positional arguments in functions. It requires the inputs to always be supplied in the correct order. If the program is dependent on that order, then it will behave in an unintended way when it receives input out of order.

To ensure the function behaves correctly regardless of what order the user provides the input I can use Keyword Arguments

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test to ``test_functions.py``

.. code-block:: python

    def test_functions_with_keyword_arguments(self):
        self.assertEqual(
            functions.passthrough_with_keyword_arguments(
                first_name='my_first_name',
                last_name='my_last_name'
            ),
            ('my_first_name', 'my_last_name')
        )

the terminal shows an :doc:`/exceptions/AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I add a function definition to ``functions.py``

  .. code-block:: python

    def passthrough_with_keyword_arguments():
        return None

  the terminal displays a :doc:`/exceptions/TypeError`

  .. code-block:: python

    TypeError: passthrough_with_keyword_arguments() got an unexpected keyword argument 'first_name'

* I alter the function signature to take in a positional argument

  .. code-block:: python

    def passthrough_with_keyword_arguments(first_name):
        return None

  the terminal shows a :doc:`/exceptions/TypeError` with a different message

  .. code-block:: python

    TypeError: passthrough_with_keyword_arguments() got an unexpected keyword argument 'last_name'

* I change the function signature to take in another positional argument

  .. code-block:: python

    def passthrough_with_keyword_arguments(first_name, last_name):
        return None

  the terminal shows an :doc:`/exceptions/AssertionError`
* I adjust the return statement to make the test pass

  .. code-block:: python

      def passthrough_with_keyword_arguments(first_name, last_name):
          return first_name, last_name

  Eureka! the terminal shows passing tests

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

So far ``passthrough_with_keyword_arguments`` looks the same as ``passthrough_with_positional_arguments`` did when it took in 2 positional arguments, I have not yet seen a difference between a ``positional argument`` and a ``keyword argument``


* I add a test that puts the input data out of order to see if there is a difference

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

  the terminal shows passing tests. Unlike in ``test_functions_with_positional_arguments`` using the name when passing inputs, ensures the function always displays output in the right order regardless of the order in which the input data is given

The function currently only takes in 2 keyword arguments. What if I want a function that can take in any number of keyword arguments? There is a starred expression for keyword arguments - ``**``.

* RED: make it fail

  I add a test to ``test_functions_with_keyword_arguments``

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

  the terminal shows a :doc:`/exceptions/TypeError`

* GREEN: make it pass


  - I change the signature of ``passthrough_with_keyword_arguments`` to accept any number of keyword arguments

    .. code-block:: python

      def passthrough_with_keyword_arguments(**keyword_arguments):
          return keyword_arguments

    the terminal shows an :doc:`/exceptions/AssertionError` for the previous test that was passing. I have introduced a regression - the new code has caused an old passing test to fail.
  - I change the expected result of ``test_functions_with_keyword_arguments`` from the terminal's output

    .. code-block:: python

      def test_functions_with_keyword_arguments(self):
          self.assertEqual(
              functions.passthrough_with_keyword_arguments(
                  first_name='my_first_name',
                  last_name='my_last_name'
              ),
              {
                  'first_name': 'my_first_name',
                  'last_name': 'my_last_name'
              }
          )

    the terminal shows an :doc:`/exceptions/AssertionError` for the next test that was passing. I have another regression

  * I change the next test to make the output match the expectation

    .. code-block:: python

      def test_functions_with_keyword_arguments(self):
          self.assertEqual(
              functions.passthrough_with_keyword_arguments(
                  first_name='my_first_name',
                  last_name='my_last_name'
              ),
              {
                  'first_name': 'my_first_name',
                  'last_name': 'my_last_name'
              }
          )
          self.assertEqual(
              functions.passthrough_with_keyword_arguments(
                  last_name='my_last_name',
                  first_name='my_first_name'
              ),
              {
                  'first_name': 'my_first_name',
                  'last_name': 'my_last_name'
              }
          )

    the terminal shows an :doc:`/exceptions/AssertionError` for the last test I added
  * time to match the last test to the expected value in the comparison

    .. code-block:: python

      def test_functions_with_keyword_arguments(self):
          self.assertEqual(
              functions.passthrough_with_keyword_arguments(
                  first_name='my_first_name',
                  last_name='my_last_name'
              ),
              {
                  'first_name': 'my_first_name',
                  'last_name': 'my_last_name'
              }
          )
          self.assertEqual(
              functions.passthrough_with_keyword_arguments(
                  last_name='my_last_name',
                  first_name='my_first_name'
              ),
              {
                  'first_name': 'my_first_name',
                  'last_name': 'my_last_name'
              }
          )
          self.assertEqual(
              functions.passthrough_with_keyword_arguments(
                a=1, b=2, c=3, d=4
              ),
              {'a': 1, 'b': 2, 'c': 3, 'd': 4}
          )

    the terminal shows passing tests. From the tests I can see that keyword arguments are treated as :doc:`dictionaries </data_structures/data_structures_dictionaries>`  in python

* REFACTOR: make it better

  I add one more test to ``test_functions_with_keyword_arguments`` to drill the lesson

  .. code-block:: python

    def test_functions_with_keyword_arguments(self):
        self.assertEqual(
            functions.passthrough_with_keyword_arguments(
                first_name='my_first_name',
                last_name='my_last_name'
            ),
            {
                'first_name': 'my_first_name',
                'last_name': 'my_last_name'
            }
        )
        self.assertEqual(
            functions.passthrough_with_keyword_arguments(
                last_name='my_last_name',
                first_name='my_first_name'
            ),
            {
                'first_name': 'my_first_name',
                'last_name': 'my_last_name'
            }
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

  the terminal shows an :doc:`/exceptions/AssertionError` and I change the expected values in the test to match the values from the function

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

  All tests are passing!
