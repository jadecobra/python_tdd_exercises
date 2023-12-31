# Conditions

Sometimes we want programs to make decisions based on inputs or conditions, and can make this happen with conditional statements. Let us explore writing conditional statements in python with Test Driven Development using the [Truth Table](https://en.wikipedia.org/wiki/Truth_table) from mathematics

There are two boolean values

- ``(True)``
- ``(False)``

### Prerequisites

- [How I setup a Test Driven Development Environment.md](./How I How I setup a Test Driven Development Environment.md.md)

---

## Nullary Operations

Nullary operations do not take in inputs and always return the same value. They are singleton [functions](./07_FUNCTIONS.md)

### RED: make it fail

create a file named `test_truth_table.py` in the ``(tests)`` folder and add the text below

```python
import unittest
import truth_table


class TestNullaryOperations(unittest.TestCase):

    def test_logical_true(self):
        self.assertTrue(truth_table.logical_true())
```

the terminal updates to show a [ModuleNotFoundError](./MODULE_NOT_FOUND_ERROR.md)

### GREEN: make it pass

- add [ModuleNotFoundError](./MODULE_NOT_FOUND_ERROR.md) to the list of exceptions encountered
  ```python
  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError
  ```
- create a file named `truth_table.py` in the project folder and the terminal displays an [AttributeError](./ATTRIBUTE_ERROR.md) which we add to our list of exceptions encountered
  ```python
  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError
  # AttributeError
  ```
- add a singleton function named ``(logical_true)`` to `truth_table.py`
  ```python
  def logical_true():
      return True
  ```
  the terminal updates to show passing tests and we are reminded that ``(True)`` is ``(True)``

### REFACTOR: make it better

- let us add a test for ``(logical_false)`` to teh ``(TestNullaryOperations)`` class in `test_truth_table.py`
  ```python
    def test_logical_false(self):
        self.assertFalse(truth_table.logical_false())
  ```
  the terminal gives another [AttributeError](./ATTRIBUTE_ERROR.md) since there is no definition for ``(logical_false)`` in `truth_table.py`
- add a function definition for ``(logical_false)`` to `truth_table.py`
  ```python
  def logical_false():
      return True
  ```
  and the terminal shows an [AssertionError](./ASSERTION_ERROR.md) since the ``(logical_false)`` function currently returns a different value from what is expected
- update the return value to ``(False)`` and the terminal shows passing tests
  ```python
  def logical_false():
      return False
  ```
- We are again reminded that ``(False)`` is ``(False)`` and ``(True)`` is ``(True)``

---

## Unary Operations

There are two unary operations

- Logical Identity
- Logical Negation

### Logical Identity

A Logical Identity operation takes input and returns it as output, it is a passthrough [function](./07_FUNCTIONS.md)

#### RED: make it fail

Add a new ``(TestCase)`` to `test_truth_table.py`

```python


class TestUnaryOperations(unittest.TestCase):

    def test_logical_identity(self):
        self.assertTrue(truth_table.logical_identity(True))
        self.assertFalse(truth_table.logical_identity(False))
```

the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md) because there is no definition for ``(logical_identity)`` in `truth_table.py`

#### GREEN: make it pass

add a function definition for ``(logical_identity)`` to `truth_table.py`

```python
def logical_identity(value):
    return value
```

the terminal updates to show passing tests

### Logical Negation

A Logical Negation operation takes input and returns its opposite as output

#### RED: make it fail

add a test for ``(logical_negation)`` to `test_truth_table.py`

```python
    def test_logical_negation(self):
        self.assertFalse(truth_table.logical_negation(True))
        self.assertTrue(truth_table.logical_negation(False))
```

the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md), there is no definition for ``(logical_negation)`` in `truth_table.py`

#### GREEN: make it pass

- update `truth_table.py` with a definition for ``(logical_negation)`` using the solution we had for ``(logical_identity)``
  ```python
  def logical_negation(value):
      return value
  ```
  the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md). The ``(logical_negation)`` function returns the value it receives as input but the test expects it to return the opposite
- we use the ``(not)`` keyword to make the function return the opposite of what it receives. Update the return statement in ``(logical_negation)`` to return the opposite of the value it receives
  ```python
def logical_negation(value):
    return not value
  ```
  the terminal updates to show passing tests

Reviewing what we know so far

- ``(True)`` is `not False`
- ``(False)`` is `not True`
- ``(False)`` is ``(False)``
- ``(True)`` is ``(True)``

We have not written any conditional statements yet, only boolean values and their opposites. We will write some in [Logical Conjunction](./TRUTH_TABLE_02_LOGICAL_CONJUNCTION.md) next