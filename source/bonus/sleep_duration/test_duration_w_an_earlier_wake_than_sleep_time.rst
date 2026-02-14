.. meta::
  :description: Handle earlier wake times in Python sleep duration calculations with TDD! Learn to use assertRaisesRegex for ValueError and refactor for robust time validation.
  :keywords: Jacob Itegboje, Python sleep duration, earlier wake time Python, TDD exception handling, Python ValueError, assertRaisesRegex Python, Python time validation, refactoring Python tests

.. include:: ../../links.rst


#################################################################################
how to measure sleep duration: test_duration_w_an_earlier_wake_than_sleep_time
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/PF6h_vOe55E?si=pLNDmUvLF8m1eof-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

This is III of a program_ that calculates the difference between a given wake and sleep time.

----

I want to test the ``duration`` :ref:`function<what is a function?>` with a ``wake_time`` that is earlier than the ``sleep_time``

*********************************************************************************
:red:`RED`: make it fail
*********************************************************************************

I add a failing test to ``test_sleep_duration.py`` with a `while statement`_ to make sure ``wake_time`` is always earlier than ``sleep_time``

.. code-block:: python

  def test_duration_w_an_earlier_wake_than_sleep_time(self):
      sleep_time = random_timestamp()
      wake_time = random_timestamp()
      while wake_time >= sleep_time:
          wake_time = random_timestamp()

      self.assertEqual(
          src.sleep_duration.duration(
              sleep_time=sleep_time,
              wake_time=wake_time
          ),
          ''
      )

  def test_duration_w_hours_and_minutes(self):
  ...

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: '-1:00' != ''
  AssertionError: '-2:12' != ''
  AssertionError: '-8:34' != ''
  AssertionError: '-10:57' != ''

*********************************************************************************
:green:`GREEN`: make it pass
*********************************************************************************


* The ``duration`` :ref:`function<what is a function?>` returns a negative timestamp when given an earlier ``wake_time`` than ``sleep_time``, which is not a real duration. I want it to return a difference when ``wake_time`` is later than or the same as ``sleep_time`` and raise ValueError_ with a message when ``wake_time`` is earlier than ``sleep_time``. I change the assertEqual_ to assertRaisesRegex_ to catch the :ref:`Exception<errors>`, if it is raised by the :ref:`function<what is a function?>`

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
            src.sleep_duration.duration(
                sleep_time=sleep_time,
                wake_time=wake_time
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: ValueError not raised

  I add a condition to the ``duration`` :ref:`function<what is a function?>` to raise the ValueError_

  .. code-block:: python

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

  the terminal_ shows a random ValueError_ for ``test_duration_w_hours_and_minutes`` when ``wake_time`` is earlier than ``sleep_time``

  .. code-block:: shell

    ValueError: wake_time: "07:33" is earlier than sleep_time: "08:12"
    ValueError: wake_time: "07:46" is earlier than sleep_time: "14:47"
    ValueError: wake_time: "23:10" is earlier than sleep_time: "23:27"
    ValueError: wake_time: "11:32" is earlier than sleep_time: "13:52"

* I add the error to the list of :ref:`Exceptions<errors>` seen in ``test_sleep_duration.py``

  .. code-block:: python

    # Exceptions seen
    # AssertionError
    # TypeError
    # NameError
    # AttributeError
    # ValueError

* then add a `while statement`_ to make sure ``wake_time`` is not earlier than ``sleep_time`` for the difference calculation

  .. code-block:: python

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
            src.sleep_duration.duration(
                sleep_time=sleep_time,
                wake_time=wake_time
            ),
            (
                f'{duration_hours:02}:'
                f'{duration_minutes:02}'
            )
        )

  the test passes with no more random failures, green, green, green, green all the way!

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

* I copy the `assertRaisesRegex`_ statement from ``test_duration_w_an_earlier_wake_than_sleep_time`` then add it to the `while statement`_ to run when ``wake_time`` is earlier than ``sleep_time``

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
                src.sleep_duration.duration(
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
            src.sleep_duration.duration(
                sleep_time=sleep_time,
                wake_time=wake_time
            ),
            (
                f'{duration_hours:02}:'
                f'{duration_minutes:02}'
            )
        )

  and comment out the condition in ``duration`` to make sure the test still works as expected

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for ``test_duration_w_an_earlier_wake_than_sleep_time`` and a random one when ``wake_time`` is earlier than ``sleep_time`` in ``test_duration_w_hours_and_minutes``

  .. code-block:: shell

    AssertionError: ValueError not raised

  the `assertRaisesRegex`_ works as expected. I remove the comments the test is green again again

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
                src.sleep_duration.duration(
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
                src.sleep_duration.duration(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                (
                    f'{duration_hours:02}:'
                    f'{duration_minutes:02}'
                )
            )

  still green

* I add a `staticmethod decorator`_ to calculate the difference between ``wake_time`` and ``sleep_time``

  .. code-block:: python

    @staticmethod
    def get_difference(
        wake_time=None, sleep_time=None
    ):
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

  then call it in ``test_duration_w_hours_and_minutes`` to change the expectation

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
                src.sleep_duration.duration(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                )
            wake_time = random_timestamp()
        else:
            self.assertEqual(
                src.sleep_duration.duration(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                self.get_difference(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )
            )

  the test passes

* I also add an ``assert`` :ref:`method<what is a function?>` for the `assertRaisesRegex`_ block

  .. code-block:: python

    def assertWakeTimeEarlier(
        self, wake_time=None, sleep_time=None
    ):
        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: "{wake_time}"'
            ' is earlier than '
            f'sleep_time: "{sleep_time}"'
        ):
            src.sleep_duration.duration(
                sleep_time=sleep_time,
                wake_time=wake_time
            )

    @staticmethod
    def get_difference(
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
                src.sleep_duration.duration(
                    sleep_time=sleep_time,
                    wake_time=wake_time
                ),
                self.get_difference(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )
            )

  all tests are still passing! Fantastic!


*********************************************************************************
review
*********************************************************************************

The challenge is to write a program_ that calculates the difference between a given wake and sleep time. I ran these tests to get something that comes close to doing it


* :ref:`test_string_splitting`
* :ref:`test_converting_strings_to_numbers`
* :ref:`test_floor_aka_integer_division`
* :ref:`test_the_modulo_operation`
* :ref:`test_duration_w_hours <how to measure sleep duration: test_duration_w_hours>`
* :ref:`test_duration_calculation`
* :ref:`test_duration_w_an_earlier_wake_than_sleep_time  <how to measure sleep duration: test_duration_w_an_earlier_wake_than_sleep_time>`
* :ref:`test_duration_w_hours_and_minutes <how to measure sleep duration: test_duration_w_hours_and_minutes>` where I used a `while statement`_ to make sure that when ``wake_time`` is earlier than ``sleep_time`` the ``duration`` :ref:`function<what is a function?>` raises ValueError_ with a message and returns the right difference between the 2, if ``wake_time`` is later than or the same as ``sleep_time``


Would you like to :ref:`test duration with timestamps that have dates? <how to measure sleep duration: test_duration_w_date_and_time>`

----

:ref:`how to measure sleep duration: tests and solution`