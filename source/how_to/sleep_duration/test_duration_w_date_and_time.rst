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

* I make a copy of ``random_timestamp``, rename it, then add a date to the `return statement`_

  .. code-block:: python

    def random_timestamp_a():
        return (
            '31/12/99 '
            f'{random.randint(0,23):02}:'
            f'{random.randint(0,59):02}'
        )

* and make a copy of ``test_duration_w_hours_and_minutes`` and rename it ``test_duration_w_date_and_time``
* then add calls to ``random_timestamp_a``

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        wake_time = random_timestamp_a()
        sleep_time = random_timestamp_a()

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time, sleep_time
            )
            wake_time = random_timestamp_a()
        else:
            ...

  and get a ValueError_

  .. code-block:: python

    ValueError: invalid literal for int() with base 10: '31/12/99 03'
    ValueError: invalid literal for int() with base 10: '31/12/99 07'
    ValueError: invalid literal for int() with base 10: '31/12/99 11'
    ValueError: invalid literal for int() with base 10: '31/12/99 21'

  the test tried to convert the timestamp string_ to a number to calculate ``difference_hours`` but it is in the wrong format

.. _test_duration_w_date_and_time_green_0:

*********************************************************************************
green: make it pass
*********************************************************************************

* I add the `unittest.skip decorator`_ to ``test_duration_w_date_and_time``
* then add an assertion to ``test_converting_strings_to_numbers`` to recreate the error

  .. code-block:: python

    def test_converting_strings_to_numbers(self):
        self.assertEqual(int('12'), 12)
        self.assertEqual(int('01'), 1)
        int('31/12/99 01')

  the terminal shows a ValueError_ with the same message from ``test_duration_w_date_and_time``

  .. code-block:: python

    ValueError: invalid literal for int() with base 10: '31/12/99 13'

  I cannot convert a string_ in the format ``'31/12/99 13'`` to a number. I handle the ValueError_ with `assertRaises`_

  .. code-block:: python

    def test_converting_strings_to_numbers(self):
        self.assertEqual(int('12'), 12)
        self.assertEqual(int('01'), 1)

        with self.assertRaises(ValueError):
            int('31/12/99 01')

  and tests are green again

* The int_ constructor_ will not work when the timestamps have a date. I need a solution that can read the date and time. I search for `date and time <https://docs.python.org/3/search.html?q=time+difference>`_ in `python's online documentation`_, to see if there is an existing solution and select the datetime_ module from the results. Reading through the available types in the module I see `datetime.datetime`_ objects which are a combination of date and time

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

I add a test to ``test_sleep_duration.py`` based on `Examples of usage: datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_ for `datetime.datetime`_ objects

.. code-block:: python

  def test_datetime_objects(self):
      self.assertEqual(
          datetime.strptime(
              "21/11/06 16:30",
              "%d/%m/%y %H:%M"
          ),
          ''
      )

  def assertWakeTimeEarlier(self, wake_time, sleep_time):
  ...

and the terminal shows a NameError_ because ``datetime`` is not defined in ``test_sleep_duration.py``, I need to import it

.. code-block:: python

  NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

.. _test_datetime_objects_green:

green: make it pass
---------------------------------------------------------------------------------

* I add an `import statement`_ for the datetime_ module,

  .. code-block:: python

    import datetime
    import random
    import sleep_duration
    import unittest
    ...

  and the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'datetime' has no attribute 'strptime'

  the reference to the ``strptime`` :ref:`method<functions>` is not right, my `import statement`_ is different than `the example in the documentation <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_. I update the call

  .. code-block:: python

    self.assertEqual(
        datetime.datetime.strptime(
            "21/11/06 16:30",
            "%d/%m/%y %H:%M"
        ),
        ''
    )

  and get an :ref:`AssertionError`,

  .. code-block:: python

    AssertionError: datetime.datetime(2006, 11, 21, 16, 30) != ''

  I copy the value on the left side of the :ref:`AssertionError` to replace the expected value in the test,

  .. code-block:: python

    self.assertEqual(
        datetime.datetime.strptime(
            "21/11/06 16:30",
            "%d/%m/%y %H:%M"
        ),
        datetime.datetime(
            2006, 11, 21, 16, 30
        )
    )

  and the test passes. From this test I see that

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

  def assertWakeTimeEarlier(self, wake_time, sleep_time):
  ...


the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: datetime.timedelta(seconds=3600) != 1

.. _test_subtracting_datetime_objects_green:

green: make it pass
---------------------------------------------------------------------------------

I copy the value on the left of the :ref:`AssertionError` and replace the expected value in the test to make it pass

.. code-block:: python

  self.assertEqual(
      wake_time-sleep_time,
      datetime.timedelta(seconds=3600)
  )

.. _test_subtracting_datetime_objects_refactor:

refactor: make it better
---------------------------------------------------------------------------------

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
      ...

from the passing tests I can

- convert a string_ to a `datetime.datetime`_ object by using `datetime.datetime.strptime`_
- subtract one `datetime.datetime`_ object from another to get a `datetime.timedelta`_ object

.. _test_converting_timedelta_to_a_string:

test_converting_timedelta_to_a_string
#################################################################################

.. _test_converting_timedelta_to_a_string_red:

red: make it fail
---------------------------------------------------------------------------------

* I want the result as a string_ not a `datetime.timedelta`_ . I add a test to see what happens when I pass it to the str_ constructor_

  .. code-block:: python

    def test_converting_timedelta_to_a_string(self):
        self.assertEqual(
            str(datetime.timedelta(seconds=1234)),
            ''
        )

    def assertWakeTimeEarlier(self, wake_time, sleep_time):
    ...

  the terminal shows an :ref:`AssertionError` with a string_ like what I want

  .. code-block:: python

    AssertionError: '0:20:34' != ''

.. _test_converting_timedelta_to_a_string_green:

green: make it pass
---------------------------------------------------------------------------------

I make the expected value in the test match the value from the terminal

.. code-block:: python

  self.assertEqual(
      str(datetime.timedelta(seconds=1234)),
      '0:20:34'
  )

and we are green. From the tests, I know I can

* convert a string_ to a `datetime.datetime`_ object using `datetime.datetime.strptime`_
* subtract one `datetime.datetime`_ object from another to get a `datetime.timedelta`_ object
* convert a `datetime.timedelta`_ object to a string_

----

.. _test_duration_w_date_and_time_green_1:

* I remove the `unittest.skip decorator`_ from ``test_duration_w_date_and_time`` and get back the :ref:`ValueError`, the test calls ``duration`` which calls ``read_timestamp`` :ref:`function<functions>` in ``sleep_duration.py``. ``read_timestamp`` cannot process timestamps that have dates because it still uses the int_ constructor_
* I make a copy of the ``duration`` :ref:`function<functions>` in ``sleep_duration.py`` and rename it to ``duration_a`` to keep the existing working solution while I try a new one
* then change the assertion in ``test_duration_w_date_and_time`` to call ``duration_a``

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration_a(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        self.get_difference(
            wake_time, sleep_time
        )
    )

* I remove ``difference_hours`` and ``difference_minutes`` from ``duration_a``
* then change the calculation for difference to use `datetime.datetime.strptime`_

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
        wake_datetime = datetime.datetime.strptime(
            wake_time, '%d/%m/%y %H:%M'
        )
        ...

  which gives me a NameError_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

  You know I did, the same thing happened earlier when I tested the datetime_ module

* I add an `import statement`_ to the top of the file

  .. code-block:: python

    import datetime


    def read_timestamp(timestamp=None, index=0):
    ...

  the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: unsupported operand type(s) for %: 'datetime.timedelta' and 'int'

  I cannot use the modulo_ operation on a `datetime.timedelta`_ object
* I remove ``duration_hours`` and ``duration_minutes`` and change the `return statement`_

  .. code-block:: python

    return str(difference)

  the terminal shows another ValueError_

  .. code-block:: python

    ValueError: invalid literal for int() with base 10: '31/12/99 17'
    ValueError: invalid literal for int() with base 10: '31/12/99 18'
    ValueError: invalid literal for int() with base 10: '31/12/99 21'
    ValueError: invalid literal for int() with base 10: '31/12/99 22'

  the calculation in ``get_difference`` still use the int_ constructor_
* I make a copy of ``get_difference``, rename it to ``get_difference_a`` and change the calculations to use the `datetime.datetime.strptime`_ :ref:`method<functions>`

  .. code-block:: python

    @staticmethod
    def get_difference_a(wake_time, sleep_time):
        difference = (
            datetime.datetime.strptime(
                wake_time, '%d/%m/%y %H:%M'
            )
          - datetime.datetime.strptime(
                wake_time, '%d/%m/%y %H:%M'
            )
        )
        return str(difference)

  then add calls to it in ``test_duration_w_date_and_time``

  .. code-block:: python

    else:
        self.assertEqual(
            sleep_duration.duration_a(
                wake_time=wake_time,
                sleep_time=sleep_time
            ),
            self.get_difference_a(
                wake_time, sleep_time
            )
        )

  and the test passes with no random failures. Fantastic!

.. _test_duration_w_date_and_time_refactor:

*********************************************************************************
refactor: make it better
*********************************************************************************


* I add a :ref:`function<functions>` that calls  `datetime.datetime.strptime`_

  .. code-block:: python

    def get_datetime(timestamp):
        return datetime.datetime.strptime(
            timestamp,
            '%d/%m/%y %H:%M'
        )


    def duration_a(wake_time=None, sleep_time=None):
    ...

  then add calls to ``get_datetime`` in ``duration_a``

  .. code-block:: python

    else:
        difference = (
            get_datetime(wake_time)
          - get_datetime(sleep_time)
        )

        return str(difference)

  still green
* I remove the ``difference`` variable and return the calculation directly

  .. code-block:: python

    else:
        return str(
            wake_datetime - sleep_datetime
        )

* I remove

  - ``read_timestamp`` in ``sleep_duration.py`` and
  - ``duration`` because ``duration_a`` is a better solution

  and get an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'sleep_duration' has no attribute 'duration'. Did you mean: 'duration_a'?

* I remove ``test_duration_w_hours_and_minutes`` since it is now covered by ``test_duration_w_date_and_time``
* I rename ``duration_a`` to ``duration`` in both files and the terminal shows all tests are still passing!
* then remove

  - ``test_converting_timedelta_to_a_string``
  - ``test_subtracting_datetime_objects`` and
  - ``test_datetime_objects``
  - ``test_the_modulo_operation``
  - ``test_floor_aka_integer_division``
  - ``test_converting_strings_to_numbers``
  - ``test_string_splitting``

  as they are not needed for the solution anymore
* I remove ``random_timestamp``
* then change ``random_timestamp_a`` to ``random_timestamp``
* the ``random_timestamp`` :ref:`function<functions>` always returns timestamps with the same date, I change it to take in dates as inputs

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

  I update the calls in the test

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        wake_time = random_timestamp('31/12/99')
        sleep_time = random_timestamp('31/12/99')
        while wake_time < sleep_time:
            wake_time = random_timestamp(
                '31/12/99'
            )

  green again. I can now test ``duration`` with any dates and times. I just cannot use dates that do not exist

* I add a variable for the pattern to remove the repetition and remove the commented code

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        wake_time = random_timestamp()
        sleep_time = random_timestamp()

        pattern = '%d/%m/%y %H:%M'
        wake_datetime = datetime.datetime.strptime(
            wake_time, pattern
        )
        sleep_datetime = datetime.datetime.strptime(
            sleep_time, pattern
        )
        ...

  still green

* I rename ``test_duration_w_date_and_time`` to ``test_duration``

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
* `test_duration_w_date_and_time`_ where I used

  - `random.randint`_ to generate random numbers for hours and minutes
  - that are :doc:`interpolated </how_to/pass_values>` in timestamps with dates as inputs for ``wake_time`` and ``sleep_time``
  - a `while statement`_ to make sure that ``wake_time`` is always later than or the same as ``sleep_time`` in the test
  - and that the ``duration`` :ref:`function<functions>` returns the right difference between  ``wake_time`` and ``sleep_time``

I also encountered the following exceptions

* :ref:`AssertionError`
* :ref:`TypeError`
* NameError_
* :ref:`AttributeError`
* ValueError_

Would you like to :ref:`write the solution using test_sleep_duration.py<test_duration_tests>` only?

----

:doc:`/code/code_sleep_duration`