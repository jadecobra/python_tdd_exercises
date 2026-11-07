.. meta::
  :description:
  :keywords:
.. include:: ../../links.rst

.. _how to make a person with lists:

#################################################################################
how to make a person with lists
#################################################################################

----

I want to use a :ref:`list<what is a list?>` like I did in :ref:`test_dir_person_object with extend and sort` to make :ref:`test_dir_person_object` and :ref:`test_dir_person_instance` simpler.

----

*********************************************************************************
preview
*********************************************************************************

I add these tests to the end of the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_person.py
  :language: python
  :linenos:
  :caption: person/tests/test_person.py
  :lines: 1-32

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :lineno-start: 34
  :caption: person/tests/test_person.py
  :lines: 34-53

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :lineno-start: 55
  :caption: person/tests/test_person.py
  :lines: 55-73

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :lineno-start: 75
  :caption: person/tests/test_person.py
  :lines: 75-105

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :lineno-start: 107
  :caption: person/tests/test_person.py
  :lines: 107-119

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :lineno-start: 121
  :caption: person/tests/test_person.py
  :lines: 121-128

.. literalinclude:: ../../code/person/tests/test_person_w_loops.py
  :language: python
  :lineno-start: 130
  :caption: person/tests/test_person.py
  :lines: 130-147

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

    uv run pytest-watcher . --now --patterns "**/*.py"

----

*********************************************************************************
test_dir_person_object with extend and sort
*********************************************************************************

The :ref:`attributes and methods of the Person object<test_dir_person_object>` are the :ref:`attributes and methods of 'object'<test_dir_object>` with extra things. I can make the :ref:`attributes and methods of the Person object<test_dir_person_object>` by adding the "extra" to the :ref:`attributes and methods of 'object'<test_dir_object>`, since they are both :ref:`lists<what is a list?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`variable<what is a variable?>` for the :ref:`attributes and methods of the Person object<test_dir_person_object>`, then add an :ref:`assertion<what is an assertion?>` for it, in  :ref:`test_dir_person_object`

.. code-block:: python
  :caption: person/tests/test_person.py
  :lineno-start: 165
  :emphasize-lines: 2-10

      def test_dir_person_object(self):
          dir_person = dir(object)
          dir_person.extend((
              'can_get_license', 'can_vote',
              'check_age', 'say_hello',
          ))
          self.assertEqual(
              dir(src.person.Person),
              dir_person
          )

          self.assertEqual(
              dir(src.person.Person),

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: Lists differ: [
      '__c[24 chars]'__dict__', '__dir__', '__doc__',
      '__eq__', '_[381 chars]llo'
  ] != [
      '__c[24 chars]'__dir__', '__doc__', '__eq__',
      '__format__', [296 chars]llo'
  ]

with a note about the difference

.. code-block:: python
  :caption: terminal

  First list contains 5 additional elements.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use :ref:`extend<test_extend_adds_items_from_an_iterable_to_end_of_a_list>` to :ref:`append<test_append_adds_item_to_end_of_a_list>` the five additional elements

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 165
    :emphasize-lines: 4-6

        def test_dir_person_object(self):
            dir_person = dir(object)
            dir_person.extend((
                '__dict__', '__firstlineno__',
                '__module__', '__static_attributes__',
                '__weakref__',
                'can_get_license', 'can_vote',
                'check_age', 'say_hello',
            ))
            self.assertEqual(
                dir(src.person.Person),
                dir_person
            )

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`.

* I add a :ref:`call to the sort method<test_sort_a_list>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 167
    :emphasize-lines: 8

            dir_person.extend((
                '__dict__', '__firstlineno__',
                '__module__', '__static_attributes__',
                '__weakref__',
                'can_get_license', 'can_vote',
                'check_age', 'say_hello',
            ))
            dir_person.sort()
            self.assertEqual(
                dir(src.person.Person),
                dir_person
            )

            self.assertEqual(
                dir(src.person.Person),
                [
                    '__class__', '__delattr__', '__dict__',
                    '__dir__', '__doc__', '__eq__',

  the test passes because :ref:`all objects inherit from 'object'<test_making_an_object_w_object>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertion<what is an assertion?>` from :ref:`test_dir_person_object`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 174

            dir_person.sort()
            self.assertEqual(
                dir(src.person.Person),
                dir_person
            )

        def test_dir_person_instance(self):

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_dir_person_object with extend and sort'

:ref:`All objects inherit attributes and methods from 'object'<test_making_an_object_w_object>`.

----

*********************************************************************************
test_dir_person_instance with extend and sort
*********************************************************************************

The :ref:`attributes and methods of an instance of the Person object<test_dir_person_instance>` are the :ref:`attributes and methods of the Person object<test_dir_person_object>` with extra. Since they are both :ref:`lists<what is a list?>` I can make the :ref:`attributes and methods of an instance of the Person object<test_dir_person_instance>` by adding the "extra" to  the :ref:`attributes and methods of the Person object<test_dir_person_object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`variable<what is a variable?>` for the :ref:`attributes and methods of an instance of the Person object<test_dir_person_instance>`, then add an :ref:`assertion<what is an assertion?>` for it

.. code-block:: python
  :caption: person/tests/test_person.py
  :lineno-start: 180
  :emphasize-lines: 2-13

      def test_dir_person_instance(self):
          dir_person_instance = dir(src.person.Person)
          self.assertEqual(
              dir(
                  src.person.Person(
                      first_name='first_name',
                      last_name='last_name',
                      sex='M',
                      year_of_birth=2026,
                  )
              ),
              dir_person_instance
          )

          self.assertEqual(
              dir(
                  src.person.Person(
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
    :caption: person/tests/test_person.py
    :lineno-start: 180
    :emphasize-lines: 2

        def test_dir_person_instance(self):
            self.maxDiff = None
            dir_person_instance = dir(src.person.Person)

  the terminal_ is my friend, and shows the difference.

* I use :ref:`extend<test_extend_adds_items_from_an_iterable_to_end_of_a_list>` to :ref:`append<test_append_adds_item_to_end_of_a_list>` the seven additional elements

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 180
    :emphasize-lines: 4-8

        def test_dir_person_instance(self):
            self.maxDiff = None
            dir_person_instance = dir(src.person.Person)
            dir_person_instance.extend((
                'age', 'first_name', 'is_citizen',
                'last_name', 'passed_test',
                'sex', 'year_of_birth',
            ))
            self.assertEqual(
                dir(
                    src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=2026,
                    )
                ),
                dir_person_instance
            )

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`.

* I add a :ref:`call to the sort method<test_sort_a_list>`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 183
    :emphasize-lines: 6

            dir_person_instance.extend((
                'age', 'first_name', 'is_citizen',
                'last_name', 'passed_test',
                'sex', 'year_of_birth',
            ))
            dir_person_instance.sort()
            self.assertEqual(
                dir(
                    src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=2026,
                    )
                ),
                dir_person_instance
            )

            self.assertEqual(
                dir(
                    src.person.Person(
                        first_name='first_name',

  the test passes because :ref:`all objects inherit from 'object'<test_making_an_object_w_object>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertion<what is an assertion?>` from :ref:`test_dir_person_instance`

  .. code-block:: python
    :caption: person/tests/test_person.py
    :lineno-start: 189

            self.assertEqual(
                dir(
                    src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=2026,
                    )
                ),
                dir_person_instance
            )


    # Exceptions seen

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_dir_person_instance with extend and sort'

:ref:`All objects inherit attributes and methods from 'object'<test_making_an_object_w_object>`.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_person.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of ``lists``

  .. code-block:: python
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

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a person with lists: tests and solutions>`

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
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`.
* :ref:`I know how to write programs that make decisions<truth table>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically with variables<how to make a Python Test Driven Development environment automatically with variables>`.
* :ref:`I know how to make a person with Exceptions<how to make a person with Exceptions>`.
* :ref:`I know how to test that an Exception is raised<how to test that an Exception is raised>`.
* :ref:`I know how to use Exception handlers in programs<how to handle Exceptions in programs>`.
* :ref:`I know how to make a person with loops<how to make a person with loops>`.
* :ref:`I know how to use lists<what is a list?>`.

:ref:`Would you like to refactor the attributes of the unittest library with lists?<test unittest with lists>`

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