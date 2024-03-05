.. include:: ../links.rst

#############################################################################
functions: test_functions_w_positional_arguments
#############################################################################

----

.. contents:: table of contents
  :local:
  :depth: 1

----

I can define a function to take in more than one input, For instance if I am writing a function to perform operations on 2 numbers as I do in :doc:`/how_to/calculator` , the function has to be able to accept the 2 numbers it performs operations on

*****************************************************************************
red: make it fail
*****************************************************************************

I add a new test to ``test_functions.py``

.. code-block:: python

    def test_functions_w_positional_arguments(self):
        self.assertEqual(
            functions.passthrough_w_positional_arguments(
                'my_first_name', 'my_last_name'
            ),
            ('my_first_name', 'my_last_name')
        )

the terminal shows an :ref:`AttributeError`

*****************************************************************************
green: make it pass
*****************************************************************************

* I add the solution I know works from ``test_passthrough_functions`` ``functions.py``

  .. code-block:: python

    def passthrough_w_positional_arguments(input_data):
        return input_data

  the terminal shows a :ref:`TypeError`
* I make the signature of ``passthrough_w_positional_arguments`` to take in more than one argument

  .. code-block:: python

    def passthrough_w_positional_arguments(
        input_data, second_argument
    ):
        return input_data

  the terminal shows an :ref:`AssertionError`
* I make ``passthrough_w_positional_arguments`` to return the two arguments it receives

  .. code-block:: python

    def passthrough_w_positional_arguments(
        input_data, second_argument
    ):
        return input_data, second_argument

  the terminal shows passing tests

*****************************************************************************
refactor: make it better
*****************************************************************************

How can I make this better?

* I called the first argument ``input_data`` and the second argument ``second_argument``. Technically, both arguments are input data, so I need a better name that is more descriptive
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

  the terminal shows an :ref:`AssertionError`
* I make the test so it has the correct output

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
* the function currently takes in 2 positional arguments. There are scenarios where a function needs to take in more arguments, like when I do not know the number of positional arguments that will be passed to the function
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

  the terminal shows a :ref:`TypeError` because 2 positional arguments were expected by the function but 4 were given
* in Python I can represent multiple arguments using a starred expression `see arbitrary argument lists <https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists>`_, so I make the signature of ``functions_w_positional_arguments`` with a starred expression to alow it take in any number of arguments

  .. code-block:: python

    def passthrough_w_positional_arguments(*arguments):
        return arguments

  the terminal shows passing tests

----