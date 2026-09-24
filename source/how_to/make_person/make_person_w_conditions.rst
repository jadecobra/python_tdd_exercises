.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): how to make a person with conditions — add can_vote and can_get_license so the person project decides with if statements. Open person; uv run pytest-watcher . --now (7 passed from datetime chapter). RED: joe.can_vote() → AttributeError: 'Person' object has no attribute 'can_vote'. GREEN: add can_vote; TypeError takes 0 positional arguments but 1 was given → @staticmethod then self; update test_dir_person_class / test_dir_person_instance (dir lists are version-fragile). Add is_citizen (default True): unexpected keyword argument, then SyntaxError parameter without a default follows parameter with a default; optional is_citizen=True; return self.is_citizen. john/mary is_citizen=False. Age gate: test_underage_citizen with year_of_birth=datetime.date.today().year-17 → AssertionError: True != False until if age < 18: return False (under 18 blocked; 18+ uses is_citizen). Mirror for can_get_license + passed_test (default False); jane/mary pass the test. Extract self.age in __init__ (calculate_age once); unittest.skip on test_when_year_of_birth_is_not_an_integer ('will always fail'). Extract check_age(age, response) as @staticmethod; can_vote/can_get_license call check_age. Review: if for decisions; dir tests hard to maintain; skip hides exceptions; four person tests still repetitive. Leads to booleans and better exception testing. Catalog: test_person_w_conditions.py + person_w_conditions.py.
  :keywords: Jacob Itegboje, Pumping Python, how to make a person with conditions, if statements, can_vote, can_get_license, is_citizen, passed_test, age < 18, 18 or older, check_age, @staticmethod, self.age, calculate_age, AttributeError can_vote, TypeError positional arguments, SyntaxError parameter without a default, AssertionError True != False, unittest.skip will always fail, test_underage_citizen, test_dir_person_class, test_dir_person_instance, year_of_birth today year-17, red green refactor, remove the commented lines, git commit -am, uv run pytest-watcher . --now, person project voting license, test_person_w_conditions, person_w_conditions

.. include:: ../../links.rst

.. _if statement: https://docs.python.org/3/tutorial/controlflow.html#if-statements
.. _if statements: :ref:`if statement<if statements>`
.. _unittest.skip decorator: https://docs.python.org/3/library/unittest.html#unittest.skip

#################################################################################
how to make a person with conditions
#################################################################################

----

I want to be able to check if a person can vote, and if they can get a license. Which means I want something in the :ref:`person project<test person with datetime>` to make decisions based on :ref:`conditions<if statements>`

* If a person is younger than ``18``, the person cannot get a license.
* If a person is younger than ``18``, the person cannot vote.
* If a person is ``18`` or older and passes a test, the person can get a license.
* If a person is ``18`` or older and the person is a citizen, the person can vote.


----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_conditions.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 65
  :lines: 65-98

.. literalinclude:: ../../code/person/tests/test_person_w_conditions.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 100
  :lines: 100-134

.. literalinclude:: ../../code/person/tests/test_person_w_conditions.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 136
  :lines: 136-171

.. literalinclude:: ../../code/person/tests/test_person_w_conditions.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 173
  :lines: 173-208

.. literalinclude:: ../../code/person/tests/test_person_w_conditions.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 210
  :lines: 210-220

.. literalinclude:: ../../code/person/tests/test_person_w_conditions.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 222
  :lines: 222-229

.. literalinclude:: ../../code/person/tests/test_person_w_conditions.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 231
  :lines: 231-238

.. literalinclude:: ../../code/person/tests/test_person_w_conditions.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 240
  :lines: 240-252

.. literalinclude:: ../../code/person/tests/test_person_w_conditions.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 254
  :lines: 254-271

.. literalinclude:: ../../code/person/tests/test_person_w_conditions.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 273
  :lines: 273-

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

    tests/test_person.py .........                      [100%]

    =================== 9 passed in P.QRs ====================

----

*********************************************************************************
add can_vote method
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`call<how to call a function with input>` to :ref:`can_vote<add can_vote method>` from :ref:`test_joe`

.. code-block:: python
  :lineno-start: 65

    def test_joe(self):
        first_name = 'joe'
        last_name = 'blow'
        ...

.. code-block:: python
  :lineno-start: 84
  :emphasize-lines: 8-14

        self.assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth
        )

        joe = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )
        self.assertEqual(joe.can_vote(), True)

    def test_jane(self):

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: 'Person' object
                  has no attribute 'can_vote'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``__init__.py`` from the ``person`` folder_ in the ``src`` folder_
* I add a :ref:`method definition<how to make a function>` to the :ref:`Person class<add Person class>` in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 12-13

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth=None,
            ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            self.sex = sex

        def can_vote():
            return True

        def say_hello(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.can_vote() takes
               0 positional arguments but 1 was given

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 10

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth=None,
            ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            self.sex = sex

        @staticmethod
        def can_vote():
            return True

        def say_hello(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    FAILED ...::TestPerson::test_dir_person_class -
        AssertionError: assert
            ['__class__',...'__eq__', ...] ==...
    FAILED ...::TestPerson::test_dir_person_instance -
        AssertionError: assert
            ['__class__',...'__eq__', ...] ==...

  the tests for the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the :ref:`Person class and an instance of it<add Person class>` are failing because I added a :ref:`method<what is a method?>` to it.

* I add ``can_vote`` to :ref:`test_dir_person_class` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 210

        def test_dir_person_class(self):
            self.assertEqual(
                dir(src.person.Person),
                [
                    '__class__', '__delattr__', '__dict__',
                    ...

  .. code-block:: python
    :lineno-start: 222
    :emphasize-lines: 2-3
    :emphasize-text: can_vote

                    '__static_attributes__', '__str__',
                    '__subclasshook__', '__weakref__',
                    'can_vote', 'say_hello',
                ]
            )

        def test_dir_person_instance(self):

* I add ``can_vote`` to :ref:`test_dir_person_instance`

  .. code-block:: python
    :lineno-start: 228

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
                    ...

  .. code-block:: python
    :lineno-start: 248
    :emphasize-text: can_vote
    :emphasize-lines: 2-3

                    '__subclasshook__', '__weakref__',
                    'can_vote', 'first_name', 'last_name',
                    'say_hello', 'sex', 'year_of_birth',
                ]
            )


    # Exceptions seen

  the test passes.

  :ref:`test_dir_person_class` and :ref:`test_dir_person_instance` are good because they help document what is in the :ref:`class<everything is an object>` and catch its changes immediately.

  :ref:`test_dir_person_class` and :ref:`test_dir_person_instance` are a problem because :ref:`class attributes<what is a class attribute?>` can change from one Python_ version to another, I have to remember the correct order of names and I am keeping two :ref:`lists<what is a list?>`. :ref:`There has to be a better way<how to make a person with a list>`.

* I open a new terminal_ then make sure I am in the ``person`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd person

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add can_vote method'

----

*********************************************************************************
add is_citizen attribute
*********************************************************************************

I want :ref:`can_vote<add can_vote method>` to return

* :red:`False` for ``no`` the person cannot vote if the person is not a citizen.
* :green:`True` for ``yes`` the person can vote if the person is a citizen.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a :ref:`call<how to call a function with input>` to :ref:`can_vote<add can_vote method>` from :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 151

        def test_mary(self):
            first_name = 'mary'
            last_name = 'public'
            ...

  .. code-block:: python
    :lineno-start: 170
    :emphasize-lines: 8-14

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            mary = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth
            )
            self.assertEqual(mary.can_vote(), False)

        def test_when_person_is_older_than_120(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

  The :ref:`can_vote method<add can_vote method>` has to make a decision based on something.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``is_citizen`` to the :ref:`instance of the Person class<add Person class>` for ``mary``

  .. code-block:: python
    :lineno-start: 177
    :emphasize-lines: 6

            mary = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                is_citizen=False,
            )
            self.assertEqual(mary.can_vote(), False)

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() got
               an unexpected keyword argument
               'is_citizen'

  because the :ref:`definition<how to make a function that takes input>` for the :ref:`__init__ method<the constructor method>` of the :ref:`Person class<add Person class>` only takes five inputs (``self``, ``first_name``, ``last_name``, ``sex`` and ``year_of_birth``) and it got :ref:`called<how to call a function with input>` it with ``is_citizen`` which is not one of those names.

* I add ``is_citizen`` to the parentheses of the :ref:`__init__ method<the constructor method>`, in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 6

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth=None,
                is_citizen,
            ):

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default
         follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I give ``is_citizen`` a value to make it :ref:`optional<test_optional_arguments>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 6

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth=None,
                is_citizen=True,
            ):

  the terminal_ goes back to the :ref:`AssertionError<what causes AssertionError?>`.

* I add an :ref:`instance attribute<what is a class attribute?>` for ``is_citizen`` so I can use it in the :ref:`can_vote method<add can_vote method>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 12

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth=None,
                is_citizen=True,
            ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            self.sex = sex
            self.is_citizen = is_citizen

        @staticmethod
        def can_vote():

  still :ref:`AssertionError<what causes AssertionError?>`.

* I use the :ref:`class attribute<what is a class attribute?>` in the :ref:`can_vote method<add can_vote method>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3

        @staticmethod
        def can_vote():
            return self.is_citizen
            return True

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I remove the :ref:`staticmethod decorator<what is the staticmethod decorator?>` from the :ref:`can_vote method<add can_vote method>` then add ``self`` to the parentheses

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1-3

        # @staticmethod
        # def can_vote():
        def can_vote(self):
            return self.is_citizen
            return True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for :ref:`test_dir_person_instance` because I added a new :ref:`attribute<what is a class attribute?>` (``is_citizen``).

* I add ``is_citizen`` to the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_dir_person_instance` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 237

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
                    ...

  .. code-block:: python
    :lineno-start: 257
    :emphasize-lines: 2-4
    :emphasize-text: is_citizen

                    '__subclasshook__', '__weakref__',
                    'can_vote', 'first_name', 'is_citizen',
                    'last_name', 'say_hello', 'sex',
                    'year_of_birth',
                ]
            )


    # Exceptions seen

  the test passes.

* I remove the commented lines and the second :ref:`return statement<the return statement>` from the :ref:`can_vote method<add can_vote method>` in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 6

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth=None,
                is_citizen=True,
            ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            self.sex = sex
            self.is_citizen = is_citizen

        def can_vote(self):
            return self.is_citizen

        def say_hello(self):

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to :ref:`can_vote<add can_vote method>` from :ref:`test_john`, in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 125

        def test_john(self):
            first_name = 'john'
            last_name = 'smith'
            ...

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 8-14

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            john = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            self.assertEqual(john.can_vote(), False)

        def test_mary(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True != False

* I add ``is_citizen`` to the :ref:`instance of the Person class<add Person class>` for ``john``

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 6

            john = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                is_citizen=False,
            )
            self.assertEqual(john.can_vote(), False)

  the test passes.

* I add a :ref:`call<how to call a function with input>` to :ref:`can_vote<add can_vote method>` from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 99

        def test_jane(self):
            first_name = 'jane'
            last_name = 'doe'
            ...

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 8-14

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            jane = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            self.assertEqual(jane.can_vote(), False)

        def test_john(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True != False

  because :ref:`a method uses the default value for a parameter when it is called without the parameter<test_optional_arguments>` and the default value for ``is_citizen`` is :ref:`True<test_what_is_true>`.

* I change the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 125
    :emphasize-lines: 7-8

            jane = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            # self.assertEqual(jane.can_vote(), False)
            self.assertEqual(jane.can_vote(), True)

        def test_john(self):

  the test passes.

* I remove the commented line from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 125

            jane = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            self.assertEqual(jane.can_vote(), True)

  ``joe`` and ``jane`` do not need to pass a value for the ``is_citizen`` parameter because :ref:`a method uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add is_citizen attribute'

----

*********************************************************************************
add condition to can_vote
*********************************************************************************

I want the :ref:`can_vote method<add can_vote method>` to use two :ref:`conditions<if statements>` to make a decision

* is the person a citizen?
* is the person younger than ``18``?

I can do that with an :ref:`if statement<if statements>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for a person who is a citizen and younger than ``18``

  .. code-block:: python
    :lineno-start: 201
    :emphasize-lines: 3-11

            self.assertEqual(mary.can_vote(), False)

        def test_underage_citizen(self):
            underage = src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=self.this_year-17,
                is_citizen=True,
            )
            self.assertEqual(underage.can_vote(), False)

        def test_when_person_is_older_than_120(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

  - because :ref:`can_vote<add can_vote method>` returns the value of ``is_citizen``, it does not care about the age of the person.
  - I use a calculation (``datetime.date.today().year-17``) as the year of birth so that the person will always be younger than ``18`` in any year the test is run.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` with a :ref:`call<how to call a function with input>` to the :ref:`calculate_age function<add calculate_age function>` from the :ref:`can_vote method<add can_vote method>` in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3-4

        def can_vote(self):
            age = calculate_age(self.year_of_birth)
            if age < 18:
                return False
            return self.is_citizen

        def say_hello(self):

  the test passes because Python_ checks if ``age`` (which is the result of ``calculate_age(self.year_of_birth)``) is less than ``18``, when ``if age < 18:`` runs

  * If ``age`` is less than ``18``, it goes to the next line - ``return False``, which returns :red:`False` as the output, then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

    .. code-block:: shell

      self.is_citizen = False
      age < 18

      person.can_vote() -> False
        └── class Person:
            └── def can_vote(self):
                └── if age < 18:
                    └── return False
                    return self.is_citizen

    .. code-block:: shell

      self.is_citizen = True
      age < 18

      person.can_vote() -> False
        └── class Person:
            └── def can_vote(self):
                └── if age < 18:
                    └── return False
                    return self.is_citizen

  * If ``age`` is greater than or equal to ``18``, it leaves the :ref:`if statement<if statements>` and continues to run the rest of the :ref:`method<what is a method?>` - ``return self.is_citizen``, which returns

    - :red:`False` as the output if the person is not a citizen

      .. code-block:: shell

        self.is_citizen = False
        age >= 18

        person.can_vote() -> False
        └── class Person:
            └── def can_vote(self):
                ├── if age < 18:
                │      return False
                └── return self.is_citizen

    - :green:`True` as the output, if the person is a citizen

      .. code-block:: shell

        self.is_citizen = True
        age >= 18

        person.can_vote() -> True
        └── class Person:
            └── def can_vote(self):
                ├── if age < 18:
                │      return False
                └── return self.is_citizen

    then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add condition to can_vote'

----

*********************************************************************************
add can_get_license method
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a :ref:`call<how to call a function with input>` to :ref:`can_get_license<add can_get_license method>` from :ref:`test_mary` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 194
    :emphasize-lines: 9

            mary = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                is_citizen=False,
            )
            self.assertEqual(mary.can_vote(), False)
            self.assertEqual(mary.can_get_license(), True)

        def test_underage_citizen(self):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: 'Person' object
                    has no attribute 'can_get_license'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`method definition<how to make a function that takes input>` for :ref:`can_get_license<add can_get_license method>` to the :ref:`Person class<add Person class>` in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 12-13

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth=None,
                is_citizen=True,
            ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            self.sex = sex
            self.is_citizen = is_citizen

        def can_get_license():
            return False

        def can_vote(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.can_get_license()
               takes 0 positional arguments but 1 was given

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3

            self.is_citizen = is_citizen

        @staticmethod
        def can_get_license():
            return True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for :ref:`test_dir_person_class` and :ref:`test_dir_person_instance`.

* I add ``can_get_license`` to :ref:`test_dir_person_class` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 247

        def test_dir_person_class(self):
            self.assertEqual(
                dir(src.person.Person),
                [
                    '__class__', '__delattr__', '__dict__',
                    ...

  .. code-block:: python
    :lineno-start: 260
    :emphasize-lines: 2
    :emphasize-text: can_get_license

                    '__subclasshook__', '__weakref__',
                    'can_get_license', 'can_vote', 'say_hello'
                ]
            )

        def test_dir_person_instance(self):

* I add ``can_get_license`` to :ref:`test_dir_person_instance`

  .. code-block:: python
    :lineno-start: 265

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
                    ...

  .. code-block:: python
    :lineno-start: 285
    :emphasize-lines: 2-4

                    '__subclasshook__', '__weakref__',
                    'can_get_license', 'can_vote', 'first_name',
                    'is_citizen', 'last_name', 'say_hello',
                    'sex', 'year_of_birth',
                ]
            )


    # Exceptions seen

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add can_get_license method'


----

*********************************************************************************
add passed_test attribute
*********************************************************************************

I want :ref:`can_get_license<add can_get_license method>` to return

* :red:`False` for ``no`` the person cannot get a license if the person did not pass the test.
* :green:`True` for ``yes`` the person can get a license if the person passed the test.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a :ref:`call<how to call a function with input>` to :ref:`can_get_license<add can_get_license method>` from :ref:`test_john`

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 9

            john = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                is_citizen=False,
            )
            self.assertEqual(john.can_vote(), False)
            self.assertEqual(john.can_get_license(), False)

        def test_mary(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True != False

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``passed_test`` to the :ref:`instance of the Person class<add Person class>` for ``john``

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 7

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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() got
               an unexpected keyword argument
               'passed_test'

  because the :ref:`definition<how to make a function that takes input>` for the :ref:`__init__ method<the constructor method>` only allows six inputs (``self``, ``first_name``, ``last_name``, ``sex``, ``year_of_birth`` and ``is_citizen``) and it got :ref:`called<how to call a function with input>` it with ``passed_test`` which is not one of those names.

* I add ``passed_test`` to the parentheses of the :ref:`__init__ method<the constructor method>`, in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 6

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth=None,
                is_citizen=True, passed_test,
            ):

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default
         follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I give ``passed_test`` a value to make it :ref:`optional<test_optional_arguments>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 6

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth=None,
                is_citizen=True, passed_test=False,
            ):

  the terminal_ goes back to the :ref:`AssertionError<what causes AssertionError?>`.

* I use ``self.passed_test`` in the :ref:`can_get_license method<add can_get_license method>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3

        @staticmethod
        def can_get_license():
            return self.passed_test
            return True

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I remove the :ref:`staticmethod decorator<what is the staticmethod decorator?>` from the :ref:`can_get_license method<add can_get_license method>` then add ``self`` to the parentheses

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1-3

        # @staticmethod
        # def can_get_license():
        def can_get_license(self):
            return self.passed_test
            return True

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'passed_test'

* I add an :ref:`instance attribute<what is a class attribute?>` for ``passed_test`` so I can use it in the :ref:`can_get_license method<add can_get_license method>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 11

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth=None,
                is_citizen=True, passed_test=False,
            ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            self.sex = sex
            self.is_citizen = is_citizen
            self.passed_test = passed_test

        @staticmethod
        def can_get_license():

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for :ref:`test_mary`

  .. code-block:: python

    AssertionError: False != True

* I add ``passed_test`` to the :ref:`instance of the Person class<add Person class>` for ``mary``

  .. code-block:: python
    :lineno-start: 196
    :emphasize-lines: 7

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for :ref:`test_dir_person_instance` because I added a new :ref:`attribute<what is a class attribute?>` (``passed_test``).

* I add ``passed_test`` to the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_dir_person_instance` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 268

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
                    ...

  .. code-block:: python
    :lineno-start: 289
    :emphasize-lines: 2-3
    :emphasize-text: passed_test

                    'can_get_license', 'can_vote', 'first_name',
                    'is_citizen', 'last_name', 'passed_test',
                    'say_hello', 'sex', 'year_of_birth',
                ]
            )


    # Exceptions seen

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines and the second :ref:`return statement<the return statement>` from the :ref:`can_get_license method<add can_get_license method>` in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 15

            self.is_citizen = is_citizen
            self.passed_test = passed_test

        def can_get_license(self):
            return self.passed_test

        def can_vote(self):

* I add a :ref:`call<how to call a function with input>` to :ref:`can_get_license<add can_get_license method>` from :ref:`test_jane`, in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 125
    :emphasize-lines: 8

            jane = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            self.assertEqual(jane.can_vote(), True)
            self.assertEqual(jane.can_get_license(), True)

        def test_john(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False != True

  because :ref:`a method uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I add ``passed_test`` to the :ref:`instance of the Person class<add Person class>` for ``jane``

  .. code-block:: python
    :lineno-start: 125
    :emphasize-lines: 6

            jane = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
                passed_test=True,
            )
            self.assertEqual(jane.can_vote(), True)
            self.assertEqual(jane.can_get_license(), True)

  the test passes.

* I add a :ref:`call<how to call a function with input>` to :ref:`can_get_license<add can_get_license method>` from :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 8

            joe = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            self.assertEqual(joe.can_vote(), True)
            self.assertEqual(joe.can_get_license(), True)

        def test_jane(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False != True

  because :ref:`a method uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I change the expectation of the :ref:`assertion<what is an assertion?>` for the :ref:`can_get_license method<add can_get_license>` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 6

            self.assertEqual(joe.can_vote(), True)
            # self.assertEqual(joe.can_get_license(), True)
            self.assertEqual(joe.can_get_license(), False)

        def test_jane(self):

  the test passes.

* I remove the commented line from :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 91

            joe = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            self.assertEqual(joe.can_vote(), True)
            self.assertEqual(joe.can_get_license(), False)

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add passed_test attribute'

``john`` and ``joe`` do not need to pass a value for the ``passed_test`` parameter because :ref:`a method uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

----

*********************************************************************************
add condition to can_get_license
*********************************************************************************

I want the :ref:`can_get_license method<add can_get_license method>` to use two :ref:`conditions<if statements>` to make a decision

* did the person pass the test?
* is the person ``18`` or older?

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_underage_citizen<add condition to can_vote>` for a person who is younger than 18 and passed the test

  .. code-block:: python
    :lineno-start: 210
    :emphasize-lines: 8, 11

        def test_underage_citizen(self):
            underage = src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=self.this_year-17,
                is_citizen=True,
                passed_test=True,
            )
            self.assertEqual(underage.can_vote(), False)
            self.assertEqual(underage.can_get_license(), False)

        def test_when_person_is_older_than_120(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

  because :ref:`can_get_license<add can_get_license method>` currently returns the value of ``passed_test``. It does not care about the age of the person.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` with a :ref:`call<how to call a function with input>` to the :ref:`calculate_age function<add calculate_age function>` from the :ref:`can_get_license method<add can_get_license method>` in ``src/person/__init__.py``

.. code-block:: python
  :lineno-start: 18
  :emphasize-lines: 3-4

      def can_get_license(self):
          age = calculate_age(self.year_of_birth)
          if age < 18:
              return False
          return self.passed_test

      def can_vote(self):

the test passes because Python_ checks if ``age`` (the result of ``calculate_age(self.year_of_birth)``) is less than ``18``, when ``if age < 18:`` runs

* If ``age`` is less than ``18``, it goes to the next line - ``return False``, which returns :red:`False` as the output, then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

  .. code-block:: shell

    self.passed_test = False
    age < 18

    person.can_get_license() -> False
    └── class Person:
        └── def can_get_license(self):
            └── if age < 18:
                └── return False
                return self.passed_test

  .. code-block:: shell

    self.passed_test = True
    age < 18

    person.can_get_license() -> False
    └── class Person:
        └── def can_get_license(self):
            └── if age < 18:
                └── return False
                return self.passed_test

* If ``age`` is greater than or equal to ``18``, it leaves the :ref:`if statement<if statements>` and continues to run the rest of the :ref:`method<what is a method?>` - ``return self.passed_test``, which returns

  - :red:`False` as the output, if the person failed the test

    .. code-block:: shell

      self.passed_test = False
      age >= 18

      person.can_get_license() -> False
      └── class Person:
          └── def can_get_license(self):
              ├── if age < 18:
              │      return False
              └── return self.passed_test

  - :green:`True` as the output, if the person passed the test

    .. code-block:: shell

      self.passed_test = True
      age >= 18

      person.can_get_license() -> True
      └── class Person:
          └── def can_get_license(self):
              ├── if age < 18:
              │      return False
              └── return self.passed_test

  then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add condition to can_get_license'

----

*********************************************************************************
extract age instance attribute
*********************************************************************************

The :ref:`can_get_license<add can_get_license method>`, :ref:`can_vote<add can_vote method>` and :ref:`say_hello methods<test_classy_person_says_hello>` of the :ref:`Person class<add Person class>` all :ref:`call the calculate_age function<add calculate_age function>`.

I can make an :ref:`attribute<what is a class attribute?>` to remove the repetition of the :ref:`calls to the calculate_age function<add calculate_age function>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add an :ref:`instance attribute<what is a class attribute?>` to the :ref:`__init__ method<the constructor method>` so that the age is calculated once when an :ref:`instance<how to test if something is an instance>` is made, not every time one of the :ref:`methods is called<how to call a function with input>`.

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 14

      class Person:

          def __init__(
                  self, first_name, last_name,
                  sex, year_of_birth=None,
                  is_citizen=True, passed_test=False,
              ):
              self.first_name = first_name
              self.last_name = last_name
              self.year_of_birth = year_of_birth
              self.sex = sex
              self.is_citizen = is_citizen
              self.passed_test = passed_test
              self.age = calculate_age(year_of_birth)

          def can_get_license(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

      FAILED ...test_dir_person_instance - AssertionError:
          Lists differ: ['__c[396 chars]_', 'age', 'can_ge...
      FAILED ...test_when_person_is_older_than_120 - AssertionError
      FAILED ...test_when_year_of_birth_is_not_an_integer - AssertionError
      FAILED ...test_when_year_of_birth_is_the_future - AssertionError

  - :ref:`test_when_year_of_birth_is_the_future` fails because the age is smaller than ``0``.
  - :ref:`test_when_year_of_birth_is_not_an_integer` fails because an :ref:`instance of the Person class<add Person class>` is made with a ``year_of_birth`` (:ref:`None<what is None?>`) that is not an integer_.
  - :ref:`test_when_person_is_older_than_120` fails because the age is bigger than ``120``.
  - :ref:`test_dir_person_instance` fails because I just added a new :ref:`class attribute<what is a class attribute?>`.

----

*********************************************************************************
how to skip a test
*********************************************************************************

I can use `unittest.skip decorator`_ to skip a test. The problem with skipping tests is that I will no longer know if the program does the thing the skipped tests were written for.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the `unittest.skip decorator`_ to :ref:`test_when_person_is_older_than_120` with a note that it will always fail since it uses a year of birth that is not an integer_, in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 219
    :emphasize-lines: 4

            self.assertEqual(underage.can_vote(), False)
            self.assertEqual(underage.can_get_license(), False)

        @unittest.skip('fails because age > 120')
        def test_when_person_is_older_than_120(self):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=self.this_year-121
            )
            # ).say_hello() fails
            # because age > 120

        def test_when_year_of_birth_is_the_future(self):

* I remove the comments from :ref:`test_when_person_is_older_than_120` because they are a repetition of the message in the `unittest.skip decorator`_

  .. code-block:: python
    :lineno-start: 222

        @unittest.skip('fails because age > 120')
        def test_when_person_is_older_than_120(self):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=self.this_year-121
            )

        def test_when_year_of_birth_is_the_future(self):

* I add the `unittest.skip decorator`_ to :ref:`test_when_year_of_birth_is_the_future` with a message that it will always fail since it uses a year of birth that is in the future

  .. code-block:: python
    :lineno-start: 231
    :emphasize-lines: 1

        @unittest.skip('fails because age < 0')
        def test_when_year_of_birth_is_the_future(self):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='F',
                year_of_birth=self.this_year+1,
            )
            # ).say_hello() fails
            # because age < 0

* I remove the comments from :ref:`test_when_year_of_birth_is_the_future`

  .. code-block:: python
    :lineno-start: 231

        @unittest.skip('fails because age < 0')
        def test_when_year_of_birth_is_the_future(self):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='F',
                year_of_birth=self.this_year+1,
            )

        def test_when_year_of_birth_is_not_an_integer(self):

* I add the `unittest.skip decorator`_ to :ref:`test_when_year_of_birth_is_not_an_integer` with a message

  .. code-block:: python
    :lineno-start: 240
    :emphasize-lines: 1-3

        @unittest.skip(
            'fails because year_of_birth is not an integer'
        )
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

* I remove the repeated message from :ref:`test_when_year_of_birth_is_not_an_integer`

  .. code-block:: python
    :lineno-start: 240

        @unittest.skip(
            'fails because year_of_birth is not an integer'
        )
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

        def test_dir_person_class(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    ================ short test summary info =================
    FAILED ...::TestPerson::test_dir_person_instance -
        AssertionError: assert ['__class__',...'__eq__', ...]
                            == ['__class__',...'__eq__', ...]
    ======== 1 failed, 6 passed, 1 skipped in S.TUs ==========

* I add ``age`` to the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_dir_person_instance`

  .. code-block:: python
    :lineno-start: 272

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
                    ...

  .. code-block:: python
    :lineno-start: 292
    :emphasize-lines: 2-5
    :emphasize-text: age

                    '__subclasshook__', '__weakref__',
                    'age', 'can_get_license', 'can_vote',
                    'first_name', 'is_citizen', 'last_name',
                    'passed_test', 'say_hello', 'sex',
                    'year_of_birth',
                ]
            )


    # Exceptions seen

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use ``self.age`` in the :ref:`can_get_license method<add can_get_license method>` in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2-4

        def can_get_license(self):
            # age = calculate_age(self.year_of_birth)
            # if age < 18:
            if self.age < 18:
                return False
            return self.passed_test

        def can_vote(self):

  the tests are still green.

* I use ``self.age`` in the :ref:`can_vote method<add can_vote method>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2-4

        def can_vote(self):
            # age = calculate_age(self.year_of_birth)
            # if age < 18:
            if self.age < 18:
                return False
            return self.is_citizen

        def say_hello(self):

  still green.

* I use ``self.age`` in the :ref:`say_hello method<add say_hello method>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5-6

        def say_hello(self):
            return (
                f'Hello, my name is {self.first_name}'
                f' {self.last_name} and I am'
                # f' {calculate_age(self.year_of_birth)}.'
                f' {self.age}.'
            )


    def calculate_age(year_of_birth):

  green.

* I remove the commented line from the :ref:`say_hello method<add say_hello method>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 4

        def say_hello(self):
            return (
                f'Hello, my name is {self.first_name}'
                f' {self.last_name} and I am {self.age}.'
            )


    def calculate_age(year_of_birth):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract age instance attribute'

----

*********************************************************************************
extract check_age method
*********************************************************************************

:ref:`can_get_license<add can_get_license method>` and :ref:`can_vote<add can_vote method>` look the same, they both

- return :red:`False` if ``self.age`` is less than ``18``
- return something else if ``self.age`` is NOT less than ``18``

.. code-block:: python

  if self.age < 18:
      return False
  return something_else

I can make a :ref:`method<what is a method?>` that removes the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`method<what is a method?>` to the :ref:`Person class<add Person class>` that checks if the age is less than ``18`` and returns something else if it is not

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 4-7

            self.passed_test = passed_test
            self.age = calculate_age(year_of_birth)

        def check_age(status):
            if self.age < 18:
                return False
            return status

        def can_get_license(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  FAILED ...test_dir_person_class - AssertionError:
      Lists differ: ['__c[393 chars]ef__', 'can_get_li...
  FAILED ...test_dir_person_instance - AssertionError:
      Lists differ: ['__c[434 chars]e', 'check_age', '...

because I added a new :ref:`method<what is a method?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``check_age`` to the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_dir_person_instance`

  .. code-block:: python
    :lineno-start: 272

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
                    ...

  .. code-block:: python
    :lineno-start: 292
    :emphasize-lines: 3-5
    :emphasize-text: check_age

                    '__subclasshook__', '__weakref__',
                    'age', 'can_get_license', 'can_vote',
                    'check_age', 'first_name', 'is_citizen',
                    'last_name', 'passed_test', 'say_hello',
                    'sex', 'year_of_birth',
                ]
            )


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError
    # SyntaxError

* I add ``check_age`` to the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_dir_person_class` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 254

        def test_dir_person_class(self):
            self.assertEqual(
                dir(src.person.Person),
                [
                    '__class__', '__delattr__', '__dict__',
                    ...

  .. code-block:: python
    :lineno-start: 267
    :emphasize-lines: 2-3
    :emphasize-text: check_age

                    '__subclasshook__', '__weakref__',
                    'can_get_license', 'can_vote', 'check_age',
                    'say_hello'
                ]
            )

        def test_dir_person_instance(self):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I :ref:`call<how to call a function with input>` the :ref:`check_age method<extract check_age method>` from the :ref:`can_get_license method<add can_get_license method>` in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2

        def can_get_license(self):
            return self.check_age(self.passed_test)
            # age = calculate_age(self.year_of_birth)
            # if age < 18:
            if self.age < 18:
                return False
            return self.passed_test

        def can_vote(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.check_age() takes
               1 positional arguments but 2 were given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add ``self`` to the parentheses of the :ref:`check_age method<extract check_age method>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4

            self.passed_test = passed_test
            self.age = calculate_age(year_of_birth)

        def check_age(self, status):
            if self.age < 18:
                return False
            return status

        def can_get_license(self):

  the test passes.

* I remove the other statements from the :ref:`can_get_license method<add can_get_license method>`

  .. code-block:: python
    :lineno-start: 24

        def can_get_license(self):
            return self.check_age(self.passed_test)

        def can_vote(self):

* I :ref:`call<how to call a function with input>` the :ref:`check_age method<extract check_age method>` from the :ref:`can_vote method<add can_vote method>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 2

        def can_vote(self):
            return self.check_age(self.is_citizen)
            # age = calculate_age(self.year_of_birth)
            # if age < 18:
            if self.age < 18:
                return False
            return self.is_citizen

        def say_hello(self):

  the tests are still green.

* I remove the other statements from the :ref:`can_vote method<add can_vote method>`

  .. code-block:: python
    :lineno-start: 27

        def can_vote(self):
            return self.check_age(self.is_citizen)

        def say_hello(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract check_age method'

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

I can use :ref:`if statements<if statements>` to write a program_ that makes decisions based on :ref:`conditions<if statements>`.

My tests have problems:

* The attribute tests - :ref:`test_dir_person_class` and :ref:`test_dir_person_instance` catch changes to the :ref:`attributes and methods of the Person class<test_dir_person_instance>` and they are a problem to maintain. :ref:`There has to be a better way<how to make a person with lists>`.
* I skipped :ref:`test_when_year_of_birth_is_the_future` and :ref:`test_when_year_of_birth_is_not_an_integer` because they are always in a :red:`RED` state since they cause an :ref:`Exception<how to test that an Exception is raised>`. The only way to know that the code causes the :ref:`Exception<how to test that an Exception is raised>` is to remove the `unittest.skip decorator`_. :ref:`There has to be a better way<how to make a person with exceptions>`
* :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` also still have the problem where they are the same three tests. :ref:`There has to be a better way<how to make a person with loops>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a person with conditions: tests and solutions>`

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

.. toctree::
  :titlesonly:
  :maxdepth: 1

  ../../basic_objects/booleans/index
  ../../make_tdd/make_tdd_automatically
  ../../truth_table/index

:ref:`Would you like to test booleans (there are only two)?<what are booleans?>`

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