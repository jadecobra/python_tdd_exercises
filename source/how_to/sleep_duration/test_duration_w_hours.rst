.. include:: ../links.rst

########################################################
test_duration_w_hours
########################################################

In this chapter, I take a look at building a program that returns the duration between a given sleep and wake time.

----

.. _test_duration_w_hours_red:

********************************************************
red: make it fail
********************************************************

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

* and I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_sleep_duration.py:7`` with the mouse to open it
* then I make ``test_failure`` pass
* and replace it pass with a failing test that expects ``1`` when the ``duration`` :ref:`function<functions>` in the ``sleep_duration`` :doc:`module </exceptions/ModuleNotFoundError>` is called with a ``wake_time`` of ``'08:00'`` and ``sleep_time`` of ``'07:00'`` which in this case is the difference between the two

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

********************************************************
green: make it pass
********************************************************

* which I add to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

* then I add an `import statement`_ at the top of the file

  .. code-block:: python

    import sleep_duration
    import unittest


    class TestSleepDuration(unittest.TestCase):
    ...

  and the terminal shows an :ref:`AttributeError` because ``sleep_duration.py`` has no definition for ``duration``

  .. code-block:: python

    AttributeError: module 'sleep_duration' has no attribute 'duration'

* I add it to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* and then open ``sleep_duration.py`` to add a name ::

    duration

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'duration' is not defined

* so I define it by assigning it to :ref:`None`

  .. code-block:: python

    duration = None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I add that to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* then make ``duration`` a :ref:`function<functions>` to make it callable_

  .. code-block:: python

    def duration():
        return None

  the terminal shows a :ref:`TypeError` with a different message about the first keyword argument given in the test

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'wake_time'

  ``test_duration_w_hours`` passes values with keyword arguments for ``wake_time`` and ``sleep_time`` when it calls the ``duration`` :ref:`function<functions>` which does not yet have these keyword arguments in its signature

* When I add the required keyword argument and set its default value to :ref:`None`

  .. code-block:: python

    def duration(wake_time=None):
        return None

  the terminal shows a :ref:`TypeError` for the next keyword argument

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'sleep_time'

* I add the keyword argument, setting the default value to :ref:`None`

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return None

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 1

  the ``duration`` :ref:`function<functions>` returns :ref:`None` but ``test_duration_w_hours`` expects ``1`` as the result

* I make the return value for ``duration`` match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return 1

  and the test passes. We are green.

.. _test_duration_w_hours_refactor_0:

********************************************************
refactor: make it better
********************************************************

The ``duration`` :ref:`function<functions>` currently returns ``1`` even when its inputs change. For it to meet the requirements it has to calculate the difference between ``wake_time`` and ``sleep_time``. I will add variables with random integers_ to cover all timestamps from ``'00:00'`` to ``'23:59'``

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

  - ``random.randint(0, 23)`` will give me a random integer_ from ``0`` up to and including ``23``
  - ``f'{wake_hour:02}:00'`` and ``f'{sleep_hour:02}:00'`` :doc:`interpolate </how_to/pass_values>` the random integers_ in the input strings_
  - the ``:02`` in ``{wake_hour:02}`` and ``{sleep_hour:02}`` tells Python to display the numbers as two digits. For example, display ``01`` instead of ``1``

* When I make the test expect the difference between ``wake_hour`` and ``sleep_hour``

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

  I get an :ref:`AssertionError` that looks like this

  .. code-block:: python

    AssertionError: 1 != -2
    AssertionError: 1 != 3
    AssertionError: 1 != -8
    AssertionError: 1 != 4

  the ``duration`` :ref:`function<function>` returns ``1`` but the test expects the subtraction of ``sleep_hour`` from ``wake_hour``

* I make the ``duration`` :ref:`function<functions>` return the subtraction of ``sleep_time`` from ``wake_time``

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return wake_time - sleep_time

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

  because Python does not have an operation defined for subtracting one string_ from another. I need a way to convert a timestamp from a string_ to an integer_.

test_string_attributes_and_methods
########################################################

The ``wake_time`` and ``sleep_time`` are currently in this format - ``XX:00`` where ``XX`` is the hours. I can calculate the difference if I can get the first 2 characters and convert them to numbers since Python can do :doc:`arithmetic </how_to/calculator>`.

.. _test_string_attributes_and_methods_red:

red: make it fail
--------------------------------------------------------

* I disable ``test_duration_w_hours`` by adding the `unittest.skip decorator`_

  .. code-block:: python

    @unittest.skip
    def test_duration_w_hours(self):
    ...

* then I add ``test_string_attributes_and_methods`` where I use the dir_ :ref:`function<functions>` to see the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of strings_, maybe that will help me find a way to break them apart or get the characters I want

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
--------------------------------------------------------

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

* it looks like there is a closing quote without an opening one, so I add it, quotes come in pairs

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
* I want to try one of the :ref:`methods<functions>` listed in ``test_string_attributes_and_methods`` to see if it will get me closer to a solution, but I cannot tell what they do by the names alone. I need more details so I use the `help system`_ to show me the `python documentation for strings`_

  .. code-block:: python

    def test_string_attributes_and_methods(self):
        ...
        self.assertEqual(help(str))

  the terminal shows documentation for the string_ module and I read the descriptions for each :ref:`method<functions>` until I see one that looks like it could solve the problem

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
########################################################

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

the terminal shows an :ref:`AssertionError`

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

and we are green again

.. _test_string_splitting_refactor:

refactor: make it better
--------------------------------------------------------

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

* and the :ref:`documentation<python documentation for strings>` said `str.split`_ takes in ``sep=None, maxsplit=-1`` as inputs and ``sep`` is the separator. When I pass in ``':'`` as the separator

  .. code-block:: python

    def test_string_splitting(self):
        self.assertEqual(
            '01:23'.split(':'),
            ['01', '23']
        )

  the test passes. I now know how to get the different parts of ``wake_time`` and ``sleep_time``

* I remove the `unittest.skip decorator`_ from ``test_duration_w_hours`` and then add calls to the `str.split`_ :ref:`method<functions>` in the ``duration`` :ref:`function<functions>` in ``sleep_duration.py``

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* I want to get the first item of the list created from splitting the timestamp string_, which I can get by using its index. Python uses `zero-based indexing`_ which means the first item is at index ``0`` and the second item is at index ``1``. See :doc:`/data_structures/lists/lists` for more. I add tests to ``test_string_splitting`` for getting specific parts of a :doc:`list </data_structures/lists/lists>` created from calling `str.split`_

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

.. test_string_splitting_green_1:

green: make it pass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* I change the value in the test to ``12``

  .. code-block:: python

    self.assertEqual(
        '12:34'.split(':')[0],
        '12'
    )

  and the terminal shows another :ref:`AssertionError` for the next line

  .. code-block:: python

    AssertionError: '34' != 0

  showing that the second item (index 1) from splitting ``'12:34'`` on the separator ``':'`` is ``'34'``

* I change that to ``34``

  .. code-block:: python

    self.assertEqual(
        '12:34'.split(':')[1],
        '34'
    )

  the test passes, bringing me back to the unsolved :ref:`TypeError` for the ``test_duration_w_hours``

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
########################################################

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

so I change the number from ``0`` to ``12``

.. code-block:: python

  self.assertEqual(int('12'), 12)

the terminal shows an :ref:`AssertionError` for the next one

.. code-block:: python

  AssertionError: 1 != 0

and I change the expectation to ``1``

.. code-block:: python

  self.assertEqual(int('01'), 1)

the terminal shows passings tests. I have another tool to help solve the problem

- I can split a string_ on a separator using `str.split`_ to get a :doc:`list </data_structures/lists/lists>` of its parts
- I can index the :doc:`list </data_structures/lists/lists>`  from splitting the string_ to get a specific item from it
- I can convert a string_ to an integer_ using the int_ constructor

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

  YES! it does, the terminal shows passing tests! The ``duration`` :ref:`function<functions>` calculates the duration between any given random sleep and wake hours in a day

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

* we are still green so I can try the same thing for ``sleep_time``

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

  - it splits the timestamp string_ on the separator ``':'``
  - it gets the first item from the split
  - then it converts the first item from the split to an integer_

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

  we are still green

* so I remove the parts of ``duration`` that are no longer used and rename ``process`` to something more descriptive like ``get_hour``

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

* I can also make ``get_hour`` use the same variable name instead of a new one for each step of the process

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

:doc:`/code/code_sleep_duration`