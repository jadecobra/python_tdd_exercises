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

I want to write the program that makes the tests in ``test_sleep_duration.py`` pass without looking at the tests

.. _test_duration_tests_red:

*********************************************************************************
red: make it fail
*********************************************************************************

I delete all the text in ``sleep_duration.py`` and the terminal shows an :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'sleep_duration' has no attribute 'duration'

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

  this means the ``duration`` :ref:`function<functions>` has to make a choice. ``test_duration_w_date_and_time`` expects a timestamp and ``test_duration_w_an_earlier_wake_than_sleep_time`` expects a ValueError_
* I copy the value from the test to replace :ref:`None` in the `return statement`_

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return '17:06:00'

  and get another :ref:`AssertionError`, the expectation of the test looks random
* I change the return statement to show what ``wake_time`` and ``sleep_time`` look like

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (wake_time, sleep_time)

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: ('31/12/99 09:52', '31/12/99 02:32') != '7:20:00'
    AssertionError: ('31/12/99 17:13', '31/12/99 14:38') != '2:35:00'
    AssertionError: ('31/12/99 17:15', '31/12/99 07:12') != '10:03:00'
    AssertionError: ('31/12/99 13:50', '31/12/99 06:44') != '7:06:00'

  ``wake_time`` and ``sleep_time`` are timestamps in the format of ``date``, ``hours`` and ``minutes``
* I go to `python's online documentation`_ and do a search for ``date and time`` and select the datetime_ :ref:`module<ModuleNotFoundError>`
* I add calls to `datetime.datetime.strptime`_ based on `Examples of usage: datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_ to calculate the difference between the two timestamps and use new variable names

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_datetime = datetime.strptime(wake_time, "%d/%m/%y %H:%M")
        sleep_datetime = datetime.strptime(sleep_time, "%d/%m/%y %H:%M")

        return (wake_datetime, sleep_datetime)

  the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'datetime' has no attribute 'strptime'

  my `import statement`_ is different than the `example in the documentation <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_
* I change the calls

  .. code-block:: python

    wake_datetime = datetime.datetime.strptime(
        wake_time, "%d/%m/%y %H:%M"
    )
    sleep_datetime = datetime.strptime(
        sleep_time, "%d/%m/%y %H:%M"
    )

  and get an :ref:`AssertionError` for

  .. code-block:: python

    AssertionError: (datetime.datetime(1999, 12, 31, 5, 33), [35 chars] 48)) != '12:45:00'

* I want to see what happens when I change the return statement to a calculation

  .. code-block:: python

    return (wake_datetime-sleep_datetime)

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: datetime.timedelta(seconds=74880) != '20:48:00'

* I add the str_ constructor

  .. code-block:: python

    return str(wake_datetime-sleep_datetime)

  I am left with the :ref:`AssertionError` for ``test_duration_w_an_earlier_wake_than_sleep_time``

  .. code-block:: python

    AssertionError: ValueError not raised

* I add a condition based on the name of the test

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_datetime = datetime.datetime.strptime(
            wake_time, "%d/%m/%y %H:%M"
        )
        sleep_datetime = datetime.datetime.strptime(
            sleep_time, "%d/%m/%y %H:%M"
        )

        if wake_datetime < sleep_datetime:
            raise ValueError
        else:
            return str(wake_datetime-sleep_datetime)

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: "wake_time: 31/12/99 01:00 is earlier than sleep_time: 31/12/99 02:00" does not match ""
    AssertionError: "wake_time: 31/12/99 01:00 is earlier than sleep_time: 31/12/99 02:00" does not match ""
    AssertionError: "wake_time: 31/12/99 20:30 is earlier than sleep_time: 31/12/99 22:56" does not match ""
    AssertionError: "wake_time: 31/12/99 11:21 is earlier than sleep_time: 31/12/99 21:01" does not match ""

  the message in the ValueError_ does not match the expectation of the tests

* I copy the message from the terminal then add it to the ValueError_

  .. code-block:: python

    raise ValueError(
        "wake_time: 31/12/99 01:00"
        " is earlier than "
        "sleep_time: 31/12/99 02:00"
    )

  and get a random :ref:`AssertionError`

  .. code-block:: python

    AssertionError: "wake_time: 31/12/99 17:14 is earlier than sleep_time: 31/12/99 18:01" does not match "wake_time: 31/12/99 01:00 is earlier than sleep_time: 31/12/99 02:00"
    AssertionError: "wake_time: 31/12/99 00:45 is earlier than sleep_time: 31/12/99 17:53" does not match "wake_time: 31/12/99 01:00 is earlier than sleep_time: 31/12/99 02:00"
    AssertionError: "wake_time: 31/12/99 12:52 is earlier than sleep_time: 31/12/99 21:25" does not match "wake_time: 31/12/99 01:00 is earlier than sleep_time: 31/12/99 02:00"
    AssertionError: "wake_time: 31/12/99 01:25 is earlier than sleep_time: 31/12/99 13:27" does not match "wake_time: 31/12/99 01:00 is earlier than sleep_time: 31/12/99 02:00"

  the timestamps in the ValueError_ message are different from what the test expects

* I change it to use the variables

  .. code-block:: python

    raise ValueError(
        f"wake_time: {wake_time}"
        " is earlier than "
        f"sleep_time: {sleep_time}"
    )

  and the terminal shows passing tests with no more random failures

.. _test_duration_tests_refactor:

*********************************************************************************
refactor: make it better
*********************************************************************************

* I create a function to call `datetime.datetime.strptime`_

  .. code-block:: python

    def get_datetime(timestamp):
        return datetime.datetime.strptime(
            timestamp, '%d/%m/%y %H:%M'
        )


    def duration(wake_time=None, sleep_time=None):
    ...

  then call it in ``duration``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_datetime = get_datetime(wake_time)
        sleep_datetime = get_datetime(sleep_time)
        ...

  all tests are still green!

*********************************************************************************
review
*********************************************************************************

I wrote a program by following the output in the terminal and `python's online documentation`_ that made the tests in ``test_sleep_duration.py`` pass