.. include:: ../links.rst

.. _constructor: https://grokipedia.com/page/Constructor_(object-oriented_programming)
.. _constructor method: constructor_

#################################################################################
classes
#################################################################################

I made a :ref:`functions<what is a function?>` that make :ref:`dictionaries<what is a dictionary?>` and strings_ in :ref:`how to make a person`. I can also do the same thing with a :ref:`class<what is a class?>` since it is a group of :ref:`attributes (variables)<what causes AttributeError?>` and :ref:`methods (functions) <what is a function?>` that belong together.

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/tests/test_person_classes.py
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

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows

  .. code-block:: python
    :emphasize-lines: 5

    rootdir: .../pumping_python/person
    configfile: pyproject.toml
    collected 3 items

    tests/test_person.py ...                              [100%]

    ==================== 3 passed in X.YZs =====================

* I hold :kbd:`ctrl` on the keyboard, then click on ``tests/test_person.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_classy_person_says_hello
*********************************************************************************

I made a person say hello with a :ref:`function<what is a function?>`. How would I do that with a :ref:`class?<what is a class?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to ``test_person.py``

.. code-block:: python
  :lineno-start: 81
  :emphasize-lines: 8-13, 15-19

            reality = src.person.say_hello(a_random_person)
            my_expectation = (
                f'Hi, my name is {first_name} {last_name}'
                f' and I am {calculate_age(year_of_birth)}'
            )
            self.assertEqual(reality, my_expectation)

        def test_classy_person_says_hello(self):
            joe = src.person.Person(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )

            reality = src.person.say_hello(joe)
            my_expectation = (
                'Hi, my name is joe blow and I am 30'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.person' has no attribute 'Person'

because there is no definition for ``Person`` in ``person.py`` in the ``src`` folder_

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`class<what is a class?>` to ``person.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 16, 18

    def factory(
            first_name, year_of_birth,
            last_name='doe', sex='M',
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': (
                datetime.datetime.today().year
               -year_of_birth
            ),
        }


    class Person:

        pass

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person() takes no arguments

  because :ref:`classes<what is a class?>` do not take arguments like a :ref:`function<what is a function?>` without a :ref:`method<what is a method?>` that handles those arguments

* I add a `constructor method`_ to the ``Person`` :ref:`class<what is a class?>` so it can take arguments

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3-4

    class Person:

        def __init__():
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() got an
        unexpected keyword argument 'first_name'

  - because the :ref:`definition<how to make a function>` for ``__init__`` does not allow calling it with inputs (the parentheses are empty) and the test sends ``'first_name'`` as input.
  - a `constructor method`_ is used to make copies of a :ref:`class<what is a class?>`

* I add the name in parentheses so that the ``__init__`` `constructor method`_ can take input

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3

    class Person:

        def __init__(first_name):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() got
        multiple values for argument 'first_name'

  because the ``__init__`` `constructor method`_ takes the :ref:`class<what is a class?>` it belongs to as the first argument

* I add ``self`` as the first argument the way I do with all the test :ref:`methods<what is a method?>` in the book

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3

    class Person:

        def __init__(self, first_name):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError:
        Person.__init__() got
        an unexpected keyword argument 'last_name'.
        Did you mean 'first_name'?

  I have seen this before, so far it is the same as making the ``factory`` :ref:`function<what is a function?>`

* I add ``last_name`` to the :ref:`definition<how to make a function>` of ``__init__``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 1

        def __init__(self, first_name, last_name):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() got
        an unexpected keyword argument 'year_of_birth'

  still the same as making the ``factory`` :ref:`function<what is a function?>`

* I add ``year_of_birth`` to the definition of the ``__init__`` :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3-6

    class Person:

        def __init__(
                self, first_name, last_name,
                year_of_birth,
            ):
            return

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'get'

  because the test calls the ``say_hello`` :ref:`function<what is a function?>` expects a :ref:`dictionary<what is a dictionary?>` and calls the :ref:`get method<test_get_value_of_a_key_in_a_dictionary>` on it. The ``Person`` :ref:`object<what is a class?>` does not have a :ref:`get method<test_get_value_of_a_key_in_a_dictionary>`. I can call :ref:`methods<what is a method?>` from outside the :ref:`class<what is a class?>` they belong to.

* I change ``reality`` in :ref:`test_classy_person_says_hello` to use a :ref:`method<what is a method?>` that belongs to ``Person``, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 8-9

        def test_classy_person_says_hello(self):
            joe = src.person.Person(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )

            # reality = src.person.say_hello(joe)
            reality = joe.say_hello(joe)
            my_expectation = (
                'Hi, my name is joe blow and I am 30'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'say_hello'

  because the test calls the ``say_hello`` :ref:`function<what is a function?>` which does not yet exist in the ``Person`` :ref:`class<what is a class?>`

* I add a :ref:`method definition<how to make a function>` for it in ``person.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 9-10

    class Person:

        def __init__(
                self, first_name, last_name,
                year_of_birth,
            ):
            return None

        def say_hello():
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.say_hello() takes 0 positional arguments
        but 2 were given

  because the :ref:`definition<how to make a function>` for ``say_hello`` does not allow inputs and the test called the :ref:`method<what is a method?>` with a :ref:`positional argument<test_functions_w_positional_arguments>` (``person``) and the error says 2 were given

* I add ``person`` to the :ref:`method definition<how to make a function>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 9

    class Person:

        def __init__(
                self, first_name, last_name,
                year_of_birth,
            ):
            return None

        def say_hello(person):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.get() takes 1 positional argument but 2 were given

  because :ref:`methods<what is a method?>` take the :ref:`class<what is a class?>` they belong to as the first argument.

* I can also add the `staticmethod decorator`_ if I do not want to add ``self`` to the :ref:`method definition<how to make a function>` because it does not use anything in the :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 9

    class Person:

        def __init__(
                self, first_name, last_name,
                year_of_birth,
            ):
            return None

        @staticmethod
        def say_hello(person):
            return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'Hi, my name is joe blow and I am 30'

  because the ``say_hello`` :ref:`method<what is a method?>` of the ``Person`` :ref:`class<what is a class?>` returns :ref:`None<what is None?>` and the test expects a string_. Progress!

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 3

        @staticmethod
        def say_hello(person):
            return 'Hi, my name is joe blow and I am 30'

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next person to :ref:`test_classy_person_says_hello` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 7-11

        def test_classy_person_says_hello(self):
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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() missing 1 required positional argument: 'sex'

  I did not provide a value for ``sex`` when I made ``joe``, and the ``factory`` :ref:`function<what is a function?>` has a default value of ``'M'`` for it

* I add a default value for ``sex`` in the  ``__init__`` :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 3

        def __init__(
                self, first_name, last_name,
                year_of_birth, sex=None,
            ):
            return None

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  :ref:`parameters without default values must come before parameters with default values<test_functions_w_positional_and_keyword_args>`

* I add a default value for ``year_of_birth``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 3

    def __init__(
            self, first_name, last_name=None,
            year_of_birth=None, sex=None,
        ):
        return None

  the test passes.

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

  the test is still green.

* I copy the :ref:`for loop<what is a for loop?>` with the :ref:`assertion<what is an assertion?>` from :ref:`test_factory_person_says_hello` and paste it in :ref:`test_classy_person_says_hello`

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
                        src.person.say_hello(person),
                        (
                            f'Hi, my name is {person.get("first_name")} '
                            f'{person.get("last_name")} '
                            f'and I am {person.get("age")}'
                        )
                    )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'get'

  the ``Person`` :ref:`class<what is a class?>` does not have a :ref:`method<what is a method?>` named ``get``

* I can use :ref:`class attributes<test_attribute_error_w_class_attributes>` directly with no need for a ``get`` :ref:`method<what is a method?>`. I change the line for the `subTest method`_

  .. code-block:: python
    :lineno-start: 100
    :emphasize-lines: 2

            for person in (joe, jane, john):
                with self.subTest(name=person.first_name):
                    self.assertEqual(

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'first_name'

* I add a :ref:`class attribute<test_attribute_error_w_class_attributes>` to the ``__init__`` :ref:`method<what is a method?>` of the ``Person`` :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 5

        def __init__(
                self, first_name, last_name=None,
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            return None

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'get'

  the test calls the ``say_hello`` :ref:`function<what is a function?>` which takes in a :ref:`dictionary<what is a dictionary?>` and calls the :ref:`get method<test_get_value_of_a_key_in_a_dictionary>`, the ``Person`` object_ does not have a :ref:`get method<test_get_value_of_a_key_in_a_dictionary>`

* I can call :ref:`methods<what is a method?>` from outside a :ref:`class<what is a class?>` the way I use a :ref:`class attribute<test_attribute_error_w_class_attributes>`. I change the call in the :ref:`assertion<what is an assertion?>` in ``test_person.py``

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

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'hello'

* I add the :ref:`method<what is a method?>` to the ``Person`` :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 8-9

        def __init__(
                self, first_name, last_name=None,
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            return None

        def say_hello():
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.hello() takes 0 positional arguments but 2 were given

  the test calls the :ref:`method<what is a method?>` with one input and the definition takes no input

* I add the `staticmethod decorator`_ to the :ref:`method<what is a method?>` because it does not use anything in the :ref:`class<what is a class?>`

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
        def say_hello():
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.hello() takes 0 positional arguments
               but 1 was given

* I add a name to the definition

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

        @staticmethod
        def say_hello(person):
            return None

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'get'

* I change the :ref:`assertion<what is an assertion?>` in :ref:`test_classy_person_says_hello` in ``test_person.py`` to use the ``first_name`` :ref:`class attribute<test_attribute_error_w_class_attributes>`

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

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

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

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: 'Person' object has no attribute 'last_name'. Did you mean: 'first_name'?

* I add a :ref:`class attribute<test_attribute_error_w_class_attributes>` for ``last_name`` to the ``__init__`` :ref:`method<what is a method?>` of the ``Person`` :ref:`class<what is a class?>` in ``person.py``

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
        def say_hello(person):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'get'

* I want to use a :ref:`method<what is a method?>` to calculate the age. I change the :ref:`assertion<what is an assertion?>` in ``test_person.py``

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

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'get_age'

* I add the :ref:`method<what is a method?>` to the ``Person`` :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 5-6


        @staticmethod
        def say_hello(person):
            return None

        def get_age():
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.get_age() takes 0 positional arguments
               but 1 was given

* I add the `staticmethod decorator`_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 5-7

        @staticmethod
        def say_hello(person):
            return None

        @staticmethod
        def get_age():
            return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'Hi, my name is john smith and I am None'

* I copy and paste the string_ in the `return statement`_ of the ``say_hello`` :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 3

        @staticmethod
        def say_hello(person):
            return 'Hi, my name is john smith and I am None'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 4

    E               - Hi, my name is john smith and I am None
    E               ?                  - ^^^^^^
    E               + Hi, my name is jane None and I am None
    E               ?                 +++++  ^

  the value for first name and last name are different

* I change the string_ in the `return statement`_ to an :ref:`f-string<what is string interpolation?>` with the value for ``first_name``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 3

        @staticmethod
        def say_hello(person):
            return f'Hi, my name is {person.first_name} smith and I am None'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 4

    E               - Hi, my name is jane smith and I am None
    E               ?                     ^^^^^
    E               + Hi, my name is jane None and I am None
    E               ?                     ^^^^

  the values for the last name are different

* I add it to the :ref:`f-string<what is string interpolation?>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 3-6

        @staticmethod
        def say_hello(person):
            return (
                f'Hi, my name is {person.first_name} '
                f'{person.last_name} and I am None'
            )

  the test passes.

----

* I can call a :ref:`method<what is a method?>` that belongs to a :ref:`class<what is a class?>` without the need to pass in the :ref:`class<what is a class?>` as input since I can use the :ref:`class<what is a class?>` with ``self``. I remove the repetition of the ``Person`` object_ in the call to the ``say_hello`` :ref:`method<what is a method?>` in ``test_person.py``

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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.hello() missing 1 required positional argument: 'person'

* I remove the `staticmethod decorator`_ from the ``say_hello`` :ref:`method<what is a method?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 26

        def __init__(
                self, first_name, last_name=None,
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            self.last_name = last_name
            return None

        def say_hello(person):
            return (
                f'Hi, my name is {person.first_name} '
                f'{person.last_name} and I am None'
            )

  the test passes.

  This works because ``person`` in the parentheses is for the ``Person`` :ref:`class<what is a class?>` that the ``say_hello`` :ref:`method<what is a method?>` is part of.

  When I wrapped the ``say_hello`` :ref:`function<what is a function?>` with the `staticmethod decorator`_, it was a :ref:`function<what is a function?>` that did not use other parts (:ref:`class attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a method?>`) of the :ref:`class<what is a class?>` it belongs to.

* I use the ``Rename Symbol`` feature of the `Integrated Development Environment (IDE)`_ to change the name of the input parameter from ``person`` to ``self`` to match :ref:`Python convention<how to use class methods and attributes>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1, 3, 4
    :emphasize-text: self

        def say_hello(self):
            return (
                f'Hi, my name is {self.first_name} '
                f'{self.last_name} and I am None'
            )

  the test is still green, and there is a problem with the last name and age.

*********************************************************************************
test_attributes_and_methods_of_classes
*********************************************************************************


I used the `dir built-in function`_ in :ref:`lists<what is a list?>` and :ref:`dictionaries<what is a dictionary?>` to show their :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a method?>`. I can also use it with the ``Person`` :ref:`class<what is a class?>`

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

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

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

  the test passes.

The attributes I defined in the ``__init__`` :ref:`method<what is a method?>` are not in the list, because the test called dir_ on ``src.person.Person`` which is the :ref:`class<what is a class?>` definition, not on an instance (copy) of the class where I would have to provide values for the ``first_name``, ``last_name``, ``sex`` and ``year_of_birth`` :ref:`attributes<test_attribute_error_w_class_attributes>`.

What is the difference between ``dir(src.person.Person)`` and ``dir(src.person.Person('jane'))``?

The 3 :ref:`methods<what is a method?>` I defined in the ``Person`` :ref:`class<what is a class?>` in ``person.py``

* __init__
* get_age
* hello

are in the list, and there are others which I never defined, which leads to the question of :ref:`where did they come from?<family ties>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_person.py`` and ``person.py`` in the :ref:`editors<2 editors>`
* I click in the terminal_ where the tests are running, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

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

* A :ref:`class<what is a class?>` is :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a method?>` that belong together
* A :ref:`class<what is a class?>` can be used to represent something
* :ref:`classes<what is a class?>` can be an easier way to manage data than :ref:`functions<what is a function?>`
* :ref:`classes<what is a class?>` make it easier to write tests for something

.. tip::

  * when I find myself writing or doing the same thing two times, I write a :ref:`function<what is a function?>`
  * when I find I have two :ref:`functions<what is a function?>` that use the same information, I write a :ref:`class<what is a class?>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have gone through a lot of things and know

* :ref:`how to make a Python test driven development environment manually<how to make a Python test driven development environment>`
* :ref:`how to raise AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<telephone>`
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

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->