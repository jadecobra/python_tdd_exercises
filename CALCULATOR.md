# How to create a Calculator using Test Driven Development

We are going to explore creating a calculator in python using Test Driven Development

### Prerequisites

- [Setup a Test Driven Development Environment](./TDD_SETUP.md) with `calculator` as the project name

---

## Add Tests

we add a TODO list to `test_calculator.py` to keep track of action items
```python
import unittest


class TestCalculator(unittest.TestCase):

    def test_failure(self):
        self.assertTrue(True)

# TODO
# test importing
# test addition
# test subtraction
# test multiplication
# test division

# Exceptions Encountered
# AssertionError
```

the terminal responds to our change, though it still shows passing tests

```shell
==================== 1 passed in 0.01s ======================

Change detected: tests/test_calculator.py

[TODAYS_DATE] Running: py.test
===================== test session starts ===================
platform <YOUR_OPERATING_SYSTEM> -- python <YOUR_python_VERSION>, pytest-<VERSION>, pluggy-<VERSION>
rootdir: <YOUR_PATH>/calculator
collected 1 item

tests/test_calculator.py .                                                                                                    [100%]

==================== 1 passed in 0.00s ======================
```

## Test Imports

add an import statement for the `calculator` module we are working on
```python
import calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_failure(self):
        self.assertTrue(True)

# TODO
# test importing
# test addition
# test subtraction
# test multiplication
# test division

# Exceptions Encountered
# AssertionError
```

since the test passes we can remove `test importing` from our todo list

## Test Addition

Moving on to the next item from our TODO list, we add a test for addition

### <span style="color:red">**RED**</span>: make it fail

- let us add a method named `test_addition` to the `TestCalculator` class
    ```python
    import unittest
    import calculator


    class TestCalculator(unittest.TestCase):

        def test_failure(self):
            self.assertTrue(True)

        def test_addition(self):
            self.assertEqual(
                calculator.add(0, 1),
                1
            )

    # TODO
    # test addition
    # test subtraction
    # test multiplication
    # test division

    # Exceptions Encountered
    # AssertionError
    ```
    - we called a new testing method `self.assertEqual` which checks if 2 things are equal. It is similar to the statement `assert x == y` or asking `is x equal to y?`, we get more experience with using `self.assertEqual` in [AssertionError](./ASSERTION_ERROR.md)
    - there are two things passed to the `self.assertEqual` for evaluation in this case
        - first - `calculator.add(0, 1)` - where we pass the values `0` and `1` to the addition function we are testing
        - second - `1` - our expected result of the addition operation when it is given `0` and `1`
        - our expectation is that `calculator.add(0, 1) is equal to 1`
- the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)
    ```python
    ...
    collected 2 items

    tests/test_calculator.py F.                                     [100%]

    =========================== FAILURES =================================
    __________________ TestCalculator.test_addition ______________________

    self = <tests.test_calculator.TestCalculator testMethod=test_addition>

        def test_addition(self):
            self.assertEqual(
    >           calculator.add(0, 1),
                1
            )
    E       AttributeError: module 'calculator' has no attribute 'add'

    tests/test_calculator.py:12: AttributeError
    ==================== short test summary info =========================
    FAILED tests/test_calculator.py::TestCalculator::test_addition - AttributeError: module 'calculator' has no attribute 'add'
    ================== 1 failed, 1 passed in 0.02s =======================
    ```

    What does this mean?
    - The error is an `AttributeError` at line 12 in `test_calculator.py`
    - [AttributeError](https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError) is raised when we try to access/call an attribute and python cannot find it
    - we can think of `calculator.add` as an address. `calculator` refers to `calculator.py` and `add` refers to something in that file that currently does not exist

### <span style="color:green">**GREEN**</span>: make it pass

- open `calculator.py` in your Interactive Development Environment(IDE) and add the name `add`
    ```python
    add
    ```
    the terminal updates to show a `NameError` because `add` is not defined, there is no assignment to the name
    ```python
    E   NameError: name 'add' is not defined
    ```
- let us update our list of exceptions encountered with `NameError`
    ```python
    # Exceptions Encountered
    # AssertionError
    # NameError
    ```
- assign the name `add` to the null value `None`
    ```python
    add = None
    ```

    the terminal now shows a new Error

    ```python
    ================== FAILURES =============================
    ___________ TestCalculator.test_addition ________________

    self = <tests.test_calculator.TestCalculator testMethod=test_addition>

        def test_addition(self):
            self.assertEqual(
    >           calculator.add(0, 1),
                1
            )
    E       TypeError: 'NoneType' object is not callable

    tests/test_calculator.py:12: TypeError
    =============== short test summary info ========================
    FAILED tests/test_calculator.py::TestCalculator::test_addition - TypeError: 'NoneType' object is not callable
    ============== 1 failed, 1 passed in 0.03s ======================
    ```

- The `AttributeError` was fixed by declaring a variable `add` in the `calculator` module, even though it is currently defined as the null value `None`
- The new error is [TypeError](./TYPE_ERROR.md) which can occur when an `object` is used in a way that it was not intended for. In this case the `add` variable is not callable. Let us update our list of exceptions encountered
    ```python
    # Exceptions Encountered
    # AssertionError
    # NameError
    # TypeError
    ```
- To make it callable we have to define it as a [function](./FUNCTIONS.md) or a [class](./CLASSES.md). Testing the `def` keyword for creating functions we update our add variable in `calculator.py` to
    ```python
    def add():
        return None
    ```
    the terminal displays a different message but still a [TypeError](./TYPE_ERROR.md)
    ```python
    ===================== FAILURES ===========================
    ___________ TestCalculator.test_addition _________________

    self = <tests.test_calculator.TestCalculator testMethod=test_addition>

        def test_addition(self):
            self.assertEqual(
    >           calculator.add(0, 1),
                1
            )
    E       TypeError: add() takes 0 positional arguments but 2 were given

    tests/test_calculator.py:12: TypeError
    ============== short test summary info ======================
    FAILED tests/test_calculator.py::TestCalculator::test_addition - TypeError: add() takes 0 positional arguments but 2 were given
    ============= 1 failed, 1 passed in 0.02s ===================
    ```
- This `TypeError` indicates that the current definition of the `add` function takes in no arguments but we provided 2 in our call, since part of our requirements is that the function should be able to take in two numbers, we will update the `add` function in `calculator.py` to match
    ```python
    def add(x, y):
        return None
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)
    ```python
    self = <tests.test_calculator.TestCalculator testMethod=test_addition>

        def test_addition(self):
    >       self.assertEqual(
                calculator.add(0, 1),
                1
            )
    E       AssertionError: None != 1

    tests/test_calculator.py:11: AssertionError
    ================ short test summary info ======================
    FAILED tests/test_calculator.py::TestCalculator::test_addition - AssertionError: None != 1
    ================ 1 failed, 1 passed in 0.02s ==================
    ```
    An `AssertionError` was the first error we encountered in [Setup TDD](./TDD_SETUP.md) when we added a test for failure.
    It is raised when an assertion is `False`, since we are using `self.assertEqual` it means the two things we provided to as inputs are not equal. In other words `calculator.add(0, 1)` is currently not equal to `1`. Let us update the `add` function in `calculator.py` so it gives the expected value
    ```python
    def add(x, y):
        return 1
    ```
    Eureka! The test passes
    ```python
    tests/test_calculator.py ..                             [100%]

    ===================== 2 passed in 0.01s ======================
    ```

### <span style="color:orange">**REFACTOR**</span>: Make it Better

Wait a minute. Is it that easy? Do we just provide the solution to make it pass? In the green phase, yes. We do whatever it takes to make the test pass even if we have to cheat. The ease with which we solved this problems reveals a problem with our test, which means we need to Make it Better.

There are a few scenarios we can consider from the users perspective. If our users try to add other numbers that are not 0 and 1, the calculator will return 1, if they also try to add negative numbers, it will return 1. It always returns 1 so the addition function even though it passes our existing test does not quite meet the requirement.

- remove `test_failure` from `test_calculator.py` since we no longer need it
    ```python
    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            self.assertEqual(
                calculator.add(0, 1),
                1
            )
    ```
- <span style="color:red">**RED**</span>: make it fail
    add a new test to `test_addition` in `test_calculator.py`
    ```python
        def test_addition(self):
            self.assertEqual(
                calculator.add(0, 1),
                1
            )
            self.assertEqual(
                calculator.add(-1, 1),
                0
            )
    ```
    the terminal responds with an [AssertionError](./ASSERTION_ERROR.md) confirming that the `add` function always returns `1` regardless of inputs
    ```python
    ======================= FAILURES =====================================
    _____________ TestCalculator.test_addition ___________________________

    self = <tests.test_calculator.TestCalculator testMethod=test_addition>

        def test_addition(self):
            self.assertEqual(
                calculator.add(0, 1),
                1
            )
    >       self.assertEqual(
                calculator.add(-1, 1),
                0
            )
    E       AssertionError: 1 != 0

    tests/test_calculator.py:15: AssertionError
    ================== short test summary info ===========================
    FAILED tests/test_calculator.py::TestCalculator::test_addition - AssertionError: 1 != 0
    ================= 1 failed, 1 passed in 0.02s ========================
    ```
- <span style="color:green">**GREEN**</span>: make it pass
    let us update the `add` function in `calculator.py` to do something with the inputs
    ```python
    def add(x, y):
        return x + y
    ```
    and the terminal shows passing tests, our confidence in the `add` function has grown
    ```python
    tests/test_calculator.py ..                      [100%]

    ====================== 2 passed in 0.01s ==============
    ```
- <span style="color:orange">**REFACTOR**</span>: Make it Better
    what if we randomize the inputs to make sure the function behaves the way we expect for any given numbers? Update `test_calculator.py` to use the [random](https://docs.python.org/3/library/random.html?highlight=random#module-random) library
    ```python
    import calculator
    import random
    import unittest


    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            self.assertEqual(
                calculator.add(x, y),
                x+y
            )
    ```
    - we assign a variable named `x` to a random integer between -1 and 1
    - we assign a variable named `y` to a random integer between -1 and 1
    - we then test that when these two variables are given to the `add` function we get the sum of the 2 variables back

    the terminal updates to show passing tests
    ```python
    tests/test_calculator.py ..                             [100%]

    ================ 2 passed in 0.01s ===========================
    ```
    - we no longer need the previous 2 tests because this new test covers the scenarios for any positive and negative number including zero
    - we can remove `test addition` from the TODO list since it passed and the task is completed
    ```python
    # TODO
    # test subtraction
    # test multiplication
    # test division
    ```

That's the Test Driven Development pattern <span style="color:red">**RED**</span> <span style="color:green">**GREEN**</span> <span style="color:orange">**REFACTOR**</span>

---


## Test Subtraction

let us add the other tests
### <span style="color:red">**RED**</span> : make it fail

- update `test_calculator.py` with `test_subtraction`
    ```python
    import unittest
    import calculator
    import random


    class TestCalculator(unittest.TestCase):

        def test_failure(self):
            self.assertTrue(True)

        def test_addition(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            self.assertEqual(
                calculator.add(x, y),
                x+y
            )

        def test_subtraction(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            self.assertEqual(
                calculator.subtract(x, y),
                x-y
            )

    # TODO
    # test subtraction
    # test multiplication
    # test division

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # TypeError
    ```
    terminal response - AttributeError
    ```python

    self = <tests.test_calculator.TestCalculator testMethod=test_subtraction>

        def test_subtraction(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            self.assertEqual(
    >           calculator.subtract(x, y),
                x-y
            )
    E       AttributeError: module 'calculator' has no attribute 'subtract'

    tests/test_calculator.py:23: AttributeError
    =============== short test summary info ======================
    FAILED tests/test_calculator.py::TestCalculator::test_subtraction - AttributeError: module 'calculator' has no attribute 'subtract'
    ============== 1 failed, 2 passed in 0.03s ==================
    ```
    update `calculator.py`
    ```python
    def add(x, y):
        return x + y

    subtract = None
    ```
    terminal response - TypeError
    ```python
    self = <tests.test_calculator.TestCalculator testMethod=test_subtraction>

        def test_subtraction(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            self.assertEqual(
    >           calculator.subtract(x, y),
                x-y
            )
    E       TypeError: 'NoneType' object is not callable

    tests/test_calculator.py:23: TypeError
    =================== short test summary info =============
    FAILED tests/test_calculator.py::TestCalculator::test_subtraction - TypeError: 'NoneType' object is not callable
    =============== 1 failed, 2 passed in 0.02s ============
    ```
    update `calculator.py`
    ```python
    def add(x, y):
        return x + y

    def subtract():
        return None
    ```
    terminal response - TypeError
    ```python
    self = <tests.test_calculator.TestCalculator testMethod=test_subtraction>

        def test_subtraction(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            self.assertEqual(
    >           calculator.subtract(x, y),
                x-y
            )
    E       TypeError: subtract() takes 0 positional arguments but 2 were given

    tests/test_calculator.py:23: TypeError
    =================== short test summary info ============================
    FAILED tests/test_calculator.py::TestCalculator::test_subtraction - TypeError: subtract() takes 0 positional arguments but 2 were given
    =================== 1 failed, 2 passed in 0.02s =========================
    ```

### <span style="color:green">**GREEN**</span> : make it pass

- update `calculator.py`
    ```python
    def add(x, y):
        return x + y

    def subtract(x, y):
        return None
    ```
    terminal response - AssertionError
    ```python
    self = <tests.test_calculator.TestCalculator testMethod=test_subtraction>

        def test_subtraction(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
    >       self.assertEqual(
                calculator.subtract(x, y),
                x-y
            )
    E       AssertionError: None != 0

    tests/test_calculator.py:22: AssertionError
    ================= short test summary info ===================
    FAILED tests/test_calculator.py::TestCalculator::test_subtraction - AssertionError: None != 0
    ================ 1 failed, 2 passed in 0.02s ================
    ```
    update `calculator.py`
    ```python
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y
    ```
    terminal response - SUCCESS!
    ```shell
    collected 3 items

    tests/test_calculator.py ...                          [100%]

    ======================= 3 passed in 0.01s ==================
    ```
- remove `test subtraction` from the TODO list

### <span style="color:orange">**REFACTOR**</span>: make it better

- How can we make this better?
- Is there any duplication that could be removed? Yes
    - `x = random.randint(-1, 1)` happens 2 times
    - `y = random.randint(-1, 1)` happens 2 times


- update `test_calculator.py`
    ```python
    import unittest
    import calculator
    import random


    class TestCalculator(unittest.TestCase):

        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

        def test_failure(self):
            self.assertTrue(True)

        def test_addition(self):
            self.assertEqual(
                calculator.add(self.x, self.y),
                self.x+self.y
            )

        def test_subtraction(self):
            self.assertEqual(
                calculator.subtract(self.x, self.y),
                self.x-self.y
            )

    # TODO
    # test multiplication
    # test division

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # TypeError
    ```
    terminal response stays the same
    the x and y variables are now initialized as class variables that can be referenced later using `self.x` and `self.y`

---

### Test Multiplication

### <span style="color:red">**RED**</span> : make it fail

update `test_calculator.py` with `test_multiplication`
```python
import unittest
import calculator
import random


class TestCalculator(unittest.TestCase):

    x = random.randint(-1, 1)
    y = random.randint(-1, 1)

    def test_failure(self):
        self.assertTrue(True)

    def test_addition(self):
        self.assertEqual(
            calculator.add(self.x, self.y),
            self.x+self.y
        )

    def test_subtraction(self):
        self.assertEqual(
            calculator.subtract(self.x, self.y),
            self.x-self.y
        )

    def test_multiplication(self):
        self.assertEqual(
            calculator.multiply(self.x, self.y),
            self.x*self.y
        )

# TODO
# test multiplication
# test division

# Exceptions Encountered
# AssertionError
# AttributeError
# TypeError
```
terminal response - AttributeError

### <span style="color:green">**GREEN**</span> : make it pass
update `calculator.py`
```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
```
terminal response - SUCCESS
### <span style="color:orange">**REFACTOR**</span>: make it better

- remove `test_multiplication` from the TODO list
- Can you think of any way to make the code better?

---

### Test Division

### <span style="color:red">**RED**</span> : make it fail
- update `test_calculator.py` with `test_division`
    ```python
    import unittest
    import calculator
    import random


    class TestCalculator(unittest.TestCase):

        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

        def test_failure(self):
            self.assertTrue(True)

        def test_addition(self):
            self.assertEqual(
                calculator.add(self.x, self.y),
                self.x+self.y
            )

        def test_subtraction(self):
            self.assertEqual(
                calculator.subtract(self.x, self.y),
                self.x-self.y
            )

        def test_multiplication(self):
            self.assertEqual(
                calculator.multiply(self.x, self.y),
                self.x*self.y
            )

        def test_division(self):
            self.assertEqual(
                calculator.divide(self.x, self.y),
                self.x/self.y
            )

    # TODO
    # test division

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # TypeError
    ```
    terminal response - AttributeError
- update `calculator.py` with `divide`
    ```python
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y
    ```
    terminal response may vary. When y is 0 we get a [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ZeroDivisionError)
    ```python
    x = 1, y = 0

        def divide(x, y):
    >       return x / y
    E       ZeroDivisionError: division by zero

    calculator.py:11: ZeroDivisionError
    ================= short test summary info ========================
    FAILED tests/test_calculator.py::TestCalculator::test_division - ZeroDivisionError: division by zero
    ==================== 1 failed, 4 passed in 0.03s =================
    ```
    add `ZeroDivisionError` to the list of errors encountered

#### How to test for Errors
- <span style="color:red">**RED**</span> : make it fail
    - update `test_calculator.py` with a test for division by zero
    ```python
    import unittest
    import calculator
    import random


    class TestCalculator(unittest.TestCase):

        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

        def test_failure(self):
            self.assertTrue(True)

        def test_addition(self):
            self.assertEqual(
                calculator.add(self.x, self.y),
                self.x+self.y
            )

        def test_subtraction(self):
            self.assertEqual(
                calculator.subtract(self.x, self.y),
                self.x-self.y
            )

        def test_multiplication(self):
            self.assertEqual(
                calculator.multiply(self.x, self.y),
                self.x*self.y
            )

        def test_division(self):
            self.assertEqual(
                calculator.divide(self.x, 0),
                self.x/0
            )
            # self.assertEqual(
            #     calculator.divide(self.x, self.y),
            #     self.x/self.y
            # )

    # TODO
    # test division

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # TypeError
    # ZeroDivisionError
    ```
    terminal response
    ```python
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    x = 0, y = 0

        def divide(x, y):
    >       return x / y
    E       ZeroDivisionError: division by zero

    calculator.py:11: ZeroDivisionError
    ================= short test summary info ======================
    FAILED tests/test_calculator.py::TestCalculator::test_division - ZeroDivisionError: division by zero
    =================== 1 failed, 4 passed in 0.02s ================
    ```

- <span style="color:green">**GREEN**</span> : make it pass
    - update `test_calculator.py` to confirm that `ZeroDivisionError` is raised when dividing by 0
    ```python
    import unittest
    import calculator
    import random


    class TestCalculator(unittest.TestCase):

        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

        def test_failure(self):
            self.assertTrue(True)

        def test_addition(self):
            self.assertEqual(
                calculator.add(self.x, self.y),
                self.x+self.y
            )

        def test_subtraction(self):
            self.assertEqual(
                calculator.subtract(self.x, self.y),
                self.x-self.y
            )

        def test_multiplication(self):
            self.assertEqual(
                calculator.multiply(self.x, self.y),
                self.x*self.y
            )

        def test_division(self):
            with self.assertRaises(ZeroDivisionError):
                calculator.divide(self.x, 0)
            # self.assertEqual(
            #     calculator.divide(self.x, self.y),
            #     self.x/self.y
            # )

    # TODO
    # test division

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # TypeError
    # ZeroDivisionError
    ```
    terminal response - SUCCESS - We now have a way to `catch` Exceptions in testing, allowing tests to continue when they encounter expected failures

- <span style="color:orange">**REFACTOR**</span>: make it better
    - update `test_calculator.py` to test other division cases when the divisor is not 0 by adding a while condition
    ```python
    import unittest
    import calculator
    import random


    class TestCalculator(unittest.TestCase):

        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

        def test_failure(self):
            self.assertTrue(True)

        def test_addition(self):
            self.assertEqual(
                calculator.add(self.x, self.y),
                self.x+self.y
            )

        def test_subtraction(self):
            self.assertEqual(
                calculator.subtract(self.x, self.y),
                self.x-self.y
            )

        def test_multiplication(self):
            self.assertEqual(
                calculator.multiply(self.x, self.y),
                self.x*self.y
            )

        def test_division(self):
            with self.assertRaises(ZeroDivisionError):
                calculator.divide(self.x, 0)
            while self.y == 0:
                self.y = random.randint(-1, 1)
            self.assertEqual(
                calculator.divide(self.x, self.y),
                self.x/self.y
            )

    # TODO
    # test division

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # TypeError
    # ZeroDivisionError
    ```
    - `while self.y == 0:` this creates a loop, you are telling python to repeat the block that follows as long as `self.y is equal to 0`
    - remove `test_division` from `TODO`

---

***CONGRATULATIONS*** You made it through writing a program that can perform the 4 basic arithmetic operations using Test Driven Development
