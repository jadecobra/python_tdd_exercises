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

I want to write a program that makes the tests in ``test_sleep_duration.py`` pass without looking at them

.. _test_duration_tests_red:

*********************************************************************************
red: make it fail
*********************************************************************************

* I close ``test_sleep_duration.py``
* then delete all the text in ``sleep_duration.py`` and the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'sleep_duration' has no attribute 'get_datetime'

.. _test_duration_tests_green:

*********************************************************************************
green: make it pass
*********************************************************************************

* I add a list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AttributeError

* and the missing name to ``sleep_duration.py``

  .. code-block:: python

    get_datetime

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'get_datetime' is not defined

  I add it to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered as well

  .. code-block:: python

    # Exceptions Encountered
    # AttributeError
    # NameError

* and define the name by assigning it to :ref:`None`

  .. code-block:: python

    get_datetime = None

  which gives me a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  another error for the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AttributeError
    # NameError
    # TypeError

* I change ``get_datetime`` to a :ref:`function<functions>` to make it callable_

  .. code-block:: python

    def get_datetime():
        return None

  and the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: get_datetime() takes 0 positional arguments but 1 was given

  then I add a name to the :ref:`function<functions>` signature

  .. code-block:: python

    def get_datetime(argument):

  and get an :ref:`AssertionError`

  .. code-block:: python

    None != datetime.datetime(2006, 11, 21, 7, 1)
    None != datetime.datetime(2006, 11, 21, 10, 59)
    None != datetime.datetime(2006, 11, 21, 13, 28)
    None != datetime.datetime(2006, 11, 21, 19, 8)

  which I add to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AttributeError
    # NameError
    # TypeError
    # AssertionError

* I copy the value from the terminal to change :ref:`None` in the `return statement`_

  .. code-block:: python

    def get_datetime(argument):
        return datetime.datetime(2006, 11, 21, 19, 8)

  and the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

* then I add an `import statement`_ for the datetime_ :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

      import datetime


      def get_datetime(argument):
      ...

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: datetime.datetime(2006, 11, 21, 19, 8) != datetime.datetime(2006, 11, 21, 0, 15)

  the expected values changed

* I change the `return statement`_ to show the input argument because I want to see how it is different from the expectation of the test

  .. code-block:: python

    def get_datetime(argument):
        return argument

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '2006/11/21 02:58' != datetime.datetime(2006, 11, 21, 2, 58)
    AssertionError: '2006/11/21 03:14' != datetime.datetime(2006, 11, 21, 3, 14)
    AssertionError: '2006/11/21 08:30' != datetime.datetime(2006, 11, 21, 8, 30)
    AssertionError: '2006/11/21 23:41' != datetime.datetime(2006, 11, 21, 23, 41)

  I need a way to convert a string_ that has a date and time to a `datetime.datetime`_ object

* I use the `example from the datetime documentation <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_ to do the conversion

  .. code-block:: python

    def get_datetime(argument):
        return datetime.datetime.strptime(
            argument, '%Y/%m/%d %H:%M'
        )

  and get an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'sleep_duration' has no attribute 'duration'

* I add the name below ``get_datetime``

  .. code-block::python

  .. code-block:: python

    duration

  and get a NameError_

  .. code-block:: python

    NameError: name 'duration' is not defined

* then assign the name to :ref:`None` to define it

  .. code-block:: python

    duration = None

  which gives me a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I define it as a :ref:`function<functions>` to make it callable_

  .. code-block:: python

    def duration():
        return None

  and the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'sleep_time'

  I add the name to the :ref:`function<functions>` signature

  .. code-block:: python

    def duration(sleep_time):

  and get a :ref:`TypeError` for another keyword argument

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'wake_time'

  which I add to the signature

  .. code-block:: python

    def duration(sleep_time, wake_time):

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: ValueError not raised

* I change the `return statement`_ to raise a ValueError_

  .. code-block:: python

    def duration(sleep_time, wake_time):
        raise ValueError

  and get another :ref:`AssertionError` because the message in the ValueError_ does not match the expectation of the test

  .. code-block:: python

    AssertionError: "wake_time: "1999/12/30 12:07" is earlier than sleep_time: "1999/12/31 13:37"" does not match ""
    AssertionError: "wake_time: "1999/12/30 05:05" is earlier than sleep_time: "1999/12/31 18:59"" does not match ""
    AssertionError: "wake_time: "1999/12/30 02:27" is earlier than sleep_time: "1999/12/31 15:12"" does not match ""
    AssertionError: "wake_time: "1999/12/30 19:05" is earlier than sleep_time: "1999/12/31 20:03"" does not match ""

* I copy the message from the terminal, then add it to the ValueError_

  .. code-block:: python

    def duration(wake_time, sleep_time):
        raise ValueError(
            "wake_time: "1999/12/30 19:05" is earlier than sleep_time: "1999/12/31 20:03""
        )

  and get a SyntaxError_ with this message

  .. code-block:: python

    SyntaxError: invalid syntax. Perhaps you forgot a comma?

  or this message

  .. code-block:: python

    SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

  python does not know where the string ends or begins because the message has double quotes inside double quotes. I add the error to the list of :doc:`Exceptions</how_to/exception_handling_programs>`

  .. code-block:: python

    # Exceptions Encountered
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError

* then change the outer double quotes to single quotes

  .. code-block:: python

    def duration(wake_time, sleep_time):
        raise ValueError(
            'wake_time: "1999/12/31 19:05"'
            ' is earlier than '
            'sleep_time: "1999/12/31 20:03"'
        )

  which gives me another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: "wake_time: "1999/12/31 03:18" is earlier than sleep_time: "1999/12/31 13:34"" does not match "wake_time: "30/12/99 19:05" is earlier than sleep_time: "1999/12/31 20:03""
    AssertionError: "wake_time: "1999/12/31 04:56" is earlier than sleep_time: "1999/12/31 05:27"" does not match "wake_time: "30/12/99 19:05" is earlier than sleep_time: "1999/12/31 20:03""
    AssertionError: "wake_time: "1999/12/31 05:58" is earlier than sleep_time: "1999/12/31 03:14"" does not match "wake_time: "30/12/99 19:05" is earlier than sleep_time: "1999/12/31 20:03""
    AssertionError: "wake_time: "1999/12/31 22:25" is earlier than sleep_time: "1999/12/31 05:05"" does not match "wake_time: "30/12/99 19:05" is earlier than sleep_time: "1999/12/31 20:03""

  the timestamps in the ValueError_ message are not the same

* I :doc:`interpolate</how_to/pass_values>` ``wake_time`` and ``sleep_time`` in the message

  .. code-block:: python

    def duration(wake_time, sleep_time):
        raise ValueError(
            f'wake_time: "{wake_time}"'
            ' is earlier than '
            f'sleep_time: "{sleep_time}"'
        )

  and get a ValueError_

  .. code-block:: python

    ValueError: wake_time: "1999/12/31 19:54" is earlier than sleep_time: "1999/12/31 18:12"
    ValueError: wake_time: "1999/12/31 22:07" is earlier than sleep_time: "1999/12/31 21:33"
    ValueError: wake_time: "1999/12/31 18:53" is earlier than sleep_time: "1999/12/31 18:01"
    ValueError: wake_time: "1999/12/31 23:39" is earlier than sleep_time: "1999/12/31 23:16"

  this is not right, the timestamps for ``wake_time`` are not earlier than ``sleep_time``, I have to add a condition to ``duration``

* I add the error to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError
    # ValueError

  then add a condition based on the message from the ValueError_

  .. code-block:: python

    def duration(sleep_time, wake_time):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            return None

  which gives me an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != '0:00:00'
    AssertionError: None != '1:02:00'
    AssertionError: None != '2:55:00'
    AssertionError: None != '16:59:00'

  the test expects a timestamp

* I change the `return statement`_ to show its inputs. I want to see the difference between ``wake_time``, ``sleep_time`` and the expectation of the test

  .. code-block:: python

    def duration(sleep_time, wake_time):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            return (sleep_time, wake_time)

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: ('1999/12/31 06:44', '1999/12/31 05:33') != '1:11:00'
    AssertionError: ('1999/12/31 17:53', '1999/12/31 11:23') != '6:30:00'
    AssertionError: ('1999/12/31 10:25', '1999/12/31 02:15') != '8:10:00'
    AssertionError: ('1999/12/31 19:14', '1999/12/31 10:00') != '9:14:00'

  it looks like the test expects the difference between the timestamps

* I return the difference between ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def duration(sleep_time, wake_time):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            return (sleep_time - wake_time)

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

  I still cannot subtract one string from another. I change the `return statement`_ back

* then add calls to ``get_datetime``

  .. code-block:: python

    def duration(sleep_time, wake_time):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            return (
                get_datetime(sleep_time),
                get_datetime(wake_time)
            )

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (datetime.datetime(1999, 12, 31, 8, 9), datetime.datetime(1999, 12, 31, 11, 38)) != '3:29:00'
    AssertionError: (datetime.datetime(1999, 12, 31, 14, 11),[36 chars] 34)) != '5:23:00'
    AssertionError: (datetime.datetime(1999, 12, 31, 3, 6), datetime.datetime(1999, 12, 31, 14, 56)) != '11:50:00'
    AssertionError: (datetime.datetime(1999, 12, 31, 5, 33), [35 chars] 48)) != '12:45:00'

* I want to see what will happen when I change the return statement to a calculation

  .. code-block:: python

    def duration(sleep_time, wake_time):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            return (
                get_datetime(sleep_time)
              - get_datetime(wake_time)
            )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: datetime.timedelta(days=-1, seconds=72900) != '3:45:00'
    AssertionError: datetime.timedelta(days=-1, seconds=45060) != '11:29:00'
    AssertionError: datetime.timedelta(days=-1, seconds=47220) != '10:53:00'
    AssertionError: datetime.timedelta(days=-1, seconds=84840) != '0:26:00'

  the test expects a string_ and the :ref:`function<functions>` returns a `datetime.timedelta`_ object. The values for days are also negative. I think I am doing something wrong

* I add the str_ constructor_ to match the format of the expectation

  .. code-block:: python

    def duration(sleep_time, wake_time):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            return str(
                get_datetime(sleep_time)
              - get_datetime(wake_time)
            )

  and get another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '-1 day, 23:22:00' != '0:38:00'
    AssertionError: '-1 day, 18:41:00' != '5:19:00'
    AssertionError: '-1 day, 21:22:00' != '2:38:00'
    AssertionError: '-1 day, 18:27:00' != '5:33:00'

  the ``duration`` :ref:`function<functions>` returns negative timestamps but the test expects positive timestamps

* I switch ``wake_time`` and ``sleep_time`` in the `return statement`_

  .. code-block:: python

    def duration(sleep_time, wake_time):
        if wake_time < sleep_time:
            raise ValueError(
                f'wake_time: "{wake_time}"'
                ' is earlier than '
                f'sleep_time: "{sleep_time}"'
            )
        else:
            return str(
                get_datetime(wake_time)
              - get_datetime(sleep_time)
            )

  and the terminal shows passing tests! YES!!

.. _test_duration_tests_refactor:

*********************************************************************************
refactor: make it better
*********************************************************************************

* I change the name of the positional argument in ``get_datetime`` to be more descriptive

  .. code-block:: python

    def get_datetime(timestamp):
        return datetime.datetime.strptime(
            timestamp, '%Y/%m/%d %H:%M'
        )

  and the terminal shows all tests are still passing

* I remove the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered because the program does not need it

*********************************************************************************
review
*********************************************************************************

The challenge was to write a program that makes the tests in ``test_sleep_duration.py`` pass without looking at them. I wrote something that returns the difference between a given ``wake_time`` and ``sleep_time`` by following these exceptions from the terminal

* :ref:`AttributeError`
* NameError_
* :ref:`TypeError`
* :ref:`AssertionError`
* SyntaxError_
* ValueError_

----

:doc:`/code/code_sleep_duration`
