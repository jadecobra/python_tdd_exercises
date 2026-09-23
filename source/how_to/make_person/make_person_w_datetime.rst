.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): test person with datetime — fix the person project's hardcoded 2026 age so say_hello stays correct every year. Open person; uv run pytest-watcher . --now (6 passed from unittest chapter). Explore the datetime module with test_dir_datetime → NameError: name 'datetime' is not defined. Did you forget to import 'datetime'?; import datetime; paste dir(datetime) as my_expectation (MAXYEAR, date, datetime, timedelta, …; list may differ by Python version). Drill datetime.date, self.maxDiff = None, TypeError: function missing required argument 'year', then datetime.date.today().year. Replace f' {2026-year_of_birth}.' with datetime.date.today().year-year_of_birth in assert_say_hello_works and assert_person_can_say_hello. Extract this_year class attribute, then calculate_age method: TypeError takes 1 positional argument but 2 were given (need self); @staticmethod then remove self. Port calculate_age to person.py (import datetime; NameError if forgotten). Assert age <= 120 (john 1580 → AssertionError; change to 1980). Assert isinstance(year_of_birth, int); optional year_of_birth=None; bool is an int so False skips the isinstance guard and fails the age bound; float/str/tuple fail. Review: datetime for current year; bare asserts stop the test so cases are commented out — need a better way to test exceptions. Catalog: test_person_w_datetime.py + person_w_datetime.py.
  :keywords: Jacob Itegboje, Pumping Python, test person with datetime, person project hardcoded 2026 age, datetime module, import datetime, NameError name 'datetime' is not defined, Did you forget to import 'datetime', dir(datetime), datetime.date, datetime.date.today().year, self.maxDiff = None, TypeError function missing required argument 'year', TypeError calculate_age takes 1 positional argument but 2 were given, @staticmethod, extract this_year, extract calculate_age, assert age <= 120, assert age >= 0, john smith year_of_birth 1580, year_of_birth 1980, isinstance year_of_birth int, boolean is also an integer, year_of_birth=None, TypeError unsupported operand type(s) for - 'int' and 'NoneType', test_when_year_of_birth_is_not_an_integer, uv run pytest-watcher . --now, red green refactor, remove the commented lines, git commit -am, person say_hello age calculation, test_person_w_datetime, person_w_datetime

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

The :ref:`person<test person with unittest>` project has a problem with the calculation of the ages. It only shows the right age if the program is run in ``2026``, because the year is hardcoded. If I run it in a different year or change the year on my computer, the ages will be wrong and the tests for :ref:`say_hello<add say_hello method>` will fail.

I want the calculation to always be right, which means the program should always know the correct year.

I can use the `datetime module`_ from `The Python Standard Library`_. You can think of it as a toolbox with different tools I can use to do things with dates and times. I can also use :ref:`assertions<what is an assertion?>` to make sure I get the right year of birth for the calculations.

----

*********************************************************************************
preview
*********************************************************************************

I add the following code by the end of the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_datetime.py
  :caption: person/tests/test_person.py
  :language: python
  :linenos:
  :lines: 1-11

.. literalinclude:: ../../code/person/tests/test_person_w_datetime.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 25
  :lines: 25-30

.. literalinclude:: ../../code/person/tests/test_person_w_datetime.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 32
  :lines: 32-47

.. literalinclude:: ../../code/person/tests/test_person_w_datetime.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 49
  :lines: 49-65

.. literalinclude:: ../../code/person/tests/test_person_w_datetime.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 119
  :lines: 119-143

.. literalinclude:: ../../code/person/tests/test_person_w_datetime.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 171
  :lines: 171-179

.. literalinclude:: ../../code/person/tests/test_person_w_datetime.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 181
  :lines: 181-189

.. literalinclude:: ../../code/person/tests/test_person_w_datetime.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 191
  :lines: 191-204

-----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd person

* I open ``test_person.py`` from the ``tests`` folder_

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1

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

* I add :ref:`test_dir_datetime` to ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 180

        def test_dir_person_instance(self):
            self.assertEqual(
                dir(
                    src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=2026,
                    )
                ),
                [
                    '__class__', '__delattr__', '__dict__',

  .. code-block:: python
    :lineno-start: 201
    :emphasize-lines: 5-9

                    'last_name', 'say_hello', 'sex', 'year_of_birth',
                ]
            )

        def test_dir_datetime(self):
            self.assertEqual(
                dir(datetime),
                []
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

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

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_, paste (:kbd:`ctrl/command+v`) them as the expectation of the :ref:`assertion<what is an assertion?>` and remove the extra characters, in :ref:`test_dir_datetime`

  .. caution:: Your list of attributes and methods may be different depending on your Python version

  .. code-block:: python
    :lineno-start: 206
    :emphasize-lines: 4-24

        def test_dir_datetime(self):
            self.assertEqual(
                dir(datetime),
                [
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
            )


    # Exceptions seen

  the test passes because when ``import datetime`` runs, Python_ brings in an :ref:`object (everything in Python is an object)<everything is an object>` for the `datetime module`_ from `The Python Standard Library`_ so I can use it in ``tests/test_person.py`` as ``datetime``.

  This means that there is a file_ or folder_ on the computer named ``datetime`` that got added when I installed Python_.


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

I add :ref:`test_dir_datetime_date` to ``tests/test_person.py``

.. code-block:: python
  :lineno-start: 206

        def test_dir_datetime(self):
            self.assertEqual(
                dir(datetime),
                [
                    'MAXYEAR',

.. code-block:: python
  :lineno-start: 228
  :emphasize-lines: 5-9

                    'tzinfo'
                ]
            )

        def test_dir_datetime_date(self):
            self.assertEqual(
                dir(datetime.date),
                []
            )


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
    :lineno-start: 232
    :emphasize-lines: 2

        def test_dir_datetime_date(self):
            self.maxDiff = None
            self.assertEqual(
                dir(datetime.date),
                []
            )


    # Exceptions seen

  - The terminal_ shows the entire difference between ``reality`` and ``my_expectation``.
  - `maxDiff`_ is an :ref:`attribute<what causes AttributeError?>` of the :ref:`unittest.TestCase class<test_dir_unittest_testcase>` that sets the maximum number of characters to show when comparing two :ref:`objects<everything is an object>` in the terminal_, when it is set to :ref:`None<what is None?>` it shows the full difference.

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_, paste (:kbd:`ctrl/command+v`) them as ``my_expectation`` and remove the extra characters

  .. code-block:: python
    :lineno-start: 232
    :emphasize-lines: 5-23
    :emphasize-text: year today

        def test_dir_datetime_date(self):
            self.maxDiff = None
            self.assertEqual(
                dir(datetime.date),
                [
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
            )


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

I add a test for the ``year`` :ref:`attribute<what is a class attribute?>` of the ``date`` :ref:`attribute<what is a class attribute?>` of the `datetime module`_ in ``tests/test_person.py``

.. code-block:: python
  :lineno-start: 253
  :emphasize-lines: 5-8

                  'weekday', 'year'
              ]
          )

      def test_dir_datetime_date_year(self):
          self.assertEqual(
              dir(datetime.date.year),
              []
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` with only :ref:`attributes<what is a class attribute?>` that start and end with double underscore (``__``)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the :ref:`assertion<what is an assertion?>` to see what the ``datetime.date.year`` :ref:`object<everything is an object>` is

  .. code-block:: python
    :lineno-start: 257
    :emphasize-lines: 3-4

        def test_dir_datetime_date_year(self):
            self.assertEqual(
                # dir(datetime.date.year),
                datetime.date.year,
                []
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <attribute 'year' of 'datetime.date' objects>
     != []

* I try :ref:`making an instance<how to test if something is an instance>` of the :ref:`datetime.date object<test_dir_datetime_date>`

  .. code-block:: python
    :lineno-start: 257
    :emphasize-lines: 4-5

        def test_dir_datetime_date_year(self):
            self.assertEqual(
                # dir(datetime.date.year),
                # datetime.date.year,
                datetime.date().year,
                []
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function missing
               required argument 'year' (pos 1)

  It is a :ref:`function<what is a function?>` that has required input. I want something that automatically knows the date and gives me the year.

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

I change :ref:`test_dir_datetime_date_year` to a test for the ``today`` :ref:`attribute<what is a class attribute?>` of the ``date`` :ref:`attribute<what is a class attribute?>` of the `datetime module`_ in ``tests/test_person.py``

.. code-block:: python
  :lineno-start: 253
  :emphasize-lines: 5-6, 10-11

                  'weekday', 'year'
              ]
          )

      # def test_dir_datetime_date_year(self):
      def test_dir_datetime_date_today(self):
          self.assertEqual(
              # dir(datetime.date.year),
              # datetime.date.year,
              # datetime.date().year,
              datetime.date.today,
              []
          )


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

* I :ref:`call<how to call a function>` the ``datetime.date.today`` :ref:`method<what is a method?>` to see what it returns

  .. code-block:: python
    :lineno-start: 257
    :emphasize-lines: 7-8

        # def test_dir_datetime_date_year(self):
        def test_dir_datetime_date_today(self):
            self.assertEqual(
                # dir(datetime.date.year),
                # datetime.date.year,
                # datetime.date().year,
                # datetime.date.today,
                datetime.date.today(),
                []
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: datetime.date(YYYY, MM, DD) != []

  where ``YYYY`` is the current year, ``MM`` is the current month and ``DD`` is the current date. Progress!

* When I :ref:`called<how to call a function>` ``datetime.date()`` it asked for the ``year`` argument, and the result of the :ref:`call<how to call a function>` to ``datetime.date.today()`` is ``datetime.date(YYYY, MM, DD)`` which looks like an :ref:`instance<how to test if something is an instance>` of the :ref:`datetime.date object<test_dir_datetime_date>` with input. I use the `dir built-in function`_ to show its :ref:`attributes<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 257
    :emphasize-lines: 8-9

        # def test_dir_datetime_date_year(self):
        def test_dir_datetime_date_today(self):
            self.assertEqual(
                # dir(datetime.date.year),
                # datetime.date.year,
                # datetime.date().year,
                # datetime.date.today,
                # datetime.date.today(),
                dir(datetime.date.today()),
                []
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` with a message about setting `self.maxDiff`_ to see the full difference

* I set `self.maxDiff`_ to :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 257
    :emphasize-lines: 3

        # def test_dir_datetime_date_year(self):
        def test_dir_datetime_date_today(self):
            self.maxDiff = None
            self.assertEqual(
                # dir(datetime.date.year),
                # datetime.date.year,
                # datetime.date().year,
                # datetime.date.today,
                # datetime.date.today(),
                dir(datetime.date.today()),
                []
            )


    # Exceptions seen

  the terminal_ shows the entire difference between ``reality`` and ``my_expectation`` and there is a ``year`` :ref:`attribute<what is a class attribute?>` because they are the same as :ref:`the attributes and methods of datetime.date<test_dir_datetime_date>`

* I change the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 257
    :emphasize-lines: 11-12

        # def test_dir_datetime_date_year(self):
        def test_dir_datetime_date_today(self):
            self.maxDiff = None
            self.assertEqual(
                # dir(datetime.date.year),
                # datetime.date.year,
                # datetime.date().year,
                # datetime.date.today,
                # datetime.date.today(),
                dir(datetime.date.today()),
                # []
                dir(datetime.date)
            )


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

I add :ref:`test_datetime_date_today_year` to test the ``year`` :ref:`attribute<what is a class attribute?>` of the result of a :ref:`call<how to call a function>` to the ``today`` :ref:`method<what is a method?>` of the ``date`` :ref:`class<everything is an object>` of the `datetime module`_ (``datetime.date.today().year``) in ``tests/test_person.py``

.. code-block:: python
  :lineno-start: 268
  :emphasize-lines: 4-8

              dir(datetime.date)
          )

      def test_datetime_date_today_year(self):
          self.assertEqual(
              datetime.date.today().year,
              1900
          )


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

* I change my expectation to match reality and the test passes.

* I remove all the datetime_ tests now that I know :ref:`datetime.date.today().year<test_datetime_date_today_year>` works

  .. code-block:: python
    :lineno-start: 181

        def test_dir_person_instance(self):
            self.assertEqual(
                dir(
                    src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=2026,
                    )
                ),
                [
                    '__class__', '__delattr__', '__dict__',

  .. code-block:: python
    :lineno-start: 202

                    'last_name', 'say_hello', 'sex', 'year_of_birth',
                ]
            )


    # Exceptions seen

:ref:`I have a way to automatically get the current year that will always be correct<test_datetime_date_today_year>`.

I imagine Python_ follows this path to get the value of :ref:`datetime.date.today().year<test_datetime_date_today_year>`

.. code-block:: shell

  datetime.date.today().year
  └── datetime
      └── class date:
          │   @staticmethod
          └── def today():
              ├── current_year  = YYYY
              ├── current_month = MM
              ├── current_day   = DD
              └── return datetime.date(
                      current_year, current_month, current_day
                  )

----

*********************************************************************************
test age with current year
*********************************************************************************

* I change the age calculation in the expectation of the :ref:`assert_say_hello_works method<move assert_say_hello_works to TestPerson>` to :ref:`datetime.date.today().year<test_datetime_date_today_year>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 14-15

        def assert_say_hello_works(
                self, first_name, last_name,
                year_of_birth,
            ):
            self.assertEqual(
                src.person.say_hello(
                    first_name=first_name,
                    last_name=last_name,
                    year_of_birth=year_of_birth
                ),
                (
                    f'Hello, my name is {first_name}'
                    f' {last_name} and I am'
                    # f' {2026-year_of_birth}.'
                    f' {datetime.date.today().year-year_of_birth}.'
                )
            )

        def assert_person_can_say_hello(
                self,first_name, last_name,
                sex, year_of_birth,
            ):

  all the tests are still green.

* I change the age calculation in the expectation of the :ref:`assert_person_can_say_hello method<move assert_person_can_say_hello to TestPerson>` to :ref:`datetime.date.today().year<test_datetime_date_today_year>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 15-16

        def assert_person_can_say_hello(
                self,first_name, last_name,
                sex, year_of_birth,
            ):
            self.assertEqual(
                src.person.Person(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                ).say_hello(),
                (
                    f'Hello, my name is {first_name}'
                    f' {last_name} and I am'
                    # f' {2026-year_of_birth}.'
                    f' {datetime.date.today().year-year_of_birth}.'
                )
            )

        def test_joe(self):

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

The :ref:`assert_say_hello_works<move assert_say_hello_works to TestPerson>` and :ref:`assert_person_can_say_hello methods<move assert_person_can_say_hello to TestPerson>` both :ref:`call datetime.date.today()<test_dir_datetime_date_today>` to get the :ref:`year attribute<test_datetime_date_today_year>`. I can use a :ref:`class attribute<what is a class attribute?>` to remove the repetition

* I go back to the terminal_ where the tests are running

* I add a :ref:`class attribute<what is a class attribute?>` to :ref:`TestPerson<add TestPerson class>` for the current year

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year

        def assert_person_factory_works(
                self, first_name, last_name,
                sex, year_of_birth
            ):

* I use the :ref:`attribute<what is a class attribute?>` for ``datetime.date.today().year`` in  the :ref:`assert_say_hello_works method<move assert_say_hello_works to TestPerson>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 15-16

        def assert_say_hello_works(
                self, first_name, last_name,
                year_of_birth,
            ):
            self.assertEqual(
                src.person.say_hello(
                    first_name=first_name,
                    last_name=last_name,
                    year_of_birth=year_of_birth
                ),
                (
                    f'Hello, my name is {first_name}'
                    f' {last_name} and I am'
                    # f' {2026-year_of_birth}.'
                    # f' {datetime.date.today().year-year_of_birth}.'
                    f' {self.this_year-year_of_birth}.'
                )
            )

        def assert_person_can_say_hello(
                self,first_name, last_name,
                sex, year_of_birth,
            ):

  still green.

* I use the :ref:`attribute<what is a class attribute?>` for ``datetime.date.today().year`` in  the :ref:`assert_person_can_say_hello method<move assert_person_can_say_hello to TestPerson>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 16-17

        def assert_person_can_say_hello(
                self,first_name, last_name,
                sex, year_of_birth,
            ):
            self.assertEqual(
                src.person.Person(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                ).say_hello(),
                (
                    f'Hello, my name is {first_name}'
                    f' {last_name} and I am'
                    # f' {2026-year_of_birth}.'
                    # f' {datetime.date.today().year-year_of_birth}.'
                    f' {self.this_year-year_of_birth}.'
                )
            )

        def test_joe(self):

  the tests are still green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract this_year attribute'

----

*********************************************************************************
extract calculate_age method
*********************************************************************************

The :ref:`assert_say_hello_works<move assert_say_hello_works to TestPerson>` and :ref:`assert_person_can_say_hello methods<move assert_person_can_say_hello to TestPerson>` both do a calculation for the age. I can use a :ref:`method<what is a method?>` to remove the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a :ref:`method<what is a method?>` to :ref:`TestPerson<add TestPerson class>` to calculate the age

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 18-19

        def assert_person_factory_works(
                self, first_name, last_name,
                sex, year_of_birth
            ):
            self.assertEqual(
                src.person.person(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                ),
                (
                    f'{first_name}, {last_name},'
                    f' {sex}, {year_of_birth}'
                )
            )

        def calculate_age(year_of_birth):
            return self.this_year - year_of_birth

        def assert_say_hello_works(
                self, first_name, last_name,
                year_of_birth,
            ):

* I use the :ref:`method<what is a method?>` for ``self.this_year-year_of_birth`` in the :ref:`assert_say_hello_works method<move assert_say_hello_works to TestPerson>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 16-17

        def assert_say_hello_works(
                self, first_name, last_name,
                year_of_birth,
            ):
            self.assertEqual(
                src.person.say_hello(
                    first_name=first_name,
                    last_name=last_name,
                    year_of_birth=year_of_birth
                ),
                (
                    f'Hello, my name is {first_name}'
                    f' {last_name} and I am'
                    # f' {2026-year_of_birth}.'
                    # f' {datetime.date.today().year-year_of_birth}.'
                    # f' {self.this_year-year_of_birth}.'
                    f' {self.calculate_age(year_of_birth)}.'
                )
            )

        def assert_person_can_say_hello(
                self,first_name, last_name,
                sex, year_of_birth,
            ):

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
  :lineno-start: 10
  :emphasize-lines: 18-19

      def assert_person_factory_works(
              self, first_name, last_name,
              sex, year_of_birth
          ):
          self.assertEqual(
              src.person.person(
                  first_name=first_name,
                  last_name=last_name,
                  sex=sex,
                  year_of_birth=year_of_birth,
              ),
              (
                  f'{first_name}, {last_name},'
                  f' {sex}, {year_of_birth}'
              )
          )

      # def calculate_age(year_of_birth):
      def calculate_age(self, year_of_birth):
          return self.this_year - year_of_birth

      def assert_say_hello_works(
              self, first_name, last_name,
              year_of_birth,
          ):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from the :ref:`assert_say_hello_works method<move assert_say_hello_works to TestPerson>`

  .. code-block:: python
    :lineno-start: 31

        def assert_say_hello_works(
                self, first_name, last_name,
                year_of_birth,
            ):
            self.assertEqual(
                src.person.say_hello(
                    first_name=first_name,
                    last_name=last_name,
                    year_of_birth=year_of_birth
                ),
                (
                    f'Hello, my name is {first_name}'
                    f' {last_name} and I am'
                    f' {self.calculate_age(year_of_birth)}.'
                )
            )

        def assert_person_can_say_hello(
                self,first_name, last_name,
                sex, year_of_birth,
            ):

* I use the :ref:`method<what is a method?>` for ``self.this_year-year_of_birth`` in the :ref:`assert_person_can_say_hello method<move assert_person_can_say_hello to TestPerson>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 17-18

        def assert_person_can_say_hello(
                self,first_name, last_name,
                sex, year_of_birth,
            ):
            self.assertEqual(
                src.person.Person(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                ).say_hello(),
                (
                    f'Hello, my name is {first_name}'
                    f' {last_name} and I am'
                    # f' {2026-year_of_birth}.'
                    # f' {datetime.date.today().year-year_of_birth}.'
                    # f' {self.this_year-year_of_birth}.'
                    f' {self.calculate_age(year_of_birth)}.'
                )
            )

        def test_joe(self):

  the test is still green.

* I remove the commented lines from the :ref:`assert_person_can_say_hello method<move assert_person_can_say_hello to TestPerson>`

  .. code-block:: python
    :lineno-start: 48

        def assert_person_can_say_hello(
                self,first_name, last_name,
                sex, year_of_birth,
            ):
            self.assertEqual(
                src.person.Person(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                ).say_hello(),
                (
                    f'Hello, my name is {first_name}'
                    f' {last_name} and I am'
                    f' {self.calculate_age(year_of_birth)}.'
                )
            )

        def test_joe(self):

* The :ref:`this_year class attribute<extract this_year attribute>` is now used in only one place - the :ref:`calculate_age method<extract calculate_age method>`. I can :ref:`call<how to call a function with input>` what it points to directly, with no need for the :ref:`class attribute<what is a class attribute?>` as a middle man

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3-7

        # def calculate_age(year_of_birth):
        def calculate_age(self, year_of_birth):
            # return self.this_year - year_of_birth
            return (
                datetime.date.today().year
              - year_of_birth
            )

        def assert_say_hello_works(
                self, first_name, last_name,
                year_of_birth,
            ):

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` since :ref:`calculate_age<extract calculate_age method>` no longer uses anything that belongs to the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 2

        # def calculate_age(year_of_birth):
        @staticmethod
        def calculate_age(self, year_of_birth):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestPerson.calculate_age() missing
        1 required positional argument: 'year_of_birth'

* I remove ``self`` from the parentheses

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 1-3

        @staticmethod
        def calculate_age(year_of_birth):
        # def calculate_age(self, year_of_birth):
            # return self.this_year - year_of_birth
            return (
                datetime.date.today().year
              - year_of_birth
            )

  the test is green again.

* I remove the commented lines from the :ref:`calculate_age method<extract calculate_age method>`

  .. code-block:: python
    :lineno-start: 27

        @staticmethod
        def calculate_age(year_of_birth):
            return (
                datetime.date.today().year
              - year_of_birth
            )

        def assert_say_hello_works(
                self, first_name, last_name,
                year_of_birth,
            ):

* I remove the :ref:`this_year attribute<extract this_year attribute>` from the :ref:`TestPerson class<add TestPerson class>` since it is no longer used

  .. code-block:: python
    :lineno-start: 6

    class TestPerson(unittest.TestCase):

        def assert_person_factory_works(
                self, first_name, last_name,
                sex, year_of_birth
            ):

  when ``self.calculate_age(year_of_birth)`` runs

  .. code-block:: shell

    self.calculate_age(year_of_birth)
    └── class TestPerson(unittest.TestCase)
        │   @staticmethod
        └── def calculate_age(year_of_birth):
            └── return (
            ┌────── datetime.date.today().year
            │     - year_of_birth
            │   )
            │
            └── datetime
                └── class date:
                    │   @staticmethod
                    └── def today():
                        ├── current_year  = YYYY
                        ├── current_month = MM
                        ├── current_day   = DD
                        └── return datetime.date(
                                current_year, current_month, current_day
                            )

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

* I go back to the terminal_ where the tests are running
* I open ``__init__.py`` from the ``person`` folder_ in the ``src`` folder_
* I add a :ref:`function<what is a function?>` to calculate the age, with the same body as the :ref:`calculate_age method<extract calculate_age method>`, in ``src/person/__init__.py``

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

* I use the :ref:`function<what is a function?>` in the :ref:`say_hello method<add say_hello method>` of the :ref:`Person class<add Person class>`

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

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell

    NameError: name 'datetime' is not defined.
               Did you forget to import 'datetime'?

  I did.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ at the top of ``src/person/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import datetime


    class Person:

  all tests are green again.

* I remove the commented line from the :ref:`say_hello method<test_classy_person_says_hello>`

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


    def person(
            first_name, last_name,
            sex, year_of_birth,
        ):

  still green.

* I remove the commented line from the :ref:`say_hello function<test say_hello function>`

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


    def person(
            first_name, last_name,
            sex, year_of_birth,
        ):

* I change the calculation in the :ref:`calculate_age method<extract calculate_age method>` to make sure the tests work, in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3

        @staticmethod
        def calculate_age(year_of_birth):
            return 1900 - year_of_birth
            return (
                datetime.date.today().year
              - year_of_birth
            )

        def assert_say_hello_works(
                self, first_name, last_name,
                year_of_birth,
            ):

  - The terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for all four people.
  - The ages of the expectations are all negative numbers, since I used a year that is earlier than the dates of birth except for ``john``. This is a problem.
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
test_when_person_is_older_than_120
*********************************************************************************

I want the :ref:`calculate_age function<add calculate_age function>` to make sure that the age of the person is not more than 120 because I do not know that there are any people alive older than that, yet. For example ``john smith`` has a ``year_of_birth`` of ``1580`` which makes him too old to be alive.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a :ref:`variable<what is a variable?>` with an :ref:`assert statement<what is an assertion?>` to the :ref:`calculate_age function<add calculate_age function>` in ``src/person/__init__.py``

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

I change the value of ``year_of_birth`` in :ref:`test_john` in ``tests/test_person.py``

.. code-block:: python
  :lineno-start: 119
  :emphasize-lines: 5-6

      def test_john(self):
          first_name = 'john'
          last_name = 'smith'
          sex = 'M'
          # year_of_birth = 1580
          year_of_birth = 1980

          self.assert_person_factory_works(
              first_name=first_name,
              last_name=last_name,
              sex=sex,
              year_of_birth=year_of_birth,
          )

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line from :ref:`test_john`

  .. code-block:: python
    :lineno-start: 119

        def test_john(self):
            first_name = 'john'
            last_name = 'smith'
            sex = 'M'
            year_of_birth = 1980

            self.assert_person_factory_works(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

* I add a test for when the person is older than ``120``

  .. code-block:: python
    :lineno-start: 145

    def test_mary(self):
        ...

  .. code-block:: python
    :lineno-start: 164
    :emphasize-lines: 8-14

        self.assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

    def test_when_person_is_older_than_120(self):
        src.person.Person(
            first_name='first_name',
            last_name='last_name',
            sex='M',
            year_of_birth=datetime.date.today().year-121
        ).say_hello()

    def test_dir_person_class(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError

  - I use ``datetime.date.today().year - 121`` to make sure the person is always older than ``120``
  - The ``short test summary info`` shows me what test the error happened in

    .. code-block:: python

      FAILED ...test_when_person_is_older_than_120 - AssertionError

* I remove the :ref:`call to the say_hello method<test_classy_person_says_hello>` then add a comment about the failure

  .. code-block:: python
    :lineno-start: 171
    :emphasize-lines: 7-9

        def test_when_person_is_older_than_120(self):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=datetime.date.today().year-121
            )
            # ).say_hello() fails
            # because person is older than 120

        def test_dir_person_class(self):

  the test is green because there are no :ref:`calls<how to call a function>` that cause an :ref:`Exception<how to handle Exceptions in tests>`.

* I remove the commented line from the :ref:`calculate_age function<add calculate_age function>` in ``src/person/__init__.py``

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
    :emphasize-lines: 1-2

    git commit -am \
    'add test_when_person_is_older_than_120:

----

*********************************************************************************
test_when_year_of_birth_is_the_future
*********************************************************************************

I want the :ref:`calculate_age function<add calculate_age function>` to also make sure that the year of birth of a person is before the current year.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a new test for when ``year_of_birth`` is in the future, in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 178
    :emphasize-lines: 4-13

            # ).say_hello() fails
            # because person is older than 120

        def test_when_year_of_birth_is_the_future(self):
            self.assertEqual(
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='F',
                    year_of_birth=datetime.date.today().year+1,
                ).say_hello(),
                AssertionError
            )

        def test_dir_person_class(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        'Hello, my name is first_name last_name and I am -1.'
     != <class 'AssertionError'>

  I use ``datetime.date.today().year + 1`` for all the years of birth in the future.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to the :ref:`calculate age function<add calculate_age function>` to make sure that the it never returns a number that is less than ``0``, in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6

    def calculate_age(year_of_birth):
        age = (
            datetime.date.today().year
          - year_of_birth
        )
        assert age >= 0
        assert age <= 120
        return age


    def say_hello(
            first_name, last_name, year_of_birth
        ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError

  the error message is still a problem. The ``short test summary info`` shows me what test the error happened in

  .. code-block:: python

    FAILED ...test_when_year_of_birth_is_the_future - AssertionError

* I remove the :ref:`assertion<what is an assertion?>` and :ref:`call to the say_hello method<test_classy_person_can_say_hello>` in :ref:`test_when_year_of_birth_is_the_future`, in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 181
    :emphasize-lines: 2-11

        def test_when_year_of_birth_is_the_future(self):
            # self.assertEqual(
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='F',
                year_of_birth=datetime.date.today().year+1,
            )
                # ).say_hello(),
                # AssertionError
            # )

        def test_dir_person_class(self):

  the test is green because there are no :ref:`calls<how to call a function>` that cause an :ref:`Exception<how to handle Exceptions in tests>`.

* I remove the commented lines from :ref:`test_when_year_of_birth_is_the_future` then add a comment about the test

  .. code-block:: python
    :lineno-start: 181
    :emphasize-lines: 8-9

        def test_when_year_of_birth_is_the_future(self):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='F',
                year_of_birth=datetime.date.today().year+1,
            )
            # ).say_hello() fails
            # because year_of_birth is in the future

        def test_dir_person_class(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_when_year_of_birth_is_the_future'

----

*********************************************************************************
test_when_year_of_birth_is_not_an_integer
*********************************************************************************

I want the :ref:`calculate_age function<add calculate_age function>` to make sure that the value for ``year_of_birth`` is an integer_ (whole number without decimals).

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a new test for when ``year_of_birth`` is not an integer_

  .. code-block:: python
    :lineno-start: 188
    :emphasize-lines: 4-9

            # ).say_hello() fails
            # because year_of_birth is in the future

        def test_when_year_of_birth_is_not_an_integer(self):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
            ).say_hello()

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

* I make ``year_of_birth`` an :ref:`optional argument<test_optional_arguments>` in the :ref:`constructor method<the constructor method>` of the :ref:`Person class<add Person class>` in ``src/person/__init__.py``

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

  because :ref:`I cannot do Arithmetic with None<test_type_error_w_the_unmixables>`.

* I add an :ref:`assertion<what is an assertion?>` with the :ref:`isinstance built-in function<how to test if something is an instance>` to make sure the :ref:`calculate age function<add calculate_age function>` only works with integers_

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2

    def calculate_age(year_of_birth):
        assert isinstance(year_of_birth, int)
        age = (
            datetime.date.today().year
          - year_of_birth
        )
        assert age >= 0
        assert age <= 120
        return age


    def say_hello(
            first_name, last_name, year_of_birth
        ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError

  another bad error message. The ``short test summary info`` shows me what test the error happened in

  .. code-block:: python

    FAILED ...test_when_year_of_birth_is_not_an_integer - AssertionError

* I add a comment, then add :ref:`False<test_what_is_false>` as the value for if a :ref:`boolean<what are booleans?>` is given as the value for the ``year_of_birth`` parameter in :ref:`test_when_year_of_birth_is_not_an_integer`, in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 6-7

        def test_when_year_of_birth_is_not_an_integer(self):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                # year_of_birth=None,       # fails
                year_of_birth=False,
            ).say_hello()

        def test_dir_person_class(self):

  the terminal shows :ref:`AssertionError<what causes AssertionError?>` for the age being greater than ``120``. Wait a minute! I was expecting that to fail at ``assert isinstance(year_of_birth, int)``. This means :ref:`a boolean is also an integer<is False an integer or a float?>`.

* I change ``year_of_birth`` from :ref:`False<test_what_is_false>` to a float_

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 6-7

        def test_when_year_of_birth_is_not_an_integer(self):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                # year_of_birth=None,     # fails
                year_of_birth=2026.0,
            ).say_hello()

        def test_dir_person_class(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

* I add a comment then change ``year_of_birth`` to a string_

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 7-8

        def test_when_year_of_birth_is_not_an_integer(self):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                # year_of_birth=None,     # fails
                # year_of_birth=2026.0,   # fails
                year_of_birth='2026',
            ).say_hello()

        def test_dir_person_class(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

* I add a comment then change ``year_of_birth`` to a tuple_

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 8-9

        def test_when_year_of_birth_is_not_an_integer(self):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                # year_of_birth=None,     # fails
                # year_of_birth=2026.0,   # fails
                # year_of_birth='2026',   # fails
                year_of_birth=(2026,),
            ).say_hello()

        def test_dir_person_class(self):

* I add comment out the :ref:`call to the say_hello method<test_classy_person_says_hello>` then add a comment about the test

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 9-12

        def test_when_year_of_birth_is_not_an_integer(self):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                # year_of_birth=None,     # fails
                # year_of_birth=2026.0,   # fails
                # year_of_birth='2026',   # fails
                # year_of_birth=(2026,),  # fails
            )
            # ).say_hello() fails
            # because year_of_birth is not an integer

        def test_dir_person_class(self):

  the test is green because there are no :ref:`calls<how to call a function>` that cause an :ref:`Exception<how to handle Exceptions in tests>`.

* I remove the commented line from the :ref:`Person class<add Person class>` in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 4

    class Person:

        def __init__(
            self, first_name, last_name,
            sex, year_of_birth=None,
        ):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_when_year_of_birth_is_not_an_integer'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_person.py`` and ``src/person/__init__.py``
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
* My tests have a new problem - when they cause an :ref:`Exception<how to test that an Exception is raised>` the test stops in a :red:`RED` state. My solution was to add notes and comment out the problems, which means the only way to know that the code causes the :ref:`Exception<how to test that an Exception is raised>` is to remove the comments. :ref:`There has to be a better way<how to test that an Exception is raised>`
* :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` also still have the problem where they are the same three tests. :ref:`There has to be a better way<how to make a person with loops>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test person with datetime: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python Test Driven Development environment manually<how to make a Python Test Driven Development environment manually>`.
* :ref:`I know what a Python module is<what is a module?>`.
* :ref:`I know how to run tests automatically<how to run tests automatically>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`I know how to make a person with strings<how to make a person with strings>`.
* :ref:`I know how to make functions that take input<functions that take input>`.
* :ref:`I know what causes TypeError<what causes TypeError?>`.
* :ref:`I know how to place values in strings<telephone>`.
* :ref:`I know how to make a person say hello with f-strings<how to make a person with f-strings>`.
* :ref:`I know how to separate tests from solutions<separate and equal>`.
* :ref:`I know what causes AttributeError<what causes AttributeError?>`.
* :ref:`I know how to make a person with a class<how to make a person with a class>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.

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