.. include:: ../../links.rst


#################################################################################
how to measure sleep duration: test_duration_w_hours_and_minutes
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/cxsSz8Ozqds?si=HGpmvrLLBj6axfjn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

This is part 2 of a program that calculates the difference between a given wake and sleep time.

.. contents:: table of contents
  :local:
  :depth: 2

----

I want to test the ``duration`` :ref:`function<functions>` with timestamps where both hours and minutes are random.

*********************************************************************************
red: make it fail
*********************************************************************************

* I change the name of ``test_duration_w_hours``

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        sleep_time = random_timestamp()
        wake_time = random_timestamp()

* then add a variable for the difference between the hours

  .. code-block:: python

    difference_hours = (
        int(wake_time.split(':')[0])
      - int(sleep_time.split(':')[0])
    )

    self.assertEqual(
        src.sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        difference_hours
    )

* and change the expectation to a timestamp format

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        f'{difference_hours:02}:00'
    )

  which gives me :ref:`AssertionError`

  .. code-block:: python

    AssertionError: -3 != '-3:00'
    AssertionError: 0 != '00:00'
    AssertionError: 8 != '08:00'
    AssertionError: 16 != '16:00'

  the ``duration`` :ref:`function<functions>` returns a number and the test expects a string_. I change it to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference_hours = (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )

        return f'{difference_hours:02}:00'

* then make a copy of ``difference_hours`` in the test, change the name, and change ``0`` to ``1`` on each line to get the difference between the minutes of ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        sleep_time = random_timestamp()
        wake_time = random_timestamp()

        difference_hours = (
            int(wake_time.split(':')[0])
          - int(sleep_time.split(':')[0])
        )
        difference_minutes = (
            int(wake_time.split(':')[1])
          - int(sleep_time.split(':')[1])
        )

* I also add ``difference_minutes`` to the expectation

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            f'{difference_hours:02}:'
            f'{difference_minutes:02}'
        )
    )

* and change the ``random_timestamp`` :ref:`function<functions>` to have random numbers from ``0`` up to and including ``59`` for the minutes

  .. code-block:: python

    def random_timestamp():
        return (
            f'{random.randint(0,23):02}:'
            f'{random.randint(0,59):02}'
        )

  I get random success when ``random_timestamp`` returns ``00`` for the minutes and :ref:`AssertionError` when it does not

  .. code-block:: python

    AssertionError: '-18:00' != '-18:44'
    AssertionError: '05:00' != '05:-16'
    AssertionError: '-2:00' != '-2:-26'
    AssertionError: '16:00' != '16:-25'

  the ``duration`` :ref:`function<functions>` returns ``00`` for the minutes part of the duration, and the test expects the difference between the minutes of ``wake_time`` and ``sleep_time``

*********************************************************************************
green: make it pass
*********************************************************************************

* I make a copy of ``difference_hours`` in ``duration``, change the name, then add it to the `return statement`_

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

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '20:20' != '20:-6'
    AssertionError: '06:06' != '06:17'
    AssertionError: '-16:-16' != '-16:-7'
    AssertionError: '02:02' != '02:07'

  the :ref:`function<functions>` returns the same numbers for hours and minutes because ``difference_hours`` and ``difference_minutes`` are the same. I make a copy of the ``get_hour`` :ref:`function<functions>`, call it ``get_minutes`` and change the index to get the second item from the timestamp split

  .. code-block:: python

    def get_minutes(timestamp):
        return int(timestamp.split(':')[1])

  then change the calls in ``difference_minutes``

  .. code-block:: python

    difference_minutes = (
        get_minutes(wake_time)
      - get_minutes(sleep_time)
    )

  and the terminal shows passing tests! There is something wrong with this calculation...

*********************************************************************************
refactor: make it better
*********************************************************************************


test_duration_calculation
#################################################################################

The ``duration`` :ref:`function<functions>` returns a subtraction of hours and a subtraction of minutes which does not give the right difference between the timestamps

red: make it fail
---------------------------------------------------------------------------------

If ``duration`` is given a ``wake_time`` of ``'03:30'`` and a ``sleep_time`` of ``'02:59'``, it should return ``'00:31'`` as the difference between the timestamps

.. code-block:: python

  def test_duration_calculation(self):
      self.assertEqual(
          src.sleep_duration.duration(
              wake_time='03:30',
              sleep_time='02:59'
          ),
          '00:31'
      )

  def test_duration_w_hours_and_minutes(self):
  ...

the terminal shows :ref:`AssertionError` when I add ``test_duration_calculation``

.. code-block:: python

  AssertionError: '01:-29' != '00:31'

``duration`` returns ``'01:-29'`` which is not a real duration, the calculation has to change

green: make it pass
---------------------------------------------------------------------------------

* I add a `return statement`_ to the ``duration`` :ref:`function<functions>` where I multiply ``difference_hours`` by ``60`` then add it to ``difference_minutes`` to get the total difference in minutes

  .. code-block:: python

    return (
        difference_hours*60
      + difference_minutes
    )

    return (
        f'{difference_hours:02}:'
        f'{difference_minutes:02}'
    )

  the terminal shows :ref:`AssertionError` for ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    AssertionError: -458 != '-7:-38'
    AssertionError: -936 != '-15:-36'
    AssertionError: -31 != '-1:29'
    AssertionError: 213 != '03:33'

  ``duration`` returns the difference as a number and the test still expects a string_. I add the `unittest.skip decorator`_ to skip it

  .. code-block:: python

    @unittest.skip
    def test_duration_w_hours_and_minutes(self):
    ...

  and get this :ref:`AssertionError` for ``test_duration_calculation``

  .. code-block:: python

    AssertionError: 31 != '00:31

  the :ref:`function<functions>` returns the right number of minutes for the difference. I need a way to change it to hours and minutes to match the expectations of the tests. I add the `unittest.skip decorator`_ to skip it while I test the solution

  .. code-block:: python

    @unittest.skip
    def test_duration_calculation(self):
    ...

  If I divide the total number of minutes by ``60``, the whole number from the result is the hours and the remainder is the minutes

test_floor_aka_integer_division
#################################################################################

The ``//`` operator returns a whole number which is how many times the bottom number can be multiplied to get a whole number that is equal to or as close to the top number as possible. It should give me the hours when I divide by ``60``

* I add a failing test for it

  .. code-block:: python

    def test_floor_aka_integer_division(self):
        self.assertEqual(120//60, 0)

    @unittest.skip
    def test_duration_calculation(self):
    ...

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 2 != 0

  the result of ``120`` divided by ``60`` is ``2`` with a remainder of ``0``. I change the expectation to the right value.

  .. code-block:: python

    self.assertEqual(120//60, 2)

  and it passes

* I add another assertion

  .. code-block:: python

    self.assertEqual(150//60, 0)

  and get :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 2 != 0

  the result of ``150`` divided by ``60`` is also ``2`` but with a remainder of ``30``. I change the expectation to the right value

  .. code-block:: python

    self.assertEqual(150//60, 2)

  and the terminal shows passing tests


test_the_modulo_operation
#################################################################################

The ``%`` operator returns the remainder when a number is divided by another, it should give me the minutes when I divide by ``60``

* I add a failing test for it

  .. code-block:: python

    def test_the_modulo_operation(self):
        self.assertEqual(120%60, 2)

    @unittest.skip
    def test_duration_calculation(self):
    ...

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0 != 2

  the remainder when ``120`` is divided by ``60`` is ``0``. I change the expectation to the right value

  .. code-block:: python

    self.assertEqual(120%60, 0)

  and the test passes

* I add another assertion

  .. code-block:: python

    self.assertEqual(150%60, 0)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 30 != 0

  the remainder when ``150`` is divided by ``60`` is ``30``. I change the expected value in the test to the right value

  .. code-block:: python

    self.assertEqual(150%60, 30)

  and the terminal shows green again

----

* I comment out the `unittest.skip decorator`_ for ``test_duration_calculation`` to get back the :ref:`AssertionError`

  .. code-block:: python

    # @unittest.skip
    def test_duration_calculation(self):

* and change the first `return statement`_ in the ``duration`` :ref:`function<functions>` to a variable for the total difference in minutes

  .. code-block:: python

    difference = (
        difference_hours*60
      + difference_minutes
    )

    return (
        f'{difference_hours:02}:'
        f'{difference_minutes:02}'
    )

  then add a variable for the hours of the duration using `floor (integer) division`_

  .. code-block:: python

    difference = (
        difference_hours*60
      + difference_minutes
    )
    duration_hours = difference // 60

  and a variable for the minutes of the duration using the modulo_ operator

  .. code-block:: python

    duration_hours = difference // 60
    duration_minutes = difference % 60

  then change ``difference_hours`` and ``difference_minutes`` in the `return statement`_

  .. code-block:: python

    return (
        f'{duration_hours:02}:'
        f'{duration_minutes:02}'
    )

  and the test passes

* I remove the `unittest.skip decorator`_ from ``test_duration_calculation``
* and comment it out for ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    # @unittest.skip
    def test_duration_w_hours_and_minutes(self):
    ...

  which gives me random successes and random :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '-11:46' != '-10:-14'
    AssertionError: '-6:04' != '-5:-56'
    AssertionError: '10:50' != '11:-10'
    AssertionError: '16:50' != '17:-10'

  the calculation in the test is still not right. I change it to match the ``duration`` :ref:`function<functions>`

  .. code-block:: python

    difference = (
        difference_hours*60
      + difference_minutes
    )
    duration_hours = difference // 60
    duration_minutes = difference % 60

  then change the variables in the expectation

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            f'{duration_hours:02}:'
            f'{duration_minutes:02}'
        )
    )

  and the test passes with no more random failures

* I take out the `unittest.skip decorator`_ from ``test_duration_w_hours_and_minutes``
* and remove ``test_duration_calculation`` because it is covered by ``test_duration_w_hours_and_minutes`` which has the right calculation
* then add a :ref:`function<functions>` in ``sleep_duration.py`` to change ``get_hour`` and ``get_minutes``

  .. code-block:: python

    def read_timestamp(timestamp=None, index=0):
        return int(timestamp.split(':')[index])

    def duration(wake_time=None, sleep_time=None):
    ...

* call it in ``duration``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference_hours = (
            read_timestamp(wake_time)
          - read_timestamp(sleep_time)
        )
        difference_minutes = (
            read_timestamp(wake_time, 1)
          - read_timestamp(sleep_time, 1)
        )
    ...

* and remove ``get_hour`` and ``get_minutes``. The terminal shows all tests are still passing!

*********************************************************************************
review
*********************************************************************************

The challenge is to write a program that calculates the difference between a given wake and sleep time. I ran the following tests to get something that comes close to doing it


* :ref:`test_string_splitting`
* :ref:`test_converting_strings_to_numbers`
* `test_floor_aka_integer_division`_
* `test_the_modulo_operation`_
* :ref:`test_duration_w_hours<how to measure sleep duration: test_duration_w_hours>`
* :ref:`test_duration_w_hours_and_minutes<how to measure sleep duration: test_duration_w_hours_and_minutes>` where I

  - used `random.randint`_ to generate random numbers

    * from the ``24`` hours in a day
    * and the ``60`` minutes in an hour

  - then :ref:`how to pass values` them in the timestamp strings that are given to the :ref:`function<functions>`
  - and `test_duration_calculation`_ to make sure that the ``duration`` :ref:`function<functions>` returns the right difference between ``wake_time`` and ``sleep_time``
  - and changes it to a timestamp format

    * by using `floor (integer) division`_ to get the hours
    * and the modulo_ operation to get the minutes

Would you like to :ref:`test duration with an earlier wake than sleep time? <how to measure sleep duration: test_duration_w_an_earlier_wake_than_sleep_time>`

----

:doc:`/code/code_sleep_duration`