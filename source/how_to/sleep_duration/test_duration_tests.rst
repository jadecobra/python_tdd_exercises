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

    AssertionError: None != '17:06:00'

  and another :ref:`AssertionError` for ``test_duration_w_an_earlier_wake_than_sleep_time``

  .. code-block:: python

    AssertionError: ValueError not raised

* I copy the value from the terminal and replace :ref:`None` in the `return statement`_

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return '17:06:00'

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