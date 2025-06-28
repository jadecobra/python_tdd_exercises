.. include:: ../links.rst


#################################################################################
functions: test_functions_w_positional_arguments
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

* :ref:`test functions<test_functions>`

----

*********************************************************************************
test_functions_w_positional_arguments
*********************************************************************************

I can make a :ref:`function<functions>` take more than one input

.. code-block:: python

    def test_functions_w_positional_arguments(self):
        self.assertEqual(
            functions.identity_w_positional_arguments(
                'my_first_name', 'my_last_name'
            ),
            ('my_first_name', 'my_last_name')
        )

the terminal shows :ref:`AttributeError`

.. code-block:: python



green: make it pass
---------------------------------------------------------------------------------

* I add a :ref:`function<functions>` to  ``functions.py``

  .. code-block:: python

    def identity_w_positional_arguments(argument):
        return argument

  the terminal shows :ref:`TypeError`

  .. code-block:: python



  I make the :ref:`function<functions>` take more than one argument

  .. code-block:: python

    def identity_w_positional_arguments(
        argument, second_argument
    ):
        return argument

  the terminal shows :ref:`AssertionError`

  .. code-block:: python



  I make it return the 2 arguments it receives

  .. code-block:: python

    def identity_w_positional_arguments(
        argument, second_argument
    ):
        return argument, second_argument

  the test passes

refactor: make it better
---------------------------------------------------------------------------------

How can I make this better?

* I change the name of the first argument to be more descriptive

  .. code-block:: python

    def identity_w_positional_arguments(
        first_argument, second_argument
    ):
        return first_argument, second_argument

  I still have passing tests

* I add another test to make sure that ``identity_w_positional_arguments`` outputs data in the order given

  .. code-block:: python

      def test_functions_w_positional_arguments(self):
          self.assertEqual(
              functions.identity_w_positional_arguments(
                  'my_first_name', 'my_last_name'
              ),
              ('my_first_name', 'my_last_name')
          )
          self.assertEqual(
              functions.identity_w_positional_arguments(
                  'my_last_name', 'my_first_name'
              ),
              ('my_first_name', 'my_last_name')
          )

  the terminal shows :ref:`AssertionError`
* I make the test so it has the right output

  .. code-block:: python

      def test_functions_w_positional_arguments(self):
          self.assertEqual(
              functions.identity_w_positional_arguments(
                  'my_first_name', 'my_last_name'
              ),
              ('my_first_name', 'my_last_name')
          )
          self.assertEqual(
              functions.identity_w_positional_arguments(
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
              functions.identity_w_positional_arguments(
                  'my_first_name', 'my_last_name'
              ),
              ('my_first_name', 'my_last_name')
          )
          self.assertEqual(
              functions.identity_w_positional_arguments(
                  'my_last_name', 'my_first_name'
              ),
              ('my_last_name', 'my_first_name')
          )
          self.assertEqual(
              functions.identity_w_positional_arguments(
                  0, 1, 2, 3
              ),
              (0, 1, 2, 3)
          )
          self.assertEqual(
              functions.identity_w_positional_arguments(
                  bool, int, float, str, tuple, list, set, dict
              ),
              (bool, int, float, str, tuple, list, set, dict)
          )

  the terminal shows :ref:`TypeError` because 2 positional arguments were expected by the :ref:`function<functions>` but 4 were given
* in Python I can represent multiple arguments using a starred expression `see arbitrary argument lists <https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists>`_, so I make the signature of ``functions_w_positional_arguments`` with a starred expression to alow it take in any number of arguments

  .. code-block:: python

    def identity_w_positional_arguments(*arguments):
        return arguments

  the terminal shows passing tests

*********************************************************************************
review
*********************************************************************************

From the tests I know

* I can use ``*name`` to represent any number of positional arguments
* that positional arguments are represented as tuples_ with parentheses - ``()``
* that identity :ref:`functions` return what they receive as input
* that constant :ref:`functions` return the same thing every time they are called
* :ref:`functions` are defined using the def_ keyword
* :ref:`functions` return :ref:`None` by default

Would you like to :ref:`test_functions_with keyword arguments? <test_functions_w_keyword_arguments>`

----

:doc:`/code/code_functions`