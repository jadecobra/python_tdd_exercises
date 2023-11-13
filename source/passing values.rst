
Passing Values
==============

When testing or using a program, I provide data as inputs to the program with an expectation of a return value.

.. code-block:: python
    input_data -> process -> output
```

It is similar to functions in mathematics where I represent a function as ``f`` with inputs ``x`` and a return value of ``y``


.. code-block:: python
    f(x) -> y
```

In testing I am asking the question is `f(x)` equal to ``y`` for the given input ``x`` for example  I could use an assert statement

.. code-block:: python
    assert f(x) == y
```

or use the `self.assertEqual` :doc:`method <functions>` from `unittest.TestCase`

.. code-block:: python
    self.assertEqual(f(x), y)
```

I am going to look at how to pass values from tests to programs using `string interpolation` with Test Driven Development

Prerequisites
-------------
[Setup a Test Driven Development Environment](./Setup a Test Driven Development Environment.rst)

---

## How to Pass Values

### RED: make it fail

create a file called `test_passing_values.py` in the ``tests`` folder with the following text


.. code-block:: python
import unittest
import telephone


class TestPassingValues(unittest.TestCase):

    def test_text_messages(self):
        self.assertEqual(
            telephone.Telephone.text('hello'),
            'I received this message: hello'
        )
```
the terminal updates to show a [ModuleNotFoundError](./ModuleNotFoundError.rst) and I add it to the list of exceptions encountered

.. code-block:: python
# Exceptions Encountered
# AssertionError
# ModuleNotFoundError
```

### GREEN: make it pass

- create a file called `telephone.py` in the project folder and the terminal updates to show an :doc:`AttributeError` which I add to the list of exceptions

.. code-block:: python
    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    ```
- update `telephone.py` with a class definition

.. code-block:: python
    class Telephone(object):

        pass
    ```
    the terminal still displays an :doc:`AttributeError` but with a different message
- I add a definition for an attribute called ``text`` to the ``Telephone`` class

.. code-block:: python
    class Telephone(object):

        text = None
    ```
    the terminal updates to show a :doc:`TypeError` because ``text`` is not `callable <https://docs.python.org/3/glossary.html#term-callable>`_ and I add the new exception to the list of exceptions encountered

.. code-block:: python
    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError
    ```
- change ``text`` to a :doc:`method <functions>` to make it callable

.. code-block:: python
    class Telephone(object):

        def text():
            return None
    ```
    the terminal displaysa :doc:`TypeError` this time because when I called `telephone.Telephone.text('hello')` in the test I provided a positional argument as input with the value ``hello``, but the signature of the :doc:`method <functions>` I defined does not take in any arguments
- modify the definition for ``text`` to take in a value

.. code-block:: python
    class Telephone(object):


        def text(value):
            return None
    ```
    I now see an :doc:`AssertionError` in the terminal
- update the return statement with the expected value to make the test pass

.. code-block:: python
        def text(value):
            return 'I received this message: hello'
    ```
    the test passes

### REFACTOR: make it better

The problem with this solution is that no matter what value I send to the `Telephone.text` :doc:`method <functions>` it will always return `'I received this message: hello'`. I need to make it more generic so it returns a value that is dependent on the input

- RED: make it fail

    add a new failing test to ``test_text_messages``


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
    ```

    the terminal updates to show an :doc:`AssertionError`

- GREEN: make it pass

    I can add variable values to strings by using [string interpolation](https://peps.python.org/pep-0498/). Let us try this out by changing the ``text`` :doc:`method <functions>` in `telephone.py`

.. code-block:: python
    def text(value):
        return f'I received this message: {value}'
    ```
    the terminal updates to show passing tests

## Passing Data Structures

I can try this with other python [data structures](./DATA_STRUCTURES.rst) to see what happens

### RED: make it fail

update ``test_text_messages`` with a new test

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
```

the terminal updates to show an :doc:`AssertionError`

### GREEN: make it pass

update the test to match the expected value


.. code-block:: python
    self.assertEqual(
        telephone.Telephone.text(None),
        "I received this message: None"
    )
```

the terminal shows passing tests

### REFACTOR: make it better

- as an exercise add the following tests to ``test_text_messages``

.. code-block:: python
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
    ```
    an :doc:`AssertionError` is displayed in the terminal
- update the test to match the expected output

.. code-block:: python
        self.assertEqual(
            telephone.Telephone.text(bool),
            "I received this message: <class 'bool'>"
        )
    ```
    the terminal updates with an :doc:`AssertionError` for the next test.
- repeat the solution for each data type until all tests pass

VOILA
You now know how to pass values and represent values as strings using interpolation