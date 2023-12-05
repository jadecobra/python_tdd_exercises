
How to pass values
==================

When testing or using a program, data can be provided as input to the program with an expectation of an output, I think of it this way

.. code-block:: python

  input_data -> process -> output


Which is similar to functions in mathematics where a function is represented as ``f`` with input ``x`` and output ``y``


.. code-block:: python

  f(x) -> y

or in other words

.. code-block:: python

  process(input_data) -> output


When testing code I am asking the question is the result of calling ``f`` with a given input ``x`` equal to ``y``? or is the result of running ``process`` with a given ``input_data`` equal to ``output``? For example  I could use an assert statement

.. code-block:: python

  assert f(x) == y
  assert process(input_data) == output


or use the `self.assertEqual` :doc:`method </functions/functions>` from `unittest.TestCase`

.. code-block:: python

  self.assertEqual(f(x), y)
  self.assertEqual(process(input_data), output)


This chapter explores how to pass values from tests to programs using `Formatted string literals <https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals>`_ for placing values inside a string


RED: make it fail
-----------------

I create a file called `test_passing_values.py` in the ``tests`` folder with the following text


.. code-block:: python

  import unittest
  import telephone


  class TestPassingValues(unittest.TestCase):

      def test_text_messages(self):
          self.assertEqual(
              telephone.Telephone.text('hello'),
              'I received this message: hello'
          )

the terminal shows a :doc:`/exceptions/ModuleNotFoundError` and I add it to the list of exceptions encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError


GREEN: make it pass
---------------------

- I create a file called ``telephone.py`` in the project folder and the terminal shows an :doc:`/exceptions/AttributeError` which I add to the list of exceptions

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

- I add a :doc:`class </classes/classes>` definition to ``telephone.py``

  .. code-block:: python

    class Telephone(object):

        pass

  the terminal still displays an :doc:`/exceptions/AttributeError` but with a different message
- I add a name called ``text`` to the ``Telephone`` class

  .. code-block:: python

    class Telephone(object):

        text

  the terminal displays a ``NameError`` and I add it to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError

- I assign ``text`` to the null value :doc:`None </data_structures/data_structures_none>`

  .. code-block:: python

    class Telephone(object):

        text = None

  and the terminal shows a :doc:`/exceptions/TypeError` because ``text`` is not `callable <https://docs.python.org/3/glossary.html#term-callable>`_
- I add the exception to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError

- I change ``text`` to a :doc:`method </functions/functions>` to make it callable

  .. code-block:: python

    class Telephone(object):

        def text():
            return None

  and the terminal displays another :doc:`/exceptions/TypeError` because when I called ``telephone.Telephone.text('hello')`` in the test I provided a positional argument as input with the value ``hello``, but the signature of the ``text`` :doc:`method </functions/functions>` does not take in any arguments
- I change the definition for ``text`` to make it accept a value as input

  .. code-block:: python

    class Telephone(object):


        def text(value):
            return None

  I now see an :doc:`/exceptions/AssertionError` in the terminal
- and change the return statement with the expected value to make the test pass

  .. code-block:: python

      def text(value):
          return 'I received this message: hello'


REFACTOR: make it better
-------------------------

The problem with this solution is that no matter what value I send to the `Telephone.text` :doc:`method </functions/functions>` it will always return `'I received this message: hello'`. I need to make it more generic so it returns a value that is dependent on the input

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new failing test to ``test_text_messages``

.. code-block:: python

  def test_text_messages(self):
      self.assertEqual(
          telephone.Telephone.text('hello'),
          'I received this message: hello'
      )
      self.assertEqual(
          telephone.Telephone.text('yes'),
          'I received this message: yes'
      )


the terminal shows an :doc:`/exceptions/AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I can add variable values to strings by using `string interpolation <https://peps.python.org/pep-0498/>`, I will change the ``text`` :doc:`method </functions/functions>` in ``telephone.py``

.. code-block:: python

  def text(value):
      return f'I received this message: {value}'

the terminal shows passing tests

Passing Data Structures
-----------------------

I want to try this with other python data structures to see what happens

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new failing test to ``test_text_messages``

.. code-block:: python

  def test_text_messages(self):
      self.assertEqual(
          telephone.Telephone.text('hello'),
          'I received this message: hello'
      )
      self.assertEqual(
          telephone.Telephone.text('yes'),
          'I received this message: yes'
      )
      self.assertEqual(
          telephone.Telephone.text(None),
          "I received this message: 'None'"
      )

the terminal shows an :doc:`/exceptions/AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the test to match the expected value


.. code-block:: python

  self.assertEqual(
      telephone.Telephone.text(None),
      "I received this message: None"
  )


the terminal shows passing tests

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

* as an exercise I add more tests to ``test_text_messages``

  .. code-block:: python

    def test_text_messages(self):
        self.assertEqual(
            telephone.Telephone.text('hello'),
            'I received this message: hello'
        )
        self.assertEqual(
            telephone.Telephone.text('yes'),
            'I received this message: yes'
        )
        self.assertEqual(
            telephone.Telephone.text(None),
            "I received this message: None"
        )
        self.assertEqual(
            telephone.Telephone.text(bool),
            "I received this message: 'bool'"
        )
        self.assertEqual(
            telephone.Telephone.text(int),
            "I received this message: 'int'"
        )
        self.assertEqual(
            telephone.Telephone.text(float),
            "I received this message: 'float'"
        )
        self.assertEqual(
            telephone.Telephone.text(tuple),
            "I received this message: 'tuple'"
        )
        self.assertEqual(
            telephone.Telephone.text(list),
            "I received this message: 'list'"
        )
        self.assertEqual(
            telephone.Telephone.text(set),
            "I received this message: 'set'"
        )
        self.assertEqual(
            telephone.Telephone.text(dict),
            "I received this message: 'dict'"
        )

  an :doc:`/exceptions/AssertionError` is displayed in the terminal
* I change the test to match the expected output

  .. code-block:: python

      self.assertEqual(
          telephone.Telephone.text(bool),
          "I received this message: <class 'bool'>"
      )

  the terminal displays an :doc:`/exceptions/AssertionError` for the next test.
* I repeat the solution for each data type until all tests pass

  .. code-block:: python

    def test_text_messages(self):
        self.assertEqual(
            telephone.Telephone.text('hello'),
            'I received this message: hello'
        )
        self.assertEqual(
            telephone.Telephone.text('yes'),
            'I received this message: yes'
        )
        self.assertEqual(
            telephone.Telephone.text(None),
            "I received this message: None"
        )
        self.assertEqual(
            telephone.Telephone.text(bool),
            "I received this message: <class 'bool'>"
        )
        self.assertEqual(
            telephone.Telephone.text(int),
            "I received this message: <class 'int'>"
        )
        self.assertEqual(
            telephone.Telephone.text(float),
            "I received this message: <class 'float'>"
        )
        self.assertEqual(
            telephone.Telephone.text(tuple),
            "I received this message: <class 'tuple'>"
        )
        self.assertEqual(
            telephone.Telephone.text(list),
            "I received this message: <class 'list'>"
        )
        self.assertEqual(
            telephone.Telephone.text(set),
            "I received this message: <class 'set'>"
        )
        self.assertEqual(
            telephone.Telephone.text(dict),
            "I received this message: <class 'dict'>"
        )

VOILA! You now know how to pass values and represent values as strings using interpolation