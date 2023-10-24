How to Pass Values
==================

When testing or using a program, we provide data as inputs to the program with an expectation of a return value.

.. code-block:: python
    input_data -> process -> output
```

It is similar to functions in mathematics where we represent a function as ``f`` with inputs ``x`` and a return value of ``y``


.. code-block:: python
    f(x) -> y
```

In testing we are asking the question is `f(x)` equal to ``y`` for the given input ``x`` e.g. we could use an assert statement

.. code-block:: python
    assert f(x) == y
```

or use the `self.assertEqual` method from `unittest.TestCase`

.. code-block:: python
    self.assertEqual(f(x), y)
```

We are going to look at how to pass values from tests to programs using `string interpolation` with Test Driven Development

Prerequisites
-------------
[How I setup a Test Driven Development Environment](./How I setup a Test Driven Development Environment.rst)

---

## How to Pass Values

### RED: make it fail

create a file named `test_passing_values.py` in the ``tests`` folder with the following text


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
the terminal updates to show a [ModuleNotFoundError](./ModuleNotFoundError.rst) and we add it to our list of exceptions encountered

.. code-block:: python
# Exceptions Encountered
# AssertionError
# ModuleNotFoundError
```

### GREEN: make it pass

- create a file named `telephone.py` in the project folder and the terminal updates to show an [AttributeError](./AttributeError.rst) which we add to our list of exceptions

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
    the terminal still displays an [AttributeError](./AttributeError.rst) but with a different message
- we add a definition for an attribute named ``text`` to the ``Telephone`` class

.. code-block:: python
    class Telephone(object):

        text = None
    ```
    the terminal updates to show a [TypeError](./TypeError.rst) because ``text`` is not callable and we add the new exception to our list of exceptions encountered

.. code-block:: python
    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError
    ```
- change ``text`` to a method to make it callable

.. code-block:: python
    class Telephone(object):

        def text():
            return None
    ```
    the terminal displays a [TypeError](./TypeError.rst) this time because when we called `telephone.Telephone.text('hello')` in the test we provided a positional argument as input with the value ``hello``, but the signature of the method we defined does not take in any arguments
- modify the definition for ``text`` to take in a value

.. code-block:: python
    class Telephone(object):


        def text(value):
            return None
    ```
    we now see an [AssertionError](./AssertionError.rst) in the terminal
- update the return statement with the expected value to make the test pass

.. code-block:: python
        def text(value):
            return 'I received this message: hello'
    ```
    the test passes

### REFACTOR: make it better

The problem with this solution is that no matter what value we send to the `Telephone.text` method it will always return `'I received this message: hello'`. We need to make it more generic so it returns a value that is dependent on the input

- RED: make it fail

    let us add a new failing test to ``test_text_messages``


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

    the terminal updates to show an [AssertionError](./AssertionError.rst)

- GREEN: make it pass

    We can add variable values to strings by using [string interpolation](https://peps.python.org/pep-0498/). Let us try this out by changing the ``text`` method in `telephone.py`

.. code-block:: python
    def text(value):
        return f'I received this message: {value}'
    ```
    the terminal updates to show passing tests

## Passing Data Structures

we can try this with other python [data structures](./DATA_STRUCTURES.rst) to see what happens

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

the terminal updates to show an [AssertionError](./AssertionError.rst)

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
    an [AssertionError](./AssertionError.rst) is displayed in the terminal
- update the test to match the expected output

.. code-block:: python
        self.assertEqual(
            telephone.Telephone.text(bool),
            "I received this message: <class 'bool'>"
        )
    ```
    the terminal updates with an [AssertionError](./AssertionError.rst) for the next test.
- repeat the solution for each data type until all tests pass

VOILA
You now know how to pass values and represent values as strings using interpolation