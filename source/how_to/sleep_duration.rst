
How to measure sleep duration
==============================

In this chapter I take a look at building a program that returns the amount of time slept based on a given sleep and wake time.

Prerequisites
-------------

:doc:`How to create a Test Driven Development Environment </how_to/create_tdd_environment>` with ``sleep_duration`` as the project name

----

Duration when given Hours
------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test to ``test_sleep_duration.py`` and remove ``test_failure`` since I no longer need it

.. code-block:: python

  import unittest


  class TestSleepDuration(unittest.TestCase):

      def test_duration_when_given_hours_only(self):
          self.assertEqual(
              sleep_duration.duration(
                wake_time='08:00',
                sleep_time='07:00'
              ),
              1
          )

the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ which I add to the list of exceptions encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # NameError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I add an import statement for the missing name

  .. code-block:: python

    import sleep_duration
    import unittest


    class TestSleepDuration(unittest.TestCase):
    ...

  and the terminal shows an :doc:`/exceptions/AttributeError` since I do not have a definition for ``duration`` in `sleep_duration.py`


* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* I add a name to ``sleep_duration.py`` and the terminal displays a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ since the name is not defined

  .. code-block:: python

    duration

* I make ``duration`` a variable by assigning it to the null value :doc:`None </data_structures/none>`

  .. code-block:: python

    duration = None

  the terminal shows a :doc:`/exceptions/TypeError` because :doc:`None </data_structures/none>` is not callable
* I add the exception to the running list

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* then define ``duration`` as a function

  .. code-block:: python

    def duration():
        return None

  the :doc:`/exceptions/TypeError` remains but with a different message about the first argument passed in from the test

* I change the definition of ``duration`` to accept the required keyword argument

  .. code-block:: python

    def duration(wake_time):
        return None

  the terminal shows a similar message as before, this time for the second keyword argument

* I change the definition the same way

  .. code-block:: python

    def duration(wake_time, sleep_time):
        return None

  the terminal now shows an :doc:`/exceptions/AssertionError` since the duration function returns :doc:`None </data_structures/none>` and the test expects ``1`` as the duration when a sleep time of ``07:00`` and a wake time of ``08:00`` is given

* I change the return value for the duration function to the expectation

  .. code-block:: python

    def duration(wake_time, sleep_time):
        return 1

GREEN! all tests are passing

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

The function currently returns ``1`` regardless of the inputs given but for it to be useful it has to calculate the difference between the wake time and the sleep time. It would be a large effort to write a test case for every permutation of sleep and wake times.

I could write a test that uses a random variable for the sleep and wake times, like in the :doc:`/how_to/calculator`


* I add an import statement for the `random <https://docs.python.org/3/library/random.html?highlight=random#module-random>`_ module to ``test_sleep_duration.py``

  .. code-block:: python

    import random
    import sleep_duration
    import unittest

* then add a new test with random values

  .. code-block:: python

    class TestSleepDuration(unittest.TestCase):

        def test_duration_when_given_hours_only(self):
            wake_hour = random.randint(0, 23)
            sleep_hour = random.randint(0, 23)
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=f'{wake_hour}:00',
                    sleep_time=f'{sleep_hour}:00'
                ),
                1
            )

  I use a random integer from ``0`` to ``23`` as the hours for sleep and wake time and interpolate them in the strings I use as inputs, this means the wake and sleep time will randomly vary from ``00:00`` to ``23:00``

* the terminal still shows the test is passing because the expected value is ``1``, I need to change it to match the true expectation, which is that it should be the duration between ``wake_time`` and ``sleep_time``.

  .. code-block:: python

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

  I get an :doc:`/exceptions/AssertionError` because ``sleep_duration.duration`` still returns ``1`` but from the test I expect the difference between ``wake_time`` and ``sleep_time``
* I change the ``duration`` function in ``sleep_duration.py`` to return a difference between the ``wake_time`` and ``sleep_time``?

  .. code-block:: python

    def duration(wake_time, sleep_time):
        return wake_time - sleep_time

  the terminal shows a :doc:`/exceptions/TypeError`. I passed in two strings and python does not have an operation defined for subtracting one string from another.

  I need to find a way to convert the timestamp from a string to a number. I know that the two inputs are currently in the format ``XX:00``, if I can parse the string to get the first two characters and convert those digits to a number I should be able to get the calculation
* to find out what options are available, I look at the :doc:`methods </functions/functions>` and ``attributes`` of `strings <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ by adding a failing test to ``test_sleep_duration.py``, this time using the `dir <https://docs.python.org/3/library/functions.html?highlight=dir#dir>`_ :doc:`function </functions/functions>`

  .. code-block:: python

    def test_string_methods_and_attributes(self):
        self.assertEqual(
            dir("00:00"),
            None
        )

  an :doc:`/exceptions/AssertionError` is raised

  .. code-block:: python

    E    AssertionError: ['__add__', '__class__', '__contains__', [918 chars]ill'] != None

* I copy the value on the left side of the comparison and replace :doc:`None </data_structures/none>` as the expected value in the test

  .. code-block:: python

      def test_string_methods_and_attributes(self):
          self.assertEqual(
              dir("00:00"),
              ['__add__', '__class__', '__contains__', [918 chars]ill']
          )

  the terminal shows a ``SyntaxError``

  .. code-block:: python

    ['__add__', '__class__', '__contains__', [918 chars]ill']
                         ^
    SyntaxError: invalid syntax

  ah, there is a closing quote, with no open quote, I add an opening quote

  .. code-block:: python

    def test_string_methods_and_attributes(self):
        self.assertEqual(
            dir("00:00"),
            ['__add__', '__class__', '__contains__', '[918 chars]ill']
        )

  I still have an :doc:`/exceptions/AssertionError` but with a different message and a suggestion

  .. code-block:: python

    E      Diff is 1265 characters long. Set self.maxDiff to None to see it.

* I try the suggestion

  .. code-block:: python

    def test_string_methods_and_attributes(self):
        self.maxDiff = None
        self.assertEqual(
          dir("00:00"),
          ['__add__', '__class__', '__contains__', '[918 chars]ill']
        )

  `maxDiff <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.maxDiff>`_ sets a limit on the number of characters the terminal shows for a difference between two objects, there is no limit when it is set to None. I now see a full list of all the attributes of a `string <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_

* I copy the values from the terminal into the test

  .. note::

    Your results may vary based on your version of Python

  .. code-block:: python

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

* the terminal displays a :doc:`/exceptions/TypeError` because python still does not support subtracting one string from another

  .. code-block:: python

      def duration(wake_time, sleep_time):
    >    return wake_time - sleep_time
    E    TypeError: unsupported operand type(s) for -: 'str' and 'str'

  I still need a way to convert a `string <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ to a number.

* I try one of the :doc:`methods </functions/functions>` listed from ``test_string_methods_and_attributes`` to see if it will get me closer to a solution. Going with just the names listed might not be enough since I do not know what they do. I can check the `python documentation <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ for extra details by using the `help <https://docs.python.org/3/library/functions.html?highlight=dir#help>`_ system

  .. code-block:: python

    self.assertEqual(
        help(str),
    )

  the terminal shows documentation for the `string <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ module, I scroll through reading through the descriptions for each :doc:`method </functions/functions>` until I see one that looks like it can solve my problem

  .. code-block:: python

    |  split(self, /, sep=None, maxsplit=-1)
    |   Return a list of the words in the string, using sep as the delimiter string.
    |
    |   sep
    |    The delimiter according which to split the string.
    |    None (the default value) means split according to any whitespace,
    |    and discard empty strings from the result.
    |   maxsplit
    |    Maximum number of splits to do.
    |    -1 (the default value) means no limit.

  the `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_ :doc:`method </functions/functions>` looks like a good solution since it splits up a word when given a ``delimeter``

* I remove the failing test and replace it with one for the `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_ :doc:`method </functions/functions>`

  .. code-block:: python

      def test_string_split_method(self):
          self.assertEqual(
              "00:00".split(),
              None
          )

  the terminal shows that `split <https://docs.python.org/3/library/stdtypes.html#str.split>` creates a list when given a string

  .. code-block:: python

    E    AssertionError: ['00:00'] != None

  I change the expectation from :doc:`None </data_structures/none>`

  .. code-block:: python

    def test_string_split_method(self):
        self.assertEqual(
            "00:00".split(),
            ["00:00"]
        )

  and the test passes with the terminal showing the :doc:`/exceptions/TypeError` that took me down this path

  .. code-block:: python

    E    TypeError: unsupported operand type(s) for -: 'str' and 'str'

* what I want is to split the string on a ``delimiter`` so I get the separate parts, something like ``["00", "00"]``, using ``:`` as the ``delimeter``. I change the test to reflect this desire

  .. code-block:: python

    def test_string_split_method(self):
        self.assertEqual(
            "00:00".split(),
            ['00', '00']
        )

  the terminal shows an :doc:`/exceptions/AssertionError`, the use of the `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_ :doc:`method </functions/functions>` has not yet given me what I want. Looking back at the documentation, I see that `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_ takes in ``self, /, sep=None, maxsplit=-1`` as inputs and ``sep`` is the ``delimiter``
* I change the test by passing in ``:`` to the `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_ :doc:`method </functions/functions>` as the ``delimiter``

  .. code-block:: python

    def test_string_split_method(self):
        self.assertEqual(
            "00:00".split(':'),
            ['00', '00']
        )

  the test passes and I now know how to get the first part of the ``wake_time`` and ``sleep_time``

* I change the definition of the ``duration`` function in ``sleep_duration.py`` using what I have learned so far

  .. code-block:: python

    def duration(wake_time, sleep_time):
        return wake_time.split(':') - sleep_time.split(':')

  the terminal still shows a :doc:`/exceptions/TypeError`, this time for trying to subtract a :doc:`list </data_structures/lists>` from a :doc:`list </data_structures/lists>`

  .. code-block:: python

    E    TypeError: unsupported operand type(s) for -: 'list' and 'list'

  Since I only need the first part of the list, I can get the specific item by using its index. Python uses zero-based indexing so the first item is at index ``0`` and the second item at ``1``
* I add a failing test to ``test_string_split_method`` to test getting specific parts of the :doc:`list </data_structures/lists>` created from splitting a `string <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_

  .. code-block:: python

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

  the terminal shows an :doc:`/exceptions/AssertionError` because the first item (item zero) from splitting ``"12:34"`` on the delimiter ``:`` is ``"12"``, good, I am closer to what I want
* I change the expected value in the test to match the value in the terminal

  .. code-block:: python

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

  the terminal shows another :doc:`/exceptions/AssertionError` , this time to confirm that the second item (item one) from splitting ``"12:34"`` on the delimiter ``:`` is ``"34"``, I am not dealing with this part yet but I can assume I would use it soon, so I change the expected value in the same way and the test passes bringing me back to the unsolved :doc:`/exceptions/TypeError`
* I change the ``duration`` function using what I have learned to only return the subtraction of the first parts of ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def duration(wake_time, sleep_time):
        return wake_time.split(':')[0] - sleep_time.split(':')[0]

  the terminal still shows a :doc:`/exceptions/TypeError` for an unsupported operation of trying to subtract one `string <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ from another, and though it is not obvious here, from ``test_string_split_method`` I know that the strings being subtracted are the values to the left of the delimiter ``:`` not the entire string value of ``wake_time`` and ``sleep_time``. For example,  if the given ``wake_time`` is ``"02:00"`` and the given ``sleep_time`` is ``"01:00"``  the program is currently trying to subtract ``"01""`` from ``"02"`` which is different from trying to subtract ``1`` from ``2``
* I now have the task of converting the string to a number so I can do the subtraction, for this I use the `int <https://docs.python.org/3/library/functions.html?highlight=int#int>`_ constructor which returns an integer for a given value. I comment out the current failing test and add a test to ``test_sleep_duration.py`` showing what `int <https://docs.python.org/3/library/functions.html?highlight=int#int>`_ does

  .. code-block:: python

    # def test_duration_when_given_hours_only(self):
    #   wake_hour = random.randint(0, 23)
    #   sleep_hour = random.randint(0, 23)
    #   self.assertEqual(
    #    sleep_duration.duration(
    #      wake_time=f'{wake_hour}:00',
    #      sleep_time=f'{sleep_hour}:00'
    #    ),
    #    wake_hour-sleep_hour
    #   )

    def test_converting_a_string_to_an_integer(self):
        self.assertEqual(int("12"), 0)

  the terminal shows an :doc:`/exceptions/AssertionError` since ``12 != 0`` and I change the test to match the expectation

  .. code-block:: python

    def test_converting_a_string_to_an_integer(self):
        self.assertEqual(int("12"), 12)

  I now have another tool to use to solve the problem

* after uncommenting the test, I am back to the :doc:`/exceptions/TypeError` I have been trying to solve. I change the ``duration`` function with what I have learned to see if it makes the test pass

  .. code-block:: python

    def duration(wake_time, sleep_time):
        return (
            int(wake_time.split(':')[0])
          - int(sleep_time.split(':')[0])
        )

  YES! I am green, with a way to randomly test if the duration function can calculate the sleep duration given any random ``sleep`` and ``wake`` time. What a beautiful life!
* I could rewrite the solution I have in a way that tries to explain what is happening to someone who does not know how to index a list or use `int <https://docs.python.org/3/library/functions.html?highlight=int#int>`_  or `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_. What do you think?

  .. code-block:: python

    def duration(wake_time, sleep_time):
        wake_time_split = wake_time.split(':')
        wake_time_hour = wake_time_split[0]
        wake_time_hour_integer = int(wake_time_hour)
        return wake_time_hour_integer - int(sleep_time.split(':')[0])

  the terminal shows all tests are still passing, so I try the same thing for ``sleep_time``

  .. code-block:: python

    def duration(wake_time, sleep_time):
        wake_time_split = wake_time.split(':')
        wake_time_hour = wake_time_split[0]
        wake_time_hour_integer = int(wake_time_hour)

        sleep_time_split = sleep_time.split(':')
        sleep_time_hour = sleep_time_split[0]
        sleep_time_hour_integer = int(sleep_time_hour)

        return wake_time_hour_integer - sleep_time_hour_integer

* There is some repetition in the function, for each string given it

  - splits the string on the delimiter ``:``
  - gets the first (0th) value from the split
  - converts the first value from the split to an integer

  I could abstract this repetition to a function and call the function for each value, the programming ancestors are singing a familiar tune - `Do Not Repeat Yourself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

  .. code-block:: python

    def function(value):
        value_split = value.split(':')
        value_hour = value_split[0]
        value_hour_integer = int(value_hour)
        return value_hour_integer

    def duration(wake_time, sleep_time):
        return function(wake_time) - function(sleep_time)

  since the tests are passing, I can rename the abstracted ``function`` to something more descriptive like ``get_hour``

  .. code-block:: python

    def get_hour(value):
        value_split = value.split(':')
        value_hour = value_split[0]
        value_hour_integer = int(value_hour)
        return value_hour_integer

    def duration(wake_time, sleep_time):
        return get_hour(wake_time) - get_hour(sleep_time)

* I could rewrite the ``get_hour`` function to use the same variable name in the operation for example

  .. code-block:: python

    def get_hour(value):
        value = value.split(':')
        value = value[0]
        value = int(value)
        return value

  the terminal still shows passing tests. This is called `Extract Method <https://refactoring.com/catalog/extractFunction.html>`_ from the `Refactoring Catalog <https://refactoring.com/catalog/>`_
* I could also rewrite it to use one line though it will no longer be as explicit

  .. code-block:: python

    def get_hour(value):
        return int(value.split(':')[0])

  the terminal still shows passing tests. Since the test is green you can try any ideas you have until you understand what has been written so far. Time for a nap.

----

Duration when given Hours and Minutes
--------------------------------------

I found a solution that provides the right duration when given sleep time and wake time in a given day. the solution does not take minutes into account when doing the calculation

RED: make it fail
^^^^^^^^^^^^^^^^^

I am going to add a failing test for that scenario to ``test_sleep_duration.py``

.. code-block:: python

    def test_duration_when_given_hours_and_minutes(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
        wake_minute = random.randint(0, 59)
        sleep_minute = random.randint(0, 59)
        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour}:{wake_minute}',
                sleep_time=f'{sleep_hour}:{sleep_minute}'
            ),
            f'{wake_hour-sleep_hour}:{wake_minute-sleep_minute}'
        )

the terminal shows an :doc:`/exceptions/AssertionError`, the expected value is now a string that contains the subtraction of the sleep hour from the wake hour, separated by a delimiter ``:`` and the subtraction of the sleep minute from the wake minute, so if for example I have a wake_time of ``08:30`` and a sleep_time of ``07:11`` I should have ``1:19`` as the output

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I change the output of the ``duration`` function in ``sleep_duration.py`` to match the format of the expected value

  .. code-block:: python

    def duration(wake_time, sleep_time):
        return (
            f'{get_hour(wake_time)-get_hour(sleep_time)}:'
            f'{wake_time-sleep_time}'
        )

  I get a :doc:`/exceptions/TypeError` because I just tried to subtract one string from another, at this point I have a long standing relationship with :doc:`/exceptions/TypeError`
* I change the second part of the timestamp to use the ``get_hour`` function

  .. code-block:: python

    def duration(wake_time, sleep_time):
        return (
            f'{get_hour(wake_time)-get_hour(sleep_time)}:'
            f'{get_hour(wake_time)-get_hour(sleep_time)}'
        )

  the terminal now shows an :doc:`/exceptions/AssertionError` because the difference in minutes is not yet calculated

* I will use the ``get_hour`` function to create a similar function which gets the minutes from a given timestamp

  .. code-block:: python

    def get_hour(value):
        return int(value.split(':')[0])

    def get_minute(value):
        return int(value.split(':')[1])

    def duration(wake_time, sleep_time):
        return (
            f'{get_hour(wake_time)-get_hour(sleep_time)}:'
            f'{get_hour(wake_time)-get_hour(sleep_time)}'
        )

  the terminal still shows an :doc:`/exceptions/AssertionError`

* after I change the ``duration`` function with a call to the new ``get_minute`` function, the test passes

  .. code-block:: python

    def get_hour(value):
        return int(value.split(':')[0])

    def get_minute(value):
        return int(value.split(':')[1])

    def duration(wake_time, sleep_time):
        return (
            f'{get_hour(wake_time)-get_hour(sleep_time)}:'
            f'{get_minute(wake_time)-get_minute(sleep_time)}'
        )

  the terminal now reveals a failure for ``test_duration_when_given_hours_only`` which passed earlier, I introduced a regression when I changed the format of the output of ``duration`` function from a number to a string

* I change ``test_duration_when_given_hours_only`` where I supplied only hours to expect a string instead of a number, making it match the current form of the ``duration`` :doc:`function </functions/functions>`

  .. code-block:: python

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

  I get an :doc:`/exceptions/AssertionError` in the terminal because I have two zeros ``:00`` in the expected return value but the duration function returns ``0`` for the minute side of the timestamp after doing a subtraction, which means ``00`` minus ``00`` is ``0`` not ``00``.

* I could change the right side of the expected value to ``0`` to make it pass, but that would not be necessary because ``test_duration_when_given_hours_and_minutes`` already shows the cases where the minutes are zero since the test uses a random number from ``0`` to ``23`` for hours and a random number from ``0`` to ``59`` for minutes.

  I remove ``test_duration_when_given_hours_only`` since I no longer need it and the terminal shows passing tests

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

The ``duration`` function currently returns a subtraction of hours and a subtraction of minutes but is not accurate for calculating real differences in time. For instance when it is given a wake time of ``3:30`` and a sleep time of ``2:59`` it will return ``1:-29`` which is not a real duration instead of ``0:31``.

This means that even though the tests are passing, once again the ``duration`` function does not meet the requirement of calculating the duration between two timestamps. I need a better way, just when I thought it was over

* I add a new test for the specific example to ``test_sleep_duration.py``

  .. code-block:: python

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

  the terminal shows an :doc:`/exceptions/AssertionError` since ``1:-29`` is not equal to ``0:31``

* after doing a search in the `python online documentation <https://docs.python.org/3/search.html>`_ for `time difference <https://docs.python.org/3/search.html?q=time+difference>`_, I select the `datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#module-datetime>`_ module since it looks like it has a solution for the problem. Reading through the available types in the module I see

  .. code-block:: python

    class datetime.timedelta
      A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.

  This looks exactly like what I am trying to achieve. I just need to know how to create `datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#module-datetime>`_ instances, which is also listed in the available types right above `datetime.timedelta <https://docs.python.org/3/library/datetime.html?highlight=datetime#timedelta-objects>`_

  .. code-block:: python

    class datetime.datetime
      A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.

  I take a look at the examples in the documentation and then add tests using the examples

  * `Examples of usage datetime objects <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_
  * `Examples of usage timedelta objects <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-timedelta>`_

* I change ``test_sleep_duration.py`` with a test for a `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ object

  .. code-block:: python

    def test_datetime_datetime_objects(self):
        self.assertEqual(
            datetime.datetime.strptime(
                "21/11/06 16:30",
                "%d/%m/%y %H:%M"
            ),
            ""
        )

  Once again I have to comment out the failing test for a short time, to see the results of the test I just added. The terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ because ``datetime`` is not defined in ``test_sleep_duration.py``, I need to import it

* I add an ``import`` statement for the `datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#module-datetime>`_ module to ``test_sleep_duration.py``

  .. code-block:: python

    import datetime
    import random
    import sleep_duration
    import unittest

  the terminal displays an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    E    AssertionError: datetime.datetime(2006, 11, 21, 16, 30) != ''

* I copy the value on the left side of the :doc:`/exceptions/AssertionError` to replace the expected value in the test

  .. code-block:: python

    def test_datetime_datetime_objects(self):
        self.assertEqual(
            datetime.datetime.strptime(
                "21/11/06 16:30",
                "%d/%m/%y %H:%M"
            ),
            datetime.datetime(2006, 11, 21, 16, 30)
        )

  from the results I see that

  - `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ takes ``year``, ``month``, ``date``, ``hours`` and ``minutes`` as inputs
  - the `datetime.datetime.strptime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime.strptime>`_ :doc:`method </functions/functions>` takes 2 `strings <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ as inputs - timestamp and a pattern.
  - the `datetime.datetime.strptime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime.strptime>`_ :doc:`method </functions/functions>` returns a `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ object
  - from the pattern provided that

    * ``%d`` is for days
    * ``%m`` is for months
    * ``%y`` is for 2 digit years
    * ``%H`` is for hours
    * ``%M`` is for minutes

* I add a test for `datetime.timedelta <https://docs.python.org/3/library/datetime.html?highlight=datetime#timedelta-objects>`_ to test subtracting two `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ objects

  .. code-block:: python

    def test_subtracting_datetime_datetime_objects(self):
        sleep_time = datetime.datetime.strptime(
            "21/11/06 16:30",
            "%d/%m/%y %H:%M"
        )
        wake_time = datetime.datetime.strptime(
            "21/11/06 17:30",
            "%d/%m/%y %H:%M"
        )
        self.assertEqual(wake_time-sleep_time, 1)

  I get an :doc:`/exceptions/AssertionError` in the terminal

  .. code-block:: python

    E    AssertionError: datetime.timedelta(seconds=3600) != 1

* I copy the value on the left of the :doc:`/exceptions/AssertionError` and replace the expected value in the test

  .. code-block:: python

    def test_subtracting_datetime_datetime_objects(self):
        sleep_time = datetime.datetime.strptime(
            "21/11/06 16:30",
            "%d/%m/%y %H:%M"
        )
        wake_time = datetime.datetime.strptime(
            "21/11/06 17:30",
            "%d/%m/%y %H:%M"
        )
        self.assertEqual(
            wake_time-sleep_time,
            datetime.timedelta(seconds=3600)
        )

  I have passing tests and a way to convert a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ to a `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ object that I can perform subtraction operations on

* So far the `datetime.timedelta <https://docs.python.org/3/library/datetime.html?highlight=datetime#timedelta-objects>`_ object I get shows seconds, but I want the result as a string. I add a test to see if I can change it to a string using the `str <https://docs.python.org/3/library/stdtypes.html#str>`_ constructor

  .. code-block:: python

    def test_converting_timedelta_to_string(self):
        self.assertEqual(
            str(datetime.timedelta(seconds=3600)),
            ''
        )

  and I get an :doc:`/exceptions/AssertionError` that looks more like what I am expecting

  .. code-block:: python

    E    AssertionError: '1:00:00' != ''

* I change the expected value in the test to match the value from the terminal output

  .. code-block:: python

    def test_converting_timedelta_to_string(self):
        self.assertEqual(
            str(datetime.timedelta(seconds=3600)),
            '1:00:00'
        )

  it looks like calling `str <https://docs.python.org/3/library/stdtypes.html#str>`_ on a `datetime.timedelta <https://docs.python.org/3/library/datetime.html?highlight=datetime#timedelta-objects>`_ object returns ae string in the format ``Hours:Minutes:Seconds``

Putting it Together
-----------------------


* I uncomment ``test_duration_calculation`` and I get the :doc:`/exceptions/AssertionError` that sent me down this hole
* I add a function for converting timestamps to ``sleep_duration.py`` and call it ``get_datetime_object``

  .. code-block:: python

    def get_datetime_object(timestamp):
        return datetime.datetime.strptime(timestamp, "%d/%m/%y %H:%M")

  the error remains the same since I have not called the new function

* I add a new return statement to the ``duration`` function with a call to the ``get_datetime_object`` above the existing return statement because I do not want to remove what has worked so far until I have a new working solution

  .. code-block:: python

    def duration(wake_time, sleep_time):
        return (
            get_datetime_object(wake_time)
          - get_datetime_object(sleep_time)
        )
        return (
            f'{get_hour(wake_time)-get_hour(sleep_time)}:'
            f'{get_minute(wake_time)-get_minute(sleep_time)}'
        )

  the terminal displays a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    E    NameError: name 'datetime' is not defined

  I encountered this earlier when testing the `datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime>`_ module

* I add an import statement to the beginning of ``sleep_duration.py``

  .. code-block:: python

    import datetime

  the terminal now shows a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ since the ``timestamp`` I give the `datetime.datetime.strptime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime.strptime>`_ function does not match the pattern I provided as the second option, I need to have a date as part of the pattern like the example

  .. code-block:: python

    E      ValueError: time data '10:57' does not match format '%d/%m/%y %H:%M'

* I add the new exception to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # ValueError

* to make the test pass for now I fix the date to the same day in the ``get_datetime_object``

  .. code-block:: python

    def get_datetime_object(timestamp):
        return datetime.datetime.strptime(
            f'21/11/06 {timestamp}',
            '%d/%m/%y %H:%M'
        )

  the terminal now shows an :doc:`/exceptions/AssertionError` because the function is currently returning a ``datetime`` object not a string
* I change the return in the ``duration`` function to return a string

  .. code-block:: python

    def duration(wake_time, sleep_time):
        difference = (
            get_datetime_object(wake_time)
          - get_datetime_object(sleep_time)
        )
        return str(difference)
        return (
            f'{get_hour(wake_time)-get_hour(sleep_time)}:'
            f'{get_minute(wake_time)-get_minute(sleep_time)}'
        )

  the terminal shows an :doc:`/exceptions/AssertionError` for ``test_duration_when_given_hours_and_minutes``, this time the values are the same for hours and minutes but not seconds

  .. code-block:: python

    E    AssertionError: '14:21:00' != '14:21'

* I change ``test_duration_when_given_hours_and_minutes`` to include seconds

  .. code-block:: python

      def test_duration_when_given_hours_and_minutes(self):
          wake_hour = random.randint(0, 23)
          sleep_hour = random.randint(0, 23)
          wake_minute = random.randint(0, 59)
          sleep_minute = random.randint(0, 59)
          self.assertEqual(
              sleep_duration.duration(
                  wake_time=f'{wake_hour}:{wake_minute}',
                  sleep_time=f'{sleep_hour}:{sleep_minute}'
              ),
              f'{wake_hour-sleep_hour}:{wake_minute-sleep_minute}:00'
          )

  I get another :doc:`/exceptions/AssertionError` since I have not yet changed ``test_duration_calculation`` with the new format
* I will randomly get an :doc:`/exceptions/AssertionError` for ``test_duration_when_given_hours_and_minutes``. Since I am using random integers for hours and minutes, there will be instances where the ``wake_hour`` is earlier than the ``sleep_hour`` leading to a negative number for example

  .. code-block:: python

    E    AssertionError: '-1 day, 14:01:00' != '-9:-59:00'

  here, the expected values are still based on how I calculated the duration earlier, subtracting the hour from hour and minute from minute independently
* I make the calculation more accurate by using the ``get_datetime_object`` function from ``sleep_duration.py``

  .. code-block:: python

      def test_duration_when_given_hours_and_minutes(self):
          wake_hour = random.randint(0, 23)
          sleep_hour = random.randint(0, 23)
          wake_minute = random.randint(0, 59)
          sleep_minute = random.randint(0, 59)
          wake_time = f'{wake_hour}:{wake_minute}'
          sleep_time = f'{sleep_hour}:{sleep_minute}'
          self.assertEqual(
              sleep_duration.duration(wake_time, sleep_time),
              str(
                  sleep_duration.get_datetime_object(wake_time)
                - sleep_duration.get_datetime_object(sleep_time)
              )
          )

* I add seconds to the expected values in ``test_duration_calculation`` so it matches the current format

  .. code-block:: python

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

  and I am green again! Lovely
* I can now remove the second return statement in the ``duration`` function in ``sleep_duration.py`` that I left to save what worked until I had a better solution

  .. code-block:: python

    def duration(wake_time, sleep_time):
        difference = (
            get_datetime_object(wake_time)
          - get_datetime_object(sleep_time)
        )
        return str(difference)

  all tests are still passing

* I remove the ``get_hour`` and ``get_minute`` :doc:`functions </functions/functions>` since they are no longer needed and all tests are still passing. It is indeed a beautiful life

----

Duration when given Earlier Wake Time Than Sleep Time
------------------------------------------------------
What happens when the ``duration`` function is given a ``wake_time`` that is earlier than a ``sleep_time``? Since the values for ``wake_time`` and ``sleep_time`` are currently random, ``test_duration_when_given_hours_and_minutes`` will randomly fail when the ``duration`` function gets a ``wake_time`` that is earlier than the ``sleep_time``

RED: make it fail
^^^^^^^^^^^^^^^^^
I add a new failing test to ``test_sleep_duration.py`` to show this

.. code-block:: python

  def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
      wake_time = "01:00"
      sleep_time = "02:00"
      self.assertEqual(
          sleep_duration.duration(wake_time, sleep_time),
          "-01:00:00"
      )

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  E    AssertionError: '-1 day, 23:00:00' != '-01:00:00'


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^^^^^^

* The ``duration`` function currently returns negative numbers when given a ``wake_time`` that is earlier than a ``sleep_time`` for example  ``'-1 day, 14:01:00'``, it accounts for a time traveling sleep scenario where you can go to sleep and wake up in the past. I wonder what mischief we could get up to, oh wait we have to watch out for Butterflies. I want to change the function to only process durations where the wake time happens after the sleep time

* I change the expected value in the test to make it pass

  .. code-block:: python

    def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
        wake_time = "01:00"
        sleep_time = "02:00"
        self.assertEqual(
            sleep_duration.duration(wake_time, sleep_time),
            '-1 day, 23:00:00'
        )

  I am green again
* I want the ``duration`` function to make a decision based on a comparison of ``wake_time`` and ``sleep_time``. When ``wake_time`` is earlier than ``sleep_time`` it should raise an :doc:`Exception </how_to/exception_handling_programs>`

  .. code-block:: python

    def duration(wake_time, sleep_time):
        wake_time = get_datetime_object(wake_time)
        sleep_time = get_datetime_object(sleep_time)
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f' than sleep_time: {sleep_time}'
            )
        else:
            return str(wake_time - sleep_time)

  the ``duration`` :doc:`function </functions/functions>` now

  - creates the ``datetime`` objects from the timestamp for ``wake_time`` and ``sleep_time``
  - checks if the ``wake_time`` is earlier than ``sleep_time``
  - returns a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ conversion of the difference between ``wake_time`` and ``sleep_time`` when ``wake_time`` is later than ``sleep_time``
  - raises a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ when ``wake_time`` is earlier than ``sleep_time`` - no more sleep time traveling

  the terminal shows a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ for ``test_duration_when_given_earlier_wake_time_than_sleep_time`` and ``test_duration_when_given_hours_and_minutes`` for the random values where ``wake_time`` is earlier than ``sleep_time`` which matches the expectation

  .. code-block:: python

    E      ValueError: wake_time: 2006-11-21 01:00:00 is earlier than sleep_time: 2006-11-21 02:00:00

* I add an :doc:`exception handler </how_to/exception_handling_programs>` using a ``try...except`` statement and a `unittest.TestCase.assertRaises <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertRaises>`_ :doc:`method </functions/functions>` to catch and confirm that the error is raised in ``test_duration_when_given_hours_and_minutes``

  .. code-block:: python

      def test_duration_when_given_hours_and_minutes(self):
          wake_hour = random.randint(0, 23)
          sleep_hour = random.randint(0, 23)
          wake_minute = random.randint(0, 59)
          sleep_minute = random.randint(0, 59)
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

  I am left with the `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ for ``test_duration_when_given_earlier_wake_time_than_sleep_time``
* I use `unittest.TestCase.assertRaises <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertRaises>`_ to catch the :doc:`exception </how_to/exception_handling_tests>`

  .. code-block:: python

      def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
          wake_time = "01:00"
          sleep_time = "02:00"
          with self.assertRaises(ValueError):
              sleep_duration.duration(wake_time, sleep_time)

  all tests are passing. Green is a beautiful color
* Congratulations! You made it this far and built a function that takes in a ``wake_time`` and ``sleep_time`` as inputs, returns the difference between the two as long as the ``wake_time`` is later than the ``sleep_time``. Though the solution works, I cheated by making it always use the same date. Time to take a break.

----

Duration when given Date and Time
-------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test to ``test_sleep_duration.py`` called ``test_duration_when_given_date_and_time`` to test the ``duration`` function with different days

.. code-block:: python

    def test_duration_when_given_date_and_time(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
        wake_minute = random.randint(0, 59)
        sleep_minute = random.randint(0, 59)
        wake_time = f'21/11/06 {wake_hour}:{wake_minute}'
        sleep_time = f'21/11/06 {sleep_hour}:{sleep_minute}'

        self.assertEqual(
            sleep_duration.duration(wake_time, sleep_time),
            str(
                sleep_duration.get_datetime_object(wake_time)
               -sleep_duration.get_datetime_object(sleep_time)
            )
        )

the terminal shows a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ similar to this

.. code-block:: python

  E      ValueError: time data '21/11/06 21/11/06 XX:XX' does not match format '%d/%m/%y %H:%M'

the timestamps I provide to the ``duration`` function as inputs do not match the expected format of ``%d/%m/%y %H:%M``

I get a repetition of the date portion because I added a date to the timestamp in the ``get_datetime_object`` to make it match the pattern

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I remove ``21/11/06`` from the string in ``get_datetime_object`` in ``sleep_duration.py``

  .. code-block:: python

    def get_datetime_object(timestamp):
        return datetime.datetime.strptime(timestamp, "%d/%m/%y %H:%M")

  the terminal shows a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ for ``test_duration_calculation`` because it no longer matches the expected timestamp format, it is missing the date portion
* I add a date to ``wake_time`` and ``sleep_time`` in ``test_duration_calculation`` to make it match the expected inputs for ``get_datetime_object``

  .. code-block:: python

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

  all the tests pass, though I have a few cases that are not raising errors because I am catching any `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ with the ``try...except`` block in ``test_duration_when_given_hours_and_minutes`` and the ``self.assertRaises`` in ``test_duration_when_given_earlier_wake_time_than_sleep_time``
* I change the ``self.assertRaises`` in ``test_duration_when_given_earlier_wake_time_than_sleep_time`` to catch the specific failure I expect using `unittest.TestCase.assertRaisesRegex <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertRaisesRegex>`_ which takes in as input an expected exception and the message it returns

  .. code-block:: python

      def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
          wake_time = "01:00"
          sleep_time = "02:00"
          with self.assertRaisesRegex(
              ValueError,
              f'wake_time: {wake_time} is earlier than sleep_time:'
              f'{sleep_time}'
          ):
              sleep_duration.duration(wake_time, sleep_time)

  the terminal responds with an :doc:`/exceptions/AssertionError` because the message raised by the `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ is different from what I expect

  .. code-block:: python

    ValueError: time data '01:00' does not match format '%d/%m/%y %H:%M'

    During handling of the above exception, another exception occurred:

    self = <tests.test_sleep_duration.TestSleepDuration testMethod=test_duration_when_given_earlier_wake_time_than_sleep_time>

        def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
            wake_time = "01:00"
            sleep_time = "02:00"
    >       with self.assertRaisesRegex(
                ValueError,
                f'wake_time: {wake_time} is earlier than sleep_time:'
                f'{sleep_time}'
            ):
    E      AssertionError: "wake_time: 01:00 is earlier than sleep_time: 02:00" does not match "time data '01:00' does not match format '%d/%m/%y %H:%M'"

  at the top of the error I see the failure details and the actual message returned by the `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_

  .. code-block:: python

    ValueError: time data '01:00' does not match format '%d/%m/%y %H:%M'

  the timestamp provided to the ``duration`` function does not match the expected format of ``day/month/year hour:minute``

* I change the ``wake_time`` and ``sleep_time`` variables to include a year

  .. code-block:: python

    def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
        wake_time = "21/11/06 01:00"
        sleep_time = "21/11/06 02:00"
        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: {wake_time} is earlier than sleep_time:'
            f'{sleep_time}'
        ):
            sleep_duration.duration(wake_time, sleep_time)

  the terminal still shows an :doc:`/exceptions/AssertionError` this time with a message showing the returned values from the ``get_datetime_object`` function do not match the values from the tests. The date formats do not match
* I change the test using the ``get_datetime_object`` function to display the correct timestamps in the message for the `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_

  .. code-block:: python

    def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
        wake_time = "21/11/06 01:00"
        sleep_time = "21/11/06 02:00"
        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: {sleep_duration.get_datetime_object(wake_time)} '
            'is earlier than sleep_time: '
            f'{sleep_duration.get_datetime_object(sleep_time)}'
        ):
            sleep_duration.duration(wake_time, sleep_time)

  all tests are passing again, the test is very specific for the case when ``wake_time`` is earlier than ``sleep_time`` and the ``duration`` function raises a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ with a specific message
* I change the ``self.assertRaises(ValueError)`` statement in ``test_duration_when_given_hours_and_minutes`` to match what I did in ``test_duration_when_given_earlier_wake_time_than_sleep_time``

  .. code-block:: python

    def test_duration_when_given_hours_and_minutes(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
        wake_minute = random.randint(0, 59)
        sleep_minute = random.randint(0, 59)
        wake_time = f'{wake_hour}:{wake_minute}'
        sleep_time = f'{sleep_hour}:{sleep_minute}'
        try:
              self.assertEqual(
                  sleep_duration.duration(wake_time, sleep_time),
                  str(sleep_duration.get_datetime_object(wake_time)-sleep_duration.get_datetime_object(sleep_time))
              )
        except ValueError:
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: {sleep_duration.get_datetime_object(wake_time)} '
                'is earlier than sleep_time: '
                f'{sleep_duration.get_datetime_object(sleep_time)}'
            ):
                sleep_duration.duration(wake_time, sleep_time)

  the terminal displays a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ about the timestamp not matching the expected format for `datetime.datetime.strptime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime.strptime>`_

  .. code-block:: python

    E      ValueError: time data '15:10' does not match format '%d/%m/%y %H:%M'

* I add a date to the ``wake_time`` and ``sleep_time`` variables

  .. code-block:: python

    def test_duration_when_given_hours_and_minutes(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
        wake_minute = random.randint(0, 59)
        sleep_minute = random.randint(0, 59)
        wake_time = f'21/11/06 {wake_hour}:{wake_minute}'
        sleep_time = f'21/11/06 {sleep_hour}:{sleep_minute}'
        try:
              self.assertEqual(
                  sleep_duration.duration(wake_time, sleep_time),
                  str(sleep_duration.get_datetime_object(wake_time)-sleep_duration.get_datetime_object(sleep_time))
              )
        except ValueError:
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: {sleep_duration.get_datetime_object(wake_time)} '
                'is earlier than sleep_time: '
                f'{sleep_duration.get_datetime_object(sleep_time)}'
            ):
                sleep_duration.duration(wake_time, sleep_time)

* the terminal will show random `ValueErrors <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ for ``test_duration_when_given_date_and_time`` because the dates are the same, there are random ``wake_time`` values that will be earlier than ``sleep_time``. I update them test by changing the value for the day

  .. code-block:: python

    def test_duration_when_given_date_and_time(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
        wake_minute = random.randint(0, 59)
        sleep_minute = random.randint(0, 59)
        wake_time = f'22/11/06 {wake_hour}:{wake_minute}'
        sleep_time = f'21/11/06 {sleep_hour}:{sleep_minute}'

        self.assertEqual(
            sleep_duration.duration(wake_time, sleep_time),
            str(
                sleep_duration.get_datetime_object(wake_time)
               -sleep_duration.get_datetime_object(sleep_time)
            )
        )

  and the test passes. We are green again! `Celebrate Good Times! <https://youtu.be/3GwjfUFyY6M?si=MItahCf7GJ--ydvv>`_

Clean up
---------

* ``test_duration_when_given_date_and_time`` looks like a duplicate of ``test_duration_when_given_hours_and_minutes``, it has the exact same variable assignment setup with the exact same test, it is only missing the ``try...except`` block, which means I can remove ``test_duration_when_given_date_and_time``

* ``test_duration_calculation`` gives specific timestamps of ``3:30`` for ``wake_time`` and ``2:59`` for ``sleep_time``, while ``test_duration_when_given_hours_and_minutes`` uses random timestamps from ``0:00`` to ``23:59`` for those variables. Since the random variables show every timestamp in a given day I can remove ``test_duration_calculation``

* The same argument could be made for ``test_duration_when_given_earlier_wake_time_than_sleep_time`` since I have a ``try...except`` block with a ``assertRaisesRegex`` that catches the random timestamps where ``wake_time`` is earlier than ``sleep_time`` I can remove ``test_duration_when_given_earlier_wake_time_than_sleep_time``

* I also need a more descriptive name for ``test_duration_when_given_hours_and_minutes`` I could rename it to ``test_duration_when_given_a_timestamp`` or ``test_duration_when_given_date_and_time``, the choice is yours programmer.

Review
-------

The challenge was to create a function that calculates the difference between two given timestamps.

To make it happen I learned


* how to convert a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ to an `integer <https://docs.python.org/3/library/functions.html#int>`_
* how to split a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ into a :doc:`list </data_structures/lists>` using a given delimiter/separator
* how to index a :doc:`list </data_structures/lists>` to get specific elements
* how to convert a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ to a `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ object using the `datetime.datetime.strptime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime.strptime>`_ method
* how to convert a `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ object to a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* how to subtract two `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ objects
* how to convert a `datetime.timedelta <https://docs.python.org/3/library/datetime.html?highlight=datetime#timedelta-objects>`_ object to a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* how to use `unittest.TestCase.assertRaisesRegex <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertRaisesRegex>`_ to catch a specific exception and message
* how to view the :doc:`methods </functions/functions>` and ``attributes`` of a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ object
* how to generate a random integer between two given integers using `random.randint <https://docs.python.org/3/library/random.html?highlight=random#random.randint>`_
* how to use the `help <https://docs.python.org/3/library/functions.html?highlight=dir#help>`_ system to view documentation


Homework
----------

Since this chapter has not been long enough, if you want to do more

* try playing with the timestamp format and pattern in ``get_datetime_object``

  What would you change in ``"%d/%m/%y %H:%M"`` to make it accept dates in a different format? for example  ``2006/11/21`` or ``11/21/2006``
* Can you randomize the values for the days in a month?
* Can you randomize the values for the months in a year?

:doc:`/code/code_sleep_duration`