.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

#################################################################################
how to make a person with exceptions
#################################################################################

----

I had a problem when I :ref:`made a person with conditions<how to make a person with conditions>`

* I skipped :ref:`test_when_year_of_birth_is_not_an_integer` because it is always in a :red:`RED` state since it causes an :ref:`Exception<errors>`.
* I commented out the bad ``year_of_birth`` in :ref:`test_john` for when a person is too old because it causes an :ref:`Exception<error>`.

Python_ has a way that allows programs to make a choice when they encounter an :ref:`Exception<errors>` and continue running without stopping. It is the :ref:`try statement<how to use try...except...else>`.

I want to use the :ref:`try statement<how to use try...except...else>` to handle making sure the program raises an :ref:`Exception<errors>`

* if the age is older than ``120``
* if the ``year_of_birth`` is not an integer_

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_exceptions.py
  :language: python
  :linenos:
  :caption: person/tests/test_person.py
  :lines: 1-13

.. literalinclude:: ../../code/person/tests/test_person_w_exceptions.py
  :language: python
  :lineno-start: 15
  :caption: person/tests/test_person.py
  :lines: 15-58

.. literalinclude:: ../../code/person/tests/test_person_w_exceptions.py
  :language: python
  :lineno-start: 60
  :caption: person/tests/test_person.py
  :lines: 60-104

.. literalinclude:: ../../code/person/tests/test_person_w_exceptions.py
  :language: python
  :lineno-start: 106
  :caption: person/tests/test_person.py
  :lines: 106-162

.. literalinclude:: ../../code/person/tests/test_person_w_exceptions.py
  :language: python
  :lineno-start: 164
  :caption: person/tests/test_person.py
  :lines: 164-209

.. literalinclude:: ../../code/person/tests/test_person_w_exceptions.py
  :language: python
  :lineno-start: 211
  :caption: person/tests/test_person.py
  :lines: 211-240

.. literalinclude:: ../../code/person/tests/test_person_w_exceptions.py
  :language: python
  :lineno-start: 242
  :caption: person/tests/test_person.py
  :lines: 242-280

.. literalinclude:: ../../code/person/tests/test_person_w_exceptions.py
  :language: python
  :lineno-start: 282
  :caption: person/tests/test_person.py
  :lines: 282-


-----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd person

* I open ``test_person.py`` from the ``tests`` folder_

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    tests/test_person.py .......                    [100%]

    ============ 7 passed, 1 skipped in T.UVs ============

----

*********************************************************************************
test_when_person_is_too_old_to_be_alive
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I open ``tests/test_person.py``
* I add :ref:`test_when_person_is_too_old_to_be_alive` for if the age of the person is greater than ``120``, in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 202
    :emphasize-lines: 15-21

        def test_underage_citizen(self):
            person = src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=datetime.date.today().year-17,
                is_citizen=True,
                passed_test=True,
            )
            self.assertEqual(person.can_vote(), False)
            self.assertEqual(
                person.can_get_license(), False
            )

        def test_when_person_is_too_old_to_be_alive(self):
            person = src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='F',
                year_of_birth=datetime.date.today().year-121,
            )

        @unittest.skip('will always fail')
        def test_when_year_of_birth_is_not_an_integer(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    E       AssertionError

  I use a calculation (``datetime.date.today().year121``) as the year of birth so that it will always be ``121`` years ago.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``src/person/__init__.py``

* I change the :ref:`assert statement<what is an assertion?>` in the :ref:`calculate_age function<extract calculate_age function>` for if the age is less than or equal to ``120`` to :ref:`raise an Exception<how to raise an Exception>` if the age is greater than ``120``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 7-9

    def calculate_age(year_of_birth):
        assert isinstance(year_of_birth, int)
        age = (
            datetime.date.today().year
          - year_of_birth
        )
        # assert age <= 120
        if age > 120:
            raise Exception
        return age


    def say_hello(
        first_name, last_name, year_of_birth,
    ):

  the terminal_ is my friend, and shows :ref:`Exception<errors>`

  .. code-block:: shell

    E           Exception

* I add a :ref:`try statement<how to use try...except...else>` to :ref:`test_when_person_is_too_old_to_be_alive` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 216
    :emphasize-lines: 2-10

        def test_when_person_is_too_old_to_be_alive(self):
            try:
                person = src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='F',
                    year_of_birth=datetime.date.today().year-121,
                )
            except:
                pass

        @unittest.skip('will always fail')
        def test_when_year_of_birth_is_not_an_integer(self):

  the test passes, confirming that when the value for ``year_of_birth`` makes the person older than ``120`` an :ref:`Exception<errors>` is raised.

  - The :ref:`try statement<how to use try...except...else>` is like an :ref:`if statement<if statements>` for :ref:`Exceptions<errors>`. It tells the program_ what to do if an :ref:`Exception<errors>` is raised. A simple way to think of it is

    - ``try`` **something**
    - ``except`` - if **something** raises an :ref:`Exception<errors>` do something else

  - pass_ is a special keyword that allows the :ref:`try statement<how to use try...except...else>` to follow Python_ language rules (the :ref:`except block<how to use try...except...else>` must have a body).

* I add a git_ commit message

  .. code-block:: python

    git commit -am \
    'add test_when_person_is_too_old_to_be_alive'

----

*********************************************************************************
add exception handler to test_when_year_of_birth_is_not_an_integer
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I remove the :ref:`unittest.skip decorator<how to skip a test>` from :ref:`test_when_year_of_birth_is_not_an_integer` and remove the comment from ``year_of_birth=None`` to test when ``year_of_birth`` is :ref:`None`, in ``tests/test_person.py``

.. code-block:: python
  :lineno-start: 224
  :emphasize-lines: 5, 9, 11-14

          except:
              pass

      def test_when_year_of_birth_is_not_an_integer(self):
          src.person.Person(
              first_name='first_name',
              last_name='last_name',
              sex='M',
              year_of_birth=None,
          )
          # year_of_birth=False,   # fails
          # year_of_birth=2026.0,  # fails
          # year_of_birth='2026',  # fails
          # year_of_birth=(2026,), # fails
          # person.say_hello()
          # fails if year_of_birth is not an integer

      def test_dir_person_class(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  E       AssertionError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``assert isinstance(year_of_birth, int)`` to an :ref:`if statement<if statements>` that :ref:`raises an Exception<how to raise an Exception>` when ``year_of_birth`` is not an :ref:`integer` in the :ref:`calculate_age function<extract calculate_age function>` in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2-4

    def calculate_age(year_of_birth):
        # assert isinstance(year_of_birth, int)
        if not isinstance(year_of_birth, int):
            raise Exception

        age = (
            datetime.date.today().year
          - year_of_birth
        )
        # assert age <= 120
        if age > 120:
            raise Exception
        return age


    def say_hello(
        first_name, last_name, year_of_birth,
    ):

  the terminal_ is my friend, and shows :ref:`Exception<errors>`

  .. code-block:: python

    E           Exception

* I add a :ref:`try statement<how to use try...except...else>` to :ref:`test_when_year_of_birth_is_not_an_integer` in ``tests/test_person.py``

  .. code-block:: python
    :lineno-start: 227
    :emphasize-lines: 2-10

        def test_when_year_of_birth_is_not_an_integer(self):
            try:
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth=None,
                )
            except:
                pass
            # year_of_birth=False,   # fails
            # year_of_birth=2026.0,  # fails
            # year_of_birth='2026',  # fails
            # year_of_birth=(2026,), # fails
            # person.say_hello()
            # fails if year_of_birth is not an integer

        def test_dir_person_class(self):

  the test passes, showing that :ref:`Exception<errors>` is raised when ``year_of_birth`` is not an integer_.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I make a person with :ref:`False<test_what_is_false>` as the value for ``year_of_birth``

  .. code-block:: python
    :lineno-start: 235
    :emphasize-lines: 4-9

            except:
                pass

            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=False,
            )

            # year_of_birth=2026.0,  # fails
            # year_of_birth='2026',  # fails
            # year_of_birth=(2026,), # fails
            # person.say_hello()
            # fails if year_of_birth is not an integer

        def test_dir_person_class(self):

  the terminal_ is my friend, and shows :ref:`Exception<errors>`

* I add a :ref:`try statement<how to use try...except...else>` for when the ``year_of_birth`` is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 235
    :emphasize-lines: 4-12

            except:
                pass

            try:
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth=False,
                )
            except:
                pass

            # year_of_birth=2026.0,  # fails

  the test passes, showing that :ref:`Exception<errors>` is raised when ``year_of_birth`` is not an integer_.

* I make a person with a float_ as the value for ``year_of_birth``

  .. code-block:: python
    :lineno-start: 245
    :emphasize-lines: 4-9

            except:
                pass

            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=2026.0,
            )

            # year_of_birth='2026',  # fails
            # year_of_birth=(2026,), # fails
            # person.say_hello()
            # fails if year_of_birth is not an integer

        def test_dir_person_class(self):

  the terminal_ is my friend, and shows :ref:`Exception<errors>`

* I add a :ref:`try statement<how to use try...except...else>` for when the ``year_of_birth`` is a float_

  .. code-block:: python
    :lineno-start: 245
    :emphasize-lines: 4-12

            except:
                pass

            try:
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth=2026.0,
                )
            except:
                pass

            # year_of_birth='2026',  # fails

  the test passes, showing that :ref:`Exception<errors>` is raised when ``year_of_birth`` is not an integer_.

* I make a person with a string_ as the value for ``year_of_birth``

  .. code-block:: python
    :lineno-start: 255
    :emphasize-lines: 4-9

            except:
                pass

            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth='2026',
            )

            # year_of_birth=(2026,), # fails
            # person.say_hello()
            # fails if year_of_birth is not an integer

        def test_dir_person_class(self):

  the terminal_ is my friend, and shows :ref:`Exception<errors>`

* I add a :ref:`try statement<how to use try...except...else>` for when the ``year_of_birth`` is a string_

  .. code-block:: python
    :lineno-start: 255
    :emphasize-lines: 4-12

            except:
                pass

            try:
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth='2026',
                )
            except:
                pass

            # year_of_birth=(2026,), # fails

  the test passes, showing that :ref:`Exception<errors>` is raised when ``year_of_birth`` is not an integer_.

* I make a person with a tuple_ as the value for ``year_of_birth``

  .. code-block:: python
    :lineno-start: 265
    :emphasize-lines: 4-9

            except:
                pass

            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=(2026,),
            )

            # person.say_hello()

  the terminal_ is my friend, and shows :ref:`Exception<errors>`

* I add a :ref:`try statement<how to use try...except...else>` for when the ``year_of_birth`` is a tuple_, and remove the other comments since I no longer need them

  .. code-block:: python
    :lineno-start: 265
    :emphasize-lines: 4-12

            except:
                pass

            try:
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth=(2026,),
                )
            except:
                pass

        def test_dir_person_class(self):

  the test passes, showing that :ref:`Exception<errors>` is raised when ``year_of_birth`` is not an integer_.

* I remove the commented lines from the :ref:`calculate_age function<extract calculate_age function>`  in ``src/person/__init__.py``

  .. code-block:: python
    :lineno-start: 44

    def calculate_age(year_of_birth):
        if not isinstance(year_of_birth, int):
            raise Exception

        age = (
            datetime.date.today().year
          - year_of_birth
        )

        if age > 120:
            raise Exception
        return age


    def say_hello(
        first_name, last_name, year_of_birth,
    ):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add exception handler to test_when_year_of_birth_is_not_an_integer'

----

*********************************************************************************
explicit is better than implicit
*********************************************************************************

The problem with using :ref:`except:<how to use try...except...else>` is that it catches all :ref:`Exceptions<errors>` which means it does not tell anyone that reads the code what the actual :ref:`Exception<errors>` is.

.. code-block:: python

  try:
      something
  except:
      something else

is the same as

.. code-block:: python

  try:
      something
  except Exception:
      something else

because :ref:`Exception<errors>` is the mother of all the :ref:`Exceptions<errors>` covered so far, they :ref:`inherit<everything is an object>` from it.

From the :PEP:`Zen of Python <20>`: ``Explicit is better than implicit``.

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the :ref:`except clause<how to use try...except...else>` in :ref:`test_when_person_is_too_old_to_be_alive` for when the ``year_of_birth`` is a tuple_ to be more specific

.. code-block:: python
  :lineno-start: 268
  :emphasize-lines: 8

          try:
              src.person.Person(
                  first_name='first_name',
                  last_name='last_name',
                  sex='M',
                  year_of_birth=(2026,),
              )
          except TypeError:
              pass

      def test_dir_person_class(self):

the terminal_ is my friend, and shows :ref:`Exception<errors>`

.. code-block:: python

  E           Exception

because :ref:`Exception<errors>` is not :ref:`TypeError<what causes TypeError?>` even though :ref:`TypeError<what causes TypeError?>` is an :ref:`Exception<errors>`. I cannot use a :ref:`child<how to test if something is a subclass>` :ref:`Exceptions<errors>` to catch its parent :ref:`Exception<errors>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`raise statement<how to raise an Exception>` in the :ref:`calculate_age function<extract calculate_age function>` for when the ``year_of_birth`` is not an integer_ to be more specific

.. code-block:: python
  :lineno-start: 44
  :emphasize-lines: 3-4

  def calculate_age(year_of_birth):
      if not isinstance(year_of_birth, int):
          # raise Exception
          raise TypeError

      age = (
          datetime.date.today().year
        - year_of_birth
      )

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`except clause<how to use try...except...else>` in :ref:`test_when_person_is_too_old_to_be_alive` for when the ``year_of_birth`` is a string_ to catch :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :lineno-start: 258
    :emphasize-lines: 8

            try:
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth='2026',
                )
            except AssertionError:
                pass

            try:

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    E           TypeError

* I change the :ref:`except clause<how to use try...except...else>` in :ref:`test_when_person_is_too_old_to_be_alive` for when the ``year_of_birth`` is a string_ to catch :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :lineno-start: 258
    :emphasize-lines: 8

            try:
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth='2026',
                )
            except TypeError:
                pass

            try:

  the test passes.

* I change the :ref:`except clause<how to use try...except...else>` in :ref:`test_when_person_is_too_old_to_be_alive` for when the ``year_of_birth`` is a string_ to catch :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python
    :lineno-start: 258
    :emphasize-lines: 8

            try:
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth='2026',
                )
            except NameError:
                pass

            try:

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    E           TypeError

* I change the :ref:`except clause<how to use try...except...else>` in :ref:`test_when_person_is_too_old_to_be_alive` for when the ``year_of_birth`` is a string_ to catch :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :lineno-start: 258
    :emphasize-lines: 8

            try:
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth='2026',
                )
            except TypeError:
                pass

            try:

  the test passes.

# NameError
# TypeError
# AttributeError
# SyntaxError

* I change the :ref:`except clause<how to use try...except...else>` in :ref:`test_when_person_is_too_old_to_be_alive` for when the ``year_of_birth`` is a string_ to be more specific

  .. code-block:: python
    :lineno-start: 258
    :emphasize-lines: 8

            try:
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth='2026',
                )
            except TypeError:
                pass

            try:

  the test is still green.




----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_person.py`` and ``src/person/__init__.py``
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

I can use :ref:`if statements<if statements>` to write a program_ that makes decisions based on :ref:`conditions<if statements>`.

My tests have problems:

* The attribute tests - :ref:`test_dir_person_class` and :ref:`test_dir_person_instance` catch changes to the :ref:`attributes and methods of the Person class<test_dir_person_instance>` and they are a problem to maintain. There has to be a better way.
* I skipped :ref:`test_when_year_of_birth_is_not_an_integer` because it is always in a :red:`RED` state since it causes an :ref:`Exception<errors>`. The only way to know that the code causes the :ref:`Exception<errors>` is to remove the `unittest.skip decorator`_. :ref:`There has to be a better way<how to test that an Exception is raised>`
* :ref:`test_joe`, :ref:`test_jane`, :ref:`test_john` and :ref:`test_mary` also still have the problem where they are the same three tests. There has to be a better way.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a person with conditions: tests and solutions>`

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
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`.
* :ref:`I know how to write programs that make decisions<truth table>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically with variables<how to make a Python Test Driven Development environment automatically with variables>`.

.. toctree::
  :titlesonly:
  :maxdepth: 1

  ../../exceptions/exception_handling/exception_handling_tests
  ../../exceptions/exception_handling/exception_handling_programs

:ref:`Would you like to test handling Exceptions in tests?<how to make a person with exceptions>`
:ref:`Would you like to test booleans (there are only two)?<what are booleans?>`

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