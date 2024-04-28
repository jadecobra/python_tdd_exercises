.. include:: ../../links.rst

.. _test_duration_w_an_earlier_wake_than_sleep_time:

#################################################################################
how to measure sleep duration: test_duration_w_an_earlier_wake_than_sleep_time
#################################################################################

This is part 3 of a program that calculates the difference between a given wake and sleep time.

.. contents:: table of contents
  :local:
  :depth: 2

----

I want to test the ``duration`` :ref:`function<functions>` with an earlier ``wake_time`` than ``sleep_time``?

.. _test_duration_w_an_earlier_wake_than_sleep_time_red:

*********************************************************************************
red: make it fail
*********************************************************************************

I add a failing test to ``test_sleep_duration.py``

.. code-block:: python

  def test_duration_w_an_earlier_wake_than_sleep_time(self):
      self.assertEqual(
          sleep_duration.duration(
              wake_time='01:00',
              sleep_time='02:00'
          ),
          ''
      )

  def test_duration_w_hours_and_minutes(self):
  ...

and get an :ref:`AssertionError`

.. code-block:: python

  AssertionError: '-1:00' != ''

.. _test_duration_w_an_earlier_wake_than_sleep_time_green:

*********************************************************************************
green: make it pass
*********************************************************************************

I change the expected value in the test

.. code-block:: python

  def test_duration_w_an_earlier_wake_than_sleep_time(self):
      self.assertEqual(
          sleep_duration.duration(
              wake_time='01:00',
              sleep_time='02:00'
          ),
          '-1:00'
      )

and it passes

.. _test_duration_w_an_earlier_wake_than_sleep_time_refactor:

*********************************************************************************
refactor: make it better
*********************************************************************************

* The ``duration`` :ref:`function<functions>` returns a negative timestamp when given an earlier ``wake_time`` than ``sleep_time``, which is not a real duration. I want it to only return a difference when ``wake_time`` is later than or the same as ``sleep_time``. I add a condition for this

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        ...

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

  - When ``difference`` is less than ``0``, ``wake_time`` is earlier than ``sleep_time`` and the ``duration`` :ref:`function<functions>` will raise an :doc:`Exception </how_to/exception_handling_programs>`
  - When ``difference`` is greater than or the same as ``0``, ``wake_time`` is later than or the same as ``sleep_time`` and the ``duration`` :ref:`function<functions>` returns the difference between the two timestamps

  the terminal shows a random ValueError_ for ``test_duration_w_hours_and_minutes`` when ``wake_time`` is earlier than ``sleep_time``

  .. code-block:: python

    ValueError: wake_time: 07:33 is earlier than sleep_time: 08:12
    ValueError: wake_time: 07:46 is earlier than sleep_time: 14:47
    ValueError: wake_time: 23:10 is earlier than sleep_time: 23:27
    ValueError: wake_time: 11:32 is earlier than sleep_time: 13:52

  and this ValueError_ for ``test_duration_w_an_earlier_wake_than_sleep_time``

  .. code-block:: python

    ValueError: wake_time: 01:00 is earlier than sleep_time: 02:00

* I add the error to the list of exceptions encountered

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

* I replace the assertEqual_ with assertRaisesRegex_ to catch the :doc:`Exception </how_to/exception_handling_tests>` and make sure it has the right message

  .. code-block:: python

    def test_duration_w_an_earlier_wake_than_sleep_time(self):
        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: {wake_time}'
            ' is earlier than '
            f'sleep_time: {sleep_time}'
        ):
            sleep_duration.duration(
                wake_time='01:00',
                sleep_time='02:00'
            )

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'wake_time' is not defined

  I add variables for ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def test_duration_w_an_earlier_wake_than_sleep_time(self):
        wake_time = '01:00'
        sleep_time = '02:00'

  then reference them in the call to ``sleep_duration.duration``

  .. code-block:: python

    sleep_duration.duration(
        wake_time=wake_time,
        sleep_time=sleep_time
    )

  and the test passes
* I remove the `unittest.skip decorator`_ for ``test_duration_w_hours_and_minutes``
* then add an :doc:`exception handler </how_to/exception_handling_programs>` using a `try statement`_ and assertRaisesRegex_ to check that the ValueError_ is raised when ``wake_time`` is earlier than ``sleep_time`` with the specific message from ``duration``

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
        except Exception:
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: {wake_time}'
                ' is earlier than '
                f'sleep_time: {sleep_time}'
            ):
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )

  and the terminal shows passing tests with no more random failures, green, green, green, green all the way
* I add a helper :ref:`function<functions>` to remove the repetition of the assertRaisesRegex_ since it it is the same in ``test_duration_w_an_earlier_wake_than_sleep_time`` and ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    def assertWakeTimeEarlier(self, wake_time, sleep_time):
        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: {wake_time}'
            ' is earlier than '
            f'sleep_time: {sleep_time}'
        ):
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            )

    def test_duration_w_an_earlier_wake_than_sleep_time(self):
    ...

* then replace the text in ``test_duration_w_an_earlier_wake_than_sleep_time`` with a call to ``assertWakeTimeEarlier``

  .. code-block:: python

    def test_duration_w_an_earlier_wake_than_sleep_time(self):
        self.assertWakeTimeEarlier(
            wake_time='03:00',
            sleep_time='02:00'
        )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: ValueError not raised

  ``03:00`` is not earlier than ``02:00``, when I change ``wake_time``

  .. code-block:: python

    self.assertWakeTimeEarlier(
        wake_time='01:00',
        sleep_time='02:00'
    )

  the test passes

* I change the `try statement`_ in ``test_duration_w_hours_and_minutes`` to use ``assertWakeTimeEarlier``

  .. code-block:: python

    except Exception:
        self.assertWakeTimeEarlier(
            wake_time=wake_time,
            sleep_time=sleep_time
        )

  and the test still shows green with no random failures. Fantastic!

.. _test_duration_w_an_earlier_wake_than_sleep_time_review:

*********************************************************************************
review
*********************************************************************************

The challenge is to write a program that calculates the difference between a given wake and sleep time. I ran the following tests to get something that comes close to doing it


* :ref:`test_string_splitting`
* :ref:`test_converting_strings_to_numbers`
* :ref:`test_floor_aka_integer_division`
* :ref:`test_the_modulo_operation`
* :ref:`test_duration_w_hours<test_duration_w_hours>`
* :ref:`test_duration_calculation`
* `test_duration_w_an_earlier_wake_than_sleep_time`_ where I used assertRaisesRegex_ to make sure the ``duration`` :ref:`function<functions>` raises a ValueError_ with a message when ``wake_time`` is earlier than ``sleep_time``
* :ref:`test_duration_w_hours_and_minutes<test_duration_w_hours_and_minutes>` where I used

  - a `try statement`_ which checks that the ``duration`` :ref:`function<functions>` returns the right difference when ``wake_time`` is later than or the same as ``sleep_time``
  - and when a ValueError_ happens uses assertRaisesRegex_ to check that it is because ``wake_time`` is earlier than ``sleep_time``


Would you like to :ref:`test duration with dates in the timestamps<test_duration_w_date_and_time>`?

----

:doc:`/code/code_sleep_duration`