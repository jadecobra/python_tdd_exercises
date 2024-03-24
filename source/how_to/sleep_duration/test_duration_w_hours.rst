.. include:: ../../links.rst

.. _test_duration_w_hours:

#############################################################################
how to measure sleep duration: test_duration_w_hours
#############################################################################

This is part 1 of 5 where I show an approach to writing a program that calculates the difference between a given sleep and wake time.

.. contents:: table of contents
  :local:
  :depth: 2

----

.. _test_duration_w_hours_red:

*****************************************************************************
red: make it fail
*****************************************************************************

* I open a terminal and run :ref:`makePythonTdd.sh` with ``sleep_duration`` as the project name

  .. code-block:: python

    ./makePythonTdd.sh sleep_duration

  .. NOTE::

    If you are using Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 sleep_duration

  and it shows an :ref:`AssertionError` after making the files I need

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_sleep_duration.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_sleep_duration.py:7`` with the mouse to open it
* then change ``True`` to ``False``
* I change the :doc:`class </classes/classes>` name to title case to match Python convention

  .. code-block:: python

    class TestSleepDuration(unittest.TestCase):

* and replace the test with a new failing test

  .. code-block:: python

    class TestSleepDuration(unittest.TestCase):

        def test_duration_w_hours(self):
            self.assertEqual(

            )

  the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: TestCase.assertEqual() missing 2 required positional arguments: 'first' and 'second'

.. _test_duration_w_hours_green:

*****************************************************************************
green: make it pass
*****************************************************************************

* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError

* then add :ref:`None` as the first and second arguments of the assertion

  .. code-block:: python

    self.assertEqual(
        None,
        None
    )

* I replace the first argument of the assertion with a reference to the ``sleep_duration`` :doc:`module </exceptions/ModuleNotFoundError>`

  .. code-block:: python

    self.assertEqual(
        sleep_duration,
        None
    )

  which gives me a NameError_

  .. code-block:: python

    NameError: name 'sleep_duration' is not defined

* I add it as an exception encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # NameError

* then add an `import statement`_ at the top of the file for the :doc:`module </exceptions/ModuleNotFoundError>`

  .. code-block:: python

    import sleep_duration
    import unittest


    class TestSleepDuration(unittest.TestCase):
    ...

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: <module 'sleep_duration' from '/workspace[46 chars].py'> != None

* I add a reference to something in the ``sleep_duration`` :doc:`module </exceptions/ModuleNotFoundError>`

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration,
        None
    )

  and get an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'sleep_duration' has no attribute 'duration'

* I add the error to the list of exceptions encountered as well

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # NameError
    # AttributeError

* then open ``sleep_duration.py`` in the editor to add the name ::

    duration

  which gives me a NameError_ in the terminal

  .. code-block:: python

    NameError: name 'duration' is not defined

* I define it by assigning it to :ref:`None`

  .. code-block:: python

    duration = None

* then add a call to ``duration`` in the test because I want it to accept inputs

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(),
        None
    )

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I make ``duration`` callable_ by defining it as a :ref:`function<functions>`

  .. code-block:: python

    def duration():
        return None

* I want the ``duration`` :ref:`function<functions>` to take in a ``wake_time`` and add it to the test with a value of ``'08:00'``

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time='08:00'
        ),
        None
    )

  the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'wake_time'

  because the name is not in the signature for ``duration``

* I add it and set its default value to :ref:`None`

  .. code-block:: python

    def duration(wake_time=None):
        return None

* I also want the ``duration`` :ref:`function<functions>` to take in a ``sleep_time`` and set the value to ``'07:00'``

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time='08:00',
            sleep_time='07:00'
        ),
        None
    )

  I get a similar :ref:`TypeError`

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'sleep_time'

  because ``sleep_time`` is not in its signature

* I add it and set its default value to :ref:`None`

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return None

* then set the expectation of the test to the inputs given

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time='08:00',
            sleep_time='07:00'
        ),
        ('08:00', '07:00')
    )

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != ('08:00', '07:00')

* the ``duration`` :ref:`function<functions>` returns :ref:`None`, I make it return the inputs instead

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return ('08:00', '07:00')

  the test passes

.. _test_duration_w_hours_refactor_0:

*****************************************************************************
refactor: make it better
*****************************************************************************

* If I change ``wake_time`` to ``'09:00'``

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time='09:00',
            sleep_time='07:00'
        ),
        ('08:00', '07:00')
    )

  the terminal still shows passing tests, but when I update the expectation to match

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time='09:00',
            sleep_time='07:00'
        ),
        ('09:00', '07:00')
    )

  I get an :ref:`AssertionError`

  .. code-block:: python

    Tuples differ: ('08:00', '07:00') != ('09:00', '07:00')

  because ``duration`` returns ``('08:00', '07:00')`` every time it is called, I change it to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return ('09:00', '07:00')

  and the test passes

* if I change ``sleep_time``

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time='09:00',
            sleep_time='06:00'
        ),
        ('09:00', '07:00')
    )

  the terminal still shows passing tests and when I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time='09:00',
            sleep_time='06:00'
        ),
        ('09:00', '06:00')
    )

  it shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ('09:00', '07:00') != ('09:00', '06:00')

  because ``duration`` returns ``('09:00', '07:00')`` every time it is called, I change it to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return ('09:00', '06:00')

  and the test passes

* I add variables to the test to remove the repetition when I make changes to ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_time = '09:00'
        sleep_time = '06:00'

        self.assertEqual(
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            ),
            (wake_time, sleep_time)
        )

* If change ``wake_time``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_time = '10:00'
        sleep_time = '06:00'

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ('09:00', '06:00') != ('10:00', '06:00')

  I update ``duration`` to match

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return ('10:00', '06:00')

  and the test passes

* when I change ``sleep_time``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_time = '10:00'
        sleep_time = '05:00'

  I get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ('10:00', '06:00') != ('10:00', '05:00')

  I update ``duration`` to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return ('10:00', '05:00')

  and the test passes

* I want to avoid changing the values of ``wake_time`` and ``sleep_time`` in the tests every time I have an idea and then updating the ``duration`` :ref:`function` to match. I make sure the function is tested with random numbers by adding an `import statement`_ for the random_ :doc:`module </exceptions/ModuleNotFoundError>` at the top of the file

  .. code-block:: python

    import random
    import sleep_duration
    import unittest

  then add variables for random hours in a day

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)

        wake_time='10:00'
        sleep_time='06:00'
    ...

  `random.randint`_ will give me a random integer_ from ``0`` up to and including ``23`` to represent the 24 hours in a day

* I :doc:`interpolate </how_to/pass_values>` them as hours for ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)

        wake_time=f'{wake_hour}:00'
        sleep_time=f'{sleep_hour}:00'
    ...

  and the terminal shows an :ref:`AssertionError` that looks like

  .. code-block:: python

    AssertionError: Tuples differ: ('09:00', '06:00') != ('10:00', '2:00')
    AssertionError: Tuples differ: ('09:00', '06:00') != ('23:00', '0:00')
    AssertionError: Tuples differ: ('09:00', '06:00') != ('7:00', '3:00')
    AssertionError: Tuples differ: ('09:00', '06:00') != ('0:00', '22:00')

* ``duration`` still returns ``('10:00', '05:00')`` but the test now uses random timestamps. I update it to return its inputs

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (wake_time, sleep_time)

  and the test passes

* I change the expectation of the test to ``wake_time-sleep_time``

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        wake_time-sleep_time
    )

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

  the timestamps are strings and I cannot subtract one string_ from another

* I change the expectation to go back to what was working

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        wake_time-sleep_time
    )

* I want to get the hours part of ``wake_time`` and ``sleep_time`` which are the first two characters. I add a call to the `help system`_ to get details on the :ref:`methods<functions>` of strings_ to see which ones could help me break a string_ apart or get specific parts from it

  .. code-block:: python

    def test_duration_w_hours(self):
        self.assertEqual(help(str))

  the terminal shows `python documentation for strings`_ and I read the descriptions until I see a :ref:`method<functions>` that looks like it could help

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

* I remove ``self.assertEqual(help(str))``

.. _test_string_splitting:

test_string_splitting
#############################################################################

.. _test_string_splitting_red:

red: make it fail
-----------------------------------------------------------------------------

I add a failing test for the `str.split`_ :ref:`method<functions>` to see what it does

.. code-block:: python

  def test_string_splitting(self):
      self.assertEqual(
          '01:23'.split(),
          None
      )

  def test_duration_w_hours(self):
  ...

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: ['01:23'] != None

`str.split`_ returns a :doc:`list </data_structures/lists/lists>` when called

.. _test_string_splitting_green:

green: make it pass
-----------------------------------------------------------------------------

I copy the :doc:`list </data_structures/lists/lists>` from the terminal and paste it in the test to make it pass

.. code-block:: python

  def test_string_splitting(self):
      self.assertEqual(
          '01:23'.split(),
          ['01:23']
      )

green again

.. _test_string_splitting_refactor:

refactor: make it better
-----------------------------------------------------------------------------

* I want to get the different parts of the timestamp - the hours and minutes, something like ``['01', '23']`` with a ``:`` as the separator

  .. code-block:: python

    def test_string_splitting(self):
        self.assertEqual(
            '01:23'.split(),
            ['01', '23']
        )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['01:23'] != ['01', '23']

* the `documentation <python documentation for strings>`_ showed that `str.split`_ takes in a separator. I want to see what happens when I pass in ``':'`` as the separator

  .. code-block:: python

    def test_string_splitting(self):
        self.assertEqual(
            '01:23'.split(':'),
            ['01', '23']
        )

  the test passes which means I know how to get the different parts of ``wake_time`` and ``sleep_time``

* I add calls to the `str.split`_ :ref:`method<functions>` in ``test_duration_w_hours``

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            wake_time.split(':'),
            sleep_time.split(':')
        )
    )

  and the terminal shows an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: Tuples differ: ('0:00', '10:00') != (['0', '00'], ['10', '00'])
    AssertionError: Tuples differ: ('23:00', '8:00') != (['23', '00'], ['8', '00'])
    AssertionError: Tuples differ: ('6:00', '11:00') != (['6', '00'], ['11', '00'])
    AssertionError: Tuples differ: ('13:00', '13:00') != (['13', '00'], ['13', '00'])

* the ``duration`` :ref:`function<functions>` returns ``wake_time`` and ``sleep_time`` but the test expects the result of splitting them. I change it to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            wake_time.split(':'),
            sleep_time.split(':')
        )

  and the terminal shows green again

* I want the hours part of the timestamp string_ which is the first item of the list from splitting it. I can get it by using its index as covered in :doc:`/data_structures/lists/lists`. Python uses `zero-based indexing`_ which means the first item is at index ``0`` and the second item is at index ``1``. I add a variable to ``test_string_splitting``

  .. code-block:: python

    def test_string_splitting(self):
        split = '01:23'.split(':')

        self.assertEqual(split, ['01', '23'])

  terminal still shows passing tests and I add an assertion for indexing the :doc:`list </data_structures/lists/lists>`

  .. code-block:: python

    self.assertEqual(split, ['01', '23'])
    self.assertEqual(split[0], 0)

  the terminal shows an :ref:`AssertionError` because the first item (index 0) from splitting ``'01:23'`` on the separator ``':'`` is ``'01'`` which is the hours part of the timestamp

  .. code-block:: python

    AssertionError: '01' != 0

* I change the value in the test to ``'01'``

  .. code-block:: python

    self.assertEqual(split[0], '01')

  and the test passes

* I add another assertion for the minutes

  .. code-block:: python

    self.assertEqual(split[0], '01')
    self.assertEqual(split[1], 1)

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '23' != 1

  the second item (index 1) from splitting ``'01:23'`` on the separator ``':'`` is ``'23'`` which is the minutes part of the timestamp

* I change the ``1`` to ``'23'``

  .. code-block:: python

    self.assertEqual(split[1], '23')

  and the test passes

* I update the expectation of ``test_duration_w_hours`` to show the first items of the list from splitting ``wake_time`` and ``sleep_time`` on the separator ``':'``

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            wake_time.split(':')[0],
            sleep_time.split(':')[0]
        )
    )

  and get an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: Tuples differ: (['0', '00'], ['19', '00']) != ('0', '19')
    AssertionError: Tuples differ: (['14', '00'], ['17', '00']) != ('14', '17')
    AssertionError: Tuples differ: (['5', '00'], ['8', '00']) != ('5', '8')
    AssertionError: Tuples differ: (['23', '00'], ['4', '00']) != ('23', '4')

* the ``duration`` :ref:`function<functions>` currently returns the result of splitting the timestamps but the test expects the hours, I change it to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            wake_time.split(':')[0],
            sleep_time.split(':')[0]
        )

  and the test passes

.. _test_converting_strings_to_numbers:

test_converting_strings_to_numbers
#############################################################################

I want to see if I can use the int_ constructor to convert a string_ to an integer_ for the calculation, since I cannot subtract one string_ from another and the hours are still strings_

.. _test_converting_strings_to_numbers_red:

red: make it fail
-----------------------------------------------------------------------------

* I add a new failing test to test hours less than ``10`` than have a ``0`` in front of them

  .. code-block:: python

    def test_converting_strings_to_numbers(self):
        self.assertEqual(int('01'), 0)

    def test_duration_w_hours(self):
    ...

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 1 != 0

.. _test_converting_strings_to_numbers_green:

green: make it pass
-----------------------------------------------------------------------------

* I change the expectation to ``1``

  .. code-block:: python

    self.assertEqual(int('01'), 1)

  and the test passes

.. _test_converting_strings_to_numbers_refactor:

refactor: make it pass
-----------------------------------------------------------------------------

* I add another assertion to test numbers greater than ``9``

  .. code-block:: python

    self.assertEqual(int('23'), 1)

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 23 != 1

* I change the number from ``1`` to ``23``

  .. code-block:: python

    self.assertEqual(int('23'), 23)

  and we are green again

* I add calls to the int_ constructor in the expectation of ``test_duration_w_hours``

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            int(wake_time.split(':')[0]),
            int(sleep_time.split(':')[0])
        )
    )

  and get an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: Tuples differ: ('0', '5') != (0, 5)
    AssertionError: Tuples differ: ('8', '21') != (8, 21)
    AssertionError: Tuples differ: ('4', '4') != (4, 4)
    AssertionError: Tuples differ: ('16', '14') != (16, 14)

* the ``duration`` :ref:`function<functions>` returns the hours as a string_ but the test expects an integer_, I change it to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            int(wake_time.split(':')[0]),
            int(sleep_time.split(':')[0])
        )

  and the test passes, I have successfully gotten the hours part of both timestamps as numbers

* I update the expectation in ``test_duration_w_hours`` to the difference between the hours

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            int(wake_time.split(':')[0])
           -int(sleep_time.split(':')[0])
        )
    )

  and get an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: (7, 23) != -16
    AssertionError: (11, 4) != 7
    AssertionError: (12, 21) != -9
    AssertionError: (14, 2) != 12

  the ``duration`` :ref:`function<functions>` returns the hours from the timestamps and the test expects the difference between them

* when I update the ``duration`` :ref:`function<functions>` to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            int(wake_time.split(':')[0])
          - int(sleep_time.split(':')[0])
        )

  the terminal shows passing tests! Celebration Time!!

* I add a function to get the hours part of a given timestamp since it is the only part that changes in the solution

  .. code-block:: python

    def get_hour(timestamp):
        return int(timestamp.split(':')[0])

  then call it in ``duration``

  .. code-block:: python

    def duration(wake_time=None, sleep_time):
        return (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )

  and the terminal still shows passing tests!

* I can call `random.randint`_ directly in ``test_sleep_duration.py`` instead of using the reference to the variables since they are only used once

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_time = f'{random.randint(0, 23)}:00'
        sleep_time = f'{random.randint(0, 23)}:00'
    ...

  the terminal still shows passing tests

* the assignments for ``wake_time`` and ``sleep_time`` look the same, time to create a function that returns a random timestamp

  .. code-block:: python

    def random_timestamp():
        return f'{random.randint(0, 23)}:00'

  and replace the timestamps with calls to ``random_timestamp``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_time = random_timestamp()
        sleep_time = random_timestamp()
    ...

  all tests are still passing!

----

.. _test_duration_w_hours_review:

*****************************************************************************
review
*****************************************************************************

The challenge is to write a program that calculates the difference between a given sleep and wake time. I ran the following tests to get something that comes close to doing it


* `test_string_splitting`_ where I

  - used the `str.split`_ :ref:`method<functions>` I found from calling the `help system`_ to split a string_ on a separator
  - and indexed the :doc:`list </data_structures/lists/lists>` from the split to get specific items

* `test_converting_strings_to_numbers`_ with the int_ constructor

* `test_duration_w_hours`_ where I

  - used `random.randint`_ to generate random numbers for the 24 hours in a day
  - and :doc:`interpolated </how_to/pass_values>` them into the timestamps
  - then test that the ``duration`` :ref:`function<functions>` subtracts the hour for ``sleep_time`` from the hour for ``wake_time``

I also encountered the following exceptions

* :ref:`AssertionError`
* :ref:`TypeError`
* NameError_
* :ref:`AttributeError`

Would you like to :ref:`test duration with hours and minutes<test_duration_w_hours_and_minutes>`?

----

:doc:`/code/code_sleep_duration`