.. meta::
  :description: Learn to calculate sleep duration in hours using Python's Test-Driven Development. Master converting string inputs to numbers and handle common coding errors efficiently.
  :keywords: Jacob Itegboje, Python sleep duration calculation, TDD time difference Python, Python string to int conversion, measure sleep hours, Python time calculation, Python error handling TDD, sleep time difference Python

.. include:: ../../links.rst


#################################################################################
how to measure sleep duration: test_duration_w_hours
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/RJf2ZHfXF7Q?si=Pk_FS6juvRv03NvK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

This is part 1 of a program_ that calculates the difference between a given wake and sleep time.

----

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``sleep_duration`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh sleep_duration

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: python

      ./makePythonTdd.ps1 sleep_duration

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_sleep_duration.py:7: AssertionError

* I hold ``ctrl`` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_sleep_duration.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format to follow Python_ :ref:`convention<conventions>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestSleepDuration(unittest.TestCase):

*********************************************************************************
RED: make it fail
*********************************************************************************

* I change the test to a new failing test

  .. code-block:: python
    :linenos:

    import unittest


    class TestSleepDuration(unittest.TestCase):

        def test_duration_w_hours(self):
            self.assertEqual(

            )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: TestCase.assertEqual() missing 2 required positional arguments: 'first' and 'second'

  which I add to the list of :ref:`Exceptions<errors>` encountered in ``test_sleep_duration.py``

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError

*********************************************************************************
GREEN: make it pass
*********************************************************************************

* I add :ref:`None` as the first and second arguments of the :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(
        None,
        None
    )

* then change the first argument to the ``sleep_duration`` :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration,
        None
    )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'src' is not defined

  I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_sleep_duration.py``

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # NameError

  then add an `import statement`_ at the top of the file for the :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

    import src.sleep_duration
    import unittest


    class TestSleepDuration(unittest.TestCase):
    ...

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: <module 'src.sleep_duration' from '/workspace[46 chars].py'> != None

* I use something in the ``sleep_duration`` :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration,
        None
    )

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.sleep_duration' has no attribute 'duration'

  I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_sleep_duration.py``

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # NameError
    # AttributeError

  then open ``sleep_duration.py`` in the :ref:`editor<2 editors>` to add the name ::

    duration

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'duration' is not defined

  I point it to :ref:`None` to define it

  .. code-block:: python

    duration = None

* then add a call to ``duration`` in the test

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration(),
        None
    )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  I make it callable_ by changing it to a :ref:`function<functions>`

  .. code-block:: python

    def duration():
        return None

* I want the ``duration`` :ref:`function<functions>` to take in a ``wake_time`` then add it to the test

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration(
            wake_time='08:00'
        ),
        None
    )

  then get :ref:`TypeError`

  .. code-block:: shell

    TypeError: duration() got an unexpected keyword argument 'wake_time'

  because the name is not in the :ref:`function's<functions>` definition. I add it with a default value of :ref:`None`

  .. code-block:: python

    def duration(wake_time=None):
        return None

* I also want the ``duration`` :ref:`function<functions>` to take in a ``sleep_time``

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration(
            wake_time='08:00',
            sleep_time='07:00'
        ),
        None
    )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: duration() got an unexpected keyword argument 'sleep_time'

  because ``sleep_time`` is not in the :ref:`function's<functions>` definition. I add it with a default value of :ref:`None`

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return None

* then set the expectation of the test to the given inputs

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration(
            wake_time='08:00',
            sleep_time='07:00'
        ),
        ('08:00', '07:00')
    )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != ('08:00', '07:00')

  the ``duration`` :ref:`function<functions>` returns :ref:`None`, I change it to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return ('08:00', '07:00')

  the test passes


*********************************************************************************
REFACTOR: make it better
*********************************************************************************

* I add :ref:`variables<test_attribute_error_w_variables>` to remove the repetition of the values for ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_time = '08:00'
        sleep_time = '07:00'

        self.assertEqual(
            src.sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            ),
            (wake_time, sleep_time)
        )

* then change ``wake_time``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_time = '09:00'
        sleep_time = '07:00'

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ('08:00', '07:00') != ('09:00', '07:00')

  I change ``duration`` to match

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return ('09:00', '07:00')

  the test passes

* I change ``sleep_time``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_time = '09:00'
        sleep_time = '06:00'

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ('09:00', '07:00') != ('09:00', '06:00')

  then change ``duration`` to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return ('09:00', '06:00')

  the test passes

* I do not want to change the values of ``wake_time`` and ``sleep_time`` in the tests every time I have an ideand then change the ``duration`` :ref:`function<functions>` to match. It would be better to test the :ref:`function<functions>` with random numbers. I add an `import statement`_ for the random_ :ref:`module<ModuleNotFoundError>`  at the top of ``test_sleep_duration.py``

  .. code-block:: python

    import random
    import src.sleep_duration
    import unittest

  then add :ref:`variables<test_attribute_error_w_variables>` for random hours in a day

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)

        wake_time='09:00'
        sleep_time='06:00'
    ...

  `random.randint`_ gives me a random number from ``0`` up to and including ``23`` for the 24 hours in a day

* I :ref:`interpolate<how to pass values>` them as hours for ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)

        wake_time=f'{wake_hour:02}:00'
        sleep_time=f'{sleep_hour:02}:00'
    ...

  the ``:02`` tells Python_ to always show the numbers as 2 digits, if it is less than ``10`` it shows have a ``0`` in front of it, for example ``01``. The terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ('09:00', '06:00') != ('10:00', '02:00')
    AssertionError: Tuples differ: ('09:00', '06:00') != ('23:00', '00:00')
    AssertionError: Tuples differ: ('09:00', '06:00') != ('07:00', '03:00')
    AssertionError: Tuples differ: ('09:00', '06:00') != ('00:00', '22:00')

  ``duration`` still returns ``('09:00', '06:00')`` but the test now uses random timestamps. I change it to return its inputs

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (wake_time, sleep_time)

  the test passes

* I change the expectation of the test to ``wake_time-sleep_time``

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (wake_time-sleep_time)
    )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

  the timestamps are strings and I cannot subtract one string_ from another. I undo the change to go back to what was working

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (wake_time, sleep_time)
    )

* I want to get the hours part of ``wake_time`` and ``sleep_time`` which are the characters before ``:``. I add a call to the `help system`_ to see which :ref:`methods<functions>` of strings_ can help me break one apart or get specific parts from it

  .. code-block:: python

    def test_duration_w_hours(self):
        self.assertEqual(help(str))
    ...

  the terminal_ shows `Python documentation for strings`_ and I read the descriptions until I see a :ref:`method<functions>` that looks like what I am looking for

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

* I remove ``self.assertEqual(help(str))``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
    ...


test_string_splitting
#################################################################################

RED: make it fail
---------------------------------------------------------------------------------

I add a failing test for the `str.split`_ :ref:`method<functions>` to see what it does

.. code-block:: python

  def test_string_splitting(self):
      self.assertEqual(
          '01:23'.split(), None
      )

  def test_duration_w_hours(self):
  ...

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: ['01:23'] != None

`str.split`_ returns a :ref:`list <lists>` when called

GREEN: make it pass
---------------------------------------------------------------------------------

I copy the :ref:`list <lists>` from the terminal_ and paste it in the test to make it pass

.. code-block:: python

  self.assertEqual(
      '01:23'.split(), ['01:23']
  )

the test passes

REFACTOR: make it better
---------------------------------------------------------------------------------

* I change the expectation to the hours and minutes as different items

  .. code-block:: python

    self.assertEqual(
        '01:23'.split(), ['01', '23']
    )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['01:23'] != ['01', '23']

  the `documentation <Python documentation for strings>`_ showed that `str.split`_ takes in a separator. I want to see what happens when I pass in ``':'`` as the separator

  .. code-block:: python

    self.assertEqual(
        '01:23'.split(':'), ['01', '23']
    )

  the test passes which means I know how to get the different parts of ``wake_time`` and ``sleep_time``

* I add calls to the `str.split`_ :ref:`method<functions>` in ``test_duration_w_hours``

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            wake_time.split(':'),
            sleep_time.split(':')
        )
    )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ('00:00', '10:00') != (['00', '00'], ['10', '00'])
    AssertionError: Tuples differ: ('23:00', '08:00') != (['23', '00'], ['08', '00'])
    AssertionError: Tuples differ: ('06:00', '11:00') != (['06', '00'], ['11', '00'])
    AssertionError: Tuples differ: ('13:00', '13:00') != (['13', '00'], ['13', '00'])

  the ``duration`` :ref:`function<functions>` returns ``wake_time`` and ``sleep_time`` but the test expects the result of splitting them. I change it to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            wake_time.split(':'),
            sleep_time.split(':')
        )

  the terminal_ shows green again

* I want the hours part of the timestamp string_ which is the first item from calling `str.split`_. From :ref:`the chapter on lists<test_index_returns_first_position_of_item_in_a_list>` I know I can get it by using its index, Python_ uses `zero-based indexing`_ which means the first item has an index of ``0`` and the second an index of ``1``. I add a :ref:`variable<test_attribute_error_w_variables>` to ``test_string_splitting``

  .. code-block:: python

    def test_string_splitting(self):
        split = '01:23'.split(':')

        self.assertEqual(split, ['01', '23'])

  the terminal_ still shows passing tests. I add an :ref:`assertion<AssertionError>` for indexing the :ref:`list <lists>`

  .. code-block:: python

    self.assertEqual(split, ['01', '23'])
    self.assertEqual(split[0], 0)

  the terminal_ shows :ref:`AssertionError` because the first item (index 0) from splitting ``'01:23'`` on the separator ``':'`` is ``'01'``, the hours part of the timestamp

  .. code-block:: shell

    AssertionError: '01' != 0

  I change the value in the test to ``'01'``

  .. code-block:: python

    self.assertEqual(split[0], '01')

  and it passes

* I add another :ref:`assertion<AssertionError>` for the minutes

  .. code-block:: python

    self.assertEqual(split[0], '01')
    self.assertEqual(split[1], '01')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '23' != '01'

  the second item (index 1) from splitting ``'01:23'`` on the separator ``':'`` is ``'23'``, the minutes part of the timestamp. I change the ``'01'`` to ``'23'``

  .. code-block:: python

    self.assertEqual(split[1], '23')

  the test passes

* I change the expectation of ``test_duration_w_hours`` to the hours from ``wake_time`` and ``sleep_time``

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            wake_time.split(':')[0],
            sleep_time.split(':')[0]
        )
    )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: (['00', '00'], ['19', '00']) != ('00', '19')
    AssertionError: Tuples differ: (['14', '00'], ['17', '00']) != ('14', '17')
    AssertionError: Tuples differ: (['05', '00'], ['08', '00']) != ('05', '08')
    AssertionError: Tuples differ: (['23', '00'], ['04', '00']) != ('23', '04')

  the ``duration`` :ref:`function<functions>` returns the result of splitting the timestamps but the test expects the hours, I change it to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            wake_time.split(':')[0],
            sleep_time.split(':')[0]
        )

  the test passes


test_converting_strings_to_numbers
#################################################################################

The hours part of the timestamp after calling `str.split`_ is still a string_ and I got :ref:`TypeError` when I tried to subtract one from another earlier. I want to see if I can use the int_ constructor_ to change a string_ to a number

* I add a new failing test to test numbers that have a ``0`` in front of them

  .. code-block:: python

    def test_converting_strings_to_numbers(self):
        self.assertEqual(int('01'), 0)

    def test_duration_w_hours(self):
    ...

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 1 != 0

  I change the expectation to ``1``

  .. code-block:: python

    self.assertEqual(int('01'), 1)

  the test passes

* I add another :ref:`assertion<AssertionError>` to test a bigger number

  .. code-block:: python

    self.assertEqual(int('23'), 1)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 23 != 1

  I change the number from ``1`` to ``23``

  .. code-block:: python

    self.assertEqual(int('23'), 23)

  the terminal_ shows green again

----

* I add calls to the int_ constructor_ in the expectation of ``test_duration_w_hours``

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            int(wake_time.split(':')[0]),
            int(sleep_time.split(':')[0])
        )
    )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ('00', '05') != (0, 5)
    AssertionError: Tuples differ: ('08', '21') != (8, 21)
    AssertionError: Tuples differ: ('04', '04') != (4, 4)
    AssertionError: Tuples differ: ('16', '14') != (16, 14)

  the ``duration`` :ref:`function<functions>` returns the hours as a string_ but the test expects them as numbers, I change it to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            int(wake_time.split(':')[0]),
            int(sleep_time.split(':')[0])
        )

  the test passes

* I change the expectation in ``test_duration_w_hours`` to the difference between the hours

  .. code-block:: python

    self.assertEqual(
        src.sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            int(wake_time.split(':')[0])
           -int(sleep_time.split(':')[0])
        )
    )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (7, 23) != -16
    AssertionError: (11, 4) != 7
    AssertionError: (12, 21) != -9
    AssertionError: (14, 2) != 12

  the ``duration`` :ref:`function<functions>` returns the hours from the timestamps and the test expects the difference between them. I change the ``duration`` :ref:`function<functions>` to match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            int(wake_time.split(':')[0])
          - int(sleep_time.split(':')[0])
        )

  the test passes! Celebration Time!!

* I add a :ref:`function<functions>` to get the hours part of a given timestamp since it is the only part that changes in the solution

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

  and the terminal_ still shows passing tests!

* ``wake_hour`` and ``sleep_hour`` are only used once in  ``test_sleep_duration.py``, I can change them with direct calls to `random.randint`_

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_time = f'{random.randint(0,23):02}:00'
        sleep_time = f'{random.randint(0,23):02}:00'
    ...

  the terminal_ still shows passing tests

* ``wake_time`` and ``sleep_time`` are defined in the same way, time to make a :ref:`function<functions>` that returns a random timestamp

  .. code-block:: python

    def random_timestamp():
        return f'{random.randint(0,23):02}:00'

  and call it in ``test_duration_w_hours``

  .. code-block:: python

    def test_duration_w_hours(self):
        sleep_time = random_timestamp()
        wake_time = random_timestamp()
    ...

  all tests are still passing! What a beautiful life!!

----


*********************************************************************************
review
*********************************************************************************

The challenge is to write a program_ that calculates the difference between a given wake and sleep time. I ran the following tests to get something that comes close to doing it


* `test_string_splitting`_ where I

  - used the `str.split`_ :ref:`method<functions>` I found by calling the `help system`_ to split a string_ on a separator
  - and indexed the :ref:`list <lists>` from the split to get specific items

* `test_converting_strings_to_numbers`_ with the int_ constructor_

* :ref:`test_duration_w_hours <how to measure sleep duration: test_duration_w_hours>` where I

  - used `random.randint`_ to generate random numbers from the 24 hours in a day and :ref:`how to pass values` them in the timestamps
  - then test that the ``duration`` :ref:`function<functions>` subtracts the hour for ``sleep_time`` from the hour for ``wake_time``

I also ran into the following :ref:`Exceptions<errors>`

* :ref:`AssertionError`
* :ref:`TypeError`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError`

Would you like to :ref:`test duration with hours and minutes? <how to measure sleep duration: test_duration_w_hours_and_minutes>`

----

:ref:`how to measure sleep duration: tests and solution`