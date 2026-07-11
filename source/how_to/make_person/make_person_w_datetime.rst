.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): test person with datetime — fix the person project's hardcoded 2026 age so say_hello stays correct every year. Open person; uv run pytest-watcher . --now (6 passed from unittest chapter). Explore the datetime module with test_dir_datetime → NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?; import datetime; paste dir(datetime) as my_expectation (MAXYEAR, date, datetime, timedelta, …; list may differ by Python version). Drill datetime.date, self.maxDiff = None, TypeError: function missing required argument 'year', then datetime.date.today().year. Replace f' {2026-year_of_birth}.' with datetime.date.today().year-year_of_birth in test_joe/jane/john/mary. Extract this_year class attribute, then calculate_age method: TypeError takes 1 positional argument but 2 were given (need self); @staticmethod then remove self. Port calculate_age to person.py (import datetime; NameError if forgotten). Assert age <= 120 (john 1580 → AssertionError; change to 1980). Assert isinstance(year_of_birth, int); optional year_of_birth=None; bool is an int so False skips the isinstance guard and fails the age bound; float/str/tuple fail. Review: datetime for current year; bare asserts stop the test so cases are commented out — need a better way to test exceptions. Catalog: test_person_w_datetime.py + person_w_datetime.py.
  :keywords: Jacob Itegboje, Pumping Python, test person with datetime, person project hardcoded 2026 age, datetime module, import datetime, NameError name 'datetime' is not defined, Did you forget to import 'datetime', dir(datetime), datetime.date, datetime.date.today().year, self.maxDiff = None, TypeError function missing required argument 'year', TypeError calculate_age takes 1 positional argument but 2 were given, @staticmethod, extract this_year, extract calculate_age, assert age <= 120, john smith year_of_birth 1580, year_of_birth 1980, isinstance year_of_birth int, boolean is also an integer, year_of_birth=None, TypeError unsupported operand type(s) for - 'int' and 'NoneType', test_when_year_of_birth_is_not_integer, uv run pytest-watcher . --now, red green refactor, remove the commented lines, git commit -am, person say_hello age calculation, test_person_w_datetime, person_w_datetime

.. include:: ../../links.rst

.. _datetime: https://docs.python.org/3/library/datetime.html?highlight=time%20difference#module-datetime
.. _datetime module: datetime_
.. _datetime.datetime: https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime-objects
.. _datetime.datetime object: `datetime.datetime`_
.. _datetime object: `datetime.datetime`_
.. _datetime.datetime.strptime: https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime.strptime
.. _datetime.timedelta: https://docs.python.org/3/library/datetime.html?highlight=datetime#timedelta-objects
.. _now: https://docs.python.org/3/library/datetime.html#datetime.datetime.now
.. _now method: now_
.. _today: https://docs.python.org/3/library/datetime.html#datetime.date.today
.. _today method: today_


#################################################################################
test person with datetime
#################################################################################

----

The :ref:`person<test person with unittest>` project has a problem with the calculation of the ages. It only shows the right age if the program is run in ``2026``, because the year is hardcoded. If I run it in a different year or change the year on my computer, the ages will be wrong and the tests for :ref:`say_hello<test say_hello method>` will fail.

I want the calculation to always be right, which means the program should always know the correct year.

I can use the `datetime module`_ from `The Python Standard Library`_. You can think of it as a toolbox with different tools I can use to do things with dates and times. I can also use :ref:`assertions<what is an assertion?>` to make sure I get the right year of birth for the calculations.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_datetime.py
  :language: python
  :linenos:

-----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd person

* I open ``test_person.py`` from the ``tests`` folder_

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    tests/test_person.py ......                         [100%]

    =================== 6 passed in M.NOs ====================

----

*********************************************************************************
test_dir_datetime
*********************************************************************************

I want to see what comes with the `datetime module`_.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add :ref:`test_dir_datetime` to ``test_person.py``

  .. code-block:: python
    :lineno-start: 262
    :emphasize-lines: 3-6

            self.assertEqual(reality, my_expectation)

        def test_dir_datetime(self):
            reality = dir(datetime)
            my_expectation = []
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'datetime' is not defined.
               Did you forget to import 'datetime'?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ for `datetime`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import datetime
    import src.person
    import unittest


    class TestPerson(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        Lists differ: [
            'MAXYEAR', 'MINYEAR', 'UTC',
            '__all__', '[179 chars]nfo'
        ] != []

  it also shows the entire difference between the :ref:`lists<what is a list?>`

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_, paste (:kbd:`ctrl/command+v`) them as ``my_expectation`` and remove the extra characters

  .. code-block:: python
    :lineno-start: 263
    :emphasize-lines: 5-25
    :emphasize-text: datetime

            self.assertEqual(reality, my_expectation)

        def test_dir_datetime(self):
            reality = dir(datetime)
            my_expectation = [
                'MAXYEAR',
                'MINYEAR',
                'UTC',
                '__all__',
                '__builtins__',
                '__cached__',
                '__doc__',
                '__file__',
                '__loader__',
                '__name__',
                '__package__',
                '__spec__',
                'date',
                'datetime',
                'datetime_CAPI',
                'time',
                'timedelta',
                'timezone',
                'tzinfo'
            ]
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes because when ``import datetime`` runs, Python_ brings in an :ref:`object (everything in Python is an object)<everything is an object>` for the `datetime module`_ from `The Python Standard Library`_ so I can use it in ``test_person.py`` as ``datetime``.

  This means that there is a file_ or folder_ on the computer named ``datetime`` that got added when I installed Python_.

  .. caution:: Your list of attributes and methods may be different depending on your Python version

----

*********************************************************************************
test_dir_datetime_date
*********************************************************************************

A few names stand out in the :ref:`list of attributes and methods of datetime<test_dir_datetime>`

* ``date`` - I assume this handles dates
* ``time`` - I assume this handles time
* ``datetime`` - I assume a combination of date and time

What I want is something that will give me the current year.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add :ref:`test_dir_datetime_date` to ``test_person.py``

.. code-block:: python
  :lineno-start: 288
  :emphasize-lines: 3-6

          self.assertEqual(reality, my_expectation)

      def test_dir_datetime_date(self):
          reality = dir(datetime.date)
          my_expectation = []
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError:
      Lists differ: [
          '__add__', '__class__', '__delattr__',
          '_[585 chars]ear'
      ] != []

with a message about how to see the entire difference

.. code-block:: python

  Diff is 787 characters long.
  Set self.maxDiff to None to see it.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I set `self.maxDiff`_ to :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 288
    :emphasize-lines: 6

            self.assertEqual(reality, my_expectation)

        def test_dir_datetime_date(self):
            reality = dir(datetime.date)
            my_expectation = []
            self.maxDiff = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  - The terminal_ shows the entire difference between ``reality`` and ``my_expectation``.
  - `maxDiff`_ is an :ref:`attribute<what causes AttributeError?>` of the :ref:`unittest.TestCase class<test_dir_unittest_testcase>` that sets the maximum number of characters to show when comparing 2 :ref:`objects<everything is an object>` in the terminal_, when it is set to :ref:`None<what is None?>` it shows the full difference.

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_, paste (:kbd:`ctrl/command+v`) them as ``my_expectation`` and remove the extra characters

  .. code-block:: python
    :lineno-start: 290
    :emphasize-lines: 3-21
    :emphasize-text: year today


        def test_dir_datetime_date(self):
            reality = dir(datetime.date)
            my_expectation = [
                '__add__', '__class__', '__delattr__',
                '__dir__', '__doc__', '__eq__',
                '__format__', '__ge__', '__getattribute__',
                '__getstate__', '__gt__', '__hash__',
                '__init__', '__init_subclass__', '__le__',
                '__lt__', '__ne__', '__new__', '__radd__',
                '__reduce__', '__reduce_ex__',
                '__replace__', '__repr__', '__rsub__',
                '__setattr__', '__sizeof__', '__str__',
                '__sub__', '__subclasshook__', 'ctime',
                'day', 'fromisocalendar', 'fromisoformat',
                'fromordinal', 'fromtimestamp',
                'isocalendar', 'isoformat', 'isoweekday',
                'max', 'min', 'month', 'replace',
                'resolution', 'strftime', 'strptime',
                'timetuple', 'today', 'toordinal',
                'weekday', 'year'
            ]
            self.maxDiff = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

----

*********************************************************************************
test_dir_datetime_date_year
*********************************************************************************

I see ``year`` in the :ref:`list of attributes and methods of datetime.date<test_dir_datetime_date>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the ``year`` :ref:`attribute<what is a class attribute?>` of the ``date`` :ref:`attribute<what is a class attribute?>` of the `datetime module`_ in ``test_person.py``

.. code-block:: python
  :lineno-start: 312
  :emphasize-lines: 3-6

          self.assertEqual(reality, my_expectation)

      def test_dir_datetime_date_year(self):
          reality = dir(datetime.date.year)
          my_expectation = []
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` with only :ref:`attributes<what is a class attribute?>` that start and end with double underscore (``__``)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the value of ``reality`` to ``datetime.date.year``

  .. code-block:: python
    :lineno-start: 314
    :emphasize-lines: 2-3

        def test_dir_datetime_date_year(self):
            # reality = dir(datetime.date.year)
            reality = datetime.date.year
            my_expectation = []
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <attribute 'year' of 'datetime.date' objects>
     != []

* I try :ref:`calling<how to call a function>` ``date``

  .. code-block:: python
    :lineno-start: 314
    :emphasize-lines: 3-4

        def test_dir_datetime_date_year(self):
            # reality = dir(datetime.date.year)
            # reality = datetime.date.year
            reality = datetime.date().year
            my_expectation = []
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function missing
               required argument 'year' (pos 1)

  I want something that automatically knows the date and gives me the year.

----

*********************************************************************************
test_dir_datetime_date_today
*********************************************************************************

I also saw ``today`` in the :ref:`list of attributes and methods of datetime.date<test_dir_datetime_date>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change :ref:`test_dir_datetime_date_year` to a test for the ``today`` :ref:`attribute<what is a class attribute?>` of the ``date`` :ref:`attribute<what is a class attribute?>` of the `datetime module`_ in ``test_person.py``

.. code-block:: python
  :lineno-start: 312
  :emphasize-lines: 3, 6-7

            self.assertEqual(reality, my_expectation)

        def test_dir_datetime_date_today(self):
            # reality = dir(datetime.date.year)
            # reality = datetime.date.year
            # reality = datetime.date().year
            reality = datetime.date.today
            my_expectation = []
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError:
      <built-in method today
       of type object at 0xffff0fab2345>
   != []

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the value of ``reality`` to a :ref:`call<how to call a function>` to ``datetime.date.today``

  .. code-block:: python
    :lineno-start: 314
    :emphasize-lines: 5-6

        def test_dir_datetime_date_today(self):
            # reality = dir(datetime.date.year)
            # reality = datetime.date.year
            # reality = datetime.date().year
            # reality = datetime.date.today
            reality = datetime.date.today()
            my_expectation = []
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: datetime.date(YYYY, MM, DD) != []

  where ``YYYY`` is the current year, ``MM`` is the current month and ``DD`` is the current date. Progress!

* When I :ref:`called<how to call a function>` ``datetime.date()`` it asked for the ``year`` argument, and the result of the :ref:`call<how to call a function>` is ``datetime.date(YYYY, MM, DD)`` which looks like a :ref:`call<how to call a function>` to ``datetime.date()``. I wonder if it also has a ``year`` :ref:`attribute<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 314
    :emphasize-lines: 6-7

        def test_dir_datetime_date_today(self):
            # reality = dir(datetime.date.year)
            # reality = datetime.date.year
            # reality = datetime.date().year
            # reality = datetime.date.today
            # reality = datetime.date.today()
            reality = dir(datetime.date.today())
            my_expectation = []
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` with a message about setting `self.maxDiff`_ to see the full difference

* I set `self.maxDiff`_ to :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 314
    :emphasize-lines: 9

        def test_dir_datetime_date_today(self):
            # reality = dir(datetime.date.year)
            # reality = datetime.date.year
            # reality = datetime.date().year
            # reality = datetime.date.today
            # reality = datetime.date.today()
            reality = dir(datetime.date.today())
            my_expectation = []
            self.maxDiff = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ shows the entire difference between ``reality`` and ``my_expectation`` and there is a ``year`` :ref:`attribute<what is a class attribute?>` because they are the same as :ref:`the attributes and methods of datetime.date<test_dir_datetime_date>`

* I change ``my_expectation``

  .. code-block:: python
    :lineno-start: 314
    :emphasize-lines: 8-9

        def test_dir_datetime_date_today(self):
            # reality = dir(datetime.date.year)
            # reality = datetime.date.year
            # reality = datetime.date().year
            # reality = datetime.date.today
            # reality = datetime.date.today()
            reality = dir(datetime.date.today())
            # my_expectation = []
            my_expectation = dir(datetime.date)
            self.maxDiff = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

----

*********************************************************************************
test_datetime_date_today_year
*********************************************************************************

It looks like I have a way to get the current year.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add :ref:`test_datetime_date_today_year` to test the ``year`` :ref:`attribute<what is a class attribute?>` of the result of a :ref:`call<how to call a function>` to the ``today`` :ref:`method<what is a method?>` of the ``date`` :ref:`class<everything is an object>` of the `datetime module`_ (``datetime.date.today().year``) in ``test_person.py``

.. code-block:: python
  :lineno-start: 324
  :emphasize-lines: 3-6

            self.assertEqual(reality, my_expectation)

        def test_datetime_date_today_year(self):
            reality = datetime.date.today().year
            my_expectation = 1900
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: YYYY != 1900

where ``YYYY`` is the current year.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``my_expectation`` to match ``reality`` and the test passes.

* I remove all the datetime_ tests now that I know :ref:`datetime.date.today().year<test_datetime_date_today_year>` works

  .. code-block:: python
    :lineno-start: 256

                'first_name',
                'last_name',
                'say_hello',
                'sex',
                'year_of_birth',
            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

:ref:`I have a way to automatically get the current year that will always be correct<test_datetime_date_today_year>`.

----

*********************************************************************************
test age with current year
*********************************************************************************

* I change the age calculation in ``my_expectation`` of :ref:`say_hello<test say_hello method>` in :ref:`test_joe` with :ref:`datetime.date.today().year<test_datetime_date_today_year>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 9-10

          reality = src.person.say_hello(
              first_name=first_name,
              last_name=last_name,
              year_of_birth=year_of_birth,
          )
          my_expectation = (
              f'Hello, my name is {first_name}'
              f' {last_name} and I am'
              # f' {2026-year_of_birth}.'
              f' {datetime.date.today().year-year_of_birth}.'
          )
          assert reality == my_expectation
          self.assertEqual(reality, my_expectation)

          joe = src.person.Person(

  the test is still green.

* I change the age calculation in ``my_expectation`` of :ref:`say_hello<test say_hello method>` in :ref:`test_jane` with :ref:`datetime.date.today().year<test_datetime_date_today_year>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 9-10

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                f' {datetime.date.today().year-year_of_birth}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            jane = src.person.Person(

  still green.

* I change the age calculation in ``my_expectation`` of :ref:`say_hello<test say_hello method>` in :ref:`test_john` with :ref:`datetime.date.today().year<test_datetime_date_today_year>`

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 9-10

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                f' {datetime.date.today().year-year_of_birth}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            john = src.person.Person(

  green.

* I change the age calculation in ``my_expectation`` of :ref:`say_hello<test say_hello method>` in :ref:`test_mary` with :ref:`datetime.date.today().year<test_datetime_date_today_year>`

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 9-10

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                f' {datetime.date.today().year-year_of_birth}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            mary = src.person.Person(

  still green.

* I open a new terminal_ then make sure I am in the ``person`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd person

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'use datetime to calculate age'

----

*********************************************************************************
extract this_year attribute
*********************************************************************************

Each test :ref:`calls datetime.date.today()<test_dir_datetime_date_today>` to get the :ref:`year attribute<test_datetime_date_today_year>`.

* I go back to the terminal_ where the tests are running

* I add a :ref:`class attribute<what is a class attribute?>` to :ref:`TestPerson<add TestPerson class>` for the current year

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year

        def test_joe(self):

* I use the :ref:`attribute<what is a class attribute?>` for ``datetime.date.today().year`` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 10-11

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                # f' {datetime.date.today().year-year_of_birth}.'
                f' {self.this_year-year_of_birth}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            joe = src.person.Person(

  still green.

* I use the :ref:`attribute<what is a class attribute?>` for ``datetime.date.today().year`` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 10-11

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                # f' {datetime.date.today().year-year_of_birth}.'
                f' {self.this_year-year_of_birth}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            jane = src.person.Person(

  green.

* I use the :ref:`attribute<what is a class attribute?>` for ``datetime.date.today().year`` in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 10-11

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                # f' {datetime.date.today().year-year_of_birth}.'
                f' {self.this_year-year_of_birth}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            john = src.person.Person(

  still green.

* I use the :ref:`attribute<what is a class attribute?>` for ``datetime.date.today().year`` in :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 164
    :emphasize-lines: 10-11

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                # f' {datetime.date.today().year-year_of_birth}.'
                f' {self.this_year-year_of_birth}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            mary = src.person.Person(

  the test is still green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract this_year attribute'

----

*********************************************************************************
extract calculate_age method
*********************************************************************************

Each test does a calculation for the age. I can make a :ref:`method<what is a method?>` to remove the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a :ref:`method<what is a method?>` to :ref:`TestPerson<add TestPerson class>` to calculate the age

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-6

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year

        def calculate_age(year_of_birth):
            return self.this_year - year_of_birth

        def test_joe(self):

* I use the :ref:`method<what is a method?>` for ``self.this_year-year_of_birth`` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 11-12

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                # f' {datetime.date.today().year-year_of_birth}.'
                # f' {self.this_year-year_of_birth}.'
                f' {self.calculate_age(year_of_birth)}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            joe = src.person.Person(

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestPerson.calculate_age() takes
        1 positional argument but 2 were given

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`calculate_age<extract calculate_age method>`

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 5-6

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year

        # def calculate_age(year_of_birth):
        def calculate_age(self, year_of_birth):
            return self.this_year - year_of_birth

        def test_joe(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 33

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {self.calculate_age(year_of_birth)}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            joe = src.person.Person(

* I use the :ref:`method<what is a method?>` for ``self.this_year-year_of_birth`` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 11-12

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                # f' {datetime.date.today().year-year_of_birth}.'
                # f' {self.this_year-year_of_birth}.'
                f' {self.calculate_age(year_of_birth)}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            jane = src.person.Person(

  the test is still green.

* I remove the commented lines from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 76

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {self.calculate_age(year_of_birth)}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            jane = src.person.Person(

* I use the :ref:`method<what is a method?>` for ``self.this_year-year_of_birth`` in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 11-12

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                # f' {datetime.date.today().year-year_of_birth}.'
                # f' {self.this_year-year_of_birth}.'
                f' {self.calculate_age(year_of_birth)}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            john = src.person.Person(

  still green.

* I remove the commented lines from :ref:`test_john`

  .. code-block:: python
    :lineno-start: 119

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {self.calculate_age(year_of_birth)}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            john = src.person.Person(

* I use the :ref:`method<what is a method?>` for ``self.this_year-year_of_birth`` in :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 162
    :emphasize-lines: 11-12

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                # f' {datetime.date.today().year-year_of_birth}.'
                # f' {self.this_year-year_of_birth}.'
                f' {self.calculate_age(year_of_birth)}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            mary = src.person.Person(

  green.

* I remove the commented lines from :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 162

            reality = src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {self.calculate_age(year_of_birth)}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            mary = src.person.Person(

* The :ref:`this_year class attribute<extract this_year attribute>` is now used in only one place :ref:`the calculate_age method<extract calculate_age method>`. I can call what it points to directly

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 7-11

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year

        # def calculate_age(year_of_birth):
        def calculate_age(self, year_of_birth):
            # return self.this_year - year_of_birth
            return (
                datetime.date.today().year
              - year_of_birth
            )

        def test_joe(self):

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` since :ref:`calculate_age<extract calculate_age method>` no longer uses anything from the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2

        # def calculate_age(year_of_birth):
        @staticmethod
        def calculate_age(self, year_of_birth):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestPerson.calculate_age() missing
        1 required positional argument: 'year_of_birth'

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I remove ``self`` from the parentheses

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3-4

        # def calculate_age(year_of_birth):
        @staticmethod
        # def calculate_age(self, year_of_birth):
        def calculate_age(year_of_birth):

  the test is green again.

* I remove the commented lines and :ref:`this_year attribute<extract this_year attribute>` since it is no longer used

  .. code-block:: python
    :lineno-start: 6

    class TestPerson(unittest.TestCase):

        @staticmethod
        def calculate_age(year_of_birth):
            return (
                datetime.date.today().year
              - year_of_birth
            )

        def test_joe(self):

  this works because Python_ follows the following path when ``self.calculate_age(year_of_birth)`` is :ref:`called<how to call a function with input>`

  .. code-block:: shell

    self.calculate_age(year_of_birth)
    └── class TestPerson(unittest.TestCase)
        │   @staticmethod
        └── def calculate_age(year_of_birth):
            └── return (
                    datetime.date.today().year
                  - year_of_birth
                )

  when ``datetime.date.today()`` runs, I imagine Python_ follows this path

  .. code-block:: shell

    datetime.date.today()
    datetime
        └── class date
            └── today()
                └── return self.date(YYYY, MM, DD)

  using substitution for :ref:`the return statement`

  .. code-block:: python

    return (
        datetime.date.today().year
      - year_of_birth
    )
    return (
        datetime.date(YYYY, MM, DD).year
      - year_of_birth
    )
    return (YYYY - year_of_birth)

  where ``YYYY`` is the current year.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract calculate_age method'

----

*********************************************************************************
add calculate_age function
*********************************************************************************

The tests use the right calculation for the age, and the solution still uses a fixed value (``2026``)

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I open ``person.py`` from the ``src`` folder_
* I add a :ref:`function<what is a function?>` to calculate the age, with the same body as the :ref:`calculate_age method<extract calculate_age method>`, in ``person.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 9-13

        def say_hello(self):
            return (
                f'Hello, my name is {self.first_name}'
                f' {self.last_name} and I am'
                f' {2026-self.year_of_birth}.'
            )


    def calculate_age(year_of_birth):
        return (
            datetime.date.today().year
          - year_of_birth
        )


    def say_hello(
        first_name, last_name, year_of_birth,
    ):

* I use the :ref:`function<what is a function?>` in the :ref:`say_hello method<test say_hello method>` of the :ref:`Person class<test Person class>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 5-6

        def say_hello(self):
            return (
                f'Hello, my name is {self.first_name}'
                f' {self.last_name} and I am'
                # f' {2026-self.year_of_birth}.'
                f' {calculate_age(self.year_of_birth)}.'
            )


    def calculate_age(year_of_birth):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'datetime' is not defined.
               Did you forget to import 'datetime'?

  I did.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ at the top of ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import datetime


    class Person:

  all tests are green again.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 12

        def say_hello(self):
            return (
                f'Hello, my name is {self.first_name}'
                f' {self.last_name} and I am'
                f' {calculate_age(self.year_of_birth)}.'
            )


    def calculate_age(year_of_birth):

* I use the :ref:`function<what is a function?>` in the :ref:`say_hello function<test say_hello function>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 7-8

    def say_hello(
        first_name, last_name, year_of_birth,
    ):
        return (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            # f' {2026-year_of_birth}.'
            f' {calculate_age(year_of_birth)}.'
        )


    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):

  still green.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 30

    def say_hello(
        first_name, last_name, year_of_birth,
    ):
        return (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {calculate_age(year_of_birth)}.'
        )


    def factory(

* I change the calculation in the :ref:`calculate_age method<extract calculate_age method>` to make sure the tests work, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2

        @staticmethod
        def calculate_age(year_of_birth):
            return 1900 - year_of_birth
            return (
                datetime.date.today().year
              - year_of_birth
            )

        def test_joe(self):

  - The terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for all four people.
  - The ages of the expectations are all negative numbers, this is a problem.
  - The results of the :ref:`call<how to call a function with input>` all have the right age. Lovely!

* I change the calculation in the :ref:`calculate_age method<extract calculate_age method>` back

  .. code-block:: python
    :lineno-start: 8

        @staticmethod
        def calculate_age(year_of_birth):
            return (
                datetime.date.today().year
              - year_of_birth
            )

        def test_joe(self):

  green again.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add calculate_age function'

----

*********************************************************************************
assert person is alive
*********************************************************************************

I want the :ref:`calculate_age function<add calculate_age function>` to make sure that the age of the person is not more than 120 because I do not know that there are any people alive older than that, yet. For example ``john smith`` has a ``year_of_birth`` of ``1580`` which makes him too old to be alive.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a :ref:`variable<what is a variable?>` with an :ref:`assert statement<what is an assertion?>` to :ref:`calculate_age function<add calculate_age function>` in ``person.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 2-3, 7-8

    def calculate_age(year_of_birth):
        # return (
        age = (
            datetime.date.today().year
          - year_of_birth
        )
        assert age <= 120
        return age


    def say_hello(
        first_name, last_name, year_of_birth,
    ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError

  another problem, the error message does not tell me much. At least the ``short test summary info`` shows me what test the error happened in

  .. code-block:: python

    FAILED ...::TestPerson::test_john - AssertionError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the value of ``year_of_birth`` in :ref:`test_john` in ``test_person.py``

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 5-6

      def test_john(self):
          first_name = 'john'
          last_name = 'smith'
          sex = 'M'
          # year_of_birth = 1580
          year_of_birth = 1980

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment about the bad ``year_of_birth``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5-8

        def test_john(self):
            first_name = 'john'
            last_name = 'smith'
            sex = 'M'
            year_of_birth = 1980
            # year_of_birth = 1580
            # raises AssertionError
            # because older than 120

* I remove the commented line from the :ref:`calculate_age function<add calculate_age function>` in ``person.py``

  .. code-block:: python
    :lineno-start: 23

    def calculate_age(year_of_birth):
        age = (
            datetime.date.today().year
          - year_of_birth
        )
        assert age <= 120
        return age


    def say_hello(
        first_name, last_name, year_of_birth,
    ):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'assert person is alive'

----

*********************************************************************************
assert year_of_birth is an integer
*********************************************************************************

I want the :ref:`Person class<test Person class>` to make sure that the value for ``year_of_birth`` is an integer_ (whole number without decimals).

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a new test

  .. code-block:: python
    :lineno-start: 186
    :emphasize-lines: 5-11

            reality = mary.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

        def test_when_year_of_birth_is_not_an_integer(self):
            person = src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
            )
            person.say_hello()

        def test_dir_person_class(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() missing
        1 required positional argument: 'year_of_birth'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I make ``year_of_birth`` an :ref:`optional argument<test_optional_arguments>` in the :ref:`Person class<test Person class>` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5-6

    class Person:

        def __init__(
            self, first_name, last_name,
            # sex, year_of_birth,
            sex, year_of_birth=None,
        ):

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -:
               'int' and 'NoneType'

  because :ref:`I cannot do Arithmetic with None<test_type_error_w_objects_that_do_not_mix>`.

* I add an :ref:`assertion<what is an assertion?>` with the :ref:`isinstance built-in function<how to test if something is an instance>` to make sure the :ref:`function<what is a function?>` only gets integers

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2

    def calculate_age(year_of_birth):
        assert isinstance(year_of_birth, int)
        age = (
            datetime.date.today().year
          - year_of_birth
        )
        assert age <= 120
        return age


    def say_hello(
        first_name, last_name, year_of_birth,
    ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError

  the error message is still a problem. The ``short test summary info`` shows me what test the error happened in

  .. code-block:: python

    FAILED ...::
        TestPerson::test_when_year_of_birth_is_not_an_integer
        - AssertionError

* I add a comment, then change ``year_of_birth`` from the :ref:`default value<test_optional_arguments>` to a :ref:`boolean<what are booleans?>` in :ref:`test_when_year_of_birth_is_not_an_integer<assert year_of_birth is an integer>`, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 6-7

        def test_when_year_of_birth_is_not_an_integer(self):
            person = src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                # year_of_birth=None,    # fails
                year_of_birth=False,
            )
            person.say_hello()

        def test_dir_person_class(self):

  the terminal shows :ref:`AssertionError<what causes AssertionError?>` for the age being greater than ``120``. Wait a minute! I was expecting that to fail at ``assert isinstance(year_of_birth, int)``. This means :ref:`a boolean is also an integer<is False an integer or a float?>`.

* I add a comment then change ``year_of_birth`` to a float_

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 7-8

        def test_when_year_of_birth_is_not_an_integer(self):
            person = src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                # year_of_birth=None,    # fails
                # year_of_birth=False,   # fails
                year_of_birth=2026.0,
            )
            person.say_hello()

        def test_dir_person_class(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

* I add a comment then change ``year_of_birth`` to a string_

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 8-9

        def test_when_year_of_birth_is_not_an_integer(self):
            person = src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                # year_of_birth=None,    # fails
                # year_of_birth=False,   # fails
                # year_of_birth=2026.0,  # fails
                year_of_birth='2026',
            )
            person.say_hello()

        def test_dir_person_class(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

* I add a comment then change ``year_of_birth`` to a tuple_

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 9-10

        def test_when_year_of_birth_is_not_an_integer(self):
            person = src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                # year_of_birth=None,    # fails
                # year_of_birth=False,   # fails
                # year_of_birth=2026.0,  # fails
                # year_of_birth='2026',  # fails
                year_of_birth=(2026,),
            )
            person.say_hello()

        def test_dir_person_class(self):

* I add a comment, then comment out the :ref:`call<how to call a function>` to :ref:`person.say_hello<test say_hello method>`

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 10, 12-14

        def test_when_year_of_birth_is_not_an_integer(self):
            person = src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                # year_of_birth=None,    # fails
                # year_of_birth=False,   # fails
                # year_of_birth=2026.0,  # fails
                # year_of_birth='2026',  # fails
                # year_of_birth=(2026,), # fails
            )
            # person.say_hello()
            # fails if year_of_birth
            # is not an integer

        def test_dir_person_class(self):

  the test is green because there is no :ref:`assertion<what is an assertion?>` or :ref:`calls<how to call a function>` that cause :ref:`AssertionError<what causes AssertionError?>`.

* I remove the commented line from the :ref:`Person class<test Person class>` in ``person.py``

  .. code-block:: python
    :lineno-start: 4

    class Person:

        def __init__(
            self, first_name, last_name,
            sex, year_of_birth=None,
        ):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'assert year_of_birth is an integer'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_person.py`` and ``person.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``person``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    ...\pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
review
*************************************************************************************

* I can use the :ref:`datetime library<test person with datetime>` to automatically get the current year for the calculation of a person's age.
* I can use :ref:`assertions<what is an assertion?>` to make sure certain :ref:`conditions<if statements>` are met before a program does something.
* My tests have a new problem - when they cause an :ref:`Exception<errors>` the test stops in a :red:`RED` state. My solution was to add notes and comment out the problems, which means the only way to know that the code causes the errors is by removing those comments. :ref:`There has to be a better way<how to test that an Exception is raised>`
* :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` also still have the problem where they are the same three tests. There has to be a better way.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test person with datetime: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

I know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what an assertion is<what is an assertion?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`
* :ref:`how to make functions that take input<functions that take input>`
* :ref:`what causes TypeError<what causes TypeError?>`
* :ref:`how to place values in strings<telephone>`
* :ref:`how to make a person say hello with f-strings<how to make a person with f-strings>`
* :ref:`how to separate tests from solutions<separate and equal>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to make a person with a class<how to make a person with a class>`
* :ref:`that everything in Python is an object<everything is an object>`
* :ref:`how to use the unittest library<another way to write tests>`
* :ref:`how to calculate age with the datetime library<test person with datetime>`

:ref:`Would you like to test None (the simplest object)?<what is None?>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->