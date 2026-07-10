.. meta::
  :description:
  :keywords:

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

The :ref:`person<how to make a person with a class>` project has a problem with the calculation of the ages. It only shows the right age if the program is run in ``2026``, because the year is hardcoded. If I run it in a different year or change the year on my computer, the tests for :ref:`say_hello<test say_hello method>` will fail.

I want the calculation to always be right, which means the program should always know the correct year.

I can do that with the `datetime module`_ from `The Python Standard Library`_. You can think of it as a toolbox with different tools I can use to do things with dates and times.

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
    :lineno-start: 4
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

  the test passes because when ``import datetime`` runs, Python_ brings in an :ref:`object (everything in Python is an object)<what is a class?>` for the `datetime module`_ from `The Python Standard Library`_ so I can use it in ``test_person.py`` as ``datetime``.

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

  the terminal_ shows the entire difference between ``reality`` and ``my_expectation``.

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

I add a test for the ``year`` :ref:`attribute<what is a class attribute?>` of the ``date`` :ref:`attribute<what is a class attribute?>` of the `datetime module`_ inj ``test_person.py``

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

I add :ref:`test_dir_datetime_date_today_year` to a test for the ``year`` :ref:`attribute<what is a class attribute?>` of the result of a :ref:`call<how to call a function>` to the ``date`` :ref:`method<what is a method?>` of the `datetime module`_ in ``test_person.py``

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

* I remove :ref:`test_dir_datetime_date`, :ref:`test_dir_datetime_date_today` add :ref:`test_datetime_date_today_year`

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
test_joe with datetime
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

  the test is still green

* I remove the commented line

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
              f' {datetime.date.today().year-year_of_birth}.'
          )
          assert reality == my_expectation
          self.assertEqual(reality, my_expectation)

----

*********************************************************************************
test_jane with datetime
*********************************************************************************

* I change the age calculation in ``my_expectation`` of :ref:`say_hello<test say_hello method>` in :ref:`test_jane` with :ref:`datetime.date.today().year<test_datetime_date_today_year>`

  .. code-block:: python
    :lineno-start: 70
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

  the test is still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 9-10

          reality = src.person.say_hello(
              first_name=first_name,
              last_name=last_name,
              year_of_birth=year_of_birth,
          )
          my_expectation = (
              f'Hello, my name is {first_name}'
              f' {last_name} and I am'
              f' {datetime.date.today().year-year_of_birth}.'
          )
          assert reality == my_expectation
          self.assertEqual(reality, my_expectation)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``my_expectation`` to match ``reality`` and the test passes.

* I remove :ref:`test_dir_datetime_date`, :ref:`test_dir_datetime_date_today` add :ref:`test_datetime_date_today_year` because I no longer need them

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
















* I open a new terminal_ then make sure I am in the ``classes`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd classes



* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_dir_datetime'



*********************************************************************************
close the project
*********************************************************************************

* I close ``test_person.py``
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

* I can use the :ref:`unittest library<another way to write tests>` to write tests with the :ref:`methods of the unittest.TestCase class<test_dir_unittest_testcase>` or I can write them with bare :ref:`assert statements<what is an assertion?>`.

* My tests for a person still have the problem where they are the same three tests. There has to be a way that I can use one test for all the people.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test person with datetime: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

You know

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