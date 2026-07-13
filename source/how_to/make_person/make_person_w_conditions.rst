.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): how to make a person with conditions — add can_vote and can_get_license so the person project decides with if statements. Open person; uv run pytest-watcher . --now (7 passed from datetime chapter). RED: joe.can_vote() → AttributeError: 'Person' object has no attribute 'can_vote'. GREEN: add can_vote; TypeError takes 0 positional arguments but 1 was given → @staticmethod then self; update test_dir_person_class / test_dir_person_instance (dir lists are version-fragile). Add is_citizen (default True): unexpected keyword argument, then SyntaxError parameter without a default follows parameter with a default; optional is_citizen=True; return self.is_citizen. john/mary is_citizen=False. Age gate: test_underage_citizen with year_of_birth=datetime.date.today().year-17 → AssertionError: True != False until if age < 18: return False (under 18 blocked; 18+ uses is_citizen). Mirror for can_get_license + passed_test (default False); jane/mary pass the test. Extract self.age in __init__ (calculate_age once); unittest.skip on test_when_year_of_birth_is_not_an_integer ('will always fail'). Extract check_age(age, response) as @staticmethod; can_vote/can_get_license call check_age. Review: if for decisions; dir tests hard to maintain; skip hides exceptions; four person tests still repetitive. Leads to booleans and better exception testing. Catalog: test_person_w_conditions.py + person_w_conditions.py.
  :keywords: Jacob Itegboje, Pumping Python, how to make a person with conditions, if statements, can_vote, can_get_license, is_citizen, passed_test, age < 18, 18 or older, check_age, @staticmethod, self.age, calculate_age, AttributeError can_vote, TypeError positional arguments, SyntaxError parameter without a default, AssertionError True != False, unittest.skip will always fail, test_underage_citizen, test_dir_person_class, test_dir_person_instance, year_of_birth today year-17, red green refactor, remove the commented lines, git commit -am, uv run pytest-watcher . --now, person project voting license, test_person_w_conditions, person_w_conditions

.. include:: ../../links.rst

.. _if statement: https://docs.python.org/3/tutorial/controlflow.html#if-statements
.. _if statements: `if statement`_
.. _unittest.skip decorator: https://docs.python.org/3/library/unittest.html#unittest.skip

#################################################################################
how to make a person with conditions
#################################################################################

----

I want to be able to check if a person can vote, and if they can get a license. In other words, I want something in the :ref:`person project<test person with datetime>` to make decisions based on :ref:`conditions<if statements>`, for example

* If a person is younger than ``18``

  - the person cannot get a license.
  - the person cannot vote.

* If a person is ``18`` or older

  - and passes a test, the person can get a license.
  - and is a citizen, the person can vote.


----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_conditions.py
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

    tests/test_person.py .......                        [100%]

    =================== 7 passed in P.QRs ====================

----

*********************************************************************************
add can_vote method
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`call<how to call a function with input>` to ``can_vote`` from :ref:`test_joe`

.. code-block:: python
  :lineno-start: 54
  :emphasize-lines: 4

          reality = joe.say_hello()
          assert reality == my_expectation
          self.assertEqual(reality, my_expectation)
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

* I open ``person.py`` from the ``src`` folder_
* I add a :ref:`function definition<how to make a function>` to the :ref:`Person class<test Person class>` in ``person.py``

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
              return (
                  f'Hello, my name is {self.first_name}'
                  f' {self.last_name} and I am'
                  f' {calculate_age(self.year_of_birth)}.'
              )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.can_vote() takes
               0 positional arguments but 1 was given

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

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

  the tests for the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the :ref:`Person class and an instance of it<test Person class>` are failing because I added a :ref:`method<what is a method?>` to it.

* I add ``can_vote`` to :ref:`test_dir_person_class`

  .. code-block:: python
    :lineno-start: 237
    :emphasize-lines: 1-2

                'can_vote',
                'say_hello',
            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

        def test_dir_person_instance(self):

* I add ``can_vote`` to :ref:`test_dir_person_instance`

  .. code-block:: python
    :lineno-start: 282
    :emphasize-lines: 1

                'can_vote',
                'first_name',
                'last_name',
                'say_hello',
                'sex',
                'year_of_birth',
            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

  These tests are good because they help document what is in the :ref:`class<everything is an object>` and catch its changes immediately.

  They are a problem because :ref:`class attributes<what is a class attribute?>` can change between Python_ versions, I have to remember the correct order of names and I am keeping two lists. There has to be a better way.

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

I want ``can_vote`` to return

* :red:`False` for ``no`` the person cannot vote if the person is not a citizen.
* :green:`True` for ``yes`` the person can vote if the person is a citizen.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a :ref:`call<how to call a function with input>` to ``can_vote`` from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 4

            reality = jane.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(jane.can_vote(), True)

        def test_john(self):

  the test is still green.

* I add a :ref:`call<how to call a function with input>` to ``can_vote`` from :ref:`test_john`

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 4

            reality = john.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(john.can_vote(), False)

        def test_mary(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True != False

  The :ref:`can_vote method<add can_vote method>` has to make a decision based on something.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``is_citizen`` to the :ref:`call<how to call a function with input>` to the :ref:`Person class<test Person class>` for ``john``

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 6

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

        def test_mary(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() got
               an unexpected keyword argument
               'is_citizen'

  because the :ref:`definition<how to make a function that takes input>` for the :ref:`__init__ method<the constructor method>` only takes five inputs (``self``, ``first_name``, ``last_name``, ``sex`` and ``year_of_birth``) and I :ref:`called<how to call a function with input>` it with ``is_citizen`` which is not one of those names.

* I add ``is_citizen`` to the parentheses of the :ref:`__init__ method<the constructor method>`, in ``person.py``

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
    :emphasize-lines: 6-7

    class Person:

        def __init__(
            self, first_name, last_name,
            sex, year_of_birth=None,
            # is_citizen,
            is_citizen=True,
        ):

  the terminal_ goes back to the :ref:`AssertionError<what causes AssertionError?>`.

* I add an :ref:`instance attribute<what is a class attribute?>` for ``is_citizen`` so I can use it in the :ref:`can_vote method<add can_vote method>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 13

    class Person:

        def __init__(
            self, first_name, last_name,
            sex, year_of_birth=None,
            # is_citizen,
            is_citizen=True,
        ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            self.sex = sex
            self.is_citizen = is_citizen

        @staticmethod

  still :ref:`AssertionError<what causes AssertionError?>`.

* I use the :ref:`class attribute<what is a class attribute?>` in the :ref:`can_vote method<add can_vote method>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 3-4

        @staticmethod
        def can_vote():
            # return True
            return self.is_citizen

        def say_hello(self):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I remove the :ref:`staticmethod decorator<what is the staticmethod decorator?>` from the :ref:`can_vote method<add can_vote method>` then add ``self`` to the parentheses

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 1-3

        # @staticmethod
        # def can_vote():
        def can_vote(self):
            # return True
            return self.is_citizen

        def say_hello(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for :ref:`test_dir_person_instance` because I added a new :ref:`attribute<what is a class attribute?>` (``is_citizen``).

* I add ``is_citizen`` to ``my_expectation`` in :ref:`test_dir_person_instance` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 285
    :emphasize-lines: 3

                'can_vote',
                'first_name',
                'is_citizen',
                'last_name',
                'say_hello',
                'sex',
                'year_of_birth',
            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

  ``joe`` and ``jane`` do not need to pass a value for the ``is_citizen`` parameter because :ref:`a method uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from ``person.py``

  .. code-block:: python
    :lineno-start: 4

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

        def can_vote(self):
            return self.is_citizen

        def say_hello(self):

* I add a :ref:`call<how to call a function with input>` to ``can_vote`` from :ref:`test_mary` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 4

            reality = mary.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(mary.can_vote(), False)

        def test_when_year_of_birth_is_not_an_integer(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True != False

  because :ref:`a method uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I add ``is_citizen`` to the :ref:`call<how to call a function with input>` to the :ref:`Person class<test Person class>` for ``mary``

  .. code-block:: python
    :lineno-start: 183
    :emphasize-lines: 6

              mary = src.person.Person(
                  first_name=first_name,
                  last_name=last_name,
                  sex=sex,
                  year_of_birth=year_of_birth,
                  is_citizen=False,
              )

              reality = mary.say_hello()
              assert reality == my_expectation
              self.assertEqual(reality, my_expectation)
              self.assertEqual(mary.can_vote(), False)

          def test_when_year_of_birth_is_not_an_integer(self):

  the test passes.

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
* I add a test for a person who is a citizen and younger than 18

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 6-14

            reality = mary.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(mary.can_vote(), False)

        def test_underage_citizen(self):
            person = src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=datetime.date.today().year-17,
                is_citizen=True,
            )
            self.assertEqual(person.can_vote(), False)

        def test_when_year_of_birth_is_not_an_integer(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

  - because ``can_vote`` returns the value of ``is_citizen``, it does not care about the age of the person.
  - I use a calculation (``datetime.date.today().year-17``) as the year of birth so that the person will always be younger than ``18`` in any year the test is run.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` with a :ref:`call<how to call a function with input>` to the :ref:`calculate_age function<add calculate_age function>` from the :ref:`can_vote method<add can_vote method>` in ``person.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3-4

        def can_vote(self):
            age = calculate_age(self.year_of_birth)
            if age < 18:
                return False
            return self.is_citizen

        def say_hello(self):

  the test passes because this happens when ``if age < 18:`` runs, Python_ checks if ``age`` which is the result of ``calculate_age(self.year_of_birth)`` is less than ``18``

* If ``age`` is greater than or equal to ``18``, it leaves the :ref:`if statement<if statements>` and continues to run the rest of the :ref:`method<what is a method?>` - ``return self.is_citizen``, which returns

  - :red:`False` as the output if the person is not a citizen

    .. code-block:: shell

      self.is_citizen = False
      age >= 18

      person.can_vote
      └──def can_vote(self):
         ├── if age < 18:
         │      return False
         └── return self.is_citizen

  - :green:`True` as the output, if the person is a citizen

    .. code-block:: shell

      self.is_citizen = True
      age >= 18

      person.can_vote
      └──def can_vote(self):
          ├── if age < 18:
          │      return False
          └── return self.is_citizen

  then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

* If ``age`` is less than ``18``, it goes to the next line - ``return False``, which returns :red:`False` as the output, then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

  .. code-block:: shell

    self.is_citizen = False
    age < 18

    person.can_vote
    └──def can_vote(self):
       └── if age < 18:
           └── return False
           return self.is_citizen

  .. code-block:: shell

    self.is_citizen = True
    age < 18

    person.can_vote
    └──def can_vote(self):
       └── if age < 18:
           └── return False
           return self.is_citizen

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

I add a :ref:`call<how to call a function with input>` to ``can_get_license`` from :ref:`test_joe`

.. code-block:: python
  :lineno-start: 54
  :emphasize-lines: 5

          reality = joe.say_hello()
          assert reality == my_expectation
          self.assertEqual(reality, my_expectation)
          self.assertEqual(joe.can_vote(), True)
          self.assertEqual(joe.can_get_license(), False)

      def test_jane(self):

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: 'Person' object
                  has no attribute 'can_get_license'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`method definition<how to make a function that takes input>` to the :ref:`Person class<test Person class>` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 14-15

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

        def can_get_license():
            return False

        def can_vote(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.can_get_license()
               takes 0 positional arguments but 1 was given

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1

        @staticmethod
        def can_get_license():
            return False

        def can_vote(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for :ref:`test_dir_person_class` and :ref:`test_dir_person_instance`.

* I add ``can_get_license`` to :ref:`test_dir_person_class` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 254
    :emphasize-lines: 1

                'can_get_license',
                'can_vote',
                'say_hello'
            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

        def test_dir_person_instance(self):

* I add ``can_get_license`` to :ref:`test_dir_person_instance`

  .. code-block:: python
    :lineno-start: 299
    :emphasize-lines: 1

                'can_get_license',
                'can_vote',
                'first_name',
                'is_citizen',
                'last_name',
                'say_hello',
                'sex',
                'year_of_birth',
            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


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

I want ``can_get_license`` to return

* :red:`False` for ``no`` the person cannot get a license if the person did not pass the test.
* :green:`True` for ``yes`` the person can get a license if the person passed the test.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`call<how to call a function with input>` to ``can_get_license`` from :ref:`test_mary`

.. code-block:: python
  :lineno-start: 192
  :emphasize-lines: 5

          reality = mary.say_hello()
          assert reality == my_expectation
          self.assertEqual(reality, my_expectation)
          self.assertEqual(mary.can_vote(), False)
          self.assertEqual(mary.can_get_license(), True)

      def test_underage_citizen(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: False != True

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``passed_test`` to the :ref:`call<how to call a function with input>` to the :ref:`Person class<test Person class>` for ``mary``

  .. code-block:: python
    :lineno-start: 184
    :emphasize-lines: 7

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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() got
               an unexpected keyword argument
               'passed_test'

  because the :ref:`definition<how to make a function that takes input>` for the :ref:`__init__ method<the constructor method>` only takes six inputs (``self``, ``first_name``, ``last_name``, ``sex``, ``year_of_birth`` and ``is_citizen``). I :ref:`called<how to call a function with input>` it with ``passed_test`` which is not one of those names.

* I add ``passed_test`` to the parentheses of the :ref:`__init__ method<the constructor method>`, in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7

    class Person:

        def __init__(
            self, first_name, last_name,
            sex, year_of_birth=None,
            is_citizen=True,
            passed_test,
        ):

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default
         follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I give ``passed_test`` a value to make it :ref:`optional<test_optional_arguments>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8

    class Person:

        def __init__(
            self, first_name, last_name,
            sex, year_of_birth=None,
            is_citizen=True,
            # passed_test,
            passed_test=False,
        ):

  the terminal_ goes back to the :ref:`AssertionError<what causes AssertionError?>`.

* I add an :ref:`instance attribute<what is a class attribute?>` for ``passed_test`` so I can use it in the :ref:`can_get_license method<add can_get_license method>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 15

    class Person:

        def __init__(
            self, first_name, last_name,
            sex, year_of_birth=None,
            is_citizen=True,
            # passed_test,
            passed_test=False,
        ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            self.sex = sex
            self.is_citizen = is_citizen
            self.passed_test = passed_test

        @staticmethod

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`.

* I use ``self.passed_test`` in the :ref:`can_get_license method<add can_get_license method>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 3-4

        @staticmethod
        def can_get_license():
            # return False
            return self.passed_test

        def can_vote(self):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I remove the :ref:`staticmethod decorator<what is the staticmethod decorator?>` from the :ref:`can_get_license method<add can_get_license method>` then add ``self`` to the parentheses

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 1-3

        # @staticmethod
        # def can_get_license():
        def can_get_license(self):
            # return False
            return self.passed_test

        def can_vote(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for :ref:`test_dir_person_instance` because I added a new :ref:`attribute<what is a class attribute?>` (``passed_test``).

* I add ``passed_test`` to ``my_expectation`` in :ref:`test_dir_person_instance` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 301
    :emphasize-lines: 6

                'can_get_license',
                'can_vote',
                'first_name',
                'is_citizen',
                'last_name',
                'passed_test',
                'say_hello',
                'sex',
                'year_of_birth',
            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from ``person.py``

  .. code-block:: python
    :lineno-start: 4

    class Person:

        def __init__(
            self, first_name, last_name,
            sex, year_of_birth=None,
            is_citizen=True,
            passed_test=False,
        ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            self.sex = sex
            self.is_citizen = is_citizen
            self.passed_test = passed_test

        def can_get_license(self):
            return self.passed_test

        def can_vote(self):

* I add a :ref:`call<how to call a function with input>` to ``can_get_license`` from :ref:`test_john`, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 5

            reality = john.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(john.can_vote(), False)
            self.assertEqual(john.can_get_license(), False)

        def test_mary(self):

  the test passes because :ref:`a method uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I add a :ref:`call<how to call a function with input>` to ``can_get_license`` from :ref:`test_jane`, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 5

            reality = jane.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)
            self.assertEqual(jane.can_vote(), True)
            self.assertEqual(jane.can_get_license(), True)

        def test_john(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False != True

  because :ref:`a method uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I add ``passed_test`` to the :ref:`call<how to call a function with input>` to the :ref:`Person class<test Person class>` for ``jane``

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 6

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

  the test passes.

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
    :lineno-start: 202
    :emphasize-lines: 8, 11-13

        def test_underage_citizen(self):
            person = src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=datetime.date.today().year-17,
                is_citizen=True,
                passed_test=True,
            )
            self.assertEqual(person.can_vote(), False)
            self.assertEqual(
                person.can_get_license(), False
            )

        def test_when_year_of_birth_is_not_an_integer(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

  because ``can_get_license`` currently returns the value of ``passed_test``. It does not care about the age of the person.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` with a :ref:`call<how to call a function with input>` to the :ref:`calculate_age function<add calculate_age function>` from the :ref:`can_get_license method<add can_get_license method>` in ``person.py``

.. code-block:: python
  :lineno-start: 19
  :emphasize-lines: 3-4

      def can_get_license(self):
          age = calculate_age(self.year_of_birth)
          if age < 18:
              return False
          return self.passed_test

      def can_vote(self):

the test passes because this happens when ``if age < 18:`` runs, Python_ checks if ``age`` which is the result of ``calculate_age(self.year_of_birth)`` is less than ``18``

* If ``age`` is greater than or equal to ``18``, it leaves the :ref:`if statement<if statements>` and continues to run the rest of the :ref:`method<what is a method?>` - ``return self.passed_test``, which returns

  - :red:`False` as the output, if the person failed the test

    .. code-block:: shell

      self.passed_test = False
      age >= 18

      person.can_get_license
      └──def can_get_license(self):
         ├── if age < 18:
         │      return False
         └── return self.passed_test

  - :green:`True` as the output, if the person passed the test

    .. code-block:: shell

      self.passed_test = True
      age >= 18

      person.can_get_license
      └──def can_get_license(self):
         ├── if age < 18:
         │      return False
         └── return self.passed_test

  then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

* If ``age`` is less than ``18``, it goes to the next line - ``return False``, which returns :red:`False` as the output, then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

  .. code-block:: shell

    self.passed_test = False
    age < 18

    person.can_get_license
    └──def can_get_license(self):
       └── if age < 18:
           └── return False
           return self.passed_test

  .. code-block:: shell

    self.passed_test = True
    age < 18

    person.can_get_license
    └──def can_get_license(self):
       └── if age < 18:
           └── return False
           return self.passed_test

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add condition to can_get_license'

----

*********************************************************************************
extract age instance attribute
*********************************************************************************

Three of the :ref:`methods<what is a method?>` of the :ref:`Person class<test Person class>` :ref:`call<how to call a function with input>` the :ref:`calculate_age function<add calculate_age function>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`instance attribute<what is a class attribute?>` to the :ref:`__init__ method<the constructor method>` so that the age is calculated once when an :ref:`instance<how to test if something is an instance>` is made, not every time one of the :ref:`methods is called<how to call a function with input>`.

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 15

  class Person:

      def __init__(
          self, first_name, last_name,
          sex, year_of_birth=None,
          is_citizen=True,
          passed_test=False,
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

  FAILED ...::TestPerson::test_dir_person_instance -
      AssertionError: assert ['__class__',...'__eq__', ...]
                          == ['__class__',...'__eq__', ...]
  FAILED ...::TestPerson::
      test_when_year_of_birth_is_not_an_integer -
          AssertionError

- :ref:`test_dir_person_instance` fails because I just added a new :ref:`class attribute<what is a class attribute?>`.
- :ref:`test_when_year_of_birth_is_not_an_integer` now fails when an :ref:`instance of the Person class<test Person class>` is made with a ``year_of_birth`` that is not an integer_.

----

*********************************************************************************
how to skip a test
*********************************************************************************

I can use `unittest.skip decorator`_ to skip a test. The problem with this solution is that I no longer know if the program does the thing the skipped test was written for.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the `unittest.skip decorator`_ to :ref:`test_when_year_of_birth_is_not_an_integer` with a note that it will always fail since it uses a year of birth that is not an integer, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 216
    :emphasize-lines: 1

        @unittest.skip('will always fail')
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
            # fails if year_of_birth is not an integer

        def test_dir_person_class(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    ================ short test summary info =================
    FAILED ...::TestPerson::test_dir_person_instance -
        AssertionError: assert ['__class__',...'__eq__', ...]
                            == ['__class__',...'__eq__', ...]
    ======== 1 failed, 6 passed, 1 skipped in S.TUs ==========

* I add ``age`` to ``my_expectation`` in :ref:`test_dir_person_instance`

  .. code-block:: python
    :lineno-start: 309
    :emphasize-lines: 1

                'age',
                'can_get_license',
                'can_vote',
                'first_name',
                'is_citizen',
                'last_name',
                'passed_test',
                'say_hello',
                'sex',
                'year_of_birth',
            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use ``self.age`` in the :ref:`can_get_license method<add can_get_license method>` in ``person.py``

  .. code-block:: python
    :lineno-start: 20
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
    :lineno-start: 27
    :emphasize-lines: 2-4

        def can_vote(self):
            # age = calculate_age(self.year_of_birth)
            # if age < 18:
            if self.age < 18:
                return False
            return self.is_citizen

        def say_hello(self):

  still green.

* I use ``self.age`` in the :ref:`say_hello method<test say_hello method>`

  .. code-block:: python
    :lineno-start: 34
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

* I remove the commented line from the :ref:`say_hello method<test say_hello method>`

  .. code-block:: python
    :lineno-start: 34

        def say_hello(self):
            return (
                f'Hello, my name is {self.first_name}'
                f' {self.last_name} and I am'
                f' {self.age}.'
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

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`method<what is a method?>` to the :ref:`Person class<test Person class>` that checks if the age is less than ``18`` and returns something else if it is not

.. code-block:: python
  :lineno-start: 27
  :emphasize-lines: 8-11

      def can_vote(self):
          # age = calculate_age(self.year_of_birth)
          # if age < 18:
          if self.age < 18:
              return False
          return self.is_citizen

      def check_age(age, response):
          if age < 18:
              return False
          return response

      def say_hello(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for :ref:`test_dir_person_class` and :ref:`test_dir_person_instance` because I added a new :ref:`method<what is a method?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``check_age`` to ``my_expectation`` in :ref:`test_dir_person_class` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 263
    :emphasize-lines: 3

                'can_get_license',
                'can_vote',
                'check_age',
                'say_hello',
            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

        def test_dir_person_instance(self):

* I add ``check_age`` to ``my_expectation`` in :ref:`test_dir_person_instance`

  .. code-block:: python
    :lineno-start: 310
    :emphasize-lines: 4

                'age',
                'can_get_license',
                'can_vote',
                'check_age',
                'first_name',
                'is_citizen',
                'last_name',
                'passed_test',
                'say_hello',
                'sex',
                'year_of_birth',
            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError
    # SyntaxError

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I :ref:`call<how to call a function with input>` the :ref:`check_age method<extract check_age method>` from the :ref:`can_vote method<add can_vote method>` in ``person.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4-9

        def can_vote(self):
            # age = calculate_age(self.year_of_birth)
            # if age < 18:
            # if self.age < 18:
            #     return False
            # return self.is_citizen
            return self.check_age(
                self.age, self.is_citizen
            )

        def check_age(age, response):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.check_age() takes
               2 positional arguments but 3 were given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to the :ref:`check_age method<extract check_age method>` since it does not use things from the :ref:`Person class<test Person class>`, only what it receives as input

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

        @staticmethod
        def check_age(age, response):
            if age < 18:
                return False
            return response

        def say_hello(self):

  the test passes.

* I remove the commented lines from the :ref:`can_vote method<add can_vote method>`

  .. code-block:: python
    :lineno-start: 27

        def can_vote(self):
            return self.check_age(
                self.age, self.is_citizen
            )

        @staticmethod
        def check_age(age, response):

* I :ref:`call<how to call a function with input>` the :ref:`check_age method<extract check_age method>` from the :ref:`can_get_license method<add can_get_license method>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 4-9

        def can_get_license(self):
            # age = calculate_age(self.year_of_birth)
            # if age < 18:
            # if self.age < 18:
            #     return False
            # return self.passed_test
            return self.check_age(
                self.age, self.passed_test
            )

        def can_vote(self):

  the tests are still green.

* I remove the commented lines from the :ref:`can_get_license method<add can_get_license method>`

  .. code-block:: python
    :lineno-start: 20

        def can_get_license(self):
            return self.check_age(
                self.age, self.passed_test
            )

        def can_vote(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract check_age method'

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

I can use :ref:`if statements<if statements>` to write a program_ that makes decisions based on :ref:`conditions<if statements>`.

My tests have problems:

* The attribute tests - :ref:`test_dir_person_class` and :ref:`test_dir_person_instance` catch changes to the :ref:`attributes and methods of the Person class<test_dir_person_instance>` and they are a problem to maintain. There has to be a better way.
* I skipped :ref:`test_when_year_of_birth_is_not_an_integer` because it is always in a :red:`RED` state since it causes an :ref:`Exception<errors>`. The only way to know that the code causes the :ref:`Exception<errors>` is to remove the `unittest.skip decorator`_. :ref:`There has to be a better way<how to test that an Exception is raised>`
* :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` also still have the problem where they are the same three tests. There has to be a better way.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a person with conditions: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python test driven development environment manually<how to make a Python test driven development environment manually>`.
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