.. meta::
  :description: Learn to pass Python sleep duration tests with TDD! Master datetime string parsing, handle various exceptions, and refine your time difference calculations.
  :keywords: Jacob Itegboje, Python sleep duration tests, TDD exception handling Python, Python datetime strptime, time difference calculation, Python error resolution, Python unit testing time, sleep duration TDD Python

.. include:: ../../links.rst


#################################################################################
how to measure sleep duration: test_duration_tests
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/jydasRSwIyE?si=yintYMCxtO7VZSZd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

This is part 5 of a program that calculates the difference between a given wake and sleep time.

.. contents:: table of contents
  :local:
  :depth: 2

----

I want to write a program that makes the tests in ``test_sleep_duration.py`` pass without looking at them

*********************************************************************************
red: make it fail
*********************************************************************************

* I close ``test_sleep_duration.py``
* then delete all the text in ``sleep_duration.py`` and the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.sleep_duration' has no attribute 'get_datetime'

*********************************************************************************
green: make it pass
*********************************************************************************

* I add a list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AttributeError

* and the missing name to ``sleep_duration.py``

  .. code-block:: python

    get_datetime

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'get_datetime' is not defined

  I add it to the list of Exceptions_ encountered as well

  .. code-block:: python

    # Exceptions Encountered
    # AttributeError
    # NameError

* and point ``get_datetime`` to :ref:`None`

  .. code-block:: python

    get_datetime = None

  which gives me :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  another error for the list of Exceptions_ encountered

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

  then I add a name to the :ref:`function's<functions>` signature

  .. code-block:: python

    def get_datetime(argument):

  and get :ref:`AssertionError`

  .. code-block:: python

    None != datetime.datetime(2006, 11, 21, 7, 1)
    None != datetime.datetime(2006, 11, 21, 10, 59)
    None != datetime.datetime(2006, 11, 21, 13, 28)
    None != datetime.datetime(2006, 11, 21, 19, 8)

  which I add to the list of Exceptions_ encountered

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

  and the terminal shows NameError_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

* I add an `import statement`_ for the datetime_ :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

      import datetime


      def get_datetime(argument):
      ...

  and get :ref:`AssertionError`

  .. code-block:: python

    AssertionError: datetime.datetime(2006, 11, 21, 19, 8) != datetime.datetime(2006, 11, 21, 0, 15)

  the expected values of the test changed

* I change the `return statement`_ to see the difference between the input and expected output

  .. code-block:: python

    def get_datetime(argument):
        return argument

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '2006/11/21 02:58' != datetime.datetime(2006, 11, 21, 2, 58)
    AssertionError: '2006/11/21 03:14' != datetime.datetime(2006, 11, 21, 3, 14)
    AssertionError: '2006/11/21 08:30' != datetime.datetime(2006, 11, 21, 8, 30)
    AssertionError: '2006/11/21 23:41' != datetime.datetime(2006, 11, 21, 23, 41)

  I need a way to change a string_ that has a date and time to a `datetime.datetime`_ object

* I use the `datetime.datetime.strptime`_ :ref:`method<functions>` to make it happen

  .. code-block:: python

    def get_datetime(argument):
        return datetime.datetime.strptime(
            argument, '%Y/%m/%d %H:%M'
        )

  and get :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.sleep_duration' has no attribute 'duration'

* I add the name below ``get_datetime``

  .. code-block::python

  .. code-block:: python

    duration

  and get NameError_

  .. code-block:: python

    NameError: name 'duration' is not defined

  I have done this dance before

* I point it to :ref:`None` to define it

  .. code-block:: python

    duration = None

  which gives me :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* then change it to a :ref:`function<functions>` to make it callable_

  .. code-block:: python

    def duration():
        return None

  and the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'sleep_time'

  I add the name to the :ref:`function's<functions>` signature

  .. code-block:: python

    def duration(sleep_time):

  and get :ref:`TypeError` for another keyword argument

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'wake_time'

  which I add to the signature

  .. code-block:: python

    def duration(sleep_time, wake_time):

  the terminal shows this :ref:`AssertionError`

  .. code-block:: python

    AssertionError: ValueError not raised

  or

  .. code-block:: python

    AssertionError: None != '2944049 days, 15:58:00'
    AssertionError: None != '130331 days, 11:57:00'
    AssertionError: None != '1829637 days, 5:10:00'
    AssertionError: None != '2846203 days, 15:15:00'

  it looks like the ``duration`` :ref:`function<functions>` has to make a decision based on its inputs

* I change the `return statement`_ to raise ValueError_ with the inputs or return the inputs to see the difference between them and the expected output

  .. code-block:: python

    def duration(sleep_time, wake_time):
        raise ValueError(sleep_time, wake_time)

* When I raise ValueError_ in ``duration`` I get another :ref:`AssertionError` because the message in the ValueError_ does not match the expectation of the test

  .. code-block:: python

    AssertionError: "wake_time: "3133/04/18 05:11" is earlier than sleep_time: "6999/09/22 05:07"" does not match "('6999/09/22 05:07', '3133/04/18 05:11')"
    AssertionError: "wake_time: "5856/04/20 15:58" is earlier than sleep_time: "7186/01/12 06:39"" does not match "('7186/01/12 06:39', '5856/04/20 15:58')"
    AssertionError: "wake_time: "5602/08/29 05:06" is earlier than sleep_time: "8373/05/08 05:29"" does not match "('8373/05/08 05:29', '5602/08/29 05:06')"
    AssertionError: "wake_time: "7413/05/24 15:04" is earlier than sleep_time: "8720/08/18 01:02"" does not match ""

  this tells me that the test expects a message with the ValueError_, or I get ValueError_ that looks like this

  .. code-block:: python

    ValueError: ('0887/08/27 17:21', '5668/08/15 20:16')
    ValueError: ('2880/08/20 10:10', '9134/08/22 20:28')
    ValueError: ('6471/03/10 05:04', '7883/06/01 02:38')
    ValueError: ('7370/08/12 21:34', '7937/03/27 01:58')

  which does not tell me anything so I comment it out to get the other message I got with the :ref:`AssertionError`, I can raise ValueError_ again or try to return the inputs

* When I get the error with the message about ``wake_time`` being earlier than ``sleep_time``, I copy it from the terminal to change the message of the ValueError_

  .. code-block:: python

    def duration(wake_time, sleep_time):
        raise ValueError(
            "wake_time: "7413/05/24 15:04" is earlier than sleep_time: "8720/08/18 01:02"" does not match ""
        )

  and get a SyntaxError_ with this message

  .. code-block:: python
    :force:

    SyntaxError: invalid syntax. Perhaps you forgot a comma?

  or this message

  .. code-block:: python

    SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

  Python_ does not know where the string ends or begins because the message has double quotes inside double quotes. I add the error to the list of Exceptions_

  .. code-block:: python

    # Exceptions Encountered
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError

  then change the outer double quotes to single quotes

  .. code-block:: python

    def duration(wake_time, sleep_time):
        raise ValueError(
            'wake_time: "7413/05/24 15:04"'
            ' is earlier than '
            'sleep_time: "8720/08/18 01:02"'
        )

  and get another :ref:`AssertionError` because the timestamps in the ValueError_ message are not the same

  .. code-block:: python

    AssertionError: "wake_time: "1184/07/11 12:07" is earlier than sleep_time: "3059/12/16 04:30"" does not match "wake_time: "0615/04/17 08:51" is earlier than sleep_time: "6631/03/18 20:25""
    AssertionError: "wake_time: "2476/05/07 19:46" is earlier than sleep_time: "9204/03/10 20:53"" does not match "wake_time: "0615/04/17 08:51" is earlier than sleep_time: "6631/03/18 20:25""
    AssertionError: "wake_time: "3208/04/09 09:10" is earlier than sleep_time: "3957/12/23 22:44"" does not match "wake_time: "0615/04/17 08:51" is earlier than sleep_time: "6631/03/18 20:25""
    AssertionError: "wake_time: "7169/09/04 15:18" is earlier than sleep_time: "9367/03/02 03:17"" does not match "wake_time: "0615/04/17 08:51" is earlier than sleep_time: "6631/03/18 20:25""

  or ValueError_

  .. code-block:: python

    ValueError: wake_time: "7413/05/24 15:04" is earlier than sleep_time: "8720/08/18 01:02"

  which tells me nothing, so I return ``sleep_time`` and ``wake_time``

  .. code-block:: python

    def duration(sleep_time, wake_time):
        return (sleep_time, wake_time)
        # raise ValueError(
        #    'wake_time: "7413/05/24 15:04"'
        #    ' is earlier than '
        #    'sleep_time: "8720/08/18 01:02"'
        # )

  and get the :ref:`AssertionError` I got before. I keep switching between the `return statement`_ and ``raise ValueError`` until I get the :ref:`AssertionError` that the ValueError_ messages do not match

* I :doc:`interpolate</how_to/pass_values>` ``wake_time`` and ``sleep_time`` in the message

  .. code-block:: python

    def duration(wake_time, sleep_time):
        # return (sleep_time, wake_time)
        raise ValueError(
            f'wake_time: "{wake_time}"'
            ' is earlier than '
            f'sleep_time: "{sleep_time}"'
        )

  and get ValueError_

  .. code-block:: python

    ValueError: wake_time: "9251/06/04 01:20" is earlier than sleep_time: "1034/03/24 22:35"
    ValueError: wake_time: "2669/08/09 17:30" is earlier than sleep_time: "2520/01/27 06:40"
    ValueError: wake_time: "3201/08/13 15:20" is earlier than sleep_time: "1074/03/31 16:44"
    ValueError: wake_time: "9810/07/30 04:29" is earlier than sleep_time: "9792/03/04 12:44"

  this is not right, the timestamps for ``wake_time`` are not earlier than ``sleep_time``. The ``duration`` :ref:`function<functions>` needs a condition to make sure it raises ValueError_ only when ``wake_time`` is earlier than ``sleep_time``. I add the error to the list of Exceptions_ encountered

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
        return (sleep_time, wake_time)

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: ('0435/03/20 02:03', '0711/05/03 10:35') != '100850 days, 8:32:00'
    AssertionError: ('2544/12/29 13:05', '4351/03/05 09:47') != '659692 days, 20:42:00'
    AssertionError: ('1583/06/02 07:48', '3962/03/06 17:07') != '868824 days, 9:19:00'
    AssertionError: ('1820/06/12 16:07', '8786/05/18 04:27') != '2544253 days, 12:20:00'

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

  and get :ref:`TypeError`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

  I still cannot subtract one string from another

* I change the `return statement`_ back, then add calls to ``get_datetime`` because I can do arithmetic_ with `datetime.datetime`_ objects

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

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: datetime.timedelta(days=-43256, seconds=82860) != '43255 days, 0:59:00'
    AssertionError: datetime.timedelta(days=-28643, seconds=68100) != '28642 days, 5:05:00'
    AssertionError: datetime.timedelta(days=-744003, seconds=22500) != '744002 days, 17:45:00'
    AssertionError: datetime.timedelta(days=-1226280, seconds=76800) != '1226279 days, 2:40:00'

  the test expects a string_ and the :ref:`function<functions>` returns a `datetime.timedelta`_ object. The values for days are also negative and the test expects positive numbers for the days, I did something wrong

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

    AssertionError: '-2681410 days, 19:19:00' != '2681409 days, 4:41:00'
    AssertionError: '-1492190 days, 13:23:00' != '1492189 days, 10:37:00'
    AssertionError: '-398812 days, 16:44:00' != '398811 days, 7:16:00'
    AssertionError: '-1209690 days, 0:49:00' != '1209689 days, 23:11:00'

  the ``duration`` :ref:`function<functions>` returns negative timestamps but the test expects positive timestamps, and the negative days all look like they are one number less than the expectation

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

* then I remove the list of Exceptions_ encountered because it was just for me

*********************************************************************************
review
*********************************************************************************

The challenge was to write a program that makes the tests in ``test_sleep_duration.py`` pass without looking at them. I wrote something that returns the difference between a given ``wake_time`` and ``sleep_time`` by following these Exceptions_ from the terminal

* :ref:`AttributeError`
* NameError_
* :ref:`TypeError`
* :ref:`AssertionError`
* SyntaxError_
* ValueError_

----

:doc:`/code/code_sleep_duration`
