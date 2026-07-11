.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

#################################################################################
how to make a person with conditions
#################################################################################

----

I want to be able to check if a person can get a license to drive, and if they can vote. In other words, I want something in the :ref:`person project<test person with datetime>` to make decisions based on :ref:`conditions<if statements>`, for example

* If a person is older than 18 and passes the driving test, the person can get a license.
* If a person is older than 18 and is a citizen, the person can vote

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
can joe vote?
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a :ref:`call<how to call a function>` to ``can_vote`` from :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 5-6

            reality = joe.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = joe.can_vote()
            self.assertIs(reality, True)

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
* I add a :ref:`function definition<how to make a function>` to the :ref:`Person class<add Person class>` in ``person.py``

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
        AssertionError: assert ['__class__',...'__eq__', ...] ==...
    FAILED ...::TestPerson::test_dir_person_instance -
        AssertionError: assert ['__class__',...'__eq__', ...] ==...

  the tests for the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the :ref:`Person class and an instance of it<add Person class>` are failing because I added a :ref:`method<what is a method?>` to it.

* I add ``can_vote`` to :ref:`test_dir_person_class`

  .. code-block:: python
    :lineno-start: 239
    :emphasize-lines: 1-2

                'can_vote',
                'say_hello',
            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

        def test_dir_person_instance(self):

* I add ``can_vote`` to :ref:`test_dir_person_instance`

  .. code-block:: python
    :lineno-start: 284
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

  These tests are good because it helps document what is in the :ref:`class<what is a class?>` and catches things immediately it changes.

  They are a problem because :ref:`class attributes<what is a class attribute>` can change between Python_ versions, I have to remember the correct order of names and I am keeping two lists. There has to be a better way.

* I open a new terminal_ then make sure I am in the ``person`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd person

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add can_vote'

----

*********************************************************************************
can jane vote?
*********************************************************************************

I add a :ref:`call<how to call a function>` to ``can_vote`` from :ref:`test_jane`

.. code-block:: python
  :lineno-start: 100
  :emphasize-lines: 5-6

          reality = jane.say_hello()
          assert reality == my_expectation
          self.assertEqual(reality, my_expectation)

          reality = jane.can_vote()
          self.assertIs(reality, True)

      def test_john(self):

the test is still green.

----

*********************************************************************************
can john vote?
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a :ref:`call<how to call a function>` to :ref:`test_john`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 5-6

            reality = joe.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = joe.can_vote()
            self.assertIs(reality, True)

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
* I add a :ref:`function definition<how to make a function>` to the :ref:`Person class<add Person class>` in ``person.py``

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
        AssertionError: assert ['__class__',...'__eq__', ...] ==...
    FAILED ...::TestPerson::test_dir_person_instance -
        AssertionError: assert ['__class__',...'__eq__', ...] ==...

  the tests for the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the :ref:`Person class and an instance of it<add Person class>` are failing because I added a :ref:`method<what is a method?>` to it.

* I add ``can_vote`` to :ref:`test_dir_person_class`

  .. code-block:: python
    :lineno-start: 239
    :emphasize-lines: 1-2

                'can_vote',
                'say_hello',
            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

        def test_dir_person_instance(self):

* I add ``can_vote`` to :ref:`test_dir_person_instance`

  .. code-block:: python
    :lineno-start: 284
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

  These tests are good because it helps document what is in the :ref:`class<what is a class?>` and catches things immediately it changes.

  They are a problem because :ref:`class attributes<what is a class attribute>` can change between Python_ versions, I have to remember the correct order of names and I am keeping two lists. There has to be a better way.

* I open a new terminal_ then make sure I am in the ``person`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd person

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add can_vote'

----


----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----



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