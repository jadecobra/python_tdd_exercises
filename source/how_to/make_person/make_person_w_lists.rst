.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): test person with lists — simplify test_dir_person_object and test_dir_person_instance with list extend and sort, and refactor test_person_object with lists and loops. Open person project; run tests with uv run pytest-watcher . --now". RED: in test_dir_person_object, dir_person = dir(object) extended with ('can_get_license', 'can_vote', 'check_age', 'say_hello') -> AssertionError: Lists differ, 'First list contains 5 additional elements'. GREEN: extend with ('__dict__', '__firstlineno__', '__module__', '__static_attributes__', '__weakref__') and call dir_person.sort(). RED: in test_dir_person_instance, dir_person_instance = dir(src.person.Person) -> AssertionError: Lists differ, 'Diff is 718 characters long. Set self.maxDiff to None to see it.'. GREEN: set self.maxDiff = None, extend with the 7 instance attributes, and call sort(). Refactor TestPerson: build people with nested for loops over years_of_birth and booleans plus an if statement for not_younger_than_18; move booleans and people into test_person_object (fixing NameError: name 'years_of_birth' is not defined and NameError: name 'not_younger_than_18' is not defined with self.), unpack tuple fields in the for loop, and remove unused class attributes. All objects inherit attributes and methods from 'object'. Next: list comprehensions.
  :keywords: Jacob Itegboje, Pumping Python, test person with lists, python list extend sort, dir(object), dir(src.person.Person), dir instance, test_dir_person_object, test_dir_person_instance, test_person_object, years_of_birth, AssertionError Lists differ, self.maxDiff = None, First list contains 5 additional elements, NameError name years_of_birth is not defined, NameError name not_younger_than_18 is not defined, all objects inherit from object, red green refactor, uv run pytest-watcher, git commit, list comprehensions
.. include:: ../../links.rst

.. _test person with lists:

#################################################################################
test person with lists
#################################################################################

----

I want to use a :ref:`list<what is a list?>` like I did in :ref:`test_dir_list with extend and sort` to make :ref:`test_dir_person_object` and :ref:`test_dir_person_instance` simpler.

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

    uv run pytest-watcher . --now"

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
refactor test_person with lists and loops
*********************************************************************************

The ``people`` :ref:`object attribute<what is an object attribute?>` is a tuple_ with some repetition and :ref:`conditions<if statements?>`.

.. code-block:: python

  year_of_birth (not_younger_than_18 | younger_than_18),
  is_citizen, passed_test,
  result of can_vote(),
  result of can_get_license(),

the last items in the tuple_ do not bother with the results because they trigger an :ref:`Exception<how to raise an Exception>` since the values for ``year_of_birth`` are not integers_

.. code-block:: python

  (None, False, False,),
  (2026.0, False, False,),
  ('2026', False, False,),
  ((2026,), False, False,),

I can use a :ref:`list<what is a list?>` with :ref:`for loops<what is a for loop?>` and :ref:`if statements` to make the ``people`` :ref:`object attribute<what is an object attribute?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add values for the result of the :ref:`calls<how to call a function with input>` to the :ref:`can_vote<add can_vote method>` and :ref:`can_get_license methods<add can_get_license method>` to make the ``people`` tuple_ more balanced

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 52
    :emphasize-lines: 7-10

            (
                # underage, not is_citizen, not passed_test
                younger_than_18, False, False,
                False, False,
            ),
            # year_of_birth is not an integer
            (None, False, False, False, False),
            (2026.0, False, False, False, False),
            ('2026', False, False, False, False),
            ((2026,), False, False, False, False),
        )

      def calculate_age(self, year_of_birth):

  the test is still green.

* I use :ref:`for loops<what is a for loop?>` to make a :ref:`list<what is a list?>` for the ``people`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 57
    :emphasize-lines: 8-19

            # year_of_birth is not an integer
            (None, False, False, False, False),
            (2026.0, False, False, False, False),
            ('2026', False, False, False, False),
            ((2026,), False, False, False, False),
        )

        booleans = (True, False)
        people = []
        for year_of_birth in (
            not_younger_than_18, younger_than_18,
            None, 2026.0, '2026', (2026,),
        ):
            for is_citizen in booleans:
                for passed_test in booleans:
                    people.append((
                        year_of_birth, is_citizen, passed_test,
                        is_citizen, passed_test,
                    ))

        def calculate_age(self, year_of_birth):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    SUBFAILED[(2009, True, True, True, True)] ...test_person_object -
        AssertionError: False != True
    SUBFAILED[(2009, True, True, True, True)] ...test_person_object -
        AssertionError: False != True
    SUBFAILED[(2009, True, True, True, True)] ...test_person_object -
        AssertionError: False != True
    SUBFAILED[(2009, True, True, True, True)] ...test_person_object -
        AssertionError: False != True

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for the year of birth

.. code-block:: python
  :caption: person/tests/test_person.py
  :lineno-start: 64
  :emphasize-lines: 9-18

      booleans = (True, False)
      people = []
      for year_of_birth in (
          not_younger_than_18, younger_than_18,
          None, 2026.0, '2026', (2026,),
      ):
          for is_citizen in booleans:
              for passed_test in booleans:
                  if year_of_birth == not_younger_than_18:
                      people.append((
                          year_of_birth, is_citizen, passed_test,
                          is_citizen, passed_test,
                      ))
                  else:
                      people.append((
                          year_of_birth, is_citizen, passed_test,
                          False, False
                      ))

      def calculate_age(self, year_of_birth):

the test is green again and is slower than when I used a tuple_ for the ``people`` :ref:`object attribute<what is an object attribute?>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the ``people`` tuple_

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 6

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year
        younger_than_18 = this_year - 17
        not_younger_than_18 = this_year - 18

        first_name = 'first_name'
        last_name = 'last_name'
        sex = 'M'

        booleans = (True, False)
        people = []

* I make an :ref:`object attribute<what is an object attribute?>` for the different values for ``year_of_birth``

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 12
    :emphasize-lines: 5-8

        first_name = 'first_name'
        last_name = 'last_name'
        sex = 'M'

        years_of_birth = (
            not_younger_than_18, younger_than_18,
            None, 2026.0, '2026', (2026,),
        )

        booleans = (True, False)

* I use the new :ref:`object attribute<what is an object attribute>` in the ``people`` :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 21
    :emphasize-lines: 3

        booleans = (True, False)
        people = []
        for year_of_birth in years_of_birth:
            for is_citizen in booleans:
                for passed_test in booleans:
                    if year_of_birth == not_younger_than_18:

  the tests are still green.

* I use the new :ref:`object attribute<what is an object attribute>` in :ref:`test_say_hello_function<extract test_say_hello_function>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 73
    :emphasize-lines: 2-3, 5-7

        def test_say_hello_function(self):
            # for a_person in self.people:
            #     year_of_birth = a_person[0]

            #     with self.subTest(a_person):
            for year_of_birth in self.years_of_birth:
                with self.subTest(year_of_birth):
                    try:
                        reality = src.person.say_hello(
                            first_name=self.first_name,
                            last_name=self.last_name,
                            year_of_birth=year_of_birth,
                        )
                    except TypeError as error:

  the test is still green.

* I remove the commented lines from :ref:`test_say_hello_function<extract test_say_hello_function>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 73

        def test_say_hello_function(self):
            for year_of_birth in self.years_of_birth:
                with self.subTest(year_of_birth):
                    try:

* I use the new :ref:`object attribute<what is an object attribute>` in :ref:`test_person_factory<extract test_person_factory>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 97
    :emphasize-lines: 2-3, 5-7

        def test_person_factory(self):
            # for a_person in self.people:
            #     year_of_birth = a_person[0]

            #     with self.subTest(a_person):
            for year_of_birth in self.years_of_birth:
                with self.subTest(year_of_birth):
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

        def test_if_person_is_not_alive(self):

  still green.

* I remove the commented lines from :ref:`test_person_factory<extract test_person_factory>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 97

        def test_person_factory(self):
            for year_of_birth in self.years_of_birth:
                with self.subTest(year_of_birth):

* I copy the ``people`` and ``booleans`` :ref:`object attributes<what is an object attribute?>` into :ref:`test_person_object<extract test_person_object>` because that is the only place where they are used

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 40
    :emphasize-lines: 2-16

        def test_person_object(self):
            booleans = (True, False)
            people = []
            for year_of_birth in years_of_birth:
                for is_citizen in booleans:
                    for passed_test in booleans:
                        if year_of_birth == not_younger_than_18:
                            people.append((
                                year_of_birth, is_citizen, passed_test,
                                is_citizen, passed_test,
                            ))
                        else:
                            people.append((
                                year_of_birth, is_citizen, passed_test,
                                False, False
                            ))

            for a_person in self.people:
                year_of_birth = a_person[0]

                with self.subTest(a_person):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python
    :caption: terminal

    NameError: name 'years_of_birth' is not defined

* I add ``self.`` to ``years_of_birth``

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 40
    :emphasize-lines: 4

        def test_person_object(self):
            booleans = (True, False)
            people = []
            for year_of_birth in self.years_of_birth:
                for is_citizen in booleans:

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python
    :caption: terminal

    NameError: name 'not_younger_than_18' is not defined

* I add ``self.`` to ``not_younger_than_18``

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 44
    :emphasize-lines: 3

                for is_citizen in booleans:
                    for passed_test in booleans:
                        if year_of_birth == self.not_younger_than_18:
                            people.append((
                                year_of_birth, is_citizen, passed_test,
                                is_citizen, passed_test,
                            ))
                        else:

  the test passes.

* I change ``self.people`` to ``people`` to use the new :ref:`variable<what is a variable?>` instead of the :ref:`object attribute<what is an object attribute?>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 51
    :emphasize-lines: 7

                        else:
                            people.append((
                                year_of_birth, is_citizen, passed_test,
                                False, False
                            ))

            for a_person in people:
                year_of_birth = a_person[0]

                with self.subTest(a_person):
                    try:

  the test is still green.

* I change the :ref:`for loop<what is a for loop?>` for the test to use names instead of :ref:`indexes<test_index_returns_the_first_position_of_a_given_item>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 51
    :emphasize-lines: 7-10, 12-15

                        else:
                            people.append((
                                year_of_birth, is_citizen, passed_test,
                                False, False
                            ))

            for (
                year_of_birth, is_citizen, passed_test,
                can_vote_result, can_get_license_result,
            ) in people:

                with self.subTest((
                    year_of_birth, is_citizen, passed_test,
                    can_vote_result, can_get_license_result,
                )):

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 66
    :emphasize-lines: 7-8

                    try:
                        an_instance = src.person.Person(
                            first_name=self.first_name,
                            last_name=self.last_name,
                            sex=self.sex,
                            year_of_birth=year_of_birth,
                            is_citizen=is_citizen,
                            passed_test=passed_test,
                        )
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

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 89
    :emphasize-lines: 1-4, 7-8

                        self.assertEqual(
                            an_instance.can_vote(),
                            can_vote_result
                        )
                        self.assertEqual(
                            an_instance.can_get_license(),
                            can_get_license_result
                        )

        def test_say_hello_function(self):

  still green.

* I remove the ``booleans`` and ``people`` :ref:`object attributes<what is an object attribute?>` because they are no longer used

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 6

    class TestPerson(unittest.TestCase):

        this_year = datetime.date.today().year
        younger_than_18 = this_year - 17
        not_younger_than_18 = this_year - 18

        first_name = 'first_name'
        last_name = 'last_name'
        sex = 'M'

        years_of_birth = (
            not_younger_than_18, younger_than_18,
            None, 2026.0, '2026', (2026,),
        )

        def calculate_age(self, year_of_birth):

  still green.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'refactor test_person with lists and loops'

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