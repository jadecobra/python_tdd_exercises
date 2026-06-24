.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): how to make a person with strings. Use variables for person data (first name, last name, sex, year of birth). pytest-watcher shows "no tests ran". RED: add def test_joe(): assert joe() == 'joe, blow, M, 1996' → NameError: name 'joe' is not defined. GREEN: joe = None → TypeError: 'NoneType' object is not callable; make def joe(): return None → AssertionError: assert None == 'joe, blow, M, 1996'; fix return value. Repeat for jane, john, mary. REFACTOR: remove the commented lines, git commit -am. Ends with 4 module-level functions that return 'name, surname, X, YYYY' strings + 4 bare assert tests + # Exceptions seen list. Shows why one function per person doesn't scale. Code: person/tests/test_person_1.py. What is next: functions that take input.
  :keywords: Jacob Itegboje, Pumping Python, how to make a person with strings, python TDD variables, NameError: name 'joe' is not defined, TypeError: 'NoneType' object is not callable, AssertionError: assert None == 'joe, blow, M, 1996', bare assert, pytest-watcher "no tests ran", remove the commented lines, def joe(): return 'joe, blow, M, 1996', functions that return strings, red green refactor, repetition in tests, test_joe test_jane test_john test_mary, person attributes as variables, what is next functions that take input

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

    .../pumping_python/person

* I open ``test_person.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows ``no tests ran``.

----

*********************************************************************************
test_person_factory_w_inputs
*********************************************************************************

----

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

* I add an :ref:`assertion<what is an assertion?>` with a call to the ``factory`` :ref:`function<what is a function?>` in :ref:`test_jane`

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

  because the ``factory`` :ref:`function<what is a function?>` always returns ``joe, blow, M, 1996`` when it is called. It has to return a string_ based on the input it gets for me to be able to use it to make more than one person.

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

  - I called the ``factory`` :ref:`function<what is a function?>` with zero inputs.
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``factory`` has one required argument (``first_name``).
  - I am violating the :ref:`function signature<how to make a function that takes input>` when I call it in a way that it was not designed to be called, which raises :ref:`TypeError<what causes TypeError?>`.

* I add ``'jane'`` to the call to the ``factory`` :ref:`function<what is a function?>` in :ref:`test_jane`

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

* I change :ref:`the return statement` of the ``factory`` :ref:`function<what is a function?>` to an :ref:`f-string<what is string interpolation?>` to use ``first_name`` in the output

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

* I add the name to the parentheses to define it in the ``factory`` :ref:`function<what is a function?>`

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

  - I called the ``factory`` :ref:`function<what is a function?>` with one input (``jane``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``factory`` has two required arguments (``first_name`` and ``last_name``).
  - I am violating the :ref:`function signature<how to make a function that takes input>` when I call it in a way that it was not designed to be called, which raises :ref:`TypeError<what causes TypeError?>`.

* I add ``'doe'`` to the call to the ``factory`` :ref:`function<what is a function?>` in :ref:`test_jane`

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

* I use :ref:`keyword arguments<test_keyword_arguments>` with a value for ``sex`` (since I have more than two) to change the call to the ``factory`` :ref:`function<what is a function?>` in :ref:`test_jane`

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

  - I called the ``factory`` :ref:`function<what is a function?>` with three :ref:`keyword arguments<test_keyword_arguments>` input (``first_name``, ``last_name`` and ``sex``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``factory`` has two required arguments (``first_name`` and ``last_name``).
  - I am violating the :ref:`function signature<how to make a function that takes input>` when I call it in a way that it was not designed to be called, which raises :ref:`TypeError<what causes TypeError?>`.

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

* I add ``sex`` to the :ref:`f-string<what is string interpolation?>` in the ``factory`` :ref:`function<what is a function?>`

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

* I add ``year_of_birth`` to the parentheses to define it in the ``factory`` :ref:`function<what is a function?>`

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

  - I called the ``factory`` :ref:`function<what is a function?>` with three :ref:`keyword arguments<test_keyword_arguments>` (``first_name``, ``last_name`` and ``sex``).
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``factory`` has four required arguments (``first_name``, ``last_name``, ``sex`` and ``year_of_birth``).
  - I am violating the :ref:`function signature<how to make a function that takes input>` when I call it in a way that it was not designed to be called, which raises :ref:`TypeError<what causes TypeError?>`.

* I add ``year_of_birth=1996`` to the call to the ``factory`` :ref:`function<what is a function?>` in :ref:`test_jane`

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

  - I called in :ref:`test_joe` the ``factory`` :ref:`function<what is a function?>` with zero arguments.
  - The :ref:`function definition (signature)<how to make a function that takes input>` of ``factory`` has four required arguments (``first_name``, ``last_name``, ``sex`` and ``year_of_birth``).
  - I am violating the :ref:`function signature<how to make a function that takes input>` when I call it in a way that it was not designed to be called, which raises :ref:`TypeError<what causes TypeError?>`.

* Since there are more than two, I add :ref:`keyword arguments<test_keyword_arguments>` to the call to the ``factory`` :ref:`function<what is a function?>` in :ref:`test_joe`

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

* I remove the commented lines from the ``factory`` :ref:`function<what is a function?>`

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

* I comment out the call to ``joe`` in :ref:`test_joe` because I no longer need it since the ``factory`` :ref:`function<what is a function?>` does the same thing

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

* I add a :ref:`variable<what is a variable?>` for ``'joe'`` to :ref:`test_joe`

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

* I add a :ref:`variable<what is a variable?>` for ``'blow'`` to :ref:`test_joe`

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

* I add a :ref:`variable<what is a variable?>` for ``'M'`` to :ref:`test_joe`

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

* I add a :ref:`variable<what is a variable?>` for ``1996`` to :ref:`test_joe`

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

* I comment out the call to ``jane`` in :ref:`test_jane` because I no longer need it since the ``factory`` :ref:`function<what is a function?>` does the same thing

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 2

    def test_jane():
        # assert jane() == 'jane, doe, F, 1991'

        # reality = factory()

* I add a :ref:`variable<what is a variable?>` for ``'jane'`` to :ref:`test_jane`

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

* I add a :ref:`variable<what is a variable?>` for ``'doe'`` to :ref:`test_jane`

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

* I add a :ref:`variable<what is a variable?>` for ``'F'`` to :ref:`test_jane`

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

* I add a :ref:`variable<what is a variable?>` for ``1991`` to :ref:`test_jane`

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
BOOM
----
----
BOOM
----
----
BOOM
----

* I remove the :ref:`assertion<what is an assertion?>` and comments then add a new test :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    # Exceptions seen
    # AssertionError

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'joe' is not defined

  because there is no definition for ``joe`` in ``test_person.py``.

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError


* I add a :ref:`variable<what is a variable?>` for ``joe`` and point it to :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    joe = None


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``joe`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    joe = None # point the name to the object
    joe()      # call the name
    None()     # substitute the value for the name

  ``None()`` raises :ref:`TypeError<what causes TypeError?>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError

* I change ``joe`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-3

    # joe = None
    def joe():
        return None


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == 'joe, blow, M, 1996'

  because when I call ``joe`` it returns :ref:`None<what is None?>`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assert joe() == 'joe, blow, M, 1996'
    assert None  == 'joe, blow, M, 1996'

  which raises :ref:`AssertionError<what causes AssertionError?>` because :ref:`None is only equal to None<what is None?>`.

* I change :ref:`the return statement` of ``joe``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # joe = None
    def joe():
        # return None
        return 'joe, blow, M, 1996'


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    # Exceptions seen

  the test passes.



* I remove the commented lines

  .. code-block:: python
    :linenos:

    def joe():
        return 'joe, blow, M, 1996'


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_joe'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test_jane
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test :ref:`function<what is a function?>`

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 5-6

  def test_joe():
      assert joe() == 'joe, blow, M, 1996'


  def test_jane():
      assert jane() == 'jane, doe, F, 1991'



  # Exceptions seen

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'jane' is not defined

because there is no definition for ``jane`` in this file_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``jane`` and point it to :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def joe():
        return 'joe, blow, M, 1996'


    jane = None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``jane`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    jane = None # point the name to the object
    jane()      # call the name
    None()      # substitute the value for the name

  ``None()`` raises :ref:`TypeError<what causes TypeError?>`.

* I change ``jane`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-7

    def joe():
        return 'joe, blow, M, 1996'


    # jane = None
    def jane():
        return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == 'jane, doe, F, 1991'

  because when I call ``jane`` it returns :ref:`None<what is None?>`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assert jane() == 'jane, doe, F, 1991'
    assert None   == 'jane, doe, F, 1991'

  which raises :ref:`AssertionError<what causes AssertionError?>` because :ref:`None is only equal to None<what is None?>`.

* I change :ref:`the return statement` of ``jane``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    def joe():
        return 'joe, blow, M, 1996'


    # jane = None
    def jane():
        # return None
        return 'jane, doe, F, 1991'


    def test_joe():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def joe():
        return 'joe, blow, M, 1996'


    def jane():
        return 'jane, doe, F, 1991'


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    def test_jane():
        assert jane() == 'jane, doe, F, 1991'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_jane'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test_john
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another test :ref:`function<what is a function?>`

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 5-6

  def test_jane():
      assert jane() == 'jane, doe, F, 1991'


  def test_john():
      assert john() == 'john, smith, M, 1580'



  # Exceptions seen

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'john' is not defined

because there is no definition for ``john`` in this file_, yet.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``john`` and point it to :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5

    def jane():
        return 'jane, doe, F, 1991'


    john = None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``john`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    john = None # point the name to the object
    john()      # call the name
    None()      # substitute the value for the name

  ``None()`` raises :ref:`TypeError<what causes TypeError?>`.

* I change ``john`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-7

    def joe():
        return 'joe, blow, M, 1996'


    # john = None
    def john():
        return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == 'john, smith, M, 1580'

  because when I call ``john`` it returns :ref:`None<what is None?>`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assert john() == 'john, smith, M, 1580'
    assert None   == 'john, smith, M, 1580'

  which raises :ref:`AssertionError<what causes AssertionError?>` because :ref:`None is only equal to None<what is None?>`.

* I change :ref:`the return statement` of ``john``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 7-8

    def jane():
        return 'jane, doe, F, 1991'


    # john = None
    def john():
        # return None
        return 'john, smith, M, 1580'


    def test_joe():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def joe():
        return 'joe, blow, M, 1996'


    def jane():
        return 'jane, doe, F, 1991'


    def john():
        return 'john, smith, M, 1580'


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    def test_jane():
        assert jane() == 'jane, doe, F, 1991'


    def test_john():
        assert john() == 'john, smith, M, 1580'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_john'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test_mary
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another test :ref:`function<what is a function?>`

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 5-6

  def test_john():
      assert john() == 'john, smith, M, 1580'


  def test_mary():
      assert mary() == 'mary, public, F, 2000'


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'mary' is not defined

because there is no definition for ``mary``, it is just a name.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``mary`` and point it to :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5

    def john():
        return 'john, smith, M, 1580'


    mary = None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``mary`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    mary = None # point the name to the object
    mary()      # call the name
    None()      # substitute the value for the name

  ``None()`` raises :ref:`TypeError<what causes TypeError?>`.

* I change ``mary`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-7

    def john():
        return 'john, smith, M, 1580'


    # mary = None
    def mary():
        return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == 'mary, public, F, 2000'

  because when I call ``mary`` it returns :ref:`None<what is None?>`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assert mary() == 'mary, public, F, 2000'
    assert None   == 'mary, public, F, 2000'

  which raises :ref:`AssertionError<what causes AssertionError?>` because :ref:`None is only equal to None<what is None?>`.

* I change :ref:`the return statement` of ``mary``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 7-8

    def john():
        return 'john, smith, M, 1580'


    # mary = None
    def mary():
        # return None
        return 'mary, public, F, 2000'


    def test_joe():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def joe():
        return 'joe, blow, M, 1996'


    def jane():
        return 'jane, doe, F, 1991'


    def john():
        return 'john, smith, M, 1580'


    def mary():
        return 'mary, public, F, 2000'


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    def test_jane():
        assert jane() == 'jane, doe, F, 1991'


    def test_john():
        assert john() == 'john, smith, M, 1580'


    def test_mary():
        assert mary() == 'mary, public, F, 2000'


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_mary'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_person.py``
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

I ran tests to make :ref:`functions<what is a function?>` that return strings_ with information for people. There are a few problems with what I have so far

- I made a :ref:`function<what is a function?>` for each person. What happens if I have to make 10 or 100 or 1000 people? I am not ready to make 1000 :ref:`functions<what is a function?>`.
- Each test is basically a repetition of the information for each person.

I want something that will take in information for a person and return a representation for the person. That way I can use one thing to make as many people as I want. I can do that with :ref:`functions that take input<what is a function?>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a person: tests and solution>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know:

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what causes AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`

:ref:`Would you like to test functions with input?<functions that take input>`

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