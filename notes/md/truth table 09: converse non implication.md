# Write conditions in python

We will continue to step through learning conditional statements in python using Test Driven Development using the [Truth Table](https://en.wikipedia.org/wiki/Truth_table)

### Prerequisites

- [How I setup a Test Driven Development Environment.md](./How I How I setup a Test Driven Development Environment.md.md)

---

## Converse NonImplication

### RED: make it fail

add a test for converse nonimplication to ``(TestBinaryOperations)``

```python
    def test_converse_non_implication(self):
        self.assertFalse(truth_table.converse_non_implication(True, True))
        self.assertFalse(truth_table.converse_non_implication(True, False))
        self.assertTrue(truth_table.converse_non_implication(False, True))
        self.assertFalse(truth_table.converse_non_implication(False, False))
```

the terminal shows an [AttributeError](./ATTRIBUTE_ERROR.md)

### GREEN: make it pass

- add a function definition to `truth_table.py`
    ```python
    def converse_non_implication(p, q):
        return False
    ```
    since the first two cases pass, the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md) for the third case
- add a condition for it
    ```python
    def converse_non_implication(p, q):
        if p == False and q == True:
            return True
        return False
    ```
    all the tests pass

### REFACTOR: make it better

- use implied conditional testing
    ```python
    def converse_non_implication(p, q):
        if not p and q  == True:
            return True
        else:
            return False
    ```
    tests pass
    ```python
    def converse_non_implication(p, q):
        if not p and q:
            return True
        else:
            return False
    ```
- rewrite with a ``(return)`` statement
    ```python
    def converse_non_implication(p, q):
        return not p and q
    ```
    Another success! All tests pass

Our knowledge has increased. We know that for any boolean operation involving 2 inputs - ``(p)`` and ``(q)`` which can take the values ``(True)`` or ``(False)``
- ``(converse_non_implication)`` is `not p and q` which is different from `not(p and q)`
- ``(logical_nor)`` is `not(p or q)`
- ``(logical_nand)`` is `not(p and q)`
- ``(exclusive_disjunction)`` is `!=` aka opposite of ``(logical_equality)``
- ``(logical_equality)`` is `==`
- ``(logical_disjunction)`` is ``(or)``
- ``(logical_conjunction)`` is ``(and)``
- ``(and)`` is "not ``(or)``"
- ``(or)`` is "not ``(and)``"
- ``(False)`` is `not True`
- ``(True)`` is `not False`
- ``(False)`` is ``(False)``
- ``(True)`` is ``(True)``
