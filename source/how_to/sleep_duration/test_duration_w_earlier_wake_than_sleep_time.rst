.. include:: ../../links.rst

.. _test_duration_w_earlier_wake_than_sleep_time:

#############################################################################
how to measure sleep duration: test_duration_w_earlier_wake_than_sleep_time
#############################################################################

This is part 3 of a program that calculates the difference between a given wake and sleep time.

.. contents:: table of contents
  :local:
  :depth: 2

----

I want to know what happens when the ``duration`` :ref:`function<functions>` is given an earlier ``wake_time`` than ``sleep_time``?

.. _test_duration_w_earlier_wake_than_sleep_time_red:

*****************************************************************************
red: make it fail
*****************************************************************************

I add a failing test to ``test_sleep_duration.py`` to find out

.. code-block:: python

  def test_duration_w_earlier_wake_than_sleep_time(self):
      self.assertEqual(
          sleep_duration.duration(
              wake_time='01:00',
              sleep_time='02:00'
          ),
          ''
      )

  def test_duration_w_hours_and_minutes(self):
  ...

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: '-1:00' != ''

.. _test_duration_w_earlier_wake_than_sleep_time_green:

*****************************************************************************
green: make it pass
*****************************************************************************

I change the expected value in the test to make it pass

.. code-block:: python

  def test_duration_w_earlier_wake_than_sleep_time(self):
      self.assertEqual(
          sleep_duration.duration(
              wake_time='01:00',
              sleep_time='02:00'
          ),
          '-1:00'
      )

and the terminal shows passing tests

.. _test_duration_w_earlier_wake_than_sleep_time_refactor:

*****************************************************************************
refactor: make it better
*****************************************************************************

* The ``duration`` :ref:`function<functions>` returns negative numbers when given an earlier ``wake_time`` than ``sleep_time``. I want it to return a difference only when ``wake_time`` is later than or equal to ``sleep_time``. I add a condition for it to make the decision

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

        difference = (
            difference_hours*60
          + difference_minutes
        )

        if difference < 0:
            raise ValueError(
                f'wake_time: {wake_time}'
                ' is earlier than '
                f'sleep_time: {sleep_time}'
            )
        else:
            duration_hours = difference // 60
            duration_minutes = difference % 60

            return (
                f'{duration_hours:02}:'
                f'{duration_minutes:02}'
            )

  - When ``wake_time_minutes`` is less than ``sleep_time_minutes``, ``wake_time`` is earlier than ``sleep_time`` and the ``duration`` :ref:`function<functions>` will raise an :doc:`Exception </how_to/exception_handling_programs>`
  - When ``wake_time_minutes`` is greater than or equal to ``sleep_time_minutes``, ``wake_time`` is later than or the same as ``sleep_time`` and the ``duration`` :ref:`function<functions>` returns the difference between the two timestamps

  the terminal shows a random ValueError_ for ``test_duration_w_hours_and_minutes`` when ``wake_time`` is earlier than ``sleep_time``

  .. code-block:: python

    ValueError: wake_time: 07:33 is earlier than sleep_time: 08:12
    ValueError: wake_time: 07:46 is earlier than sleep_time: 14:47

  and this ValueError_ for ``test_duration_w_earlier_wake_than_sleep_time``

  .. code-block:: python

    ValueError: wake_time: 01:00 is earlier than sleep_time: 02:00

* I add the error to the list of exceptions encountered though I made this one happen

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # NameError
    # AttributeError
    # ValueError

* then add the `unittest.skip decorator`_ to ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    @unittest.skip
    def test_duration_w_hours_and_minutes(self):
    ...

* I add variables for ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def test_duration_w_earlier_wake_than_sleep_time(self):
        wake_time = '01:00'
        sleep_time = '02:00'

        self.assertEqual(
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            ),
            '-1:00'
        )

* I replace the ``self.assertEqual`` with `assertRaisesRegex`_ to catch the :doc:`Exception </how_to/exception_handling_tests>` with the specific message raised in ``test_duration_w_earlier_wake_than_sleep_time``

  .. code-block:: python

    with self.assertRaisesRegex(
        ValueError,
        f'wake_time: {wake_time} is earlier '
        f'than sleep_time: {sleep_time}'
    ):
        sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        )

  the terminal shows passing tests
* I remove the `unittest.skip decorator`_ for ``test_duration_w_hours_and_minutes``
* then add an :doc:`exception handler </how_to/exception_handling_programs>` using a `try statement`_ and `assertRaisesRegex`_ to confirm the ValueError_ is raised when ``wake_time`` is earlier than ``sleep_time`` with the specific message from ``duration``

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        ...

        try:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                (
                    f'{duration_hours:02}:'
                    f'{duration_minutes:02}'
                )
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

  and we are green, green, green, green all the way

*****************************************************************************
review
*****************************************************************************

The challenge is to write a program that calculates the difference between a given wake and sleep time. I ran the following tests to get something that comes close to doing it


* :ref:`test_string_splitting`
* :ref:`test_converting_strings_to_numbers`
* :ref:`test_floor_aka_integer_division`
* :ref:`test_the_modulo_operation`
* :ref:`test_duration_w_hours<test_duration_w_hours>`
* :ref:`test_duration_calculation`
* `test_duration_w_earlier_wake_than_sleep_time`_ where I

  - used `assertRaisesRegex`_ to make sure the ``duration`` :ref:`function<functions>` raises a ValueError_ with a message when ``wake_time`` is earlier than ``sleep_time`` and
  - returns the difference between the two when ``wake_time`` is later than or the same as ``sleep_time``

* :ref:`test_duration_w_hours_and_minutes<test_duration_w_hours_and_minutes>` where I used

  - a `try statement`_ that calls the :ref:`function<function>` and when a ValueError_ happens
  - checks for the message I want with `assertRaisesRegex`_


Would you like to :ref:`test duration with a date and time<test_duration_w_date_and_time>`?

----

:doc:`/code/code_sleep_duration`