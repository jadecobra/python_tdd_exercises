.. include:: ../links.rst

########################################################
test_duration_w_hours_and_minutes
########################################################

In this chapter, I take a look at building a program that returns the duration between a given sleep and wake time.

----

The ``duration`` :ref:`function<functions>` has only been tested with timestamps that have random hours and ``00`` as minutes. For it to meet the requirements, it should accept timestamps with random hours and random minutes.

.. _test_duration_w_hours_and_minutes_red:

red: make it fail
========================================================

* I copy ``test_duration_w_hours`` in ``test_sleep_duration.py``, paste it below the original
* then rename the copy to ``test_duration_w_hours_and_minutes`` adding variables for random minutes

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        wake_hour = random_hour()
        wake_minutes = random.randint(0, 59)

        sleep_hour = random_hour()
        sleep_minutes = random.randint(0, 59)

        difference_hours = wake_hour - sleep_hour
        difference_minutes = wake_minutes - sleep_minutes

        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour:02}:{wake_minutes:02}',
                sleep_time=f'{sleep_hour:02}:{sleep_minutes:02}'
            ),
            f'{difference_hours:02}:{difference_minutes:02}'
        )

  and the terminal shows an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: 4 != '4:-20'
    AssertionError: 6 != '-7:00'
    AssertionError: -5 != '-15:-37'
    AssertionError: -8 != '-40:-40'

  the ``duration`` :ref:`function<functions>` returns a number but ``test_duration_w_hours_and_minutes`` expects a string_ that contains the subtraction of ``sleep_hour`` from ``wake_hour`` and the subtraction of ``sleep_minutes`` from ``wake_minutes`` separated by a ``:``

.. _test_duration_w_hours_and_minutes_green:

green: make it pass
========================================================

* I make the output of the ``duration`` :ref:`function<functions>` match the format of the expected value in the test by adding the same variables and calculations

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

        return f'{difference_hours:02}:{difference_minutes:02}'

  and the terminal shows an :ref:`AssertionError` for ``test_duration_w_hours`` because it expects an integer_ not a string_

  .. code-block:: python

    AssertionError: '5:5' != 5
    AssertionError: '-8:-8' != -8
    AssertionError: '1:1' != 1
    AssertionError: '-3:-3' != -3

  and an :ref:`AssertionError` for ``test_duration_w_hours_and_minutes`` because ``duration`` returns the same value for ``difference_hours`` and ``difference_minutes``

  .. code-block:: python

    AssertionError: '7:7' != '07:-13'
    AssertionError: '-16:-16' != '-16:-22'
    AssertionError: '14:14' != '14:36'
    AssertionError: '-2:-2' != '-2:-49'

* The change for the new test has made ``test_duration_w_hours`` fail so I disable ``test_duration_w_hours_and_minutes`` with the `unittest.skip decorator`_ while I fix the failure

  .. code-block:: python

    @unittest.skip
    def test_duration_w_hours_and_minutes(self):
    ...

* then I make ``test_duration_w_hours`` use the new format

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random_hour()
        sleep_hour = random_hour()

        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour:02}:00',
                sleep_time=f'{sleep_hour:02}:00'
            ),
            f'{wake_hour-sleep_hour}:00'
        )

  and the terminal shows an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: '06:00' != '6:00'
    AssertionError: '-19:-19' != '-19:00'
    AssertionError: '17:17' != '17:00'
    AssertionError: '-8:-8' != '-8:00'

  the ``duration`` :ref:`function<functions>` returns the right value for hours and minutes, but displays 1 digit for minutes while ``test_duration_w_hours`` expects 2 digits for minutes

* I add ``difference_hours`` to ``test_duration_w_hours`` so it can show 2 digits for hours

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random_hour()
        sleep_hour = random_hour()

        difference_hours = (
            wake_hour - sleep_hour
        )

        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour:02}:00',
                sleep_time=f'{sleep_hour:02}:00'
            ),
            f'{difference_hours:02}:00'
        )

  the terminal shows an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: '-9:-9' != '-9:00'
    AssertionError: '03:03' != '03:00'
    AssertionError: '-15:-23' != '-15:00'
    AssertionError: '12:12' != '12:00'


  the ``duration`` :ref:`function<functions>` returns the same values for hours and minutes because it calls ``get_hour`` for the hours and minutes while ``test_duration_w_hours`` expects the minutes to always be ``00``. I need a different calculation for ``difference_minutes``

* I copy ``get_hour`` in ``sleep_duration.py``, paste it below the original
* then change the name of the copy to ``get_minutes`` and the index to ``1`` to get the minutes part from splitting the timestamp

  .. code-block:: python

    def get_hour(timestamp):
        return int(timestamp.split(':')[0])

    def get_minutes(timestamp):
        return int(timestamp.split(':')[1])

* I also add calls to ``get_minutes`` in the calculation for ``difference_minutes`` in the ``duration`` :ref:`function<functions>`

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference_hours = (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )
        difference_minutes = (
            get_minutes(wake_time)
          - get_minutes(sleep_time)
        )

        return f'{difference_hours:02}:{difference_minutes:02}'

  and things are green again with no more random failures

* When I take away the `unittest.skip decorator`_ from ``test_duration_w_hours_and_minutes``, it passes. It looks like making sure ``test_duration_w_hours`` passed, also made ``test_duration_w_hours_and_minutes`` pass

.. _test_duration_w_hours_and_minutes_refactor:

refactor: make it better
========================================================

* I remove ``test_duration_w_hours`` because the timestamps it tests are included in what is provided by ``test_duration_w_hours_and_minutes`` which uses a random integer_ from ``0`` up to and including ``23`` for hours, and a random integer_ from ``0`` up to and including ``59`` for minutes. This means it covers all timestamps from ``00:00`` up to and including ``23:59``, which is all the hours and minutes in a day
* and then add a :ref:`function<functions>` for making random minutes

  .. code-block:: python

    def random_minutes():
        return random.randint(0, 59)


    class TestSleepDuration(unittest.TestCase):
    ...

  and add calls to it in ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        wake_hour = random_hour()
        wake_minutes = random_minutes()

        sleep_hour = random_hour()
        sleep_minutes = random_minutes()

        difference_hours = wake_hour - sleep_hour
        difference_minutes = wake_minutes - sleep_minutes

        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour:02}:{wake_minutes:02}',
                sleep_time=f'{sleep_hour:02}:{sleep_minutes:02}'
            ),
            f'{difference_hours:02}:{difference_minutes:02}'
        )

  the terminal shows all tests are still passing

----

:doc:`/code/code_sleep_duration`