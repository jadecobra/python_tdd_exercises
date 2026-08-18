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

* :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` have the same three tests.
* :ref:`test_when_year_of_birth_is_not_an_integer` has four tests that are basically the same, the only thing that changes are the values for the ``year_of_birth`` parameter.

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
  :lines: 75-105

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

    tests/test_person.py .........                  [100%]

    ================= 9 passed in W.XYs ==================

----

*********************************************************************************
extract test_factory_function
*********************************************************************************

The tests for the :ref:`factory function<test person factory>` in :ref:`test_john`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` make a :ref:`call<how to call a function with input>` to the :ref:`factory function<test person factory>` then compare the result with a string_.

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the :ref:`factory function<test person factory>` to ``tests/test_person.py``

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 10-22

  class TestPerson(unittest.TestCase):

      @staticmethod
      def calculate_age(year_of_birth):
          return (
              datetime.date.today().year
            - year_of_birth
          )

      def test_factory_function(self):
          people = (
              ('joe', 'blow', 'M', 1996),
          )
          for a_person in people:
              reality = src.person.factory(
                  first_name=a_person[0],
                  last_name=a_person[1],
                  sex=a_person[2],
                  year_of_birth=a_person[3],
              )
              my_expectation = None
              self.assertEqual(reality, my_expectation)

      def test_joe(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'joe, blow, M, 1996' != None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``my_expectation`` to match ``reality``

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 12

      def test_factory_function(self):
          people = (
              ('joe', 'blow', 'M', 1996),
          )
          for a_person in people:
              reality = src.person.factory(
                  first_name=a_person[0],
                  last_name=a_person[1],
                  sex=a_person[2],
                  year_of_birth=a_person[3],
              )
              my_expectation = 'joe, blow, M, 1996'
              self.assertEqual(reality, my_expectation)

      def test_joe(self):

the test passes.

* I made a tuple_ named ``people`` that contains a tuple for ``joe``

  .. code-block:: python

    people = (
        ('joe', 'blow', 'M', 1996),
    )

* I use a :ref:`for loop<what is a for loop?>` to repeat the same commands for each item in the ``people`` tuple, in this case there is only one item - the tuple_ for ``joe``

  .. code-block:: python

    for a_person in (
        ('joe', 'blow', 'M', 1996),
    ):

* I use the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of each item in ``joe`` for the parameters when the test :ref:`calls<how to call a function with input>` the :ref:`factory function<test person factory>`

  .. code-block:: shell

    for a_person in people:
    ├── a_person = ('joe', 'blow', 'M', 1996)
    └── reality = src.person.factory(
            first_name=a_person[0],
            last_name=a_person[1],
            sex=a_person[2],
            year_of_birth=a_person[3],
        )
        └── src/person/__init__.py
            └── def factory(
                    first_name, last_name,
                    sex, year_of_birth,
                ):
                ├── first_name    = 'joe'
                ├── last_name     = 'blow'
                ├── sex           = 'M'
                ├── year_of_birth = 1996
                └── return (
                        f'{first_name}, {last_name},'
                        f' {sex}, {year_of_birth}'
                    )
                    return 'joe, blow, M, 1996'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add ``jane`` to the tuple_ of ``people``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3

        def test_factory_function(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
            )
            for a_person in people:

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'jane, doe, F, 1991' != 'joe, blow, M, 1996'

  because the result when the :ref:`factory function<test person factory>` is :ref:`called<how to call a function with input>` with ``'jane'``, ``'doe'``, ``'F'`` and ``'1991'`` as input is ``'jane, doe, F, 1991'`` not ``'joe, blow, M, 1996'``.

  .. code-block:: shell

        for a_person in (
    ┌───┴── ('jane', 'doe', 'F', 1991),
    │       ('joe', 'blow', 'M', 1996),
    │   ):
    ├── a_person = ('jane', 'doe', 'F', 1991)
    └── reality = src.person.factory(
            first_name=a_person[0],
            last_name=a_person[1],
            sex=a_person[2],
            year_of_birth=a_person[3],
        )
        └── src/person/__init__.py
            └── def factory(
                    first_name, last_name,
                    sex, year_of_birth,
                ):
                ├── first_name    = 'jane'
                ├── last_name     = 'doe'
                ├── sex           = 'F'
                ├── year_of_birth = 1991
                └── return (
                        f'{first_name}, {last_name},'
                        f' {sex}, {year_of_birth}'
                    )
                    return 'jane, doe, F, 1991'

* I change ``my_expectation`` to match ``reality`` for ``jane``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 13-14

        def test_factory_function(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
            )
            for a_person in people:
                reality = src.person.factory(
                    first_name=a_person[0],
                    last_name=a_person[1],
                    sex=a_person[2],
                    year_of_birth=a_person[3],
                )
                # my_expectation = 'joe, blow, M, 1996'
                my_expectation = 'jane, doe, F, 1991'
                self.assertEqual(reality, my_expectation)

        def test_joe(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'joe, blow, M, 1996' != 'jane, doe, F, 1991'

  because the result when the :ref:`factory function<test person factory>` is :ref:`called<how to call a function with input>` with ``'joe'``, ``'blow'``, ``'M'`` and ``'1996'`` as input is ``'joe, blow, M, 1996'`` not ``'jane, doe, F, 1991'``. The :ref:`for loop<what is a for loop?>` goes through each item in the ``people`` tuple_ one at a time.

* I change ``my_expectation`` in :ref:`test_factory_function<extract test_factory_function>` to an :ref:`f-string<what is string interpolation?>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 2-6

                # my_expectation = 'joe, blow, M, 1996'
                # my_expectation = 'jane, doe, F, 1991'
                my_expectation = (
                    f'{a_person[0]}, {a_person[1]},'
                    f' {a_person[2]}, {a_person[3]}'
                )
                self.assertEqual(reality, my_expectation)

        def test_joe(self):

  the test passes.

* I add :ref:`variables<what is a variable?>` for ``a_person[0]``, ``a_person[1]``, ``a_person[2]`` and ``a_person[3]``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 7-10

        def test_factory_function(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
            )
            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]

                reality = src.person.factory(
                    first_name=a_person[0],
                    last_name=a_person[1],
                    sex=a_person[2],
                    year_of_birth=a_person[3],
                )

* I use the :ref:`variables<what is a variable?>` for ``a_person[0]``, ``a_person[1]``, ``a_person[2]`` and ``a_person[3]``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2-9, 14-17

                reality = src.person.factory(
                    # first_name=a_person[0],
                    # last_name=a_person[1],
                    # sex=a_person[2],
                    # year_of_birth=a_person[3],
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                )
                # my_expectation = 'joe, blow, M, 1996'
                # my_expectation = 'jane, doe, F, 1991'
                my_expectation = (
                    # f'{a_person[0]}, {a_person[1]},'
                    # f' {a_person[2]}, {a_person[3]}'
                    f'{first_name}, {last_name},'
                    f' {sex}, {year_of_birth}'
                )
                self.assertEqual(reality, my_expectation)

        def test_joe(self):

  the test is still green.

* I add a tuple_ for ``mary``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5

        def test_factory_function(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
            )
            for a_person in people:

  still green.

* I add a tuple_ for ``john``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 6

        def test_factory_function(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
            )
            for a_person in people:

  green, showing that for each tuple_ in the ``people`` tuple_, the :ref:`assertion<what is an assertion?>` is :ref:`True<test_what_is_true>`.

* I add a tuple_ for a person with a string_ as the ``year_of_birth``

  .. code-block:: python
    :lineno-start: 15

        def test_factory_function(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a string'),
            )
            for a_person in people:

  the test is still green, because the :ref:`factory function<test person factory>` returns a string with the inputs it gets.

* I remove the commented lines from :ref:`test_factory_function<extract test_factory_function>`

  .. code-block:: python
    :lineno-start: 15

        def test_factory_function(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a string'),
            )
            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]

                reality = src.person.factory(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                )
                my_expectation = (
                    f'{first_name}, {last_name},'
                    f' {sex}, {year_of_birth}'
                )
                self.assertEqual(reality, my_expectation)

        def test_joe(self):

* I remove the test for the :ref:`factory function<test person factory>` from :ref:`test_joe` since it is now a repetition

  .. code-block:: python
    :lineno-start: 41

        def test_joe(self):
            first_name = 'joe'
            last_name = 'blow'
            sex = 'M'
            year_of_birth = 1996

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
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = joe.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(joe.can_vote(), True)
            self.assertEqual(joe.can_get_license(), False)

        def test_jane(self):

* I remove the test for the :ref:`factory function<test person factory>` from :ref:`test_jane` since it is now a repetition

  .. code-block:: python
    :lineno-start: 73

        def test_jane(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = 1991

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
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                passed_test=True,
            )

            reality = jane.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(jane.can_vote(), True)
            self.assertEqual(jane.can_get_license(), True)

        def test_john(self):

* I remove the test for the :ref:`factory function<test person factory>` from :ref:`test_john` since it is now a repetition

  .. code-block:: python
    :lineno-start: 106

        def test_john(self):
            first_name = 'john'
            last_name = 'smith'
            sex = 'M'
            year_of_birth = 1980

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
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                is_citizen=False,
            )

            reality = john.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(john.can_vote(), False)
            self.assertEqual(john.can_get_license(), False)

        def test_mary(self):

* I remove the test for the :ref:`factory function<test person factory>` from :ref:`test_mary` since it is now a repetition

  .. code-block:: python
    :lineno-start: 139

        def test_mary(self):
            first_name = 'mary'
            last_name = 'public'
            sex = 'F'
            year_of_birth = 2000

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
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                is_citizen=False,
                passed_test=True,
            )

            reality = mary.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(mary.can_vote(), False)
            self.assertEqual(mary.can_get_license(), True)

        def test_underage_citizen(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract test_factory_function'

The :ref:`for loop<what is a for loop?>` allows me to test any number of people with the same test. I no longer have to write one test for each person.

----

*********************************************************************************
extract test_say_hello_function
*********************************************************************************

The tests for the :ref:`say_hello function<test say_hello function>` in :ref:`test_john`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` make a :ref:`call<how to call a function with input>` to the :ref:`say_hello function<test say_hello function>` then compare the result with a string_

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the :ref:`say_hello function<test say_hello function>`

.. code-block:: python
  :lineno-start: 39
  :emphasize-lines: 3-14, 16-22

              self.assertEqual(reality, my_expectation)

      def test_say_hello_function(self):
          people = (
              ('jane', 'doe', 'F', 1991),
              ('joe', 'blow', 'M', 1996),
              ('mary', 'public', 'F', 2000),
              ('john', 'smith', 'M', 1980),
              ('first_name', 'last_name', 'F', 'a string'),
          )
          for a_person in people:
              first_name = a_person[0]
              last_name = a_person[1]
              year_of_birth = a_person[3]

              reality = src.person.say_hello(
                  first_name=first_name,
                  last_name=last_name,
                  year_of_birth=year_of_birth,
              )
              my_expectation = None
              self.assertEqual(reality, my_expectation)

      def test_joe(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError:
      'Hello, my name is jane doe and I am 35.'
   != None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``my_expectation`` in :ref:`test_say_hello_function<extract test_say_hello_function>` to match the string_ in the terminal_

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 6-9

                reality = src.person.say_hello(
                    first_name=first_name,
                    last_name=last_name,
                    year_of_birth=year_of_birth,
                )
                my_expectation = (
                    'Hello, my name is jane doe'
                    ' and I am 35.'
                )
                self.assertEqual(reality, my_expectation)

        def test_joe(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hello, my name is joe blow and I am 30.'
     != 'Hello, my name is jane doe and I am 35.'

  the test passed for ``jane`` but fails for ``joe``.

* I change ``my_expectation`` to an :ref:`f-string<what is string interpolation?>` in :ref:`test_say_hello_function<extract test_say_hello_function>`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 6-14

                reality = src.person.say_hello(
                    first_name=first_name,
                    last_name=last_name,
                    year_of_birth=year_of_birth,
                )
                # my_expectation = (
                #     'Hello, my name is jane doe'
                #     ' and I am 35.'
                # )
                my_expectation = (
                    f'Hello, my name is {first_name}'
                    f' {last_name} and I am'
                    f' {self.calculate_age(year_of_birth)}.'
                )
                self.assertEqual(reality, my_expectation)

        def test_joe(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError>`

  .. code-block:: python

    E           TypeError

  because the :ref:`say_hello function<test say_hello function>` calls the :ref:`calculate_age function<extract calculate_age function>` which raises :ref:`TypeError<what causes TypeError?>` when ``year_of_birth`` is not an integer_

  .. code-block:: shell

        for a_person in (
        │   ('jane', 'doe', 'F', 1991),
        │   ('joe', 'blow', 'M', 1996),
        │   ('mary', 'public', 'F', 2000),
        │   ('john', 'smith', 'M', 1980),
    ┌───┴── ('first_name', 'last_name', 'F', 'a string'),
    │   ):
    ├── a_person = ('first_name', 'last_name', 'F', 'a string')
    ├── first_name = a_person[0]
    ├── last_name = a_person[1]
    ├── year_of_birth = a_person[3]
    └── reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        └── src/person/__init__.py
            └── def say_hello(
                    first_name, last_name, year_of_birth,
                ):
                ├── first_name    = 'first_name'
                ├── last_name     = 'last_name'
                ├── year_of_birth = 'a string'
                └── return (
                    ├── f'Hello, my name is {first_name}'
                    ├── f' {last_name} and I am'
                    └──  f' {calculate_age(year_of_birth)}.'
                    )   │
                        └── def calculate_age(year_of_birth):
                            └── if not isinstance(
                                      year_of_birth, int
                                ):
                                └── raise TypeError
                                ...

* I open ``__init__.py`` from the ``person`` folder_ in the ``src`` folder_

* I add a message to the :ref:`calculate_age function<extract calculate_age function>` for when :ref:`TypeError<what causes TypeError?>` is :ref:`raised<how to raise an Exception>`, in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 44
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

* I add a :ref:`try statement<how to handle Exceptions>` to :ref:`test_say_hello_function<extract test_say_hello_function>` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 6-13

            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                year_of_birth = a_person[3]

                try:
                    reality = src.person.say_hello(
                        first_name=first_name,
                        last_name=last_name,
                        year_of_birth=year_of_birth,
                    )
                except TypeError:
                    pass

                # my_expectation = (
                #     'Hello, my name is jane doe'
                #     ' and I am 35.'
                # )

  the terminal_ is my friend, and shows :ref:`TypeError`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'int' and 'str'

  because ``my_expectation`` in :ref:`test_say_hello_function<extract test_say_hello_function>` makes a :ref:`call<how to call a function with input>` to the :ref:`calculate_age method of TestPerson<extract calculate_age method>` which raises :ref:`TypeError<what causes TypeError?>` because :ref:`I cannot do subtraction with a string and a number<test_type_error_w_the_unmixables>`.

  .. code-block:: shell

        for a_person in (
        │   ('jane', 'doe', 'F', 1991),
        │   ('joe', 'blow', 'M', 1996),
        │   ('mary', 'public', 'F', 2000),
        │   ('john', 'smith', 'M', 1980),
    ┌───┴── ('first_name', 'last_name', 'F', 'a string'),
    │   ):
    ├── a_person = ('first_name', 'last_name', 'F', 'a string')
    ├── first_name = a_person[0]
    ├── last_name = a_person[1]
    ├── year_of_birth = a_person[3]
    │   ...
    └── my_expectation = (
        ├── f'Hello, my name is {first_name}'
        ├── f' {last_name} and I am'
        └── f' {self.calculate_age(year_of_birth)}.'
        )   │
            │   @staticmethod
            └── def calculate_age(year_of_birth):
                ├── year_of_birth = 'a string'
                └── return (
                        datetime.date.today().year
                      - year_of_birth
                    )

* I add an :ref:`else clause<how to use try...except...else>` to :ref:`test_say_hello_function<extract test_say_hello_function>` so that it only runs the :ref:`assertion<what is an assertion?>` if the :ref:`call to the say_hello function<extract say_hello function>` does not raise :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 9-15

                try:
                    reality = src.person.say_hello(
                        first_name=first_name,
                        last_name=last_name,
                        year_of_birth=year_of_birth,
                    )
                except TypeError:
                    pass
                else:
                    my_expectation = (
                        f'Hello, my name is {first_name}'
                        f' {last_name} and I am'
                        f' {self.calculate_age(year_of_birth)}.'
                    )
                    self.assertEqual(reality, my_expectation)

                # my_expectation = (
                #     'Hello, my name is jane doe'
                #     ' and I am 35.'
                # )

        def test_joe(self):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I want to test the error message to make sure :ref:`test_say_hello_function<extract test_say_hello_function>` only catches :ref:`TypeError<what causes TypeError?>` with this specific message. I can use the :ref:`Exception<how to test that an Exception is raised>` in the :ref:`except block` as an :ref:`object<everything is an object>`.

  .. code-block:: python
    :lineno-start: 54
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

  the test is still green

* I add :ref:`assertEqual<test_assert_equal>` to the :ref:`except block<how to handle Exceptions>` with the `dir built-in function`_ to see the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the :ref:`Exception<how to test that an Exception is raised>` in the :ref:`except block<how to handle Exceptions>`

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2

                except TypeError as error:
                    self.assertEqual(dir(error), [])
                else:

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` with the list of :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>`. Three of the names stand out because they do not have double underscores (``__``) before and after - ``add_note``, ``args`` and ``with_traceback``.

* I change the :ref:`assertion<what is an assertion?>` to see what is in ``add_note``

  .. code-block:: python
    :lineno-start: 60
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
    :lineno-start: 60
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

* I change the :ref:`assertion<what is an assertion?>` to see what is in ``args``

  .. code-block:: python
    :lineno-start: 60
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
    :lineno-start: 60
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
    :lineno-start: 44
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

* I undo the change

  .. code-block:: python
    :lineno-start: 44

    def calculate_age(year_of_birth):
        if not isinstance(year_of_birth, int):
            raise TypeError(
                f"'{year_of_birth}' is not an integer"
            )

        age = (
            datetime.date.today().year
          - year_of_birth
        )

        if age > 120:
            raise ValueError
        return age


    def say_hello(
        first_name, last_name, year_of_birth,
    ):

  the test is green again.

* I remove the commented lines from :ref:`test_say_hello_function<extract test_say_hello_function>` in ``tests/test_person.py``

  .. code-block:: python
    :emphasize-lines: 41

        def test_say_hello_function(self):
            people = (
                ('jane', 'doe', 'F', 1991),
                ('joe', 'blow', 'M', 1996),
                ('mary', 'public', 'F', 2000),
                ('john', 'smith', 'M', 1980),
                ('first_name', 'last_name', 'F', 'a string'),
            )
            for a_person in people:
                first_name = a_person[0]
                last_name = a_person[1]
                year_of_birth = a_person[3]

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
                    my_expectation = (
                        f'Hello, my name is {first_name}'
                        f' {last_name} and I am'
                        f' {self.calculate_age(year_of_birth)}.'
                    )
                    self.assertEqual(reality, my_expectation)

        def test_joe(self):

* I remove the test for the :ref:`say_hello function<test say_hello function>` from :ref:`test_joe` since it is now a repetition, and move ``my_expectation`` below ``reality`` in the test for the :ref:`say_hello method<test say_hello method>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 15-19

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

            reality = joe.say_hello()
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {self.calculate_age(year_of_birth)}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(joe.can_vote(), True)
            self.assertEqual(joe.can_get_license(), False)

        def test_jane(self):

* I remove the test for the :ref:`say_hello function<test say_hello function>` from :ref:`test_jane` since it is now a repetition, and move ``my_expectation`` below ``reality`` in the test for the :ref:`say_hello method<test say_hello method>`

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 16-20

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

            reality = jane.say_hello()
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {self.calculate_age(year_of_birth)}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(jane.can_vote(), True)
            self.assertEqual(jane.can_get_license(), True)

        def test_john(self):

* I remove the test for the :ref:`say_hello function<test say_hello function>` from :ref:`test_john` since it is now a repetition, and move ``my_expectation`` below ``reality`` in the test for the :ref:`say_hello method<test say_hello method>`

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 16-20

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
            )

            reality = john.say_hello()
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {self.calculate_age(year_of_birth)}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(john.can_vote(), False)
            self.assertEqual(john.can_get_license(), False)

        def test_mary(self):

* I remove the test for the :ref:`say_hello function<test say_hello function>` from :ref:`test_mary` since it is now a repetition, and move ``my_expectation`` below ``reality`` in the test for the :ref:`say_hello method<test say_hello method>`

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 17-21

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

            reality = mary.say_hello()
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {self.calculate_age(year_of_birth)}.'
            )
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(mary.can_vote(), False)
            self.assertEqual(mary.can_get_license(), True)

        def test_underage_citizen(self):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract test_say_hello_function'

For each person in the ``people`` tuple_, this test :ref:`calls the say_hello function<test say_hello function>`

* If the :ref:`call raises TypeError<how to raise an Exception>`, it :ref:`asserts<what is an assertion?>` that the error message is correct

  - If the error message is not correct it raises :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: shell

          for a_person in (
          │   ('jane', 'doe', 'F', 1991),
          │   ('joe', 'blow', 'M', 1996),
          │   ('mary', 'public', 'F', 2000),
          │   ('john', 'smith', 'M', 1980),
      ┌───┴── ('first_name', 'last_name', 'F', 'a string'),
      │   ):
      ├── a_person = ('first_name', 'last_name', 'F', 'a string')
      ├── first_name = a_person[0]
      ├── last_name = a_person[1]
      ├── year_of_birth = a_person[3]
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
                      ├── first_name    = 'first_name'
                      ├── last_name     = 'last_name'
                      ├── year_of_birth = 'a string'
                      └── return (
                          ├── f'Hello, my name is {first_name}'
                          ├── f' {last_name} and I am'
                          └── f' {calculate_age(year_of_birth)}.'
                          )   │
                              └── def calculate_age(year_of_birth):
                                  └── if not isinstance(
                                          year_of_birth, int
                                      ):
      ┌───────────────────────────────┴── raise TypeError(
      │                                       'BOOM!!!'
      │                                   )
      └── except TypeError as error:
          └── self.assertEqual(
                  error.args[0],
                  f"'{year_of_birth}' is not an integer"
              )
              └── raise AssertionError
          else:
              ...

  - If the error message is correct the test passes

    .. code-block:: shell

          for a_person in (
          │   ('jane', 'doe', 'F', 1991),
          │   ('joe', 'blow', 'M', 1996),
          │   ('mary', 'public', 'F', 2000),
          │   ('john', 'smith', 'M', 1980),
      ┌───┴── ('first_name', 'last_name', 'F', 'a string'),
      │   ):
      ├── a_person = ('first_name', 'last_name', 'F', 'a string')
      ├── first_name = a_person[0]
      ├── last_name = a_person[1]
      ├── year_of_birth = a_person[3]
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
                      ├── first_name    = 'first_name'
                      ├── last_name     = 'last_name'
                      ├── year_of_birth = 'a string'
                      └── return (
                          ├── f'Hello, my name is {first_name}'
                          ├── f' {last_name} and I am'
                          └── f' {calculate_age(year_of_birth)}.'
                          )   │
                              └── def calculate_age(year_of_birth):
                                  └── if not isinstance(
                                          year_of_birth, int
                                      ):
      ┌───────────────────────────────┴── raise TypeError(
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

* If the :ref:`call to the say_hello function<test say_hello function>` does not :ref:`raise TypeError<how to raise an Exception>`, it :ref:`asserts<what is an assertion?>` that the result of the :ref:`call<how to call a function with input>` matches the expectation

  .. code-block:: shell

          for a_person in (
          │   ('jane', 'doe', 'F', 1991),
          │   ('joe', 'blow', 'M', 1996),
          │   ('mary', 'public', 'F', 2000),
      ┌───┴── ('john', 'smith', 'M', 1980),
      │       ('first_name', 'last_name', 'F', 'a string'),
      │   ):
      ├── a_person = ('john', 'smith', 'M', 1980),
      ├── first_name = a_person[0]
      ├── last_name = a_person[1]
      ├── year_of_birth = a_person[3]
      ├── try:
      │       reality = src.person.say_hello(
      │           first_name=first_name,
      │           last_name=last_name,
      │           year_of_birth=year_of_birth,
      │       )
      │       └── src/person/__init__.py
      │           └── def say_hello(
      │                   first_name, last_name, year_of_birth,
      │               ):
      │               ├── first_name    = 'john'
      │               ├── last_name     = 'smith'
      │               ├── year_of_birth = 1980
      │               └── return (
      │                   ├── f'Hello, my name is {first_name}'
      │                   ├── f' {last_name} and I am'
      │                   └── f' {calculate_age(year_of_birth)}.'
      │                   )   │
      │                       └── def calculate_age(year_of_birth):
      │                           ├── ...
      │                           └── return age
      ├── except TypeError as error:
      │       ...
      └── else:
          ├── my_expectation = (
          │   ├── f'Hello, my name is {first_name}'
          │   ├── f' {last_name} and I am'
          │   └── f' {self.calculate_age(year_of_birth)}.'
          │   )   │
          │       │   @staticmethod
          │       └── def calculate_age(year_of_birth):
          │           └── return (
          │                   datetime.date.today().year
          │                 - year_of_birth
          │               )
          └── self.assertEqual(reality, my_expectation)


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
* :ref:`I know how to make a person with a class<how to make a person with a class>`.
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