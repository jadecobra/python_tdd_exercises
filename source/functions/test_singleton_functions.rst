.. include:: ../links.rst

.. _test_singleton_functions:

#############################################################################
functions: test_singleton_functions
#############################################################################

----

.. contents:: table of contents
  :local:
  :depth: 1

----

Singleton :ref:`functions` always return the same thing when called

.. _test_singleton_functions_red:

*****************************************************************************
red: make it fail
*****************************************************************************

I add a test to ``test_functions.py``

.. code-block:: python

    def test_singleton_functions(self):
        self.assertEqual(functions.singleton(), 'my_first_name')

the terminal shows an :ref:`AttributeError`

.. _test_singleton_functions_green:

*****************************************************************************
green: make it pass
*****************************************************************************

I make ``functions.py`` to make it pass

.. code-block:: python

  def singleton():
      return 'my_first_name'

.. _test_singleton_functions_w_inputs:

*****************************************************************************
test_singleton_functions_w_inputs
*****************************************************************************

.. _test_singleton_functions_w_inputs_red:

red: make it pass
#############################################################################


I add a new test that checks if a singleton that accepts inputs returns the same value regardless of the inputs

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

the terminal shows an :ref:`AttributeError`

.. _test_singleton_functions_w_inputs_green:

green: make it pass
#############################################################################

and I add a function for ``singleton_w_inputs`` to ``functions.py``

.. code-block:: python

  def singleton_w_inputs(*args):
      return 'joe'

the terminal shows passing tests

----

.. _test_singleton_functions_w_inputs_review:

*****************************************************************************
review
*****************************************************************************

From the tests I know

* that singleton functions return the same thing every time they are called
* functions are defined using the `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword
* functions return :ref:`None` by default

Would you like to :ref:`test_passthrough_functions`?

----

:doc:`/code/code_functions`