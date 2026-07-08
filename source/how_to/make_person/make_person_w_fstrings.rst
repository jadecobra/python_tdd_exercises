.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): how to make a person with f-strings. Use f-strings + one factory function (instead of one function per person) that takes first_name, last_name, sex, year_of_birth and returns 'name, surname, X, YYYY'. Add say_hello using f-strings for 'Hello, my name is ... and I am N.'. Start in the person project; uv run pytest-watcher . --now. Progressively introduce f-strings in the return, required args then keyword arguments, move factory and say_hello to src/person.py (AttributeError: module 'src.person' has no attribute 'factory'), use local variables in tests to remove repetition of the data, remove commented lines. Ends with 4 tests calling src.person.factory + src.person.say_hello + # Exceptions seen (AssertionError, NameError, TypeError, AttributeError). Shows why even with f-strings the 4 tests are repetitive. What is next: separate and equal functions. Code: person/tests/test_person_w_fstrings.py and person/solutions/person_w_fstrings.py.
  :keywords: Jacob Itegboje, Pumping Python, how to make a person with f-strings, python f-strings, f-string factory function, one function instead of one per person, src.person, import src.person, AttributeError module 'src.person' has no attribute 'factory', TypeError missing required positional argument, uv run pytest-watcher, red green refactor f-strings, variables remove repetition in tests, first_name last_name sex year_of_birth, say_hello f-string age 2026-year_of_birth, remove the commented lines, test_joe test_jane test_john test_mary, person factory with f-strings, separate tests and solution, what is next separate and equal functions

.. include:: ../../links.rst

#################################################################################
how to make a person with f-strings
#################################################################################

----

Since I can pass :ref:`objects<what is a class?>` into a string_ with :ref:`f-strings<what is string interpolation?>`. I can write one :ref:`function<what is a function?>` that makes a person instead of making one :ref:`function<what is a function?>` for each person.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_fstrings.py
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

    .../pumping_python/ove

* I open ``test_person.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows the tests from before are passing.

----

*********************************************************************************
test person factory
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` to :ref:`test_joe` in ``test_person.py``

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 4-6

    def test_joe():
        assert joe() == 'joe, blow, M, 1996'

        reality = factory()
        my_expectation = 'joe, blow, M, 1996'
        assert reality == my_expectation


    def test_jane():

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'factory' is not defined

because I have not defined ``factory`` in ``test_person.py``, yet.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function definition<how to make a function that takes input>` for it

.. code-block:: python
  :linenos:
  :emphasize-lines: 1-2

  def factory():
      return 'joe, blow, M, 1996'


  def joe():

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` with a call to the :ref:`factory function<test person factory>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 12-14

    def test_joe():
        assert joe() == 'joe, blow, M, 1996'

        reality = factory()
        my_expectation = 'joe, blow, M, 1996'
        assert reality == my_expectation


    def test_jane():
        assert jane() == 'jane, doe, F, 1991'

        reality = factory()
        my_expectation = 'jane, doe, F, 1991'
        assert reality == my_expectation


    def test_john():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'joe, blow, M, 1996'
                        == 'jane, doe, F, 1991'

  because the :ref:`factory function<test person factory>` always returns ``joe, blow, M, 1996`` when it is called. It has to return a string_ based on the input it gets for me to be able to use it to make more than one person.

* I :ref:`make the function take input<how to make a function that takes input>` for the first name

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # def factory():
    def factory(first_name):
        return 'joe, blow, M, 1996'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() missing
               1 required positional argument:
               'first_name'

  because

  - I called the :ref:`factory function<test person factory>` with zero inputs.
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``factory`` has one required argument (``first_name``).
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I add ``'jane'`` to the call to the :ref:`factory function<test person factory>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4-5

    def test_jane():
        assert jane() == 'jane, doe, F, 1991'

        # reality = factory()
        reality = factory('jane')
        my_expectation = 'jane, doe, F, 1991'
        assert reality == my_expectation


    def test_john():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'joe, blow, M, 1996'
                        == 'jane, doe, F, 1991'

* I change :ref:`the return statement` of the :ref:`factory function<test person factory>` to an :ref:`f-string<what is string interpolation?>` to use ``first_name`` in the output

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # def factory():
    def factory(first_name):
        # return 'joe, blow, M, 1996'
        return f'{first_name}, blow, M, 1996'


    def joe():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'jane, blow, M, 1996'
                        == 'jane, doe, F, 1991'

  the first names match. Progress!

* I add ``last_name`` to :ref:`the return statement`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-8

    # def factory():
    def factory(first_name):
        # return 'joe, blow, M, 1996'
        # return f'{first_name}, blow, M, 1996'
        return (
            f'{first_name}, {last_name},'
            ' M, 1996'
        )


    def joe():

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'last_name' is not defined

* I add the name to the parentheses to define it in the :ref:`factory function<test person factory>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    # def factory():
    # def factory(first_name):
    def factory(first_name, last_name):
        # return 'joe, blow, M, 1996'
        # return f'{first_name}, blow, M, 1996'
        return (
            f'{first_name}, {last_name},'
            ' M, 1996'
        )


    def joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() missing
               1 required positional argument:
               'last_name'

  because

  - I called the :ref:`factory function<test person factory>` with one input (``jane``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``factory`` has two required arguments (``first_name`` and ``last_name``).
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I add ``'doe'`` to the call to the :ref:`factory function<test person factory>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 5-6

    def test_jane():
        assert jane() == 'jane, doe, F, 1991'

        # reality = factory()
        # reality = factory('jane')
        reality = factory('jane', 'doe')
        my_expectation = 'jane, doe, F, 1991'
        assert reality == my_expectation


    def test_john():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'jane, doe, M, 1996'
                        == 'jane, doe, F, 1991'

  the first and last names match. More progress.

* I use :ref:`keyword arguments<test_keyword_arguments>` with a value for ``sex`` (since I have more than two) to change the call to the :ref:`factory function<test person factory>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 6-11

    def test_jane():
        assert jane() == 'jane, doe, F, 1991'

        # reality = factory()
        # reality = factory('jane')
        # reality = factory('jane', 'doe')
        reality = factory(
            first_name='jane',
            last_name='doe',
            sex='F',
        )
        my_expectation = 'jane, doe, F, 1991'
        assert reality == my_expectation


    def test_john():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() got an unexpected
               keyword argument 'sex'

  because

  - I called the :ref:`factory function<test person factory>` with three :ref:`keyword arguments<test_keyword_arguments>` input (``first_name``, ``last_name`` and ``sex``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``factory`` has two required arguments (``first_name`` and ``last_name``).
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I add ``sex`` in the parentheses of the ``factory`` :ref:`function definition<how to make a function that takes input>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(first_name, last_name, sex):
        # return 'joe, blow, M, 1996'
        # return f'{first_name}, blow, M, 1996'
        return (
            f'{first_name}, {last_name},'
            ' M, 1996'
        )


    def joe():

  the terminal_ shows the last :ref:`AssertionError<what causes AssertionError?>` again.

* I add ``sex`` to the :ref:`f-string<what is string interpolation?>` in the :ref:`factory function<test person factory>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9-10

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(first_name, last_name, sex):
        # return 'joe, blow, M, 1996'
        # return f'{first_name}, blow, M, 1996'
        return (
            f'{first_name}, {last_name},'
            # ' M, 1996'
            f' {sex}, 1996'
        )


    def joe():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'jane, doe, F, 1996'
                        == 'jane, doe, F, 1991'

  the first name, last name and sex match. Yes!

* I add ``year_of_birth`` to :ref:`the return statement`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(first_name, last_name, sex):
        # return 'joe, blow, M, 1996'
        # return f'{first_name}, blow, M, 1996'
        return (
            f'{first_name}, {last_name},'
            # ' M, 1996'
            # f' {sex}, 1996'
            f' {sex}, {year_of_birth}'
        )


    def joe():

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'year_of_birth' is not defined

* I add ``year_of_birth`` to the parentheses to define it in the :ref:`factory function<test person factory>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-8

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    # def factory(first_name, last_name, sex):
    def factory(
        first_name, last_name,
        sex, year_of_birth
    ):
        # return 'joe, blow, M, 1996'
        # return f'{first_name}, blow, M, 1996'
        return (
            f'{first_name}, {last_name},'
            # ' M, 1996'
            # f' {sex}, 1996'
            f' {sex}, {year_of_birth}'
        )


    def joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() missing
               1 required positional argument:
               'year_of_birth'

  because

  - I called the :ref:`factory function<test person factory>` with three :ref:`keyword arguments<test_keyword_arguments>` (``first_name``, ``last_name`` and ``sex``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``factory`` has four required arguments (``first_name``, ``last_name``, ``sex`` and ``year_of_birth``).
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I add ``year_of_birth=1996`` to the call to the :ref:`factory function<test person factory>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 11

    def test_jane():
        assert jane() == 'jane, doe, F, 1991'

        # reality = factory()
        # reality = factory('jane')
        # reality = factory('jane', 'doe')
        reality = factory(
            first_name='jane',
            last_name='doe',
            sex='F',
            year_of_birth=1991,
        )
        my_expectation = 'jane, doe, F, 1991'
        assert reality == my_expectation


    def test_john():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() missing
               4 required positional arguments:
               'first_name', 'last_name', 'sex',
               and 'year_of_birth'

  because

  - I called in :ref:`test_joe` the :ref:`factory function<test person factory>` with zero arguments.
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``factory`` has four required arguments (``first_name``, ``last_name``, ``sex`` and ``year_of_birth``).
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* Since there are more than two, I add :ref:`keyword arguments<test_keyword_arguments>` to the call to the :ref:`factory function<test person factory>` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 4-10

    def test_joe():
        assert joe() == 'joe, blow, M, 1996'

        # reality = factory()
        reality = factory(
            first_name='joe',
            last_name='blow',
            sex='M',
            year_of_birth=1996,
        )
        my_expectation = 'joe, blow, M, 1996'
        assert reality == my_expectation


    def test_jane():

  the test passes and I have one :ref:`function<what is a function?>` that I can use to make any number of people.

----

* I remove the commented lines from the :ref:`factory function<test person factory>`

  .. code-block:: python
    :linenos:

    def factory(
        first_name, last_name,
        sex, year_of_birth
    ):
        return (
            f'{first_name}, {last_name},'
            f' {sex}, {year_of_birth}'
        )


    def joe():

* I comment out the call to ``joe`` in :ref:`test_joe` because I no longer need it since the :ref:`factory function<test person factory>` does the same thing

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 2

    def test_joe():
        # assert joe() == 'joe, blow, M, 1996'

        reality = factory(
            first_name='joe',
            last_name='blow',
            sex='M',
            year_of_birth=1996,
        )
        my_expectation = 'joe, blow, M, 1996'
        assert reality == my_expectation


    def test_jane():

* I add a :ref:`variable<what is a variable?>` for ``'joe'`` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3

    def test_joe():
        # assert joe() == 'joe, blow, M, 1996'
        first_name = 'joe'

        reality = factory(
            first_name='joe',
            last_name='blow',
            sex='M',
            year_of_birth=1996,
        )
        my_expectation = 'joe, blow, M, 1996'
        assert reality == my_expectation


    def test_jane():

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'joe'``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 6-7, 12-16

    def test_joe():
        # assert joe() == 'joe, blow, M, 1996'
        first_name = 'joe'

        reality = factory(
            # first_name='joe',
            first_name=first_name,
            last_name='blow',
            sex='M',
            year_of_birth=1996,
        )
        # my_expectation = 'joe, blow, M, 1996'
        my_expectation = (
            f'{first_name}, blow,'
            ' M, 1996'
        )
        assert reality == my_expectation


    def test_jane():

  the test is still green.

* I add a :ref:`variable<what is a variable?>` for ``'blow'`` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4

    def test_joe():
        # assert joe() == 'joe, blow, M, 1996'
        first_name = 'joe'
        last_name = 'blow'

        reality = factory(
            # first_name='joe',
            first_name=first_name,
            last_name='blow',
            sex='M',
            year_of_birth=1996,
        )
        # my_expectation = 'joe, blow, M, 1996'
        my_expectation = (
            f'{first_name}, blow,'
            ' M, 1996'
        )
        assert reality == my_expectation


    def test_jane():

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'blow'``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 9-10, 16-17

    def test_joe():
        # assert joe() == 'joe, blow, M, 1996'
        first_name = 'joe'
        last_name = 'blow'

        reality = factory(
            # first_name='joe',
            first_name=first_name,
            # last_name='blow',
            last_name=last_name,
            sex='M',
            year_of_birth=1996,
        )
        # my_expectation = 'joe, blow, M, 1996'
        my_expectation = (
            # f'{first_name}, blow,'
            f'{first_name}, {last_name},'
            ' M, 1996'
        )
        assert reality == my_expectation


    def test_jane():

  still green.

* I add a :ref:`variable<what is a variable?>` for ``'M'`` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 5

    def test_joe():
        # assert joe() == 'joe, blow, M, 1996'
        first_name = 'joe'
        last_name = 'blow'
        sex = 'M'

        reality = factory(
            # first_name='joe',
            first_name=first_name,
            # last_name='blow',
            last_name=last_name,
            sex='M',
            year_of_birth=1996,
        )

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'M'``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 12-13, 20-21

    def test_joe():
        # assert joe() == 'joe, blow, M, 1996'
        first_name = 'joe'
        last_name = 'blow'
        sex = 'M'

        reality = factory(
            # first_name='joe',
            first_name=first_name,
            # last_name='blow',
            last_name=last_name,
            # sex='M',
            sex=sex,
            year_of_birth=1996,
        )
        # my_expectation = 'joe, blow, M, 1996'
        my_expectation = (
            # f'{first_name}, blow,'
            f'{first_name}, {last_name},'
            # ' M, 1996'
            f' {sex}, 1996'
        )
        assert reality == my_expectation


    def test_jane():

  green.

* I add a :ref:`variable<what is a variable?>` for ``1996`` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 6

    def test_joe():
        # assert joe() == 'joe, blow, M, 1996'
        first_name = 'joe'
        last_name = 'blow'
        sex = 'M'
        year_of_birth = 1996

        reality = factory(
            # first_name='joe',
            first_name=first_name,
            # last_name='blow',
            last_name=last_name,
            # sex='M',
            sex=sex,
            year_of_birth=1996,
        )

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``1996``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 15-16, 23-24

    def test_joe():
        # assert joe() == 'joe, blow, M, 1996'
        first_name = 'joe'
        last_name = 'blow'
        sex = 'M'
        year_of_birth = 1996

        reality = factory(
            # first_name='joe',
            first_name=first_name,
            # last_name='blow',
            last_name=last_name,
            # sex='M',
            sex=sex,
            # year_of_birth=1996,
            year_of_birth=year_of_birth,
        )
        # my_expectation = 'joe, blow, M, 1996'
        my_expectation = (
            # f'{first_name}, blow,'
            f'{first_name}, {last_name},'
            # ' M, 1996'
            # f' {sex}, 1996'
            f' {sex}, {year_of_birth}'
        )
        assert reality == my_expectation


    def test_jane():

  still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 27

    def test_joe():
        first_name = 'joe'
        last_name = 'blow'
        sex = 'M'
        year_of_birth = 1996

        reality = factory(
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


    def test_jane():

----

* I comment out the call to ``jane`` in :ref:`test_jane` because I no longer need it since the :ref:`factory function<test person factory>` does the same thing

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 2

    def test_jane():
        # assert jane() == 'jane, doe, F, 1991'

        # reality = factory()

* I add a :ref:`variable<what is a variable?>` for ``'jane'`` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3

    def test_jane():
        # assert jane() == 'jane, doe, F, 1991'
        first_name = 'jane'

        # reality = factory()

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'jane'``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 9-10, 15-19

    def test_jane():
        # assert jane() == 'jane, doe, F, 1991'
        first_name = 'jane'

        # reality = factory()
        # reality = factory('jane')
        # reality = factory('jane', 'doe')
        reality = factory(
            # first_name='jane',
            first_name=first_name,
            last_name='doe',
            sex='F',
            year_of_birth=1991,
        )
        # my_expectation = 'jane, doe, F, 1991'
        my_expectation = (
            f'{first_name}, doe,'
            ' F, 1991'
        )
        assert reality == my_expectation


    def test_john():

  the test is still green.

* I add a :ref:`variable<what is a variable?>` for ``'doe'`` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4

    def test_jane():
        # assert jane() == 'jane, doe, F, 1991'
        first_name = 'jane'
        last_name = 'doe'

        # reality = factory()

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'doe'``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 12-13, 19-20

    def test_jane():
        # assert jane() == 'jane, doe, F, 1991'
        first_name = 'jane'
        last_name = 'doe'

        # reality = factory()
        # reality = factory('jane')
        # reality = factory('jane', 'doe')
        reality = factory(
            # first_name='jane',
            first_name=first_name,
            # last_name='doe',
            last_name=last_name,
            sex='F',
            year_of_birth=1991,
        )
        # my_expectation = 'jane, doe, F, 1991'
        my_expectation = (
            # f'{first_name}, doe,'
            f'{first_name}, {last_name},'
            ' F, 1991'
        )
        assert reality == my_expectation


    def test_john():

  still green.

* I add a :ref:`variable<what is a variable?>` for ``'F'`` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 5

    def test_jane():
        # assert jane() == 'jane, doe, F, 1991'
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'

        # reality = factory()

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'F'``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 15-16, 23-24

    def test_jane():
        # assert jane() == 'jane, doe, F, 1991'
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'

        # reality = factory()
        # reality = factory('jane')
        # reality = factory('jane', 'doe')
        reality = factory(
            # first_name='jane',
            first_name=first_name,
            # last_name='doe',
            last_name=last_name,
            # sex='F',
            sex=sex,
            year_of_birth=1991,
        )
        # my_expectation = 'jane, doe, F, 1991'
        my_expectation = (
            # f'{first_name}, doe,'
            f'{first_name}, {last_name},'
            # ' F, 1991'
            f' {sex}, 1991'
        )
        assert reality == my_expectation


    def test_john():

  green.

* I add a :ref:`variable<what is a variable?>` for ``1991`` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 6

    def test_jane():
        # assert jane() == 'jane, doe, F, 1991'
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = 1991

        # reality = factory()

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``1991``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 18-19, 26-27

    def test_jane():
        # assert jane() == 'jane, doe, F, 1991'
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = 1991

        # reality = factory()
        # reality = factory('jane')
        # reality = factory('jane', 'doe')
        reality = factory(
            # first_name='jane',
            first_name=first_name,
            # last_name='doe',
            last_name=last_name,
            # sex='F',
            sex=sex,
            # year_of_birth=1991,
            year_of_birth=year_of_birth,
        )
        # my_expectation = 'jane, doe, F, 1991'
        my_expectation = (
            # f'{first_name}, doe,'
            f'{first_name}, {last_name},'
            # ' F, 1991'
            # f' {sex}, 1991'
            f' {sex}, {year_of_birth}'
        )
        assert reality == my_expectation


    def test_john():

  still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 46

    def test_jane():
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = 1991

        reality = factory(
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


    def test_john():

----

* I change the call in :ref:`test_john` to a call to the :ref:`factory function<test person factory>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 2-10

    def test_john():
        # assert john() == 'john, smith, M, 1580'
        reality = factory(
            first_name='john',
            last_name='smith',
            sex='M',
            year_of_birth=1580,
        )
        my_expectation = 'jane, doe, F, 1991'
        assert reality == my_expectation


    def test_mary():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

      AssertionError: assert 'john, smith, M, 1580'
                          == 'jane, doe, F, 1991'

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 9-10

    def test_john():
        # assert john() == 'john, smith, M, 1580'
        reality = factory(
            first_name='john',
            last_name='smith',
            sex='M',
            year_of_birth=1580,
        )
        # my_expectation = 'jane, doe, F, 1991'
        my_expectation = 'john, smith, M, 1580'
        assert reality == my_expectation


    def test_mary():

  the test passes.

* I add a :ref:`variable<what is a variable?>` for ``'john'`` in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 3

    def test_john():
        # assert john() == 'john, smith, M, 1580'
        first_name = 'john'

        reality = factory(
            first_name='john',
            last_name='smith',
            sex='M',
            year_of_birth=1580,
        )
        # my_expectation = 'jane, doe, F, 1991'
        my_expectation = 'john, smith, M, 1580'
        assert reality == my_expectation


    def test_mary():

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'john'``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 6-7, 13-17

    def test_john():
        # assert john() == 'john, smith, M, 1580'
        first_name = 'john'

        reality = factory(
            # first_name='john',
            first_name=first_name,
            last_name='smith',
            sex='M',
            year_of_birth=1580,
        )
        # my_expectation = 'jane, doe, F, 1991'
        # my_expectation = 'john, smith, M, 1580'
        my_expectation = (
            f'{first_name}, smith,'
            ' M, 1580'
        )
        assert reality == my_expectation


    def test_mary():

  the test is still green.

* I add a :ref:`variable<what is a variable?>` for ``'smith'`` in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 4

    def test_john():
        # assert john() == 'john, smith, M, 1580'
        first_name = 'john'
        last_name = 'smith'

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'smith'``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 9-10, 17-18

    def test_john():
        # assert john() == 'john, smith, M, 1580'
        first_name = 'john'
        last_name = 'smith'

        reality = factory(
            # first_name='john',
            first_name=first_name,
            # last_name='smith',
            last_name=last_name,
            sex='M',
            year_of_birth=1580,
        )
        # my_expectation = 'jane, doe, F, 1991'
        # my_expectation = 'john, smith, M, 1580'
        my_expectation = (
            # f'{first_name}, smith,'
            f'{first_name}, {last_name},'
            ' M, 1580'
        )
        assert reality == my_expectation


    def test_mary():

  still green.

* I add a :ref:`variable<what is a variable?>` for ``'M'`` in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 5

    def test_john():
        # assert john() == 'john, smith, M, 1580'
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'M'``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 12-13, 21-22

    def test_john():
        # assert john() == 'john, smith, M, 1580'
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'

        reality = factory(
            # first_name='john',
            first_name=first_name,
            # last_name='smith',
            last_name=last_name,
            # sex='M',
            sex=sex,
            year_of_birth=1580,
        )
        # my_expectation = 'jane, doe, F, 1991'
        # my_expectation = 'john, smith, M, 1580'
        my_expectation = (
            # f'{first_name}, smith,'
            f'{first_name}, {last_name},'
            # ' M, 1580'
            f' {sex}, 1580'
        )
        assert reality == my_expectation


    def test_mary():

  green.

* I add a :ref:`variable<what is a variable?>` for ``1580`` in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 6

    def test_john():
        # assert john() == 'john, smith, M, 1580'
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'
        year_of_birth = 1580

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``1580``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 15-16, 24-25

    def test_john():
        # assert john() == 'john, smith, M, 1580'
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'
        year_of_birth = 1580

        reality = factory(
            # first_name='john',
            first_name=first_name,
            # last_name='smith',
            last_name=last_name,
            # sex='M',
            sex=sex,
            # year_of_birth=1580,
            year_of_birth=year_of_birth,
        )
        # my_expectation = 'jane, doe, F, 1991'
        # my_expectation = 'john, smith, M, 1580'
        my_expectation = (
            # f'{first_name}, smith,'
            f'{first_name}, {last_name},'
            # ' M, 1580'
            # f' {sex}, 1580'
            f' {sex}, {year_of_birth}'
        )
        assert reality == my_expectation


    def test_mary():

  still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 65

    def test_john():
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'
        year_of_birth = 1580

        reality = factory(
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


    def test_mary():

* I make the same change to :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 3-6, 8-17

    def test_mary():
        # assert mary() == 'mary, public, F, 2000'
        first_name = 'mary'
        last_name = 'public'
        sex = 'F'
        year_of_birth = 2000

        reality = factory(
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


    # Exceptions seen

  the test is still green.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 84

    def test_mary():
        first_name = 'mary'
        last_name = 'public'
        sex = 'F'
        year_of_birth = 2000

        reality = factory(
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


    # Exceptions seen

* I remove the ``joe``, ``jane``, ``john`` and ``mary`` :ref:`functions<what is a function?>` because they are no longer used

  .. code-block:: python
    :linenos:

    def factory(
        first_name, last_name,
        sex, year_of_birth
    ):
        return (
            f'{first_name}, {last_name},'
            f' {sex}, {year_of_birth}'
        )


    def test_joe():

  the :ref:`factory function<test person factory>` can make a string_ for any person I want when I give it the first name, last name, sex and year of birth.

* I open a new terminal_ then change directories to ``person``

  .. code-block:: python
    :emphasize-lines: 1

    cd person

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract factory function'

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I change ``reality`` for :ref:`test_joe` to be the result of a call to the :ref:`factory function<test person factory>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a call to the :ref:`factory function<test person factory>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 7-8

    def test_joe():
        first_name = 'joe'
        last_name = 'blow'
        sex = 'M'
        year_of_birth = 1996

        # reality = factory(
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


    def test_jane():

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'src' is not

  because ``src`` is not defined in ``test_person.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ at the top of ``test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.person


    def factory(
        first_name, last_name,
        sex, year_of_birth
    ):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.person' has no attribute 'factory'

  because there is nothing named ``factory`` in ``person.py`` in the ``src`` folder_.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 5
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError

* I open ``person.py`` from the ``src`` folder_
* I delete all the text in the file_ then add a copy of the :ref:`factory function<test person factory>` to ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-8

    def factory(
        first_name, last_name,
        sex, year_of_birth
    ):
        return (
            f'{first_name}, {last_name},'
            f' {sex}, {year_of_birth}'
        )

  the test passes because

  - when ``import src.person`` runs, Python_ brings in an :ref:`object<what is a class?>` for the ``person.py`` file_ from the ``src`` folder_ so I can use it in ``test_person.py`` as ``src.person``
  - when ``src.person.factory`` is called, Python_ calls the :ref:`factory function<test person factory>` from the :ref:`object<what is a class?>` it imported for the ``person.py`` file_ from the ``src`` folder_ (``src.person``)

  I think of ``src.person.factory`` like an address

  - ``factory`` is something in ``person``, in this case it is a :ref:`function<what is a function?>` in ``person``
  - ``person`` is something in ``src``, in this case it is ``person.py`` (a :ref:`module<what is a module?>`) in the ``src`` folder_
  - ``src`` is something Python_ can import (a :ref:`module<what is a module?>`, `Python package`_ or folder_)

    .. code-block:: shell

      src.person.factory
      src
      └── person.py
          └── def factory(
                  first_name, last_name,
                  sex, year_of_birth
              ):
              └── return (
                      f'{first_name}, {last_name},'
                      f' {sex}, {year_of_birth}'
                  )

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line from :ref:`test_joe` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 14

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


    def test_jane():

* I change ``reality`` for :ref:`test_jane` to be the result of a call to the :ref:`factory function<test person factory>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 7-8

    def test_jane():
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = 1991

        # reality = factory(
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


    def test_john():

  the test is still green.

* I remove the commented line from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 33

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


    def test_john():

* I change ``reality`` for :ref:`test_john` to be the result of a call to the :ref:`factory function<test person factory>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 7-8

    def test_john():
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'
        year_of_birth = 1580

        # reality = factory(
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


    def test_mary():

  still green.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 52

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


    def test_mary():

* I do the same thing to the call to the :ref:`factory function<test person factory>` in :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 7-8

    def test_mary():
        first_name = 'mary'
        last_name = 'public'
        sex = 'F'
        year_of_birth = 2000

        # reality = factory(
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


    # Exceptions seen

  green.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 71

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


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError

* I remove the :ref:`factory function<test person factory>` from ``test_person.py``

  .. code-block:: python
    :linenos:

    import src.person


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


    def test_jane():

  all the tests are still green because the calls that were made to the :ref:`factory function<test person factory>` that was in ``test_person.py`` are now to the :ref:`factory function<test person factory>` in ``person.py`` in the ``src`` folder_. When ``src.person.factory`` is called, Python_ follows this path

  .. code-block:: shell

    src.person.factory
    src
    └── person.py
        └── def factory(
                first_name, last_name,
                sex, year_of_birth
            ):
            └── return (
                    f'{first_name}, {last_name},'
                    f' {sex}, {year_of_birth}'
                )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move factory function to person.py'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can write solutions in a different module from the tests<separate and equal>`.


----

*********************************************************************************
test say_hello function
*********************************************************************************

I want the person I make to say hi. I can make a :ref:`function<what is a function?>` that takes input about a person and returns a message.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_joe` in ``test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 22-32

    import src.person


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

        reality = say_hello(
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


    def test_jane():

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'say_hello' is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function definition<how to make a function that takes input>` for it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import src.person


    def say_hello():
        return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: say_hello() got an
               unexpected keyword argument
               'first_name'

  because

  - I called the :ref:`say_hello function<test say_hello function>` with three :ref:`keyword arguments<test_keyword_arguments>` (``first_name``, ``last_name`` and ``year_of_birth``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``factory`` allows zero input, because the parentheses are empty.
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I add ``first_name`` in parentheses

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1-2

    # def say_hello():
    def say_hello(first_name):
        return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: say_hello()
               got an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

* I add ``last_name`` in parentheses

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2-3

    # def say_hello():
    # def say_hello(first_name):
    def say_hello(first_name, last_name):
        return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: say_hello()
               got an unexpected keyword argument
               'year_of_birth'

  because

  - I called the :ref:`say_hello function<test say_hello function>` with three :ref:`keyword arguments<test_keyword_arguments>` (``first_name``, ``last_name`` and ``year_of_birth``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``factory`` allows two arguments (``first_name``, ``last_name``).
  - :ref:`The call to a function must match its signature (definition)<what causes TypeError?>`.

* I add ``year_of_birth`` in parentheses

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-7

    # def say_hello():
    # def say_hello(first_name):
    # def say_hello(first_name, last_name):
    def say_hello(
        first_name, last_name,
        year_of_birth
    ):
        return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None
        == 'Hello, my name is joe blow and I am 30.'

* I change :ref:`the return statement` to give the test what it wants

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 8-9

    # def say_hello():
    # def say_hello(first_name):
    # def say_hello(first_name, last_name):
    def say_hello(
        first_name, last_name,
        year_of_birth
    ):
        # return None
        return 'Hello, my name is joe blow and I am 30.'


    def test_joe():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`say_hello function<test say_hello function>` to :ref:`test_jane` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 19-29

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

        reality = say_hello(
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


    def test_john():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'Hello, my name ... and I am 30.'
                        == 'Hello, my name ... and I am 35.'

  - because the :ref:`say_hello function<test say_hello function>` always returns ``'Hello, my name is joe blow and I am 30.'`` when it is called. It has to return a string_ based on the input it gets for me to be able to use it to make messages based on the person.
  - :ref:`I need better error messages<another way to write tests>`.

* I change :ref:`the return statement` of the :ref:`say_hello function<test say_hello function>` to an :ref:`f-string<what is string interpolation?>` to use ``first_name`` in the output

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 9-13

    # def say_hello():
    # def say_hello(first_name):
    # def say_hello(first_name, last_name):
    def say_hello(
        first_name, last_name,
        year_of_birth
    ):
        # return None
        # return 'Hello, my name is joe blow and I am 30.'
        return (
            f'Hello, my name is {first_name}'
            ' blow and I am 30.'
        )


    def test_joe():

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'Hello, my name ... and I am 30.'
                        == 'Hello, my name ... and I am 35.'

  the first names now match and :ref:`I still need better error messages<another way to write tests>`.

* I add ``last_name`` to :ref:`the return statement`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 12-13

    # def say_hello():
    # def say_hello(first_name):
    # def say_hello(first_name, last_name):
    def say_hello(
        first_name, last_name,
        year_of_birth
    ):
        # return None
        # return 'Hello, my name is joe blow and I am 30.'
        return (
            f'Hello, my name is {first_name}'
            # ' blow and I am 30.'
            f' {last_name} and I am 30.'
        )


    def test_joe():

  the terminal shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'Hello, my name ... and I am 30.'
                        == 'Hello, my name ... and I am 35.'

  the ages are different.

* I add the age calculation to :ref:`the return statement`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 10, 15-16


    # def say_hello():
    # def say_hello(first_name):
    # def say_hello(first_name, last_name):
    def say_hello(
        first_name, last_name,
        year_of_birth
    ):
        # return None
        # return 'Hello, my name is joe blow and I am 30.'
        age = 2026 - year_of_birth

        return (
            f'Hello, my name is {first_name}'
            # ' blow and I am 30.'
            # f' {last_name} and I am 30.'
            f' {last_name} and I am {age}.'
        )


    def test_joe():

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`say_hello function<test say_hello function>` to :ref:`test_john` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 19-29

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

        reality = say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            'Hello, my name is jane'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_mary():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'Hello, my name ...and I am 446.'
                        == 'Hello, my name ...and I am 446.'

  - The first names are different.
  - :ref:`I want more detail in the error messages<another way to write tests>`.

* I change ``my_expectation`` to match ``reality`` in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 7-8

        reality = say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            # 'Hello, my name is jane'
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_mary():

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`say_hello function<test say_hello function>` to :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 19-29

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

        reality = say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            ' smith and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'Hello, my name ... and I am 26.'
                        == 'Hello, my name ... and I am 26.'

  - The last names are different.
  - I want better messages that show as much of the difference in the summary.

* I change ``my_expectation`` to match ``reality`` in :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 8-9

        reality = say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            # ' smith and I am'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    # Exceptions seen

  the test passes.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 116

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

        reality = say_hello(
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


    # Exceptions seen

  the test passes because Python_ uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

  .. code-block:: python

    say_hello(
        first_name=first_name,
        last_name=last_name,
        year_of_birth=year_of_birth,
    )
        say_hello(
            first_name, last_name,
            year_of_birth,
        )
            first_name = 'mary'
            last_name = 'public'
            year_of_birth = 1991

            age = 2026 - year_of_birth
            age = 2026 - 1991
            age = 35

            return (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}.'
            )
            return f'Hello, my name is mary public and I am 35'

----

*********************************************************************************
separate and equal say_hello
*********************************************************************************

* I change ``reality`` to be the result of a call to the :ref:`say_hello function<test say_hello function>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a call to the :ref:`say_hello function<test say_hello function>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 19-20

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

        # reality = say_hello(
        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            # ' smith and I am'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.person'
                    has no attribute 'say_hello'

  because there is nothing named ``say_hello`` in the ``person.py`` file_ in the ``src`` folder_.

* I add a copy of the :ref:`say_hello function<test say_hello function>` without the commented lines to ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-20

    def factory(
        first_name, last_name,
        sex, year_of_birth
    ):
        return (
            f'{first_name}, {last_name},'
            f' {sex}, {year_of_birth}'
        )


    def say_hello(
        first_name, last_name,
        year_of_birth
    ):
        age = 2026 - year_of_birth

        return (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am {age}.'
        )

  the test passes.

* I remove the commented lines from :ref:`test_mary` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 117

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


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError

* I change ``reality`` for :ref:`test_john` to be the result of a call to the :ref:`say_hello function<test say_hello function>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 19-20

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

        # reality = say_hello(
        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            # 'Hello, my name is jane'
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation


    def test_mary():

  the test is still green.

* I remove the commented lines from :ref:`test_john`

  .. code-block:: python
    :lineno-start: 85

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


    def test_mary():

* I change ``reality`` for :ref:`test_joe` to be the result of a call to the :ref:`say_hello function<test say_hello function>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 19-20

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

        # reality = say_hello(
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


    def test_jane():

  the test is still green.

* I remove the commented line from :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 23

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


    def test_jane():

* I change ``reality`` for :ref:`test_jane` to be the result of a call to the :ref:`say_hello function<test say_hello function>` of the ``person`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 19-20

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

        # reality = say_hello(
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


    def test_john():

  the test is still green.

* I remove the commented line from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 54

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


    def test_john():

* I remove the :ref:`say_hello function<test say_hello function>` from ``test_person.py``

  .. code-block:: python
    :linenos:

    import src.person


    def test_joe():

  all the tests are still green because the calls that were made to the :ref:`say_hello function<test say_hello function>` that was in ``test_person.py`` are now to the :ref:`say_hello function<test say_hello function>` in ``person.py`` in the ``src`` folder_. When ``src.person.say_hello`` is called, Python_ follows this path

  .. code-block:: shell

    src.person.say_hello
    src
    └── person.py
        └── def say_hello(
                first_name, last_name,
                year_of_birth
            ):
            ├── age = 2026 - year_of_birth
            │
            └── return (
                    f'Hello, my name is {first_name}'
                    f' {last_name} and I am {age}.'
                )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add say_hello function'

  the terminal_ shows a summary of the changes then goes back to the command line.

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
                    has no attribute 'say_hello'

* I add the name

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    say_hello


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

    NameError: name 'say_hello' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # say_hello
    say_hello = None


    # factory

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because ``say_hello`` points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I make ``say_hello`` a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-4

    # say_hello
    # say_hello = None
    def say_hello():
        return None


    # factory

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: say_hello() got
               an unexpected keyword argument
               'first_name'

  because this :ref:`function definition<how to make a function that takes input>` does not allow any inputs, the parentheses are empty.

* I add ``first_name`` in the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # say_hello
    # say_hello = None
    # def say_hello():
    def say_hello(first_name):
        return None


    # factory

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: say_hello() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

  because the :ref:`function definition<how to make a function that takes input>` now only allows one input (``first_name``) and it was called with a :ref:`keyword argument<test_keyword_arguments>` (``last_name``).

* I add ``last_name`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    # say_hello
    # say_hello = None
    # def say_hello():
    # def say_hello(first_name):
    def say_hello(first_name, last_name):
        return None


    # factory

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: say_hello() got
               an unexpected keyword argument
               'year_of_birth'

  because the :ref:`function definition<how to make a function that takes input>` only allows two inputs (``first_name`` and ``last_name``) and it was called with a :ref:`keyword argument<test_keyword_arguments>` (``year_of_birth``).

* I add ``year_of_birth`` to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-8

    # say_hello
    # say_hello = None
    # def say_hello():
    # def say_hello(first_name):
    # def say_hello(first_name, last_name):
    def say_hello(
        first_name, last_name, year_of_birth
    ):
        return None


    # factory

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None
        == 'Hello, my name is mary public and I am 26.'

* I use :kbd:`ctrl/command+c` (Windows_ & Linux_/MacOS_) on the keyboard to copy the string_ from the terminal and :kbd:`ctrl/command+v` to paste it to replace :ref:`None<what is None?>` in :ref:`the return statement`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9-10

    # say_hello
    # say_hello = None
    # def say_hello():
    # def say_hello(first_name):
    # def say_hello(first_name, last_name):
    def say_hello(
        first_name, last_name, year_of_birth
    ):
        # return None
        return 'Hello, my name is mary public and I am 26.'


    # factory

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'mary, public, F, 2000'
                        == 'john, smith, M, 1580'

  because the :ref:`factory function<test person factory>` always returns ``'mary, public, F, 2000'`` and this test expects ``'john, smith, M, 1580'``.

* I change the :ref:`return statement<the return statement>` of the :ref:`factory function<test person factory>` to see the difference between the input and the expected output (remember :ref:`the identity function?<test_identity_function>`)

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

    AssertionError: assert 'Hello, my name ... and I am 26.'
                        == 'Hello, my name ...and I am 446.'

  because the :ref:`say_hello function<test say_hello function>` always returns ``'Hello, my name is mary public and I am 26.'`` and this test expects ``'Hello, my name is john smith and I am 446.'``

* I change the :ref:`return statement<the return statement>` of the :ref:`say_hello function<test say_hello function>` to see the difference between the input and the expected output

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11

    # say_hello
    # say_hello = None
    # def say_hello():
    # def say_hello(first_name):
    # def say_hello(first_name, last_name):
    def say_hello(
        first_name, last_name, year_of_birth
    ):
        # return None
        # return 'Hello, my name is mary public and I am 26.'
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

    # say_hello
    # say_hello = None
    # def say_hello():
    # def say_hello(first_name):
    # def say_hello(first_name, last_name):
    def say_hello(
        first_name, last_name, year_of_birth
    ):
        # return None
        # return 'Hello, my name is mary public and I am 26.'
        # return first_name, last_name, year_of_birth
        return (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am {year_of_birth}.'
        )


    # factory

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'Hello, my name ...nd I am 2000.'
                        == 'Hello, my name ... and I am 26.'

  It looks like ``26`` is the age.

* I change the ``year_of_birth`` value to a calculation of the age

  .. code-block:: python
    :linenos:
    :emphasize-lines: 14-15

    # say_hello
    # say_hello = None
    # def say_hello():
    # def say_hello(first_name):
    # def say_hello(first_name, last_name):
    def say_hello(
        first_name, last_name, year_of_birth
    ):
        # return None
        # return 'Hello, my name is mary public and I am 26.'
        # return first_name, last_name, year_of_birth
        return (
            f'Hello, my name is {first_name}'
            # f' {last_name} and I am {year_of_birth}.'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )


    # factory

  all tests are green!

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def say_hello(
        first_name, last_name, year_of_birth
    ):
        return (
            f'Hello, my name is {first_name}'
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

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'test person with f-strings'

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

    There has to be `a better way<how to make a person with a class>`, where I can give those values once, and get a representation for a person when I call the :ref:`factory function<test person factory>` and a message when I call the :ref:`say_hello function<test say_hello function>`.

For now, I am going to :ref:`clean up the functions project<separate and equal functions>` so the tests and solutions are in separate files_.

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
* :ref:`what an assertion is<what is an assertion?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`
* :ref:`how to make functions that take input<functions that take input>`
* :ref:`what causes TypeError<what causes TypeError?>`
* :ref:`how to place values in strings<telephone>`
* :ref:`how to make a person say hello with f-strings<how to make a person with f-strings>`

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