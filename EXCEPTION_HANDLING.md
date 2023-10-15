# handle Exceptions in python

This chapter covers how to handle Exceptions in python using Test Driven Development

### Prerequisites

- [Setup a Test Driven Development Environment](./TDD_SETUP.md)

---

## Exceptions

Exceptions are raised in python when an error occurs and break execution of the program. When an exception is encountered no further instructions in the program will run.
This is useful because it means there is some violation that should be taken care of for the program to proceed as intended.

It also a pain when it causes the program to exit prematurely. What if we want our program to run regardless of errors? We might want it to give messages to the user who may not care or understand the details that come with Exceptions?

Enter Exception Handling. In python there is a mechanism for handling exceptions that allows a program to "make a decision" when it encounters an Exception. Enough words, let us write some code

## Test that an Exception is raised

### **RED**: make it fail

create a file named `test_exception_handling.py` in the `tests` folder and add the following

```python
import unittest
import module


class TestExceptionHandling(unittest.TestCase):

    def test_catching_module_not_found_error_in_tests(self):
        import non_existent_module
```

the terminal gives us a [ModuleNotFoundError](./MODULE_NOT_FOUND_ERROR.md) and we add it to our list of exceptions encountered

```python
# Exceptions Encountered
# AssertionError
# ModuleNotFoundError
```

### **GREEN**: make it pass

One way to take care of this error is to create the module, but in this case we want to catch/handle the exception in the test as a way to prove in the code that a `ModuleNotFoundError` will be raised for this module named `non_existent_module`. We add a `self.assertRaises` to `test_catching_module_not_found_error_in_tests`

```python
    def test_catching_module_not_found_error_in_tests(self):
        with self.assertRaises(ModuleNotFoundError):
            import non_existent_module
```

the terminal updates to show passing tests. How does all this work?
- we use the `self.assertRaises` method from the `unittest.TestCase` class which takes a given exception as its input, in this case `ModuleNotFoundError` and checks if that error is raised by the statements given in the context below(the indented block after the `with` statement)
- `with` - creates the context in which we are testing the exception is created.
    - Do you want to [read more about the with statement](https://docs.python.org/3/reference/compound_stmts.html?highlight=statement#the-with-statement)?
    - Do you want to [read more about with statement context managers](https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers)?
    - Do you want to [read PEP 343 - The "with" Statement](https://peps.python.org/pep-0343/)?

### **REFACTOR**: make it better

Since we know how to catch/handle an exception with `unittest`, there are a few things we can do with this information. We can test that a program fails in an expected way, deliberately cause failures and design for failure

- #### **RED**: make it fail

    add a new test to `TestExceptionHandling` in `test_exception_handling.py`

    ```python
        def test_catching_attribute_errors_in_tests(self):
            module.non_existent_attribute
    ```
    the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md) because the called attribute `non_existent_attribute` does not exist in `module.py`
    ```python
    E       AttributeError: module 'module' has no attribute 'non_existent_attribute'
    ```
    add the exception to our running list
    ```python
    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    ```

- #### **GREEN**: make it pass

    update `test_catching_attribute_errors_in_tests` with `self.assertRaises`

    ```python
        def test_catching_attribute_errors_in_tests(self):
            with self.assertRaises(AttributeError):
                module.non_existent_attribute
    ```

    the terminal updates to show passing tests. Let's do it again with `methods` for good measure

- #### **RED**: make it fail

    add a failing line to `test_catching_attribute_errors_in_tests`

    ```python
        def test_catching_attribute_errors_in_tests(self):
            with self.assertRaises(AttributeError):
                module.non_existent_attribute
            module.non_existent_function()
    ```
    the terminal updates to show [AttributeError](./ATTRIBUTE_ERROR.md) because the called method `non_existent_function` does not exist in `module.py`
    ```python
    E       AttributeError: module 'module' has no attribute 'non_existent_function'
    ```

- #### **GREEN**: make it pass

    add `self.assertRaises` and indent the failing line to place it within the context
    ```python
        def test_catching_attribute_errors_in_tests(self):
            with self.assertRaises(AttributeError):
                module.non_existent_attribute
            with self.assertRaises(AttributeError):
                module.non_existent_function()
    ```
    the terminal updates to show passing tests

- #### **RED**: make it fail

    let us add another failing line to `test_catching_attribute_errors_in_tests`

    ```python
        def test_catching_attribute_errors_in_tests(self):
            with self.assertRaises(AttributeError):
                module.non_existent_attribute
            with self.assertRaises(AttributeError):
                module.non_existent_function()
            module.NonExistentClass()
    ```
    the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)
    ```python
    E       AttributeError: module 'module' has no attribute 'NonExistentClass'
    ```

- #### **GREEN**: make it pass

    add `self.assertRaises` to make it pass
    ```python
        def test_catching_attribute_errors_in_tests(self):
            with self.assertRaises(AttributeError):
                module.non_existent_attribute
            with self.assertRaises(AttributeError):
                module.non_existent_function()
            with self.assertRaises(AttributeError):
                module.NonExistentClass()
    ```
    the terminal displays passing tests

- #### **RED**: make it fail

    update `test_catching_attribute_errors_in_tests` with a new failing line
    ```python
        def test_catching_attribute_errors_in_tests(self):
            with self.assertRaises(AttributeError):
                module.non_existent_attribute
            with self.assertRaises(AttributeError):
                module.non_existent_function()
            with self.assertRaises(AttributeError):
                module.NonExistentClass()
            module.Class.non_existent_attribute
    ```
    the terminal shows an [AttributeError](./ATTRIBUTE_ERROR.md)
    ```python
    E       AttributeError: type object 'Class' has no attribute 'non_existent_attribute'
    ```

- #### **GREEN**: make it pass

    add `self.assertRaises` to catch the error
    ```python
        def test_catching_attribute_errors_in_tests(self):
            with self.assertRaises(AttributeError):
                module.non_existent_attribute
            with self.assertRaises(AttributeError):
                module.non_existent_function()
            with self.assertRaises(AttributeError):
                module.NonExistentClass()
            with self.assertRaises(AttributeError):
                module.Class.non_existent_attribute
    ```
    the terminal updates to show passing tests

- #### **RED**: make it fail

    we trigger another attribute error, by adding a line to `test_catching_attribute_errors_in_tests`
    ```python
        def test_catching_attribute_errors_in_tests(self):
            with self.assertRaises(AttributeError):
                module.non_existent_attribute
            with self.assertRaises(AttributeError):
                module.non_existent_function()
            with self.assertRaises(AttributeError):
                module.NonExistentClass()
            with self.assertRaises(AttributeError):
                module.Class.non_existent_attribute
            module.Class.non_existent_method()
    ```
    the terminal updates to show another [AttributeError](./ATTRIBUTE_ERROR.md)
    ```python
        E       AttributeError: type object 'Class' has no attribute 'non_existent_method'
    ```
- #### **GREEN**: make it pass

    add `self.assertRaises` to make it pass
    ```python
        def test_catching_attribute_errors_in_tests(self):
            with self.assertRaises(AttributeError):
                module.non_existent_attribute
            with self.assertRaises(AttributeError):
                module.non_existent_function()
            with self.assertRaises(AttributeError):
                module.NonExistentClass()
            with self.assertRaises(AttributeError):
                module.Class.non_existent_attribute
            with self.assertRaises(AttributeError):
                module.Class.non_existent_method()
    ```
    the terminal updates to show passing tests

- #### **REFACTOR**: make it better

    We just created the same context 5 times, this is a good candidate for a rewrite. let us remove the duplication. since our `self.assertRaises` catches an [AttributeError](./ATTRIBUTE_ERROR.md) in each case, we only need to state it once and place all the lines that raise the error underneath it.
    ```python
        def test_catching_attribute_errors_in_tests(self):
            with self.assertRaises(AttributeError):
                module.non_existent_attribute
                module.non_existent_function()
                module.NonExistentClass()
                module.Class.non_existent_attribute
                module.Class.non_existent_method()
    ```
    all our tests are still passing

---

## handle Exceptions in programs

Earlier on we learned how to verify that an exception gets raised, we will now look at how to handle exceptions in programs

### **RED**: make it fail

Let us deliberately trigger an exception in our code and then handle it, add a failing test to `test_exception_handling.py` with a new test
```python
    def test_catching_exceptions(self):
        exceptions.raise_exception_error()
```

the terminal updates to show a `NameError` and we update our running list of exceptions encountered
```python
# Exceptions Encountered
# AssertionError
# ModuleNotFoundError
# AttributeError
# NameError
```

### **GREEN**: make it pass
- A `NameError` is raised when a name is used within a module and there is no definition for it. In our code above we call `exceptions.raise_exception_error` but there is no definition for `exceptions`. update the `import` section with a new line
    ```python
    import unittest
    import module
    import exceptions
    ```
    the terminal now gives us a [ModuleNotFoundError](./MODULE_NOT_FOUND_ERROR.md)
- create a file named `exceptions.py` in the `<PROJECT_NAME>` folder, and the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)
- update `exceptions.py` with the name of the attribute called in the test, and the terminal updates to show a `NameError` since we have not defined `raises_exception_error`
    ```python
    raises_exception_error
    ```
- define `raises_exception_error` and the terminal updates to show a [TypeError](./TYPE_ERROR.md)
    ```python
    raises_exception_error = None
    ```
    which we add to our running list of exceptions encountered
    ```python
    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError
    ```
- redefine `raises_exception_error` as a function and the terminal updates to show passing tests
    ```python
    def raises_exception_error():
        return None
    ```
- let us update the function to trigger an `Exception` by using the `raise` keyword
    ```python
    def raises_exception_error():
        raise Exception
    ```
    the terminal updates to show
    ```python
    E       Exception
    ```
- we add a `self.assertRaises` to `test_catching_exceptions` in `test_exception_handling.py` to confirm that this error happens and allow our tests to continue
    ```python
    def test_catching_exceptions(self):
        with self.assertRaises(Exception):
            exceptions.raises_exception_error()
    ```
    the terminal shows passing tests

*CONGRATULATIONS!*
You now know how to deliberately create an exception, you now have absolute power to reshape the universe to your will

### **REFACTOR**: make it better

let us add exception handling to our program so it does not end when it encounters an exception but instead gives a message

- #### **RED**: make it fail

    add a new test to `test_exception_handling`
    ```python
        def test_catching_things_that_fail(self):
            self.assertEqual(
                exceptions.exception_handler(exceptions.raises_exception_error),
                'failed'
            )
    ```

    the terminal updates to show an [AttributeError](./AttributeError)

- ### **GREEN**: make it pass
    add a name to `exceptions.py` and the terminal updates to show `NameError`
        ```python
        exception_handler
        ```
    define `exception_handler` and the terminal displays a [TypeError](./TYPE_ERROR.md)
        ```python
        exception_handler = None
        ```
    redefine `exception_handler` as a function updates the [TypeError](./TYPE_ERROR.md) with a new message
        ```python
        def exception_handler():
            return None
        ```
    update the signature for `exception_handler` to accept a positional argument
        ```python
        def exception_handler(argument):
            return None
        ```
        the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)
        ```python
        E       AssertionError: None != 'failed'
        ```
        because the result of calling `exceptions.exception_handler` with `exceptions.raises_exception_error`  as the input is currently `None` which is not equal to `failed`
    change `exception_handler` to return `failed` and the terminal updates to show passing tests
        ```python
        def exception_handler(argument):
            return 'failed'
        ```

- #### **RED**: make it fail

    our solution is faulty, the `exception_handler` always returns `failed` regardless of what we provide as an argument, we should add a new test to `test_exception_handling` that provides a different input with an expectation of a different result
    ```python
        def test_catching_things_that_succeed(self):
            self.assertEqual(
                exceptions.exception_handler(exceptions.does_not_raise_exception_error),
                'succeeded'
            )
    ```
    the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)

- #### **GREEN**: make it pass

    add `does_not_raise_exception_error` to `exceptions.py` and the terminal updates to show a `NameError`
    ```python
    does_not_raise_exception_error
    ```
    define `does_not_raise_exception_error` as a variable
    ```python
    does_not_raise_exception_error = None
    ```
    and the terminal updates to show [AssertionError](./ASSERTION_ERROR.md)
    ```
    E       AssertionError: 'failed' != 'succeeded'
    ```
    because the value returned by `exceptions.exception_handler` when given `exceptions.does_not_raise_exception_error` as an input is `failed` which is not equal to `succeeded`

    For our purpose of learning to handle exceptions we want the `exception_handler` function to return a different input based on the exceptions that occur within the function. Let us update `exception_handler` in `exceptions.py` to call a function it receives as input
    ```python
    def exception_handler(function):
        return function()
    ```
    the terminal updates to show a [TypeError](./TYPE_ERROR.md) because `does_not_raise_exception_error` is not a function, we will redefine `does_not_raise_exception_error` to make it callable
    ```python
    def does_not_raise_exception_error():
        return None
    ```
    the terminal updates to show
    ```python
    AssertionError: None != 'succeeded'
    ```
    because the `exception_handler` function returns the result of calling the function it receives as input, when we call `exceptions.exception_handler(exceptions.does_not_raise_exception_error)` it in turn calls `does_not_raise_exception_error` and returns the result of the call which we defined as `None`. Since the result is not equal to `succeeded`, our expectation is not met.

    To catch/handle exceptions in python we use a `try...except...else` statement. This allows the program to make a decision when it encounters an Exception. Update `exception_handler` in `exceptions.py` to handle exceptions
    ```python
    def exception_handler(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'
    ```
    the terminal updates to show passing tests

    We can think of the  `try...except...else` statement as `try` something, if it raises an `Exception` do this, if it does not raise an exception do do something else. In this case
    - `try` calling `function()`
    - `except Exception` - if `function()` raises an Exception return `failed`
    - `else` - if `function()` does not raise an Exception return `succeeded`
    - do you want to
        - [read more about the try statement?](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)
        - [read more about exception handling?](https://docs.python.org/3/tutorial/errors.html?highlight=try%20except#handling-exceptions)


## How to use try...except...else...finally

### **RED**: make it fail

add a new failing test to `test_exception_handling.py`
```python
    def test_finally_always_returns(self):
        self.assertEqual(
            exceptions.always_returns(exceptions.does_not_raise_exception_error),
            "always_returns_this"
        )
```

this will cause an [AttributeError](./ATTRIBUTE_ERROR.md)

### **GREEN**: make it pass

- add a name to `exceptions.py` and the terminal updates to show a `NameError`
    ```python
    always_returns
    ```
- define `always_returns` as a variable and we get an [AttributeError](./ATTRIBUTE_ERROR.md)
    ```python
    always_returns = None
    ```
- redefine `always_returns` as a function and the terminal displays a [TypeError](./TYPE_ERROR.md)
    ```python
    def always_returns():
        return None
    ```
- update the signature of `always_returns` to accept a function that we call and return its value
    ```python
    def always_returns(function):
        return function()
    ```
    the terminal updates to show
    ```python
    AssertionError: None != 'always_returns_this'
    ```
    because `exceptions.always_returns` returns the value of `does_not_raise_exception_error` which is `None` and is not equal to our expectation in the test which is `always_returns_this`
- add exception handling with using `try...except...else`
    ```python
    def always_returns(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'
    ```
    the terminal displays an [AssertionError](./ASSERTION_ERROR.md) and since no exception is raised when `does_not_raise_exception_error` is called by `always_returns_this`, it returns `succeeded` which is not equal to `always_returns_this`
- we can try adding another return statement to the function to see if that would work
    ```python
    def always_returns(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'
        return 'always_returns_this'
    ```
    no change, the terminal still has the same error. In python the `return` statement is the last thing executed in the function, nothing else after that statement. Since the function returns `suceeded` it ignores the return statement below it. We can add a clause to force it to ignore the other return statements and only return what we want
- add a `finally` clause to the `try...except...else` block
    ```python
    def always_returns(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'
        finally:
            return 'always_returns_this'
    ```
    the terminal updates to show passing tests. the `finally` clause is always executed regardless of what happens in the `try` block
- let us add one more test to verify that the code in the `finally` block will always execute, update `test_finally_always_returns`
    ```python
    def test_finally_always_returns(self):
        self.assertEqual(
            exceptions.always_returns(exceptions.does_not_raise_exception_error),
            "always_returns_this"
        )
        self.assertEqual(
            exceptions.always_returns(exceptions.raises_exception_error),
            'always_returns_this'
        )
    ```
    It is important to note that `always_returns` could have been defined as a `singleton` [function](./FUNCTIONS.md) and the tests would still pass, but that would not illustrate how to use `try...except...else...finally`
    ```python
    def always_returns(function):
        return 'always_returns_this`
    ```

*CONGRATULATIONS*
Your python powers are growing, you now know
- how to deliberately raise exceptions
- how to verify that exceptions are raised
- how to handle exceptions when they occur