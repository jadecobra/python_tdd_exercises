functions
====================

The focus of this chapter is on functions in python using Test Driven Development

A ``(function)`` is a callable unit/block of code. It is a way to encapsulate statements that can be used after they are written to accomplish a task. With functions we make code modular which makes it easier to test and reuse.

In programming we process input data of some form and output data in some form. We can think of it as

```python
    input_data -> program -> output_data
    program(input_data) -> output_data
```
We can think of the ``(program)`` in this illustration as the ``(function)`` that carries out the processing of ``(input_data)`` to return ``(output_data)``


### Prerequisites

- [How I setup a Test Driven Development Environment.md](./How I How I setup a Test Driven Development Environment.md.md)

---

## How to Define functions

``(functions)`` are defined using the ``(def)`` keyword, a name, parentheses and a colon at the end

### RED: make it fail

let us a create a file named `test_functions.py` in the ``(tests)`` folder and add the following failing test

```python
import unittest
import functions


class TestFunctions(unittest.TestCase):

    def test_functions_with_pass(self):
        self.assertIsNone(functions.function_with_pass())
```

the terminal displays a [ModuleNotFoundError](./MODULE_NOT_FOUND_ERROR.md), and we add it to our list of exceptions encountered
```python
# Exceptions Encountered
# AssertionError
# ModuleNotFoundError
```

### GREEN: make it pass

- create a file named `functions.py` in the project folder and the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md), which we add to our running list of exceptions encountered
    ```python
    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    ```
- update `functions.py` with a function definition
    ```python
    def function_with_pass():
        pass
    ```
    and the terminal displays a passing test
    - the test checks if the value of the call to `functions.function_with_pass` is ``(None)``
    - the function definition simply says ``(pass)`` yet the test passes
    - ``(pass)`` is a placeholder keyword which allows the function definition to follow python syntax rules
    - the test passes because in python all functions return ``(None)`` by default, we can imagine the function has an invisible line that says `return None`

### REFACTOR: make it better

let us test if functions really always return ``(None)`` by default

- #### RED: make it fail
    add a new failing test to ``(TestFunctions)`` in `test_functions.py`

    ```python
        def test_functions_with_return(self):
            self.assertIsNone(functions.function_with_return())
    ```
    the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)

- #### GREEN: make it pass

    add a new function to `functions.py` to make the test pass, this time with a ``(return)`` statement instead of ``(pass)``
    ```python
    def function_with_return(self):
        return
    ```
    the terminal shows this test is also passing. We have defined 2 functions with different statements in their body but they both return the same result, because "in python all functions return ``(None)`` by default, we can imagine the function has an invisible line that says `return None`"
- #### RED: make it fail
    we can add one more test to the ``(TestFunctions)`` class in `test_functions.py` to help drive home the point
    ```python
        def test_functions_with_return_none(self):
            self.assertIsNone(functions.function_with_return_none())
    ```
    the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)
- #### GREEN: make it pass

    from the [Zen of Python](https://peps.python.org/pep-0020/) - `Explicit is better than implicit.` Let us add a function definition to `functions.py` this time with an explicit ``(return)`` statement showing the value returned

    ```python
    def function_with_return_none():
        return None
    ```
    and the terminal updates to show passing tests.

The 3 ways we have defined functions so far have the exact same outcome, they all `return None`. If `Explicit is better than implicit.` I prefer to use `return None` telling anyone who reads the code exactly what the function returns.

Here is what we know so far about functions in python
- functions are defined using the ``(def)`` keyword
- functions return ``(None)`` by default

## Passthrough Functions

A function returns ``(output)``, and can take ``(input)```. As a simple test let us create a `passthrough function` which is a function that returns the input it receives as output

### RED: make it fail

add a failing test to the ``(TestFunctions)`` class in `test_functions.py`

```python
    def test_passthrough_function(self):
        self.assertEqual(functions.passthrough(False), False)
```
the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)

### GREEN: make it pass

- update `functions.py` with a function definition
    ```python
    def passthrough():
        return None
    ```
    the terminal updates to show a [TypeError](./TYPE_ERROR.md) because the definition for ``(passthrough)`` does not allow ``(inputs)`` but our test sends ``(False)`` as input
    ```python
    TypeError: passthrough() takes 0 positional arguments but 1 was given
    ```
- add the new exception to the list of exceptions encountered
    ```python
    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError
    ```
- update ``(passthrough)`` in `functions.py` to take 1 positional argument
    ```python
    def passthrough(input_data):
        return None
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)
    ```python
    AssertionError: None != False
    ```
    because the result of calling `functions.passthrough` with ``(False)`` as input is ``(None)`` which is not equal to ``(False)`` which is our expected result
- change the definition of ``(passthrough)`` to make the test pass
    ```python
    def passthrough(input_data):
        return False
    ```
    the terminal updates to show passing tests. We are geniuses!

### REFACTOR: make it better

Wait a minute! Something is not quite right here. The definition for a ``(passthrough)`` function was that it returned the same thing it was given, our test passes when ``(False)`` is given as input, will it still pass when another value is given or will it always return ``(False)``? There is a way to find out, let us test it

- #### RED: make it fail

    update ``(test_passthrough_function)`` in ``(TestFunctions)`` in `test_functions.py`  with a new test
    ```python
        def test_passthrough_function(self):
            self.assertEqual(functions.passthrough(False), False)
            self.assertEqual(functions.passthrough(True), True)
    ```
    the terminal shows an [AssertionError](./ASSERTION_ERROR.md)
    ```python
    AssertionError: False != True
    ```
    the function returns ``(False)`` instead of ``(True)`` in the second case, confirming our suspicions, we are not all the way geniuses, yet

- #### GREEN: make it pass

    change the definition of ``(passthrough)`` in `functions.py`
    ```python
    def passthrough(input_data):
        return input_data
    ```
    the terminal updates to show passing tests. We have more confidence that our passthrough function will likely return the input data it is given. Let us add more tests for good measure using the other python [Data Structures](./DATA_STRUCTURES.md)

- #### REFACTOR: make it better

    update ``(test_passthrough_function)``
    ```python
        def test_passthrough_function(self):
            self.assertEqual(functions.passthrough(False), False)
            self.assertEqual(functions.passthrough(True), True)
            self.assertEqual(functions.passthrough(None), False)
            self.assertEqual(functions.passthrough(int), False)
            self.assertEqual(functions.passthrough(str), False)
            self.assertEqual(functions.passthrough(tuple), False)
            self.assertEqual(functions.passthrough(list), False)
            self.assertEqual(functions.passthrough(set), False)
            self.assertEqual(functions.passthrough(dict), False)
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md) for each line until we make the input match the output, proving that the passthrough function we have defined returns the input it is given. Hooray! We are geniuses again

## Functions with positional arguments

We can define our function to take in more than one input, For instance if we are writing a function to perform operations on 2 numbers as we do in [TDD_CALCULATOR](./TDD_CALCULATOR.md), the function has to be able to accept the 2 numbers it performs operations on

### RED: make it fail

add a new test to `test_functions.py`, replacing ``(my_first_name)`` and ``(my_last_name)`` with your first and last names
```python
    def test_functions_with_positional_arguments(self):
        self.assertEqual(
            functions.passthrough_with_positional_arguments(
                'my_first_name', 'my_last_name'
            ),
            ('my_first_name', 'my_last_name')
        )
```
the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)

### GREEN: make it pass

- update `functions.py` with the solution we know works from ``(test_passthrough_function)``
    ```python
    def passthrough_with_positional_arguments(input_data):
        return input_data
    ```
    the terminal updates to show a [TypeError](./TYPE_ERROR.md)
- change the signature of ``(passthrough_with_positional_arguments)`` to take in more than one argument
    ```python
    def passthrough_with_positional_arguments(input_data, second_argument):
        return input_data
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)
- update ``(passthrough_with_positional_arguments)`` to return the two arguments it receives
    ```python
    def passthrough_with_positional_arguments(input_data, second_argument):
        return input_data, second_argument
    ```
    the terminal displays passing tests

### REFACTOR: make it better

How can we make this better?
- We named the first argument ``(input_data)`` and the second argument ``(second_argument)``. Technically, both arguments are input data, so we need a better name that is more descriptive, How can we make this better?
- modify the signature of ``(passthrough_with_positional_arguments)`` to use more descriptive names
    ```python
    def passthrough_with_positional_arguments(first_argument, second_argument):
        return first_argument, second_argument
    ```
    we still have passing tests
- let us add another test to ensure that ``(passthrough_with_positional_arguments)`` outputs data in the order given. update ``(test_functions_with_positional_arguments)``
    ```python
        def test_functions_with_positional_arguments(self):
            self.assertEqual(
                functions.passthrough_with_positional_arguments(
                    'my_first_name', 'my_last_name'
                ),
                ('my_first_name', 'my_last_name')
            )
            self.assertEqual(
                functions.passthrough_with_positional_arguments(
                    'my_last_name', 'my_first_name'
                ),
                ('my_first_name', 'my_last_name')
            )
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)
- update the test to the correct output
    ```python
        def test_functions_with_positional_arguments(self):
            self.assertEqual(
                functions.passthrough_with_positional_arguments(
                    'my_first_name', 'my_last_name'
                ),
                ('my_first_name', 'my_last_name')
            )
            self.assertEqual(
                functions.passthrough_with_positional_arguments(
                    'my_last_name', 'my_first_name'
                ),
                ('my_last_name', 'my_first_name')
            )
    ```
    the terminal updates to show passing tests
- our function only takes in 2 positional arguments, though there are scenarios where a function needs to take in more arguments. For instance, if we do not know the number of positional arguments that will be given before hand
- let us update ``(test_functions_with_positional_arguments)`` with tests for cases where the number of positional arguments received is not known
    ```python
        def test_functions_with_positional_arguments(self):
            self.assertEqual(
                functions.passthrough_with_positional_arguments(
                    'my_first_name', 'my_last_name'
                ),
                ('my_first_name', 'my_last_name')
            )
            self.assertEqual(
                functions.passthrough_with_positional_arguments(
                    'my_last_name', 'my_first_name'
                ),
                ('my_last_name', 'my_first_name')
            )
            self.assertEqual(
                functions.passthrough_with_positional_arguments(
                    0, 1, 2, 3
                ),
                (0, 1, 2, 3)
            )
            self.assertEqual(
                functions.passthrough_with_positional_arguments(
                    bool, int, float, str, tuple, list, set, dict
                ),
                (bool, int, float, str, tuple, list, set, dict)
            )
    ```
    the terminal updates to show a [TypeError](./TYPE_ERROR.md) because 2 positional arguments were expected by the function but 4 were given
- In python we can represent multiple arguments using a starred expression [see arbitrary argument lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists). Let us update the signature of ``(functions_with_positional_arguments)`` with a starred expression to take in any number of arguments
    ```python
    def passthrough_with_positional_arguments(*arguments):
        return arguments
    ```
    the terminal updates to show passing tests

## Functions with keyword arguments

There is an inherent problem with using positional arguments in functions. It requires the inputs to always be supplied in the correct sequence. If the program is dependent on that sequence, then it will behave in an unintended way when it receives input out of order. There is a way to ensure our function behaves correctly regardless of what order the user provides the input - Keyword Arguments

### RED: make it fail

add a new test to `test_functions.py`

```python
    def test_functions_with_keyword_arguments(self):
        self.assertEqual(
            functions.passthrough_with_keyword_arguments(
                first_name='my_first_name',
                last_name='my_last_name'
            ),
            ('my_first_name', 'my_last_name')
        )
```
the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)

### GREEN: make it pass

- add a function definition to `functions.py`
    ```python
    def passthrough_with_keyword_arguments():
        return None
    ```
    the terminal displays
    ```python
    TypeError: passthrough_with_keyword_arguments() got an unexpected keyword argument 'first_name'
    ```
-   alter the function signature to take in a positional argument
    ```python
    def passthrough_with_keyword_arguments(first_name):
        return None
    ```
    the terminal prints out
    ```python
    TypeError: passthrough_with_keyword_arguments() got an unexpected keyword argument 'last_name'
    ```
- update the function signature to take in another positional argument
    ```python
    def passthrough_with_keyword_arguments(first_name, last_name):
        return None
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)
- adjust the return statement to make the test pass
    ```python
    def passthrough_with_keyword_arguments(first_name, last_name):
        return first_name, last_name
    ```
    Eureka! the terminal updates to show passing tests

### REFACTOR: make it better

So far ``(passthrough_with_keyword_arguments)`` looks the same as ``(passthrough_with_positional_arguments)`` did when it took in 2 positional arguments, we have not yet seen a difference between a `positional argument` and a `keyword argument`

- add a test that puts the input data out of order to see if there is a difference
    ```python
        def test_functions_with_keyword_arguments(self):
            self.assertEqual(
                functions.passthrough_with_keyword_arguments(
                    first_name='my_first_name',
                    last_name='my_last_name'
                ),
                ('my_first_name', 'my_last_name')
            )
            self.assertEqual(
                functions.passthrough_with_keyword_arguments(
                    last_name='my_last_name',
                    first_name='my_first_name'
                ),
                ('my_first_name', 'my_last_name')
            )
    ```
    the terminal updates to show passing tests. Unlike in ``(test_functions_with_positional_arguments)`` using the name when passing inputs, ensures the function always displays output in the right order regardless of the order in which the input data is given

    Our function currently only takes in 2 keyword arguments. What if we wanted a function that can take in any number of keyword arguments? There is a starred expression for keyword arguments - `**`.

- #### RED: make it fail
    let us add a test to ``(test_functions_with_keyword_arguments)``
    ```python
        def test_functions_with_keyword_arguments(self):
            self.assertEqual(
                functions.passthrough_with_keyword_arguments(
                    first_name='my_first_name',
                    last_name='my_last_name'
                ),
                ('my_first_name', 'my_last_name')
            )
            self.assertEqual(
                functions.passthrough_with_keyword_arguments(
                    last_name='my_last_name',
                    first_name='my_first_name'
                ),
                ('my_first_name', 'my_last_name')
            )
            self.assertEqual(
                functions.passthrough_with_keyword_arguments(
                    a=1, b=2, c=3, d=4
                ),
                {}
            )
    ```
    the terminal updates to show a [TypeError](./TYPE_ERROR.md)

- #### GREEN: make it pass

    - change the signature of ``(passthrough_with_keyword_arguments)`` to accept any number of keyword arguments
        ```python
        def passthrough_with_keyword_arguments(**keyword_arguments):
            return keyword_arguments
        ```
        the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md) for our previous test that was passing. We have introduced a regression - our new code has caused an old passing test to fail.
    - update the expected result of ``(test_functions_with_keyword_arguments)`` from the terminal's output
        ```python
    def test_functions_with_keyword_arguments(self):
        self.assertEqual(
            functions.passthrough_with_keyword_arguments(
                first_name='my_first_name',
                last_name='my_last_name'
            ),
            {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
        )
        ```
        the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md) for the next test that was passing. We have another regression
    - change the next test to make the output match the expectation
        ```python
            def test_functions_with_keyword_arguments(self):
                self.assertEqual(
                    functions.passthrough_with_keyword_arguments(
                        first_name='my_first_name',
                        last_name='my_last_name'
                    ),
                    {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
                )
                self.assertEqual(
                    functions.passthrough_with_keyword_arguments(
                        last_name='my_last_name',
                        first_name='my_first_name'
                    ),
                    {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
                )
        ```
        the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md) for the last test we added
    - time to match the last test to the expected value in the comparison
        ```python
    def test_functions_with_keyword_arguments(self):
        self.assertEqual(
            functions.passthrough_with_keyword_arguments(
                first_name='my_first_name',
                last_name='my_last_name'
            ),
            {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
        )
        self.assertEqual(
            functions.passthrough_with_keyword_arguments(
                last_name='my_last_name',
                first_name='my_first_name'
            ),
            {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
        )
        self.assertEqual(
            functions.passthrough_with_keyword_arguments(
                a=1, b=2, c=3, d=4
            ),
            {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        )
        ```
        the terminal updates to show passing tests. We now know that keyword arguments are treated as [Dictionaries](./09_DICTIONARIES.md) in python

- #### REFACTOR: make it better

    let us add one more test to ``(test_functions_with_keyword_arguments)`` to drill the lesson
    ```python
        def test_functions_with_keyword_arguments(self):
            self.assertEqual(
                functions.passthrough_with_keyword_arguments(
                    first_name='my_first_name',
                    last_name='my_last_name'
                ),
                {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
            )
            self.assertEqual(
                functions.passthrough_with_keyword_arguments(
                    last_name='my_last_name',
                    first_name='my_first_name'
                ),
                {'first_name': 'my_first_name', 'last_name': 'my_last_name'}
            )
            self.assertEqual(
                functions.passthrough_with_keyword_arguments(
                    a=1, b=2, c=3, d=4
                ),
                {'a': 1, 'b': 2, 'c': 3, 'd': 4}
            )
            self.assertEqual(
                functions.passthrough_with_keyword_arguments(
                    a_boolean=bool,
                    an_integer=int,
                    a_float=float,
                    a_string=str,
                    a_tuple=tuple,
                    a_list=list,
                    a_set=set,
                    a_dictionary=dict
                ),
                {}
            )
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md) and we update the test with the right values to make the test pass
    ```python
        self.assertEqual(
            functions.passthrough_with_keyword_arguments(
                a_boolean=bool,
                an_integer=int,
                a_float=float,
                a_string=str,
                a_tuple=tuple,
                a_list=list,
                a_set=set,
                a_dictionary=dict
            ),
            {
                'a_boolean': bool,
                'an_integer': int,
                'a_float': float,
                'a_string': str,
                'a_tuple': tuple,
                'a_list': list,
                'a_set': set,
                'a_dictionary': dict
            }
        )
    ```

## Functions with positional and keyword arguments

We could also define functions to take in both positional arguments and keyword arguments

### RED: make it fail

add a new failing test to `test_functions.py`
```python
    def test_functions_with_positional_and_keyword_arguments(self):
        self.assertEqual(
            functions.accepts_positional_and_keyword_arguments(
                last_name='my_last_name', 'my_first_name'
            ),
            {}
        )
```

the terminal updates to show a ``(SyntaxError)`` because we put a positional argument after a keyword argument and we update our running list of exceptions encountered
```python
# Exceptions Encountered
# AssertionError
# ModuleNotFoundError
# AttributeError
# TypeError
# SyntaxError
```

### GREEN: make it pass

- fix the order of arguments in ``(test_functions_with_positional_and_keyword_arguments)``
    ```python
    def test_functions_with_positional_and_keyword_arguments(self):
        self.assertEqual(
            functions.accepts_positional_and_keyword_arguments('my_first_name', last_name='my_last_name'),
            {}
        )
    ```
    the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)
- add a definition for the function to `functions.py`
    ```python
    def accepts_positional_and_keyword_arguments():
        return None
    ```
    the terminal updates to show a [TypeError](./TYPE_ERROR.md)
    ```python
    TypeError: accepts_positional_and_keyword_arguments() got an unexpected keyword argument 'last_name'
    ```
- modify the function signature to take in an argument
    ```python
    def accepts_positional_and_keyword_arguments(last_name):
        return None
    ```
    the terminal updates to show another [TypeError](./TYPE_ERROR.md)
    ```python
    TypeError: accepts_positional_and_keyword_arguments() got multiple values for argument 'last_name'
    ```
- add another argument to the function signature
    ```python
    def accepts_positional_and_keyword_arguments(last_name, first_name):
        return None
    ```
    the terminal shows the same error even though we have 2 different arguments. We need a way to let the program know which argument is positional and which is a keyword argument
- reorder the arguments in the signature
    ```python
    def accepts_positional_and_keyword_arguments(first_name, last_name):
        return None
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)
- edit the return statement to make the test pass
    ```python
    def accepts_positional_and_keyword_arguments(first_name, last_name):
        return first_name, last_name
    ```
    the terminal updates the [AssertionError](./ASSERTION_ERROR.md) with the values we just added
- modify ``(test_functions_with_positional_and_keyword_arguments)`` to make our results match the expectation
    ```python
        def test_functions_with_positional_and_keyword_arguments(self):
            self.assertEqual(
                functions.accepts_positional_and_keyword_arguments(
                    'my_first_name', last_name='my_last_name'
                ),
                ('my_first_name', 'my_last_name')
            )
    ```
    the terminal reveals passing tests

### REFACTOR: make it better

Hold on a second. This looks exactly like what we did in ``(test_functions_with_positional_arguments)``. We cannot tell from the function signature which argument is positional and which is a keyword argument and do not want to wait for the function to fail when we send in values to figure it out
- change the function signature of ``(accepts_positional_and_keyword_arguments)`` to have a default value for the keyword argument
    ```python
    def accepts_positional_and_keyword_arguments(first_name, last_name=None):
        return first_name, last_name
    ```
    all tests are still passing
- we did not add a default argument for ``(first_name)``, let us test What would happen if we did
    ```python
    def accepts_positional_and_keyword_arguments(first_name=None, last_name=None):
        return first_name, last_name
    ```
    we still have passing tests. It looks like python lets us use default arguments with no issues, and we can provide keyword arguments positionally without using the name. let us add another test to prove this
- add a test to ``(test_functions_with_positional_and_keyword_arguments)``
    ```python
        def test_functions_with_positional_and_keyword_arguments(self):
            self.assertEqual(
                functions.accepts_positional_and_keyword_arguments(
                    'my_first_name', last_name='my_last_name'
                ),
                ('my_first_name', 'my_last_name')
            )
            self.assertEqual(
                functions.accepts_positional_and_keyword_arguments(
                    'my_first_name', 'my_last_name'
                ),
                ('my_first_name', 'my_last_name')
            )
    ```
    all the tests are still passing. The problem here is without the names the program is going to take the input data in the order we provide it so it is better to be explicit with the names because from the [Zen of Python](https://peps.python.org/pep-0020/) `Explicit is better than implicit.`
- let us add 2 tests, this time for an unknown number of positional and keyword arguments
    ```python
    def test_functions_with_positional_and_keyword_arguments(self):
        self.assertEqual(
            functions.accepts_positional_and_keyword_arguments(
                'my_first_name', last_name='my_last_name'
            ),
            ('my_first_name', 'my_last_name')
        )
        self.assertEqual(
            functions.accepts_positional_and_keyword_arguments(
                'my_first_name', 'my_last_name'
            ),
            ('my_first_name', 'my_last_name')
        )
        self.assertEqual(
            functions.accepts_positional_and_keyword_arguments(),
            (None, None)
        )
        self.assertEqual(
            functions.accepts_positional_and_keyword_arguments(
                bool, int, float, str, tuple, list, set, dict,
                a_boolean=bool, an_integer=int, a_float=float,
                a_string=str, a_tuple=tuple, a_list=list,
                a_set=set, a_dictionary=dict
            ),
            ()
        )
    ```
    the terminal updates to show a [TypeError](./TYPE_ERROR.md) because the function signature specifically only has two keyword arguments which are not provided in the call
- using what we know from previous tests we can alter the function to use starred expressions
    ```python
    def accepts_positional_and_keyword_arguments(*args, **kwargs):
        return args, kwargs
    ```
    the terminal updates to show a failure for a previous passing test
    ```python
        def test_functions_with_positional_and_keyword_arguments(self):
    >       self.assertEqual(
                functions.accepts_positional_and_keyword_arguments('my_first_name', last_name='my_last_name'),
                ('my_first_name', 'my_last_name')
            )
    E       AssertionError: Tuples differ: (('my_first_name',), {'last_name': 'my_last_name'}) != ('my_first_name', 'my_last_name')
    ```
- we will comment out the other tests for a bit, so we can focus on the failing test
    ```python
        def test_functions_with_positional_and_keyword_arguments(self):
            self.assertEqual(
                functions.accepts_positional_and_keyword_arguments(
                    'my_first_name', last_name='my_last_name'
                ),
                ('my_first_name', 'my_last_name')
            )
            # self.assertEqual(
            #    functions.accepts_positional_and_keyword_arguments(
            #        'my_first_name', 'my_last_name'
            #    ),
            #     (('my_first_name', 'last_name'), {})
            # )
            # self.assertEqual(
            #     functions.accepts_positional_and_keyword_arguments(),
            #     (None, None)
            # )
            # self.assertEqual(
            # functions.accepts_positional_and_keyword_arguments(
            #     bool, int, float, str, tuple, list, set, dict,a_boolean=bool, an_integer=int, a_float=float,a_string=str, a_tuple=tuple, a_list=list, a_set=set,
            #     a_dictionary=dict
            #     ),
            #     ()
            # )
    ```
- update the expected values in the test to make it pass
    ```python
            self.assertEqual(
                functions.accepts_positional_and_keyword_arguments(
                    'my_first_name', last_name='my_last_name'
                ),
                (('my_first_name',), {'last_name': 'my_last_name'})
            )
    ```
    the terminal updates to show tests passing, with the positional argument in parentheses and the keyword argument in curly braces
- uncomment the next test
    ```python
            self.assertEqual(
                functions.accepts_positional_and_keyword_arguments(
                    'my_first_name', 'my_last_name'
                ),
                (('my_first_name', 'last_name'), {})
            )
    ```
    the terminal updates to show
    ```python
    >       self.assertEqual(
                functions.accepts_positional_and_keyword_arguments('my_first_name', 'my_last_name'),
                (('my_first_name', 'last_name'), {})
            )
    E       AssertionError: Tuples differ: (('my_first_name', 'my_last_name'), {}) != (('my_first_name', 'last_name'), {})
    ```
- update the test to make it pass with both positional arguments in parentheses and empty curly braces since there are no keyword arguments
    ```python
            self.assertEqual(
                functions.accepts_positional_and_keyword_arguments(
                    'my_first_name', 'my_last_name'
                ),
                (('my_first_name', 'my_last_name'), {})
            )
    ```
    the terminal updates to show passing tests
- uncomment the next test to see it fail
    ```python
            self.assertEqual(
                functions.accepts_positional_and_keyword_arguments(),
                (None, None)
            )
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)
    ```python
    AssertionError: Tuples differ: ((), {}) != (None, None)
    ```
- update the test to make it pass with empty parentheses and curly braces as the expectation since no positional or keyword arguments were provided as inputs
    ```python
            self.assertEqual(
                functions.accepts_positional_and_keyword_arguments(),
                ((), {})
            )
    ```
- uncomment the last test to see it fail and the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)
    ```python
    AssertionError: Tuples differ: ((<class 'bool'>, <class 'int'>, <class 'f[307 chars]t'>}) != ()
    ```
- update the test to make it pass
    ```python
            self.assertEqual(
                functions.accepts_positional_and_keyword_arguments(
                    bool, int, float, str, tuple, list, set, dict,
                    a_boolean=bool, an_integer=int, a_float=float,
                    a_string=str, a_tuple=tuple, a_list=list,
                    a_set=set, a_dictionary=dict
                ),
                (
                    (bool, int, float, str, tuple, list, set, dict,),
                    {
                        'a_boolean': bool,
                        'an_integer': int,
                        'a_float': float,
                        'a_string': str,
                        'a_tuple': tuple,
                        'a_list': list,
                        'a_set': set,
                        'a_dictionary': dict
                    }
                )
            )
    ```
    the terminal updates to show passing tests
- From what we have seen so far, in python
    - positional arguments are represented as [tuples](./DATA_STRUCTURES.md) with parentheses - `()`
    - keyword arguments are represented as [dictionaries](./DICTIONARIES.md) with curly braces - `{}`
    - we can use `*name` to represent any number of positional arguments
    - we can use `**name` to represent any number of keyword arguments
    - we can define default values for arguments
    - positional arguments must come before keyword arguments

## Singleton Functions

A singleton function is a function that returns the same thing every time it is called.

### RED: make it fail

add a test to `test_functions.py`
```python
    def test_singleton_function(self):
        self.assertEqual(functions.singleton(), 'my_first_name')
```
the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)

### GREEN: make it pass

update `functions.py` to make it pass
```python
def singleton():
    return 'my_first_name'
```

### REFACTOR: make it better

add a new test that checks if a singleton that accepts inputs returns the same value when it is given inputs

- update `test_functions.py`
    ```python
        def test_singleton_function_with_input(self):
            self.assertEqual(functions.singleton_with_input('Bob', 'James', 'Frank'), 'joe')
            self.assertEqual(functions.singleton_with_input('a', 2, 'c', 3), 'joe')
    ```
    the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)
- add a function for ``(singleton_with_inputs)`` to `functions.py` to make the test pass
    ```python
    def singleton_with_inputs(*args):
        return 'joe'
    ```

*WELL DONE!*
You now know
- that singleton functions return the same thing every time they are called
- that positional arguments are represented as [tuples](./DATA_STRUCTURES.md) with parentheses - `()`
- that keyword arguments are represented as [dictionaries](./DICTIONARIES.md) with curly braces - `{}`
- how to write functions in python that can take in any number of positional or keyword arguments as inputs
- we can use `*name` to represent any number of positional arguments
- we can use `**name` to represent any number of keyword arguments
- we can define default values for arguments
- positional arguments must come before keyword arguments

Do you want to read more?
- [functions](https://docs.python.org/3/glossary.html#term-function)
- [methods](https://docs.python.org/3/glossary.html#term-method)
- [parameters](https://docs.python.org/3/glossary.html#term-parameter)
- [function definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
- [nested scope](https://docs.python.org/3/glossary.html#term-nested-scope)