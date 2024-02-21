.. include:: ../links.rst

*****************************************************************************
how to measure sleep duration: test_duration_w_earlier_wake_than_sleep_time
*****************************************************************************

In this chapter, I take a look at building a program that returns the duration between a given sleep and wake time.

----

test_duration_w_earlier_wake_than_sleep_time
========================================================

What happens when the ``duration`` :ref:`function<functions>` is given an earlier ``wake_time`` than ``sleep_time``?

.. _test_duration_w_earlier_wake_than_sleep_time_red:

red: make it fail
--------------------------------------------------------

I will add a failing test to ``test_sleep_duration.py`` to find out

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

green: make it pass
--------------------------------------------------------

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

refactor: make it better
--------------------------------------------------------

* The ``duration`` :ref:`function<functions>` currently returns negative numbers when given an earlier ``wake_time`` than ``sleep_time``. I want it to return durations only when ``wake_time`` is later than or equal to ``sleep_time``. I will add a condition so it makes this decision

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
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

  - When ``wake_time_minutes`` is less than ``sleep_time_minutes``, ``wake_time`` is earlier than ``sleep_time`` and the ``duration`` :ref:`function<functions>` will raise an :doc:`Exception </how_to/exception_handling_programs>`
  - When ``wake_time_minutes`` is greater than or equal to ``sleep_time_minutes``, ``wake_time`` is later than or the same as ``sleep_time`` and the ``duration`` :ref:`function<functions>` returns the difference between the two timestamps

  the terminal shows a ValueError_ that looks like this for ``test_duration_w_earlier_wake_than_sleep_time`` and the random cases in ``test_duration_w_hours_and_minutes`` where ``wake_time`` is earlier than ``sleep_time``

  .. code-block:: python

    ValueError: wake_time: 20:26 is earlier than sleep_time: 23:50

* I add the error to the list of exceptions encountered even though I made this one happen

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError
    # ValueError

* and then use `assertRaisesRegex`_ to catch the :doc:`Exception </how_to/exception_handling_tests>` with the specific message raised in ``test_duration_w_earlier_wake_than_sleep_time``

  .. code-block:: python

    def test_duration_w_earlier_wake_than_sleep_time(self):
        wake_time = '01:00'
        sleep_time = '02:00'

        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: {wake_time} is earlier '
            f'than sleep_time: {sleep_time}'
        ):
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            )

  and the test passes, leaving the random ValueError_ for ``test_duration_w_hours_and_minutes`` when ``wake_time`` is earlier than ``sleep_time``

* I add an :doc:`exception handler </how_to/exception_handling_programs>` using a `try statement`_ and `assertRaisesRegex`_ to confirm the ValueError_ is raised when ``wake_time`` is earlier than ``sleep_time`` with the specific message from ``duration``

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        wake_hour = random_hour()
        wake_minutes = random_minutes()
        wake_time_minutes = (
            (wake_hour * 60)
           + wake_minutes
        )
        wake_time = f'{wake_hour:02}:{wake_minutes:02}'

        sleep_hour = random_hour()
        sleep_minutes = random_minutes()
        sleep_time_minutes = (
            (sleep_hour) * 60
           + sleep_minutes
        )
        sleep_time = f'{sleep_hour:02}:{sleep_minutes:02}'

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

  and we are green, green, green, green all the way

I have a :ref:`function<functions>` that

* takes in a ``wake_time`` and ``sleep_time`` as inputs
* raises a ValueError_ with a message when ``wake_time`` is earlier than ``sleep_time``
* returns the difference between the two when ``wake_time`` is later than or the same as ``sleep_time``

----
