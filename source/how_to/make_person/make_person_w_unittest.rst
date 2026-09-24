.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): test person with unittest — move the person project's tests onto unittest.TestCase, then move helper assert functions onto TestPerson as methods. Open person; uv run pytest-watcher . --now (6 passed). Add class TestPerson(object) with test_failure → AttributeError: 'TestPerson' object has no attribute 'assertEqual'. Parent unittest.TestCase → NameError name 'unittest' is not defined (pytest: Did you forget to import 'unittest'?); import unittest → AssertionError: False != True then green with assertEqual(True, True). For test_joe, test_jane, test_john, test_mary: move into TestPerson → TypeError takes 0 positional arguments but 1 was given; @staticmethod then later self. For test_dir_person_class and test_dir_person_instance: add self; assert_equal to self.assertNotEqual then self.assertEqual. Move assert_person_can_say_hello, assert_say_hello_works, assert_person_factory_works onto TestPerson → TypeError missing self / got multiple values for argument 'first_name'; add self; self.assertNotEqual → AssertionError e.g. 'Hello, my name is joe blow and I am 30.' == same / 'joe, blow, M, 1996' == same; switch to self.assertEqual; drop unused assert_equal; git commit. Ends with TestPerson + 3 helper methods + 6 tests + # Exceptions seen AssertionError NameError TypeError AttributeError SyntaxError. Review: unittest.TestCase methods or bare assert; tests still repeat the same three calls per person. What is next: test telephone with unittest.
  :keywords: Jacob Itegboje, Pumping Python, test person with unittest, person unittest, TestPerson, unittest.TestCase, import unittest, AttributeError has no attribute assertEqual, NameError name 'unittest' is not defined, Did you forget to import unittest, AssertionError False != True, TypeError takes 0 positional arguments but 1 was given, TypeError missing self, got multiple values for argument first_name, self first argument method, staticmethod, assertNotEqual, assertEqual, assert_person_factory_works, assert_say_hello_works, assert_person_can_say_hello, joe blow M 1996, Hello my name is joe blow and I am 30, jane doe, john smith, mary public, test_dir_person_class, test_dir_person_instance, dir(Person), uv run pytest-watcher . --now, red green refactor, remove the commented lines, git commit -am, same three tests per person, another way to write tests, test_person_w_unittest

.. include:: ../../links.rst

#################################################################################
test person with unittest
#################################################################################

----

I want to use the :ref:`unittest library<another way to write tests>` in the :ref:`person<how to make a person with an object>` project.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_unittest.py
  :caption: person/tests/test_person.py
  :language: python
  :linenos:
  :lines: 1-22

.. literalinclude:: ../../code/person/tests/test_person_w_unittest.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 24
  :lines: 24-39

.. literalinclude:: ../../code/person/tests/test_person_w_unittest.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 41
  :lines: 41-57

.. literalinclude:: ../../code/person/tests/test_person_w_unittest.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 59
  :lines: 59-83

.. literalinclude:: ../../code/person/tests/test_person_w_unittest.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 85
  :lines: 85-109

.. literalinclude:: ../../code/person/tests/test_person_w_unittest.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 111
  :lines: 111-135

.. literalinclude:: ../../code/person/tests/test_person_w_unittest.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 137
  :lines: 137-161

.. literalinclude:: ../../code/person/tests/test_person_w_unittest.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 163
  :lines: 163-178

.. literalinclude:: ../../code/person/tests/test_person_w_unittest.py
  :caption: person/tests/test_person.py
  :language: python
  :lineno-start: 180
  :lines: 180-

-----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd person

* I open ``test_person.py`` from the ``tests`` folder_

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    tests/test_person.py ......                         [100%]

    =================== 6 passed in A.BCs ====================

----

*********************************************************************************
add TestPerson class
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`class<everything is an object>` named ``TestPerson`` to ``test_person.py``

.. code-block:: python
  :lineno-start: 45
  :emphasize-lines: 19, 21-22

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

* I add :ref:`unittest.TestCase<test_dir_unittest_testcase>` as the parent :ref:`class<everything is an object>` of ``TestPerson``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 1-2

    # class TestPerson(object):
    class TestPerson(unittest.TestCase):

        def test_failure(self):
            self.assertEqual(False, True)

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell

    NameError: name 'unittest' is not defined.
               Did you forget to import 'unittest'?

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import src.person
    import unittest


    def assert_equal(left, right):
        assert left == right

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False != True

* I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 64
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
    :lineno-start: 46

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
move test_joe to TestPerson
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I remove :ref:`test_failure` from the :ref:`TestPerson class<add TestPerson class>`

* I move :ref:`test_joe` to make it a :ref:`method<what is a method?>` of the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 3-7, 9-14, 16-20, 22-27

    class TestPerson(unittest.TestCase):

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
                year_of_birth=year_of_birth
            )


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

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_joe` because ...

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 3-4

    class TestPerson(unittest.TestCase):

        @staticmethod
        def test_joe():
            first_name = 'joe'

  the test is green again.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'move test_joe to TestPerson'

----

*********************************************************************************
move test_jane to TestPerson
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_jane` to make it a :ref:`method<what is a method?>` of the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 8-12, 14-19, 21-25, 27-32

            assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth
            )

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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestPerson.test_jane() takes
               0 positional arguments but 1 was given

  because ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_jane` since it also does not use anything in the :ref:`TestPerson class<add TestPerson class>`, yet

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 8-9

            assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth
            )

        @staticmethod
        def test_jane():

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'move test_jane to TestPerson'

----

*********************************************************************************
move test_john to TestPerson
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_john` to make it a :ref:`method<what is a method?>` of the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 8-12, 14-19, 21-25, 27-32

            assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

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

* I also add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_john`

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 8-9

            assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

        @staticmethod
        def test_john():

  green again.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'move test_john to TestPerson'

----

*********************************************************************************
move test_mary to TestPerson
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_mary` to make it a :ref:`method<what is a method?>` of the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 8-12, 14-19, 21-25, 27-32

            assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

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


    def test_dir_person_class():

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

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_mary` because I can use it when a :ref:`method<what is a method?>` does not use anything in the :ref:`class<everything is an object>` it belongs to

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 8-9

            assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

        @staticmethod
        def test_mary():

  green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'move test_mary to TestPerson'

----

*********************************************************************************
test_dir_person_class with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_dir_person_class` to make it a :ref:`method<what is a method?>` of the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 167
    :emphasize-lines: 8-12

            assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

        def test_dir_person_class():
            assert_equal(
                dir(src.person.Person),
                [
                    '__class__', '__delattr__', '__dict__',


  .. code-block:: python
    :lineno-start: 187
    :emphasize-lines: 1-3

                    '__subclasshook__', '__weakref__', 'say_hello'
                ]
            )


    def test_dir_person_instance():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestPerson.test_dir_person_class()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_dir_person_class`

.. code-block:: python
  :lineno-start: 167
  :emphasize-lines: 8-9

          assert_person_can_say_hello(
              first_name=first_name,
              last_name=last_name,
              sex=sex,
              year_of_birth=year_of_birth,
          )

      # def test_dir_person_class():
      def test_dir_person_class(self):
          assert_equal(
              dir(src.person.Person),
              [
                  '__class__', '__delattr__', '__dict__',

green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` in :ref:`test_dir_person_class`

  .. code-block:: python
    :lineno-start: 174
    :emphasize-lines: 3-4

        # def test_dir_person_class():
        def test_dir_person_class(self):
            # assert_equal(
            self.assertNotEqual(
                dir(src.person.Person),
                [
                    '__class__', '__delattr__', '__dict__',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`.

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_Equal>` in :ref:`test_dir_person_class`

  .. code-block:: python
    :lineno-start: 174
    :emphasize-lines: 4-5

        # def test_dir_person_class():
        def test_dir_person_class(self):
            # assert_equal(
            # self.assertNotEqual(
            self.assertEqual(
                dir(src.person.Person),
                [
                    '__class__', '__delattr__', '__dict__',

  the test passes.

* I remove the commented lines from :ref:`test_dir_person_class`

  .. code-block:: python
    :lineno-start: 167

            assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

        def test_dir_person_class(self):
            self.assertEqual(
                dir(src.person.Person),
                [
                    '__class__', '__delattr__', '__dict__',

  .. code-block:: python
    :lineno-start: 187

                    '__subclasshook__', '__weakref__', 'say_hello'
                ]
            )


    def test_dir_person_instance():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'move test_dir_person_class to TestPerson'

----

*********************************************************************************
test_dir_person_instance with unittest
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I move :ref:`test_dir_person_instance` to make it a :ref:`method<what is a method?>` of the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 187
    :emphasize-lines: 5-16

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

  .. code-block:: python
    :lineno-start: 212
    :emphasize-lines: 1-3

                    'last_name', 'say_hello', 'sex', 'year_of_birth',
                ]
            )


    # Exceptions seen


  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestPerson.test_dir_person_instance()
        takes 0 positional arguments but 1 was given

  because ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``self`` to the parentheses of :ref:`test_dir_person_instance`

.. code-block:: python
  :lineno-start: 187
  :emphasize-lines: 5-6

                  '__subclasshook__', '__weakref__', 'say_hello'
              ]
          )

      # def test_dir_person_instance():
      def test_dir_person_instance(self):
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


the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` in :ref:`test_dir_person_instance`

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 3-4

        # def test_dir_person_instance():
        def test_dir_person_instance(self):
            # assert_equal(
            self.assertNotEqual(
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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`.

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_Equal>` in :ref:`test_dir_person_instance`

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 4-5

        # def test_dir_person_instance():
        def test_dir_person_instance(self):
            # assert_equal(
            # self.assertNotEqual(
            self.assertEqual(
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

  the test passes.

* I remove the commented lines from :ref:`test_dir_person_instance`

  .. code-block:: python
    :lineno-start: 187

                    '__subclasshook__', '__weakref__', 'say_hello'
                ]
            )

        def test_dir_person_instance(self):
            self.assertEqual(
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

  .. code-block:: python
    :lineno-start: 212

                    'last_name', 'say_hello', 'sex', 'year_of_birth',
                ]
            )


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError
    # SyntaxError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'move test_dir_person_instance to TestPerson'

----

*********************************************************************************
move assert_person_can_say_hello to TestPerson
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a copy of the :ref:`assert_person_can_say_hello function<extract assert_person_can_say_hello function>` to make it a :ref:`method<what is a method?>` of the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 3-19

    class TestPerson(unittest.TestCase):

        def assert_person_can_say_hello(
                first_name, last_name,
                sex, year_of_birth,
            ):
            assert_equal(
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

        @staticmethod
        def test_joe():

* I change the :ref:`call<how to call a function with input>` from the :ref:`assert_person_can_say_hello function<extract assert_person_can_say_hello function>` to the :ref:`assert_person_can_say_hello method<move assert_person_can_say_hello to TestPerson>` of the :ref:`TestPerson class<add TestPerson class>` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 84

        @staticmethod
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

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 7-8

            assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            # assert_person_can_say_hello(
            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth
            )

        @staticmethod
        def test_jane():

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'self' is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``self`` to the parentheses of :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2-3

        @staticmethod
        # def test_joe():
        def test_joe(self):
            first_name = 'joe'
            last_name = 'blow'
            sex = 'M'
            year_of_birth = 1996

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestPerson.test_joe() missing
               1 required positional argument: 'self'

* I comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>` from :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 1

        # @staticmethod
        # def test_joe():
        def test_joe(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestPerson.assert_person_can_say_hello()
               got multiple values for argument 'first_name'

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add ``self`` to the parentheses of the :ref:`assert_person_can_say_hello method of the TestPerson class<move assert_person_can_say_hello to TestPerson>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 4-5

    class TestPerson(unittest.TestCase):

        def assert_person_can_say_hello(
                # first_name, last_name,
                self, first_name, last_name,
                sex, year_of_birth,
            ):

  the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` in the :ref:`assert_person_can_say_hello method of the TestPerson class<move assert_person_can_say_hello to TestPerson>`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 6-7

        def assert_person_can_say_hello(
                # first_name, last_name,
                self,first_name, last_name,
                sex, year_of_birth,
            ):
            # assert_equal(
            self.assertNotEqual(
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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Hello, my name is joe blow and I am 30.'
                 == 'Hello, my name is joe blow and I am 30.'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_Equal>` in the :ref:`assert_person_can_say_hello method of the TestPerson class<move assert_person_can_say_hello to TestPerson>`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 7-8

        def assert_person_can_say_hello(
                # first_name, last_name,
                self,first_name, last_name,
                sex, year_of_birth,
            ):
            # assert_equal(
            # self.assertNotEqual(
            self.assertEqual(
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

  the test is green again.

* I remove the commented lines from the :ref:`assert_person_can_say_hello method of the TestPerson class<move assert_person_can_say_hello to TestPerson>`

  .. code-block:: python
    :lineno-start: 64

    class TestPerson(unittest.TestCase):

        def assert_person_can_say_hello(
                self,first_name, last_name,
                sex, year_of_birth,
            ):
            self.assertEqual(
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

        # @staticmethod
        # def test_joe():
        def test_joe(self):

* I change the :ref:`call<how to call a function with input>` from the :ref:`assert_person_can_say_hello function<extract assert_person_can_say_hello function>` to the :ref:`assert_person_can_say_hello method<move assert_person_can_say_hello to TestPerson>` of the :ref:`TestPerson class<add TestPerson class>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 113

        @staticmethod
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

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 7-8

            assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            # assert_person_can_say_hello(
            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

        @staticmethod
        def test_john():

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses of :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 2-3

        @staticmethod
        # def test_jane():
        def test_jane(self):
            first_name = 'jane'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestPerson.test_jane() missing
               1 required positional argument: 'self'

* I comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>` from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 1

        # @staticmethod
        # def test_jane():
        def test_jane(self):
            first_name = 'jane'

  the test is green again.

* I change the :ref:`call<how to call a function with input>` from the :ref:`assert_person_can_say_hello function<extract assert_person_can_say_hello function>` to the :ref:`assert_person_can_say_hello method<move assert_person_can_say_hello to TestPerson>` of the :ref:`TestPerson class<add TestPerson class>` in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 142

        @staticmethod
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

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 7-8

            assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            # assert_person_can_say_hello(
            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

        @staticmethod
        def test_mary():

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses of :ref:`test_john`

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 2-3

        @staticmethod
        # def test_john():
        def test_john(self):
            first_name = 'john'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestPerson.test_john() missing
               1 required positional argument: 'self'

* I comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>` from :ref:`test_john`

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 1

        # @staticmethod
        # def test_john():
        def test_john(self):
            first_name = 'john'

  the test is green again.

* I change the :ref:`call<how to call a function with input>` from the :ref:`assert_person_can_say_hello function<extract assert_person_can_say_hello function>` to the :ref:`assert_person_can_say_hello method<move assert_person_can_say_hello to TestPerson>` of the :ref:`TestPerson class<add TestPerson class>` in :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 171

        @staticmethod
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

  .. code-block:: python
    :lineno-start: 185
    :emphasize-lines: 7-8

            assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            # assert_person_can_say_hello(
            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

        def test_dir_person_class(self):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses of :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 171
    :emphasize-lines: 2-3

        @staticmethod
        # def test_mary():
        def test_mary(self):
            first_name = 'mary'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestPerson.test_mary() missing
               1 required positional argument: 'self'

* I comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>` from :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 171
    :emphasize-lines: 1

        # @staticmethod
        # def test_mary():
        def test_mary(self):
            first_name = 'mary'

  green again.

* I remove the :ref:`assert_person_can_say_hello function<extract assert_person_can_say_hello function>` since it is now a repetition

  .. code-block:: python
    :linenos:

    import src.person
    import unittest


    def assert_equal(left, right):
        assert left == right


    def assert_say_hello_works(
            first_name, last_name,
            year_of_birth,
        ):

  all the tests are still green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'move assert_person_can_say_hello to TestPerson'

----

*********************************************************************************
move assert_say_hello_works to TestPerson
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a copy of the :ref:`assert_say_hello_works function<extract assert_say_hello_works function>` to make it a :ref:`method<what is a method?>` of the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 3-18

    class TestPerson(unittest.TestCase):

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

        def assert_person_can_say_hello(
                self, first_name, last_name,
                sex, year_of_birth,
            ):

* I change the :ref:`call<how to call a function with input>` from the :ref:`assert_say_hello_works function<extract assert_say_hello_works function>` to the :ref:`assert_say_hello_works method<move assert_say_hello_works to TestPerson>` of the :ref:`TestPerson class<add TestPerson class>` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 16-17

        # @staticmethod
        # def test_joe():
        def test_joe(self):
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

            # assert_say_hello_works(
            self.assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestPerson.assert_say_hello_works()
               got multiple values for argument 'first_name'

  because ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``self`` to the parentheses of the :ref:`assert_say_hello_works method of the TestPerson class<move assert_say_hello_works to TestPerson>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4-5

    class TestPerson(unittest.TestCase):

        def assert_say_hello_works(
                # first_name, last_name,
                self,first_name, last_name,
                year_of_birth,
            ):

  the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line from the :ref:`assert_say_hello_works method of the TestPerson class<move assert_say_hello_works to TestPerson>`

  .. code-block:: python
    :lineno-start: 45

    class TestPerson(unittest.TestCase):

        def assert_say_hello_works(
                self,first_name, last_name,
                year_of_birth,
            ):

* I change the :ref:`call<how to call a function with input>` from the :ref:`assert_say_hello_works function<extract assert_say_hello_works function>` to the :ref:`assert_say_hello_works method<move assert_say_hello_works to TestPerson>` of the :ref:`TestPerson class<add TestPerson class>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 16-17

        # @staticmethod
        # def test_jane():
        def test_jane(self):
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

            # assert_say_hello_works(
            self.assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

  the test is still green.

* I change the :ref:`call<how to call a function with input>` from the :ref:`assert_say_hello_works function<extract assert_say_hello_works function>` to the :ref:`assert_say_hello_works method<move assert_say_hello_works to TestPerson>` of the :ref:`TestPerson class<add TestPerson class>` in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 16-17

        # @staticmethod
        # def test_john():
        def test_john(self):
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

            # assert_say_hello_works(
            self.assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

  still green.

* I change the :ref:`call<how to call a function with input>` from the :ref:`assert_say_hello_works function<extract assert_say_hello_works function>` to the :ref:`assert_say_hello_works method<move assert_say_hello_works to TestPerson>` of the :ref:`TestPerson class<add TestPerson class>` in :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 172
    :emphasize-lines: 16-17

        # @staticmethod
        # def test_mary():
        def test_mary(self):
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

            # assert_say_hello_works(
            self.assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

  green.

* I change the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` in the :ref:`assert_say_hello_works method of the TestPerson class<move assert_say_hello_works to TestPerson>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 5-6

        def assert_say_hello_works(
                self, first_name, last_name,
                year_of_birth,
            ):
            # assert_equal(
            self.assertNotEqual(
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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    FAILED ...test_jane - AssertionError:
        'Hello, my name is jane doe and I am 35.'
     == 'Hello, my name is jane doe and I am 35.'
    FAILED ...test_joe - AssertionError:
        'Hello, my name is joe blow and I am 30.'
     == 'Hello, my name is joe blow and I am 30.'
    FAILED ...test_john - AssertionError:
        'Hello, my name is john smith and I am 446.'
     == 'Hello, my name is john smith and I am 446.'
    FAILED ...test_mary - AssertionError:
        'Hello, my name is mary public and I am 26.'
     == 'Hello, my name is mary public and I am 26.'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_Equal>` in the :ref:`assert_say_hello_works method of the TestPerson class<move assert_say_hello_works to TestPerson>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 6-7

        def assert_say_hello_works(
                self, first_name, last_name,
                year_of_birth,
            ):
            # assert_equal(
            # self.assertNotEqual(
            self.assertEqual(
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

  the test is green again.

* I remove the commented lines from the :ref:`assert_say_hello_works method of the TestPerson class<move assert_say_hello_works to TestPerson>`

  .. code-block:: python
    :lineno-start: 47

        def assert_say_hello_works(
                self, first_name, last_name,
                year_of_birth,
            ):
            self.assertEqual(
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

        def assert_person_can_say_hello(

* I remove the :ref:`assert_say_hello_works function<extract assert_say_hello_works function>` since it is now a repetition

  .. code-block:: python
    :linenos:

    import src.person
    import unittest


    def assert_equal(left, right):
        assert left == right


    def assert_person_factory_works(
            first_name, last_name,
            sex, year_of_birth
        ):

  the tests are still green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'move assert_say_hello_works to TestPerson'

----

*********************************************************************************
move assert_person_factory_works to TestPerson
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a copy of the :ref:`assert_person_factory_works function<extract assert_person_factory_works function>` to make it a :ref:`method<what is a method?>` of the :ref:`TestPerson class<add TestPerson class>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3-18

    class TestPerson(unittest.TestCase):

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

        def assert_say_hello_works(
                self, first_name, last_name,
                year_of_birth,
            ):

* I change the :ref:`call<how to call a function with input>` from the :ref:`assert_person_factory_works function<extract assert_person_factory_works function>` to the :ref:`assert_person_factory_works method<move assert_person_factory_works to TestPerson>` of the :ref:`TestPerson class<add TestPerson class>` in :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 9-10

        # @staticmethod
        # def test_joe():
        def test_joe(self):
            first_name = 'joe'
            last_name = 'blow'
            sex = 'M'
            year_of_birth = 1996

            # assert_person_factory_works(
            self.assert_person_factory_works(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth
            )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestPerson.assert_person_factory_works()
               got multiple values for argument 'first_name'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``self`` to the parentheses of the :ref:`assert_person_factory_works method of the TestPerson class<move assert_person_factory_works to TestPerson>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4-5

    class TestPerson(unittest.TestCase):

        def assert_person_factory_works(
                # first_name, last_name,
                self, first_name, last_name,
                sex, year_of_birth
            ):

  green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line from the :ref:`assert_person_factory_works method of the TestPerson class<move assert_person_factory_works to TestPerson>`

  .. code-block:: python
    :lineno-start: 27

    class TestPerson(unittest.TestCase):

        def assert_person_factory_works(
                self, first_name, last_name,
                sex, year_of_birth
            ):

* I remove the commented lines from :ref:`test_joe`

  .. code-block:: python
    :lineno-start: 63

        def assert_person_can_say_hello(
                self,first_name, last_name,
                sex, year_of_birth,
            ):
            self.assertEqual(
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

  .. code-block:: python
    :lineno-start: 81

        def test_joe(self):
            first_name = 'joe'
            last_name = 'blow'
            sex = 'M'
            year_of_birth = 1996

            self.assert_person_factory_works(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth
            )

  .. code-block:: python
    :lineno-start: 94

            self.assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth
            )

        # @staticmethod
        # def test_jane():
        def test_jane(self):

* I change the :ref:`call<how to call a function with input>` from the :ref:`assert_person_factory_works function<extract assert_person_factory_works function>` to the :ref:`assert_person_factory_works method<move assert_person_factory_works to TestPerson>` of the :ref:`TestPerson class<add TestPerson class>` in :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 9-10

        # @staticmethod
        # def test_jane():
        def test_jane(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = 1991

            # assert_person_factory_works(
            self.assert_person_factory_works(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

  still green.

* I remove the commented lines from :ref:`test_jane`

  .. code-block:: python
    :lineno-start: 100

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth
            )

        def test_jane(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = 1991

            self.assert_person_factory_works(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

  .. code-block:: python
    :lineno-start: 120

            self.assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

        # @staticmethod
        # def test_john():
        def test_john(self):

* I change the :ref:`call<how to call a function with input>` from the :ref:`assert_person_factory_works function<extract assert_person_factory_works function>` to the :ref:`assert_person_factory_works method<move assert_person_factory_works to TestPerson>` of the :ref:`TestPerson class<add TestPerson class>` in :ref:`test_john`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 9-10

        # @staticmethod
        # def test_john():
        def test_john(self):
            first_name = 'john'
            last_name = 'smith'
            sex = 'M'
            year_of_birth = 1580

            # assert_person_factory_works(
            self.assert_person_factory_works(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

  the test is still green.

* I remove the commented lines from :ref:`test_john`

  .. code-block:: python
    :lineno-start: 126

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

        def test_john(self):
            first_name = 'john'
            last_name = 'smith'
            sex = 'M'
            year_of_birth = 1580

            self.assert_person_factory_works(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

  .. code-block:: python
    :lineno-start: 146

            self.assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

        # @staticmethod
        # def test_mary():
        def test_mary(self):

* I change the :ref:`call<how to call a function with input>` from the :ref:`assert_person_factory_works function<extract assert_person_factory_works function>` to the :ref:`assert_person_factory_works method<move assert_person_factory_works to TestPerson>` of the :ref:`TestPerson class<add TestPerson class>` in :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 9-10

        # @staticmethod
        # def test_mary():
        def test_mary(self):
            first_name = 'mary'
            last_name = 'public'
            sex = 'F'
            year_of_birth = 2000

            # assert_person_factory_works(
            self.assert_person_factory_works(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

  green.

* I remove the commented lines from :ref:`test_mary`

  .. code-block:: python
    :lineno-start: 152

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

        def test_mary(self):
            first_name = 'mary'
            last_name = 'public'
            sex = 'F'
            year_of_birth = 2000

            self.assert_person_factory_works(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

  .. code-block:: python
    :lineno-start: 172

            self.assert_say_hello_works(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
            )

            self.assert_person_can_say_hello(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            )

        def test_dir_person_class(self):

* I change the :ref:`call<how to call a function with input>` to my :ref:`assert_equal function<extract assert_equal function>` to the :ref:`assertNotEqual method of the unittest.TestCase class<test_assert_not_equal>` in the :ref:`assert_person_factory_works method of the TestPerson class<move assert_person_factory_works to TestPerson>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 5-6

        def assert_person_factory_works(
                self, first_name, last_name,
                sex, year_of_birth
            ):
            # assert_equal(
            self.assertNotEqual(
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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    FAILED ...test_jane - AssertionError:
        'jane, doe, F, 1991' == 'jane, doe, F, 1991'
    FAILED ...test_joe - AssertionError:
        'joe, blow, M, 1996' == 'joe, blow, M, 1996'
    FAILED ...test_john - AssertionError:
        'john, smith, M, 1580' == 'john, smith, M, 1580'
    FAILED ...test_mary - AssertionError:
        'mary, public, F, 2000' == 'mary, public, F, 2000'

* I change :ref:`assertNotEqual<test_assert_not_equal>` to :ref:`assertEqual<test_assert_Equal>` in the :ref:`assert_person_factory_works method of the TestPerson class<move assert_person_factory_works to TestPerson>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 6-7

        def assert_person_factory_works(
                self, first_name, last_name,
                sex, year_of_birth
            ):
            # assert_equal(
            # self.assertNotEqual(
            self.assertEqual(
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

  the test is green again.

* I remove the commented lines from the :ref:`assert_person_factory_works method of the TestPerson class<move assert_person_factory_works to TestPerson>`

  .. code-block:: python
    :lineno-start: 27

    class TestPerson(unittest.TestCase):

        def assert_person_factory_works(
                self, first_name, last_name,
                sex, year_of_birth
            ):
            self.assertEqual(
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

* I remove the :ref:`assert_person_factory_works function<extract assert_person_factory_works function>` since it is now a repetition and my :ref:`assert_equal function<extract assert_equal function>` since it is no longer used

  .. code-block:: python
    :linenos:

    import src.person
    import unittest


    class TestPerson(unittest.TestCase):

  green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'move assert_person_factory_works to TestPerson'

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

* I can use the :ref:`unittest library<another way to write tests>` to write tests with the :ref:`methods of the unittest.TestCase class<test_dir_unittest_testcase>` or I can write them with bare :ref:`assert statements<what is an assertion?>`.

* My tests for a person still have the problem where they are the same three tests. :ref:`There has to be a way that I can use one test for all the people<how to make a person with loops>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test person with unittest: tests>`

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
* :ref:`I know how to make a person with an object<how to make a person with an object>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.

:ref:`Would you like to test the telephone project with the unittest library?<test telephone with unittest>`

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