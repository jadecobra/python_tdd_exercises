.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): how to make a person with a class. Use class + __init__ (the constructor method) + self to store first_name, last_name, sex, year_of_birth once; add say_hello method so you call joe.say_hello() without repeating the values. Start in person project from prior chapter; uv run pytest-watcher . --now. RED: Person(...) -> TypeError (no __init__), empty __init__ -> TypeError got unexpected keyword 'last_name', add self. attrs; GREEN: implement using f-string with self; move to src/person.py (AttributeError); use locals in tests + kw calls for factory/say_hello/Person; add dir() tests on class vs instance. REFACTOR remove commented lines. Ends with 6 tests (joe/jane/john/mary + 2 dir tests); # Exceptions seen includes SyntaxError. Review: each test repeats the same three calls; class avoids repeating the data values. Code from person/tests/test_person_w_class.py and person/solutions/person_w_class.py. What is next: test classes (everything is an object).
  :keywords: Jacob Itegboje, Pumping Python, how to make a person with a class, python class __init__ constructor self, Person class say_hello method, src.person.Person, src.person.person, TypeError: Person.__init__() got an unexpected keyword argument 'last_name', Did you mean, AttributeError class has no attribute 'first_name' on class vs instance, dir(src.person.Person), dir(instance), uv run pytest-watcher . --now, red green refactor class, remove the commented lines, test_joe, test_dir_person_class, test_dir_person_instance, first_name last_name sex year_of_birth, 2026 - year_of_birth, repetition of three calls per test, class groups attributes and methods, what is next everything is an object

.. include:: ../../links.rst

.. _constructor: https://grokipedia.com/page/Constructor_(object-oriented_programming)
.. _constructor method: constructor_
.. _staticmethod decorator: https://docs.python.org/3/library/functions.html#staticmethod

#################################################################################
how to make a person with a class
#################################################################################

----

The :ref:`factory<extract person function>` and :ref:`say_hello functions<test say_hello function>` use three of the same inputs

* ``first_name``
* ``last_name``
* ``year_of_birth``

I want to give those values once, and get a representation for a person. I can do that with a :ref:`class<everything is an object>`.

I think of :ref:`classes<everything is an object>` as :ref:`attributes (variables)<what is a class attribute?>` and :ref:`methods (functions) <what is a method?>` that belong together (a classification).

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_class.py
  :language: python
  :linenos:
  :caption: person/tests/test_person.py
  :lines: 1-5

.. literalinclude:: ../../code/person/tests/test_person_w_class.py
  :language: python
  :lineno-start: 8
  :caption: person/tests/test_person.py
  :lines: 8-24

.. literalinclude:: ../../code/person/tests/test_person_w_class.py
  :language: python
  :lineno-start: 27
  :caption: person/tests/test_person.py
  :lines: 27-42

.. literalinclude:: ../../code/person/tests/test_person_w_class.py
  :language: python
  :lineno-start: 45
  :caption: person/tests/test_person.py
  :lines: 45-60

.. literalinclude:: ../../code/person/tests/test_person_w_class.py
  :language: python
  :lineno-start: 63
  :caption: person/tests/test_person.py
  :lines: 63-87

.. literalinclude:: ../../code/person/tests/test_person_w_class.py
  :language: python
  :lineno-start: 90
  :caption: person/tests/test_person.py
  :lines: 90-114

.. literalinclude:: ../../code/person/tests/test_person_w_class.py
  :language: python
  :lineno-start: 117
  :caption: person/tests/test_person.py
  :lines: 117-141

.. literalinclude:: ../../code/person/tests/test_person_w_class.py
  :language: python
  :lineno-start: 144
  :caption: person/tests/test_person.py
  :lines: 144-168

.. literalinclude:: ../../code/person/tests/test_person_w_class.py
  :language: python
  :lineno-start: 171
  :caption: person/tests/test_person.py
  :lines: 171-186

.. literalinclude:: ../../code/person/tests/test_person_w_class.py
  :language: python
  :lineno-start: 188
  :caption: person/tests/test_person.py
  :lines: 188-

-----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd person

  the terminal_ shows I am in the ``person`` folder_

  .. code-block:: python

    .../pumping_python/person

* I open ``test_person.py`` from the ``tests`` folder_

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    tests/test_person.py ....                           [100%]

    =================== 4 passed in A.BCs ====================

----

*********************************************************************************
add Person class
*********************************************************************************

I made a :ref:`function<what is a function?>` that makes a string_ to represent a person when I give it ``first_name``, ``last_name``, ``sex`` and ``year_of_birth``. I can also represent a person with a :ref:`class<everything is an object>` because it is :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` that belong together.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I make an :ref:`instance<how to test if something is an instance>` of a :ref:`class<everything is an object>` to represent ``joe`` in :ref:`test_joe` in ``tests/test_person.py``

.. code-block:: python
  :lineno-start: 38
  :emphasize-lines: 20-25
  :emphasize-text: Person

  def test_joe():
      first_name = 'joe'
      last_name = 'blow'
      sex = 'M'
      year_of_birth = 1996

      assert_person_factory_works(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth
      )

      assert_say_hello_works(
          first_name=first_name,
          last_name=last_name,
          year_of_birth=year_of_birth,
      )

      joe = Person(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )


  def test_jane():

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

.. code-block:: python

  NameError: name 'Person' is not defined

because there is no definition for ``Person`` in ``tests/test_person.py``.

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


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

  - The terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

    .. code-block:: python

      TypeError: Person() takes no arguments

    because :ref:`classes<everything is an object>` do not take arguments like a :ref:`function<what is a function?>` and I "called" this one with four arguments.

  - :ref:`classes<everything is an object>` need a :ref:`method (function)<what is a method?>` that handles arguments.
  - I can :ref:`make a class with the pass keyword<test_making_a_class_w_pass>`.
----

*********************************************************************************
the constructor method
*********************************************************************************

A `constructor method`_ is used to define what happens when :ref:`an instance (a copy) of a class<how to test if something is an instance>` is made.

* I add the `constructor method`_ to the :ref:`Person class<add Person class>` so it can take arguments

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-5

    class Person:

        # pass
        def __init__():
            return None


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() got
        an unexpected keyword argument 'first_name'

  I am violating the :ref:`method signature<how to make a function that takes input>` when I :ref:`call<how to call a function with input>` it in a way that is different from its :ref:`definition<how to make a function that takes input>`.

  .. code-block:: shell

    Person(
        first_name='joe',
        last_name='blow',
        sex='M',
        year_of_birth=1996,
    )
    └── Person.__init__(
            first_name='joe',
            last_name='blow',
            sex='M',
            year_of_birth=1996,
        )
        └── def __init__():
                return None

  which raises :ref:`TypeError<what causes TypeError?>` since the :ref:`__init__ method<the constructor method>` gets :ref:`called<how to call a function with input>` with a :ref:`name<test_keyword_arguments>` (``first_name``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I add ``first_name`` in parentheses so that the :ref:`__init__ method<the constructor method>` can take input

  .. code-block:: python
    :lineno-start: 4
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

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

  The test :ref:`calls the function<how to call a function with input>` with four :ref:`keyword arguments<test_keyword_arguments>` ``(first_name, last_name, sex and year_of_birth')``.

  Python_ does not know which value to use for the first argument if I use a :ref:`keyword<test_keyword_arguments>` and its :ref:`position<test_positional_arguments>`.

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

  - ``self`` is Python_ convention, I can use any name I want.
  - ``self`` is the :ref:`instance of the class<how to test if something is an instance>`.
  - The terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

    .. code-block:: shell

      TypeError:
          Person.__init__() got
          an unexpected keyword argument 'last_name'.
          Did you mean 'first_name'?

  - ``self`` is for the :ref:`instance of the class<how to test if something is an instance>`.
  - I am violating the :ref:`method signature<how to make a function that takes input>` when I :ref:`call<how to call a function with input>` it in a way that is different from its :ref:`definition<how to make a function that takes input>`

    .. code-block:: shell

      Person(
          first_name='joe',
          last_name='blow',
          sex='M',
          year_of_birth=1996,
      )
      └── Person.__init__(
              self,
              first_name='joe',
              last_name='blow',    # not in definition
              sex='M',
              year_of_birth=1996,
          )
          └── def __init__():
                  return None

    which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` got :ref:`called<how to call a function with input>` with a :ref:`name<test_keyword_arguments>` (``last_name``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

  - this is the same as making the :ref:`person function<extract person function>`.

* I add ``last_name`` to the :ref:`definition<how to make a function>` of :ref:`__init__<the constructor method>`

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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        Person.__init__() got
        an unexpected keyword argument 'sex'

  - ``self`` is the :ref:`instance of the class<how to test if something is an instance>`.
  - I am violating the :ref:`method signature<how to make a function that takes input>` when I :ref:`call<how to call a function with input>` it in a way that is different from its :ref:`definition<how to make a function that takes input>`.

    .. code-block:: shell

      Person(
          first_name='joe',
          last_name='blow',
          sex='M',
          year_of_birth=1996,
      )
      └── Person.__init__(
              self,
              first_name='joe',
              last_name='blow',
              sex='M',             # not in definition
              year_of_birth=1996,
          )
          └── def __init__(self, first_name, last_name):
                  return None

    which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` got :ref:`called<how to call a function with input>` with a :ref:`name<test_keyword_arguments>` (``sex``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.
  - Still the same as making the :ref:`person function<extract person function>`.

* I add ``sex`` to the :ref:`definition<how to make a function>` of the :ref:`__init__ method<the constructor method>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-12

    class Person:

        # pass
        # def __init__():
        # def __init__(first_name):
        # def __init__(self, first_name):
        # def __init__(self, first_name, last_name):
        def __init__(
                self, first_name, last_name,
                sex,
            ):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() got
               an unexpected keyword argument 'year_of_birth'

  - ``self`` is the :ref:`instance of the class<how to test if something is an instance>`.
  - I am violating the :ref:`method signature<how to make a function that takes input>` when I :ref:`call<how to call a function with input>` it in a way that is different from its :ref:`definition<how to make a function that takes input>`.

    .. code-block:: shell

      Person(
          first_name='joe',
          last_name='blow',
          sex='M',
          year_of_birth=1996,
      )
      └── Person.__init__(
              self,
              first_name='joe',
              last_name='blow',
              sex='M',
              year_of_birth=1996,  # not in definition
          )
          └── def __init__(
                      self, first_name, last_name,
                      sex,
                  ):
                  return None

    which raises :ref:`TypeError<what causes TypeError?>` because the ``__init__`` :ref:`method<what is a method?>` got :ref:`called<how to call a function with input>` with a :ref:`name<test_keyword_arguments>` (``year_of_birth``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.
  - Same as with the :ref:`person function<extract person function>`.

* I add ``year_of_birth`` to the :ref:`definition<how to make a function>` of the :ref:`__init__ method<the constructor method>`

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
                # sex,
                sex, year_of_birth,
            ):
            return None

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from the :ref:`Person class<add Person class>`

  .. code-block:: python
    :lineno-start: 4

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth,
            ):
            return None


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):


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
add say_hello method
*********************************************************************************

I made a person :ref:`say hi with a function<test say_hello function>`, I can also do the same thing with a :ref:`class<everything is an object>` because it is :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` that belong together.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` with a :ref:`call<how to call a function with input>` to the :ref:`say_hello function<test say_hello function>` with the :ref:`attributes<what is a class attribute?>` of ``joe`` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 20-25, 27-37

    def test_joe():
        first_name = 'joe'
        last_name = 'blow'
        sex = 'M'
        year_of_birth = 1996

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

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
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_jane():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'first_name'

  because there is nothing named ``first_name`` in the :ref:`Person class<add Person class>`, so Python_ cannot reach the ``first_name`` :ref:`attribute<what is a class attribute?>` of ``joe``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``self.first_name`` to the :ref:`__init__ method<the constructor method>` of the :ref:`Person class<add Person class>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth,
            ):
            self.first_name
            return None

  the terminal_ still shows :ref:`AttributeError<what causes AttributeError?>` because all I have done is add a reference to the ``first_name``, not defined it.

* I point ``self.first_name`` to the value for ``first_name`` when the :ref:`__init__ method<the constructor method>` is :ref:`called<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth,
            ):
            # self.first_name
            self.first_name = first_name
            return None

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: 'Person' object
                    has no attribute 'last_name'.
                    Did you mean: 'first_name'?

  because there is nothing named ``last_name`` in the :ref:`Person class<add Person class>`, so Python_ cannot reach the ``last_name`` :ref:`attribute<what is a class attribute?>` of ``joe``.

* I add ``self.last_name`` and point it to the value for ``last_name`` when the :ref:`__init__ method<the constructor method>` is called

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 9

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth,
            ):
            # self.first_name
            self.first_name = first_name
            self.last_name = last_name
            return None

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object
                    has no attribute 'year_of_birth'

  because there is nothing named ``year_of_birth`` in the :ref:`Person class<add Person class>`, so Python_ cannot reach the ``year_of_birth`` :ref:`attribute<what is a class attribute?>` of ``joe``.

* I add ``self.year_of_birth`` and point it to the value for ``year_of_birth`` when the :ref:`__init__ constructor method<the constructor method>` is called

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 10

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth,
            ):
            # self.first_name
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            return None

  the test passes.

  .. code-block:: shell

      ├── first_name = 'joe'
      ├── last_name = 'blow'
      ├── sex = 'M'
      ├── year_of_birth = 1996
      └── joe = Person(
              first_name=first_name,
              last_name=last_name,
              sex=sex,
              year_of_birth=year_of_birth,
          )
          └── Person.__init__(
                  self,
                  first_name=first_name,
                  last_name=last_name,
                  sex=sex,
                  year_of_birth=year_of_birth,
              )
              └── def __init__(
                      self, first_name, last_name,
                      sex, year_of_birth,
                  ):
                  ├── self.first_name = 'joe'
                  ├── self.last_name = 'blow'
                  ├── self.year_of_birth = 1996
                  └── return None

  ``self`` is the :ref:`instance of the class<how to test if something is an instance>`, ``joe`` in this case.

  .. code-block:: shell

    src.person.say_hello(
        first_name=joe.first_name,
        last_name=joe.last_name,
        year_of_birth=joe.year_of_birth,
    )
    └── src/
        └── person/
            └── __init__.py
                └── def say_hello(
                        first_name, last_name, year_of_birth,
                    ):
                    ├── first_name    = 'joe'
                    ├── last_name     = 'blow'
                    ├── year_of_birth = 1996
                    └── return (
                            f'Hello, my name is {first_name}'
                            f' {last_name} and I am'
                            f' {2026-year_of_birth}.'
                        )
                        return 'Hello, my name is joe blow and I am 30.'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line from the :ref:`Person class<add Person class>`

  .. code-block:: python
    :lineno-start: 4

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth,
            ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            return None


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

* I change the :ref:`call<how to call a function with input>` to ``src.person.say_hello`` in :ref:`test_joe` to a call to the :ref:`say_hello method<add say_hello method>` of the :ref:`Person class<add Person class>`

  .. code-block:: python
    :lineno-start: 69
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
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_jane():

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: type object 'Person'
                    has no attribute 'say_hello'

  because the test :ref:`calls<how to call a function with input>` the :ref:`say_hello method<add say_hello method>` which does not yet exist in the :ref:`Person class<add Person class>`.

* I add a :ref:`method definition<how to make a function>` for ``say_hello`` to the :ref:`Person class<add Person class>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 12-13

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth,
            ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            return None

        def say_hello():
            return None


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() got
               an unexpected keyword argument 'first_name'

  because the :ref:`say_hello method<add say_hello method>` got :ref:`called<how to call a function with input>` with a :ref:`name<test_keyword_arguments>` (``first_name``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I add ``first_name`` to the :ref:`method definition<how to make a function>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1-2

        # def say_hello():
        def say_hello(first_name):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: Person.say_hello() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

  because the :ref:`say_hello method<add say_hello method>` got :ref:`called<how to call a function with input>` with a :ref:`name<test_keyword_arguments>` (``last_name``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I add ``last_name`` to the :ref:`method definition<how to make a function>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2-3

        # def say_hello():
        # def say_hello(first_name):
        def say_hello(first_name, last_name):
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() got
               an unexpected keyword argument 'year_of_birth'

  because the :ref:`say_hello method<add say_hello method>` got :ref:`called<how to call a function with input>` with a :ref:`name<test_keyword_arguments>` (``year_of_birth``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I add ``year_of_birth`` to the :ref:`method definition<how to make a function>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3-4

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        def say_hello(first_name, last_name, year_of_birth):
            return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        assert None
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


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

  the test passes.

  .. code-block:: shell

    Person.say_hello(
        first_name=joe.first_name,
        last_name=joe.last_name,
        year_of_birth=joe.year_of_birth,
    )
    └── class Person:
        └── def say_hello(first_name, last_name, year_of_birth):
            ├── first_name    = 'joe'
            ├── last_name     = 'blow'
            ├── year_of_birth = 1996
            └── return 'Hello, my name is joe blow and I am 30.'

* I add a :ref:`call<how to call a function with input>` to the :ref:`say_hello method<add say_hello method>` of the :ref:`Person class<add person class>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 20-25, 27-37

    def test_jane():
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = 1991

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

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
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_john():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'Hello, my name ... and I am 30.'
                        == 'Hello, my name ... and I am 35.'

* I change :ref:`the return statement` to an :ref:`f-string<what is string interpolation?>` like I did with the :ref:`say_hello function<test say_hello function>`

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


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

  the test passes.

  .. code-block:: shell

      ├── first_name = 'jane'
      ├── last_name = 'doe'
      ├── sex = 'F'
      ├── year_of_birth = 1991
      └── jane = Person(
              first_name=first_name,
              last_name=last_name,
              sex=sex,
              year_of_birth=year_of_birth,
          )
          └── Person.__init__(
                  self,
                  first_name=first_name,
                  last_name=last_name,
                  sex=sex,
                  year_of_birth=year_of_birth,
              )
              └── def __init__(
                      self, first_name, last_name,
                      sex, year_of_birth,
                  ):
                  ├── self.first_name = 'jane'
                  ├── self.last_name = 'doe'
                  ├── self.year_of_birth = 1991
                  └── return None

  .. code-block:: shell

    Person.say_hello(
        first_name=jane.first_name,
        last_name=jane.last_name,
        year_of_birth=jane.year_of_birth,
    )
    └── def say_hello(first_name, last_name, year_of_birth):
        ├── first_name    = 'jane'
        ├── last_name     = 'doe'
        ├── year_of_birth = 1991
        └── return (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {2026-year_of_birth}.'
            )
            return 'Hello, my name is jane doe and I am 35.'

* I add an :ref:`instance (copy)<how to test if something is an instance>` of the :ref:`Person class<add person class>` to the :ref:`call<how to call a function with input>` to the :ref:`say_hello method<add say_hello method>` from :ref:`test_joe` because the :ref:`instance<how to test if something is an instance>` has the :ref:`attributes<what is a class attribute?>` I use in the :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 3

        # reality = src.person.say_hello(
        reality = Person.say_hello(
            person=joe,
            first_name=joe.first_name,
            last_name=joe.last_name,
            year_of_birth=joe.year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_jane():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() got
               an unexpected keyword argument 'person'

  because the :ref:`say_hello method<add say_hello method>` got :ref:`called<how to call a function with input>` with a :ref:`name<test_keyword_arguments>` (``person``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I add ``person`` to the :ref:`method definition for say_hello<add say_hello method>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 4-7

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        # def say_hello(first_name, last_name, year_of_birth):
        def say_hello(
                person, first_name, last_name, year_of_birth,
            ):
            # return None
            # return 'Hello, my name is joe blow and I am 30.'
            return (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {2026-year_of_birth}.'
            )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() missing
               1 required positional argument: 'person'

  I have to make the same change to :ref:`test_jane`

* I add the ``person`` :ref:`keyword argument<test_keyword_arguments>` to the :ref:`call<how to call a function with input>` to the :ref:`say_hello method<add say_hello method>` from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 132
    :emphasize-lines: 2

        reality = Person.say_hello(
            person=jane,
            first_name=jane.first_name,
            last_name=jane.last_name,
            year_of_birth=jane.year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_john():

  the test passes.

* I change :ref:`the return statement` of the :ref:`say_hello method<add say_hello method>` to use the :ref:`attributes<what is a class attribute?>` of the :ref:`class instance<how to test if something is an instance>` it receives as input

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 11-16

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        # def say_hello(first_name, last_name, year_of_birth):
        def say_hello(
                person, first_name, last_name, year_of_birth,
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


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

  the tests are still green

  .. code-block:: shell

    instance = Person(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )
    └── Person.__init__(
            self,
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )
        └── def __init__(
                self, first_name, last_name,
                sex, year_of_birth,
            ):
            ├── self.first_name    = first_name
            ├── self.last_name     = last_name
            ├── self.year_of_birth = year_of_birth
            └── return None

  .. code-block:: shell

    Person.say_hello(
        person=instance,
        first_name=instance.first_name,
        last_name=instance.last_name,
        year_of_birth=instance.year_of_birth,
    )
    └── Person.say_hello(
            person=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            year_of_birth=instance.year_of_birth,
        )
        └── def say_hello(
                person, first_name, last_name, year_of_birth,
            ):
            ├── person        = instance
            ├── first_name    = first_name
            ├── last_name     = last_name
            ├── year_of_birth = year_of_birth
            └── return (
                    f'Hello, my name is {person.first_name}'
                    f' {person.last_name} and I am'
                    f' {2026-person.year_of_birth}.'
                )
                return (
                    f'Hello, my name is {instance.first_name}'
                    f' {instance.last_name} and I am'
                    f' {2026-instance.year_of_birth}.'
                )

* I remove the ``first_name``, ``last_name`` and ``year_of_birth`` arguments from the :ref:`call<how to call a function with input>` to the :ref:`say_hello method<add say_hello method>` from :ref:`test_joe` since they are repetitions of the :ref:`class attributes<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 4-6

        # reality = src.person.say_hello(
        reality = Person.say_hello(
            person=joe,
            # first_name=joe.first_name,
            # last_name=joe.last_name,
            # year_of_birth=joe.year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_jane():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() missing
               3 required positional arguments:
               'first_name', 'last_name', and 'year_of_birth'

* I remove ``first_name``, ``last_name`` and ``year_of_birth`` from the :ref:`definition of the say_hello method<add say_hello method>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 6-7

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        # def say_hello(first_name, last_name, year_of_birth):
        def say_hello(
                # person, first_name, last_name, year_of_birth,
                person,
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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() got
               an unexpected keyword argument 'first_name'

  because the :ref:`say_hello method<add say_hello method>` got :ref:`called<how to call a function with input>` from :ref:`test_jane` with a :ref:`name<test_keyword_arguments>` (``first_name``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I remove the ``first_name``, ``last_name`` and ``year_of_birth`` arguments from the :ref:`call<how to call a function with input>` from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 3-5

        reality = Person.say_hello(
            person=jane,
            # first_name=jane.first_name,
            # last_name=jane.last_name,
            # year_of_birth=jane.year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_john():

  the test passes. This is still a repetition, I give an :ref:`instance (copy)<how to test if something is an instance>` of the :ref:`Person class<add person class>` as input to the :ref:`say_hello method<add Person class>` of the same :ref:`class<everything is an object>`.

* I change the :ref:`call<how to call a function with input>` to the :ref:`say_hello method<add say_hello method>` from :ref:`test_jane` because the :ref:`say_hello method<add say_hello method>` is in the :ref:`Person class<add Person class>` so its :ref:`copies<how to test if something is an instance>` also have the :ref:`say_hello method<add say_hello method>`

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 1-2

        # reality = Person.say_hello(
        reality = jane.say_hello(
            person=jane,
            # first_name=jane.first_name,
            # last_name=jane.last_name,
            # year_of_birth=jane.year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_john():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() got
               multiple values for argument 'person'

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument and I gave a value when I :ref:`called the method<how to call a function with input>`.

----

*********************************************************************************
what is the staticmethod decorator?
*********************************************************************************

* I can use the `staticmethod decorator`_ if I do not want to add ``self`` to the :ref:`method definition<how to make a function>` when it does not use anything that belongs to the :ref:`class<everything is an object>`, so I do not send more than what the :ref:`method<what is a method?>` needs. I add ``@staticmethod`` to the :ref:`say_hello method<add say_hello method>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        # def say_hello(first_name, last_name, year_of_birth):
        @staticmethod
        def say_hello(
                # person, first_name, last_name, year_of_birth,
                person,
            ):

  the test passes.

* I change the :ref:`call<how to call a function with input>` to ``Person.say_hello`` from :ref:`test_joe` because the :ref:`say_hello method<add say_hello method>` is in the :ref:`Person class<add Person class>`, there is no need for it to take a copy of the :ref:`Person class<add Person class>` as input since it should be able to use its own :ref:`attributes<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 2-4

        # reality = src.person.say_hello(
        # reality = Person.say_hello(
        reality = joe.say_hello(
            # person=joe,
            # first_name=joe.first_name,
            # last_name=joe.last_name,
            # year_of_birth=joe.year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_jane():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() missing
               1 required positional argument: 'person'

* I make ``person`` :ref:`optional<test_optional_arguments>` in the :ref:`say_hello method<add say_hello method>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 8-9

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        # def say_hello(first_name, last_name, year_of_birth):
        @staticmethod
        def say_hello(
                # person, first_name, last_name, year_of_birth,
                # person,
                person=None,
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
                # person, first_name, last_name, year_of_birth,
                # person,
                person=None,
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

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

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
                # person, first_name, last_name, year_of_birth,
                # person,
                # person=None,
                self, person=None,
            ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.say_hello() missing
               1 required positional argument: 'self'

* I remove the `staticmethod decorator`_ because I no longer need it since the :ref:`say_hello method<add say_hello method>` is using :ref:`class attributes<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5

        # def say_hello():
        # def say_hello(first_name):
        # def say_hello(first_name, last_name):
        # def say_hello(first_name, last_name, year_of_birth):
        # @staticmethod
        def say_hello(
                # person, first_name, last_name, year_of_birth,
                # person
                # person=None
                self, person=None
            ):

  the test passes because

  .. code-block:: shell

    instance = Person(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )
    └── Person.__init__(
            self,
            first_name='joe',
            last_name='blow',
            sex='M',
            year_of_birth=1996,
        )
        └── def __init__(
                self, first_name, last_name,
                sex, year_of_birth,
            ):
            ├── self.first_name    = first_name
            ├── self.last_name     = last_name
            ├── self.year_of_birth = year_of_birth
            └── return None

  ``self`` is the :ref:`instance of the class<how to test if something is an instance>`, ``instance`` in this case

  .. code-block:: shell

    instance.say_hello()
    └── class Person:
        └── def say_hello(self, person=None):
            ├── self = instance
            └── return (
                    f'Hello, my name is {self.first_name}'
                    f' {self.last_name} and I am'
                    f' {2026-self.year_of_birth}.'
                )
                return (
                    f'Hello, my name is {instance.first_name}'
                    f' {instance.last_name} and I am'
                    f' {2026-instance.year_of_birth}.'
                )

  a simple way to think of ``instance.say_hello()`` is

  .. code-block:: python

    instance = Person()
    instance.say_hello() == Person().say_hello()
    instance.say_hello() == Person().say_hello(Person())
    instance.say_hello() == instance.say_hello(Person())
    instance.say_hello() == instance.say_hello(instance)

  I do not need to pass ``joe`` as input to the :ref:`say_hello method<add say_hello method>` since it is ``self``.

* I remove ``person=jane`` from the :ref:`call<how to call a function with input>` to the :ref:`say_hello method<add say_hello method>` from :ref:`test_jane` because the :ref:`say_hello method<add say_hello method>` is in the :ref:`Person class<add Person class>`

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 3

        # reality = Person.say_hello(
        reality = jane.say_hello(
            # person=jane,
            # first_name=jane.first_name,
            # last_name=jane.last_name,
            # year_of_birth=jane.year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_john():

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`say_hello method<add say_hello method>` to :ref:`test_john`

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 20-25, 27-33

    def test_john():
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'
        year_of_birth = 1580

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        john = Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = john.say_hello()
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == None


    def test_mary():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        assert 'Hello, my name is john smith and I am 446.'
            == None

* I change my expectation to match ``reality`` in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 184
    :emphasize-lines: 7-8

        reality = john.say_hello()
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        # assert reality == None
        assert reality == my_expectation


    def test_mary():

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`say_hello method<add say_hello method>` to :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 194
    :emphasize-lines: 20-25, 27-33

    def test_mary():
        first_name = 'mary'
        last_name = 'public'
        sex = 'F'
        year_of_birth = 2000

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        mary = Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = mary.say_hello()
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == None


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        assert 'Hello, my name is mary public and I am 26.'
             == None

* I change my expectation to match ``reality`` in :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 220
    :emphasize-lines: 7-8

        reality = mary.say_hello()
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        # assert reality == None
        assert reality == my_expectation


    # Exceptions seen

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add say_hello method'

Since the :ref:`say_hello method<add say_hello method>` is the same as the :ref:`say_hello function<test say_hello function>` I could have use the :ref:`say_hello method<add say_hello method>` to :ref:`call<how to call a function with input>` the :ref:`say_hello function<test say_hello function>` to get the same result

.. code-block:: python

      def say_hello(self):
          return say_hello(
              first_name=self.first_name,
              last_name=self.last_name,
              year_of_birth=self.year_of_birth,
          )

----

*********************************************************************************
separate and equal Person class
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I change ``mary`` in :ref:`test_mary` to be an :ref:`instance<how to test if something is an instance>` of the :ref:`Person class<add person class>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of the :ref:`Person class<add person class>` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 213
    :emphasize-lines: 1-2

        # mary = Person(
        mary = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = mary.say_hello()
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        # assert reality == None
        assert reality == my_expectation


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.person'
                    has no attribute 'Person'

  because there is nothing with that name in ``src/person/__init__.py``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``__init__.py`` from the ``person`` folder_ in the ``src`` folder_

* I add the name to ``src/person/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    Person


    def say_hello(
            first_name, last_name, year_of_birth
        ):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'Person' is not defined

* I point ``Person`` to :ref:`None<what is None?>` to define it

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

  because the ``Person`` :ref:`function<what is a function?>` got :ref:`called<how to call a function with input>` with a :ref:`name<test_keyword_arguments>` (``first_name``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I add ``first_name`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # Person
    # Person = None
    # def Person():
    def Person(first_name):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: Person() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

  because the ``Person`` :ref:`function<what is a function?>` got :ref:`called<how to call a function with input>` with a :ref:`name<test_keyword_arguments>` (``last_name``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I add ``last_name`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    # Person
    # Person = None
    # def Person():
    # def Person(first_name):
    def Person(first_name, last_name):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person() got
               an unexpected keyword argument 'sex'

  because the ``Person`` :ref:`function<what is a function?>` got :ref:`called<how to call a function with input>` with a :ref:`name<test_keyword_arguments>` (``sex``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person() got
               an unexpected keyword argument 'year_of_birth'

  because the ``Person`` :ref:`function<what is a function?>` got :ref:`called<how to call a function with input>` with a :ref:`name<test_keyword_arguments>` (``year_of_birth``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

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

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'NoneType' object
                    has no attribute 'say_hello'

  because the :ref:`function<what is a function?>` I just made returns :ref:`None<what is None?>`

  .. code-block:: shell

    ├── first_name = 'mary'
    ├── last_name = 'public'
    ├── sex = 'F'
    ├── year_of_birth = 2000
    └── mary = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )
        └── src/
            └── person/
                └── __init__.py
                    └── def Person(
                            first_name, last_name,
                            sex, year_of_birth,
                        ):
                        └── return None

  .. code-block:: python

    reality = mary.say_hello()
    reality = None.say_hello()

  which raises :ref:`AttributeError<what causes AttributeError?>` since :ref:`None<what is None?>` does not have anything named ``say_hello`` in it.

* I change ``Person`` to a :ref:`class<everything is an object>`

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

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: 'return' outside function

* I add SyntaxError_ to the list of :ref:`Exceptions<how to test that an Exception is raised>` seen, in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 231
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError
    # SyntaxError

* I change :ref:`the return statement` in the ``Person`` :ref:`class<everything is an object>` to the pass_ keyword, in ``src/person/__init__.py``

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

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'first_name' is not defined

  because the only definitions for ``first_name`` are in the :ref:`say_hello<test say_hello function>` and :ref:`person functions<extract person function>` in ``src/person/__init__.py``.

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
    #         first_name, last_name,
    #         sex, year_of_birth,
    #     ):
    class Person:

        def __init__(
                first_name, last_name,
                sex, year_of_birth,
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
                sex, year_of_birth,
            ):
            # return None
            pass

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Person' object has no attribute 'say_hello'

  better, I can add an :ref:`attribute<what is a class attribute?>` to a :ref:`class<everything is an object>`.

* I add the name to the :ref:`Person class<add Person class>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3

    class Person:

        say_hello

        def __init__(
                # first_name, last_name,
                self, first_name, last_name,
                sex, year_of_birth,
            ):
            # return None
            pass

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

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
                sex, year_of_birth,
            ):
            # return None
            pass

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I change ``say_hello`` to a :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 4, 14-15

    class Person:

        # say_hello
        # say_hello = None

        def __init__(
                # first_name, last_name,
                self, first_name, last_name,
                sex, year_of_birth,
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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        assert None
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

* I remove the commented lines from :ref:`test_mary` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 194

    def test_mary():
        first_name = 'mary'
        last_name = 'public'
        sex = 'F'
        year_of_birth = 2000

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        mary = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = mary.say_hello()
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    # Exceptions seen

* I change ``john`` in :ref:`test_john` to be an :ref:`instance<how to test if something is an instance>` of the :ref:`Person class<add person class>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 171
    :emphasize-lines: 7-8

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        # john = Person(
        john = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = john.say_hello()
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        # assert reality == None
        assert reality == my_expectation


    def test_mary():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'Hello, my name ... and I am 26.'
                        == 'Hello, my name ...and I am 446.'

* I change :ref:`the return statement` of the :ref:`say_hello method<add say_hello method>` to return the input, in ``src/person/__init__.py``

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

  because ``argument`` is :ref:`an instance (a copy)<how to test if something is an instance>` of the :ref:`Person class<add Person class>`.

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

* I add ``self.first_name`` to the :ref:`__init__ constructor method<the constructor method>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 12-13

    class Person:

        # say_hello
        # say_hello = None

        def __init__(
                # first_name, last_name,
                self, first_name, last_name,
                sex, year_of_birth,
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

* I add ``self.last_name`` to the :ref:`__init__ method<the constructor method>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 9

        def __init__(
                # first_name, last_name,
                self, first_name, last_name,
                sex, year_of_birth,
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

* I add ``self.year_of_birth`` to the :ref:`__init__ constructor method<the constructor method>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 10

        def __init__(
                # first_name, last_name,
                self, first_name, last_name,
                sex, year_of_birth,
            ):
            # return None
            # pass
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth

        # def say_hello():

  the test passes.

* I change ``argument`` to ``self`` in the :ref:`say_hello method<add say_hello method>` to follow :ref:`Python convention<conventions>`

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
    instance.say_hello() == Person().say_hello(Person())
    instance.say_hello() == instance.say_hello(Person())
    instance.say_hello() == instance.say_hello(instance)

  I do not need to pass the :ref:`instance<how to test if something is an instance>` as input to the :ref:`say_hello method<add say_hello method>` since it is ``self``.

* I remove the commented lines from :ref:`test_john` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 158

    def test_john():
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'
        year_of_birth = 1580

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        john = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = john.say_hello()
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_mary():

* I change ``jane`` in :ref:`test_jane` to be an :ref:`instance<how to test if something is an instance>` of the :ref:`Person class<add person class>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 130
    :emphasize-lines: 7-8

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

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
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_john():

  the test is still green.

* I remove the commented lines from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 117

    def test_jane():
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = 1991

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        jane = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = jane.say_hello()
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_john():

* I change ``joe`` in :ref:`test_joe` to be an :ref:`instance<how to test if something is an instance>` of the :ref:`Person class<add person class>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 7-8

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

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
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_jane():

  the test is still green.

* I remove the commented lines from :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 75

    def test_joe():
        first_name = 'joe'
        last_name = 'blow'
        sex = 'M'
        year_of_birth = 1996

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        joe = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = joe.say_hello()
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_jane():

* I remove the :ref:`Person class<add Person class>` from ``tests/test_person.py``

  .. code-block:: python

    import src.person


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

  all the tests are still green because the :ref:`instances<how to test if something is an instance>` of the :ref:`Person class<add Person class>` that were in ``tests/test_person.py`` are now of the :ref:`Person class<add Person class>` in ``src/person/__init__.py``.

  .. code-block:: shell

    src.person.Person
    src/
    └── person/
        └── __init__.py
            └── class Person:
                └── def __init__(
                        self, first_name, last_name,
                        sex, year_of_birth,
                    ):
                    ├── self.first_name = first_name
                    ├── self.last_name = last_name
                    └── self.year_of_birth = year_of_birth

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move Person class to src'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can write solutions in a different module from the tests<separate and equal>`.

----

*********************************************************************************
extract assert_person_can_say_hello function
*********************************************************************************

:ref:`test_joe`, :ref:`tesT_jane`, :ref:`test_john` and :ref:`test_mary` use the same process to test the :ref:`say_hello method<add say_hello method>`, they

- make an :ref:`instance<how to test if something is an instance>` of the :ref:`Person class<add Person class>` with values for ``first_name``, ``last_name``, ``sex`` and ``year_of_birth``
- :ref:`call<how to call a function with input>` the :ref:`say_hello method of the Person class<add say_hello method>` with the values of ``first_name``, ``last_name`` and ``year_of_birth``
- make a string_ with the values of ``first_name``, ``last_name`` and ``year_of_birth``
- :ref:`assert<what is an assertion?>` that the result of the :ref:`call<how to call a function with input>` to the :ref:`say_hello method<add say_hello method>` is equal to the string_

.. code-block:: python

  instance = src.person.Person(
      first_name=first_name,
      last_name=last_name,
      sex=sex,
      year_of_birth=year_of_birth,
  )

  reality = instance.say_hello()
  my_expectation = (
      f'Hello, my name is {first_name}'
      f' {last_name} and I am'
      f' {2026-year_of_birth}.'
  )
  assert reality == my_expectation

I can make a :ref:`function<what is a function?>` that takes in ``first_name``, ``last_name`` and ``year_of_birth`` then :ref:`asserts<what is an assertion?>` that the result of the :ref:`call<how to call a function with input>` to the :ref:`say_hello method<add say_hello method>` with the values is equal to the string_ with the values of the given parameters.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a new :ref:`function<what is a function?>` to :ref:`assert<what is an assertion?>` that the result of the :ref:`call<how to call a function with input>` to the :ref:`say_hello method<add say_hello method>` with the :ref:`variables<what is a variable?>` is equal to the string_ with the values of the given parameters, in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-13, 15-21

    import src.person


    def assert_person_can_say_hello(
            first_name, last_name,
            sex, year_of_birth,
        ):
        instance = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = instance.say_hello()
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality != my_expectation


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

* I use the :ref:`assert_person_can_say_hello function<extract assert_person_can_say_hello function>` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 20-39

    def test_joe():
        first_name = 'joe'
        last_name = 'blow'
        sex = 'M'
        year_of_birth = 1996

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        # joe = src.person.Person(
        #     first_name=first_name,
        #     last_name=last_name,
        #     sex=sex,
        #     year_of_birth=year_of_birth,
        # )

        # reality = joe.say_hello()
        # my_expectation = (
        #     f'Hello, my name is {first_name}'
        #     f' {last_name} and I am'
        #     f' {2026-year_of_birth}.'
        # )
        # assert reality == my_expectation
        assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )


    def test_jane():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'Hello, my name is joe blow and I am 30.'
                        != 'Hello, my name is joe blow and I am 30.'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` in the :ref:`assert_person_can_say_hello function<extract assert_person_can_say_hello function>`

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 18-19

  def assert_person_can_say_hello(
          first_name, last_name,
          sex, year_of_birth,
      ):
      instance = src.person.Person(
          first_name=first_name,
          last_name=last_name,
          sex=sex,
          year_of_birth=year_of_birth,
      )

      reality = instance.say_hello()
      my_expectation = (
          f'Hello, my name is {first_name}'
          f' {last_name} and I am'
          f' {2026-year_of_birth}.'
      )
      # assert reality != my_expectation
      assert reality == my_expectation


  def assert_say_hello_works(
          first_name, last_name,
          year_of_birth,
      ):

the test passes.

.. code-block:: shell

  assert_person_can_say_hello(
        first_name=first_name, last_name=last_name,
        sex=sex, year_of_birth=year_of_birth,
  ) -> None
  └── def assert_person_can_say_hello(
          first_name, last_name,
          sex, year_of_birth,
      ):
      ├── instance = src.person.Person(
      │       first_name=first_name,
      │       last_name=last_name,
      │       sex=sex,
      │       year_of_birth=year_of_birth,
      │   )
      │   └── src/person/__init__.py
      │       └── class Person:
      │           └── def __init__(
      │                   self, first_name, last_name,
      │                   sex, year_of_birth,
      │               ):
      │               ├── self.first_name = first_name
      │               ├── self.last_name = last_name
      │               └── self.year_of_birth = year_of_birth
      ├── reality = instance.say_hello()
      │             └── class Person:
      │                 └── def say_hello(self):
      │                     └── return (
      │                             f'Hello, my name is {self.first_name}'
      │                             f' {self.last_name} and I am'
      │                             f' {2026-self.year_of_birth}.'
      │                         )
      ├── my_expectation = (
      │       f'Hello, my name is {first_name}'
      │       f' {last_name} and I am'
      │       f' {2026-year_of_birth}.'
      │   )
      └── assert reality == my_expectation

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----


* I remove the commented line from :ref:`assert_person_can_say_hello<extract assert_person_can_say_hello function>`

  .. code-block:: python
    :lineno-start: 4

    def assert_person_can_say_hello(
            first_name, last_name,
            sex, year_of_birth,
        ):
        instance = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = instance.say_hello()
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

* I remove the commented lines from :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 58

    def test_joe():
        first_name = 'joe'
        last_name = 'blow'
        sex = 'M'
        year_of_birth = 1996

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )


    def test_jane():

* I use the :ref:`assert_person_can_say_hello function<extract assert_person_can_say_hello function>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 20-39

    def test_jane():
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = 1991

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        # jane = src.person.Person(
        #     first_name=first_name,
        #     last_name=last_name,
        #     sex=sex,
        #     year_of_birth=year_of_birth,
        # )

        # reality = jane.say_hello()
        # my_expectation = (
        #     f'Hello, my name is {first_name}'
        #     f' {last_name} and I am'
        #     f' {2026-year_of_birth}.'
        # )
        # assert reality == my_expectation
        assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )


    def test_john():

  the test is still green.

* I remove the commented lines from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 85

    def test_jane():
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = 1991

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )


    def test_john():

* I use the :ref:`assert_person_can_say_hello function<extract assert_person_can_say_hello function>` in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 20-39

    def test_john():
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'
        year_of_birth = 1580

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        # john = src.person.Person(
        #     first_name=first_name,
        #     last_name=last_name,
        #     sex=sex,
        #     year_of_birth=year_of_birth,
        # )

        # reality = john.say_hello()
        # my_expectation = (
        #     f'Hello, my name is {first_name}'
        #     f' {last_name} and I am'
        #     f' {2026-year_of_birth}.'
        # )
        # assert reality == my_expectation
        assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )


    def test_mary():

  still green.

* I remove the commented lines from :ref:`test_john`

  .. code-block:: python
    :lineno-start: 112

    def test_john():
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'
        year_of_birth = 1580

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )


    def test_mary():

* I use the :ref:`assert_person_can_say_hello function<extract assert_person_can_say_hello function>` in :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 139
    :emphasize-lines: 20-39

    def test_mary():
        first_name = 'mary'
        last_name = 'public'
        sex = 'F'
        year_of_birth = 2000

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        # mary = src.person.Person(
        #     first_name=first_name,
        #     last_name=last_name,
        #     sex=sex,
        #     year_of_birth=year_of_birth,
        # )

        # reality = mary.say_hello()
        # my_expectation = (
        #     f'Hello, my name is {first_name}'
        #     f' {last_name} and I am'
        #     f' {2026-year_of_birth}.'
        # )
        # assert reality == my_expectation
        assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )


    # Exceptions seen

  green.

* I remove the commented lines from :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 139

    def test_mary():
        first_name = 'mary'
        last_name = 'public'
        sex = 'F'
        year_of_birth = 2000

        assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract assert_person_can_say_hello function'

----

*********************************************************************************
use assert_equal function
*********************************************************************************

:ref:`assert_person_can_say_hello<extract assert_person_can_say_hello function>`, :ref:`assert_say_hello_works<extract assert_say_hello_works function>` and :ref:`assert_person_factory_works<assert_person_factory_works function>` all :ref:`assert<what is an assertion?>` that something is equal to something else

.. code-block:: python

  assert reality == my_expectation

I can use the :ref:`assert_equal function<extract assert_equal function>` that takes in two inputs then :ref:`asserts<what is an assertion?>` that they are equal.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add the :ref:`assert_equal function<extract assert_equal function>` to ``tests/test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import src.person


    def assert_equal(left, right):
        assert left != right


    def assert_person_can_say_hello(
            first_name, last_name,
            sex, year_of_birth,
        ):

* I use the :ref:`assert_equal function<extract assert_equal function>` in :ref:`assert_person_can_say_hello<extract assert_person_can_say_hello function>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 18*19

    def assert_person_can_say_hello(
            first_name, last_name,
            sex, year_of_birth,
        ):
        instance = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = instance.say_hello()
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        # assert reality == my_expectation
        assert_equal(reality, my_expectation)


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    FAILED ...::test_joe - AssertionError:
        assert 'Hello, my name is joe blow and I am 30.' != ...
    FAILED ...::test_jane - AssertionError:
        assert 'Hello, my name is jane doe and I am 35.' != ...
    FAILED ...::test_john - AssertionError:
        assert 'Hello, my name is john smith and I am 446.' ...
    FAILED ...::test_mary - AssertionError:
        assert 'Hello, my name is mary public and I am 26.' ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` in the :ref:`assert_equal function<extract assert_equal function>`

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 18-19

  def assert_equal(left, right):
      # assert left != right
      assert left == right


  def assert_person_can_say_hello(
          first_name, last_name,
          sex, year_of_birth,
      ):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line from :ref:`assert_equal<extract assert_equal function>`

  .. code-block:: python
    :lineno-start: 4

    def assert_equal(left, right):
        assert left == right


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

* I use the value of ``my_expectation`` in :ref:`assert_person_can_say_hello<extract assert_person_can_say_hello function>` without a :ref:`variable<what is a variable?>` since it is only used once

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2-16

        reality = instance.say_hello()
        # my_expectation = (
        #     f'Hello, my name is {first_name}'
        #     f' {last_name} and I am'
        #     f' {2026-year_of_birth}.'
        # )
        # assert reality == my_expectation
        # assert_equal(reality, my_expectation)
        assert_equal(
            reality,
            (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {2026-year_of_birth}.'
            )
        )


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

  the test is still green.

* I do the same thing with ``reality`` in :ref:`assert_person_can_say_hello<extract assert_person_can_say_hello function>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 1, 10-11

        # reality = instance.say_hello()
        # my_expectation = (
        #     f'Hello, my name is {first_name}'
        #     f' {last_name} and I am'
        #     f' {2026-year_of_birth}.'
        # )
        # assert reality == my_expectation
        # assert_equal(reality, my_expectation)
        assert_equal(
            # reality,
            instance.say_hello(),
            (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {2026-year_of_birth}.'
            )
        )


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

  still green.

* I use the :ref:`instance<how to test if something is an instance>` of the :ref:`Person class<add Person class>` directly without a :ref:`variable<what is a variable?>` since it is only used once

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 5-10, 22-28

    def assert_person_can_say_hello(
            first_name, last_name,
            sex, year_of_birth,
        ):
        # instance = src.person.Person(
        #     first_name=first_name,
        #     last_name=last_name,
        #     sex=sex,
        #     year_of_birth=year_of_birth,
        # )

        # reality = instance.say_hello()
        # my_expectation = (
        #     f'Hello, my name is {first_name}'
        #     f' {last_name} and I am'
        #     f' {2026-year_of_birth}.'
        # )
        # assert reality == my_expectation
        # assert_equal(reality, my_expectation)
        assert_equal(
            # reality,
            # instance.say_hello(),
            src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            ).say_hello(),
            (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {2026-year_of_birth}.'
            )
        )

  green and not as easy to read.

* I use the :ref:`assert_equal function<extract assert_equal function>` in :ref:`assert_say_hello_works<extract assert_say_hello_works function>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 5-27

    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):
        # reality = src.person.say_hello(
        #     first_name=first_name,
        #     last_name=last_name,
        #     year_of_birth=year_of_birth
        # )
        # my_expectation = (
        #     f'Hello, my name is {first_name}'
        #     f' {last_name} and I am'
        #     f' {2026-year_of_birth}.'
        # )
        # assert reality == my_expectation
        assert_equal(
            src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth
            ),
            (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {2026-year_of_birth}.'
            )
        )


    def assert_person_factory_works(
            first_name, last_name,
            sex, year_of_birth
        ):

  the tests are still green.

* I remove the commented lines from :ref:`assert_say_hello_works<extract assert_say_hello_works function>`

  .. code-block:: python
    :lineno-start: 27

    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):
        assert_equal(
            src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth
            ),
            (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {2026-year_of_birth}.'
            )
        )


    def assert_person_factory_works(
            first_name, last_name,
            sex, year_of_birth
        ):

* I use the :ref:`assert_equal function<extract assert_equal function>` in :ref:`assert_person_factory_works<extract assert_person_factory_works function>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 5-27

    def assert_person_factory_works(
            first_name, last_name,
            sex, year_of_birth
        ):
        # reality = src.person.person(
        #     first_name=first_name,
        #     last_name=last_name,
        #     sex=sex,
        #     year_of_birth=year_of_birth,
        # )
        # my_expectation = (
        #     f'{first_name}, {last_name},'
        #     f' {sex}, {year_of_birth}'
        # )
        # assert reality == my_expectation
        assert_equal(
            src.person.person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            ),
            (
                f'{first_name}, {last_name},'
                f' {sex}, {year_of_birth}'
            )
        )


    def test_joe():

  still green.

* I remove the commented lines from :ref:`assert_person_factory_works<extract assert_person_factory_works function>`

  .. code-block:: python
    :lineno-start: 45

    def assert_person_factory_works(
            first_name, last_name,
            sex, year_of_birth
        ):
        assert_equal(
            src.person.person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            ),
            (
                f'{first_name}, {last_name},'
                f' {sex}, {year_of_birth}'
            )
        )


    def test_joe():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract assert_equal function'

I used the :ref:`assert_equal function<extract assert_equal function>` to remove repetition which ended up adding more lines to the code than before I used it.

----

*********************************************************************************
test_dir_person_class
*********************************************************************************

Python_ has the `dir built-in function`_ which shows the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the :ref:`object<everything is an object>` it is given in parentheses. It allows me to see what makes up an :ref:`object<everything is an object>` without looking at the code or reading the documentation. I can then run tests to see what each thing does.

I want to use it to see the :ref:`attributes and methods of the Person class<test_dir_person_class>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a new test with the `dir built-in function`_ in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 163
    :emphasize-lines: 9-13

        assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )


    def test_dir_person_class():
        assert_equal(
            dir(src.person.Person),
            None
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        assert ['__class__', '__delattr__', '__dict__',
                '__dir__', '__doc__', '__eq__', ...]
            == None

  because dir_ returned a :ref:`list <what is a list?>` (anything in square brackets ``[ ]``) and the expectation of the :ref:`assertion<what is an assertion?>` is :ref:`None<what is None?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_ and paste (:kbd:`ctrl/command+v`) them as the expectation

  .. code-block:: python
    :lineno-start: 171
    :emphasize-lines: 4-8

    def test_dir_person_class():
        assert_equal(
            dir(src.person.Person),
            # None
            [
                '__class__', '__delattr__', '__dict__',
                '__dir__', '__doc__', '__eq__', ...
            ]
        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E         AssertionError:
                  assert ['__class__',...'__eq__', ...]
                      == ['__class__',...'__eq__', ...]
    E
    E         At index 6 diff: '__firstlineno__' != Ellipsis
    E         Left contains 23 more items,
                  first extra item: '__format__'
    E         Use -v to get more diff

* I click in the terminal_ where the tests are running then press :kbd:`v` on the keyboard for `pytest-watcher`_ to show me more of the difference between ``reality`` and ``my_expectation`` and it shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E         ...Full output truncated (31 lines hidden),
                 use '-vv' to show

* I press :kbd:`w` on the keyboard in the terminal_ where the tests are running, to show the menu for `pytest-watcher`_ and it shows

  .. code-block:: python
    :emphasize-lines: 2, 10

    [pytest-watcher]
    Current runner args: [-v]

    Controls:
    > Enter : Invoke test runner
    > r     : reset all runner args
    > c     : change runner args
    > f     : run only failed tests (--lf)
    > p     : drop to pdb on fail (--pdb)
    > v     : increase verbosity (-v)
    > e     : Erase terminal screen
    > q     : quit pytest-watcher

* I press :kbd:`c` on the keyboard to change runner args, and the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 7, 14

    [pytest-watcher]
    Current runner args: []

    Controls:
    > Enter : Invoke test runner
    > r     : reset all runner args
    > c     : change runner args
    > f     : run only failed tests (--lf)
    > p     : drop to pdb on fail (--pdb)
    > v     : increase verbosity (-v)
    > e     : Erase terminal screen
    > q     : quit pytest-watcher

    Enter new runner args: -vv

* I type :kbd:`-+v+v` then press :kbd:`enter` to show the full difference, and the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with the full :ref:`list<what is a list?>`.

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_ and paste (:kbd:`ctrl/command+v`) them as the expectation

  .. caution:: Your list of attributes and methods may be different because of your Python version.

  .. code-block:: python
    :lineno-start: 171
    :emphasize-lines: 4-15
    :emphasize-text: __init__ say_hello

    def test_dir_person_class():
        assert_equal(
            dir(src.person.Person),
            [
                '__class__', '__delattr__', '__dict__',
                '__dir__', '__doc__', '__eq__',
                '__firstlineno__', '__format__', '__ge__',
                '__getattribute__', '__getstate__', '__gt__',
                '__hash__', '__init__', '__init_subclass__',
                '__le__', '__lt__', '__module__', '__ne__',
                '__new__', '__reduce__', '__reduce_ex__',
                '__repr__', '__setattr__', '__sizeof__',
                '__static_attributes__', '__str__',
                '__subclasshook__', '__weakref__', 'say_hello'
            ]
        )


    # Exceptions seen

  - the test passes.
  - The :ref:`__init__<the constructor method>` and :ref:`say_hello methods<add say_hello method>` I defined are in the :ref:`list of attributes and methods<test_dir_person_class>`.
  - There are names in the :ref:`list<what is a list?>` that I did not define, which leads to the question of :ref:`where did they come from?<everything is an object>`
  - The :ref:`attributes<what is a class attribute?>` I defined in the :ref:`__init__ method<the constructor method>` are not in the :ref:`list<what is a list?>`, because the test called dir_ on ``src.person.Person`` which is the :ref:`class<everything is an object>`, not :ref:`an instance of the class<how to test if something is an instance>`.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_dir_person_class'


----

*********************************************************************************
test_dir_person_instance
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to see the difference between the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of :ref:`an instance<how to test if something is an instance>` and the actual :ref:`class<everything is an object>`

.. code-block:: python
  :lineno-start: 182
  :emphasize-lines: 7-29

                '__repr__', '__setattr__', '__sizeof__',
                '__static_attributes__', '__str__',
                '__subclasshook__', '__weakref__', 'say_hello'
            ]
        )

    def test_dir_person_instance():
        assert_equal(
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
                '__dir__', '__doc__', '__eq__',
                '__firstlineno__', '__format__', '__ge__',
                '__getattribute__', '__getstate__', '__gt__',
                '__hash__', '__init__', '__init_subclass__',
                '__le__', '__lt__', '__module__', '__ne__',
                '__new__', '__reduce__', '__reduce_ex__',
                '__repr__', '__setattr__', '__sizeof__',
                '__static_attributes__', '__str__',
                '__subclasshook__', '__weakref__', 'say_hello'
            ]
        )


    # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :emphasize-lines: 11
  :emphasize-text: first_name last_name year_of_birth

  AssertionError:
      assert [
          '__class__', '__delattr__', '__dict__', '__dir__',
          '__doc__', '__eq__', '__firstlineno__', '__format__',
          '__ge__', '__getattribute__', '__getstate__', '__gt__',
          '__hash__', '__init__', '__init_subclass__', '__le__',
          '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
          '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
          '__static_attributes__', '__str__', '__subclasshook__',
          '__weakref__',
          'first_name', 'last_name', 'say_hello', 'year_of_birth'
      ]
   == [
          '__class__', '__delattr__', '__dict__', '__dir__',
          '__doc__', '__eq__', '__firstlineno__', '__format__',
          '__ge__', '__getattribute__', '__getstate__', '__gt__',
          '__hash__', '__init__', '__init_subclass__', '__le__',
          '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
          '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
          '__static_attributes__', '__str__', '__subclasshook__',
          '__weakref__', 'say_hello'
      ]

because ``first_name``, ``last_name`` and ``year_of_birth`` are missing. Why is there no ``sex``?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the missing :ref:`attributes<what is a class attribute?>` to the expectation of the :ref:`assertion<what is an assertion?>` of :ref:`test_dir_person_instance`

.. code-block:: python
  :lineno-start: 198
  :emphasize-lines: 11-12
  :emphasize-text: first_name last_name year_of_birth

            [
                '__class__', '__delattr__', '__dict__',
                '__dir__', '__doc__', '__eq__',
                '__firstlineno__', '__format__', '__ge__',
                '__getattribute__', '__getstate__', '__gt__',
                '__hash__', '__init__', '__init_subclass__',
                '__le__', '__lt__', '__module__', '__ne__',
                '__new__', '__reduce__', '__reduce_ex__',
                '__repr__', '__setattr__', '__sizeof__',
                '__static_attributes__', '__str__',
                '__subclasshook__', '__weakref__', 'first_name',
                'last_name', 'say_hello', 'year_of_birth',
            ]
        )


    # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add ``sex`` to the :ref:`list<what is a list?>` of :ref:`attributes and methods of the instance of the Person class<test_dir_person_instance>`

  .. code-block:: python
    :lineno-start: 188
    :emphasize-lines: 22

    def test_dir_person_instance():
        assert_equal(
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
                '__dir__', '__doc__', '__eq__',
                '__firstlineno__', '__format__', '__ge__',
                '__getattribute__', '__getstate__', '__gt__',
                '__hash__', '__init__', '__init_subclass__',
                '__le__', '__lt__', '__module__', '__ne__',
                '__new__', '__reduce__', '__reduce_ex__',
                '__repr__', '__setattr__', '__sizeof__',
                '__static_attributes__', '__str__',
                '__subclasshook__', '__weakref__', 'first_name',
                'last_name', 'say_hello', 'sex', 'year_of_birth',
            ]
        )


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError
    # SyntaxError

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 22
    :emphasize-text: sex

      AssertionError:
          assert [
              '__class__', '__delattr__', '__dict__', '__dir__',
              '__doc__', '__eq__', '__firstlineno__', '__format__',
              '__ge__', '__getattribute__', '__getstate__', '__gt__',
              '__hash__', '__init__', '__init_subclass__', '__le__',
              '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
              '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
              '__static_attributes__', '__str__', '__subclasshook__',
              '__weakref__',
              'first_name', 'last_name', 'say_hello', 'year_of_birth'
          ]
       == [
              '__class__', '__delattr__', '__dict__', '__dir__',
              '__doc__', '__eq__', '__firstlineno__', '__format__',
              '__ge__', '__getattribute__', '__getstate__', '__gt__',
              '__hash__', '__init__', '__init_subclass__', '__le__',
              '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
              '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
              '__static_attributes__', '__str__', '__subclasshook__',
              '__weakref__', 'first_name', 'last_name', 'say_hello',
              'sex', 'year_of_birth'
          ]

  the ``sex`` :ref:`attribute<what is a class attribute?>` is not defined anywhere in the :ref:`Person class<add Person class>`.

* I add ``self.sex`` to the :ref:`__init__ method<the constructor method>` of the :ref:`Person class<add Person class>` in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 16

    class Person:

        # say_hello
        # say_hello = None

        def __init__(
                # first_name, last_name,
                self, first_name, last_name,
                sex, year_of_birth,
            ):
            # return None
            # pass
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            self.sex = sex

        # def say_hello():

  the test passes.

* I remove the commented lines from the :ref:`Person class<separate and equal Person class>`

  .. code-block:: python
    :linenos:

    class Person:

        def __init__(
                self, first_name, last_name,
                sex, year_of_birth,
            ):
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = year_of_birth
            self.sex = sex

        def say_hello(self):
            return (
                f'Hello, my name is {self.first_name}'
                f' {self.last_name} and I am'
                f' {2026-self.year_of_birth}.'
            )


    def say_hello(
            first_name, last_name, year_of_birth
        ):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_dir_person_instance'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``src/person/__init__.py`` and ``tests/test_person.py``
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

* I ran tests to write a :ref:`class<everything is an object>` that makes a person when given ``first_name``, ``last_name``, ``sex`` and ``year_of_birth`` and has a :ref:`method<what is a method?>` so I do not have to pass the same values every time I want to do something with a person.

* My tests have a problem, each test is now the same three tests. There has to be a way that I can use one test for all the people.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a person with a class: tests and solution>`

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

.. toctree::
  :titlesonly:
  :maxdepth: 1

  ../../classes/inheritance
  ../../classes/unittest

:ref:`Would you like to know where the extra attributes and methods of the Person class came from?<everything is an object>`

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