
##############################
How to measure sleep duration
##############################

In this chapter I take a look at building a program that returns the amount of time slept based on a given sleep and wake time.

****************
Prerequisites
****************

:doc:`How to create a Test Driven Development Environment </how_to/create_tdd_environment>` with ``sleep_duration`` as the project name

----

********************************
Duration when given Hours
********************************

RED: make it fail
====================

I remove ``test_failure`` since I no longer need it, and add a failing test to ``test_sleep_duration.py`` to check that when the ``duration`` :doc:`function </functions/functions>` is given a ``sleep_time`` of ``7:00`` and a ``wake_time`` of ``8:00`` it should return ``1`` as the duration, which is the difference between the two timestamps

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

the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

.. code-block:: python

  NameError: name 'sleep_duration' is not defined

GREEN: make it pass
====================

* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

* then add an import statement for the missing name

  .. code-block:: python

    import sleep_duration
    import unittest


    class TestSleepDuration(unittest.TestCase):
    ...

  and the terminal shows an :doc:`/exceptions/AttributeError`. I do not have a definition for ``duration`` in ``sleep_duration.py``

  .. code-block:: python

    AttributeError: module 'sleep_duration' has no attribute 'duration'


* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* I add a name to ``sleep_duration.py`` ::

    duration

  and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ since the name is not defined ::

      NameError: name 'duration' is not defined

* I make ``duration`` a variable by assigning it to the null value :doc:`None </data_structures/none>` ::

    duration = None

  and the terminal shows a :doc:`/exceptions/TypeError` because :doc:`None </data_structures/none>` is not callable ::

    TypeError: 'NoneType' object is not callable

* I add the exception to the list of exceptions encountered in ``test_sleep_duration.py``

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* then I define ``duration`` as a function in ``sleep_duration.py`` ::

    def duration():
        return None

  the terminal shows a :doc:`/exceptions/TypeError` with a different message about the first argument passed in from the test ::

    TypeError: duration() got an unexpected keyword argument 'wake_time'

* I change the definition of ``duration`` to accept the required keyword argument, setting its default value to :doc:`None </data_structures/none>`

  .. code-block:: python

    def duration(wake_time=None):
        return None

  the terminal shows a similar :doc:`/exceptions/TypeError` message for the second argument

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'sleep_time'

* I add the second keyword argument to the definition of the ``duration`` :doc:`function </functions/functions>`

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return None

  the terminal shows an :doc:`/exceptions/AssertionError`. The duration function returns :doc:`None </data_structures/none>` but the test expects ``1`` as the duration when a sleep time of ``07:00`` and a wake time of ``08:00`` is given

  .. code-block:: python

    AssertionError: None != 1

* I change the return value for the ``duration`` function to make it match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return 1

  and the test passes. We are green.


REFACTOR: make it better
=========================

The function currently returns ``1`` regardless of the inputs given but for it to be useful it has to calculate the difference between ``wake_time`` and ``sleep_time``

I could write a test case for every possible sleep and wake time, or  write one test that uses random variables which will cover ``00:00`` to ``23:59``

* I add an import statement for the `random <https://docs.python.org/3/library/random.html?highlight=random#module-random>`_ module to ``test_sleep_duration.py``

  .. code-block:: python

    import random
    import sleep_duration
    import unittest

* then add a new test with random values for the hours part of the timestamps

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

  I use a random integer from ``0`` to ``23`` as the hours for sleep and wake time and :doc:`interpolate </how_to/passing_values>` them in the input strings. This means the sleep and wake times will vary randomly from ``00:00`` to ``23:00`` to cover all the possible hours in a day

* the terminal still shows the test is passing because the expected value is ``1``. I change the test to match the requirement of the difference between ``wake_time`` and ``sleep_time``

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

  since ``sleep_duration.duration`` still returns ``1`` but the test expects the difference between ``wake_time`` and ``sleep_time``, the terminal shows an :doc:`/exceptions/AssertionError` similar to this

  .. code-block:: python

    AssertionError: 1 != -2

* I change the ``duration`` function in ``sleep_duration.py`` to return a difference between ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return wake_time - sleep_time

  the terminal shows a :doc:`/exceptions/TypeError`. I passed in two strings but python does not have an operation defined for subtracting one string from another

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

  I need to find a way to convert the timestamp from a string to a number.

* I know that the two inputs are currently in this format - ``XX:00``. If I can get the first two characters and convert them to a number I know I can calculate the difference since python has arithmetic definitions defined. To give me a clue about how to break the string apart or get the characters I want, I use the `dir <https://docs.python.org/3/library/functions.html?highlight=dir#dir>`_ :doc:`function </functions/functions>` to see what :doc:`methods </functions/functions>` and ``attributes`` of `strings <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ are available

  .. code-block:: python

    def test_string_methods_and_attributes(self):
        self.assertEqual(
            dir("00:00"),
            None
        )

    def test_duration_when_given_hours_only(self):
        ...

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: ['__add__', '__class__', '__contains__', [918 chars]ill'] != None

* I copy the value on the left side of the comparison and replace :doc:`None </data_structures/none>` as the expected value in the test

  .. code-block:: python

      def test_string_methods_and_attributes(self):
          self.assertEqual(
              dir("00:00"),
              ['__add__', '__class__', '__contains__', [918 chars]ill']
          )

  the terminal shows a ``SyntaxError``

  .. code-block:: python

    E       ['__add__', '__class__', '__contains__', [918 chars]ill']
    E                                                              ^
    E   SyntaxError: unterminated string literal (detected at line 11)

* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* ah, there is a closing quote, with no open quote. I add an opening quote

  .. code-block:: python

    def test_string_methods_and_attributes(self):
        self.assertEqual(
            dir("00:00"),
            ['__add__', '__class__', '__contains__', '[918 chars]ill']
        )

  and the terminal shows an :doc:`/exceptions/AssertionError` with a different message and a suggestion

  .. code-block:: python

    Diff is 1284 characters long. Set self.maxDiff to None to see it.

* I try the suggestion by adding ``self.maxDiff = None``

  .. code-block:: python

    def test_string_methods_and_attributes(self):
        self.maxDiff = None
        self.assertEqual(
          dir("00:00"),
          ['__add__', '__class__', '__contains__', '[918 chars]ill']
        )

  `unittest.TestCase.maxDiff <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.maxDiff>`_ sets a limit on the number of characters the terminal shows for a difference between two objects, there is no limit when it is set to :doc:`None </data_structures/none>`. The terminal shows a full list of all the attributes of a `string <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_

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
                  '__getstate__',
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

* the test passes and the the terminal shows the :doc:`/exceptions/TypeError` from earlier because python still does not support subtracting one string from another

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

  I need a way to convert a `string <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ to a number.

* I want to try one of the :doc:`methods </functions/functions>` listed from ``test_string_methods_and_attributes`` to see if it will get me closer to a solution, but looking at the names listed does not give me enough information since I do not know what they do. I check the `python documentation <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ for extra details by using the `help system <https://docs.python.org/3/library/functions.html?highlight=dir#help>`_

  .. code-block:: python

    def test_duration_when_given_hours_only(self):
        help(str)
        ...

  the terminal shows documentation for the `string <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ module. I scroll through reading through the descriptions for each :doc:`method </functions/functions>` until I see one that looks like it can solve my problem

  .. code-block:: python

    ...
    |
    |  split(self, /, sep=None, maxsplit=-1)
    |      Return a list of the substrings in the string, using sep as the separator string.
    |
    |        sep
    |          The separator used to split the string.
    |
    ...

  the `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_ :doc:`method </functions/functions>` looks like a good solution since it splits up a word when given a separator

* I remove the call to the help system ``help(str)`` and add a failing test for the `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_ :doc:`method </functions/functions>` to help me understand it better

  .. code-block:: python

      def test_splitting_a_string(self):
          self.assertEqual(
              "00:00".split(),
              None
          )

      def test_duration_when_given_hours_only(self):
      ...


  the terminal shows an :doc:`/exceptions/AssertionError` and I see that `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_ creates a :doc:`list </data_structures/lists>` when called

  .. code-block:: python

    AssertionError: ['00:00'] != None

  I change the expectation to make the test pass

  .. code-block:: python

    def test_splitting_a_string(self):
        self.assertEqual(
            "00:00".split(),
            ["00:00"]
        )

  and the terminal shows the :doc:`/exceptions/TypeError` that took me down this path

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

* I want to `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_ the string on a ``separator`` so I get the separate parts, something like ``["00", "00"]``, using ``:`` as the separator. I change the expectation of the test to match this idea

  .. code-block:: python

    def test_splitting_a_string(self):
        self.assertEqual(
            "00:00".split(),
            ['00', '00']
        )

  and the terminal shows an :doc:`/exceptions/AssertionError`, the use of the `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_ :doc:`method </functions/functions>` has not yet given me what I want but has brought me closer, the shapes at least look the same

  .. code-block:: python

    AssertionError: Lists differ: ['00:00'] != ['00', '00']

* Looking back at the documentation, I see that `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_ takes in ``self, /, sep=None, maxsplit=-1`` as inputs and ``sep`` is the ``separator``. I pass in ``:`` to the `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_ :doc:`method </functions/functions>` as the ``separator``

  .. code-block:: python

    def test_splitting_a_string(self):
        self.assertEqual(
            "00:00".split(':'),
            ['00', '00']
        )

  and the test passes. I now know how to get the first parts of ``wake_time`` and ``sleep_time``

* Using what I have learned so far, I change the definition of the ``duration`` function in ``sleep_duration.py``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return wake_time.split(':') - sleep_time.split(':')

  the terminal shows a :doc:`/exceptions/TypeError`, this time for trying to subtract a :doc:`list </data_structures/lists>` from a :doc:`list </data_structures/lists>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'list' and 'list'

* I only need the first part of the list and can get the specific item by using its index. Python uses zero-based indexing so the first item is at index ``0`` and the second item at index ``1``. See :doc:`/data_structures/lists/lists` for more.
  I add tests to ``test_splitting_a_string`` for getting specific parts of the :doc:`list </data_structures/lists>` created from splitting a `string <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_

  .. code-block:: python

    def test_splitting_a_string(self):
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

    def test_duration_when_given_hours_only(self):
    ...

  the terminal shows an :doc:`/exceptions/AssertionError` because the first item (item zero) from splitting ``"12:34"`` on the separator ``:`` is ``"12"`` ::

    AssertionError: '12' != 0

  this is closer to what I want
* I change the expected value in the test to match the value in the terminal

  .. code-block:: python

        self.assertEqual(
            "12:34".split(':')[0],
            "12"
        )

  the terminal shows another :doc:`/exceptions/AssertionError` ::

    AssertionError: '34' != 0

  this shows that the second item (item one) from splitting ``"12:34"`` on the separator ``':'`` is ``"34"``
* I change the expected value in the same way

  .. code-block:: python

    self.assertEqual(
        "12:34".split(':')[1],
        "34"
    )

  the tests pass, bringing me back to the unsolved :doc:`/exceptions/TypeError`

* using what I have learned, I make the ``duration`` function return the subtraction of the first parts of ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return wake_time.split(':')[0] - sleep_time.split(':')[0]

  the terminal shows a :doc:`/exceptions/TypeError` for an unsupported operation of trying to subtract one `string <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ from another, and though it is not explicit here, from ``test_splitting_a_string`` I know that the strings being subtracted are the values to the left of the separator ``:``, not the entire string value of ``wake_time`` and ``sleep_time``. For example,  if the given ``wake_time`` is ``"02:00"`` and the given ``sleep_time`` is ``"01:00"``  the program is currently trying to subtract ``"01"`` from ``"02"`` which is different from trying to subtract ``1`` from ``2``. ``"01"`` is a string and ``1`` is a number.
* The next task is to convert the string to a number so I can do the subtraction. I use the `int <https://docs.python.org/3/library/functions.html?highlight=int#int>`_ constructor which returns an integer for a given value. I comment out the current failing test and add a test to ``test_sleep_duration.py`` to show what `int <https://docs.python.org/3/library/functions.html?highlight=int#int>`_ does

  .. code-block:: python

    def test_converting_a_string_to_an_integer(self):
        self.assertEqual(int("12"), 0)

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

  the terminal shows an :doc:`/exceptions/AssertionError` since ``12 != 0`` ::

    AssertionError: 12 != 0

* I change the test to match the expectation

  .. code-block:: python

    def test_converting_a_string_to_an_integer(self):
        self.assertEqual(int("12"), 12)

  Great! I now have another tool to help solve the problem. From the tests so far I can

  - split a string on a separator
  - index a list
  - convert strings to numbers

* I uncomment the test to show the :doc:`/exceptions/TypeError` I have been trying to solve, then add the conversion using the `int <https://docs.python.org/3/library/functions.html?highlight=int#int>`_ constructor to the ``duration`` function to see if it makes the test pass

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            int(wake_time.split(':')[0])
          - int(sleep_time.split(':')[0])
        )

  YES! I am green! The ``duration`` function can calculate the sleep duration given any random ``sleep`` and ``wake`` hour. What a beautiful life!
* I can rewrite the solution I have in a way that tries to explain what is happening to someone who does not know how to index a list or use `int <https://docs.python.org/3/library/functions.html?highlight=int#int>`_  or `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time_split = wake_time.split(':')
        wake_time_hour = wake_time_split[0]
        wake_time_hour_integer = int(wake_time_hour)
        return wake_time_hour_integer - int(sleep_time.split(':')[0])

  the terminal shows all tests are still passing, so I try the same thing for ``sleep_time``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time_split = wake_time.split(':')
        wake_time_hour = wake_time_split[0]
        wake_time_hour_integer = int(wake_time_hour)

        sleep_time_split = sleep_time.split(':')
        sleep_time_hour = sleep_time_split[0]
        sleep_time_hour_integer = int(sleep_time_hour)

        return wake_time_hour_integer - sleep_time_hour_integer

* For each string given, the ``duration`` function

  - splits the string on the separator ``:``
  - gets the first item from the split
  - converts the first item from the split to an integer

  I can make these steps a separate function and call it for ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def function(timestamp):
        timestamp_split = timestamp.split(':')
        timestamp_hour = timestamp_split[0]
        timestamp_hour_integer = int(timestamp_hour)
        return timestamp_hour_integer

    def duration(wake_time=None, sleep_time=None):
        return function(wake_time) - function(sleep_time)

  since the tests are passing, I can rename ``function`` to something more descriptive like ``get_hour``

  .. code-block:: python

    def get_hour(timestamp):
        timestamp_split = timestamp.split(':')
        timestamp_hour = timestamp_split[0]
        timestamp_hour_integer = int(timestamp_hour)
        return timestamp_hour_integer

    def duration(wake_time=None, sleep_time=None):
        return get_hour(wake_time) - get_hour(sleep_time)

  all tests are still passing. I have not broken anything yet

* I can rewrite the ``get_hour`` function to use the same variable name instead of a new name for each step in the process, for example

  .. code-block:: python

    def get_hour(value):
        value = value.split(':')
        value = value[0]
        value = int(value)
        return value

  the terminal still shows passing tests
* I can also rewrite the ``get_hour`` function to use one line though it will no longer be as explicit as above

  .. code-block:: python

    def get_hour(timestamp):
        return int(timestamp.split(':')[0])

  the terminal still shows passing tests.

Since the test is green you can try any ideas you want until you understand what has been written so far. Time for a nap.

----

****************************************
Duration when given Hours and Minutes
****************************************

I have a solution that provides the right duration when given sleep time and wake time hours, though it does not take minutes into account when doing the calculation.

For the ``duration`` function to meet the requirements, it has to accept timestamps with hours and minutes for the sleep and wake times.

RED: make it fail
====================

I add a failing test in ``test_sleep_duration.py`` that takes minutes into account

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

the terminal shows an :doc:`/exceptions/AssertionError` similar to this

.. code-block:: python

  AssertionError: 4 != '4:-20'

the expected duration is now a string that contains the subtraction of the sleep hour from the wake hour, separated by a separator ``:`` and the subtraction of the sleep minute from the wake minute. For example, when I have a ``wake_time`` of ``08:30`` and a ``sleep_time`` of ``07:11``, I should have ``1:19`` as the output

GREEN: make it pass
====================

* I change the output of the ``duration`` function in ``sleep_duration.py`` to match the format of the expected value in the test

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            f'{get_hour(wake_time)-get_hour(sleep_time)}:'
            f'{wake_time-sleep_time}'
        )

  I get a :doc:`/exceptions/TypeError` because I just tried to subtract one string from another. At this point I have a long standing relationship with this error

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

* I change the second part of the returned duration to use the ``get_hour`` function

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            f'{get_hour(wake_time)-get_hour(sleep_time)}:'
            f'{get_hour(wake_time)-get_hour(sleep_time)}'
        )

  the terminal shows an :doc:`/exceptions/AssertionError` because changing the format causes an error in ``test_duration_when_given_hours_only`` which still expects a number

  .. code-block:: python

    AssertionError: '-4:-4' != -4

* I change ``test_duration_when_given_hours_only`` to use the new format

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

  the terminal shows an :doc:`/exceptions/AssertionError` similar to this

  .. code-block:: python

    AssertionError: '17:17' != '17:00'

  the ``duration`` function currently uses ``get_hour`` for hours and minutes. I need to create a function that calculates the difference between the minutes

* I use the ``get_hour`` function as a reference to create a similar function which gets the minutes from a given timestamp

  .. code-block:: python

    def get_hour(timestamp):
        return int(timestamp.split(':')[0])

    def get_minute(timestamp):
        return int(timestamp.split(':')[1])

  the terminal still shows an :doc:`/exceptions/AssertionError`

* after I add a call to the new ``get_minute`` function in the ``duration`` function

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            f'{get_hour(wake_time)-get_hour(sleep_time)}:'
            f'{get_minute(wake_time)-get_minute(sleep_time)}'
        )

  the test passes and I am left with an :doc:`/exceptions/AssertionError` for ``test_duration_when_given_hours_only``

  .. code-block:: python

    AssertionError: '-8:0' != '-8:00'

* I update ``test_duration_when_given_hours_only`` to make the test pass

  .. code-block:: python

    def test_duration_when_given_hours_only(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour}:00',
                sleep_time=f'{sleep_hour}:00'
            ),
            f'{wake_hour-sleep_hour}:0'
        )

REFACTOR: make it better
=========================

* Since ``test_duration_when_given_hours_and_minutes`` uses a random number from ``0`` to ``23`` for hours and a random number from ``0`` to ``59`` for minutes, it covers all timestamps from ``00:00`` to ``23:59``. This means ``test_duration_when_given_hours_only`` which tests hours only is no longer necessary so I remove it
* The ``duration`` function currently returns a subtraction of hours and a subtraction of minutes which is not accurate for calculating real differences between two timestamps. For instance when it is given a wake time of ``3:30`` and a sleep time of ``2:59`` it should return ``0:31`` but it returns ``1:-29`` which is not a real duration. This means that even though the tests are passing, once again the ``duration`` function does not meet the requirement of calculating the difference between two timestamps. I need a better way.
* I add a new test for the specific example to ``test_sleep_duration.py``

  .. code-block:: python

    def test_duration_calculation(self):
        self.assertEqual(
            sleep_duration.duration(
                wake_time='3:30',
                sleep_time='2:59'
            ),
            '0:31'
        )

  the terminal shows an :doc:`/exceptions/AssertionError` since ``1:-29`` is not equal to ``0:31``

  .. code-block:: python

    AssertionError: '1:-29' != '0:31'
* To calculate a difference between hours and minutes I need to do the following

  - convert timestamp to total minutes for each timestamp given by multiplying the hour by 60 and adding the minutes
  - subtract total ``wake_time`` minutes from total ``sleep_time`` minutes
  - return the difference between total ``wake_time`` minutes and total ``sleep_time`` minutes as hours and minutes
* I add these steps to the ``duration`` function keeping the original solution that has worked so far until all the tests pass

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time_minutes = (get_hour(wake_time) * 60) + get_minute(wake_time)
        sleep_time_minutes = (get_hour(sleep_time) * 60) + get_minute(sleep_time)
        difference = wake_time_minutes - sleep_time_minutes
        difference_hours = difference // 60
        difference_minutes = difference % 60
        return f'{difference_hours}:{difference_minutes}'
        return (
            f'{get_hour(wake_time)-get_hour(sleep_time)}:'
            f'{get_minute(wake_time)-get_minute(sleep_time)}'
        )

  the terminal shows passing tests but since ``test_duration_when_given_hours_and_minutes`` uses the wrong calculation it will randomly show an :doc:`/exceptions/AssertionError` similar to this

  .. code-block:: python

    AssertionError: '2:55' != '3:-5'

* I update ``test_duration_when_given_hours_and_minutes`` to use the right calculation

  .. code-block:: python

    def test_duration_when_given_hours_and_minutes(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
        wake_minute = random.randint(0, 59)
        sleep_minute = random.randint(0, 59)
        wake_time_minutes = wake_hour * 60 + wake_minute
        sleep_time_minutes = sleep_hour * 60 + sleep_minute
        difference = wake_time_minutes - sleep_time_minutes
        difference_hours = difference // 60
        difference_minutes = difference % 60
        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour}:{wake_minute}',
                sleep_time=f'{sleep_hour}:{sleep_minute}'
            ),
            f'{difference_hours}:{difference_minutes}'
        )

  and we have passing tests again

  .. NOTE::

    - the ``//`` operator returns the whole number result of diving one number by another
    - the ``%`` operator returns the remainder result of diving one number by another
* Since ``test_duration_when_given_hours_and_minutes`` covers all the timestamps from ``00:00`` to ``23:59`` and calculates a real duration, I can remove ``test_duration_calculation``
* I can also remove the second return statement from the ``duration`` function because I have a working solution that is better than the previous one
* I can also write a function to get the total minutes from a timestamp and call it in the ``duration`` function

  .. code-block:: python

    def get_total_minutes(timestamp):
        return get_hour(timestamp) * 60 + get_minute(timestamp)

    def duration(wake_time=None, sleep_time=None):
        wake_time_minutes = get_total_minutes(wake_time)
        sleep_time_minutes = get_total_minutes(sleep_time)
        difference = wake_time_minutes - sleep_time_minutes
        difference_hours = difference // 60
        difference_minutes = difference % 60
        return f'{difference_hours}:{difference_minutes}'

  the terminal shows passing tests. We are still green.

* since I only call ``wake_time_minutes`` and ``sleep_time_minutes`` when I calculate the difference, I do not need the variable names, I can do the calculation directly

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference = get_total_minutes(wake_time) - get_total_minutes(sleep_time)
        difference_hours = difference // 60
        difference_minutes = difference % 60
        return f'{difference_hours}:{difference_minutes}'

  the terminal still shows passing tests

* I can also do the same with ``difference_hours`` and ``difference_minutes``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference = (
            get_total_minutes(wake_time)
          - get_total_minutes(sleep_time)
        )
        return f'{difference // 60}:{difference % 60}'

  We are still green. Take a look at the last two blocks of code. Which do you like better?
* I can also create a function that replaces the ``get_hour`` and ``get_minute`` functions

  .. code-block:: python

    def parse_timestamp(timestamp=None, index=0):
        return int(timestamp.split(':')[index])

    def get_total_minutes(timestamp):
        return (
            (parse_timestamp(timestamp, 0) * 60)
           + parse_timestamp(timestamp, 1)
        )

********************************************************
Duration when given Earlier Wake Time than Sleep Time
********************************************************

What happens when the ``duration`` function is given a ``wake_time`` that is earlier than a ``sleep_time``?

RED: make it fail
=========================

I add a new failing test to ``test_sleep_duration.py`` to find out

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

  AssertionError: '-1:0' != '-01:00:00'


GREEN: make it pass
=========================

* The ``duration`` function currently returns negative numbers when given a ``wake_time`` that is earlier than a ``sleep_time``. It makes it possible to measure a time traveling sleep scenario where the traveler can go to sleep in the present and wake up in the past. I wonder what mischief we could get up to, but wait we have to watch out for those Butterflies. I want to change the function to only process durations where the wake time happens after the sleep time, time traveling is too complicated

* I change the expected value in the test to make it pass

  .. code-block:: python

    def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
        wake_time = "01:00"
        sleep_time = "02:00"
        self.assertEqual(
            sleep_duration.duration(wake_time, sleep_time),
            '-1:0'
        )

  I am green again
* I change the ``duration`` function to make a decision based on the difference between ``wake_time`` and ``sleep_time``. When the difference is less than ``0``, it is a negative number which means the ``wake_time`` is earlier (less) than the ``sleep_time`` and the function should raise an :doc:`Exception </how_to/exception_handling_programs>` otherwise it should return the difference between them converted to hours and minutes

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference = (
            get_total_minutes(wake_time)
          - get_total_minutes(sleep_time)
        )
        if difference < 0:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
        else:
            return f'{difference // 60}:{difference % 60}'

  the ``duration`` :doc:`function </functions/functions>`

  - calculates the difference between ``wake_time`` and ``sleep_time``
  - checks if the difference between ``wake_time`` and ``sleep_time`` is less than 0

    * raises a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ when ``wake_time`` is earlier (greater) than ``sleep_time`` - no more sleep time traveling
    * returns a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ conversion of the difference between ``wake_time`` and ``sleep_time`` when ``wake_time`` is later (less) than ``sleep_time``

  the terminal shows a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ for ``test_duration_when_given_earlier_wake_time_than_sleep_time`` and ``test_duration_when_given_hours_and_minutes`` for the random values where ``wake_time`` is earlier than ``sleep_time``

  .. code-block:: python

    ValueError: wake_time: 20:26 is earlier than sleep_time: 23:50
* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError
    # ValueError

* I use `unittest.TestCase.assertRaises <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertRaises>`_ to catch the :doc:`exception </how_to/exception_handling_tests>` in ``test_duration_when_given_earlier_wake_time_than_sleep_time``

  .. code-block:: python

    def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
        wake_time = "01:00"
        sleep_time = "02:00"
        with self.assertRaises(ValueError):
            sleep_duration.duration(wake_time, sleep_time)

  the test passes and I am left with the `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ for ``test_duration_when_given_hours_and_minutes``
* I add an :doc:`exception handler </how_to/exception_handling_programs>` using a ``try...except`` statement and a `unittest.TestCase.assertRaises <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertRaises>`_ :doc:`method </functions/functions>` to catch and confirm the `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ when it is raised in ``test_duration_when_given_hours_and_minutes``

  .. code-block:: python

    def test_duration_when_given_hours_and_minutes(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
        wake_minute = random.randint(0, 59)
        sleep_minute = random.randint(0, 59)
        wake_time_minutes = wake_hour * 60 + wake_minute
        sleep_time_minutes = sleep_hour * 60 + sleep_minute
        difference = wake_time_minutes - sleep_time_minutes
        difference_hours = difference // 60
        difference_minutes = difference % 60
        wake_time = f'{wake_hour}:{wake_minute}'
        sleep_time = f'{sleep_hour}:{sleep_minute}'
        try:
            self.assertEqual(
                sleep_duration.duration(wake_time, sleep_time),
                f'{difference_hours}:{difference_minutes}'
            )
        except ValueError:
            with self.assertRaises(ValueError):
                sleep_duration.duration(wake_time, sleep_time)

  all tests are passing. Green is a beautiful color
* I no longer need ``test_duration_when_given_earlier_wake_time_than_sleep_time`` since it is covered by ``test_duration_when_given_hours_and_minutes`` so I remove it
* Congratulations! You made it this far and built a function that

  - takes in a ``wake_time`` and ``sleep_time`` as inputs
  - returns the difference between the two when the ``wake_time`` is later (greater) than the ``sleep_time``
  - raises a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ when the ``wake_time`` is earlier (less) than the ``sleep_time``

It is time to take a break.

----

********************************************************
Duration when given Date and Time
********************************************************

So far we have dealt with timestamps that are based on hours and minutes only. The assumption has been that the timestamps occur on the same day, but I could fall asleep on a Monday and wake up on a Tuesday. How would the ``duration`` function behave when it is given different dates?

RED: make it fail
=========================

I add a failing test to ``test_sleep_duration.py`` called ``test_duration_when_given_date_and_time`` to test the ``duration`` function with different days

.. code-block:: python

    def test_duration_when_given_date_and_time(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
        wake_minute = random.randint(0, 59)
        sleep_minute = random.randint(0, 59)
        wake_time_minutes = wake_hour * 60 + wake_minute
        sleep_time_minutes = sleep_hour * 60 + sleep_minute
        difference = wake_time_minutes - sleep_time_minutes
        difference_hours = difference // 60
        difference_minutes = difference % 60
        wake_time = f'21/11/06 {wake_hour}:{wake_minute}'
        sleep_time = f'21/11/06 {sleep_hour}:{sleep_minute}'

        self.assertEqual(
            sleep_duration.duration(wake_time, sleep_time),
            f'{difference_hours}:{difference_minutes}'
        )

the terminal shows a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ because the ``parse_timestamp`` function tries to convert the string to an integer but the string is currently in the wrong format

.. code-block:: python

  ValueError: invalid literal for int() with base 10: '21/11/06 16'


GREEN: make it pass
=========================

* The ``split`` function was given a separator of ``:`` when we only used hours and minutes, but behaves differently when I use a date. I add a test to ``test_splitting_a_string`` to show this

  .. code-block:: python

    self.assertEqual(
        "21/11/06 16:40".split(':')[0],
        ''
    )

  the terminal shows an :doc:`/exceptions/AssertionError`
* I update the test with the correct values to make it pass

  .. code-block:: python

    self.assertEqual(
        "21/11/06 16:40".split(':')[0],
        '21/11/06 16'
    )

  I cannot convert a string in the format ``'21/11/06 16'`` to an integer

* I need a solution that is capable of reading the date and time. Writing one myself would require a lot of work as I would have to account for the variance in months, February has 28 days except in leap years when it has 29 days and some months have 30 days while others have 31 days

* I do a search in the `python online documentation <https://docs.python.org/3/search.html>`_ for `time difference <https://docs.python.org/3/search.html?q=time+difference>`_, and select the `datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#module-datetime>`_ module since it looks like it has a solution for this problem. Reading through the available types in the module, I see I can create `datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#module-datetime>`_ instances

  .. code-block:: python

    class datetime.datetime
      A combination of a date and a time.
      Attributes: year, month, day, hour,
      minute, second, microsecond, and tzinfo.

  I also see

  .. code-block:: python

    class datetime.timedelta
      A duration expressing the difference between
      two date, time, or datetime instances to
      microsecond resolution.

* I add tests using the examples in the documentation to help me understand how to use the `datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#module-datetime>`_ module

  * `Examples of usage datetime objects <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_
  * `Examples of usage timedelta objects <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-timedelta>`_

* I add a test for `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ objects to ``test_sleep_duration.py``

  .. code-block:: python

    def test_datetime_datetime_objects(self):
        self.assertEqual(
            datetime.datetime.strptime(
                "21/11/06 16:30",
                "%d/%m/%y %H:%M"
            ),
            ""
        )

    def test_duration_when_given_hours_and_minutes(self):
    ...

* then comment out ``test_duration_when_given_date_and_time`` to see the results of the test I just added

  .. code-block:: python

    # def test_duration_when_given_date_and_time(self):
    #     wake_hour = random.randint(0, 23)
    #     sleep_hour = random.randint(0, 23)
    #     wake_minute = random.randint(0, 59)
    #     sleep_minute = random.randint(0, 59)
    #     wake_time_minutes = wake_hour * 60 + wake_minute
    #     sleep_time_minutes = sleep_hour * 60 + sleep_minute
    #     difference = wake_time_minutes - sleep_time_minutes
    #     difference_hours = difference // 60
    #     difference_minutes = difference % 60
    #     wake_time = f'21/11/06 {wake_hour}:{wake_minute}'
    #     sleep_time = f'21/11/06 {sleep_hour}:{sleep_minute}'

    #     self.assertEqual(
    #         sleep_duration.duration(wake_time, sleep_time),
    #         f'{difference_hours}:{difference_minutes}'
    #     )

* the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ because ``datetime`` is not defined in ``test_sleep_duration.py``. I need to import it

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

* I add an ``import`` statement for the `datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#module-datetime>`_ module to ``test_sleep_duration.py``

  .. code-block:: python

    import datetime
    import random
    import sleep_duration
    import unittest

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: datetime.datetime(2006, 11, 21, 16, 30) != ''

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

  and the terminal shows passing tests. From the test I see that

  - `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ takes ``year``, ``month``, ``date``, ``hours`` and ``minutes`` as inputs
  - the `datetime.datetime.strptime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime.strptime>`_ :doc:`method </functions/functions>`

    * takes 2 `strings <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ as inputs - timestamp and a pattern
    * returns a `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ object
  - from the pattern provided as input, it also looks like

    * ``%d`` is for days
    * ``%m`` is for months
    * ``%y`` is for 2 digit years
    * ``%H`` is for hours
    * ``%M`` is for minutes

* I add a test for subtracting two `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ objects

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

    def test_duration_when_given_hours_and_minutes(self):
    ...

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: datetime.timedelta(seconds=3600) != 1

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

  With these passing tests. I see that I can

  - convert a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ to a `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ object
  - subtract one `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ object from another to get a `datetime.timedelta <https://docs.python.org/3/library/datetime.html?highlight=datetime#timedelta-objects>`_ object

* So far the `datetime.timedelta <https://docs.python.org/3/library/datetime.html?highlight=datetime#timedelta-objects>`_ object I get shows seconds, but I want the result as a string. I add a test to see if I can change it to a string using the `str <https://docs.python.org/3/library/stdtypes.html#str>`_ constructor

  .. code-block:: python

    def test_converting_timedelta_to_string(self):
        self.assertEqual(
            str(datetime.timedelta(seconds=3600)),
            ''
        )

    def test_duration_when_given_hours_and_minutes(self):
    ...

  and I get an :doc:`/exceptions/AssertionError` with a message that looks more like what I want

  .. code-block:: python

    AssertionError: '1:00:00' != ''

* I change the expected value in the test to match the value from the terminal

  .. code-block:: python

    def test_converting_timedelta_to_string(self):
        self.assertEqual(
            str(datetime.timedelta(seconds=3600)),
            '1:00:00'
        )

  it looks like calling `str <https://docs.python.org/3/library/stdtypes.html#str>`_ on a `datetime.timedelta <https://docs.python.org/3/library/datetime.html?highlight=datetime#timedelta-objects>`_ object returns a string in the format ``Hours:Minutes:Seconds``

  From the tests so far I know that I can

  - convert a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ to a `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ object
  - subtract one `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ object from another to get a `datetime.timedelta <https://docs.python.org/3/library/datetime.html?highlight=datetime#timedelta-objects>`_ object
  - convert a `datetime.timedelta <https://docs.python.org/3/library/datetime.html?highlight=datetime#timedelta-objects>`_ object to a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_

* I uncomment ``test_duration_when_given_date_and_time`` to return to the `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ that sent me down this path
* I add a function for converting timestamps to ``sleep_duration.py`` and call it ``get_datetime_object``

  .. code-block:: python

    def get_datetime_object(timestamp):
        return datetime.datetime.strptime(
            timestamp, "%d/%m/%y %H:%M"
        )

  the error remains the same since I have not called the new function yet

* I add a new return statement to the ``duration`` function with a call to the ``get_datetime_object`` above the existing return statement because I do not want to remove what has worked so far until I have a new working solution. Python does not execute anything in a function after a ``return`` statement so the second return statement is never run

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference = (
            get_datetime_object(wake_time)
          - get_datetime_object(sleep_time)
        )
        return str(difference)
        difference = (
            get_total_minutes(wake_time)
          - get_total_minutes(sleep_time)
        )
        if difference < 0:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
        else:
            return f'{difference // 60}:{difference % 60}'

  the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

  I encountered this earlier when testing the `datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime>`_ module

* I add an import statement to the top of ``sleep_duration.py``

  .. code-block:: python

    import datetime

    def parse_timestamp(timestamp=None, index=0):
    ...

  the terminal shows an :doc:`/exceptions/AssertionError` similar to this

  .. code-block:: python

    AssertionError: datetime.timedelta(days=-1, seconds=84420) != '-1:27'

* I update ``test_duration_when_given_date_and_time`` to use the right format and remove unused variables

  .. code-block:: python

    def test_duration_when_given_date_and_time(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
        wake_minute = random.randint(0, 59)
        sleep_minute = random.randint(0, 59)
        wake_time = f'21/11/06 {wake_hour}:{wake_minute}'
        sleep_time = f'21/11/06 {sleep_hour}:{sleep_minute}'
        pattern = "%d/%m/%y %H:%M"
        difference = (
            datetime.datetime.strptime(wake_time, pattern)
          - datetime.datetime.strptime(sleep_time, pattern)
        )
        self.assertEqual(
            sleep_duration.duration(wake_time, sleep_time),
            str(difference)
        )

  the terminal shows passing tests
* Before I remove the second return statement in the ``duration`` function, I update the new statement to do a comparison of ``wake_time`` and ``sleep_time`` so it raises a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ when the ``wake_time`` is earlier than the ``sleep_time``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time = get_datetime_object(wake_time)
        sleep_time = get_datetime_object(sleep_time)
        if wake_time < sleep_time:
            difference = wake_time - sleep_time
            return str(difference)
        else:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
        difference = (
            get_total_minutes(wake_time)
          - get_total_minutes(sleep_time)
        )
        if difference < 0:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
        else:
            return f'{difference // 60}:{difference % 60}'

  the terminal shows a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_ similar to this for values where ``wake_time`` is earlier (less) than ``sleep_time``

  .. code-block:: python

    ValueError: wake_time: 2006-11-21 14:50:00 is earlier than sleep_time: 2006-11-21 01:58:00

  the error looks wrong. ``14:50:00`` is not earlier than ``01:58:00`` on the same day.
* I update the condition to use a greater than sign instead

  .. code-block:: python

    if wake_time > sleep_time:

  the terminal shows a `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_

  .. code-block:: python

    ValueError: wake_time: 2006-11-21 04:22:00 is earlier than sleep_time: 2006-11-21 16:30:00

  this message looks more like it - ``04:22:00`` is definitely earlier than ``16:30:00``

* I remove the statements after the return statement in the ``duration`` function since things are working the way I expect

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time = get_datetime_object(wake_time)
        sleep_time = get_datetime_object(sleep_time)
        if wake_time > sleep_time:
            difference = wake_time - sleep_time
            return str(difference)
        else:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
* I add the ``try...except`` block from ``test_duration_when_given_hours_and_minutes`` to ``test_duration_when_given_date_and_time``

  .. code-block:: python

    def test_duration_when_given_date_and_time(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
        wake_minute = random.randint(0, 59)
        sleep_minute = random.randint(0, 59)
        wake_time = f'21/11/06 {wake_hour}:{wake_minute}'
        sleep_time = f'21/11/06 {sleep_hour}:{sleep_minute}'
        pattern = "%d/%m/%y %H:%M"
        difference = (
            datetime.datetime.strptime(wake_time, pattern)
          - datetime.datetime.strptime(sleep_time, pattern)
        )
        try:
            self.assertEqual(
                sleep_duration.duration(wake_time, sleep_time),
                str(difference)
            )
        except ValueError:
            with self.assertRaises(ValueError):
                sleep_duration.duration(wake_time, sleep_time)

  All tests are passing. I am green

REFACTOR: make it better
=========================

* I remove ``parse_timestamp`` and ``get_total_minutes`` from ``sleep_duration.py`` since I no longer need them
* I can remove the ``difference`` variable from the ``duration`` function since it is only called once

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time = get_datetime_object(wake_time)
        sleep_time = get_datetime_object(sleep_time)
        if wake_time > sleep_time:
            return str(wake_time - sleep_time)
        else:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
* I remove ``test_duration_when_given_hours_and_minutes`` since ``test_duration_when_given_date_and_time`` covers the same timestamps and also includes dates
* I rename ``test_duration_when_given_date_and_time`` to ``test_duration``

*********
Review
*********

The challenge was to create a function that calculates the difference between two given timestamps.

To make it happen I had to

* convert a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ to an `integer <https://docs.python.org/3/library/functions.html#int>`_
* split a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ into a :doc:`list </data_structures/lists>` using a given separator
* index a :doc:`list </data_structures/lists>` to get specific items
* convert a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ to a `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ object using the `datetime.datetime.strptime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime.strptime>`_ method
* convert a `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ object to a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* subtract two `datetime.datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects>`_ objects
* convert a `datetime.timedelta <https://docs.python.org/3/library/datetime.html?highlight=datetime#timedelta-objects>`_ object to a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* view the :doc:`methods </functions/functions>` and ``attributes`` of a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ object
* generate a random integer between two given integers using `random.randint <https://docs.python.org/3/library/random.html?highlight=random#random.randint>`_
* use the `help system <https://docs.python.org/3/library/functions.html?highlight=dir#help>`_ to view documentation

I also encountered the following exceptions

* :doc:`/exceptions/AssertionError`
* `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_
* :doc:`/exceptions/AttributeError`
* :doc:`/exceptions/TypeError`
* `SyntaxError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#SyntaxError>`_
* `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_

************
Homework
************

Since this chapter has not been long enough, if you want to do more

* try playing with the timestamp format and pattern in ``get_datetime_object``

  What would you change in ``"%d/%m/%y %H:%M"`` to make it accept dates in a different format? for example  ``2006/11/21`` or ``11/21/2006``
* Can you randomize the values for the days in a month?
* Can you randomize the values for the months in a year?

----

:doc:`/code/code_sleep_duration`