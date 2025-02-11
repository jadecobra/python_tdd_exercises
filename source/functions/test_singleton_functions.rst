.. include:: ../links.rst

.. _test_singleton_functions:

#################################################################################
functions: test_singleton_functions
#################################################################################

----

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with ``functions`` as the name of the project

----

*********************************************************************************
test_singleton_functions
*********************************************************************************

Singleton :ref:`functions` always return the same thing when called

red: make it fail
---------------------------------------------------------------------------------

I add a test to ``test_functions.py``

.. code-block:: python

    def test_singleton_functions(self):
        self.assertEqual(functions.singleton(), 'my_first_name')

the terminal shows :ref:`AttributeError`

green: make it pass
---------------------------------------------------------------------------------

I change the :ref:`function<functions>` to make it pass

.. code-block:: python

  def singleton():
      return 'my_first_name'

----

*********************************************************************************
test_singleton_functions_w_inputs
*********************************************************************************

red: make it fail
---------------------------------------------------------------------------------

I add a new test that checks if a singleton that takes inputs returns the same value regardless of the inputs

.. code-block:: python

  def test_singleton_functions_w_inputs(self):
      self.assertEqual(
          functions.singleton_w_inputs('Bob', 'James', 'Frank'),
          'joe'
      )
      self.assertEqual(
          functions.singleton_w_inputs('a', 2, 'c', 3),
          'joe'
      )

the terminal shows :ref:`AttributeError`



green: make it pass
---------------------------------------------------------------------------------

and I add a:ref:`function<functions>`for ``singleton_w_inputs`` to ``functions.py``

.. code-block:: python

  def singleton_w_inputs(*args):
      return 'joe'

the terminal shows passing tests

----

*********************************************************************************
review
*********************************************************************************

From the tests I know

* that singleton :ref:`functions` return the same thing every time they are called
* :ref:`functions` are defined using the def_ keyword
* :ref:`functions` return :ref:`None` by default

Would you like to :ref:`test passthrough functions?<test_passthrough_functions>`

----

:doc:`/code/code_functions`