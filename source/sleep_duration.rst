
How to measure sleep duration
=============================

Let us take a look at building a program which gives us the amount of time I have been asleep based on a given sleep, wake time and dates to give an accurate result.

Prerequisites
-------------

:doc:`How to Setup a Test Driven Development Environment <setup_tdd_environment>` with ``sleep_duration`` as the project name

----

Duration when given hours only
------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

write a failing test in ``test_sleep_duration.py``

.. code-block:: python

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


* add an import statement for the missing name

  .. code-block:: python

  import sleep_duration
  import unittest

  class TestSleepDuration(unittest.TestCase):


  the terminal shows an :doc:`AttributeError` since I do not have a definition for ``duration`` in `sleep_duration.py`


* I add the error to the list of exceptions encountered

  .. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # NameError
  # AttributeError

* add a name to ``sleep_duration.py`` and the terminal displays a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

  duration

* make ``duration`` a variable by assigning it to the null value :doc:`None <data_structures_none>`

  .. code-block:: python

  duration = None

  the terminal outputs a :doc:`TypeError` because :doc:`None <data_structures_none>` is not callable
* I add the exception to the running list

  .. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # NameError
  # AttributeError
  # TypeError

* define ``duration`` as a function

  .. code-block:: python

  def duration():
    return None

  the :doc:`TypeError` remains but with a different message about the first argument passed in from the test

* change the definition of ``duration`` to accept the required keyword argument

  .. code-block:: python

   def duration(wake_time):
     return None

  the terminal outputs a similar message as before, this time for the second keyword argument

* I change the definition the same way

  .. code-block:: python

   def duration(wake_time, sleep_time):
    return None

  the terminal now shows an :doc:`/AssertionError` since the duration function returns :doc:`None <data_structures_none>` and the test expects ``1`` as the duration when a sleep time of ``07:00`` and a wake time of ``08:00`` is given

* change the return value for the duration function to the expectation

  .. code-block:: python

   def duration(wake_time, sleep_time):
    return 1

 GREEN! all tests are passing

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

The function currently returns ``1`` regardless of the inputs given but for it to be useful it has to calculate the difference between the wake time and the sleep time. It would be a large effort to write a test case for every permutation of sleep and wake times.

What if I write a test that uses a random variable for the sleep and wake times? If you have done the `Create a Calculator using Test Drive Development <./calculator.rst>`_ then you already know how to implement this solution


* add an import statement for the ``random`` library to ``test_sleep_duration.py``

  .. code-block:: python

   import random
   import sleep_duration
   import unittest

* add a new test with random values

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

  here I use a random integer from 0 to 23 as the hours for sleep and wake time and interpolate them in the strings I use as inputs, this means the wake and sleep time will randomly vary from ``00:00`` to ``23:00``

* the terminal still shows the test is passing because the expected value is ``1``, I need to change it to match the true expectation, which is that it should be the duration between ``wake_time`` and ``sleep_time``. Change the expected value in the test to be a calculation

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

  now I have an :doc:`/AssertionError` because ``sleep_duration.duration`` still returns ``1`` but from the test I expect the difference between ``wake_time`` and ``sleep_time``
* change the ``duration`` function in ``sleep_duration.py`` to return a difference between the ``wake_time`` and ``sleep_time``?

  .. code-block:: python

    def duration(wake_time, sleep_time):
      return wake_time - sleep_time

  the terminal outputs a :doc:`TypeError`\ , I passed in two strings and python does not have an operation defined for subtracting one string from another. I need to find a way to convert the timestamp from a string to a number. I know that the two inputs are currently in the format ``XX:00``, if I can parse the string to get the first two characters and convert those digits to a number I should be able to get the calculation
* to find out what options are available to us, look at the ``methods`` and ``attributes`` of strings by adding a failing test to ``test_sleep_duration.py``, this time using the ``dir`` function

  .. code-block:: python

    def test_string_methods_and_attributes(self):
      self.assertEqual(
        dir("00:00"),
        None
      )

  an :doc:`/AssertionError` is raised

  .. code-block:: python

  E    AssertionError: ['__add__', '__class__', '__contains__', [918 chars]ill'] != None

* copy the value on the left side of the comparison and replace :doc:`None <data_structures_none>` as the expected value in the test

  .. code-block:: python

      def test_string_methods_and_attributes(self):
       self.assertEqual(
         dir("00:00"),
         ['__add__', '__class__', '__contains__', [918 chars]ill']
       )

  the terminal shows a ``SyntaxError``

  .. code-block:: python

    E    ['__add__', '__class__', '__contains__', [918 chars]ill']
    E                        ^
    E  SyntaxError: invalid syntax

  ah, there is a closing quote, with no open quote, add an opening quote

  .. code-block:: python

  def test_string_methods_and_attributes(self):
    self.assertEqual(
      dir("00:00"),
      ['__add__', '__class__', '__contains__', '[918 chars]ill']
    )

  I still have an :doc:`/AssertionError` but with a different message and a suggestion

  .. code-block:: python

   E      Diff is 1265 characters long. Set self.maxDiff to None to see it.

* What if I try the suggestion?

  .. code-block:: python

   def test_string_methods_and_attributes(self):
    self.maxDiff = None
    self.assertEqual(
      dir("00:00"),
      ['__add__', '__class__', '__contains__', '[918 chars]ill']
    )

  ``maxDiff`` sets a limit on the number of characters the terminal outputs for a difference between two objects, there is no limit when it is set to None. I now see a full list of all the attributes of a string ``"00:00"``

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

* the terminal displays a :doc:`TypeError` because python does not support subtracting one string from another

  .. code-block:: python

    wake_time = '7:00', sleep_time = '21:00'

      def duration(wake_time, sleep_time):
    >    return wake_time - sleep_time
    E    TypeError: unsupported operand type(s) for -: 'str' and 'str'

  I am now at a point where I get the two random values passed in and are trying to do a calculation, but because both values are strings, the calculation does not work. I need to find a way to convert the strings to numbers

* What if I try one of the :doc:`methods <functions>` listed from ``test_string_methods_and_attributes`` to see if one of them might get us closer to a solution? Going with just the names of :doc:`methods <functions>` and attributes might not be enough since I do not know what they do, let us take a look at the documentation for extra details. Add a failing test with the ``help`` keyword to see documentation about `strings <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_

  .. code-block:: python

   self.assertEqual(
    help("00:00"),
   )

  the terminal outputs documentation for the string, I scroll through reading through the descriptions for each :doc:`method <functions>` until I see one that looks like it can solve the problem

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

  the ``split`` :doc:`method <functions>` looks like a good solution since it splits up a word when given a delimeter

* remove the failing test and replace it with one for the ``split`` method

  .. code-block:: python

      def test_string_split_method(self):
       self.assertEqual(
         "00:00".split(),
         None
       )

  the terminal shows us that split creates a list when given a string

  .. code-block:: python

    E    AssertionError: ['00:00'] != None

  I change the expectation from :doc:`None <data_structures_none>` and the test passes with the terminal showing us the :doc:`TypeError` that took us down this path

  .. code-block:: python

   E    TypeError: unsupported operand type(s) for -: 'str' and 'str'

* but what I want is to split the string on a ``delimiter`` so I get the separate parts, something like ``["00", "00"]``, using ``:`` as the delimeter. change the test to reflect the desires

  .. code-block:: python

  def test_string_split_method(self):
    self.assertEqual(
      "00:00".split(),
      ['00', '00']
    )

  the terminal shows an :doc:`/AssertionError`\ , the use of the ``split`` :doc:`method <functions>` has not yet given us what I want. Looking back at the documentation, the definition for ``split`` takes in ``self, /, sep=None, maxsplit=-1`` and ``sep`` is the delimiter
* change the test by passing in ``:`` as the delimiter

  .. code-block:: python

   def test_string_split_method(self):
     self.assertEqual(
       "00:00".split(':'),
       ['00', '00']
     )

  the test passes and I now know how to get the first part of the wake and sleep times

* What if I try using what I know so far to solve this problem? Edit the definition of the ``duration`` function in ``sleep_duration.py``

  .. code-block:: python

   def duration(wake_time, sleep_time):
     return wake_time.split(':') - sleep_time.split(':')

  the terminal still shows a :doc:`TypeError`\ , this time for trying to subtract a list from a list

  .. code-block:: python

    E    TypeError: unsupported operand type(s) for -: 'list' and 'list'

  Since I only need the first part of the list, I can get the specific item by using its index. Python uses zero-based indexing so the first item is at index 0 and the second item at 1, add a test to understand this
* add a failing test to ``test_string_split_method``

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

  the terminal shows us an :doc:`/AssertionError` because the first item (item zero) from splitting ``"12:34"`` on the delimiter ``:`` is ``"12"``, good, I am closer to what I want
* change the expected value in the test to match the value in the terminal

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

  the terminal shows another :doc:`/AssertionError`\ , this time to confirm that the second item (item one) from splitting ``"12:34"`` on the delimiter ``:`` is ``"34"``, I am not dealing with this part yet but I can assume I would use it soon, change the expected value in the same way and the test passes bringing us back to the unsolved :doc:`TypeError`
* using what I know, how to ``split`` a string on a delimiter :doc:`method <functions>` and how to index a list, change the duration function to only return the subtraction of the first parts of ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def duration(wake_time, sleep_time):
      return wake_time.split(':')[0] - sleep_time.split(':')[0]

  the terminal still outputs to show a :doc:`TypeError` for an unsupported operation of trying to subtract a string from another, and though it is not obvious here, the strings being subtracted are the values to the left of the delimiter ``:`` not the entire string value of ``wake_time`` and ``sleep_time`` i.e. for a given wake_time of "02:00" and a given sleep_time of "01:00" the program is currently trying to subtract "01" from "02"
* I now have the task of converting the string to a number so I can do the subtraction, for this I use the ``int`` keyword which returns an integer for a given value. I should add a test to see how it works, change ``test_sleep_duration.py`` and comment out the current failing test

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

  the terminal shows an :doc:`/AssertionError` since ``12 != 0``, I change the test and it shows passing tests

  .. code-block:: python

      def test_converting_a_string_to_an_integer(self):
       self.assertEqual(int("12"), 12)

  I now have another tool to use to solve the problem

* after uncommenting the commented test, I am back to the :doc:`TypeError` I have been trying to solve. I change the duration function with the knowledge to see if it makes the test pass

  .. code-block:: python

    def duration(wake_time, sleep_time):
      return int(wake_time.split(':')[0]) - int(sleep_time.split(':')[0])

  EUREKA! I am green, with a way to randomly test if the duration function can calculate the sleep duration given any random ``sleep`` and ``wake`` time.
* You could also write the solution I have in a way that explains what is happening to someone who does not know how to index a list or use ``int`` or\ ``split``. Let's try adding some variables

  .. code-block:: python

    def duration(wake_time, sleep_time):
      wake_time_split = wake_time.split(':')
      wake_time_hour = wake_time_split[0]
      wake_time_hour_integer = int(wake_time_hour)
      return wake_time_hour_integer - int(sleep_time.split(':')[0])

  the terminal shows all tests are still passing. The refactor I wrote works. After doing the same thing for ``sleep_time``, I still have passing tests
* there is a repetition in the function, for each string given we
  * split the string on the delimiter ``:``
  * get the first(0th) value from the split
  * convert first value from the split to an integer
  I could abstract that out to a function and call the function for each value

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

  the terminal still shows passing tests
* I could also rewrite it to use one line

  .. code-block:: python

    def get_hour(value):
      return int(value.split(':')[0])

  the terminal still shows passing tests. Since I am green you can try any ideas you have until you understand what I have written so far.

Duration when given hours and minutes
-------------------------------------

I found a solution that provides the right duration when given sleep time and wake time in a given day. the solution does not take into account minutes in the calculation

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

the terminal shows an :doc:`/AssertionError` the expected value is now a string that contains the subtraction of the sleep hour from the wake hour, separated by a delimiter ``:`` and the subtraction of the sleep minute from the wake minute, so if I have a wake_time of ``08:30`` and a sleep_time of ``07:11`` I should have ``1:19`` as the output

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* change the output of the ``duration`` function in ``sleep_duration.py`` to match the format of the expected value

  .. code-block:: python

    def duration(wake_time, sleep_time):
      return f'{get_hour(wake_time)-get_hour(sleep_time)}:{wake_time-sleep_time}'

  I get a :doc:`TypeError` because I just tried to subtract one string from another
* I change the second part of the timestamp to use the ``get_hour`` function

  .. code-block:: python

    def duration(wake_time, sleep_time):
      return f'{get_hour(wake_time)-get_hour(sleep_time)}:{get_hour(wake_time)-get_hour(sleep_time)}'

  the terminal now shows an :doc:`/AssertionError` because the difference in minutes is not yet calculated

* let us use the ``get_hour`` function to create a similar function which gets the minutes from a given timestamp

  .. code-block:: python

    def get_hour(value):
      return int(value.split(':')[0])

    def get_minute(value):
      return int(value.split(':')[1])

    def duration(wake_time, sleep_time):
      return f'{get_hour(wake_time)-get_hour(sleep_time)}:{get_hour(wake_time)-get_hour(sleep_time)}'

  the terminal still shows an :doc:`/AssertionError`

* after I change the ``duration`` function with a call to the new ``get_minute`` function, the test passes

  .. code-block:: python

    def get_hour(value):
      return int(value.split(':')[0])

    def get_minute(value):
      return int(value.split(':')[1])

    def duration(wake_time, sleep_time):
      return f'{get_hour(wake_time)-get_hour(sleep_time)}:{get_minute(wake_time)-get_minute(sleep_time)}'

  the terminal now reveals a failure for ``test_duration_when_given_hours_only`` which passed earlier, I introduced a regression when I changed the format of the output of ``duration`` function from a number to a string

* considering what I know so far, I can use a string to represent a duration as it allows us to express hours and minutes. Let us change ``test_duration_when_given_hours_only``  where I supplied only hours to expect a string instead of a number

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

  I get an :doc:`/AssertionError` in the terminal because I have two zeros ``:00`` in the expected return value but the duration function returns ``0`` for the minute side of the timestamp after doing a subtraction, which means ``00`` minus ``00`` is ``0`` not ``00``.

  I could change the right side of the expected value to ``0`` to make it pass, but that would not be necessary because ``test_duration_when_given_hours_and_minutes`` already covers the cases where the minutes are zero since the test uses a random number from ``0`` to ``23`` for hours and a random number from ``0`` to ``59`` for minutes.

* delete ``test_duration_when_given_hours_only`` since I no longer need it and the terminal shows passing tests

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

The ``duration`` function currently returns a subtraction of hours and a subtraction of minutes but is not accurate for calculating real differences in time. For instance if you give a wake time of ``3:30`` and a sleep time of ``2:59`` it will give us ``1:-29`` which is not a real duration instead of ``0:31`` which is the actual duration.

This means that even though the tests are passing, once again the ``duration`` function does not meet the requirement of calculating the duration between two timestamps. I need a better way.


* add a new test to ``test_sleep_duration.py``

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

  the terminal shows an :doc:`/AssertionError` since ``1:-29`` is not equal to ``0:31``

* after doing a search in the python documentation for `time difference <https://docs.python.org/3/search.html?q=time+difference>`_ on https://docs.python.org/3/search.html, select the `datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#module-datetime>`_ library since it looks like it has a solution for the problem. Reading through the available types in the module I come upon

  .. code-block:: python

  class datetime.timedelta
    A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.

  This looks exactly like what I am trying to achieve. I just need to know how to create ``datetime`` instances, which is also listed in the available types right above ``datetime.timedelta``

  .. code-block:: python

  class datetime.datetime
    A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.

  I can take a look at the examples in the documentation and then add tests using the examples

  * `Examples of usage datetime objects <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_
  * `Examples of usage timedelta objects <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-timedelta>`_

* change ``test_sleep_duration.py`` with a test for a ``datetime`` object

  .. code-block:: python

  def test_datetime_objects(self):
    self.assertEqual(
      datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
      ""
    )

  Once again I have to comment out ``test_duration_calculation`` for a short time, to see the results of the test I just added. The terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ because ``datetime`` is not defined in ``test_sleep_duration.py``, I need to import it

* add an ``import`` statement for the ``datetime`` library

  .. code-block:: python

  import datetime
  import random
  import sleep_duration
  import unittest

  the terminal displays an :doc:`/AssertionError`

  .. code-block:: python

  E    AssertionError: datetime.datetime(2006, 11, 21, 16, 30) != ''

* copy the value on the left side of the equation to replace the expected value in the test

  .. code-block:: python

  def test_datetime_objects(self):
    self.assertEqual(
      datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
      datetime.datetime(2006, 11, 21, 16, 30)
    )

  from the results I can make the following conclusions about ``datetime`` objects from the ``datetime`` library.

  * ``datetime.datetime`` takes ``year``, ``month``, ``date``, ``hours`` and ``minutes`` as inputs
  * ``datetime.datetime.strptime`` takes a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ and ``pattern`` as inputs
  * when I use ``strptime`` it returns a ``datetime.datetime`` object
  * I also notice from the pattern provided that

  - ``%d`` means day
  - ``%m`` means month
  - ``%y`` means a 2 digit year
  - ``%H`` means hour
  - ``%M`` means minute

* add a test for ``timedelta`` to test subtracting two datetime objects

  .. code-block:: python

  def test_subtracting_datetime_objects(self):
    sleep_time = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
    wake_time = datetime.datetime.strptime("21/11/06 17:30", "%d/%m/%y %H:%M")
    self.assertEqual(wake_time-sleep_time, 1)

  I get an [AssertionError] in the terminal

  .. code-block:: python

  E    AssertionError: datetime.timedelta(seconds=3600) != 1

* copy the value on the left of the equation and replace the expected value in the test

  .. code-block:: python

  def test_subtracting_datetime_objects(self):
    sleep_time = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
    wake_time = datetime.datetime.strptime("21/11/06 17:30", "%d/%m/%y %H:%M")
    self.assertEqual(
      wake_time-sleep_time,
      datetime.timedelta(seconds=3600)
    )

  I have passing tests and now have a way to convert a string to a datetime object that I can perform subtraction operations on.

* So far the ``timedelta`` object I get shows seconds, but I wanted the result as a string. Let us try changing it to a string using the `str <https://docs.python.org/3/library/stdtypes.html#str>`_ keyword by adding a new test

  .. code-block:: python

  def test_converting_timedelta_to_string(self):
    self.assertEqual(
      str(datetime.timedelta(seconds=3600)),
      ''
    )

  and I get an :doc:`/AssertionError` that looks more like what I am expecting

  .. code-block:: python

  E    AssertionError: '1:00:00' != ''

* change the expected value in the test to match the expected value in the terminal output

  .. code-block:: python

   def test_converting_timedelta_to_string(self):
    self.assertEqual(
      str(datetime.timedelta(seconds=3600)),
      '1:00:00'
    )

  it looks like calling `str <https://docs.python.org/3/library/stdtypes.html#str>`_ on a ``timedelta`` object gives us the string in the format ``Hours:Minutes:Seconds``

Putting it all together
-----------------------


* uncomment ``test_duration_calculation`` and I get the :doc:`/AssertionError` I had before
* add a function called ``get_datetime_object`` to use for converting timestamps in the format I want in ``sleep_duration.py``

  .. code-block:: python

    def get_datetime_object(timestamp):
      return datetime.datetime.strptime(timestamp, "%d/%m/%y %H:%M")

  the error remains the same since I have not called the new function

* add a new return statement to the ``duration`` function with a call to the ``get_datetime_object``

  .. code-block:: python

  def duration(wake_time, sleep_time):
   return get_datetime_object(wake_time) - get_datetime_object(sleep_time)
   return f'{get_hour(wake_time)-get_hour(sleep_time)}:{get_minute(wake_time)-get_minute(sleep_time)}'

  the terminal displays a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

  E    NameError: name 'datetime' is not defined

  I encountered this earlier when testing the ``datetime`` library

* change ``sleep_duration.py`` with an import statement at the beginning of the filoe

  .. code-block:: python
    import datetime

  the terminal now shows a ``ValueError`` since the ``timestamp`` I give the ``strptime`` function in does not match the pattern I provided as the second option, I need to have a date as part of the pattern like the example since

  .. code-block:: python
    E      ValueError: time data '10:57' does not match format '%d/%m/%y %H:%M'

* I add the new exception to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* to make the test pass for now I will fix the date to the same day in the ``get_datetime_object``

  .. code-block:: python

    def get_datetime_object(timestamp):
      return datetime.datetime.strptime(f'21/11/06 {timestamp}', "%d/%m/%y %H:%M")

  the terminal now shows an :doc:`/AssertionError` because the function is currently returning a ``datetime`` object not a string
* change the return in the ``duration`` function to return a string

  .. code-block:: python

    def duration(wake_time, sleep_time):
      difference = get_datetime_object(wake_time) - get_datetime_object(sleep_time)
      return str(difference)
      return f'{get_hour(wake_time)-get_hour(sleep_time)}:{get_minute(wake_time)-get_minute(sleep_time)}'

  the terminal shows an :doc:`/AssertionError`\ , this time the values are the same except I am missing the part for seconds

  .. code-block:: python

    E    AssertionError: '14:21:00' != '14:21'

* change ``test_duration_when_given_hours_and_minutes`` to include seconds

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

  I get another :doc:`/AssertionError` in the terminal since I have not yet changed ``test_duration_calculation`` with the new format
* I will randomly get an :doc:`/AssertionError` for ``test_duration_when_given_hours_and_minutes``. Since I am using random integers for hours and minutes, there will be instances where the ``wake_hour`` is earlier than the ``sleep_hour`` leading to a negative number for example

  .. code-block:: python

    E    AssertionError: '-1 day, 14:01:00' != '-9:-59:00'

  here, the expected values are still based on the how I calculated the duration earlier, subtracting the hour from hour and minute from minute independently.
* change the calculation to be more accurate by using the ``get_datetime_object`` function from ``sleep_duration.py``

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

* edit the test to make the expected values match

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
* What if I remove the second return statement in the ``duration`` function in ``sleep_duration.py`` I left it there as a way to save what worked until confirmation that the new solution works better

  .. code-block:: python

      def duration(wake_time, sleep_time):
       difference = get_datetime_object(wake_time) - get_datetime_object(sleep_time)
       return str(difference)

  all tests are still passing

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Taking another look at the failing test I notice that the ``duration`` function returns negative numbers when given a ``wake_time`` that is earlier than a ``sleep_time`` for example  ``'-1 day, 14:01:00'``

Our ``duration`` function now accounts for a time traveling sleep scenario where you can go to sleep and wake up in the past.


* Let us add a test for it and see if I can change the function to only process durations where the wake time happens after the sleep time

  .. code-block:: python

      def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
       wake_time = "01:00"
       sleep_time = "02:00"
       self.assertEqual(
         sleep_duration.duration(wake_time, sleep_time),
         "-01:00:00"
       )

  the terminal shows an :doc:`/AssertionError`

  .. code-block:: python

    E    AssertionError: '-1 day, 23:00:00' != '-01:00:00'

* change the test to make it pass

  .. code-block:: python

      def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
       wake_time = "01:00"
       sleep_time = "02:00"
       self.assertEqual(
         sleep_duration.duration(wake_time, sleep_time),
         '-1 day, 23:00:00'
       )

  I am green again
* I want the ``duration`` function to make a decision based on a comparison of ``wake_time`` and ``sleep_time``. If ``wake_time`` is earlier than ``sleep_time`` it should raise an :doc:`exception_handling`

  .. code-block:: python

    def duration(wake_time, sleep_time):
      wake_time = get_datetime_object(wake_time)
      sleep_time = get_datetime_object(sleep_time)
      if wake_time < sleep_time:
       raise ValueError(f'wake_time: {wake_time} is earlier than sleep_time: {sleep_time}')
      else:
       return str(wake_time - sleep_time)

  * it creates the ``datetime`` objects from the timestamp for ``wake_time`` and ``sleep_time``
  * I added a condition that checks if the ``wake_time`` is earlier than ``sleep_time``
  * it returns a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ conversion of the difference between ``wake_time`` and ``sleep_time`` if ``wake_time`` is later than ``sleep_time``
  *
  it raises a ``ValueError`` if ``wake_time`` is earlier than ``sleep_time``

  the terminal shows a ``ValueError`` for ``test_duration_when_given_earlier_wake_time_than_sleep_time`` and ``test_duration_when_given_hours_and_minutes`` for the random values where ``wake_time`` is earlier than ``sleep_time`` which matches the expectation

  .. code-block:: python

    E      ValueError: wake_time: 2006-11-21 01:00:00 is earlier than sleep_time: 2006-11-21 02:00:00

* to catch the error I need to add an `Exception Handler <./EXCEPTION_HANDLING.rst>`_ using a ``try...except`` statement and a ``self.assertRaises`` :doc:`method <functions>` call to confirm that the error is raised, change ``test_duration_when_given_hours_and_minutes``

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

  I am left with the ``ValueError`` for ``test_duration_when_given_earlier_wake_time_than_sleep_time``
* change ``test_duration_when_given_earlier_wake_time_than_sleep_time`` with a ``self.assertRaises`` to catch the ``ValueError``

  .. code-block:: python

      def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
       wake_time = "01:00"
       sleep_time = "02:00"
       with self.assertRaises(ValueError):
         sleep_duration.duration(wake_time, sleep_time),

  all tests are passing, I can clean up things I no longer need
* remove ``get_hour`` and ``get_minute`` from ``sleep_duration.py``. Congratulations! You've built a function that takes in a ``wake_time`` and ``sleep_time`` as inputs and returns the difference between the two as long as the ``wake_time`` is later than the ``sleep_time``. Though the solution works I cheated by making it always use the same date. I will now proceed to change the function to accept different days

Duration when given day, hours and minutes
------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a failing test to ``test_sleep_duration.py`` called ``test_duration_when_given_date_and_time``

.. code-block:: python

    def test_duration_when_given_date_and_time(self):
      wake_hour = random.randint(0, 23)
      sleep_hour = random.randint(0, 23)
      wake_minute = random.randint(0, 59)
      sleep_minute = random.randint(0, 59)
      wake_time = f'21/11/06 {wake_hour}:{wake_minute}'
      sleep_time = f'21/11/07 {sleep_hour}:{sleep_minute}'

      self.assertEqual(
       sleep_duration.duration(wake_time, sleep_time),
       str(sleep_duration.get_datetime_object(wake_time)-sleep_duration.get_datetime_object(sleep_time))
      )

the terminal shows a ``ValueError`` similar to this

.. code-block:: python

  E      ValueError: time data '21/11/06 21/11/06 8:9' does not match format '%d/%m/%y %H:%M'

the timestamps I provide to the ``duration`` function as inputs do not match the expected format of ``%d/%m/%y %H:%M``, I get a repetition of the date portion because in the ``get_datetime_object`` I added a date to the timestamp to make it match the pattern

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* remove ``21/11/06`` from the string in ``get_datetime_object`` in ``sleep_duration.py``

  .. code-block:: python

    def get_datetime_object(timestamp):
      return datetime.datetime.strptime(timestamp, "%d/%m/%y %H:%M")

  the terminal shows a ``ValueError`` for ``test_duration_calculation`` because it no longer matches the expected timestamp format, it is missing the date portion
* add a date to ``wake_time`` and ``sleep_time`` in ``test_duration_calculation`` to make it match the expected inputs for ``get_datetime_object``

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

  all the tests pass, though I have a few cases that are not raising errors because I am catching any ``ValueError`` with the ``try...except`` block in ``test_duration_when_given_hours_and_minutes`` and the ``self.assertRaises`` in ``test_duration_when_given_earlier_wake_time_than_sleep_time``
* I change the ``self.assertRaises`` from ``test_duration_when_given_earlier_wake_time_than_sleep_time`` to catch the specific failure I expect using ``self.assertRaisesRegex`` which takes in as input an expected exception and the message it returns

  .. code-block:: python

      def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
       wake_time = "01:00"
       sleep_time = "02:00"
       with self.assertRaisesRegex(ValueError, f'wake_time: {wake_time} is earlier than sleep_time: {sleep_time}'):
         sleep_duration.duration(wake_time, sleep_time)

  the terminal responds with an :doc:`/AssertionError` because the message raised by the ``ValueError`` is different from what I expect

  .. code-block:: python

    ValueError: time data '01:00' does not match format '%d/%m/%y %H:%M'

    During handling of the above exception, another exception occurred:

    self = <tests.test_sleep_duration.TestSleepDuration testMethod=test_duration_when_given_earlier_wake_time_than_sleep_time>

      def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
       wake_time = "01:00"
       sleep_time = "02:00"
       with self.assertRaisesRegex(ValueError, f'wake_time: {wake_time} is earlier than sleep_time: {sleep_time}'):
    >      sleep_duration.duration(wake_time, sleep_time)
    E      AssertionError: "wake_time: 01:00 is earlier than sleep_time: 02:00" does not match "time data '01:00' does not match format '%d/%m/%y %H:%M'"

  at the top of the error I see the failure details I see the actual message returned by the ``ValueError``

  .. code-block:: python

    ValueError: time data '01:00' does not match format '%d/%m/%y %H:%M'

  the timestamp provided to the ``duration`` function does not match the expected format of ``day/month/year hour:minute``

* change the ``wake_time`` and ``sleep_time`` variables to include a year

  .. code-block:: python

    def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
      wake_time = "21/11/06 01:00"
      sleep_time = "21/11/06 02:00"
      with self.assertRaisesRegex(ValueError, f'wake_time: {wake_time} is earlier than sleep_time: {sleep_time}'):
       sleep_duration.duration(wake_time, sleep_time)

  the terminal still shows an :doc:`/AssertionError` this time with an changed message showing the returned values from the ``get_datetime_object`` function
* I change the test using the ``get_datetime_object`` function to display the correct timestamps in the ``ValueError`` message

  .. code-block:: python

      def test_duration_when_given_earlier_wake_time_than_sleep_time(self):
       wake_time = "21/11/06 01:00"
       sleep_time = "21/11/06 02:00"
       with self.assertRaisesRegex(ValueError, f'wake_time: {sleep_duration.get_datetime_object(wake_time)} is earlier than sleep_time: {sleep_duration.get_datetime_object(sleep_time)}'):
         sleep_duration.duration(wake_time, sleep_time)

  all tests are passing again, the test is very specific for the case when ``wake_time`` is earlier than ``sleep_time`` and displays an appropriate error message, I am left with ``test_duration_when_given_hours_and_minutes``
* change the ``self.assertRaises(ValueError)`` statement in ``test_duration_when_given_hours_and_minutes`` to match what I did in ``test_duration_when_given_earlier_wake_time_than_sleep_time``

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
         with self.assertRaisesRegex(ValueError, f'wake_time: {sleep_duration.get_datetime_object(wake_time)} is earlier than sleep_time: {sleep_duration.get_datetime_object(sleep_time)}'):
           sleep_duration.duration(wake_time, sleep_time)

  the terminal displays a ``ValueError`` about the timestamp not matching the expected format for ``strptime``

  .. code-block::

    E      ValueError: time data '15:10' does not match format '%d/%m/%y %H:%M'

* add a year to the ``wake_time`` and ``sleep_time`` variables

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
         with self.assertRaisesRegex(ValueError, f'wake_time: {sleep_duration.get_datetime_object(wake_time)} is earlier than sleep_time: {sleep_duration.get_datetime_object(sleep_time)}'):
           sleep_duration.duration(wake_time, sleep_time)

  the terminal shows all tests are passing again

Clean up
--------

* ``test_duration_when_given_day_and_time`` looks like a duplicate of ``test_duration_when_given_hours_and_minutes``, it has the exact same variable assignment setup with the exact same test, it is only missing the ``try...except`` block, which means I can remove ``test_duration_when_given_day_and_time``

* ``test_duration_calculation`` gives specific timestamps of ``3:30`` for ``wake_time`` and ``2:59`` for ``sleep_time``, while ``test_duration_when_given_hours_and_minutes`` uses random timestamps from ``0:00`` to ``23:59`` for those variables. Since the random variables cover every timestamp in a given day I can remove ``test_duration_calculation``

* The same argument could be made for ``test_duration_when_given_earlier_wake_time_than_sleep_time`` since I have a ``try...except`` block with a ``assertRaisesRegex`` that catches the random timestamps where ``wake_time`` is earlier than ``sleep_time`` I can remove ``test_duration_when_given_earlier_wake_time_than_sleep_time``

* The first test I wrote was ``test_failure`` and I no longer need it

* I also need a more descriptive name for ``test_duration_when_given_hours_and_minutes`` I could rename it to ``test_duration_when_given_a_timestamp`` or ``test_duration_when_given_date_and_time``, the choice is yours programmer.

Review
-----

Our challenge was to create a function that calculates the difference between two given timestamps and to make it happen I learned


* how to convert a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ to an `integer <https://docs.python.org/3/library/functions.html#int>`_
* how to split a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ into a :doc:`list </data_structures_lists>` using a given delimiter/separator
* how to index a :doc:`list </data_structures_lists>` to get specific elements
* how to convert a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ to a ``datetime`` object using the ``datetime.datetime.strptime`` method
* how to convert a ``datetime`` object to a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* how to subtract two ``datetime`` objects
* how to convert a ``timedelta`` to a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
* how to use ``assertRaisesRegex`` to catch a specific exception and message
* how to view the ``methods`` and ``attributes`` of a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ object
* how to generate a random integer between two given integers using ``random.randint``
* how to use the ``help`` keyword to view documentation

If you want to do more, try playing with the timestamp format and pattern in ``get_datetime_object``. What would you change in ``"%d/%m/%y %H:%M"`` to make it accept dates in a different format for example  ``2006/11/21`` or ``11/21/2006``?
