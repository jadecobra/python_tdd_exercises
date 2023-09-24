# How to create a Calculator using Test Driven Development

We are going to explore creating a calculator with python using Test Driven Development

### Prerequisites

- [Setup a Test Driven Development Environment](./TDD_SETUP.md) with `calculator` as the project name

---

## Add Tests

let us add a TODO list to `test_calculator.py` to keep track of action items
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

since the test passes we can remove `test importing` from our TODO list

## Test Addition

Moving on to the next item we test for addition

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
    - we called a new testing method from the `unittest.TestCase` class called `assertEqual` which checks if 2 things are equal. It is similar to the statement `assert x == y` or asking `is x equal to y?`
    - there are two things passed to the `assertEqual` method for evaluation in this case
        - first - `calculator.add(0, 1)` - where we give the values `0` and `1` as inputs
        - second - `1` - our expected result from `calculator.add` when it is given `0` and `1`
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
    - [AttributeError](https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError) is raised when we try to access or call an attribute that python cannot find
    - we can think of `calculator.add` as an address
        - `calculator` refers to `calculator.py`
        - `add` refers to something with `calculator.py` file that currently does not exist

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

    the terminal now shows a new error

    ```python
    E       TypeError: 'NoneType' object is not callable
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
    the terminal still shows a [TypeError](./TYPE_ERROR.md) but with a different message, progress
    ```python
    E       TypeError: add() takes 0 positional arguments but 2 were given
    ```
- This `TypeError` indicates that the current definition of the `add` function takes in no arguments but we provided 2 in our call, since part of our requirement is that the `add` function should take in two numbers, we will update it in `calculator.py` to match
    ```python
    def add(x, y):
        return None
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)
    ```python
    E       AssertionError: None != 1
    ```
    An `AssertionError` was the first error we encountered in [Setup TDD](./TDD_SETUP.md) after adding a test for failure.
    It is raised when an assertion is `False`, since we are using `self.assertEqual` it means the two things we provided as inputs are not equal. In other words `calculator.add(0, 1)` is currently not equal to `1`. Let us update the `add` function in `calculator.py` so it gives the expected value
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

Wait a minute. Is it that easy? Do we just provide the solution to make it pass? In the green phase, yes. We do whatever it takes to make the test pass even if we have to cheat. The ease with which we solved this problems reveals a problem with our test, which means we need to "Make it Better".

There are a few scenarios we can consider from the users perspective. If our users try to add other numbers that are not 0 and 1, the calculator will return 1. If they also try to add negative numbers, it will also return 1. The function always returns 1 regardless of the inputs the user gives, even though it passes our existing test it still does not meet the actual requirement.

- remove `test_failure` from `test_calculator.py` since we no longer need it
    ```python
    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            self.assertEqual(
                calculator.add(0, 1),
                1
            )
    ```
- <span style="color:red">**RED**</span>: make it fail by adding a new test to `test_addition` in `test_calculator.py`
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
    E       AssertionError: 1 != 0
    ```
- <span style="color:green">**GREEN**</span>: make it pass by updating the `add` function in `calculator.py` to add up the inputs
    ```python
    def add(x, y):
        return x + y
    ```
    and the terminal shows passing tests, increasing our confidence in the `add` function
    ```python
    tests/test_calculator.py ..                      [100%]

    ====================== 2 passed in 0.01s ==============
    ```
- <span style="color:orange">**REFACTOR**</span>: Make it Better by randomizing the inputs to make sure the function behaves the way we expect for any given numbers. Update `test_calculator.py` to use the [random](https://docs.python.org/3/library/random.html?highlight=random#module-random) library
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
    - we assign a variable named `x` to a random integer between -1 and 1 to represent the case of negative numbers, positive numbers and zero
    - we assign a variable named `y` to a random integer between -1 and 1 just like above
    - we then test that when these two variables are given to the `add` function we get the sum of the 2 variables back

    the terminal updates to show passing tests
    ```python
    tests/test_calculator.py ..                             [100%]

    ================ 2 passed in 0.01s ===========================
    ```
    - we no longer need the previous tests because this new test covers the scenarios for zero, positive and negative numbers
    - we can remove `test addition` from our TODO list since it passed and the task is completed
    ```python
    # TODO
    # test subtraction
    # test multiplication
    # test division
    ```

That's the Test Driven Development pattern <span style="color:red">**RED**</span> <span style="color:green">**GREEN**</span> <span style="color:orange">**REFACTOR**</span>

---

## Test Subtraction

We will now add a failing test since addition works and our next action item from the TODO list is to test subtraction,

### <span style="color:red">**RED**</span> : make it fail

- update `test_calculator.py` with a method named `test_subtraction`
    ```python
    class TestCalculator(unittest.TestCase):

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
    ```

    the terminal responds with an [AttributeError](./ATTRIBUTE_ERROR.md)

    ```python
            self.assertEqual(
    >           calculator.subtract(x, y),
                x-y
            )
    E       AttributeError: module 'calculator' has no attribute 'subtract'
    ```

### <span style="color:green">**GREEN**</span> : make it pass
- add a variable assignment to `calculator.py`
    ```python
    def add(x, y):
        return x + y

    subtract = None
    ```
    and the terminal gives us a [TypeError](./TYPE_ERROR.md)

    ```python
    E       TypeError: 'NoneType' object is not callable
    ```
- change the definition of the `subtract` variable to make it callable
    ```python
    def add(x, y):
        return x + y

    def subtract():
        return None
    ```
    the terminal now shows a [TypeError](./TYPE_ERROR.md) with a different error message
    ```python
    E       TypeError: subtract() takes 0 positional arguments but 2 were given
    ```
- we change the definition of the `subtract` function to match our expectation
    ```python
    def add(x, y):
        return x + y

    def subtract(x, y):
        return None
    ```
    the terminal responds with an [AssertionError](./ASSERTION_ERROR.md)
    ```python
    >       self.assertEqual(
                calculator.subtract(x, y),
                x-y
            )
    E       AssertionError: None != 0
    ```
- we update the `subtract` function in `calculator.py` to perform an operation on its inputs
    ```python
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y
    ```
    the terminal shows passing tests - SUCCESS!
    ```python
    collected 3 items

    tests/test_calculator.py ...                          [100%]

    ======================= 3 passed in 0.01s ==================
    ```
- `test subtraction` can now be removed from our TODO list
    ```python
    # TODO
    # test multiplication
    # test division
    ```

### <span style="color:orange">**REFACTOR**</span>: make it better

- How can we make this better? Is there any duplication that could be removed?
    - `x = random.randint(-1, 1)` happens twice
    - `y = random.randint(-1, 1)` happens twice
- we could update `test_calculator.py` to create the random variables once

    ```python
    import calculator
    import random
    import unittest


    class TestCalculator(unittest.TestCase):

        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

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
    ```
    the x and y variables are now initialized once as class attributes that can be referenced later in every test using `self.x` and `self.y`, the terminal shows all tests are still passing

---

## Test Multiplication

We will now move on the next item on the TODO list which is to test multiplication

### <span style="color:red">**RED**</span> : make it fail

we add a failing test `test_calculator.py` named `test_multiplication`
```python
import unittest
import calculator
import random


class TestCalculator(unittest.TestCase):

    x = random.randint(-1, 1)
    y = random.randint(-1, 1)

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
```

the terminal responds with an [AttributeError](./ATTRIBUTE_ERROR.md)

### <span style="color:green">**GREEN**</span> : make it pass

using what we know so far we update `calculator.py` with a definition for multiplication

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
```

SUCCESS! The terminal shows passing tests and we remove `test_multiplication` from the TODO list

```python
# TODO
# test division
```

### <span style="color:orange">**REFACTOR**</span>: make it better

Can you think of a way to make the code we have better?

---

## Test Division

Let us now add the final test from our TODO list, the division test

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
    ```
    once again the terminal shows an [AttributeError](./ATTRIBUTE_ERROR.md)

### <span style="color:green">**GREEN**</span> : make it pass

- update `calculator.py` with a `divide` function
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
    here our terminal response varies, When `y` is 0 we get a [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ZeroDivisionError) like below
    ```python
    x = 1, y = 0

        def divide(x, y):
    >       return x / y
    E       ZeroDivisionError: division by zero
    ```
- we add `ZeroDivisionError` to the list of exceptions encountered
    ```python
    # Exceptions Encountered
    # AssertionError
    # NameError
    # TypeError
    # ZeroDivisionError
    ```

#### How to test for Errors
- <span style="color:red">**RED**</span> : make it fail

    we add a failing test to `test_calculator.py` to intentionally trigger a `ZeroDivisionError` and comment out our test previous test that sometimes fails, this helps us remove the variability from the test
    ```python
        def test_division(self):
            self.assertEqual(
                calculator.divide(self.x, 0),
                self.x/0
            )
            # self.assertEqual(
            #     calculator.divide(self.x, self.y),
            #     self.x/self.y
            # )
    ```
    the terminal confirms our expectations with a failure
    ```python
    x = 0, y = 0

        def divide(x, y):
    >       return x / y
    E       ZeroDivisionError: division by zero
    ```
- <span style="color:green">**GREEN**</span> : make it pass

    we update `test_calculator.py` to confirm that a `ZeroDivisionError` is raised when we try to divide a number by 0 by using `self.assertRaises`
    ```python
        def test_division(self):
            with self.assertRaises(ZeroDivisionError):
                calculator.divide(self.x, 0)
            # self.assertEqual(
            #     calculator.divide(self.x, self.y),
            #     self.x/self.y
            # )
    ```
    the terminal shows passing tests, and we now have a way to `catch` Exceptions when testing, which allows us to confirm that code raises an error and allow our other tests to continue when they encounter expected failures

- <span style="color:orange">**REFACTOR**</span>: make it better
    we can update `test_division` to test other division cases when the divisor is not 0 by adding a condition
    ```python
        def test_division(self):
            with self.assertRaises(ZeroDivisionError):
                calculator.divide(self.x, 0)
            while self.y == 0:
                self.y = random.randint(-1, 1)
            self.assertEqual(
                calculator.divide(self.x, self.y),
                self.x/self.y
            )
    ```
    - `while self.y == 0:` creates a loop that repeats whatever indented code follows as long as `self.y` is equal to `0`
    - `self.y = random.randint(-1, 1)` assigns a random variable to `self.y` that could be -1, 0 or 1
    - our loop tells python to assign a random variable to `self.y` as long as it is equal to 0
- remove `test_division` from our TODO list since the tests all pass

---

***CONGRATULATIONS*** You made it through writing a program that can perform the 4 basic arithmetic operations using Test Driven Development. What would you like to do next?