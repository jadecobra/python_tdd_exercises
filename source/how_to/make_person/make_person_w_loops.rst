.. meta::
  :description:
  :keywords:
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
  :language: python
  :linenos:
  :caption: person/tests/test_person.py
  :lines: 1-32

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :lineno-start: 34
  :caption: person/tests/test_person.py
  :lines: 34-53

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :lineno-start: 55
  :caption: person/tests/test_person.py
  :lines: 55-73

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :lineno-start: 75
  :caption: person/tests/test_person.py
  :lines: 75-92

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :lineno-start: 94
  :caption: person/tests/test_person.py
  :lines: 94-105

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :lineno-start: 107
  :caption: person/tests/test_person.py
  :lines: 107-119

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :lineno-start: 121
  :caption: person/tests/test_person.py
  :lines: 121-128

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :lineno-start: 130
  :caption: person/tests/test_person.py
  :lines: 130-147

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
    :lineno-start: 44
    :emphasize-lines: 19-29

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
            for person in people:

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
            for person in people:

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
            for person in people:

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
            for person in people:

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

* I remove the :ref:`assert_person_factory_works method<extract assert_person_factory_works function>` from the :ref:`TestPerson class<add TestPerson class>`

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
    :emphasize-lines: 3

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

* I remove the :ref:`assert_say_hello_works method<extract assert_say_hello_works function>` from the :ref:`TestPerson class<add TestPerson class>`

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

The tests in :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` make an :ref:`instance<how to test if something is an instance>` of the :ref:`Person class<add Person class>`, then :ref:`call<how to call a function with input>` its :ref:`say_hello method<add say_hello method>` comparing the results in :ref:`assertions<what is an assertion?>`

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

I add a test for the :ref:`say_hello method<add say_hello method>` of the :ref:`Person class<add Person class>`

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

* I remove the :ref:`assert_person_can_say_hello method<extract assert_person_can_say_hello function>` from the :ref:`TestPerson class<add TestPerson class>`

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

For each person in the ``people`` tuple_, this test :ref:`makes an instance<how to test if something is an instance>` of the :ref:`Person class<add Person class>` which makes an ``age`` :ref:`attribute<what is an object attribute?>` by :ref:`calling<how to call a function with input>` the :ref:`calculate_age function<extract calculate_age function>` with the given ``year_of_birth`` parameter.

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

* If the :ref:`call to the calculate_age function<extract calculate_age function>` from the :ref:`__init__ method<the constructor method>` of the :ref:`Person class<add Person class>` does not :ref:`raise TypeError<how to raise an Exception>`, it :ref:`asserts<what is an assertion?>` that the result of the :ref:`call to the say_hello method<add say_hello method>` matches the expectation

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

* I add an :ref:`object attribute<what is an object attribute?>` for the ``people`` tuple_ to the :ref:`TestPerson class<add TestPerson class>`

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

The tests in :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john`, :ref:`test_mary` and :ref:`test_underage_citizen<add condition to can_vote>` make an :ref:`instance<how to test if something is an instance>` of the :ref:`Person class<add Person class>`, then :ref:`call<how to call a function with input>` its :ref:`can_vote method<add can_vote method>` comparing the results in :ref:`assertions<what is an assertion?>`.

.. code-block:: python

    a_person = src.person.Person(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
        is_citizen=False | True,
        passed_test=False | True,
    )
    self.assertEqual(a_person.can_vote(), False | True)

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
                    a_person = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='F',
                        year_of_birth=row[0],
                        is_citizen=row[1],
                    )
                    self.assertEqual(a_person.can_vote(), True)

        def test_joe(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  SUBFAILED(row=(2009, True)) ...test_if_person_can_vote -
      AssertionError: False != True

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
                  a_person = src.person.Person(
                      first_name='first_name',
                      last_name='last_name',
                      sex='F',
                      year_of_birth=row[0],
                      is_citizen=row[1],
                  )
                  self.assertEqual(a_person.can_vote(), False)

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
                    a_person = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='F',
                        year_of_birth=row[0],
                        is_citizen=row[1],
                    )
                    self.assertEqual(a_person.can_vote(), row[3])

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

                    self.assertEqual(a_person.can_vote(), row[2])

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
                    a_person = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='F',
                        year_of_birth=row[0],
                        is_citizen=row[1],
                    )
                    self.assertEqual(
                        a_person.can_vote(), row[2]
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

The tests in :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john`, :ref:`test_mary` and :ref:`test_underage_citizen<add condition to can_vote>`  make an :ref:`instance<how to test if something is an instance>` of the :ref:`Person class<add Person class>`, then :ref:`call<how to call a function with input>` its :ref:`can_get_license method<add can_get_license method>` comparing the results in :ref:`assertions<what is an assertion?>`.

.. code-block:: python

    a_person = src.person.Person(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
        is_citizen=False | True,
        passed_test=False | True,
    )
    self.assertEqual(a_person.can_get_license(), False | True)

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

I add a test with an :ref:`assertion<what is an assertion?>` for if a person is :red:`NOT younger` than ``18`` AND has :red:`NOT passed` the test.

==============  ============== ================
age < 18        passed test    can get license
==============  ============== ================
:red:`False`    :red:`False`   :red:`False`
==============  ============== ================

.. code-block:: python
  :lineno-start: 120
  :emphasize-lines: 3-18

                    self.assertEqual(a_person.can_vote(), row[2])

        def test_if_person_can_get_license(self):
            truth_table = (
                (datetime.date.today().year-18, False, False),
            )
            for row in truth_table:
                with self.subTest(row=row):
                    a_person = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=row[0],
                        passed_test=row[1],
                    )
                    self.assertEqual(
                        a_person.can_get_license(), True
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
                      a_person.can_get_license(), False
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
                        a_person.can_get_license(), row[-1]
                    )

        def test_joe(self):

  the test passes.

* I add a tuple_ to the ``truth_table`` tuple_ for if a person is :green:`younger than` ``18`` AND has :red:`NOT passed` the test

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

* I add a tuple_ to the ``truth_table`` tuple_ for if a person is :green:`younger than` ``18`` AND has :green:`passed` the test

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
                    a_person = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=row[0],
                        passed_test=row[1],
                    )
                    self.assertEqual(
                        a_person.can_get_license(), row[-1]
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

* I add an :ref:`object attribute<what is an object attribute?>` for the ``truth_table`` tuple_ to the :ref:`TestPerson class<add TestPerson class>`

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
                    a_person = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='F',
                        year_of_birth=row[0],
                        is_citizen=row[1],
                    )
                    self.assertEqual(a_person.can_vote(), row[2])

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
                    a_person = src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=row[0],
                        passed_test=row[1],
                    )
                    self.assertEqual(
                        a_person.can_get_license(), row[-1]
                    )

        def test_when_person_is_older_than_120(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract truth_table object attribute'

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
  :lineno-start: 136
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
  :lineno-start: 136
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
    :lineno-start: 136
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
    :lineno-start: 136

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
  :lineno-start: 151
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
  :lineno-start: 136
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
    :lineno-start: 136
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
    :lineno-start: 151
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
    :lineno-start: 151

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
  :lineno-start: 132
  :emphasize-lines: 5-21

                  self.assertEqual(
                      a_person.can_get_license(), row[-1]
                  )

      def test_if_person_is_not_alive(self):
          years = (
              self.this_year+1,
              self.this_year-121,
          )
          for year_of_birth in years:
              with self.subTest(year_of_birth=year_of_birth):
                  with self.assertRaisesRegex(
                      ValueError,
                      'BOOM!!!'
                  ):
                      src.person.Person(
                          first_name='first_name',
                          last_name='last_name',
                          sex='M',
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

I change the error message in :ref:`test_if_person_is_not_alive` to match

.. code-block:: python
  :lineno-start: 136
  :emphasize-lines:

      def test_if_person_is_not_alive(self):
          years = (
              self.this_year+1,
              self.this_year-121,
          )
          for year_of_birth in years:
              with self.subTest(year_of_birth=year_of_birth):
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

      def test_when_person_is_older_than_120(self):

the test passses.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I can put the two `with statements`_ together

  .. code-block:: python
    :lineno-start: 136

* I remove :ref:`test_when_person_is_older_than_120` because it is now a repetition

  .. code-block:: python
    :lineno-start: 136

        def test_if_person_is_not_alive(self):
            years = (
                self.this_year+1,
                self.this_year-121,
            )
            for year_of_birth in years:
                with self.subTest(year_of_birth=year_of_birth):
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

* I remove :ref:`test_when_year_of_birth_is_the_future` because it is now a repetition

  .. code-block:: python
    :lineno-start: 136

        def test_if_person_is_not_alive(self):
        years = (
            self.this_year+1,
            self.this_year-121,
        )
        for year_of_birth in years:
            with self.subTest(year_of_birth=year_of_birth):
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

    def test_when_year_of_birth_is_not_an_integer(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract test_if_person_is_not_alive'









----

*********************************************************************************
use loops in test_when_year_of_birth_is_not_an_integer
*********************************************************************************

:ref:`test_when_perso`


* I change the :ref:`Exception raised<how to raise an Exception>` in the :ref:`calculate_age function<extract calculate_age function>` if the value of the ``year_of_birth`` parameter is not an integer_

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

* I can use the :ref:`try statement<how to handle Exceptions>` to make sure a program can make a decision when it runs into an :ref:`Exception<how to test that an Exception is raised>`.
* I can use the :ref:`try statement<how to handle Exceptions>` in a test to confirm that a program :ref:`raises an Exception<how to raise an Exception>` when certain conditions are met.
* I can use the :ref:`raise statement<how to raise an Exception>` to make an :ref:`Exception<how to test that an Exception is raised>` happen to stop a program from running past a certain point.

My tests still have problems:

* The attribute tests - :ref:`test_dir_person_class` and :ref:`test_dir_person_instance` catch changes to the :ref:`attributes and methods of the Person class<test_dir_person_instance>` and they are a problem to maintain. There has to be a better way.
* :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` all still have the same three tests. There has to be a better way.
* :ref:`test_when_year_of_birth_is_not_an_integer` has four tests that are basically the same, the only thing that changes are the values for the ``year_of_birth`` parameter. There has to be a better way.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a person with Exceptions: tests and solutions>`

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

.. toctree::
  :titlesonly:
  :maxdepth: 1

  ../../basic_objects/lists
  ../../basic_objects/list_comprehensions

:ref:`Would you like to test handling Exceptions in tests?<how to test that an Exception is raised>`

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