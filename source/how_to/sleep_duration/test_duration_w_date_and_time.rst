.. meta::
  :description: Learn to calculate sleep duration with date and time in Python! Master the datetime module, strptime, and TDD for accurate timestamp difference calculations.
  :keywords: Jacob Itegboje, Python sleep duration, Python datetime module, calculate time with date Python, strptime Python, TDD time calculation, Python timestamp difference, sleep duration calculator

.. include:: ../../links.rst


#################################################################################
how to measure sleep duration: test_duration_w_date_and_time
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/LQDh03LiKz4?si=WKU0KwdHNBSYLwfx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

This is part 4 of a program that calculates the difference between a given wake and sleep time.

----

I want to test the ``duration`` :ref:`function<functions>` with timestamps that have dates

*********************************************************************************
red: make it fail
*********************************************************************************

* I make a copy of ``random_timestamp``, change the name of the copy, then add a date to the `return statement`_

  .. code-block:: python

    def random_timestamp_a():
        return (
            '1999/12/31 '
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
                src.sleep_duration.duration(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                self.get_difference(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )
            )

  the terminal shows ValueError_

  .. code-block:: python

    ValueError: invalid literal for int() with base 10: '1999/12/31 03'
    ValueError: invalid literal for int() with base 10: '1999/12/31 07'
    ValueError: invalid literal for int() with base 10: '1999/12/31 11'
    ValueError: invalid literal for int() with base 10: '1999/12/31 21'

  the test calls ``duration``, which calls ``read_timestamp``, which uses the int_ constructor_ to change the timestamp string_ to a number after it calls `str.split`_, but it is not in the right format


*********************************************************************************
green: make it pass
*********************************************************************************

* I add the `unittest.skip decorator`_ to ``test_duration_w_date_and_time``

  .. code-block:: python

    @unittest.skip
    def test_duration_w_date_and_time(self):
    ...

* then add an :ref:`assertion<AssertionError>` in ``test_converting_strings_to_numbers`` to see if I can make the same ValueError_ happen again to make sure the problem is with converting the string to a number

  .. code-block:: python

    def test_converting_strings_to_numbers(self):
        self.assertEqual(int('12'), 12)
        self.assertEqual(int('01'), 1)

        int('1999/12/31 21')

  the terminal shows ValueError_ with the same message from ``test_duration_w_date_and_time``

  .. code-block:: python

    ValueError: invalid literal for int() with base 10: '1999/12/31 21'

  I cannot use the int_ constructor_ to change a timestamp string_ to a number when it has a date. I add an `assertRaises`_ to :ref:`handle<how to test that an Exception is raised>` the ValueError_

  .. code-block:: python

    def test_converting_strings_to_numbers(self):
        self.assertEqual(int('12'), 12)
        self.assertEqual(int('01'), 1)

        with self.assertRaises(ValueError):
            int('1999/12/31 21')

  and the test is green again

* I remove the `unittest.skip decorator`_ from ``test_duration_w_date_and_time``
* then change the call in the :ref:`assertion<AssertionError>` to a different :ref:`function<functions>`

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
                src.sleep_duration.duration_a(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                self.get_difference(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )
            )

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.sleep_duration' has no attribute 'duration_a'...

* I make a copy of the ``duration`` :ref:`function<functions>` in ``sleep_duration.py`` and change the name to ``duration_a`` to keep the working solution while I try a new one. I change the ``else`` block to return :ref:`None`

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

  the terminal shows ValueError_

  .. code-block:: python

    ValueError: invalid literal for int() with base 10: '1999/12/31 22'

  because the test calls the ``get_difference`` :ref:`method<functions>` in the expectation which uses the int_ constructor_

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
                src.sleep_duration.duration_a(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                (wake_time, sleep_time)
            )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != ('1999/12/31 09:52', '1999/12/31 07:11')
    AssertionError: None != ('1999/12/31 18:16', '1999/12/31 11:21')
    AssertionError: None != ('1999/12/31 13:10', '1999/12/31 12:00')
    AssertionError: None != ('1999/12/31 16:41', '1999/12/31 12:35')

  I change the `return statement`_ in ``duration_a``

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

  the test passes

*********************************************************************************
refactor: make it better
*********************************************************************************

I want something that can read dates and times from timestamps. I search `python's online documentation`_ for `date and time <https://docs.python.org/3/search.html?q=date+and+time>`_ to see if there is an existing solution and select the datetime_ :ref:`module<ModuleNotFoundError>` from the results. The available types in the :ref:`module<ModuleNotFoundError>` show `datetime.datetime`_ objects

.. code-block:: python

  class datetime.datetime
    A combination of a date and a time.
      Attributes: year, month, day, hour,
      minute, second, microsecond, and tzinfo.


test_datetime_objects
#################################################################################

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

the terminal shows NameError_

.. code-block:: python

  NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

green: make it pass
---------------------------------------------------------------------------------

I add an `import statement`_ for the datetime_ module

.. code-block:: python

  import datetime
  import random
  import src.sleep_duration
  import unittest
  ...

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'datetime' has no attribute 'strptime'

because my `import statement`_ is different from `the example in the documentation <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_, so I add the :ref:`module<ModuleNotFoundError>` name to the call

.. code-block:: python

  def test_datetime_objects(self):
      self.assertEqual(
          datetime.datetime.strptime(
              "21/11/06 16:30",
              "%d/%m/%y %H:%M"
          ),
          ''
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: datetime.datetime(2006, 11, 21, 16, 30) != ''

I copy the value from the left side of the :ref:`AssertionError` and paste it as the expected value in the test

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

The `datetime.datetime.strptime`_ :ref:`method<functions>` returns a `datetime.datetime`_ object when given 2 strings_ as inputs - a timestamp and a pattern that is for the timestamp. The pattern provided is

- ``%d`` for days
- ``%m`` for months
- ``%y`` for 2 digit years
- ``%H`` for hours
- ``%M`` for minutes

there are more details in `strftime() and strptime() behavior <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior>`_

refactor: make it better
---------------------------------------------------------------------------------

* I change the order in the date to test the pattern

  .. code-block:: python

    def test_datetime_objects(self):
        self.assertEqual(
            datetime.datetime.strptime(
                "06/11/21 16:30",
                "%d/%m/%y %H:%M"
            ),
            datetime.datetime(
                2006, 11, 21, 16, 30
            )
        )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: datetime.datetime(2021, 11, 6, 16, 30) != datetime.datetime(2006, 11, 21, 16, 30)

  when I change the pattern to match

  .. code-block:: python

    def test_datetime_objects(self):
        self.assertEqual(
            datetime.datetime.strptime(
                "06/11/21 16:30",
                "%y/%m/%d %H:%M"
            ),
            datetime.datetime(
                2006, 11, 21, 16, 30
            )
        )

  the test passes

* I change the year to four digits

  .. code-block:: python

    def test_datetime_objects(self):
        self.assertEqual(
            datetime.datetime.strptime(
                "2006/11/21 16:30",
                "%y/%m/%d %H:%M"
            ),
            datetime.datetime(
                2006, 11, 21, 16, 30
            )
        )

  the terminal shows ValueError_

  .. code-block:: python

    ValueError: time data '2006/11/21 16:30' does not match format '%y/%m/%d %H:%M'

  and when I change the pattern to use ``%Y`` for the year

  .. code-block:: python

    def test_datetime_objects(self):
        self.assertEqual(
            datetime.datetime.strptime(
                "2006/11/21 16:30",
                "%Y/%m/%d %H:%M"
            ),
            datetime.datetime(
                2006, 11, 21, 16, 30
            )
        )

  the terminal shows green again

* I add calls to the `datetime.datetime.strptime`_ :ref:`method<functions>` in ``test_duration_w_date_and_time``

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
                src.sleep_duration.duration_a(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                (
                    datetime.datetime.strptime(
                        wake_time,
                        '%Y/%m/%d %H:%M'
                    ),
                    datetime.datetime.strptime(
                        sleep_time,
                        '%Y/%m/%d %H:%M'
                    )
                )
            )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ('1999/12/31 07:20', '1999/12/31 03:08') != (datetime.datetime(1999, 12, 31, 7, 20), datetime.datetime(1999, 12, 31, 3, 8))
    AssertionError: Tuples differ: ('1999/12/31 15:01', '1999/12/31 00:37') != (datetime.datetime(1999, 12, 31, 15, 1), datetime.datetime(1999, 12, 31, 0, 37))
    AssertionError: Tuples differ: ('1999/12/31 20:50', '1999/12/31 14:22') != (datetime.datetime(1999, 12, 31, 20, 50), [35 chars] 22))
    AssertionError: Tuples differ: ('1999/12/31 16:40', '1999/12/31 13:39') != (datetime.datetime(1999, 12, 31, 16, 40), [35 chars] 39))

  ``duration_a`` returns the timestamps as strings_ and the test expects them as `datetime.datetime`_ objects. I change the `return statement`_ to match

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
                    wake_time, '%Y/%m/%d %H:%M'
                ),
                datetime.datetime.strptime(
                    sleep_time, '%Y/%m/%d %H:%M'
                )
            )

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

  I add an `import statement`_ to the top of ``sleep_duration.py``

  .. code-block:: python

    import datetime


    def read_timestamp(timestamp=None, index=0):
    ...

  the test passes

* I just called `datetime.datetime.strptime`_ 5 times in a row with the same pattern, time to add a :ref:`function<functions>` to remove some repetition

  .. code-block:: python

    def get_datetime(timestamp):
        return datetime.datetime.strptime(
            timestamp, '%Y/%m/%d %H:%M'
        )


    def duration_a(wake_time=None, sleep_time=None):
    ...

  and call it in the `return statement`_ of ``duration_a``

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


test_get_datetime
#################################################################################

red: make it fail
---------------------------------------------------------------------------------

I want a test for the ``get_datetime`` :ref:`function<functions>` so I change the name of ``test_datetime_objects`` to ``test_get_datetime`` and make it call ``src.sleep_duration.get_datetime`` which calls the `datetime.datetime.strptime`_ :ref:`method<functions>`

.. code-block:: python

  def test_get_datetime(self):
      self.assertEqual(
          src.sleep_duration.get_datetime(
              "21/11/06 16:30"
          ),
          datetime.datetime(
              2006, 11, 21, 16, 30
          )
      )

I change the expectation to use `datetime.datetime.strptime`_

.. code-block:: python

  def test_get_datetime(self):
      self.assertEqual(
          src.sleep_duration.get_datetime(
              "2006/11/21 16:30"
          ),
          datetime.datetime.strptime(
              '2006/11/21 16:30',
              '%Y/%m/%d %H:%M'
          )
      )

then add a variable for a random timestamp

.. code-block:: python

  def test_get_datetime(self):
      timestamp = random_timestamp_a()
      self.assertEqual(
          src.sleep_duration.get_datetime(
              timestamp
          ),
          datetime.datetime.strptime(
              '2006/11/21 16:30',
              '%Y/%m/%d %H:%M'
          )
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: datetime.datetime(1999, 12, 31, 0, 23) != datetime.datetime(2006, 11, 21, 16, 30)
  AssertionError: datetime.datetime(1999, 12, 31, 8, 55) != datetime.datetime(2006, 11, 21, 16, 30)
  AssertionError: datetime.datetime(1999, 12, 31, 9, 16) != datetime.datetime(2006, 11, 21, 16, 30)
  AssertionError: datetime.datetime(1999, 12, 31, 15, 5) != datetime.datetime(2006, 11, 21, 16, 30)

green: make it pass
---------------------------------------------------------------------------------

I add the variable to the expectation

.. code-block:: python

  def test_get_datetime(self):
      timestamp = random_timestamp_a()
      self.assertEqual(
          src.sleep_duration.get_datetime(
              timestamp
          ),
          datetime.datetime.strptime(
              timestamp,
              '%Y/%m/%d %H:%M'
          )
      )

the terminal shows green again

refactor: make it better
---------------------------------------------------------------------------------

I change the calls to `datetime.datetime.strptime`_ to ``src.sleep_duration.get_datetime``

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
              src.sleep_duration.duration_a(
                  sleep_time=sleep_time,
                  wake_time=wake_time
              ),
              (
                  src.sleep_duration.get_datetime(
                      wake_time
                  ),
                  src.sleep_duration.get_datetime(
                      sleep_time
                  )
              )
          )

and the test is still green

----

* I change the expectation in the test to the difference between the timestamps because I can do arithmetic_ with `datetime.datetime`_ objects

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
                src.sleep_duration.duration_a(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                (
                    src.sleep_duration.get_datetime(
                        wake_time
                    )
                  - src.sleep_duration.get_datetime(
                        sleep_time
                    )
                )
            )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (datetime.datetime(1999, 12, 31, 16, 1), datetime.datetime(1999, 12, 31, 14, 6)) != datetime.timedelta(seconds=6900)
    AssertionError: (datetime.datetime(1999, 12, 31, 9, 57), datetime.datetime(1999, 12, 31, 1, 3)) != datetime.timedelta(seconds=32040)
    AssertionError: (datetime.datetime(1999, 12, 31, 23, 59),[35 chars], 1)) != datetime.timedelta(seconds=7080)
    AssertionError: (datetime.datetime(1999, 12, 31, 16, 1), [35 chars] 55)) != datetime.timedelta(seconds=7560)

  the ``duration_a`` :ref:`function<functions>` returns `datetime.datetime`_ objects and the test expects a `datetime.timedelta`_ object. I change it to match the expectation

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

  the test passes

* I add the str_ constructor_ to the expectation in the test because I want the result as a string_ not a `datetime.timedelta`_ object

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
                src.sleep_duration.duration_a(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                str(
                    src.sleep_duration.get_datetime(
                        wake_time
                    )
                  - src.sleep_duration.get_datetime(
                        sleep_time
                    )
                )
            )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: datetime.timedelta(seconds=4440) != '1:14:00'
    AssertionError: datetime.timedelta(seconds=15780) != '4:23:00'
    AssertionError: datetime.timedelta(seconds=31020) != '8:37:00'
    AssertionError: datetime.timedelta(seconds=49920) != '13:52:00'

  when I make the same change to the `return statement`_ in ``duration_a``

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

  the test passes

* I remove ``duration`` because ``duration_a`` is a better solution
* which means I can remove ``read_timestamp`` because no one calls it anymore. The terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.sleep_duration' has no attribute 'duration'...

* I change the name of ``duration_a`` to ``duration`` in ``sleep_duration.py`` and ``test_sleep_duration.py`` which leaves me with ValueError_

  .. code-block:: python

    ValueError: time data '04:51' does not match format '%Y/%m/%d %H:%M'
    ValueError: time data '13:35' does not match format '%Y/%m/%d %H:%M'
    ValueError: time data '12:26' does not match format '%Y/%m/%d %H:%M'
    ValueError: time data '23:20' does not match format '%Y/%m/%d %H:%M'

  ``test_duration_w_hours_and_minutes`` does not have dates in its timestamps. I remove it because it is covered by ``test_duration_w_date_and_time``

* then remove ``get_difference`` because no one calls it anymore
* I also remove the following tests because they do not test the solution directly

  - ``test_the_modulo_operation``
  - ``test_floor_aka_integer_division``
  - ``test_converting_strings_to_numbers``
  - ``test_string_splitting``

* and remove ``random_timestamp`` because no one calls it anymore
* then change the name of ``random_timestamp_a`` to ``random_timestamp``
* the new ``random_timestamp`` :ref:`function<functions>` always returns timestamps with the same date, I change it to return random dates as well

  .. code-block:: python

    def random_timestamp(date):
        return (
            f'{random.randint(0,9999):04}/'
            f'{random.randint(1,12):02}/'
            f'{random.randint(1,31):02} '
            f'{random.randint(0,23):02}:'
            f'{random.randint(0,59):02}'
        )

  the terminal shows a random ValueError_

  .. code-block:: python

    ValueError: day is out of range for month

  I need to make sure the random dates that are made by the :ref:`function<functions>` are real dates

* I change the name of ``random_timestamp`` to ``get_random_timestamp`` and make a new :ref:`function<functions>` to make sure the random timestamps generated are good

  .. code-block:: python

    def get_random_timestamp():
        return (
            f'{random.randint(0,9999):04}/'
            f'{random.randint(1,12):02}/'
            f'{random.randint(1,31):02} '
            f'{random.randint(0,23):02}:'
            f'{random.randint(0,59):02}'
        )


    def random_timestamp():
        result = get_random_timestamp()
        try:
            src.sleep_duration.get_datetime(result)
        except ValueError:
            return random_timestamp()
        else:
            return result

  The new ``random_timestamp`` :ref:`function<functions>` does the following

  - generates a random timestamp by calling ``get_random_timestamp``
  - checks if the timestamp is good by calling ``src.sleep_duration.get_datetime``
  - if the timestamp is good, the :ref:`function<functions>` returns it
  - if the timestamp is bad, it raises ValueError_ and repeats the process by calling itself

* I can add another :ref:`function<functions>` to remove some repetition

  .. code-block:: python

    def random_number(start, end, digits=2):
        return f'{random.randint(start, end):0{digits}}'

  then add calls to it in ``get_random_timestamp``

  .. code-block:: python

    def get_random_timestamp():
        return (
            f'{random_number(0,9999,4)}/'
            f'{random_number(1,12)}/'
            f'{random_number(1,31)} '
            f'{random_number(0,23)}:'
            f'{random_number(0,59)}'
        )

  all tests are still green
* I change ``test_duration_w_date_and_time`` to ``test_duration`` the terminal shows all tests are still passing

.. _sleep_duration_review:

*********************************************************************************
review
*********************************************************************************

The challenge was to write a program that calculates the difference between a given wake and sleep time. I ran the following tests to get something that does it

* :ref:`test_string_splitting`
* :ref:`test_converting_strings_to_numbers`
* :ref:`test_floor_aka_integer_division`
* :ref:`test_the_modulo_operation`
* :ref:`test_duration_w_hours <how to measure sleep duration: test_duration_w_hours>`
* :ref:`test_duration_calculation`
* :ref:`test_duration_w_an_earlier_wake_than_sleep_time <how to measure sleep duration: test_duration_w_an_earlier_wake_than_sleep_time>`
* :ref:`test_duration_w_hours_and_minutes<how to measure sleep duration: test_duration_w_hours_and_minutes>`
* `test_datetime_objects`_ where I used `python's online documentation`_ to read about the `datetime.datetime.strptime`_ :ref:`method<functions>` which I used to change a string_ to a `datetime.datetime`_ object
* `test_get_datetime`_
* :ref:`test_duration_w_date_and_time <how to measure sleep duration: test_duration_w_date_and_time>` where I used

  - `random.randint`_ and an :ref:`how to test that an Exception is raised` to generate timestamps with random dates and times that are :ref:`how to pass values` in strings for ``wake_time`` and ``sleep_time``
  - a `while statement`_ to make sure that when ``wake_time`` is earlier than ``sleep_time`` the ``duration`` :ref:`function<functions>` raises ValueError_ with a message and returns the right difference between the 2 when ``wake_time`` is later than or the same as ``sleep_time``

I also ran into the following :ref:`Exceptions<errors>`

* :ref:`AssertionError`
* :ref:`TypeError`
* NameError_
* :ref:`AttributeError`
* ValueError_

Would you like to :ref:`write the solution without looking at test_sleep_duration.py? <how to measure sleep duration: test_duration_tests>`

----

:ref:`how to measure sleep duration: tests and solution`