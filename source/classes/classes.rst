.. meta::
  :description: Step-by-step TDD tutorial for transitioning from dictionary factories to Python classes. Learn the class keyword, __init__ constructor, self parameter, instance attributes, and unittest.TestCase.setUp. Learn how to systematically diagnose and fix common beginner bugs: TypeError: Person() takes no arguments, TypeError: got multiple values for argument 'first_name', NameError: name 'self' is not defined, SyntaxError: parameter without a default follows parameter with a default, and AttributeError: object has no attribute. Master object inspection using the dir() function.
  :keywords: Jacob Itegboje, Pumping Python, python class tutorial for beginners, test-driven development classes python, dictionary factory vs class python, when to write a class in python, __init__ constructor method self parameter, why use self in python class, how does unittest setUp method work, reset class attributes before every test python, using dir() function to inspect python objects, how to call instance methods directly, TypeError Person takes no arguments, TypeError Person.__init__ got multiple values for argument, TypeError say_hello takes 0 positional arguments but 2 were given, NameError name self is not defined, AttributeError object has no attribute get, SyntaxError parameter without default follows parameter with default, staticmethod decorator vs instance method, when to remove staticmethod python, python red green refactor class tutorial

.. include:: ../links.rst

.. _constructor: https://grokipedia.com/page/Constructor_(object-oriented_programming)
.. _constructor method: constructor_
.. _staticmethod: https://docs.python.org/3/library/functions.html#staticmethod
.. _staticmethod decorator: staticmethod_

#################################################################################
classes
#################################################################################

I made :ref:`functions<what is a function?>` that make :ref:`dictionaries (test_factory_w_keyword_arguments)<test_factory_w_keyword_arguments>` and :ref:`strings (test_factory_person_says_hello)<test_factory_person_says_hello>` in :ref:`how to make a person`.

I can also use a :ref:`class<everything is an object>` to represent a person, because it is a group of :ref:`attributes (variables)<what is a class attribute?>` and :ref:`methods (functions) <what is a function?>` that belong together.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/person/tests/test_person_classes.py
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
* :ref:`what is the staticmethod decorator?`

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

* I hold :kbd:`ctrl` on the keyboard, then click on ``tests/test_person.py`` to open it

----

*********************************************************************************
test_classy_person_says_hello
*********************************************************************************

I made a person :ref:`say hello with a function<test_factory_person_says_hello>`, I can also do the same thing with a :ref:`class<everything is an object>` because it is :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` that belong together.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to ``test_person.py``

.. code-block:: python
  :lineno-start: 69
  :emphasize-lines: 23-28, 30-32
  :emphasize-text: Person

      def test_factory_person_says_hello(self):
          first_name = get_random_name()
          last_name = get_random_name()
          sex = pick_one('F', 'M')

          year_of_birth = get_random_year_of_birth()
          age = calculate_age(year_of_birth)

          a_random_person = src.person.factory(
              first_name=first_name,
              last_name=last_name,
              sex=sex,
              year_of_birth=year_of_birth,
          )

          reality = src.person.say_hello(a_random_person)
          my_expectation = (
              f'Hello, my name is {first_name} {last_name}'
              f' and I am {age}'
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

* I add a :ref:`class<everything is an object>` to ``person.py``

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
              - year_of_birth
            ),
        }


    class Person:

        pass

  - I can :ref:`make a class with the pass keyword<test_making_a_class_w_pass>`
  - the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

    .. code-block:: python

      TypeError: Person() takes no arguments

    because :ref:`classes<everything is an object>` do not take arguments like a :ref:`function<what is a function?>` without a :ref:`method<what is a method?>` that handles those arguments

* I add a `constructor method`_ to the ``Person`` :ref:`class<everything is an object>` so it can take arguments, it is used to define how copies of the :ref:`class<everything is an object>` are made

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3-5

    class Person:

        # pass
        def __init__():
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() got an
        unexpected keyword argument 'first_name'

  - because the :ref:`definition<how to make a function>` for ``__init__`` does not allow calling it with inputs (the parentheses are empty) and the test sends ``'first_name'`` as input.
  - a `constructor method`_ is used to make copies of a :ref:`class<everything is an object>`

* I add the name in parentheses so that the ``__init__`` `constructor method`_ can take input

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4-5

    class Person:

        # pass
        # def __init__():
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
    :emphasize-lines: 5-6

    class Person:

        # pass
        # def __init__():
        # def __init__(first_name):
        def __init__(self, first_name):
            return None

  - ``self`` is Python_ convention, I can use any name I want
  - the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

    .. code-block:: shell

      TypeError:
          Person.__init__() got
          an unexpected keyword argument 'last_name'.
          Did you mean 'first_name'?

    I have seen this before, so far it is the same as making the :ref:`factory function<test_factory_w_keyword_arguments>`

* I add ``last_name`` to the :ref:`definition<how to make a function>` of ``__init__``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 6-7

    class Person:

        # pass
        # def __init__():
        # def __init__(first_name):
        # def __init__(self, first_name):
        def __init__(self, first_name, last_name):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() got
        an unexpected keyword argument 'year_of_birth'

  still the same as making the :ref:`factory function<test_factory_w_keyword_arguments>`

* I add ``year_of_birth`` to the :ref:`definition<how to make a function>` of the :ref:`__init__ method<the constructor method>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 7-8

    class Person:

        # pass
        # def __init__():
        # def __init__(first_name):
        # def __init__(self, first_name):
        # def __init__(self, first_name, last_name):
        def __init__(
            self, first_name, last_name,
            year_of_birth,
        ):
            return None

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError:
        'Person' object has no attribute 'get'

  because

  - the test calls the ``say_hello`` :ref:`function<what is a function?>`
  - the ``say_hello`` :ref:`function<what is a function?>` expects a :ref:`dictionary<what is a dictionary?>`
  - the ``say_hello`` :ref:`function<what is a function?>` calls the :ref:`get method<test_get_value_of_a_key_in_a_dictionary>` on what it receives and
  - the ``Person`` :ref:`object<everything is an object>` it receives is not a :ref:`dictionary<what is a dictionary?>` and does not have a :ref:`get method<test_get_value_of_a_key_in_a_dictionary>`

* I change ``reality`` in :ref:`test_classy_person_says_hello` to use a :ref:`method<what is a method?>` I can add to ``Person``, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 8-9
    :emphasize-text: joe

        def test_classy_person_says_hello(self):
            joe = src.person.Person(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )

            # reality = src.person.say_hello(joe)
            reality = src.person.Person.say_hello(joe)
            my_expectation = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError:
        'Person' object has no attribute 'say_hello'

  because the test calls the ``say_hello`` :ref:`function<what is a function?>` which does not yet exist in the ``Person`` :ref:`class<everything is an object>`

* I add a :ref:`method definition<how to make a function>` for it to the ``Person`` :ref:`class<everything is an object>` in ``person.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 14-15

    class Person:

        # pass
        # def __init__():
        # def __init__(first_name):
        # def __init__(self, first_name):
        # def __init__(self, first_name, last_name):
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

  because the :ref:`definition<how to make a function>` for ``say_hello`` does not allow inputs and the test called the :ref:`method<what is a method?>` with one :ref:`positional argument<test_positional_arguments>` (``person``). Why did the error say two were given when the test only sends one?

* I add ``person`` to the :ref:`method definition<how to make a function>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 14-15

    class Person:

        # pass
        # def __init__():
        # def __init__(first_name):
        # def __init__(self, first_name):
        # def __init__(self, first_name, last_name):
        def __init__(
            self, first_name, last_name,
            year_of_birth,
        ):
            return None

        # def say_hello():
        def say_hello(person):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.say_hello() takes 1 positional argument
        but 2 were given

  because :ref:`methods<what is a method?>` take the copy of the :ref:`class<everything is an object>` (``self``) they belong to as the first argument.

----

=================================================================================
what is the staticmethod decorator?
=================================================================================

----

* I can use the `staticmethod decorator`_ if I do not want to add ``self`` to the :ref:`method definition<how to make a function>` when it does not use anything in the :ref:`class<everything is an object>` that way I am not sending more information than what the :ref:`method<what is a method?>` needs. I add ``@staticmethod`` to ``say_hello``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 15

    class Person:

        # pass
        # def __init__():
        # def __init__(first_name):
        # def __init__(self, first_name):
        # def __init__(self, first_name, last_name):
        def __init__(
            self, first_name, last_name,
            year_of_birth,
        ):
            return None

        # def say_hello():
        @staticmethod
        def say_hello(person):
            return None

  the test passes. I can call :ref:`methods<what is a method?>` from outside the :ref:`class<everything is an object>` they belong to.

  * I made a copy of the ``Person`` :ref:`class<everything is an object>` named ``joe``
  * I called the :ref:`say_hello method<test_classy_person_says_hello>` of the ``Person`` :ref:`class<everything is an object>` with ``joe`` (which is a copy of the ``Person`` :ref:`class<everything is an object>`) as input. Confused? It is confusing and there is a better way.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

I want the :ref:`say_hello method<test_classy_person_says_hello>` of the ``Person`` :ref:`class<everything is an object>` to return a string_ for the person it receives, the same way the ``say_hello`` :ref:`function<what is a function?>` returns a string_ for the person (:ref:`dictionary<what is a dictionary?>`) it receives as input

* I change ``my_expectation`` to an :ref:`f-string<what is string interpolation?>` in :ref:`test_classy_person_says_hello` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 10-14

        def test_classy_person_says_hello(self):
            joe = src.person.Person(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )

            # reality = src.person.say_hello(joe)
            reality = src.person.Person.say_hello(joe)
            # my_expectation = None
            my_expectation = (
                'Hello, my name is joe blow and I am'
                f' {calculate_age(1996)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'Hello, my name is joe blow and I am 30'

* I copy the value from the terminal_ and paste it in the :ref:`return statement<the return statement>` for the :ref:`say_hello method<test_classy_person_says_hello>` of the ``Person`` :ref:`class<everything is an object>` in ``person.py``

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 4-5

        # def say_hello():
        @staticmethod
        def say_hello(person):
            # return None
            return 'Hello, my name is joe blow and I am 30'

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the next person to :ref:`test_classy_person_says_hello` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 10-14, 16-21
    :emphasize-text: Person jane

            # reality = src.person.say_hello(joe)
            reality = src.person.Person.say_hello(joe)
            # my_expectation = None
            my_expectation = (
                'Hello, my name is joe blow and I am'
                f' {calculate_age(1996)}'
            )
            self.assertEqual(reality, my_expectation)

            jane = src.person.Person(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )

            reality = src.person.Person.say_hello(jane)
            my_expectation = (
                'Hello, my name is jane doe and I am'
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

* I add ``sex`` to the :ref:`definition<how to make a function>` of the :ref:`__init__ method<the constructor method>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 10-11
    :emphasize-text: sex

    class Person:

        # pass
        # def __init__():
        # def __init__(first_name):
        # def __init__(self, first_name):
        # def __init__(self, first_name, last_name):
        def __init__(
            self, first_name, last_name,
            # year_of_birth,
            year_of_birth, sex,
        ):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() missing
        1 required positional argument: 'sex'

  because when the test calls the ``Person`` :ref:`object<everything is an object>` to make ``joe`` it does not provide a value for ``sex`` which I just made a required argument when I added it to the ``__init__`` :ref:`method definition<how to make a function>`, I have to make it a choice

* I add a default value for ``sex`` to make it optional

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 4-5

        def __init__(
            self, first_name, last_name,
            # year_of_birth,
            # year_of_birth, sex,
            year_of_birth, sex=None,
        ):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() missing
        1 required positional argument: 'last_name'

  because when the test calls the ``Person`` :ref:`object<everything is an object>` to make ``jane`` it does not provide a value for ``last_name`` which is a required argument, I have to make it a choice as well

* I add a default value for ``last_name`` to make it optional

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2-3

        def __init__(
            # self, first_name, last_name,
            self, first_name, last_name=None,
            # year_of_birth,
            # year_of_birth, sex,
            year_of_birth, sex=None,
        ):
            return None

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows
                 parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I add a default value for ``year_of_birth`` to make it optional

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 6-7

        def __init__(
            # self, first_name, last_name,
            self, first_name, last_name=None,
            # year_of_birth,
            # year_of_birth, sex,
            # year_of_birth, sex=None,
            year_of_birth=None, sex=None,
        ):
            return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
          'Hello, my name is joe blow and I am 30'
       != 'Hello, my name is jane doe and I am 35'

  Progress. I can make the ``say_hello`` :ref:`function<what is a function?>` use :ref:`attributes<what is a class attribute?>` of the person it receives as input to make the message.

* I change the string_ in the :ref:`return statement<the return statement>` of the ``say_hello`` :ref:`method<what is a function?>` of the ``Person`` :ref:`class<everything is an object>` to an :ref:`f-string<what is string interpolation?>` with the ``first_name`` :ref:`attribute<what is a class attribute?>` of the person it receives, in ``person.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 5-9

        # def say_hello():
        @staticmethod
        def say_hello(person):
            # return None
            # return 'Hello, my name is joe blow and I am 30'
            return (
                f'Hello, my name is {person.first_name} blow'
                ' and I am 30'
            )

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError:
        'Person' object has no attribute 'first_name'

  because there is no definition for ``first_name`` in the ``Person`` :ref:`class definition<how to make a class>`

* I add an :ref:`attribute<what is a class attribute?>` to the ``Person`` :ref:`class<everything is an object>` for ``first_name``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3

    class Person:

        first_name = 'jane'

        # pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hello, my name is jane blow and I am 30'
     != 'Hello, my name is joe blow and I am 30'

  because I used a fixed value (``jane``) and the first :ref:`assertion<what is an assertion?>` of the test expects ``joe``. I have to get the value from the :ref:`object<everything is an object>` that is passed to the ``say_hello`` :ref:`method<what is a function?>`.

* I add a :ref:`variable<what is a variable?>` to the :ref:`__init__ method<the constructor method>` to use it to allow changing the ``first_name`` :ref:`attribute<what is a class attribute?>` anytime a copy of the ``Person`` :ref:`class<everything is an object>` is made

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 18

    class Person:

        first_name = 'jane'

        # pass
        # def __init__():
        # def __init__(first_name):
        # def __init__(self, first_name):
        # def __init__(self, first_name, last_name):
        def __init__(
            # self, first_name, last_name,
            self, first_name, last_name=None,
            # year_of_birth,
            # year_of_birth, sex,
            # year_of_birth, sex=None,
            year_of_birth=None, sex=None,
        ):
            first_name = first_name
            return None

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hello, my name is jane blow and I am 30'
     != 'Hello, my name is joe blow and I am 30'

* I change the :ref:`variable<what is a variable?>` to a :ref:`class attribute<what is a class attribute?>` by adding ``self.`` before it

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 9-10

        def __init__(
            # self, first_name, last_name,
            self, first_name, last_name=None,
            # year_of_birth,
            # year_of_birth, sex,
            # year_of_birth, sex=None,
            year_of_birth=None, sex=None,
        ):
            # first_name = first_name
            self.first_name = first_name
            return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-text: doe blow 30 35

    AssertionError:
        'Hello, my name is jane blow and I am 30'
     != 'Hello, my name is jane doe and I am 35'

  the first names are the same, the last names and ages are different

----

* I add the ``last_name`` :ref:`attribute<what is a class attribute?>` to the string_ in the :ref:`return statement<the return statement>` of the ``say_hello`` :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 7-9

        # def say_hello():
        @staticmethod
        def say_hello(person):
            # return None
            # return 'Hello, my name is joe blow and I am 30'
            return (
                # f'Hello, my name is {person.first_name} blow'
                f'Hello, my name is {person.first_name}'
                f' {person.last_name}'
                ' and I am 30'
            )

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Person' object has no attribute 'last_name'.
        Did you mean: 'first_name'?

  because there is no definition for ``last_name`` in the ``Person`` :ref:`class definition<how to make a class>`

* I add an :ref:`attribute<what is a class attribute?>` to the ``Person`` :ref:`class<everything is an object>` for ``last_name``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4

    class Person:

        first_name = 'jane'
        last_name = 'doe'

        # pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hello, my name is joe doe and I am 30'
     != 'Hello, my name is joe blow and I am 30'

  because I used a fixed value (``doe``) and the first :ref:`assertion<what is an assertion?>` of the test expects ``blow``. I have to get the value from the :ref:`object<everything is an object>` that is passed to the ``say_hello`` :ref:`method<what is a function?>`.

* I add a :ref:`variable<what is a variable?>` to the :ref:`__init__ method<the constructor method>` to use it to allow changing the ``last_name`` :ref:`attribute<what is a class attribute?>` anytime a copy of the ``Person`` :ref:`class<everything is an object>` is made

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 16

        # pass
        # def __init__():
        # def __init__(first_name):
        # def __init__(self, first_name):
        # def __init__(self, first_name, last_name):
        def __init__(
            # self, first_name, last_name,
            self, first_name, last_name=None,
            # year_of_birth,
            # year_of_birth, sex,
            # year_of_birth, sex=None,
            year_of_birth=None, sex=None,
        ):
            # first_name = first_name
            self.first_name = first_name
            last_name = last_name
            return None

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hello, my name is joe doe and I am 30'
     != 'Hello, my name is joe blow and I am 30'

* I change ``last_name`` to a :ref:`class attribute<what is a class attribute?>` in the :ref:`__init__ method<the constructor method>` by adding ``self.`` before it

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 11-12

        def __init__(
            # self, first_name, last_name,
            self, first_name, last_name=None,
            # year_of_birth,
            # year_of_birth, sex,
            # year_of_birth, sex=None,
            year_of_birth=None, sex=None,
        ):
            # first_name = first_name
            self.first_name = first_name
            # last_name = last_name
            self.last_name = last_name
            return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-text: doe blow 30 35

    AssertionError:
        'Hello, my name is jane None and I am 30'
     != 'Hello, my name is jane doe and I am 35'

  - the first names are the same and last names and ages are different
  - the :ref:`__init__ method<the constructor method>` used :ref:`None<what is None?>` for the value of ``self.last_name`` because the :ref:`default value<test_optional_arguments>` for the ``last_name`` parameter of the :ref:`method<what is a method?>` is :ref:`None<what is None?>`. This means that

    .. code-block:: python

      src.person.Person(
          first_name='jane',
          sex='F',
          year_of_birth=1991,
      )

    is the same as

    .. code-block:: python

      src.person.Person.__init__(
          first_name='jane',
          sex='F',
          year_of_birth=1991,
          last_name=None,
      )

    because :ref:`a method uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I change the :ref:`default value<test_optional_arguments>` for ``last_name`` in the :ref:`__init__ method<the constructor method>` to ``'doe'`` to give the test what it wants

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 3-4

        def __init__(
            # self, first_name, last_name,
            # self, first_name, last_name=None,
            self, first_name, last_name='doe',
            # year_of_birth,
            # year_of_birth, sex,
            # year_of_birth, sex=None,
            year_of_birth=None, sex=None,
        ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-text: 30 35

    AssertionError:
        'Hello, my name is jane doe and I am 30'
     != 'Hello, my name is jane doe and I am 35'

  the age is the only thing that is different

----

* I add a calculation for the age with the ``year_of_birth`` :ref:`attribute<what is a class attribute?>` to the :ref:`return statement<the return statement>` of the ``say_hello`` :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 4-7, 14-15

        # def say_hello():
        @staticmethod
        def say_hello(person):
            age = (
                datetime.datetime.today().year
              - person.year_of_birth
            )
            # return None
            # return 'Hello, my name is joe blow and I am 30'
            return (
                # f'Hello, my name is {person.first_name} blow'
                f'Hello, my name is {person.first_name}'
                f' {person.last_name}'
                # f' and I am 30'
                f' and I am {age}'
            )

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Person' object has no attribute 'year_of_birth'

  because there is no definition for ``year_of_birth`` in the ``Person`` :ref:`class definition<how to make a class>`

* I add an :ref:`attribute<what is a class attribute?>` to the ``Person`` :ref:`class<everything is an object>` for ``year_of_birth``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 5

    class Person:

        first_name = 'jane'
        last_name = 'doe'
        year_of_birth = 1991

        # pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hello, my name is joe blow and I am 35'
     != 'Hello, my name is joe blow and I am 30'

  because I used a fixed value (``1991``) and the first :ref:`assertion<what is an assertion?>` of the test expects ``datetime.datetime.now().year-1996``. I have to get the value from the :ref:`object<everything is an object>` that is passed to the ``say_hello`` :ref:`method<what is a function?>`.

* I add a :ref:`variable<what is a variable?>` to the :ref:`__init__ method<the constructor method>` to use it to allow changing the ``year_of_birth`` :ref:`attribute<what is a class attribute?>` anytime a copy of the ``Person`` :ref:`class<everything is an object>` is made

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 16

        def __init__(
            # self, first_name, last_name,
            # self, first_name, last_name=None,
            self, first_name, last_name='doe',
            # year_of_birth,
            # year_of_birth, sex,
            # year_of_birth, sex=None,
            year_of_birth=None, sex=None,
        ):
            # first_name = first_name
            self.first_name = first_name
            # last_name = last_name
            self.last_name = last_name
            year_of_birth = year_of_birth
            return None

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hello, my name is joe blow and I am 35'
     != 'Hello, my name is joe blow and I am 30'

* I change ``year_of_birth`` to a :ref:`class attribute<what is a class attribute?>` in the :ref:`__init__ method<the constructor method>` by adding ``self.`` before it

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 14-15

        def __init__(
            # self, first_name, last_name,
            # self, first_name, last_name=None,
            self, first_name, last_name='doe',
            # year_of_birth,
            # year_of_birth, sex,
            # year_of_birth, sex=None,
            year_of_birth=None, sex=None,
        ):
            # first_name = first_name
            self.first_name = first_name
            # last_name = last_name
            self.last_name = last_name
            # year_of_birth = year_of_birth
            self.year_of_birth = year_of_birth
            return None

  the test passes. What a beautiful life.

* ``self.first_name``, ``self.last_name`` and ``self.year_of_birth`` are now defined twice in the :ref:`class<everything is an object>`. I remove the first definition since the :ref:`attributes<what is a class attribute?>` are also made in the :ref:`__init__ method<the constructor method>` and that gets called when copies of the ``Person`` :ref:`class<everything is an object>` are made, no need to have a default person be ``jane doe`` born in ``1991``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3-5

    class Person:

        # first_name = 'jane'
        # last_name = 'doe'
        # year_of_birth = 1991

        # pass

  the test is still green.

* ``datetime.datetime.today().year`` gets used to calculate the age in the :ref:`say_hello method<test_classy_person_says_hello>` of the ``Person`` :ref:`class<everything is an object>` and the :ref:`return statement<the return statement>` of the :ref:`factory function<test_factory_w_keyword_arguments>`. I make a helper :ref:`function<what is a function?>` to calculate the age, the same way I do in the tests

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-8

    import datetime


    def calculate_age(year_of_birth):
        return (
            datetime.datetime.today().year
          - year_of_birth
        )


    def say_hello(a_dictionary):

* I use the new :ref:`function<what is a function?>` for the age calculation in the :ref:`factory function<test_factory_w_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 9-13

    def factory(
            first_name, year_of_birth,
            last_name='doe', sex='M',
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            # 'age': (
            #     datetime.datetime.today().year
            #   - year_of_birth
            # ),
            'age': calculate_age(year_of_birth),
        }


    class Person:

  still green.

* I use the new :ref:`function<what is a function?>` for the age calculation in the :ref:`say_hello method<test_classy_person_says_hello>` of the ``Person`` :ref:`class<everything is an object>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 4-8

        # def say_hello():
        @staticmethod
        def say_hello(person):
            # age = (
            #     datetime.datetime.today().year
            #   - person.year_of_birth
            # )
            age = calculate_age(person.year_of_birth)
            # return None
            # return 'Hello, my name is joe blow and I am 30'
            return (
                # f'Hello, my name is {person.first_name} blow'
                f'Hello, my name is {person.first_name}'
                f' {person.last_name}'
                # f' and I am 30'
                f' and I am {age}'
            )

  green.

* The :ref:`say_hello method<test_classy_person_says_hello>` is in the ``Person`` :ref:`class<everything is an object>`, there is no need for it to take a copy of the ``Person`` :ref:`class<everything is an object>` as input since it should be able to access the :ref:`attributes<what is a class attribute?>` of the :ref:`class<everything is an object>` it belongs to. I change ``person.`` to ``self.`` to use :ref:`class attributes<what is a class attribute?>` instead

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 8-9, 14-15, 17-18

        # def say_hello():
        @staticmethod
        def say_hello(person):
            # age = (
            #     datetime.datetime.today().year
            #   - person.year_of_birth
            # )
            # age = calculate_age(person.year_of_birth)
            age = calculate_age(self.year_of_birth)
            # return None
            # return 'Hello, my name is joe blow and I am 30'
            return (
                # f'Hello, my name is {person.first_name} blow'
                # f'Hello, my name is {person.first_name}'
                # f' {person.last_name}'
                # f' and I am 30'
                f'Hello, my name is {self.first_name}'
                f' {self.last_name}'
                f' and I am {age}'
            )

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I change the name of the input parameter from ``person`` to ``self``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3-4

        # def say_hello():
        @staticmethod
        # def say_hello(person):
        def say_hello(self):

  the test is green again.

* I remove the `staticmethod decorator`_ because I no longer need it since the :ref:`say_hello method<test_classy_person_says_hello>` is using :ref:`class attributes<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2

        # def say_hello():
        # @staticmethod
        # def say_hello(person):
        def say_hello(self):

  the test is still green.

* I change the call to ``src.person.say_hello(joe)`` for ``joe`` because I can call :ref:`methods<what is a method?>` directly from a copy of a :ref:`class<everything is an object>`, in :ref:`test_classy_person_says_hello` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 3-4

            # reality = src.person.say_hello(joe)
            # reality = src.person.Person.say_hello(joe)
            reality = joe.say_hello()
            # my_expectation = None
            my_expectation = (
                'Hello, my name is joe blow and I am'
                f' {calculate_age(1996)}'
            )
            self.assertEqual(reality, my_expectation)

            jane = src.person.Person(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )

  still green.

* I change the call to ``src.person.say_hello(joe)`` for ``jane`` as well

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 7-8

            jane = src.person.Person(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )

            # reality = src.person.Person.say_hello(jane)
            reality = jane.say_hello()
            my_expectation = (
                'Hello, my name is jane doe and I am'
                f' {calculate_age(1991)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  green.

* I add an :ref:`assertion<what is an assertion?>` for the next person

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 9-13, 15-20
    :emphasize-text: Person john

            # reality = src.person.Person.say_hello(jane)
            reality = jane.say_hello()
            my_expectation = (
                'Hello, my name is jane doe and I am'
                f' {calculate_age(1991)}'
            )
            self.assertEqual(reality, my_expectation)

            john = src.person.Person(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )

            reality = john.say_hello()
            my_expectation = (
                'Hello, my name is jane doe and I am'
                f' {calculate_age(1991)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hello, my name is john smith and I am 446'
     != 'Hello, my name is jane doe and I am 35'

* I change ``my_expectation`` to match ``reality`` for ``john``

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 3-6

            reality = john.say_hello()
            my_expectation = (
                # 'Hello, my name is jane doe and I am'
                # f' {calculate_age(1991)}'
                'Hello, my name is john smith and I am'
                f' {calculate_age(1580)}'
            )
            self.assertEqual(reality, my_expectation)

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``mary``

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 10-15, 17-22
    :emphasize-text: Person a_person

            reality = john.say_hello()
            my_expectation = (
                # 'Hello, my name is jane doe and I am'
                # f' {calculate_age(1991)}'
                'Hello, my name is john smith and I am'
                f' {calculate_age(1580)}'
            )
            self.assertEqual(reality, my_expectation)

            mary = src.person.Person(
                first_name='mary',
                last_name='public',
                year_of_birth=2000,
                sex='F',
            )

            reality = a_person.say_hello()
            my_expectation = (
                'Hello, my name is john smith and I am'
                f' {calculate_age(1580)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hello, my name is mary public and I am 26'
     != 'Hello, my name is john smith and I am 446'

* I change ``my_expectation`` to match ``reality`` for ``mary``

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 10-11

            mary = src.person.Person(
                first_name='mary',
                last_name='public',
                year_of_birth=2000,
                sex='F',
            )

            reality = a_person.say_hello()
            my_expectation = (
                'Hello, my name is mary public and I am'
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

* I go back to the terminal_ where the tests are running

* I add :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 2-3, 5-6

        def test_classy_person_says_hello(self):
            first_name = 'joe'
            last_name = 'blow'

            year_of_birth = 1996
            age = calculate_age(year_of_birth)

            joe = src.person.Person(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``'joe'``, ``'blow'`` and ``1996``

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 2-7, 15-18

            joe = src.person.Person(
                # first_name='joe',
                # last_name='blow',
                # year_of_birth=1996,
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            # reality = src.person.say_hello(joe)
            # reality = src.person.Person.say_hello(joe)
            reality = joe.say_hello()
            # my_expectation = None
            my_expectation = (
                # 'Hello, my name is joe blow and I am'
                # f' {calculate_age(1996)}'
                f'Hello, my name is {first_name} {last_name}'
                f' and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

  the test is still green.

* I add :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 13-14, 16-17

            # reality = src.person.say_hello(joe)
            # reality = src.person.Person.say_hello(joe)
            reality = joe.say_hello()
            # my_expectation = None
            my_expectation = (
                # 'Hello, my name is joe blow and I am'
                # f' {calculate_age(1996)}'
                f'Hello, my name is {first_name} {last_name}'
                f' and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'jane'
            last_name = 'doe'

            year_of_birth = 1991
            age = calculate_age(year_of_birth)

            jane = src.person.Person(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )


* I use the :ref:`variables<what is a variable?>` to remove repetition of ``'jane'`` and ``1991``

  .. code-block:: python
    :lineno-start: 126
    :emphasize-lines: 2, 4-6, 12-15

            jane = src.person.Person(
                # first_name='jane',
                sex='F',
                # year_of_birth=1991,
                first_name=first_name,
                year_of_birth=year_of_birth,
            )

            # reality = src.person.Person.say_hello(jane)
            reality = jane.say_hello()
            my_expectation = (
                # 'Hello, my name is jane doe and I am'
                # f' {calculate_age(1991)}'
                f'Hello, my name is {first_name} {last_name}'
                f' and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            john = src.person.Person(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )

  the test is still green.

* I do the same thing with ``john``

  .. code-block:: python
    :lineno-start: 134
    :emphasize-lines: 11-12, 14-15, 18-23, 30-33

            # reality = src.person.Person.say_hello(jane)
            reality = jane.say_hello()
            my_expectation = (
                # 'Hello, my name is jane doe and I am'
                # f' {calculate_age(1991)}'
                f'Hello, my name is {first_name} {last_name}'
                f' and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'john'
            last_name = 'smith'

            year_of_birth = 1580
            age = calculate_age(year_of_birth)

            john = src.person.Person(
                # first_name='john',
                # last_name='smith',
                # year_of_birth=1580,
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = john.say_hello()
            my_expectation = (
                # 'Hello, my name is jane doe and I am'
                # f' {calculate_age(1991)}'
                # 'Hello, my name is john smith and I am'
                # f' {calculate_age(1580)}'
                f'Hello, my name is {first_name} {last_name}'
                f' and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

  the test is still green.

* I do the same thing with ``mary``

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 12-13, 15-16, 19-24, 32-35

            reality = john.say_hello()
            my_expectation = (
                # 'Hello, my name is jane doe and I am'
                # f' {calculate_age(1991)}'
                # 'Hello, my name is john smith and I am'
                # f' {calculate_age(1580)}'
                f'Hello, my name is {first_name} {last_name}'
                f' and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'mary'
            last_name = 'public'

            year_of_birth = 2000
            age = calculate_age(year_of_birth)

            mary = src.person.Person(
                # first_name='mary',
                # last_name='public',
                # year_of_birth=2000,
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
                sex='F',
            )

            reality = a_person.say_hello()
            my_expectation = (
                # 'Hello, my name is john smith and I am'
                # f' {calculate_age(1580)}'
                # 'Hello, my name is mary public and I am'
                # f' {calculate_age(2000)}'
                f'Hello, my name is {first_name} {last_name}'
                f' and I am {age}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green

* I can add a random person with random values for the ``first_name``, ``last_name`` and ``age`` :ref:`variables<what is a variable?>` that are sent in the call to ``src.person.Person`` to replace ``joe``, ``jane``, ``john`` and ``mary`` since they are all made the same way

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 2-3, 5-6, 8-12, 14-16

        def test_classy_person_says_hello(self):
            first_name = get_random_name()
            last_name = get_random_name()

            year_of_birth = get_random_year_of_birth()
            age = calculate_age(year_of_birth)

            a_random_person = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = a_random_person.say_hello()
            my_expectation = ''
            self.assertEqual(reality, my_expectation)

            first_name = 'joe'
            last_name = 'blow'

  the terminal_ is my friend and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Hello, my name is Z Y and I am X' != ''

* I change ``my_expectation`` to match ``reality`` for ``a_random_person``

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 2-6

            reality = a_random_person.say_hello()
            # my_expectation = ''
            my_expectation = (
                f'Hello, my name is {first_name} {last_name}'
                f' and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

  the test passes.

* I remove the commented lines and the other people from :ref:`test_classy_person_says_hello` because ``a_random_person`` covers their cases

  .. code-block:: python
    :lineno-start: 91

        def test_classy_person_says_hello(self):
            first_name = get_random_name()
            last_name = get_random_name()

            year_of_birth = get_random_year_of_birth()
            age = calculate_age(year_of_birth)

            a_random_person = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = a_random_person.say_hello()
            my_expectation = (
                f'Hello, my name is {first_name} {last_name}'
                f' and I am {age}'
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

I make the values for ``first_name`` in the tests the same way each time, since ``TestPerson`` is a :ref:`class<everything is an object>`, I can use a :ref:`class attribute<what is a class attribute?>` to remove repetition of how I make it, then have all the :ref:`methods<what is a method?>` reference it

* I go back to the terminal_ where the tests are running

* I add a :ref:`class attribute<what is a class attribute?>` called ``random_first_name`` to the ``TestPerson`` :ref:`object<everything is an object>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 3

    class TestPerson(unittest.TestCase):

        random_first_name = get_random_name()

        def test_factory_w_keyword_arguments(self):

* I use the new :ref:`class attribute<what is a class attribute?>` in :ref:`test_factory_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 5-6

        def test_factory_w_keyword_arguments(self):
            year_of_birth = get_random_year_of_birth()

            a_person = dict(
                # first_name=get_random_name(),
                first_name=self.random_first_name,
                last_name=get_random_name(),
                sex=pick_one('F', 'M'),
            )

  the test is still green.

* I use the new :ref:`class attribute<what is a class attribute?>` in :ref:`test_factory_w_optional_arguments`

  .. code-block:: python
    :lineno-start: 56
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
    :lineno-start: 75
    :emphasize-lines: 2-3, 11-12, 20-22

        def test_factory_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            last_name = get_random_name()
            sex = pick_one('F', 'M')

            year_of_birth = get_random_year_of_birth()
            age = calculate_age(year_of_birth)

            a_random_person = src.person.factory(
                # first_name=first_name,
                first_name=self.random_first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(a_random_person)
            my_expectation = (
                # f'Hello, my name is {first_name} {last_name}'
                f'Hello, my name is {self.random_first_name}'
                f' {last_name}'
                f' and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

        def test_classy_person_says_hello(self):

  the test is still green.

* I use the new :ref:`class attribute<what is a class attribute?>` in :ref:`test_classy_person_says_hello`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 2-3, 10-11, 18-20

        def test_classy_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            last_name = get_random_name()

            year_of_birth = get_random_year_of_birth()
            age = calculate_age(year_of_birth)

            a_random_person = src.person.Person(
                # first_name=first_name,
                first_name=self.random_first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = a_random_person.say_hello()
            my_expectation = (
                # f'Hello, my name is {first_name} {last_name}'
                f'Hello, my name is {self.random_first_name}'
                f' {last_name}'
                f' and I am {age}'
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

I call the ``get_random_year_of_birth`` :ref:`function<what is a function?>` for ``year_of_birth`` in each test, since ``TestPerson`` is a :ref:`class<everything is an object>`, I can use a :ref:`class attribute<what is a class attribute?>` to remove repetition of those calls, then have all the :ref:`methods<what is a method?>` reference the value it returns

* I go back to the terminal_ where the tests are running

* I add a :ref:`class attribute<what is a class attribute?>` called ``random_year_of_birth`` to the ``TestPerson`` :ref:`object<everything is an object>`

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
    :emphasize-lines: 2-3, 14-15, 19-22

        def test_factory_w_keyword_arguments(self):
            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth

            a_person = dict(
                # first_name=get_random_name(),
                first_name=self.random_first_name,
                last_name=get_random_name(),
                sex=pick_one('F', 'M'),
            )

            reality = src.person.factory(
                **a_person,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )
            my_expectation = dict(
                **a_person,
                # age=calculate_age(year_of_birth),
                age=calculate_age(
                    self.random_year_of_birth
                ),
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_w_optional_arguments(self):

  still green.

* I use ``self.random_year_of_birth`` in :ref:`test_factory_w_optional_arguments`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 4-5, 10-11, 18-21

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
                age=calculate_age(
                    self.random_year_of_birth
                ),
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_person_says_hello(self):

  still green.

* I use ``self.random_year_of_birth`` in :ref:`test_factory_person_says_hello`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 7-10, 17-18

        def test_factory_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            last_name = get_random_name()
            sex = pick_one('F', 'M')

            # year_of_birth = get_random_year_of_birth()
            # age = calculate_age(year_of_birth)
            year_of_birth = self.random_year_of_birth
            age = calculate_age(self.random_year_of_birth)

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
                # f'Hello, my name is {first_name} {last_name}'
                f'Hello, my name is {self.random_first_name}'
                f' {last_name}'
                f' and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

        def test_classy_person_says_hello(self):

  still green.

* I use ``self.random_year_of_birth`` in :ref:`test_classy_person_says_hello`

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 6-9, 15-16

        def test_classy_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            last_name = get_random_name()

            # year_of_birth = get_random_year_of_birth()
            # age = calculate_age(year_of_birth)
            year_of_birth = self.random_year_of_birth
            age = calculate_age(self.random_year_of_birth)

            a_random_person = src.person.Person(
                # first_name=first_name,
                first_name=self.random_first_name,
                last_name=last_name,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )

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

* I go back to the terminal_ where the tests are running

* I add a :ref:`class attribute<what is a class attribute?>` called ``random_last_name`` to the ``TestPerson`` :ref:`object<everything is an object>`

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
    :emphasize-lines: 8-9

        def test_factory_w_keyword_arguments(self):
            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth

            a_person = dict(
                # first_name=get_random_name(),
                first_name=self.random_first_name,
                # last_name=get_random_name(),
                last_name=self.random_last_name,
                sex=pick_one('F', 'M'),
            )

  green.

* I use ``self.random_last_name`` in :ref:`test_factory_person_says_hello`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 4-5, 16-17, 27-28

        def test_factory_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            # last_name = get_random_name()
            last_name = self.random_last_name
            sex = pick_one('F', 'M')

            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth
            # age = calculate_age(year_of_birth)
            age = calculate_age(self.random_year_of_birth)

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
                # f'Hello, my name is {first_name} {last_name}'
                f'Hello, my name is {self.random_first_name}'
                # f' {last_name}'
                f' {self.random_last_name}'
                f' and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

        def test_classy_person_says_hello(self):

  green.

* I use ``self.random_last_name`` in :ref:`test_classy_person_says_hello`

  .. code-block:: python
    :lineno-start: 120
    :emphasize-lines: 4-5, 15-16, 25-26

        def test_classy_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            # last_name = get_random_name()
            last_name = self.random_last_name

            # year_of_birth = get_random_year_of_birth()
            # age = calculate_age(year_of_birth)
            year_of_birth = self.random_year_of_birth
            age = calculate_age(self.random_year_of_birth)

            a_random_person = src.person.Person(
                # first_name=first_name,
                first_name=self.random_first_name,
                # last_name=last_name,
                last_name=self.random_last_name,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )

            reality = a_random_person.say_hello()
            my_expectation = (
                # f'Hello, my name is {first_name} {last_name}'
                f'Hello, my name is {self.random_first_name}'
                # f' {last_name}'
                f' {self.random_last_name}'
                f' and I am {age}'
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
extract age class attribute
*********************************************************************************

I call the ``calculate_age`` :ref:`function<what is a function?>` with the ``self.random_year_of_birth`` :ref:`attribute<what is a class attribute?>` in each test, since ``TestPerson`` is a :ref:`class<everything is an object>`, I can use a :ref:`class attribute<what is a class attribute?>` to remove repetition of those calls, then have all the :ref:`methods<what is a method?>` reference the value  it returns

* I go back to the terminal_ where the tests are running

* I add a :ref:`class attribute<what is a class attribute?>` called ``age`` to the ``TestPerson`` :ref:`object<everything is an object>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 6

    class TestPerson(unittest.TestCase):

        random_first_name = get_random_name()
        random_last_name = get_random_name()
        random_year_of_birth = get_random_year_of_birth()
        age = calculate_age(random_year_of_birth)

        def test_factory_w_keyword_arguments(self):

* I use ``self.age`` in :ref:`test_factory_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 9-12

            reality = src.person.factory(
                **a_person,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )
            my_expectation = dict(
                **a_person,
                # age=calculate_age(year_of_birth),
                # age=calculate_age(
                #     self.random_year_of_birth
                # ),
                age=self.age,
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_w_optional_arguments(self):

  still green.

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_factory_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 39

        def test_factory_w_keyword_arguments(self):
            a_person = dict(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                sex=pick_one('F', 'M'),
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
    :lineno-start: 62
    :emphasize-lines: 13-16

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
                # age=calculate_age(
                #     self.random_year_of_birth
                # ),
                age=self.age,
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_person_says_hello(self):

  still green.

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_factory_w_optional_arguments`

  .. code-block:: python
    :lineno-start: 56

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
    :lineno-start: 69
    :emphasize-lines: 11-12, 30-31

        def test_factory_person_says_hello(self):
            # first_name = get_random_name()
            first_name = self.random_first_name
            # last_name = get_random_name()
            last_name = self.random_last_name
            sex = pick_one('F', 'M')

            # year_of_birth = get_random_year_of_birth()
            year_of_birth = self.random_year_of_birth
            # age = calculate_age(year_of_birth)
            # age = calculate_age(self.random_year_of_birth)
            age = self.age

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
                # f'Hello, my name is {first_name} {last_name}'
                f'Hello, my name is {self.random_first_name}'
                # f' {last_name}'
                f' {self.random_last_name}'
                # f' and I am {age}'
                f' and I am {self.age}'
            )
            self.assertEqual(reality, my_expectation)

        def test_classy_person_says_hello(self):

  still green.

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_factory_person_says_hello`

  .. code-block:: python
    :lineno-start: 69

        def test_factory_person_says_hello(self):
            a_random_person = src.person.factory(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                year_of_birth=self.random_year_of_birth,
            )

            reality = src.person.say_hello(a_random_person)
            my_expectation = (
                f'Hello, my name is {self.random_first_name}'
                f' {self.random_last_name}'
                f' and I am {self.age}'
            )
            self.assertEqual(reality, my_expectation)

        def test_classy_person_says_hello(self):

  I remove the ``sex`` :ref:`variable<what is a variable?>` and parameter because it is not used in this test. I guess ``a_random_person`` is not all that random since it will always have ``'M'`` as ``sex`` in this test.

* I use ``self.age`` in :ref:`test_classy_person_says_hello`

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 4-5, 22-23

            # year_of_birth = get_random_year_of_birth()
            # age = calculate_age(year_of_birth)
            year_of_birth = self.random_year_of_birth
            # age = calculate_age(self.random_year_of_birth)
            age = self.age

            a_random_person = src.person.Person(
                # first_name=first_name,
                first_name=self.random_first_name,
                # last_name=last_name,
                last_name=self.random_last_name,
                # year_of_birth=year_of_birth,
                year_of_birth=self.random_year_of_birth,
            )

            reality = a_random_person.say_hello()
            my_expectation = (
                # f'Hello, my name is {first_name} {last_name}'
                f'Hello, my name is {self.random_first_name}'
                # f' {last_name}'
                f' {self.random_last_name}'
                # f' and I am {age}'
                f' and I am {self.age}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green.

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_classy_person_says_hello`

  .. code-block:: python
    :lineno-start: 84

        def test_classy_person_says_hello(self):
            a_random_person = src.person.Person(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                year_of_birth=self.random_year_of_birth,
            )

            reality = a_random_person.say_hello()
            my_expectation = (
                f'Hello, my name is {self.random_first_name}'
                f' {self.random_last_name}'
                f' and I am {self.age}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  I also do not need the ``sex`` :ref:`variable<what is a variable?>` and parameter in this test.

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

A problem with the current setup with the :ref:`class attributes<what is a class attribute?>` is that they are made once when the :ref:`class<everything is an object>` is initialized. This means that even though they all use random values, those values are created once and every test that references the values after that is using the exact same values for each test.

I want each test to get new random values every time they run and the :ref:`unittest.TestCase class<test_dir_unittest_testcase>` has a way to do that - the `setUp method`_, it runs before every test is run.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add the `unittest.TestCase.setUp method`_ to ``TestPerson`` then move the :ref:`class attributes<what is a class attribute?>` into it

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 3-6, 8-12

    class TestPerson(unittest.TestCase):

        # random_first_name = get_random_name()
        # random_last_name = get_random_name()
        # random_year_of_birth = get_random_year_of_birth()
        # age = calculate_age(random_year_of_birth)

        def setUp(self):
            random_first_name = get_random_name()
            random_last_name = get_random_name()
            random_year_of_birth = get_random_year_of_birth()
            age = calculate_age(random_year_of_birth)

        def test_factory_w_keyword_arguments(self):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    FAILED ...test_classy_person_says_hello -
        AttributeError: 'TestPerson' object has
        no attribute 'random_first_name'
    FAILED ...test_factory_person_says_hello -
        AttributeError: 'TestPerson' object has
        no attribute 'random_first_name'
    FAILED ...test_factory_w_keyword_arguments -
        AttributeError: 'TestPerson' object has
        no attribute 'random_first_name'
    FAILED ...test_factory_w_optional_arguments -
        AttributeError: 'TestPerson' object has
        no attribute 'random_first_name'

  because the ``first_name`` :ref:`variable<what is a variable?>` now belongs to the `setUp method`_, the other :ref:`methods<what is a method?>` have no way to reach it. I have to make it a :ref:`class attribute<what is a class attribute?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the ``first_name`` :ref:`variable<what is a variable?>` to a :ref:`class attribute<what is a class attribute?>` in the `setUp method`_ for the test :ref:`methods<what is a method?>` to be able to use it

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 2-3
    :emphasize-text: self

      def setUp(self):
          # random_first_name = get_random_name()
          self.random_first_name = get_random_name()
          random_last_name = get_random_name()
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
    FAILED ...test_factory_w_optional_arguments -
        AttributeError: 'TestPerson' object has
        no attribute 'random_year_of_birth'.

  because the ``year_of_birth`` and ``last_name`` :ref:`variables<what is a variable?>` now belong to the `setUp method`_, the other :ref:`methods<what is a method?>` have no way to reach them. I have to make them :ref:`class attributes<what is a class attribute?>`

* I change the ``year_of_birth`` and ``last_name`` :ref:`variables<what is a variable?>` to :ref:`class attributes<what is a class attribute?>` in the `setUp method`_ for the test :ref:`methods<what is a method?>` to be able to use them as well

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 4-13
    :emphasize-text: self

        def setUp(self):
            # random_first_name = get_random_name()
            self.random_first_name = get_random_name()
            # random_last_name = get_random_name()
            self.random_last_name = get_random_name()
            # random_year_of_birth = get_random_year_of_birth()
            # age = calculate_age(random_year_of_birth)
            self.random_year_of_birth = (
                get_random_year_of_birth()
            )
            age = calculate_age(
                self.random_year_of_birth
            )

        def test_factory_w_keyword_arguments(self):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    FAILED ...test_classy_person_says_hello -
        AttributeError: 'TestPerson' object has
        no attribute 'age'
    FAILED ...test_factory_person_says_hello -
        AttributeError: 'TestPerson' object has
        no attribute 'age'
    FAILED ...test_factory_w_keyword_arguments -
        AttributeError: 'TestPerson' object has
        no attribute 'age'
    FAILED ...test_factory_w_optional_arguments -
        AttributeError: 'TestPerson' object has
        no attribute 'age'

  because the ``age`` belongs to the `setUp method`_, and the other :ref:`methods<what is a method?>` have no way to reach it. I have to make it a :ref:`class attribute<what is a class attribute?>`

* I change the ``age`` :ref:`variable<what is a variable?>` to :ref:`class attributes<what is a class attribute?>` in the `setUp method`_ for the other :ref:`methods<what is a method?>` to be able to use it

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 11-12
    :emphasize-text: self

        def setUp(self):
            # random_first_name = get_random_name()
            self.random_first_name = get_random_name()
            # random_last_name = get_random_name()
            self.random_last_name = get_random_name()
            # random_year_of_birth = get_random_year_of_birth()
            # age = calculate_age(random_year_of_birth)
            self.random_year_of_birth = (
                get_random_year_of_birth()
            )
            # age = calculate_age(
            self.age = calculate_age(
                self.random_year_of_birth
            )

        def test_factory_w_keyword_arguments(self):

  the test passes.

The `unittest.TestCase.setUp method`_ runs before every test, in this case it sets these :ref:`class attributes (variables)<test_attribute_error_w_class_attributes>` to new values before every test

- ``self.random_first_name`` to the result of calling the ``get_random_name`` :ref:`function<what is a function?>`, which returns a random name
- ``self.random_last_name`` to the result of calling the ``get_random_name`` :ref:`function<what is a function?>`, which returns a random name
- ``self.random_year_of_birth`` to the result of calling the ``get_random_year_of_birth`` :ref:`function<what is a function?>` which returns a random year between 120 years ago and the current year
- ``self.age`` to the result of calling the ``calculate_age`` :ref:`function<what is a function?>`, which returns the current year minus ``self.random_year_of_birth``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I no longer need the :ref:`calculate_age function<extract calculate_age function>` because it is only called by the `setUp method`_. I use `datetime.datetime.now`_ directly

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 12-18

        def setUp(self):
            # random_first_name = get_random_name()
            self.random_first_name = get_random_name()
            # random_last_name = get_random_name()
            self.random_last_name = get_random_name()
            # random_year_of_birth = get_random_year_of_birth()
            # age = calculate_age(random_year_of_birth)
            self.random_year_of_birth = (
                get_random_year_of_birth()
            )
            # age = calculate_age(
            # self.age = calculate_age(
            #     self.random_year_of_birth
            # )
            self.age = (
                datetime.datetime.now().year
              - self.random_year_of_birth
            )

        def test_factory_w_keyword_arguments(self):

  the test is still green.

* I no longer need the :ref:`get_random_year_of_birth function<extract get_random_year_of_birth function>` because it is only called by the `setUp method`_. I use `random.randint`_ directly

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 8-14

        def setUp(self):
            # random_first_name = get_random_name()
            self.random_first_name = get_random_name()
            # random_last_name = get_random_name()
            self.random_last_name = get_random_name()
            # random_year_of_birth = get_random_year_of_birth()
            # age = calculate_age(random_year_of_birth)
            # self.random_year_of_birth = (
            #     get_random_year_of_birth()
            # )
            this_year = datetime.datetime.now().year
            self.random_year_of_birth = random.randint(
                this_year-120, this_year
            )
            # age = calculate_age(
            # self.age = calculate_age(
            #     self.random_year_of_birth
            # )
            self.age = (
                datetime.datetime.now().year
              - self.random_year_of_birth
            )

        def test_factory_w_keyword_arguments(self):

  still green.

* I use the ``this_year`` :ref:`variable<what is a variable?>` in the calculation for ``self.age``

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 19-23

        def setUp(self):
            # random_first_name = get_random_name()
            self.random_first_name = get_random_name()
            # random_last_name = get_random_name()
            self.random_last_name = get_random_name()
            # random_year_of_birth = get_random_year_of_birth()
            # age = calculate_age(random_year_of_birth)
            # self.random_year_of_birth = (
            #     get_random_year_of_birth()
            # )
            this_year = datetime.datetime.now().year
            self.random_year_of_birth = random.randint(
                this_year-120, this_year
            )
            # age = calculate_age(
            # self.age = calculate_age(
            #     self.random_year_of_birth
            # )
            # self.age = (
            #     datetime.datetime.now().year
            #   - self.random_year_of_birth
            # )
            self.age = this_year - self.random_year_of_birth

        def test_factory_w_keyword_arguments(self):

  green. ``datetime.datetime.now().year`` is now called once each time the `setUp method`_ runs

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 32

    class TestPerson(unittest.TestCase):

        def setUp(self):
            self.random_first_name = get_random_name()
            self.random_last_name = get_random_name()
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
test_dir_person_instance
*********************************************************************************

Python has the `dir built-in function`_ which shows the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the :ref:`object<everything is an object>` it is given in parentheses. It allows me to see what makes up an :ref:`object<everything is an object>` without looking at the code or reading the documentation. I can then run tests to see what each thing does.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a new test with the `dir built-in function`_ in ``test_person.py``

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 9-12

            reality = a_random_person.say_hello()
            my_expectation = (
                f'Hello, my name is {self.random_first_name}'
                f' {self.random_last_name}'
                f' and I am {self.age}'
            )
            self.assertEqual(reality, my_expectation)

        def test_dir_person_class(self):
            reality = dir(src.person.Person)
            my_expectation = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Lists differ:
        ['__class__', '__delattr__', '__dict__',
         '[377 chars]llo']
     != None

  because dir_ returned a :ref:`list <what is a list?>` (anything in square brackets ``[ ]``) and ``my_expectation`` is :ref:`None<what is None?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_ and paste (:kbd:`ctrl/command+v`) them as ``my_expectation``

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 3-7

        def test_dir_person_class(self):
            reality = dir(src.person.Person)
            # my_expectation = None
            my_expectation = [
                '__class__', '__delattr__', '__dict__',
                [371 chars]llo'
            ]
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    E       [371 chars]llo'
    E                     ^
    E   SyntaxError: unterminated string literal
                     (detected at line 94)

  because I have a closing :ref:`quote<quotes>` (``'``) without a matching opening one and :ref:`enclosures must be closed once open<enclosures>`

* I add the opening :ref:`quote<quotes>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 6

        def test_dir_person_class(self):
            reality = dir(src.person.Person)
            # my_expectation = None
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
    :lineno-start: 89
    :emphasize-lines: 4-37
    :emphasize-text: __init__ say_hello

        def test_dir_person_class(self):
            reality = dir(src.person.Person)
            # my_expectation = None
            # my_expectation = [
            #     '__class__', '__delattr__', '__dict__',
            #     '[371 chars]llo'
            # ]
            my_expectation = E       - ['__class__',
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

* I use the ``find and replace`` feature of the `Integrated Development Environment (IDE)`_ to remove the extra characters, then remove the commented lines

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 3-34
    :emphasize-text: __init__ say_hello

        def test_dir_person_class(self):
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

  - the test passes.
  - the ``__init__`` and ``say_hello`` :ref:`methods<what is a method?>` I defined are in the list
  - there are names in the list that I did not define, which leads to the question of :ref:`where did they come from?<family ties>`
  - The attributes I defined in the :ref:`__init__ method<the constructor method>` are not in the list, because the test called dir_ on ``src.person.Person`` which is the :ref:`class<everything is an object>`, not an instance (copy) of the class

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_dir_person_class'


----

*********************************************************************************
test_dir_person_class
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of an instance/copy of the ``Person`` :ref:`class<everything is an object>` to see the difference between it and the original

.. code-block:: python
  :lineno-start: 118
  :emphasize-lines: 8-14, 16-49

              '__str__',
              '__subclasshook__',
              '__weakref__',
              'say_hello',
          ]
          self.assertEqual(reality, my_expectation)

      def test_dir_person_instance(self):
          an_instance_of_person = src.person.Person(
              first_name=self.random_first_name,
              last_name=self.random_last_name,
              year_of_birth=self.random_year_of_birth,
              sex=pick_one('F', 'M')
          )

          reality = dir(an_instance_of_person)
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


  # Exceptions

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: Lists differ:
      ['__c[393 chars]ef__', 'first_name', 'last_name',
        'say_hello', 'year_of_birth']
   != ['__c[393 chars]ef__', 'say_hello']

because ``first_name``, ``last_name`` and ``year_of_birth`` are missing. Why is there no ``sex``?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the missing :ref:`attributes<what is an attribute?>` to ``my_expectation``

.. code-block:: python
  :lineno-start: 133
  :emphasize-lines: 32-33, 35

          reality = dir(an_instance_of_person)
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
              'first_name',
              'last_name',
              'say_hello',
              'year_of_birth',
          ]
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add ``sex`` to the list

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 35

            reality = dir(an_instance_of_person)
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
                'first_name',
                'last_name',
                'say_hello',
                'sex',
                'year_of_birth',
            ]
            self.assertEqual(reality, my_expectation)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Lists differ:
        ['__c[400 chars]'first_name', 'last_name',
         'say_hello', 'year_of_birth']
     != ['__c[400 chars]'first_name', 'last_name',
         'say_hello', 'sex', 'year_of_birth']

  the ``sex`` :ref:`attribute<what is a class attribute?>` is not defined anywhere in the ``Person`` :ref:`class<everything is an object>`

* I add ``self.sex`` to the :ref:`__init__ method<the constructor method>` of the ``Person`` :ref:`class<everything is an object>` in ``person.py``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 21

        # pass
        # def __init__():
        # def __init__(first_name):
        # def __init__(self, first_name):
        # def __init__(self, first_name, last_name):
        def __init__(
            # self, first_name, last_name,
            # self, first_name, last_name=None,
            self, first_name, last_name='doe',
            # year_of_birth,
            # year_of_birth, sex,
            # year_of_birth, sex=None,
            year_of_birth=None, sex=None,
        ):
            # first_name = first_name
            self.first_name = first_name
            # last_name = last_name
            self.last_name = last_name
            # year_of_birth = year_of_birth
            self.year_of_birth = year_of_birth
            self.sex = sex
            return None

  the test passes

* I remove the commented lines

  .. code-block:: python
    :linenos:

    import datetime


    def calculate_age(year_of_birth):
        return (
            datetime.datetime.today().year
          - year_of_birth
        )


    def say_hello(a_dictionary):
        return (
            f'Hello, my name is {a_dictionary.get("first_name")}'
            f' {a_dictionary.get("last_name")}'
            f' and I am {a_dictionary.get("age")}'
        )


    def factory(
            first_name, year_of_birth,
            last_name='doe', sex='M',
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': calculate_age(year_of_birth),
        }


    class Person:

        def __init__(
            self, first_name, last_name='doe',
            year_of_birth=None, sex=None,
        ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            self.sex = sex
            return None

        def say_hello(self):
            age = calculate_age(self.year_of_birth)
            return (
                f'Hello, my name is {self.first_name}'
                f' {self.last_name}'
                f' and I am {age}'
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_dir_person_instance'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_person.py`` and ``person.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``person``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<classes: tests and solutions>`

----

*************************************************************************************
review
*************************************************************************************

There are few problems with what I have now

* anyone seeing the tests for the first time has to read the :ref:`class attributes<what is a class attribute?>`

  .. code-block:: python

    class TestPerson(unittest.TestCase):

        def setUp(self):
            self.random_first_name = get_random_name()
            self.random_last_name = get_random_name()
            this_year = datetime.datetime.now().year
            self.random_year_of_birth = random.randint(
                this_year-120, this_year
            )
            self.age = this_year - self.random_year_of_birth

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

    f'Hello, my name is {self.random_first_name}'
    f' {self.random_last_name} '
    f'and I am {self.age}'

To review

* A :ref:`class<everything is an object>` is :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` that belong together
* A :ref:`class<everything is an object>` can be used to represent something
* A :ref:`class attributes<what is a class attribute?>` is a :ref:`variable<what is a variable?>` that belongs to a :ref:`class<everything is an object>`
* A :ref:`method<what is a method?>` is a :ref:`function<what is a function?>` that belongs to a :ref:`class<everything is an object>`
* :ref:`classes<everything is an object>` can be an easier way to manage data than :ref:`functions<what is a function?>`
* :ref:`classes<everything is an object>` make it easier to write tests for something

.. tip::

  * when I find myself writing or doing the same thing two times, I write a :ref:`function<what is a function?>`
  * when I find I have two :ref:`functions<what is a function?>` that use the same information, I write a :ref:`class<everything is an object>`

:ref:`How many questions can you answer about classes?<questions about classes>`

----

*************************************************************************************
what is next?
*************************************************************************************

You have gone through a lot of things and know:


* :ref:`I know how to make a Python test driven development environment manually<how to make a Python test driven development environment manually>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`how to use classes<classes>`

:ref:`Would you like to test what causes AttributeError<what causes AttributeError?>` or :ref:`Would you like to know where the extra attributes and methods of the Person class came from?<family ties>`

You know enough to go into the world and use Python_. If you stopped going through the book at this point, you would be fine because you know how to make :ref:`classes<everything is an object>`, :ref:`functions<what is a function?>` and can make :ref:`dictionaries<what is a dictionary?>` which is what is behind a lot of the things you will encounter.

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