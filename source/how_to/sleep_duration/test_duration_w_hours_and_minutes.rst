.. include:: ../../links.rst

.. _test_duration_w_hours_and_minutes:

#############################################################################
how to measure sleep duration: test_duration_w_hours_and_minutes
#############################################################################

This is part 2 of 5 where I show an approach to writing a program that calculates the difference between a given wake and sleep time.

.. contents:: table of contents
  :local:
  :depth: 2

----

The ``duration`` :ref:`function<functions>` has only been tested with timestamps that have random hours and ``00`` as minutes. For it to meet the requirements, it should accept timestamps with random hours and random minutes.

.. _test_duration_w_hours_and_minutes_red:

*****************************************************************************
red: make it fail
*****************************************************************************

* I copy ``test_duration_w_hours`` in ``test_sleep_duration.py`` and paste it below the original
* then rename the copy to ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        wake_time = random_timestamp()
        sleep_time = random_timestamp()

        self.assertEqual(
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            ),
            (
                int(wake_time.split(':')[0])
               -int(sleep_time.split(':')[0])
            )
        )

* and add a variable for the calculation of the difference in hours

  .. code-block:: python

    difference_hours = (
        int(wake_time.split(':')[0])
        -int(sleep_time.split(':')[0])
    )

    self.assertEqual(
        sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        difference_hours
    )

* I change the expectation to include minutes in the duration

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        f'{difference_hours:02}:00'
    )

  which gives me an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: -3 != '-3:00'
    AssertionError: 0 != '00:00'
    AssertionError: 8 != '08:00'
    AssertionError: 16 != '16:00'

  the ``duration`` :ref:`function<functions>` returns a number and the tests expects a timestamp string_

.. _test_duration_w_hours_and_minutes_green:

*****************************************************************************
green: make it pass
*****************************************************************************

* I change it to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference_hours = (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )

        return f'{difference_hours:02}:00'

  and the terminal shows an :ref:`AssertionError` for ``test_duration_w_hours``

  .. code-block:: python

    AssertionError: '-12:00' != -12
    AssertionError: '-5:00' != -5
    AssertionError: '-2:00' != -2
    AssertionError: '03:00' != 3

  it still expects the previous format. I change it to match

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_time = random_timestamp()
        sleep_time = random_timestamp()

        difference_hours = (
            int(wake_time.split(':')[0])
           -int(sleep_time.split(':')[0])
        )

        self.assertEqual(
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            ),
            f'{difference_hours:02}:00'
        )

  and the test passes

.. _test_duration_w_hours_and_minutes_refactor:

*****************************************************************************
refactor: make it better
*****************************************************************************

* ``test_duration_w_hours`` and ``test_duration_w_hours_and_minutes`` are now the same test so I remove ``test_duration_w_hours``
* I want to subtract the minutes of ``sleep_time`` from ``wake_time`` and add a variable for it in the test

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        wake_time = random_timestamp()
        sleep_time = random_timestamp()

        difference_hours = (
            int(wake_time.split(':')[0])
           -int(sleep_time.split(':')[0])
        )
        difference_minutes = (
            int(wake_time.split(':')[1])
           -int(sleep_time.split(':')[1])
        )

        self.assertEqual(
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            ),
            f'{difference_hours:02}:{difference_minutes:02}'
        )

  the terminal still shows passing tests because ``random_timestamp`` returns timestamps that always have ``00`` as minutes

* When I change it to return random numbers from ``0`` up to and including ``59`` for the minutes by using `random.randint`_

  .. code-block:: python

    def random_timestamp():
        return (
            f'{random.randint(0,23):02}:'
            f'{random.randint(0,59):02}'
        )

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '-18:00' != '-18:44'
    AssertionError: '18:00' != '18:-10'
    AssertionError: '-2:00' != '-2:-26'
    AssertionError: '16:00' != '16:-25'

  the ``duration`` :ref:`function<functions>` always returns ``00`` for the minutes part of the duration. I add a variable for the difference in minutes by copying ``difference_hours``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference_hours = (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )
        difference_minutes = (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )

        return (
            f'{difference_hours:02}:'
            f'{difference_minutes:02}'
        )

  the terminal shows another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '20:20' != '20:-6'
    AssertionError: '06:06' != '06:17'
    AssertionError: '-16:-16' != '-16:-7'
    AssertionError: '02:02' != '02:07'

  the ``duration`` :ref:`function<functions>` returns the same numbers for hours and minutes and the test expects the difference between the minutes of ``wake_time`` and ``sleep_time``. I make a copy of the ``get_hour`` :ref:`function<functions>` and call it ``get_minutes`` with the index for the second item from splitting the timestamp

  .. code-block:: python

    def get_minutes(timestamp):
        return int(timestamp.split(':')[1])

  then replace the calls in ``difference_minutes``

  .. code-block:: python

    difference_minutes = (
        get_minutes(wake_time)
      - get_minutes(sleep_time)
    )

  all tests are still passing though there is something wrong with this calculation

*****************************************************************************
review
*****************************************************************************

The challenge is to write a program that calculates the difference between a given wake and sleep time. I ran the following tests to get something that comes close to doing it


* :ref:`test_string_splitting`
* :ref:`test_converting_strings_to_numbers`
* :ref:`test_duration_w_hours`
* `test_duration_w_hours_and_minutes`_ where I

  - used `random.randint`_ to generate random numbers

    * from the 24 hours in a day
    * and the 60 minutes in an hour

  - then :doc:`interpolated </how_to/pass_values>` them in the timestamps
  - and test that the ``duration`` :ref:`function<functions>` subtracts

    * the hour for ``sleep_time`` from the hour for ``wake_time``
    * and the minutes for ``sleep_time`` from the minutes for ``wake_time``

Would you like to :ref:`test the duration calculation<test_duration_calculation>`?

----

:doc:`/code/code_sleep_duration`