# Sleep Duration

Let us take a look at building a program which gives us the amount of time we have been asleep based on a given sleep and wake time which includes the dates to give an accurate result.

### Prerequisites

- [How I setup a Test Driven Development Environment.md](./How I How I setup a Test Driven Development Environment.md.md) with ``(sleep_duration)`` as the project name

---

## Duration when given hours only

### RED: make it fail

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

the terminal shows a ``(NameError)`` which we add to our list of exceptions encountered

```python
# Exceptions Encountered
# AssertionError
# NameError
```

### GREEN: make it pass

- add an import statement for the missing name
    ```python
    import sleep_duration
    import unittest


    class TestSleepDuration(unittest.TestCase):
    ```
    the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md) since we do not have a definition for ``(duration)`` in `sleep_duration.py`
- we update our list of exceptions encountered
    ```python
    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    ```
- add a name to `sleep_duration.py` and the terminal displays a ``(NameError)``
    ```python
    duration
    ```
- make ``(duration)`` a variable by assigning it to the null value ``(None)``
    ```python
    duration = None
    ```
    the terminal outputs a [TypeError](./TYPE_ERROR.md) because ``(None)`` is not callable
- we add the exception to our running list
    ```python
    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    ```
- define ``(duration)`` as a function
    ```python
    def duration():
        return None
    ```
    the [TypeError](./TYPE_ERROR.md) remains but with a different message about the first argument passed in from the test
- change the definition of ``(duration)`` to accept the required keyword argument
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
    the terminal now shows an [AssertionError](./ASSERTION_ERROR.md) since our duration function returns ``(None)`` and the test expects ``(1)`` as the duration when a sleep time of `07:00` and a wake time of `08:00` is given
- modify the return value for the duration function to our expectation
    ```python
    def duration(wake_time, sleep_time):
        return 1
    ```
    green! all tests are passing

### REFACTOR: make it better

The function currently returns ``(1)`` regardless of the inputs given but for it to be useful it has to calculate the difference between the wake time and the sleep time. It would be a large effort to write a test case for every permutation of sleep and wake times.

Let us try writing a test that uses a random variable for the sleep and wake times. If you have done the [TDD_CALCULATOR](./TDD_CALCULATOR.md) then you already know how to implement this solution

- add an import statement for the ``(random)`` library to `test_sleep_duration.py`
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
- the terminal still shows our test is passing because our expected value is 1, we need to change it to match the true expectation which is that it should be the duration between ``(wake_time)`` and ``(sleep_time)``. Change the expected value in the test to be a calculation
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
    now we have an [AssertionError](./ASSERTION_ERROR.md) because `sleep_duration.duration` still returns ``(1)`` but from our test we expect the difference between ``(wake_time)`` and ``(sleep_time)``
- let us update the ``(duration)`` function in `sleep_duration.py` to return a difference between the ``(wake_time)`` and ``(sleep_time)``
    ```python
    def duration(wake_time, sleep_time):
        return wake_time - sleep_time
    ```
    the terminal outputs a [TypeError](./TYPE_ERROR.md), we passed in two strings and python does not have an operation defined for subtracting one string from another. We need to find a way to convert the timestamp from a string to a number. We know that our two inputs are currently in the format `XX:00`, if we can parse the string to get the first two characters and convert that those digits to a number we should be able to get our calculation
- to find out what options are available to us, we look at the ``(methods)`` and ``(attributes)`` of strings by adding a failing test to `test_sleep_duration.py`, this time using the ``(dir)`` function
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
- copy the value on the left side of the comparison and replace ``(None)`` as the expected value in the test
    ```python
        def test_string_methods_and_attributes(self):
            self.assertEqual(
                dir("00:00"),
                ['__add__', '__class__', '__contains__', [918 chars]ill']
            )
    ```
    the terminal shows a ``(SyntaxError)``
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
    ``(maxDiff)`` sets a limit on the number of characters the terminal outputs for a difference between two objects, there is no limit when it is set to None. We now see a full list of all the attributes of a string `"00:00"`
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
- let us try one of the methods listed from ``(test_string_methods_and_attributes)`` to see if one of them might get us closer to a solution. Going with just the names of methods and attributes might not be enough since we do not know what they do, let us look at the documentation for extra details. Add a failing test the ``(help)`` keyword to see documentation about ``(strings)``
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
- remove the failing test and replace it with one for the ``(split)`` method
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
    we change the expectation from ``(None)`` and the test passes with the terminal showing us the [TypeError](./TYPE_ERROR.md) that took us down this path
    ```python
    E       TypeError: unsupported operand type(s) for -: 'str' and 'str'
    ```
- but what we want is to split the string on a ``(delimiter)`` so we get the separate parts, something like `["00", "00"]`, using `:` as our delimeter let us update the test to reflect our desires
    ```python
        def test_string_split_method(self):
            self.assertEqual(
                "00:00".split(),
                ['00', '00']
            )
    ```
    the terminal shows an [AssertionError](./ASSERTION_ERROR.md), our use of the ``(split)`` method has not yet given us what we want. Looking back at the documentation, the definition for ``(split)`` takes in `self, /, sep=None, maxsplit=-1` and ``(sep)`` is the delimiter
- passing in `:` as the delimiter, we change the test
    ```python
        def test_string_split_method(self):
            self.assertEqual(
                "00:00".split(':'),
                ['00', '00']
            )
    ```
    the test passes and we now know how to get the first part of our wake and sleep times
- let us try using what we know so far to solve this problem, edit the definition of the ``(duration)`` function in `sleep_duration.py`
    ```python
    def duration(wake_time, sleep_time):
        return wake_time.split(':') - sleep_time.split(':')
    ```
    the terminal still shows a [TypeError](./TYPE_ERROR.md), this time for trying to subtract a list from a list
    ```python
    E       TypeError: unsupported operand type(s) for -: 'list' and 'list'
    ```
    Since we only need the first part of our list, we can get the specific item by using its index. Python uses zero-based indexing so our first item is at index 0 and the second item at 1, let us add a test to understand this
- add a failing test to ``(test_string_split_method)``
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
- using what we know, how to ``(split)`` a string on a delimiter method and how to index a list, update the duration function to only return the subtraction of the first parts of ``(wake_time)`` and ``(sleep_time)``
    ```python
    def duration(wake_time, sleep_time):
        return wake_time.split(':')[0] - sleep_time.split(':')[0]
    ```
    the terminal still outputs to show a [TypeError](./TYPE_ERROR.md) for an unsupported operation of trying to subtract a string from another, and though it is not obvious here, the strings being subtracted are the values to the left of the delimiter `:` not the entire string value of ``(wake_time)`` and ``(sleep_time)`` i.e. for a given wake_time of "02:00" and a given sleep_time of "01:00" our program is currently trying to subtract "01" from "02"
- we now have the task of converting our string to a number so we can do the subtraction, for this we use the ``(int)`` keyword which returns an integer for a given value. We should add a test to see how it works, update `test_sleep_duration.py` and comment out the current failing test
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
    EUREKA! We are green, with a way to randomly test if our duration function can calculate the sleep duration given any random ``(sleep)`` and ``(wake)`` time.
- You could also write the solution we have in a way that explains what is happening to someone who does not know how to index a list or use ``(int)`` or``(split)``. Let's try adding some variables
    ```python
    def duration(wake_time, sleep_time):
        wake_time_split = wake_time.split(':')
        wake_time_hour = wake_time_split[0]
        wake_time_hour_integer = int(wake_time_hour)
        return wake_time_hour_integer - int(sleep_time.split(':')[0])
    ```
    the terminal shows all tests are still passing. The refactor we wrote works. After doing the same thing for ``(sleep_time)``, we still have passing tests
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
    since the tests are passing, we can rename the abstracted ``(function)`` to something more descriptive like ``(get_hour)``
    ```python
    def get_hour(value):
        value_split = value.split(':')
        value_hour = value_split[0]
        value_hour_integer = int(value_hour)
        return value_hour_integer

    def duration(wake_time, sleep_time):
        return get_hour(wake_time) - get_hour(sleep_time)
    ```
- we could rewrite the ``(get_hour)`` function to use the same variable name in the operation e.g.
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

### RED: make it fail

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

### GREEN: make it pass

- update the output of the ``(duration)`` function in `sleep_duration.py` to match the format of the expected value
    ```python
    def duration(wake_time, sleep_time):
        return f'{get_hour(wake_time)-get_hour(sleep_time)}:{wake_time-sleep_time}'
    ```
    we get a [TypeError](./ASSERTION_ERROR.md) because we just tried to subtract one string from another
- we modify the second part of our timestamp to use the ``(get_hour)`` function
    ```python
    def duration(wake_time, sleep_time):
        return f'{get_hour(wake_time)-get_hour(sleep_time)}:{get_hour(wake_time)-get_hour(sleep_time)}'
    ```
    the terminal now shows an [AssertionError](./ASSERTION_ERROR.md) because the difference in minutes is not yet calculated
- let us use the ``(get_hour)`` function to create a similar function which gets the minutes from a given timestamp
    ```python
    def get_hour(value):
        return int(value.split(':')[0])

    def get_minute(value):
        return int(value.split(':')[1])

    def duration(wake_time, sleep_time):
        return f'{get_hour(wake_time)-get_hour(sleep_time)}:{get_hour(wake_time)-get_hour(sleep_time)}'
    ```
    the terminal still shows an [AssertionError](./ASSERTION_ERROR.md)
- after updating the ``(duration)`` function with a call to the new ``(get_minute)`` function, the test passes
    ```python
    def get_hour(value):
        return int(value.split(':')[0])

    def get_minute(value):
        return int(value.split(':')[1])

    def duration(wake_time, sleep_time):
        return f'{get_hour(wake_time)-get_hour(sleep_time)}:{get_minute(wake_time)-get_minute(sleep_time)}'
    ```
    the terminal now reveals a failure for ``(test_duration_when_given_hours_only)`` which passed earlier, we introduced a regression when we changed the format the ``(duration)`` function outputs from a number to a string
- considering what we know so far, we can use a string to represent a duration as it allows us to express hours and minutes. Let us change ``(test_duration_when_given_hours_only)``  where we supplied only hours expect a string instead of a number
    ```python
        def test_duration_when_given_hours_only(self):
            wake_hour = random.randint(0, 23)
            sleep_hour = random.randint(0, 23)
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=f'{wake_hour}:00',
                    sleep_time=f'{sleep_hour}:00'
                ),
                f'{wake_hour-sleep_hour}:00'
            )
    ```
    we get an [AssertionError](./ASSERTION_ERROR.md) in the terminal because we have two zeros `:00` in the expected return value but the duration function returns ``(0)`` for the minute side of our timestamp after doing a subtraction, i.e. ``(00)`` minus ``(00)`` is ``(0)`` not ``(00)``. We could update the right side of the expected value to ``(0)`` to make it pass, but that would not be necessary because ``(test_duration_when_given_hours_and_minutes)`` already covers the cases where the minutes are zero since we are doing a random number from ``(0)`` to ``(23)`` for hours and a random number from ``(0)`` to ``(59)`` for minutes.
- delete ``(test_duration_when_given_hours_only)`` since we no longer need it and the terminal shows passing tests

### REFACTOR: make it better

The ``(duration)`` function currently returns a subtraction of hours and a subtraction of minutes but is not accurate for calculating real differences in time. For instance if you give a wake time of `3:30` and a sleep time of `2:59` it will give us `1:-29` which is not a real duration instead of `0:31` which is the actual duration, this means that even though our tests are passing, once again the ``(duration)`` function does not meet the requirement of calculating the duration between two timestamps. We need a better way.

- add a new test to `test_sleep_duration.py`
    ```python
        def test_duration_calculation(self):
            wake_hour = 3
            sleep_hour = 2
            wake_minute = 30
            sleep_minute = 59
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=f'{wake_hour}:{wake_minute}',
                    sleep_time=f'{sleep_hour}:{sleep_minute}'
                ),
                '0:31'
            )
    ```
    the terminal shows an [AssertionError](./ASSERTION_ERROR.md) since `1:-29` is not equal to `0:31`
- we do a quick search in the python documentation for [time difference](https://docs.python.org/3/search.html?q=time+difference) on https://docs.python.org/3/search.html and select the [datetime](https://docs.python.org/3/library/datetime.html?highlight=time%20difference#module-datetime) library since it looks like the most appropriate for our problem, after reading through the available types in the module we come upon
    ```python
    class datetime.timedelta
        A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.
    ```
    this looks exactly like what we are trying to achieve. We just need to know how to create datetime instances, which is also listed in the available types right above `datetime.timedelta`
    ```python
    class datetime.datetime
        A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
    ```
    We can take a look at the examples in the documentation and then add tests using the examples
    - [Examples of usage datetime objects](https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime)
    - [Examples of usage timedelta objects](https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-timedelta)
- update `test_sleep_duration.py` with a test for a ``(datetime)`` object
    ```python
        def test_datetime_objects(self):
            self.assertEqual(
                datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
                ""
            )
    ```
    once again we have to comment out ``(test_duration_calculation)`` to see the results of the test we just added. The terminal shows a ``(NameError)`` because ``(datetime)`` is not defined in `test_sleep_duration.py`, we need to import it
- add an ``(import)`` statement for the ``(datetime)`` library
    ```python
    import datetime
    import random
    import sleep_duration
    import unittest
    ```
    the terminal reveals an [AssertionError](./ASSERTION_ERROR.md)
    ```python
    E       AssertionError: datetime.datetime(2006, 11, 21, 16, 30) != ''
    ```
- copy the value on the left side of the equation to replace the expected value in the test
    ```python
        def test_datetime_objects(self):
            self.assertEqual(
                datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
                datetime.datetime(2006, 11, 21, 16, 30)
            )
    ```
    from the results we can make the following conclusions about ``(datetime)`` objects from the ``(datetime)`` library.
    - `datetime.datetime.strptime` takes a ``(string)`` and ``(pattern)`` as inputs
    - `datetime.datetime` takes ``(year)``, ``(month)``, ``(date)``, ``(hours)`` and ``(minutes)`` as inputs
    - when we use ``(strptime)`` it returns a `datetime.datetime` object
    - we can also deduce from the pattern provided that
        - `%d` means day
        - `%m` means month
        - `%y` means a 2 digit year
        - `%H` means hour
        - `%M` means minute
- let us add a test for ``(timedelta)`` to test subtracting two datetime objects
    ```python
        def test_subtracting_datetime_objects(self):
            sleep_time = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
            wake_time = datetime.datetime.strptime("21/11/06 17:30", "%d/%m/%y %H:%M")
            self.assertEqual(wake_time-sleep_time, 1)
    ```
    we get an [AssertionError] in the terminal
    ```python
    E       AssertionError: datetime.timedelta(seconds=3600) != 1
    ```
- copy the value on the left of the equation and replace the expected value in the test
    ```python
        def test_subtracting_datetime_objects(self):
            sleep_time = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
            wake_time = datetime.datetime.strptime("21/11/06 17:30", "%d/%m/%y %H:%M")
            self.assertEqual(
                wake_time-sleep_time,
                datetime.timedelta(seconds=3600)
            )
    ```
    we have passing tests and now have a way to convert a string to a datetime object that we can perform subtraction operations on.
- So far the ``(timedelta)`` object we get shows seconds, but we wanted our result as a string. Let us try changing it to a string using the ``(str)`` keyword by adding a new test
    ```python
        def test_converting_timedelta_to_string(self):
            self.assertEqual(
                str(datetime.timedelta(seconds=3600)),
                ''
            )
    ```
    and we get an [AssertionError](./ASSERTION_ERROR.md) that looks more like what we are expecting
    ```python
    E       AssertionError: '1:00:00' != ''
    ```
- modify the expected value in the test to match the expected value in the terminal output
    ```python
        def test_converting_timedelta_to_string(self):
            self.assertEqual(
                str(datetime.timedelta(seconds=3600)),
                '1:00:00'
            )
    ```
    it looks like calling ``(str)`` on a ``(timedelta)`` object gives us the string in the format `Hours:Minutes:Seconds`

## Putting it all together

- uncomment ``(test_duration_calculation)`` and we get the [AssertionError](./ASSERTION_ERROR.md) we had before
- add a function called ``(get_datetime_object)`` to use for converting timestamps in the format we want in `sleep_duration.py`
    ```python
    def get_datetime_object(timestamp):
        return datetime.datetime.strptime(timestamp, "%d/%m/%y %H:%M")
    ```
    the error remains the same since we have not called the new function
- add a new return statement to the ``(duration)`` function with a call to the ``(get_datetime_object)``
    ```python
    def duration(wake_time, sleep_time):
        return get_datetime_object(wake_time) - get_datetime_object(sleep_time)
        return f'{get_hour(wake_time)-get_hour(sleep_time)}:{get_minute(wake_time)-get_minute(sleep_time)}'
    ```
    the terminal displays a ``(NameError)``
    ```python
    E       NameError: name 'datetime' is not defined
    ```
    we encountered this earlier when we were testing the ``(datetime)`` library
- update `sleep_duration.py` with an import statement at the beginning of the filoe
    ```python
    import datetime


    ```
    the terminal now shows a ``(ValueError)`` since the ``(timestamp)`` we give the ``(strptime)`` function in does not match the pattern we provided as the second option, we need to have a date as part of the pattern like the example since
    ```python
    E           ValueError: time data '10:57' does not match format '%d/%m/%y %H:%M'
    ```
- We add the new exception to our list of exceptions encountered
    ```python
    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    ```
- to make the test pass for now we will fix the date to the same day in the ``(get_datetime_object)``
    ```python
    def get_datetime_object(timestamp):
        return datetime.datetime.strptime(f'21/11/06 {timestamp}', "%d/%m/%y %H:%M")
    ```
    the terminal now shows an [AssertionError](./ASSERTION_ERROR.md) because our function is currently returning a ``(datetime)`` object not a string
- change the return in the ``(duration)`` function to return a string
    ```python
    def duration(wake_time, sleep_time):
        difference = get_datetime_object(wake_time) - get_datetime_object(sleep_time)
        return str(difference)
        return f'{get_hour(wake_time)-get_hour(sleep_time)}:{get_minute(wake_time)-get_minute(sleep_time)}'
    ```
    the terminal shows an [AssertionError](./ASSERTION_ERROR.md), this time our values are the same except we are missing the part for seconds
    ```python
    E       AssertionError: '14:21:00' != '14:21'
    ```
- modify ``(test_duration_when_given_hours_and_minutes)`` to include seconds
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
                f'{wake_hour-sleep_hour}:{wake_minute-sleep_minute}:00'
            )
    ```
    we get another [AssertionError](./ASSERTION_ERROR.md) in the terminal since we have not yet updated ``(test_duration_calculation)`` with the new format
- we will randomly get an [AssertionError](./ASSERTION_ERROR.md) for ``(test_duration_when_given_hours_and_minutes)``. Since we are using random integers for hours and minutes, there will be instances where the ``(wake_hour)`` is earlier than the ``(sleep_hour)`` leading to a negative number e.g.
    ```python
    E       AssertionError: '-1 day, 14:01:00' != '-9:-59:00'
    ```
    here, our expected values are still based on the way we were calculating the duration, subtracting the hour from hour and minute from minute independently.
- update the calculation to be more accurate by using the ``(get_datetime_object)`` function from `sleep_duration.py`
    ```python
        def test_duration_when_given_hours_and_minutes(self):
            wake_hour = random.randint(0, 24)
            sleep_hour = random.randint(0, 24)
            wake_minute = random.randint(0, 60)
            sleep_minute = random.randint(0, 60)
            wake_time = f'{wake_hour}:{wake_minute}'
            sleep_time = f'{sleep_hour}:{sleep_minute}'
            self.assertEqual(
                sleep_duration.duration(wake_time, sleep_time),
                str(
                    sleep_duration.get_datetime_object(wake_time)
                  - sleep_duration.get_datetime_object(sleep_time)
                )
            )
    ```
- edit the test to make the expected values match
    ```python
        def test_duration_calculation(self):
            wake_hour = 3
            sleep_hour = 2
            wake_minute = 30
            sleep_minute = 59
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=f'{wake_hour}:{wake_minute}',
                    sleep_time=f'{sleep_hour}:{sleep_minute}'
                ),
                '0:31:00'
            )
    ```
    and we are green again! Lovely
- let us remove the second return statement in the ``(duration)`` function in `sleep_duration.py` we left it there as a way to save what worked until confirmation that our new solution works better
    ```python
        def duration(wake_time, sleep_time):
            difference = get_datetime_object(wake_time) - get_datetime_object(sleep_time)
            return str(difference)
    ```
    all tests are still passing

### REFACTOR: make it better

Taking another look at the failing test we notice that our ``(duration)`` function returns negative numbers when given a ``(wake_time)`` that is earlier than a ``(sleep_time)`` e.g. `'-1 day, 14:01:00'`

Our ``(duration)`` function now accounts for a time traveling sleep scenario where you can go to sleep and wake up in the past.

- Let us add a test for it and see if we can update the function to only process durations where the wake time happens after the sleep time
    ```python
        def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
            wake_time = "01:00"
            sleep_time = "02:00"
            self.assertEqual(
                sleep_duration.duration(wake_time, sleep_time),
                "-01:00:00"
            )
    ```
    the terminal shows an [AssertionError](./ASSERTION_ERROR.md)
    ```python
    E       AssertionError: '-1 day, 23:00:00' != '-01:00:00'
    ```
- update the test to make it pass
    ```python
        def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
            wake_time = "01:00"
            sleep_time = "02:00"
            self.assertEqual(
                sleep_duration.duration(wake_time, sleep_time),
                '-1 day, 23:00:00'
            )
    ```
    we are green again
- we want the ``(duration)`` function to make a decision based on a comparison of ``(wake_time)`` and ``(sleep_time)``. If ``(wake_time)`` is earlier than ``(sleep_time)`` it should raise an [Exception](./EXCEPTION_HANDLING.md)
    ```python
    def duration(wake_time, sleep_time):
        wake_time = get_datetime_object(wake_time)
        sleep_time = get_datetime_object(sleep_time)
        if wake_time < sleep_time:
            raise ValueError(f'wake_time: {wake_time} is earlier than sleep_time: {sleep_time}')
        else:
            return str(wake_time - sleep_time)
    ```
    - it creates the ``(datetime)`` objects from our timestamp for ``(wake_time)`` and ``(sleep_time)``
    - we added a condition that checks if the ``(wake_time)`` is earlier than ``(sleep_time)``
    - it returns a ``(string)`` conversion of the difference between ``(wake_time)`` and ``(sleep_time)`` if ``(wake_time)`` is later than ``(sleep_time)``
    - it raises a ``(ValueError)`` if ``(wake_time)`` is earlier than ``(sleep_time)``

    the terminal shows a ``(ValueError)`` for ``(test_duration_when_given_earlier_wake_time_than_sleep_time)`` and ``(test_duration_when_given_hours_and_minutes)`` for the random values where ``(wake_time)`` is earlier than ``(sleep_time)`` which matches our expectation
    ```python
    E           ValueError: wake_time: 2006-11-21 01:00:00 is earlier than sleep_time: 2006-11-21 02:00:00
    ```
- to catch the error we need to add an [Exception Handler](./EXCEPTION_HANDLING.md) using a `try...except` statement and a `self.assertRaises` method call to confirm that the error is raised, update ``(test_duration_when_given_hours_and_minutes)``
    ```python
        def test_duration_when_given_hours_and_minutes(self):
            wake_hour = random.randint(0, 24)
            sleep_hour = random.randint(0, 24)
            wake_minute = random.randint(0, 60)
            sleep_minute = random.randint(0, 60)
            wake_time = f'{wake_hour}:{wake_minute}'
            sleep_time = f'{sleep_hour}:{sleep_minute}'
            try:
                self.assertEqual(
                    sleep_duration.duration(wake_time, sleep_time),
                    str(sleep_duration.get_datetime_object(wake_time)-sleep_duration.get_datetime_object(sleep_time))
                )
            except ValueError:
                with self.assertRaises(ValueError):
                    sleep_duration.duration(wake_time, sleep_time)
    ```
    we are left with the ``(ValueError)`` for ``(test_duration_when_given_earlier_wake_time_than_sleep_time)``
- update ``(test_duration_when_given_earlier_wake_time_than_sleep_time)`` with a `self.assertRaises` to catch the ``(ValueError)``
    ```python
        def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
            wake_time = "01:00"
            sleep_time = "02:00"
            with self.assertRaises(ValueError):
                sleep_duration.duration(wake_time, sleep_time),
    ```
    all tests are passing, we can clean up things we no longer need
- remove ``(get_hour)`` and ``(get_minute)`` from `sleep_duration.py`. Congratulations! You've built a function that takes in a ``(wake_time)`` and ``(sleep_time)`` as inputs and returns the difference between the two as long as the ``(wake_time)`` is later than the ``(sleep_time)``. Though our solution works we cheated by making it always use the same date. We will now proceed to modify the function to accept different days

## Duration when given day, hours and minutes

### RED: make it fail

add a failing test to `test_sleep_duration.py` called ``(test_duration_when_given_date_and_time)``

```python
    def test_duration_when_given_date_and_time(self):
        wake_hour = random.randint(0, 24)
        sleep_hour = random.randint(0, 24)
        wake_minute = random.randint(0, 60)
        sleep_minute = random.randint(0, 60)
        wake_time = f'21/11/06 {wake_hour}:{wake_minute}'
        sleep_time = f'21/11/07 {sleep_hour}:{sleep_minute}'

        self.assertEqual(
            sleep_duration.duration(wake_time, sleep_time),
            str(sleep_duration.get_datetime_object(wake_time)-sleep_duration.get_datetime_object(sleep_time))
        )
```

the terminal updates to show a ``(ValueError)`` similar to this

```python
E           ValueError: time data '21/11/06 21/11/06 8:9' does not match format '%d/%m/%y %H:%M'
```

the timestamps we provide to the ``(duration)`` function as inputs do not match the expected format of `%d/%m/%y %H:%M`, we get a repetition of the date portion because in the ``(get_datetime_object)`` we added a date to the timestamp to make it match the pattern

### GREEN: make it pass

- remove `21/11/06` from the string in ``(get_datetime_object)`` in `sleep_duration.py`
    ```python
    def get_datetime_object(timestamp):
        return datetime.datetime.strptime(timestamp, "%d/%m/%y %H:%M")
    ```
    the terminal updates to show a ``(ValueError)`` for ``(test_duration_calculation)`` because it no longer matches the expected timestamp format, it is missing the date portion
- add a date to ``(wake_time)`` and ``(sleep_time)`` in ``(test_duration_calculation)`` to make it match the expected inputs for ``(get_datetime_object)``
    ```python
        def test_duration_calculation(self):
            wake_hour = 3
            sleep_hour = 2
            wake_minute = 30
            sleep_minute = 59
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=f'21/11/06 {wake_hour}:{wake_minute}',
                    sleep_time=f'21/11/06 {sleep_hour}:{sleep_minute}'
                ),
                '0:31:00'
            )
    ```
    all the tests pass, though we have a few cases that are not raising errors because we are catching any ``(ValueError)`` with the `try...except` block in ``(test_duration_when_given_hours_and_minutes)`` and the `self.assertRaises` in ``(test_duration_when_given_earlier_wake_time_than_sleep_time)``
- we update the `self.assertRaises` from ``(test_duration_when_given_earlier_wake_time_than_sleep_time)`` to catch the specific failure we expect using `self.assertRaisesRegex` which takes in as input an expected exception and the message it returns
    ```python
        def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
            wake_time = "01:00"
            sleep_time = "02:00"
            with self.assertRaisesRegex(ValueError, f'wake_time: {wake_time} is earlier than sleep_time: {sleep_time}'):
                sleep_duration.duration(wake_time, sleep_time)
    ```
    the terminal responds with an [AssertionError](./ASSERTION_ERROR.md) because the message raised by the ``(ValueError)`` is different from what we expect
    ```python
    ValueError: time data '01:00' does not match format '%d/%m/%y %H:%M'

    During handling of the above exception, another exception occurred:

    self = <tests.test_sleep_duration.TestSleepDuration testMethod=test_duration_when_given_earlier_wake_time_than_sleep_time>

        def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
            wake_time = "01:00"
            sleep_time = "02:00"
            with self.assertRaisesRegex(ValueError, f'wake_time: {wake_time} is earlier than sleep_time: {sleep_time}'):
    >           sleep_duration.duration(wake_time, sleep_time)
    E           AssertionError: "wake_time: 01:00 is earlier than sleep_time: 02:00" does not match "time data '01:00' does not match format '%d/%m/%y %H:%M'"
    ```
    at the top of the error we see the failure details we see the actual message returned by the ``(ValueError)``
    ```python
    ValueError: time data '01:00' does not match format '%d/%m/%y %H:%M'
    ```
    the timestamp provided to the ``(duration)`` function does not match the expected format of `day/month/year hour:minute`
- modify the ``(wake_time)`` and ``(sleep_time)`` variables to include a year
    ```python
    def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
        wake_time = "21/11/06 01:00"
        sleep_time = "21/11/06 02:00"
        with self.assertRaisesRegex(ValueError, f'wake_time: {wake_time} is earlier than sleep_time: {sleep_time}'):
            sleep_duration.duration(wake_time, sleep_time)
    ```
    the terminal still shows an [AssertionError](./ASSERTION_ERROR.md) this time with an updated message showing the returned values from the ``(get_datetime_object)`` function
- we update the test using the ``(get_datetime_object)`` function to display the correct timestamps in the ``(ValueError)`` message
    ```python
        def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
            wake_time = "21/11/06 01:00"
            sleep_time = "21/11/06 02:00"
            with self.assertRaisesRegex(ValueError, f'wake_time: {sleep_duration.get_datetime_object(wake_time)} is earlier than sleep_time: {sleep_duration.get_datetime_object(sleep_time)}'):
                sleep_duration.duration(wake_time, sleep_time)
    ```
    all tests are passing again, our test is very specific for the case when ``(wake_time)`` is earlier than ``(sleep_time)`` and displays an appropriate error message, we are left with ``(test_duration_when_given_hours_and_minutes)``
- change the `self.assertRaises(ValueError)` statement in ``(test_duration_when_given_hours_and_minutes)`` to match what we did in ``(test_duration_when_given_earlier_wake_time_than_sleep_time)``
    ```python
        def test_duration_when_given_hours_and_minutes(self):
            wake_hour = random.randint(0, 24)
            sleep_hour = random.randint(0, 24)
            wake_minute = random.randint(0, 60)
            sleep_minute = random.randint(0, 60)
            wake_time = f'{wake_hour}:{wake_minute}'
            sleep_time = f'{sleep_hour}:{sleep_minute}'
            try:
                self.assertEqual(
                    sleep_duration.duration(wake_time, sleep_time),
                    str(sleep_duration.get_datetime_object(wake_time)-sleep_duration.get_datetime_object(sleep_time))
                )
            except ValueError:
                with self.assertRaisesRegex(ValueError, f'wake_time: {sleep_duration.get_datetime_object(wake_time)} is earlier than sleep_time: {sleep_duration.get_datetime_object(sleep_time)}'):
                    sleep_duration.duration(wake_time, sleep_time)
    ```
    the terminal displays a ``(ValueError)`` about the timestamp not matching the expected format for ``(strptime)``
    ```
    E           ValueError: time data '15:10' does not match format '%d/%m/%y %H:%M'
    ```
- add a year to the ``(wake_time)`` and ``(sleep_time)`` variables
    ```python
        def test_duration_when_given_hours_and_minutes(self):
            wake_hour = random.randint(0, 24)
            sleep_hour = random.randint(0, 24)
            wake_minute = random.randint(0, 60)
            sleep_minute = random.randint(0, 60)
            wake_time = f'21/11/06 {wake_hour}:{wake_minute}'
            sleep_time = f'21/11/06 {sleep_hour}:{sleep_minute}'
            try:
                self.assertEqual(
                    sleep_duration.duration(wake_time, sleep_time),
                    str(sleep_duration.get_datetime_object(wake_time)-sleep_duration.get_datetime_object(sleep_time))
                )
            except ValueError:
                with self.assertRaisesRegex(ValueError, f'wake_time: {sleep_duration.get_datetime_object(wake_time)} is earlier than sleep_time: {sleep_duration.get_datetime_object(sleep_time)}'):
                    sleep_duration.duration(wake_time, sleep_time)
    ```
    the terminal shows all tests are passing again

## Clean up

``(test_duration_when_given_day_and_time)`` looks like a duplicate of ``(test_duration_when_given_hours_and_minutes)``, it has the exact same variable assignment setup with the exact same test, it is only missing the `try...except` block, which means we can remove ``(test_duration_when_given_day_and_time)``

``(test_duration_calculation)`` gives specific timestamps of `3:30` for ``(wake_time)`` and `2:59` for ``(sleep_time)``, while ``(test_duration_when_given_hours_and_minutes)`` uses random timestamps from `0:00` to `23:59` for those variables. Since the random variables cover every timestamp in a given day we can remove ``(test_duration_calculation)``

The same argument could be made for ``(test_duration_when_given_earlier_wake_time_than_sleep_time)`` since we have a `try...except` block with a ``(assertRaisesRegex)`` that catches the random timestamps where ``(wake_time)`` is earlier than ``(sleep_time)`` we can remove ``(test_duration_when_given_earlier_wake_time_than_sleep_time)``

The first test we wrote was ``(test_failure)`` and we no longer need it

We also need a more descriptive name for ``(test_duration_when_given_hours_and_minutes)`` we could rename it to ``(test_duration_when_given_a_timestamp)`` or ``(test_duration_when_given_date_and_time)``, the choice is yours programmer.

## Recap

Our challenge was to create a function that calculates the difference between two given timestamps and to make it happen we learned
- how to convert a ``(string)`` to an ``(integer)``
- how to split a ``(string)`` into a ``(list)`` using a given delimiter/separator
- how to index a ``(list)`` to get specific elements
- how to convert a ``(string)`` to a ``(datetime)`` object using the `datetime.datetime.strptime` function
- how to convert a ``(datetime)`` object to a ``(string)``
- how to subtract two ``(datetime)`` objects
- how to convert a ``(timedelta)`` to a ``(string)``
- how to use ``(assertRaisesRegex)`` to catch a specific exception and message
- how to view the ``(methods)`` and ``(attributes)`` of the ``(string)`` object
- how to use the `random.randint` to generate a random integer between two given integers
- how to use the ``(help)`` keyword to view documentation

If you want to do more, try playing with the timestamp format and pattern in ``(get_datetime_object)``. What would you change in `"%d/%m/%y %H:%M"` to make it accept dates in a different format e.g. `2006/11/21` or `11/21/2006`?