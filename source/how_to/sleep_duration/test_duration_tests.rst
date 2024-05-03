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

I want to write the program that makes the tests in ``test_sleep_duration.py`` pass without looking at them

.. _test_duration_tests_red:

*********************************************************************************
red: make it fail
*********************************************************************************

* I close ``test_sleep_duration.py``
* then delete all the text in ``sleep_duration.py`` and the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'sleep_duration' has no attribute 'get_datetime'

  which I add to a list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AttributeError

.. _test_duration_tests_green:

*********************************************************************************
green: make it pass
*********************************************************************************

* I add the name to the file

  .. code-block:: python

    get_datetime

  and get a NameError_

  .. code-block:: python

    NameError: name 'get_datetime' is not defined

* I add it to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered as well

  .. code-block:: python

    # Exceptions Encountered
    # AttributeError
    # NameError

* then define the name by assigning it to :ref:`None`

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

  I add a name to the :ref:`function<functions>` signature

  .. code-block:: python

    def get_datetime(argument):

  and get an :ref:`AssertionError`

  .. code-block:: python

    None != datetime.datetime(1999, 12, 31, 7, 1)
    None != datetime.datetime(1999, 12, 31, 10, 59)
    None != datetime.datetime(1999, 12, 31, 13, 28)
    None != datetime.datetime(1999, 12, 31, 19, 8)

* which I add to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AttributeError
    # NameError
    # TypeError
    # AssertionError

* I copy the value from the terminal to change :ref:`None` in the `return statement`_

  .. code-block:: python

    def get_datetime(argument):
        return datetime.datetime(1999, 12, 31, 19, 8)

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

* I add an `import statement`_ for the datetime_ :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

      import datetime


      def get_datetime(argument):
      ...

  and get another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: datetime.datetime(1999, 12, 31, 19, 8) != datetime.datetime(1999, 12, 31, 0, 15)

  the values change

* I change the `return statement` to show the input argument because I want to see the relationship to the expectation of the test

  .. code-block:: python

    def get_datetime(argument):
        return argument

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '31/12/99 02:58' != datetime.datetime(1999, 12, 31, 2, 58)
    AssertionError: '31/12/99 03:14' != datetime.datetime(1999, 12, 31, 3, 14)
    AssertionError: '31/12/99 08:30' != datetime.datetime(1999, 12, 31, 8, 30)
    AssertionError: '31/12/99 23:41' != datetime.datetime(1999, 12, 31, 23, 41)

  I need a way to convert a string_ that has a date and time to a `datetime.datetime`_ object

* I look at `Examples of usage: datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_ for `datetime.datetime`_ objects to learn how to do the conversion. The example with the `datetime.datetime.strptime` :ref:`method<functions>` looks like what I need. I make a copy of it to add to the ``get_datetime`` :ref:`function<functions>`, and change the timestamp to reference ``argument``

  .. code-block:: python

    def get_datetime(argument):
        return datetime.strptime(
            argument, "%d/%m/%y %H:%M"
        )

  which gives me an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'datetime' has no attribute 'strptime'

  the reference to the ``strptime`` :ref:`method<functions>` is not right, my `import statement`_ is different from `the example in the documentation <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_. I add the module name to the call

  .. code-block:: python

    def get_datetime(argument):
        return datetime.datetime.strptime(
            argument, "%d/%m/%y %H:%M"
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

    TypeError: duration() got an unexpected keyword argument 'wake_time'

  I add the name to the :ref:`function<functions>` signature with a default value of :ref:`None`

  .. code-block:: python

    def duration(wake_time=None):

  and get a :ref:`TypeError` for another keywwrd argument

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'sleep_time'

  which I add to the signature with a default value of :ref:`None`

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):

  the terminal shows an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: None != '0:00:00'
    AssertionError: None != '1:02:00'
    AssertionError: None != '2:55:00'
    AssertionError: None != '16:59:00'

  or

  .. code-block:: python

    AssertionError: ValueError not raised

  it looks like the ``duration`` :ref:`function<functions>` has to make a choice. The test expects a timestamp or a ValueError_

* I change the `return statement`_ to display its inputs and ignore the :ref:`AssertionErrors<AssertionError>` about the ValueError_ to work on it later. I want to see the relationship between ``wake_time``, ``sleep_time`` and the expectation of the test so I can figure out the timestamp parts

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (wake_time, sleep_time)

  the terminal shows an :ref:`AssertionError` when it does not expect a ValueError_

  .. code-block:: python

    AssertionError: ('31/12/99 06:44', '31/12/99 05:33') != '1:11:00'
    AssertionError: ('31/12/99 17:53', '31/12/99 11:23') != '6:30:00'
    AssertionError: ('31/12/99 10:25', '31/12/99 02:15') != '8:10:00'
    AssertionError: ('31/12/99 19:14', '31/12/99 10:00') != '9:14:00'

  it looks like the test expects the difference between the timestamps

* I add calls to ``get_datetime`` to calculate the difference between the two timestamps and use new variable names

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_datetime = get_datetime(wake_time)
        sleep_datetime = get_datetime(sleep_time)
        return (wake_datetime, sleep_datetime)

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (datetime.datetime(1999, 12, 31, 5, 33), [35 chars] 48)) != '12:45:00'

* I want to see what happens when I change the return statement to a calculation

  .. code-block:: python

    return (wake_datetime - sleep_datetime)

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: datetime.timedelta(seconds=4020) != '1:07:00'
    AssertionError: datetime.timedelta(seconds=16200) != '4:30:00'
    AssertionError: datetime.timedelta(seconds=52740) != '14:39:00'
    AssertionError: datetime.timedelta(seconds=74880) != '20:48:00'

* I add the str_ constructor_

  .. code-block:: python

    return str(wake_datetime - sleep_datetime)

  the test passes, and I am left with the random :ref:`AssertionError` when ValueError_ is not raised

* I add a condition to the :ref:`function<functions>` based on the name ``assertWakeTimeEarlier`` and the differences I encountered were all positive

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        if wake_time < sleep_time:
            raise ValueError
        else:
            wake_datetime = get_datetime(wake_time)
            sleep_datetime = get_datetime(sleep_time)
            return str(wake_datetime - sleep_datetime)

  the terminal shows an :ref:`AssertionError` because the message in the ValueError_ does not match the expectation of the test

  .. code-block:: python

    AssertionError: "wake_time: "31/12/99 12:07" is earlier than sleep_time: "31/12/99 13:37"" does not match ""
    AssertionError: "wake_time: "31/12/99 05:05" is earlier than sleep_time: "31/12/99 18:59"" does not match ""
    AssertionError: "wake_time: "31/12/99 02:27" is earlier than sleep_time: "31/12/99 15:12"" does not match ""
    AssertionError: "wake_time: "31/12/99 19:05" is earlier than sleep_time: "31/12/99 20:03"" does not match ""

* I copy the message from the terminal then add it to the ValueError_

  .. code-block:: python

    if wake_time < sleep_time:
        raise ValueError("wake_time: "31/12/99 19:05" is earlier than sleep_time: "31/12/99 20:03"")

  and get a SyntaxError_

  .. code-block:: python

    SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

  python does not know where the string ends or begins because the message has double quotes inside double quotes

* I add the error to the list of :doc:`Exceptions</how_to/exception_handling_programs>`

  .. code-block:: python

    # Exceptions Encountered
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError

* then change the outer double quotes to single quotes

  .. code-block:: python

    raise ValueError(
        'wake_time: "31/12/99 19:05"'
        ' is earlier than '
        'sleep_time: "31/12/99 20:03"'
    )

  which gives me another :ref:`AssertionError` for the timestamps in the ValueError_ message not matching

* I :doc:`interpolate</how_to/pass_values>` ``wake_time`` and ``sleep_time`` in the message

  .. code-block:: python

    raise ValueError(
        f'wake_time: "{wake_time}"'
        ' is earlier than '
        f'sleep_time: "{sleep_time}"'
    )

  and the terminal shows passing tests! YES!!

.. _test_duration_tests_refactor:

*********************************************************************************
refactor: make it better
*********************************************************************************

* I return the calculation directly without creating the variables

  .. code-block:: python

    else:
        return str(
            get_datetime(wake_time)
          - get_datetime(sleep_time)
        )

  the terminal shows all tests are still passing
* and I remove the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

*********************************************************************************
review
*********************************************************************************

The challenge was to write a program that passes the tests in ``test_sleep_duration.py`` without looking at them. I wrote something that calculates the difference between a given ``wake_time`` and ``sleep_time`` by following the exceptions encountered in the terminal

* :ref:`AttributeError`
* NameError_
* :ref:`TypeError`
* :ref:`AssertionError`
* SyntaxError_

----

:doc:`/code/code_sleep_duration`
