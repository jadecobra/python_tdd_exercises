.. include:: ../links.rst

.. _constructor: https://grokipedia.com/page/Constructor_(object-oriented_programming)
.. _constructor method: constructor_
.. _staticmethod: https://docs.python.org/3/library/functions.html#staticmethod
.. _staticmethod decorator: staticmethod_

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
        Person.get() takes 1 positional argument
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

* I add the :ref:`class attribute<test_attribute_error_w_class_attributes>` to the ``__init__`` :ref:`method<what is a method?>` so that the ``say_hello`` :ref:`method<what is a function?>` can use it

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

* I add an :ref:`assertion<what is an assertion?>` for the next person in :ref:`test_factory_person_says_hello` in ``test_person.py``

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
extract class attributes
*********************************************************************************

I make the values for ``first_name`` in the tests the same way each time, since ``TestPerson`` is a :ref:`class<what is a class?>`, I can use :ref:`class attributes<what is a class attribute?>` to remove repetition of how I make it, then have all the :ref:`methods<what is a method?>` reference it

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

----



*********************************************************************************
extract get_age method
*********************************************************************************

I want to use a :ref:`method<what is a method?>` to calculate the age.

* I go back to the terminal_ that is running the tests

* I change the :ref:`assertion<what is an assertion?>` in ``test_person.py``

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