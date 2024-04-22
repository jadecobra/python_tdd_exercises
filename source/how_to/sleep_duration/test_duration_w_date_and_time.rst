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

I want to see what would happen if I added dates to the timestamps?

.. _test_duration_w_date_and_time_red:

*********************************************************************************
red: make it fail
*********************************************************************************

* I copy ``test_duration_w_hours_and_minutes`` and paste it below the original
* then rename the copy to ``test_duration_w_date_and_time`` to test ``duration`` with timestamps that have a date, hours and minutes

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        wake_hour = random_hour()
        wake_minutes = random_minutes()
        wake_time_minutes = (
            (wake_hour * 60)
           + wake_minutes
        )
        wake_time = f'31/12/99 {wake_hour:02}:{wake_minutes:02}'

        sleep_hour = random_hour()
        sleep_minutes = random_minutes()
        sleep_time_minutes = (
            (sleep_hour * 60)
          + sleep_minutes
        )
        sleep_time=f'31/12/99 {sleep_hour:02}:{sleep_minutes:02}'

        difference = (
            wake_time_minutes
          - sleep_time_minutes
        )
        difference_hours = difference // 60
        difference_minutes = difference % 60

        try:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                f'{difference_hours:02}:{difference_minutes:02}'
            )
        except ValueError:
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            ):
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: "wake_time: 31/12/99 13:04 is earlier than sleep_time: 31/12/99 15:25" does not match "invalid literal for int() with base 10: '31/12/99 13'"

  it looks like ``test_duration_w_date_and_time`` encountered a ValueError_ with a different message than the one expected in the test. The assertRaisesRegex_ works, the test would have missed this if I did not specify what error message to catch

.. _test_duration_w_date_and_time_green_0:

*********************************************************************************
green: make it pass
*********************************************************************************

* The ``read_timestamp`` :ref:`function<functions>` tries to convert the given string_ to an integer but it is in the wrong format

  .. code-block:: python

    invalid literal for int() with base 10: '31/12/99 13'

* The `str.split`_ :ref:`method<functions>` was given a separator of a ``':'`` when the timestamp contained only hours and minutes, but behaves differently when the timestamp has a date. I add a test to ``test_string_splitting`` for this

  .. code-block:: python

    def test_string_splitting(self):
        self.assertEqual(
            '01:23'.split(':'),
            ['01', '23']
        )

        split = '12:34'.split(':')
        self.assertEqual(
            split[0],
            '12'
        )
        self.assertEqual(
            split[1],
            '34'
        )

        self.assertEqual(
            '31/12/99 13:04'.split(':')[0],
            ''
        )

  the terminal shows the :ref:`AssertionError` for ``test_duration_w_date_and_time`` and another for ``test_string_splitting``

  .. code-block:: python

    AssertionError: '31/12/99 13' != ''

  so I disable ``test_duration_w_date_and_time`` by adding the `unittest.skip decorator`_

  .. code-block:: python

    ...
    @unittest.skip
    def test_duration_w_date_and_time(self):
    ...

* then change ``test_string_splitting`` with the right values to make it pass

  .. code-block:: python

    self.assertEqual(
        '31/12/99 13:04'.split(':')[0],
        '31/12/99 13'
    )

* I also add a test to ``test_converting_strings_to_numbers`` to confirm that the ValueError_ is raised when calling the int_ constructor on the result of ``'31/12/99 13:04'.split(':')[0]``

  .. code-block:: python

    def test_converting_strings_to_numbers(self):
        self.assertEqual(int('12'), 12)
        self.assertEqual(int('01'), 1)
        int('31/12/99 13')

  and the terminal shows a ValueError_ with the same message from ``test_duration_w_date_and_time``

  .. code-block:: python

    ValueError: invalid literal for int() with base 10: '31/12/99 13'

  I cannot convert a string_ in the format ``'31/12/99 13'`` to an integer

* I handle the ValueError_ with `assertRaises`_

  .. code-block:: python

    def test_converting_strings_to_numbers(self):
        self.assertEqual(int('12'), 12)
        self.assertEqual(int('01'), 1)

        with self.assertRaises(ValueError):
            int('31/12/99 13')

  and tests are green again

* I need a solution that can read the date and time. Writing one myself requires calculating the number of days in months for every year. Instead, I search for `time difference <https://docs.python.org/3/search.html?q=time+difference>`_ in `python's online documentation`_, to see if there is an existing solution and select the datetime_ module from the results since it looks like the right one. Reading through the available types in the module I see `datetime.datetime`_ objects which are a combination of date and time

  .. code-block:: python

    class datetime.datetime
      A combination of a date and a time.
        Attributes: year, month, day, hour,
        minute, second, microsecond, and tzinfo.

  and `datetime.timedelta`_ objects which are the difference between two `datetime.datetime`_ instances

  .. code-block:: python

    class datetime.timedelta
      A duration expressing the difference between
        two date, time, or datetime instances to
        microsecond resolution.

.. _test_datetime_objects:

test_datetime_objects
#################################################################################

.. _test_datetime_objects_red:

red: make it fail
-----------------------------------------------------------------------------

I add a test to ``test_sleep_duration.py`` based on `Examples of usage: datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_ for `datetime.datetime`_ objects

.. code-block:: python

  def test_datetime_objects(self):
      self.assertEqual(
          datetime.datetime.strptime(
              "21/11/06 16:30",
              "%d/%m/%y %H:%M"
          ),
          ''
      )

  def test_duration_w_an_earlier_wake_than_sleep_time(self):
  ...

and the terminal shows a NameError_ because ``datetime`` is not defined in ``test_sleep_duration.py``, I need to import it

.. code-block:: python

  NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

.. _test_datetime_objects_green:

green: make it pass
-----------------------------------------------------------------------------

I add an `import statement`_ for the datetime_ module,

.. code-block:: python

  import datetime
  import random
  import sleep_duration
  import unittest
  ...

the terminal shows an :ref:`AssertionError`,

.. code-block:: python

  AssertionError: datetime.datetime(2006, 11, 21, 16, 30) != ''

I copy the value on the left side of the :ref:`AssertionError` to replace the expected value in the test,

.. code-block:: python

  def test_datetime_objects(self):
      self.assertEqual(
          datetime.datetime.strptime(
              "21/11/06 16:30",
              "%d/%m/%y %H:%M"
          ),
          datetime.datetime(2006, 11, 21, 16, 30)
      )

and the terminal shows passing tests. From this test I see that

* when the `datetime.datetime.strptime`_ :ref:`method<functions>` is given 2 strings_ as inputs - a timestamp and a pattern, it returns a `datetime.datetime`_ object with ``year``, ``month``, ``date``, ``hours`` and ``minutes``
* It also looks like the pattern provided means

  - ``%d`` is for days
  - ``%m`` is for months
  - ``%y`` is for 2 digit years
  - ``%H`` is for hours
  - ``%M`` is for minutes

  you can see more in `strftime() and strptime() behavior <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior>`_

.. _test_subtracting_datetime_objects:

test_subtracting_datetime_objects
#################################################################################

.. _test_subtracting_datetime_objects_red:

red: make it fail
-----------------------------------------------------------------------------

I add a test for subtracting two `datetime.datetime`_ objects

.. code-block:: python

  def test_subtracting_datetime_objects(self):
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
          1
      )

  def test_duration_w_hours_and_minutes(self):
  ...


the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: datetime.timedelta(seconds=3600) != 1

.. _test_subtracting_datetime_objects_green:

green: make it pass
-----------------------------------------------------------------------------

I copy the value on the left of the :ref:`AssertionError` and replace the expected value in the test to make it pass

.. code-block:: python

  self.assertEqual(
      wake_time-sleep_time,
      datetime.timedelta(seconds=3600)
  )

.. _test_subtracting_datetime_objects_refactor:

refactor: make it better
-----------------------------------------------------------------------------

I add a variable to remove the duplication of the timestamp pattern

.. code-block:: python

  def test_subtracting_datetime_objects(self):
      pattern = '%d/%m/%y %H:%M'
      sleep_time = datetime.datetime.strptime(
          '21/11/06 16:30', pattern
      )
      wake_time = datetime.datetime.strptime(
          '21/11/06 17:30', pattern
      )

      self.assertEqual(
      wake_time-sleep_time,
      datetime.timedelta(seconds=3600)
  )

With these passing tests. I see that I can

- convert a string_ to a `datetime.datetime`_ object by using `datetime.datetime.strptime`_
- subtract one `datetime.datetime`_ object from another to get a `datetime.timedelta`_ object

.. _test_converting_timedelta_to_string:

test_converting_timedelta_to_string
#################################################################################

.. _test_converting_timedelta_to_string_red:

red: make it fail
-----------------------------------------------------------------------------

* The `datetime.timedelta`_ object I get shows seconds, but I want the result as a string_. What happens when I pass it to the str_ constructor?

  .. code-block:: python

    def test_converting_timedelta_to_string(self):
        self.assertEqual(
            str(datetime.timedelta(seconds=7654)),
            ''
        )

    def test_duration_w_hours_and_minutes(self):
    ...

  the terminal shows an :ref:`AssertionError` with a string_ like what I want

  .. code-block:: python

    AssertionError: '2:07:34' != ''

.. _test_converting_timedelta_to_string_green:

green: make it pass
-----------------------------------------------------------------------------

I make the expected value in the test match the value from the terminal

.. code-block:: python

  self.assertEqual(
      str(datetime.timedelta(seconds=7654)),
      '2:07:34'
  )

and we are green. It looks like calling str_ on a `datetime.timedelta`_ object returns a string_ in the format ``Hours:Minutes:Seconds``

From the tests, I know I can

* convert a string_ to a `datetime.datetime`_ object using `datetime.datetime.strptime`_
* subtract one `datetime.datetime`_ object from another to get a `datetime.timedelta`_ object
* convert a `datetime.timedelta`_ object to a string_

----

.. _test_duration_w_date_and_time_green_1:

* I take off the `unittest.skip decorator`_ from ``test_duration_w_date_and_time`` to return to the ValueError_ that sent me down this path
* then rename the ``duration`` :ref:`function<functions>` in ``sleep_duration.py`` to ``duration_a`` to keep the existing working solution while I try a new one

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
        wake_time_minutes = get_total_minutes(wake_time)
        sleep_time_minutes = get_total_minutes(sleep_time)

        if wake_time_minutes < sleep_time_minutes:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
        else:
            difference = (
                wake_time_minutes
            - sleep_time_minutes
            )
            difference_hours = difference // 60
            difference_minutes = difference % 60

            return f'{difference_hours:02}:{difference_minutes:02}'

* and make a :ref:`function<functions>` called ``get_datetime_object`` that uses `datetime.datetime.strptime`_ to read timestamps

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
    ...

    def get_datetime_object(timestamp):
        return datetime.datetime.strptime(
            timestamp, '%d/%m/%y %H:%M'
        )

* and a new ``duration`` :ref:`function<functions>` with calls to ``get_datetime_object`` when calculating the difference between ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference = (
            get_datetime_object(wake_time)
          - get_datetime_object(sleep_time)
        )
        return str(difference)

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

  You know I did. I encountered this earlier when testing the datetime_ module

* I add an `import statement`_ to the top of ``sleep_duration.py``

  .. code-block:: python

    import datetime

    def read_timestamp(timestamp=None, index=0):
    ...

  and the terminal shows an :ref:`AssertionError` for ``test_duration_w_an_earlier_wake_than_sleep_time`` and ``test_duration_w_hours_and_minutes``,  that looks like this

  .. code-block:: python

    AssertionError: "wake_time: 10:52 is earlier than sleep_time: 04:00" does not match "time data '10:52' does not match format '%d/%m/%y %H:%M'"

  I have another ValueError_, this time for a timestamp that does not match the expected pattern of ``'%d/%m/%y %H:%M'`` and another :ref:`AssertionError` for ``test_duration_w_date_and_time`` that looks like this

  .. code-block:: python

    AssertionError: '5:46:00' != '05:46'

* I change ``test_duration_w_hours_and_minutes`` to match the new timestamp format and notice that it is the same exact same test as ``test_duration_w_date_and_time`` so I remove it, I do not need the same test twice
* I add dates to ``test_duration_w_an_earlier_wake_than_sleep_time``

  .. code-block:: python

    def test_duration_w_an_earlier_wake_than_sleep_time(self):
        wake_time = '21/12/12 01:00'
        sleep_time = '21/12/12 02:00'

        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: {wake_time} is earlier '
            f'than sleep_time: {sleep_time}'
        ):
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            )

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: ValueError not raised

  the new ``duration`` function is missing the condition for when ``wake_time`` is earlier than ``sleep_time`` so it did not raise the ValueError_ in ``test_duration_w_an_earlier_wake_than_sleep_time``

* When I add the condition

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_datetime = get_datetime_object(wake_time)
        sleep_datetime = get_datetime_object(sleep_time)

        if wake_datetime < sleep_datetime:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
        else:
            difference = (
                wake_datetime
              - sleep_datetime
            )

            return str(difference)

  the terminal shows random :ref:`AssertionErrors<AssertionError>` ``test_duration_w_date_and_time`` when ``wake_time`` is earlier than ``sleep_time`` that look like this

  .. code-block:: python

    AssertionError: '8:50:00' != '08:50'
    AssertionError: '7:00:00' != '09:09'
    AssertionError: '-1 day, 20:36:00' != '-1:52'
    AssertionError: '9:42:00' != '19:34'

  the test is still using the total minutes calculations so we have different formats and results

* I make ``test_duration_w_date_and_time`` use `datetime.datetime`_ objects for the calculations

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        wake_hour = random_hour()
        wake_minutes = random_minutes()
        wake_time_minutes = (
            (wake_hour * 60)
           + wake_minutes
        )
        wake_time = f'31/12/99 {wake_hour:02}:{wake_minutes:02}'

        sleep_hour = random_hour()
        sleep_minutes = random_minutes()
        sleep_time_minutes = (
            (sleep_hour * 60)
           + sleep_minutes
        )
        sleep_time = f'31/12/99 {sleep_hour:02}:{sleep_minutes:02}'

        pattern = '%d/%m/%y %H:%M'
        difference = (
            datetime.datetime.strptime(
                wake_time, pattern
            )
          - datetime.datetime.strptime(
                sleep_time, pattern
            )
        )

        try:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(difference)
            )
        except ValueError:
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            ):
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )

  the terminal shows passing tests and I no longer have random failures, things are green all the way

.. _test_duration_w_date_and_time_refactor:

*********************************************************************************
refactor: make it better
*********************************************************************************

* I remove ``wake_time_minutes`` and ``sleep_time_minutes`` because they are no longer used
* as well as ``wake_hour``, ``wake_minutes``, ``sleep_hour`` and ``sleep_minutes``, and replacing them with direct calls to ``random_hour`` and ``random_minutes`` since they are only used once after assignment

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        wake_time = f'31/12/99 {random_hour()}:{random_minutes():02}'
        sleep_time = f'31/12/99 {random_hour()}:{random_minutes():02}'

        pattern = '%d/%m/%y %H:%M'
        difference = (
            datetime.datetime.strptime(
                wake_time, pattern
            )
          - datetime.datetime.strptime(
                sleep_time, pattern
            )
        )

        try:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(difference)
            )
        except ValueError:
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            ):
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )

* then I make a :ref:`function<functions>` to make random timestamps for a given date

  .. code-block:: python

    def random_hour():
    ...

    def random_minutes():
    ...

    def get_random_timestamp(date):
        return f'{date} {random_hour():02}:{random_minutes():02}'

  and add calls to it in ``test_duration_w_date_and_time``

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        wake_time = get_random_timestamp('31/12/99')
        sleep_time = get_random_timestamp('31/12/99')

        pattern = '%d/%m/%y %H:%M'
        difference = (
            datetime.datetime.strptime(
                wake_time, pattern
            )
          - datetime.datetime.strptime(
                sleep_time, pattern
            )
        )

        try:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(difference)
            )
        except ValueError:
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            ):
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )

* since ``random_hour`` and ``random_minutes`` are only called in in ``get_random_timestamp``, I can call ``random.randint`` directly to replace them

  .. code-block:: python

    def get_random_timestamp(date):
        return f'{date} {random.randint(0,23):02}:{random.randint(0,59):02}'

  which allows me to remove ``random_hour`` and ``random_minutes`` since they are no longer called by anyone

* I remove ``duration_a`` from ``sleep_duration.py`` because ``duration`` is a better solution
* which means I can remove ``get_total_minutes`` and ``read_timestamp`` because they are no longer called by anyone
* and I remove the ``difference`` variable from ``duration`` since it is only used once. I can do the calculation directly

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_datetime = get_datetime_object(wake_time)
        sleep_datetime = get_datetime_object(sleep_time)

        if wake_datetime < sleep_datetime:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
        else:
            return str(
                wake_datetime
              - sleep_datetime
            )

  and we are still green all the way

.. _sleep_duration_review:

*********************************************************************************
review
*********************************************************************************

The challenge was to write a program that calculates the difference between a given wake and sleep time. I ran the following tests to get something that does it

* :ref:`test_string_splitting` where I

  - used the `str.split`_ :ref:`method<functions>` I found by calling the `help system`_ to split a string_ on a separator
  - and indexed the :doc:`list </data_structures/lists/lists>` from the split to get specific items

* :ref:`test_converting_strings_to_numbers` with the int_ constructor

* `test_floor_aka_integer_division`_
* `test_the_modulo_operation`_
* `test_datetime_objects`_ where I

  - used `python's online documentation`_
  - converted a string_ to a `datetime.datetime`_ object using the `datetime.datetime.strptime`_ :ref:`method<functions>`

* `test_subtracting_datetime_objects`_
* `test_converting_timedelta_to_string`_
* `test_duration_w_an_earlier_wake_than_sleep_time`_
* :ref:`test_duration_w_hours_and_minutes` where I

  - used `random.randint`_ to generate random numbers

    * from the 24 hours in a day
    * and the 60 minutes in an hour

  - then :doc:`interpolated </how_to/pass_values>` them in the timestamps
  - :ref:`test_duration_w_hours` and `test_duration_calculation` to make sure that the ``duration`` :ref:`function<functions>` calculates the difference between ``wake_time`` and ``sleep_time`` by

    * converting the timestamp to minutes
    * subtracting the total minutes of ``sleep_time`` from ``wake_time``
    * and converting the difference to a duration in hours and minutes by using `floor (integer) division`_ and the modulo_ operator

* `test_duration_w_date_and_time`_

  - using `random.randint`_ to generate random integers for hours and minutes
  - using timestamps with dates, and times ranging from ``'00:00'`` up to and including ``'23:59'`` as inputs for ``wake_time`` and ``sleep_time``
  - confirming a ValueError_ is raised when ``wake_time`` is earlier than ``sleep_time``

I also encountered the following exceptions

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`
* SyntaxError_
* ValueError_

----

:doc:`/code/code_sleep_duration`