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
* and change ``True`` to ``False`` to make ``test_failure`` pass
* then replace the test with a new failing test

  .. code-block:: python

    def test_duration_w_hours(self):
        self.assertEqual(

        )

  and I get a :ref:`TypeError` in the terminal

  .. code-block:: python

    TypeError: TestCase.assertEqual() missing 2 required positional arguments: 'first' and 'second'

  ``assertEqual`` takes in two values to make a comparison

.. _test_duration_w_hours_green:

*****************************************************************************
green: make it pass
*****************************************************************************

* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError

* then add :ref:`None` as the first and second arguments to the assertion

  .. code-block:: python

    self.assertEqual(
        None,
        None
    )

  and the test passes

.. _test_duration_w_hours_refactor_0:

*****************************************************************************
refactor: make it better
*****************************************************************************

* I replace the first argument in the assertion with a reference to the ``sleep_duration`` :doc:`module </exceptions/ModuleNotFoundError>`

  .. code-block:: python

    self.assertEqual(
        sleep_duration,
        None
    )

  which gives me a NameError_

  .. code-block:: python

    NameError: name 'sleep_duration' is not defined

* so I add it as an exception encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # NameError

* when I add an `import statement`_ at the top of the file for the :doc:`module </exceptions/ModuleNotFoundError>`

  .. code-block:: python

    import sleep_duration
    import unittest


    class TestSleepDuration(unittest.TestCase):
    ...

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: <module 'sleep_duration' from '/workspace[46 chars].py'> != None

* so I add a reference to something in the ``sleep_duration`` :doc:`module </exceptions/ModuleNotFoundError>`

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration,
        None
    )

  and get an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'sleep_duration' has no attribute 'duration'

* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # NameError
    # AttributeError

* then open ``sleep_duration.py`` to add the name ::

    duration

  and get a NameError_ in the terminal

  .. code-block:: python

    NameError: name 'duration' is not defined

* I define it by assigning it to :ref:`None`

  .. code-block:: python

    duration = None

  and the test passes

* I add a call to ``duration`` in the test because I want it to accept inputs

  .. code-block:: python

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

  green again

* I want the ``duration`` :ref:`function<functions>` to take in a ``wake_time`` of ``08:00`` and add it to the test

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

* When I add the keyword argument to the signature and set its default value to :ref:`None`

  .. code-block:: python

    def duration(wake_time=None):
        return None

  the test passes

* I also want the ``duration`` :ref:`function<functions>` to take in a ``sleep_time`` of ``'07:00'``

  .. code-block:: python

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

  because ``sleep_time`` is not in its signature

* I add the second keyword argument, setting the default value to :ref:`None`

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return None

  and the test passes

* I set the expectation of the test to the inputs given

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

* the ``duration`` :ref:`function<functions>` currently returns :ref:`None` so I make it the inputs

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (wake_time, sleep_time)

  and the test passes, green again

* I add variables to the test to remove the repetition

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_time='08:00'
        sleep_time='07:00'

        self.assertEqual(
            sleep_duration.duration(
                wake_time=wake_time,
                sleep_time=sleep_time
            ),
            (wake_time, sleep_time)
        )

* then change the expectation of the test to ``wake_time-sleep_time``

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

  I cannot subtract one string_ from another

.. _test_string_attributes_and_methods:

test_string_attributes_and_methods
#############################################################################

I want to get the hours portion of the ``wake_time`` and ``sleep_time`` which are the first two characters

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
    # TypeError
    # NameError
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

* I copy and paste the values from the terminal into the test, and remove the extra characters - ``'E       -  '`` using find and replace - ``ctrl+h`` (windows/linux) ``command+option+f`` (mac)

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

.. _test_string_splitting:

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

and the terminal shows an :ref:`AssertionError`

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

* and the `documentation <python documentation for strings>`_ said `str.split`_ takes in ``sep=None, maxsplit=-1`` as inputs and ``sep`` is the separator. I want to see what happens when I pass in ``':'`` as the separator

  .. code-block:: python

    def test_string_splitting(self):
        self.assertEqual(
            '01:23'.split(':'),
            ['01', '23']
        )

  the test passes. I now know how to get the different parts of ``wake_time`` and ``sleep_time``

* I comment out the `unittest.skip decorator`_ for ``test_duration_w_hours`` by hitting ``ctrl+/`` (windows/linux) or ``command+/`` (mac)

  .. code-block:: python

    # @unittest.skip
    def test_duration_w_hours(self):
    ...

* then add calls to the `str.split`_ :ref:`method<functions>`

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            wake_time.split(':')
            -sleep_time.split(':')
        )
    )

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'list' and 'list'

  this time for trying to subtract one :doc:`list </data_structures/lists/lists>` from another

.. _test_string_splitting_red_1:

red: make it fail
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* I want the first item of the list from splitting the timestamp string_, which I can get by using its index. Python uses `zero-based indexing`_ which means the first item is at index ``0`` and the second item is at index ``1``. See :doc:`/data_structures/lists/lists` for more.
* I uncomment the `unittest.skip decorator`_ to disable ``test_duration_w_hours``

  .. code-block:: python

    @unittest.skip
    def test_duration_w_hours(self):
    ...

* then add tests to ``test_string_splitting`` for getting specific parts of the :doc:`list </data_structures/lists/lists>` from calling `str.split`_

  .. code-block:: python

    def test_string_splitting(self):
        self.assertEqual(
            '01:23'.split(':'),
            ['01', '23']
        )

        split = '12:34'.split(':')
        self.assertEqual(split[0], 0)

  the terminal shows an :ref:`AssertionError` because the first item (index 0) from splitting ``'12:34'`` on the separator ``':'`` is ``'12'`` which is the hours part of the timestamp

  .. code-block:: python

    AssertionError: '12' != 0

.. test_string_splitting_green_1:

green: make it pass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* I change the value in the test to ``'12'``

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

* I change that to ``'34'``

  .. code-block:: python

    self.assertEqual(split[1], '34')

  and the test passes

* I comment out the `unittest.skip decorator`_ for ``test_duration_w_hours``  to bring me back to the unsolved :ref:`TypeError`

  .. code-block:: python

    # @unittest.skip
    def test_duration_w_hours(self):
    ...

* then update the expectation to the result of subtracting the first items of the list from splitting ``wake_time`` and ``sleep_time`` on the separator ``':'``

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time=wake_time,
            sleep_time=sleep_time
        ),
        (
            wake_time.split(':')[0]
            -sleep_time.split(':')[0]
        )
    )

  and get a :ref:`TypeError` for an unsupported operation of trying to subtract one string_ from another. I know from ``test_string_splitting`` that the strings being subtracted are just the hours portion, not the entire values of ``wake_time`` and ``sleep_time`` but they are still strings not numbers

.. _test_converting_strings_to_integers:

test_converting_strings_to_integers
#############################################################################

I want to see if I can use the int_ constructor to convert a string_ to an integer_

.. _test_converting_strings_to_integers_red:

red: make it fail
-----------------------------------------------------------------------------

* I uncomment the `unittest.skip decorator`_ to disable the current failing test

  .. code-block:: python

    @unittest.skip
    def test_duration_w_hours(self):
    ...

* then add a new failing test

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

* I change the expectation to ``1``

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

  we are green again

----

.. _test_duration_w_hours_refactor_1:

* I comment out the `unittest.skip decorator`_ for ``test_duration_w_hours``  to bring me back to the unsolved :ref:`TypeError`

  .. code-block:: python

    # @unittest.skip
    def test_duration_w_hours(self):
    ...

* and update the expectation to include calls to the int_ constructor

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

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: ('08:00', '07:00') != 1

  the ``duration`` :ref:`function<functions>` returns the inputs but the test now expects the difference

* I take what I have learned from the tests to make it match the expectation of returning the difference between the hours

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            int(wake_time.split(':')[0])
          - int(sleep_time.split(':')[0])
        )

  and the terminal shows passing tests! Celebration Time!!

* I want to make sure that the function is tested with random numbers, so I add an `import statement`_ for the random_ :doc:`module </exceptions/ModuleNotFoundError>` to ``test_sleep_duration.py``

  .. code-block:: python

    import random
    import sleep_duration
    import unittest

* then add variables for random hours in a day

  .. code-block:: python

    # @unittest.skip
    def test_duration_w_hours(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)

        wake_time='08:00'
        sleep_time='07:00'
    ...

  ``random.randint(0, 23)`` will give me a random integer_ from ``0`` up to and including ``23`` to represent the 24 hours in a day

* I :doc:`interpolate </how_to/pass_values>` these random integers_ in the input strings_ for ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)

        wake_time=f'{wake_hour:02}:00'
        sleep_time=f'{sleep_hour:02}:00'
    ...

  the terminal still shows passing tests. The ``:02`` in ``{wake_hour:02}`` and ``{sleep_hour:02}`` tell Python to always display two characters for the numbers, with a leading zero when it is one digit. For example, display ``01`` instead of ``1``

* then add a :ref:`function<functions>` that makes random hours

  .. code-block:: python

    import random
    import sleep_duration
    import unittest

    def random_hour():
        return random.randint(0, 23)


    class TestSleepDuration(unittest.TestCase):
    ...

  and call it in ``test_duration_w_hours``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random_hour()
        sleep_hour = random_hour()
    ...

  the terminal still shows passing tests
* I remove the `unittest.skip decorator`_
* Since all the tests are passing I can rewrite the solution in ``sleep_duration.py`` as steps by using variables

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_hour_integer = int(wake_time.split(':')[0])

        return (
            wake_hour_integer,
            int(sleep_time.split(':')[0])
        )

  still green so I will do the same for sleep_time

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_hour_integer = int(wake_time.split(':')[0])
        sleep_hour_integer = int(sleep_time.split(':')[0])

        return (
            wake_hour_integer
          - sleep_hour_integer
        )

  all tests are still passing

* I can break the variables down further

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_hour = wake_time.split(':')[0]
        wake_hour_integer = int(wake_hour)

        sleep_hour = sleep_time.split(':')[0]
        sleep_hour_integer = int(sleep_hour)
    ...

* one more time

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        wake_time_split = wake_time.split(':')
        wake_hour = wake_time_split[0]
        wake_hour_integer = int(wake_hour)

        sleep_time_split = sleep_time.split(':')
        sleep_hour = sleep_time_split[0]
        sleep_hour_integer = int(sleep_hour)
    ...

  and the terminal still shows passing tests

* I can also make these steps a separate :ref:`function<functions>` that is called for ``wake_time`` and ``sleep_time`` to remove the repetition since the only thing that is different are the timestamps

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

  still green

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

* which means I can play around and do things like make ``get_hour`` use the same variable instead of a new one for each step of the process

  .. code-block:: python

    def get_hour(timestamp):
        value = timestamp.split(':')
        value = value[0]
        value = int(value)
        return value

  or change it to use one line, though it might not be as easy to understand

  .. code-block:: python

    def get_hour(timestamp):
        return int(timestamp.split(':')[0])

  and the terminal still shows passing tests

----

.. _test_duration_w_hours_review:

*****************************************************************************
review
*****************************************************************************

The challenge is to write a program that calculates the difference between a given sleep and wake time. I ran the following tests to get something that comes close to doing it

* `test_string_attributes_and_methods`_ where

  - I used the dir_ :ref:`function<functions>`
  - and `help system`_ to find the `str.split`_ :ref:`method<functions>`

* `test_string_splitting`_ where I

  - used the `str.split`_ :ref:`method<functions>` to split a string_ on a separator
  - and indexed the :doc:`list </data_structures/lists/lists>` from the split to get specific items

* `test_converting_strings_to_integers`_ where I used the int_ constructor
* and `test_duration_w_hours`_ where I used

  - `random.randint`_ to generate random integers for hours
  - and :doc:`interpolation </how_to/pass_values>` to test the functions with random hours

I also encountered the following exceptions

* :ref:`AssertionError`
* :ref:`TypeError`
* NameError_
* :ref:`AttributeError`
* SyntaxError_

Would you like to :ref:`test duration with hours and minutes<test_duration_w_hours_and_minutes>`?

----

:doc:`/code/code_sleep_duration`