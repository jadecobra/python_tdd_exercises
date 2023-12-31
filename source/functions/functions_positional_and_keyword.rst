
functions: positional and keyword arguments
-------------------------------------------

I can also define functions to take both positional arguments and keyword arguments as inputs

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new failing test to ``test_functions.py``

.. code-block:: python

    def test_functions_with_positional_and_keyword_arguments(self):
        self.assertEqual(
        functions.accepts_positional_and_keyword_arguments(
            last_name='my_last_name', 'my_first_name'
        ),
        {}
      )

the terminal shows a ``SyntaxError`` because I put a positional argument after a keyword argument. I add the error to the list of exceptions encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError
  # AttributeError
  # TypeError
  # SyntaxError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I fix the order of arguments in ``test_functions_with_positional_and_keyword_arguments`` since keyword arguments come after positional arguments

  .. code-block:: python

    def test_functions_with_positional_and_keyword_arguments(self):
        self.assertEqual(
            functions.accepts_positional_and_keyword_arguments(
                'my_first_name', last_name='my_last_name'
            ),
            {}
        )

  the terminal shows an :doc:`/exceptions/AttributeError`
* I add a definition for the function to ``functions.py``

  .. code-block:: python

    def accepts_positional_and_keyword_arguments():
        return None

  the terminal shows a :doc:`/exceptions/TypeError`

  .. code-block:: python

    TypeError: accepts_positional_and_keyword_arguments() got an unexpected keyword argument 'last_name'

* I change the function signature to take in an argument

  .. code-block:: python

    def accepts_positional_and_keyword_arguments(last_name):
        return None

  the terminal shows another :doc:`/exceptions/TypeError`

  .. code-block:: python

    TypeError: accepts_positional_and_keyword_arguments() got multiple values for argument 'last_name'

* I add another argument to the function signature

  .. code-block:: python

    def accepts_positional_and_keyword_arguments(last_name, first_name):
        return None

  the terminal shows the same error even though I have 2 different arguments. I need a way to let the ``accepts_positional_and_keyword_arguments`` know which argument is positional and which is a keyword argument
* I reorder the arguments in the signature

  .. code-block:: python

    def accepts_positional_and_keyword_arguments(first_name, last_name):
        return None

  the terminal shows an :doc:`/exceptions/AssertionError`
* I edit the return statement to make the test pass

  .. code-block:: python

    def accepts_positional_and_keyword_arguments(first_name, last_name):
        return first_name, last_name

  the terminal changes the :doc:`/exceptions/AssertionError` with the values I just added
* I change ``test_functions_with_positional_and_keyword_arguments`` to make the results match the expectation

  .. code-block:: python

      def test_functions_with_positional_and_keyword_arguments(self):
          self.assertEqual(
          functions.accepts_positional_and_keyword_arguments(
                  'my_first_name', last_name='my_last_name'
              ),
              ('my_first_name', 'my_last_name')
          )

  the terminal shows passing tests

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Hold on a second. This looks exactly like what I did in ``test_functions_with_positional_arguments``. I cannot tell from the function signature which argument is positional and which is a keyword argument and do not want to wait for the function to fail when I send in values to find out


* I change the function signature of ``accepts_positional_and_keyword_arguments`` to have a default value for the keyword argument

  .. code-block:: python

    def accepts_positional_and_keyword_arguments(first_name, last_name=None):
        return first_name, last_name

  all tests are still passing
* I did not add a default argument for ``first_name``, what would happen if I did?

  .. code-block:: python

    def accepts_positional_and_keyword_arguments(first_name=None, last_name=None):
        return first_name, last_name

  I still have passing tests. It looks like python lets us use default arguments with no issues, and I can provide keyword arguments positionally without using the name.
* I add another test to ``test_functions_with_positional_and_keyword_arguments`` to show this

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
* I add 2 tests, this time for an unknown number of positional and keyword arguments

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

  the terminal shows a :doc:`/exceptions/TypeError` because the function signature only has two keyword arguments which are not provided in the call
* using what I know from previous tests I can alter the function to use starred expressions

  .. code-block:: python

    def accepts_positional_and_keyword_arguments(*args, **kwargs):
        return args, kwargs

  the terminal shows a failure for a previous passing test. I have introduced a regression

  .. code-block:: python

      def test_functions_with_positional_and_keyword_arguments(self):
    >   self.assertEqual(
            functions.accepts_positional_and_keyword_arguments('my_first_name', last_name='my_last_name'),
            ('my_first_name', 'my_last_name')
        )
    E   AssertionError: Tuples differ: (('my_first_name',), {'last_name': 'my_last_name'}) != ('my_first_name', 'my_last_name')

* I comment out the other tests for a bit, so I can focus on the failing test

  .. code-block:: python

      def test_functions_with_positional_and_keyword_arguments(self):
          self.assertEqual(
            functions.accepts_positional_and_keyword_arguments(
              'my_first_name', last_name='my_last_name'
            ),
            ('my_first_name', 'my_last_name')
          )
          # self.assertEqual(
          #    functions.accepts_positional_and_keyword_arguments(
          #        'my_first_name', 'my_last_name'
          #    ),
          #    (('my_first_name', 'last_name'), {})
          # )
          # self.assertEqual(
          #     functions.accepts_positional_and_keyword_arguments(),
          #     (None, None)
          # )
          # self.assertEqual(
          #    functions.accepts_positional_and_keyword_arguments(
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
        functions.accepts_positional_and_keyword_arguments(
            'my_first_name', last_name='my_last_name'
        ),
        (('my_first_name',), {'last_name': 'my_last_name'})
    )

  the terminal shows tests passing, with the positional argument in parentheses and the keyword argument in curly braces
* I uncomment the next test

  .. code-block:: python

    self.assertEqual(
        functions.accepts_positional_and_keyword_arguments(
            'my_first_name', 'my_last_name'
        ),
        (('my_first_name', 'last_name'), {})
    )

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    >    self.assertEqual(
             functions.accepts_positional_and_keyword_arguments(
                 'my_first_name', 'my_last_name'
             ),
             (('my_first_name', 'last_name'), {})
         )
    E    AssertionError: Tuples differ: (('my_first_name', 'my_last_name'), {}) != (('my_first_name', 'last_name'), {})

* I change the test to make it pass with both positional arguments in parentheses and empty curly braces since there are no keyword arguments

  .. code-block:: python

      self.assertEqual(
          functions.accepts_positional_and_keyword_arguments(
              'my_first_name', 'my_last_name'
          ),
          (('my_first_name', 'my_last_name'), {})
      )

  and the terminal shows passing tests
* I uncomment the next test to see it fail

  .. code-block:: python

      self.assertEqual(
          functions.accepts_positional_and_keyword_arguments(),
          (None, None)
      )

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ((), {}) != (None, None)

* I change the test to make it pass with empty parentheses and curly braces as the expectation since no positional or keyword arguments were provided as inputs

  .. code-block:: python

    self.assertEqual(
        functions.accepts_positional_and_keyword_arguments(),
        ((), {})
    )

* I uncomment the last test to see it fail and the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block::

    AssertionError: Tuples differ: ((<class 'bool'>, <class 'int'>, <class 'f[307 chars]t'>}) != ()

* I change the test to make it pass

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

  the terminal shows passing tests
* From the tests I know that

  * positional arguments are represented as `tuples <https://docs.python.org/3/library/stdtypes.html#tuple>`_ with parentheses - ``()``
  * keyword arguments are represented as :doc:`dictionaries </data_structures/dictionaries>`  with curly braces - ``{}``
  * I can use ``*name`` to represent any number of positional arguments
  * I can use ``**name`` to represent any number of keyword arguments
  * I can define default values for arguments
  * positional arguments must come before keyword arguments
