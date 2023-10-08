# Sleep Duration

Let us take a look at building a program which gives us the amount of time we have been asleep based on a given sleep and wake time which includes the dates to give an accurate result.

### Prerequisites

- [Setup a Test Driven Development Environment](./TDD_SETUP.md) with `sleep_duration` as the project name

---

## Duration when given hours only

### <span style="color:red">**RED**</span>: make it fail

write a failing test in `test_sleep_duration.py`
```python
    def test_duration_when_given_hours_only(self):
        self.assertEqual(
            sleep_duration.duration(
                wake_time='08:00',
                sleep_time='07:00'
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
    the [TypeError](./TYPE_ERROR.md) remains but with a different message about the first argument passed in from the test
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
- modify the return value for the duration function to our expectation
    ```python
    def duration(wake_time, sleep_time):
        return 1
    ```
    green! all tests are passing

### <span style="color:orange">**REFACTOR**</span>: make it better

The function currently returns `1` regardless of the inputs given but for it to be useful it has to calculate the difference between the wake time and the sleep time. It would be a large effort to write a test case for every permutation of sleep and wake times.

Let us try writing a test that uses a random variable for the sleep and wake times. If you have done the [TDD_CALCULATOR](./TDD_CALCULATOR.md) then you already know how to implement this solution

- add an import statement for the `random` library to `test_sleep_duration.py`
    ```python
    import random
    import sleep_duration
    import unittest
    ```
- add a new test with random values
    ```python
    class TestSleepDuration(unittest.TestCase):

        def test_duration_when_given_hours_only(self):
            wake_hour = random.randint(0, 24)
            sleep_hour = random.randint(0, 24)
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=f'{wake_hour}:00',
                    sleep_time=f'{sleep_hour}:00'
                ),
                1
            )
    ```
    here we use a random integer from 0 to 23 as the hours for sleep and wake time and interpolate them to the strings we use as inputs, this means our wake and sleep time will randomly vary from `00:00` to `23:00`
- the terminal still shows our test is passing because our expected value is 1, we need to change it to match the true expectation which is that it should be the duration between `wake_time` and `sleep_time`. Change the expected value in the test to be a calculation
    ```python
        def test_duration_when_given_hours_only(self):
            wake_hour = random.randint(0, 23)
            sleep_hour = random.randint(0, 23)
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=f'{wake_hour}:00',
                    sleep_time=f'{sleep_hour}:00'
                ),
                wake_hour-sleep_hour
            )
    ```
    now we have an [AssertionError](./ASSERTION_ERROR.md) because `sleep_duration.duration` still returns `1` but from our test we expect the difference between `wake_time` and `sleep_time`
- let us update the `duration` function in `sleep_duration.py` to return a difference between the `wake_time` and `sleep_time`
    ```python
    def duration(wake_time, sleep_time):
        return wake_time - sleep_time
    ```
    the terminal outputs a [TypeError](./TYPE_ERROR.md), we passed in two strings and python does not have an operation defined for subtracting one string from another. We need to find a way to convert the timestamp from a string to a number. We know that our two inputs are currently in the format `XX:00`, if we can parse the string to get the first two characters and convert that those digits to a number we should be able to get our calculation
- to find out what options are available to us, we look at the `methods` and `attributes` of strings by adding a failing test to `test_sleep_duration.py`, this time using the `dir` function
    ```python
        def test_string_methods_and_attributes(self):
            self.assertEqual(
                dir("00:00"),
                None
            )
    ```
    an [AssertionError](./ASSERTION_ERROR.md) is raised
    ```python
    E       AssertionError: ['__add__', '__class__', '__contains__', [918 chars]ill'] != None
    ```
- copy the value on the left side of the comparison and replace `None` as the expected value in the test
    ```python
        def test_string_methods_and_attributes(self):
            self.assertEqual(
                dir("00:00"),
                ['__add__', '__class__', '__contains__', [918 chars]ill']
            )
    ```
    the terminal shows a `SyntaxError`
    ```python
    E       ['__add__', '__class__', '__contains__', [918 chars]ill']
    E                                                     ^
    E   SyntaxError: invalid syntax
    ```
    ah, there is a closing quote, with no open quote, let us add an opening quote
    ```python
        def test_string_methods_and_attributes(self):
            self.assertEqual(
                dir("00:00"),
                ['__add__', '__class__', '__contains__', '[918 chars]ill']
            )
    ```
    we still have an [AssertionError](./ASSERTION_ERROR.md) but with a different message and a suggestion
    ```python
    E           Diff is 1265 characters long. Set self.maxDiff to None to see it.
    ```
- let us try the suggestion
    ```python
        def test_string_methods_and_attributes(self):
            self.maxDiff = None
            self.assertEqual(
                dir("00:00"),
                ['__add__', '__class__', '__contains__', '[918 chars]ill']
            )
    ```
    `maxDiff` sets a limit on the number of characters the terminal outputs for a difference between two objects, there is no limit when it is set to None. We now see a full list of all the attributes of a string `"00:00"`
    ```python
        def test_string_methods_and_attributes(self):
            self.maxDiff = None
            self.assertEqual(
                dir("00:00"),
                [
                    '__add__',
                    '__class__',
                    '__contains__',
                    '__delattr__',
                    '__dir__',
                    '__doc__',
                    '__eq__',
                    '__format__',
                    '__ge__',
                    '__getattribute__',
                    '__getitem__',
                    '__getnewargs__',
                    '__gt__',
                    '__hash__',
                    '__init__',
                    '__init_subclass__',
                    '__iter__',
                    '__le__',
                    '__len__',
                    '__lt__',
                    '__mod__',
                    '__mul__',
                    '__ne__',
                    '__new__',
                    '__reduce__',
                    '__reduce_ex__',
                    '__repr__',
                    '__rmod__',
                    '__rmul__',
                    '__setattr__',
                    '__sizeof__',
                    '__str__',
                    '__subclasshook__',
                    'capitalize',
                    'casefold',
                    'center',
                    'count',
                    'encode',
                    'endswith',
                    'expandtabs',
                    'find',
                    'format',
                    'format_map',
                    'index',
                    'isalnum',
                    'isalpha',
                    'isascii',
                    'isdecimal',
                    'isdigit',
                    'isidentifier',
                    'islower',
                    'isnumeric',
                    'isprintable',
                    'isspace',
                    'istitle',
                    'isupper',
                    'join',
                    'ljust',
                    'lower',
                    'lstrip',
                    'maketrans',
                    'partition',
                    'removeprefix',
                    'removesuffix',
                    'replace',
                    'rfind',
                    'rindex',
                    'rjust',
                    'rpartition',
                    'rsplit',
                    'rstrip',
                    'split',
                    'splitlines',
                    'startswith',
                    'strip',
                    'swapcase',
                    'title',
                    'translate',
                    'upper',
                    'zfill'
                ]
            )
    ```
- the terminal displays a [TypeError](./TYPE_ERROR.md) because python does not support subtracting one string from another
    ```python
    wake_time = '7:00', sleep_time = '21:00'

        def duration(wake_time, sleep_time):
    >       return wake_time - sleep_time
    E       TypeError: unsupported operand type(s) for -: 'str' and 'str'
    ```
    we are now at a point where we get the two random values we pass in and are trying to do a calculation, but because both values are strings, the calculation does not work. We need to find a way to convert the strings to numbers
- let us try one of the methods listed from `test_string_methods_and_attributes` to see if one of them might get us closer to a solution. Going with just the names of methods and attributes might not be enough since we do not know what they do, let us look at the documentation for extra details. Add a failing test the `help` keyword to see documentation about `strings`
    ```python
        self.assertEqual(
            help("00:00"),
        )
    ```
    the terminal outputs a long documentation, we scroll up reading through the descriptions for each method until we see one that looks like it can solve our problem
    ```python
    |  split(self, /, sep=None, maxsplit=-1)
    |      Return a list of the words in the string, using sep as the delimiter string.
    |
    |      sep
    |        The delimiter according which to split the string.
    |        None (the default value) means split according to any whitespace,
    |        and discard empty strings from the result.
    |      maxsplit
    |        Maximum number of splits to do.
    |        -1 (the default value) means no limit.
    ```
    we will give this method a try since it splits up a word when given a delimeter
- remove the failing test and replace it with one for the `split` method
    ```python
        def test_string_split_method(self):
            self.assertEqual(
                "00:00".split(),
                None
            )
    ```
    the terminal shows us that split creates a list of our string
    ```python
    E       AssertionError: ['00:00'] != None
    ```
    we change the expectation from `None` and the test passes with the terminal showing us the [TypeError](./TYPE_ERROR.md) that took us down this path
    ```python
    E       TypeError: unsupported operand type(s) for -: 'str' and 'str'
    ```
- but what we want is to split the string on a `delimiter` so we get the separate parts, something like `["00", "00"]`, using `:` as our delimeter let us update the test to reflect our desires
    ```python
        def test_string_split_method(self):
            self.assertEqual(
                "00:00".split(),
                ['00', '00']
            )
    ```
    the terminal shows an [AssertionError](./ASSERTION_ERROR.md), our use of the `split` method has not yet given us what we want. Looking back at the documentation, the definition for `split` takes in `self, /, sep=None, maxsplit=-1` and `sep` is the delimiter
- passing in `:` as the delimiter, we change the test
    ```python
        def test_string_split_method(self):
            self.assertEqual(
                "00:00".split(':'),
                ['00', '00']
            )
    ```
    the test passes and we now know how to get the first part of our wake and sleep times
- let us try using what we know so far to solve this problem, edit the definition of the `duration` function in `sleep_duration.py`
    ```python
    def duration(wake_time, sleep_time):
        return wake_time.split(':') - sleep_time.split(':')
    ```
    the terminal still shows a [TypeError](./TYPE_ERROR.md), this time for trying to subtract a list from a list
    ```python
    E       TypeError: unsupported operand type(s) for -: 'list' and 'list'
    ```
    Since we only need the first part of our list, we can get the specific item by using its index. Python uses zero-based indexing so our first item is at index 0 and the second item at 1, let us add a test to understand this
- add a failing test to `test_string_split_method`
    ```python
        def test_string_split_method(self):
            self.assertEqual(
                "00:00".split(':'),
                ['00', '00']
            )
            self.assertEqual(
                "12:34".split(':')[0],
                0
            )
            self.assertEqual(
                "12:34".split(':')[1],
                0
            )
    ```
    the terminal updates to show us an [AssertionError](./ASSERTION_ERROR.md) because the first item (item zero) from splitting `"12:34"` on the delimiter `:` is `"12"`, good, we are closer to what we want
- change the expected value in the test to match the value in the terminal
    ```python
    def test_string_split_method(self):
            self.assertEqual(
                "00:00".split(':'),
                ['00', '00']
            )
            self.assertEqual(
                "12:34".split(':')[0],
                "12"
            )
            self.assertEqual(
                "12:34".split(':')[1],
                0
            )
    ```
    the terminal shows another [AssertionError](./ASSERTION_ERROR.md), this time to confirm that the second item (item one) from splitting `"12:34"` on the delimiter `:` is `"34"`, we are not dealing with this part yet but we can assume we would use it soon, update the expected value in the same way and the test passes bringing us back to our unsolved [TypeError](./TYPE_ERROR.md)
- using what we know, how to `split` a string on a delimiter method and how to index a list, update the duration function to only return the subtraction of the first parts of `wake_time` and `sleep_time`
    ```python
    def duration(wake_time, sleep_time):
        return wake_time.split(':')[0] - sleep_time.split(':')[0]
    ```
    the terminal still outputs to show a [TypeError](./TYPE_ERROR.md) for an unsupported operation of trying to subtract a string from another, and though it is not obvious here, the strings being subtracted are the values to the left of the delimiter `:` not the entire string value of `wake_time` and `sleep_time` i.e. for a given wake_time of "02:00" and a given sleep_time of "01:00" our program is currently trying to subtract "01" from "02"
- we now have the task of converting our string to a number so we can do the subtraction, for this we use the `int` keyword which returns an integer for a given value. We should add a test to see how it works, update `test_sleep_duration.py` and comment out the current failing test
    ```python
        # def test_duration_when_given_hours_only(self):
        #     wake_hour = random.randint(0, 23)
        #     sleep_hour = random.randint(0, 23)
        #     self.assertEqual(
        #         sleep_duration.duration(
        #             wake_time=f'{wake_hour}:00',
        #             sleep_time=f'{sleep_hour}:00'
        #         ),
        #         wake_hour-sleep_hour
        #     )

        def test_converting_a_string_to_an_integer(self):
            self.assertEqual(int("12"), 0)
    ```
    the terminal shows an [AssertionError](./ASSERTION_ERROR.md) since `12 != 0`, we update the test and it shows passing tests
    ```python
        def test_converting_a_string_to_an_integer(self):
            self.assertEqual(int("12"), 12)
    ```
    we now have another tool to use to solve the problem
- after uncommenting the commented test, we are back to the [TypeError](./TYPE_ERROR.md) we have been trying to solve. We update the duration function with our knowledge to see if it makes the test pass
    ```python
    def duration(wake_time, sleep_time):
        return int(wake_time.split(':')[0]) - int(sleep_time.split(':')[0])
    ```
    EUREKA! We are green, with a way to randomly test if our duration function can calculate the sleep duration given any random `sleep` and `wake` time.
- You could also write the solution we have in a way that explains what is happening to someone who does not know how to index a list or use `int` or`split`. Let's try adding some variables
    ```python
    def duration(wake_time, sleep_time):
        wake_time_split = wake_time.split(':')
        wake_time_hour = wake_time_split[0]
        wake_time_hour_integer = int(wake_time_hour)
        return wake_time_hour_integer - int(sleep_time.split(':')[0])
    ```
    the terminal shows all tests are still passing. The refactor we wrote works. After doing the same thing for `sleep_time`, we still have passing tests
- there is a repetition in our function, for each string given
    - split the string on the delimiter `:`
    - get the first(0th) value from the split
    - convert first value from the split to an integer
    we could abstract that out to a function and call the function for each value
    ```python
    def function(value):
        value_split = value.split(':')
        value_hour = value_split[0]
        value_hour_integer = int(value_hour)
        return value_hour_integer

    def duration(wake_time, sleep_time):
        return function(wake_time) - function(sleep_time)
    ```
    since the tests are passing, we can rename the abstracted `function` to something more descriptive like `get_hour`
    ```python
    def get_hour(value):
        value_split = value.split(':')
        value_hour = value_split[0]
        value_hour_integer = int(value_hour)
        return value_hour_integer

    def duration(wake_time, sleep_time):
        return get_hour(wake_time) - get_hour(sleep_time)
    ```
- we could rewrite the `get_hour` function to use the same variable name in the operation e.g.
    ```python
    def get_hour(value):
        value = value.split(':')
        value = value[0]
        value = int(value)
        return value
    ```
    the terminal still shows passing tests
- we could also rewrite it to use one line
    ```python
    def get_hour(value):
        return int(value.split(':')[0])
    ```
    the terminal still shows passing tests. Since we are green you can try any ideas you have until you understand what we have written so far.

## Duration when given hours and minutes

We found a solution that provides the right duration when given sleep time and wake time in a given day. Our solution does not take into account minutes in the calculation

### <span style="color:red">**RED**</span>: make it fail

we are going to add a failing test for that scenario to `test_sleep_duration.py`

```python
    def test_duration_when_given_hours_and_minutes(self):
        wake_hour = random.randint(0, 24)
        sleep_hour = random.randint(0, 24)
        wake_minute = random.randint(0, 60)
        sleep_minute = random.randint(0, 60)
        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour}:{wake_minute}',
                sleep_time=f'{sleep_hour}:{sleep_minute}'
            ),
            f'{wake_hour-sleep_hour}:{wake_minute-sleep_minute}'
        )
```

the terminal shows an [AssertionError](./ASSERTION_ERROR.md) the expected value is now a string that contains the subtraction of the sleep hour from the wake hour, separated by a delimiter `:` and the subtraction of the sleep minute from the wake minute, so if we have a wake_time of `08:30` and a sleep_time of `07:11` we should have `1:19` as the output

### <span style="color:green">**GREEN**</span>: make it pass

- update the output of the `duration` function in `sleep_duration.py` to match the format of the expected value
    ```python
    def duration(wake_time, sleep_time):
        return f'{get_hour(wake_time)-get_hour(sleep_time)}:{wake_time-sleep_time}'
    ```
    we get a [TypeError](./ASSERTION_ERROR.md) because we just tried to subtract one string from another
- we modify the second part of our timestamp to use the `get_hour` function
    ```python
    def duration(wake_time, sleep_time):
        return f'{get_hour(wake_time)-get_hour(sleep_time)}:{get_hour(wake_time)-get_hour(sleep_time)}'
    ```
    the terminal now shows an [AssertionError](./ASSERTION_ERROR.md) because the difference in minutes is not yet calculated
- let us use the `get_hour` function to create a similar function which gets the minutes from a given timestamp
    ```python
    def get_hour(value):
        return int(value.split(':')[0])

    def get_minute(value):
        return int(value.split(':')[1])

    def duration(wake_time, sleep_time):
        return f'{get_hour(wake_time)-get_hour(sleep_time)}:{get_hour(wake_time)-get_hour(sleep_time)}'
    ```
    the terminal still shows an [AssertionError](./ASSERTION_ERROR.md)
- after updating the `duration` function with a call to the new `get_minute` function, the test passes
    ```python
    def get_hour(value):
        return int(value.split(':')[0])

    def get_minute(value):
        return int(value.split(':')[1])

    def duration(wake_time, sleep_time):
        return f'{get_hour(wake_time)-get_hour(sleep_time)}:{get_minute(wake_time)-get_minute(sleep_time)}'
    ```
    the terminal now reveals a failure for `test_duration_when_given_hours_only` which passed earlier, we introduced a regression when we changed the format the `duration` function outputs from a number to a string
- considering what we know so far, we can use a string to represent a duration as it allows us to express hours and minutes

### <span style="color:orange">**REFACTOR**</span>: make it better