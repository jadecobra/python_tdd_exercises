.. meta::
  :description: Learn how to transition from dictionary factories to Python classes using Test-Driven Development (TDD). This beginner-friendly tutorial covers the class keyword, __init__ constructor methods, self parameters, instance attributes, unittest.TestCase.setUp fixtures, and inspecting objects with the dir() function. Systematically debug common errors like TypeError, AttributeError, and SyntaxError.
  :keywords: Jacob Itegboje, Pumping Python, Python class tutorial, TDD Python class, __init__ constructor method, self parameter Python, unittest setUp method, dir function class, factory function vs class, TypeError Person takes no arguments, AttributeError module has no attribute, unexpected keyword argument, multiple values for argument, SyntaxError parameter without default, staticmethod decorator, class attributes and methods, Red Green Refactor

.. include:: ../links.rst

.. _constructor: https://grokipedia.com/page/Constructor_(object-oriented_programming)
.. _constructor method: constructor_
.. _staticmethod: https://docs.python.org/3/library/functions.html#staticmethod
.. _staticmethod decorator: staticmethod_

#################################################################################
classes
#################################################################################

I made :ref:`functions<what is a function?>` that make :ref:`dictionaries<what is a dictionary?>` and strings_ in :ref:`how to make a person`. I can also do the same thing with a :ref:`class<what is a class?>` since it is a group of :ref:`attributes (variables)<what is a class attribute?>` and :ref:`methods (functions) <what is a function?>` that belong together.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/tests/test_person_classes.py
  :language: python
  :linenos:

*********************************************************************************
questions about classes
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`what is a class?`
* :ref:`what is a class attribute?`
* :ref:`what is a method?`
* :ref:`how can I make sure things my tests need are run before every test?<how to use the setUp method to reset class attributes for every test>`

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
  :emphasize-lines: 8-13, 15-17
  :emphasize-text: Person

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
            my_expectation = None
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

  because the ``__init__`` `constructor method`_ takes the instance it belongs to as the first argument

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

* I add ``year_of_birth`` to the :ref:`definition<how to make a function>` of the ``__init__`` :ref:`method<what is a method?>`

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

  because the test calls the ``say_hello`` :ref:`function<what is a function?>` expects a :ref:`dictionary<what is a dictionary?>` and calls the :ref:`get method<test_get_value_of_a_key_in_a_dictionary>` on it. The ``Person`` :ref:`object<what is a class?>` does not have a :ref:`get method<test_get_value_of_a_key_in_a_dictionary>`.

* I change ``reality`` in :ref:`test_classy_person_says_hello` to use a :ref:`method<what is a method?>` that belongs to ``Person``, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 8-9
    :emphasize-text: joe

        def test_classy_person_says_hello(self):
            joe = src.person.Person(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )

            # reality = src.person.say_hello(joe)
            reality = joe.say_hello(joe)
            my_expectation = None
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

  because the :ref:`definition<how to make a function>` for ``say_hello`` does not allow inputs and the test called the :ref:`method<what is a method?>` with one :ref:`positional argument<test_functions_w_positional_arguments>` (``person``) and the error says two were given

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

    TypeError:
        Person.say_hello() takes 1 positional argument
        but 2 were given

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

  the test passes. I can call :ref:`methods<what is a method?>` from outside the :ref:`class<what is a class?>` they belong to.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

I want the ``say_hello`` :ref:`method<what is a method?>` to return a string_ for the person it belongs to, the same way the ``say_hello`` :ref:`function<what is a function?>` returns a string_ for the person it receives as input

* I change ``my_expectation`` to an :ref:`f-string<what is string interpolation?>` in :ref:`test_classy_person_says_hello` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 10-13

        def test_classy_person_says_hello(self):
            joe = src.person.Person(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )

            # reality = src.person.say_hello(joe)
            reality = joe.say_hello(joe)
            my_expectation = (
                'Hi, my name is joe blow and I am'
                f' {calculate_age(1996)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'Hi, my name is joe blow and I am 30'

* I copy the value from the terminal_ and paste it in the `return statement`_ for the ``say_hello`` :ref:`method<what is a method?>` of the ``Person`` :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

    def say_hello(person):
        return 'Hi, my name is joe blow and I am 30'

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the next person to :ref:`test_classy_person_says_hello` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 9-13, 15-20
    :emphasize-text: Person jane

            # reality = src.person.say_hello(joe)
            reality = joe.say_hello(joe)
            my_expectation = (
                'Hi, my name is joe blow and I am'
                f' {calculate_age(1996)}'
            )
            self.assertEqual(reality, my_expectation)

            jane = src.person.Person(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )

            reality = jane.say_hello(jane)
            my_expectation = (
                'Hi, my name is jane doe and I am'
                f' {calculate_age(1991)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() got an
        unexpected keyword argument 'sex'

  because the ``__init__`` :ref:`method definition<how to make a function>` does not have a parameter named ``sex``

* I add ``sex`` to the :ref:`definition<how to make a function>` of the ``__init__`` :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 5
    :emphasize-text: sex

    class Person:

        def __init__(
                self, first_name, last_name,
                year_of_birth, sex,
            ):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() missing
        1 required positional argument: 'sex'

  because when the test calls the ``Person`` :ref:`object<what is a class?>` to make ``joe`` it does not provide a value for ``sex`` which I just made a required argument when I added it to the ``__init__`` :ref:`method definition<how to make a function>`, I have to make it a choice

* I add a default value for ``sex`` to make it optional

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3

        def __init__(
                self, first_name, last_name,
                year_of_birth, sex=None,
            ):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() missing
        1 required positional argument: 'last_name'

  because when the test calls the ``Person`` :ref:`object<what is a class?>` to make ``jane`` it does not provide a value for ``last_name`` which is a required argument, I have to make it a choice

* I add a default value for ``last_name`` to make it optional

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

        def __init__(
                self, first_name, last_name=None,
                year_of_birth, sex=None,
            ):
            return None

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows
                 parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_functions_w_positional_and_keyword_args>`

* I add a default value for ``year_of_birth`` to make it optional

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3

        def __init__(
                self, first_name, last_name=None,
                year_of_birth=None, sex=None,
            ):
            return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
          'Hi, my name is joe blow and I am 30'
       != 'Hi, my name is jane doe and I am 35'

  the ``say_hello`` :ref:`function<what is a function?>` should use the ``Person`` :ref:`object<what is a class?>` to make the message. I can do that with the :ref:`class attributes<what is a class attribute?>`.

* I change the string_ to an :ref:`f-string<what is string interpolation?>` with :ref:`class attributes<what is a class attribute?>` for the ``first_name``, in ``person.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 11-15

    class Person:

        def __init__(
                self, first_name, last_name=None,
                year_of_birth=None, sex=None,
            ):
            return None

        @staticmethod
        def say_hello(person):
            # return 'Hi, my name is joe blow and I am 30'
            return (
                f'Hi, my name is {self.first_name} blow'
                ' and I am 30'
            )

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

  because I made ``say_hello`` a `staticmethod`_ when it was not using anything in the :ref:`class<what is a class?>`

* I remove the `staticmethod decorator` then add ``self`` in the parentheses

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 1-2

        # @staticmethod
        def say_hello(self, person):
            # return 'Hi, my name is joe blow and I am 30'
            return (
                f'Hi, my name is {self.first_name} blow'
                ' and I am 30'
            )

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'first_name'

  because I do not have a definition for ``first_name`` in the ``Person`` :ref:`object<what is a class?>`

* I add the :ref:`class attribute<what is a class attribute?>` to the ``__init__`` :ref:`method<what is a method?>` so that the ``say_hello`` :ref:`method<what is a function?>` can use it

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 5

        def __init__(
                self, first_name, last_name=None,
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-text: doe blow 30 35

    AssertionError:
        'Hi, my name is jane blow and I am 30'
     != 'Hi, my name is jane doe and I am 35'

  the first names are the same, the last name and ages are different

* I add a reference to the ``last_name`` in the `return statement`_ of the ``say_hello`` :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 5-7

        # @staticmethod
        def say_hello(self, person):
            # return 'Hi, my name is joe blow and I am 30'
            return (
                # f'Hi, my name is {self.first_name} blow'
                f'Hi, my name is {self.first_name}'
                f' {self.last_name}'
                ' and I am 30'
            )

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Person' object has no attribute 'last_name'.
        Did you mean: 'first_name'?

  because I do not have a definition for ``first_name`` in the ``Person`` :ref:`object<what is a class?>`

* I add ``self.last_name`` to the ``__init__`` :ref:`method<what is a method?>` so that the ``say_hello`` :ref:`method<what is a function?>` can use it

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 6

        def __init__(
                self, first_name, last_name=None,
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            self.last_name = last_name
            return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-text: None


    AssertionError:
        'Hi, my name is jane None and I am 30'
     != 'Hi, my name is jane doe and I am 35'

  because the default value for ``last_name`` is :ref:`None<what is None?>`

* I change the default value for ``last_name`` in the ``__init__`` :ref:`method<what is a method?>` to ``'doe'`` to give the test what it wants

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

        def __init__(
                self, first_name, last_name='doe',
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            self.last_name = last_name
            return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-text: 30 35

    AssertionError:
        'Hi, my name is jane doe and I am 30'
     != 'Hi, my name is jane doe and I am 35'

  the age is the only thing that is different

* I add a calculation for the age with the ``year_of_birth`` in the `return statement`_ of the ``say_hello`` :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4-6, 11-13

        # @staticmethod
        def say_hello(self, person):
            age = (
                datetime.datetime.today().year
              - self.year_of_birth
            )
            # return 'Hi, my name is joe blow and I am 30'
            return (
                # f'Hi, my name is {self.first_name} blow'
                f'Hi, my name is {self.first_name}'
                # f' {self.last_name}'
                # ' and I am 30'
                f' {self.last_name} and I am {age}'
            )

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Person' object has no attribute 'year_of_birth'

  because I do not have a definition for ``year_of_birth`` in the ``Person`` :ref:`object<what is a class?>`

* I add ``self.year_of_birth`` to the ``__init__`` :ref:`method<what is a method?>` so that the ``say_hello`` :ref:`method<what is a function?>` can use it

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 7

        def __init__(
                self, first_name, last_name='doe',
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            return None

  the test passes. What a beautiful life.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 27

    class Person:

        def __init__(
                self, first_name, last_name='doe',
                year_of_birth=None, sex=None,
            ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            return None

        def say_hello(self, person):
            age = (
                datetime.datetime.today().year
              - self.year_of_birth
            )
            return (
                f'Hi, my name is {self.first_name}'
                f' {self.last_name} and I am {age}'
            )

* I add an :ref:`assertion<what is an assertion?>` for the next person in :ref:`test_classy_person_says_hello` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 14-18, 20-25
    :emphasize-text: Person john

            jane = src.person.Person(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )

            reality = jane.say_hello(jane)
            my_expectation = (
                'Hi, my name is jane doe and I am'
                f' {calculate_age(1991)}'
            )
            self.assertEqual(reality, my_expectation)

            john = src.person.Person(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )

            reality = john.say_hello(john)
            my_expectation = (
                'Hi, my name is jane doe and I am'
                f' {calculate_age(1991)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hi, my name is john smith and I am 446'
     != 'Hi, my name is jane doe and I am 35'

* I change ``my_expectation`` to match ``reality`` for ``john``

  .. code-block:: python
    :lineno-start: 116
    :emphasize-lines: 9-10

            john = src.person.Person(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )

            reality = john.say_hello(john)
            my_expectation = (
                'Hi, my name is john smith and I am'
                f' {calculate_age(1580)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``a_person``

  .. code-block:: python
    :lineno-start: 116
    :emphasize-lines: 14-19, 21-26
    :emphasize-text: Person a_person

            john = src.person.Person(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )

            reality = john.say_hello(john)
            my_expectation = (
                'Hi, my name is john smith and I am'
                f' {calculate_age(1580)}'
            )
            self.assertEqual(reality, my_expectation)

            a_person = src.person.Person(
                first_name='person',
                last_name='public',
                year_of_birth=2000,
                sex='F',
            )

            reality = a_person.say_hello(a_person)
            my_expectation = (
                'Hi, my name is john smith and I am'
                f' {calculate_age(1580)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hi, my name is person public and I am 26'
     != 'Hi, my name is john smith and I am 446'

* I change ``my_expectation`` to match ``reality`` for ``a_person``

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 10-11

            a_person = src.person.Person(
                first_name='person',
                last_name='public',
                year_of_birth=2000,
                sex='F',
            )

            reality = a_person.say_hello(a_person)
            my_expectation = (
                'Hi, my name is person public and I am'
                f' {calculate_age(2000)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I open a new terminal_ then change directories to ``person``

  .. code-block:: python
    :emphasize-lines: 1

    cd person

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_classy_person_says_hello'

----

*********************************************************************************
test_classy_person_says_hello with random values
*********************************************************************************

I want to use random values to :ref:`test_classy_person_says_hello`

* I go back to the terminal_ that is running the tests

* I add a random person with random values for the ``first_name``, ``last_name`` and ``age`` :ref:`variables<what is a variable?>` that are sent in the call to ``src.person.Person``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 2-5, 7-12, 14-18

        def test_classy_person_says_hello(self):
            first_name = get_random_name()
            last_name = get_random_name()
            sex = pick_one('F', 'M')
            year_of_birth = get_random_year_of_birth()

            a_random_person = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = a_random_person.say_hello(
                a_random_person
            )
            my_expectation = ''
            self.assertEqual(reality, my_expectation)

            joe = src.person.Person(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )

  the terminal_ is my friend and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Hi, my name is Z Y and I am X' != ''

* I change ``my_expectation`` to match ``reality`` for ``a_random_person``

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 11-14

            a_random_person = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = a_random_person.say_hello(
                a_random_person
            )
            my_expectation = (
                f'Hi, my name is {first_name} {last_name}'
                f' and I am {calculate_age(year_of_birth)}'
            )
            self.assertEqual(reality, my_expectation)

  the test passes

* I remove the commented lines and the other people from :ref:`test_classy_person_says_hello` because ``a_random_person`` covers their cases

  .. code-block:: python
    :lineno-start: 88

        def test_classy_person_says_hello(self):
            first_name = get_random_name()
            last_name = get_random_name()
            sex = pick_one('F', 'M')
            year_of_birth = get_random_year_of_birth()

            a_random_person = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = a_random_person.say_hello(
                a_random_person
            )
            my_expectation = (
                f'Hi, my name is {first_name} {last_name}'
                f' and I am {calculate_age(year_of_birth)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'test_classy_person_says_hello with random values'

----

*********************************************************************************
extract random_first_name class attribute
*********************************************************************************

I make the values for ``first_name`` in the tests the same way each time, since ``TestPerson`` is a :ref:`class<what is a class?>`, I can use a :ref:`class attribute<what is a class attribute?>` to remove repetition of how I make it, then have all the :ref:`methods<what is a method?>` reference it

* I go back to the terminal_ that is running the tests

* I add a :ref:`class attribute<what is a class attribute?>` called ``random_first_name`` to the ``TestPerson`` :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 3

    class TestPerson(unittest.TestCase):

        random_first_name = get_random_name()

        def test_factory_w_keyword_arguments(self):

* I use the new :ref:`class attribute<what is a class attribute?>` in :ref:`test_factory_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 3-4

        def test_factory_w_keyword_arguments(self):
            a_person = dict(
                # first_name=get_random_name(),
                first_name=self.random_first_name,
                last_name=get_random_name(),
                sex=pick_one('F', 'M'),
            )
            year_of_birth = get_random_year_of_birth()

  the test is still green.

* I use the new :ref:`class attribute<what is a class attribute?>` in :ref:`test_factory_w_optional_arguments`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2-3, 7-8, 12-13

        def test_factory_w_optional_arguments(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            year_of_birth = get_random_year_of_birth()

            reality = src.person.factory(
                # first_name=first_name,
                first_name=self.random_first_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                # first_name=first_name,
                first_name=self.random_first_name,
                last_name='doe',
                sex='M',
                age=calculate_age(year_of_birth),
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_person_says_hello(self):

  the test is still green.

* I use the new :ref:`class attribute<what is a class attribute?>` in :ref:`test_factory_person_says_hello`

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 2-3, 9-10, 18-20

        def test_factory_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            last_name = get_random_name()
            sex = pick_one('F', 'M')
            year_of_birth = get_random_year_of_birth()

            a_random_person = src.person.factory(
                # first_name=first_name,
                first_name=self.random_first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(a_random_person)
            my_expectation = (
                # f'Hi, my name is {first_name} {last_name}'
                f'Hi, my name is {self.random_first_name}'
                f' {last_name}'
                f' and I am {calculate_age(year_of_birth)}'
            )
            self.assertEqual(reality, my_expectation)

        def test_classy_person_says_hello(self):

  the test is still green.

* I use the new :ref:`class attribute<what is a class attribute?>` in :ref:`test_classy_person_says_hello`

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 2-3, 9-10, 20-22

        def test_classy_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            last_name = get_random_name()
            sex = pick_one('F', 'M')
            year_of_birth = get_random_year_of_birth()

            a_random_person = src.person.Person(
                # first_name=first_name,
                first_name=self.random_first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = a_random_person.say_hello(
                a_random_person
            )
            my_expectation = (
                # f'Hi, my name is {first_name} {last_name}'
                f'Hi, my name is {self.random_first_name}'
                f' {last_name}'
                f' and I am {calculate_age(year_of_birth)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract random_first_name class attribute'

----

*********************************************************************************
extract random_year_of_birth class attribute
*********************************************************************************

I call the ``get_random_year_of_birth`` :ref:`function<what is a function?>` for ``year_of_birth`` in each test, since ``TestPerson`` is a :ref:`class<what is a class?>`, I can use a :ref:`class attribute<what is a class attribute?>` to remove repetition of those calls, then have all the :ref:`methods<what is a method?>` reference the value it returns

* I go back to the terminal_ that is running the tests

* I add a :ref:`class attribute<what is a class attribute?>` called ``random_year_of_birth`` to the ``TestPerson`` :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 4

    class TestPerson(unittest.TestCase):

        random_first_name = get_random_name()
        random_year_of_birth = get_random_year_of_birth()

        def test_factory_w_keyword_arguments(self):

* I use ``self.random_year_of_birth`` in :ref:`test_factory_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 8-9, 13-14, 18-19

        def test_factory_w_keyword_arguments(self):
            a_person = dict(
                # first_name=get_random_name(),
                first_name=self.random_first_name,
                last_name=get_random_name(),
                sex=pick_one('F', 'M'),
            )
            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth

            reality = src.person.factory(
                **a_person,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )
            my_expectation = dict(
                **a_person,
                # age=calculate_age(year_of_birth),
                age=calculate_age(self.random_year_of_birth),
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_w_optional_arguments(self):

  still green.

* I use ``self.random_year_of_birth`` in :ref:`test_factory_w_optional_arguments`

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 4-5, 10-11, 18-19

        def test_factory_w_optional_arguments(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth

            reality = src.person.factory(
                # first_name=first_name,
                first_name=self.random_first_name,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )
            my_expectation = dict(
                # first_name=first_name,
                first_name=self.random_first_name,
                last_name='doe',
                sex='M',
                # age=calculate_age(year_of_birth),
                age=calculate_age(self.random_year_of_birth),
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_person_says_hello(self):

  still green.

* I use ``self.random_year_of_birth`` in :ref:`test_factory_person_says_hello`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 6-7, 14-15, 22-25

        def test_factory_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            last_name = get_random_name()
            sex = pick_one('F', 'M')
            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth

            a_random_person = src.person.factory(
                # first_name=first_name,
                first_name=self.random_first_name,
                last_name=last_name,
                sex=sex,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )

            reality = src.person.say_hello(a_random_person)
            my_expectation = (
                # f'Hi, my name is {first_name} {last_name}'
                f'Hi, my name is {self.random_first_name}'
                # f' {last_name}'
                # f' and I am {calculate_age(year_of_birth)}'
                f' {last_name} and I am'
                f' {calculate_age(self.random_year_of_birth)}'
            )
            self.assertEqual(reality, my_expectation)

        def test_classy_person_says_hello(self):

  still green.

* I use ``self.random_year_of_birth`` in :ref:`test_classy_person_says_hello`

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 6-7, 14-15, 24-27

        def test_classy_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            last_name = get_random_name()
            sex = pick_one('F', 'M')
            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth

            a_random_person = src.person.Person(
                # first_name=first_name,
                first_name=self.random_first_name,
                last_name=last_name,
                sex=sex,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )

            reality = a_random_person.say_hello(
                a_random_person
            )
            my_expectation = (
                # f'Hi, my name is {first_name} {last_name}'
                f'Hi, my name is {self.random_first_name}'
                # f' {last_name}'
                # f' and I am {calculate_age(year_of_birth)}'
                f' {last_name} and I am'
                f' {calculate_age(self.random_year_of_birth)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract random_year_of_birth class attribute'

----

*********************************************************************************
extract random_last_name class attribute
*********************************************************************************

The ``last_name`` :ref:`variable<what is a variable?>` is made the same way in three of the four tests, I can use a :ref:`class attribute<what is a class attribute?>` to remove its repetition then have all the :ref:`methods<what is a method?>` reference the value

* I go back to the terminal_ that is running the tests

* I add a :ref:`class attribute<what is a class attribute?>` called ``random_last_name`` to the ``TestPerson`` :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 4

    class TestPerson(unittest.TestCase):

        random_first_name = get_random_name()
        random_last_name = get_random_name()
        random_year_of_birth = get_random_year_of_birth()

        def test_factory_w_keyword_arguments(self):

* I use ``self.random_last_name`` in :ref:`test_factory_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 5-6

        def test_factory_w_keyword_arguments(self):
            a_person = dict(
                # first_name=get_random_name(),
                first_name=self.random_first_name,
                # last_name=get_random_name(),
                last_name=self.random_last_name,
                sex=pick_one('F', 'M'),
            )
            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth

  green.

* I use ``self.random_last_name`` in :ref:`test_factory_person_says_hello`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 4-5, 13-14, 26-27

        def test_factory_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            # last_name = get_random_name()
            last_name = self.random_last_name
            sex = pick_one('F', 'M')
            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth

            a_random_person = src.person.factory(
                # first_name=first_name,
                first_name=self.random_first_name,
                # last_name=last_name,
                last_name=self.random_last_name,
                sex=sex,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )

            reality = src.person.say_hello(a_random_person)
            my_expectation = (
                # f'Hi, my name is {first_name} {last_name}'
                f'Hi, my name is {self.random_first_name}'
                # f' {last_name}'
                # f' and I am {calculate_age(year_of_birth)}'
                # f' {last_name} and I am'
                f' {self.random_last_name} and I am'
                f' {calculate_age(self.random_year_of_birth)}'
            )
            self.assertEqual(reality, my_expectation)

        def test_classy_person_says_hello(self):

  green.

* I use ``self.random_last_name`` in :ref:`test_classy_person_says_hello`

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 4-5, 13-14, 28-29

        def test_classy_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            # last_name = get_random_name()
            last_name = self.random_last_name
            sex = pick_one('F', 'M')
            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth

            a_random_person = src.person.Person(
                # first_name=first_name,
                first_name=self.random_first_name,
                # last_name=last_name,
                last_name=self.random_last_name,
                sex=sex,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )

            reality = a_random_person.say_hello(
                a_random_person
            )
            my_expectation = (
                # f'Hi, my name is {first_name} {last_name}'
                f'Hi, my name is {self.random_first_name}'
                # f' {last_name}'
                # f' and I am {calculate_age(year_of_birth)}'
                # f' {last_name} and I am'
                f' {self.random_last_name} and I am'
                f' {calculate_age(self.random_year_of_birth)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract random_last_name class attribute'

----

*********************************************************************************
extract random_sex class attribute
*********************************************************************************

The ``sex`` :ref:`variable<what is a variable?>` is made the same way in three of the four tests, I can use a :ref:`class attribute<what is a class attribute?>` to remove its repetition then have all the :ref:`methods<what is a method?>` reference the value

* I go back to the terminal_ that is running the tests

* I add a :ref:`class attribute<what is a class attribute?>` called ``random_sex`` to the ``TestPerson`` :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 5

    class TestPerson(unittest.TestCase):

        random_first_name = get_random_name()
        random_last_name = get_random_name()
        random_sex = pick_one('F', 'M')
        random_year_of_birth = get_random_year_of_birth()

        def test_factory_w_keyword_arguments(self):

* I use ``self.random_sex`` in :ref:`test_factory_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 7-8

        def test_factory_w_keyword_arguments(self):
            a_person = dict(
                # first_name=get_random_name(),
                first_name=self.random_first_name,
                # last_name=get_random_name(),
                last_name=self.random_last_name,
                # sex=pick_one('F', 'M'),
                sex=self.random_sex,
            )
            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth

  the test is still green.

* I use ``self.random_sex`` in :ref:`test_factory_person_says_hello`

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 6-7, 16-17

        def test_factory_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            # last_name = get_random_name()
            last_name = self.random_last_name
            # sex = pick_one('F', 'M')
            sex = self.random_sex
            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth

            a_random_person = src.person.factory(
                # first_name=first_name,
                first_name=self.random_first_name,
                # last_name=last_name,
                last_name=self.random_last_name,
                # sex=sex,
                sex=self.random_sex,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )

  the test is still green.

* I use ``self.random_sex`` in :ref:`test_classy_person_says_hello`

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 4-5, 13-14, 28-29

        def test_classy_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            # last_name = get_random_name()
            last_name = self.random_last_name
            # sex = pick_one('F', 'M')
            sex = self.random_sex
            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth

            a_random_person = src.person.Person(
                # first_name=first_name,
                first_name=self.random_first_name,
                # last_name=last_name,
                last_name=self.random_last_name,
                # sex=sex,
                sex=self.random_sex,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )

  the test is still green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract random_sex class attribute'

----

*********************************************************************************
extract age class attribute
*********************************************************************************

I call the ``calculate_age`` :ref:`function<what is a function?>` with the ``year_of_birth`` :ref:`variable<what is a variable?>` in each test, since ``TestPerson`` is a :ref:`class<what is a class?>`, I can use a :ref:`class attribute<what is a class attribute?>` to remove repetition of those calls, then have all the :ref:`methods<what is a method?>` reference the value  it returns

* I go back to the terminal_ that is running the tests

* I add a :ref:`class attribute<what is a class attribute?>` called ``age`` to the ``TestPerson`` :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 7

    class TestPerson(unittest.TestCase):

        random_first_name = get_random_name()
        random_last_name = get_random_name()
        random_sex = pick_one('F', 'M')
        random_year_of_birth = get_random_year_of_birth()
        age = calculate_age(random_year_of_birth)

        def test_factory_w_keyword_arguments(self):

* I use ``self.age`` in :ref:`test_factory_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 9-10

            reality = src.person.factory(
                **a_person,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )
            my_expectation = dict(
                **a_person,
                # age=calculate_age(year_of_birth),
                # age=calculate_age(self.random_year_of_birth),
                age=self.age,
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_w_optional_arguments(self):

  still green.

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_factory_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 40

        def test_factory_w_keyword_arguments(self):
            a_person = dict(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                sex=self.random_sex,
            )

            reality = src.person.factory(
                **a_person,
                year_of_birth=self.random_year_of_birth,
            )
            my_expectation = dict(
                **a_person,
                age=self.age,
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_w_optional_arguments(self):

* I use ``self.age`` in :ref:`test_factory_w_optional_arguments`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 13-14

            reality = src.person.factory(
                # first_name=first_name,
                first_name=self.random_first_name,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )
            my_expectation = dict(
                # first_name=first_name,
                first_name=self.random_first_name,
                last_name='doe',
                sex='M',
                # age=calculate_age(year_of_birth),
                # age=calculate_age(self.random_year_of_birth),
                age=self.age,
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_person_says_hello(self):

  still green.

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_factory_w_optional_arguments`

  .. code-block:: python
    :lineno-start: 57

        def test_factory_w_optional_arguments(self):
            reality = src.person.factory(
                first_name=self.random_first_name,
                year_of_birth=self.random_year_of_birth,
            )
            my_expectation = dict(
                first_name=self.random_first_name,
                last_name='doe',
                sex='M',
                age=self.age,
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_person_says_hello(self):

* I use ``self.age`` in :ref:`test_factory_person_says_hello`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 8-11

            reality = src.person.say_hello(a_random_person)
            my_expectation = (
                # f'Hi, my name is {first_name} {last_name}'
                f'Hi, my name is {self.random_first_name}'
                # f' {last_name}'
                # f' and I am {calculate_age(year_of_birth)}'
                # f' {last_name} and I am'
                # f' {self.random_last_name} and I am'
                # f' {calculate_age(self.random_year_of_birth)}'
                f' {self.random_last_name} '
                f'and I am {self.age}'
            )
            self.assertEqual(reality, my_expectation)

        def test_classy_person_says_hello(self):

  still green.

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_factory_person_says_hello`

  .. code-block:: python
    :lineno-start: 70

        def test_factory_person_says_hello(self):
            a_random_person = src.person.factory(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                sex=self.random_sex,
                year_of_birth=self.random_year_of_birth,
            )

            reality = src.person.say_hello(a_random_person)
            my_expectation = (
                f'Hi, my name is {self.random_first_name}'
                f' {self.random_last_name} '
                f'and I am {self.age}'
            )
            self.assertEqual(reality, my_expectation)

        def test_classy_person_says_hello(self):

* I use ``self.age`` in :ref:`test_classy_person_says_hello`

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 10-13

            reality = a_random_person.say_hello(
                a_random_person
            )
            my_expectation = (
                # f'Hi, my name is {first_name} {last_name}'
                f'Hi, my name is {self.random_first_name}'
                # f' {last_name}'
                # f' and I am {calculate_age(year_of_birth)}'
                # f' {last_name} and I am'
                # f' {self.random_last_name} and I am'
                # f' {calculate_age(self.random_year_of_birth)}'
                f' {self.random_last_name} '
                f'and I am {self.age}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green.

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_classy_person_says_hello`

  .. code-block:: python
    :lineno-start: 86

        def test_classy_person_says_hello(self):
            a_random_person = src.person.Person(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                sex=self.random_sex,
                year_of_birth=self.random_year_of_birth,
            )

            reality = a_random_person.say_hello(
                a_random_person
            )
            my_expectation = (
                f'Hi, my name is {self.random_first_name}'
                f' {self.random_last_name} '
                f'and I am {self.age}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract age class attribute'


:ref:`I can remove repetition with class attributes<what is a class attribute?>`

----

****************************************************************************************
how to use the setUp method to reset class attributes for every test
****************************************************************************************

There are problems with the current setup with the :ref:`class attributes<what is a class attribute?>`

* anyone seeing the tests for the first time has to read the :ref:`class attributes<what is a class attribute?>`

  .. code-block:: python

    class TestPerson(unittest.TestCase):

        random_first_name = get_random_name()
        random_last_name = get_random_name()
        random_sex = pick_one('F', 'M')
        random_year_of_birth = get_random_year_of_birth()
        age = calculate_age(random_year_of_birth)

        def test_factory_w_keyword_arguments(self):

  to know how they are created then referenced in each test

* :ref:`test_factory_w_keyword_arguments` needs the person reading the test to know about :ref:`double starred expressions`

  .. code-block:: python

    src.person.factory(
        **a_person,
        year_of_birth=self.random_year_of_birth,
    )

  .. code-block:: python

    dict(
        **a_person,
        age=self.age,
    )

  to know why using the :ref:`dictionary<what is a dictionary?>` works in the call to ``src.person.factory`` and inside another :ref:`dictionary<what is a dictionary?>`

* :ref:`test_factory_person_says_hello` and :ref:`test_classy_person_says_hello` need the person reading the test to know about :ref:`f-strings<what is string interpolation?>`

  .. code-block:: python

    f'Hi, my name is {self.random_first_name}'
    f' {self.random_last_name} '
    f'and I am {self.age}'

* the other problem is :ref:`class attributes<what is a class attribute?>` are made once when the :ref:`class<what is a class?>` is initialized. This means that even though they all use random values, those values are created once and every test that references the values is using the exact same values for each test.

  I want the test to get new random values every time they run and the `unittest.TestCase class`_ has a way to do that - the `setUp method`_. It makes sure that whatever setup I want runs before each test

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add the `unittest.TestCase.setUp method`_ to ``TestPerson`` then move the :ref:`class attributes<what is a class attribute?>` into it

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 3-7, 9-14

    class TestPerson(unittest.TestCase):

        # random_first_name = get_random_name()
        # random_last_name = get_random_name()
        # random_sex = pick_one('F', 'M')
        # random_year_of_birth = get_random_year_of_birth()
        # age = calculate_age(random_year_of_birth)

        def setUp(self):
            random_first_name = get_random_name()
            random_last_name = get_random_name()
            random_sex = pick_one('F', 'M')
            random_year_of_birth = get_random_year_of_birth()
            age = calculate_age(random_year_of_birth)

        def test_factory_w_keyword_arguments(self):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    FAILED ...test_classy_person_says_hello - AttributeError:
        'TestPerson' object has no attribute 'random_first_name'
    FAILED ...test_factory_person_says_hello - AttributeError:
        'TestPerson' object has no attribute 'random_first_name'
    FAILED ...test_factory_w_keyword_arguments - AttributeError:
        'TestPerson' object has no attribute 'random_first_name'
    FAILED ...test_factory_w_optional_arguments - AttributeError:
        'TestPerson' object has no attribute 'random_first_name'

  because the ``first_name`` :ref:`variable<what is a variable?>` now belongs to the `setUp method`_, the other tests have no way to reach it. I have to make it a :ref:`class attribute<what is a class attribute?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the ``first_name`` :ref:`variable<what is a variable?>` to a :ref:`class attribute<what is a class attribute?>` in the `setUp method`_ for the other tests to be able to use it

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 2-3
    :emphasize-text: self

        def setUp(self):
            # random_first_name = get_random_name()
            self.random_first_name = get_random_name()
            random_last_name = get_random_name()
            random_sex = pick_one('F', 'M')
            random_year_of_birth = get_random_year_of_birth()
            age = calculate_age(random_year_of_birth)

        def test_factory_w_keyword_arguments(self):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    FAILED ...test_classy_person_says_hello - AttributeError:
        'TestPerson' object has no attribute 'random_last_name'.
        Did you mean: 'random_first_name'?
    FAILED ...test_factory_person_says_hello - AttributeError:
        'TestPerson' object has no attribute 'random_last_name'.
        Did you mean: 'random_first_name'?
    FAILED ...test_factory_w_keyword_arguments - AttributeError:
        'TestPerson' object has no attribute 'random_last_name'.
        Did you mean: 'random_first_name'?
    FAILED ...test_factory_w_optional_arguments - AttributeError:
        'TestPerson' object has no attribute 'random_year_of_birth'.

  because the ``year_of_birth`` and ``last_name`` :ref:`variables<what is a variable?>` now belong to the `setUp method`_, the other tests have no way to reach them. I have to make them :ref:`class attributes<what is a class attribute?>`

* I change the ``year_of_birth`` and ``last_name`` :ref:`variables<what is a variable?>` to :ref:`class attributes<what is a class attribute?>` in the `setUp method`_ for the other tests to be able to use them

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 4-5, 7-10
    :emphasize-text: self

        def setUp(self):
            # random_first_name = get_random_name()
            self.random_first_name = get_random_name()
            # random_last_name = get_random_name()
            self.random_last_name = get_random_name()
            random_sex = pick_one('F', 'M')
            # random_year_of_birth = get_random_year_of_birth()
            self.random_year_of_birth = get_random_year_of_birth()
            # age = calculate_age(random_year_of_birth)
            age = calculate_age(self.random_year_of_birth)

        def test_factory_w_keyword_arguments(self):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    FAILED ...test_classy_person_says_hello - AttributeError:
        'TestPerson' object has no attribute 'random_sex'
    FAILED ...test_factory_person_says_hello - AttributeError:
        'TestPerson' object has no attribute 'random_sex'
    FAILED ...test_factory_w_keyword_arguments - AttributeError:
        'TestPerson' object has no attribute 'random_sex'
    FAILED ...test_factory_w_optional_arguments - AttributeError:
        'TestPerson' object has no attribute 'age'

  because the ``age`` and ``random_sex`` :ref:`variables<what is a variable?>` now belong to the `setUp method`_, the other tests have no way to reach them. I have to make them :ref:`class attributes<what is a class attribute?>`

* I change the ``age`` and ``random_sex`` :ref:`variables<what is a variable?>` to :ref:`class attributes<what is a class attribute?>` in the `setUp method`_ for the other tests to be able to use them

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 4-5, 7-10
    :emphasize-text: self

        def setUp(self):
            # random_first_name = get_random_name()
            self.random_first_name = get_random_name()
            # random_last_name = get_random_name()
            self.random_last_name = get_random_name()
            # random_sex = pick_one('F', 'M')
            self.random_sex = pick_one('F', 'M')
            # random_year_of_birth = get_random_year_of_birth()
            self.random_year_of_birth = get_random_year_of_birth()
            # age = calculate_age(random_year_of_birth)
            # age = calculate_age(self.random_year_of_birth)
            self.age = calculate_age(self.random_year_of_birth)

        def test_factory_w_keyword_arguments(self):

  the test passes.

The `unittest.TestCase.setUp method`_ runs before every test, in this case it sets these :ref:`class attributes (variables)<test_attribute_error_w_class_attributes>` to new values before every test

- ``self.random_first_name`` to the result of calling the ``get_random_name`` :ref:`function<what is a function?>`, which returns a random name
- ``self.random_last_name`` to the result of calling the ``get_random_name`` :ref:`function<what is a function?>`, which returns a random name
- ``self.random_sex`` to a random sex value between ``'F'`` and ``'M'``
- ``self.random_year_of_birth`` to the result of calling the ``get_random_year_of_birth`` :ref:`function<what is a function?>` which returns a random year between 120 years ago and the current year
- ``self.age`` to the result of calling the ``calculate_age`` :ref:`function<what is a function?>`, which returns the current year minus ``self.random_year_of_birth``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I no longer need the :ref:`calculate_age function<extract calculate_age function>` because it is only called once by the `setUp method`_

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 13-16

        def setUp(self):
            # random_first_name = get_random_name()
            self.random_first_name = get_random_name()
            # random_last_name = get_random_name()
            self.random_last_name = get_random_name()
            # random_sex = pick_one('F', 'M')
            self.random_sex = pick_one('F', 'M')
            # random_year_of_birth = get_random_year_of_birth()
            self.random_year_of_birth = get_random_year_of_birth()
            # age = calculate_age(random_year_of_birth)
            # age = calculate_age(self.random_year_of_birth)
            # self.age = calculate_age(self.random_year_of_birth)
            self.age = (
                datetime.datetime.now().year
              - self.random_year_of_birth
            )

        def test_factory_w_keyword_arguments(self):

  the test is still green.

* I no longer need the :ref:`get_random_year_of_birth function<extract get_random_year_of_birth function>` because it is only called once by the `setUp method`_

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 9-13

        def setUp(self):
            # random_first_name = get_random_name()
            self.random_first_name = get_random_name()
            # random_last_name = get_random_name()
            self.random_last_name = get_random_name()
            # random_sex = pick_one('F', 'M')
            self.random_sex = pick_one('F', 'M')
            # random_year_of_birth = get_random_year_of_birth()
            # self.random_year_of_birth = get_random_year_of_birth()
            this_year = datetime.datetime.now().year
            self.random_year_of_birth = random.randint(
                this_year-120, this_year
            )
            # age = calculate_age(random_year_of_birth)
            # age = calculate_age(self.random_year_of_birth)
            # self.age = calculate_age(self.random_year_of_birth)
            self.age = (
                datetime.datetime.now().year
              - self.random_year_of_birth
            )

        def test_factory_w_keyword_arguments(self):

  still green.

* I can use the ``this_year`` :ref:`variable<what is a variable?>` in the calculation for ``self.age``

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 17-21

        def setUp(self):
            # random_first_name = get_random_name()
            self.random_first_name = get_random_name()
            # random_last_name = get_random_name()
            self.random_last_name = get_random_name()
            # random_sex = pick_one('F', 'M')
            self.random_sex = pick_one('F', 'M')
            # random_year_of_birth = get_random_year_of_birth()
            # self.random_year_of_birth = get_random_year_of_birth()
            this_year = datetime.datetime.now().year
            self.random_year_of_birth = random.randint(
                this_year-120, this_year
            )
            # age = calculate_age(random_year_of_birth)
            # age = calculate_age(self.random_year_of_birth)
            # self.age = calculate_age(self.random_year_of_birth)
            # self.age = (
            #     datetime.datetime.now().year
            #   - self.random_year_of_birth
            # )
            self.age = this_year - self.random_year_of_birth

        def test_factory_w_keyword_arguments(self):

  green. ``datetime.datetime.now().year`` is now called only once each time the `setUp method`_ runs

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 32

    class TestPerson(unittest.TestCase):

        def setUp(self):
            self.random_first_name = get_random_name()
            self.random_last_name = get_random_name()
            self.random_sex = pick_one('F', 'M')

            this_year = datetime.datetime.now().year
            self.random_year_of_birth = random.randint(
                this_year-120, this_year
            )
            self.age = this_year - self.random_year_of_birth

        def test_factory_w_keyword_arguments(self):

* I remove the :ref:`calculate_age<extract calculate_age function>` and :ref:`get_random_year_of_birth functions<extract get_random_year_of_birth function>`

  .. code-block:: python
    :linenos:

    import datetime
    import random
    import src.person
    import unittest


    def pick_one(*choices):
        return random.choice(choices)


    def get_random_name():
        return pick_one(
            'jane', 'joe', 'john', 'person',
            'doe', 'smith', 'blow', 'public',
        )


    class TestPerson(unittest.TestCase):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'move class attributes to setUp method'

----

*********************************************************************************
test_attributes_and_methods_of_classes
*********************************************************************************

Python has the `dir built-in function`_ which shows the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the :ref:`object<what is a class?>` it is given in parentheses. This allows me to explore what an :ref:`object<what is a class?>` contains without looking at the code or reading the documentation, I can then run tests to see what each thing does.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a new test with the `dir built-in function`_ in ``test_person.py``

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 11-14

              reality = a_random_person.say_hello(
                  a_random_person
              )
              my_expectation = (
                  f'Hi, my name is {self.random_first_name}'
                  f' {self.random_last_name} '
                  f'and I am {self.age}'
              )
              self.assertEqual(reality, my_expectation)

          def test_attributes_and_methods_of_a_class(self):
              reality = dir(src.person.Person)
              my_expectation = None
              self.assertEqual(reality, my_expectation)


      # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Lists differ:
        ['__class__', '__delattr__', '__dict__', '[377 chars]llo']
     != None

  because dir_ returned a :ref:`list <what is a list?>` (anything in square brackets ``[ ]``) and ``my_expectation`` is :ref:`None<what is None?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_ and paste (:kbd:`ctrl/command+v`) them as ``my_expectation``

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 3-6

        def test_attributes_and_methods_of_a_class(self):
            reality = dir(src.person.Person)
            my_expectation = [
                '__class__', '__delattr__', '__dict__',
                [371 chars]llo'
            ]
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: unterminated string literal (detected at line 99)

  because I have a closing :ref:`quote<quotes>` (``'``) without a matching opening one

* I add the opening :ref:`quote<quotes>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 5

        def test_attributes_and_methods_of_a_class(self):
            reality = dir(src.person.Person)
            my_expectation = [
                '__class__', '__delattr__', '__dict__',
                '[371 chars]llo'
            ]
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Lists differ:
        ['__c[32 chars]_', '__dir__', '__doc__', '__eq__',
         '__firstli[329 chars]llo']
     != ['__c[32 chars]_', '[371 chars]llo']

  it shows me the entire :ref:`list<what is a list?>` below the message

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_ and paste (:kbd:`ctrl/command+v`) them as ``my_expectation``

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 3-32
    :emphasize-text: __init__ say_hello

        def test_attributes_and_methods_of_a_class(self):
            reality = dir(src.person.Person)
            my_expectation = ['__class__',
    E       -  '__delattr__',
    E       -  '__dict__',
    E       -  '__dir__',
    E       -  '__doc__',
    E       -  '__eq__',
    E       -  '__firstlineno__',
    E       -  '__format__',
    E       -  '__ge__',
    E       -  '__getattribute__',
    E       -  '__getstate__',
    E       -  '__gt__',
    E       -  '__hash__',
    E       -  '__init__',
    E       -  '__init_subclass__',
    E       -  '__le__',
    E       -  '__lt__',
    E       -  '__module__',
    E       -  '__ne__',
    E       -  '__new__',
    E       -  '__reduce__',
    E       -  '__reduce_ex__',
    E       -  '__repr__',
    E       -  '__setattr__',
    E       -  '__sizeof__',
    E       -  '__static_attributes__',
    E       -  '__str__',
    E       -  '__subclasshook__',
    E       -  '__weakref__',
    E       -  'say_hello']
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'E' is not defined

* I use the ``find and replace`` feature of the `Integrated Development Environment (IDE)`_ to remove the extra characters

.. code-block:: python
  :lineno-start: 95
  :emphasize-lines: 3-34
  :emphasize-text: __init__ say_hello

        def test_attributes_and_methods_of_a_class(self):
            reality = dir(src.person.Person)
            my_expectation = [
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
                'say_hello',
            ]
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am \
    'add test_attributes_and_methods_of_a_class'

The attributes I defined in the ``__init__`` :ref:`method<what is a method?>` are not in the list, because the test called dir_ on ``src.person.Person`` which is the :ref:`class<what is a class?>` definition, not on an instance (copy) of the class where I would have to provide values for the ``first_name``, ``last_name``, ``sex`` and ``year_of_birth`` :ref:`attributes<what is a class attribute?>`.

What is the difference between ``dir(src.person.Person)`` and ``dir(src.person.Person('jane'))``?

The :ref:`methods<what is a method?>` I defined in the ``Person`` :ref:`class<what is a class?>` in ``person.py``

* __init__
* :ref:`say_hello<test_classy_person_says_hello>`

are in the :ref:`list<what is a list?>`, and there are others which I did not define, which leads to the question of :ref:`where did they come from?<family ties>`

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

* A :ref:`class<what is a class?>` is :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` that belong together
* A :ref:`class<what is a class?>` can be used to represent something
* A :ref:`class attributes<what is a class attribute?>` is a :ref:`variable<what is a variable?>` that belongs to a :ref:`class<what is a class?>`
* A :ref:`method<what is a function?>` is a :ref:`function<what is a function?>` that belongs to a :ref:`class<what is a class?>`
* :ref:`classes<what is a class?>` can be an easier way to manage data than :ref:`functions<what is a function?>`
* :ref:`classes<what is a class?>` make it easier to write tests for something

.. tip::

  * when I find myself writing or doing the same thing two times, I write a :ref:`function<what is a function?>`
  * when I find I have two :ref:`functions<what is a function?>` that use the same information, I write a :ref:`class<what is a class?>`

:ref:`How many questions can you answer about classes?<questions about classes>`

----

*************************************************************************************
what is next?
*************************************************************************************

You have gone through a lot of things and know:


* :ref:`how to make a Python test driven development environment manually<how to make a Python test driven development environment>`
* :ref:`how to raise AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`how to make classes<classes>`

:ref:`Would you like to test what causes AttributeError<what causes AttributeError?>` or :ref:`Would you like to know where the extra attributes and methods of the Person class came from?<family ties>`

You know enough to go into the world and use Python_. If you stopped going through the book at this point, you would be fine because you know how to make :ref:`classes<what is a class?>`, :ref:`functions<what is a function?>` and can make :ref:`dictionaries<what is a dictionary?>` which is what is behind a lot of the things you will encounter.

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