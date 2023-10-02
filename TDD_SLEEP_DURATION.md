# Sleep Duration

Let us take a look at building a program which gives us the amount of time we have been asleep based on a given sleep and wake time which includes the dates to give an accurate result.

### Prerequisites

- [Setup a Test Driven Development Environment](./TDD_SETUP.md) with `sleep_duration` as the project name

---

##

### <span style="color:red">**RED**</span>: make it fail

write a failing test
```python
    def test_duration(self):
        self.assertEqual(
            sleep_duration.duration(
                wake_time='08:00',
                sleep_time="07:00"
            ),
            1
        )
```

the terminal shows a `NameError` which we add to our list of exceptions encountered

```python
# Exceptions Encountered
# AssertionError
# NameError
```

### <span style="color:green">**GREEN**</span>: make it pass

- add an import statement for the missing name
    ```python
    import unittest
    import sleep_duration


    class TestSleepDuration(unittest.TestCase):
    ```
    the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md) since we do not have a definition for `duration` in `sleep_duration.py`
- we update our list of exceptions encountered
    ```python
    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    ```
- add a name to `sleep_duration.py` and the terminal displays a `NameError`
    ```python
    duration
    ```
- make `duration` a variable by assigning it to the null value `None`
    ```python
    duration = None
    ```
    the terminal outputs a [TypeError](./TYPE_ERROR.md) because `None` is not callable
- we add the exception to our running list
    ```python
    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    ```
- define `duration` as a function
    ```python
    def duration():
        return None
    ```
    the [TypeError](./TYPE_ERROR.md) remains but with a different message the arguments passed in from the tests
- change the definition of `duration` to accept the required keyword argument
    ```python
    def duration(wake_time):
        return None
    ```
    the terminal outputs a similar message as before, this time for the second keyword argument
- we update the definition the same way
    ```python
    def duration(wake_time, sleep_time):
        return None
    ```
    the terminal now shows an [AssertionError](./ASSERTION_ERROR.md) since our duration function returns `None` and the test expects `1` as the duration when a sleep time of `07:00` and a wake time of `08:00` is given

### <span style="color:orange">**REFACTOR**</span>: make it better