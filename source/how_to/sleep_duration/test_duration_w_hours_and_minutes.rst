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

    ...
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

  the ``duration`` :ref:`function<functions>` returns a number and the tests expects the duration as a string_

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
* I add a variable to subtract the minutes of ``sleep_time`` from ``wake_time``

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
    ...

* then update the expectation to use the variable for the minutes

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            f'{difference_hours:02}:'
            f'{difference_minutes:02}'
        )
    )

  the terminal still shows passing tests because ``random_timestamp`` returns timestamps that always have ``00`` as minutes

* When I change it to return random numbers from ``0`` up to and including ``59`` for the minutes by using `random.randint`_

  .. code-block:: python

    def random_timestamp():
        return (
            f'{random.randint(0,23):02}:'
            f'{random.randint(0,59):02}'
        )

  I get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '-18:00' != '-18:44'
    AssertionError: '18:00' != '18:-10'
    AssertionError: '-2:00' != '-2:-26'
    AssertionError: '16:00' != '16:-25'

  the ``duration`` :ref:`function<functions>` always returns ``00`` for the minutes part of the duration. I add a variable for the difference in minutes by copying ``difference_hours``, renaming it and adding it to the return statement

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

  the ``duration`` :ref:`function<functions>` returns the same numbers for hours and minutes and the test expects the difference between the minutes of ``wake_time`` and ``sleep_time``. I make a copy of the ``get_hour`` :ref:`function<functions>`, call it ``get_minutes`` then change the index to get the second item from splitting the timestamp

  .. code-block:: python

    def get_minutes(timestamp):
        return int(timestamp.split(':')[1])

  and replace the calls in ``difference_minutes``

  .. code-block:: python

    difference_minutes = (
        get_minutes(wake_time)
      - get_minutes(sleep_time)
    )

  the terminal shows passing tests! Something is wrong with this calculation...

.. _test_duration_calculation:

test_duration_calculation
#############################################################################

The ``duration`` :ref:`function<functions>` currently returns a subtraction of hours and a subtraction of minutes which is not correct for calculating the difference between two timestamps

.. _test_duration_calculation_red:

red: make it fail
-----------------------------------------------------------------------------

If ``duration`` is given a ``wake_time`` of ``'03:30'`` and a ``sleep_time`` of ``'02:59'``, it should return ``'00:31'`` as the difference between the timestamps

.. code-block:: python

  def test_duration_calculation(self):
      self.assertEqual(
          sleep_duration.duration(
              wake_time='03:30',
              sleep_time='02:59'
          ),
          '00:31'
      )

but the terminal shows this :ref:`AssertionError` when I add ``test_duration_calculation``

.. code-block:: python

  AssertionError: '01:-29' != '00:31'

the ``duration`` :ref:`function<functions>` returns ``'01:-29'`` which is not a real duration. I need to change the calculation

.. _test_duration_calculation_green:

green: make it pass
-----------------------------------------------------------------------------

* I rename ``duration`` to keep a copy of my current working solution

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
        difference_hours = (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )
        difference_minutes = (
            get_minutes(wake_time)
          - get_minutes(sleep_time)
        )

        return f'{difference_hours:02}:{difference_minutes:02}'

* then add a new ``duration`` :ref:`function<functions>` with the following steps to calculate a real difference between the two timestamps

  - get total minutes for each timestamp by multiplying the hour by 60 and adding the minutes
  - get the difference by subtracting total ``sleep_time`` minutes from total ``wake_time`` minutes
  - return the difference between total ``wake_time`` and total ``sleep_time`` minutes as hours and minutes by

    * using `floor (integer) division`_ to get the whole number value of dividing the difference by 60 for the hours
    * using the modulo_ operator to get the remainder from dividing the difference by 60 for the minutes

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time_minutes = (
            (get_hour(wake_time) * 60)
           + get_minutes(wake_time)
        )
        sleep_time_minutes = (
            (get_hour(sleep_time) * 60)
           + get_minutes(sleep_time)
        )

        difference = (
            wake_time_minutes
          - sleep_time_minutes
        )
        difference_hours = difference // 60
        difference_minutes = difference % 60

        return f'{difference_hours:02}:{difference_minutes:02}'

  ``test_duration_calculation`` passes and since ``test_duration_w_hours_and_minutes`` uses the wrong calculation, the terminal shows random successes or :ref:`AssertionErrors<AssertionError>`

  .. code-block:: python

    AssertionError: '10:53' != '11:-7'
    AssertionError: '01:59' != '02:-1'
    AssertionError: '06:54' != '07:-6'
    AssertionError: '-16:26' != '-15:-34'

* I add the correct calculation to ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        wake_time = random_timestamp()
        sleep_time = random_timestamp()
        wake_time_minutes = (
            (int(wake_time.split(':')[0]) * 60)
           + int(wake_time.split(':')[1])
        )
        sleep_time_minutes = (
            (int(sleep_time.split(':')[0]) * 60)
           + int(sleep_time.split(':')[1])
        )
        difference = (
            wake_time_minutes
          - sleep_time_minutes
        )
        difference_hours = difference // 60
        difference_minutes = difference % 60

        self.assertEqual(
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            ),
            f'{difference_hours:02}:{difference_minutes:02}'
        )

  and I have passing tests again! I will sleep easier tonight!!

.. _test_duration_calculation_refactor:

refactor: make it better
-----------------------------------------------------------------------------

* I remove ``test_duration_calculation`` from ``test_sleep_duration.py`` because it is now covered by ``test_duration_w_hours_and_minutes`` which has the correct calculation
* I remove ``duration_a`` from ``sleep_duration.py`` since the working solution in ``duration`` is better
* and then I write a :ref:`function<functions>` to get the total minutes from a timestamp and call it in ``duration``

  .. code-block:: python

    def get_total_minutes(timestamp):
        return (
            (get_hour(timestamp) * 60)
           + get_minutes(timestamp)
        )

    def duration(wake_time=None, sleep_time=None):
        wake_time_minutes = get_total_minutes(wake_time)
        sleep_time_minutes = get_total_minutes(sleep_time)

        difference = (
            wake_time_minutes
          - sleep_time_minutes
        )
        difference_hours = difference // 60
        difference_minutes = difference % 60

        return f'{difference_hours:02}:{difference_minutes:02}'

  the terminal still shows passing tests

* I also write a :ref:`function<functions>` to replace ``get_hour`` and ``get_minutes`` then call it in ``get_total_minutes``

  .. code-block:: python

    def parse_timestamp(timestamp=None, index=0):
        return int(timestamp.split(':')[index])

    def get_total_minutes(timestamp):
        return (
            (parse_timestamp(timestamp, 0) * 60)
           + parse_timestamp(timestamp, 1)
        )

  we are still green

* since all the tests are passing, I remove ``get_hour`` and ``get_minutes`` because they have been replaced by ``parse_timestamp``


test_floor_aka_integer_division
#############################################################################

I just added two things so I add tests for them. The ``//`` operator returns a whole number that tells how many times the bottom number can be multiplied to get a whole number that is equal to or as close to the top number as possible

.. _test_floor_aka_integer_division_red:

red: make it fail
-----------------------------------------------------------------------------

I add a failing test for it

.. code-block:: python

  def test_floor_aka_integer_division(self):
      self.assertEqual(120//60, 0)

  def test_duration_w_hours_and_minutes(self):
  ...

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 2 != 0

.. _test_floor_aka_integer_division_green:

green: make it pass
-----------------------------------------------------------------------------

I change the expectation in the test to the correct value. The result of dividing ``120`` by ``60`` is ``2`` with a remainder of ``0``

.. code-block:: python

  self.assertEqual(120//60, 2)

and it passes

.. _test_floor_aka_integer_division_refactor:

refactor: make it better
-----------------------------------------------------------------------------

I add another assertion

.. code-block:: python

  self.assertEqual(150//60, 0)

and get an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 2 != 0

then I change the expected value for it to the correct value. The result of dividing ``150`` by ``60`` is also ``2`` but with a remainder of ``30``

.. code-block:: python

  self.assertEqual(150//60, 2)

and the terminal shows passing tests

.. _test_modulo_operation

test_modulo_operation
#############################################################################

The ``%`` operator returns the remainder from dividing one number by another

.. _test_modulo_operation_red:

red: make it fail
-----------------------------------------------------------------------------

I add a failing test for it

.. code-block:: python

  def test_modulo_operation(self):
      self.assertEqual(120%60, 2)

  def test_duration_w_hours_and_minutes(self):
  ...

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 0 != 2

.. _test_modulo_operation_green:

green: make it pass
-----------------------------------------------------------------------------

I change the expectation in the test to the correct value. The remainder from dividing ``120`` by ``60`` is ``0``

.. code-block:: python

  self.assertEqual(120%60, 0)

and the test passes

.. _test_modulo_operation_refactor:

refactor: make it better
-----------------------------------------------------------------------------

I add another assertion

.. code-block:: python

  self.assertEqual(150%60, 2)

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 30 != 2

then I change the expected value in the test to the correct value. The remainder from dividing ``150`` by ``60`` is ``30``

.. code-block:: python

  self.assertEqual(150%60, 30)

things are green again

----

*****************************************************************************
review
*****************************************************************************

The challenge is to write a program that calculates the difference between a given wake and sleep time. I ran the following tests to get something that comes close to doing it


* :ref:`test_string_splitting` where I

  - used the `str.split`_ :ref:`method<functions>` I found by calling the `help system`_ to split a string_ on a separator
  - and indexed the :doc:`list </data_structures/lists/lists>` from the split to get specific items

* :ref:`test_converting_strings_to_numbers` with the int_ constructor
* `test_floor_aka_integer_division`_
* `test_modulo_operation`_
* :ref:`test_duration_w_hours`
* :ref:`test_duration_w_hours_and_minutes` where I

  - used `random.randint`_ to generate random numbers

    * from the 24 hours in a day
    * and the 60 minutes in an hour

  - then :doc:`interpolated </how_to/pass_values>` them in the timestamps
  - and `test_duration_calculation`_ to make sure that the ``duration`` :ref:`function<functions>` calculates the difference between ``wake_time`` and ``sleep_time`` by

    * converting the timestamp to minutes
    * subtracting the total minutes of ``sleep_time`` from ``wake_time``
    * and converting the difference to a duration in hours and minutes by using `floor (integer) division`_ and the modulo_ operator

Would you like to :ref:`test duration with an earlier wake than sleep time<test_duration_w_earlier_wake_than_sleep_time>`?

----

:doc:`/code/code_sleep_duration`