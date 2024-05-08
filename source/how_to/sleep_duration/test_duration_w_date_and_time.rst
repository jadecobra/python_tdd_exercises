.. include:: ../../links.rst

.. _test_duration_w_date_and_time:

#################################################################################
how to measure sleep duration: test_duration_w_date_and_time
#################################################################################

This is part 4 of a program that calculates the difference between a given wake and sleep time.

.. contents:: table of contents
  :local:
  :depth: 2

----

I want to test the ``duration`` :ref:`function<functions>` with dates in the timestamps

.. _test_duration_w_date_and_time_red:

*********************************************************************************
red: make it fail
*********************************************************************************

* I make a copy of ``random_timestamp``, change the name of the copy, then add a date to the `return statement`_

  .. code-block:: python

    def random_timestamp_a():
        return (
            '31/12/99 '
            f'{random.randint(0,23):02}:'
            f'{random.randint(0,59):02}'
        )

* I also make a copy of ``test_duration_w_hours_and_minutes`` and change the name to ``test_duration_w_date_and_time``
* then add calls to ``random_timestamp_a``

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        sleep_time = random_timestamp_a()
        wake_time = random_timestamp_a()

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time, sleep_time
            )
            wake_time = random_timestamp_a()
        else:
            self.assertEqual(
                sleep_duration.duration(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                self.get_difference(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )
            )

  and get a ValueError_

  .. code-block:: python

    ValueError: invalid literal for int() with base 10: '31/12/99 03'
    ValueError: invalid literal for int() with base 10: '31/12/99 07'
    ValueError: invalid literal for int() with base 10: '31/12/99 11'
    ValueError: invalid literal for int() with base 10: '31/12/99 21'

  the test calls ``duration`` which calls ``read_timestamp`` that converts the timestamp string_ to a number by using the int_ constructor_ but it is in the wrong format

.. _test_duration_w_date_and_time_green_0:

*********************************************************************************
green: make it pass
*********************************************************************************

* I copy the string from the terminal
* then add the `unittest.skip decorator`_ to ``test_duration_w_date_and_time``

  .. code-block:: python

    @unittest.skip
    def test_duration_w_date_and_time(self):
    ...

* and add an assertion to ``test_converting_strings_to_numbers`` to make the error I just saw

  .. code-block:: python

    def test_converting_strings_to_numbers(self):
        self.assertEqual(int('12'), 12)
        self.assertEqual(int('01'), 1)
        int('31/12/99 01')

  the terminal shows a ValueError_ with the same message from ``test_duration_w_date_and_time``

  .. code-block:: python

    ValueError: invalid literal for int() with base 10: '31/12/99 13'

  I cannot use the int_ constructor_ to convert a timestamp string_ to a number when it has a date. I add an `assertRaises`_ to :doc:`handle</how_to/exception_handling_tests>` the ValueError_

  .. code-block:: python

    def test_converting_strings_to_numbers(self):
        self.assertEqual(int('12'), 12)
        self.assertEqual(int('01'), 1)

        with self.assertRaises(ValueError):
            int('31/12/99 01')

  and the test is green again

* I remove the `unittest.skip decorator`_ from ``test_duration_w_date_and_time`` to get back the ValueError_
* and make a copy of the ``duration`` :ref:`function<functions>` in ``sleep_duration.py``, then change the name to ``duration_a`` to keep the working solution while I try a new one
* I remove ``difference_hours``, ``difference_minutes``, ``duration_hours``, ``duration_minutes`` and ``difference`` from ``duration_a`` and change the `return statement`_

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            return None

* then change the assertion in ``test_duration_w_date_and_time`` to reference the new :ref:`function<functions>`

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        sleep_time = random_timestamp_a()
        wake_time = random_timestamp_a()

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp_a()
        else:
            self.assertEqual(
                sleep_duration.duration_a(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                self.get_difference(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )
            )

  and the terminal shows the same ValueError_

  .. code-block:: python

    ValueError: invalid literal for int() with base 10: '31/12/99 22'

  the test calls ``get_difference`` in the expectation which uses the int_ constructor_ in its calculations
* I change it to return ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        sleep_time = random_timestamp_a()
        wake_time = random_timestamp_a()

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                sleep_time=sleep_time,
                wake_time=wake_time,
            )
            wake_time = random_timestamp_a()
        else:
            self.assertEqual(
                sleep_duration.duration_a(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                (wake_time, sleep_time)
            )

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != ('31/12/99 09:52', '31/12/99 07:11')
    AssertionError: None != ('31/12/99 18:16', '31/12/99 11:21')
    AssertionError: None != ('31/12/99 13:10', '31/12/99 12:00')
    AssertionError: None != ('31/12/99 16:41', '31/12/99 12:35')

* then change the `return statement`_ in ``duration_a``

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            return (wake_time, sleep_time)

  and the test passes

.. _test_duration_w_date_and_time_refactor:

*********************************************************************************
refactor: make it better
*********************************************************************************

The int_ constructor_ will not work when the timestamps have a date. I need a solution that can read timestamps with date and time. I search for `date and time <https://docs.python.org/3/search.html?q=date+and+time>`_ in `python's online documentation`_, to see if there is an existing solution and select the datetime_ :ref:`module<ModuleNotFoundError>` from the results. Reading through the available types in the :ref:`module<ModuleNotFoundError>` I see `datetime.datetime`_ objects which are a combination of date and time

.. code-block:: python

  class datetime.datetime
    A combination of a date and a time.
      Attributes: year, month, day, hour,
      minute, second, microsecond, and tzinfo.

.. _test_datetime_objects:

test_datetime_objects
#################################################################################

.. _test_datetime_objects_red:

red: make it fail
---------------------------------------------------------------------------------

I add a test to ``test_sleep_duration.py`` from `Examples of usage: datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_ for `datetime.datetime`_ objects

.. code-block:: python

  def test_datetime_objects(self):
      self.assertEqual(
          datetime.strptime(
              "21/11/06 16:30",
              "%d/%m/%y %H:%M"
          ),
          ''
      )

  def test_duration_w_date_and_time(self):
  ...

and the terminal shows a NameError_

.. code-block:: python

  NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

.. _test_datetime_objects_green:

green: make it pass
---------------------------------------------------------------------------------

I add an `import statement`_ for the datetime_ module

.. code-block:: python

  import datetime
  import random
  import sleep_duration
  import unittest
  ...

and the terminal shows an :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'datetime' has no attribute 'strptime'

the reference to the ``strptime`` :ref:`method<functions>` is not right, my `import statement`_ is different from `the example in the documentation <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_. I add the :ref:`module<ModuleNotFoundError>` name to the call

.. code-block:: python

  def test_datetime_objects(self):
      self.assertEqual(
          datetime.datetime.strptime(
              "21/11/06 16:30",
              "%d/%m/%y %H:%M"
          ),
          ''
      )

and get an :ref:`AssertionError`

.. code-block:: python

  AssertionError: datetime.datetime(2006, 11, 21, 16, 30) != ''

I copy the value on the left side of the :ref:`AssertionError` to change the expected value in the test,

.. code-block:: python

  def test_datetime_objects(self):
      self.assertEqual(
          datetime.datetime.strptime(
              "21/11/06 16:30",
              "%d/%m/%y %H:%M"
          ),
          datetime.datetime(
              2006, 11, 21, 16, 30
          )
      )

and it passes

When the `datetime.datetime.strptime`_ :ref:`method<functions>` is given 2 strings_ as inputs - a timestamp and a pattern, it returns a `datetime.datetime`_ object based on the pattern provided. The pattern provided means

- ``%d`` is for days
- ``%m`` is for months
- ``%y`` is for 2 digit years
- ``%H`` is for hours
- ``%M`` is for minutes

there are more details in `strftime() and strptime() behavior <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior>`_

.. _test_datetime_objects_refactor:

refactor: make it better
---------------------------------------------------------------------------------

* I add calls to the `datetime.datetime.strptime`_ :ref:`method` in ``test_duration_w_date_and_time``

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        sleep_time = random_timestamp_a()
        wake_time = random_timestamp_a()

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp_a()
        else:
            self.assertEqual(
                sleep_duration.duration_a(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                (
                    datetime.datetime.strptime(
                        wake_time,
                        '%d/%m/%y %H:%M'
                    ),
                    datetime.datetime.strptime(
                        sleep_time,
                        '%d/%m/%y %H:%M'
                    )
                )
            )

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ('31/12/99 07:20', '31/12/99 03:08') != (datetime.datetime(1999, 12, 31, 7, 20), datetime.datetime(1999, 12, 31, 3, 8))
    AssertionError: Tuples differ: ('31/12/99 15:01', '31/12/99 00:37') != (datetime.datetime(1999, 12, 31, 15, 1), datetime.datetime(1999, 12, 31, 0, 37))
    AssertionError: Tuples differ: ('31/12/99 20:50', '31/12/99 14:22') != (datetime.datetime(1999, 12, 31, 20, 50), [35 chars] 22))
    AssertionError: Tuples differ: ('31/12/99 16:40', '31/12/99 13:39') != (datetime.datetime(1999, 12, 31, 16, 40), [35 chars] 39))

* I change the `return statement`_ in ``duration_a``

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            return (
                datetime.datetime.strptime(
                    wake_time, '%d/%m/%y %H:%M'
                ),
                datetime.datetime.strptime(
                    sleep_time, '%d/%m/%y %H:%M'
                )
            )

  which gives me a NameError_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

  You know I did! I add an `import statement`_ to the top of ``sleep_duration.py``

  .. code-block:: python

    import datetime


    def read_timestamp(timestamp=None, index=0):
    ...

  and the test passes

* I add a :ref:`function<functions>` that calls `datetime.datetime.strptime`_ to remove repetition

  .. code-block:: python

    def get_datetime(timestamp):
        return datetime.datetime.strptime(
            timestamp, '%d/%m/%y %H:%M'
        )


    def duration_a(wake_time=None, sleep_time=None):
    ...

  then call it in the `return statement`_ of ``duration_a``

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            return (
                get_datetime(wake_time),
                get_datetime(sleep_time)
            )

  still green!

.. _test_get_datetime:

test_get_datetime
#################################################################################

.. _test_get_datetime_red:

red: make it fail
---------------------------------------------------------------------------------

* I want to add a test for the ``get_datetime`` :ref:`function<functions>`. I change ``test_datetime_objects`` to ``test_get_datetime`` and make it reference ``sleep_duration.get_datetime`` which calls `datetime.datetime.strptime`_

  .. code-block:: python

    def test_get_datetime(self):
        self.assertEqual(
            sleep_duration.get_datetime(
                "21/11/06 16:30"
            ),
            datetime.datetime(
                2006, 11, 21, 16, 30
            )
        )

  still green! The test has a problem, the timestamp is always the same. I want to test with random timestamps

* I change the expectation to use `datetime.datetime.strptime`_

  .. code-block:: python

    def test_get_datetime(self):
        self.assertEqual(
            sleep_duration.get_datetime(
                '21/11/06 16:30'
            ),
            datetime.datetime.strptime(
                '21/11/06 16:30',
                '%d/%m/%y %H:%M'
            )
        )

* then add a variable with a random timestamp

  .. code-block:: python

    def test_get_datetime(self):
        timestamp = random_timestamp_a()
        self.assertEqual(
            sleep_duration.get_datetime(
                timestamp
            ),
            datetime.datetime.strptime(
                '21/11/06 16:30',
                '%d/%m/%y %H:%M'
            )
        )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: datetime.datetime(1999, 12, 31, 0, 23) != datetime.datetime(2006, 11, 21, 16, 30)
    AssertionError: datetime.datetime(1999, 12, 31, 8, 55) != datetime.datetime(2006, 11, 21, 16, 30)
    AssertionError: datetime.datetime(1999, 12, 31, 9, 16) != datetime.datetime(2006, 11, 21, 16, 30)
    AssertionError: datetime.datetime(1999, 12, 31, 15, 5) != datetime.datetime(2006, 11, 21, 16, 30)

.. _test_get_datetime_green:

green: make it pass
---------------------------------------------------------------------------------

I add the variable to the expectation

.. code-block:: python

  def test_get_datetime(self):
      timestamp = random_timestamp_a()
      self.assertEqual(
          sleep_duration.get_datetime(
              timestamp
          ),
          datetime.datetime.strptime(
              timestamp,
              '%d/%m/%y %H:%M'
          )
      )

and the terminal shows green again

.. _test_get_datetime_refactor:

refactor: make it better
---------------------------------------------------------------------------------

* I change the calls to `datetime.datetime.strptime`_ to ``sleep_duration.get_datetime``

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        sleep_time = random_timestamp_a()
        wake_time = random_timestamp_a()

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp_a()
        else:
            self.assertEqual(
                sleep_duration.duration_a(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                (
                    sleep_duration.get_datetime(
                        wake_time
                    ),
                    sleep_duration.get_datetime(
                        sleep_time
                    )
                )
            )

  the terminal shows green again

----

* I change the expectation in the test to the difference between the timestamps

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        sleep_time = random_timestamp_a()
        wake_time = random_timestamp_a()

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp_a()
        else:
            self.assertEqual(
                sleep_duration.duration_a(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                (
                    sleep_duration.get_datetime(
                        wake_time
                    )
                  - sleep_duration.get_datetime(
                        sleep_time
                    )
                )
            )

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (datetime.datetime(1999, 12, 31, 16, 1), datetime.datetime(1999, 12, 31, 14, 6)) != datetime.timedelta(seconds=6900)
    AssertionError: (datetime.datetime(1999, 12, 31, 9, 57), datetime.datetime(1999, 12, 31, 1, 3)) != datetime.timedelta(seconds=32040)
    AssertionError: (datetime.datetime(1999, 12, 31, 23, 59),[35 chars], 1)) != datetime.timedelta(seconds=7080)
    AssertionError: (datetime.datetime(1999, 12, 31, 16, 1), [35 chars] 55)) != datetime.timedelta(seconds=7560)

  the ``duration_a`` :ref:`function<functions>` returns `datetime.datetime`_ objects and the test expects `datetime.timedelta` object. I change it to match the expectation

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            return (
                get_datetime(wake_time)
              - get_datetime(sleep_time)
            )

  and the test passes

* I change the expectation in the test because I want the result as a string_ not a `datetime.timedelta`_ object

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        sleep_time = random_timestamp_a()
        wake_time = random_timestamp_a()

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp_a()
        else:
            self.assertEqual(
                sleep_duration.duration_a(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                str(
                    sleep_duration.get_datetime(
                        wake_time
                    )
                  - sleep_duration.get_datetime(
                        sleep_time
                    )
                )
            )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: datetime.timedelta(seconds=4440) != '1:14:00'
    AssertionError: datetime.timedelta(seconds=15780) != '4:23:00'
    AssertionError: datetime.timedelta(seconds=31020) != '8:37:00'
    AssertionError: datetime.timedelta(seconds=49920) != '13:52:00'

  I make the same change to the `return statement`_ in ``duration_a``

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            return str(
                get_datetime(wake_time)
              - get_datetime(sleep_time)
            )

  and the test passes! It is time to dance!!

* I remove

  - ``duration`` because ``duration_a`` is a better solution, and
  - ``read_timestamp`` because no one is calling it anymore

  the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'sleep_duration' has no attribute 'duration'...

* I change the name of ``duration_a`` to ``duration`` in both files and the terminal shows a ValueError_

  .. code-block:: python

    ValueError: time data '04:51' does not match format '%d/%m/%y %H:%M'
    ValueError: time data '13:35' does not match format '%d/%m/%y %H:%M'
    ValueError: time data '12:26' does not match format '%d/%m/%y %H:%M'
    ValueError: time data '23:20' does not match format '%d/%m/%y %H:%M'

  ``test_duration_w_hours_and_minutes`` does not have dates in its timestamps. I remove it because it is covered by ``test_duration_w_date_and_time``

* then remove

  - ``get_difference`` because no one calls it anymore, and
  - ``test_the_modulo_operation``
  - ``test_floor_aka_integer_division``
  - ``test_converting_strings_to_numbers``
  - ``test_string_splitting``

  because they do not test the solution directly

* I remove ``random_timestamp`` and change the name of ``random_timestamp_a`` to ``random_timestamp``
* this ``random_timestamp`` :ref:`function<functions>` always returns timestamps with the same date, I change it to take in a date as input

  .. code-block:: python

    def random_timestamp(date):
        return (
            f'{date} '
            f'{random.randint(0,23):02}:'
            f'{random.randint(0,59):02}'
        )

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: random_timestamp() missing 1 required positional argument: 'date'

  I add dates to the calls in the tests

  .. code-block:: python

    def test_get_datetime(self):
        timestamp = random_timestamp('31/12/99')
        self.assertEqual(
            sleep_duration.get_datetime(
                timestamp
            ),
            datetime.datetime.strptime(
                timestamp,
                '%d/%m/%y %H:%M'
            )
        )

    def test_duration_w_date_and_time(self):
        sleep_time = random_timestamp('31/12/99')
        wake_time = random_timestamp('31/12/99')

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                sleep_time=sleep_time,
                wake_time=wake_time,
            )
            wake_time = random_timestamp(
                '31/12/99'
            )
        else:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(
                    sleep_duration.get_datetime(
                        wake_time
                    )
                  - sleep_duration.get_datetime(
                        sleep_time
                    )
                )
            )

  the terminal shows green again

* I add a variable to remove repetition and make sure ``wake_time`` has the same date inside and outside the `while statement`_

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        sleep_time = random_timestamp('31/12/99')

        wake_date = '31/12/99'
        wake_time = random_timestamp(wake_date)

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp(
                wake_date
            )
        else:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(
                    sleep_duration.get_datetime(
                        wake_time
                    )
                  - sleep_duration.get_datetime(
                        sleep_time
                    )
                )
            )

* I change the date for ``sleep_time`` to test it

  .. code-block:: python

    sleep_time = random_timestamp('30/12/99')

  still green, then change it to a bad date

  .. code-block:: python

    sleep_time = random_timestamp('32/12/99')

  and the test is stuck in a loop, this is a problem, I change the date back

  .. code-block:: python

    sleep_time = random_timestamp('31/12/99')

  green again

* When I change ``wake_date``

  .. code-block:: python

    wake_date = '30/12/99'

  the test is stuck in a loop because ``wake_date`` is earlier than the date for ``sleep_time``, another problem. When I change it to a date that does not exist

  .. code-block:: python

    wake_date = '32/12/99'

  the terminal shows a get a ValueError_

  .. code-block:: python

    ValueError: time data '32/12/99 01:11' does not match format '%d/%m/%y %H:%M'

  this is better. I want the same thing to happen when I use a date that does not exist for ``sleep_time``

* I change ``wake_date`` back and change the date for ``sleep_time`` to cause the loop to not end, then change the `while statement`_ to call ``sleep_duration.get_datetime``

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        sleep_time = random_timestamp('32/12/99')

        wake_date = '31/12/99'
        wake_time = random_timestamp(wake_date)

        while (
            sleep_duration.get_datetime(wake_time)
          < sleep_duration.get_datetime(sleep_time)
        ):
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp(
                wake_date
            )
        else:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(
                    sleep_duration.get_datetime(
                        wake_time
                    )
                  - sleep_duration.get_datetime(
                        sleep_time
                    )
                )
            )

  the terminal shows a ValueError_

  .. code-block:: python

    ValueError: time data '32/12/99 08:15' does not match format '%d/%m/%y %H:%M'
    ValueError: time data '32/12/99 09:36' does not match format '%d/%m/%y %H:%M'
    ValueError: time data '32/12/99 10:27' does not match format '%d/%m/%y %H:%M'
    ValueError: time data '32/12/99 19:27' does not match format '%d/%m/%y %H:%M'

  good! I want bad dates to cause an error. I change ``sleep_time`` back to a real date, and the test is green again.

* I change ``wake_date`` to an earlier date to cause the loop to run with no end

  .. code-block:: python

    wake_date = '30/12/99'

  then add a variable and use it to fix the problem when ``wake_date``  is earlier than the date for ``sleep_time``

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        sleep_date = '31/12/99'
        sleep_time = random_timestamp(sleep_date)

        wake_date = '31/12/99'
        wake_time = random_timestamp(wake_date)

        while (
            sleep_duration.get_datetime(wake_time)
          < sleep_duration.get_datetime(sleep_time)
        ):
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp(
                sleep_date
            )
        else:
            self.assertEqual(
                sleep_duration.duration(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                str(
                    sleep_duration.get_datetime(
                        wake_time
                    )
                  - sleep_duration.get_datetime(
                        sleep_time
                    )
                )
            )

  the loop ends and the terminal shows green again, I change ``wake_date`` back and the terminal still shows green

* I remove the ``wake_date`` variable because it is only used once

  .. code-block:: python

    def test_duration(self):
        sleep_date = '31/12/99'
        sleep_time = random_timestamp(sleep_date)
        wake_time = random_timestamp('3/12/99')

        while (
            sleep_duration.get_datetime(wake_time)
          < sleep_duration.get_datetime(sleep_time)
        ):
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp(
                sleep_date
            )
        else:
            self.assertEqual(
                sleep_duration.duration(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                str(
                    sleep_duration.get_datetime(
                        wake_time
                    )
                  - sleep_duration.get_datetime(
                        sleep_time
                    )
                )
            )

* then change ``test_duration_w_date_and_time`` to ``test_duration`` and all is well that ends well

.. _sleep_duration_review:

*********************************************************************************
review
*********************************************************************************

The challenge was to write a program that calculates the difference between a given wake and sleep time. I ran the following tests to get something that does it

* :ref:`test_string_splitting`
* :ref:`test_converting_strings_to_numbers`
* :ref:`test_floor_aka_integer_division`
* :ref:`test_the_modulo_operation`
* `test_datetime_objects`_ where I

  - used `python's online documentation`_
  - and converted a string_ to a `datetime.datetime`_ object using the `datetime.datetime.strptime`_ :ref:`method<functions>`

* :ref:`test_duration_w_hours<test_duration_w_hours>`
* :ref:`test_duration_calculation`
* :ref:`test_duration_w_an_earlier_wake_than_sleep_time<test_duration_w_an_earlier_wake_than_sleep_time>`
* :ref:`test_duration_w_hours_and_minutes<test_duration_w_hours_and_minutes>`
* `test_get_datetime`_
* `test_duration_w_date_and_time`_ where I used

  - `random.randint`_ to generate random numbers for hours and minutes
  - that are :doc:`interpolated </how_to/pass_values>` in timestamps with dates as inputs for ``wake_time`` and ``sleep_time``
  - a `while statement`_ to make sure that when ``wake_time`` is earlier than ``sleep_time`` the ``duration`` :ref:`function<functions>` raises a ValueError_ with a message
  - and when ``wake_time`` is later than or the same as ``sleep_time`` it returns the right difference between them

I also encountered the following exceptions

* :ref:`AssertionError`
* :ref:`TypeError`
* NameError_
* :ref:`AttributeError`
* ValueError_

Would you like to :ref:`write the solution using test_sleep_duration.py<test_duration_tests>` only?

----

:doc:`/code/code_sleep_duration`