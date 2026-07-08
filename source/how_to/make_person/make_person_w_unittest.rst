.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

#################################################################################
test person with unittest
#################################################################################

----

I want to use the :ref:`unittest library<another way to write tests>` in the :ref:`person<how to make a person with a class>` project.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_unittest.py
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
add TestPerson class
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`class<what is a class?>` named ``TestPerson`` to ``test_person.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 4, 6-7

  import src.person


  class TestPerson(object):

      def test_failure(self):
          self.assertEqual(False, True)


  def test_joe():

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: 'TestPerson' object
                  has no attribute 'assertEqual'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`unittest.TestCase<test_attributes_and_methods_of_unittest_testcase>` as the parent :ref:`class<what is a class?>` of ``TestPerson``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import src.person


    # class TestPerson(object):
    class TestPerson(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'unittest' is not defined.
               Did you forget to import 'unittest'?

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import unittest
    import src.person


    # class TestPerson(object):
    class TestPerson(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False != True

* I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    # class TestPerson(object):
    class TestPerson(unittest.TestCase):

        def test_failure(self):
            # self.assertEqual(False, True)
            self.assertEqual(True, True)


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

    import unittest
    import src.person


    class TestPerson(unittest.TestCase):

        def test_failure(self):
            self.assertEqual(True, True)


    def test_joe():

* I open a new terminal_ then make sure I am in the ``person`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd person

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add TestPerson class'

----

*********************************************************************************
test_joe with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_joe` to make it a :ref:`method<what is a method?>` of the :ref:`TestPerson class<add TestPerson class>` and replace ``test_failure``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-7, 9-19, 21-31, 33-38, 40-41

    class TestPerson(unittest.TestCase):

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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestPerson.test_joe() takes
               0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_joe`

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 1-2

      # def test_joe():
      def test_joe(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the :ref:`factory function<test person factory>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 19

        # def test_joe():
        def test_joe(self):
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
            self.assertNotEqual(reality, my_expectation)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'joe, blow, M, 1996'
                 == 'joe, blow, M, 1996'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_Equal>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2-3

            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

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

  the test passes.

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the :ref:`say_hello function<test say_hello function>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 12

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
            self.assertNotEqual(reality, my_expectation)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Hello, my name is joe blow and I am 30.'
                 == 'Hello, my name is joe blow and I am 30.'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2-3

            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            joe = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = joe.say_hello()

  the test passes.

* I add a :ref:`call<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` for the :ref:`say_hello method<test say_hello method>` of the :ref:`Person class<test Person class>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 3

            reality = joe.say_hello()
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    def test_jane():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Hello, my name is joe blow and I am 30.'
                 == 'Hello, my name is joe blow and I am 30.'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 3-4

            reality = joe.say_hello()
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_jane():

  the test passes.

* I remove the commented lines from :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 5

    class TestPerson(unittest.TestCase):

        def test_joe(self):
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
            self.assertEqual(reality, my_expectation)

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
            self.assertEqual(reality, my_expectation)

            joe = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = joe.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_jane():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'move test_joe to TestPerson'

----

*********************************************************************************
test_jane with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_jane` to make it a :ref:`method<what is a method?>` of the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 5-9, 11-21, 23-33, 35-40, 42-43

            reality = joe.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestPerson.test_jane() takes
               0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_jane`

.. code-block:: python
  :lineno-start: 46
  :emphasize-lines: 5-6

            reality = joe.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

        # def test_jane():
        def test_jane(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 19, 32, 43

        # def test_jane():
        def test_jane(self):
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
            self.assertNotEqual(reality, my_expectation)

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
            self.assertNotEqual(reality, my_expectation)

            jane = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = jane.say_hello()
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    def test_john():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'jane, doe, F, 1991'
                 == 'jane, doe, F, 1991'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_Equal>` for the :ref:`factory function<test person factory>`, in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2-3

            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

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
            self.assertNotEqual(reality, my_expectation)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Hello, my name is jane doe and I am 35.'
                 == 'Hello, my name is jane doe and I am 35.'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`say_hello function<test say_hello function>`, in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 2-3

            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            jane = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = jane.say_hello()

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Hello, my name is jane doe and I am 35.'
                 == 'Hello, my name is jane doe and I am 35.'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`say hello method<test say_hello method>` of the :ref:`Person class<test Person class>`, in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 3-4

            reality = jane.say_hello()
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_john():

  the test passes.

* I remove the commented lines from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 48

            self.assertEqual(reality, my_expectation)

        def test_jane(self):
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
            self.assertEqual(reality, my_expectation)

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
            self.assertEqual(reality, my_expectation)

            jane = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = jane.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_john():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'move test_jane to TestPerson'

----

*********************************************************************************
test_john with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_john` to make it a :ref:`method<what is a method?>` of the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 5-9, 11-21, 23-33, 35-40, 42-43

            reality = jane.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestPerson.test_john() takes
               0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_john`

.. code-block:: python
  :lineno-start: 46
  :emphasize-lines: 5-6

          reality = jane.say_hello()
          assert reality == my_expectation
          self.assertEqual(reality, my_expectation)

      # def test_john():
      def test_john(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 19, 32, 43

        # def test_john():
        def test_john(self):
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
            self.assertNotEqual(reality, my_expectation)

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
            self.assertNotEqual(reality, my_expectation)

            john = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = john.say_hello()
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    def test_mary():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'john, smith, M, 1580'
                 == 'john, smith, M, 1580'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_Equal>` for the :ref:`factory function<test person factory>`, in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 2-3

            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

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
            self.assertNotEqual(reality, my_expectation)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Hello, my name is john smith and I am 446.'
                 == 'Hello, my name is john smith and I am 446.'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`say_hello function<test say_hello function>`, in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 2-3

            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            john = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = john.say_hello()

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Hello, my name is john smith and I am 446.'
                 == 'Hello, my name is john smith and I am 446.'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`say hello method<test say_hello method>` of the :ref:`Person class<test Person class>`, in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 3-4

            reality = john.say_hello()
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_mary():

  the test passes.

* I remove the commented lines from :ref:`test_john`

  .. code-block:: python
    :lineno-start: 91

            self.assertEqual(reality, my_expectation)

        def test_john(self):
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
            self.assertEqual(reality, my_expectation)

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
            self.assertEqual(reality, my_expectation)

            john = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = john.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    def test_mary():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'move test_john to TestPerson'

----

*********************************************************************************
test_mary with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I move :ref:`test_mary` to make it a :ref:`method<what is a method?>` of the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 132
    :emphasize-lines: 5-9, 11-21, 23-33, 35-40, 42-43

            reality = john.say_hello()
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

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


    def test_attributes_and_methods_of_person_class():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestPerson.test_mary() takes
               0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_mary`

.. code-block:: python
  :lineno-start: 132
  :emphasize-lines: 5-6

          reality = john.say_hello()
          assert reality == my_expectation
          self.assertEqual(reality, my_expectation)

      # def test_mary():
      def test_mary(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`calls<how to call a function with input>` to the :ref:`assertNotEqual method<test_assert_not_equal>` in :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 19, 32, 43

        # def test_mary():
        def test_mary(self):
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
            self.assertNotEqual(reality, my_expectation)

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
            self.assertNotEqual(reality, my_expectation)

            mary = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = mary.say_hello()
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)


    def test_attributes_and_methods_of_person_class():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

     AssertionError: 'mary, public, F, 2000'
                  == 'mary, public, F, 2000

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_Equal>` for the :ref:`factory function<test person factory>`, in :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 2-3

            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

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
            self.assertNotEqual(reality, my_expectation)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Hello, my name is mary public and I am 26.'
                 == 'Hello, my name is mary public and I am 26.'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`say_hello function<test say_hello function>`, in :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 167
    :emphasize-lines: 2-3

            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            mary = src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

            reality = mary.say_hello()

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Hello, my name is mary public and I am 26.'
                 == 'Hello, my name is mary public and I am 26.'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_equal>` for the :ref:`say hello method<test say_hello method>` of the :ref:`Person class<test Person class>`, in :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 178
    :emphasize-lines: 3-4

            reality = mary.say_hello()
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)


    def test_attributes_and_methods_of_person_class():

  the test passes.

* I remove the commented lines from :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 134

        self.assertEqual(reality, my_expectation)

    def test_mary(self):
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
        self.assertEqual(reality, my_expectation)

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
        self.assertEqual(reality, my_expectation)

        mary = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = mary.say_hello()
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)


def test_attributes_and_methods_of_person_class():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'move test_mary to TestPerson'

----




----

*********************************************************************************
close the project
*********************************************************************************

* I close ``person.py`` and ``test_person.py``
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

* I ran tests to write a :ref:`class<what is a class?>` that makes a person when given ``first_name``, ``last_name``, ``sex`` and ``year_of_birth`` and has a :ref:`method<what is a method?>` so I do not have to pass the same values every time I want to do something with a person.

* I saw the following :ref:`Exceptions<errors>`

  - :ref:`AssertionError<what causes AssertionError?>`
  - :ref:`NameError<test_catching_name_error_in_tests>`
  - :ref:`TypeError<what causes TypeError?>`
  - :ref:`AttributeError<what causes AttributeError?>`
  - SyntaxError_

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

You know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what an assertion is<what is an assertion?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`
* :ref:`how to make functions that take input<functions that take input>`
* :ref:`what causes TypeError?`
* :ref:`how to place values in strings<telephone>`
* :ref:`how to make a person say hello with f-strings<how to make a person with f-strings>`
* :ref:`how to separate tests from solutions<separate and equal functions>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to make a person with a class<how to make a person with a class>`

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