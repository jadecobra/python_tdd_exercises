.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): how to make a person with f-strings. Use f-strings + one factory function (instead of one function per person) that takes first_name, last_name, sex, year_of_birth and returns 'name, surname, X, YYYY'. Add say_hello using f-strings for 'Hello, my name is ... and I am N.'. Start in the person project; uv run pytest-watcher . --now. Progressively introduce f-strings in the return, required args then keyword arguments, move factory and say_hello to src/person.py (AttributeError: module 'src.person' has no attribute 'factory'), use local variables in tests to remove repetition of the data, remove commented lines. Ends with 4 tests calling src.person.factory + src.person.say_hello + # Exceptions seen (AssertionError, NameError, TypeError, AttributeError). Shows why even with f-strings the 4 tests are repetitive. What is next: separate and equal functions. Code: person/tests/test_person_w_fstrings.py and person/solutions/person_w_fstrings.py.
  :keywords: Jacob Itegboje, Pumping Python, how to make a person with f-strings, python f-strings, f-string factory function, one function instead of one per person, src.person, import src.person, AttributeError module 'src.person' has no attribute 'factory', TypeError missing required positional argument, uv run pytest-watcher, red green refactor f-strings, variables remove repetition in tests, first_name last_name sex year_of_birth, say_hello f-string age 2026-year_of_birth, remove the commented lines, test_joe test_jane test_john test_mary, person factory with f-strings, separate tests and solution, what is next separate and equal functions

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

The :ref:`factory<test person factory>` and :ref:`say_hello functions<test say_hello function>` use three of the same inputs

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
test Person class
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

      reality = src.person.say_hello(
          first_name=first_name,
          last_name=last_name,
          year_of_birth=year_of_birth,
      )
      my_expectation = (
          f'Hello, my name is {first_name}'
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

  - I can :ref:`make a class with the pass keyword<test_making_a_class_w_pass>`.
  - The terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

    .. code-block:: python

      TypeError: Person() takes no arguments

    because this happens when ``joe = Person(first_name=first_name, last_name=last_name, sex=sex, year_of_birth=year_of_birth)`` runs

    .. code-block:: python

      joe = Person(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )
          Person(
              first_name=first_name,
              last_name=last_name,
              sex=sex,
              year_of_birth=year_of_birth,
          ) # has no constructor method

    which raises :ref:`TypeError<what causes TypeError?>` since :ref:`classes<what is a class?>` do not take arguments like a :ref:`function<what is a function?>` without a :ref:`method<what is a method?>` that handles those arguments and I called this one with four arguments.

----

*********************************************************************************
the constructor method
*********************************************************************************

A `constructor method`_ is used to define what happens when :ref:`an instance (a copy)`copy of a  :ref:`class<what is a class?>` is made.

* I add a `constructor method`_ to the :ref:`Person class<test Person class>` so it can take arguments

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

  - Here is what is happens when ``joe = Person(first_name=first_name, last_name=last_name, sex=sex, year_of_birth=year_of_birth)`` runs

    .. code-block:: python

      joe = Person(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )
          Person.__init__(
              first_name='joe',
              last_name='blow',
              sex='M',
              year_of_birth=1996,
          )

    which raises :ref:`TypeError<what causes TypeError?>` because the :ref:`definition<how to make a function>` for ``__init__`` does not allow calling it with inputs (the parentheses are empty) and the test sends four :ref:`keyword arguments<test_keyword_arguments>` as input.
  - I am violating the :ref:`method signature<how to make a function that takes input>` when I call it in a way that it was not designed to be called.

* I add the name in parentheses so that the ``__init__`` :ref:`constructor method<the constructor method>` can take input

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

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

  The test calls the :ref:`function<what is a function?>` with four :ref:`keyword arguments<test_keyword_arguments>` ``(first_name, last_name, sex and year_of_birth')``. How does Python_ know which value to use for the first argument if I use the :ref:`position<test_positional_arguments>` and a :ref:`keyword<test_keyword_arguments>`?

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
  - ``self`` is the :ref:`instance of the class<what is a class?>`.
  - The terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

    .. code-block:: shell

      TypeError:
          Person.__init__() got
          an unexpected keyword argument 'last_name'.
          Did you mean 'first_name'?

    because this happens when ``joe = Person(first_name=first_name, last_name=last_name, sex=sex, year_of_birth=year_of_birth)`` runs

    .. code-block:: python

      joe = Person(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )
          Person.__init__(
              self,
              first_name='joe',
              last_name='blow',    # not in definition
              sex='M',
              year_of_birth=1996,
          )

    which raises :ref:`TypeError<what causes TypeError?>` since the :ref:`definition<how to make a function>` of ``__init__`` only allows two arguments (``self`` and ``first_name``) and the test calls it with five (``self``, ``first_name``, ``last_name``, ``sex`` and ``year_of_birth``).
  - ``self`` is the :ref:`instance of the class<what is a class?>`.
  - I am violating the :ref:`method signature<how to make a function that takes input>` when I call it in a way that it was not designed to be called.
  - I have seen this before, so far it is the same as making the :ref:`factory function<test person factory>`.

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

  - because this happens when ``joe = Person(first_name=first_name, last_name=last_name, sex=sex, year_of_birth=year_of_birth)`` runs

    .. code-block:: python

      joe = Person(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )
          Person.__init__(
              self,
              first_name='joe',
              last_name='blow',
              sex='M',             # not in definition
              year_of_birth=1996,
          )

    which raises :ref:`TypeError<what causes TypeError?>` since the :ref:`definition<how to make a function>` of ``__init__`` only allows three arguments (``self``,  ``first_name`` and ``last_name``) and the test calls it with five (``self``, ``first_name``, ``last_name``, ``sex`` and ``year_of_birth``).
  - ``self`` is the :ref:`instance of the class<what is a class?>`.
  - I am violating the :ref:`method signature<how to make a function that takes input>` when I call it in a way that it was not designed to be called.
  - Still the same as making the :ref:`factory function<test person factory>`.

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

  - because this happens when ``joe = Person(first_name=first_name, last_name=last_name, sex=sex, year_of_birth=year_of_birth)`` runs

    .. code-block:: python

      joe = Person(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )
          Person.__init__(
              self,
              first_name='joe',
              last_name='blow',
              sex='M',
              year_of_birth=1996,  # not in definition
          )

    which raises :ref:`TypeError<what causes TypeError?>` since the :ref:`definition<how to make a function>` of ``__init__`` only allows three arguments (``self``,  ``first_name``, ``last_name`` and ``sex``) and the test calls it with five (``self``, ``first_name``, ``last_name``, ``sex`` and ``year_of_birth``).
  - ``self`` is the :ref:`instance of the class<what is a class?>`.
  - I am violating the :ref:`method signature<how to make a function that takes input>` when I call it in a way that it was not designed to be called.
  - Same as with the :ref:`factory function<test person factory>`.

* I add ``sex`` to the :ref:`definition<how to make a function>` of the ``__init__`` :ref:`constructor method<the constructor method>`

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
test say_hello method
*********************************************************************************

I made a person :ref:`say hi with a function<test say_hello function>`, I can also do the same thing with a :ref:`class<what is a class?>` because it is :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` that belong together.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` with a call to the :ref:`say_hello function<test say_hello function>` with the :ref:`attributes<what is a class attribute?>` of ``joe`` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 8-13

        joe = Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = src.person.say_hello(
            first_name=joe.first_name,
            last_name=joe.last_name,
            year_of_birth=joe.year_of_birth,
        )
        assert reality == my_expectation


    def test_jane():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'first_name'

  because there is nothing named ``first_name`` in the :ref:`Person class<test Person class>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``self.first_name`` to the :ref:`definition<how to make a function>` of the ``__init__`` :ref:`constructor method<the constructor method>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7

    class Person:

        def __init__(
            self, first_name, last_name,
            year_of_birth, sex
        ):
            self.first_name
            return None


    def test_joe():

  the terminal_ still shows :ref:`AttributeError<what causes AttributeError?>` because this is just a reference to the name, not a definition.

* I point ``self.first_name`` to the value for ``first_name`` when the ``__init__`` :ref:`method<what is a method?>` is called

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8

    class Person:

        def __init__(
            self, first_name, last_name,
            year_of_birth, sex
        ):
            # self.first_name
            self.first_name = first_name
            return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: 'Person' object
                    has no attribute 'last_name'.
                    Did you mean: 'first_name'?

* I add ``self.last_name`` and point it to the value for ``last_name`` when the ``__init__`` :ref:`method<what is a method?>` is called

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 9

    class Person:

        def __init__(
            self, first_name, last_name,
            year_of_birth, sex
        ):
            # self.first_name
            self.first_name = first_name
            self.last_name = last_name
            return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object
                    has no attribute 'year_of_birth'

* I add ``self.year_of_birth`` and point it to the value for ``year_of_birth`` when the ``__init__`` :ref:`constructor method<the constructor method>` is called

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 10

    class Person:

        def __init__(
            self, first_name, last_name,
            year_of_birth, sex
        ):
            # self.first_name
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            return None


    def test_joe():

  the test passes, because

  - given

    .. code-block:: python

      first_name = 'joe'
      last_name = 'blow'
      sex = 'M'
      year_of_birth = 1996

  - when ``joe = Person(first_name=first_name, last_name=last_name, sex=sex, year_of_birth=year_of_birth)`` runs

    .. code-block:: python

      joe = Person(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )
          Person.__init__(
              self,
              first_name='joe',
              last_name='blow',
              sex='M',
              year_of_birth=1996,
          )
              self.first_name = 'joe'
              self.last_name = 'blow'
              self.year_of_birth = 1996

    ``self`` is the :ref:`instance of the class<what is a class?>`.

  - When ``reality = src.person.say_hello(first_name=joe.first_name, last_name=joe.last_name,year_of_birth=joe.year_of_birth)`` runs

    .. code-block:: python

      reality = src.person.say_hello(
          first_name=joe.first_name,
          last_name=joe.last_name,
          year_of_birth=joe.year_of_birth,
      )
          reality = src.person.say_hello(
              first_name='joe',
              last_name='blow',
              year_of_birth=1996,
          )

    Python_ follows this path

    .. code-block:: shell

      src
      └── person.py
          └── def say_hello(
                  first_name, last_name, year_of_birth
              ):
                  return (
                      f'Hello, my name is {first_name}'
                      f' {last_name} and I am'
                      f' {2026-year_of_birth}.'
                  )

  and the result is ``'Hello, my name is joe blow and I am 30.'``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line

  .. code-block:: python
    :lineno-start: 4

    class Person:

        def __init__(
            self, first_name, last_name,
            year_of_birth, sex
        ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            return None


    def test_joe():

* I change the call to ``src.person.say_hello`` in :ref:`test_joe` to a call to the :ref:`say_hello method<test say_hello method>` of the :ref:`Person class<test Person class>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 8-9
    :emphasize-text: joe

        joe = Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        # reality = src.person.say_hello(
        reality = Person.say_hello(
            first_name=joe.first_name,
            last_name=joe.last_name,
            year_of_birth=joe.year_of_birth,
        )
        assert reality == my_expectation


    def test_jane():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: type object 'Person'
                    has no attribute 'say_hello'

  because the test calls the :ref:`say_hello method<test say_hello method>` which does not yet exist in the :ref:`Person class<test Person class>`.

* I add a :ref:`method definition<how to make a function>` for it to the :ref:`Person class<test Person class>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 12-13

    class Person:

        def __init__(
            self, first_name, last_name,
            year_of_birth, sex
        ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            return None

        def say_hello():
            return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() got
               an unexpected keyword argument 'first_name'

  because the :ref:`definition<how to make a function>` for ``say_hello`` does not allow inputs and the test called the :ref:`method<what is a method?>` with one :ref:`keyword argument<test_keyword_arguments>` (``first_name``).

* I add ``first_name`` to the :ref:`method definition<how to make a function>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1-2

        # def say_hello():
        def say_hello(first_name):
            return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: Person.say_hello() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

* I add ``last_name`` to the :ref:`method definition<how to make a function>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2-3

        # def say_hello():
        # def say_hello(first_name):
        def say_hello(first_name, last_name):
            return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() got
               an unexpected keyword argument 'year_of_birth'

* I add ``year_of_birth`` to the :ref:`method definition<how to make a function>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3-4

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        def say_hello(first_name, last_name, year_of_birth):
            return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None
        == 'Hello, my name is joe blow and I am 30.'

* I change :ref:`the return statement` to match

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5-6

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        def say_hello(first_name, last_name, year_of_birth):
            # return None
            return 'Hello, my name is joe blow and I am 30.'


    def test_joe():

  the test passes.

* I add a call to the :ref:`Person class<test person class>` and :ref:`say_hello method<test say_hello method>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 31-36, 38-43

    def test_jane():
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = 1991

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

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation

        jane = Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = Person.say_hello(
            first_name=jane.first_name,
            last_name=jane.last_name,
            year_of_birth=jane.year_of_birth,
        )
        assert reality == my_expectation


    def test_john():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'Hi, my name ... and I am 30.'
                        == 'Hi, my name ... and I am 35.'

* I change :ref:`the return statement` to an :ref:`f-string<what is string interpolation?>` with the input like the :ref:`say_hello function<test say_hello function>` in ``person.py`` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 6-11

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        def say_hello(first_name, last_name, year_of_birth):
            # return None
            # return 'Hello, my name is joe blow and I am 30.'
            return (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {2026-year_of_birth}.'
            )


    def test_joe():

  the test passes. This is still repeating the values for ``first_name``, ``last_name`` and ``year_of_birth``.

* I change the call to the :ref:`say_hello method<test say_hello method>` in :ref:`test_joe` to take in an :ref:`instance (copy)<how to test if something is an instance of a class>` of the :ref:`Person class<test person class>` since it will already have the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 3

        # reality = src.person.say_hello(
        reality = Person.say_hello(
            person=joe,
            first_name=joe.first_name,
            last_name=joe.last_name,
            year_of_birth=joe.year_of_birth,
        )
        assert reality == my_expectation


    def test_jane():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() got
               an unexpected keyword argument 'person'

* I add ``person`` to the :ref:`method definition for say_hello<test say_hello method>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines:

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        # def say_hello(first_name, last_name, year_of_birth):
        def say_hello(
            person, first_name, last_name, year_of_birth
        ):
            # return None
            # return 'Hello, my name is joe blow and I am 30.'
            return (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {2026-year_of_birth}.'
            )


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() missing
               1 required positional argument: 'person'

  I have to make the same change to :ref:`test_jane`

* I add the ``person`` :ref:`keyword argument<test_keyword_arguments>` to the call to the :ref:`say_hello method<test say_hello method>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 116
    :emphasize-lines: 2

        reality = Person.say_hello(
            person=jane,
            first_name=jane.first_name,
            last_name=jane.last_name,
            year_of_birth=jane.year_of_birth,
        )
        assert reality == my_expectation


    def test_john():

  the test passes.

* I change :ref:`the return statement` of the :ref:`say_hello method<test say_hello method>` to use the :ref:`attributes<what is a class attribute?>` of the :ref:`class instance<how to test if something is an instance of a class>` it receives as input

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 11-16

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        # def say_hello(first_name, last_name, year_of_birth):
        def say_hello(
            person, first_name, last_name, year_of_birth
        ):
            # return None
            # return 'Hello, my name is joe blow and I am 30.'
            return (
                # f'Hello, my name is {first_name}'
                # f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                f'Hello, my name is {person.first_name}'
                f' {person.last_name} and I am'
                f' {2026-person.year_of_birth}.'
            )


    def test_joe():

  the test passes because

  - given

    .. code-block:: python

      first_name = 'joe'
      last_name = 'blow'
      sex = 'M'
      year_of_birth = 1996

  - when ``joe = Person(first_name=first_name, last_name=last_name, sex=sex, year_of_birth=year_of_birth)`` runs

    .. code-block:: python

      joe = Person(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )
          Person.__init__(
              self,
              first_name='joe',
              last_name='blow',
              sex='M',
              year_of_birth=1996,
          )
              self.first_name = 'joe'
              self.last_name = 'blow'
              self.year_of_birth = 1996

    ``self`` is the :ref:`instance of the class<what is a class?>` aka ``joe``.

  - When ``reality = Person.say_hello(person=joe, first_name=joe.first_name, last_name=joe.last_name,year_of_birth=joe.year_of_birth)`` runs

    .. code-block:: python

      reality = Person.say_hello(
          person=joe,
          first_name=joe.first_name,
          last_name=joe.last_name,
          year_of_birth=joe.year_of_birth,
      )
          reality = src.person.say_hello(
              person=joe,
              first_name='joe',
              last_name='blow',
              year_of_birth=1996,
          )
              return (
                  f'Hello, my name is {person.first_name}'
                  f' {person.last_name} and I am'
                  f' {2026-person.year_of_birth}.'
              )
              return (
                  f'Hello, my name is {joe.first_name}'
                  f' {joe.last_name} and I am'
                  f' {2026-joe.year_of_birth}.'
              )

  and the result is ``'Hello, my name is joe blow and I am 30.'``

* I remove the ``first_name``, ``last_name`` and ``year_of_birth`` arguments from the call in :ref:`test_joe` since they are repetitions of the :ref:`class attributes<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 4-6

        # reality = src.person.say_hello(
        reality = Person.say_hello(
            person=joe,
            # first_name=joe.first_name,
            # last_name=joe.last_name,
            # year_of_birth=joe.year_of_birth,
        )
        assert reality == my_expectation


    def test_jane():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() missing
               3 required positional arguments:
               'first_name', 'last_name', and 'year_of_birth'

* I remove ``first_name``, ``last_name`` and ``year_of_birth`` from the :ref:`definition of the say_hello method<test say_hello method>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 6-7

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        # def say_hello(first_name, last_name, year_of_birth):
        def say_hello(
            # person, first_name, last_name, year_of_birth
            person
        ):
            # return None
            # return 'Hello, my name is joe blow and I am 30.'
            return (
                # f'Hello, my name is {first_name}'
                # f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                f'Hello, my name is {person.first_name}'
                f' {person.last_name} and I am'
                f' {2026-person.year_of_birth}.'
            )


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() got
               an unexpected keyword argument 'first_name'

* I remove the ``first_name``, ``last_name`` and ``year_of_birth`` arguments from the call in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 3-5

        reality = Person.say_hello(
            person=jane,
            # first_name=jane.first_name,
            # last_name=jane.last_name,
            # year_of_birth=jane.year_of_birth,
        )
        assert reality == my_expectation


    def test_john():

  the test passes. This is still a repetition. I give an :ref:`instance (copy)<how to test if something is an instance of a class>` of the :ref:`Person class<test person class>` as input to the :ref:`say_hello method<test Person class>` of the :ref:`Person class<test person class>` (``Person.say_hello``).

* I change the call to the :ref:`say_hello method<test say_hello method>` in :ref:`test_jane` because the :ref:`say_hello method<test say_hello method>` is in the :ref:`Person class<test Person class>` so its :ref:`copies<how to test if something is an instance of a class>` also have the :ref:`say_hello method<test say_hello method>`

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 1-2

        # reality = Person.say_hello(
        reality = jane.say_hello(
            person=jane,
            # first_name=jane.first_name,
            # last_name=jane.last_name,
            # year_of_birth=jane.year_of_birth,
        )
        assert reality == my_expectation


    def test_john():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() got
               multiple values for argument 'person'

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

*********************************************************************************
what is the staticmethod decorator?
*********************************************************************************

* I can use the `staticmethod decorator`_ if I do not want to add ``self`` to the :ref:`method definition<how to make a function>` when it does not use anything in the :ref:`class<what is a class?>` that way I am not sending more information than what the :ref:`method<what is a method?>` needs. I add ``@staticmethod`` to the :ref:`say_hello method<test say_hello method>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        # def say_hello(first_name, last_name, year_of_birth):
        @staticmethod
        def say_hello(
            # person, first_name, last_name, year_of_birth
            person
        ):
            # return None
            # return 'Hello, my name is joe blow and I am 30.'
            return (
                # f'Hello, my name is {first_name}'
                # f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                f'Hello, my name is {person.first_name}'
                f' {person.last_name} and I am'
                f' {2026-person.year_of_birth}.'
            )


    def test_joe():

  the test passes.

* I change the call to ``Person.say_hello`` in :ref:`test_joe` because the :ref:`say_hello method<test say_hello method>` is in the :ref:`Person class<test Person class>`, there is no need for it to take a copy of the :ref:`Person class<test Person class>` as input since it should be able to use its own :ref:`attributes<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2-4

        # reality = src.person.say_hello(
        # reality = Person.say_hello(
        reality = joe.say_hello(
            # person=joe,
            # first_name=joe.first_name,
            # last_name=joe.last_name,
            # year_of_birth=joe.year_of_birth,
        )
        assert reality == my_expectation


    def test_jane():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() missing
               1 required positional argument: 'person'

* I make ``person`` :ref:`optional<test_optional_arguments>` in the :ref:`say_hello method<test say_hello method>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 8-9

    # def say_hello():
    # def say_hello(first_name):
    # def say_hello(first_name, last_name):
    # def say_hello(first_name, last_name, year_of_birth):
    @staticmethod
    def say_hello(
        # person, first_name, last_name, year_of_birth
        # person
        person=None
    ):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'NoneType' object
                    has no attribute 'first_name'

* I change ``person.`` to ``self.`` in :ref:`the return statement`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 17-22

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        # def say_hello(first_name, last_name, year_of_birth):
        @staticmethod
        def say_hello(
            # person, first_name, last_name, year_of_birth
            # person
            person=None
        ):
            # return None
            # return 'Hello, my name is joe blow and I am 30.'
            return (
                # f'Hello, my name is {first_name}'
                # f' {last_name} and I am'
                # f' {2026-year_of_birth}.'
                # f'Hello, my name is {person.first_name}'
                # f' {person.last_name} and I am'
                # f' {2026-person.year_of_birth}.'
                f'Hello, my name is {self.first_name}'
                f' {self.last_name} and I am'
                f' {2026-self.year_of_birth}.'
            )


    def test_joe():

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 9-10

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        # def say_hello(first_name, last_name, year_of_birth):
        @staticmethod
        def say_hello(
            # person, first_name, last_name, year_of_birth
            # person
            # person=None
            self, person=None
        ):

  the terminal_ is my friend, and shows :ref:`TypeError`

  .. code-block:: python

    TypeError: Person.say_hello() missing
               1 required positional argument: 'self'

* I remove the `staticmethod decorator`_ because I no longer need it since the :ref:`say_hello method<test say_hello method>` is using :ref:`class attributes<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        # def say_hello(first_name, last_name, year_of_birth):
        # @staticmethod
        def say_hello(
            # person, first_name, last_name, year_of_birth
            # person
            # person=None
            self, person=None
        ):

  the test passes because

  - given

    .. code-block:: python

      first_name = 'joe'
      last_name = 'blow'
      sex = 'M'
      year_of_birth = 1996

  - when ``joe = Person(first_name=first_name, last_name=last_name, sex=sex, year_of_birth=year_of_birth)`` runs

    .. code-block:: python

      joe = Person(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )
          Person.__init__(
              self,
              first_name='joe',
              last_name='blow',
              sex='M',
              year_of_birth=1996,
          )
              self.first_name = 'joe'
              self.last_name = 'blow'
              self.year_of_birth = 1996

    ``self`` is the :ref:`instance of the class<what is a class?>` aka ``joe``.

  - When ``reality = joe.say_hello()`` runs

    .. code-block:: python

      reality = joe.say_hello()
          return (
              f'Hello, my name is {self.first_name}'
              f' {self.last_name} and I am'
              f' {2026-self.year_of_birth}.'
          )
          # inside joe, self == joe
          return (
              f'Hello, my name is {joe.first_name}'
              f' {joe.last_name} and I am'
              f' {2026-joe.year_of_birth}.'
          )

    and the result is ``'Hello, my name is joe blow and I am 30.'``

  - a simple way to think of ``joe.say_hello()`` is

    .. code-block:: python

      joe.say_hello() == Person().say_hello()
      joe.say_hello() == joe.say_hello(Person())
      joe.say_hello() == joe.say_hello(joe)

    I do not need to pass ``joe`` as input to the :ref:`say_hello method<test say_hello method>` since it is ``self``.

* I remove ``person=jane`` from the call to the :ref:`say_hello method<test say_hello method>` in :ref:`test_jane` because the :ref:`say_hello method<test say_hello method>` is in the :ref:`Person class<test Person class>`

  .. code-block:: python
    :lineno-start: 126
    :emphasize-lines: 3

        # reality = Person.say_hello(
        reality = jane.say_hello(
            # person=jane,
            # first_name=jane.first_name,
            # last_name=jane.last_name,
            # year_of_birth=jane.year_of_birth,
        )
        assert reality == my_expectation


    def test_john():

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_john` for the :ref:`say_hello method<test say_hello method>`

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 13-18, 20-21

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation

        john = Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = john.say_hello()
        assert reality == None


    def test_mary():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        assert 'Hello, my name is john smith and I am 446.'
            == None

* I change my expectation to match ``reality``

  .. code-block:: python
    :lineno-start: 166
    :emphasize-lines: 9-10

        john = Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = john.say_hello()
        # assert reality == None
        assert reality == my_expectation


    def test_mary():

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_mary` for the :ref:`say_hello method<test say_hello method>`

  .. code-block:: python
    :lineno-start: 196
    :emphasize-lines: 13-18, 20-21

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation

        mary = Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = mary.say_hello()
        assert reality == None


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        assert 'Hello, my name is mary public and I am 26.'
             == None

* I change my expectation to match ``reality``

  .. code-block:: python
    :lineno-start: 208
    :emphasize-lines: 9-10

        mary = Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = mary.say_hello()
        # assert reality == None
        assert reality == my_expectation


    # Exceptions seen

  the test passes because

  - given

    .. code-block:: python

      first_name = 'mary'
      last_name = 'public'
      sex = 'F'
      year_of_birth = 2000

  - when ``mary = Person(first_name=first_name, last_name=last_name, sex=sex, year_of_birth=year_of_birth)`` runs

    .. code-block:: python

      mary = Person(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )
          Person.__init__(
              self,
              first_name='mary',
              last_name='public',
              sex='F',
              year_of_birth=2000,
          )
              self.first_name = 'mary'
              self.last_name = 'public'
              self.year_of_birth = 2000

    ``self`` is the :ref:`instance of the class<what is a class?>` aka ``mary``.

  - When ``reality = mary.say_hello()`` runs

    .. code-block:: python

      reality = mary.say_hello()
          return (
              f'Hello, my name is {self.first_name}'
              f' {self.last_name} and I am'
              f' {2026-self.year_of_birth}.'
          )
          # inside mary, self == mary
          return (
              f'Hello, my name is {mary.first_name}'
              f' {mary.last_name} and I am'
              f' {2026-mary.year_of_birth}.'
          )

    and the result is ``'Hello, my name is mary public and I am 26.'``

  - a simple way to think of ``mary.say_hello()``

    .. code-block:: python

      mary.say_hello() == Person().say_hello()
      mary.say_hello() == mary.say_hello(Person())
      mary.say_hello() == mary.say_hello(mary)

    I do not need to pass ``mary`` as input to the :ref:`say_hello method<test say_hello method>` since it is ``self``.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add say_hello method'

----

*********************************************************************************
separate and equal Person class
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I change ``mary`` in :ref:`test_mary` to be the result of a call to the :ref:`Person class<test person class>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a call to the :ref:`Person class<test person class>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 196
    :emphasize-lines: 13-14

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation

        # mary = Person(
        mary = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = mary.say_hello()
        # assert reality == None
        assert reality == my_expectation


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.person' has no attribute 'Person'

  because there is nothing with that name in the ``person.py`` file_ in the ``src`` folder_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``person.py`` from the ``src`` folder_

* I add the name to ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    Person


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'Person' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # Person
    Person = None


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I change ``Person`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-4

    # Person
    # Person = None
    def Person():
        return None


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person() got
               an unexpected keyword argument 'first_name'

* I add ``first_name`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # Person
    # Person = None
    # def Person():
    def Person(first_name):
        return None


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: Person() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

* I add ``first_name`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    # Person
    # Person = None
    # def Person():
    # def Person(first_name):
    def Person(first_name, last_name):
        return None


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person() got
               an unexpected keyword argument 'sex'

* I add ``sex`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    # Person
    # Person = None
    # def Person():
    # def Person(first_name):
    # def Person(first_name, last_name):
    def Person(first_name, last_name, sex):
        return None


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person() got
               an unexpected keyword argument 'year_of_birth'

* I add ``year_of_birth`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-10

    # Person
    # Person = None
    # def Person():
    # def Person(first_name):
    # def Person(first_name, last_name):
    # def Person(first_name, last_name, sex):
    def Person(
        first_name, last_name,
        sex, year_of_birth,
    ):
        return None


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'NoneType' object
                    has no attribute 'say_hello'

  because the :ref:`function<what is a function?>` I just made returns :ref:`None<what is None?>`

  - given

    .. code-block:: python

      first_name = 'mary'
      last_name = 'public'
      sex = 'F'
      year_of_birth = 2000

  - when ``mary = Person(first_name=first_name, last_name=last_name, sex=sex, year_of_birth=year_of_birth)`` runs

    .. code-block:: python

      mary = Person(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )
          Person(
              first_name='mary',
              last_name='public',
              sex='F',
              year_of_birth=2000,
          )
              return None

  - When ``reality = mary.say_hello()`` runs

    .. code-block:: python

      reality = mary.say_hello()
      reality = None.say_hello()

  which raises :ref:`AttributeError<what causes AttributeError?>` since :ref:`None<what is None?>` does not have anything named ``say_hello`` in it.

* I change ``Person`` to a :ref:`class<what is a class?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    # Person
    # Person = None
    # def Person():
    # def Person(first_name):
    # def Person(first_name, last_name):
    # def Person(first_name, last_name, sex):
    # def Person(
    class Person(
        first_name, last_name,
        sex, year_of_birth,
    ):
        return None


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: 'return' outside function

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 221
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError
    # SyntaxError

* I change :ref:`the return statement` to the pass_ keyword, in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 12-13

    # Person
    # Person = None
    # def Person():
    # def Person(first_name):
    # def Person(first_name, last_name):
    # def Person(first_name, last_name, sex):
    # def Person(
    class Person(
        first_name, last_name,
        sex, year_of_birth,
    ):
        # return None
        pass


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'first_name' is not defined

  because the only definitions for ``first_name`` are in the :ref:`say_hello<test say_hello function>` and :ref:`factory functions<test person factory>` in ``person.py``.

* I add :ref:`the constructor method` to handle the inputs

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-12, 14-19

    # Person
    # Person = None
    # def Person():
    # def Person(first_name):
    # def Person(first_name, last_name):
    # def Person(first_name, last_name, sex):
    # def Person(
    # class Person(
    #     first_name, last_name,
    #     sex, year_of_birth,
    # ):
    class Person:

        def __init__(
            first_name, last_name,
            sex, year_of_birth
        ):
            # return None
            pass


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() got
               multiple values for argument 'first_name'

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add ``self`` to :ref:`the constructor method`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 4-5

    class Person:

        def __init__(
            # first_name, last_name,
            self, first_name, last_name,
            sex, year_of_birth
        ):
            # return None
            pass


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'say_hello'

  better, I can add an :ref:`attribute<what is a class attribute?>` to a :ref:`class<what is a class?>`.

* I add the name to the :ref:`Person class<test Person class>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3

    class Person:

        say_hello

        def __init__(
            # first_name, last_name,
            self, first_name, last_name,
            sex, year_of_birth
        ):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'say_hello' is not defined

* I point ``say_hello`` to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3-4

    class Person:

        # say_hello
        say_hello = None

        def __init__(
            # first_name, last_name,
            self, first_name, last_name,
            sex, year_of_birth
        ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I change it to a :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 4, 14-15

    class Person:

        # say_hello
        # say_hello = None

        def __init__(
            # first_name, last_name,
            self, first_name, last_name,
            sex, year_of_birth
        ):
            # return None
            pass

        def say_hello():
            return None


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() takes
               0 positional arguments but 1 was given

* I add a name to the parentheses

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 1-2

        # def say_hello():
        def say_hello(argument):
            return None


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None
        == 'Hello, my name is mary public and I am 26.'

* I copy and paste the string_ from the terminal_ to use as :ref:`the return statement`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3-4

        # def say_hello():
        def say_hello(argument):
            # return None
            return 'Hello, my name is mary public and I am 26.'


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_mary` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 178

    def test_mary():
        first_name = 'mary'
        last_name = 'public'
        sex = 'F'
        year_of_birth = 2000

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

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation

        mary = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = mary.say_hello()
        assert reality == my_expectation


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError
    # SyntaxError

* I change ``john`` in :ref:`test_john` to be the result of a call to the :ref:`Person class<test person class>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 13-14

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation

        # john = Person(
        john = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = john.say_hello()
        # assert reality == None
        assert reality == my_expectation


    def test_mary():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'Hi, my name ... and I am 26.'
                        == 'Hi, my name ...and I am 446.'

* I change :ref:`the return statement` of the :ref:`say_hello method<test say_hello method>` to return the input, in ``person.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4-5

        # def say_hello():
        def say_hello(argument):
            # return None
            # return 'Hello, my name is mary public and I am 26.'
            return argument


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        assert <src.person.Person object at 0xffffb012cd34>
            == 'Hello, my name is mary public and I am 26.'

  because ``argument`` is :ref:`an instance (a copy)<how to test if something is an instance of a class>` of the :ref:`Person class<test Person class>`.

* I change :ref:`the return statement` to use :ref:`class attributes<what is a class attribute?>` in an :ref:`f-string<what is string interpolation?>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5-10

        # def say_hello():
        def say_hello(argument):
            # return None
            # return 'Hello, my name is mary public and I am 26.'
            # return argument
            return (
                f'Hello, my name is {argument.first_name}'
                f' {argument.last_name} and I am'
                f' {2026-argument.year_of_birth}.'
            )


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object
                    has no attribute 'first_name'

  because I have not defined a :ref:`class attribute<what is a class attribute?>` named ``first_name``.

* I add ``self.first_name`` to the ``__init__`` :ref:`constructor method<the constructor method>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 12-13

    class Person:

        # say_hello
        # say_hello = None

        def __init__(
            # first_name, last_name,
            self, first_name, last_name,
            sex, year_of_birth
        ):
            # return None
            # pass
            self.first_name = first_name

        # def say_hello():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: 'Person' object
                    has no attribute 'last_name'.
                    Did you mean: 'first_name'?

  because I have not defined a :ref:`class attribute<what is a class attribute?>` named ``last_name``.

* I add ``self.last_name`` to the ``__init__`` :ref:`constructor method<the constructor method>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 9

        def __init__(
            # first_name, last_name,
            self, first_name, last_name,
            sex, year_of_birth
        ):
            # return None
            # pass
            self.first_name = first_name
            self.last_name = last_name

        # def say_hello():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object
                    has no attribute 'year_of_birth'

  because I have not defined a :ref:`class attribute<what is a class attribute?>` named ``year_of_birth``.

* I add ``self.year_of_birth`` to the ``__init__`` :ref:`constructor method<the constructor method>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 10

        def __init__(
            # first_name, last_name,
            self, first_name, last_name,
            sex, year_of_birth
        ):
            # return None
            # pass
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth

        # def say_hello():

  the test passes.

* I change ``argument`` to ``self`` in the :ref:`say_hello method<test say_hello method>` to follow :ref:`Python convention<conventions>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 2-3, 8-13

        # def say_hello():
        # def say_hello(argument):
        def say_hello(self):
            # return None
            # return 'Hello, my name is mary public and I am 26.'
            # return argument
            return (
                # f'Hello, my name is {argument.first_name}'
                # f' {argument.last_name} and I am'
                # f' {2026-argument.year_of_birth}.'
                f'Hello, my name is {self.first_name}'
                f' {self.last_name} and I am'
                f' {2026-self.year_of_birth}.'
            )


    def say_hello(
        first_name, last_name, year_of_birth
    ):

  the test is still green because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument which means

  .. code-block:: python

    instance = Person()
    instance.say_hello() == Person().say_hello()
    instance.say_hello() == instance.say_hello(Person())
    instance.say_hello() == instance.say_hello(instance)

  I do not need to pass the :ref:`instance<how to test if something is an instance of a class>` as input to the :ref:`say_hello method<test say_hello method>` since it is ``self``.

* I remove the commented lines from the :ref:`Person class<test Person class>` in ``person.py``

  .. code-block:: python
    :linenos:

    class Person:

        def __init__(
            self, first_name, last_name,
            sex, year_of_birth
        ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth

        def say_hello(self):
            return (
                f'Hello, my name is {self.first_name}'
                f' {self.last_name} and I am'
                f' {2026-self.year_of_birth}.'
            )


    def say_hello(
        first_name, last_name, year_of_birth
    ):

* I remove the commented lines from :ref:`test_john` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 136

    def test_john():
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'
        year_of_birth = 1580

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

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation

        john = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = john.say_hello()
        assert reality == my_expectation


    def test_mary():

* I change ``jane`` in :ref:`test_jane` to be the result of a call to the :ref:`Person class<test person class>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 13-14

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation

        # jane = Person(
        jane = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        # reality = Person.say_hello(
        reality = jane.say_hello(
            # person=jane,
            # first_name=jane.first_name,
            # last_name=jane.last_name,
            # year_of_birth=jane.year_of_birth,
        )
        assert reality == my_expectation


    def test_john():

  the test is still green.

* I remove the commented lines from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 89

    def test_jane():
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = 1991

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

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation

        jane = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = jane.say_hello()
        assert reality == my_expectation


    def test_john():

* I change ``joe`` in :ref:`test_joe` to be the result of a call to the :ref:`Person class<test person class>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 13-14

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation

        # joe = Person(
        joe = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        # reality = src.person.say_hello(
        # reality = Person.say_hello(
        reality = joe.say_hello(
            # person=joe,
            # first_name=joe.first_name,
            # last_name=joe.last_name,
            # year_of_birth=joe.year_of_birth,
        )
        assert reality == my_expectation


    def test_jane():

  the test is still green.

* I remove the commented lines from :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 41

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

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation

        joe = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = joe.say_hello()
        assert reality == my_expectation


    def test_jane():

* I remove the :ref:`Person class<test Person class>` from ``test_person.py``

  .. code-block:: python

    import src.person


    def test_joe():

  all the tests are still green because the calls that were made to the :ref:`Person class<test Person class>` that was in ``test_person.py`` are now to the :ref:`Person class<test Person class>` in ``person.py`` in the ``src`` folder_. When ``src.person.Person`` is called, Python_ follows this path

  .. code-block:: shell

    src
    └── person.py
        └── class Person:

                def __init__(
                    self, first_name, last_name,
                    sex, year_of_birth
                ):
                    self.first_name = first_name
                    self.last_name = last_name
                    self.year_of_birth = year_of_birth

                def say_hello(self):
                    return (
                        f'Hello, my name is {self.first_name}'
                        f' {self.last_name} and I am'
                        f' {2026-self.year_of_birth}.'
                    )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move Person class to person.py'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can write solutions in a different module from the tests<separate and equal>`.

----

*********************************************************************************
test_attributes_and_methods_of_person_instance
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

        def test_attributes_and_methods_of_person_class(self):
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

        def test_attributes_and_methods_of_person_class(self):
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

        def test_attributes_and_methods_of_person_class(self):
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

        def test_attributes_and_methods_of_person_class(self):
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

        def test_attributes_and_methods_of_person_class(self):
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
  - The attributes I defined in the ``__init__`` :ref:`method<what is a method?>` are not in the list, because the test called dir_ on ``src.person.Person`` which is the :ref:`class<what is a class?>`, not an instance (copy) of the class

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_attributes_and_methods_of_person_class'


----

*********************************************************************************
test_attributes_and_methods_of_person_class
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of an instance/copy of the ``Person`` :ref:`class<what is a class?>` to see the difference between it and the original

.. code-block:: python
  :lineno-start: 118
  :emphasize-lines: 8-14, 16-49

              '__str__',
              '__subclasshook__',
              '__weakref__',
              'say_hello',
          ]
          self.assertEqual(reality, my_expectation)

      def test_attributes_and_methods_of_person_instance(self):
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

  the ``sex`` :ref:`attribute<what is a class attribute?>` is not defined anywhere in the ``Person`` :ref:`class<what is a class?>`

* I add ``self.sex`` to the ``__init__`` :ref:`method<what is a method?>` of the ``Person`` :ref:`class<what is a class?>` in ``person.py``

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
    'add test_attributes_and_methods_of_person_instance'

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
  - The :ref:`factory<test person factory>` and :ref:`say_hello functions<test say_hello function>` use three of the same inputs

    * ``first_name``
    * ``last_name``
    * ``year_of_birth``

    There has to be a better way, where I can give those values once, and get a representation for a person when I call the :ref:`factory function<test person factory>` and a message when I call the :ref:`say_hello function<test say_hello function>`.

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