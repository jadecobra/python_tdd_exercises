.. include:: ../../links.rst

.. _test_duration_w_hours:

#############################################################################
how to measure sleep duration: test_duration_w_hours
#############################################################################

This is part 1 of 5 where the challenge is to create a :ref:`function<functions>` that calculates the difference between 2 given timestamps

----

.. _test_duration_w_hours_red:

*****************************************************************************
red: make it fail
*****************************************************************************

* I open a terminal and run :ref:`createPythonTdd.sh` with ``sleep_duration`` as the project name

  .. code-block:: python

    ./createPythonTdd.sh sleep_duration

  .. NOTE::

    If you are using Windows without `Windows Subsystem Linux`_ use :ref:`createPythonTdd.ps1`

    .. code-block:: python

      ./createPythonTdd.ps1 sleep_duration

  and it shows an :ref:`AssertionError` after making the files I need

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_sleep_duration.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_sleep_duration.py:7`` with the mouse to open it
* change ``True`` to ``False`` to make ``test_failure`` pass
* then replace the test with a new failing test that calls the ``sleep_duration`` :doc:`module </exceptions/ModuleNotFoundError>`

  .. code-block:: python

    def test_duration_w_hours(self):
        self.assertEqual(
            sleep_duration
        )

  and I get a NameError_ in the terminal

  .. code-block:: python

    NameError: name 'sleep_duration' is not defined

.. _test_duration_w_hours_green:

*****************************************************************************
green: make it pass
*****************************************************************************

* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

* then add an `import statement`_ at the top of the file for the :doc:`module </exceptions/ModuleNotFoundError>`

  .. code-block:: python

    import sleep_duration
    import unittest


    class TestSleepDuration(unittest.TestCase):
    ...

  the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: TestCase.assertEqual() missing 1 required positional argument: 'second'

* I add the error to the list of exceptions as well

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # TypeError

* then set the expectation for the test to :ref:`None`

  .. code-block:: python

    def test_duration_w_hours(self):
        self.assertEqual(
            sleep_duration,
            None
        )

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: <module 'sleep_duration' from '/workspace[46 chars].py'> != None

* so I add a reference to something in the ``sleep_duration`` :doc:`module </exceptions/ModuleNotFoundError>`

  .. code-block:: python

    def test_duration_w_hours(self):
        self.assertEqual(
            sleep_duration.duration,
            None
        )

  and get an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'sleep_duration' has no attribute 'duration'

  because there is no definition for it in the file

* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # TypeError
    # AttributeError

* then open ``sleep_duration.py`` to add the name ::

    duration

  and get a NameError_ in the terminal

  .. code-block:: python

    NameError: name 'duration' is not defined

* so I define it by assigning it to :ref:`None`

  .. code-block:: python

    duration = None

  and the test passes

.. _test_duration_w_hours_refactor_0:

*****************************************************************************
refactor: make it better
*****************************************************************************

* I add a call to ``duration`` in the test because I want it to accepts inputs

  .. code-block:: python

    def test_duration_w_hours(self):
        self.assertEqual(
            sleep_duration.duration(),
            None
        )

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* then I make ``duration`` a :ref:`function<functions>` to make it callable_

  .. code-block:: python

    def duration():
        return None

  and the test passes. green again

* I want the ``duration`` :ref:`function<functions>` in the ``sleep_duration`` :doc:`module </exceptions/ModuleNotFoundError>` to take in a ``wake_time`` of ``08:00`` and add it to the test

  .. code-block:: python

    def test_duration_w_hours(self):
        self.assertEqual(
            sleep_duration.duration(
                wake_time='08:00'
            ),
            None
        )

  the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'wake_time'

  because the test calls the ``duration`` :ref:`function<functions>` with ``wake_time`` but the name is not in its signature

* When I add the required keyword argument to the signature and set its default value to :ref:`None`

  .. code-block:: python

    def duration(wake_time=None):
        return None

  the test passes

* I also want the ``duration`` :ref:`function<functions>` to take in a ``sleep_time`` of ``'07:00'``

  .. code-block:: python

    def test_duration_w_hours(self):
        self.assertEqual(
            sleep_duration.duration(
                wake_time='08:00',
                sleep_time='07:00'
            ),
            None
        )

  and get another :ref:`TypeError`

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'sleep_time'

  because the test calls the ``duration`` :ref:`function<functions>` with ``sleep_time`` but the name is not in its signature

* I add the second keyword argument, setting the default value to :ref:`None`

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return None

  and the test passes

* I set the expectation of the test to ``1`` which is the difference between these two timestamps

  .. code-block:: python

    def test_duration_w_hours(self):
        self.assertEqual(
            sleep_duration.duration(
                wake_time='08:00',
                sleep_time='07:00'
            ),
            1
        )

  and get an :ref:`AssertionError` in the terminal

  .. code-block:: python

    AssertionError: None != 1

  the ``duration`` :ref:`function<functions>` returns :ref:`None` but ``test_duration_w_hours`` expects ``1`` as the result

* so I make the return value for ``duration`` match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return 1

  and the test passes, green again

* This :ref:`function<functions>` will always return ``1`` even when I change the values for ``wake_time`` and ``sleep_time`` which would not be correct. I add variables for random integers_ to cover all timestamps from ``'00:00'`` to ``'23:00'`` To avoid writing a series of tests for changing timestamps. First, I add an `import statement`_ for the random_ :doc:`module </exceptions/ModuleNotFoundError>` to ``test_sleep_duration.py``

  .. code-block:: python

    import random
    import sleep_duration
    import unittest

* then add variables for random values as the hours part of the ``wake_time`` and ``sleep_time`` timestamps in the test

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
    ...

  ``random.randint(0, 23)`` will give me a random integer_ from ``0`` up to and including ``23`` to represent the 24 hours in a day

* I :doc:`interpolate </how_to/pass_values>` these random integers_ in the input strings_

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)

        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour:02}:00',
                sleep_time=f'{sleep_hour:02}:00'
            ),
            1
        )

  the ``:02`` in ``{wake_hour:02}`` and ``{sleep_hour:02}`` tells Python to always display two characters for the numbers, with a leading zero when it is one digit. For example, display ``01`` instead of ``1``

* When I make the test expect the difference between ``wake_hour`` and ``sleep_hour``

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time=f'{wake_hour:02}:00',
            sleep_time=f'{sleep_hour:02}:00'
        ),
        wake_hour-sleep_hour
    )

  I get an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: 1 != -2
    AssertionError: 1 != 3
    AssertionError: 1 != -8
    AssertionError: 1 != 4

  the ``duration`` :ref:`function<functions>` returns ``1`` but the test expects the difference between ``sleep_hour`` and ``wake_hour``

* I make the ``duration`` :ref:`function<functions>` return ``wake_time`` minus ``sleep_time``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return wake_time - sleep_time

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

  because Python does not have an operation defined for subtracting one string_ from another. I need a way to convert a timestamp from a string_ to an integer_.

.. _test_string_attributes_and_methods:

test_string_attributes_and_methods
#############################################################################

The ``wake_time`` and ``sleep_time`` are currently in this format - ``XX:00`` where ``XX`` is the hours. I can calculate the difference if I can get the first 2 characters and convert them to numbers since I can do :doc:`arithmetic </how_to/calculator>` with Python

.. _test_string_attributes_and_methods_red:

red: make it fail
-----------------------------------------------------------------------------

* I disable ``test_duration_w_hours`` by adding the `unittest.skip decorator`_

  .. code-block:: python

    @unittest.skip
    def test_duration_w_hours(self):
    ...

* then add ``test_string_attributes_and_methods`` where I use the dir_ :ref:`function<functions>` to see the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of strings_, maybe it will help me find a way to break them apart or get the characters I want

  .. code-block:: python

    def test_string_attributes_and_methods(self):
        self.assertEqual(
            dir('00:00'),
            None
        )

    @unittest.skip
    def test_duration_w_hours(self):
    ...

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: ['__add__', '__class__', '__contains__', [934 chars]ill'] != None

.. _test_string_attributes_and_methods_green:

green: make it pass
-----------------------------------------------------------------------------

* I copy and paste the values on the left side of the comparison to replace :ref:`None` in the test

  .. code-block:: python

    def test_string_attributes_and_methods(self):
        self.assertEqual(
            dir('00:00'),
            ['__add__', '__class__', '__contains__', [934 chars]ill']
        )

  and the terminal shows a SyntaxError_

  .. code-block:: python

    E       ['__add__', '__class__', '__contains__', [934 chars]ill']
    E                                                              ^
    E   SyntaxError: unterminated string literal (detected at line 11)

  which I add to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # TypeError
    # AttributeError
    # SyntaxError

* there is a closing quote without an opening one, so I add it since quotes come in pairs

  .. code-block:: python

    def test_string_attributes_and_methods(self):
        self.assertEqual(
            dir('00:00'),
            ['__add__', '__class__', '__contains__', '[934 chars]ill']
        )

  and the terminal shows an :ref:`AssertionError` with a different message and a suggestion

  .. code-block:: python

    Diff is 1284 characters long. Set self.maxDiff to None to see it.

* I add the suggestion

  .. code-block:: python

    def test_string_attributes_and_methods(self):
        self.maxDiff = None
        self.assertEqual(
            dir('00:00'),
            ['__add__', '__class__', '__contains__', '[934 chars]ill']
        )

  - and the terminal shows the list of :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of a string_, thank you Python
  - `unittest.TestCase.maxDiff`_ sets a limit on the number of characters the terminal shows for a difference between two objects. There is no limit when it is set to :ref:`None`

* I copy and paste the values from the terminal into the test, and remove the extra characters - ``'E       -  '`` using find and replace

  .. NOTE::

    Some attributes may be missing because of your Python version

  .. code-block:: python

    def test_string_attributes_and_methods(self):
        self.maxDiff = None
        self.assertEqual(
            dir('00:00'),
            [
                '__add__',
                '__class__',
                '__contains__',
                '__delattr__',
                '__dir__',
                '__doc__',
                '__eq__',
                '__format__',
                '__ge__',
                '__getattribute__',
                '__getitem__',
                '__getnewargs__',
                '__getstate__',
                '__gt__',
                '__hash__',
                '__init__',
                '__init_subclass__',
                '__iter__',
                '__le__',
                '__len__',
                '__lt__',
                '__mod__',
                '__mul__',
                '__ne__',
                '__new__',
                '__reduce__',
                '__reduce_ex__',
                '__repr__',
                '__rmod__',
                '__rmul__',
                '__setattr__',
                '__sizeof__',
                '__str__',
                '__subclasshook__',
                'capitalize',
                'casefold',
                'center',
                'count',
                'encode',
                'endswith',
                'expandtabs',
                'find',
                'format',
                'format_map',
                'index',
                'isalnum',
                'isalpha',
                'isascii',
                'isdecimal',
                'isdigit',
                'isidentifier',
                'islower',
                'isnumeric',
                'isprintable',
                'isspace',
                'istitle',
                'isupper',
                'join',
                'ljust',
                'lower',
                'lstrip',
                'maketrans',
                'partition',
                'removeprefix',
                'removesuffix',
                'replace',
                'rfind',
                'rindex',
                'rjust',
                'rpartition',
                'rsplit',
                'rstrip',
                'split',
                'splitlines',
                'startswith',
                'strip',
                'swapcase',
                'title',
                'translate',
                'upper',
                'zfill'
            ]
        )

  and the test passes
* I want to try one of the :ref:`methods<functions>` listed in ``test_string_attributes_and_methods`` to see if it will get me closer to a solution, but I cannot tell what they do by the names alone. I need more details so I use the `help system`_ to show me the `python documentation for strings`_

  .. code-block:: python

    def test_string_attributes_and_methods(self):
        ...
        self.assertEqual(help(str))

  the terminal shows documentation for the string_ :doc:`module </exceptions/ModuleNotFoundError>` and I read the descriptions for each :ref:`method<functions>` until I see one that looks like it could solve the problem

  .. code-block:: python

    ...
    |
    |  split(self, /, sep=None, maxsplit=-1)
    |      Return a list of the substrings in the string,
    |      using sep as the separator string.
    |
    |        sep
    |          The separator used to split the string.
    |
    ...

  the `str.split`_ :ref:`method<functions>` looks like a good solution since it splits up a word on a given separator

test_string_splitting
#############################################################################

.. _test_string_splitting_red_0:

red: make it fail
-----------------------------------------------------------------------------

I remove ``self.assertEqual(help(str))``, add a failing test for the `str.split`_ :ref:`method<functions>` to see what it does

.. code-block:: python

  def test_string_splitting(self):
      self.assertEqual(
          '01:23'.split(),
          None
      )

  @unittest.skip
  def test_duration_w_hours(self):
  ...

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: ['01:23'] != None

`str.split`_ returns a :doc:`list </data_structures/lists/lists>` when called

.. _test_string_splitting_green_0:

green: make it pass
-----------------------------------------------------------------------------

I copy the :doc:`list </data_structures/lists/lists>` in the terminal and paste it in the test to make it pass

.. code-block:: python

  def test_string_splitting(self):
      self.assertEqual(
          '01:23'.split(),
          ['01:23']
      )

and we are green again

.. _test_string_splitting_refactor:

refactor: make it better
-----------------------------------------------------------------------------

* I want to get the different parts of the timestamp, the hours and minutes, something like ``['01', '23']`` with a ``:`` as the separator


  .. code-block:: python

    def test_string_splitting(self):
        self.assertEqual(
            '01:23'.split(),
            ['01', '23']
        )

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['01:23'] != ['01', '23']

* and the `documentation <python documentation for strings>`_ said `str.split`_ takes in ``sep=None, maxsplit=-1`` as inputs and ``sep`` is the separator. When I pass in ``':'`` as the separator

  .. code-block:: python

    def test_string_splitting(self):
        self.assertEqual(
            '01:23'.split(':'),
            ['01', '23']
        )

  the test passes. I now know how to get the different parts of ``wake_time`` and ``sleep_time``

* I comment out the `unittest.skip decorator`_ from ``test_duration_w_hours``

  .. code-block:: python

    # @unittest.skip
    def test_duration_w_hours(self):
    ...

* and then add calls to the `str.split`_ :ref:`method<functions>` in the ``duration`` :ref:`function<functions>` in ``sleep_duration.py``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            wake_time.split(':')
          - sleep_time.split(':')
        )

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'list' and 'list'

  this time for trying to subtract one :doc:`list </data_structures/lists/lists>` from another

.. _test_string_splitting_red_1:

red: make it fail
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* I want to get the first item of the list created from splitting the timestamp string_, which I can get by using its index. Python uses `zero-based indexing`_ which means the first item is at index ``0`` and the second item is at index ``1``. See :doc:`/data_structures/lists/lists` for more. I add tests to ``test_string_splitting`` for getting specific parts of a :doc:`list </data_structures/lists/lists>` created from calling `str.split`_

  .. code-block:: python

    def test_string_splitting(self):
        self.assertEqual(
            '01:23'.split(':'),
            ['01', '23']
        )

        split = '12:34'.split(':')
        self.assertEqual(split[0], 0)

    def test_duration_w_hours(self):
    ...

  the terminal shows an :ref:`AssertionError` because the first item (index 0) from splitting ``'12:34'`` on the separator ``':'`` is ``'12'`` which is the hours part of the timestamp

  .. code-block:: python

    AssertionError: '12' != 0

.. test_string_splitting_green_1:

green: make it pass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* I change the value in the test to ``12``

  .. code-block:: python

    self.assertEqual(split[0], '12')

  and the test passes

* I add another test for getting the second item from the list

  .. code-block:: python

    self.assertEqual(split[0], '12')
    self.assertEqual(split[1], 1)

  and the terminal an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '34' != 1

  showing that the second item (index 1) from splitting ``'12:34'`` on the separator ``':'`` is ``'34'`` which is the minutes part of the timestamp

* I change that to ``34``

  .. code-block:: python

    self.assertEqual(split[1], '34')

  and the test passes, bringing me back to the unsolved :ref:`TypeError` for the ``test_duration_w_hours``

* I make the ``duration`` :ref:`function<functions>` return the result of subtracting the first items of the list from splitting ``wake_time`` and ``sleep_time`` on the separator ``':'``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            wake_time.split(':')[0]
          - sleep_time.split(':')[0]
        )

  and get a :ref:`TypeError` for an unsupported operation of trying to subtract one string_ from another. I know from ``test_string_splitting`` that the strings being subtracted are the values to the left of the separator ``':'``, not the entire values of ``wake_time`` and ``sleep_time``.

  For example, if the given ``wake_time`` is ``'02:00'`` and the given ``sleep_time`` is ``'01:00'``, the ``duration`` :ref:`function<functions>` tries to subtract ``'01'`` from ``'02'`` which is different than trying to subtract ``1`` from ``2`` - ``'01'`` is a string_ and ``1`` is an integer_

test_converting_strings_to_integers
#############################################################################

I want to see if I can use the int_ constructor to convert a string_ to an integer_

.. _test_converting_strings_to_integers_red:

red: make it fail
-----------------------------------------------------------------------------

I uncomment the `unittest.skip decorator`_ to disable the current failing test

.. code-block:: python

  @unittest.skip
  def test_duration_w_hours(self):
  ...

then add a new failing test called ``test_converting_strings_to_integers``

.. code-block:: python

  def test_converting_strings_to_integers(self):
      self.assertEqual(int('01'), 0)

  @unittest.skip
  def test_duration_w_hours(self):
  ...

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 1 != 0

.. _test_converting_strings_to_integers_green:

green: make it pass
-----------------------------------------------------------------------------

* so I change the expectation to ``1``

  .. code-block:: python

    self.assertEqual(int('01'), 1)

  and the test passes

* I add another line to test numbers greater than ``9``

  .. code-block:: python

    self.assertEqual(int('12'), 1)

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 12 != 1

* so I change the number from ``1`` to ``12``

  .. code-block:: python

    self.assertEqual(int('12'), 12)

  and we are green again

----

.. _test_duration_w_hours_refactor_1:

* I remove the `unittest.skip decorator`_ from ``test_duration_w_hours`` to show the :ref:`TypeError` I have been trying to solve
* and add the conversion of a string_ to an integer_ using the int_ constructor to the ``duration`` :ref:`function<functions>` to see if it will make the test pass

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            int(wake_time.split(':')[0])
          - int(sleep_time.split(':')[0])
        )

  and it does, the terminal shows passing tests! Celebration Time

* Since all the tests are passing I can rewrite the solution as a series of steps for someone who does not know how to use `str.split`_, index a :doc:`list </data_structures/lists/lists>` or use the int_ constructor

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time_split = wake_time.split(':')
        wake_hour = wake_time_split[0]
        wake_hour_integer = int(wake_hour)

        return (
            wake_hour_integer
          - int(sleep_time.split(':')[0])
        )

* we are still green so I can try the same thing for ``sleep_time``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        ...

        sleep_time_split = sleep_time.split(':')
        sleep_hour = sleep_time_split[0]
        sleep_hour_integer = int(sleep_hour)

        return (
            wake_hour_integer
          - sleep_hour_integer
        )

  and the terminal still shows passing tests

* I can make these steps a separate :ref:`function<functions>` that is called for ``wake_time`` and ``sleep_time`` to remove the repetition since the only thing that is different are the timestamps

  .. code-block:: python

    def process(timestamp):
        split = timestamp.split(':')
        hour = split[0]
        hour_integer = int(hour)
        return hour_integer

    def duration(wake_time=None, sleep_time=None):
        wake_time_split = wake_time.split(':')
        wake_hour = wake_time_split[0]
        wake_hour_integer = int(wake_hour)

        sleep_time_split = sleep_time.split(':')
        sleep_hour = sleep_time_split[0]
        sleep_hour_integer = int(sleep_hour)

        return (
            process(wake_time)
          - process(sleep_time)
        )

  we are still green

* so I remove the parts of ``duration`` that are no longer used and rename ``process`` to something more descriptive like ``get_hour``

  .. code-block:: python

    def get_hour(timestamp):
        split = timestamp.split(':')
        hour = split[0]
        hour_integer = int(hour)
        return hour_integer

    def duration(wake_time=None, sleep_time=None):
        return (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )

  the terminal still shows passing tests

* which means I can play around and do things like make ``get_hour`` use the same variable name instead of a new one for each step of the process

  .. code-block:: python

    def get_hour(value):
        value = value.split(':')
        value = value[0]
        value = int(value)
        return value

  or change it to use one line, though it might not be as easy to understand

  .. code-block:: python

    def get_hour(timestamp):
        return int(timestamp.split(':')[0])

* I can also make a :ref:`function<functions>` that makes random hours in ``test_sleep_duration.py``

  .. code-block:: python

    import random
    import sleep_duration
    import unittest

    def random_hour():
        return random.randint(0, 23)


    class TestSleepDuration(unittest.TestCase):
    ...

  and then call it in ``test_duration_w_hours``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random_hour()
        sleep_hour = random_hour()

        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour:02}:00',
                sleep_time=f'{sleep_hour:02}:00'
            ),
            wake_hour-sleep_hour
        )

  the terminal still shows passing tests

----

.. _test_duration_w_hours_review:

*****************************************************************************
review
*****************************************************************************

The challenge is to create a :ref:`function<functions>` that calculates the difference between 2 given timestamps. I ran the following tests so far to make something that comes close to doing it

* `test_string_attributes_and_methods`_ where

  - I used the dir_ :ref:`function<functions>`
  - used the `help system`_ to view the `python documentation for strings`_

* `test_string_splitting`_ where I

  - used the `str.split`_ :ref:`method<functions>` to split a string_ on a separator
  - indexed the :doc:`list </data_structures/lists/lists>` from the split to get specific items

* `test_converting_strings_to_integers`_
* `test_duration_w_hours`_ where I

  - used `random.randint`_ to generate random integers for hours
  - used :doc:`interpolation </how_to/pass_values>` to test the functions with random hours

I also encountered the following exceptions

* :ref:`AssertionError`
* NameError_
* :ref:`TypeError`
* :ref:`AttributeError`
* SyntaxError_

Would you like to :ref:`test duration with hours and minutes<test_duration_w_hours_and_minutes>`?

----

:doc:`/code/code_sleep_duration`