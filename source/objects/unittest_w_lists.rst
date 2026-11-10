.. meta::
  :description:
  :keywords:

.. include:: ../links.rst

#################################################################################
test unittest with lists
#################################################################################

I want to use a :ref:`list<what is a list?>` like I did in :ref:`test_dir_list with extend and sort` to make :ref:`test_dir_unittest` and :ref:`test_dir_unittest_testcase` simpler.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/tests/test_unittest.py
  :caption: unittest/tests/test_unittest.py
  :language: python
  :linenos:
  :lines: 1-26

.. literalinclude:: ../code/tests/test_unittest.py
  :caption: unittest/tests/test_unittest.py
  :language: python
  :lineno-start: 28
  :lines: 28-78

.. literalinclude:: ../code/tests/test_unittest.py
  :caption: unittest/tests/test_unittest.py
  :language: python
  :lineno-start: 80
  :lines: 80-94

.. literalinclude:: ../code/tests/test_unittest.py
  :caption: unittest/tests/test_unittest.py
  :language: python
  :lineno-start: 96
  :lines: 96-114

.. literalinclude:: ../code/tests/test_unittest.py
  :caption: unittest/tests/test_unittest.py
  :language: python
  :lineno-start: 116
  :lines: 116-

-----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd unittest

* I open ``test_unittest.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now --patterns "**/*.py"

----

*********************************************************************************
test_dir_unittest_testcase with extend and sort
*********************************************************************************

The :ref:`attributes and methods of the unittest.TestCase object<test_dir_unittest>` are the :ref:`attributes and methods of the unittest object<test_dir_unittest>` with extra things. I can make the :ref:`attributes and methods of the unittest.TestCase object<test_dir_unittest_testcase>` by adding the "extra" to the :ref:`attributes and methods of the unittest object<test_dir_object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`variable<what is a variable?>` for the :ref:`attributes and methods of the unittest.TestCase object<test_dir_unittest_testcase>`, then add an :ref:`assertion<what is an assertion?>` for it, in  :ref:`test_dir_unittest`

.. code-block:: python
  :caption: unittest/tests/test_unittest.py
  :lineno-start: 28
  :emphasize-lines: 2-6

        def test_dir_unittest_testcase(self):
            dir_unittest_testcase = dir(unittest)
            self.assertEqual(
                dir(unittest.TestCase),
                dir_unittest_testcase
            )

            reality = dir(unittest.TestCase)

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: Lists differ: [
      '__call__', '__class__', '__delattr__', '_[1726 chars]ass'
  ] != [
      'BaseTestSuite', 'FunctionTestCase', 'Isol[578 chars]til'
  ]

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I set maxDiff_ to :ref:`None<what is None?>`

  .. code-block:: python
    :caption: unittest/tests/test_unittest.py
    :lineno-start: 28
    :emphasize-lines: 2

        def test_dir_unittest_testcase(self):
            self.maxDiff = None
            dir_unittest_testcase = dir(unittest)

* I use :ref:`extend<test_extend_adds_items_from_an_iterable_to_end_of_a_list>` to :ref:`append<test_append_adds_item_to_end_of_a_list>` the additional elements

  .. code-block:: python
    :caption: unittest/tests/test_unittest.py
    :lineno-start: 165
    :emphasize-lines: 4-6

        def test_dir_unittest(self):
            dir_unittest = dir(object)
            dir_unittest.extend((
                '__dict__', '__firstlineno__',
                '__module__', '__static_attributes__',
                '__weakref__',
                'can_get_license', 'can_vote',
                'check_age', 'say_hello',
            ))
            self.assertEqual(
                dir(src.unittest.Person),
                dir_unittest
            )

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`.

* I add a :ref:`call to the sort method<test_sort_a_list>`

  .. code-block:: python
    :caption: unittest/tests/test_unittest.py
    :lineno-start: 167
    :emphasize-lines: 8

            dir_unittest.extend((
                '__dict__', '__firstlineno__',
                '__module__', '__static_attributes__',
                '__weakref__',
                'can_get_license', 'can_vote',
                'check_age', 'say_hello',
            ))
            dir_unittest.sort()
            self.assertEqual(
                dir(src.unittest.Person),
                dir_unittest
            )

            self.assertEqual(
                dir(src.unittest.Person),
                [
                    '__class__', '__delattr__', '__dict__',
                    '__dir__', '__doc__', '__eq__',

  the test passes because :ref:`all objects inherit from 'object'<test_making_an_object_w_object>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertion<what is an assertion?>` from :ref:`test_dir_unittest`

  .. code-block:: python
    :caption: unittest/tests/test_unittest.py
    :lineno-start: 174

            dir_unittest.sort()
            self.assertEqual(
                dir(src.unittest.Person),
                dir_unittest
            )

        def test_dir_unittest_instance(self):

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_dir_unittest with extend and sort'

:ref:`All objects inherit attributes and methods from 'object'<test_making_an_object_w_object>`.

----

*********************************************************************************
test_dir_unittest_instance with extend and sort
*********************************************************************************

The :ref:`attributes and methods of an instance of the Person object<test_dir_unittest_instance>` are the :ref:`attributes and methods of the unittest object<test_dir_unittest>` with extra. Since they are both :ref:`lists<what is a list?>` I can make the :ref:`attributes and methods of an instance of the Person object<test_dir_unittest_instance>` by adding the "extra" to  the :ref:`attributes and methods of the unittest object<test_dir_unittest>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`variable<what is a variable?>` for the :ref:`attributes and methods of an instance of the Person object<test_dir_unittest_instance>`, then add an :ref:`assertion<what is an assertion?>` for it

.. code-block:: python
  :caption: unittest/tests/test_unittest.py
  :lineno-start: 180
  :emphasize-lines: 2-13

      def test_dir_unittest_instance(self):
          dir_unittest_instance = dir(src.unittest.Person)
          self.assertEqual(
              dir(
                  src.unittest.Person(
                      first_name='first_name',
                      last_name='last_name',
                      sex='M',
                      year_of_birth=2026,
                  )
              ),
              dir_unittest_instance
          )

          self.assertEqual(
              dir(
                  src.unittest.Person(
                      first_name='first_name',

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: Lists differ: [
      '__c[396 chars]_', 'age', 'can_get_license',
      'can_vote', 'che[96 chars]rth'
  ] != [
      '__c[396 chars]_', 'can_get_license', 'can_vote',
      'check_age', 'say_hello'
  ]

with a note about the difference

.. code-block:: python
  :caption: terminal

  Diff is 718 characters long. Set self.maxDiff to None to see it.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``self.maxDiff = None``

  .. code-block:: python
    :caption: unittest/tests/test_unittest.py
    :lineno-start: 180
    :emphasize-lines: 2

        def test_dir_unittest_instance(self):
            self.maxDiff = None
            dir_unittest_instance = dir(src.unittest.Person)

  the terminal_ is my friend, and shows the difference.

* I use :ref:`extend<test_extend_adds_items_from_an_iterable_to_end_of_a_list>` to :ref:`append<test_append_adds_item_to_end_of_a_list>` the seven additional elements

  .. code-block:: python
    :caption: unittest/tests/test_unittest.py
    :lineno-start: 180
    :emphasize-lines: 4-8

        def test_dir_unittest_instance(self):
            self.maxDiff = None
            dir_unittest_instance = dir(src.unittest.Person)
            dir_unittest_instance.extend((
                'age', 'first_name', 'is_citizen',
                'last_name', 'passed_test',
                'sex', 'year_of_birth',
            ))
            self.assertEqual(
                dir(
                    src.unittest.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=2026,
                    )
                ),
                dir_unittest_instance
            )

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`.

* I add a :ref:`call to the sort method<test_sort_a_list>`

  .. code-block:: python
    :caption: unittest/tests/test_unittest.py
    :lineno-start: 183
    :emphasize-lines: 6

            dir_unittest_instance.extend((
                'age', 'first_name', 'is_citizen',
                'last_name', 'passed_test',
                'sex', 'year_of_birth',
            ))
            dir_unittest_instance.sort()
            self.assertEqual(
                dir(
                    src.unittest.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=2026,
                    )
                ),
                dir_unittest_instance
            )

            self.assertEqual(
                dir(
                    src.unittest.Person(
                        first_name='first_name',

  the test passes because :ref:`all objects inherit from 'object'<test_making_an_object_w_object>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertion<what is an assertion?>` from :ref:`test_dir_unittest_instance`

  .. code-block:: python
    :caption: unittest/tests/test_unittest.py
    :lineno-start: 189

            self.assertEqual(
                dir(
                    src.unittest.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=2026,
                    )
                ),
                dir_unittest_instance
            )


    # Exceptions seen

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_dir_unittest_instance with extend and sort'

:ref:`All objects inherit attributes and methods from 'object'<test_making_an_object_w_object>`.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_unittest.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of ``lists``

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

----

*************************************************************************************
review
*************************************************************************************

:ref:`All objects inherit attributes and methods from 'object'<test_making_an_object_w_object>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test unittest with lists: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python Test Driven Development environment manually<how to make a Python Test Driven Development environment manually>`.
* :ref:`I know what a Python module is<what is a module?>`.
* :ref:`I know how to run tests automatically<how to run tests automatically>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`I know how to make a unittest with strings<how to make a unittest with strings>`.
* :ref:`I know how to make functions that take input<functions that take input>`.
* :ref:`I know what causes TypeError<what causes TypeError?>`.
* :ref:`I know how to place values in strings<telephone>`.
* :ref:`I know how to make a unittest say hello with f-strings<how to make a unittest with f-strings>`.
* :ref:`I know how to separate tests from solutions<separate and equal>`.
* :ref:`I know what causes AttributeError<what causes AttributeError?>`.
* :ref:`I know how to make a unittest with an object<how to make a unittest with an object>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test unittest with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a unittest with conditions<how to make a unittest with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`.
* :ref:`I know how to write programs that make decisions<truth table>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically with variables<how to make a Python Test Driven Development environment automatically with variables>`.
* :ref:`I know how to make a unittest with Exceptions<how to make a unittest with Exceptions>`.
* :ref:`I know how to test that an Exception is raised<how to test that an Exception is raised>`.
* :ref:`I know how to use Exception handlers in programs<how to handle Exceptions in programs>`.
* :ref:`I know how to make a unittest with loops<how to make a unittest with loops>`.
* :ref:`I know how to use lists<what is a list?>`.

:ref:`Would you like to test list comprehensions?<test unittest with lists>`

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