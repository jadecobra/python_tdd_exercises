.. meta::
  :description: Pumping Python, how to make a person with loops, by Johnny Blase. Repeated person checks become one for loop over a people tuple of tuples on TestPerson. Each row is year_of_birth, is_citizen, passed_test, then the expected can_vote and can_get_license results. test_person_class, test_say_hello_function, and test_person_factory share self.first_name, self.last_name, self.sex, self.this_year, younger_than_18, and not_younger_than_18. subTest(a_person) names the failing row. Non-integer rows None, 2026.0, '2026', and (2026,) hit except TypeError and assert "'{year_of_birth}' is not an integer". test_if_person_is_not_alive uses one with for subTest and assertRaisesRegex(ValueError, f'a {age} year old person is not alive.') on this_year+1 and this_year-121. test_when_person_is_older_than_120 and test_when_year_of_birth_is_the_future are removed because that test covers both. A wrong regex such as BOOM!!! fails as AssertionError: "BOOM!!!" does not match "a -1 year old person is too old to be alive." before the message becomes "is not alive." dir(Person) tests remain.
  :keywords: for loop, people tuple, subTest, test_person_class, test_person_factory, test_say_hello_function, test_if_person_is_not_alive, assertRaisesRegex, ValueError, TypeError, year_of_birth, can_vote, can_get_license, this_year, Pumping Python, Johnny Blase
.. include:: ../../links.rst

.. _how to make a person with loops:

#################################################################################
how to make a person with loops
#################################################################################

----

I have a problem in ``person/tests/test_person.py``

* :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` have the same :ref:`assertions<what is an assertion?>`.
* :ref:`test_when_year_of_birth_is_not_an_integer` also has :ref:`assertions<what is an assertion?>` that are basically the same, the only thing that changes are the values for the ``year_of_birth`` parameter.

This means that if I add more people or more cases where ``year_of_birth`` is not an integer_ I would have to add more tests.

I want to use one test for each of the three tests for each person, and one test for every case where ``year_of_birth`` is not an integer. I can do this with :ref:`for loops<what is a for loop?>`.

A :ref:`for loop<what is a for loop?>` is a way to repeat the same command over an :ref:`iterable<what is an iterable?>` (a collection of items), it is written like this

.. code-block:: python

  for item in collection:
      do something

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :caption: person/tests/test_person.py
  :language: python
  :linenos:
  :lines: 1-14

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 16
  :lines: 16-31

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 32
  :lines: 32-46

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 47
  :lines: 47-65

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :caption: person/tests/test_person.py
  :lineno-start: 67
  :lines: 67-99

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :caption: person/tests/test_person.py
  :lineno-start: 100
  :lines: 100-124

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 126
  :lines: 126-143

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 144
  :lines: 144-163

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 165
  :lines: 165-182

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 184
  :lines: 184-210

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 213
  :lines: 213-218

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

----

*********************************************************************************
extract test_person_factory
*********************************************************************************

The tests for the :ref:`person function<extract person function>` in :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` make a :ref:`call<how to call a function with input>` to the :ref:`person function<extract person function>` then compare the result with a string_.

.. code-block:: python

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

I can make one :ref:`function<what is a function?>` with a :ref:`for loop<what is a for loop?>` to remove the repetition.

----

* I add a test for the :ref:`person function<extract person function>` to ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 47

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

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 1-11

          def test_person_factory(self):
              people = (
                  ('joe', 'blow', 'M', 1996),
              )
              for a_person in people:
                  self.assert_person_factory_works(
                      first_name=a_person[0],
                      last_name=a_person[1],
                      sex=a_person[2],
                      year_of_birth=a_person[3],
                  )

          def test_joe(self):

  the test is still green.

* I made a tuple_ named ``people`` that contains a tuple_ for ``joe``

  .. code-block:: python

    people = (
        ('joe', 'blow', 'M', 1996),
    )

* I use a :ref:`for loop<what is a for loop?>` to repeat the same commands for each item in the ``people`` tuple, in this case there is only one item - the tuple_ for ``joe``

  .. code-block:: python

    for a_person in (
        ('joe', 'blow', 'M', 1996),
    ):

* I use the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of each item in ``joe`` for the parameters when the test :ref:`calls<how to call a function with input>` the :ref:`person function<extract person function>`

  .. code-block:: shell

    for a_person in people:
    ├── a_person = ('joe', 'blow', 'M', 1996)
    └── self.assert_person_factory_works(
            first_name=a_person[0],     # 'joe'
            last_name=a_person[1],      # 'blow'
            sex=a_person[2],            # 'M'
            year_of_birth=a_person[3],  # 1996
        )
        └── def assert_person_factory_works(
                self, first_name, last_name,
                sex, year_of_birth
            ):
            ├── first_name    = 'joe'   # a_person[0]
            ├── last_name     = 'blow'  # a_person[1]
            ├── sex           = 'M'     # a_person[2]
            ├── year_of_birth = 1996    # a_person[3]
            └── self.assertEqual(
            ┌────── src.person.person(
            │           first_name=first_name,        # 'joe'
            │           last_name=last_name,          # 'blow'
            │           sex=sex,                      # 'M'
            │           year_of_birth=year_of_birth,  # 1996
            │       ),
            │       (
            │           f'{first_name}, {last_name},'
            │           f' {sex}, {year_of_birth}'
            │       )
            │   )
            └────── src/person/__init__.py
                    └── def person(
                            first_name, last_name,
                            sex, year_of_birth,
                        ):
                        ├── first_name    = 'joe'   # a_person[0]
                        ├── last_name     = 'blow'  # a_person[1]
                        ├── sex           = 'M'     # a_person[2]
                        ├── year_of_birth = 1996    # a_person[3]
                        └── return (
                                f'{first_name}, {last_name},'
                                f' {sex}, {year_of_birth}'
                            )
                            return 'joe, blow, M, 1996'

* I add ``jane`` to the tuple_ of ``people``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 3

        def test_person_factory(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
            )
            for a_person in people:

  still green, because the result when the :ref:`person function<extract person function>` is :ref:`called<how to call a function with input>` with ``'jane'``, ``'doe'``, ``'F'`` and ``'1991'`` is ``'jane, doe, F, 1991'``.

  .. code-block:: shell

        for a_person in (
    ┌───┴── ('jane', 'doe', 'F', 1991),
    │       ('joe', 'blow', 'M', 1996),
    │   ):
    ├────── a_person = ('jane', 'doe', 'F', 1991)
    └────── self.assert_person_factory_works(
                first_name=a_person[0],     # 'jane'
                last_name=a_person[1],      # 'doe'
                sex=a_person[2],            # 'F'
                year_of_birth=a_person[3],  # 1991
            )
            └── def assert_person_factory_works(
                    self, first_name, last_name,
                    sex, year_of_birth
                ):
                └── self.assertEqual(
                ┌────── src.person.person(
                │           first_name=first_name,        # 'jane'
                │           last_name=last_name,          # 'doe'
                │           sex=sex,                      # 'F'
                │           year_of_birth=year_of_birth,  # 1991
                │       ),
                │       (
                │           f'{first_name}, {last_name},'
                │           f' {sex}, {year_of_birth}'
                │       )
                │   )
                └────── src/person/__init__.py
                        └── def person(
                                first_name, last_name,
                                sex, year_of_birth,
                            ):
                            ├── first_name    = 'jane'  # a_person[0]
                            ├── last_name     = 'doe'   # a_person[1]
                            ├── sex           = 'F'     # a_person[2]
                            ├── year_of_birth = 1991    # a_person[3]
                            └── return (
                                    f'{first_name}, {last_name},'
                                    f' {sex}, {year_of_birth}'
                                )
                                return 'jane, doe, M, 1991'

* I add a tuple_ for ``mary``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 5

        def test_person_factory(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
            )
            for a_person in people:

  still green.

  .. code-block:: shell

        for a_person in (
        │   ('joe', 'blow', 'M', 1996),
        │   ('jane', 'doe', 'F', 1991),
    ┌───┴── ('mary', 'public', 'F', 2000),
    │   ):
    ├────── a_person = ('mary', 'public', 'F', 2000)
    └────── self.assert_person_factory_works(
                first_name=a_person[0],     # 'mary'
                last_name=a_person[1],      # 'public'
                sex=a_person[2],            # 'F'
                year_of_birth=a_person[3],  # 2000
            )
            └── def assert_person_factory_works(
                    self, first_name, last_name,
                    sex, year_of_birth
                ):
                └── self.assertEqual(
                ┌────── src.person.person(
                │           first_name=first_name,        # 'mary'
                │           last_name=last_name,          # 'public'
                │           sex=sex,                      # 'F'
                │           year_of_birth=year_of_birth,  # 2000
                │       ),
                │       (
                │           f'{first_name}, {last_name},'
                │           f' {sex}, {year_of_birth}'
                │       )
                │   )
                └────── src/person/__init__.py
                        └── def person(
                                first_name, last_name,
                                sex, year_of_birth,
                            ):
                            ├── first_name    = 'mary'    # a_person[0]
                            ├── last_name     = 'public'  # a_person[1]
                            ├── sex           = 'F'       # a_person[2]
                            ├── year_of_birth = 2000      # a_person[3]
                            └── return (
                                    f'{first_name}, {last_name},'
                                    f' {sex}, {year_of_birth}'
                                )
                                return 'mary, public, M, 2000'

* I add a tuple_ for ``john``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 6

        def test_person_factory(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
            )
            for a_person in people:

  green, showing that for each tuple_ in the ``people`` tuple_, the :ref:`assertion<what is an assertion?>` is :ref:`True<test_what_is_true>`.

  .. code-block:: shell

        for a_person in (
        │   ('joe', 'blow', 'M', 1996),
        │   ('jane', 'doe', 'F', 1991),
        │   ('mary', 'public', 'F', 2000),
    ┌───┴── ('john', 'smith', 'M', 1980),
    │   ):
    ├────── a_person = ('john', 'smith', 'M', 1980)
    └────── self.assert_person_factory_works(
                first_name=a_person[0],     # 'john'
                last_name=a_person[1],      # 'smith'
                sex=a_person[2],            # 'M'
                year_of_birth=a_person[3],  # 1980
            )
            └── def assert_person_factory_works(
                    self, first_name, last_name,
                    sex, year_of_birth
                ):
                └── self.assertEqual(
                ┌────── src.person.person(
                │           first_name=first_name,        # 'john'
                │           last_name=last_name,          # 'smith'
                │           sex=sex,                      # 'M'
                │           year_of_birth=year_of_birth,  # 1980
                │       ),
                │       (
                │           f'{first_name}, {last_name},'
                │           f' {sex}, {year_of_birth}'
                │       )
                │   )
                └────── src/person/__init__.py
                        └── def person(
                                first_name, last_name,
                                sex, year_of_birth,
                            ):
                            ├── first_name    = 'john'    # a_person[0]
                            ├── last_name     = 'smith'  # a_person[1]
                            ├── sex           = 'M'       # a_person[2]
                            ├── year_of_birth = 1980      # a_person[3]
                            └── return (
                                    f'{first_name}, {last_name},'
                                    f' {sex}, {year_of_birth}'
                                )
                                return 'john, smith, M, 1980'

* I add a tuple_ for a person with a string_ as the ``year_of_birth``

  .. code-block:: python
    :lineno-start: 15

        def test_person_factory(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a string'),
            )
            for a_person in people:

  the test is still green, because the :ref:`person function<extract person function>` returns a string with the inputs it gets.

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_person_factory_works method<extract assert_person_factory_works function>` from :ref:`test_joe` since it is now a repetition

  .. code-block:: python
    :lineno-start: 81

        def test_joe(self):
            first_name = 'joe'
            last_name = 'blow'
            sex = 'M'
            year_of_birth = 1996

            self.assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            ...

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_person_factory_works method<extract assert_person_factory_works function>` from :ref:`test_jane` since it is now a repetition

  .. code-block:: python
    :lineno-start: 109

        def test_jane(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = 1991

            self.assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            ...

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_person_factory_works method<extract assert_person_factory_works function>` from :ref:`test_john` since it is now a repetition

  .. code-block:: python
    :lineno-start: 138

        def test_john(self):
            first_name = 'john'
            last_name = 'smith'
            sex = 'M'
            year_of_birth = 1980

            self.assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            ...

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_person_factory_works method<extract assert_person_factory_works function>` from :ref:`test_mary` since it is now a repetition

  .. code-block:: python
    :lineno-start: 168

        def test_mary(self):
            first_name = 'mary'
            last_name = 'public'
            sex = 'F'
            year_of_birth = 2000

            self.assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            ...

* I no longer need the :ref:`assert_person_factory_works method<extract assert_person_factory_works function>` because it is only used by :ref:`test_person_factory<extract test_person_factory>`

  .. code-block:: python
    :lineno-start: 65

        def test_person_factory(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a_string')
            )
            for a_person in people:
                self.assert_person_factory_works(
                    first_name=a_person[0],
                    last_name=a_person[1],
                    sex=a_person[2],
                    year_of_birth=a_person[3],
                )

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 1-4, 6-14

                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]

                self.assertEqual(
                    src.person.person(
                        first_name=first_name,
                        last_name=last_name,
                        sex=sex,
                        year_of_birth=year_of_birth,
                    ),
                    None
                )

        def test_joe(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'jane, doe, F, 1991' != None

* I change the expectation of the :ref:`assertion<what is an assertion?>` to ``'jane, doe, F, 1991'``

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 8

                self.assertEqual(
                    src.person.person(
                        first_name=first_name,
                        last_name=last_name,
                        sex=sex,
                        year_of_birth=year_of_birth,
                    ),
                    'jane, doe, F, 1991'
                )

        def test_joe(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'joe, blow, M, 1996' != 'jane, doe, F, 1991'

  because the :ref:`for loop<what is a for loop?>` moved to the next item in the ``people`` tuple_ (``'joe'``)

* I change the expectation to the :ref:`f-string<what is string interpolation?>` from the :ref:`assert_person_factory_works method<extract assert_person_factory_works function>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 8-11

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

        def test_joe(self):

  the test passes.

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_person_factory_works method<extract assert_person_factory_works function>` from :ref:`test_person_factory<extract test_person_factory>`

  .. code-block:: python
    :lineno-start: 65

        def test_person_factory(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a_string')
            )
            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]

  .. code-block:: python
    :lineno-start: 79

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

        def test_joe(self):

  the tests are still green.

* I remove the :ref:`assert_person_factory_works method<extract assert_person_factory_works function>` from the :ref:`TestPerson class<add TestPerson object>`

  .. code-block:: python
    :lineno-start: 6

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year

        def calculate_age(self, year_of_birth):
            return self.this_year - year_of_birth

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract test_person_factory'

The :ref:`for loop<what is a for loop?>` allows me to test any number of people with the same test. I no longer have to write one test for each person.

----

*********************************************************************************
extract test_say_hello_function
*********************************************************************************

The tests for the :ref:`say_hello function<test say_hello function>` in :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` make a :ref:`call<how to call a function with input>` to the :ref:`say_hello function<test say_hello function>` then compare the result with a string_.

.. code-block:: python

    self.assertEqual(
        src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        ),
        (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {self.calculate_age(year_of_birth)}.'
        )
    )

I can make one :ref:`function<what is a function?>` with a :ref:`for loop<what is a for loop?>` to remove the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the :ref:`say_hello function<test say_hello function>`

.. code-block:: python
  :lineno-start: 30

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

.. code-block:: python
  :lineno-start: 48
  :emphasize-lines: 1-12, 14-18

        def test_say_hello_function(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a_string')
            )
            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                year_of_birth = a_person[3]

                self.assert_say_hello_works(
                    first_name=first_name,
                    last_name=last_name,
                    year_of_birth=year_of_birth,
                )

        def test_person_factory(self):

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  E           TypeError

because

- the the :ref:`say_hello function<test say_hello function>` :ref:`calls<how to call a function with input>` the :ref:`calculate_age function<extract calculate_age function>`
- the :ref:`calculate_age function<extract calculate_age function>` raises :ref:`TypeError<what causes TypeError?>` when ``year_of_birth`` is not an integer_. ``year_of_birth`` is a string_ in the last tuple_ in the ``people`` tuple_ (``('first_name', 'last_name', 'F', 'a_string')``)

  .. code-block:: shell

        for person in (
        │   ('jane', 'doe', 'F', 1991),
        │   ('joe', 'blow', 'M', 1996),
        │   ('mary', 'public', 'F', 2000),
        │   ('john', 'smith', 'M', 1980),
    ┌───┴── ('first_name', 'last_name', 'F', 'a string'),
    │   ):
    ├────── a_person = ('first_name', 'last_name', 'F', 'a string')
    ├────── first_name = a_person[0]    # 'first_name'
    ├────── last_name = a_person[1]     # 'last_name'
    ├────── year_of_birth = a_person[3] # 'a string'
    └────── self.assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )
            └── def assert_person_factory_works(
                    self, first_name, last_name,
                    sex, year_of_birth
                ):
                └── self.assertEqual(
                ┌────── src.person.say_hello(
                │           first_name=first_name,
                │           last_name=last_name,
                │           year_of_birth=year_of_birth,
                │       ),
                │       (
                │           f'Hello, my name is {first_name}'
                │           f' {last_name} and I am'
                │           f' {self.calculate_age(year_of_birth)}.'
                │       )
                │   )
                └────── src/person/__init__.py
                        └── def say_hello(
                                    first_name, last_name, year_of_birth
                                ):
                                ├── first_name    = 'first_name'  # a_person[0]
                                ├── last_name     = 'last_name'   # a_person[1]
                                ├── year_of_birth = 'a string'    # a_person[3]
                                └── return (
                                        f'Hello, my name is {first_name}'
                                        f' {last_name} and I am'
                                        f' {calculate_age(year_of_birth)}.'
                                    )   │
                                        └── def calculate_age(year_of_birth):
                                            ├── year_of_birth = 'a string'
                                            └── if not isinstance(
                                                    year_of_birth, int
                                                ):
                                                └── raise TypeError
                                                ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``__init__.py`` from the ``person`` folder_ in the ``src`` folder_

* I add a message to the :ref:`calculate_age function<extract calculate_age function>` for when :ref:`TypeError<what causes TypeError?>` is :ref:`raised<how to raise an Exception>`, in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 3-5

    def calculate_age(year_of_birth):
        if not isinstance(year_of_birth, int):
            raise TypeError(
                f"'{year_of_birth}' is not an integer"
            )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'a string' is not an integer

  better.

* I change the statements in the :ref:`assert_say_hello_works method<extract assert_say_hello_works functions>` to a :ref:`try statement with an else clause<how to use try...except...else>` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5-26

        def assert_say_hello_works(
                self, first_name, last_name,
                year_of_birth,
            ):
            try:
                reality = src.person.say_hello(
                    first_name=first_name,
                    last_name=last_name,
                    year_of_birth=year_of_birth,
                )
            except TypeError:
                pass
            else:
                self.assertEqual(
                    reality,
                    # src.person.say_hello(
                    #     first_name=first_name,
                    #     last_name=last_name,
                    #     year_of_birth=year_of_birth,
                    # ),
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

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I want to test the error message to make sure the :ref:`assert_say_hello_works method<extract assert_say_hello_works function>` only catches :ref:`TypeError<what causes TypeError?>` with this specific message. I can use the :ref:`Exception<how to test that an Exception is raised>` in the :ref:`except block<how to handle Exceptions>` as an :ref:`object<everything is an object>` to do this

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 7

            try:
                reality = src.person.say_hello(
                    first_name=first_name,
                    last_name=last_name,
                    year_of_birth=year_of_birth,
                )
            except TypeError as error:
                pass
            else:

  the test is still green.

* I add :ref:`assertEqual<test_assertEqual>` to the :ref:`except block<how to handle Exceptions>` with the `dir built-in function`_ to see the :ref:`attributes<what is an object attribute?>` and :ref:`methods<what is a method?>` of the :ref:`Exception object<how to test that an Exception is raised>` in the :ref:`except block<how to handle Exceptions>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 2

                except TypeError as error:
                    self.assertEqual(dir(error), [])
                else:

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` with the list of :ref:`attributes<what is an object attribute?>` and :ref:`methods<what is a method?>`. Three of the names stand out because they do not have double underscores (``__``) before and after - ``add_note``, ``args`` and ``with_traceback``.

* I change the :ref:`assertion<what is an assertion?>` to see what ``add_note`` is

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 2-3

                except TypeError as error:
                    # self.assertEqual(dir(error), [])
                    self.assertEqual(error.add_note, None)
                else:

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <built-in method add_note
          of TypeError object at 0xffff7ed65c43>
     != None

  because ``add_note`` is a :ref:`method<what is a method?>`.

* I :ref:`call<how to call a function with input>` the ``add_note`` :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3

                except TypeError as error:
                    # self.assertEqual(dir(error), [])
                    self.assertEqual(error.add_note(), None)
                else:

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: BaseException.add_note() takes
               exactly one argument (0 given)

  this is not what I want, on to the next one.

* I change the :ref:`assertion<what is an assertion?>` to see what ``args`` is

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-4

                except TypeError as error:
                    # self.assertEqual(dir(error), [])
                    # self.assertEqual(error.add_note(), None)
                    self.assertEqual(error.args, None)
                else:

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ("'a string' is not an integer",) != None

  fantastic! ``args`` is a tuple_ that has the error message as its first and only item.

* I use the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of the error message with an :ref:`f-string<what is string interpolation?>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 4-7

                except TypeError as error:
                    # self.assertEqual(dir(error), [])
                    # self.assertEqual(error.add_note(), None)
                    self.assertEqual(
                        error.args[0],
                        f"'{year_of_birth}' is not an integer"
                    )
                else:

  the test passes.

* I change the message for :ref:`TypeError<what causes TypeError?>` in the :ref:`calculate_age function<extract calculate_age function>` in ``src/person/__init__.py`` to test my change

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 3

    def calculate_age(year_of_birth):
        if not isinstance(year_of_birth, int):
            raise TypeError('BOOM!!!')
            raise TypeError(
                f"'{year_of_birth}' is not an integer"
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'BOOM!!!' != "'a string' is not an integer"

  because the error message is not correct

  .. code-block:: shell

            for a_person in (
            │   ('jane', 'doe', 'F', 1991),
            │   ('joe', 'blow', 'M', 1996),
            │   ('mary', 'public', 'F', 2000),
            │   ('john', 'smith', 'M', 1980),
        ┌───┴── ('first_name', 'last_name', 'F', 'a string'),
        │   ):
        ├────── first_name = a_person[0]    # 'first_name'
        ├────── last_name = a_person[1]     # 'last_name'
        ├────── year_of_birth = a_person[3] # 'a string'
        └────── self.assert_say_hello_works(
                    first_name=first_name,
                    last_name=last_name,
                    year_of_birth=year_of_birth,
                )
                └── def assert_say_hello_works(
                        self, first_name, last_name,
                        year_of_birth,
                    ):
                    └── try:
                            reality = src.person.say_hello(
                                first_name=first_name,
                                last_name=last_name,
                                year_of_birth=year_of_birth,
                            )
                            └── src/person/__init__.py
                                  └── def say_hello(
                                          first_name, last_name, year_of_birth,
                                      ):
                                      └── return (
                                          ├── f'Hello, my name is {first_name}'
                                          ├── f' {last_name} and I am'
                                          └── f' {calculate_age(year_of_birth)}.'
                                          )   │
                                              └── def calculate_age(year_of_birth):
                                                  ├── year_of_birth = 'a string'
                                                  └── if not isinstance(
                                                          year_of_birth, int
                                                      ):
                      ┌───────────────────────────────┴── raise TypeError('BOOM!!!')
                      └── except TypeError as error:
                          └── self.assertEqual(
                                  error.args[0],
                                  f"'{year_of_birth}' is not an integer"
                              )
                              └── raise AssertionError
                          else:
                              ...

* I undo the change

  .. code-block:: python
    :lineno-start: 37

    def calculate_age(year_of_birth):
        if not isinstance(year_of_birth, int):
            raise TypeError(
                f"'{year_of_birth}' is not an integer"
            )

        age = (
            datetime.date.today().year
          - year_of_birth
        )

        if age < 0 or age > 120:
            raise ValueError
        return age

  the test is green again.

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_say_hello_works method<extract assert_say_hello_works function>` from :ref:`test_joe` since it is now a repetition

  .. code-block:: python
    :lineno-start: 109

        def test_joe(self):
            first_name = 'joe'
            last_name = 'blow'
            sex = 'M'
            year_of_birth = 1996

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth
            )
            ...

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_say_hello_works method<extract assert_say_hello_works function>` from :ref:`test_jane` since it is now a repetition

  .. code-block:: python
    :lineno-start: 131

        def test_jane(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = 1991

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            ...

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_say_hello_works method<extract assert_say_hello_works function>` from :ref:`test_john` since it is now a repetition

  .. code-block:: python
    :lineno-start: 154

        def test_john(self):
            first_name = 'john'
            last_name = 'smith'
            sex = 'M'
            year_of_birth = 1980

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            ...

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_say_hello_works method<extract assert_say_hello_works function>` from :ref:`test_mary` since it is now a repetition

  .. code-block:: python
    :lineno-start: 178

        def test_mary(self):
            first_name = 'mary'
            last_name = 'public'
            sex = 'F'
            year_of_birth = 2000

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            ...

* I no longer need the :ref:`assert_say_hello_works method<extract assert_say_hello_works function>` because it is only used by :ref:`test_say_hello_function<extract test_say_hello_function>`

  .. code-block:: python
    :lineno-start: 63

        def test_say_hello_function(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a_string')
            )
            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                year_of_birth = a_person[3]

                self.assert_say_hello_works(
                    first_name=first_name,
                    last_name=last_name,
                    year_of_birth=year_of_birth,
                )

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 1-16

                try:
                    reality = src.person.say_hello(
                        first_name=first_name,
                        last_name=last_name,
                        year_of_birth=year_of_birth,
                    )
                except TypeError as error:
                    self.assertEqual(
                        error.args[0],
                        f"'{year_of_birth}' is not an integer"
                    )
                else:
                    self.assertEqual(
                        reality,
                        None
                    )

        def test_person_factory(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Hello, my name is jane doe and I am YY.' != None

* I change the expectation to ``'Hello, my name is jane doe and I am YY.'``

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 4

                else:
                    self.assertEqual(
                        reality,
                        'Hello, my name is jane doe and I am YY.'
                    )

        def test_person_factory(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Hello, my name is joe blow and I am XX.'
                 != 'Hello, my name is jane doe and I am YY.'

  because the :ref:`for loop<what is a for loop?>` moved to the next item in the ``people`` tuple_ (``'joe'``)

* I change the expectation to the :ref:`f-string<what is string interpolation?>` from the :ref:`assert_say_hello_works method<extract assert_say_hello_works function>`

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 4-8

                else:
                    self.assertEqual(
                        reality,
                        (
                            f'Hello, my name is {first_name}'
                            f' {last_name} and I am'
                            f' {self.calculate_age(year_of_birth)}.'
                        )
                    )

        def test_person_factory(self):

  the test passes.

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_say_hello_works method<extract assert_say_hello_works function>` from :ref:`test_say_hello_function<extract test_say_hello_function>`

  .. code-block:: python
    :lineno-start: 63

        def test_say_hello_function(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a_string')
            )
            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                year_of_birth = a_person[3]

  .. code-block:: python
    :lineno-start: 76

                try:
                    reality = src.person.say_hello(
                        first_name=first_name,
                        last_name=last_name,
                        year_of_birth=year_of_birth,
                    )
                except TypeError as error:
                    self.assertEqual(
                        error.args[0],
                        f"'{year_of_birth}' is not an integer"
                    )
                else:
                    self.assertEqual(
                        reality,
                        (
                            f'Hello, my name is {first_name}'
                            f' {last_name} and I am'
                            f' {self.calculate_age(year_of_birth)}.'
                        )
                    )

        def test_person_factory(self):

* I remove the :ref:`assert_say_hello_works method<extract assert_say_hello_works function>` from the :ref:`TestPerson class<add TestPerson object>`

  .. code-block:: python
    :lineno-start: 6

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year

        def calculate_age(self, year_of_birth):
            return self.this_year - year_of_birth

        def assert_person_can_say_hello(
                self,first_name, last_name,
                sex, year_of_birth,
            ):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract test_say_hello_function'

For each person in the ``people`` tuple_, this test :ref:`calls the say_hello function<test say_hello function>`

* If the :ref:`call raises TypeError<how to raise an Exception>`, it :ref:`asserts<what is an assertion?>` that the error message is correct

  - If the error message is not correct it raises :ref:`AssertionError<what causes AssertionError?>`

  - If the error message is correct the test passes

    .. code-block:: shell

              for a_person in (
              │   ('jane', 'doe', 'F', 1991),
              │   ('joe', 'blow', 'M', 1996),
              │   ('mary', 'public', 'F', 2000),
              │   ('john', 'smith', 'M', 1980),
          ┌───┴── ('first_name', 'last_name', 'F', 'a string'),
          │   ):
          ├────── first_name = a_person[0]    # 'first_name'
          ├────── last_name = a_person[1]     # 'last_name'
          ├────── year_of_birth = a_person[3] # 'a string'
          └────── try:
                      reality = src.person.say_hello(
                          first_name=first_name,
                          last_name=last_name,
                          year_of_birth=year_of_birth,
                      )
                      └── src/person/__init__.py
                            └── def say_hello(
                                    first_name, last_name, year_of_birth,
                                ):
                                ├── first_name    = 'first_name'  # a_person[0]
                                ├── last_name     = 'last_name'   # a_person[1]
                                ├── year_of_birth = 'a string'    # a_person[3]
                                └── return (
                                    ├── f'Hello, my name is {first_name}'
                                    ├── f' {last_name} and I am'
                                    └── f' {calculate_age(year_of_birth)}.'
                                    )   │
                                        └── def calculate_age(year_of_birth):
                                            ├── year_of_birth = 'a string'
                                            └── if not isinstance(
                                                    year_of_birth, int
                                                ):
              ┌─────────────────────────────────┴── raise TypeError(
              │                                       f"'{year_of_birth}'"
              │                                       " is not an integer"
              │                                   )
              └── except TypeError as error:
                  └── self.assertEqual(
                          error.args[0],
                          f"'{year_of_birth}' is not an integer"
                      )
                  else:
                      ...

* If the :ref:`call to the calculate_age function<extract calculate_age function>` from the :ref:`say_hello function<test say_hello function>` does not :ref:`raise TypeError<how to raise an Exception>`, it :ref:`asserts<what is an assertion?>` that the result of the :ref:`call<how to call a function with input>` matches the expectation

  .. code-block:: shell

          for person in (
          │   ('jane', 'doe', 'F', 1991),
          │   ('joe', 'blow', 'M', 1996),
          │   ('mary', 'public', 'F', 2000),
      ┌───┴── ('john', 'smith', 'M', 1980),
      │       ('first_name', 'last_name', 'F', 'a string'),
      │   ):
      ├────── first_name = a_person[0]    # 'john'
      ├────── last_name = a_person[1]     # 'smith'
      ├────── year_of_birth = a_person[3] # 1980
      └───┬── try:
          │       reality = src.person.say_hello(
          │           first_name=first_name,
          │           last_name=last_name,
          │           year_of_birth=year_of_birth,
          │       )
          │       └── src/person/__init__.py
          │             └── def say_hello(
          │                     first_name, last_name, year_of_birth,
          │                 ):
          │                 ├── first_name    = 'john'  # a_person[0]
          │                 ├── last_name     = 'smith' # a_person[1]
          │                 ├── year_of_birth = 1980    # a_person[3]
          │                 └── return (
          │                     ├── f'Hello, my name is {first_name}'
          │                     ├── f' {last_name} and I am'
          │                     └── f' {calculate_age(year_of_birth)}.'
          │                     )   │
          │                         └── def calculate_age(year_of_birth):
          │                             ├── year_of_birth = 1980 # a_person[3]
          │                             ├── ...
          │                             └── return age
          │   except TypeError as error:
          │       ...
          └── else:
              └── self.assertEqual(
                      reality,
                      (
                          f'Hello, my name is {first_name}'
                          f' {last_name} and I am'
                          f' {self.calculate_age(year_of_birth)}.'
                      )   │
                  )       └── def calculate_age(self, year_of_birth):
                              ├── year_of_birth = 1980  # a_person[3]
                              └── return self.this_year - year_of_birth

----

*********************************************************************************
extract test_say_hello_method
*********************************************************************************

The tests in :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` make an :ref:`instance<how to test if something is an instance>` of the :ref:`Person class<add Person object>`, then :ref:`call<how to call a function with input>` its :ref:`say_hello method<add say_hello method>` comparing the results in :ref:`assertions<what is an assertion?>`

.. code-block:: python

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

I can make one :ref:`function<what is a function?>` with a :ref:`for loop<what is a for loop?>` to remove the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the :ref:`say_hello method<add say_hello method>` of the :ref:`Person class<add Person object>`

.. code-block:: python
  :lineno-start: 13

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

.. code-block:: python
  :lineno-start: 31
  :emphasize-lines: 1-13, 15-20

        def test_say_hello_method(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a_string')
            )
            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]

                self.assert_person_can_say_hello(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth
                )

        def test_say_hello_function(self):

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  E           TypeError: 'a_string' is not an integer

this is the correct :ref:`Exception<how to test that an Exception is raised>` for when the ``year_of_birth`` is not an integer. I need :ref:`a better way to know which item in the people tuple raised the Exception<the subTest method>`.

----

*********************************************************************************
the subTest method
*********************************************************************************

:ref:`unittest.TestCase<test_dir_unittest_testcase>` has a :ref:`method<what is a method?>` that I can use to show what items in a :ref:`loop<what is a for loop?>` cause a failure in a test. It gives me a way to name each sub test in each loop.

* I add a :ref:`call<how to call a function with input>` to the `unittest.TestCase.subTest method`_ in :ref:`test_say_hello_method<extract test_say_hello_method>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 15-21

        def test_say_hello_method(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a_string')
            )
            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]

                with self.subTest(first_name=first_name):
                    self.assert_person_can_say_hello(
                        first_name=first_name,
                        last_name=last_name,
                        sex=sex,
                        year_of_birth=year_of_birth
                    )

        def test_say_hello_function(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :emphasize-text: SUBFAILED

    SUBFAILED(first_name='first_name') ...test_say_hello_method -
        TypeError: 'a string' is not an integer

  better. ``SUBFAILED(first_name='first_name')`` shows the value I gave in ``with self.subTest(first_name=first_name)`` as the label for the sub test. I can use any name and values I want.

* I add ``year_of_birth`` to the :ref:`call<how to call a function with input>` to the `subTest method`_

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 7-10

            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]

                with self.subTest(
                    first_name=first_name,
                    year_of_birth=year_of_birth,
                ):
                    self.assert_person_can_say_hello(
                        first_name=first_name,
                        last_name=last_name,
                        sex=sex,
                        year_of_birth=year_of_birth
                    )

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>` with the extra name and value.

  .. code-block:: python
    :emphasize-text: year_of_birth SUBFAILED

    SUBFAILED(first_name='first_name', year_of_birth='a string') ...
        test_say_hello_method - TypeError: 'a string' is not an integer

  this is clearer.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I move the statements in the :ref:`assert_person_can_say_hello method<extract assert_person_can_say_hello function>` to a :ref:`try...except...else clause<how to use try...except...else>` like I did for :ref:`test_say_hello_function<extract test_say_hello_function>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5-31

        def assert_person_can_say_hello(
                self,first_name, last_name,
                sex, year_of_birth,
            ):
            try:
                reality = src.person.Person(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                ).say_hello()
            except TypeError as error:
                self.assertEqual(
                    error.args[0],
                    f"'{year_of_birth}' is not an integer"
                )
            else:
                self.assertEqual(
                    reality,
                    # src.person.Person(
                    #     first_name=first_name,
                    #     last_name=last_name,
                    #     sex=sex,
                    #     year_of_birth=year_of_birth,
                    # ).say_hello(),
                    (
                        f'Hello, my name is {first_name}'
                        f' {last_name} and I am'
                        f' {self.calculate_age(year_of_birth)}.'
                    )
                )

        def test_say_hello_method(self):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the error message for if the value of the ``year_of_birth`` parameter is not an integer_ in the :ref:`calculate_age function<extract calculate_age function>`, in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 3

    def calculate_age(year_of_birth):
        if not isinstance(year_of_birth, int):
            raise TypeError('BAP!!!')
            raise TypeError(
                f"'{year_of_birth}' is not an integer"
            )

  the terminal_ is my friend, and shows :ref:`ASsertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: SUBFAILED

    SUBFAILED(first_name='first_name', year_of_birth='a string') ...
        test_say_hello_method - AssertionError:
            'BAP!!!' != "'a string' is not an integer"
    FAILED tests/test_person.py...
        test_say_hello_function - AssertionError:
            'BAP!!!' != "'a string' is not an integer"

  because the error messages do not match

  .. code-block:: shell

        for a_person in (
        │   ('jane', 'doe', 'F', 1991),
        │   ('joe', 'blow', 'M', 1996),
        │   ('mary', 'public', 'F', 2000),
        │   ('john', 'smith', 'M', 1980),
    ┌───┴── ('first_name', 'last_name', 'F', 'a string'),
    │   ):
    ├────── first_name = a_person[0]    # 'first_name'
    ├────── last_name = a_person[1]     # 'last_name'
    ├────── sex = a_person[2]           # 'F'
    ├────── year_of_birth = a_person[3] # 'a string'
    └────── with self.subTest(
                first_name=first_name,
                year_of_birth=year_of_birth,
            ):
            └── self.assert_person_can_say_hello(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth
                )
                └── def assert_person_can_say_hello(
                        self,first_name, last_name,
                        sex, year_of_birth,
                    ):
                    └── try:
                            reality = src.person.Person(
                                first_name=first_name,
                                last_name=last_name,
                                sex=sex,
                                year_of_birth=year_of_birth,
                            ).say_hello()
                            └── src/person/__init__.py
                                  └── class Person:
                                      └── def __init__(
                                              self, first_name, last_name,
                                              sex, year_of_birth=None,
                                              is_citizen=True, passed_test=False,
                                          ):
                                          ├── self.first_name = first_name
                                          ├── self.last_name = last_name
                                          ├── self.year_of_birth = year_of_birth
                                          ├── self.sex = sex
                                          ├── self.is_citizen = is_citizen
                                          ├── self.passed_test = passed_test
                                          └── self.age = calculate_age(
                                                  year_of_birth
                                              )
                                              └── def calculate_age(year_of_birth):
                                                  ├── year_of_birth = 'a string'
                                                  └── if not isinstance(
                                                          year_of_birth, int
                                                      ):
                    ┌─────────────────────────────────┴── raise TypeError('BAP!!!')
                    └── except TypeError as error:
                        └── self.assertEqual(
                                error.args[0],
                                f"'{year_of_birth}' is not an integer"
                            )
                            └── raise AssertionError
                        else:
                            ...

* I want :ref:`test_say_hello_function<extract test_say_hello_function>` to also show which person :ref:`raises an Exception<how to raise an Exception>`. I add a :ref:`call<how to call a function with input>` to the `subTest method`_ from :ref:`test_say_hello_function<extract test_say_hello_function>` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 70

        def test_say_hello_function(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a_string')
            )
            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                year_of_birth = a_person[3]

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 1-24

                with self.subTest(
                    first_name=first_name,
                    year_of_birth=year_of_birth,
                ):
                    try:
                        reality = src.person.say_hello(
                            first_name=first_name,
                            last_name=last_name,
                            year_of_birth=year_of_birth,
                        )
                    except TypeError as error:
                        self.assertEqual(
                            error.args[0],
                            f"'{year_of_birth}' is not an integer"
                        )
                    else:
                        self.assertEqual(
                            reality,
                            (
                                f'Hello, my name is {first_name}'
                                f' {last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )

        def test_person_factory(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with the first name and year_of_birth of the person that :ref:`raised the Exception<how to raise an Exception>`

  .. code-block:: python
    :emphasize-text: SUBFAILED year_of_birth

    SUBFAILED(first_name='first_name', year_of_birth='a string') ...
        test_say_hello_method - AssertionError:
            'BAP!!!' != "'a string' is not an integer"
    SUBFAILED(first_name='first_name', year_of_birth='a string') ...
        test_say_hello_function - AssertionError:
            'BAP!!!' != "'a string' is not an integer"

* I change the error message in the :ref:`calculate_age function<extract calculate_age function>` for if the value of the ``year_of_birth`` parameter is not an integer_ back to the correct message, in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 37

    def calculate_age(year_of_birth):
        if not isinstance(year_of_birth, int):
            raise TypeError(
                f"'{year_of_birth}' is not an integer"
            )

  the tests are green again.

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_person_can_say_hello<extract assert_person_can_say_hello function>` from :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 135

        def test_joe(self):
            first_name = 'joe'
            last_name = 'blow'
            sex = 'M'
            year_of_birth = 1996

            joe = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            self.assertEqual(joe.can_vote(), True)
            self.assertEqual(joe.can_get_license(), False)

        def test_jane(self):

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_person_can_say_hello<extract assert_person_can_say_hello function>` from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 150

        def test_jane(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = 1991

            jane = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                passed_test=True,
            )
            self.assertEqual(jane.can_vote(), True)
            self.assertEqual(jane.can_get_license(), True)

        def test_john(self):

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_person_can_say_hello<extract assert_person_can_say_hello function>` from :ref:`test_john`

  .. code-block:: python
    :lineno-start: 166

        def test_john(self):
            first_name = 'john'
            last_name = 'smith'
            sex = 'M'
            year_of_birth = 1980

            john = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                is_citizen=False,
                passed_test=False,
            )
            self.assertEqual(john.can_vote(), False)
            self.assertEqual(john.can_get_license(), False)

        def test_mary(self):

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_person_can_say_hello<extract assert_person_can_say_hello function>` from :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 183

        def test_mary(self):
            first_name = 'mary'
            last_name = 'public'
            sex = 'F'
            year_of_birth = 2000

            mary = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                is_citizen=False,
                passed_test=True,
            )
            self.assertEqual(mary.can_vote(), False)
            self.assertEqual(mary.can_get_license(), True)

        def test_underage_citizen(self):

* I no longer need the :ref:`assert_person_can_say_hello method<extract assert_person_can_say_hello function>` because it is only used by :ref:`test_say_hello_method<extract test_say_hello_method>`

  .. code-block:: python
    :lineno-start: 45

        def test_say_hello_method(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a_string')
            )
            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]

  .. code-block:: python
    :lineno-start: 59

                with self.subTest(
                    first_name=first_name,
                    year_of_birth=year_of_birth,
                ):
                    self.assert_person_can_say_hello(
                        first_name=first_name,
                        last_name=last_name,
                        sex=sex,
                        year_of_birth=year_of_birth
                    )


  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 1-17

                    try:
                        reality = src.person.Person(
                            first_name=first_name,
                            last_name=last_name,
                            sex=sex,
                            year_of_birth=year_of_birth,
                        ).say_hello()
                    except TypeError as error:
                        self.assertEqual(
                            error.args[0],
                            f"'{year_of_birth}' is not an integer"
                        )
                    else:
                        self.assertEqual(
                            reality,
                            None
                        )

        def test_say_hello_function(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for each one of the people with an integer_ for ``year_of_birth``

  .. code-block:: python

    SUBFAILED(first_name='jane', year_of_birth=1991) ... -
        AssertionError: 'Hello, my name is jane doe and I am YY.' != None
    SUBFAILED(first_name='joe', year_of_birth=1996) ... -
        AssertionError: 'Hello, my name is joe blow and I am XX.' != None
    SUBFAILED(first_name='mary', year_of_birth=2000) ... -
        AssertionError: 'Hello, my name is mary public and I am ZZ.' != None
    SUBFAILED(first_name='john', year_of_birth=1980) ... -
        AssertionError: 'Hello, my name is john smith and I am AA.' != None

* I change the expectation of the :ref:`assertion<what is an assertion?>` to ``'Hello, my name is jane doe and I am YY.'``

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 4

                    else:
                        self.assertEqual(
                            reality,
                            'Hello, my name is jane doe and I am YY.'
                        )

        def test_say_hello_function(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(first_name='joe', year_of_birth=1996) ...test_say_hello_method -
        AssertionError: 'Hello, my name is joe blow and I am XX.'
                     != 'Hello, my name is jane doe and I am YY.'
    SUBFAILED(first_name='mary', year_of_birth=2000) ...test_say_hello_method -
        AssertionError: 'Hello, my name is mary public and I am ZZ.'
                     != 'Hello, my name is jane doe and I am YY.'
    SUBFAILED(first_name='john', year_of_birth=1980) ...test_say_hello_method -
        AssertionError: 'Hello, my name is john smith and I am AA.'
                     != 'Hello, my name is jane doe and I am YY.'.

  the :ref:`assertion<what is an assertion?>` now fails for the other people in the ``people`` tuple_.

* I change the expectation to the :ref:`f-string<what is string interpolation?>` from the :ref:`assert_person_can_say_hello method<extract assert_person_can_say_hello function>`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 4-8

                    else:
                        self.assertEqual(
                            reality,
                            (
                                f'Hello, my name is {first_name}'
                                f' {last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )

        def test_say_hello_function(self):

  the test passes.

* I remove the :ref:`call<how to call a function with input>` to the :ref:`assert_person_factory_works method<extract assert_person_factory_works function>` from :ref:`test_say_hello_method<extract test_say_hello_method>`

  .. code-block:: python
    :lineno-start: 45

        def test_say_hello_method(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a_string')
            )
            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]

  .. code-block:: python
    :lineno-start: 59

                with self.subTest(
                    first_name=first_name,
                    year_of_birth=year_of_birth,
                ):
                    try:
                        reality = src.person.Person(
                            first_name=first_name,
                            last_name=last_name,
                            sex=sex,
                            year_of_birth=year_of_birth,
                        ).say_hello()
                    except TypeError as error:
                        self.assertEqual(
                            error.args[0],
                            f"'{year_of_birth}' is not an integer"
                        )
                    else:
                        self.assertEqual(
                            reality,
                            (
                                f'Hello, my name is {first_name}'
                                f' {last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )

        def test_say_hello_function(self):

* I remove the :ref:`assert_person_can_say_hello method<extract assert_person_can_say_hello function>` from the :ref:`TestPerson class<add TestPerson object>`

  .. code-block:: python
    :lineno-start: 6

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year

        def calculate_age(self, year_of_birth):
            return self.this_year - year_of_birth

        def test_say_hello_method(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract test_say_hello_method'

For each person in the ``people`` tuple_, this test :ref:`makes an instance<how to test if something is an instance>` of the :ref:`Person class<add Person object>` which makes an ``age`` :ref:`attribute<what is an object attribute?>` by :ref:`calling<how to call a function with input>` the :ref:`calculate_age function<extract calculate_age function>` with the given ``year_of_birth`` parameter.

* If the :ref:`call raises TypeError<how to raise an Exception>`, it :ref:`asserts<what is an assertion?>` that the error message is correct

  - If the error message is not correct, it raises :ref:`AssertionError<what causes AssertionError?>`

  - If the error message is correct, the test passes

    .. code-block:: shell

          for a_person in (
          │   ('jane', 'doe', 'F', 1991),
          │   ('joe', 'blow', 'M', 1996),
          │   ('mary', 'public', 'F', 2000),
          │   ('john', 'smith', 'M', 1980),
      ┌───┴── ('first_name', 'last_name', 'F', 'a string'),
      │   ):
      ├────── first_name = a_person[0]    # 'first_name'
      ├────── last_name = a_person[1]     # 'last_name'
      ├────── sex = a_person[2]           # 'F'
      ├────── year_of_birth = a_person[3] # 'a string'
      └────── with self.subTest(
                  first_name=first_name,
                  year_of_birth=year_of_birth,
              ):
              └── try:
                      reality = src.person.Person(
                          first_name=first_name,
                          last_name=last_name,
                          sex=sex,
                          year_of_birth=year_of_birth,
                      ).say_hello()
                      └── src/person/__init__.py
                            └── class Person:
                                └── def __init__(
                                        self, first_name, last_name,
                                        sex, year_of_birth=None,
                                        is_citizen=True, passed_test=False,
                                    ):
                                    ├── self.first_name = first_name
                                    ├── self.last_name = last_name
                                    ├── self.year_of_birth = year_of_birth
                                    ├── self.sex = sex
                                    ├── self.is_citizen = is_citizen
                                    ├── self.passed_test = passed_test
                                    └── self.age = calculate_age(
                                            year_of_birth
                                        )
                                        └── def calculate_age(year_of_birth):
                                            ├── year_of_birth = 'a string'
                                            └── if not isinstance(
                                                    year_of_birth, int
                                                ):
              ┌─────────────────────────────────┴── raise TypeError(
              │                                        f"'{year_of_birth}'"
              │                                        " is not an integer"
              │                                     )
              └── except TypeError as error:
                  └── self.assertEqual(
                          error.args[0],
                          f"'{year_of_birth}' is not an integer"
                      )
                  else:
                      ...

* If the :ref:`call to the calculate_age function<extract calculate_age function>` from the :ref:`__init__ method<the constructor method>` of the :ref:`Person class<add Person object>` does not :ref:`raise TypeError<how to raise an Exception>`, it :ref:`asserts<what is an assertion?>` that the result of the :ref:`call to the say_hello method<add say_hello method>` matches the expectation

  .. code-block:: shell

        for person in (
        │   ('jane', 'doe', 'F', 1991),
    ┌───┴── ('joe', 'blow', 'M', 1996),
    │       ('mary', 'public', 'F', 2000),
    │       ('john', 'smith', 'M', 1980),
    │       ('first_name', 'last_name', 'F', 'a string'),
    │   ):
    ├────── first_name = a_person[0]    # 'joe'
    ├────── last_name = a_person[1]     # 'blow'
    ├────── sex = a_person[2]           # 'M'
    ├────── year_of_birth = a_person[3] # 1996
    └────── with self.subTest(
                first_name=first_name,
                year_of_birth=year_of_birth,
            ):
            ├── try:
            │       reality = src.person.Person(
            │           first_name=first_name,
            │           last_name=last_name,
            │           sex=sex,
            │           year_of_birth=year_of_birth,
            │       ).say_hello()
            │       ├── src/person/__init__.py
            │       │    └── class Person:
            │       │        └── def __init__(
            │       │               self, first_name, last_name,
            │       │               sex, year_of_birth=None,
            │       │               is_citizen=True, passed_test=False,
            │       │            ):
            │       │            ├── self.first_name = first_name
            │       │            ├── self.last_name = last_name
            │       │            ├── self.year_of_birth = year_of_birth
            │       │            ├── self.sex = sex
            │       │            ├── self.is_citizen = is_citizen
            │       │            ├── self.passed_test = passed_test
            │       │            └── self.age = calculate_age(
            │       │                   year_of_birth
            │       │                )
            │       │                └── def calculate_age(year_of_birth):
            │       │                    ├── year_of_birth = 'a string'
            │       │                    └── if not isinstance(
            │       │                           year_of_birth, int
            │       │                        ):
            │       │                        └── def calculate_age(year_of_birth):
            │       │                            ├── year_of_birth = 1996
            │       │                            ├── ...
            │       │                            └── return age
            │       └── def say_hello(self):
            │           └── return (
            │                   f'Hello, my name is {self.first_name}'
            │                   f' {self.last_name} and I am {self.age}.'
            │               )
            ├── except TypeError as error:
            │       ...
            └── else:
                └── self.assertEqual(
                        reality,
                        (
                            f'Hello, my name is {first_name}'
                            f' {last_name} and I am'
                            f' {self.calculate_age(year_of_birth)}.'
                        )
                    )   │
                        └── def calculate_age(self, year_of_birth):
                            ├── year_of_birth = 1996
                            └── return self.this_year - year_of_birth

----

*********************************************************************************
extract people object attribute
*********************************************************************************

:ref:`test_person_factory<extract test_person_factory>`, :ref:`test_say_hello_function<extract test_say_hello_function>` and :ref:`test_say_hello_method<extract test_say_hello_method>` all use the same tuple_ of persons.

* I add an :ref:`object attribute<what is an object attribute?>` for the ``people`` tuple_ to the :ref:`TestPerson class<add TestPerson object>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4-10

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year
        people = (
            ('jane', 'doe', 'F', 1991),
            ('joe', 'blow', 'M', 1996),
            ('mary', 'public', 'F', 2000),
            ('john', 'smith', 'M', 1980),
            ('first_name', 'last_name', 'F', 'a_string')
        )

        def calculate_age(self, year_of_birth):

* I use the :ref:`object attribute<what is an object attribute?>` for ``people`` in the :ref:`for loop<what is a for loop?>` in :ref:`test_say_hello_method<extract test_say_hello_method>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 2-10

        def test_say_hello_method(self):
            # people = (
            #     ('jane', 'doe', 'F', 1991),
            #     ('joe', 'blow', 'M', 1996),
            #     ('mary', 'public', 'F', 2000),
            #     ('john', 'smith', 'M', 1980),
            #     ('first_name', 'last_name', 'F', 'a_string')
            # )
            # for a_person in people:
            for a_person in self.people:
                first_name = a_person[0]

  the test is still green.

* I remove the commented lines from :ref:`test_say_hello_method<extract test_say_hello_method>`

  .. code-block:: python
    :lineno-start: 20

        def test_say_hello_method(self):
            for a_person in self.people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]
                ...

* I use the :ref:`object attribute<what is an object attribute?>` for ``people`` in the :ref:`for loop<what is a for loop?>` in :ref:`test_say_hello_function<extract test_say_hello_function>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2-10

        def test_say_hello_function(self):
            # people = (
            #     ('jane', 'doe', 'F', 1991),
            #     ('joe', 'blow', 'M', 1996),
            #     ('mary', 'public', 'F', 2000),
            #     ('john', 'smith', 'M', 1980),
            #     ('first_name', 'last_name', 'F', 'a_string')
            # )
            # for a_person in people:
            for a_person in self.people:
                first_name = a_person[0]

  still green.

* I remove the commented lines from :ref:`test_say_hello_function<extract test_say_hello_function>`

  .. code-block:: python
    :lineno-start: 53

        def test_say_hello_function(self):
            for a_person in self.people:
                first_name = a_person[0]
                last_name = a_person[1]
                year_of_birth = a_person[3]
                ...

* I use the :ref:`object attribute<what is an object attribute?>` for ``people`` in the :ref:`for loop<what is a for loop?>` in :ref:`test_person_factory<extract test_person_factory>`

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2-10

        def test_person_factory(self):
            # people = (
            #     ('jane', 'doe', 'F', 1991),
            #     ('joe', 'blow', 'M', 1996),
            #     ('mary', 'public', 'F', 2000),
            #     ('john', 'smith', 'M', 1980),
            #     ('first_name', 'last_name', 'F', 'a_string')
            # )
            # for a_person in people:
            for a_person in self.people:
                first_name = a_person[0]

  the test is still green.

* I remove the commented lines from :ref:`test_person_factory<extract test_person_factory>`

  .. code-block:: python
    :lineno-start: 84

        def test_person_factory(self):
            for a_person in self.people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]
                ...

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract people object attribute'

----

*********************************************************************************
extract test_if_person_can_vote
*********************************************************************************

The tests in :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john`, :ref:`test_mary` and :ref:`test_underage_citizen<add condition to can_vote>` make an :ref:`instance<how to test if something is an instance>` of the :ref:`Person class<add Person object>`, then :ref:`call<how to call a function with input>` its :ref:`can_vote method<add can_vote method>` comparing the results in :ref:`assertions<what is an assertion?>`.

.. code-block:: python

    an_instance = src.person.Person(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
        is_citizen=False | True,
        passed_test=False | True,
    )
    self.assertEqual(an_instance.can_vote(), False | True)

I can make one :ref:`function<what is a function?>` with a :ref:`for loop<what is a for loop?>` to remove the repetition.

The :ref:`can_vote method of the Person class<add can_vote method>` sends two parameters (``age`` and ``response``) when it :ref:`calls the check_age method<extract check_age method>` to return :red:`False` or :green:`True` for if a person :red:`cannot vote` or :green:`can vote` based on the following inputs

* is the person younger than 18?
* is the person a citizen?

The :ref:`truth table` for the :ref:`can_vote method<add can_vote method>` is

==============  ============== ==============
age < 18        is citizen     can vote
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
:green:`True`   :red:`False`   :red:`False`
:red:`False`    :green:`True`  :green:`True`
:red:`False`    :red:`False`   :red:`False`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for if a person is :green:`younger` than ``18`` AND is a :green:`citizen`

==============  ============== ==============
age < 18        is citizen     can vote
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
==============  ============== ==============

.. code-block:: python
  :lineno-start: 84

        def test_person_factory(self):
            for a_person in self.people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]

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

.. code-block:: python
  :lineno-start: 104
  :emphasize-lines: 1-14

        def test_if_person_can_vote(self):
            truth_table = (
                (datetime.date.today().year-17, True),
            )
            for row in truth_table:
                with self.subTest(row=row):
                    an_instance = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='F',
                        year_of_birth=row[0],
                        is_citizen=row[1],
                    )
                    self.assertEqual(an_instance.can_vote(), True)

        def test_joe(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  SUBFAILED(row=(2009, True)) ...AssertionError: False != True

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :green:`True` to :red:`False` in the :ref:`assertion<what is an assertion?>` for if a person is :green:`younger` than ``18`` AND is a :green:`citizen`

.. code-block:: python
  :lineno-start: 104
  :emphasize-lines: 14

      def test_if_person_can_vote(self):
          truth_table = (
              (datetime.date.today().year-17, True),
          )
          for row in truth_table:
              with self.subTest(row=row):
                  an_instance = src.person.Person(
                      first_name='first_name',
                      last_name='last_name',
                      sex='F',
                      year_of_birth=row[0],
                      is_citizen=row[1],
                  )
                  self.assertEqual(an_instance.can_vote(), False)

      def test_joe(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a tuple_ to the ``truth_table`` tuple_ for if a person is :green:`younger` than ``18`` AND is :red:`NOT a citizen`

  ==============  ============== ==============
  age < 18        is citizen     can vote
  ==============  ============== ==============
  :green:`True`   :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 4

        def test_if_person_can_vote(self):
            truth_table = (
                (datetime.date.today().year-17, True),
                (datetime.date.today().year-17, False),
            )
            for row in truth_table:

  the test is still green.

* I add a tuple_ to the ``truth_table`` tuple_ for if a person is :red:`NOT younger` than ``18`` AND is a :green:`citizen`

  ==============  ============== ==============
  age < 18        is citizen     can vote
  ==============  ============== ==============
  :red:`False`    :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 5

        def test_if_person_can_vote(self):
            truth_table = (
                (datetime.date.today().year-17, True),
                (datetime.date.today().year-17, False),
                (datetime.date.today().year-18, True),
            )
            for row in truth_table:

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(row=(2008, True)) ...test_if_person_can_vote -
        AssertionError: True != False

* I add the expectation to the tuples_ for the rows in the ``truth_table`` tuple_

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 3-5

        def test_if_person_can_vote(self):
            truth_table = (
                (datetime.date.today().year-17, True, False),
                (datetime.date.today().year-17, False, False),
                (datetime.date.today().year-18, True, True),
            )
            for row in truth_table:

* I use the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of the new values as the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 10

            for row in truth_table:
                with self.subTest(row=row):
                    an_instance = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='F',
                        year_of_birth=row[0],
                        is_citizen=row[1],
                    )
                    self.assertEqual(an_instance.can_vote(), row[3])

    def test_joe(self):

  the terminal_ is my friend, and shows :ref:`IndexError<test_index_error>`

  .. code-block:: python
    :emphasize-text: SUBFAILED

    SUBFAILED(row=(2009, True, False)) ...test_if_person_can_vote -
        IndexError: tuple index out of range
    SUBFAILED(row=(2009, False, False)) ...test_if_person_can_vote -
        IndexError: tuple index out of range
    SUBFAILED(row=(2008, True, True)) ...test_if_person_can_vote -
        IndexError: tuple index out of range

* I change the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` to the right number

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 1

                    self.assertEqual(an_instance.can_vote(), row[2])

  the test passes.

* I add a tuple_ to the ``truth_table`` tuple_ for if a person is :red:`NOT younger` than ``18`` AND is :red:`NOT a citizen`

  ==============  ============== ==============
  age < 18        is citizen     can vote
  ==============  ============== ==============
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 6

        def test_if_person_can_vote(self):
            truth_table = (
                (datetime.date.today().year-17, True, False),
                (datetime.date.today().year-17, False, False),
                (datetime.date.today().year-18, True, True),
                (datetime.date.today().year-18, False, False),
            )
            for row in truth_table:
                with self.subTest(row=row):
                    an_instance = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='F',
                        year_of_birth=row[0],
                        is_citizen=row[1],
                    )
                    self.assertEqual(
                        an_instance.can_vote(), row[2]
                    )

        def test_joe(self):

  still green.

* I remove the :ref:`assertion<what is an assertion?>` for the :ref:`can_vote method<add can_vote method>` from :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 122

        def test_joe(self):
            first_name = 'joe'
            last_name = 'blow'
            sex = 'M'
            year_of_birth = 1996

            joe = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            self.assertEqual(joe.can_get_license(), False)

        def test_jane(self):

* I remove the :ref:`assertion<what is an assertion?>` for the :ref:`can_vote method<add can_vote method>` from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 136

        def test_jane(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = 1991

            jane = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                passed_test=True,
            )
            self.assertEqual(jane.can_get_license(), True)

        def test_john(self):

* I remove the :ref:`assertion<what is an assertion?>` for the :ref:`can_vote method<add can_vote method>` from :ref:`test_john`

  .. code-block:: python
    :lineno-start: 151

        def test_john(self):
            first_name = 'john'
            last_name = 'smith'
            sex = 'M'
            year_of_birth = 1980

            john = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                is_citizen=False,
                passed_test=False,
            )
            self.assertEqual(john.can_get_license(), False)

        def test_mary(self):

* I remove the :ref:`assertion<what is an assertion?>` for the :ref:`can_vote method<add can_vote method>` from :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 167

        def test_mary(self):
            first_name = 'mary'
            last_name = 'public'
            sex = 'F'
            year_of_birth = 2000

            mary = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                is_citizen=False,
                passed_test=True,
            )
            self.assertEqual(mary.can_get_license(), True)

        def test_underage_citizen(self):

* I remove the :ref:`assertion<what is an assertion?>` for the :ref:`can_vote method<add can_vote method>` from :ref:`test_underage_citizen<add condition to can_vote>`

  .. code-block:: python
    :lineno-start: 183

        def test_underage_citizen(self):
            underage = src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=self.this_year-17,
                is_citizen=True,
                passed_test=True,
            )
            self.assertEqual(underage.can_get_license(), False)

        def test_when_person_is_older_than_120(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract test_if_person_can_vote'

----

*********************************************************************************
extract test_if_person_can_get_license
*********************************************************************************

The tests in :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john`, :ref:`test_mary` and :ref:`test_underage_citizen<add condition to can_vote>`  make an :ref:`instance<how to test if something is an instance>` of the :ref:`Person class<add Person object>`, then :ref:`call<how to call a function with input>` its :ref:`can_get_license method<add can_get_license method>` comparing the results in :ref:`assertions<what is an assertion?>`.

.. code-block:: python

    an_instance = src.person.Person(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
        is_citizen=False | True,
        passed_test=False | True,
    )
    self.assertEqual(
        an_instance.can_get_license(), False | True
    )

I can make one :ref:`function<what is a function?>` with a :ref:`for loop<what is a for loop?>` to remove the repetition.

The :ref:`can_get_license method of the Person class<add can_get_license method>` also sends two parameters when it :ref:`calls the check_age method<extract check_age method>` to return :red:`False` or :green:`True` for if a person :red:`cannot get a license` or :green:`can get a license` based on the following inputs

* is the person younger than 18?
* did the person pass the test?

The :ref:`truth table` for the :ref:`can_get_license<add can_get_license method>` is

==============  ============== ================
age < 18        passed test    can get license
==============  ============== ================
:green:`True`   :green:`True`  :red:`False`
:green:`True`   :red:`False`   :red:`False`
:red:`False`    :green:`True`  :green:`True`
:red:`False`    :red:`False`   :red:`False`
==============  ============== ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for if a person is :red:`NOT younger` than ``18`` AND has :red:`NOT passed` the test

==============  ============== ================
age < 18        passed test    can get license
==============  ============== ================
:red:`False`    :red:`False`   :red:`False`
==============  ============== ================

.. code-block:: python
  :lineno-start: 120
  :emphasize-lines: 3-18

                    self.assertEqual(an_instance.can_vote(), row[2])

        def test_if_person_can_get_license(self):
            truth_table = (
                (datetime.date.today().year-18, False, False),
            )
            for row in truth_table:
                with self.subTest(row=row):
                    an_instance = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=row[0],
                        passed_test=row[1],
                    )
                    self.assertEqual(
                        an_instance.can_get_license(), True
                    )

        def test_joe(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :emphasize-text: SUBFAILED

  SUBFAILED(row=(2008, False, False)) ...test_if_person_can_get_license
      - AssertionError: False != True

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation of the :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :lineno-start: 135
  :emphasize-lines: 2

                  self.assertEqual(
                      an_instance.can_get_license(), False
                  )

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a tuple_ to the ``truth_table`` tuple_ for if a person is :red:`NOT younger` than ``18`` AND has :green:`passed` the test

  ==============  ============== ================
  age < 18        passed test    can get license
  ==============  ============== ================
  :red:`False`    :green:`True`  :green:`True`
  ==============  ============== ================

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 3

        def test_if_person_can_get_license(self):
            truth_table = (
                (datetime.date.today().year-18, True, True),
                (datetime.date.today().year-18, False, False),
            )
            for row in truth_table:

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(row=(2008, True, True)) ...
        test_if_person_can_get_license - AssertionError:
            True != False

* I use the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` to change the expectation to the last item of the ``row`` tuple_

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 2

                    self.assertEqual(
                        an_instance.can_get_license(), row[-1]
                    )

        def test_joe(self):

  the test passes.

* I add a tuple_ to the ``truth_table`` tuple_ for if a person is :green:`younger` than ``18`` AND has :red:`NOT passed` the test

  ==============  ============== ================
  age < 18        passed test    can get license
  ==============  ============== ================
  :green:`True`   :red:`False`   :red:`False`
  ==============  ============== ================

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 3

        def test_if_person_can_get_license(self):
            truth_table = (
                (datetime.date.today().year-17, False, False),
                (datetime.date.today().year-18, True, True),
                (datetime.date.today().year-18, False, False),
            )
            for row in truth_table:

  the test is still green.

* I add a tuple_ to the ``truth_table`` tuple_ for if a person is :green:`younger` than ``18`` AND has :green:`passed` the test

  ==============  ============== ================
  age < 18        passed test    can get license
  ==============  ============== ================
  :green:`True`   :green:`True`  :red:`False`
  ==============  ============== ================

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 3

        def test_if_person_can_get_license(self):
            truth_table = (
                (datetime.date.today().year-17, True, False),
                (datetime.date.today().year-17, False, False),
                (datetime.date.today().year-18, True, True),
                (datetime.date.today().year-18, False, False),
            )
            for row in truth_table:

  still green.

* I remove :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john`, :ref:`test_mary` and :ref:`test_underage_citizen<add condition to can_vote>`  since they are now repetitions of :ref:`test_if_person_can_get_license<extract test_if_person_can_get_license>`

  .. code-block:: python
    :lineno-start: 122

        def test_if_person_can_get_license(self):
            truth_table = (
                (datetime.date.today().year-17, True, False),
                (datetime.date.today().year-17, False, False),
                (datetime.date.today().year-18, True, True),
                (datetime.date.today().year-18, False, False),
            )
            for row in truth_table:
                with self.subTest(row=row):
                    an_instance = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=row[0],
                        passed_test=row[1],
                    )
                    self.assertEqual(
                        an_instance.can_get_license(), row[-1]
                    )

        def test_when_person_is_older_than_120(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract test_if_person_can_get_license'

----

*********************************************************************************
extract truth_table object attribute
*********************************************************************************

The ``truth_table`` tuple_ is used in both :ref:`test_if_person_can_vote<extract test_if_person_can_vote>` and :ref:`test_if_person_can_get_license<extract test_if_person_can_get_license>`. I can make an :ref:`object attribute<what is an object attribute?>` to remove the repetition.

* I add an :ref:`object attribute<what is an object attribute?>` for the ``truth_table`` tuple_ to the :ref:`TestPerson class<add TestPerson object>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 11-16

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year
        people = (
            ('jane', 'doe', 'F', 1991),
            ('joe', 'blow', 'M', 1996),
            ('mary', 'public', 'F', 2000),
            ('john', 'smith', 'M', 1980),
            ('first_name', 'last_name', 'F', 'a_string')
        )
        truth_table = (
            (datetime.date.today().year-17, True, False),
            (datetime.date.today().year-17, False, False),
            (datetime.date.today().year-18, True, True),
            (datetime.date.today().year-18, False, False),
        )

        def calculate_age(self, year_of_birth):

* I use the :ref:`object attribute<what is an object attribute?>` for ``truth_table`` in the :ref:`for loop<what is a for loop?>` in :ref:`test_if_person_can_vote<extract test_if_person_can_vote>`

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 2-9

        def test_if_person_can_vote(self):
            # truth_table = (
            #     (datetime.date.today().year-17, True, False),
            #     (datetime.date.today().year-17, False, False),
            #     (datetime.date.today().year-18, True, True),
            #     (datetime.date.today().year-18, False, False),
            # )
            # for row in truth_table:
            for row in self.truth_table:
                with self.subTest(row=row):

  the test is still green.

* I remove the commented lines from :ref:`test_if_person_can_vote<extract test_if_person_can_vote>`

  .. code-block:: python
    :lineno-start: 110

        def test_if_person_can_vote(self):
            for row in self.truth_table:
                with self.subTest(row=row):
                    an_instance = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='F',
                        year_of_birth=row[0],
                        is_citizen=row[1],
                    )
                    self.assertEqual(an_instance.can_vote(), row[2])

        def test_if_person_can_get_license(self):

* I use the :ref:`object attribute<what is an object attribute?>` for ``truth_table`` in the :ref:`for loop<what is a for loop?>` in :ref:`test_if_person_can_get_license<extract test_if_person_can_get_license>`

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines:

        def test_if_person_can_get_license(self):
            # truth_table = (
            #     (datetime.date.today().year-17, True, False),
            #     (datetime.date.today().year-17, False, False),
            #     (datetime.date.today().year-18, True, True),
            #     (datetime.date.today().year-18, False, False),
            # )
            # for row in truth_table:
            for row in self.truth_table:
                with self.subTest(row=row):

  still green.

* I remove the commented lines from :ref:`test_if_person_can_vote<extract test_if_person_can_vote>`

  .. code-block:: python
    :lineno-start: 122

        def test_if_person_can_get_license(self):
            for row in self.truth_table:
                with self.subTest(row=row):
                    an_instance = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=row[0],
                        passed_test=row[1],
                    )
                    self.assertEqual(
                        an_instance.can_get_license(), row[-1]
                    )

        def test_when_person_is_older_than_120(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract truth_table object attribute'

----

*********************************************************************************
extract test_person_class
*********************************************************************************

:ref:`test_say_hello_method<extract test_say_hello_method>`, :ref:`test_if_person_can_vote<extract test_if_person_can_vote>` and :ref:`test_if_person_can_get_license<extract test_if_person_can_get_license>` make an :ref:`instance<how to test if something is an instance>` of the :ref:`Person class<add Person object>`, then :ref:`call methods<how to call a function with input>` and compare the results in :ref:`assertions<what is an assertion?>`

.. code-block:: python

  reality = src.person.Person(
      first_name=first_name,
      last_name=last_name,
      sex=sex,
      year_of_birth=year_of_birth,
  ).say_hello()

  self.assertEqual(
      reality,
      (
          f'Hello, my name is {first_name}'
          f' {last_name} and I am'
          f' {self.calculate_age(year_of_birth)}.'
      )
  )

.. code-block:: python

  an_instance = src.person.Person(
      first_name='first_name',
      last_name='last_name',
      sex='M',
      year_of_birth=row[0],
      passed_test=row[1],
  )
  self.assertEqual(an_instance.can_vote(), row[2])
  self.assertEqual(an_instance.can_get_license(), row[-1])

I can make one :ref:`function<what is a function?>` with a :ref:`for loop<what is a for loop?>` to remove the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with the code from :ref:`test_say_hello_method<extract test_say_hello method>` for the :ref:`Person class<add Person object>`

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 4-9

    def calculate_age(self, year_of_birth):
        return self.this_year - year_of_birth

    def test_person_class(self):
        for a_person in self.people:
            first_name = a_person[0]
            last_name = a_person[1]
            sex = a_person[2]
            year_of_birth = a_person[3]

.. code-block:: python
  :lineno-start: 33
  :emphasize-lines: 1-25

            with self.subTest(
                first_name=first_name,
                year_of_birth=year_of_birth,
            ):
                try:
                    an_instance = src.person.Person(
                        first_name=first_name,
                        last_name=last_name,
                        sex=sex,
                        year_of_birth=year_of_birth,
                    )
                except TypeError as error:
                    self.assertEqual(
                        error.args[0],
                        f"'{year_of_birth}' is not an integer"
                    )
                else:
                    self.assertEqual(
                        an_instance.boom(),
                        (
                            f'Hello, my name is {first_name}'
                            f' {last_name} and I am'
                            f' {self.calculate_age(year_of_birth)}.'
                        )
                    )

    def test_say_hello_method(self):

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  SUBFAILED(first_name='jane', year_of_birth=1991)
      AttributeError: 'Person' object has no attribute 'boom'
  SUBFAILED(first_name='joe', year_of_birth=1996)
      AttributeError: 'Person' object has no attribute 'boom'
  SUBFAILED(first_name='mary', year_of_birth=2000)
      AttributeError: 'Person' object has no attribute 'boom'
  SUBFAILED(first_name='john', year_of_birth=1980)
      AttributeError: 'Person' object has no attribute 'boom'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``boom`` to ``say_hello`` in the :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :lineno-start: 49
  :emphasize-lines: 3

                  else:
                      self.assertEqual(
                          an_instance.say_hello(),
                          (
                              f'Hello, my name is {first_name}'
                              f' {last_name} and I am'
                              f' {self.calculate_age(year_of_birth)}.'
                          )
                      )

      def test_say_hello_method(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove :ref:`test_say_hello_method<extract test_say_hello method>` because it is now a repetition

  .. code-block:: python
    :lineno-start: 49

                    else:
                        self.assertEqual(
                            an_instance.say_hello(),
                            (
                                f'Hello, my name is {first_name}'
                                f' {last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )

        def test_say_hello_function(self):

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`can_vote method<add can_vote method>` to :ref:`test_person_class<extract test_person_class>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 10

                    else:
                        self.assertEqual(
                            an_instance.say_hello(),
                            (
                                f'Hello, my name is {first_name}'
                                f' {last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )
                        self.assertEqual(an_instance.can_vote(), False)

        def test_say_hello_function(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(first_name='jane', year_of_birth=1991)
        AssertionError: True != False
    SUBFAILED(first_name='joe', year_of_birth=1996)
        AssertionError: True != False
    SUBFAILED(first_name='mary', year_of_birth=2000)
        AssertionError: True != False
    SUBFAILED(first_name='john', year_of_birth=1980)
        AssertionError: True != False

* I add values for ``is_citizen`` to the ``people`` :ref:`object attribute<what is an object attribute?>` of the :ref:`TestPerson class<add TestPerson object>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-24

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year
        people = (
            (
                'jane', 'doe', 'F', 1991,
                True,
            ),
            (
                'joe', 'blow', 'M', 1996,
                True,
            ),
            (
                'mary', 'public', 'F', 2000,
                False,
            ),
            (
                'john', 'smith', 'M', 1980,
                False,
            ),
            (
                'first_name', 'last_name', 'F', 'a_string',
                False,
            )
        )

* I use the values for the ``is_citizen`` parameter when making an :ref:`instance<how to test if something is an instance>` of  the :ref:`Person class<add Person object>` in :ref:`test_person_class<extract test_person_class>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 7

        def test_person_class(self):
            for a_person in self.people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]
                is_citizen = a_person[4]

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 11

                with self.subTest(
                    first_name=first_name,
                    year_of_birth=year_of_birth,
                ):
                    try:
                        an_instance = src.person.Person(
                            first_name=first_name,
                            last_name=last_name,
                            sex=sex,
                            year_of_birth=year_of_birth,
                            is_citizen=is_citizen,
                        )
                    except TypeError as error:

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I change the expectation of the :ref:`assertion<what is an assertion?>` for the :ref:`can_vote method<add can_vote method>` to use the value of the ``is_citizen`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 10

                    else:
                        self.assertEqual(
                            an_instance.say_hello(),
                            (
                                f'Hello, my name is {first_name}'
                                f' {last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )
                        self.assertEqual(an_instance.can_vote(), is_citizen)

        def test_say_hello_function(self):

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`can_get_license method<add can_get_license method>` to :ref:`test_person_class<extract test_person_class>`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 11

                else:
                        self.assertEqual(
                            an_instance.say_hello(),
                            (
                                f'Hello, my name is {first_name}'
                                f' {last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )
                        self.assertEqual(an_instance.can_vote(), is_citizen)
                        self.assertEqual(an_instance.can_get_license(), True)

        def test_say_hello_function(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(first_name='jane', year_of_birth=1991)
        AssertionError: False != True
    SUBFAILED(first_name='joe', year_of_birth=1996)
        AssertionError: False != True
    SUBFAILED(first_name='mary', year_of_birth=2000)
        AssertionError: False != True
    SUBFAILED(first_name='john', year_of_birth=1980)
        AssertionError: False != True

* I add values for ``passed_test`` to the ``people`` :ref:`object attribute<what is an object attribute?>` of the :ref:`TestPerson class<add TestPerson object>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4, 8, 12, 16, 20

        people = (
            (
                'jane', 'doe', 'F', 1991,
                True, True,
            ),
            (
                'joe', 'blow', 'M', 1996,
                True, False,
            ),
            (
                'mary', 'public', 'F', 2000,
                False, True,
            ),
            (
                'john', 'smith', 'M', 1980,
                False, False,
            ),
            (
                'first_name', 'last_name', 'F', 'a_string',
                False, False,
            )
        )

* I use the values for the ``passed_test`` parameter when making an :ref:`instance<how to test if something is an instance>` of  the :ref:`Person class<add Person object>` in :ref:`test_person_class<extract test_person_class>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 8

        def test_person_class(self):
            for a_person in self.people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]
                is_citizen = a_person[4]
                passed_test = a_person[5]


  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 12

                with self.subTest(
                    first_name=first_name,
                    year_of_birth=year_of_birth,
                ):
                    try:
                        an_instance = src.person.Person(
                            first_name=first_name,
                            last_name=last_name,
                            sex=sex,
                            year_of_birth=year_of_birth,
                            is_citizen=is_citizen,
                            passed_test=passed_test,
                        )
                    except TypeError as error:

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I change the expectation of the :ref:`assertion<what is an assertion?>` for the :ref:`can_get_license method<add can_get_license method>` to use the value of the ``passed_test`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 11-13

                    else:
                        self.assertEqual(
                            an_instance.say_hello(),
                            (
                                f'Hello, my name is {first_name}'
                                f' {last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )
                        self.assertEqual(an_instance.can_vote(), is_citizen)
                        self.assertEqual(
                            an_instance.can_get_license(), passed_test
                        )

        def test_say_hello_function(self):

  the test passes.

* :ref:`test_person_class<extract test_person_class>` is missing the cases for if a person :green:`younger` than ``18``

  ==============  ============== ==============
  age < 18        is citizen     can vote
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :red:`False`
  ==============  ============== ==============

  ==============  ============== ================
  age < 18        passed test    can get license
  ==============  ============== ================
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :red:`False`
  ==============  ============== ================

  which gives this :ref:`truth table` when put together

  ==============  ============== ============== ==============  ================
  age < 18        is citizen     passed_test    can vote        can_get_license
  ==============  ============== ============== ==============  ================
  :green:`True`   :green:`True`  :green:`True`  :red:`False`    :red:`False`
  :green:`True`   :red:`False`   :green:`True`  :red:`False`    :red:`False`
  :green:`True`   :green:`True`  :red:`False`   :red:`False`    :red:`False`
  :green:`True`   :red:`False`   :red:`False`   :red:`False`    :red:`False`
  ==============  ============== ============== ==============  ================

  I add tuples_ for these cases to the ``people`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 9

    people = (
        (
            'jane', 'doe', 'F', 1991,
            True, True,
        ),
        (
            'joe', 'blow', 'M', 1996,
            True, False,
        ),
        (
            'mary', 'public', 'F', 2000,
            False, True,
        ),
        (
            'john', 'smith', 'M', 1980,
            False, False,
        ),

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 1-24

        (
            # underage, is_citizen, passed_test
            'first_name', 'last_name', 'M',
            datetime.date.today().year-17,
            True, True,
        ),
        (
            # underage, not is_citizen, passed_test
            'first_name', 'last_name', 'M',
            datetime.date.today().year-17,
            False, True,
        ),
        (
            # underage, is_citizen, not passed_test
            'first_name', 'last_name', 'M',
            datetime.date.today().year-17,
            True, False,
        ),
        (
            # underage, not is_citizen, not passed_test
            'first_name', 'last_name', 'M',
            datetime.date.today().year-17,
            False, False,
        ),
        (
            'first_name', 'last_name', 'F', 'a_string',
            False, False,
        )
    )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(first_name='first_name', year_of_birth=YYYY) ...
        AssertionError: False != True
    SUBFAILED(first_name='first_name', year_of_birth=YYYY) ...
        AssertionError: False != True
    SUBFAILED(first_name='first_name', year_of_birth=YYYY) ...
        AssertionError: False != True

  I need a better error message, so I know which tuples_ caused the failures.

* I change the names in :ref:`the subTest method` to show the entire tuple_ in :ref:`test_person_class<extract test_person_class>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 10

        def test_person_class(self):
            for a_person in self.people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]
                is_citizen = a_person[4]
                passed_test = a_person[5]

                with self.subTest(a_person):
                    try:

  the terminal_ shows

  .. code-block:: python

    SUBFAILED[('first_name', 'last_name', 'M', YYYY, True, True)] ...
        AssertionError: False != True
    SUBFAILED[('first_name', 'last_name', 'M', YYYY, False, True)] ...
        AssertionError: False != True
    SUBFAILED[('first_name', 'last_name', 'M', YYYY, True, False)] ...
        AssertionError: False != True

  because I used the value for the ``is_citizen`` :ref:`variable<what is a variable?>` as the expectation of the :ref:`assertion<what is an assertion>` for the :ref:`can_vote method<add can_vote method>` which is wrong when the person is :green:`younger` than ``18``, the expectation should always be :red:`False`.

* I add the expectation for all the cases of the :ref:`can_vote method<add can_vote method>` to the ``people`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4, 8, 12

        people = (
            (
                'jane', 'doe', 'F', 1991,
                True, True, True,
            ),
            (
                'joe', 'blow', 'M', 1996,
                True, False, True,
            ),
            (
                'mary', 'public', 'F', 2000,
                False, True, False,
            ),

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3, 9, 15

            (
                'john', 'smith', 'M', 1980,
                False, False, False,
            ),
            (
                # underage, is_citizen, passed_test
                'first_name', 'last_name', 'M',
                datetime.date.today().year-17,
                True, True, False,
            ),
            (
                # underage, not is_citizen, passed_test
                'first_name', 'last_name', 'M',
                datetime.date.today().year-17,
                False, True, False,
            ),

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 5, 11, 15

            (
                # underage, is_citizen, not passed_test
                'first_name', 'last_name', 'M',
                datetime.date.today().year-17,
                True, False, False,
            ),
            (
                # underage, not is_citizen, not passed_test
                'first_name', 'last_name', 'M',
                datetime.date.today().year-17,
                False, False, False,
            ),
            (
                'first_name', 'last_name', 'F', 'a_string',
                False, False, False,
            )
        )

* I remove the ``is_citizen`` :ref:`variable<what is a variable?>` then change the expectation of the :ref:`assertion<what is an assertion?>` for the :ref:`can_vote method<add can_vote method>` in :ref:`test_person_class<extract test_person_class>` to the new item I added to the tuples_ in the ``people`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 7

        def test_person_class(self):
            for a_person in self.people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]
                # is_citizen = a_person[4]
                passed_test = a_person[5]

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 8-9

                with self.subTest(a_person):
                    try:
                        an_instance = src.person.Person(
                            first_name=first_name,
                            last_name=last_name,
                            sex=sex,
                            year_of_birth=year_of_birth,
                            # is_citizen=is_citizen,
                            is_citizen=a_person[4],
                            passed_test=passed_test,
                        )
                    except TypeError as error:

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 10-11

                    else:
                        self.assertEqual(
                            an_instance.say_hello(),
                            (
                                f'Hello, my name is {first_name}'
                                f' {last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )
                        # self.assertEqual(an_instance.can_vote(), is_citizen)
                        self.assertEqual(an_instance.can_vote(), a_person[6])
                        self.assertEqual(
                            an_instance.can_get_license(), passed_test
                        )

        def test_say_hello_function(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED[('first_name', 'last_name', 'M', YYYY, True, True, False)] ...
        AssertionError: False != True
    SUBFAILED[('first_name', 'last_name', 'M', YYYY, False, True, False)] ...
        AssertionError: False != True

  because I used the value for the ``passed_test`` :ref:`variable<what is a variable?>` as the expectation of the :ref:`assertion<what is an assertion>` for the :ref:`can_get_license method<add can_get_license method>` which is wrong when the person is :green:`younger` than ``18``, the expectation should always be :red:`False`.

* I add the expectation for all the cases of the :ref:`can_get_license method<add can_get_license method>` to the ``people`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4, 8, 12

        people = (
            (
                'jane', 'doe', 'F', 1991,
                True, True, True, True,
            ),
            (
                'joe', 'blow', 'M', 1996,
                True, False, True, False,
            ),
            (
                'mary', 'public', 'F', 2000,
                False, True, False, True,
            ),

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3, 9, 15

            (
                'john', 'smith', 'M', 1980,
                False, False, False, False,
            ),
            (
                # underage, is_citizen, passed_test
                'first_name', 'last_name', 'M',
                datetime.date.today().year-17,
                True, True, False, False,
            ),
            (
                # underage, not is_citizen, passed_test
                'first_name', 'last_name', 'M',
                datetime.date.today().year-17,
                False, True, False, False,
            ),

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 5, 11, 15

            (
                # underage, is_citizen, not passed_test
                'first_name', 'last_name', 'M',
                datetime.date.today().year-17,
                True, False, False, False,
            ),
            (
                # underage, not is_citizen, not passed_test
                'first_name', 'last_name', 'M',
                datetime.date.today().year-17,
                False, False, False, False,
            ),
            (
                'first_name', 'last_name', 'F', 'a_string',
                False, False, False, False,
            )
        )
        truth_table = (
            (datetime.date.today().year-17, True, False),
            (datetime.date.today().year-17, False, False),
            (datetime.date.today().year-18, True, True),
            (datetime.date.today().year-18, False, False),
        )

        def calculate_age(self, year_of_birth):

* I remove the ``passed_test`` :ref:`variable<what is a variable?>` then change the expectation of the :ref:`assertion<what is an assertion?>` for the :ref:`can_get_license method<add can_get_license method>` in :ref:`test_person_class<extract test_person_class>` to the new item I added to the tuples_ in the ``people`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 8

        def test_person_class(self):
            for a_person in self.people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]
                # is_citizen = a_person[4]
                # passed_test = a_person[5]

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 10-11

                with self.subTest(a_person):
                    try:
                        an_instance = src.person.Person(
                            first_name=first_name,
                            last_name=last_name,
                            sex=sex,
                            year_of_birth=year_of_birth,
                            # is_citizen=is_citizen,
                            is_citizen=a_person[4],
                            # passed_test=passed_test,
                            passed_test=a_person[5],
                        )
                    except TypeError as error:

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 13-14

                    else:
                        self.assertEqual(
                            an_instance.say_hello(),
                            (
                                f'Hello, my name is {first_name}'
                                f' {last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )
                        # self.assertEqual(an_instance.can_vote(), is_citizen)
                        self.assertEqual(an_instance.can_vote(), a_person[6])
                        self.assertEqual(
                            # an_instance.can_get_license(), passed_test
                            an_instance.can_get_license(), a_person[7]
                        )

        def test_say_hello_function(self):

  the test passes.

* I remove the commented lines from :ref:`test_person_class<extract test_person_class>`

  .. code-block:: python
    :lineno-start: 65

        def test_person_class(self):
            for a_person in self.people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]

  .. code-block:: python
    :lineno-start: 72

                with self.subTest(a_person):
                    try:
                        an_instance = src.person.Person(
                            first_name=first_name,
                            last_name=last_name,
                            sex=sex,
                            year_of_birth=year_of_birth,
                            is_citizen=a_person[4],
                            passed_test=a_person[5],
                        )
                    except TypeError as error:
                        self.assertEqual(
                            error.args[0],
                            f"'{year_of_birth}' is not an integer"
                        )

  .. code-block:: python
    :lineno-start: 87

                    else:
                        self.assertEqual(
                            an_instance.say_hello(),
                            (
                                f'Hello, my name is {first_name}'
                                f' {last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )
                        self.assertEqual(an_instance.can_vote(), a_person[6])
                        self.assertEqual(
                            an_instance.can_get_license(), a_person[7]
                        )

        def test_say_hello_function(self):

* I remove :ref:`test_if_person_can_vote<extract test_if_person_can_vote>` because it is now a repetition
* I remove :ref:`test_if_person_can_get_license<extract test_if_person_can_get_license>` because it is now a repetition

  .. code-block:: python
    :lineno-start: 132

        def test_person_factory(self):
            for a_person in self.people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]

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

        def test_when_person_is_older_than_120(self):

* I remove the ``truth_table`` :ref:`object_attribute<what is an object attribute?>` because it is no longer used

  .. code-block:: python
    :lineno-start: 50

            (
                'first_name', 'last_name', 'F', 'a_string',
                False, False, False, False,
            )
        )

        def calculate_age(self, year_of_birth):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract test_person_class'

----

*********************************************************************************
extract object attributes
*********************************************************************************

The ``people`` :ref:`object attribute<what is an object attribute?>` can be described with the following :ref:`truth table`

- If a person is :green:`younger` than ``18``

  ==============  ============== ============== ==============  ================
  age < 18        is citizen     passed_test    can vote        can_get_license
  ==============  ============== ============== ==============  ================
  :green:`True`   :green:`True`  :green:`True`  :red:`False`    :red:`False`
  :green:`True`   :red:`False`   :green:`True`  :red:`False`    :red:`False`
  :green:`True`   :green:`True`  :red:`False`   :red:`False`    :red:`False`
  :green:`True`   :red:`False`   :red:`False`   :red:`False`    :red:`False`
  ==============  ============== ============== ==============  ================

- If a person is :red:`NOT younger` than ``18``

  ==============  ============== ============== ==============  ================  ======
  age < 18        is citizen     passed_test    can vote        can_get_license   person
  ==============  ============== ============== ==============  ================  ======
  :red:`False`    :green:`True`  :green:`True`  :green:`True`   :green:`True`     jane
  :red:`False`    :red:`False`   :green:`True`  :red:`False`    :green:`True`     mary
  :red:`False`    :green:`True`  :red:`False`   :green:`True`   :red:`False`      joe
  :red:`False`    :red:`False`   :red:`False`   :red:`False`    :red:`False`      john
  ==============  ============== ============== ==============  ================  ======


* I make an :ref:`object attribute<what is an object attribute?>` for ``datetime.date.today().year-17``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year
        younger_than_18 = this_year - 17
        people = (

* I change the comments then use the new :ref:`object attribute<what is an object attribute?>` for ``datetime.date.today().year-17`` from the ``people`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 2, 4, 8, 10, 14, 16, 20, 22

            (
                # is_citizen, passed_test
                'first_name', 'last_name', 'M',
                younger_than_18,
                True, True, False, False,
            ),
            (
                # not is_citizen, passed_test
                'first_name', 'last_name', 'M',
                younger_than_18,
                False, True, False, False,
            ),
            (
                # is_citizen, not passed_test
                'first_name', 'last_name', 'M',
                younger_than_18,
                True, False, False, False,
            ),
            (
                # not is_citizen, not passed_test
                'first_name', 'last_name', 'M',
                younger_than_18,
                False, False, False, False,
            ),
            (
                'first_name', 'last_name', 'F', 'a_string',
                False, False, False, False,
            )
        )

  the tests are still green.

* I add a new :ref:`object attribute<what is an object attribute?>` for if a person is :red:`NOT younger` than ``18``

  .. code-block:: python
    :lineno-start: 6

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year
        younger_than_18 = this_year - 17
        not_younger_than_18 = this_year - 18
        people = (

* I add comments then use the new :ref:`object attribute<what is an object attribute?>` for the ``year_of_birth`` values of ``jane``, ``joe``, ``mary`` and ``john`` in the ``people`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3-5, 9-11, 15-17, 21-23

        people = (
            (
                # is_citizen, passed_test
                'jane', 'doe', 'F',
                not_younger_than_18,
                True, True, True, True,
            ),
            (
                # is_citizen, not passed_test
                'joe', 'blow', 'M',
                not_younger_than_18,
                True, False, True, False,
            ),
            (
                # not is_citizen, passed_test
                'mary', 'public', 'F',
                not_younger_than_18,
                False, True, False, True,
            ),
            (
                # not is_citizen, not passed_test
                'john', 'smith', 'M',
                not_younger_than_18,
                False, False, False, False,
            ),

  still green.

* I change the values for ``first_name``, ``last_name`` and ``sex`` to ``'first_name', 'last_name', 'M',`` for all the tuples_ in the ``people`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4, 10, 16, 22

        people = (
            (
                # is_citizen, passed_test
                'first_name', 'last_name', 'M',
                not_younger_than_18,
                True, True, True, True,
            ),
            (
                # not is_citizen, not passed_test
                'first_name', 'last_name', 'M',
                not_younger_than_18,
                True, False, True, False,
            ),
            (
                # not is_citizen, passed_test
                'first_name', 'last_name', 'M',
                not_younger_than_18,
                False, True, False, True,
            ),
            (
                # not is_citizen, not passed_test
                'first_name', 'last_name', 'M',
                not_younger_than_18,
                False, False, False, False,
            ),

  green.

* I add :ref:`object attributes<what is an object attribute?>` for ``first_name``, ``last_name`` and ``sex``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 7-9

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year
        younger_than_18 = this_year - 17
        not_younger_than_18 = this_year - 18

        first_name = 'first_name'
        last_name = 'last_name'
        sex = 'M'

        people = (

* I use the new :ref:`object attributes<what is an object attribute?>` for ``first_name``, ``last_name`` and ``sex``, move them out of the :ref:`for loop<what is a for loop?>` in :ref:`test_person_class<extract test_person_class>`

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 2-4, 7

        def test_person_class(self):
            first_name = self.first_name
            last_name = self.last_name
            sex = self.sex

            for a_person in self.people:
                year_of_birth = a_person[3]

                with self.subTest(a_person):

  still green.

* I use the new :ref:`object attributes<what is an object attribute?>` for ``first_name`` and ``last_name``, then move them out of the :ref:`for loop<what is a for loop?>` in :ref:`test_say_hello_function<extract test_say_hello_function>`

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 2-3, 6, 8

        def test_say_hello_function(self):
            first_name = self.first_name
            last_name = self.last_name

            for a_person in self.people:
                year_of_birth = a_person[3]

                with self.subTest(a_person):
                    try:

  the test is still green.

* I use the new :ref:`object attributes<what is an object attribute?>` for ``first_name``, ``last_name`` and ``sex``, then move them out of the :ref:`for loop<what is a for loop?>` in :ref:`test_person_factory<extract test_person_factory>`

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 2-4, 7

        def test_person_factory(self):
            first_name = self.first_name
            last_name = self.last_name
            sex = self.sex

            for a_person in self.people:
                year_of_birth = a_person[3]

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 1-13

                with self.subTest(a_person):
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

        def test_when_person_is_older_than_120(self):

  still green.

* I use the :ref:`object attributes<what is an object attribute?>` directly in :ref:`test_person_factory<extract test_person_factory>` (I do not need the :ref:`variables<what is a variable?>`)

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 2, 8-11, 14-15

        def test_person_factory(self):
            for a_person in self.people:
                year_of_birth = a_person[3]

                with self.subTest(a_person):
                    self.assertEqual(
                        src.person.person(
                            first_name=self.first_name,
                            last_name=self.last_name,
                            sex=self.sex,
                            year_of_birth=year_of_birth,
                        ),
                        (
                            f'{self.first_name}, {self.last_name},'
                            f' {self.sex}, {year_of_birth}'
                        )
                    )

        def test_when_person_is_older_than_120(self):

  green.

* I use the :ref:`object attributes<what is an object attribute?>` directly in :ref:`test_say_hello_function<extract test_say_hello_function>`

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 2, 8-10

        def test_say_hello_function(self):
            for a_person in self.people:
                year_of_birth = a_person[3]

                with self.subTest(a_person):
                    try:
                        reality = src.person.say_hello(
                            first_name=self.first_name,
                            last_name=self.last_name,
                            year_of_birth=year_of_birth,
                        )

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 10-11

                    except TypeError as error:
                        self.assertEqual(
                            error.args[0],
                            f"'{year_of_birth}' is not an integer"
                        )
                    else:
                        self.assertEqual(
                            reality,
                            (
                                f'Hello, my name is {self.first_name}'
                                f' {self.last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )

        def test_person_factory(self):

* I use the :ref:`object attributes<what is an object attribute?>` directly in :ref:`test_person_class<extract test_person_class>`

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 2, 8-10

        def test_person_class(self):
            for a_person in self.people:
                year_of_birth = a_person[3]

                with self.subTest(a_person):
                    try:
                        an_instance = src.person.Person(
                            first_name=self.first_name,
                            last_name=self.last_name,
                            sex=self.sex,
                            year_of_birth=year_of_birth,
                            is_citizen=a_person[4],
                            passed_test=a_person[5],
                        )

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 10-11

                    except TypeError as error:
                        self.assertEqual(
                            error.args[0],
                            f"'{year_of_birth}' is not an integer"
                        )
                    else:
                        self.assertEqual(
                            an_instance.say_hello(),
                            (
                                f'Hello, my name is {self.first_name}'
                                f' {self.last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )
                        self.assertEqual(an_instance.can_vote(), a_person[6])
                        self.assertEqual(
                            an_instance.can_get_license(), a_person[7]
                        )

        def test_say_hello_function(self)

* I remove the values of ``first_name``, ``last_name`` amd ``sex`` from the tuples_ in the ``people`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4

        people = (
            (
                # is_citizen, passed_test
                # 'first_name', 'last_name', 'M',
                not_younger_than_18,
                True, True, True, True,
            ),

  the terminal_ is my friend, and shows :ref:`IndexError<test_index_error>` and ValueError_

  .. code-block:: python

    SUBFAILED[(2008, True, True, True, True)] ...test_person_class -
        IndexError: tuple index out of range
    SUBFAILED[(2008, True, True, True, True)] ...test_say_hello_function -
        ValueError

  because the positions changed when I changed the tuple_. I would have to change all the :ref:`indexes<test_index_returns_first_position_of_item_in_a_list>` if I change the tuple_, there has to be :ref:`a better way<how to make a person with dictionaries>`

* I undo the change

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4

        people = (
            (
                # is_citizen, passed_test
                'first_name', 'last_name', 'M',
                not_younger_than_18,
                True, True, True, True,
            ),

  the tests are green again.

* I change the values for the first three items of the tuples_ in the ``people`` :ref:`object attribute<what is an object attribute?>` to the ``year_of_birth`` value and the :ref:`boolean<what are booleans?>` for ``is_citizen`` and ``passed_test``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4, 10, 16

        people = (
            (
                # is_citizen, passed_test
                not_younger_than_18, True, True,
                not_younger_than_18,
                True, True, True, True,
            ),
            (
                # is_citizen, not passed_test
                not_younger_than_18, True, False,
                not_younger_than_18,
                True, False, True, False,
            ),
            (
                # not is_citizen, passed_test
                not_younger_than_18, False, True,
                not_younger_than_18,
                False, True, False, True,
            ),

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 3, 9, 15

            (
                # not is_citizen, not passed_test
                not_younger_than_18, False, False,
                not_younger_than_18,
                False, False, False, False,
            ),
            (
                # underage, is_citizen, passed_test
                younger_than_18, True, True,
                younger_than_18,
                True, True, False, False,
            ),
            (
                # underage, not is_citizen, passed_test
                younger_than_18, False, True,
                younger_than_18,
                False, True, False, False,
            ),

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 3, 9, 14-15

            (
                # underage, is_citizen, not passed_test
                younger_than_18, True, False,
                younger_than_18,
                True, False, False, False,
            ),
            (
                # underage, not is_citizen, not passed_test
                younger_than_18, False, False,
                younger_than_18,
                False, False, False, False,
            ),
            (
                'a_string', False, False,
                'a_string',
                False, False, False, False,
            )
        )

        def calculate_age(self, year_of_birth):

  the tests are still green.

* I change the :ref:`indexes<test_index_returns_first_position_of_item_in_a_list>` for ``year_of_birth``, ``is_citizen`` and ``passed_test`` in :ref:`test_person_class<extract test_person_class>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 3, 12-13

        def test_person_class(self):
            for a_person in self.people:
                year_of_birth = a_person[0]

                with self.subTest(a_person):
                    try:
                        person = src.person.Person(
                            first_name=self.first_name,
                            last_name=self.last_name,
                            sex=self.sex,
                            year_of_birth=year_of_birth,
                            is_citizen=a_person[1],
                            passed_test=a_person[2],
                        )
                    except TypeError as error:

  still green.

* I change the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` for ``year_of_birth`` in :ref:`test_say_hello_function<extract test_say_hello_function>`

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 3

        def test_say_hello_function(self):
            for a_person in self.people:
                year_of_birth = a_person[0]

                with self.subTest(a_person):

  green.

* I change the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` for ``year_of_birth`` in :ref:`test_person_factory<extract test_person_factory>`

  .. code-block:: python
    :lineno-start: 134
    :emphasize-lines: 3

        def test_person_factory(self):
            for a_person in self.people:
                year_of_birth = a_person[0]

                with self.subTest(a_person):

  still green.

* I remove the repeated values from the tuples_ in the ``people`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5, 10, 15

        people = (
            (
                # is_citizen, passed_test
                not_younger_than_18, True, True,
                True, True,
            ),
            (
                # is_citizen, not passed_test
                not_younger_than_18, True, False,
                True, False,
            ),
            (
                # not is_citizen, passed_test
                not_younger_than_18, False, True,
                False, True,
            ),

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 4, 9, 14

            (
                # not is_citizen, not passed_test
                not_younger_than_18, False, False,
                False, False,
            ),
            (
                # underage, is_citizen, passed_test
                younger_than_18, True, True,
                False, False,
            ),
            (
                # underage, not is_citizen, passed_test
                younger_than_18, False, True,
                False, False,
            ),

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 4, 9, 13

            (
                # underage, is_citizen, not passed_test
                younger_than_18, True, False,
                False, False,
            ),
            (
                # underage, not is_citizen, not passed_test
                younger_than_18, False, False,
                False, False,
            ),
            (
                'a_string', False, False,
                False, False,
            )
        )

        def calculate_age(self, year_of_birth):

  the terminal_ is my friend, and shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    SUBFAILED[(2008, True, True, True, True)] ...test_person_class -
        IndexError: tuple index out of range
    SUBFAILED[(2008, True, False, True, False)] ...test_person_class -
        IndexError: tuple index out of range
    SUBFAILED[(2008, False, True, False, True)] ...test_person_class -
        IndexError: tuple index out of range
    SUBFAILED[(2008, False, False, False, False)] ...test_person_class -
        IndexError: tuple index out of range
    SUBFAILED[(2009, True, True, False, False)] ...test_person_class -
        IndexError: tuple index out of range
    SUBFAILED[(2009, False, True, False, False)] ...test_person_class -
        IndexError: tuple index out of range
    SUBFAILED[(2009, True, False, False, False)] ...test_person_class -
        IndexError: tuple index out of range
    SUBFAILED[(2009, False, False, False, False)] ...test_person_class -
        IndexError: tuple index out of range

* I change the :ref:`indexes<test_index_returns_first_position_of_item_in_a_list>` for the expectations of the results to :ref:`calls<how to call a function with input>` of the :ref:`can_vote<add can_vote method>` and :ref:`can_get_license methods<add can_get_license method>` in :ref:`test_person_class<extract test_person_class>`

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 10, 12

                    else:
                        self.assertEqual(
                            an_instance.say_hello(),
                            (
                                f'Hello, my name is {self.first_name}'
                                f' {self.last_name} and I am'
                                f' {self.calculate_age(year_of_birth)}.'
                            )
                        )
                        self.assertEqual(an_instance.can_vote(), a_person[3])
                        self.assertEqual(
                            an_instance.can_get_license(), a_person[4]
                        )

        def test_say_hello_function(self):

  the test is green again.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract object attributes'

----

*********************************************************************************
use assertRaises with test_when_person_is_older_than_120
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I use the :ref:`assertRaises method<another way to test if an Exception is raised>` to replace the :ref:`try statement<how to handle Exceptions>` in :ref:`test_when_person_is_older_than_120`

.. code-block:: python
  :lineno-start: 143
  :emphasize-lines: 2-3, 10-11

      def test_when_person_is_older_than_120(self):
          # try:
          with self.assertRaises(TypeError):
              src.person.Person(
                  first_name='first_name',
                  last_name='last_name',
                  sex='M',
                  year_of_birth=self.this_year-121
              )
          # except ValueError:
          #     pass

      def test_when_year_of_birth_is_the_future(self):

the terminal_ is my friend, and shows ValueError_

.. code-block:: python

  E           ValueError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`Exception<how to test that an Exception is raised>` to match

.. code-block:: python
  :lineno-start: 143
  :emphasize-lines: 3

      def test_when_person_is_older_than_120(self):
          # try:
          with self.assertRaises(ValueError):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change :ref:`assertRaises<another way to test if an Exception is raised>` to :ref:`assertRaisesRegex<how to test the message of an Exception>` to test the message of the :ref:`Exception<how to test that an Exception is raised>`

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 3-4, 6-9, 14-15

        def test_when_person_is_older_than_120(self):
            # try:
            year_of_birth = self.this_year - 121
            age = self.calculate_age(year_of_birth)

            with self.assertRaisesRegex(
                ValueError,
                f'a {age} year old person is too old to be alive.'
            ):
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    # year_of_birth=self.this_year-121,
                    year_of_birth=year_of_birth,
                )
            # except ValueError:
            #     pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        "a 121 year old person is too old to be alive."
        does not match ""

* I add a message to the :ref:`Exception<how to test that an Exception is raised>` in the :ref:`calculate_age function<add calculate_age function>` in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 13-15

    def calculate_age(year_of_birth):
        if not isinstance(year_of_birth, int):
            raise TypeError(
                f"'{year_of_birth}' is not an integer"
            )

        age = (
            datetime.date.today().year
          - year_of_birth
        )

        if age < 0 or age > 120:
            raise ValueError(
                f'a {age} year old person is too old to be alive.'
            )
        return age

  the test passes.

* I remove the commented lines from :ref:`test_when_person_is_older_than_120` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 143

        def test_when_person_is_older_than_120(self):
            year_of_birth = self.this_year - 121
            age = self.calculate_age(year_of_birth)

            with self.assertRaisesRegex(
                ValueError,
                f'a {age} year old person is too old to be alive.'
            ):
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth=year_of_birth,
                )

        def test_when_year_of_birth_is_the_future(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'use assertRaises with test_when_person_is_older_than_120'

----

*********************************************************************************
use assertRaises with test_when_year_of_birth_is_the_future
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I use the :ref:`assertRaisesRegex method<how to test the message of an Exception>` to replace the :ref:`try statement<how to handle Exceptions>` in :ref:`test_when_year_of_birth_is_the_future`

.. code-block:: python
  :lineno-start: 158
  :emphasize-lines: 2-5, 12-13

      def test_when_year_of_birth_is_the_future(self):
          # try:
          with self.assertRaisesRegex(
              ValueError, 'BOOM!!!'
          ):
              src.person.Person(
                  first_name='first_name',
                  last_name='last_name',
                  sex='F',
                  year_of_birth=self.this_year+1,
              )
          # except ValueError:
          #     pass

      def test_when_year_of_birth_is_not_an_integer(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError:
      "BOOM!!!" does not match
      "a -1 year old person is too old to be alive."

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`Exception<how to test that an Exception is raised>` to match

.. code-block:: python
  :lineno-start: 158
  :emphasize-lines: 3

      def test_when_year_of_birth_is_the_future(self):
          # try:
          with self.assertRaises(ValueError):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change :ref:`assertRaises<another way to test if an Exception is raised>` to :ref:`assertRaisesRegex<how to test the message of an Exception>` to test the message of the :ref:`Exception<how to test that an Exception is raised>`

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 3-5, 12-13

        def test_when_year_of_birth_is_the_future(self):
            # try:
            with self.assertRaisesRegex(
                ValueError, 'BOOM!!!'
            ):
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='F',
                    year_of_birth=self.this_year+1,
                )
            # except ValueError:
            #     pass

        def test_when_year_of_birth_is_not_an_integer(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        "BOOM!!!" does not match
        "a -1 year old person is too old to be alive."

  I need a better message for if a person is too old to be alive or too young to be alive.

* I change the message of the :ref:`Exception<how to test that an Exception is raised>` in the :ref:`calculate_age function<add calculate_age function>` in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 14

    def calculate_age(year_of_birth):
        if not isinstance(year_of_birth, int):
            raise TypeError(
                f"'{year_of_birth}' is not an integer"
            )

        age = (
            datetime.date.today().year
          - year_of_birth
        )

        if age < 0 or age > 120:
            raise ValueError(
                f'a {age} year old person is not alive.'
            )
        return age

  the terminal is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    FAILED ...test_when_person_is_older_than_120 -
        AssertionError: "a 121 year old person is too old to be alive."
         does not match "a 121 year old person is not alive."
    FAILED ...test_when_year_of_birth_is_the_future -
        AssertionError: "BOOM!!!" does not match
                        "a -1 year old person is not alive."

* I change the error message in :ref:`test_when_person_is_older_than_120` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 7

        def test_when_person_is_older_than_120(self):
            year_of_birth = self.this_year - 121
            age = self.calculate_age(year_of_birth)

            with self.assertRaisesRegex(
                ValueError,
                f'a {age} year old person is not alive.'
            ):
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth=year_of_birth,
                )

        def test_when_year_of_birth_is_the_future(self):

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I change the error message in :ref:`test_when_year_of_birth_is_the_future`

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 3-4, 7-8, 14-15

        def test_when_year_of_birth_is_the_future(self):
            # try:
            year_of_birth = self.this_year + 1
            age = self.calculate_age(year_of_birth)

            with self.assertRaisesRegex(
                ValueError,
                f'a {age} year old person is not alive.'
            ):
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='F',
                    # year_of_birth=self.this_year+1,
                    year_of_birth=year_of_birth,
                )
            # except ValueError:
            #     pass

  the test passes.

* I remove the commented lines from :ref:`test_when_year_of_birth_is_the_future`

  .. code-block:: python
    :lineno-start: 158

        def test_when_year_of_birth_is_the_future(self):
            year_of_birth = self.this_year + 1
            age = self.calculate_age(year_of_birth)

            with self.assertRaisesRegex(
                ValueError,
                f'a {age} year old person is not alive.'
            ):
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='F',
                    year_of_birth=year_of_birth,
                )

        def test_when_year_of_birth_is_not_an_integer(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'use assertRaises with test_when_year_of_birth_is_the_future'

----

*********************************************************************************
extract test_if_person_is_not_alive
*********************************************************************************

:ref:`test_when_person_is_older_than_120` and :ref:`test_when_year_of_birth_is_the_future` both check if ValueError_ is :ref:`raised<how to raise an Exception>` if ``year_of_birth`` makes the person older than ``120`` or younger than ``0``

.. code-block:: python

  age = self.calculate_age(year_of_birth)

  with self.assertRaisesRegex(
      ValueError,
      f'a {age} year old person is not alive.'
  ):
      src.person.Person(
          first_name='first_name',
          last_name='last_name',
          sex='M',
          year_of_birth=year_of_birth,
      )

I can make one :ref:`function<what is a function?>` with a :ref:`for loop<what is a for loop?>` to remove the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for if a person is born in the future or is older than ``120``

.. code-block:: python
  :lineno-start: 125

        def test_person_factory(self):
            for a_person in self.people:
                year_of_birth = a_person[0]

                with self.subTest(a_person):
                    self.assertEqual(
                        src.person.person(
                            first_name=self.first_name,
                            last_name=self.last_name,
                            sex=self.sex,
                            year_of_birth=year_of_birth,
                        ),
                        (
                            f'{self.first_name}, {self.last_name},'
                            f' {self.sex}, {year_of_birth}'
                        )
                    )

.. code-block:: python
  :lineno-start: 143
  :emphasize-lines: 1-6, 8-18

        def test_if_person_is_not_alive(self):
            for year_of_birth in (
                self.this_year+1,
                self.this_year-121,
            ):
                age = self.calculate_age(year_of_birth)

                with self.subTest(year_of_birth):
                    with self.assertRaisesRegex(
                        ValueError,
                        'BOOM!!!'
                    ):
                        src.person.Person(
                            first_name=self.first_name,
                            last_name=self.last_name,
                            sex=self.sex,
                            year_of_birth=year_of_birth,
                        )

        def test_when_person_is_older_than_120(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  SUBFAILED(year_of_birth=XXXX) ...AssertionError:
      "BOOM!!!" does not match "a -1 year old person is not alive."
  SUBFAILED(year_of_birth=YYYY) ...AssertionError:
      "BOOM!!!" does not match "a 121 year old person is not alive."

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the error message in :ref:`extract test_if_person_is_not_alive` to match

.. code-block:: python
  :lineno-start: 143
  :emphasize-lines: 11

        def test_if_person_is_not_alive(self):
            for year_of_birth in (
                self.this_year+1,
                self.this_year-121,
            ):
                age = self.calculate_age(year_of_birth)

                with self.subTest(year_of_birth):
                    with self.assertRaisesRegex(
                        ValueError,
                        f'a {age} year old person is not alive.'
                    ):
                        src.person.Person(
                            first_name=self.first_name,
                            last_name=self.last_name,
                            sex=self.sex,
                            year_of_birth=year_of_birth,
                        )

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I put the two `with statements`_ together

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 8-20

        def test_if_person_is_not_alive(self):
            for year_of_birth in (
                self.this_year+1,
                self.this_year-121,
            ):
                age = self.calculate_age(year_of_birth)

                with (
                    self.subTest(year_of_birth),
                    self.assertRaisesRegex(
                        ValueError,
                        f'a {age} year old person is not alive.'
                    ),
                ):
                    src.person.Person(
                        first_name=self.first_name,
                        last_name=self.last_name,
                        sex=self.sex,
                        year_of_birth=year_of_birth,
                    )

        def test_when_person_is_older_than_120(self):

  the test is still green.

* I remove :ref:`test_when_person_is_older_than_120` because it is now covered by :ref:`test_if_person_is_not_alive<extract test_if_person_is_not_alive>`
* I remove :ref:`test_when_year_of_birth_is_the_future` because it is now covered by :ref:`test_if_person_is_not_alive<extract test_if_person_is_not_alive>`

  .. code-block:: python
    :lineno-start: 157

                    src.person.Person(
                        first_name=self.first_name,
                        last_name=self.last_name,
                        sex=self.sex,
                        year_of_birth=year_of_birth,
                    )

        def test_when_year_of_birth_is_not_an_integer(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract test_if_person_is_not_alive'


----

*********************************************************************************
move test_when_year_of_birth_is_not_an_integer to test_person_class
*********************************************************************************

:ref:`test_when_year_of_birth_is_not_an_integer` has multiple :ref:`try statements<how to handle Exceptions>` for if ``year_of_birth`` is not an integer_. It is also the last tuple_ in the ``people`` :ref:`object attribute<what is an object attribute?>` - its ``year_of_birth`` values are not integers_. I can use the :ref:`object attributes<what is an object attribute?>`  to remove the repetition

* I add tuples_ for the cases in :ref:`test_when_year_of_birth_is_not_an_integer` to the ``people`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 6-10

            (
                # underage, not is_citizen, not passed_test
                younger_than_18, False, False,
                False, False,
            ),
            # year_of_birth is not an integer
            (None, False, False,),
            (2026.0, False, False,),
            ('2026', False, False,),
            ((2026,), False, False,),
            (
                'a_string', False, False,
                False, False,
            ),
        )

        def calculate_age(self, year_of_birth):

  the tests are still green.

* I change the expected :ref:`Exception<how to test that an Exception is raised>` in :ref:`test_person_class<extract test_person_class>` to test my change

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 10

                    try:
                        person = src.person.Person(
                            first_name=self.first_name,
                            last_name=self.last_name,
                            sex=self.sex,
                            year_of_birth=year_of_birth,
                            is_citizen=a_person[1],
                            passed_test=a_person[2],
                        )
                    except IndexError as error:
                        self.assertEqual(
                            error.args[0],
                            f"'{year_of_birth}' is not an integer"
                        )
                    else:

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    SUBFAILED[(None, False, False)] ...test_person_class -
        TypeError: 'None' is not an integer
    SUBFAILED[(2026.0, False, False)] ...test_person_class -
        TypeError: '2026.0' is not an integer
    SUBFAILED[('2026', False, False)] ...test_person_class -
        TypeError: '2026' is not an integer
    SUBFAILED[((2026,), False, False)] ...test_person_class -
        TypeError: '(2026,)' is not an integer
    SUBFAILED[('a_string', False, False, False, False)] ...test_person_class -
        TypeError: 'a_string' is not an integer

  good, the test works.

* I undo the change

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 1

                    except TypeError as error:
                        self.assertEqual(
                            error.args[0],
                            f"'{year_of_birth}' is not an integer"
                        )
                    else:

  the test is green again.

* I remove the last tuple_ from the ``people`` :ref:`object attribute<what is an object attribute?>` because it is a repetition of when ``year_of_birth`` is a string_ (``('2026', False, False,),``)

  .. code-block:: python
    :lineno-start: 57

            # year_of_birth is not an integer
            (None, False, False,),
            (2026.0, False, False,),
            ('2026', False, False,),
            ((2026,), False, False,),
        )

        def calculate_age(self, year_of_birth):

* I remove :ref:`test_when_year_of_birth_is_not_an_integer` because it is now covered by :ref:`test_person_class<extract test_person_class>`

  .. code-block:: python
    :lineno-start: 144

        def test_if_person_is_not_alive(self):
            for year_of_birth in (
                self.this_year+1,
                self.this_year-121,
            ):
                age = self.calculate_age(year_of_birth)

                with (
                    self.subTest(year_of_birth),
                    self.assertRaisesRegex(
                        ValueError,
                        f'a {age} year old person is not alive.'
                    ),
                ):
                    src.person.Person(
                        first_name=self.first_name,
                        last_name=self.last_name,
                        sex=self.sex,
                        year_of_birth=year_of_birth,
                    )

        def test_dir_person_class(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move test_when_year_of_birth_is_not_an_integer to test_person_class'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_person.py`` and ``src/person/__init__.py``
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.
* I `change directory`_ to the parent of ``person``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

----

*************************************************************************************
review
*************************************************************************************

I can use :ref:`for loops<what is a for loop?>` for things that repeat.

My tests still have problems:

* The attribute tests - :ref:`test_dir_person_class` and :ref:`test_dir_person_instance` catch changes to the :ref:`attributes and methods of the Person class<test_dir_person_instance>` and they are a problem to maintain. :ref:`There has to be a better way<how to make a person with lists>`.
* The ``people`` :ref:`object attribute<what is an object attribute>` is confusing, anyone who reads it without going through the process of making it would not know what the :ref:`booleans<what is a boolean?>` stands for and the last few tuples_ I added are a different length than the others. :ref:`There has to be a better way<how to make a person with dictionaries>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a person with loops: tests and solutions>`

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
* :ref:`I know how to make a person with an object<how to make a person with an object>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`.
* :ref:`I know how to write programs that make decisions<truth table>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically with variables<how to make a Python Test Driven Development environment automatically with variables>`.
* :ref:`I know how to make a person with Exceptions<how to make a person with Exceptions>`.
* :ref:`I know how to test that an Exception is raised<how to test that an Exception is raised>`.
* :ref:`I know how to use Exception handlers in programs<how to handle Exceptions in programs>`.
* :ref:`I know how to make a person with loops<how to make a person with loops>`.

.. toctree::
  :titlesonly:
  :maxdepth: 1


  ../../exceptions/AssertionError/AssertionError_w_loops
  ../../truth_table/projects/atm/atm_w_loops
  ../../basic_objects/booleans/booleans_w_loops
  ../../truth_table/projects/car/car_w_loops
  ../../truth_table/projects/elevator/elevator_w_loops
  ../../functions/functions_w_loops
  ../../truth_table/projects/microwave/microwave_w_loops
  ../../basic_objects/none_w_loops
  ../../objects/objects_w_loops
  ../../how_to/telephone/telephone_w_loops
  ../../truth_table/projects/traffic_light/traffic_light_w_loops
  ../../truth_table/binary_operations/binary_operations_w_loops

:ref:`Would you like to test AssertionError with loops?<test AssertionError with loops>`

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