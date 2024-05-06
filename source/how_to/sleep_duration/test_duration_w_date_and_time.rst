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

  the test called ``duration`` which called ``read_timestamp`` that converts the timestamp string_ to a number by using the int_ constructor_ but it is in the wrong format

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

  I cannot convert a timestamp string_ to a number when it has a date with the int_ constructor_. I :doc:`handle</how_to/exception_handling_tests>` the ValueError_ with `assertRaises`_

  .. code-block:: python

    def test_converting_strings_to_numbers(self):
        self.assertEqual(int('12'), 12)
        self.assertEqual(int('01'), 1)

        with self.assertRaises(ValueError):
            int('31/12/99 01')

  and the test is green again

* The int_ constructor_ will not work when the timestamps have a date. I need a solution that can read the date and time. I search for `date and time <https://docs.python.org/3/search.html?q=dare+and+time>`_ in `python's online documentation`_, to see if there is an existing solution and select the datetime_ module from the results. Reading through the available types in the module I see `datetime.datetime`_ objects which are a combination of date and time

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

  def assertWakeTimeEarlier(self, wake_time=None, sleep_time=None):
  ...

and the terminal shows a NameError_ because ``datetime`` is not defined in ``test_sleep_duration.py``

.. code-block:: python

  NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

I have to import it to use it

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

the reference to the ``strptime`` :ref:`method<functions>` is not right, my `import statement`_ is different from `the example in the documentation <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_. I add the module name to the call

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

* when the `datetime.datetime.strptime`_ :ref:`method<functions>` is given 2 strings_ as inputs - a timestamp and a pattern, it returns a `datetime.datetime`_ object based on the pattern provided
* and the pattern provided means

  - ``%d`` is for days
  - ``%m`` is for months
  - ``%y`` is for 2 digit years
  - ``%H`` is for hours
  - ``%M`` is for minutes

  there are more details in `strftime() and strptime() behavior <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior>`_

.. _test_subtracting_datetime_objects:

test_subtracting_datetime_objects
#################################################################################

.. _test_subtracting_datetime_objects_red:

red: make it fail
---------------------------------------------------------------------------------

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

  def assertWakeTimeEarlier(self, wake_time=None, sleep_time=None):
  ...


the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: datetime.timedelta(seconds=3600) != 1

.. _test_subtracting_datetime_objects_green:

green: make it pass
---------------------------------------------------------------------------------

I copy the value on the left of the :ref:`AssertionError` and change the expected value in the test to make it pass

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
          datetime.timedelta(seconds=3600)
      )

.. _test_subtracting_datetime_objects_refactor:

refactor: make it better
---------------------------------------------------------------------------------

* I add a `static method`_ to remove the repetition of the call to `datetime.datetime.strptime`_ with the same timestamp pattern

  .. code-block:: python

    @staticmethod
    def get_datetime(wake_time):
        return datetime.datetime.strptime(
            wake_time, '%d/%m/%y %H:%M'
        )

    def test_datetime_objects(self):
    ...

* then call it in ``test_datetime_objects``

  .. code-block:: python

    def test_datetime_objects(self):
        self.assertEqual(
            self.get_datetime("21/11/06 16:30"),
            datetime.datetime(
                2006, 11, 21, 16, 30
            )
        )

* and ``test_subtracting_datetime_objects``

  .. code-block:: python

    def test_subtracting_datetime_objects(self):
        sleep_time = self.get_datetime(
            '21/11/06 16:30'
        )
        wake_time = self.get_datetime(
            '21/11/06 17:30'
        )

        self.assertEqual(
            wake_time-sleep_time,
            datetime.timedelta(seconds=3600)
        )

I can convert a string_ to a `datetime.datetime`_ object by using `datetime.datetime.strptime`_ and subtract one `datetime.datetime`_ object from another to get a `datetime.timedelta`_ object

.. _test_converting_timedelta_to_a_string:

test_converting_timedelta_to_a_string
#################################################################################

.. _test_converting_timedelta_to_a_string_red:

red: make it fail
---------------------------------------------------------------------------------

I want the result as a string_ not a `datetime.timedelta`_  object. I add a test to see what happens when I call the str_ constructor_ with it

.. code-block:: python

  def test_converting_timedelta_to_a_string(self):
      self.assertEqual(
          str(datetime.timedelta(seconds=1234)),
          ''
      )

  def assertWakeTimeEarlier(self, wake_time=None, sleep_time=None):
  ...

the terminal shows an :ref:`AssertionError` with a string_

.. code-block:: python

  AssertionError: '0:20:34' != ''

.. _test_converting_timedelta_to_a_string_green:

green: make it pass
---------------------------------------------------------------------------------

I make the expected value in the test match the value from the terminal

.. code-block:: python

  def test_converting_timedelta_to_a_string(self):
      self.assertEqual(
          str(datetime.timedelta(seconds=1234)),
          '0:20:34'
      )

and the tests passes. From these tests, I know I can

* convert a string_ to a `datetime.datetime`_ object using `datetime.datetime.strptime`_
* subtract one `datetime.datetime`_ object from another to get a `datetime.timedelta`_ object
* convert a `datetime.timedelta`_ object to a string_

----

.. _test_duration_w_date_and_time_green_1:

* I remove the `unittest.skip decorator`_ from ``test_duration_w_date_and_time`` and get back the ValueError_, the test calls ``duration`` which calls ``read_timestamp`` in ``sleep_duration.py``, that cannot process timestamps that have dates because it still uses the int_ constructor_
* I make a copy of the ``duration`` :ref:`function<functions>` in ``sleep_duration.py`` and change the name to ``duration_a`` to keep the working solution while I try a new one
* then remove ``difference_hours``, ``difference_minutes``, ``duration_hours``, ``duration_minutes`` and ``difference`` from ``duration_a`` and change the `return statement`_

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

  and the terminal shows the same ValueError_

  .. code-block:: python

    ValueError: invalid literal for int() with base 10: '31/12/99 22'

  ``test_duration_w_date_and_time`` calls ``get_difference`` which has the old calculations that use the int_ constructor_
* I remove the call to ``get_difference`` from ``test_duration_w_date_and_time``

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
                None
            )

* change the assertion in ``test_duration_w_date_and_time`` to call ``duration_a``

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
                sleep_duration.duration_a(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                self.get_difference(
                    wake_time, sleep_time
                )
            )

* then add a new calculation that calls ``get_datetime`` in the test, and change the expectation in the assertion

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
            difference = (
                self.get_datetime(wake_time)
              - self.get_datetime(sleep_time)
            )
            self.assertEqual(
                sleep_duration.duration_a(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(difference)
            )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != '0:53:00'
    AssertionError: None != '7:59:00'
    AssertionError: None != '9:02:00'
    AssertionError: None != '10:16:00'

* I add the calculation to ``duration_a`` and change the `return statement`_

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            difference = (
                get_datetime(wake_time)
              - get_datetime(sleep_time)
            )
            return str(difference)

  and get a NameError_

  .. code-block:: python

    NameError: name 'get_datetime' is not defined

* I add the :ref:`function<functions>` to call `datetime.datetime.strptime`_ with a pattern by copying the ``get_datetime`` method from ``test_sleep_duration.py``

  .. code-block:: python

    def get_datetime(timestamp):
        return datetime.datetime.strptime(
            timestamp,
            '%d/%m/%y %H:%M'
        )


    def duration_a(wake_time=None, sleep_time=None):
    ...

  the terminal shows another NameError_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

* I add an `import statement`_ to the top of ``sleep_duration.py``

  .. code-block:: python

    import datetime


    def read_timestamp(timestamp=None, index=0):
    ...

  and the test passes with no random failures! Fantastic!!

.. _test_duration_w_date_and_time_refactor:

*********************************************************************************
refactor: make it better
*********************************************************************************

* I remove the ``difference`` variable and return the calculation directly

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

* then remove

  - ``duration`` and
  - ``read_timestamp``

  because ``duration_a`` is a better solution, the terminal shows an :ref:`AttributeError`

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

  - ``get_difference`` because no one is calling it, and
  - ``test_converting_timedelta_to_a_string``
  - ``test_subtracting_datetime_objects``
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

  I add dates to the calls in the test

  .. code-block:: python

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
            difference = (
                self.get_datetime(wake_time)
              - self.get_datetime(sleep_time)
            )
            self.assertEqual(
                sleep_duration.duration_a(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(difference)
            )

  and the terminal shows green again. I can now test ``duration`` with any dates and times

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
            difference = (
                self.get_datetime(wake_time)
              - self.get_datetime(sleep_time)
            )
            self.assertEqual(
                sleep_duration.duration_a(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(difference)
            )

* I change the date for ``sleep_time`` to test it

  .. code-block:: python

    sleep_time = random_timestamp('30/12/99')

  still green, then change it to a date that cannot exist

  .. code-block:: python

    sleep_time = random_timestamp('32/12/99')

  and the test is stuck in a loop. I have a problem, I change the date back

  .. code-block:: python

    sleep_time = random_timestamp('31/12/99')

  green again

* When I change the date for ``wake_date``

  .. code-block:: python

    wake_date = '30/12/99'

  the test is stuck in a loop that does not end because ``wake_date`` is earlier than the date for ``sleep_time``, another problem. When I change it to a date that does not exist

  .. code-block:: python

    wake_date = '32/12/99'

  the terminal shows a get a ValueError_

  .. code-block:: python

    ValueError: time data '32/12/99 01:11' does not match format '%d/%m/%y %H:%M'

  this is better. I want the same thing to happen when I use a date that does not exist for ``sleep_time``
* I change ``wake_time`` back and change ``sleep_time`` again to cause the loop to not end, then change the `while statement`_ to call ``get_datetime``

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        sleep_time = random_timestamp('32/12/99')

        wake_date = '31/12/99'
        wake_time = random_timestamp(wake_date)

        while (
            self.get_datetime(wake_time)
          < self.get_datetime(sleep_time)
        ):
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp(
                wake_date
            )
        else:
            difference = (
                self.get_datetime(wake_time)
              - self.get_datetime(sleep_time)
            )
            self.assertEqual(
                sleep_duration.duration_a(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(difference)
            )

  the terminal shows a ValueError_

  .. code-block:: python

    ValueError: time data '32/12/99 08:15' does not match format '%d/%m/%y %H:%M'
    ValueError: time data '32/12/99 09:36' does not match format '%d/%m/%y %H:%M'
    ValueError: time data '32/12/99 10:27' does not match format '%d/%m/%y %H:%M'
    ValueError: time data '32/12/99 19:27' does not match format '%d/%m/%y %H:%M'

  good! I want bad dates to cause an error. I change ``sleep_time`` back to a real date, and the test is green again.

* I change ``wake_date`` to an earlier date to cause the loop that does not end

  .. code-block:: python

    wake_date = '30/12/99'

  then add a variable and use it to fix the problem of the loop that does not end when ``wake_date``  is earlier than the date for ``sleep_time``

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        sleep_date = '31/12/99'
        sleep_time = random_timestamp(sleep_date)

        wake_date = '31/12/99'
        wake_time = random_timestamp(wake_date)

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_date = sleep_date
            wake_time = random_timestamp(
                wake_date
            )
        else:
            difference = (
                self.get_datetime(wake_time)
              - self.get_datetime(sleep_time)
            )
            self.assertEqual(
                sleep_duration.duration_a(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(difference)
            )

  the loop ends and the terminal shows green again, I change ``wake_date`` back
* then remove the ``difference`` variable from the test to do the calculation directly

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        sleep_date = '31/12/99'
        sleep_time = random_timestamp(sleep_date)

        wake_date = '31/12/99'
        wake_time = random_timestamp(wake_date)

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_date = sleep_date
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
                    self.get_datetime(wake_time)
                  - self.get_datetime(sleep_time)
                )
            )

  the terminal still shows green

.. _test_get_datetime:

test_get_datetime
#################################################################################

* I want to add a test for the ``get_datetime`` :ref:`function<functions>` in the ``sleep_duration`` :ref:`module<ModuleNotFoundError>`. I change ``test_datetime_objects`` to ``test_get_datetime`` and make it reference ``sleep_duration.get_datetime`` because they are the same

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

  still green! The test has a problem, the values never change. I want to test the :ref:`function<functions>` with random timestamps

* I add a new variable and change the assertion

  .. code-block:: python

    def test_get_datetime(self):
        timestamp = random_timestamp('31/12/99')
        self.assertEqual(
            sleep_duration.get_datetime(
                timestamp
            ),
            datetime.datetime.strptime(
                timestamp, '%d/%m/%y %H:%M'
            )
        )

  the terminal still shows green

* I remove ``get_datetime`` :ref:`method<functions>` from ``test_sleep_duration.py`` because ``test_get_datetime`` covers what it does, and get an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: 'TestSleepDuration' object has no attribute 'get_datetime'. Did you mean: 'test_get_datetime'?

  I change all the calls from ``self.get_datetime`` to ``sleep_duration.get_datetime``

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
            wake_date = sleep_date
            wake_time = random_timestamp(wake_date)
        else:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(
                    sleep_duration.get_datetime(wake_time)
                  - sleep_duration.get_datetime(sleep_time)
                )
            )

  the terminal shows green again

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
  - converted a string_ to a `datetime.datetime`_ object using the `datetime.datetime.strptime`_ :ref:`method<functions>`

* `test_subtracting_datetime_objects`_
* `test_converting_timedelta_to_a_string`_
* :ref:`test_duration_w_hours<test_duration_w_hours>`
* :ref:`test_duration_calculation`
* :ref:`test_duration_w_an_earlier_wake_than_sleep_time<test_duration_w_an_earlier_wake_than_sleep_time>`
* :ref:`test_duration_w_hours_and_minutes<test_duration_w_hours_and_minutes>`
* `test_get_datetime`_
* `test_duration_w_date_and_time`_ where I used

  - `random.randint`_ to generate random numbers for hours and minutes
  - that are :doc:`interpolated </how_to/pass_values>` in timestamps with dates as inputs for ``wake_time`` and ``sleep_time``
  - a `while statement`_ to make sure that when ``wake_time`` is earlier than ``sleep_time`` the ``duration`` :ref:`function<functions>` raises a ValueError_ with a message
  - and returns the right difference when ``wake_time`` is later than or the same as ``sleep_time``

I also encountered the following exceptions

* :ref:`AssertionError`
* :ref:`TypeError`
* NameError_
* :ref:`AttributeError`
* ValueError_

Would you like to :ref:`write the solution using test_sleep_duration.py<test_duration_tests>` only?

----

:doc:`/code/code_sleep_duration`