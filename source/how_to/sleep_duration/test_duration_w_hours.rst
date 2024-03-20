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
        return (wake_time, sleep_time)

  and the test passes, Green is a beautiful color!

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

  I get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ('09:00', '07:00') != ('08:00', '07:00')

  when I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time='09:00',
            sleep_time='07:00'
        ),
        ('09:00', '07:00')
    )

  the test passes

* the same thing happens if I change ``sleep_time``

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time='09:00',
            sleep_time='06:00'
        ),
        ('09:00', '07:00')
    )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ('09:00', '06:00') != ('09:00', '07:00')

  when I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        sleep_duration.duration(
            wake_time='09:00',
            sleep_time='06:00'
        ),
        ('09:00', '06:00')
    )

  the test passes, the ``duration`` :ref:`function<functions>` is returning what it gets as inputs
* I add variables to the test to avoid the repetition when I make changes to ``wake_time`` and ``sleep_time``

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

  the timestamps are strings and I cannot subtract one string_ from another

.. _test_string_attributes_and_methods:

test_string_attributes_and_methods
#############################################################################

I want to get the first two characters of ``wake_time`` and ``sleep_time`` which are the hours

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

  I get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: ['__add__', '__class__', '__contains__', [934 chars]ill'] != None

.. _test_string_attributes_and_methods_green:

green: make it pass
-----------------------------------------------------------------------------

* I copy the values from the left side of the comparison and paste to replace :ref:`None` in the test

  .. code-block:: python

    def test_string_attributes_and_methods(self):
        self.assertEqual(
            dir('00:00'),
            ['__add__', '__class__', '__contains__', [934 chars]ill']
        )

  the terminal shows a SyntaxError_

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

* there is a closing quote without an opening one, I add it since :ref:`quotes come in pairs<conventions_enclosures>`

  .. code-block:: python

    def test_string_attributes_and_methods(self):
        self.assertEqual(
            dir('00:00'),
            ['__add__', '__class__', '__contains__', '[934 chars]ill']
        )

  the terminal shows an :ref:`AssertionError` with a different message and a suggestion

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

  - and the terminal shows the full list of :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of a string_
  - `unittest.TestCase.maxDiff`_ sets a limit on the number of characters the terminal shows for a difference between two objects. There is no limit when it is set to :ref:`None`

* I copy and paste the values from the terminal into the test, and remove the extra characters - ``'E       -  '`` using find and replace - ``ctrl+h`` (windows/linux) or ``command+option+f`` (mac)

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
* I want to try one of the :ref:`methods<functions>` listed in ``test_string_attributes_and_methods`` to see if it will get me closer to a solution, but I cannot tell what they do by the names alone. I will use the `help system`_ to get more details

  .. code-block:: python

    def test_string_attributes_and_methods(self):
        ...
        self.assertEqual(help(str))

  the terminal shows `python documentation for strings`_ and I read the descriptions for each :ref:`method<functions>` until I see one that looks like it could solve the problem

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

.. _test_string_splitting_red:

red: make it fail
-----------------------------------------------------------------------------

I remove ``self.assertEqual(help(str))`` then add a failing test for the `str.split`_ :ref:`method<functions>` to see what it does

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

and we are green again

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

  and the terminal shows an :ref:`AssertionError`

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

* I comment out the `unittest.skip decorator`_ for ``test_duration_w_hours`` by hitting ``ctrl+/`` (windows/linux) or ``command+/`` (mac)

  .. code-block:: python

    # @unittest.skip
    def test_duration_w_hours(self):
    ...

* then add calls to the `str.split`_ :ref:`method<functions>` in the calculation

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

  I cannot subtract one :doc:`list </data_structures/lists/lists>` from another

.. _test_string_splitting_refactor_red:

red: make it fail
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* I want the hours part of the timestamp which is the first item of the list from splitting the timestamp string_. I can get it by using its index as covered in :doc:`/data_structures/lists/lists`. Python uses `zero-based indexing`_ which means the first item is at index ``0`` and the second item is at index ``1``
* I remove the comment from the `unittest.skip decorator`_ to disable ``test_duration_w_hours`` by hitting ``ctrl+/`` (windows/linux) or ``command+/`` (mac)

  .. code-block:: python

    @unittest.skip
    def test_duration_w_hours(self):
    ...

* then add a variable and an assertion to ``test_string_splitting`` for getting specific parts of the :doc:`list </data_structures/lists/lists>` from calling `str.split`_

  .. code-block:: python

    def test_string_splitting(self):
        split = '01:23'.split(':')

        self.assertEqual(
            split,
            ['01', '23']
        )
        self.assertEqual(split[0], 0)

  the terminal shows an :ref:`AssertionError` because the first item (index 0) from splitting ``'01:23'`` on the separator ``':'`` is ``'01'`` which is the hours part of the timestamp

  .. code-block:: python

    AssertionError: '01' != 0

.. _test_string_splitting_refactor_green:

green: make it pass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* I change the value in the test to ``'01'``

  .. code-block:: python

    self.assertEqual(split[0], '01')

  and the test passes

.. _test_string_splitting_refactor_refactor:

refactor: make it better
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

----

.. _test_duration_w_hours_refactor_1:

* I comment out the `unittest.skip decorator`_ for ``test_duration_w_hours``  to bring me back to the unsolved :ref:`TypeError` by hitting ``ctrl+/`` (windows/linux) or ``command+/`` (mac)

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

  and get a :ref:`TypeError` for once again trying to subtract one string_ from another

.. _test_converting_strings_to_integers:

test_converting_strings_to_integers
#############################################################################

I want to see if I can use the int_ constructor to convert a string_ to an integer_ for the calculation

.. _test_converting_strings_to_integers_red:

red: make it fail
-----------------------------------------------------------------------------

* I remove the comment from the `unittest.skip decorator`_ to disable the current failing test by hitting ``ctrl+/`` (windows/linux) or ``command+/`` (mac)

  .. code-block:: python

    @unittest.skip
    def test_duration_w_hours(self):
    ...

* then add a new failing test to test hours less than 10 than have a 0 in front of them

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

.. _test_converting_strings_to_integers_refactor:

refactor: make it pass
-----------------------------------------------------------------------------

* I add another assertion to test numbers greater than ``9``

  .. code-block:: python

    self.assertEqual(int('12'), 1)

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 12 != 1

* I change the number from ``1`` to ``12``

  .. code-block:: python

    self.assertEqual(int('12'), 12)

  and we are green again

----

.. _test_duration_w_hours_refactor_2:

* I comment out the `unittest.skip decorator`_ for ``test_duration_w_hours``  to bring me back to the unsolved :ref:`TypeError` by hitting ``ctrl+/`` (windows/linux) or ``command+/`` (mac)

  .. code-block:: python

    # @unittest.skip
    def test_duration_w_hours(self):
    ...

* then add calls to the int_ constructor as part of the calculation in the test

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

    AssertionError: ('09:00', '06:00') != 3

  when I change ``wake_time`` to a different value

  .. code-block:: python

    # @unittest.skip
    def test_duration_w_hours(self):
        wake_time = '10:00'
        sleep_time = '06:00'

  I get an :ref:`AssertionError` where the values change on both sides

  .. code-block:: python

    AssertionError: ('10:00', '06:00') != 4

  the same thing happens when I change ``sleep_time``

  .. code-block:: python

    # @unittest.skip
    def test_duration_w_hours(self):
        wake_time = '10:00'
        sleep_time = '05:00'

  an :ref:`AssertionError` where the values change on both sides

  .. code-block:: python

    AssertionError: ('10:00', '05:00') != 5

  the ``duration`` :ref:`function<functions>` returns its inputs but the test now expects the difference between the hours

* I take what I learned from the tests to make it match the expectation

  .. code-block:: python

    def duration(wake_time=None, sleep_time=None):
        return (
            int(wake_time.split(':')[0])
          - int(sleep_time.split(':')[0])
        )

  and the terminal shows passing tests! Celebration Time!!

* to avoid changing the values of ``wake_time`` and ``sleep_time`` in the tests when I have an idea, I make sure the function is tested with random numbers by adding an `import statement`_ for the random_ :doc:`module </exceptions/ModuleNotFoundError>` to ``test_sleep_duration.py``

  .. code-block:: python

    import random
    import sleep_duration
    import unittest

  then I add variables to the test for random hours in a day

  .. code-block:: python

    # @unittest.skip
    def test_duration_w_hours(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)

        wake_time='11:00'
        sleep_time='04:00'
    ...

  `random.randint`_ will give me a random integer_ from ``0`` up to and including ``23`` to represent the 24 hours in a day

* I add an assertion to see what values I get from `random.randint`_

  .. code-block:: python

    # @unittest.skip
    def test_duration_w_hours(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)
        self.assertEqual(wake_hour, sleep_hour)

  and get an :ref:`AssertionError` that looks like

  .. code-block:: python

    AssertionError: 9 != 7
    AssertionError: 16 != 3
    AssertionError: 3 != 6
    AssertionError: 20 != 8

  since the numbers are random the test will sometimes pass when ``wake_hour`` and ``sleep_hour`` are the same

* I remove the assertion after confirming that ``wake_hour`` and ``sleep_hour`` are random integers_
* then I :doc:`interpolate </how_to/pass_values>` them as hours for ``wake_time`` and ``sleep_time``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_hour = random.randint(0, 23)
        sleep_hour = random.randint(0, 23)

        wake_time=f'{wake_hour:02}:00'
        sleep_time=f'{sleep_hour:02}:00'
    ...

  ``:02`` in ``{wake_hour:02}`` and ``{sleep_hour:02}`` tell Python to always display two characters for the numbers, with a leading zero when it is one digit. For example, display ``01`` instead of ``1``

* I add an assertion to check that ``wake_time`` and ``sleep_time`` look correct and are still random

  .. code-block:: python

    wake_time=f'{wake_hour:02}:00'
    sleep_time=f'{sleep_hour:02}:00'
    self.assertEqual(wake_time, sleep_time)

  and the terminal shows an :ref:`AssertionError` that looks like

  .. code-block:: python

    AssertionError: '20:00' != '02:00'
    AssertionError: '12:00' != '13:00'
    AssertionError: '08:00' != '11:00'
    AssertionError: '10:00' != '17:00'

* I add a :ref:`function<functions>` to return random hours because ``wake_hour`` and ``sleep_hour`` both use the same call to `random.randint`_

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
    ...

  and confirm in the terminal that ``wake_time`` and ``sleep_time`` still look right

* I can also call ``random_hour`` directly instead of using the reference to the variables since they are only used once

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_time = f'{random_hour():02}:00'
        sleep_time = f'{random_hour():02}:00'
        self.assertEqual(wake_time, sleep_time)
    ...

  and the assertion still confirms that the values for ``wake_time`` and ``sleep_time`` look right

* the assignments for ``wake_time`` and ``sleep_time`` look the same, time to create a function that returns a random timestamp

  .. code-block:: python

    def random_hour():
        return random.randint(0, 23)

    def random_timestamp():
        return f'{random_hour():02}:00'

  and replace the timestamps with calls to ``random_timestamp``

  .. code-block:: python

    def test_duration_w_hours(self):
        wake_time = random_timestamp()
        sleep_time = random_timestamp()
        self.assertEqual(wake_time, sleep_time)
    ...

* since the values for ``wake_time`` and ``sleep_time`` look right, I remove ``self.assertEqual(wake_time, sleep_time)`` and the terminal shows passing tests
* I remove the `unittest.skip decorator`_
* then add a function to get the hours part of a given timestamp since that is all that changes in the solution in ``sleep_duration.py``

  .. code-block:: python

    def process(timestamp):
        return int(timestamp.split(':')[0])

  then call it in ``duration``

  .. code-block:: python

    def duration(wake_time=None, sleep_time):
        return (
            process(wake_time)
          - process(sleep_time)
        )

* since the tests are still passing I rename ``process`` to something more descriptive

  .. code-block:: python

    def get_hour(timestamp):
        return int(timestamp.split(':')[0])

    def duration(wake_time=None, sleep_time):
        return (
            get_hour(wake_time)
          - get_hour(sleep_time)
        )

  and the terminal still shows passing tests!

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

* `test_converting_strings_to_integers`_ with the int_ constructor
* and `test_duration_w_hours`_ where I

  - used `random.randint`_ to generate random integers for the 24 hours in a day
  - then :doc:`interpolated </how_to/pass_values>` the random hours into the timestamps to test the ``duration`` :ref:`function<functions>`
  - and test that it subtracts the hour for ``sleep_time`` from the hour for ``wake_time``

I also encountered the following exceptions

* :ref:`AssertionError`
* :ref:`TypeError`
* NameError_
* :ref:`AttributeError`
* SyntaxError_

Would you like to :ref:`test duration with hours and minutes<test_duration_w_hours_and_minutes>`?

----

:doc:`/code/code_sleep_duration`