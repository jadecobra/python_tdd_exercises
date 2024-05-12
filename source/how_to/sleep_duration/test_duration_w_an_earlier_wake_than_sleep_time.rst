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

I want to test the ``duration`` :ref:`function<functions>` with a ``wake_time`` that is earlier than the ``sleep_time``

.. _test_duration_w_an_earlier_wake_than_sleep_time_red:

*********************************************************************************
red: make it fail
*********************************************************************************

I add a failing test to ``test_sleep_duration.py`` with a `while statement`_ to make sure ``wake_time`` is always earlier than ``sleep_time``

.. code-block:: python

  def test_duration_w_an_earlier_wake_than_sleep_time(self):
      sleep_time = random_timestamp()
      wake_time = random_timestamp()
      while wake_time >= sleep_time:
          wake_time = random_timestamp()

      self.assertEqual(
          sleep_duration.duration(
              sleep_time=sleep_time,
              wake_time=wake_time
          ),
          ''
      )

  def test_duration_w_hours_and_minutes(self):
  ...

and get an :ref:`AssertionError`

.. code-block:: python

  AssertionError: '-1:00' != ''
  AssertionError: '-2:12' != ''
  AssertionError: '-8:34' != ''
  AssertionError: '-10:57' != ''

.. _test_duration_w_an_earlier_wake_than_sleep_time_green:

*********************************************************************************
green: make it pass
*********************************************************************************


* The ``duration`` :ref:`function<functions>` returns a negative timestamp when given an earlier ``wake_time`` than ``sleep_time``, which is not a real duration. I want it to return a difference when ``wake_time`` is later than or the same as ``sleep_time`` and raise a ValueError_ with a message when ``wake_time`` is earlier than ``sleep_time``. I change the assertEqual_ to assertRaisesRegex_ to catch the :doc:`Exception</how_to/exception_handling_programs>` when it is raised by the :ref:`function<functions>`

  .. code-block:: python

    def test_duration_w_an_earlier_wake_than_sleep_time(self):
        sleep_time = random_timestamp()
        wake_time = random_timestamp()
        while wake_time >= sleep_time:
            wake_time = random_timestamp()

        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: "{wake_time}"'
            ' is earlier than '
            f'sleep_time: "{sleep_time}"'
        ):
            sleep_duration.duration(
                sleep_time=sleep_time,
                wake_time=wake_time
            )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: ValueError not raised

  I add a :doc:`condition</data_structures/booleans/booleans>` to the ``duration`` :ref:`function<functions>` to raise the ValueError_

  .. code-block:: python
      :emphasize-lines: 1,4

    def duration(wake_time=None, sleep_time=None):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
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

            duration_hours = difference // 60
            duration_minutes = difference % 60

            return (
                f'{duration_hours:02}:'
                f'{duration_minutes:02}'
            )

  and the terminal shows a random ValueError_ for ``test_duration_w_hours_and_minutes`` when ``wake_time`` is earlier than ``sleep_time``

  .. code-block:: python

    ValueError: wake_time: "07:33" is earlier than sleep_time: "08:12"
    ValueError: wake_time: "07:46" is earlier than sleep_time: "14:47"
    ValueError: wake_time: "23:10" is earlier than sleep_time: "23:27"
    ValueError: wake_time: "11:32" is earlier than sleep_time: "13:52"

* I add the error to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # NameError
    # AttributeError
    # ValueError

* then add a `while statement`_ to make sure ``wake_time`` is not earlier than ``sleep_time`` for the difference calculation

  .. code-block:: python
    :emphasize-lines: 4,5

    def test_duration_w_hours_and_minutes(self):
        sleep_time = random_timestamp()
        wake_time = random_timestamp()
        while wake_time < sleep_time:
            wake_time = random_timestamp()

        difference_hours = (
            int(wake_time.split(':')[0])
          - int(sleep_time.split(':')[0])
        )
        difference_minutes = (
            int(wake_time.split(':')[1])
          - int(sleep_time.split(':')[1])
        )

        difference = (
            difference_hours*60
          + difference_minutes
        )
        duration_hours = difference // 60
        duration_minutes = difference % 60

        self.assertEqual(
            sleep_duration.duration(
                sleep_time=sleep_time,
                wake_time=wake_time
            ),
            (
                f'{duration_hours:02}:'
                f'{duration_minutes:02}'
            )
        )

  and the terminal shows passing tests with no more random failures, green, green, green, green all the way!

.. _test_duration_w_an_earlier_wake_than_sleep_time_refactor:

*********************************************************************************
refactor: make it better
*********************************************************************************

* I copy the `assertRaisesRegex`_ statement from ``test_duration_w_an_earlier_wake_than_sleep_time`` and add it to the `while statement`_ in ``test_duration_w_date_and_time`` to remove repetition. It will run when ``wake_time`` is earlier than ``sleep_time``

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        sleep_time = random_timestamp()
        wake_time = random_timestamp()

        while wake_time < sleep_time:
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            ):
                sleep_duration.duration(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                )
            wake_time = random_timestamp()

        difference_hours = (
            int(wake_time.split(':')[0])
          - int(sleep_time.split(':')[0])
        )
        difference_minutes = (
            int(wake_time.split(':')[1])
          - int(sleep_time.split(':')[1])
        )

        difference = (
            difference_hours*60
          + difference_minutes
        )
        duration_hours = difference // 60
        duration_minutes = difference % 60

        self.assertEqual(
            sleep_duration.duration(
                sleep_time=sleep_time,
                wake_time=wake_time
            ),
            (
                f'{duration_hours:02}:'
                f'{duration_minutes:02}'
            )
        )

  I comment out the condition in ``duration`` to make sure the test still works as expected

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        # if wake_time < sleep_time:
        #     raise ValueError(
        #         f'wake_time: "{wake_time}"'
        #         ' is earlier than '
        #         f'sleep_time: "{sleep_time}"'
        #     )
        # else:
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

            duration_hours = difference // 60
            duration_minutes = difference % 60

            return (
                f'{duration_hours:02}:'
                f'{duration_minutes:02}'
            )

  and get an :ref:`AssertionError` for ``test_duration_w_an_earlier_wake_than_sleep_time`` and a random one for ``test_duration_w_hours_and_minutes`` when ``wake_time`` is earlier than ``sleep_time``

  .. code-block:: python

    AssertionError: ValueError not raised

  the ``assertWakeTimeEarlier`` :ref:`method<functions>` works as expected. I remove the comments and the terminal shows green again
* I remove ``test_duration_w_an_earlier_wake_than_sleep_time`` because it is now covered by ``test_duration_w_hours_and_minutes``
* then add an ``else`` block for the rest of the code in ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        sleep_time = random_timestamp()
        wake_time = random_timestamp()

        while wake_time < sleep_time:
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            ):
                sleep_duration.duration(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                )
            wake_time = random_timestamp()
        else:
            difference_hours = (
                int(wake_time.split(':')[0])
              - int(sleep_time.split(':')[0])
            )
            difference_minutes = (
                int(wake_time.split(':')[1])
              - int(sleep_time.split(':')[1])
            )

            difference = (
                difference_hours*60
              + difference_minutes
            )
            duration_hours = difference // 60
            duration_minutes = difference % 60

            self.assertEqual(
                sleep_duration.duration(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                (
                    f'{duration_hours:02}:'
                    f'{duration_minutes:02}'
                )
            )

  still green

* I add a `static method`_ to calculate the difference between ``wake_time`` and ``sleep_time``

  .. code-block:: python

    @staticmethod
    def get_difference(wake_time=None, sleep_time=None):
        difference_hours = (
            int(wake_time.split(':')[0])
          - int(sleep_time.split(':')[0])
        )
        difference_minutes = (
            int(wake_time.split(':')[1])
          - int(sleep_time.split(':')[1])
        )

        difference = (
            difference_hours*60
            + difference_minutes
        )
        duration_hours = difference // 60
        duration_minutes = difference % 60

        return (
            f'{duration_hours:02}:'
            f'{duration_minutes:02}'
        )

    def test_duration_w_hours_and_minutes(self):
    ...

  then call it in ``test_duration_w_hours_and_minutes`` to replace the expectation

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        sleep_time = random_timestamp()
        wake_time = random_timestamp()

        while wake_time < sleep_time:
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            ):
                sleep_duration.duration(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                )
            wake_time = random_timestamp()
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

  still green

* I also add an ``assert`` :ref:`method<functions>` for the `assertRaisesRegex`_ block

  .. code-block:: python

    def assertWakeTimeEarlier(self, wake_time=None, sleep_time=None):
        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: "{wake_time}"'
            ' is earlier than '
            f'sleep_time: "{sleep_time}"'
        ):
            sleep_duration.duration(
                sleep_time=sleep_time,
                wake_time=wake_time
            )

    @staticmethod
    def get_difference(wake_time=None, sleep_time=None):
    ...

  and call it in ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        sleep_time = random_timestamp()
        wake_time = random_timestamp()

        while wake_time < sleep_time:
            self.assertWakeTimeEarlier(
                wake_time=wake_time,
                sleep_time=sleep_time
            )
            wake_time = random_timestamp()
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

  all tests are still passing!

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
* `test_duration_w_an_earlier_wake_than_sleep_time`_
* :ref:`test_duration_w_hours_and_minutes<test_duration_w_hours_and_minutes>` where I used a `while statement`_

  - to make sure that when ``wake_time`` is earlier than ``sleep_time`` the ``duration`` :ref:`function<functions>` raises a ValueError_ with a message
  - and it returns the right difference between the two when ``wake_time`` is later than or the same as ``sleep_time``


Would you like to :ref:`test duration with timestamps that have dates?<test_duration_w_date_and_time>`

----

:doc:`/code/code_sleep_duration`