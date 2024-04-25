.. include:: ../../links.rst

.. _test_duration_tests:

#################################################################################
how to measure sleep duration: test_duration_tests
#################################################################################

This is part 5 of a program that calculates the difference between a given wake and sleep time.

.. contents:: table of contents
  :local:
  :depth: 2

----

I want to write the program that makes the tests in ``test_sleep_duration.py`` pass

.. _test_duration_tests_red:

*********************************************************************************
red: make it fail
*********************************************************************************

I delete all the text in ``sleep_duration.py`` and the terminal shows an :ref:`AttributeError`

.. _test_duration_tests_green:

*********************************************************************************
green: make it pass
*********************************************************************************

* I add the name

  .. code-block:: python

    duration

  and get a NameError_

* then assign the name to :ref:`None`

  .. code-block:: python

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I change ``duration`` to a :ref:`function<functions>` to make it callable_

  .. code-block:: python

    def duration():
        return None

  which gives me another :ref:`TypeError`

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'wake_time'

  and I add the name to the :ref:`function<functions>` signature with a default value of :ref:`None`

  .. code-block:: python

    def duration(wake_time=None):

  the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'sleep_time'

  which I add to the signature with a default value of :ref:`None`

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):

  and get an :ref:`AssertionError` for ``test_duration_w_date_and_time``

  .. code-block:: python

    AssertionError: None != '-1 day, 12:53:00'
    AssertionError: None != '-1 day, 8:42:00'
    AssertionError: None != '4:04:00'
    AssertionError: None != '17:06:00'

  and another :ref:`AssertionError` for ``test_duration_w_an_earlier_wake_than_sleep_time``

  .. code-block:: python

    AssertionError: ValueError not raised

  this means the ``duration`` :ref:`function<functions>` has to make a choice. ``test_duration_w_hours_and_minutes`` expects a timestamp and ``test_duration_w_an_earlier_wake_than_sleep_time`` expects a ValueError_
* I add a condition based on the name of the test

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        if wake_time < sleep_time:
            raise ValueError
        else:
            return None

  and get an :ref:`AssertionError` for ``test_duration_w_hours_and_minutes``  and ``test_duration_w_an_earlier_wake_than_sleep_time``

  .. code-block:: python

    AssertionError: "wake_time: 31/12/99 01:00 is earlier than sleep_time: 31/12/99 02:00" does not match ""
    AssertionError: "wake_time: 31/12/99 01:00 is earlier than sleep_time: 31/12/99 02:00" does not match ""
    AssertionError: "wake_time: 31/12/99 20:30 is earlier than sleep_time: 31/12/99 22:56" does not match ""
    AssertionError: "wake_time: 31/12/99 11:21 is earlier than sleep_time: 31/12/99 21:01" does not match ""

  the message in the ValueError_ does not match the expectations of the tests

* I copy the message from the terminal then add it to the ValueError_

  .. code-block:: python

    raise ValueError(
        "wake_time: 31/12/99 01:00"
        " is earlier than "
        "sleep_time: 31/12/99 02:00"
    )

  and get an :ref:`AssertionError` for ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    "wake_time: 31/12/99 07:56 is earlier than sleep_time: 31/12/99 13:31" does not match "wake_time: 31/12/99 01:00 is earlier than sleep_time: 31/12/99 02:00"

  the timestamp values do not match. I :ref:`interpolate<string interpolation>` the values for ``wake_time`` and ``sleep_time`` since they change

  .. code-block:: python

    raise ValueError(
        f"wake_time: {wake_time}"
        " is earlier than "
        f"sleep_time: {sleep_time}"
    )

  and the terminal shows random successes and the previous :ref:`AssertionErrors<AssertionError>` for ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    AssertionError: None != '6:55:00'
    AssertionError: None != '8:38:00'
    AssertionError: None != '9:57:00'
    AssertionError: None != '12:53:00'

* I copy the value from the terminal and replace :ref:`None` in the `return statement`_

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        if wake_time < sleep_time:
            raise ValueError(
                f"wake_time: {wake_time}"
                " is earlier than "
                f"sleep_time: {sleep_time}"
            )
        else:
            return '17:06:00'

  and get a random :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '17:06:00' != '6:30:00'
    AssertionError: '17:06:00' != '3:32:00'
    AssertionError: '17:06:00' != '13:05:00'
    AssertionError: '17:06:00' != '9:38:00'

  the expectations of the test look random. I need a different solution






* I copy the variables from ``test_duration_w_date_and_time``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        pattern = '%d/%m/%y %H:%M'
        wake_datetime = datetime.datetime.strptime(
            wake_time, pattern
        )
        sleep_datetime = datetime.datetime.strptime(
            sleep_time, pattern
        )

  and get a NameError_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

  I add an `import statement`_ for datetime_

  .. code-block:: python

    import datetime


    def duration(wake_time=None, sleep_time=None):

* then change the return to the difference between the two datetime_ objects

  .. code-block:: python

    return str(
        wake_datetime
      - sleep_datetime
    )

  the terminal shows an :ref:`AssertionError` for ``test_duration_w_an_earlier_wake_than_sleep_time``

  .. code-block:: python

    AssertionError: ValueError not raised

* I add a condition to the ``duration`` :ref:`function<functions>`

  .. code-block:: python

    if wake_datetime < sleep_datetime:
        raise ValueError
    else:
        return str(
            wake_datetime
        - sleep_datetime
        )

  which gives me another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: "wake_time: 31/12/99 01:00 is earlier than sleep_time: 31/12/99 02:00" does not match ""

* I copy the message from ``assertWakeTimeEarlier`` and paste it as the message for the ValueError_ in ``duration``

  .. code-block:: python

    if wake_datetime < sleep_datetime:
        raise ValueError(
            f'wake_time: {wake_time}'
            ' is earlier than '
            f'sleep_time: {sleep_time}'
        )
    else:
        return str(
            wake_datetime
        - sleep_datetime
        )

  and the terminal shows passing tests

.. _test_duration_tests_refactor:

*********************************************************************************
refactor: make it better
*********************************************************************************

* I create a :ref:`function<functions>` in ``sleep_duration.py`` to replace the calls to `datetime.datetime.strptime`_

  .. code-block:: python

    def get_datetime(wake_time, pattern):
        return datetime.datetime.strptime(
            wake_time, pattern
        )

  and change the calls in ``duration``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        pattern = '%d/%m/%y %H:%M'
        wake_datetime = get_datetime(
            wake_time, pattern
        )
        sleep_datetime = get_datetime(
            sleep_time, pattern
        )

  still green

* pattern gets used for ``wake_datetime`` and ``sleep_datetime`` object, I can add it to the ``get_datetime`` as a parameter with a default value

  .. code-block:: python

    def get_datetime(wake_time, pattern='%d/%m/%y %H:%M'):
    ...

  and remove ``pattern`` from ``duration``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_datetime = get_datetime(
            wake_time
        )
        sleep_datetime = get_datetime(
            sleep_time
        )

  the terminal still shows passing tests

----