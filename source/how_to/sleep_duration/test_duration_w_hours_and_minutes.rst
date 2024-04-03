.. include:: ../../links.rst

.. _test_duration_w_hours_and_minutes:

#############################################################################
how to measure sleep duration: test_duration_w_hours_and_minutes
#############################################################################

This is part 2 of an approach to writing a program that calculates the difference between a given wake and sleep time.

.. contents:: table of contents
  :local:
  :depth: 2

----

The ``duration`` :ref:`function<functions>` has only been tested with timestamps that have random hours and ``00`` as minutes. For it to meet the requirements, it should accept timestamps with random hours and random minutes.

.. _test_duration_w_hours_and_minutes_red:

*****************************************************************************
red: make it fail
*****************************************************************************

* I rename ``test_duration_w_hours`` to ``test_duration_w_hours_and_minutes``

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

  the ``duration`` :ref:`function<functions>` returns a number and the test expects a string_

* I change it to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference_hours = (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )

        return f'{difference_hours:02}:00'



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

* ``random_timestamp`` returns timestamps that always have ``00`` as minutes. When I change it to return random numbers from ``0`` up to and including ``59`` for the minutes by using `random.randint`_

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

  the ``duration`` :ref:`function<functions>` always returns ``00`` for the minutes part of the duration

.. _test_duration_w_hours_and_minutes_green:

*****************************************************************************
green: make it pass
*****************************************************************************

* I add a variable for the difference in minutes by copying ``difference_hours``, renaming it and adding it to the return statement

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

.. _test_duration_w_hours_and_minutes_refactor:

*****************************************************************************
refactor: make it better
*****************************************************************************

.. _test_duration_calculation:

test_duration_calculation
#############################################################################

The ``duration`` :ref:`function<functions>` returns a subtraction of hours and a subtraction of minutes which is not correct for calculating the difference between two timestamps

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

* I make a copy of ``duration`` to keep a copy of my current working solution and rename the original

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
    ...

* then change the return statement of the ``duration`` :ref:`function<functions>` to multiply ``difference_hours`` by ``60`` so I can convert the total difference to minutes

  .. code-block:: python

    return (
        difference_hours*60
      + difference_minutes
    )

  and get this :ref:`AssertionError` for ``test_duration_calculation``

  .. code-block:: python

    AssertionError: 31 != '00:31

  and an :ref:`AssertionError` for ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    AssertionError: -458 != '-7:-38'
    AssertionError: -936 != '-15:-36'
    AssertionError: -31 != '-1:29'
    AssertionError: 213 != '03:33'

  ``duration`` returns the difference as minutes but the tests expects them as hours and minutes. I need a way to convert minutes to hours and minutes

* I add the `unittest.skip decorator`_ to disable the failing tests while I find a solution

  .. code-block:: python

    @unittest.skip
    def test_duration_w_hours_and_minutes(self):
    ...

    @unittest.skip
    def test_duration_calculation(self):
    ...

test_floor_aka_integer_division
#############################################################################

The ``//`` operator returns a whole number that tells how many times the bottom number can be multiplied to get a whole number that is equal to or as close to the top number as possible. It should give me the hours when I divide by 60

.. _test_floor_aka_integer_division_red:

red: make it fail
-----------------------------------------------------------------------------

I add a failing test for it

.. code-block:: python

  def test_floor_aka_integer_division(self):
      self.assertEqual(120//60, 0)

  @unittest.skip
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

* I add another assertion

  .. code-block:: python

    self.assertEqual(150//60, 0)

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 2 != 0

  then I change the expected value for it to the correct value. The result of dividing ``150`` by ``60`` is also ``2`` but with a remainder of ``30``

  .. code-block:: python

    self.assertEqual(150//60, 2)

  and the terminal shows passing tests

* I comment out the `unittest.skip decorator`_ for ``test_duration_calculation`` with ``ctrl`` (windows/linux) or ``command`` (mac) and ``/`` on the keyboard

  .. code-block:: python

    # @unittest.skip
    def test_duration_calculation(self):

* then add a variable for the total difference as minutes in ``duration``

  .. code-block:: python

    ...
    difference = (
        difference_hours*60
      + difference_minutes
    )

    return difference

  I also add a variable for the duration as hours using `floor (integer) division`_

  .. code-block:: python

    duration_hours = difference // 60

  and change the return statement to the expected format

  .. code-block:: python

    return f'{duration_hours:02}:{difference_minutes:02}'

  then get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '00:-29' != '00:31'

  the hours part of the duration is correct but the minutes are still wrong. I need a way to get the remainder after dividing by ``60``

* I remove the comment on the `unittest.skip decorator`_ for ``test_duration_calculation`` with ``ctrl`` (windows/linux) or ``command`` (mac) and ``/`` on the keyboard

  .. code-block:: python

    @unittest.skip
    def test_duration_calculation(self):

  and the terminal shows green again

.. _test_modulo_operation:

test_modulo_operation
#############################################################################

The ``%`` operator returns the remainder from dividing one number by another, it should help me get the remainder

.. _test_modulo_operation_red:

red: make it fail
-----------------------------------------------------------------------------

I add a failing test for it

.. code-block:: python

  def test_modulo_operation(self):
      self.assertEqual(120%60, 2)

  @unittest.skip
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

* I add another assertion

  .. code-block:: python

    self.assertEqual(150%60, 0)

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 30 != 0

  then I change the expected value in the test to the correct value. The remainder from dividing ``150`` by ``60`` is ``30``

  .. code-block:: python

    self.assertEqual(150%60, 30)

  things are green again

* I comment out the `unittest.skip decorator`_ for ``test_duration_calculation`` with ``ctrl`` (windows/linux) or ``command`` (mac) and ``/`` on the keyboard
* then add a new variable to the ``duration`` :ref:`function<functions>` and reference it in the return statement

  .. code-block:: python

    duration_hours = difference // 60
    duration_minutes = difference % 60

    return (
        f'{duration_hours:02}:'
        f'{duration_minutes:02}'
    )

  the test passes

* I remove the `unittest.skip decorator`_ from ``test_duration_calculation``
* and comment it out for ``test_duration_w_hours_and_minutes`` with ``ctrl+/`` (windows/linux) or ``command+/`` (mac) on the keyboard

  .. code-block:: python

    # @unittest.skip
    def test_duration_w_hours_and_minutes(self):
    ...

  which gives me random successes and random :ref:`AssertionErrors<AssertionError>`

  .. code-block:: python

    AssertionError: '-11:46' != '-10:-14'
    AssertionError: '-6:04' != '-5:-56'
    AssertionError: '10:50' != '11:-10'
    AssertionError: '16:50' != '17:-10'

  the test is still using the wrong calculation. I change it to match the ``duration`` :ref:`function<functions>`

  .. code-block:: python

    difference = (
        difference_hours*60
      + difference_minutes
    )
    duration_hours = difference // 60
    duration_minutes = difference % 60

  then add the new variables in the expectation

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            f'{duration_hours:02}:'
            f'{difference_minutes:02}'
        )
    )

  and the test passes with no more random failures

* I remove ``test_duration_calculation`` from ``test_sleep_duration.py`` because it is now covered by ``test_duration_w_hours_and_minutes`` which has the correct calculation
* then remove ``duration_a`` from ``sleep_duration.py`` since the working solution in ``duration`` is better
* and write a :ref:`function<functions>` to replace ``get_hour`` and ``get_minutes``

  .. code-block:: python

    def parse_timestamp(timestamp=None, index=0):
        return int(timestamp.split(':')[index])

*  I call it in ``duration``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference_hours = (
            parse_timestamp(wake_time, 0)
          - parse_timestamp(sleep_time, 0)
        )
        difference_minutes = (
            parse_timestamp(wake_time, 1)
          - parse_timestamp(sleep_time, 1)
        )
    ...

  the terminal still shows green

* I remove ``get_hour`` and ``get_minutes`` and all the tests are still passing! I will sleep easier tonight!!


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
* :ref:`test_duration_w_hours<test_duration_w_hours>`
* `test_duration_w_hours_and_minutes`_ where I

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