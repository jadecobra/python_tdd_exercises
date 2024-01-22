
###################
How to pass values
###################

When testing or using a program, data can be provided as input to the program with an expectation of an output, I think of it this way

.. code-block:: python

  input_data -> process -> output


Which is similar to functions in mathematics where a function is represented as ``f`` with ``x`` as input and ``y`` as output


.. code-block:: python

  f(x) -> y

in other words

.. code-block:: python

  process(input_data) -> output


When testing code I want to know if the result of calling ``f`` with a given input ``x`` is equal to ``y`` or if the result of running ``process`` with ``input_data`` is equal to ``output``

* Here is an example with an assert statement

  .. code-block:: python

    assert f(x) == y
    assert process(input_data) == output

* Here is an example with the `unittest.TestCase.assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ :doc:`method </functions/functions>`

  .. code-block:: python

    self.assertEqual(f(x), y)
    self.assertEqual(process(input_data), output)


this chapter goes over how to pass values from tests to programs using `Formatted string literals <https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals>`_ to place values inside a string

****************
Prerequisites
****************

:doc:`Create a Test Driven Development Environment </how_to/create_tdd_environment>` with ``telephone`` as the project name

----

*******************
RED: make it fail
*******************

I add a test to ``test_telephone.py``

.. code-block:: python

  class TestTelephone(unittest.TestCase):

      def test_failure(self):
          self.assertFalse(True)

      def test_text_messages(self):
          self.assertEqual(
              telephone.text('hello'),
              'I received this message: hello'
          )

and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

.. code-block:: python

  NameError: name 'telephone' is not defined

which I add to the list of exceptions

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # NameError

**********************
GREEN: make it pass
**********************

* I remove ``test_failure`` then add an import statement for the ``telephone`` module

  .. code-block:: python

    import telephone
    import unittest

  the terminal shows an :doc:`/exceptions/AttributeError` ::

    AttributeError: module 'telephone' has no attribute 'text'

* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

- then add a name to ``telephone.py``

  .. code-block:: python

    text

  and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    NameError: name 'text' is not defined


- I assign ``text`` to the null value :doc:`None </data_structures/none>`

  .. code-block:: python

    text = None

  and the terminal shows a :doc:`/exceptions/TypeError` because ``text`` is not `callable <https://docs.python.org/3/glossary.html#term-callable>`_

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

- I add the exception to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

- I change ``text`` in ``telephone.py`` to a :doc:`function </functions/functions>` to make it `callable <https://docs.python.org/3/glossary.html#term-callable>`_

  .. code-block:: python

      def text():
          return None

  and the terminal shows another :doc:`/exceptions/TypeError`

  .. code-block:: python

    TypeError: text() takes 0 positional arguments but 1 was given

  I provided a positional argument as input with the value ``'hello'`` when I called ``telephone.text`` in the test , but the current signature of the ``text`` :doc:`function </functions/functions>` does not allow it accept any inputs
- I change the definition for ``text`` to make it accept a value as input

  .. code-block:: python

    def text(value):
        return None

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: None != 'I received this message: hello'

- I change the return value to match the expectation and the test pass

  .. code-block:: python

    def text(value):
        return 'I received this message: hello'

**************************
REFACTOR: make it better
**************************

The problem with this solution is that no matter what value I send to the ``text`` :doc:`function </functions/functions>` it will always return ``'I received this message: hello'``. I need to make it return a value based on the input it receives

RED: make it fail
=========================

I add a new failing test to ``test_text_messages``

.. code-block:: python

  def test_text_messages(self):
      self.assertEqual(
          telephone.text('hello'),
          'I received this message: hello'
      )
      self.assertEqual(
          telephone.text('yes'),
          'I received this message: yes'
      )


the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: 'I received this message: hello' != 'I received this message: yes'

GREEN: make it pass
=========================

I change the ``text`` :doc:`function </functions/functions>` in ``telephone.py`` to use an ``f`` string which allows passing variable values to strings. This is called `string interpolation <https://peps.python.org/pep-0498/>`_

.. code-block:: python

  def text(value):
      return f'I received this message: {value}'

the terminal shows passing tests

**************************
Passing Data Structures
**************************

I want to try this with other python data structures to see what happens

RED: make it fail
=========================

I add a new failing test to ``test_text_messages``

.. code-block:: python

  def test_text_messages(self):
      self.assertEqual(
          telephone.text('hello'),
          'I received this message: hello'
      )
      self.assertEqual(
          telephone.text('yes'),
          'I received this message: yes'
      )
      self.assertEqual(
          telephone.text(None),
          'I received this message: "None"'
      )

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: 'I received this message: None' != 'I received this message: "None"'

GREEN: make it pass
=========================

I change the test to match the expected value


.. code-block:: python

  self.assertEqual(
      telephone.text(None),
      'I received this message: None'
  )


the terminal shows passing tests

REFACTOR: make it better
=========================

* as an exercise I add more tests to ``test_text_messages``

  .. code-block:: python

    def test_text_messages(self):
        self.assertEqual(
            telephone.text('hello'),
            'I received this message: hello'
        )
        self.assertEqual(
            telephone.text('yes'),
            'I received this message: yes'
        )
        self.assertEqual(
            telephone.text(None),
            'I received this message: None'
        )
        self.assertEqual(
            telephone.text(bool),
            "I received this message: 'bool'"
        )
        self.assertEqual(
            telephone.text(int),
            "I received this message: 'int'"
        )
        self.assertEqual(
            telephone.text(float),
            "I received this message: 'float'"
        )
        self.assertEqual(
            telephone.text(tuple),
            "I received this message: 'tuple'"
        )
        self.assertEqual(
            telephone.text(list),
            "I received this message: 'list'"
        )
        self.assertEqual(
            telephone.text(set),
            "I received this message: 'set'"
        )
        self.assertEqual(
            telephone.text(dict),
            "I received this message: 'dict'"
        )

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: "I received this message: <class 'bool'>" != "I received this message: 'bool'"

* I change the test to match the expected output

  .. code-block:: python

      self.assertEqual(
          telephone.text(bool),
          "I received this message: <class 'bool'>"
      )

  the terminal shows an :doc:`/exceptions/AssertionError` for the next test

  .. code-block:: python

    AssertionError: "I received this message: <class 'int'>" != "I received this message: 'int'"

* I repeat the solution for each data type until all tests pass

  .. code-block:: python

    def test_text_messages(self):
        self.assertEqual(
            telephone.text('hello'),
            'I received this message: hello'
        )
        self.assertEqual(
            telephone.text('yes'),
            'I received this message: yes'
        )
        self.assertEqual(
            telephone.text(None),
            "I received this message: None"
        )
        self.assertEqual(
            telephone.text(bool),
            "I received this message: <class 'bool'>"
        )
        self.assertEqual(
            telephone.text(int),
            "I received this message: <class 'int'>"
        )
        self.assertEqual(
            telephone.text(float),
            "I received this message: <class 'float'>"
        )
        self.assertEqual(
            telephone.text(tuple),
            "I received this message: <class 'tuple'>"
        )
        self.assertEqual(
            telephone.text(list),
            "I received this message: <class 'list'>"
        )
        self.assertEqual(
            telephone.text(set),
            "I received this message: <class 'set'>"
        )
        self.assertEqual(
            telephone.text(dict),
            "I received this message: <class 'dict'>"
        )

VOILA! You now know how to pass values from a test to a program and can represent values as strings using interpolation. You also encountered the following exceptions

* :doc:`/exceptions/AssertionError`
* `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_
* :doc:`/exceptions/AttributeError`
* :doc:`/exceptions/TypeError`

Would you like to know :doc:`/how_to/create_person`?

----

:doc:`/code/code_pass_values`