.. _test_duration_w_date_and_time_refactor:

refactor: make it better
--------------------------------------------------------

* I remove some repetition from ``test_duration_w_date_and_time`` by using variables for the `datetime.datetime`_ objects

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        pattern = '%d/%m/%y %H:%M'

        wake_time = f'31/12/99 {random_hour():02}:{random_minutes():02}'
        wake_datetime_object = datetime.datetime.strptime(
            wake_time, pattern
        )

        sleep_time = f'31/12/99 {random_hour():02}:{random_minutes():02}'
        wake_datetime_object = datetime.datetime.strptime(
            sleep_time, pattern
        )

        difference = (
            wake_datetime_object
          - sleep_datetime_object
        )

        try:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                str(difference)
            )
        except ValueError:
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: {wake_datetime_object} is earlier '
                f'than sleep_time: {sleep_datetime_object}'
            ):
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )

* I remove ``duration_a`` from ``sleep_duration.py`` because ``duration`` is a better solution
* I remove ``parse_timestamp`` and ``get_total_minutes`` because they are no longer used
* and I remove the ``difference`` variable from ``duration`` since it is only used once. I can do the calculation directly

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time = get_datetime_object(wake_time)
        sleep_time = get_datetime_object(sleep_time)

        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
        else:
            return str(wake_time-sleep_time)

  and we are still green all the way

.. _sleep_duration_review:

review
********************************************************

The challenge was to create a :ref:`function<functions>` that calculates the difference between 2 given timestamps. I ran the following tests to help me create it

* `test_string_attributes_and_methods`_
* `test_string_splitting`_ where I

  - used the `help system`_ to view documentation
  - used the `str.split`_ :ref:`method<functions>`_ to split a string_ on a separator
  - indexed the :doc:`list </data_structures/lists/lists>` from the split to get specific items

* `test_converting_strings_to_integers`_
* `test_floor_aka_integer_division`_
* `test_modulo_operation`_
* `test_datetime_objects`_ where I

  - used `python's online documentation`_
  - converted a string_ to a `datetime.datetime`_ object using the `datetime.datetime.strptime`_ :ref:`method<functions>`

* `test_subtracting_datetime_objects`_
* `test_converting_timedelta_to_string`_
* `test_duration_w_date_and_time`_

  - using `random.randint`_ to generate random integers for hours and minutes
  - using timestamps with dates and times ranging from ``'00:00'`` up to and including ``'23:59'`` as inputs for ``wake_time`` and ``sleep_time``
  - confirming a ValueError_ is raised when ``wake_time`` is earlier than ``sleep_time``
  - `test_duration_w_hours`_
  - `test_duration_w_hours_and_minutes`_
  - `test_duration_calculation`_
  - `test_duration_w_earlier_wake_than_sleep_time`_

I also encountered the following exceptions

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`
* SyntaxError_
* ValueError_

----

:doc:`/code/code_sleep_duration`
