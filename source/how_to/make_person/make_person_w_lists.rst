.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

.. _test person with lists:

#################################################################################
test person with lists
#################################################################################

----

I want to use :ref:`lists<what is a list?>` in the ``person`` project.

----

*********************************************************************************
preview
*********************************************************************************

I change these tests in the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_lists.py
  :caption: person/tests/test_person.py
  :language: python
  :linenos:
  :lines: 1-22

.. literalinclude:: ../../code/person/tests/test_person_w_lists.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 24
  :lines: 24-80

.. literalinclude:: ../../code/person/tests/test_person_w_lists.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 82
  :lines: 82-104

.. literalinclude:: ../../code/person/tests/test_person_w_lists.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 106
  :lines: 106-120

.. literalinclude:: ../../code/person/tests/test_person_w_lists.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 143
  :lines: 143-156

.. literalinclude:: ../../code/person/tests/test_person_w_lists.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 158
  :lines: 158-177

-----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd person

* I open ``test_person.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now

----

*********************************************************************************
add people list to test_person_object
*********************************************************************************

The ``people`` :ref:`object attribute<what is an object attribute?>` is a tuple_ with some repetition and :ref:`conditions<if statements?>`.

.. code-block:: python

  year_of_birth (not_younger_than_18 | younger_than_18),
  is_citizen (False | True),
  passed_test (False | True),
  can_vote (False | True),
  can_get_license (False | True),

The ``year_of_birth`` values are repeated for each combination of :ref:`booleans<what are booleans?>`. I want to make a :ref:`list<what is a list?>` that has the ``year_of_birth`` values once, and has the combinations for ``is_citizen``, ``passed_test``, ``can_vote`` and ``can_get_license`` tied to it.

- If ``year_of_birth`` is :red:`NOT an integer`

  ============== ============== ==============  ================
  is citizen     passed_test    can vote        can_get_license
  ============== ============== ==============  ================
  :green:`True`  :green:`True`  :red:`False`    :red:`False`
  :red:`False`   :green:`True`  :red:`False`    :red:`False`
  :green:`True`  :red:`False`   :red:`False`    :red:`False`
  :red:`False`   :red:`False`   :red:`False`    :red:`False`
  ============== ============== ==============  ================

- If a person is :green:`younger` than ``18``

  ============== ============== ==============  ================
  is citizen     passed_test    can vote        can_get_license
  ============== ============== ==============  ================
  :green:`True`  :green:`True`  :red:`False`    :red:`False`
  :red:`False`   :green:`True`  :red:`False`    :red:`False`
  :green:`True`  :red:`False`   :red:`False`    :red:`False`
  :red:`False`   :red:`False`   :red:`False`    :red:`False`
  ============== ============== ==============  ================

- If a person is :red:`NOT younger` than ``18``

  ============== ============== ==============  ================
  is citizen     passed_test    can vote        can_get_license
  ============== ============== ==============  ================
  :green:`True`  :green:`True`  :green:`True`   :green:`True`
  :red:`False`   :green:`True`  :red:`False`    :green:`True`
  :green:`True`  :red:`False`   :green:`True`   :red:`False`
  :red:`False`   :red:`False`   :red:`False`    :red:`False`
  ============== ============== ==============  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`list<what is a list?>` with an :ref:`assertion<what is an assertion?>` to :ref:`test_person_object`

.. code-block:: python
  :caption: person/tests/test_person.py
  :lineno-start: 79
  :emphasize-lines: 2-8, 10

      def test_person_object(self):
          people = []
          for year_of_birth in (
              self.not_younger_than_18,
              self.younger_than_18,
              None, 2027.0, '2027', (2027,),
          ):
              people.append((year_of_birth, ()))

          self.assertEqual(people, [])

          for (
              year_of_birth,
              is_citizen, passed_test,
              can_vote, can_get_license,
          ) in self.people:

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: Lists differ: [
      (XXXX, ()), (YYYY, ()), (None, ()),
      (2027.0, ()), ('2027', ()), ((2027,), ())
  ] != []

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I copy the :ref:`list<what is a list?>` from the terminal_ and paste it as the expectation of the new :ref:`assertion<what is an assertion?>` in :ref:`test_person_object<extract test_person_object>`

.. code-block:: python
  :caption: person/tests/test_person.py
  :lineno-start: 86
  :emphasize-lines: 3-13

              people.append((year_of_birth, ()))

          self.assertEqual(
              people,
              [
                  (XXXX, ()),
                  (YYYY, ()),
                  (None, ()),
                  (2027.0, ()),
                  ('2027', ()),
                  ((2027,), ())
              ]
          )

          for (
              year_of_birth,
              is_citizen, passed_test,
              can_vote, can_get_license,
          ) in self.people:

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use a :ref:`for loop<what is a for loop?>` to add the values of ``is_citizen`` to the tuple_ for each ``year_of_birth``

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 79
    :emphasize-lines: 2, 9-12

        def test_person_object(self):
            booleans = (False, True)
            people = []
            for year_of_birth in (
                self.not_younger_than_18,
                self.younger_than_18,
                None, 2027.0, '2027', (2027,),
            ):
                row = []
                for is_citizen in booleans:
                    row.append(is_citizen)
                people.append((year_of_birth, row))

            self.assertEqual(
                people,
                ...

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [
        (XXXX, [False, True]), (YYYY, [False, True]),
        (N[91 chars]ue])
    ] != [
        (XXXX, ()), (YYYY, ()), (None, ()),
        (2027.0, ())[25 chars] ())
    ]

  close, but not quite. I want each value of ``is_citizen`` to be its own tuple_ since I will be adding values for ``passed_test``, ``can_vote`` and ``can_get_license``

  .. code-block:: python

    (
        XXXX, [
            (True, True, True, True),
            (True, False, True, False),
            (False, True, False, True),
            (False, False, False, False),
        ],
        ...
    )

* I change the append statement for ``row``

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 87
    :emphasize-lines: 3

                row = []
                for is_citizen in booleans:
                    row.append((is_citizen,))
                people.append((year_of_birth, row))

  the terminal_ shows

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [
        (XXXX, [(False,), (True,)]), (YYYY, [(False,), ([127 chars],)])
    ] != [
        (XXXX, ()), (YYYY, ()), (None, ()),
        (2027.0, ())[25 chars] ())
    ]

  better.

* I add a :ref:`for loop<what is a for loop?>` for ``passed_test``

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 87
    :emphasize-lines: 3-4

                row = []
                for is_citizen in booleans:
                    for passed_test in booleans:
                        row.append((is_citizen, passed_test,))
                people.append((year_of_birth, row))

  the terminal_ shows

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [
        (XXXX, [
            (False, False),
            (False, True),
            (True, Fa[373 chars]e)])
    ] != [
        (XXXX, ()), (YYYY, ()), (None, ()),
        (2027.0, ())[25 chars] ())
    ]

  closer.

* I add a :ref:`for loop<what is a for loop?>` for ``can_vote``

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 87
    :emphasize-lines: 4-8

                row = []
                for is_citizen in booleans:
                    for passed_test in booleans:
                        for can_vote in booleans:
                            row.append((
                                is_citizen, passed_test,
                                can_vote,
                            ))
                people.append((year_of_birth, row))

  the terminal_ shows

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [
        (XXXX, [
            (False, False, False),
            (False, False, Tr[1045 chars]e)])
    ] != [
        (XXXX, ()), (YYYY, ()), (None, ()),
        (2027.0, ())[25 chars] ())
    ]

* I add a :ref:`for loop<what is a for loop?>` for ``can_get_license``

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 87
    :emphasize-lines: 5, 8

                row = []
                for is_citizen in booleans:
                    for passed_test in booleans:
                        for can_vote in booleans:
                            for can_get_license in booleans:
                                row.append((
                                    is_citizen, passed_test,
                                    can_vote, can_get_license,
                                ))
                people.append((year_of_birth, row))

  the terminal_ shows

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [
        (XXXX, [
            (False, False, False, False),
            (False, Fa[2701 chars]e)])
    ] != [
        (XXXX, ()), (YYYY, ()),
        (None, ()), (2027.0, ())[25 chars] ())
    ]

  lovely.

* I set maxDiff_ to :ref:`None<what is None?>` to see the entire difference between the :ref:`lists<what is a list?>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 79
    :emphasize-lines: 2

        def test_person_object(self):
            self.maxDiff = None

            booleans = (False, True)
            people = []

  each ``year_of_birth`` now has the sixteen combinations of ``is_citizen``, ``passed_test``, ``can_vote`` and  ``can_get_license``. It removes repetition of ``year_of_birth`` and is better than the ``people`` :ref:`object attribute<what is an object attribute?>` because it covers more cases.

* I remove the :ref:`assertion<what is an assertion?>` for the ``people`` :ref:`variable<what is a variable?>` then try the :ref:`variable` in place of ``self.people``

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 98
    :emphasize-lines: 7-8

                people.append((year_of_birth, row))

            for (
                year_of_birth,
                is_citizen, passed_test,
                can_vote, can_get_license,
            ) in people:
            # ) in self.people:
                with self.subTest(
                    a_person=(
                        self.first_name, self.last_name,
                        self.sex, year_of_birth,
                        is_citizen, passed_test,
                        can_vote, can_get_license,
                    )
                ):

  the terminal_ is my friend, and shows ValueError_

  .. code-block:: python
    :caption: terminal

    ValueError: not enough values to unpack (expected 5, got 2)

  because the ``people`` :ref:`variable<what is a variable?>` is a :ref:`list<what is a list?>` that contains tuples_ and each tuple_ contains two items not five.

  .. code-block:: python

    [
        (
            year_of_birth,
            [
                (False, False, False, False),
                (False, False, False, True),
                (False, False, True, False),
                (False, False, True, True),
                (False, True, False, False),
                (False, True, False, True),
                (False, True, True, False),
                (False, True, True, True),
                (True, False, False, False),
                (True, False, False, True),
                (True, False, True, False),
                (True, False, True, True),
                (True, True, False, False),
                (True, True, False, True),
                (True, True, True, False),
                (True, True, True, True)
            ]
        ),
        ...
    ]

* I change the :ref:`for loop<what is a for loop?>` to match what is in the :ref:`variable<what is a variable?>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 100
    :emphasize-lines: 2, 4-24

            for (
                year_of_birth, inputs_outputs
            ) in people:
                for (
                    is_citizen, passed_test,
                    can_vote, can_get_license,
                ) in inputs_outputs:
                    with self.subTest(
                        a_person=(
                            self.first_name, self.last_name,
                            self.sex, year_of_birth,
                            is_citizen, passed_test,
                            can_vote, can_get_license,
                        )
                    ):
                        try:
                            an_instance = src.person.Person(
                                first_name=self.first_name,
                                last_name=self.last_name,
                                sex=self.sex,
                                year_of_birth=year_of_birth,
                                is_citizen=is_citizen,
                                passed_test=passed_test,
                            )

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 100
    :emphasize-lines: 1-21

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
                            self.assertEqual(
                                an_instance.can_vote(), can_vote
                            )
                            self.assertEqual(
                                an_instance.can_get_license(),
                                can_get_license
                            )

        def test_say_hello_function(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for twenty four sub tests because the values for ``can_vote`` from the ``people`` :ref:`variable<what is a variable?>` do not match the expectation of the test. For example

  * since a person that is younger than ``18`` cannot vote or get a license even if they are a citizen and pass the test

    ``(younger_than_18, True, True, True, True)`` should be ``(younger_than_18, True, True, False, False)``

  * since a person that is NOT younger than ``18`` AND is NOT a citizen AND did not pass the test cannot vote or get a license

    ``(not_younger_than_18, False, False, True, True)`` should be ``(not_younger_than_18, False, False, False, False)``

* I change the values given to the :ref:`append method<test_append_adds_item_to_end_of_a_list>` for the results of ``can_vote`` and ``passed_test``

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 89
    :emphasize-lines: 8

                row = []
                for is_citizen in booleans:
                    for passed_test in booleans:
                        for can_vote in booleans:
                            for can_get_license in booleans:
                                row.append((
                                    is_citizen, passed_test,
                                    is_citizen, passed_test,
                                ))
                people.append((year_of_birth, row))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for twelve sub tests. I got twelve to pass.

* I remove the :ref:`for loops<what is a for loop?>` for ``can_vote`` and ``can_get_license`` since their values are based on ``is_citizen`` and ``passed_test``, a lot of the tuples_ are now repetitions

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 89
    :emphasize-lines: 4-7

                row = []
                for is_citizen in booleans:
                    for passed_test in booleans:
                        row.append((
                            is_citizen, passed_test,
                            is_citizen, passed_test,
                        ))
                people.append((year_of_birth, row))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for three sub tests

  .. code-block:: python
    :caption: terminal

    SUBFAILED(a_person=(
        'first_name', 'last_name', 'M',
        YYYY, False, True, ...
    )) ... AssertionError: False != True
    SUBFAILED(a_person=(
        'first_name', 'last_name', 'M',
        YYYY, True, False, ...
    )) ... AssertionError: False != True
    SUBFAILED(a_person=(
        'first_name', 'last_name', 'M',
        YYYY, True, True, ...
    )) ... AssertionError: False != True

* The remaining cases are for when ``year_of_birth`` makes the person younger than ``18`` or is NOT an integer, which means the expectation for those cases is :ref:`False<test_what_is_false>`. I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 89
    :emphasize-lines: 4-13

                row = []
                for is_citizen in booleans:
                    for passed_test in booleans:
                        if year_of_birth == self.not_younger_than_18:
                            row.append((
                                is_citizen, passed_test,
                                is_citizen, passed_test,
                            ))
                        else:
                            row.append((
                                is_citizen, passed_test,
                                False, False,
                            ))
                people.append((year_of_birth, row))

  the test passes.

* I use a :ref:`conditional expression<conditional expression>` with a :ref:`variable<what is a variable?>` to remove duplication of the tuple_

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 89
    :emphasize-lines: 4-11

                row = []
                for is_citizen in booleans:
                    for passed_test in booleans:
                        is_not_younger_than_18 = (
                            year_of_birth == self.not_younger_than_18
                        )
                        row.append((
                            is_citizen, passed_test,
                            is_citizen and is_not_younger_than_18,
                            passed_test and is_not_younger_than_18,
                        ))
                people.append((year_of_birth, row))

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` to see what is in the ``people`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 100
    :emphasize-lines: 3

                people.append((year_of_birth, row))

            self.assertEqual(people, [])

            for (
                year_of_birth, inputs_outputs
            ) in people:

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`. The ``people`` :ref:`list<what is a list?>` has tuples_ which have a value for ``year_of_birth`` and a tuple_ of the combinations for ``is_citizen``, ``passed_test`` and the expected result of a :ref:`call<how to call a function with input>` to the :ref:`can_vote<add can_vote method>` and :ref:`can_get_license methods<add can_get_license method>`.

  .. code-block:: python

    [
        (
            not_younger_than_18,
            [
                (False, False, False, False),
               (False, True, False, True),
               (True, False, True, False),
               (True, True, True, True)
            ]
        ),
        (
            younger_than_18,
            [
                (False, False, False, False),
                 (False, True, False, False),
                 (True, False, False, False),
                 (True, True, False, False)
            ]
        ),
        (
            not an integer,
            [
                (False, False, False, False),
                (False, True, False, False),
                (True, False, False, False),
                (True, True, False, False)
            ]
        ),
        ...
    ]

  I like this better than the ``people`` :ref:`object attribute<what is an object attribute?>` because it covers all combinations for ``is_citizen`` and ``passed_test`` for when ``year_of_birth`` is NOT an integer. The ``people`` :ref:`list<what is a list?>` is more complicated to make than the ``people`` :ref:`object attribute<what is an object attribute?>`.

* I undo the change

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 100

                people.append((year_of_birth, row))

            for (
                year_of_birth, inputs_outputs
            ) in people:

  the test is green again

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add people list to test_person_object'

----

*********************************************************************************
extract years_of_birth object attribute
*********************************************************************************

:ref:`test_person_object<extract test_person_object>`, :ref:`test_say_hello_function<extract test_say_hello_function>` and :ref:`test_person_factory<extract test_person_factory>` all use the same values for ``year_of_birth``

.. code-block:: python

  class TestPerson(unittest.TestCase):

      this_year = datetime.date.today().year
      not_younger_than_18 = this_year - 18
      younger_than_18 = this_year - 17

.. code-block:: python

  for year_of_birth in (
      self.not_younger_than_18,
      self.younger_than_18,
      None, 2027.0, '2027', (2027,),
  ):

.. code-block:: python

  for a_person in self.people:
      year_of_birth = a_person[0]

I can use an :ref:`object attribute<what is an object attribute?>` to remove the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I remove the ``people`` :ref:`object attribute<what is an object attribute?>`

.. code-block:: python
  :caption: person/tests/test_person.py
  :lineno-start: 6

  class TestPerson(unittest.TestCase):

      this_year = datetime.date.today().year
      not_younger_than_18 = this_year - 18
      younger_than_18 = this_year - 17

      first_name = 'first_name'
      last_name = 'last_name'
      sex = 'M'

      def calculate_age(self, year_of_birth):

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>` for :ref:`test_say_hello_function<extract test_say_hello_function>` and :ref:`test_person_factory<extract test_person_factory>`

.. code-block:: python
  :caption: terminal

  AttributeError: 'TestPerson' object
                  has no attribute 'people'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I copy the :ref:`for loop<what is a for loop?>` for ``year_of_birth`` from :ref:`test_person_object<extract test_person_object>` and paste it in :ref:`test_say_hello_function<extract test_say_hello_function>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 88
    :emphasize-lines: 2-6

        def test_say_hello_function(self):
            for year_of_birth in (
                self.not_younger_than_18,
                self.younger_than_18,
                None, 2027.0, '2027', (2027,),
            ):
                with self.subTest(
                    first_name=self.first_name,
                    year_of_birth=year_of_birth,
                ):

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>` for :ref:`test_person_factory<extract test_person_factory>`.

* I paste the :ref:`for loop<what is a for loop?>` for ``year_of_birth`` from :ref:`test_person_object<extract test_person_object>` in :ref:`test_person_factory<extract test_person_factory>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 119
    :emphasize-lines: 2-6

        def test_person_factory(self):
            for year_of_birth in (
                self.not_younger_than_18,
                self.younger_than_18,
                None, 2027.0, '2027', (2027,),
            ):
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

        def test_when_person_is_not_alive(self):

  the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`object attribute<what is an object attribute?>` for the years of birth

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 6
    :emphasize-lines: 7-11

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year
        not_younger_than_18 = this_year - 18
        younger_than_18 = this_year - 17

        years_of_birth = (
            not_younger_than_18,
            younger_than_18,
            None, 2027.0, '2027', (2027,),
        )

        first_name = 'first_name'

* I use the new :ref:`object attribute<what is an object attribute?>` in :ref:`test_person_object<extract test_person_object>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 25
    :emphasize-lines: 6

        def test_person_object(self):
            self.maxDiff = None

            booleans = (False, True)
            people = []
            for year_of_birth in self.years_of_birth:
                row = []

  the test is still green.

* I use the new :ref:`object attribute<what is an object attribute?>` in :ref:`test_say_hello_function<extract test_say_hello_function>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 90
    :emphasize-lines: 1

        def test_say_hello_function(self):
            for year_of_birth in self.years_of_birth:
                with self.subTest(
                    first_name=self.first_name,
                    year_of_birth=year_of_birth,
                ):

  still green.

* I use the new :ref:`object attribute<what is an object attribute?>` in :ref:`test_person_factory<extract test_person_factory>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 117
    :emphasize-lines: 2

        def test_person_factory(self):
            for year_of_birth in self.people:
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

        def test_when_person_is_not_alive(self):

  green.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'extract years_of_birth object attribute'

----

*********************************************************************************
test_dir_person_object with extend and sort
*********************************************************************************

The :ref:`attributes and methods of the Person object<test_dir_person_object>` are the :ref:`attributes and methods of 'object'<test_dir_object>` with extra things. I can make the :ref:`attributes and methods of the Person object<test_dir_person_object>` by adding the "extra" to the :ref:`attributes and methods of 'object'<test_dir_object>`, since they are both :ref:`lists<what is a list?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`variable<what is a variable?>` for the :ref:`attributes and methods of the Person object<test_dir_person_object>`, then add an :ref:`assertion<what is an assertion?>` for it, in :ref:`test_dir_person_object`

.. code-block:: python
  :caption: person/tests/test_person.py
  :lineno-start: 165
  :emphasize-lines: 2-10

      def test_dir_person_object(self):
          dir_person = dir(object)
          dir_person.extend((
              'can_get_license', 'can_vote',
              'check_age', 'say_hello',
          ))
          self.assertEqual(
              dir(src.person.Person),
              dir_person
          )

          self.assertEqual(
              dir(src.person.Person),

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: Lists differ: [
      '__c[24 chars]'__dict__', '__dir__', '__doc__',
      '__eq__', '_[381 chars]llo'
  ] != [
      '__c[24 chars]'__dir__', '__doc__', '__eq__',
      '__format__', [296 chars]llo'
  ]

with a note about the difference

.. code-block:: python
  :caption: terminal

  First list contains 5 additional elements.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use :ref:`extend<test_extend_adds_items_from_an_iterable_to_end_of_a_list>` to :ref:`append<test_append_adds_item_to_end_of_a_list>` the five additional elements

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 165
    :emphasize-lines: 4-6

        def test_dir_person_object(self):
            dir_person = dir(object)
            dir_person.extend((
                '__dict__', '__firstlineno__',
                '__module__', '__static_attributes__',
                '__weakref__',
                'can_get_license', 'can_vote',
                'check_age', 'say_hello',
            ))
            self.assertEqual(
                dir(src.person.Person),
                dir_person
            )

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`.

* I add a :ref:`call to the sort method<test_sort_a_list>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 167
    :emphasize-lines: 8

            dir_person.extend((
                '__dict__', '__firstlineno__',
                '__module__', '__static_attributes__',
                '__weakref__',
                'can_get_license', 'can_vote',
                'check_age', 'say_hello',
            ))
            dir_person.sort()
            self.assertEqual(
                dir(src.person.Person),
                dir_person
            )

            self.assertEqual(
                dir(src.person.Person),
                [
                    '__class__', '__delattr__', '__dict__',
                    '__dir__', '__doc__', '__eq__',

  the test passes because :ref:`all objects inherit from 'object'<test_making_an_object_w_object>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertion<what is an assertion?>` from :ref:`test_dir_person_object`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 174

            dir_person.sort()
            self.assertEqual(
                dir(src.person.Person),
                dir_person
            )

        def test_dir_person_instance(self):

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_dir_person_object with extend and sort'

:ref:`All objects inherit attributes and methods from 'object'<test_making_an_object_w_object>`.

----

*********************************************************************************
test_dir_person_instance with extend and sort
*********************************************************************************

The :ref:`attributes and methods of an instance of the Person object<test_dir_person_instance>` are the :ref:`attributes and methods of the Person object<test_dir_person_object>` with extra. Since they are both :ref:`lists<what is a list?>` I can make the :ref:`attributes and methods of an instance of the Person object<test_dir_person_instance>` by adding the "extra" to the :ref:`attributes and methods of the Person object<test_dir_person_object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`variable<what is a variable?>` for the :ref:`attributes and methods of an instance of the Person object<test_dir_person_instance>`, then add an :ref:`assertion<what is an assertion?>` for it

.. code-block:: python
  :caption: person/tests/test_person.py
  :lineno-start: 180
  :emphasize-lines: 2-13

      def test_dir_person_instance(self):
          dir_person_instance = dir(src.person.Person)
          self.assertEqual(
              dir(
                  src.person.Person(
                      first_name='first_name',
                      last_name='last_name',
                      sex='M',
                      year_of_birth=2026,
                  )
              ),
              dir_person_instance
          )

          self.assertEqual(
              dir(
                  src.person.Person(
                      first_name='first_name',

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: Lists differ: [
      '__c[396 chars]_', 'age', 'can_get_license',
      'can_vote', 'che[96 chars]rth'
  ] != [
      '__c[396 chars]_', 'can_get_license', 'can_vote',
      'check_age', 'say_hello'
  ]

with a note about the difference

.. code-block:: python
  :caption: terminal

  Diff is 718 characters long. Set self.maxDiff to None to see it.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``self.maxDiff = None``

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 180
    :emphasize-lines: 2

        def test_dir_person_instance(self):
            self.maxDiff = None
            dir_person_instance = dir(src.person.Person)

  the terminal_ is my friend, and shows the difference.

* I use :ref:`extend<test_extend_adds_items_from_an_iterable_to_end_of_a_list>` to :ref:`append<test_append_adds_item_to_end_of_a_list>` the seven additional elements

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 180
    :emphasize-lines: 4-8

        def test_dir_person_instance(self):
            self.maxDiff = None
            dir_person_instance = dir(src.person.Person)
            dir_person_instance.extend((
                'age', 'first_name', 'is_citizen',
                'last_name', 'passed_test',
                'sex', 'year_of_birth',
            ))
            self.assertEqual(
                dir(
                    src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=2026,
                    )
                ),
                dir_person_instance
            )

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`.

* I add a :ref:`call to the sort method<test_sort_a_list>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 183
    :emphasize-lines: 6

            dir_person_instance.extend((
                'age', 'first_name', 'is_citizen',
                'last_name', 'passed_test',
                'sex', 'year_of_birth',
            ))
            dir_person_instance.sort()
            self.assertEqual(
                dir(
                    src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=2026,
                    )
                ),
                dir_person_instance
            )

            self.assertEqual(
                dir(
                    src.person.Person(
                        first_name='first_name',

  the test passes because :ref:`all objects inherit from 'object'<test_making_an_object_w_object>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertion<what is an assertion?>` from :ref:`test_dir_person_instance`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 189

            self.assertEqual(
                dir(
                    src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=2026,
                    )
                ),
                dir_person_instance
            )


    # Exceptions seen

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_dir_person_instance with extend and sort'

:ref:`All objects inherit attributes and methods from 'object'<test_making_an_object_w_object>`.



----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_person.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of ``person``

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

----

*************************************************************************************
review
*************************************************************************************

:ref:`All objects inherit attributes and methods from 'object'<test_making_an_object_w_object>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test person with lists: tests>`

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
* :ref:`I know that everything in Python is an object<what is an object?>`.
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
* :ref:`I know how to use lists<what is a list?>`.

:ref:`Would you like to test list comprehensions?<what is a list comprehension?>`

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