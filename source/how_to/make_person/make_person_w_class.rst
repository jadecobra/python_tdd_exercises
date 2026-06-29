.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): how to make a person with f-strings. Use f-strings + one factory function (instead of one function per person) that takes first_name, last_name, sex, year_of_birth and returns 'name, surname, X, YYYY'. Add say_hi using f-strings for 'Hi, my name is ... and I am N.'. Start in the person project; uv run pytest-watcher . --now. Progressively introduce f-strings in the return, required args then keyword arguments, move factory and say_hi to src/person.py (AttributeError: module 'src.person' has no attribute 'factory'), use local variables in tests to remove repetition of the data, remove commented lines. Ends with 4 tests calling src.person.factory + src.person.say_hi + # Exceptions seen (AssertionError, NameError, TypeError, AttributeError). Shows why even with f-strings the 4 tests are repetitive. What is next: separate and equal functions. Code: person/tests/test_person_w_fstrings.py and person/solutions/person_w_fstrings.py.
  :keywords: Jacob Itegboje, Pumping Python, how to make a person with f-strings, python f-strings, f-string factory function, one function instead of one per person, src.person, import src.person, AttributeError module 'src.person' has no attribute 'factory', TypeError missing required positional argument, uv run pytest-watcher, red green refactor f-strings, variables remove repetition in tests, first_name last_name sex year_of_birth, say_hi f-string age 2026-year_of_birth, remove the commented lines, test_joe test_jane test_john test_mary, person factory with f-strings, separate tests and solution, what is next separate and equal functions

.. include:: ../../links.rst

.. _class: https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes
.. _classes: class_
.. _constructor: https://grokipedia.com/page/Constructor_(object-oriented_programming)
.. _constructor method: constructor_
.. _staticmethod: https://docs.python.org/3/library/functions.html#staticmethod
.. _staticmethod decorator: staticmethod_

#################################################################################
how to make a person with a class
#################################################################################

----

The :ref:`factory<test person factory>` and :ref:`say_hi functions<test say_hi>` use three of the same inputs

* ``first_name``
* ``last_name``
* ``year_of_birth``

I want to give those values once, and get a representation for a person. I can do that with a class_

*********************************************************************************
what is a class?
*********************************************************************************

I think of classes_ as :ref:`attributes (variables)<what is a class attribute?>` and :ref:`methods (functions) <what is a method?>` that belong together.

----

*********************************************************************************
what is a class attribute?
*********************************************************************************

A :ref:`class attribute<what is a class attribute?>` is a :ref:`variable<what is a variable?>` that belongs to a class_.

----

*********************************************************************************
what is a method?
*********************************************************************************

A :ref:`method<what is a method?>` is a :ref:`function<what is a function?>` that belongs to a class_.

----

*********************************************************************************
how to make a class
*********************************************************************************

classes_ are made with

* the class_ keyword
* a name in :ref:`CapWords format<CapWords>` that tells what the group of :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` does - naming things is its own challenge
* :ref:`attributes<what is a class attribute?>`
* :ref:`methods<what is a method?>`

.. code-block:: python

  class NameOfClass:

      attribute = SOMETHING

      def method():
          the body of the method
          return output

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_class.py
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

  the terminal_ shows I am in the ``person`` folder_

  .. code-block:: shell

    .../pumping_python/person

* I open ``test_person.py`` from the ``tests`` folder_

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    tests/test_person.py ....                           [100%]

    =================== 4 passed in A.BCs ====================

----

*********************************************************************************
test person class
*********************************************************************************

I made a :ref:`function<what is a function?>` that makes a string_ to represent a person when I give it ``first_name``, ``last_name``, ``sex`` and ``year_of_birth``. I can also represent a person with a :ref:`class<what is a class?>` because it is :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` that belong together.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add make a copy of a :ref:`class<what is a class?>` to represent ``joe`` in :ref:`test_joe` in ``test_person.py``

.. code-block:: python
  :lineno-start:

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 31-36
  :emphasize-text: Person

  def test_joe():
      first_name = 'joe'
      last_name = 'blow'
      sex = 'M'
      year_of_birth = 1996

      reality = src.person.factory(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )
      my_expectation = (
          f'{first_name}, {last_name},'
          f' {sex}, {year_of_birth}'
      )
      assert reality == my_expectation

      reality = src.person.say_hi(
          first_name=first_name,
          last_name=last_name,
          year_of_birth=year_of_birth,
      )
      my_expectation = (
          f'Hi, my name is {first_name}'
          f' {last_name} and I am'
          f' {2026-year_of_birth}.'
      )
      assert reality == my_expectation

      joe = Person(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )


  def test_jane():

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'Person' is not defined

because there is no definition for ``Person`` in ``test_person.py``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`class definition<how to make a class>` for ``Person``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4, 6

    import src.person


    class Person:

        pass


    def test_joe():

  - I can :ref:`make a class with the pass keyword<test_making_a_class_w_pass>`
  - the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

    .. code-block:: python

      TypeError: Person() takes no arguments

    because :ref:`classes<what is a class?>` do not take arguments like a :ref:`function<what is a function?>` without a :ref:`method<what is a method?>` that handles those arguments.

* I add a `constructor method`_ to the ``Person`` :ref:`class<what is a class?>` so it can take arguments, it is used to define how copies of the :ref:`class<what is a class?>` are made

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-5

    class Person:

        # pass
        def __init__():
            return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() got
        an unexpected keyword argument 'first_name'

  - because the :ref:`definition<how to make a function>` for ``__init__`` does not allow calling it with inputs (the parentheses are empty) and the test sends ``'first_name'`` as input.
  - A `constructor method`_ is used to handle arguments given when a copy of a  :ref:`class<what is a class?>` is made.
  - A `constructor method`_ is used to make copies of a :ref:`class<what is a class?>`.

* I add the name in parentheses so that the ``__init__`` `constructor method`_ can take input

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    class Person:

        # pass
        # def __init__():
        def __init__(first_name):
            return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() got
        multiple values for argument 'first_name'

  because the ``__init__`` `constructor method`_ takes the :ref:`instance (copy)<how to test if something is an instance of a class>` it belongs to as the first argument.

* I add ``self`` as the first argument

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5-6

    class Person:

        # pass
        # def __init__():
        # def __init__(first_name):
        def __init__(self, first_name):
            return None


    def test_joe():

  - ``self`` is Python_ convention, I can use any name I want.
  - The terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

    .. code-block:: shell

      TypeError:
          Person.__init__() got
          an unexpected keyword argument 'last_name'.
          Did you mean 'first_name'?

    I have seen this before, so far it is the same as making the :ref:`factory function<test person factory>`.

* I add ``last_name`` to the :ref:`definition<how to make a function>` of ``__init__``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 6-7

    class Person:

        # pass
        # def __init__():
        # def __init__(first_name):
        # def __init__(self, first_name):
        def __init__(self, first_name, last_name):
            return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() got
        an unexpected keyword argument 'year_of_birth'

  still the same as making the :ref:`factory function<test person factory>`.

* I add ``year_of_birth`` to the :ref:`definition<how to make a function>` of the ``__init__`` :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-11

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


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() got
               an unexpected keyword argument 'sex'

  same as with the :ref:`factory function<test person factory>`.

* I add ``sex`` to the :ref:`definition<how to make a function>` of the ``__init__`` `constructor method`_

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 10-11

    class Person:

        # pass
        # def __init__():
        # def __init__(first_name):
        # def __init__(self, first_name):
        # def __init__(self, first_name, last_name):
        def __init__(
            self, first_name, last_name,
            # year_of_birth,
            year_of_birth, sex
        ):
            return None


    def test_joe():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 4

    class Person:

        def __init__(
            self, first_name, last_name,
            year_of_birth, sex
        ):
            return None


    def test_joe():

* I open a new terminal_ then change directories to ``person``

  .. code-block:: python
    :emphasize-lines: 1

    cd person

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add Person class'

----

*********************************************************************************
test classy person say_hi
*********************************************************************************

I made a person :ref:`say hi with a function<test say_hi>`, I can also do the same thing with a :ref:`class<what is a class?>` because it is :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` that belong together.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` with a call to the :ref:`say_hi function<test say_hi>` with the :ref:`attributes<what is a class attribute?>` of ``joe`` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 8-13

        joe = Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = src.person.say_hi(
            first_name=joe.first_name,
            last_name=joe.last_name,
            year_of_birth=joe.year_of_birth,
        )
        assert reality == my_expectation


    def test_jane():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'first_name'

  because there is nothing named ``first_name`` in the ``Person`` :ref:`class<what is a class?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``self.first_name`` to the :ref:`definition<how to make a function>` of the ``__init__`` `constructor method`_

  .. code-block:: python

    class Person:

        def __init__(
            self, first_name, last_name,
            year_of_birth, sex
        ):
            self.first_name
            return None


    def test_joe():

  the terminal_ still shows :ref:`AttributeError<what causes AttributeError?>` because this is just a reference to the name, not a definition.

* I point ``self.first_name`` to the value for ``first_name`` when a



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

  because the test calls the ``say_hello`` :ref:`function<what is a function?>` which does not yet exist in the ``Person`` :ref:`class<what is a class?>`

* I add a :ref:`method definition<how to make a function>` for it to the ``Person`` :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
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
    :lineno-start: 4
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

  because :ref:`methods<what is a method?>` take the copy of the :ref:`class<what is a class?>` (``self``) they belong to as the first argument.

----

=================================================================================
what is the staticmethod decorator?
=================================================================================

----

* I can use the `staticmethod decorator`_ if I do not want to add ``self`` to the :ref:`method definition<how to make a function>` when it does not use anything in the :ref:`class<what is a class?>` that way I am not sending more information than what the :ref:`method<what is a method?>` needs. I add ``@staticmethod`` to ``say_hello``

  .. code-block:: python
    :lineno-start: 4
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

  the test passes. I can call :ref:`methods<what is a method?>` from outside the :ref:`class<what is a class?>` they belong to.

  * I made a copy of the ``Person`` :ref:`class<what is a class?>` named ``joe``
  * I called the :ref:`say_hello method<test_classy_person_says_hello>` of the ``Person`` :ref:`class<what is a class?>` with ``joe`` (which is a copy of the ``Person`` :ref:`class<what is a class?>`) as input. Confused? It is confusing and there is a better way.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

I want the :ref:`say_hello method<test_classy_person_says_hello>` of the ``Person`` :ref:`class<what is a class?>` to return a string_ for the person it receives, the same way the ``say_hello`` :ref:`function<what is a function?>` returns a string_ for the person (:ref:`dictionary<what is a dictionary?>`) it receives as input

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
                'Hi, my name is joe blow and I am'
                f' {calculate_age(1996)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'Hi, my name is joe blow and I am 30'

* I copy the value from the terminal_ and paste it in the :ref:`return statement<the return statement>` for the :ref:`say_hello method<test_classy_person_says_hello>` of the ``Person`` :ref:`class<what is a class?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 4-5

        # def say_hello():
        @staticmethod
        def say_hello(person):
            # return None
            return 'Hi, my name is joe blow and I am 30'

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
                'Hi, my name is joe blow and I am'
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
    :lineno-start: 4
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
          'Hi, my name is joe blow and I am 30'
       != 'Hi, my name is jane doe and I am 35'

  Progress. I can make the ``say_hello`` :ref:`function<what is a function?>` use :ref:`attributes<what is a class attribute?>` of the person it receives as input to make the message.

* I change the string_ in the :ref:`return statement<the return statement>` of the ``say_hello`` :ref:`method<what is a function?>` of the ``Person`` :ref:`class<what is a class?>` to an :ref:`f-string<what is string interpolation?>` with the ``first_name`` :ref:`attribute<what is a class attribute?>` of the person it receives, in ``person.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 5-9

        # def say_hello():
        @staticmethod
        def say_hello(person):
            # return None
            # return 'Hi, my name is joe blow and I am 30'
            return (
                f'Hi, my name is {person.first_name} blow'
                ' and I am 30'
            )

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError:
        'Person' object has no attribute 'first_name'

  because there is no definition for ``first_name`` in the ``Person`` :ref:`class definition<how to make a class>`

* I add an :ref:`attribute<what is a class attribute?>` to the ``Person`` :ref:`class<what is a class?>` for ``first_name``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    class Person:

        first_name = 'jane'

        # pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hi, my name is jane blow and I am 30'
     != 'Hi, my name is joe blow and I am 30'

  because I used a fixed value (``jane``) and the first :ref:`assertion<what is an assertion?>` of the test expects ``joe``. I have to get the value from the :ref:`object<everything is an object>` that is passed to the ``say_hello`` :ref:`method<what is a function?>`.

* I add a :ref:`variable<what is a variable?>` to the ``__init__`` :ref:`method<what is a method?>` to use it to allow changing the ``first_name`` :ref:`attribute<what is a class attribute?>` anytime a copy of the ``Person`` :ref:`class<what is a class?>` is made

  .. code-block:: python
    :lineno-start: 4
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
        'Hi, my name is jane blow and I am 30'
     != 'Hi, my name is joe blow and I am 30'

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
        'Hi, my name is jane blow and I am 30'
     != 'Hi, my name is jane doe and I am 35'

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
            # return 'Hi, my name is joe blow and I am 30'
            return (
                # f'Hi, my name is {person.first_name} blow'
                f'Hi, my name is {person.first_name}'
                f' {person.last_name}'
                ' and I am 30'
            )

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Person' object has no attribute 'last_name'.
        Did you mean: 'first_name'?

  because there is no definition for ``last_name`` in the ``Person`` :ref:`class definition<how to make a class>`

* I add an :ref:`attribute<what is a class attribute?>` to the ``Person`` :ref:`class<what is a class?>` for ``last_name``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4

    class Person:

        first_name = 'jane'
        last_name = 'doe'

        # pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hi, my name is joe doe and I am 30'
     != 'Hi, my name is joe blow and I am 30'

  because I used a fixed value (``doe``) and the first :ref:`assertion<what is an assertion?>` of the test expects ``blow``. I have to get the value from the :ref:`object<everything is an object>` that is passed to the ``say_hello`` :ref:`method<what is a function?>`.

* I add a :ref:`variable<what is a variable?>` to the ``__init__`` :ref:`method<what is a method?>` to use it to allow changing the ``last_name`` :ref:`attribute<what is a class attribute?>` anytime a copy of the ``Person`` :ref:`class<what is a class?>` is made

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
        'Hi, my name is joe doe and I am 30'
     != 'Hi, my name is joe blow and I am 30'

* I change ``last_name`` to a :ref:`class attribute<what is a class attribute?>` in the ``__init__`` :ref:`method<what is a method?>` by adding ``self.`` before it

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
        'Hi, my name is jane None and I am 30'
     != 'Hi, my name is jane doe and I am 35'

  - the first names are the same and last names and ages are different
  - the ``__init__`` :ref:`method<what is a method?>` used :ref:`None<what is None?>` for the value of ``self.last_name`` because the :ref:`default value<test_optional_arguments>` for the ``last_name`` parameter of the :ref:`method<what is a method?>` is :ref:`None<what is None?>`. This means that

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

* I change the :ref:`default value<test_optional_arguments>` for ``last_name`` in the ``__init__`` :ref:`method<what is a method?>` to ``'doe'`` to give the test what it wants

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
        'Hi, my name is jane doe and I am 30'
     != 'Hi, my name is jane doe and I am 35'

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
            # return 'Hi, my name is joe blow and I am 30'
            return (
                # f'Hi, my name is {person.first_name} blow'
                f'Hi, my name is {person.first_name}'
                f' {person.last_name}'
                # f' and I am 30'
                f' and I am {age}'
            )

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Person' object has no attribute 'year_of_birth'

  because there is no definition for ``year_of_birth`` in the ``Person`` :ref:`class definition<how to make a class>`

* I add an :ref:`attribute<what is a class attribute?>` to the ``Person`` :ref:`class<what is a class?>` for ``year_of_birth``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5

    class Person:

        first_name = 'jane'
        last_name = 'doe'
        year_of_birth = 1991

        # pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hi, my name is joe blow and I am 35'
     != 'Hi, my name is joe blow and I am 30'

  because I used a fixed value (``1991``) and the first :ref:`assertion<what is an assertion?>` of the test expects ``datetime.datetime.now().year-1996``. I have to get the value from the :ref:`object<everything is an object>` that is passed to the ``say_hello`` :ref:`method<what is a function?>`.

* I add a :ref:`variable<what is a variable?>` to the ``__init__`` :ref:`method<what is a method?>` to use it to allow changing the ``year_of_birth`` :ref:`attribute<what is a class attribute?>` anytime a copy of the ``Person`` :ref:`class<what is a class?>` is made

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
        'Hi, my name is joe blow and I am 35'
     != 'Hi, my name is joe blow and I am 30'

* I change ``year_of_birth`` to a :ref:`class attribute<what is a class attribute?>` in the ``__init__`` :ref:`method<what is a method?>` by adding ``self.`` before it

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

* ``self.first_name``, ``self.last_name`` and ``self.year_of_birth`` are now defined twice in the :ref:`class<what is a class?>`. I remove the first definition since the :ref:`attributes<what is a class attribute?>` are also made in the ``__init__`` :ref:`method<what is a method?>` and that gets called when copies of the ``Person`` :ref:`class<what is a class?>` are made, no need to have a default person be ``jane doe`` born in ``1991``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-5

    class Person:

        # first_name = 'jane'
        # last_name = 'doe'
        # year_of_birth = 1991

        # pass

  the test is still green.

* ``datetime.datetime.today().year`` gets used to calculate the age in the :ref:`say_hello method<test_classy_person_says_hello>` of the ``Person`` :ref:`class<what is a class?>` and the :ref:`return statement<the return statement>` of the :ref:`factory function<test person factory>`. I make a helper :ref:`function<what is a function?>` to calculate the age, the same way I do in the tests

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

* I use the new :ref:`function<what is a function?>` for the age calculation in the :ref:`factory function<test person factory>`

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

* I use the new :ref:`function<what is a function?>` for the age calculation in the :ref:`say_hello method<test_classy_person_says_hello>` of the ``Person`` :ref:`class<what is a class?>`

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
            # return 'Hi, my name is joe blow and I am 30'
            return (
                # f'Hi, my name is {person.first_name} blow'
                f'Hi, my name is {person.first_name}'
                f' {person.last_name}'
                # f' and I am 30'
                f' and I am {age}'
            )

  green.

* The :ref:`say_hello method<test_classy_person_says_hello>` is in the ``Person`` :ref:`class<what is a class?>`, there is no need for it to take a copy of the ``Person`` :ref:`class<what is a class?>` as input since it should be able to access the :ref:`attributes<what is a class attribute?>` of the :ref:`class<what is a class?>` it belongs to. I change ``person.`` to ``self.`` to use :ref:`class attributes<what is a class attribute?>` instead

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
            # return 'Hi, my name is joe blow and I am 30'
            return (
                # f'Hi, my name is {person.first_name} blow'
                # f'Hi, my name is {person.first_name}'
                # f' {person.last_name}'
                # f' and I am 30'
                f'Hi, my name is {self.first_name}'
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

* I change the call to ``src.person.say_hello(joe)`` for ``joe`` because I can call :ref:`methods<what is a method?>` directly from a copy of a :ref:`class<what is a class?>`, in :ref:`test_classy_person_says_hello` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 3-4

            # reality = src.person.say_hello(joe)
            # reality = src.person.Person.say_hello(joe)
            reality = joe.say_hello()
            # my_expectation = None
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
                'Hi, my name is jane doe and I am'
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
                'Hi, my name is jane doe and I am'
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
    :lineno-start: 128
    :emphasize-lines: 3-6

            reality = john.say_hello()
            my_expectation = (
                # 'Hi, my name is jane doe and I am'
                # f' {calculate_age(1991)}'
                'Hi, my name is john smith and I am'
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
                # 'Hi, my name is jane doe and I am'
                # f' {calculate_age(1991)}'
                'Hi, my name is john smith and I am'
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
                'Hi, my name is john smith and I am'
                f' {calculate_age(1580)}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hi, my name is mary public and I am 26'
     != 'Hi, my name is john smith and I am 446'

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
                'Hi, my name is mary public and I am'
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
BOOM
----

----
BOOM
----

----
BOOM
----

----
BOOM
----

*********************************************************************************
test_person
*********************************************************************************

Since the solutions are separate from the tests, I can write the programs_ that make the tests pass without looking at ``test_person.py``.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I close ``test_person.py``

* I delete all the text in ``person.py`` and the terminal_ shows 9 failures. I start with the last :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    FAILED ...::test_joe - AttributeError:
        module 'src.person' has no attribute 'factory'
    FAILED ...::test_jane - AttributeError:
        module 'src.person' has no attribute 'factory'
    FAILED ...::test_john - AttributeError:
        module 'src.person' has no attribute 'factory'
    FAILED ...::test_mary - AttributeError:
        module 'src.person' has no attribute 'factory'
    =================== 4 failed in A.BCs ===================

  Can you make the tests pass without looking at how I solve it below? You can come back to compare solutions when you are done or if you get stuck.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name to ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    factory

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'factory' is not defined

* I point ``factory`` to :ref:`None (the simplest object)<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # factory
    factory = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because ``factory`` points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I change ``factory`` to a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-4

    # factory
    # factory = None
    def factory():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() got
               an unexpected keyword argument
               'first_name'

  because this :ref:`function definition<how to make a function that takes input>` does not allow any inputs, the parentheses are empty.

* I add ``first_name`` in the parentheses so the :ref:`function<what is a function?>` can take input

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # factory
    # factory = None
    # def factory():
    def factory(first_name):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: factory() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

  because the :ref:`function definition<how to make a function that takes input>` now only allows one input (``first_name``) and it was called with a :ref:`keyword argument<test_keyword_arguments>` (``last_name``).

* I add ``last_name`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    # factory
    # factory = None
    # def factory():
    # def factory(first_name):
    def factory(first_name, last_name):
        return None


  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() got
               an unexpected keyword argument 'sex'

  because the :ref:`function definition<how to make a function that takes input>` only allows two inputs (``first_name`` and ``last_name``) and it was called with a :ref:`keyword argument<test_keyword_arguments>` (``sex``).

* I add ``sex`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    # factory
    # factory = None
    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(first_name, last_name, sex):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() got
               an unexpected keyword argument
               'year_of_birth'

  because the :ref:`function definition<how to make a function that takes input>` only allows three inputs (``first_name``, ``last_name``, ``sex``) and it was called with a :ref:`keyword argument<test_keyword_arguments>` (``year_of_birth``).

* I add ``year_of_birth`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-10

    # factory
    # factory = None
    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    # def factory(first_name, last_name, sex):
    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == 'mary, public, F, 2000'

* I change :ref:`the return statement` to match the expectation of the test

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-12

    # factory
    # factory = None
    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    # def factory(first_name, last_name, sex):
    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return 'mary, public, F, 2000'

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.person'
                    has no attribute 'say_hi'

* I add the name

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    say_hi


    # factory
    # factory = None
    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    # def factory(first_name, last_name, sex):
    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return 'mary, public, F, 2000'

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'say_hi' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # say_hi
    say_hi = None


    # factory

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because ``say_hi`` points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I make ``say_hi`` a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-4

    # say_hi
    # say_hi = None
    def say_hi():
        return None


    # factory

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: say_hi() got
               an unexpected keyword argument
               'first_name'

  because this :ref:`function definition<how to make a function that takes input>` does not allow any inputs, the parentheses are empty.

* I add ``first_name`` in the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # say_hi
    # say_hi = None
    # def say_hi():
    def say_hi(first_name):
        return None


    # factory

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: say_hi() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

  because the :ref:`function definition<how to make a function that takes input>` now only allows one input (``first_name``) and it was called with a :ref:`keyword argument<test_keyword_arguments>` (``last_name``).

* I add ``last_name`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    # say_hi
    # say_hi = None
    # def say_hi():
    # def say_hi(first_name):
    def say_hi(first_name, last_name):
        return None


    # factory

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: say_hi() got
               an unexpected keyword argument
               'year_of_birth'

  because the :ref:`function definition<how to make a function that takes input>` only allows two inputs (``first_name`` and ``last_name``) and it was called with a :ref:`keyword argument<test_keyword_arguments>` (``year_of_birth``).

* I add ``year_of_birth`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-8

    # say_hi
    # say_hi = None
    # def say_hi():
    # def say_hi(first_name):
    # def say_hi(first_name, last_name):
    def say_hi(
        first_name, last_name, year_of_birth
    ):
        return None


    # factory

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None
        == 'Hi, my name is mary public and I am 26.'

* I use :kbd:`ctrl/command+c` (Windows_ & Linux_/MacOS_) on the keyboard to copy the string_ from the terminal and :kbd:`ctrl/command+v` to paste it to replace :ref:`None<what is None?>` in :ref:`the return statement`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9-10

    # say_hi
    # say_hi = None
    # def say_hi():
    # def say_hi(first_name):
    # def say_hi(first_name, last_name):
    def say_hi(
        first_name, last_name, year_of_birth
    ):
        # return None
        return 'Hi, my name is mary public and I am 26.'


    # factory

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'mary, public, F, 2000'
                        == 'john, smith, M, 1580'

  because :ref:`the factory function<test person factory>` always returns ``'mary, public, F, 2000'`` and this test expects ``'john, smith, M, 1580'``.

* I change the :ref:`return statement<the return statement>` of :ref:`the factory function<test person factory>` to see the difference between the input and the expected output (remember :ref:`the identity function?<test_identity_function>`)

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 11-12

    # factory
    # factory = None
    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    # def factory(first_name, last_name, sex):
    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        # return 'mary, public, F, 2000'
        return first_name, last_name, sex, year_of_birth

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('mary', 'public', 'F', 2000)
                         == 'mary, public, F, 2000'

  the ``first_name``, ``last_name``, ``sex`` and ``year_of_birth`` are part of the output.

* I change :ref:`the return statement` to an :ref:`f-string<what is string interpolation?>` with those values

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 12-16

    # factory
    # factory = None
    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    # def factory(first_name, last_name, sex):
    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        # return 'mary, public, F, 2000'
        # return first_name, last_name, sex, year_of_birth
        return (
            f'{first_name}, {last_name},'
            f' {sex}, {year_of_birth}'
        )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'Hi, my name ... and I am 26.'
                        == 'Hi, my name ...and I am 446.'

  because :ref:`the say_hi function<test say_hi>` always returns ``'Hi, my name is mary public and I am 26.'`` and this test expects ``'Hi, my name is john smith and I am 446.'``

* I change the :ref:`return statement<the return statement>` of :ref:`the say_hi function<test say_hi>` to see the difference between the input and the expected output

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11

    # say_hi
    # say_hi = None
    # def say_hi():
    # def say_hi(first_name):
    # def say_hi(first_name, last_name):
    def say_hi(
        first_name, last_name, year_of_birth
    ):
        # return None
        # return 'Hi, my name is mary public and I am 26.'
        return first_name, last_name, year_of_birth


    # factory

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert ('mary', 'public', 'F', 2000)
                         == 'mary, public, F, 2000'

  the ``first_name`` and ``last_name`` are part of the output.

* I change :ref:`the return statement` to an :ref:`f-string<what is string interpolation?>` with the input values

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-15

    # say_hi
    # say_hi = None
    # def say_hi():
    # def say_hi(first_name):
    # def say_hi(first_name, last_name):
    def say_hi(
        first_name, last_name, year_of_birth
    ):
        # return None
        # return 'Hi, my name is mary public and I am 26.'
        # return first_name, last_name, year_of_birth
        return (
            f'Hi, my name is {first_name}'
            f' {last_name} and I am {year_of_birth}.'
        )


    # factory

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'Hi, my name ...nd I am 2000.'
                        == 'Hi, my name ... and I am 26.'

  It looks like ``26`` is the age.

* I change the ``year_of_birth`` value to a calculation of the age

  .. code-block:: python
    :linenos:
    :emphasize-lines: 14-15

    # say_hi
    # say_hi = None
    # def say_hi():
    # def say_hi(first_name):
    # def say_hi(first_name, last_name):
    def say_hi(
        first_name, last_name, year_of_birth
    ):
        # return None
        # return 'Hi, my name is mary public and I am 26.'
        # return first_name, last_name, year_of_birth
        return (
            f'Hi, my name is {first_name}'
            # f' {last_name} and I am {year_of_birth}.'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )


    # factory

  all tests are green!

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def say_hi(
        first_name, last_name, year_of_birth
    ):
        return (
            f'Hi, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )


    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return (
            f'{first_name}, {last_name},'
            f' {sex}, {year_of_birth}'
        )

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``person.py``
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

* I ran tests to write one :ref:`function<what is a function?>` that makes a person when given ``first_name``, ``last_name``, ``sex`` and ``year_of_birth`` so I do not have to make one :ref:`function<what is a function?>` for each person.
* I also ran tests to make another :ref:`function<what is a function?>` that uses :ref:`f-strings<what is string interpolation?>` to make a string_ that represents the person I make saying hi when I give it ``first_name``, ``last_name``, and ``year_of_birth``.
* I saw the following :ref:`Exceptions<errors>`

  - :ref:`AssertionError<what causes AssertionError?>`
  - :ref:`NameError<test_catching_name_error_in_tests>`
  - :ref:`TypeError<what causes TypeError?>`
  - :ref:`AttributeError<what causes AttributeError?>`

* My tests and solutions have a few problems,

  - Each test is basically the same two tests, there has to be a way that I can use one test for all the people.
  - The :ref:`factory<test person factory>` and :ref:`say_hi functions<test say_hi>` use three of the same inputs

    * ``first_name``
    * ``last_name``
    * ``year_of_birth``

    There has to be a better way, where I can give those values once, and get a representation for a person when I call :ref:`the factory function<test person factory>` and a message when I call :ref:`the say_hi function<test say_hi>`.

For now, I am going to :ref:`clean up the functions project<separate and equal functions>` so the tests and solutions are in separate files.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a person with f-strings: tests and solution>`

----

*************************************************************************************
what is next?
*************************************************************************************

You know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what causes AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`
* :ref:`how to make functions that take input<functions that take input>`
* :ref:`how to place values in strings<telephone>`
* :ref:`how to make a person say hi with f-strings<how to make a person with f-strings>`

:ref:`Would you like to see me separate the tests and functions in the functions project?<separate and equal functions>`

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