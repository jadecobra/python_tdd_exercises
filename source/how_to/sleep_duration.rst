.. include:: ../links.rst

********************************************************
how to measure sleep duration
********************************************************

In this chapter, I take a look at building a program that returns the duration between a given sleep and wake time.

----

test_duration_w_hours
========================================================

.. _test_duration_w_hours_red:

red: make it fail
--------------------------------------------------------

* I open a terminal and call :ref:`createPythonTdd.sh` with ``sleep_duration`` as the project name

  .. code-block:: python

    ./createPythonTdd.sh sleep_duration

  .. NOTE::

    If you are using Windows without `Windows Subsystem Linux`_ use :ref:`createPythonTdd.ps1`

    .. code-block:: python

      ./createPythonTdd.ps1 sleep_duration

  the terminal shows

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_sleep_duration.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_sleep_duration.py:7`` with my mouse to open the file in the editor
* then remove ``test_failure`` after making it pass
* I add a failing test to check that when the ``duration`` :ref:`function<functions>` in the ``sleep_duration`` :doc:`module </exceptions/ModuleNotFoundError>` is called with a ``wake_time`` of ``'08:00'`` and ``sleep_time`` of ``'07:00'`` it returns ``1`` which in this case is the difference between the two

  .. code-block:: python

    import unittest


    class TestSleepDuration(unittest.TestCase):

        def test_duration_w_hours(self):
            self.assertEqual(
                sleep_duration.duration(
                    wake_time='08:00',
                    sleep_time='07:00'
                ),
                1
            )

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'sleep_duration' is not defined

.. _test_duration_w_hours_green:

green: make it pass
--------------------------------------------------------

* which I add to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

* I add an `import statement`_ for the missing name at the top of the file

  .. code-block:: python

    import sleep_duration
    import unittest


    class TestSleepDuration(unittest.TestCase):
    ...

  and the terminal shows an :ref:`AttributeError` because I do not have a definition for ``duration`` in ``sleep_duration.py``

  .. code-block:: python

    AttributeError: module 'sleep_duration' has no attribute 'duration'

* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* then open ``sleep_duration.py`` to add a name ::

    duration

  and the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'duration' is not defined

* I make ``duration`` a variable by assigning it to :ref:`None`

  .. code-block:: python

    duration = None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* which I add to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I make ``duration`` a :ref:`function<functions>` to make it callable_

  .. code-block:: python

    def duration():
        return None

  and the terminal shows a :ref:`TypeError` with a different message about the first keyword argument given in the test

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'wake_time'

  ``test_duration_w_hours`` passes values with keyword arguments named ``wake_time`` and ``sleep_time`` to the ``duration`` :ref:`function<functions>`, and those keyword arguments were not provided in the signature when it was defined

* When I add the required keyword argument with a default value to :ref:`None`

  .. code-block:: python

    def duration(wake_time=None):
        return None

  the terminal shows a similar :ref:`TypeError` message for the second keyword argument

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'sleep_time'

* I also add the second keyword argument setting its default value to :ref:`None`

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return None

  and the terminal shows an :ref:`AssertionError`. The ``duration`` :ref:`function<functions>` returned :ref:`None` but ``test_duration_w_hours`` expects ``1`` as the result

  .. code-block:: python

    AssertionError: None != 1

* I make the return value match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return 1

  and the test passes

.. _test_duration_w_hours_refactor_0:

refactor: make it better
--------------------------------------------------------

The ``duration`` :ref:`function<functions>` currently returns ``1`` even when its inputs change. For it to meet the requirements it has to calculate the difference between ``wake_time`` and ``sleep_time``. I will add a test that uses random variables to cover all timestamps from ``'00:00'`` to ``'23:59'``

* I add an `import statement`_ for the random_ module to ``test_sleep_duration.py``

  .. code-block:: python

    import random
    import sleep_duration
    import unittest

* then add random values for the hours part of the timestamps in ``test_duration_w_hours``

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

  - ``random.randint(0, 23)`` returns a random integer_ from ``0`` up to and including ``23``
  - ``f'{wake_hour:02}:00'`` and ``f'{sleep_hour:02}:00'`` :doc:`interpolate </how_to/pass_values>` the random integers_ in the input strings_
  - the ``:02`` in ``{wake_hour:02}`` and ``{sleep_hour:02}`` tell Python to display the numbers as two digits. For example, display ``01`` instead of ``1``

* When I make the test match the requirement of the difference between ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)

        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour:02}:00',
                sleep_time=f'{sleep_hour:02}:00'
            ),
            wake_hour-sleep_hour
        )

  the terminal shows an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: 1 != -2
    AssertionError: 1 != 3
    AssertionError: 1 != -8
    AssertionError: 1 != 4

* I make the ``duration`` :ref:`function<functions>` return the subtraction of ``sleep_time`` from ``wake_time``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return wake_time - sleep_time

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

  because Python does not have an operation defined for subtracting one string_ from another. I need a way to convert a timestamp from a string_ to an integer_.

test_string_attributes_and_methods
========================================================

The ``wake_time`` and ``sleep_time`` are currently in this format - ``XX:00``. I can calculate the difference if I can get the first 2 characters and convert them to numbers since Python can do :doc:`arithmetic </how_to/calculator>`.

.. _test_string_attributes_and_methods_red:

red: make it fail
--------------------------------------------------------

* I disable ``test_duration_w_hours`` by adding the `unittest.skip decorator`_

  .. code-block:: python

    @unittest.skip
    def test_duration_w_hours(self):
    ...

* then use the dir_ :ref:`function<functions>` to see the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of strings_, maybe that will help me find a way to break them apart or get the characters I want

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
    # AttributeError
    # TypeError
    # SyntaxError

* there is a closing quote with no open quote, so I add one

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

  - and the terminal shows the list of :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of a string_
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
* I want to try one of the :ref:`methods<functions>` listed in ``test_string_attributes_and_methods`` to see if it will get me closer to a solution, but I cannot tell what they do by the names alone. I need more details so I use the `help system`_ to check the `python documentation for strings`_

  .. code-block:: python

    def test_string_attributes_and_methods(self):
        ...
        self.assertEqual(help(str))

  the terminal shows documentation for the string_ module and I scroll through reading the descriptions for each :ref:`method<functions>` until I see one that looks like it could solve the problem

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
========================================================

.. _test_string_splitting_red_0:

red: make it fail
--------------------------------------------------------

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

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: ['01:23'] != None

`str.split`_ returns a :doc:`list </data_structures/lists/lists>` when called

.. _test_string_splitting_green_0:

green: make it pass
--------------------------------------------------------

I copy the :doc:`list </data_structures/lists/lists>` in the terminal and paste it in the test to make it pass

.. code-block:: python

  def test_string_splitting(self):
      self.assertEqual(
          '01:23'.split(),
          ['01:23']
      )

.. _test_string_splitting_refactor:

refactor: make it better
--------------------------------------------------------

* I change the expectation of the test because I want to split the string_ on a separator to get the different parts, something like ``['01', '23']`` with a ``:`` as the separator

  .. code-block:: python

    def test_string_splitting(self):
        self.assertEqual(
            '01:23'.split(),
            ['01', '23']
        )

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['01:23'] != ['01', '23']

* From the documentation `str.split`_ takes in ``sep=None, maxsplit=-1`` as inputs and ``sep`` is the separator. I pass in ``':'`` as the separator

  .. code-block:: python

    def test_string_splitting(self):
        self.assertEqual(
            '01:23'.split(':'),
            ['01', '23']
        )

  and the test passes. Whoa! I now know how to get the different parts of ``wake_time`` and ``sleep_time``

* I remove the `unittest.skip decorator`_ from ``test_duration_w_hours``
* then add calls to the `str.split`_ :ref:`method<functions>` in the ``duration`` :ref:`function<functions>` in ``sleep_duration.py``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            wake_time.split(':')
          - sleep_time.split(':')
        )

  and the terminal shows a :ref:`TypeError`, this time for trying to subtract one :doc:`list </data_structures/lists/lists>` from another

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'list' and 'list'

.. _test_string_splitting_red_1:

red: make it fail
--------------------------------------------------------

* I only need the first item of the list created from splitting the timestamp string_, which I can get by using its index. Python uses `zero-based indexing`_ which means the first item is at index ``0`` and the second item is at index ``1``. See :doc:`/data_structures/lists/lists` for more. I add tests to ``test_string_splitting`` for getting specific parts of a :doc:`list </data_structures/lists/lists>` created from calling `str.split`_

  .. code-block:: python

    def test_string_splitting(self):
        self.assertEqual(
            '01:23'.split(':'),
            ['01', '23']
        )

        timestamp_split = '12:34'.split(':')
        self.assertEqual(
            timestamp_split[0],
            0
        )
        self.assertEqual(
            timestamp_split[1],
            0
        )

    def test_duration_w_hours(self):
    ...

  the terminal shows an :ref:`AssertionError` because the first item (index 0) from splitting ``'12:34'`` on the separator ``':'`` is ``'12'``

  .. code-block:: python

    AssertionError: '12' != 0

  this is closer to what I want

.. test_string_splitting_green_1:

green: make it pass
--------------------------------------------------------

* I make the expected value in the test match the value in the terminal

  .. code-block:: python

    self.assertEqual(
        '12:34'.split(':')[0],
        '12'
    )

  and the terminal shows another :ref:`AssertionError` for the next line

  .. code-block:: python

    AssertionError: '34' != 0

  showing that the second item (index 1) from splitting ``'12:34'`` on the separator ``':'`` is ``'34'``

* When I make the expected value in the test match the value in the terminal,

  .. code-block:: python

    self.assertEqual(
        '12:34'.split(':')[1],
        '34'
    )

  the test passes, bringing me back to the unsolved :ref:`TypeError`

* I take what I have learned and make the ``duration`` :ref:`function<functions>` return the result of subtracting the first items of the list got from splitting ``wake_time`` and ``sleep_time`` on the separator ``':'``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            wake_time.split(':')[0]
          - sleep_time.split(':')[0]
        )

  and the terminal shows a :ref:`TypeError` for an unsupported operation of trying to subtract one string_ from another. I know from ``test_string_splitting`` that the strings being subtracted are the values to the left of the separator ``':'``, not the entire values of ``wake_time`` and ``sleep_time``.

  For example, if the given ``wake_time`` is ``'02:00'`` and the given ``sleep_time`` is ``'01:00'``, the ``duration`` :ref:`function<functions>` tries to subtract ``'01'`` from ``'02'`` which is different than trying to subtract ``1`` from ``2`` - ``'01'`` is a string_ and ``1`` is an integer_

test_converting_strings_to_integers
========================================================

I want to see if I can use the int_ constructor to convert a string_ to an integer_

.. _test_converting_strings_to_integers_red:

red: make it fail
--------------------------------------------------------

I disable the current failing test by using the `unittest.skip decorator`_

.. code-block:: python

  @unittest.skip
  def test_duration_w_hours(self):
  ...

then add a new failing test called ``test_converting_strings_to_integers``

.. code-block:: python

  def test_converting_strings_to_integers(self):
      self.assertEqual(int('12'), 0)
      self.assertEqual(int('01'), 0)

  @unittest.skip
  def test_duration_w_hours(self):
  ...

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 12 != 0

.. _test_converting_strings_to_integers_green:

green: make it pass
--------------------------------------------------------

When I make the failing line match the value in the terminal

.. code-block:: python

  self.assertEqual(int('12'), 12)

the terminal shows an :ref:`AssertionError` for the next one

.. code-block:: python

  AssertionError: 1 != 0

and when I make the next line match the value in the terminal

.. code-block:: python

  self.assertEqual(int('01'), 1)

the terminal shows passings tests. Things are green again and I have another tool to help solve the problem

- I can split a string_ on a separator using `str.split`_ to get a :doc:`list </data_structures/lists/lists>` of its parts
- I can index the :doc:`list </data_structures/lists/lists>`  from splitting the string_ to get a specific item from it
- I can convert a string_ to an integer_ using the int_ constructor

----

.. _test_duration_w_hours_refactor_1:

* I remove the `unittest.skip decorator`_ from ``test_duration_w_hours`` to show the :ref:`TypeError` I have been trying to solve
* then add the conversion using the int_ constructor to the ``duration`` :ref:`function<functions>` to see if it will make the test pass

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            int(wake_time.split(':')[0])
          - int(sleep_time.split(':')[0])
        )

  and it does, the terminal shows green! YES! The ``duration`` :ref:`function<functions>` calculates the duration between any given random sleep and wake hours in a day. What a beautiful life!

* Since all the tests are passing I can rewrite the solution as a series of steps for someone who does not know how to use `str.split`_, index a :doc:`list </data_structures/lists/lists>` or use the int_ constructor

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time_split = wake_time.split(':')
        wake_time_hour = wake_time_split[0]
        wake_time_hour_integer = int(wake_time_hour)

        return (
            # int(wake_time.split(':')[0])
            wake_time_hour_integer
          - int(sleep_time.split(':')[0])
        )

  and the terminal shows all tests are still passing

* so I try the same thing for ``sleep_time``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time_split = wake_time.split(':')
        wake_time_hour = wake_time_split[0]
        wake_time_hour_integer = int(wake_time_hour)

        sleep_time_split = sleep_time.split(':')
        sleep_time_hour = sleep_time_split[0]
        sleep_time_hour_integer = int(sleep_time_hour)

        return (
            wake_time_hour_integer
        # - int(sleep_time.split(':')[0])
          - sleep_time_hour_integer
        )

  and the terminal still shows passing tests

* the ``duration`` :ref:`function<functions>` does the following for each given timestamp

  - splits the timestamp string_ on the separator ``':'``
  - gets the first item from the split
  - then converts the first item from the split to an integer_

  I can make these steps a separate :ref:`function<functions>` that is called for ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def process(timestamp):
        timestamp_split = timestamp.split(':')
        timestamp_hour = timestamp_split[0]
        timestamp_hour_integer = int(timestamp_hour)
        return timestamp_hour_integer

    def duration(wake_time=None, sleep_time=None):
        return (
            process(wake_time)
          - process(sleep_time)
        )

        wake_time_split = wake_time.split(':')
        wake_time_hour = wake_time_split[0]
        wake_time_hour_integer = int(wake_time_hour)

        sleep_time_split = sleep_time.split(':')
        sleep_time_hour = sleep_time_split[0]
        sleep_time_hour_integer = int(sleep_time_hour)

        return (
            wake_time_hour_integer
          - sleep_time_hour_integer
        )

  and the terminal shows all tests are still green

* I remove the parts of ``duration`` that are no longer used and rename ``process`` to something more descriptive

  .. code-block:: python

    def get_hour(timestamp):
        timestamp_split = timestamp.split(':')
        timestamp_hour = timestamp_split[0]
        timestamp_hour_integer = int(timestamp_hour)
        return timestamp_hour_integer

    def duration(wake_time=None, sleep_time=None):
        return (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )

  the terminal still shows passing tests

* I can also make ``get_hour`` use the same variable name instead of a new one for each step

  .. code-block:: python

    def get_hour(value):
        value = value.split(':')
        value = value[0]
        value = int(value)
        return value

* or change ``get_hour`` to use one line, though it might not be as easy to understand

  .. code-block:: python

    def get_hour(timestamp):
        return int(timestamp.split(':')[0])

* I can also create a :ref:`function<functions>` that makes random hours in ``test_sleep_duration.py``

  .. code-block:: python

    import random
    import sleep_duration
    import unittest

    def random_hour():
        return random.randint(0, 23)


    class TestSleepDuration(unittest.TestCase):
    ...

  then call it in ``test_duration_w_hours``

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

  and the terminal still shows passing tests

I think it is time for a break ...

----

test_duration_w_hours_and_minutes
========================================================

The ``duration`` :ref:`function<functions>` has only been tested with timestamps that have random hours and ``00`` as the minutes. For it to meet the requirements, it should accept timestamps with random hours and random minutes.

.. _test_duration_w_hours_and_minutes_red:

red: make it fail
--------------------------------------------------------

* I copy ``test_duration_w_hours`` in ``test_sleep_duration.py``, paste it below the original
* then rename the copy to ``test_duration_w_hours_and_minutes`` adding variables for random minutes

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        wake_hour = random_hour()
        wake_minutes = random.randint(0, 59)

        sleep_hour = random_hour()
        sleep_minutes = random.randint(0, 59)

        difference_hours = wake_hour - sleep_hour
        difference_minutes = wake_minutes - sleep_minutes

        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour:02}:{wake_minutes:02}',
                sleep_time=f'{sleep_hour:02}:{sleep_minutes:02}'
            ),
            f'{difference_hours:02}:{difference_minutes:02}'
        )

  and the terminal shows an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: 4 != '4:-20'
    AssertionError: 6 != '-7:00'
    AssertionError: -5 != '-15:-37'
    AssertionError: -8 != '-40:-40'

  the ``duration`` :ref:`function<functions>` returns the numbers on the left but ``test_duration_w_hours_and_minutes`` expects the strings_ on the right because I changed the expected duration to a string_ that contains the subtraction of ``sleep_hour`` from ``wake_hour`` and the subtraction of ``sleep_minutes`` from ``wake_minutes`` separated by a ``:``

.. _test_duration_w_hours_and_minutes_green:

green: make it pass
--------------------------------------------------------

* I make the output of ``duration`` match the format of the expected value in the test by adding the same variables and calculations

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference_hours = (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )
        difference_minutes = (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )

        return f'{difference_hours}:{difference_minutes}'

  and the terminal shows an :ref:`AssertionError` for ``test_duration_w_hours`` because it expects an integer_ not a string_

  .. code-block:: python

    AssertionError: '5:5' != 5
    AssertionError: '-8:-8' != -8
    AssertionError: '1:1' != 1
    AssertionError: '-3:-3' != -3

  and an :ref:`AssertionError` for ``test_duration_w_hours_and_minutes`` because ``duration`` returns the same value for ``difference_hours`` and ``difference_minutes``

  .. code-block:: python

    AssertionError: '7:7' != '07:-13'
    AssertionError: '-16:-16' != '-16:-22'
    AssertionError: '14:14' != '14:36'
    AssertionError: '-2:-2' != '-2:-49'

* The change for the new test has made ``test_duration_w_hours`` fail so I disable ``test_duration_w_hours_and_minutes`` with the `unittest.skip decorator`_ while I fix the failure

  .. code-block:: python

    @unittest.skip
    def test_duration_w_hours_and_minutes(self):
    ...

* then I make ``test_duration_w_hours`` use the new format

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random_hour()
        sleep_hour = random_hour()

        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour:02}:00',
                sleep_time=f'{sleep_hour:02}:00'
            ),
            f'{wake_hour-sleep_hour}:00'
        )

  and the terminal shows an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: '1:1' != '1:00'
    AssertionError: '-19:-19' != '-19:00'
    AssertionError: '17:17' != '17:00'
    AssertionError: '-8:-8' != '-8:00'

  the ``duration`` :ref:`function<functions>` returns the strings_ on the left which uses ``get_hour`` for the hours and minutes and ``test_duration_w_hours`` expects the strings_ on the right which always have ``00`` as minutes. I need to update the calculation for ``difference_minutes``

* I copy ``get_hour`` in ``sleep_duration.py``, paste it below the original
* then change the name of the copy to ``get_minutes`` and the index to ``1`` to get the minutes part from splitting the timestamp

  .. code-block:: python

    def get_hour(timestamp):
        return int(timestamp.split(':')[0])

    def get_minutes(timestamp):
        return int(timestamp.split(':')[1])

* I also add calls to ``get_minutes`` in the calculation for ``difference_minutes`` in the ``duration`` :ref:`function<functions>`

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference_hours = (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )
        difference_minutes = (
            get_minutes(wake_time)
          - get_minutes(sleep_time)
        )

        return f'{difference_hours}:{difference_minutes}'

  and the terminal shows an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: '4:0' != '4:00'
    AssertionError: '-4:0' != '-4:00'
    AssertionError: '21:0' != '21:00'
    AssertionError: '-10:0' != '-10:00'

  the ``duration`` :ref:`function<functions>` returns the right value for hours and minutes, but displays 1 digit for minutes while ``test_duration_w_hours`` expects 2 digits for minutes

* I make ``duration`` show two digits for hours and minutes in the result

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference_hours = (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )
        difference_minutes = (
            get_minutes(wake_time)
          - get_minutes(sleep_time)
        )

        return f'{difference_hours:02}:{difference_minutes:02}'

  and the terminal shows random successes or :ref:`AssertionErrors<AssertionError>` like

  .. code-block:: python

    AssertionError: '06:00' != '6:00'

  the ``duration`` :ref:`function<functions>` returns the hours as 2 digits while ``test_duration_w_hours`` expects 1 digit for hours

* I add ``difference_hours`` to ``test_duration_w_hours`` so it can show 2 digits for hours

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random_hour()
        sleep_hour = random_hour()

        difference_hours = wake_hour - sleep_hour

        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour:02}:00',
                sleep_time=f'{sleep_hour:02}:00'
            ),
            f'{difference_hours:02}:00'
        )

  and all tests pass, we are green again

* When I remove the `unittest.skip decorator`_ from ``test_duration_w_hours_and_minutes``, the terminal shows passing tests. It looks like making sure ``test_duration_w_hours`` passed, also made ``test_duration_w_hours_and_minutes`` pass

.. _test_duration_w_hours_and_minutes_refactor_0:

refactor: make it better
--------------------------------------------------------

* I remove ``test_duration_w_hours`` because the timestamps it tests are included in what is provided by ``test_duration_w_hours_and_minutes`` which uses a random integer_ from ``0`` up to and including ``23`` for hours, and a random integer_ from ``0`` up to and including ``59`` for minutes. This means it covers all timestamps from ``00:00`` up to and including ``23:59``, which is all the hours and minutes in a day.
* I also add a :ref:`function<functions>` for making random minutes

  .. code-block:: python

    ...

    def random_hour():
        return random.randint(0, 23)

    def random_minutes():
        return random.randint(0, 59)


    class TestSleepDuration(unittest.TestCase):
    ...

  and add calls to it in ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        wake_hour = random_hour()
        wake_minutes = random_minutes()

        sleep_hour = random_hour()
        sleep_minutes = random_minutes()

        difference_hours = wake_hour - sleep_hour
        difference_minutes = wake_minutes - sleep_minutes

        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour:02}:{wake_minutes:02}',
                sleep_time=f'{sleep_hour:02}:{sleep_minutes:02}'
            ),
            f'{difference_hours:02}:{difference_minutes:02}'
        )

  the terminal shows all tests are still passing

test_duration_calculation
========================================================

The ``duration`` :ref:`function<functions>` currently returns a subtraction of hours and a subtraction of minutes which is not correct for calculating the difference between two timestamps

.. _test_duration_calculation_red:

red: make it fail
--------------------------------------------------------

If ``duration`` is given a ``wake_time`` of ``'03:30'`` and a ``sleep_time`` of ``'02:59'``, it should return ``'00:31'`` as the difference between the timestamps

.. code-block:: python

  def test_duration_calculation(self):
      self.assertEqual(
          sleep_duration.duration(
              wake_time='03:30',
              sleep_time='02:59'
          ),
          '00:31'
      )

but the terminal shows this :ref:`AssertionError` when I add ``test_duration_calculation``

.. code-block:: python

  AssertionError: '01:-29' != '00:31'

the ``duration`` :ref:`function<functions>` returns ``'01:-29'`` which is not a real duration

.. _test_duration_calculation_green:

green: make it pass
--------------------------------------------------------

* I rename ``duration`` to keep a copy of my current working solution

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
        difference_hours = (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )
        difference_minutes = (
            get_minutes(wake_time)
          - get_minutes(sleep_time)
        )

        return f'{difference_hours:02}:{difference_minutes:02}'

* then add a new ``duration`` :ref:`function<functions>` with the following steps to calculate a real difference between two timestamps

  - get total minutes for each timestamp by multiplying the hour by 60 and adding the minutes
  - get the difference by subtracting total ``sleep_time`` minutes from total ``wake_time`` minutes
  - return the difference between total ``wake_time`` and total ``sleep_time`` minutes as hours and minutes by

    * using `floor (integer) division`_ to get the whole number value of dividing the difference by 60 for the hours
    * using the modulo_ operator to get the remainder from dividing the difference by 60 for the minutes

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time_minutes = (
            (get_hour(wake_time) * 60)
           + get_minutes(wake_time)
        )
        sleep_time_minutes = (
            (get_hour(sleep_time) * 60)
           + get_minutes(sleep_time)
        )

        difference = (
            wake_time_minutes
          - sleep_time_minutes
        )
        difference_hours = difference // 60
        difference_minutes = difference % 60

        return f'{difference_hours:02}:{difference_minutes:02}'

  ``test_duration_calculation`` passes and since ``test_duration_w_hours_and_minutes`` uses the wrong calculation, the terminal shows random successes or :ref:`AssertionErrors<AssertionError>` that look like this

  .. code-block:: python

    AssertionError: '10:53' != '11:-7'

* I add the correct calculation to ``test_duration_w_hours_and_minutes``

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        wake_hour = random_hour()
        wake_minutes = random_minutes()
        wake_time_minutes = (
            (wake_hour * 60)
           + wake_minutes
        )

        sleep_hour = random_hour()
        sleep_minutes = random_minutes()
        sleep_time_minutes = (
            (sleep_hour * 60)
          + sleep_minutes
        )

        difference = (
            wake_time_minutes
          - sleep_time_minutes
        )
        difference_hours = difference // 60
        difference_minutes = difference % 60

        self.assertEqual(
            sleep_duration.duration(
                wake_time=f'{wake_hour:02}:{wake_minutes:02}',
                sleep_time=f'{sleep_hour:02}:{sleep_minutes:02}'
            ),
            f'{difference_hours:02}:{difference_minutes:02}'
        )

  and I have passing tests again! Green is a beautiful color.

test_floor_aka_integer_division
========================================================

The ``//`` operator returns a whole number that tells how many times the bottom number can be multiplied to get a whole number that is equal to or as close to the top number as possible

.. _test_floor_aka_integer_division_red:

red: make it fail
--------------------------------------------------------

I add a failing test for it

.. code-block:: python

  def test_floor_aka_integer_division(self):
      self.assertEqual(120//60, 0)
      self.assertEqual(150//60, 0)

  def test_duration_w_hours_and_minutes(self):
  ...

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 2 != 0

.. _test_floor_aka_integer_division_green:

green: make it pass
--------------------------------------------------------

* I change the first expected value in the test to the correct value. The result of dividing ``120`` by ``60`` is ``2`` with a remainder of ``0``

  .. code-block:: python

    self.assertEqual(120//60, 2)

  and the terminal shows an :ref:`AssertionError` for the next line

  .. code-block:: python

    AssertionError: 2 != 0

* then I change the expected value for it to the correct value. The result of dividing ``150`` by ``60`` is also ``2`` but with a remainder of ``30``

  .. code-block:: python

    self.assertEqual(150//60, 2)

  and the terminal shows passing tests

test_modulo_operation
========================================================

The ``%`` operator returns the remainder from dividing one number by another

.. _test_modulo_operation_red:

red: make it fail
--------------------------------------------------------

I add a failing test for it

.. code-block:: python

  def test_modulo_operation(self):
      self.assertEqual(120%60, 2)
      self.assertEqual(150%60, 2)

  def test_duration_w_hours_and_minutes(self):
  ...

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 0 != 2

.. _test_modulo_operation_green:

green: make it pass
--------------------------------------------------------

* I change the first expected value in the test to the correct value. The remainder from dividing ``120`` by ``60`` is ``0``

  .. code-block:: python

    self.assertEqual(120%60, 0)

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 30 != 2

* then I change the second expected value in the test to the correct value. The remainder from dividing ``150`` by ``60`` is ``30``

  .. code-block:: python

    self.assertEqual(150%60, 30)

  and the terminal shows passing tests

----

.. _test_duration_w_hours_and_minutes_refactor_0:

* I remove ``test_duration_calculation`` from ``test_sleep_duration.py`` because it is now covered by ``test_duration_w_hours_and_minutes``
* I remove ``duration_a`` from ``sleep_duration.py`` since the working solution in ``duration`` is better
* and then I write a :ref:`function<functions>` to get the total minutes from a timestamp and call it in ``duration``

  .. code-block:: python

    def get_total_minutes(timestamp):
        return (
            (get_hour(timestamp) * 60)
           + get_minutes(timestamp)
        )

    def duration(wake_time=None, sleep_time=None):
        wake_time_minutes = get_total_minutes(wake_time)
        sleep_time_minutes = get_total_minutes(sleep_time)

        difference = (
            wake_time_minutes
          - sleep_time_minutes
        )
        difference_hours = difference // 60
        difference_minutes = difference % 60

        return f'{difference_hours:02}:{difference_minutes:02}'

  the terminal still shows passing tests

* I also write a :ref:`function<functions>` to replace ``get_hour`` and ``get_minutes`` then call it in ``get_total_minutes``

  .. code-block:: python

    def parse_timestamp(timestamp=None, index=0):
        return int(timestamp.split(':')[index])

    def get_total_minutes(timestamp):
        return (
            (parse_timestamp(timestamp, 0) * 60)
           + parse_timestamp(timestamp, 1)
        )

  all tests are still passing

* I remove ``get_hour`` and ``get_minutes`` since they have been replaced by ``parse_timestamp``

----

test_duration_w_earlier_wake_than_sleep_time
========================================================

What happens when the ``duration`` :ref:`function<functions>` is given an earlier ``wake_time`` than ``sleep_time``?

.. _test_duration_w_earlier_wake_than_sleep_time_red:

red: make it fail
--------------------------------------------------------

I will add a failing test to ``test_sleep_duration.py`` to find out

.. code-block:: python

  def test_duration_w_earlier_wake_than_sleep_time(self):
      self.assertEqual(
          sleep_duration.duration(
              wake_time='01:00',
              sleep_time='02:00'
          ),
          ''
      )

  def test_duration_w_hours_and_minutes(self):
  ...

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: '-1:00' != ''

.. _test_duration_w_earlier_wake_than_sleep_time_green:

green: make it pass
--------------------------------------------------------

I change the expected value in the test to make it pass

.. code-block:: python

  def test_duration_w_earlier_wake_than_sleep_time(self):
      self.assertEqual(
          sleep_duration.duration(
              wake_time='01:00',
              sleep_time='02:00'
          ),
          '-1:00'
      )

and the terminal shows passing tests

.. _test_duration_w_earlier_wake_than_sleep_time_refactor:

refactor: make it better
--------------------------------------------------------

* The ``duration`` :ref:`function<functions>` currently returns negative numbers when given an earlier ``wake_time`` than ``sleep_time``. It measures a time traveling scenario where the traveler can go to sleep in the present and wake up in the past. I want it to return durations only when ``wake_time`` is later than or equal to ``sleep_time``, time traveling is hard. I will add a condition so it makes a decision

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time_minutes = get_total_minutes(wake_time)
        sleep_time_minutes = get_total_minutes(sleep_time)

        if wake_time_minutes < sleep_time_minutes:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
        else:
            difference = (
                wake_time_minutes
            - sleep_time_minutes
            )
            difference_hours = difference // 60
            difference_minutes = difference % 60

            return f'{difference_hours:02}:{difference_minutes:02}'

  - When ``wake_time_minutes`` is less than ``sleep_time_minutes``, ``wake_time`` is earlier than ``sleep_time`` and the ``duration`` :ref:`function<functions>` will raise an :doc:`Exception </how_to/exception_handling_programs>`
  - When ``wake_time_minutes`` is greater than or equal to ``sleep_time_minutes``, ``wake_time`` is later than or the same as ``sleep_time`` and the ``duration`` :ref:`function<functions>` returns the difference between the two timestamps

  the terminal shows a ValueError_ that looks like this for ``test_duration_w_earlier_wake_than_sleep_time`` and the random cases in ``test_duration_w_hours_and_minutes`` where ``wake_time`` is earlier than ``sleep_time``

  .. code-block:: python

    ValueError: wake_time: 20:26 is earlier than sleep_time: 23:50

* I add the error to the list of exceptions encountered even though I made this one happen

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError
    # ValueError

* then use `assertRaisesRegex`_ to catch the :doc:`Exception </how_to/exception_handling_tests>` with the specific message raised in ``test_duration_w_earlier_wake_than_sleep_time``

  .. code-block:: python

    def test_duration_w_earlier_wake_than_sleep_time(self):
        wake_time = '01:00'
        sleep_time = '02:00'

        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: {wake_time} is earlier '
            f'than sleep_time: {sleep_time}'
        ):
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            )

  and the test passes, leaving the random ValueError_ for ``test_duration_w_hours_and_minutes``

* I add an :doc:`exception handler </how_to/exception_handling_programs>` using a `try statement`_ and `assertRaisesRegex`_ to confirm the ValueError_ is raised when ``wake_time`` is earlier than ``sleep_time`` with the specific message from ``duration``

  .. code-block:: python

    def test_duration_w_hours_and_minutes(self):
        wake_hour = random_hour()
        wake_minutes = random_minutes()
        wake_time_minutes = (
            (wake_hour * 60)
           + wake_minutes
        )
        wake_time = f'{wake_hour:02}:{wake_minutes:02}'

        sleep_hour = random_hour()
        sleep_minutes = random_minutes()
        sleep_time_minutes = (
            (sleep_hour) * 60
           + sleep_minutes
        )
        sleep_time = f'{sleep_hour:02}:{sleep_minutes:02}'

        difference = (
            wake_time_minutes
          - sleep_time_minutes
        )
        difference_hours = difference // 60
        difference_minutes = difference % 60

        try:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                f'{difference_hours:02}:{difference_minutes:02}'
            )
        except ValueError:
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            ):
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )

  all tests are passing. Green, green, green, green all the way

I have a :ref:`function<functions>` that

* takes in a ``wake_time`` and ``sleep_time`` as inputs
* raises a ValueError_ with a message when ``wake_time`` is earlier than ``sleep_time``
* returns the difference between the two when ``wake_time`` is later than or the same as ``sleep_time``

Time for another break.

----

test_duration_w_date_and_time
========================================================

The ``duration`` :ref:`function<functions>` has been tested with timestamps that have hours and minutes with no date, but I could fall asleep on a Monday and wake up on a Tuesday. What would happen if I added dates to the timestamps?

.. _test_duration_w_date_and_time_red:

red: make it fail
--------------------------------------------------------

* I copy ``test_duration_w_hours_and_minutes`` and paste it below the original
* then rename the copy to ``test_duration_w_date_and_time`` to test ``duration`` with timestamps that have a date, hours and minutes

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        wake_hour = random_hour()
        wake_minutes = random_minutes()
        wake_time_minutes = (
            (wake_hour * 60)
           + wake_minutes
        )
        wake_time = f'31/12/99 {wake_hour:02}:{wake_minutes:02}'

        sleep_hour = random_hour()
        sleep_minutes = random_minutes()
        sleep_time_minutes = (
            (sleep_hour * 60)
          + sleep_minutes
        )
        sleep_time=f'31/12/99 {sleep_hour:02}:{sleep_minutes:02}'

        difference = (
            wake_time_minutes
          - sleep_time_minutes
        )
        difference_hours = difference // 60
        difference_minutes = difference % 60

        try:
            self.assertEqual(
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                ),
                f'{difference_hours:02}:{difference_minutes:02}'
            )
        except ValueError:
            with self.assertRaisesRegex(
                ValueError,
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            ):
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: "wake_time: 31/12/99 13:04 is earlier than sleep_time: 31/12/99 15:25" does not match "invalid literal for int() with base 10: '31/12/99 13'"

  it looks like ``test_duration_w_date_and_time`` encountered a ValueError_ with a different message than the one expected in the test. The `assertRaisesRegex`_ statement works, the test would have missed this if I did not specify what error message to catch

.. _test_duration_w_date_and_time_green_0:

green: make it pass
--------------------------------------------------------

* The ``parse_timestamp`` :ref:`function<functions>` tries to convert the given string_ to an integer but it is in the wrong format

  .. code-block:: python

    invalid literal for int() with base 10: '31/12/99 13'

* The `str.split`_ :ref:`method<functions>` was given a separator of a ``':'`` when the timestamp contained only hours and minutes, but behaves differently when the timestamp has a date. I will add a test to ``test_string_splitting`` for this

  .. code-block:: python

    def test_string_splitting(self):
        self.assertEqual(
            '01:23'.split(':'),
            ['01', '23']
        )

        timestamp_split = '12:34'.split(':')
        self.assertEqual(
            timestamp_split[0],
            '12'
        )
        self.assertEqual(
            timestamp_split[1],
            '34'
        )

        self.assertEqual(
            '31/12/99 13:04'.split(':')[0],
            ''
        )

  the terminal shows the :ref:`AssertionError` for ``test_duration_w_date_and_time`` and another for ``test_string_splitting``

  .. code-block:: python

    AssertionError: '31/12/99 13' != ''

  so I disable ``test_duration_w_date_and_time`` by adding the `unittest.skip decorator`_

  .. code-block:: python

    ...
    @unittest.skip
    def test_duration_w_date_and_time(self):
    ...

* then update ``test_string_splitting`` with the correct values to make it pass

  .. code-block:: python

    self.assertEqual(
        '31/12/99 13:04'.split(':')[0],
        '31/12/99 13'
    )

* I also add a test to ``test_converting_strings_to_integers`` to confirm that the ValueError_ is raised when calling the int_ constructor on the result of ``'31/12/99 13:04'.split(':')[0]``

  .. code-block:: python

    def test_converting_strings_to_integers(self):
        self.assertEqual(int('12'), 12)
        self.assertEqual(int('01'), 1)
        int('31/12/99 13')

  and the terminal shows a ValueError_ with the same message from ``test_duration_w_date_and_time``

  .. code-block:: python

    ValueError: invalid literal for int() with base 10: '31/12/99 13'

  I cannot convert a string_ in the format ``'31/12/99 13'`` to an integer

* I handle the ValueError_ with `assertRaises`_

  .. code-block:: python

    def test_converting_strings_to_integers(self):
        self.assertEqual(int('12'), 12)
        self.assertEqual(int('01'), 1)

        with self.assertRaises(ValueError):
            int('31/12/99 13')

  and tests are green again

* I need a solution that can read the date and time. Writing one myself requires calculating the number of days in months for every year. I do a search for `time difference <https://docs.python.org/3/search.html?q=time+difference>`_ in the `python online documentation`_ instead, to see if there is an existing solution and select the datetime_ module from the results since it looks like the right one. Reading through the available types in the module I see `datetime.datetime`_ objects which are a combination of date and time

  .. code-block:: python

    class datetime.datetime
      A combination of a date and a time.
        Attributes: year, month, day, hour,
        minute, second, microsecond, and tzinfo.

  and `datetime.timedelta`_ objects which are the difference between two `datetime.datetime`_ instances

  .. code-block:: python

    class datetime.timedelta
      A duration expressing the difference between
        two date, time, or datetime instances to
        microsecond resolution.

test_datetime_objects
========================================================

.. _test_datetime_objects_red:

red: make it fail
--------------------------------------------------------

I add a test to ``test_sleep_duration.py`` based on `Examples of usage: datetime <https://docs.python.org/3/library/datetime.html?highlight=time%20difference#examples-of-usage-datetime>`_ for `datetime.datetime`_ objects

.. code-block:: python

  def test_datetime_objects(self):
      self.assertEqual(
          datetime.datetime.strptime(
              '21/11/06 16:30',
              '%d/%m/%y %H:%M'
          ),
          ''
      )

  def test_duration_w_earlier_wake_than_sleep_time(self):
  ...

and the terminal shows a NameError_ because ``datetime`` is not defined in ``test_sleep_duration.py``, I need to import it

.. code-block:: python

  NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

.. _test_datetime_objects_green:

green: make it pass
--------------------------------------------------------

I add an `import statement`_ for the datetime_ module,

.. code-block:: python

  import datetime
  import random
  import sleep_duration
  import unittest
  ...

the terminal shows an :ref:`AssertionError`,

.. code-block:: python

  AssertionError: datetime.datetime(2006, 11, 21, 16, 30) != ''

I copy the value on the left side of the :ref:`AssertionError` to replace the expected value in the test,

.. code-block:: python

  def test_datetime_objects(self):
      self.assertEqual(
          datetime.datetime.strptime(
              '21/11/06 16:30',
              '%d/%m/%y %H:%M'
          ),
          datetime.datetime(2006, 11, 21, 16, 30)
      )

and the terminal shows passing tests. From this test I see that

* when the `datetime.datetime.strptime`_ :ref:`method<functions>` is given 2 strings_ as inputs - a timestamp and a pattern, it returns a `datetime.datetime`_ object with ``year``, ``month``, ``date``, ``hours`` and ``minutes``
* It also looks like the pattern provided means

  - ``%d`` is for days
  - ``%m`` is for months
  - ``%y`` is for 2 digit years
  - ``%H`` is for hours
  - ``%M`` is for minutes

  you can see more in `strftime() and strptime() behavior <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior>`_

test_subtracting_datetime_objects
========================================================

.. _test_subtracting_datetime_objects_red:

red: make it fail
--------------------------------------------------------

I add a test for subtracting two `datetime.datetime`_ objects

.. code-block:: python

  def test_subtracting_datetime_objects(self):
      sleep_time = datetime.datetime.strptime(
          '21/11/06 16:30',
          '%d/%m/%y %H:%M'
      )
      wake_time = datetime.datetime.strptime(
          '21/11/06 17:30',
          '%d/%m/%y %H:%M'
      )

      self.assertEqual(
          wake_time-sleep_time,
          1
      )

  def test_duration_w_hours_and_minutes(self):
  ...


the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: datetime.timedelta(seconds=3600) != 1

.. _test_subtracting_datetime_objects_green:

green: make it pass
--------------------------------------------------------

I copy the value on the left of the :ref:`AssertionError` and replace the expected value in the test to make it pass

.. code-block:: python

  self.assertEqual(
      wake_time-sleep_time,
      datetime.timedelta(seconds=3600)
  )

With these passing tests. I see that I can

- convert a string_ to a `datetime.datetime`_ object
- subtract one `datetime.datetime`_ object from another to get a `datetime.timedelta`_ object

.. _test_subtracting_datetime_objects_refactor:

refactor: make it better
--------------------------------------------------------

I add a variable to remove the duplication of the timestamp pattern

.. code-block:: python

  def test_subtracting_datetime_objects(self):
      pattern = '%d/%m/%y %H:%M'
      sleep_time = datetime.datetime.strptime(
          '21/11/06 16:30', pattern
      )
      wake_time = datetime.datetime.strptime(
          '21/11/06 17:30', pattern
      )
      self.assertEqual(wake_time-sleep_time, 1)

test_converting_timedelta_to_string
========================================================

.. _test_converting_timedelta_to_string_red:

red: make it fail
--------------------------------------------------------

* The `datetime.timedelta`_ object I get shows seconds, but I want the result as a string_. What happens when I pass it to the str_ constructor?

  .. code-block:: python

    def test_converting_timedelta_to_string(self):
        self.assertEqual(
            str(datetime.timedelta(seconds=7654)),
            ''
        )

    def test_duration_w_hours_and_minutes(self):
    ...

  the terminal shows an :ref:`AssertionError` with a string_ like what I want

  .. code-block:: python

    AssertionError: '2:07:34' != ''

.. _test_converting_timedelta_to_string_green:

green: make it pass
--------------------------------------------------------

I make the expected value in the test match the value from the terminal

.. code-block:: python

  self.assertEqual(
      str(datetime.timedelta(seconds=7654)),
      '2:07:34'
  )

and the test passes. It looks like calling str_ on a `datetime.timedelta`_ object returns a string_ in the format ``Hours:Minutes:Seconds``

From the tests, I know I can

* convert a string_ to a `datetime.datetime`_ object
* subtract one `datetime.datetime`_ object from another to get a `datetime.timedelta`_ object
* convert a `datetime.timedelta`_ object to a string_

----

.. _test_duration_w_date_and_time_green_1:

* I remove the `unittest.skip decorator`_ from ``test_duration_w_date_and_time`` to return to the ValueError_ that sent me down this path
* I rename the ``duration`` :ref:`function<functions>` in ``sleep_duration.py`` to ``duration_a`` to keep the existing working solution while I try a new one

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
        wake_time_minutes = get_total_minutes(wake_time)
        sleep_time_minutes = get_total_minutes(sleep_time)

        if wake_time_minutes < sleep_time_minutes:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
        else:
            difference = (
                wake_time_minutes
            - sleep_time_minutes
            )
            difference_hours = difference // 60
            difference_minutes = difference % 60

            return f'{difference_hours:02}:{difference_minutes:02}'

* then add a :ref:`function<functions>` to ``sleep_duration.py`` called ``get_datetime_object`` that uses `datetime.datetime.strptime`_ to read timestamps

  .. code-block:: python

    def duration_a(wake_time=None, sleep_time=None):
    ...

    def get_datetime_object(timestamp):
        return datetime.datetime.strptime(
            timestamp, '%d/%m/%y %H:%M'
        )

* and a new ``duration`` :ref:`function<functions>` with calls to ``get_datetime_object`` when calculating the difference between ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        difference = (
            get_datetime_object(wake_time)
          - get_datetime_object(sleep_time)
        )
        return str(difference)

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

  You know I did. I encountered this earlier when testing the datetime_ module

* I add an `import statement`_ to the top of ``sleep_duration.py``

  .. code-block:: python

    import datetime

    def parse_timestamp(timestamp=None, index=0):
    ...

  and the terminal shows an :ref:`AssertionError` for ``test_duration_w_earlier_wake_than_sleep_time`` and ``test_duration_w_hours_and_minutes``,  that looks like this

  .. code-block:: python

    AssertionError: "wake_time: 10:52 is earlier than sleep_time: 04:00" does not match "time data '10:52' does not match format '%d/%m/%y %H:%M'"

  I have another ValueError_, this time for a timestamp that does not match the expected pattern of ``'%d/%m/%y %H:%M'`` and another :ref:`AssertionError` for ``test_duration_w_date_and_time`` that looks like this

  .. code-block:: python

    AssertionError: '5:46:00' != '05:46'

* I change ``test_duration_w_hours_and_minutes`` to match the new timestamp format and notice that it is the same exact same test as ``test_duration_w_date_and_time`` so I remove it
* and add dates to ``test_duration_w_earlier_wake_than_sleep_time``

  .. code-block:: python

    def test_duration_w_earlier_wake_than_sleep_time(self):
        wake_time = '21/12/12 01:00'
        sleep_time = '21/12/12 02:00'

        with self.assertRaisesRegex(
            ValueError,
            f'wake_time: {wake_time} is earlier '
            f'than sleep_time: {sleep_time}'
        ):
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            )

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: ValueError not raised

  the new ``duration`` function is missing the condition for when ``wake_time`` is earlier than ``sleep_time`` so it did not raise the ValueError_ in ``test_duration_w_earlier_wake_than_sleep_time``

* When I add the condition

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_datetime = get_datetime_object(wake_time)
        sleep_datetime = get_datetime_object(sleep_time)

        if wake_datetime < sleep_datetime:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
        else:
            difference = (
                wake_datetime
              - sleep_datetime
            )

            return str(difference)

  the terminal shows random :ref:`AssertionErrors<AssertionError>` ``test_duration_w_date_and_time`` when ``wake_time`` is earlier than ``sleep_time`` that look like this

  .. code-block:: python

    AssertionError: '8:50:00' != '08:50'
    AssertionError: '7:00:00' != '09:09'
    AssertionError: '-1 day, 20:36:00' != '-1:52'
    AssertionError: '9:42:00' != '19:34'

  the test is still using the total minutes calculations so we have different formats and results

* I make ``test_duration_w_date_and_time`` use `datetime.datetime`_ objects for the calculations and remove unused variables

  .. code-block:: python

        def test_duration_w_date_and_time(self):
        wake_hour = random_hour()
        wake_minutes = random_minutes()
        wake_time = f'31/12/99 {wake_hour}:{wake_minutes:02}'

        sleep_hour = random_hour()
        sleep_minutes = random_minutes()
        sleep_time = f'31/12/99 {sleep_hour}:{sleep_minutes:02}'

        pattern = '%d/%m/%y %H:%M'
        difference = (
            datetime.datetime.strptime(
                wake_time, pattern
            )
          - datetime.datetime.strptime(
                sleep_time, pattern
            )
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
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            ):
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )

  the terminal shows passing tests and I no longer have random failures, things are green all the way

.. _test_duration_w_date_and_time_refactor:

refactor: make it better
--------------------------------------------------------

* I remove ``wake_hour``, ``wake_minutes``, ``sleep_hour`` and ``sleep_minutes`` and replace them with calls to ``random_hour`` and ``random_minutes`` since they are declared and only used once

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        wake_time = f'31/12/99 {random_hour()}:{random_minutes():02}'
        sleep_time = f'31/12/99 {random_hour()}:{random_minutes():02}'

        pattern = '%d/%m/%y %H:%M'
        difference = (
            datetime.datetime.strptime(
                wake_time, pattern
            )
          - datetime.datetime.strptime(
                sleep_time, pattern
            )
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
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            ):
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )

* then I create a :ref:`function<functions>` to create random timestamps for a given date

  .. code-block:: python

    def random_hour():
    ...

    def random_minutes():
    ...

    def get_random_timestamp(date):
        return f'{date} {random_hour():02}:{random_minutes():02}'

  and call it in ``test_duration_w_date_and_time``

  .. code-block:: python

    def test_duration_w_date_and_time(self):
        wake_time = get_random_timestamp('31/12/99')
        sleep_time = get_random_timestamp('31/12/99')

        pattern = '%d/%m/%y %H:%M'
        difference = (
            datetime.datetime.strptime(
                wake_time, pattern
            )
          - datetime.datetime.strptime(
                sleep_time, pattern
            )
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
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            ):
                sleep_duration.duration(
                    wake_time=wake_time,
                    sleep_time=sleep_time
                )

* I call ``random.randint`` directly in ``get_random_timestamp``

  .. code-block:: python

    def get_random_timestamp(date):
        return f'{date} {random.randint(0, 23):02}:{random.randint(0, 59):02}'

  which allows me to remove ``random_hour`` and ``random_minutes`` since they are no longer called by anyone

* I remove ``duration_a`` from ``sleep_duration.py`` because ``duration`` is a better solution
* I remove ``get_total_minutes`` and ``parse_timestamp`` because they are no longer called by anyone
* and I remove the ``difference`` variable from ``duration`` since it is only used once. I can do the calculation directly

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_datetime = get_datetime_object(wake_time)
        sleep_datetime = get_datetime_object(sleep_time)

        if wake_datetime < sleep_datetime:
            raise ValueError(
                f'wake_time: {wake_time} is earlier '
                f'than sleep_time: {sleep_time}'
            )
        else:
            return str(wake_datetime-sleep_datetime)

  and we are still green all the way

.. _sleep_duration_review:

review
========================================================

The challenge was to create a :ref:`function<functions>` that calculates the difference between 2 given timestamps. I ran the following tests to help me create it

* `test_string_attributes_and_methods`_
* `test_string_splitting`_ where I

  - used the `help system`_ to view documentation
  - used the `str.split`_ :ref:`method<functions>` to split a string_ on a separator
  - indexed the :doc:`list </data_structures/lists/lists>` from the split to get specific items

* `test_converting_strings_to_integers`_
* `test_floor_aka_integer_division`_
* `test_modulo_operation`_
* `test_datetime_objects`_ where I

  - used the `python online documentation`_
  - converted a string_ to a `datetime.datetime`_ object using the `datetime.datetime.strptime`_ :ref:`method<functions>`

* `test_subtracting_datetime_objects`_
* `test_converting_timedelta_to_string`_
* `test_duration_w_earlier_wake_than_sleep_time`_
* `test_duration_w_date_and_time`_

  - using `random.randint`_ to generate random integers for hours and minutes
  - using timestamps with dates, and times ranging from ``'00:00'`` up to and including ``'23:59'`` as inputs for ``wake_time`` and ``sleep_time``
  - confirming a ValueError_ is raised when ``wake_time`` is earlier than ``sleep_time``
  - `test_duration_w_hours`_
  - `test_duration_w_hours_and_minutes`_
  - `test_duration_calculation`_

I also encountered the following exceptions

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`
* SyntaxError_
* ValueError_

----

:doc:`/code/code_sleep_duration`
