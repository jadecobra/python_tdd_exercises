.. meta::
  :description: A step-by-step Python Test-Driven Development (TDD) tutorial for beginners building a person dictionary factory function. Learn modern project setup with uv init and git; automate testing with pytest-watcher and unittest; and systematically resolve AssertionError, NameError, AttributeError, TypeError, and SyntaxError. Covers advanced refactoring using datetime.datetime.now(), random.choice, random.randint, starred parameter lists (*args), and double-star (**) dictionary unpacking.
  :keywords: Jacob Itegboje, Python TDD tutorial for beginners, step by step python test driven development, how to use uv python package manager, pytest-watcher automatic test runner, unittest assertEqual AssertionError, datetime.datetime.now year calculation, how to use random.choice in tests, random.randint test parameters, python unexpected keyword argument TypeError, python parameters without default values order, python double star dictionary unpacking, red green refactor example, catching NameError and AttributeError in python tests, how to fix TypeError: 'NoneType' object is not callable, why does my test show NameError: name 'src' is not defined, python SyntaxError: parameter without a default follows parameter with a default, testing python factory function returning dict, starred expressions

.. include:: ../links.rst

.. _random.choice: https://docs.python.org/3/library/random.html#random.choice
.. _choice method: `random.choice`_
.. _random.choice method: `random.choice`_

#################################################################################
how to make a person
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/MAzF1fF-mwg?si=4mUekNwDAFGboUlM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

This is an exercise in making :ref:`dictionaries<what is a dictionary?>` with :ref:`functions<what is a function?>`, two important :ref:`objects<everything is an object>` to know in Python_.

I want to make a contact list or database of people. I can use a :ref:`function<what is a function?>` to represent filling out information for a person, for example

* First Name
* Last Name (Surname)
* Sex
* Year of Birth

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/person/tests/test_person.py
  :language: python
  :linenos:

-----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``person``
* I open a terminal_
* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init person

  the terminal_ shows

  .. code-block:: shell

    Initialized project `person` at `.../pumping_python/person`

  then goes back to the command line.

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd person

  the terminal_ shows I am in the ``person`` folder_

  .. code-block:: shell

    .../pumping_python/person

* I use mkdir_ to make a folder_ named ``src``

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line.

* I use the `mv program`_ to change the name of ``main.py`` to ``person.py`` and move it to the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        mv main.py src/person.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        Move-Item main.py src/person.py

  the terminal_ goes back to the command line.

* I `make a directory`_ for the tests

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line.

* I make the ``tests`` directory_ a `Python package`_

  .. danger:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/__init__.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/__init__.py

  the terminal_ goes back to the command line.

* I make a :ref:`Python file<what is a module?>` for the tests in the ``tests`` directory_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/test_person.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/test_person.py

  the terminal_ goes back to the command line.

* I open ``test_person.py``

* I add :ref:`the first failing test<test_failure>` to ``test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestPerson(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I go back to the terminal_ to make a requirements file_ for the `Python packages`_ I need

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

  the terminal_ goes back to the command line.

* I add `pytest-watcher`_ to the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

  the terminal_ goes back to the command line.

* I use uv_ to install `pytest-watcher`_ with the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal_ shows that it installed `pytest-watcher`_ and its dependencies.

* I add the new files_ and folders_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

  the terminal_ goes back to the command line.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'setup project'

  the terminal_ shows

  .. code-block:: python

    [main (root-commit) a0b12c3] setup project
     9 files changed, 145 insertions(+)
     create mode 100644 .gitignore
     create mode 100644 .python-version
     create mode 100644 README.md
     create mode 100644 pyproject.toml
     create mode 100644 requirements.txt
     create mode 100644 src/person.py
     create mode 100644 tests/__init__.py
     create mode 100644 tests/test_person.py
     create mode 100644 uv.lock

  then goes back to the command line.

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 8, 10

    ======================== FAILURES ========================
    ______________________ TestPerson.test_failure ________________________

    self = <tests.test_person.TestPerson testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_person.py:7: AssertionError
    ================ short test summary info =================
    FAILED tests/test_person.py::TestPerson::test_failure - AssertionError: True is not false
    =================== 1 failed in X.YZs ====================

  because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`.

  .. admonition:: if the terminal_ does not show the same error, then check if

    * your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    and try ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestPerson(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes.

----

*********************************************************************************
test_factory_w_keyword_arguments
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change :ref:`test_failure` to :ref:`test_factory_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-6

    class TestPerson(unittest.TestCase):

        def test_factory_w_keyword_arguments(self):
            reality = src.person.factory()
            my_expectation = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen
    # AssertionError

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'src' is not defined

  because there is no definition for ``src`` in ``test_person.py``

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ for the ``person`` :ref:`module<what is a module?>` at the top of ``test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.person
    import unittest

  - ``import src.person`` brings in an :ref:`object (everything in Python is an object)<everything is an object>` for the ``person.py`` :ref:`module<what is a module?>` from the ``src`` folder_ so I can use it in ``test_person.py``
  - the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

    .. code-block:: python

      AttributeError: module 'src.person'
                      has no attribute 'factory'

    because there is nothing in ``person.py`` named ``factory``

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``person.py`` from the ``src`` folder

* I delete all the text in the file_, then add a :ref:`function<what is a function?>` to ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def factory():
        return None

  the test passes because when ``src.person.factory()`` is called, Python_ checks ``person.py`` in the ``src`` folder_ for a :ref:`function definition<how to make a function>` with the name ``factory`` and finds it.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I want the :ref:`function<what is a function?>` to take an argument called ``first_name``. I add it to the call from the test in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2-5

        def test_factory_w_keyword_arguments(self):
            # reality = src.person.factory()
            reality = src.person.factory(
                first_name='first_name',
            )
            my_expectation = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() got
               an unexpected keyword argument 'first_name'

  because the :ref:`function definition<how to make a function>` for ``factory`` in ``person.py`` in the ``src`` folder_, does not allow calling it with inputs (the parentheses are empty) and the test sends ``'first_name'`` as input.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add ``first_name`` as an input parameter to the :ref:`function<what is a function?>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # def factory():
    def factory(first_name):
        return None

  the test passes.

-----

* I want the :ref:`function<what is a function?>` to take an argument called ``last_name``. I add it to the test in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_factory_w_keyword_arguments(self):
            # reality = src.person.factory()
            reality = src.person.factory(
                first_name='first_name',
                last_name='last_name',
            )
            my_expectation = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: factory() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

  because the test called the :ref:`factory function<test_factory_w_keyword_arguments>` with a :ref:`keyword argument<test_keyword_arguments>` (``last_name``) that is not in the :ref:`function definition<how to make a function>`.

* I add ``last_name`` to the :ref:`function definition<how to make a function>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    # def factory():
    # def factory(first_name):
    def factory(first_name, last_name):
        return None

  the test passes.

----

* I want the :ref:`function<what is a function?>` to take an argument called ``sex``. I add it to the test in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6

        def test_factory_w_keyword_arguments(self):
            # reality = src.person.factory()
            reality = src.person.factory(
                first_name='first_name',
                last_name='last_name',
                sex='M',
            )
            my_expectation = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() got
               an unexpected keyword argument 'sex'

  because the test called the :ref:`factory function<test_factory_w_keyword_arguments>` with a :ref:`keyword argument<test_keyword_arguments>` (``sex``) that is not in the :ref:`function definition<how to make a function>`.

* I add ``sex`` as an input parameter to the :ref:`factory function<test_factory_w_keyword_arguments>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-7

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(
            first_name, last_name,
            sex,
        ):
        return None

  the test passes.

----

* I want the :ref:`function<what is a function?>` to take an argument for ``year_of_birth``. I add it to the test in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 7

        def test_factory_w_keyword_arguments(self):
            # reality = src.person.factory()
            reality = src.person.factory(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=2000,
            )
            my_expectation = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() got
               an unexpected keyword argument 'year_of_birth'

  because the test called the :ref:`factory function<test_factory_w_keyword_arguments>` with a :ref:`keyword argument<test_keyword_arguments>` (``year_of_birth``) that is not in the :ref:`function definition<how to make a function>`.

* I add the name to the :ref:`function definition<how to make a function>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return None

  the test passes.

----

* I want the :ref:`factory function<test_factory_w_keyword_arguments>` to return a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by commas) as output when it is called. I change ``my_expectation`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9-10

        def test_factory_w_keyword_arguments(self):
            # reality = src.person.factory()
            reality = src.person.factory(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=2000,
            )
            # my_expectation = None
            my_expectation = dict()
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != {}

  because this happens when the test runs

  .. code-block:: python

    reality        = src.person.factory(
                         first_name='first_name',
                         last_name='last_name',
                         sex='M',
                         year_of_birth=2000,
                     )
                     # the factory function returns
                     None

  .. code-block:: python

    my_expectation = dict()
                     # the dict constructor returns
                     {}

  .. code-block:: python

    self.assertEqual(reality, my_expectation)
    self.assertEqual(None   , {}            )

  which raises :ref:`AssertionError<what causes AssertionError?>` since the :ref:`function<what is a function?>` returns :ref:`None<what is None?>` and the :ref:`assertion<what is an assertion?>` expects ``{}``.

* I change :ref:`None<what is None?>` in the :ref:`return statement<the return statement>`, to give the test what it wants, in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        # return None
        return {}

  the test passes because ``{}`` and ``dict()`` are two ways to :ref:`make the empty dictionary<test_making_a_dictionary>`.

----

* I add a :ref:`key<test_keys_of_a_dictionary>` called ``first_name`` to the :ref:`dictionary<what is a dictionary?>` for ``my_expectation``, with the same :ref:`value<test_values_of_a_dictionary>` as what is given in the call to the :ref:`factory function<test_factory_w_keyword_arguments>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10-13

        def test_factory_w_keyword_arguments(self):
            # reality = src.person.factory()
            reality = src.person.factory(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=2000,
            )
            # my_expectation = None
            # my_expectation = dict()
            my_expectation = dict(
                first_name='first_name',
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {} != {'first_name': 'first_name'}

  because this happens when the test runs

  .. code-block:: python

    reality        = src.person.factory(
                         first_name='first_name',
                         last_name='last_name',
                         sex='M',
                         year_of_birth=2000,
                     )
                     {} # the factory function returns {}

  .. code-block:: python

    my_expectation = dict(first_name='first_name')
                     {'first_name': 'first_name'}

  .. code-block:: python

    self.assertEqual(reality, my_expectation              )
    # is the same as
    self.assertEqual({}     , {'first_name': 'first_name'})

  which raises :ref:`AssertionError<what causes AssertionError?>` since the :ref:`function<what is a function?>` returns :ref:`the empty dictionary<test_making_a_dictionary>` and the :ref:`assertion<what is an assertion?>` expects one with ``first_name`` as the :ref:`key<test_keys_of_a_dictionary>`.

* I change the :ref:`return statement<the return statement>` to give the test what it wants, in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9-10

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        # return None
        # return {}
        return {'first_name': 'first_name'}

  the test passes.

* I change the value of ``first_name`` to ``'jane'`` to use a real name for ``reality`` and ``my_expectation``, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3-4, 10-11

        def test_factory_w_keyword_arguments(self):
            # reality = src.person.factory()
            reality = src.person.factory(
                # first_name='first_name',
                first_name='jane',
                last_name='last_name',
                sex='M',
                year_of_birth=2000,
            )
            # my_expectation = None
            # my_expectation = dict()
            my_expectation = dict(
                # first_name='first_name',
                first_name='jane',
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'first_name': 'first_name'}
                 != {'first_name': 'jane'}

  because this happens when the test runs

  .. code-block:: python

    reality        = src.person.factory(
                         first_name='jane',
                         last_name='last_name',
                         sex='M',
                         year_of_birth=2000,
                     )
                     # the factory function returns
                     {'first_name': 'first_name'}

  .. code-block:: python

    my_expectation = dict(first_name='jane')
                     # the dict constructor returns
                     {'first_name': 'jane'}

  .. code-block:: python

    self.assertEqual(reality, my_expectation)
    # is the same as
    self.assertEqual(
        {'first_name': 'first_name'},
        {'first_name': 'jane'}
    )

  which raises :ref:`AssertionError<what causes AssertionError?>` since I changed the :ref:`value<test_values_of_a_dictionary>` for ``first_name`` to ``'jane'`` in ``my_expectation`` and the :ref:`function<what is a function?>` returns a :ref:`dictionary<what is a dictionary?>` with a different value (``'first_name'``).

* I change the :ref:`value<test_values_of_a_dictionary>` for the ``first_name`` :ref:`key<test_keys_of_a_dictionary>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        # return None
        # return {}
        # return {'first_name': 'first_name'}
        return {'first_name': 'jane'}

  the test passes.

* I typed the value for ``first_name`` two times in the test, which means I had to make a change in two places when I wanted a different value for it. I add a :ref:`variable<what is a variable?>` for ``'jane'`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'

            # reality = src.person.factory()

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'jane'`` from the test

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 7-8, 17-18

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'

            # reality = src.person.factory()
            reality = src.person.factory(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                last_name='last_name',
                sex='M',
                year_of_birth=2000,
            )
            # my_expectation = None
            # my_expectation = dict()
            my_expectation = dict(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green. I now only need to change the value of ``first_name`` in one place in the test.

----

* I add a :ref:`key<test_keys_of_a_dictionary>` called ``last_name`` to the :ref:`dictionary<what is a dictionary?>` for ``my_expectation``, with the same :ref:`value<test_values_of_a_dictionary>` as what is given in the call to the :ref:`factory function<test_factory_w_keyword_arguments>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 19

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'

            # reality = src.person.factory()
            reality = src.person.factory(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                last_name='last_name',
                sex='M',
                year_of_birth=2000,
            )
            # my_expectation = None
            # my_expectation = dict()
            my_expectation = dict(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                last_name='last_name',
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        {'first_name': 'jane'}
     != {'first_name': 'jane', 'last_name': 'last_name'}

  because this happens when the test runs

  .. code-block:: python

    first_name = 'jane'

  .. code-block:: python

    reality        = src.person.factory(
                         first_name=first_name,
                         last_name='last_name',
                         sex='M',
                         year_of_birth=2000,
                     )
                     # the factory function returns
                     {'first_name': 'jane'}

  .. code-block:: python

    my_expectation = dict(
                         first_name=first_name,
                         last_name='last_name',
                     )
                     # the dict constructor returns
                     {
                         'first_name': 'jane',
                         'last_name': 'last_name'
                     }

  .. code-block:: python

    self.assertEqual(reality, my_expectation)
    # is the same as
    self.assertEqual(
        {'first_name': 'jane'},
        {'first_name': 'jane', 'last_name': 'last_name'}
    )

* I change the :ref:`return statement<the return statement>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-15

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        # return None
        # return {}
        # return {'first_name': 'first_name'}
        # return {'first_name': 'jane'}
        return {
            'first_name': 'jane',
            'last_name': 'last_name',
        }

  the test passes.

* I change the value of ``last_name`` to ``'doe'`` to use a real name for ``reality`` and ``my_expectation``, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9-10, 20-21

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'

            # reality = src.person.factory()
            reality = src.person.factory(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                last_name='doe',
                sex='M',
                year_of_birth=2000,
            )
            # my_expectation = None
            # my_expectation = dict()
            my_expectation = dict(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                last_name='doe',
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        {'first_name': 'jane', 'last_name': 'last_name'}
     != {'first_name': 'jane', 'last_name': 'doe'}

  because this happens when the test runs

  .. code-block:: python

    first_name = 'jane'

  .. code-block:: python

    reality        = src.person.factory(
                         first_name=first_name,
                         last_name='doe',
                         sex='M',
                         year_of_birth=2000,
                     )
                     # the factory function returns
                     {
                         'first_name': 'jane',
                         'last_name': 'last_name'
                     }

  .. code-block:: python

    my_expectation = dict(
                         first_name=first_name,
                         last_name='doe',
                     )
                     # the dict constructor returns
                     {
                         'first_name': 'jane',
                         'last_name': 'doe'
                     }

  .. code-block:: python

    self.assertEqual(reality, my_expectation)
    # is the same as
    self.assertEqual(
        {'first_name': 'jane', 'last_name': 'last_name'},
        {'first_name': 'jane', 'last_name': 'doe'}
    )

  which raises :ref:`AssertionError<what causes AssertionError?>` since I changed the :ref:`value<test_values_of_a_dictionary>` for ``last_name`` to ``'doe'`` in ``my_expectation`` and the :ref:`function<what is a function?>` returns a :ref:`dictionary<what is a dictionary?>` with a different value (``'last_name'``).

* I change the :ref:`value<test_values_of_a_dictionary>` for the ``last_name`` :ref:`key<test_keys_of_a_dictionary>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 14-15

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        # return None
        # return {}
        # return {'first_name': 'first_name'}
        # return {'first_name': 'jane'}
        return {
            'first_name': 'jane',
            # 'last_name': 'last_name',
            'last_name': 'doe',
        }

  the test passes.

* I typed the value for ``last_name`` two times in the test, which means I had to make a change in two places when I wanted a different value for it. I add a :ref:`variable<what is a variable?>` for ``'doe'`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'

            # reality = src.person.factory()

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'doe'`` from the test

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 11-12, 23-24

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'

            # reality = src.person.factory()
            reality = src.person.factory(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
                sex='M',
                year_of_birth=2000,
            )
            # my_expectation = None
            # my_expectation = dict()
            my_expectation = dict(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green. I now only need to change the value of ``last_name`` in one place in the test.

----

* I add a :ref:`key<test_keys_of_a_dictionary>` called ``sex`` to the :ref:`dictionary<what is a dictionary?>` for ``my_expectation``, with the same :ref:`value<test_values_of_a_dictionary>` as what is given in the call to the :ref:`factory function<test_factory_w_keyword_arguments>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 25

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'

            # reality = src.person.factory()
            reality = src.person.factory(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
                sex='M',
                year_of_birth=2000,
            )
            # my_expectation = None
            # my_expectation = dict()
            my_expectation = dict(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
                sex='M',
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe'}
                 != {'first_name': 'jane', 'last_name': 'doe',
                     'sex': 'M'}

  because this happens when the test runs

  .. code-block:: python

    first_name = 'jane'
    last_name = 'doe'

  .. code-block:: python

    reality        = src.person.factory(
                         first_name=first_name,
                         last_name=last_name,
                         sex='M',
                         year_of_birth=2000,
                     )
                     # the factory function returns
                     {
                         'first_name': 'jane',
                         'last_name': 'doe'
                     }

  .. code-block:: python

    my_expectation = dict(
                         first_name=first_name,
                         last_name=last_name,
                         sex='M'
                     )
                     # the dict constructor returns
                     {
                         'first_name': 'jane',
                         'last_name': 'doe',
                         'sex': 'M'
                     }

  .. code-block:: python

    self.assertEqual(reality, my_expectation)
    # is the same as
    self.assertEqual(
        {'first_name': 'jane', 'last_name': 'doe'},
        {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M'}
    )

* I add a new :ref:`key<test_keys_of_a_dictionary>` to the :ref:`return statement<the return statement>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 16

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        # return None
        # return {}
        # return {'first_name': 'first_name'}
        # return {'first_name': 'jane'}
        return {
            'first_name': 'jane',
            # 'last_name': 'last_name',
            'last_name': 'doe',
            'sex': 'M',
        }

  the test passes.

* I change the value of ``sex`` to ``'F'`` for ``reality`` and ``my_expectation``, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 13-14, 26-27

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'

            # reality = src.person.factory()
            reality = src.person.factory(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
                # sex='M',
                sex='F',
                year_of_birth=2000,
            )
            # my_expectation = None
            # my_expectation = dict()
            my_expectation = dict(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
                # sex='M',
                sex='F',
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M'}
     != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'}

  because this happens when the test runs

  .. code-block:: python

    first_name = 'jane'
    last_name = 'doe'

  .. code-block:: python

    reality        = src.person.factory(
                         first_name=first_name,
                         last_name=last_name,
                         sex='F',
                         year_of_birth=2000,
                     )
                     # the factory function returns
                     {
                         'first_name': 'jane',
                         'last_name': 'doe',
                         'sex': 'M'
                     }

  .. code-block:: python

    my_expectation = dict(
                         first_name=first_name,
                         last_name=last_name,
                         sex='F'
                     )
                     # the dict constructor returns
                     {
                         'first_name': 'jane',
                         'last_name': 'doe',
                         'sex': 'F'
                     }

  .. code-block:: python

    self.assertEqual(reality, my_expectation)
    # is the same as
    self.assertEqual(
        {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M'},
        {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'}
    )

  which raises :ref:`AssertionError<what causes AssertionError?>` since I changed the :ref:`value<test_values_of_a_dictionary>` for ``sex`` to ``'F'`` in ``my_expectation`` and the :ref:`function<what is a function?>` returns a :ref:`dictionary<what is a dictionary?>` with a different value (``'M'``).

* I change the :ref:`value<test_values_of_a_dictionary>` for the ``sex`` :ref:`key<test_keys_of_a_dictionary>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 16-17

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        # return None
        # return {}
        # return {'first_name': 'first_name'}
        # return {'first_name': 'jane'}
        return {
            'first_name': 'jane',
            # 'last_name': 'last_name',
            'last_name': 'doe',
            # 'sex': 'M',
            'sex': 'F',
        }

  the test passes.

* I typed the value for ``sex`` two times in the test, which means I had to make a change in two places when I wanted a different value for it. I add a :ref:`variable<what is a variable?>` for ``'F'`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'

            # reality = src.person.factory()

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'F'``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 15-16, 29-30

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'

            # reality = src.person.factory()
            reality = src.person.factory(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
                # sex='M',
                # sex='F',
                sex=sex,
                year_of_birth=2000,
            )
            # my_expectation = None
            # my_expectation = dict()
            my_expectation = dict(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
                # sex='M',
                # sex='F',
                sex=sex,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green. I now only need to change the value of ``sex`` in one place in the test.

----

* I want the :ref:`factory function<test_factory_w_keyword_arguments>` to return the age of the person it makes. I add a :ref:`key<test_keys_of_a_dictionary>` to ``my_expectation``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 31

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'

            # reality = src.person.factory()
            reality = src.person.factory(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
                # sex='M',
                # sex='F',
                sex=sex,
                year_of_birth=2000,
            )
            # my_expectation = None
            # my_expectation = dict()
            my_expectation = dict(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
                # sex='M',
                # sex='F',
                sex=sex,
                age=2026-2000,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'}
     != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F',
         'age': 26}

  because this happens when the test runs

  .. code-block:: python

    first_name = 'jane'
    last_name = 'doe'
    sex = 'F'

  .. code-block:: python

    reality        = src.person.factory(
                         first_name=first_name,
                         last_name=last_name,
                         sex=sex,
                         year_of_birth=2000,
                     )
                     # the factory function returns
                     {
                         'first_name': 'jane',
                         'last_name': 'last_name',
                         'sex': 'F'
                     }

  .. code-block:: python

    my_expectation = dict(
                         first_name=first_name,
                         last_name=last_name,
                         sex=sex,
                         age=2026-2000,
                     )
                     # the dict constructor returns
                     {
                         'first_name': 'jane',
                         'last_name': 'doe',
                         'sex': 'F',
                         'age': 26
                     }

  .. code-block:: python

    self.assertEqual(reality, my_expectation)
    self.assertEqual(
        {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'},
        {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F',
         'age': 26}
    )

* I add a new :ref:`key<test_keys_of_a_dictionary>` to the :ref:`return statement<the return statement>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 18

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        # return None
        # return {}
        # return {'first_name': 'first_name'}
        # return {'first_name': 'jane'}
        return {
            'first_name': 'jane',
            # 'last_name': 'last_name',
            'last_name': 'doe',
            # 'sex': 'M',
            'sex': 'F',
            'age': 26,
        }

  the test passes.

* I change ``2000`` to ``1996`` for ``reality`` and ``my_expectation``, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 17-18, 32-33

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'

            # reality = src.person.factory()
            reality = src.person.factory(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
                # sex='M',
                # sex='F',
                sex=sex,
                # year_of_birth=2000,
                year_of_birth=1996,
            )
            # my_expectation = None
            # my_expectation = dict()
            my_expectation = dict(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
                # sex='M',
                # sex='F',
                sex=sex,
                # age=2026-2000,
                age=2026-1996,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F',
         'age': 26}
     != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F',
         'age': 30}

  because this happens when the test runs

  .. code-block:: python

    first_name = 'jane'
    last_name = 'doe'
    sex = 'F'

  .. code-block:: python

    reality        = src.person.factory(
                         first_name=first_name,
                         last_name=last_name,
                         sex=sex,
                         year_of_birth=1996,
                     )
                     # the factory function returns
                     {
                         'first_name': 'jane',
                         'last_name': 'doe',
                         'sex': 'F'
                         'age': 26
                     }

  .. code-block:: python

    my_expectation = dict(
                         first_name=first_name,
                         last_name=last_name,
                         sex=sex,
                         age=2026-1996
                     )
                     # the dict constructor returns
                     {
                         'first_name': 'jane',
                         'last_name': 'doe',
                         'sex': 'F',
                         'age': 30
                     }

  .. code-block:: python

    self.assertEqual(reality, my_expectation)
    self.assertEqual(
        {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F',
         'age': 26},
        {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F',
         'age': 30}
    )

  which raises :ref:`AssertionError<what causes AssertionError?>` since I changed the calculation for ``age`` to ``2026-1996`` in ``my_expectation`` and the :ref:`function<what is a function?>` returns a :ref:`dictionary<what is a dictionary?>` with a different value (``26``).

* I change the :ref:`value<test_values_of_a_dictionary>` for the ``age`` :ref:`key<test_keys_of_a_dictionary>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 18-19

    # def factory():
    # def factory(first_name):
    # def factory(first_name, last_name):
    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        # return None
        # return {}
        # return {'first_name': 'first_name'}
        # return {'first_name': 'jane'}
        return {
            'first_name': 'jane',
            # 'last_name': 'last_name',
            'last_name': 'doe',
            # 'sex': 'M',
            'sex': 'F',
            # 'age': 26,
            'age': 30,
        }

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'F',
            'age': 30,
        }

* I typed the year of birth two times in the test, which means I had to make a change in two places when I wanted a different value for it. I add a :ref:`variable<what is a variable?>` for ``1996`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = 1996

            # reality = src.person.factory()

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``1996`` from the test

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 19-20, 35-36

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = 1996

            # reality = src.person.factory()
            reality = src.person.factory(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
                # sex='M',
                # sex='F',
                sex=sex,
                # year_of_birth=2000,
                # year_of_birth=1996,
                year_of_birth=year_of_birth,
            )
            # my_expectation = None
            # my_expectation = dict()
            my_expectation = dict(
                # first_name='first_name',
                # first_name='jane',
                first_name=first_name,
                # last_name='last_name',
                # last_name='doe',
                last_name=last_name,
                # sex='M',
                # sex='F',
                sex=sex,
                # age=2026-2000,
                # age=2026-1996,
                age=2026-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green. I now only need to change the value of ``year_of_birth`` in one place in the test.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 7

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = 1996

            reality = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                age=2026-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I open a new terminal_ then change directories to ``person``

  .. code-block:: python
    :emphasize-lines: 1

    cd person

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_factory_w_keyword_arguments'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test factory with current year
*********************************************************************************

There is a problem with the calculation for the age, it will be wrong if this program_ is run after 2026.

I want the value of the age to be a calculation based on the current year so that it will always be correct (at least most of the time).

I can do that with the `datetime module`_ from `The Python Standard Library`_ which is used for dates and times.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I change ``2026`` in ``my_expectation`` to use a :ref:`method<what is a method?>` from the `datetime module`_

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 17-21

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = 1996

            reality = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                # age=2026-year_of_birth,
                age=(
                    datetime.datetime.today().year
                  - year_of_birth
                ),
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'datetime' is not defined.
               Did you forget to import 'datetime'?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ for the `datetime module`_ at the top of ``test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import datetime
    import src.person
    import unittest

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'use current year for age calculation'

  the terminal_ shows a summary of the changes then goes back to the command line.

* ``import datetime`` brings in an :ref:`object (everything in Python is an object)<everything is an object>` for the `datetime module`_ so I can use it in ``test_person.py``. This means I can assume there is a ``datetime.py`` file_ on the computer that came with Python_

  .. code-block:: python

    import datetime    # import object for datetime.py

* ``datetime.datetime`` is a reference to the `datetime object`_ of the `datetime module`_. Wait a minute, that is the same name again. Do I have to remember all this?

  .. code-block:: python

    datetime.datetime  # use datetime object from datetime.py

* ``datetime.datetime.now()`` is a call to the `now method`_ of the `datetime.datetime object`_ from the `datetime module`_, it returns a `datetime.datetime object`_. Oh boy!

  .. code-block:: python

    datetime.datetime.now()   # returns datetime.datetime object

  I can also use the `today method`_ to get the same value

* ``datetime.datetime.today()`` is a call to the `today method`_ of the `datetime.datetime object`_ from the `datetime module`_, it also returns a `datetime.datetime object`_

  .. code-block:: python

    datetime.datetime.today() # returns datetime.datetime object

* ``datetime.datetime`` :ref:`objects<everything is an object>` have a ``year`` :ref:`attribute<what is a class attribute?>` that gives me the value of the current year which means I can do this to get the value of the current year

  .. code-block:: python

    result = datetime.datetime.now()
    this_year = result.year

  which is the same as

  .. code-block:: python

    this_year = datetime.datetime.now().year

  or

  .. code-block:: python

    result = datetime.datetime.today()
    this_year = result.year

  which is the same as

  .. code-block:: python

    this_year = datetime.datetime.today().year

  that was a lot of words, they become clearer in the chapters on :ref:`classes<everything is an object>`.

----

*********************************************************************************
test factory with random year_of_birth
*********************************************************************************

I want to use random values in the test to make sure the :ref:`factory function<test_factory_w_keyword_arguments>` can handle different values for ``year_of_birth`` and always calculates the right age.

I can do that with the `random module`_ from `The Python Standard Library`_ which is used to make fake random numbers.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I use a random integer_ (a whole number without decimals) for the ``year_of_birth`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 12-16

    import datetime
    import src.person
    import unittest


    class TestPerson(unittest.TestCase):

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            # year_of_birth = 1996
            year_of_birth = random.randint(
                datetime.datetime.now().year-120,
                datetime.datetime.now().year
            )

            reality = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'random' is not defined.
               Did you forget to import 'random'?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ for the `random module`_ at the top of ``test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import datetime
    import random
    import src.person
    import unittest

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 3, 5

    AssertionError:
        {'first_name': 'jane', 'last_name': 'doe',
          'sex': 'F', 'age': 30}
      != {'first_name': 'jane', 'last_name': 'doe',
          'sex': 'F', 'age': X}

  where ``X`` is a random age

  - ``import random`` brings in an :ref:`object (everything in Python is an object)<everything is an object>` for the `random module`_ so I can use it in ``test_person.py``. This means I can assume there is a ``random.py`` file_ on the computer that came with Python_

    .. code-block:: python

      import random    # import object for random.py

  - ``random.randint`` is a :ref:`method<what is a method?>` of the `random module`_. Okay, this one does not use the same name again.
  - ``datetime.datetime.now().year`` gives me the value of the current year
  - ``datetime.datetime.now().year-120`` gives me the value of the current year minus ``120`` (I assume there are no people older than ``120``, yet)
  - ``random.randint(datetime.datetime.now().year-120, datetime.datetime.now().year)`` is a call to the `randint method`_ of the `random module`_ with ``datetime.datetime.now().year-120`` and ``datetime.datetime.now().year`` as :ref:`positional arguments<test_positional_arguments>`. I can assume there is some definition in ``random.py`` that looks like this

    .. code-block:: python

      def randint(first_number, second_number):
          return random number
                 between first_number and second_number
                 including second_number

    it returns a random number from 120 years ago, up to and including the current year

  - anytime I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to save the file_, the test runs again and I get a new random :ref:`value<test_values_of_a_dictionary>` for the ``age`` :ref:`key<test_keys_of_a_dictionary>`

* I add a calculation for the age with the `today method`_ to the :ref:`return statement<the return statement>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9-13

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'F',
            # 'age': 30,
            'age': (
                datetime.datetime.today().year
              - year_of_birth
            ),
        }

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'datetime' is not defined.
               Did you forget to import 'datetime'?

  because datetime_ is not defined in this file_.

* I add an `import statement`_ for the `datetime module`_ at the top of ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import datetime


    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):

  the test passes because ``import datetime`` brings in an :ref:`object (everything in Python is an object)<everything is an object>` for the `datetime module`_ so I can use it in ``person.py``.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``datetime.datetime.now().year`` in ``test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 14

    import datetime
    import src.person
    import unittest
    import random


    class TestPerson(unittest.TestCase):

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'

            this_year = datetime.datetime.now().year
            # year_of_birth = 1996
            year_of_birth = random.randint(
                datetime.datetime.now().year-120,
                datetime.datetime.now().year
            )

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``datetime.datetime.now().year`` from the test

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 9-11, 26-27

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'

            this_year = datetime.datetime.now().year
            # year_of_birth = 1996
            year_of_birth = random.randint(
                # datetime.datetime.now().year-120,
                # datetime.datetime.now().year
                this_year-120, this_year
            )

            reality = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                # age=2026-year_of_birth,
                age=(
                    # datetime.datetime.today().year
                    this_year
                  - year_of_birth
                ),
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 21

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'

            this_year = datetime.datetime.now().year
            year_of_birth = random.randint(
                this_year-120, this_year
            )

            reality = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'use random values for year_of_birth'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test factory with random sex
*********************************************************************************

I want to use random values in the test to make sure the :ref:`factory function<test_factory_w_keyword_arguments>` can handle different values for ``sex``.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add randomness to the ``sex`` :ref:`variable<what is a variable?>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4-5

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            # sex = 'F'
            sex = random.choice(('F', 'M'))

            this_year = datetime.datetime.now().year

* I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to run the test a few times

  - if the value of ``sex`` is ``'F'``, the test passes
  - if the value of  ``sex`` is ``'M'``, the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: python
      :emphasize-text: M F

      AssertionError:
          {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F',
           'age': X}
       != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M',
           'age': X}

    where ``X`` is the random age

  - ``random`` is the `random module`_
  - ``random.choice`` is a :ref:`method<what is a method?>` of the `random module`_
  - ``('F', 'M')`` is a tuple_ with two strings_
  - ``random.choice(('F', 'M'))`` is a call to the `choice method`_ of the `random module`_ with ``('F', 'M')`` as input. I can assume there is some definition in ``random.py`` that looks like this

    .. code-block:: python

      def choice(collection):
          return random object from collection

    it randomly returns ``'F'`` or ``'M'`` every time the test runs.

  - I can also use random.choice(``'FM'``) to get the same result as ``random.choice(('F', 'M'))`` because a string_ like a tuple_ is :ref:`iterable<what is an iterable?>` and `random.choice`_ expects an :ref:`iterable<what is an iterable?>` as input

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I use the ``sex`` input parameter as the :ref:`value<test_values_of_a_dictionary>` for the ``'sex'`` :ref:`key<test_keys_of_a_dictionary>` instead of a value that does not change, in the :ref:`return statement<the return statement>` in ``person.py``

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 8-9

  def factory(
          first_name, last_name,
          sex, year_of_birth,
      ):
      return {
          'first_name': 'jane',
          'last_name': 'doe',
          # 'sex': 'F',
          'sex': sex,
          # 'age': 30,
          'age': (
              datetime.datetime.today().year
            - year_of_birth
          ),
      }

I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to run the test a few times and it passes with no random failures.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line in ``test_person.py``

  .. code-block:: python
    :lineno-start: 9

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = random.choice(('F', 'M'))

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'use random values for sex'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test factory with random last name
*********************************************************************************

I want to use random values in the test to make sure the :ref:`factory function<test_factory_w_keyword_arguments>` can handle different values for ``last_name``.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I use `random.choice`_ for the ``last_name`` :ref:`variable<what is a variable?>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3-6

        def test_factory_w_keyword_arguments(self):
            first_name = 'jane'
            # last_name = 'doe'
            last_name = random.choice((
                'doe', 'smith', 'blow', 'public',
            ))
            sex = random.choice(('F', 'M'))

* I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to run the test a few times

  - if the value of ``last_name`` is ``'doe'``, the test passes
  - if the value of ``last_name`` is NOT ``doe``, the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: python

      AssertionError:
          {'first_name': 'jane', 'last_name': 'doe', 'sex': Y,
           'age': X}
       != {'first_name': 'jane', 'last_name': Z,     'sex': Y,
           'age': X}

    where ``Z`` is the random last name, ``Y`` is the random sex and ``X`` is the random age

  - ``random.choice(('doe', 'smith', 'blow', 'public',))`` is a call to the `choice method`_ of the `random module`_ with ``('doe', 'smith', 'blow', 'public',)`` as input. It randomly returns ``'doe'`` or ``'smith'`` or ``'blow'`` or ``'public'`` every time the test runs.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I use the ``last_name`` input parameter as the :ref:`value<test_values_of_a_dictionary>` for the ``'last_name'`` :ref:`key<test_keys_of_a_dictionary>` instead of a value that does not change in the :ref:`return statement<the return statement>` in ``person.py``

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 7-8

  def factory(
          first_name, last_name,
          sex, year_of_birth,
      ):
      return {
          'first_name': 'jane',
          # 'last_name': 'doe',
          'last_name': last_name,
          # 'sex': 'F',
          'sex': sex,
          # 'age': 30,
          'age': (
              datetime.datetime.today().year
            - year_of_birth
          ),
      }

I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to run the test a few times and it passes with no random failures

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line from ``test_person.py``

  .. code-block:: python
    :lineno-start: 9

    def test_factory_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = random.choice((
            'doe', 'smith', 'blow', 'public',
        ))
        sex = random.choice(('F', 'M'))

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'use random values for last_name'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test factory with random first name
*********************************************************************************

I want to use random values in the test to make sure the :ref:`factory function<test_factory_w_keyword_arguments>` can handle different values for ``first_name``.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add randomness to the ``first_name`` :ref:`variable<what is a variable?>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2-5

        def test_factory_w_keyword_arguments(self):
            # first_name = 'jane'
            first_name = random.choice((
                'jane', 'joe', 'john', 'person',
            ))
            last_name = random.choice((
                'doe', 'smith', 'blow', 'public',
            ))
            sex = random.choice(('F', 'M'))

* I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to run the test a few times

  - if the value of ``first_name`` is ``'jane'``, the test passes
  - if the value of ``first_name`` is NOT ``'jane'`` the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: python

      AssertionError:
          {'first_name': 'jane', 'last_name': Z, 'sex': Y, 'age': X}
       != {'first_name': A,      'last_name': Z, 'sex': Y, 'age': X}

    where ``A`` is the random first name, ``Z`` is the random last name, ``Y`` is the random sex, and ``X`` is the random age

  - ``random.choice(('jane', 'joe', 'john', 'person',))`` is a call to the `choice method`_ of the `random module`_ with ``('jane', 'joe', 'john', 'person',)`` as input. It randomly returns ``'jane'`` or ``'joe'`` or ``'john'`` or ``'person'`` every time the test runs.


----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I use the ``first_name`` input parameter as the :ref:`value<test_values_of_a_dictionary>` for the ``'first_name'`` :ref:`key<test_keys_of_a_dictionary>` instead of a value that does not change, in the :ref:`return statement<the return statement>` in ``person.py``

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 6-7

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            # 'first_name': 'jane',
            'first_name': first_name,
            # 'last_name': 'doe',
            'last_name': last_name,
            # 'sex': 'F',
            'sex': sex,
            # 'age': 30,
            'age': (
                datetime.datetime.today().year
              - year_of_birth
            ),
        }

I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to run the test a few times and it passes with no random failures.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :linenos:

    import datetime


    def factory(
            first_name, last_name,
            sex, year_of_birth,
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

* I remove the commented line from ``test_person.py``

  .. code-block:: python
    :lineno-start: 9

        def test_factory_w_keyword_arguments(self):
            first_name = random.choice((
                'jane', 'joe', 'john', 'person',
            ))
            last_name = random.choice((
                'doe', 'smith', 'blow', 'public',
            ))
            sex = random.choice(('F', 'M'))

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'use random values for first_name'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
extract pick_one function
*********************************************************************************

The ``first_name``, ``last_name`` and ``sex`` :ref:`variables<what is a variable?>` all call the `random.choice method`_. I can add a :ref:`function<what is a function?>` for the calls.

----

* I go back to the terminal_ where the tests are running

* I add a :ref:`function<what is a function?>` for the calls to the `random.choice method`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    import datetime
    import src.person
    import unittest
    import random


    def pick_one(choices):
        return random.choice(choices)


    class TestPerson(unittest.TestCase):

        def test_factory_w_keyword_arguments(self):

* I use the new :ref:`function<what is a function?>` for the ``first_name`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2-3

        def test_factory_w_keyword_arguments(self):
            # first_name = random.choice((
            first_name = pick_one((
                'jane', 'joe', 'john', 'person',
            ))
            last_name = random.choice((
                'doe', 'smith', 'blow', 'public',
            ))
            sex = random.choice(('F', 'M'))

  the test is still green. So far, this is exactly the same as `random.choice`_, why would I make a :ref:`function<what is a function?>` that is exactly the same?

* Each call to the `random.choice`_ passes a tuple_ (:ref:`an iterable<what is an iterable?>`). I want the :ref:`function<what is a function?>` to be able to take any number of arguments I send, without knowing how many I will send

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3-4, 6-7

        def test_factory_w_keyword_arguments(self):
            # first_name = random.choice((
            # first_name = pick_one((
            first_name = pick_one(
                'jane', 'joe', 'john', 'person',
            # ))
            )
            last_name = random.choice((
                'doe', 'smith', 'blow', 'public',
            ))
            sex = random.choice(('F', 'M'))

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: pick_one() takes
               1 positional argument but 4 were given

  because the :ref:`function definition<how to make a function>` only takes one input and the test sends four.

* I add a :ref:`starred expressions<starred expressions>` like I did in :ref:`test_unknown_number_of_arguments` so that the ``pick_one`` :ref:`function<what is a function?>` can take any number of :ref:`positional arguments<test_positional_arguments>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

    def pick_one(*choices):
        return random.choice(choices)

  the test is green again, because

  .. code-block:: python

    first_name = pick_one('jane', 'joe', 'john', 'person')
                     pick_one(*choices)
                     random.choice(('jane', 'joe', 'john', 'person'))
                 # randomly return
                 # 'jane' or 'joe' or 'john' or 'person'

  :ref:`Python reads the positional arguments as a tuple<how Python reads starred expressions>` in the :ref:`function<what is a function?>` since I used a :ref:`starred expressions<starred expressions>` (``*choices``).

* I use the new :ref:`function<what is a function?>` for the ``last_name`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 8-9, 11-12

        def test_factory_w_keyword_arguments(self):
            # first_name = random.choice((
            # first_name = pick_one((
            first_name = pick_one(
                'jane', 'joe', 'john', 'person',
            # ))
            )
            # last_name = random.choice((
            last_name = pick_one(
                'doe', 'smith', 'blow', 'public',
            # ))
            )
            sex = random.choice(('F', 'M'))

  the test is still green, because

  .. code-block:: python

    last_name = pick_one('doe', 'smith', 'blow', 'public')
                    pick_one(*choices)
                    random.choice(('doe', 'smith', 'blow', 'public'))
                # randomly return
                # 'doe' or 'smith' or 'blow' or 'public'

  :ref:`Python reads the positional arguments as a tuple<how Python reads starred expressions>` in the :ref:`function<what is a function?>` since I used a :ref:`starred expressions<starred expressions>` (``*choices``).

* I use the new :ref:`function<what is a function?>` for the ``sex`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 13-14

        def test_factory_w_keyword_arguments(self):
            # first_name = random.choice((
            # first_name = pick_one((
            first_name = pick_one(
                'jane', 'joe', 'john', 'person',
            # ))
            )
            # last_name = random.choice((
            last_name = pick_one(
                'doe', 'smith', 'blow', 'public',
            # ))
            )
            # sex = random.choice(('F', 'M'))
            sex = pick_one('F', 'M')

  still green, because

  .. code-block:: python

    sex = pick_one('F', 'M'')
              pick_one(*choices)
              random.choice(('F', 'M'))
          # randomly return 'F' or 'M'

  :ref:`Python reads the positional arguments as a tuple<how Python reads starred expressions>` in the :ref:`function<what is a function?>` since I used a :ref:`starred expressions<starred expressions>` (``*choices``).

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 25

        def test_factory_w_keyword_arguments(self):
            first_name = pick_one(
                'jane', 'joe', 'john', 'person',
            )
            last_name = pick_one(
                'doe', 'smith', 'blow', 'public',
            )
            sex = pick_one('F', 'M')

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract pick_one function'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test factory with a dictionary
*********************************************************************************

The difference between the call to the :ref:`factory function<test_factory_w_keyword_arguments>` (``reality``) and the :ref:`dictionary<what is a dictionary?>` for ``my_expectation`` in the test is - ``year_of_birth`` and ``age``. One takes in a value for ``year_of_birth`` and the other uses ``year_of_birth`` to calculate the age, the other things are the same.

I can use a :ref:`dictionary<what is a dictionary?>` to remove the parts that are the same.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a :ref:`dictionary<what is a dictionary?>` for ``first_name``, ``last_name`` and ``year_of_birth``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 10-14

        def test_factory_w_keyword_arguments(self):
            first_name = pick_one(
                'jane', 'joe', 'john', 'person',
            )
            last_name = pick_one(
                'doe', 'smith', 'blow', 'public',
            )
            sex = pick_one('F', 'M')

            a_person = dict(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
            )

            this_year = datetime.datetime.now().year
            year_of_birth = random.randint(
                this_year-120, this_year
            )

* I use the new :ref:`variable<what is a variable?>` to remove ``first_name``, ``last_name``, and ``sex`` from the call to ``src.person.factory``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 22-25

        def test_factory_w_keyword_arguments(self):
            first_name = pick_one(
                'jane', 'joe', 'john', 'person',
            )
            last_name = pick_one(
                'doe', 'smith', 'blow', 'public',
            )
            sex = pick_one('F', 'M')

            a_person = dict(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
            )

            this_year = datetime.datetime.now().year
            year_of_birth = random.randint(
                this_year-120, this_year
            )

            reality = src.person.factory(
                # first_name=first_name,
                # last_name=last_name,
                # sex=sex,
                a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() missing
               2 required positional arguments:
               'last_name' and 'sex'

  because this happens

  .. code-block:: python

    first_name = pick_one('jane', 'joe', 'john', 'person',)
    last_name = pick_one('doe', 'smith', 'blow', 'public',)
    sex = pick_one('F', 'M')

  .. code-block:: python

    a_person = dict(
                   first_name=first_name,
                   last_name=last_name,
                   sex=sex,
               )

  .. code-block:: python

    reality = src.person.factory(
                  a_person,
                  year_of_birth
              )
                  src.person.factory(
                      first_name=a_person,
                      year_of_birth=year_of_birth
                  )

  - which raises :ref:`TypeError<what causes TypeError?>` since  I called the :ref:`factory function<test_factory_w_keyword_arguments>` with ``a_person`` as the first :ref:`positional argument<test_positional_arguments>` (``first_name``) and a value for ``year_of_birth``.  The :ref:`function<what is a function?>` wants the other required arguments.
  - Python_ uses the value for ``year_of_birth`` for the ``year_of_birth`` parameter because the names are the same, even though this given as the second :ref:`positional argument<test_positional_arguments>`.

  I want the :ref:`function<what is a function?>` to take the :ref:`key-value pairs of the dictionary<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` (``a_person``) as :ref:`keyword arguments<test_keyword_arguments>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I use a :ref:`double starred expressions<double starred expressions>` for the :ref:`dictionary<what is a dictionary?>` like I did in :ref:`test_unknown_number_of_arguments` to make it take the :ref:`key-value pairs of the dictionary<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` as :ref:`keyword arguments<test_keyword_arguments>`

.. code-block:: python
  :lineno-start: 33
  :emphasize-lines: 5-6

            reality = src.person.factory(
                # first_name=first_name,
                # last_name=last_name,
                # sex=sex,
                # a_person,
                **a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

the test is green again, because this happens

.. code-block:: python

  first_name = pick_one('jane', 'joe', 'john', 'person',)
  last_name = pick_one('doe', 'smith', 'blow', 'public',)
  sex = pick_one('F', 'M')

.. code-block:: python

  a_person = dict(
                 first_name=first_name,
                 last_name=last_name,
                 sex=sex,
             )

.. code-block:: python

  reality = src.person.factory(
                a_person,
                year_of_birth
            )
                src.person.factory(
                    **a_person,
                    year_of_birth
                )
                src.person.factory(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth
                )

:ref:`Python sends the dictionary as keyword arguments<how Python reads double starred expressions>` since I used a :ref:`double starred expressions<double starred expressions>` (``**a_person``).

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use the :ref:`variable<what is a variable?>` for ``my_expectation``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 10-13

            reality = src.person.factory(
                # first_name=first_name,
                # last_name=last_name,
                # sex=sex,
                # a_person,
                **a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                # first_name=first_name,
                # last_name=last_name,
                # sex=sex,
                a_person,
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green because this happens

  .. code-block:: python

    first_name = pick_one('jane', 'joe', 'john', 'person',)
    last_name = pick_one('doe', 'smith', 'blow', 'public',)
    sex = pick_one('F', 'M')

  .. code-block:: python

    a_person = dict(
                   first_name=first_name,
                   last_name=last_name,
                   sex=sex,
               )

  .. code-block:: python

    my_expectation = dict(
                         a_person,
                         age=this_year-year_of_birth
                     )
                         dict(
                             first_name=first_name,
                             last_name=last_name,
                             sex=sex,
                             age=this_year-year_of_birth
                         )

  the :ref:`dict constructor<test_making_a_dictionary>` can take another :ref:`dictionary<what is a dictionary?>` as input and uses the :ref:`key-value pairs of the dictionary<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` as :ref:`keyword arguments<test_keyword_arguments>`.

* I use the values of ``first_name``, ``last_name`` and the ``sex`` :ref:`variables<what is a variable?>` in the ``a_person`` :ref:`dictionary<what is a dictionary?>` because they are now only used once (by ``a_person``)

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2-8, 11-20

        def test_factory_w_keyword_arguments(self):
            # first_name = pick_one(
            #     'jane', 'joe', 'john', 'person',
            # )
            # last_name = pick_one(
            #     'doe', 'smith', 'blow', 'public',
            # )
            # sex = pick_one('F', 'M')

            a_person = dict(
                # first_name=first_name,
                # last_name=last_name,
                # sex=sex,
                first_name=pick_one(
                    'jane', 'joe', 'john', 'person',
                ),
                last_name=pick_one(
                    'doe', 'smith', 'blow', 'public',
                ),
                sex=pick_one('F', 'M'),
            )

  still green.

* I add a :ref:`function<what is a function?>` with a tuple_ of all the names for the test to have more random names to pick from

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5-9

    def pick_one(*choices):
        return random.choice(choices)


    def get_random_name():
        return pick_one(
            'jane', 'joe', 'john', 'person',
            'doe', 'smith', 'blow', 'public',
        )


    class TestPerson(unittest.TestCase):

        def test_factory_w_keyword_arguments(self):

* I use the :ref:`function<what is a function?>` in the ``a_person`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 14-21

        def test_factory_w_keyword_arguments(self):
            # first_name = pick_one(
            #     'jane', 'joe', 'john', 'person',
            # )
            # last_name = pick_one(
            #     'doe', 'smith', 'blow', 'public',
            # )
            # sex = pick_one('F', 'M')

            a_person = dict(
                # first_name=first_name,
                # last_name=last_name,
                # sex=sex,
                # first_name=pick_one(
                #     'jane', 'joe', 'john', 'person',
                # ),
                # last_name=pick_one(
                #     'doe', 'smith', 'blow', 'public',
                # ),
                first_name=get_random_name(),
                last_name=get_random_name(),
                sex=pick_one('F', 'M'),
            )

  green.

* I change the :ref:`assertion<what is an assertion?>` to make sure the test works correctly

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 16-17

            reality = src.person.factory(
                # first_name=first_name,
                # last_name=last_name,
                # sex=sex,
                # a_person,
                **a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                # first_name=first_name,
                # last_name=last_name,
                # sex=sex,
                a_person,
                age=this_year-year_of_birth,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, {})


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        {'first_name': A, 'last_name': Z, 'sex': Y, 'age': X}
     != {}

  where ``A`` is the random first name, ``Z`` is the random last name, ``Y`` is the random sex, and ``X`` is the random age.

* I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to run the test a few times and I get random values for ``'first_name'``, ``'last_name'``, ``'sex'`` and ``'age'`` each time

* I change the :ref:`assertion<what is an assertion?>` back

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 16-17

            reality = src.person.factory(
                # first_name=first_name,
                # last_name=last_name,
                # sex=sex,
                # a_person,
                **a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                # first_name=first_name,
                # last_name=last_name,
                # sex=sex,
                a_person,
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, {})


    # Exceptions seen

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 20
    :emphasize-text: get_random_name pick_one a_person

        def test_factory_w_keyword_arguments(self):
            a_person = dict(
                first_name=get_random_name(),
                last_name=get_random_name(),
                sex=pick_one('F', 'M'),
            )

            this_year = datetime.datetime.now().year
            year_of_birth = random.randint(
                this_year-120, this_year
            )

            reality = src.person.factory(
                **a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                a_person,
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract a_person dictionary'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*************************************************************************************
test_factory_w_optional_arguments
*************************************************************************************

I want to see what happens when I try to make a person without a value for the ``last_name`` argument.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I make a copy of :ref:`test_factory_w_keyword_arguments` and paste it below in ``test_person.py``

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 11-16, 18-21, 23-31

            reality = src.person.factory(
                **a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                a_person,
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_w_keyword_arguments(self):
            a_person = dict(
                first_name=get_random_name(),
                last_name=get_random_name(),
                sex=pick_one('F', 'M'),
            )

            this_year = datetime.datetime.now().year
            year_of_birth = random.randint(
                this_year-120, this_year
            )

            reality = src.person.factory(
                **a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                a_person,
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I change the name of the new test to :ref:`test_factory_w_optional_arguments`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 11
    :emphasize-text: test_factory_w_optional_arguments

            reality = src.person.factory(
                **a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                a_person,
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_w_optional_arguments(self):
            a_person = dict(
                first_name=get_random_name(),
                last_name=get_random_name(),
                sex=pick_one('F', 'M'),
            )

* I comment out the ``last_name`` :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in the ``a_person`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 4

        def test_factory_w_optional_arguments(self):
            a_person = dict(
                first_name=get_random_name(),
                # last_name=get_random_name(),
                sex=pick_one('F', 'M'),
            )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() missing 1 required
               positional argument: 'last_name'

  because this test no longer gives a value for ``last_name`` when it calls the :ref:`factory function<test_factory_w_keyword_arguments>`, I have to make ``last_name`` a choice, not a requirement.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a default value for ``last_name`` to make it optional, in the :ref:`factory function<test_factory_w_keyword_arguments>` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2-3

    def factory(
            # first_name, last_name,
            first_name, last_name=None,
            sex, year_of_birth,
        ):

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows
                 parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen in ``test_person.py``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I add a default value for ``sex`` to make it optional, in the :ref:`factory function<test_factory_w_keyword_arguments>` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    def factory(
            # first_name, last_name,
            first_name, last_name=None,
            # sex, year_of_birth,
            sex=None, year_of_birth,
        ):

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows
                 parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I add a default value for ``year_of_birth`` to make it optional

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5-6

    def factory(
            # first_name, last_name,
            first_name, last_name=None,
            # sex, year_of_birth,
            # sex=None, year_of_birth,
            sex=None, year_of_birth=None,
        ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: last_name

    AssertionError:
        {'first_name': Z, 'last_name': None, 'sex': Y,
         'age': X}
     != {'first_name': Z, 'sex': Y, 'age': X}

  because this happens when :ref:`the factory function<test_factory_w_keyword_arguments>` is called without a value for ``last_name``

  .. code-block:: python

    a_person = dict(
                   first_name=get_random_name(),
                   sex=pick_one('F', 'M'),
               )

  .. code-block:: python

    reality = src.person.factory(
                  **a_person,
                  year_of_birth=year_of_birth,
              )
                  src.person.factory(
                      first_name=get_random_name(),
                      sex=pick_one('F', 'M'),
                      year_of_birth=year_of_birth,
                  )
                  src.person.factory(
                      first_name=get_random_name(),
                      sex=pick_one('F', 'M'),
                      last_name=None, # use the default value
                      year_of_birth=year_of_birth,
                  )
              # the factory function returns
              {'first_name': Z, 'last_name': None, 'sex': Y,
                'age': X}

  .. code-block:: python

    my_expectation = dict(
                         a_person,
                         age=this_year-year_of_birth,
                     )
                         dict(
                             first_name=get_random_name(),
                             sex=pick_one('F', 'M'),
                             year_of_birth=year_of_birth,
                         )
                     # the dict constructor returns
                     {'first_name': Z, 'sex': Y, 'age': X}

  - which raises :ref:`AssertionError<what causes AssertionError?>` since the :ref:`factory function<test_factory_w_keyword_arguments>` returns a :ref:`dictionary<what is a dictionary?>` with a ``'last_name'`` :ref:`key<test_keys_of_a_dictionary>`, and the :ref:`assertion<what is an assertion?>` expects a :ref:`dictionary<what is a dictionary?>` without that :ref:`key<test_keys_of_a_dictionary>`
  - ``X`` is the random age, ``Y`` is the random sex and ``Z`` is the random first name

* I add a :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` for ``last_name`` to ``my_expectation`` in :ref:`test_factory_w_optional_arguments` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 7

            reality = src.person.factory(
                **a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                a_person,
                last_name='doe',
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: doe None

    AssertionError:
        {'first_name': Z, 'last_name': None,
         'sex': Y, 'age': X}
     != {'first_name': Z, 'sex': Y,
         'last_name': 'doe', 'age': X}

  because the :ref:`factory function<test_factory_w_keyword_arguments>` returns a :ref:`dictionary<what is a dictionary?>` with a :ref:`value<test_values_of_a_dictionary>` of :ref:`None<what is None?>` for ``last_name`` and the :ref:`assertion<what is an assertion?>` expects ``'doe'``.

* I change the default value for ``last_name`` in the :ref:`factory function<test_factory_w_keyword_arguments>` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3, 6

    def factory(
            # first_name, last_name,
            # first_name, last_name=None,
            # sex, year_of_birth,
            # sex=None, year_of_birth,
            first_name, last_name='doe',
            sex=None, year_of_birth=None,
        ):

  the test passes because the :ref:`default value<test_optional_arguments>` for the ``last_name`` parameter of the :ref:`function<what is a function?>` is ``'doe'``. This means that

  .. code-block:: python

    src.person.factory(
        first_name=first_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )

  is the same as

  .. code-block:: python

    src.person.factory(
        first_name=first_name,
        sex=sex,
        year_of_birth=year_of_birth,
        last_name='doe',
    )

  because :ref:`a function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I comment out the ``sex`` :ref:`key<test_keys_of_a_dictionary>` in :ref:`test_factory_w_optional_arguments` to see what happens when I call the :ref:`factory function<test_factory_w_keyword_arguments>` without it, in ``test_person.py``

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 10

        def test_factory_w_optional_arguments(self):
            this_year = datetime.datetime.now().year
            year_of_birth = random.randint(
                this_year-120, this_year
            )

            a_person = dict(
                first_name=get_random_name(),
                # last_name=get_random_name(),
                # sex=pick_one('F', 'M'),
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: sex

    AssertionError:
        {'first_name': Y, 'last_name': 'doe,
         'sex': None, 'age': X}
     != {'first_name': Y, 'last_name': 'doe', 'age': X}

  because this happens when :ref:`the factory function<test_factory_w_keyword_arguments>` is called without a value for ``sex``

  .. code-block:: python

    a_person = dict(first_name=get_random_name())

  .. code-block:: python

    reality = src.person.factory(
                  **a_person,
                  year_of_birth=year_of_birth,
              )
                  src.person.factory(
                      first_name=get_random_name(),
                      year_of_birth=year_of_birth,
                  )
                  src.person.factory(
                      first_name=get_random_name(),
                      sex=None,        # use the default value
                      last_name='doe', # use the default value
                      year_of_birth=year_of_birth,
                  )
              # the factory function returns
              {'first_name': Y, 'last_name': 'doe,
               'sex': None, 'age': X}

  .. code-block:: python

    my_expectation = dict(
                         a_person,
                         last_name='doe',
                         age=this_year-year_of_birth,
                     )
                         dict(
                             first_name=get_random_name(),
                             last_name='doe',
                             age=this_year-year_of_birth,
                         )
                     # the dict constructor returns
                     {'first_name': Y, 'last_name': 'doe', 'age': X}

  - which raises :ref:`AssertionError<what causes AssertionError?>` since the :ref:`factory function<test_factory_w_keyword_arguments>` returns a :ref:`dictionary<what is a dictionary?>` with a ``'sex'`` :ref:`key<test_keys_of_a_dictionary>`, and the :ref:`assertion<what is an assertion?>` expects a :ref:`dictionary<what is a dictionary?>` without that :ref:`key<test_keys_of_a_dictionary>`
  - ``X`` is the random age, ``Y`` is the random first name

* I add a :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` for ``sex`` to ``my_expectation`` in :ref:`test_factory_w_optional_arguments`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 8

            reality = src.person.factory(
                **a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                a_person,
                last_name='doe',
                sex='M',
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: M None

    AssertionError:
        {'first_name': Y, 'last_name': 'doe',
         'sex': None, 'age': X}
     != {'first_name': Y, 'last_name': 'doe',
         'sex': 'M', 'age': X}

  because the :ref:`factory function<test_factory_w_keyword_arguments>` returns a :ref:`dictionary<what is a dictionary?>` with a :ref:`value<test_values_of_a_dictionary>` of :ref:`None<what is None?>` for ``sex`` and the :ref:`assertion<what is an assertion?>` expects ``'M'``.

* I change the default value for ``sex`` in the :ref:`factory function<test_factory_w_keyword_arguments>` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8

    def factory(
            # first_name, last_name,
            # first_name, last_name=None,
            # sex, year_of_birth,
            # sex=None, year_of_birth,
            first_name, last_name='doe',
            # sex=None, year_of_birth=None,
            sex='M', year_of_birth=None,
        ):

  the test passes because the :ref:`default value<test_optional_arguments>` for the ``sex`` parameter of the :ref:`function<what is a function?>` is ``'M'``. This means that

  .. code-block:: python

    src.person.factory(
        first_name=first_name,
        year_of_birth=year_of_birth,
    )

  is the same as

  .. code-block:: python

    src.person.factory(
        first_name=first_name,
        year_of_birth=year_of_birth,
        last_name='doe',
        sex='M',
    )

  because :ref:`a function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

----

* I no longer need the ``a_person`` :ref:`dictionary<what is a dictionary?>` in :ref:`test_factory_w_optional_arguments` because it only has one :ref:`key<test_keys_of_a_dictionary>`, I can use a :ref:`variable<what is a variable?>` for ``first_name`` instead

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2

        def test_factory_w_optional_arguments(self):
            first_name = get_random_name()
            a_person = dict(
                first_name=get_random_name(),
                # last_name=get_random_name(),
                # sex=pick_one('F', 'M'),
            )

* I use the :ref:`variable<what is a variable?>` for ``first_name`` in the call to ``src.person.factory``

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 3

            reality = src.person.factory(
                **a_person,
                first_name=first_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                a_person,
                last_name='doe',
                sex='M',
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: src.person.factory() got multiple values
               for keyword argument 'first_name'

  because this happens

  .. code-block:: python

    first_name = get_random_name()
    a_person = dict(first_name=get_random_name())

  .. code-block:: python

    reality = src.person.factory(
                  **a_person,
                  first_name=first_name,
                  year_of_birth=year_of_birth,
              )
                  src.person.factory(
                      first_name=get_random_nam(),
                      first_name=first_name, # repeated keyword
                      year_of_birth=year_of_birth
                  )

  the ``a_person`` :ref:`dictionary<what is a dictionary?>` has a :ref:`key<test_keys_of_a_dictionary>` called ``first_name``, ``src.person.factory`` gets called with the same :ref:`keyword argument<test_keyword_arguments>` twice.

* I comment out ``**a_person,``

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2

            reality = src.person.factory(
                # **a_person,
                first_name=first_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                a_person,
                last_name='doe',
                sex='M',
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to run the test a few times

  - if the values for ``first_name`` match, the test passes
  - if the values for ``first_name`` are not the same, the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: python

      AssertionError:
          {'first_name': Y, 'last_name': 'doe',
           'sex': 'M', 'age': X}
       != {'first_name': Z, 'last_name': 'doe',
           'sex': 'M', 'age': X}

    where ``Y`` and ``Z`` are the random first names, and ``X`` is the random age

* I add a :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` for ``first_name`` to ``my_expectation`` in :ref:`test_factory_w_optional_arguments`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 8

            reality = src.person.factory(
                # **a_person,
                first_name=first_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                a_person,
                first_name=first_name,
                last_name='doe',
                sex='M',
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I remove the commented lines and the ``a_person`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 42

        def test_factory_w_optional_arguments(self):
            first_name = get_random_name()

            this_year = datetime.datetime.now().year
            year_of_birth = random.randint(
                this_year-120, this_year
            )

            reality = src.person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                first_name=first_name,
                last_name='doe',
                sex='M',
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green.

* I remove the commented lines from ``person.py``

  .. code-block:: python
    :lineno-start: 4

    def factory(
            first_name, last_name='doe',
            sex='M', year_of_birth=None,
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

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_factory_w_optional_arguments'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test_factory_person_says_hello
*********************************************************************************

I have a :ref:`function<what is a function?>` that takes in ``first_name``, ``last_name``, ``sex`` and ``year_of_birth`` for a person and returns a :ref:`dictionary<what is a dictionary?>` with ``first_name``, ``last_name``, ``sex`` and ``age`` (based on the ``year_of_birth``) as :ref:`keys<test_keys_of_a_dictionary>`.

What if I want the person to say hello, How would I do that? I can write a :ref:`function<what is a function?>` that takes in a person (:ref:`dictionary<what is a dictionary?>`) and returns a message (string_).

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a new test to ``test_person.py``

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 13-18, 20-22

            reality = src.person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                first_name=first_name,
                last_name='doe',
                sex='M',
                age=this_year-year_of_birth,
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_person_says_hello(self):
            joe = src.person.factory(
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

    AttributeError: module 'src.person'
                    has no attribute 'say_hello'

  because ``person.py`` does not have a :ref:`function<what is a function?>` named ``say_hello``, yet.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the :ref:`function<what is a function?>` to ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 16-17

    def factory(
            first_name, last_name='doe',
            sex='M', year_of_birth=None,
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


    def say_hello():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: say_hello() takes
               0 positional arguments but 1 was given

  because the :ref:`definition<how to make a function>` for ``say_hello`` does not allow inputs and the test called the :ref:`function<what is a function?>` with a :ref:`positional argument<test_positional_arguments>` (``person``).

* I add a name to the definition

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 1-2

    # def say_hello():
    def say_hello(person):
        return None

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

I want the ``say_hello`` :ref:`function<what is a function?>` to return a string_ for the person (:ref:`dictionary<what is a dictionary?>`) I give as input

* I change ``my_expectation`` to an :ref:`f-string<what is string interpolation?>` in :ref:`test_factory_person_says_hello` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 9-13

        def test_factory_person_says_hello(self):
            joe = src.person.factory(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )

            reality = src.person.say_hello(joe)
            # my_expectation = None
            my_expectation = (
                'Hello, my name is joe blow and I am'
                f' {datetime.datetime.now().year-1996}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        None != 'Hello, my name is joe blow and I am 30'

* I copy (:kbd:`ctrl/command+c`) the value from the terminal_ and paste it (:kbd:`ctrl/command+v`) in the :ref:`return statement<the return statement>` in ``person.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3-4

    # def say_hello():
    def say_hello(person):
        # return None
        return 'Hello, my name is joe blow and I am 30'

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for another person, to :ref:`test_factory_person_says_hello` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 9-13, 15-19

            reality = src.person.say_hello(joe)
            # my_expectation = None
            my_expectation = (
                'Hello, my name is joe blow and I am'
                f' {datetime.datetime.now().year-1996}'
            )
            self.assertEqual(reality, my_expectation)

            jane = src.person.factory(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )

            reality = src.person.say_hello(jane)
            my_expectation = (
                'Hello, my name is jane doe and I am'
                f' {datetime.datetime.now().year-1991}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: jane doe

    AssertionError:
          'Hello, my name is joe blow and I am 30'
       != 'Hello, my name is jane doe and I am 35'

  I have to make sure the ``say_hello`` :ref:`function<what is a function?>` uses the :ref:`values<test_values_of_a_dictionary>` of the ``person`` :ref:`dictionary<what is a dictionary?>` to make the message. I can do that with the :ref:`get method of dictionaries<test_get_value_of_a_key_in_a_dictionary>`.

* I change the string_ to an :ref:`f-string<what is string interpolation?>` with the :ref:`value<test_values_of_a_dictionary>` for the ``first_name`` in ``person.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3, 6-9

    # def say_hello():
    def say_hello(person):
        first_name = person.get('first_name')
        # return None
        # return 'Hello, my name is joe blow and I am 30'
        return (
            f'Hello, my name is {first_name}'
            ' blow and I am 30'
        )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-text: doe blow 30 35

    AssertionError:
        'Hello, my name is jane blow and I am 30'
     != 'Hello, my name is jane doe and I am 35'

  the values for ``first_name`` are the same because

  * this happens when ``jane = src.person.factory(first_name='jane', sex='F', year_of_birth=1991)`` runs

    .. code-block:: python

      jane = src.person.factory(
                 first_name='jane',
                 sex='F',
                 year_of_birth=1991,
             )
                 src.person.factory(
                     first_name='jane',
                     last_name='doe', # use the default value
                     year_of_birth=1991,
                     sex='F'
                 )
             # the factory function returns
             {'first_name': 'jane', 'last_name': 'doe',
              'sex': 'F', 'age': 35}

  * this happens in ``say_hello`` when  ``src.person.say_hello(jane)`` runs

    .. code-block:: python

      first_name = person.get('first_name')
                     jane.get('first_name')
                     {
                         'first_name': 'jane',
                         'last_name': 'doe',
                         'sex': 'F', 'age': 35
                     }.get('first_name')
                   # the get method returns
                   'jane'

    .. code-block:: python

      return (
          f'Hello, my name is {first_name}'
          ' blow and I am 30'
      )

  .. code-block:: python

    src.person.say_hello(jane)
    # the say_hello function returns
    'Hello, my name is jane blow and I am 30'

  which raises :ref:`AssertionError<what causes AssertionError?>` since the values for ``last_name`` and ``age`` are different.

* I use the :ref:`get method of the dictionary<test_get_value_of_a_key_in_a_dictionary>` to get the :ref:`value<test_values_of_a_dictionary>` for the ``last_name`` :ref:`key<test_keys_of_a_dictionary>`, then add it to the :ref:`return statement<the return statement>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4, 8-11

    # def say_hello():
    def say_hello(person):
        first_name = person.get('first_name')
        last_name = person.get('last_name')
        # return None
        # return 'Hello, my name is joe blow and I am 30'
        return (
            # f'Hello, my name is {first_name}'
            # ' blow and I am 30'
            f'Hello, my name is {first_name} {last_name}'
            ' and I am 30'
        )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-text: 30 35

    AssertionError:
        'Hello, my name is jane doe and I am 30'
     != 'Hello, my name is jane doe and I am 35'

  the values for ``last_name`` are the same because

  * this happens when ``jane = src.person.factory(first_name='jane', sex='F', year_of_birth=1991)`` runs

    .. code-block:: python

      jane = src.person.factory(
                 first_name='jane',
                 sex='F',
                 year_of_birth=1991,
             )
                 src.person.factory(
                     first_name='jane',
                     last_name='doe', # use the default value
                     year_of_birth=1991,
                     sex='F'
                 )
             # the factory function returns
             {'first_name': 'jane', 'last_name': 'doe',
              'sex': 'F', 'age': 35}

  * this happens in ``say_hello`` when  ``src.person.say_hello(jane)`` runs

    .. code-block:: python

      first_name = person.get('first_name')
                   # the get method returns
                   'jane'

    .. code-block:: python

      last_name = person.get('last_name')
                    jane.get('last_name')
                    {
                        'first_name': 'jane',
                        'last_name': 'doe',
                        'sex': 'F', 'age': 35
                    }.get('last_name')
                  # the get method returns
                  'doe'

    .. code-block:: python

      return (
          f'Hello, my name is {first_name} {last_name}'
          ' and I am 30'
      )

  .. code-block:: python

    src.person.say_hello(jane)
    # the say_hello function returns
    'Hello, my name is jane doe and I am 30'

  which raises :ref:`AssertionError<what causes AssertionError?>` since the values for ``age`` are different.

* I use the :ref:`get method of the dictionary<test_get_value_of_a_key_in_a_dictionary>` to get the :ref:`value<test_values_of_a_dictionary>` for the ``age`` :ref:`key<test_keys_of_a_dictionary>` , then add it to the :ref:`return statement<the return statement>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5, 12-13

    # def say_hello():
    def say_hello(person):
        first_name = person.get('first_name')
        last_name = person.get('last_name')
        age = person.get('age')
        # return None
        # return 'Hello, my name is joe blow and I am 30'
        return (
            # f'Hello, my name is {first_name}'
            # ' blow and I am 30'
            f'Hello, my name is {first_name} {last_name}'
            # ' and I am 30'
            f' and I am {age}'
        )

  the test passes because

  * this happens when ``jane = src.person.factory(first_name='jane', sex='F', year_of_birth=1991)`` runs

    .. code-block:: python

      jane = src.person.factory(
                 first_name='jane',
                 sex='F',
                 year_of_birth=1991,
             )
                 src.person.factory(
                     first_name='jane',
                     last_name='doe', # use the default value
                     year_of_birth=1991,
                     sex='F'
                 )
             # the factory function returns
             {'first_name': 'jane', 'last_name': 'doe',
              'sex': 'F', 'age': 35}

  * this happens in ``say_hello`` when  ``src.person.say_hello(jane)`` runs

    .. code-block:: python

      first_name = person.get('first_name')
                   # the get method returns
                   'jane'
      last_name  = person.get('last_name')
                   # the get method returns
                   'doe'

    .. code-block:: python

      age = person.get('age')
              jane.get('age')
              {
                  'first_name': 'jane',
                  'last_name': 'doe',
                  'sex': 'F', 'age': 35
              }.get('age')
            # the get method returns
            35

    .. code-block:: python

      return (
          f'Hello, my name is {first_name} {last_name}'
          f' and I am {age}'
      )

  .. code-block:: python

    src.person.say_hello(jane)
    # the say_hello function returns
    'Hello, my name is jane doe and I am 35'

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 19
    :emphasize-text: get

    def say_hello(person):
        first_name = person.get('first_name')
        last_name = person.get('last_name')
        age = person.get('age')

        return (
            f'Hello, my name is {first_name} {last_name}'
            f' and I am {age}'
        )

* I add an :ref:`assertion<what is an assertion?>` for a new person to :ref:`test_factory_person_says_hello` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 14-18, 20-25

            jane = src.person.factory(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )

            reality = src.person.say_hello(jane)
            my_expectation = (
                'Hello, my name is jane doe and I am'
                f' {datetime.datetime.now().year-1991}'
            )
            self.assertEqual(reality, my_expectation)

            john = src.person.factory(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )

            reality = src.person.say_hello(john)
            my_expectation = (
                'Hello, my name is jane doe and I am'
                f' {datetime.datetime.now().year-1991}'
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
    :lineno-start: 90
    :emphasize-lines: 9-12

            john = src.person.factory(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )

            reality = src.person.say_hello(john)
            my_expectation = (
                # 'Hello, my name is jane doe and I am'
                # f' {datetime.datetime.now().year-1991}'
                'Hello, my name is john smith and I am'
                f' {datetime.datetime.now().year-1580}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for one more person

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 10-15, 17-22

            reality = src.person.say_hello(john)
            my_expectation = (
                # 'Hello, my name is jane doe and I am'
                # f' {datetime.datetime.now().year-1991}'
                'Hello, my name is john smith and I am'
                f' {datetime.datetime.now().year-1580}'
            )
            self.assertEqual(reality, my_expectation)

            mary = src.person.factory(
                first_name='mary',
                last_name='public',
                year_of_birth=2000,
                sex='F',
            )

            reality = src.person.say_hello(mary)
            my_expectation = (
                'Hello, my name is john smith and I am'
                f' {datetime.datetime.now().year-1580}'
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
    :lineno-start: 105
    :emphasize-lines: 10-13

            mary = src.person.factory(
                first_name='mary',
                last_name='public',
                year_of_birth=2000,
                sex='F',
            )

            reality = src.person.say_hello(mary)
            my_expectation = (
                # 'Hello, my name is john smith and I am'
                # f' {datetime.datetime.now().year-1580}'
                'Hello, my name is mary public and I am'
                f' {datetime.datetime.now().year-2000}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add a :ref:`variable<what is a variable?>` for ``datetime.datetime.now().year``

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 2

        def test_factory_person_says_hello(self):
            this_year = datetime.datetime.now().year

            joe = src.person.factory(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``datetime.datetime.now().year`` from the test

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 14-15, 29-30, 43-44, 61-62

        def test_factory_person_says_hello(self):
            this_year = datetime.datetime.now().year

            joe = src.person.factory(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )

            reality = src.person.say_hello(joe)
            # my_expectation = None
            my_expectation = (
                'Hello, my name is joe blow and I am'
                # f' {datetime.datetime.now().year-1996}'
                f' {this_year-1996}'
            )
            self.assertEqual(reality, my_expectation)

            jane = src.person.factory(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )

            reality = src.person.say_hello(jane)
            my_expectation = (
                'Hello, my name is jane doe and I am'
                # f' {datetime.datetime.now().year-1991}'
                f' {this_year-1991}'
            )
            self.assertEqual(reality, my_expectation)

            john = src.person.factory(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )

            reality = src.person.say_hello(john)
            my_expectation = (
                # 'Hello, my name is jane doe and I am'
                # f' {datetime.datetime.now().year-1991}'
                'Hello, my name is john smith and I am'
                # f' {datetime.datetime.now().year-1580}'
                f' {this_year-1580}'
            )
            self.assertEqual(reality, my_expectation)

            mary = src.person.factory(
                first_name='mary',
                last_name='public',
                year_of_birth=2000,
                sex='F',
            )

            reality = src.person.say_hello(mary)
            my_expectation = (
                # 'Hi my name is john smith and I am'
                # f' {datetime.datetime.now().year-1580}'
                'Hello, my name is mary public and I am'
                # f' {datetime.datetime.now().year-2000}'
                f' {this_year-2000}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green.

* I add :ref:`variables<what is a variable?>` for ``'mary'``, ``'public'``, ``2000`` and the age calculation of ``mary``

  .. code-block:: python
    :lineno-start: 100
    :emphasize-lines: 11-14

            reality = src.person.say_hello(john)
            my_expectation = (
                # 'Hello, my name is jane doe and I am'
                # f' {datetime.datetime.now().year-1991}'
                'Hello, my name is john smith and I am'
                # f' {datetime.datetime.now().year-1580}'
                f' {this_year-1580}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'mary'
            last_name = 'public'
            year_of_birth = 2000
            age = this_year - year_of_birth

            mary = src.person.factory(
                first_name='mary',
                last_name='public',
                year_of_birth=2000,
                sex='F',
            )

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``'mary'``, ``'public'``, ``2000`` and the age calculation

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 7-12, 20, 22-24

            first_name = 'mary'
            last_name = 'public'
            year_of_birth = 2000
            age = this_year - year_of_birth

            mary = src.person.factory(
                # first_name='mary',
                # last_name='public',
                # year_of_birth=2000,
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
                sex='F',
            )

            reality = src.person.say_hello(mary)
            my_expectation = (
                # 'Hi my name is john smith and I am'
                # f' {datetime.datetime.now().year-1580}'
                # 'Hello, my name is mary public and I am'
                # f' {datetime.datetime.now().year-2000}'
                # f' {this_year-2000}'
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green.

* I add :ref:`variables<what is a variable?>` for ``'john'``, ``'smith'``, ``1580`` and the age calculation of ``john``

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 9-12

            reality = src.person.say_hello(jane)
            my_expectation = (
                'Hello, my name is jane doe and I am'
                # f' {datetime.datetime.now().year-1991}'
                f' {this_year-1991}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'john'
            last_name = 'smith'
            year_of_birth = 1580
            age = this_year - year_of_birth

            john = src.person.factory(
                first_name='john',
                last_name='smith',
                year_of_birth=1580,
            )

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``'john'``, ``'smith'``, ``1580`` and the age calculation

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 7-12, 19, 21-23

            first_name = 'john'
            last_name = 'smith'
            year_of_birth = 1580
            age = this_year - year_of_birth

            john = src.person.factory(
                # first_name='john',
                # last_name='smith',
                # year_of_birth=1580,
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(john)
            my_expectation = (
                # 'Hello, my name is jane doe and I am'
                # f' {datetime.datetime.now().year-1991}'
                # 'Hello, my name is john smith and I am'
                # f' {datetime.datetime.now().year-1580}'
                # f' {this_year-1580}'
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

  green.

* I add :ref:`variables<what is a variable?>` for ``'jane'``, ``1991`` and the age calculation of ``jane``

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 10-12

            reality = src.person.say_hello(joe)
            # my_expectation = None
            my_expectation = (
                'Hello, my name is joe blow and I am'
                # f' {datetime.datetime.now().year-1996}'
                f' {this_year-1996}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'jane'
            year_of_birth = 1991
            age = this_year - year_of_birth

            jane = src.person.factory(
                first_name='jane',
                sex='F',
                year_of_birth=1991,
            )

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``'jane'``, ``1991`` and the age calculation

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 6-7, 9-10, 15, 17-19

            first_name = 'jane'
            year_of_birth = 1991
            age = this_year - year_of_birth

            jane = src.person.factory(
                # first_name='jane',
                first_name=first_name,
                sex='F',
                # year_of_birth=1991,
                year_of_birth=year_of_birth
            )

            reality = src.person.say_hello(jane)
            my_expectation = (
                # 'Hello, my name is jane doe and I am'
                # f' {datetime.datetime.now().year-1991}'
                # f' {this_year-1991}'
                f'Hello, my name is {first_name}'
                f' doe and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

  still green.

* I add :ref:`variables<what is a variable?>` for ``'joe'``, ``'blow'``, ``1996`` and the age calculation for ``joe``

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 4-7

        def test_factory_person_says_hello(self):
            this_year = datetime.datetime.now().year

            first_name = 'joe'
            last_name = 'blow'
            year_of_birth = 1996
            age = this_year - year_of_birth

            joe = src.person.factory(
                first_name='joe',
                last_name='blow',
                year_of_birth=1996,
            )

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``'joe'``, ``'blow'``, ``1996`` and the age calculation

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 10-15, 21, 23-25

        def test_factory_person_says_hello(self):
            this_year = datetime.datetime.now().year

            first_name = 'joe'
            last_name = 'blow'
            year_of_birth = 1996
            age = this_year - year_of_birth

            joe = src.person.factory(
                # first_name='joe',
                # last_name='blow',
                # year_of_birth=1996,
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(joe)
            # my_expectation = None
            my_expectation = (
                # 'Hello, my name is joe blow and I am'
                # f' {datetime.datetime.now().year-1996}'
                # f' {this_year-1996}'
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 62

        def test_factory_person_says_hello(self):
            this_year = datetime.datetime.now().year

            first_name = 'joe'
            last_name = 'blow'
            year_of_birth = 1996
            age = this_year - year_of_birth

            joe = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(joe)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'jane'
            year_of_birth = 1991
            age = this_year - year_of_birth

            jane = src.person.factory(
                first_name=first_name,
                sex='F',
                year_of_birth=year_of_birth
            )

            reality = src.person.say_hello(jane)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' doe and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'john'
            last_name = 'smith'
            year_of_birth = 1580
            age = this_year - year_of_birth

            john = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(john)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'mary'
            last_name = 'public'
            year_of_birth = 2000
            age = this_year - year_of_birth

            mary = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
                sex='F',
            )

            reality = src.person.say_hello(mary)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am \
    'add test_factory_person_says_hello'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
extract get_current_year function
*********************************************************************************

Each test uses ``datetime.datetime.now().year`` to get the current year.

* I go back to the terminal_ where the tests are running

* I add a :ref:`function<what is a function?>` that returns the value of the current year

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 8-9

    def get_random_name():
        return pick_one(
            'jane', 'joe', 'john', 'person',
            'doe', 'smith', 'blow', 'public',
        )


    def get_current_year():
        return datetime.datetime.now().year


    class TestPerson(unittest.TestCase):

        def test_factory_w_keyword_arguments(self):

* I use the new :ref:`function<what is a function?>` for ``this_year`` in :ref:`test_factory_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 8-9

        def test_factory_w_keyword_arguments(self):
            a_person = dict(
                first_name=get_random_name(),
                last_name=get_random_name(),
                sex=pick_one('F', 'M'),
            )

            # this_year = datetime.datetime.now().year
            this_year = get_current_year()
            year_of_birth = random.randint(
                this_year-120, this_year
            )

  the test is still green.

* I use the :ref:`function<what is a function?>` for ``this_year`` in :ref:`test_factory_w_optional_arguments`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 4-5

        def test_factory_w_optional_arguments(self):
            first_name = get_random_name()

            # this_year = datetime.datetime.now().year
            this_year = get_current_year()
            year_of_birth = random.randint(
                this_year-120, this_year
            )

  still green.

* I use the :ref:`function<what is a function?>` for ``this_year`` in :ref:`test_factory_person_says_hello`

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 2-3

        def test_factory_person_says_hello(self):
            # this_year = datetime.datetime.now().year
            this_year = get_current_year()

            first_name = 'joe'
            last_name = 'blow'
            year_of_birth = 1996
            age = this_year - year_of_birth

  green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract get_current_year function'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
extract calculate_age function
*********************************************************************************

Each :ref:`assertion<what is an assertion?>` in every test has a calculation for the age

* I go back to the terminal_ where the tests are running

* I add a :ref:`function<what is a function?>` to calculate age

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 5-9

    def get_current_year():
        return datetime.datetime.now().year


    def calculate_age(year_of_birth):
        return (
            get_current_year()
          - year_of_birth
        )


    class TestPerson(unittest.TestCase):

        def test_factory_w_keyword_arguments(self):

* I add a :ref:`call<how to call a function with input>` to the :ref:`function<what is a function?>` for the value of ``age`` in ``my_expectation`` in :ref:`test_factory_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 7-8

            reality = src.person.factory(
                **a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                a_person,
                # age=this_year-year_of_birth,
                age=calculate_age(year_of_birth),
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_w_optional_arguments(self):

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 31
    :emphasize-text: calculate_age

        def test_factory_w_keyword_arguments(self):
            a_person = dict(
                first_name=get_random_name(),
                last_name=get_random_name(),
                sex=pick_one('F', 'M'),
            )

            this_year = get_current_year()
            year_of_birth = random.randint(
                this_year-120, this_year
            )

            reality = src.person.factory(
                **a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                a_person,
                age=calculate_age(year_of_birth),
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_w_optional_arguments(self):

* I add a :ref:`call<how to call a function with input>` to the :ref:`function<what is a function?>` for the value of ``age`` in ``my_expectation`` in :ref:`test_factory_w_optional_arguments`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 9-10

            reality = src.person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                first_name=first_name,
                last_name='doe',
                sex='M',
                # age=this_year-year_of_birth,
                age=calculate_age(year_of_birth),
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_person_says_hello(self):

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 53
    :emphasize-text: calculate_age

        def test_factory_w_optional_arguments(self):
            first_name = get_random_name()

            this_year = get_current_year()
            year_of_birth = random.randint(
                this_year-120, this_year
            )

            reality = src.person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                first_name=first_name,
                last_name='doe',
                sex='M',
                age=calculate_age(year_of_birth),
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_person_says_hello(self):

* I add a :ref:`call<how to call a function with input>` to the :ref:`function<what is a function?>` for the value of ``age`` for ``joe`` in :ref:`test_factory_person_says_hello`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 8-9

        def test_factory_person_says_hello(self):
            # this_year = datetime.datetime.now().year
            this_year = get_current_year()

            first_name = 'joe'
            last_name = 'blow'
            year_of_birth = 1996
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

            joe = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(joe)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'jane'
            year_of_birth = 1991
            age = this_year - year_of_birth

  the test is still green.

* I add a :ref:`call<how to call a function with input>` to the :ref:`function<what is a function?>` for the value of ``age`` for ``jane``

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 3-4

            first_name = 'jane'
            year_of_birth = 1991
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

            jane = src.person.factory(
                first_name=first_name,
                sex='F',
                year_of_birth=year_of_birth
            )

            reality = src.person.say_hello(jane)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' doe and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'john'
            last_name = 'smith'
            year_of_birth = 1580
            age = this_year - year_of_birth

  still green.

* I add a :ref:`call<how to call a function with input>` to the :ref:`function<what is a function?>` for the value of ``age`` for ``john``

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 4-5

            first_name = 'john'
            last_name = 'smith'
            year_of_birth = 1580
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

            john = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(john)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'mary'
            last_name = 'public'
            year_of_birth = 2000
            age = this_year - year_of_birth

  green.

* I add a :ref:`call<how to call a function with input>` to the :ref:`function<what is a function?>` for the value of ``age`` for ``mary``

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 10-11

            first_name = 'mary'
            last_name = 'public'
            year_of_birth = 2000
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

  the test is still green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract calculate_age function'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test_factory_person_says_hello with random year_of_birth
*********************************************************************************

I want to use random values for ``year_of_birth`` in the tests

* I go back to the terminal_ where the tests are running

* I use a call to `random.randint`_ to get a random value for the ``year_of_birth`` of ``joe``

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 7-10

        def test_factory_person_says_hello(self):
            # this_year = datetime.datetime.now().year
            this_year = get_current_year()

            first_name = 'joe'
            last_name = 'blow'
            # year_of_birth = 1996
            year_of_birth = random.randint(
                this_year-120, this_year
            )
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

            joe = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(joe)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'jane'
            year_of_birth = 1991
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

  the test is still green.

* I use a call to `random.randint`_ to get a random value for the ``year_of_birth`` of ``jane``

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 2-5

            first_name = 'jane'
            # year_of_birth = 1991
            year_of_birth = random.randint(
                this_year-120, this_year
            )
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

            jane = src.person.factory(
                first_name=first_name,
                sex='F',
                year_of_birth=year_of_birth
            )

            reality = src.person.say_hello(jane)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' doe and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'john'
            last_name = 'smith'
            year_of_birth = 1580
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

  still green.

* I use a call to `random.randint`_ to get a random value for the ``year_of_birth`` of ``john``

  .. code-block:: python
    :lineno-start: 120
    :emphasize-lines: 3-6

            first_name = 'john'
            last_name = 'smith'
            # year_of_birth = 1580
            year_of_birth = random.randint(
                this_year-120, this_year
            )
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

            john = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(john)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'mary'
            last_name = 'public'
            year_of_birth = 2000
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

  green.

* I use a call to `random.randint`_ to get a random value for the ``year_of_birth`` of ``mary``

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 3-6

            first_name = 'mary'
            last_name = 'public'
            # year_of_birth = 2000
            year_of_birth = random.randint(
                this_year-120, this_year
            )
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

            mary = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
                sex='F',
            )

            reality = src.person.say_hello(mary)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'test_factory_person_says_hello with random year_of_birth'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
extract get_random_year_of_birth function
*********************************************************************************

I make the ``this_year`` and ``year_of_birth`` :ref:`variables<what is a variable?>` the same way in all three tests.

* I go back to the terminal_ where the tests are running

* I add a :ref:`function<what is a function?>` to use to replace the repetition of making the values for the ``this_year`` and ``year_of_birth`` :ref:`variables<what is a variable?>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 8-12

    def calculate_age(year_of_birth):
        return (
            get_current_year()
          - year_of_birth
        )


    def get_random_year_of_birth():
        this_year = get_current_year()
        return random.randint(
            this_year-120, this_year
        )


    class TestPerson(unittest.TestCase):

        def test_factory_w_keyword_arguments(self):

* I use the ``get_random_year_of_birth`` :ref:`function<what is a function?>` to replace the repetition of making the values for the ``this_year`` and ``year_of_birth`` :ref:`variables<what is a variable?>` in :ref:`test_factory_w_keyword_arguments`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 8-12

        def test_factory_w_keyword_arguments(self):
            a_person = dict(
                first_name=get_random_name(),
                last_name=get_random_name(),
                sex=pick_one('F', 'M'),
            )

            # this_year = get_current_year()
            # year_of_birth = random.randint(
            #     this_year-120, this_year
            # )
            year_of_birth = get_random_year_of_birth()

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 38

        def test_factory_w_keyword_arguments(self):
            a_person = dict(
                first_name=get_random_name(),
                last_name=get_random_name(),
                sex=pick_one('F', 'M'),
            )
            year_of_birth = get_random_year_of_birth()

            reality = src.person.factory(
                **a_person,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                a_person,
                age=calculate_age(year_of_birth),
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_w_optional_arguments(self):

* I use the ``get_random_year_of_birth`` :ref:`function<what is a function?>` to replace the repetition of making the values for the ``this_year`` and ``year_of_birth`` :ref:`variables<what is a variable?>` in :ref:`test_factory_w_optional_arguments`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 4-8

        def test_factory_w_optional_arguments(self):
            first_name = get_random_name()

            # this_year = get_current_year()
            # year_of_birth = random.randint(
            #     this_year-120, this_year
            # )
            year_of_birth = get_random_year_of_birth()

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 56

        def test_factory_w_optional_arguments(self):
            first_name = get_random_name()
            year_of_birth = get_random_year_of_birth()

            reality = src.person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
            )
            my_expectation = dict(
                first_name=first_name,
                last_name='doe',
                sex='M',
                age=calculate_age(year_of_birth),
            )
            self.assertEqual(reality, my_expectation)

        def test_factory_person_says_hello(self):

* I use the ``get_random_year_of_birth`` :ref:`function<what is a function?>` to replace the repetition of making the values for the ``this_year`` and ``year_of_birth`` :ref:`variables<what is a variable?>` for ``joe`` in :ref:`test_factory_person_says_hello`

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 8-10, 12

        def test_factory_person_says_hello(self):
            # this_year = datetime.datetime.now().year
            this_year = get_current_year()

            first_name = 'joe'
            last_name = 'blow'
            # year_of_birth = 1996
            # year_of_birth = random.randint(
            #     this_year-120, this_year
            # )
            # age = this_year - year_of_birth
            year_of_birth = get_random_year_of_birth()
            age = calculate_age(year_of_birth)

            joe = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(joe)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'jane'
            # year_of_birth = 1991
            year_of_birth = random.randint(
                this_year-120, this_year
            )
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

  the test is still green.

* I use the ``get_random_year_of_birth`` :ref:`function<what is a function?>` to replace the repetition of making the values for the ``this_year`` and ``year_of_birth`` :ref:`variables<what is a variable?>` for ``jane``

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 3-5, 7

            first_name = 'jane'
            # year_of_birth = 1991
            # year_of_birth = random.randint(
            #     this_year-120, this_year
            # )
            # age = this_year - year_of_birth
            year_of_birth = get_random_year_of_birth()
            age = calculate_age(year_of_birth)

            jane = src.person.factory(
                first_name=first_name,
                sex='F',
                year_of_birth=year_of_birth
            )

            reality = src.person.say_hello(jane)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' doe and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'john'
            last_name = 'smith'
            # year_of_birth = 1580
            year_of_birth = random.randint(
                this_year-120, this_year
            )
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

  still green.

* I use the ``get_random_year_of_birth`` :ref:`function<what is a function?>` to replace the repetition of making the values for the ``this_year`` and ``year_of_birth`` :ref:`variables<what is a variable?>` for ``john``

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 4-6, 8

            first_name = 'john'
            last_name = 'smith'
            # year_of_birth = 1580
            # year_of_birth = random.randint(
            #     this_year-120, this_year
            # )
            # age = this_year - year_of_birth
            year_of_birth = get_random_year_of_birth()
            age = calculate_age(year_of_birth)

            john = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(john)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'mary'
            last_name = 'public'
            # year_of_birth = 2000
            year_of_birth = random.randint(
                this_year-120, this_year
            )
            # age = this_year - year_of_birth
            age = calculate_age(year_of_birth)

  green.

* I use the ``get_random_year_of_birth`` :ref:`function<what is a function?>` to replace the repetition of making the values for the ``this_year`` and ``year_of_birth`` :ref:`variables<what is a variable?>` for ``mary``

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 4-6, 8

            first_name = 'mary'
            last_name = 'public'
            # year_of_birth = 2000
            # year_of_birth = random.randint(
            #     this_year-120, this_year
            # )
            # age = this_year - year_of_birth
            year_of_birth = get_random_year_of_birth()
            age = calculate_age(year_of_birth)

  still green.

* I remove the commented lines and ``this_year`` :ref:`variable<what is a variable?>` since it is no longer used

  .. code-block:: python
    :lineno-start: 72

        def test_factory_person_says_hello(self):
            first_name = 'joe'
            last_name = 'blow'
            year_of_birth = get_random_year_of_birth()
            age = calculate_age(year_of_birth)

            joe = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(joe)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'jane'
            year_of_birth = get_random_year_of_birth()
            age = calculate_age(year_of_birth)

            jane = src.person.factory(
                first_name=first_name,
                sex='F',
                year_of_birth=year_of_birth
            )

            reality = src.person.say_hello(jane)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' doe and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'john'
            last_name = 'smith'
            year_of_birth = get_random_year_of_birth()
            age = calculate_age(year_of_birth)

            john = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            reality = src.person.say_hello(john)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
            )
            self.assertEqual(reality, my_expectation)

            first_name = 'mary'
            last_name = 'public'
            year_of_birth = get_random_year_of_birth()
            age = calculate_age(year_of_birth)

            mary = src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
                sex='F',
            )

            reality = src.person.say_hello(mary)
            my_expectation = (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am {age}'
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
    'extract get_random_year_of_birth function'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test_person_tests
*********************************************************************************

I want to write the solution without looking at the tests

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I close ``test_person.py``
* then I delete all the text in ``person.py``, the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    FAILED ...test_factory_person_says_hello -
        AttributeError: module 'src.person' has
                        no attribute 'factory'
    FAILED ...test_factory_w_keyword_arguments -
        AttributeError: module 'src.person' has
                        no attribute 'factory'
    FAILED ...test_factory_w_optional_arguments -
        AttributeError: module 'src.person' has
                        no attribute 'factory'

  because there is nothing in ``person.py`` with the name ``factory``.

Can you make the tests pass without looking at how I solve it below? You can come back to compare solutions when you are done or if you get stuck.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    factory

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'factory' is not defined

  because I have not told Python_ what ``factory`` means

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # factory
    factory = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because ``factory`` points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I make ``factory`` a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

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
               an unexpected keyword argument 'first_name'

  because the test called the :ref:`factory function<test_factory_w_keyword_arguments>` with a :ref:`keyword argument<test_keyword_arguments>` (``first_name``) that is not in the :ref:`function definition<how to make a function>`

* I add ``first_name`` to the :ref:`function definition<how to make a function>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # factory
    # factory = None
    # def factory():
    def factory(first_name):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() got
               an unexpected keyword argument 'year_of_birth'

  because the test called the :ref:`factory function<test_factory_w_keyword_arguments>` with a :ref:`keyword argument<test_keyword_arguments>` (``year_of_birth``) that is not in the :ref:`function definition<how to make a function>`

* I add ``year_of_birth`` to the :ref:`function definition<how to make a function>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    # factory
    # factory = None
    # def factory():
    # def factory(first_name):
    def factory(first_name, year_of_birth):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != {'first_name': Y,
                             'last_name': 'doe',
                             'sex': 'M', 'age': X}

  because the :ref:`assertion<what is an assertion?>` expects a :ref:`dictionary<what is a dictionary?>` and the :ref:`factory function<test_factory_w_keyword_arguments>` returns :ref:`None<what is None?>`

* I copy and paste the :ref:`dictionary<what is a dictionary?>` from the terminal_ to make the :ref:`function<what is a function?>` return a :ref:`dictionary<what is a dictionary?>` instead of :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-12

    # factory
    # factory = None
    # def factory():
    # def factory(first_name):
    def factory(first_name, year_of_birth):
        # return None
        return {
            'first_name': 'john',
            'last_name': 'doe',
            'sex': 'M',
            'age': 55,
        }

  I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to run the test a few times and the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        {'first_name': A, 'last_name': 'doe',
         'sex': 'M', 'age': Y}
     != {'first_name': Z, 'last_name': 'doe',
         'sex': 'M', 'age': X}

  the :ref:`values<test_values_of_a_dictionary>` of the ``age`` and ``first_name`` :ref:`keys<test_keys_of_a_dictionary>` change randomly

* I use the ``first_name`` input parameter in the :ref:`return statement<the return statement>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9

    # factory
    # factory = None
    # def factory():
    # def factory(first_name):
    def factory(first_name, year_of_birth):
        # return None
        return {
            # 'first_name': 'john',
            'first_name': first_name,
            'last_name': 'doe',
            'sex': 'M',
            'age': 55,
        }

  the first name matches and if the ages are different, the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        {'first_name': Z, 'last_name': 'doe',
         'sex': 'M', 'age': Y}
     != {'first_name': Z, 'last_name': 'doe',
         'sex': 'M', 'age': X}

  and :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: factory() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

* I use the ``year_of_birth`` input parameter in the :ref:`return statement<the return statement>` for the :ref:`value<test_values_of_a_dictionary>` of ``age``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 12-13

    # factory
    # factory = None
    # def factory():
    # def factory(first_name):
    def factory(first_name, year_of_birth):
        # return None
        return {
            # 'first_name': 'john',
            'first_name': first_name,
            'last_name': 'doe',
            'sex': 'M',
            # 'age': 55,
            'age': year_of_birth,
        }

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        {'first_name': Y, 'last_name': 'doe',
         'sex': 'M', 'age': ABCD}
     != {'first_name': Y, 'last_name': 'doe',
         'sex': 'M', 'age': X}

  because the :ref:`factory function<test_factory_w_keyword_arguments>` returned 4 digits (a year) as the :ref:`value<test_values_of_a_dictionary>` for the ``age`` :ref:`key<test_keys_of_a_dictionary>`, and the :ref:`assertion<what is an assertion?>` expects the difference between that :ref:`value<test_values_of_a_dictionary>` and the current year

* I add an `import statement`_ for the `datetime module`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import datetime



    # factory
    # factory = None
    # def factory():
    # def factory(first_name):
    def factory(first_name, year_of_birth):

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I use the `datetime module`_ to get the current year, then use it for the ``age`` calculation

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 10-13

    def factory(first_name, year_of_birth):
        # return None
        return {
            # 'first_name': 'john',
            'first_name': first_name,
            'last_name': 'doe',
            'sex': 'M',
            # 'age': 55,
            # 'age': year_of_birth,
            'age': (
                datetime.datetime.today().year
              - year_of_birth
            ),
        }

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: factory() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

  because the test called the :ref:`factory function<test_factory_w_keyword_arguments>` with a :ref:`keyword argument<test_keyword_arguments>` (``last_name``) that is not in the :ref:`function definition<how to make a function>`

* I add a new input parameter to the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1-5
    :emphasize-text: last_name

    # def factory(first_name, year_of_birth):
    def factory(
            first_name, year_of_birth,
            last_name,
        ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() missing 1 required
               positional argument: 'last_name'

  because the test called the :ref:`function<what is a function?>` with another argument and Python_ took that argument as a :ref:`positional argument<test_positional_arguments>` for ``last_name``

* I add a default value for ``last_name`` so Python_ does not take it is a :ref:`positional argument<test_positional_arguments>` when a name is not given

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3-4

    def factory(
            first_name, year_of_birth,
            # last_name,
            last_name=None,
        ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() got
               an unexpected keyword argument 'sex'

  because the test called the :ref:`factory function<test_factory_w_keyword_arguments>` with a :ref:`keyword argument<test_keyword_arguments>` (``sex``) that is not in the :ref:`function definition<how to make a function>`

* I add the name to the :ref:`definition of the function<how to make a function>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 4-5
    :emphasize-text: sex

    def factory(
            first_name, year_of_birth,
            # last_name,
            # last_name=None,
            last_name=None, sex,
        ):

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows
                 parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I add a default value for ``sex`` to make it optional

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 5-6

    def factory(
            first_name, year_of_birth,
            # last_name,
            # last_name=None,
            # last_name=None, sex,
            last_name=None, sex=None,
        ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`
  ``first_name`` and ``age`` match. If the last names are different, the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: B A

    AssertionError:
        {'first_name': C, 'last_name': B, 'sex': Z, 'age': X}
     != {'first_name': C, 'last_name': A, 'sex': Y, 'age': X}

  and :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.person'
                    has no attribute 'say_hello'

* I use the ``sex`` input parameter in the :ref:`return statement<the return statement>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 13-14

    def factory(
            first_name, year_of_birth,
            # last_name,
            # last_name=None,
            # last_name=None, sex,
            last_name=None, sex=None,
        ):
        # return None
        return {
            # 'first_name': 'john',
            'first_name': first_name,
            'last_name': 'doe',
            # 'sex': 'M',
            'sex': sex,
            # 'age': 55,
            # 'age': year_of_birth,
            'age': (
                datetime.datetime.today().year
              - year_of_birth
            ),
        }

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: None M

    AssertionError:
        {'first_name': Y, 'last_name': 'doe',
         'sex': None, 'age': X}
     != {'first_name': Y, 'last_name': 'doe',
         'sex': 'M', 'age': X}

  because the :ref:`assertion<what is an assertion?>` expects ``'M'`` as the :ref:`value<test_values_of_a_dictionary>` of ``sex`` and the :ref:`function<what is a function?>` returns :ref:`None<what is None?>` which is its default value

* I change the default value of ``sex`` to ``'M'``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 6-7

    def factory(
        first_name, year_of_birth,
        # last_name,
        # last_name=None,
        # last_name=None, sex,
        # last_name=None, sex=None,
        last_name=None, sex='M',
    ):

  I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to run the test a few times and if the ``last_name`` is not ``'doe'``, the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: doe

    AssertionError:
        {'first_name': A, 'last_name': 'doe', 'sex': Y, 'age': X}
     != {'first_name': A, 'last_name': Z, 'sex': Y, 'age': X}

  because the ``last_name`` :ref:`value<test_values_of_a_dictionary>` is different between the two :ref:`dictionaries<what is a dictionary?>`. It still shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.person'
                    has no attribute 'say_hello'

* I use the ``last_name`` input parameter in the :ref:`return statement<the return statement>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 13-14

    def factory(
            first_name, year_of_birth,
            # last_name,
            # last_name=None,
            # last_name=None, sex,
            # last_name=None, sex=None,
            last_name=None, sex='M',
        ):
        # return None
        return {
            # 'first_name': 'john',
            'first_name': first_name,
            # 'last_name': 'doe',
            'last_name': last_name,
            # 'sex': 'M',
            'sex': sex,
            # 'age': 55,
            # 'age': year_of_birth,
            'age': (
                datetime.datetime.today().year
              - year_of_birth
            ),
        }

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: doe

    AssertionError:
        {'first_name': Z, 'last_name': None,
         'sex': Y, 'age': X}
     != {'first_name': Z, 'last_name': 'doe',
         'sex': Y, 'age': X}

  because the :ref:`assertion<what is an assertion?>` expects ``'doe'`` as the :ref:`value<test_values_of_a_dictionary>` of ``last_name`` and the :ref:`function<what is a function?>` returns :ref:`None<what is None?>` which is its default value

* I change the default value for ``last_name`` to match the expectation

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 7-8

    def factory(
            first_name, year_of_birth,
            # last_name,
            # last_name=None,
            # last_name=None, sex,
            # last_name=None, sex=None,
            # last_name=None, sex='M',
            last_name='doe', sex='M',
        ):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.person'
                    has no attribute 'say_hello'

  because I do not have a definition for ``say_hello``

* I add ``say_hello``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

    import datetime


    say_hello


    # factory
    # factory = None
    # def factory():
    # def factory(first_name):
    # def factory(first_name, year_of_birth):
    def factory(

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'say_hello' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import datetime


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
    :emphasize-lines: 5-7

    import datetime


    # say_hello
    # say_hello = None
    def say_hello():
        return None


    # factory

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: say_hello() takes 0 positional arguments
               but 1 was given

  because the :ref:`function definition<how to make a function>` for ``say_hello`` does not allow calling it with inputs (the parentheses are empty) and the test sends input.

* I add a name to the :ref:`function definition<how to make a function>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-4

    # say_hello
    # say_hello = None
    # def say_hello():
    def say_hello(argument):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'Hello, my name is Z Y and I am Z'

  because the test expects a string_ and the ``say_hello`` :ref:`function<what is a function?>` returns :ref:`None<what is None?>`

* I copy (:kbd:`ctrl/command+c`) the string_ from the terminal_ and paste it (:kbd:`ctrl/command+v`) to replace the :ref:`return statement<the return statement>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5-6

    # say_hello
    # say_hello = None
    # def say_hello():
    def say_hello(argument):
        # return None
        return 'Hello, my name is jade doe and I am 66'


    # factory

  I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to run the test a few times, and the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'Hello, my name is Z Y and I am X'
     != 'Hello, my name is A B and I am C'

  the names and ages change

* I return the input to compare it with what the test expects

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 6

    # say_hello
    # say_hello = None
    # def say_hello():
    def say_hello(argument):
        # return None
        return argument
        return 'Hello, my name is jade doe and I am 66'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: X Z A

    AssertionError:
        {'first_name': A, 'last_name': Z, 'sex': Y, 'age': X}
    != 'Hello, my name is A Z and I am X'

  the test sends a :ref:`dictionary<what is a dictionary?>` as input and expects a string_ as output, and the string_ uses the :ref:`values<test_values_of_a_dictionary>` of the ``first_name``, ``last_name`` and ``age`` :ref:`keys<test_keys_of_a_dictionary>` from the :ref:`dictionary<what is a dictionary?>` it receives

* I return an :ref:`f-string<what is string interpolation?>` with the :ref:`values<test_values_of_a_dictionary>` of the ``first_name``, ``last_name`` and ``age`` :ref:`keys<test_keys_of_a_dictionary>` from the dictionary

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 6-10
    :emphasize-text: get

    # say_hello
    # say_hello = None
    # def say_hello():
    def say_hello(argument):
        # return None
        return (
            f'Hello, my name is {argument.get("first_name")}'
            f' {argument.get("last_name")}'
            f' and I am {argument.get("age")}'
        )
        return argument
        return 'Hello, my name is jade doe and I am 66'

  the test passes. Okay!

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use the ``Rename Symbol`` feature of the `Integrated Development Environment (IDE)`_ to change ``argument`` to make it clearer

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4, 7-9
    :emphasize-text: a_dictionary

    # say_hello
    # say_hello = None
    # def say_hello():
    def say_hello(a_dictionary):
        # return None
        return (
            f'Hello, my name is {a_dictionary.get("first_name")}'
            f' {a_dictionary.get("last_name")}'
            f' and I am {a_dictionary.get("age")}'
        )
        return a_dictionary
        return 'Hello, my name is jade doe and I am 66'

* I remove the commented lines and other `return statements`_

  .. code-block:: python
    :linenos:

    import datetime


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
            'age': (
                datetime.datetime.today().year
              - year_of_birth
            ),
        }

  This :ref:`factory function<test_factory_w_keyword_arguments>` only has two parameters with :ref:`default values<test_optional_arguments>` (``last_name`` and ``sex``)

  .. code-block:: python
    :emphasize-text: None

    def factory(
            first_name, year_of_birth,
            last_name='doe', sex='M',
        ):

  the first solution had three parameters with :ref:`default values<test_optional_arguments>` (``last_name``, ``sex`` and ``year_of_birth``)

  .. code-block:: python
    :emphasize-text: None

    def factory(
            first_name, last_name='doe',
            sex='M', year_of_birth=None,
        ):

  I can learn new things from repetition.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am \
    'refactor factory and say_hello functions'

  the terminal_ shows a summary of the changes then goes back to the command line.

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

I ran tests to make

* a :ref:`function<what is a function?>` that takes in :ref:`keyword arguments<test_keyword_arguments>` as input, has :ref:`default values<test_optional_arguments>` for some of them, performs an action based on an input and returns a :ref:`dictionary<what is a dictionary?>` as output

* a :ref:`function<what is a function?>` that takes in a :ref:`dictionary<what is a dictionary?>` and returns a string_ as output with :ref:`values<test_values_of_a_dictionary>` of :ref:`keys<test_keys_of_a_dictionary>` from the :ref:`dictionary<what is a dictionary?>`

I also saw these :ref:`Exceptions<errors>`

* :ref:`AssertionError<what causes AssertionError?>`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError<what causes AttributeError?>`
* :ref:`TypeError<what causes TypeError?>`
* SyntaxError_

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a person: tests and solution>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python test driven development environment manually<how to make a Python test driven development environment manually>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`how to make dictionaries with functions<how to make a person>`

:ref:`Would you like to see another way to make a person?<everything is an object>`

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