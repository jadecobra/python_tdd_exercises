.. include:: ../links.rst

.. _constructor: https://grokipedia.com/page/Constructor_(object-oriented_programming)
.. _constructor method: constructor_

#################################################################################
classes
#################################################################################

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/tests/test_person.py
  :language: python
  :linenos:

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`how to make a person`

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``person`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd person

  the terminal_ shows I am in the ``person`` folder_

  .. code-block:: python

    .../pumping_python/person

* I activate the `virtual environment`_

  .. code-block:: python
    :emphasize-lines: 1

    source .venv/bin/activate

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` NOT ``source .venv/bin/activate``

    .. code-block:: Powershell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  the terminal_ shows

  .. code-block:: python

    (.venv) .../pumping_python/person

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher --now --delay 0 .

  the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 4

    rootdir: .../pumping_python/person
    collected 2 items

    tests/test_person.py ..                                             [100%]

    ============================ 2 passed in X.YZs =============================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_person.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_factory_person_greeting
*********************************************************************************

I have a :ref:`function<what is a function?>` that takes in first name, last name, sex and year of birth for a person and returns a :ref:`dictionary<what is a dictionary?>` with the first name, last name, sex and age based on the year of birth.

What if I want the person to send a message about themselves. How would I do that? I can write a :ref:`function<what is a function?>` that takes in a person and returns a message

* I add a new test where I make a person

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 9-14


                dict(
                    first_name=self.random_first_name,
                    last_name='doe',
                    sex='M',
                    age=this_year()-self.random_year_of_birth,
                )
            )

        def test_factory_person_greeting(self):
            joe = src.person.factory(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )


    # Exceptions seen

  the ``factory`` :ref:`function<what is a function?>` will give ``joe`` a default value of ``'M'``   for ``sex`` because I did not give a value for it

* I add another person

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 7-11

        def test_factory_person_greeting(self):
            joe = src.person.factory(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )
            jane = src.person.factory(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )


    # Exceptions

  the ``factory`` :ref:`function<what is a function?>` will give ``jane`` a default value of ``doe`` for ``last_name`` because I did not give a value for it

* I add one more person

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 6-10

            jane = src.person.factory(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )
            john = src.person.factory(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )


    # Exceptions seen

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a `for loop`_ with the `subTest method`_ and an :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :lineno-start: 66
  :emphasize-lines: 7-12

          john = src.person.factory(
              first_name='john',
              last_name='smith',
              year_of_birth=1580,
          )

          for person in (joe, jane, john):
              with self.subTest(name=person.get('first_name')):
                  self.assertEqual(
                      src.person.hello(person),
                      None
                  )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>` for each one of the people

.. code-block:: python

  AttributeError: module 'src.person' has no attribute 'hello'

``person.py`` does not have a :ref:`function<what is a function?>` named ``hello``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``person.py`` in the :ref:`editor<2 editors>`
* I add the :ref:`function<what is a function?>` to ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 13-14

    def factory(
            first_name, year_of_birth,
            last_name='doe', sex='M',
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }


    def hello():
        return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: hello() takes 0 positional arguments but 1 was given

* I add a name to the definition

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1

    def hello(person):
        return None

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

I want the ``hello`` :ref:`function<what is a function?>` to return a message for the person I give as input

* I change the expectation in ``test_factory_person_greeting`` in ``test_person.py`` with an :ref:`f-string<how to pass values>` like I did in :ref:`how to pass values`

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 6-8

            for person in (joe, jane, john):
                with self.subTest(name=person.get('first_name')):
                    self.assertEqual(
                        src.person.hello(person),
                        (
                            f'Hi, my name is {person.get("first_name")} '
                            f'{person.get("last_name")} '
                            f'and I am {person.get("age")}'
                        )
                    )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'Hi, my name is john smith and I am 446'

* I copy the value from the terminal_ and paste it in the `return statement`_ in ``person.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2

    def hello(person):
        return 'Hi, my name is john smith and I am 446'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    E               - Hi, my name is john smith and I am 446
    E               + Hi, my name is jane doe and I am 35

  the first name, last name and ages are different

* I change the string_ to an :ref:`f-string<how to pass values>` with the value for ``first_name``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2

    def hello(person):
        return f'Hi, my name is {person.get("first_name")} smith and I am 446'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 4

    E               - Hi, my name is jane smith and I am 446
    E               ?                     ^^^^^          ^^^
    E               + Hi, my name is jane doe and I am 35
    E               ?                     ^^^          ^^

  the first name is the same, the last name and ages are different

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2-5

    def hello(person):
        return (
            f'Hi, my name is {person.get("first_name")} '
            f'{person.get("last_name")} and I am 446'
        )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines:  2, 4

    E               - Hi, my name is jane doe and I am 446
    E               ?                                  ^^^
    E               + Hi, my name is jane doe and I am 35
    E               ?                                  ^^

  the age is the only thing that is different now

* I add the age to the `return statement`_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5

    def hello(person):
        return (
            f'Hi, my name is {person.get("first_name")} '
            f'{person.get("last_name")} '
            f'and I am {person.get("age")}'
        )

  the test passes

The solution works, it needs different :ref:`functions<what is a function?>` - one to make the person and one to make the message.

----

*********************************************************************************
test_classy_person_greeting
*********************************************************************************

I can also make a person with a :ref:`class<what is a class?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to ``test_person.py``

.. code-block:: python
  :lineno-start: 72
  :emphasize-lines: 12-17

          for person in (joe, jane, john):
              with self.subTest(name=person.get('first_name')):
                  self.assertEqual(
                      src.person.hello(person),
                      (
                          f'Hi, my name is {person.get("first_name")} '
                          f'{person.get("last_name")} '
                          f'and I am {person.get("age")}'
                      )
                  )

      def test_classy_person_greeting(self):
          joe = src.person.Person(
              first_name='joe',
              last_name='blow',
              year_of_birth=1996,
          )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.person' has no attribute 'Person'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 9, 11

    def hello(person):
        return (
            f'Hi, my name is {person.get("first_name")} '
            f'{person.get("last_name")} '
            f'and I am {person.get("age")}'
        )


    class Person:

        pass

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person() takes no arguments

* classes_ have a `constructor method`_ that is used to make copies of the :ref:`class<what is a class?>`. I add it

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 3-4

    class Person:

        def __init__():
            return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() got an unexpected keyword argument 'first_name'

* I add the name

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 3

    class Person:

        def __init__(first_name):
            return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() got multiple values for argument 'first_name'

* The ``__init__`` :ref:`method<what is a function?>` takes the :ref:`class<what is a class?>` as the first argument. I add ``self`` the way I do with all the tests in the book

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 3

    class Person:

        def __init__(self, first_name):
            return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: Person.__init__() got an unexpected keyword argument 'last_name'. Did you mean 'first_name'?

  I have seen this before, so far it is the same as making the ``factory`` :ref:`function<what is a function?>`

* I add ``last_name``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 1

        def __init__(self, first_name, last_name):
            return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() got an unexpected keyword argument 'year_of_birth'

  still the same as making the ``factory`` :ref:`function<what is a function?>`

* I add ``year_of_birth`` to the definition

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 3-6

    class Person:

        def __init__(
                self, first_name, last_name,
                year_of_birth,
            ):
            return

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next person to ``test_classy_person_greeting``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 7-11

        def test_classy_person_greeting(self):
            joe = src.person.Person(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )
            jane = src.person.Person(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() got an unexpected keyword argument 'sex'

* I add ``sex`` to the ``__init__`` :ref:`method<functions>` in ``person.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 3

        def __init__(
                self, first_name, last_name,
                year_of_birth, sex,
            ):
            return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() missing 1 required positional argument: 'sex'

  I did not provide a value for ``sex`` when I made ``joe``, and the ``factory`` :ref:`function<what is a function?>` has a default value of ``'M'`` for it

* I add a default value for ``sex`` in the  ``__init__`` :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 3

        def __init__(
                self, first_name, last_name,
                year_of_birth, sex=None,
            ):
            return None

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  I cannot put a parameter that does NOT have a default value after a parameter that has a default value

* I add a default value for ``year_of_birth``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 3

    def __init__(
            self, first_name, last_name=None,
            year_of_birth=None, sex=None,
        ):
        return None

  the test passes

----

* I add the next person

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 6-10

            jane = src.person.Person(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )
            john = src.person.Person(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )


    # Exceptions seen

  the test is still green

* I copy the `for loop`_ with the :ref:`assertion<what is an assertion?>` from :ref:`test_factory_person_greeting` and paste it in ``test_classy_person_greeting``

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 7-16

            john = src.person.Person(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )

            for person in (joe, jane, john):
                with self.subTest(name=person.get('first_name')):
                    self.assertEqual(
                        src.person.hello(person),
                        (
                            f'Hi, my name is {person.get("first_name")} '
                            f'{person.get("last_name")} '
                            f'and I am {person.get("age")}'
                        )
                    )


    # Exceptions seen

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'get'

  the ``Person`` :ref:`class<what is a class?>` does not have a :ref:`method<what is a function?>` named ``get``

* I can use :ref:`class attributes<test_attribute_error_w_class_attributes>` directly with no need for a ``get`` :ref:`method<what is a function?>`. I change the line for the `subTest method`_

  .. code-block:: python
    :lineno-start: 100
    :emphasize-lines: 2

            for person in (joe, jane, john):
                with self.subTest(name=person.first_name):
                    self.assertEqual(

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'first_name'

* I add a :ref:`class attribute<test_attribute_error_w_class_attributes>` to the ``__init__`` :ref:`method<what is a function?>` of the ``Person`` :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 5

        def __init__(
                self, first_name, last_name=None,
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            return None

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'get'

  the test calls the ``hello`` :ref:`function<what is a function?>` which takes in a :ref:`dictionary<what is a dictionary?>` and calls the :ref:`get method<test_get_value_of_a_key_in_a_dictionary>`, the ``Person`` object_ does not have a :ref:`get method<test_get_value_of_a_key_in_a_dictionary>`

* I can call :ref:`methods<what is a function?>` from outside a :ref:`class<what is a class?>` the way I use a :ref:`class attribute<test_attribute_error_w_class_attributes>`. I change the call in the :ref:`assertion<what is an assertion?>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 2

                    self.assertEqual(
                        person.hello(person),
                        (
                            f'Hi, my name is {person.get("first_name")} '
                            f'{person.get("last_name")} '
                            f'and I am {person.get("age")}'
                        )
                    )

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'hello'

* I add the :ref:`method<what is a function?>` to the ``Person`` :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 8-9

        def __init__(
                self, first_name, last_name=None,
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            return None

        def hello():
            return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.hello() takes 0 positional arguments but 2 were given

  the test calls the :ref:`method<what is a function?>` with one input and the definition takes no input

* I add the `staticmethod decorator`_ to the :ref:`method<what is a function?>` because it does not use anything in the :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 8-10

        def __init__(
                self, first_name, last_name=None,
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            return None

        @staticmethod
        def hello():
            return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.hello() takes 0 positional arguments but 1 was given

* I add a name to the definition

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

        @staticmethod
        def hello(person):
            return None

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'get'

* I change the :ref:`assertion<what is an assertion?>` in ``test_classy_person_greeting`` in ``test_person.py`` to use the ``first_name`` :ref:`class attribute<test_attribute_error_w_class_attributes>`

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 4

                    self.assertEqual(
                        person.hello(person),
                        (
                            f'Hi, my name is {person.first_name} '
                            f'{person.get("last_name")} '
                            f'and I am {person.get("age")}'
                        )
                    )

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'get'

* I make the same change for the last name

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 5

                    self.assertEqual(
                        person.hello(person),
                        (
                            f'Hi, my name is {person.first_name} '
                            f'{person.last_name} '
                            f'and I am {person.get("age")}'
                        )
                    )

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: 'Person' object has no attribute 'last_name'. Did you mean: 'first_name'?

* I add a :ref:`class attribute<test_attribute_error_w_class_attributes>` for ``last_name`` to the ``__init__`` :ref:`method<what is a function?>` of the ``Person`` :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 6

        def __init__(
                self, first_name, last_name=None,
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            self.last_name = last_name
            return None

        @staticmethod
        def hello(person):

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'get'

* I want to use a :ref:`method<what is a function?>` to calculate the age. I change the :ref:`assertion<what is an assertion?>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 6

                    self.assertEqual(
                        person.hello(person),
                        (
                            f'Hi, my name is {person.first_name} '
                            f'{person.last_name} '
                            f'and I am {person.get_age()}'
                        )
                    )

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'get_age'

* I add the :ref:`method<what is a function?>` to the ``Person`` :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 5-6


        @staticmethod
        def hello(person):
            return None

        def get_age():
            return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.get_age() takes 0 positional arguments but 1 was given

* I add the `staticmethod decorator`_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 5-7

        @staticmethod
        def hello(person):
            return None

        @staticmethod
        def get_age():
            return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'Hi, my name is john smith and I am None'

* I copy and paste the string_ in the `return statement`_ of the ``hello`` :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 3

        @staticmethod
        def hello(person):
            return 'Hi, my name is john smith and I am None'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 4

    E               - Hi, my name is john smith and I am None
    E               ?                  - ^^^^^^
    E               + Hi, my name is jane None and I am None
    E               ?                 +++++  ^

  the value for first name and last name are different

* I change the string_ in the `return statement`_ to an :ref:`f-string<how to pass values>` with the value for ``first_name``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 3

        @staticmethod
        def hello(person):
            return f'Hi, my name is {person.first_name} smith and I am None'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 4

    E               - Hi, my name is jane smith and I am None
    E               ?                     ^^^^^
    E               + Hi, my name is jane None and I am None
    E               ?                     ^^^^

  the values for the last name are different

* I add it to the :ref:`f-string<how to pass values>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 3-6

        @staticmethod
        def hello(person):
            return (
                f'Hi, my name is {person.first_name} '
                f'{person.last_name} and I am None'
            )

  the test passes

----

* I can call a :ref:`method<what is a function?>` that belongs to a :ref:`class<what is a class?>` without the need to pass in the :ref:`class<what is a class?>` as input since I can use the :ref:`class<what is a class?>` with ``self``. I remove the repetition of the ``Person`` object_ in the call to the ``hello`` :ref:`method<what is a function?>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 100
    :emphasize-lines: 4
    :emphasize-text: ( )

            for person in (joe, jane, john):
                with self.subTest(name=person.first_name):
                    self.assertEqual(
                        person.hello(),
                        (
                            f'Hi, my name is {person.first_name} '
                            f'{person.last_name} '
                            f'and I am {person.get_age()}'
                        )
                    )


    # Exceptions seen

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.hello() missing 1 required positional argument: 'person'

* I remove the `staticmethod decorator`_ from the ``hello`` :ref:`method<what is a function?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 26

        def __init__(
                self, first_name, last_name=None,
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            self.last_name = last_name
            return None

        def hello(person):
            return (
                f'Hi, my name is {person.first_name} '
                f'{person.last_name} and I am None'
            )

  the test passes.

  This works because ``person`` in the parentheses is for the ``Person`` :ref:`class<what is a class?>` that the ``hello`` :ref:`method<what is a function?>` is part of.

  When I wrapped the ``hello`` :ref:`function<what is a function?>` with the `staticmethod decorator`_, it was a :ref:`function<what is a function?>` that did not use other parts (:ref:`class attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a function?>`) of the :ref:`class<what is a class?>` it belongs to.

* I use the ``Rename Symbol`` feature of the `Integrated Development Environment (IDE)`_ to change the name of the input parameter from ``person`` to ``self`` to match :ref:`Python convention<how to use class methods and attributes>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1, 3, 4
    :emphasize-text: self

        def hello(self):
            return (
                f'Hi, my name is {self.first_name} '
                f'{self.last_name} and I am None'
            )

  the test is still green, and there is a problem with the last name and age.

----

*********************************************************************************
test_update_factory_person_year_of_birth
*********************************************************************************


I made a person named ``john`` in :ref:`test_factory_person_greeting` and :ref:`test_classy_person_greeting` with a year of birth of ``1580``.

Maybe I made a mistake when typing his age and typed ``5`` instead of ``9``. How would I change the year of birth of a person made with the ``factory`` :ref:`function<what is a function?>` if I cannot change the original year of birth?

* I could try updating the ``year_of_birth``
* I could try making a :ref:`function<what is a function?>` that takes a person and a new year of birth as inputs, and returns the person with the correct age
* I could make a new ``factory`` :ref:`function<what is a function?>` that returns a :ref:`dictionary<what is a dictionary?>` with ``year_of_birth`` as a :ref:`key<test_keys_of_a_dictionary>` which allows me to change it, then make another :ref:`function<what is a function?>` that calculates the age from the returned :ref:`dictionary<what is a dictionary?>` - this sounds like a lot of work, I would also have to rewrite the tests. No, thank you
* I could make a :ref:`class<what is a class?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I cannot update the ``year_of_birth`` :ref:`key<test_keys_of_a_dictionary>` because the :ref:`function<what is a function?>` returns a :ref:`dictionary<what is a dictionary?>` that does not have a ``year_of_birth`` :ref:`key<test_keys_of_a_dictionary>`. I add a new test

.. code-block:: python
  :lineno-start: 100
  :emphasize-lines: 12-18


            for person in (joe, jane, john):
                with self.subTest(name=person.first_name):
                    self.assertEqual(
                        person.hello(),
                        (
                            f'Hi, my name is {person.first_name} '
                            f'{person.last_name} '
                            f'and I am {person.get_age()}'
                        )
                    )

        def test_update_factory_person_year_of_birth(self):
            person = src.person.factory(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )
            self.assertEqual(person.get('age', 0))


    # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 446 != 0

----

=================================================================================
:green:`GREEN`: make it passs
----

=================================================================================

----

I change the expectation

.. code-block:: python
  :lineno-start: 117
  :emphasize-lines: 1

          self.assertEqual(person.get('age'), 446)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I try to use the ``year_of_birth`` :ref:`key<test_keys_of_a_dictionary>`

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 3

            self.assertEqual(person.get('age'), 446)

            person['year_of_birth']


    # Exceptions seen

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: 'year_of_birth'

  there is no ``year_of_birth`` :ref:`key<test_keys_of_a_dictionary>` in the :ref:`dictionary<what is a dictionary?>` returned by the ``factory`` :ref:`function<what is a function?>`

* I add :ref:`KeyError<test_key_error>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 7
    :emphasize-text: KeyError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError
    # KeyError

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 3-4

            self.assertEqual(person.get('age'), 446)

            with self.assertRaises(KeyError):
                person['year_of_birth']


    # Exceptions seen

  the test passes

* I add a new :ref:`value<test_values_of_a_dictionary>` for ``year_of_birth`` with the :ref:`setdefault method<test_setdefault_adds_given_key_to_a_dictionary>`

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 3-6

            with self.assertRaises(KeyError):
                person['year_of_birth']
            self.assertEqual(
                person.setdefault('year_of_birth', 1980),
                None
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1980 != None

* I change the expectation

  .. code-block:: python
    :lineno-start: 121

            self.assertEqual(
                person.setdefault('year_of_birth', 1980),
                1980
            )

  the test passes because the :ref:`dictionary<what is a dictionary?>` now has a :ref:`key<test_keys_of_a_dictionary>` named ``year_of_birth`` with the new value

* I add an :ref:`assertion<what is an assertion?>` for the age of ``john smith`` again

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 5

            self.assertEqual(
                person.setdefault('year_of_birth', 1980),
                1980
            )
            self.assertEqual(person.get('age'), 46)

    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 446 != 46

  the ``factory`` :ref:`function<what is a function?>` uses the value for ``year_of_birth`` to calculate the age when it makes the :ref:`dictionary<what is a dictionary?>`.

  When I change the value or add the :ref:`key<test_keys_of_a_dictionary>`, it does not do anything to the age. :ref:`There has to be a better way<test_update_classy_person_year_of_birth>`

* I change the expectation

  .. code-block:: python
    :lineno-start: 125
    :emphasize-lines: 1

    self.assertEqual(person.get('age'), 446)

  the test passes

----

* I can make a :ref:`function<what is a function?>` that takes a person and a new year of birth as inputs, and returns the person with the correct age. I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 125
    :emphasize-lines: 3-11

            self.assertEqual(person.get('age'), 446)

            self.assertEqual(
                src.person.update_year_of_birth(person, 1980),
                dict(
                    first_name=person.get('first_name'),
                    last_name=person.get('last_name'),
                    sex=person.get('sex'),
                    age=this_year()-1980,
                )
            )


    # Exceptions seen

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.person' has no attribute 'update_year_of_birth'

* I add the :ref:`function<what is a function?>` to ``person.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 9-10

    def hello(person):
        return (
            f'Hi, my name is {person.get("first_name")} '
            f'{person.get("last_name")} '
            f'and I am {person.get("age")}'
        )


    def update_year_of_birth():
        return None


    class Person:

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: update_year_of_birth() takes 0 positional arguments but 2 were given

* I add the two names in parentheses

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 1

    def update_year_of_birth(person, new_year_of_birth):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != {'first_name': 'john', 'last_name': 'smith', 'sex': 'M', 'age': 46}

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2-7

    def update_year_of_birth(person, new_year_of_birth):
        return factory(
            first_name=person.get('first_name'),
            last_name=person.get('last_name'),
            sex=person.get('sex'),
            year_of_birth=new_year_of_birth,
        )


    class Person:

  the test passes

----

* time to remove some duplication. I add a :ref:`variable<what is a variable?>` for the original year of birth in ``test_update_factory_person_year_of_birth`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 2

        def test_update_factory_person_year_of_birth(self):
            original_year_of_birth = 1580

            person = src.person.factory(

  the test is still green

* I use the :ref:`variable<what is a variable?>` in the call to ``src.person.factory``

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 6-7

            original_year_of_birth = 1580

            person = src.person.factory(
                first_name='john',
                last_name='smith',
                # year_of_birth=1580,
                year_of_birth=original_year_of_birth,
            )

  still green

* I use the :ref:`variable<what is a variable?>` in the first :ref:`assertion<what is an assertion?>` for the age

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 7-11

            person = src.person.factory(
                first_name='john',
                last_name='smith',
                # year_of_birth=1580,
                year_of_birth=original_year_of_birth,
            )
            # self.assertEqual(person.get('age'), 446)
            self.assertEqual(
                person.get('age'),
                this_year()-original_year_of_birth
            )

            with self.assertRaises(KeyError):

  green

* I use the :ref:`variable<what is a variable?>` in the second :ref:`assertion<what is an assertion?>` for the age

  .. code-block:: python
    :lineno-start: 126
    :emphasize-lines: 7-11

            with self.assertRaises(KeyError):
                person['year_of_birth']
            self.assertEqual(
                person.setdefault('year_of_birth', 1980),
                1980
            )
            # self.assertEqual(person.get('age'), 446)
            self.assertEqual(
                person.get('age'),
                this_year()-original_year_of_birth
            )

            self.assertEqual(

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 111

        def test_update_factory_person_year_of_birth(self):
            original_year_of_birth = 1580

            person = src.person.factory(
                first_name='john',
                last_name='smith',
                year_of_birth=original_year_of_birth,
            )
            self.assertEqual(
                person.get('age'),
                this_year()-original_year_of_birth
            )

            with self.assertRaises(KeyError):
                person['year_of_birth']
            self.assertEqual(
                person.setdefault('year_of_birth', 1980),
                1980
            )
            self.assertEqual(
                person.get('age'),
                this_year()-original_year_of_birth
            )

            self.assertEqual(
                src.person.update_year_of_birth(person, 1980),
                dict(
                    first_name=person.get('first_name'),
                    last_name=person.get('last_name'),
                    sex=person.get('sex'),
                    age=this_year()-1980,
                )
            )


    # Exceptions seen

  the test is still green

----

* I add a :ref:`variable<what is a variable?>` for the new year of birth

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 3

        def test_update_factory_person_year_of_birth(self):
            original_year_of_birth = 1580
            new_year_of_birth = 1980

            person = src.person.factory(

  still green

* I use the :ref:`variable<what is a variable?>` in the :ref:`assertion<what is an assertion?>` for the call to the :ref:`setdefault method<test_setdefault_adds_given_key_to_a_dictionary>`

  .. code-block:: python
    :lineno-start: 125
    :emphasize-lines: 4-7

              with self.assertRaises(KeyError):
                  person['year_of_birth']
              self.assertEqual(
                  # person.setdefault('year_of_birth', 1980),
                  person.setdefault('year_of_birth', new_year_of_birth),
                  # 1980
                  new_year_of_birth
              )
              self.assertEqual(

  the test is still green

* I use the :ref:`variable<what is a variable?>`  in the last :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 2-6, 11-12

            self.assertEqual(
                # src.person.update_year_of_birth(person, 1980),
                src.person.update_year_of_birth(
                    person,
                    new_year_of_birth
                ),
                dict(
                    first_name=person.get('first_name'),
                    last_name=person.get('last_name'),
                    sex=person.get('sex'),
                    # age=this_year()-1980,
                    age=this_year()-new_year_of_birth,
                )
            )


    # Exceptions seen

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 111

        def test_update_factory_person_year_of_birth(self):
            original_year_of_birth = 1580
            new_year_of_birth = 1980

            person = src.person.factory(
                first_name='john',
                last_name='smith',
                year_of_birth=original_year_of_birth,
            )
            self.assertEqual(
                person.get('age'),
                this_year()-original_year_of_birth
            )

            with self.assertRaises(KeyError):
                person['year_of_birth']
            self.assertEqual(
                person.setdefault('year_of_birth', new_year_of_birth),
                new_year_of_birth
            )
            self.assertEqual(
                person.get('age'),
                this_year()-original_year_of_birth
            )

            self.assertEqual(
                src.person.update_year_of_birth(
                    person,
                    new_year_of_birth
                ),
                dict(
                    first_name=person.get('first_name'),
                    last_name=person.get('last_name'),
                    sex=person.get('sex'),
                    age=this_year()-new_year_of_birth,
                )
            )


    # Exceptions seen

  green

----

* I add a :ref:`variable<what is a variable?>` for the original age calculation

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 3

        def test_update_factory_person_year_of_birth(self):
            original_year_of_birth = 1580
            original_age = this_year() - original_year_of_birth
            new_year_of_birth = 1980

* I use the :ref:`variable<what is a variable?>` in the first :ref:`assertion<what is an assertion?>` for the age

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 8-9

            person = src.person.factory(
                first_name='john',
                last_name='smith',
                year_of_birth=original_year_of_birth,
            )
            self.assertEqual(
                person.get('age'),
                # this_year()-original_year_of_birth
                original_age
            )

  the test is still green

* I use the :ref:`variable<what is a variable?>` in the second :ref:`assertion<what is an assertion?>` for the age

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 9-10

            with self.assertRaises(KeyError):
                person['year_of_birth']
            self.assertEqual(
                person.setdefault('year_of_birth', new_year_of_birth),
                new_year_of_birth
            )
            self.assertEqual(
                person.get('age'),
                # this_year()-original_year_of_birth
                original_age
            )

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 111

        def test_update_factory_person_year_of_birth(self):
            original_year_of_birth = 1580
            original_age = this_year() - original_year_of_birth
            new_year_of_birth = 1980

            person = src.person.factory(
                first_name='john',
                last_name='smith',
                year_of_birth=original_year_of_birth,
            )
            self.assertEqual(
                person.get('age'),
                original_age
            )

            with self.assertRaises(KeyError):
                person['year_of_birth']
            self.assertEqual(
                person.setdefault('year_of_birth', new_year_of_birth),
                new_year_of_birth
            )
            self.assertEqual(
                person.get('age'),
                original_age
            )

            self.assertEqual(
                src.person.update_year_of_birth(
                    person,
                    new_year_of_birth
                ),
                dict(
                    first_name=person.get('first_name'),
                    last_name=person.get('last_name'),
                    sex=person.get('sex'),
                    age=this_year()-new_year_of_birth,
                )
            )


    # Exceptions seen

I had to make a new person with the same first name, last name, sex and the new year of birth to change the year of birth. How would I solve this problem with a :ref:`class<what is a class?>`?

----

*********************************************************************************
test_update_classy_person_year_of_birth
*********************************************************************************


----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test

.. code-block:: python
  :lineno-start: 142
  :emphasize-lines: 9-15

              dict(
                  first_name=person.get('first_name'),
                  last_name=person.get('last_name'),
                  sex=person.get('sex'),
                  age=this_year()-new_year_of_birth,
              )
          )

      def test_update_classy_person_year_of_birth(self):
          person = src.person.Person(
              first_name='john',
              last_name='smith',
              year_of_birth=1580,
          )
          self.assertEqual(person.get_age(), 0)


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: None != 0

the ``get_age`` :ref:`method<what is a function?>` returns :ref:`None<what is None?>`. I want it to return the difference between this year and the year of birth

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a calculation to the ``get_age`` :ref:`method<what is a function?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 3

        @staticmethod
        def get_age():
            return this_year() - self.year_of_birth

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'this_year' is not defined

* I add the :ref:`function<what is a function?>` at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import datetime


    def this_year():
        return datetime.datetime.today().year


    def factory(

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the definition of the ``get_age`` :ref:`method<what is a function?>` parentheses

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2

        @staticmethod
        def get_age(self):
            return this_year() - self.year_of_birth

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.get_age() missing 1 required positional argument: 'self'

* I remove the `staticmethod decorator`_ from the ``get_age`` :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 47

        def hello(self):
            return (
                f'Hi, my name is {self.first_name} '
                f'{self.last_name} and I am None'
            )

        def get_age(self):
            return this_year() - self.year_of_birth

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'year_of_birth'

* I add a :ref:`class attribute<test_attribute_error_w_class_attributes>` to the ``__init__`` :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 9

    class Person:

        def __init__(
                self, first_name, last_name=None,
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            return None

        def hello(self):
            return (
                f'Hi, my name is {self.first_name} '
                f'{self.last_name} and I am {self.get_age()}'
            )

        def get_age(self):
            return this_year() - self.year_of_birth

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 446 != 0

* I change the expectation in ``test_person.py``

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 1

            self.assertEqual(person.get_age(), 446)

  the terminal_ shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell
    :emphasize-lines: 2, 4

    E               - Hi, my name is john smith and I am None
    E               ?                                    ^^^^
    E               + Hi, my name is john smith and I am 446
    E               ?                                    ^^^

  ``test_update_factory_person_year_of_birth`` expects a number, the ``hello`` :ref:`method<what is a function?>` returns :ref:`None<what is None?>`

* I add a call to the ``get_age`` :ref:`method<what is a function?>` in the ``hello`` :ref:`method<what is a function?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 4

        def hello(self):
            return (
                f'Hi, my name is {self.first_name} '
                f'{self.last_name} and I am {self.get_age()}'
            )

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use the ``this_year`` :ref:`function<what is a function?>` in the ``factory`` :ref:`function<what is a function?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 9-10

    def factory(
            first_name, year_of_birth,
            last_name='doe', sex='M',
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            # 'age': datetime.datetime.today().year - year_of_birth,
            'age': this_year() - year_of_birth,
        }

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 8

    def factory(
            first_name, year_of_birth,
            last_name='doe', sex='M',
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': this_year() - year_of_birth,
        }

* I can change the value of a :ref:`class attribute<test_attribute_error_w_class_attributes>` after the object_ has been made, kind of like I did in :ref:`test_setting_items_in_a_list`. I add a statement to ``test_update_classy_person_year_of_birth`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 3

            self.assertEqual(person.get_age(), 446)

            person.year_of_birth = 1980


    # Exceptions seen

* I add another :ref:`assertion<what is an assertion?>` for the age calculation

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 4

            self.assertEqual(person.get_age(), 446)

            person.year_of_birth = 1980
            self.assertEqual(person.get_age(), 446)


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 46 != 446

* I change the expectation in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 1

            self.assertEqual(person.get_age(), this_year()-1980)

  the test passes. Wait! That was a lot simpler than doing it with just :ref:`functions<what is a function?>`

* I add a :ref:`variable<what is a variable?>` to remove repetition

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 3

            self.assertEqual(person.get_age(), 446)

            new_year_of_birth = 1980
            person.year_of_birth = 1980
            self.assertEqual(person.get_age(), this_year()-1980)


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 2-8

            new_year_of_birth = 1980
            # person.year_of_birth = 1980
            person.year_of_birth = new_year_of_birth
            # self.assertEqual(person.get_age(), this_year()-1980)
            self.assertEqual(
                person.get_age(),
                this_year()-new_year_of_birth
            )


    # Exceptions seen

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 150

        def test_update_classy_person_year_of_birth(self):
            person = src.person.Person(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )
            self.assertEqual(person.get_age(), 446)

            new_year_of_birth = 1980
            person.year_of_birth = new_year_of_birth
            self.assertEqual(
                person.get_age(),
                this_year()-new_year_of_birth
            )


    # Exceptions seen

  still green

.. NOTE::

  - Classes_ have :ref:`attributes<test_attribute_error_w_class_attributes>` that can be changed.
  - Since the age calculation uses the ``year_of_birth``, and is done when I call it, not when the person is made, it will always calculate the right age.
  - It is easier to make changes to a person when I use a :ref:`class<what is a class?>` than when I use only :ref:`functions<what is a function?>`

----

*********************************************************************************
test with random person
*********************************************************************************


I want to add randomness to the test

* I add a :ref:`class attribute<test_attribute_error_w_class_attributes>` for ``last_name`` to the `setUp method`_ in ``test_person.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 6

        def setUp(self):
            self.random_year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            self.random_first_name = choose('jane', 'joe', 'john', 'person')
            self.random_last_name = choose('doe', 'smith', 'blow', 'public')

        def test_factory_takes_keyword_arguments(self):

* ``self.random_first_name`` and ``self.random_last_name`` look the same. I add a :ref:`class attribute<test_attribute_error_w_class_attributes>` for the values of the names passed to the ``choose`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3-6

    class TestPerson(unittest.TestCase):

        RANDOM_NAMES = (
            'jane', 'joe', 'john', 'person',
            'doe', 'smith', 'blow', 'public',
        )

        def setUp(self):

* I use ``RANDOM_NAMES`` in the calls to the ``choose`` :ref:`function<what is a function?>` for ``random_first_name`` and ``random_last_name``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 5-8

        def setUp(self):
            self.random_year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            # self.random_first_name = choose('jane', 'joe', 'john', 'person')
            self.random_first_name = choose(*self.RANDOM_NAMES)
            # self.random_last_name = choose('doe', 'smith', 'blow', 'public')
            self.random_last_name = choose(*self.RANDOM_NAMES)

  the tests are still green and there are now more names to choose from

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 22

        def setUp(self):
            self.random_year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            self.random_first_name = choose(*self.RANDOM_NAMES)
            self.random_last_name = choose(*self.RANDOM_NAMES)

        def test_factory_takes_keyword_arguments(self):

* I use ``self.random_last_name`` in :ref:`test_factory_takes_keyword_arguments`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 4-5

        def test_factory_takes_keyword_arguments(self):
            a_person = dict(
                first_name=self.random_first_name,
                # last_name=choose('doe', 'smith', 'blow', 'public'),
                last_name=self.random_last_name,
                sex=choose('F', 'M'),
            )

  the test is still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 29

        def test_factory_takes_keyword_arguments(self):
            a_person = dict(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                sex=choose('F', 'M'),
            )

  still green

----

* I add a :ref:`class attribute<test_attribute_error_w_class_attributes>` for ``sex`` to the `setUp method`_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 7

        def setUp(self):
            self.random_year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            self.random_first_name = choose(*self.RANDOM_NAMES)
            self.random_last_name = choose(*self.RANDOM_NAMES)
            self.random_sex = choose('M', 'F')

        def test_factory_takes_keyword_arguments(self):

* I use the new :ref:`class attribute<test_attribute_error_w_class_attributes>` in :ref:`test_factory_takes_keyword_arguments`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 5-6

        def test_factory_takes_keyword_arguments(self):
            a_person = dict(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                # sex=choose('F', 'M'),
                sex=self.random_sex,
            )

  green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 30

        def test_factory_takes_keyword_arguments(self):
            a_person = dict(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                sex=self.random_sex,
            )

  still green

----

* I make a random person with the ``factory`` :ref:`function<what is a function?>` in the `setUp method`_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 8-13

        def setUp(self):
            self.random_year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            self.random_first_name = choose(*self.RANDOM_NAMES)
            self.random_last_name = choose(*self.RANDOM_NAMES)
            self.random_sex = choose('M', 'F')
            self.random_factory_person = src.person.factory(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                sex=self.random_sex,
                year_of_birth=self.random_year_of_birth,
            )

        def test_factory_takes_keyword_arguments(self):

* I use the ``random_factory_person`` :ref:`class attribute<test_attribute_error_w_class_attributes>` in the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_factory_takes_keyword_arguments`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 6-10

            self.assertEqual(
                src.person.factory(
                    **a_person,
                    year_of_birth=self.random_year_of_birth,
                ),
                # dict(
                #     **a_person,
                #     age=this_year()-self.random_year_of_birth,
                # )
                self.random_factory_person
            )

        def test_factory_w_default_arguments(self):

  the test is still green

* I no longer need the ``a_person`` :ref:`variable<what is a variable?>`, I can use the :ref:`class attributes<test_attribute_error_w_class_attributes>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3-6

            self.assertEqual(
                src.person.factory(
                    # **a_person,
                    first_name=self.random_first_name,
                    last_name=self.random_last_name,
                    sex=self.random_sex,
                    year_of_birth=self.random_year_of_birth,
                ),
                # dict(
                #     **a_person,
                #     age=this_year()-self.random_year_of_birth,
                # )
                self.random_factory_person
            )

  green

* I remove the commented lines and the ``a_person`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 36

        def test_factory_takes_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name=self.random_first_name,
                    last_name=self.random_last_name,
                    sex=self.random_sex,
                    year_of_birth=self.random_year_of_birth,
                ),
                self.random_factory_person
            )

        def test_factory_w_default_arguments(self):

  green again. Do I still need :ref:`test_factory_takes_keyword_arguments`?

----

* I add an :ref:`assertion<what is an assertion?>` with the ``random_factory_person`` :ref:`class attribute<test_attribute_error_w_class_attributes>` to ``test_factory_person_greeting``

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 7-14

            john = src.person.factory(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )

            self.assertEqual(
                src.person.hello(self.random_factory_person),
                (
                    f'Hi, my name is {self.random_first_name} '
                    f'{self.random_last_name} '
                    f'and I am {this_year()-self.random_year_of_birth}'
                )
            )

            for person in (joe, jane, john):

  the test is still green

* I remove the 3 people I made with the ``factory`` :ref:`function<what is a function?>` and the `for loop`_ with the :ref:`assertion<what is an assertion?>` because they are no longer needed, the random person covers all their cases and more

  .. code-block:: python
    :lineno-start: 61

        def test_factory_person_greeting(self):
            self.assertEqual(
                src.person.hello(self.random_factory_person),
                (
                    f'Hi, my name is {self.random_first_name} '
                    f'{self.random_last_name} '
                    f'and I am {this_year()-self.random_year_of_birth}'
                )
            )

        def test_classy_person_greeting(self):

  still

----

* I have to make a random person with the ``Person`` :ref:`class<what is a class?>` to do the same thing for ``test_classy_person_greeting``. I will come back to it

----

* I use the ``random_year_of_birth`` :ref:`class attribute<test_attribute_error_w_class_attributes>` in ``test_update_factory_person_year_of_birth``

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 2-3

        def test_update_factory_person_year_of_birth(self):
            # original_year_of_birth = 1580
            original_year_of_birth = self.random_year_of_birth

  the test is still green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the calculation

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 4-5

        def test_update_factory_person_year_of_birth(self):
            # original_year_of_birth = 1580
            original_year_of_birth = self.random_year_of_birth
            # original_age = this_year() - original_year_of_birth
            original_age = this_year() - self.random_year_of_birth
            new_year_of_birth = 1980

  still green

* I point ``person`` to the ``self.random_factory_person`` :ref:`class attribute<test_attribute_error_w_class_attributes>`

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 3-8

            new_year_of_birth = 1980

            # person = src.person.factory(
            #     first_name='john',
            #     last_name='smith',
            #     year_of_birth=original_year_of_birth,
            # )
            person = self.random_factory_person
            self.assertEqual(

  still green

* I use the ``self.random_factory_person`` :ref:`class attribute<test_attribute_error_w_class_attributes>` in the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 3-4

            person = self.random_factory_person
            self.assertEqual(
                # person.get('age'),
                self.random_factory_person.get('age'),
                original_age
            )

            with self.assertRaises(KeyError):

  still green

* I remove the commented lines and the ``original_year_of_birth`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 99

        def test_update_factory_person_year_of_birth(self):
            original_age = this_year() - self.random_year_of_birth
            new_year_of_birth = 1980

            person = self.random_factory_person
            self.assertEqual(
                self.random_factory_person.get('age'),
                original_age
            )

            with self.assertRaises(KeyError):

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the assertRaises_ block

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 2-3

            with self.assertRaises(KeyError):
                # person['year_of_birth']
                self.random_factory_person['year_of_birth']
            self.assertEqual(

  still green

* I use the ``self.random_factory_person`` :ref:`class attribute<test_attribute_error_w_class_attributes>` in the :ref:`assertion<what is an assertion?>` for the :ref:`setdefault method<test_setdefault_adds_given_key_to_a_dictionary>`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 2-5
    :emphasize-text: ) ,

            self.assertEqual(
                # person.setdefault('year_of_birth', new_year_of_birth),
                self.random_factory_person.setdefault(
                    'year_of_birth', new_year_of_birth
                ),
                new_year_of_birth
            )

  still green

* I use ``self.random_factory_person`` in the second :ref:`assertion<what is an assertion?>` for the age

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 2-3

            self.assertEqual(
                # person.get('age'),
                self.random_factory_person.get('age'),
                original_age
            )

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 109

            with self.assertRaises(KeyError):
                self.random_factory_person['year_of_birth']
            self.assertEqual(
                self.random_factory_person.setdefault(
                    'year_of_birth', new_year_of_birth
                ),
                new_year_of_birth
            )
            self.assertEqual(
                self.random_factory_person.get('age'),
                original_age
            )

  the test is still green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the call to ``src.person.update_year_of_birth`` in the :ref:`assertion<what is an assertion?>` for the ``year_of_birth`` update

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 3-4

            self.assertEqual(
                src.person.update_year_of_birth(
                    # person,
                    self.random_factory_person,
                    new_year_of_birth
                ),

  still green

* I use the other :ref:`class attributes<test_attribute_error_w_class_attributes>` in the expected :ref:`dictionary<what is a dictionary?>` of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 2-7

                dict(
                    # first_name=person.get('first_name'),
                    first_name=self.random_first_name,
                    # last_name=person.get('last_name'),
                    last_name=self.random_last_name,
                    # sex=person.get('sex'),
                    sex=self.random_sex,
                    age=this_year()-new_year_of_birth,
                )

  green

* I remove the commented lines and the ``person`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 99

        def test_update_factory_person_year_of_birth(self):
            original_age = this_year() - self.random_year_of_birth
            new_year_of_birth = 1980

            self.assertEqual(
                self.random_factory_person.get('age'),
                original_age
            )

            with self.assertRaises(KeyError):
                self.random_factory_person['year_of_birth']
            self.assertEqual(
                self.random_factory_person.setdefault(
                    'year_of_birth', new_year_of_birth
                ),
                new_year_of_birth
            )
            self.assertEqual(
                self.random_factory_person.get('age'),
                original_age
            )

            self.assertEqual(
                src.person.update_year_of_birth(
                    self.random_factory_person,
                    new_year_of_birth
                ),
                dict(
                    first_name=self.random_first_name,
                    last_name=self.random_last_name,
                    sex=self.random_sex,
                    age=this_year()-new_year_of_birth,
                )
            )

        def test_update_classy_person_year_of_birth(self):

  still green

----

* ``this_year() - self.random_year_of_birth`` is in the tests a few times. I add a :ref:`class attribute<test_attribute_error_w_class_attributes>` for it in the `setUp method`_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 5

        def setUp(self):
            self.random_year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            self.original_age = this_year() - self.random_year_of_birth
            self.random_first_name = choose(*self.RANDOM_NAMES)
            self.random_last_name = choose(*self.RANDOM_NAMES)

* I use the new :ref:`class attribute<test_attribute_error_w_class_attributes>` in :ref:`test_factory_w_default_arguments`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 5-6

                dict(
                    first_name=self.random_first_name,
                    last_name='doe',
                    sex='M',
                    # age=this_year()-self.random_year_of_birth,
                    age=self.original_age,
                )

  the test is still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 48

        def test_factory_w_default_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name=self.random_first_name,
                    year_of_birth=self.random_year_of_birth,
                ),
                dict(
                    first_name=self.random_first_name,
                    last_name='doe',
                    sex='M',
                    age=self.original_age,
                )
            )

        def test_factory_person_greeting(self):

  green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in ``test_factory_person_greeting``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 4-5

                (
                    f'Hi, my name is {self.random_first_name} '
                    f'{self.random_last_name} '
                    # f'and I am {this_year()-self.random_year_of_birth}'
                    f'and I am {self.original_age}'
                )

  the test is still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 62

        def test_factory_person_greeting(self):
            self.assertEqual(
                src.person.hello(self.random_factory_person),
                (
                    f'Hi, my name is {self.random_first_name} '
                    f'{self.random_last_name} '
                    f'and I am {self.original_age}'
                )
            )

        def test_classy_person_greeting(self):

  still green

* I use ``self.original_age`` in ``test_update_factory_person_year_of_birth``

  .. code-block:: python
    :lineno-start: 100
    :emphasize-lines: 2-3

        def test_update_factory_person_year_of_birth(self):
            # original_age = this_year() - self.random_year_of_birth
            original_age = self.original_age
            new_year_of_birth = 1980

  the test is still green

* I use ``self.original_age`` in the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 5-6

            new_year_of_birth = 1980

            self.assertEqual(
                self.random_factory_person.get('age'),
                # original_age
                self.original_age
            )

  green

* I use it in the second :ref:`assertion<what is an assertion?>` for the age

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 9-10

            self.assertEqual(
                self.random_factory_person.setdefault(
                    'year_of_birth', new_year_of_birth
                ),
                new_year_of_birth
            )
            self.assertEqual(
                self.random_factory_person.get('age'),
                # original_age
                self.original_age
            )

            self.assertEqual(

  still green

* I remove the commented line and the ``original_age`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 100

        def test_update_factory_person_year_of_birth(self):
            new_year_of_birth = 1980

            self.assertEqual(
                self.random_factory_person.get('age'),
                self.original_age
            )

            with self.assertRaises(KeyError):
                self.random_factory_person['year_of_birth']
            self.assertEqual(
                self.random_factory_person.setdefault(
                    'year_of_birth', new_year_of_birth
                ),
                new_year_of_birth
            )
            self.assertEqual(
                self.random_factory_person.get('age'),
                self.original_age
            )

            self.assertEqual(
                src.person.update_year_of_birth(
                    self.random_factory_person,
                    new_year_of_birth
                ),
                dict(
                    first_name=self.random_first_name,
                    last_name=self.random_last_name,
                    sex=self.random_sex,
                    age=this_year()-new_year_of_birth,
                )
            )

        def test_update_classy_person_year_of_birth(self):

----

* I add a random person made with the ``Person`` :ref:`class<what is a class?>` to the `setUp method`_

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 7-12

            self.random_factory_person = src.person.factory(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                sex=self.random_sex,
                year_of_birth=self.random_year_of_birth,
            )
            self.random_classy_person = src.person.Person(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                sex=self.random_sex,
                year_of_birth=self.random_year_of_birth,
            )

        def test_factory_takes_keyword_arguments(self):

* I add an :ref:`assertion<what is an assertion?>` with the new :ref:`class attribute<test_attribute_error_w_class_attributes>` to ``test_classy_person_greeting``

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 7-14

            john = src.person.Person(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )

            self.assertEqual(
                self.random_classy_person.hello(),
                (
                    f'Hi, my name is {self.random_first_name} '
                    f'{self.random_last_name} '
                    f'and I am {self.original_age}'
                )
            )

            for person in (joe, jane, john):

  still green

* I remove the 3 people I made with the ``Person`` :ref:`class<what is a class?>` and the `for loop`_ with its :ref:`assertion<what is an assertion?>` because they are no longer needed, the random person covers those cases and more

  .. code-block:: python
    :lineno-start: 78

        def test_classy_person_greeting(self):
            self.assertEqual(
                self.random_classy_person.hello(),
                (
                    f'Hi, my name is {self.random_first_name} '
                    f'{self.random_last_name} '
                    f'and I am {self.original_age}'
                )
            )

        def test_update_factory_person_year_of_birth(self):

  still green

* the expected message in ``test_classy_person_greeting`` and ``test_factory_person_greeting`` are now the same. I add a :ref:`method<what is a function?>` to remove the repetition

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 9-14

                dict(
                    first_name=self.random_first_name,
                    last_name='doe',
                    sex='M',
                    age=self.original_age
                )
            )

        def expected_greeting(self):
            return (
                f'Hi, my name is {self.random_first_name} '
                f'{self.random_last_name} '
                f'and I am {self.original_age}'
            )

        def test_factory_person_greeting(self):

* I use the new :ref:`method<what is a function?>` in ``test_factory_person_greeting``

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 4-9

        def test_factory_person_greeting(self):
            self.assertEqual(
                src.person.hello(self.random_factory_person),
                # (
                #     f'Hi, my name is {self.random_first_name} '
                #     f'{self.random_last_name} '
                #     f'and I am {self.original_age}'
                # )
                self.expected_greeting()
            )

        def test_classy_person_greeting(self):

  the test is still green

* I use it in ``test_classy_person_greeting``

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 4-9

        def test_classy_person_greeting(self):
            self.assertEqual(
                self.random_classy_person.hello(),
                # (
                #     f'Hi, my name is {self.random_first_name} '
                #     f'{self.random_last_name} '
                #     f'and I am {self.original_age}'
                # )
                self.expected_greeting()
            )

        def test_update_factory_person_year_of_birth(self):

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 68

        def expected_greeting(self):
            return (
                f'Hi, my name is {self.random_first_name} '
                f'{self.random_last_name} '
                f'and I am {self.original_age}'
            )

        def test_factory_person_greeting(self):
            self.assertEqual(
                src.person.hello(self.random_factory_person),
                self.expected_greeting()
            )

        def test_classy_person_greeting(self):
            self.assertEqual(
                self.random_classy_person.hello(),
                self.expected_greeting()
            )

        def test_update_factory_person_year_of_birth(self):

  green

* I use the ``random_classy_person`` :ref:`class attribute<test_attribute_error_w_class_attributes>` in ``test_update_classy_person_year_of_birth``

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 2-7

        def test_update_classy_person_year_of_birth(self):
            # person = src.person.Person(
            #     first_name='john',
            #     last_name='smith',
            #     year_of_birth=1580,
            # )
            person = self.random_classy_person
            self.assertEqual(person.get_age(), 446)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: X != 446

* I use ``self.original_age`` in the first :ref:`assertion<what is an assertion?>` for the age

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 2-3

            person = self.random_classy_person
            # self.assertEqual(person.get_age(), 446)
            self.assertEqual(person.get_age(), self.original_age)

            new_year_of_birth = 1980

  the test is green again

* I remove the commented lines then use ``self.random_classy_person`` in the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 3-7

        def test_update_classy_person_year_of_birth(self):
            person = self.random_classy_person
            self.assertEqual(
                # person.get_age(),
                self.random_classy_person.get_age(),
                self.original_age
            )

            new_year_of_birth = 1980

  the test is still green

* I use the new year of birth as the value for the ``year_of_birth`` :ref:`attribute<test_attribute_error_w_class_attributes>` of ``self.random_classy_person``

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 2-3

            new_year_of_birth = 1980
            # person.year_of_birth = new_year_of_birth
            self.random_classy_person.year_of_birth = new_year_of_birth
            self.assertEqual(
                person.get_age(),
                this_year()-new_year_of_birth
            )

  green

* I use ``self.random_classy_person`` in the second :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 5-6

            new_year_of_birth = 1980
            # person.year_of_birth = new_year_of_birth
            self.random_classy_person.year_of_birth = new_year_of_birth
            self.assertEqual(
                # person.get_age(),
                self.random_classy_person.get_age(),
                this_year()-new_year_of_birth
            )


    # Exceptions seen

  the test is still green

* I remove the commented lines and the ``person`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 121

        def test_update_classy_person_year_of_birth(self):
            self.assertEqual(
                self.random_classy_person.get_age(),
                self.original_age
            )

            new_year_of_birth = 1980
            self.random_classy_person.year_of_birth = new_year_of_birth
            self.assertEqual(
                self.random_classy_person.get_age(),
                this_year()-new_year_of_birth
            )


    # Exceptions seen

  still green

----

* the ``new_year_of_birth`` :ref:`variable<what is a variable?>` is the same in ``test_update_factory_person_year_of_birth`` and ``test_update_classy_person_year_of_birth``. I add a new :ref:`class attribute<test_attribute_error_w_class_attributes>` to the `setUp method`_ because I want to use random numbers for it

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 5-7

        def setUp(self):
            self.random_year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            self.random_new_year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            self.original_age = this_year() - self.random_year_of_birth

  this is also doing the same thing two times, even though the results are different

* I make a :ref:`function<what is a function?>` to remove the repetition

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 5-8

    def this_year():
        return datetime.datetime.now().year


    def random_year_of_birth():
        return random.randint(
            this_year()-120, this_year()
        )


    class TestPerson(unittest.TestCase):

* I point ``self.random_year_of_birth`` to the result of calling the new :ref:`function<what is a function?>` in the `setUp method`_

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 2-5

        def setUp(self):
            # self.random_year_of_birth = random.randint(
            #     this_year()-120, this_year()
            # )
            self.random_year_of_birth = random_year_of_birth()
            self.random_new_year_of_birth = random.randint(

  the test is still green

* I call the :ref:`function<what is a function?>` for the ``new_year_of_birth`` :ref:`attribute<test_attribute_error_w_class_attributes>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 5-9

        def setUp(self):
            # self.random_year_of_birth = random.randint(
            #     this_year()-120, this_year()
            # )
            self.random_year_of_birth = random_year_of_birth()
            # self.random_new_year_of_birth = random.randint(
            #     this_year()-120, this_year()
            # )
            self.random_new_year_of_birth = random_year_of_birth()
            self.original_age = this_year() - self.random_year_of_birth

  green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 28

        def setUp(self):
            self.random_year_of_birth = random_year_of_birth()
            self.random_new_year_of_birth = random_year_of_birth()
            self.original_age = this_year() - self.random_year_of_birth
            self.random_first_name = choose(*self.RANDOM_NAMES)

* I use ``self.random_new_year_of_birth`` in ``test_update_factory_person_year_of_birth``

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 2-3

        def test_update_factory_person_year_of_birth(self):
            # new_year_of_birth = 1980
            new_year_of_birth = self.random_new_year_of_birth

  still green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the :ref:`assertion<what is an assertion?>` for the call to the :ref:`setdefault method<test_setdefault_adds_given_key_to_a_dictionary>`

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 3-4

            self.assertEqual(
                self.random_factory_person.setdefault(
                    # 'year_of_birth', new_year_of_birth
                    'year_of_birth', self.random_new_year_of_birth
                ),
                new_year_of_birth
            )

  the test is still green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` as the expectation of the :ref:`assertion<what is an assertion?>` for the call to the :ref:`setdefault method<test_setdefault_adds_given_key_to_a_dictionary>`

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 6-7

            self.assertEqual(
                self.random_factory_person.setdefault(
                    # 'year_of_birth', new_year_of_birth
                    'year_of_birth', self.random_new_year_of_birth
                ),
                # new_year_of_birth
                self.random_new_year_of_birth
            )

  still green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the call to ``src.person.update_year_of_birth``

  .. code-block:: python
    :lineno-start: 116
    :emphasize-lines: 4-5

            self.assertEqual(
                src.person.update_year_of_birth(
                    self.random_factory_person,
                    # new_year_of_birth
                    self.random_new_year_of_birth
                ),

  still green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the calculation for the new age

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 5-6

                dict(
                    first_name=self.random_first_name,
                    last_name=self.random_last_name,
                    sex=self.random_sex,
                    # age=this_year()-new_year_of_birth,
                    age=this_year()-self.random_new_year_of_birth,
                )

  the test is still green

* I remove the commented lines and the ``new_year_of_birth`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 92

        def test_update_factory_person_year_of_birth(self):
            self.assertEqual(
                self.random_factory_person.get('age'),
                self.original_age
            )

            with self.assertRaises(KeyError):
                self.random_factory_person['year_of_birth']
            self.assertEqual(
                self.random_factory_person.setdefault(
                    'year_of_birth', self.random_new_year_of_birth
                ),
                self.random_new_year_of_birth
            )
            self.assertEqual(
                self.random_factory_person.get('age'),
                self.original_age
            )

            self.assertEqual(
                src.person.update_year_of_birth(
                    self.random_factory_person,
                    self.random_new_year_of_birth
                ),
                dict(
                    first_name=self.random_first_name,
                    last_name=self.random_last_name,
                    sex=self.random_sex,
                    age=this_year()-self.random_new_year_of_birth,
                )
            )

        def test_update_classy_person_year_of_birth(self):

  green around the rosie, a pocket full of posies

* on to ``test_update_classy_person_year_of_birth``. I point the ``new_year_of_birth`` :ref:`variable<what is a variable?>` to the :ref:`class attribute<test_attribute_error_w_class_attributes>`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 7-8

        def test_update_classy_person_year_of_birth(self):
            self.assertEqual(
                self.random_classy_person.get_age(),
                self.original_age
            )

            # new_year_of_birth = 1980
            new_year_of_birth = self.random_new_year_of_birth
            self.random_classy_person.year_of_birth = new_year_of_birth

  the test is still green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the assignment of the new value

  .. code-block:: python
    :lineno-start: 130
    :emphasize-lines: 3-4

            # new_year_of_birth = 1980
            new_year_of_birth = self.random_new_year_of_birth
            # self.random_classy_person.year_of_birth = new_year_of_birth
            self.random_classy_person.year_of_birth = self.random_new_year_of_birth
            self.assertEqual(

  still green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 130
    :emphasize-lines: 7-8

            # new_year_of_birth = 1980
            new_year_of_birth = self.random_new_year_of_birth
            # self.random_classy_person.year_of_birth = new_year_of_birth
            self.random_classy_person.year_of_birth = self.random_new_year_of_birth
            self.assertEqual(
                self.random_classy_person.get_age(),
                # this_year()-new_year_of_birth
                this_year()-self.random_new_year_of_birth
            )


  green

* I remove the commented lines and the ``new_year_of_birth`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 124

        def test_update_classy_person_year_of_birth(self):
            self.assertEqual(
                self.random_classy_person.get_age(),
                self.original_age
            )

            self.random_classy_person.year_of_birth = self.random_new_year_of_birth
            self.assertEqual(
                self.random_classy_person.get_age(),
                this_year()-self.random_new_year_of_birth
            )


    # Exceptions seen

  the test is still green

----

* There are two calculations that happen in the tests, one for the new age and another for the original age

  .. code-block:: python

    this_year() - self.random_year_of_birth
    this_year() - self.random_new_year_of_birth

  I add a :ref:`function<what is a function?>` that does the calculation to ``test_person.py``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 7-8

    def random_year_of_birth():
        return random.randint(
            this_year()-120, this_year()
        )


    def get_age(year_of_birth):
        return this_year() - year_of_birth


    class TestPerson(unittest.TestCase):

* I point ``self.original_age`` in the `setUp method`_ to the result of calling the :ref:`function<what is a function?>` with ``self.random_year_of_birth``

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 4-5

        def setUp(self):
            self.random_year_of_birth = random_year_of_birth()
            self.random_new_year_of_birth = random_year_of_birth()
            # self.original_age = this_year() - self.random_year_of_birth
            self.original_age = get_age(self.random_year_of_birth)
            self.random_first_name = choose(*self.RANDOM_NAMES)

  the test is still green

* I remove the commented line then add a new :ref:`class attribute<test_attribute_error_w_class_attributes>` for the calculation of the new age

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 5

        def setUp(self):
            self.random_year_of_birth = random_year_of_birth()
            self.random_new_year_of_birth = random_year_of_birth()
            self.original_age = get_age(self.random_year_of_birth)
            self.new_age = get_age(self.random_new_year_of_birth)
            self.random_first_name = choose(*self.RANDOM_NAMES)


* I use the new :ref:`class attribute<test_attribute_error_w_class_attributes>` in ``test_update_factory_person_year_of_birth``

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 5-6

                dict(
                    first_name=self.random_first_name,
                    last_name=self.random_last_name,
                    sex=self.random_sex,
                    # age=this_year()-self.random_new_year_of_birth,
                    age=self.new_age,
                )

  the test is still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 97

        def test_update_factory_person_year_of_birth(self):
            self.assertEqual(
                self.random_factory_person.get('age'),
                self.original_age
            )

            with self.assertRaises(KeyError):
                self.random_factory_person['year_of_birth']
            self.assertEqual(
                self.random_factory_person.setdefault(
                    'year_of_birth', self.random_new_year_of_birth
                ),
                self.random_new_year_of_birth
            )
            self.assertEqual(
                self.random_factory_person.get('age'),
                self.original_age
            )

            self.assertEqual(
                src.person.update_year_of_birth(
                    self.random_factory_person,
                    self.random_new_year_of_birth
                ),
                dict(
                    first_name=self.random_first_name,
                    last_name=self.random_last_name,
                    sex=self.random_sex,
                    age=self.new_age,
                )
            )

        def test_update_classy_person_year_of_birth(self):

  green

* use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in ``test_update_classy_person_year_of_birth``

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 3-4

            self.assertEqual(
                self.random_classy_person.get_age(),
                # this_year()-self.random_new_year_of_birth
                self.new_age
            )

  still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 129

        def test_update_classy_person_year_of_birth(self):
            self.assertEqual(
                self.random_classy_person.get_age(),
                self.original_age
            )

            self.random_classy_person.year_of_birth = self.random_new_year_of_birth
            self.assertEqual(
                self.random_classy_person.get_age(),
                self.new_age
            )


    # Exceptions seen


I wonder what red and yellow look like, that was a lot of green.

----

*********************************************************************************
test_class_w_default_arguments
*********************************************************************************



In :ref:`test_factory_w_default_arguments`, I tested what happens when I call the ``factory`` :ref:`function<what is a function?>` without giving a value for ``last_name`` and ``sex``.

In those cases the :ref:`functions<what is a function?>` uses default values of ``'doe'`` for ``last_name`` and ``'M'`` for ``sex``.

I want to add a test for the ``Person`` :ref:`class<what is a class?>` to make sure it does the same thing when I do not provide a value for ``last_name`` or ``sex`` when making a person.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a new test with a person made with the ``Person`` :ref:`class<what is a class?>` without a value for ``last_name`` and ``sex`` and an :ref:`assertion<what is an assertion?>` for the value of the ``last_name``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 9-14

                dict(
                    first_name=self.random_first_name,
                    last_name='doe',
                    sex='M',
                    age=self.original_age
                )
            )

        def test_class_w_default_arguments(self):
            person = src.person.Person(
                first_name=self.random_first_name,
                year_of_birth=self.random_year_of_birth,
            )
            self.assertEqual(person.first_name, None)

        def expected_greeting(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: X != None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` for ``random_first_name`` to make the expectation match

.. code-block:: python
  :lineno-start: 83
  :emphasize-lines: 1

            self.assertEqual(person.first_name, self.random_first_name)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the value of the ``last_name``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2

            self.assertEqual(person.first_name, self.random_first_name)
            self.assertEqual(person.last_name, 'doe')

        def expected_greeting(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'doe'

* I change the default value for ``last_name`` in the ``__init__`` :ref:`method<what is a function?>` of the ``Person`` :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4

    class Person:

        def __init__(
                self, first_name, last_name='doe',
                year_of_birth=None, sex=None,
            ):

  the test passes

----

* I add another :ref:`assertion<what is an assertion?>` for the value of ``sex`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 3

            self.assertEqual(person.first_name, self.random_first_name)
            self.assertEqual(person.last_name, 'doe')
            self.assertEqual(person.sex, 'M')

        def expected_greeting(self):

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'sex'

* I add the :ref:`class attribute<test_attribute_error_w_class_attributes>` to the ``__init__`` :ref:`method<what is a function?>` of the ``Person`` :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 8

        def __init__(
                self, first_name, last_name='doe',
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            self.sex = sex
            return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'M'

* I change the default value for ``sex``

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 2

        def __init__(
                self, first_name, last_name='doe',
                year_of_birth=None, sex='M',
            ):

  the test passes

----

There is a problem with the ``year_of_birth``, its default value is :ref:`None<what is None?>`, which means if I do not give a value for it when I make a person with the ``factory`` :ref:`function<what is a function?>` or ``Person`` :ref:`class<what is a class?>`, :ref:`TypeError<what causes TypeError?>` will be raised.

* I remove ``year_of_birth`` from the call to the ``Person`` class in ``test_class_w_default_arguments`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 78

        def test_class_w_default_arguments(self):
            person = src.person.Person(
                first_name=self.random_first_name,
                # year_of_birth=self.random_year_of_birth,
            )

  the test is still green

* I remove the commented line then add an :ref:`assertion<what is an assertion?>` for the age

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 2, 6

        def test_class_w_default_arguments(self):
            person = src.person.Person(self.random_first_name)
            self.assertEqual(person.first_name, self.random_first_name)
            self.assertEqual(person.last_name, 'doe')
            self.assertEqual(person.sex, 'M')
            self.assertEqual(person.get_age(), None)

        def expected_greeting(self):

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'

  because the ``get_age`` :ref:`method<what is a function?>` tries to subtract ``year_of_birth`` from this year, and ``year_of_birth`` is :ref:`None<what is None?>`

* I add a default value for ``year_of_birth`` in the ``__init__`` :ref:`method<what is a function?>` of the ``Person`` :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3

        def __init__(
                self, first_name, last_name='doe',
                year_of_birth=this_year(), sex='M',
            ):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 != None

* I change the expectation in ``test_person.py``

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 2

            self.assertEqual(person.sex, 'M')
            self.assertEqual(person.get_age(), 0)

        def expected_greeting(self):

  the test passes

----

* I remove the value for ``year_of_birth`` in the call to ``src.person.factory`` in :ref:`test_factory_w_default_arguments`

  .. code-block:: python
    :lineno-start: 64

        def test_factory_w_default_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name=self.random_first_name,
                    # year_of_birth=self.random_year_of_birth,
                ),

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() missing 1 required positional argument: 'year_of_birth'

* I add a default value for ``year_of_birth`` to make it a choice in the ``factory`` :ref:`function<what is a function?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2

    def factory(
            first_name, year_of_birth=None,
            last_name='doe', sex='M',
        ):

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'

* I change the default value for ``year_of_birth`` to this year

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2

    def factory(
            first_name, year_of_birth=this_year(),
            last_name='doe', sex='M',
        ):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 5

    E       - {'age': 0, 'first_name': Y, 'last_name': 'doe', 'sex': 'M'}
    E       ?         ^
    E
    E       + {'age': X, 'first_name': Y, 'last_name': 'doe', 'sex': 'M'}
    E       ?         ^

* I change the expectation in :ref:`test_factory_w_default_arguments` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 5-6

                dict(
                    first_name=self.random_first_name,
                    last_name='doe',
                    sex='M',
                    # age=self.original_age
                    age=0
                )

  the test passes

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 64

        def test_factory_w_default_arguments(self):
            self.assertEqual(
                src.person.factory(self.random_first_name),
                dict(
                    first_name=self.random_first_name,
                    last_name='doe',
                    sex='M',
                    age=0
                )
            )

        def test_class_w_default_arguments(self):

  the tests are still green

----

The tests so far have a problem, they check that the input and the output are the same, with no checks for what type of input it is. This means I can use a :ref:`data type<data structures>` that is not a string_ for ``first_name`` and ``last_name`` and ``sex`` and the tests would still pass. I would only get :ref:`TypeError<what causes TypeError?>` when I use a value for ``year_of_birth`` that is not a number, though if I use a :ref:`boolean<what are booleans?>`, the calculation would still work.

You know enough to add tests for these problems, to make sure that the right inputs are always used. Send me your solutions when you do, I would love to see them.

----

*********************************************************************************
test_attributes_and_methods_of_classes
*********************************************************************************


I used the `dir built-in function`_ in :ref:`lists<what is a list?>` and :ref:`dictionaries<what is a dictionary?>` to show their :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a function?>`. I can also use it with the ``Person`` :ref:`class<what is a class?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test

.. code-block:: python
  :lineno-start: 140
  :emphasize-lines: 6-10

            self.assertEqual(
                self.random_classy_person.get_age(),
                self.new_age
            )

        def test_attributes_and_methods_of_a_class(self):
            self.assertEqual(
                dir(src.person.Person),
                []
            )


    # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: Lists differ: ['__class__', '__delattr__', '__dict__', '[377 chars]llo'] != []

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I copy and paste the values from the terminal_ and remove the extra characters I do not need with the ``find and replace`` feature of the `Integrated Development Environment (IDE)`_

.. code-block:: python
  :lineno-start: 145
  :emphasize-lines: 4-36

        def test_attributes_and_methods_of_a_class(self):
            self.assertEqual(
                dir(src.person.Person),
                [
                    '__class__',
                    '__delattr__',
                    '__dict__',
                    '__dir__',
                    '__doc__',
                    '__eq__',
                    '__firstlineno__',
                    '__format__',
                    '__ge__',
                    '__getattribute__',
                    '__getstate__',
                    '__gt__',
                    '__hash__',
                    '__init__',
                    '__init_subclass__',
                    '__le__',
                    '__lt__',
                    '__module__',
                    '__ne__',
                    '__new__',
                    '__reduce__',
                    '__reduce_ex__',
                    '__repr__',
                    '__setattr__',
                    '__sizeof__',
                    '__static_attributes__',
                    '__str__',
                    '__subclasshook__',
                    '__weakref__',
                    'get_age',
                    'hello'
                ]
            )


    # Exceptions seen

  the test passes

The attributes I defined in the ``__init__`` :ref:`method<what is a function?>` are not in the list, because I called dir_ on ``src.person.Person`` which is the :ref:`class<what is a class?>` definition, not on an instance (copy) of the class where I would have to provide values for the ``first_name``, ``last_name``, ``sex`` and ``year_of_birth`` :ref:`attributes<test_attribute_error_w_class_attributes>`.

What is the difference between ``dir(src.person.Person)`` and ``dir(src.person.Person('jane'))``?

The 3 :ref:`methods<what is a function?>` I defined in the ``Person`` :ref:`class<what is a class?>` in ``person.py``

* __init__
* get_age
* hello

are in the list, and there are others which I never defined, which leads to the question of :ref:`where did they come from?<family ties>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_person.py`` and ``person.py`` in the :ref:`editors<2 editors>`
* I click in the terminal_ and use :kbd:`ctrl+c` on the keyboard to leave the tests
* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/person

* I `change directory`_ to the parent of ``person``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<classes: tests and solutions>`

----

*************************************************************************************
review
*************************************************************************************

* A :ref:`class<what is a class?>` is :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a function?>` that belong together
* A :ref:`class<what is a class?>` can be used to represent something
* classes_ can be an easier way to manage data than :ref:`functions<what is a function?>`
* classes_ make it easier to write tests for something

.. TIP::

  * when I find myself writing or doing the same thing two times, I write a :ref:`function<what is a function?>`
  * when I find I have two :ref:`functions<what is a function?>` that use the same information, I write a :ref:`class<what is a class?>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have gone through a lot of things and know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<list comprehensions>`
* :ref:`what you can do with dictionaries<dictionaries>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`what you can do with classes<what is a class?>`

:ref:`Would you like to know where the extra attributes and methods of the Person class came from?<family ties>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->