.. include:: ../links.rst


#################################################################################
functions: test_functions_w_positional_arguments
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----


*********************************************************************************
test_functions_w_positional_arguments
*********************************************************************************

I can define a :ref:`function<functions>` to take in more than one input, For instance if I am writing a :ref:`function<functions>` to perform operations on 2 numbers as I do in :doc:`/how_to/calculator` , the :ref:`function<functions>` has to be able to take the 2 numbers it performs operations on. I add a new test to ``test_functions.py``

.. code-block:: python

    def test_functions_w_positional_arguments(self):
        self.assertEqual(
            functions.passthrough_w_positional_arguments(
                'my_first_name', 'my_last_name'
            ),
            ('my_first_name', 'my_last_name')
        )

the terminal shows :ref:`AttributeError`

green: make it pass
---------------------------------------------------------------------------------

* I add the solution I know works from ``test_passthrough_functions`` ``functions.py``

  .. code-block:: python

    def passthrough_w_positional_arguments(argument):
        return argument

  the terminal shows :ref:`TypeError`
* I make the signature of ``passthrough_w_positional_arguments`` to take in more than one argument

  .. code-block:: python

    def passthrough_w_positional_arguments(
        argument, second_argument
    ):
        return argument

  the terminal shows :ref:`AssertionError`
* I make ``passthrough_w_positional_arguments`` return the two arguments it receives

  .. code-block:: python

    def passthrough_w_positional_arguments(
        argument, second_argument
    ):
        return argument, second_argument

  the terminal shows passing tests

refactor: make it better
---------------------------------------------------------------------------------

How can I make this better?

* I called the first argument ``argument`` and the second argument ``second_argument``. Technically, both arguments are input data, so I need a better name that is more descriptive
* I make the signature of ``passthrough_w_positional_arguments`` to use more descriptive names

  .. code-block:: python

    def passthrough_w_positional_arguments(
        first_argument, second_argument
    ):
        return first_argument, second_argument

  I still have passing tests
* I add another test to ensure that ``passthrough_w_positional_arguments`` outputs data in the order given

  .. code-block:: python

      def test_functions_w_positional_arguments(self):
          self.assertEqual(
              functions.passthrough_w_positional_arguments(
                  'my_first_name', 'my_last_name'
              ),
              ('my_first_name', 'my_last_name')
          )
          self.assertEqual(
              functions.passthrough_w_positional_arguments(
                  'my_last_name', 'my_first_name'
              ),
              ('my_first_name', 'my_last_name')
          )

  the terminal shows :ref:`AssertionError`
* I make the test so it has the right output

  .. code-block:: python

      def test_functions_w_positional_arguments(self):
          self.assertEqual(
              functions.passthrough_w_positional_arguments(
                  'my_first_name', 'my_last_name'
              ),
              ('my_first_name', 'my_last_name')
          )
          self.assertEqual(
              functions.passthrough_w_positional_arguments(
                  'my_last_name', 'my_first_name'
              ),
              ('my_last_name', 'my_first_name')
          )

  the terminal shows passing tests
* the :ref:`function<functions>` currently takes in 2 positional arguments. There are scenarios where a :ref:`function<functions>` needs to take in more arguments, like when I do not know the number of positional arguments that will be passed to the function
* I add tests for cases where the number of positional arguments received is not known ``test_functions_w_positional_arguments``

  .. code-block:: python

      def test_functions_w_positional_arguments(self):
          self.assertEqual(
              functions.passthrough_w_positional_arguments(
                  'my_first_name', 'my_last_name'
              ),
              ('my_first_name', 'my_last_name')
          )
          self.assertEqual(
              functions.passthrough_w_positional_arguments(
                  'my_last_name', 'my_first_name'
              ),
              ('my_last_name', 'my_first_name')
          )
          self.assertEqual(
              functions.passthrough_w_positional_arguments(
                  0, 1, 2, 3
              ),
              (0, 1, 2, 3)
          )
          self.assertEqual(
              functions.passthrough_w_positional_arguments(
                  bool, int, float, str, tuple, list, set, dict
              ),
              (bool, int, float, str, tuple, list, set, dict)
          )

  the terminal shows :ref:`TypeError` because 2 positional arguments were expected by the :ref:`function<functions>` but 4 were given
* in Python I can represent multiple arguments using a starred expression `see arbitrary argument lists <https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists>`_, so I make the signature of ``functions_w_positional_arguments`` with a starred expression to alow it take in any number of arguments

  .. code-block:: python

    def passthrough_w_positional_arguments(*arguments):
        return arguments

  the terminal shows passing tests

*********************************************************************************
review
*********************************************************************************

From the tests I know

* I can use ``*name`` to represent any number of positional arguments
* that positional arguments are represented as tuples_ with parentheses - ``()``
* that passthrough :ref:`functions` return what they receive as input
* that singleton :ref:`functions` return the same thing every time they are called
* :ref:`functions` are defined using the def_ keyword
* :ref:`functions` return :ref:`None` by default

Would you like to :ref:`test_functions_with keyword arguments? <test_functions_w_keyword_arguments>`

----

:doc:`/code/code_functions`