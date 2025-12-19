.. meta::
  :description: Learn to build a Python person dictionary with a factory function using TDD. This tutorial covers keyword arguments, default values, and exception handling.
  :keywords: Jacob Itegboje, python dictionary from function, python factory function tutorial, python tdd with pytest, create person object in python, python function with default keyword arguments, python test driven development example, handling exceptions in python unit tests, python dictionary with random values

.. include:: ../links.rst

.. _now: https://docs.python.org/3/library/datetime.html#datetime.datetime.now
.. _today: https://docs.python.org/3/library/datetime.html#datetime.date.today

#################################################################################
how to make a person
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/MAzF1fF-mwg?si=4mUekNwDAFGboUlM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

This is an exercise in making :ref:`dictionaries` with :ref:`functions`. I think these are the 2 most important concepts in Python_

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: ../code/tests/test_person.py
  :language: python
  :linenos:

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``person`` as the name of the project

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh person

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: shell

      ./makePythonTdd.ps1 person

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_person.py:7: AssertionError

* I hold :kbd:`ctrl` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_person.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format to follow Python_ :ref:`convention<conventions>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestPerson(unittest.TestCase):

*********************************************************************************
test_takes_keyword_arguments
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I change ``test_failure`` to ``test_takes_keyword_arguments``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-10

    import unittest


    class TestPerson(unittest.TestCase):

        def test_takes_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(),
                None
            )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'src' is not defined

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_person.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # NameError

* then I add an `import statement`_ for the ``person`` :ref:`module<ModuleNotFoundError>` at the top of the file

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.person
    import unittest

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.person' has no attribute 'factory'

* I add it to the list of :ref:`Exceptions<errors>` encountered

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* I open ``person.py`` from the ``src`` folder in the :ref:`editor<2 editors>` then I add a :ref:`function<functions>`

  .. code-block:: python
    :linenos:

    def factory():
        return None

  the test passes

* I want the :ref:`function<functions>` to take in a keyword argument named ``first_name``. I add it to the test in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

        def test_takes_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name='first_name',
                ),
                None
            )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: factory() got an unexpected keyword argument 'first_name'

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_person.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* then I add ``first_name`` as an input parameter to the :ref:`function<functions>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def factory(first_name):
        return None

  the test passes

* I want the :ref:`function<functions>` to take in a keyword argument named ``last_name``. I add it to the test in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_takes_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name='first_name',
                    last_name='last_name',
                ),
                None
            )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: factory() got an unexpected keyword argument 'last_name'

* I add ``last_name`` to the :ref:`function<functions>` definition in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def factory(first_name, last_name):
        return None

  the test passes

* I want the :ref:`function<functions>` to take in a keyword argument named ``sex``. I add it to the test in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6

        def test_takes_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                ),
                None
            )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: factory() got an unexpected keyword argument 'sex'

* I add ``sex`` as input to the :ref:`function<functions>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def factory(
            first_name, last_name,
            sex,
        ):
        return None

  the test passes

* I want the :ref:`function<functions>` to take in a keyword argument for ``year_of_birth`` and give it the result of calling another :ref:`function<functions>`. I add it to the test in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 7

        def test_takes_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth=this_year(),
                ),
                None
            )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'this_year' is not defined

* I add a definition for the ``this_year`` :ref:`function<functions>` above the :ref:`class<classes>` definition in ``test_person.py``

  .. NOTE:: the ...(ellipsis) represents code that does not need to change in this part

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    import unittest
    import src.person


    def this_year():
        return None


    class TestPerson(unittest.TestCase):

        def test_takes_keyword_arguments(self):
            ...

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: factory() got an unexpected keyword argument 'year_of_birth'

  when I add the name to the :ref:`function<functions>` definition in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return None

  the test passes

* I want the ``factory`` :ref:`function<functions>` to return a :ref:`dictionary<dictionaries>` as output, I change the expectation in the :ref:`assertion<AssertionError>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 9

        def test_takes_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth=this_year(),
                ),
                dict()
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != {}

  I change the `return statement`_ in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {}

  the test passes because ``{}`` and ``dict()`` are two ways to write an empty :ref:`dictionary<dictionaries>`

* I want the expected :ref:`dictionary<dictionaries>` in the test to have a key named ``first_name`` with the same value as what is given when the ``factory`` :ref:`function<functions>` is called. I change it in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 10

        def test_takes_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth=this_year(),
                ),
                dict(
                    first_name='first_name',
                )
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {} != {'first_name': 'first_name'}

* I change the `return statement`_ in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {'first_name': 'first_name'}

  the test passes

* ``'first_name'`` appears twice in the test, which means I have to make a change in 2 places if I want a different value for it. I add a :ref:`variable<test_attribute_error_w_variables>` to remove the repetition in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2, 6, 12

        def test_takes_keyword_arguments(self):
            first_name = 'first_name'

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    last_name='last_name',
                    sex='M',
                    year_of_birth=this_year()
                ),
                dict(
                    first_name=first_name,
                )
            )

  the test is still green. I now only need to change the value of ``first_name`` in one place

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2

        def test_takes_keyword_arguments(self):
            first_name = 'jane'

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    last_name='last_name',
                    sex='M',
                    year_of_birth=this_year()
                ),
                dict(
                    first_name=first_name,
                )
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': 'first_name'} != {'first_name': 'jane'}

* I change the `return statement`_ in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {'first_name': 'jane'}

  and the test is green again

* I want the :ref:`dictionary<dictionaries>` to have a key named ``last_name`` with the same value as what is given in the call to the ``factory`` :ref:`function<functions>`. I add it to the expectation in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 13

        def test_takes_keyword_arguments(self):
            first_name = 'jane'

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    last_name='last_name',
                    sex='M',
                    year_of_birth=this_year()
                ),
                dict(
                    first_name=first_name,
                    last_name='last_name',
                )
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': 'jane'} != {'first_name': 'jane', 'last_name': 'last_name'}

* I change the `return statement`_ in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': 'jane',
            'last_name': 'last_name',
        }

  the test passes

* ``'last_name'`` happens twice in the test, I add a :ref:`variable<test_attribute_error_w_variables>` to remove the duplication like I did with ``first_name`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3,8,14

        def test_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'last_name'

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    last_name=last_name,
                    sex='M',
                    year_of_birth=this_year()
                ),
                dict(
                    first_name=first_name,
                    last_name=last_name,
                )
            )

  I change the value

  .. NOTE:: the ...(ellipsis) represents code that does not need to change in this part

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

        def test_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'

            ...

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': 'jane', 'last_name': 'last_name'} != {'first_name': 'jane', 'last_name': 'doe'}

* I change the `return statement`_ in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
        }

  the test passes

* I add a key named ``sex`` to the :ref:`dictionary<dictionaries>` with the same value as what is given in the call to the ``factory`` :ref:`function<functions>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 15

        def test_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    last_name=last_name,
                    sex='M',
                    year_of_birth=this_year(),
                ),
                dict(
                    first_name=first_name,
                    last_name=last_name,
                    sex='M',
                )
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': 'jane', 'last_name': 'doe'} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M'}

  I change the `return statement`_ in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'M',
        }

  the terminal_ shows green again

* I add a :ref:`variable<test_attribute_error_w_variables>` to remove the repetition in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4,10,16

        def test_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'M'

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=this_year(),
                ),
                dict(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                )
            )

  the test is still green

* when I change the value of the ``sex`` variable_

  .. NOTE:: the ...(ellipsis) represents code that does not need to change in this part

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

        def test_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'

            ...

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M'} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'}

  I change the `return statement`_ in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'F',
        }

  and the test is green again

* I add a calculation and a key for ``age`` to the expectation in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 17

        def test_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=this_year(),
                ),
                dict(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    age=this_year()-this_year(),
                )
            )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'

  I cannot do subtraction with :ref:`None` and I want the value for the current year

* I add an `import statement`_ at the top of ``test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import datetime
    import src.person
    import unittest


    def this_year():
        return None

  datetime_ is a :ref:`module<ModuleNotFoundError>` from the `Python standard library`_ that is used for dates and times

* I change the `return statement`_ in the ``this_year`` :ref:`function <functions>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def this_year():
        return datetime.datetime.now().year

  ``datetime.datetime.now().year`` returns the ``year`` :ref:`attribute<AttributeError>` of the ``datetime`` :ref:`object<classes>` returned by the now_ :ref:`method<functions>` of the ``datetime`` :ref:`class<classes>`, from the datetime_ :ref:`module<ModuleNotFoundError>`. If you are confused, do not worry, that was a lot of terminology, it is explained in more detail when I :ref:`test AttributeError<test_attribute_error>` and :ref:`classes`

  .. ADMONITION:: I can also use the today_ :ref:`method<functions>` to get the same value

    .. code-block:: python
      :lineno-start: 6
      :emphasize-lines: 2

      def this_year():
          return datetime.datetime.today().year

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0}

  the new :ref:`dictionary<dictionaries>` has a value for ``age``

* I change the `return statement`_ in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 9

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'F',
            'age': 0,
        }

  the test passes

* I add a :ref:`variable<test_attribute_error_w_variables>` to remove duplication from ``test_person.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 5,12,18

        def test_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = this_year()

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                ),
                dict(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    age=this_year()-year_of_birth,
                )
            )

  and the test is still green

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add an `import statement`_ at the top of ``test_person.py`` to use random values in the tests

  .. TIP:: I like to arrange `import statements`_ alphabetically

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2

    import datetime
    import random
    import src.person
    import unittest

  random_ is a :ref:`module<ModuleNotFoundError>` from the `Python standard library`_ that is used to make fake random numbers. I use it for the ``year_of_birth`` variable_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5-7

        def test_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )

            ...

  ``random.randint(this_year()-120, this_year())`` gives me a random number from 120 years ago, up to and including the current year which is returned by ``this_year()``. I hit save :kbd:`ctrl+s` (Windows/Linux) or :kbd:`command+s` (mac) a few times to run the tests and and when the age is not ``0``, the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': X}

  I add the age calculation from ``test_person.py`` to the `return statement`_ in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 9

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'F',
            'age': this_year() - year_of_birth,
        }

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'this_year' is not defined

  because I called a :ref:`function<functions>` that is NOT in ``person.py``.

* I use the `return statement`_ of the ``this_year()`` :ref:`function<functions>` from ``test_person.py`` to change ``this_year()`` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 9

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'F,
            'age': datetime.datetime.now().year - year_of_birth,
        }

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

  I add an `import statement`_ at the top of ``person.py``

  .. NOTE:: the ...(ellipsis) represents code that does not need to change in this part

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import datetime


    def factory(
        ...

  the test passes

* I add randomness to the ``sex`` :ref:`variable<test_attribute_error_w_variables>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4

        def test_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = random.choice(('F', 'M'))
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )

            ...

  ``random.choice(('F', 'M'))`` randomly gives me ``F`` or ``M`` every time the test runs. I hit save :kbd:`ctrl+s` (Windows/Linux) or :kbd:`command+s` (mac) a few times to run the tests and the terminal_ shows success when ``sex`` is randomly ``'F'``, and when it is randomly ``'M'``, the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': X} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': X}

  I add the ``sex`` input parameter instead of a value that does not change to the `return statement`_ in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 8

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': sex,
            'age': datetime.datetime.now().year - year_of_birth,
        }

  the test passes with no more random failures

* I use `random.choice`_ with the ``last_name`` :ref:`variable<test_attribute_error_w_variables>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3-5

        def test_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = random.choice((
                'doe', 'smith', 'blow', 'public',
            ))
            sex = random.choice(('F', 'M'))
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )

            ...

  I hit save :kbd:`ctrl+s` (Windows/Linux) or :kbd:`command+s` (mac) a few times to run the tests and the terminal_ shows success when ``last_name`` is ``'doe'``, and when it is not, the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': X, 'age': Y} != {'first_name': 'jane', 'last_name': 'public', 'sex': X, 'age': Y}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': X, 'age': Y} != {'first_name': 'jane', 'last_name': 'smith', 'sex': X, 'age': Y}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': X, 'age': Y} != {'first_name': 'jane', 'last_name': 'blow', 'sex': X, 'age': Y}

  I add the ``last_name`` input parameter in the `return statement`_ in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': 'jane',
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  and the test is green again

* I do the same thing for the ``first_name`` :ref:`variable<test_attribute_error_w_variables>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2-4

        def test_takes_keyword_arguments(self):
            first_name = random.choice((
                'jane', 'joe', 'john', 'person',
            ))
            last_name = random.choice((
                'doe', 'smith', 'blow', 'public',
            ))
            sex = random.choice(('F', 'M'))
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )

            ...

  I hit save :kbd:`ctrl+s` (Windows/Linux) or :kbd:`command+s` (mac) a few times to run the tests and the terminal_ shows green when ``first_name`` is ``'jane'``, and when it is not, the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': 'jane', 'last_name': X, 'sex': Y, 'age': Z} != {'first_name': 'joe', 'last_name': X, 'sex': Y, 'age': Z}
    AssertionError: {'first_name': 'jane', 'last_name': X, 'sex': Y, 'age': Z} != {'first_name': 'john', 'last_name': X, 'sex': Y, 'age': Z}
    AssertionError: {'first_name': 'jane', 'last_name': X, 'sex': Y, 'age': Z} != {'first_name': 'person', 'last_name': X, 'sex': Y, 'age': Z}

  I add the ``first_name`` input parameter in the `return statement`_ in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 6

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  the test passes!

----

*************************************************************************************
test_function_w_default_keyword_arguments
*************************************************************************************

I want to see what happens when I try to make a person without a value for the ``last_name`` argument

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I select ``test_takes_keyword_arguments``, then copy (:kbd:`ctrl+c` (Windows/Linux) or ``command+c`` (mac)) and paste (:kbd:`ctrl+v` (Windows/Linux) or ``command+v`` (mac)) it below in ``test_person.py``
* I change the name of the new test to ``test_function_w_default_keyword_arguments`` and comment out the ``last_name`` variable_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 40,44-46

    import datetime
    import random
    import src.person
    import unittest


    def this_year():
        return datetime.datetime.now().year


    class TestPerson(unittest.TestCase):

        def test_takes_keyword_arguments(self):
            first_name = random.choice((
                'jane', 'joe', 'john', 'person',
            ))
            last_name = random.choice((
                'doe', 'smith', 'blow', 'public',
            ))
            sex = random.choice(('F', 'M'))
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                ),
                dict(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    age=this_year()-year_of_birth,
                )
            )

        def test_function_w_default_keyword_arguments(self):
            first_name = random.choice((
                'jane', 'joe', 'john', 'person',
            ))
            # last_name = random.choice((
            #    'doe', 'smith', 'blow', 'public',
            # ))
            sex = random.choice(('F', 'M'))
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                ),
                dict(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    age=this_year()-year_of_birth,
                )
            )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'last_name' is not defined

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I comment out ``last_name`` in the call to the ``factory`` :ref:`function<functions>` in ``test_function_w_default_keyword_arguments``

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 4

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    # last_name=last_name,
                    year_of_birth=year_of_birth,
                    sex=sex,
                ),
                dict(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    age=this_year() - year_of_birth,
                )
            )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: factory() missing 1 required positional argument: 'last_name'

  the ``factory`` :ref:`function<functions>` is called with 3 arguments in ``test_function_w_default_keyword_arguments`` but the definition expects 4 in ``person.py``

* I add a default value for ``last_name`` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2

    def factory(
            first_name, last_name=None,
            sex, year_of_birth,
        ):
        ...

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: parameter without a default follows parameter with a default

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_person.py``

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 6

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I add a default value for the ``sex`` parameter in the ``factory`` :ref:`function<functions>` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    def factory(
            first_name, last_name=None,
            sex=None, year_of_birth,
        ):
        ...

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: parameter without a default follows parameter with a default

* I give the ``year_of_birth`` parameter a default value as well

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    def factory(
            first_name, last_name=None,
            sex=None, year_of_birth=None,
        ):
        ...

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'last_name' is not defined

  the value for the ``last_name`` key in the expected :ref:`dictionary<dictionaries>` in ``test_function_w_default_keyword_arguments`` points to the ``last_name`` :ref:`variable<test_attribute_error_w_variables>` which I just commented out

* I change the expectation of ``test_function_w_default_keyword_arguments`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 10

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    # last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                ),
                dict(
                    first_name=first_name,
                    last_name='doe',
                    sex=sex,
                    age=this_year()-year_of_birth,
                )
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': X, 'last_name': None, 'sex': Y, 'age': Z} != {'first_name': X, 'last_name': 'doe', 'sex': Y, 'age': Z}

  the ``factory`` :ref:`function<functions>` returns a :ref:`dictionary<dictionaries>` with a value of :ref:`None` for ``last_name`` and the test expects ``'doe'``

* I change the default value for ``last_name`` in the ``factory`` :ref:`function<functions>` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2

    def factory(
            first_name, last_name='doe',
            sex=None, year_of_birth=None,
        ):
        ...

  the test passes

  .. ADMONITION:: When the ``factory`` :ref:`function<functions>` is called with no value for the ``last_name`` argument, it uses ``'doe'`` because that is the default value in the :ref:`function<functions>` definition, it is the same as calling it with ``last_name='doe'``

    .. code-block:: python
      :emphasize-lines: 5

      src.person.factory(
          first_name=first_name,
          sex=sex,
          year_of_birth=year_of_birth,
          last_name='doe',
      )

* I remove the commented lines from ``test_function_w_default_keyword_arguments`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 40

        def test_function_w_default_keyword_arguments(self):
            first_name = random.choice((
                'jane', 'joe', 'john', 'person',
            ))
            sex = random.choice(('F', 'M'))
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                ),
                dict(
                    first_name=first_name,
                    last_name='doe',
                    sex=sex,
                    age=this_year()-year_of_birth,
                )
            )

* I comment out the ``sex`` :ref:`variable<test_attribute_error_w_variables>` in the test to see what happens if I do not know its value

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 5

        def test_function_w_default_keyword_arguments(self):
            first_name = random.choice((
                'jane', 'joe', 'john', 'person',
            ))
            # sex = random.choice(('F', 'M'))
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'sex' is not defined

* I comment out ``sex`` in the call to the ``factory`` :ref:`function<functions>` in the :ref:`assertion<AssertionError>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 4

          self.assertEqual(
              src.person.factory(
                  first_name=first_name,
                  # sex=sex,
                  year_of_birth=year_of_birth,
              ),
              dict(
                  first_name=first_name,
                  last_name='doe',
                  sex=sex,
                  age=this_year()-year_of_birth,
              )
          )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'sex' is not defined

  the value in the expected :ref:`dictionary<dictionaries>` still uses the ``sex`` :ref:`variable<test_attribute_error_w_variables>` I commented out. I change the expectation

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 10

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                # sex=sex,
                year_of_birth=year_of_birth,
            ),
            dict(
                first_name=first_name,
                last_name='doe',
                sex='M',
                age=this_year()-year_of_birth,
            )
        )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': X, 'last_name': 'doe', 'sex': None, 'age': Y} != {'first_name': X, 'last_name': 'doe', 'sex': 'M', 'age': Y}

  the ``factory`` :ref:`function<functions>` returns a :ref:`dictionary<dictionaries>` with :ref:`None` as the value for ``sex`` and the test expects ``'M'``

* I add a default value for ``sex`` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    def factory(
            first_name, last_name='doe',
            sex='M', year_of_birth=None
        ):
        ...

  the test passes

  .. ADMONITION:: When the ``factory`` :ref:`function<functions>` is called with no value for the ``sex`` argument, it uses ``'M'`` because that is the default value in the :ref:`function<functions>` definition, it is the same as calling it with ``sex='M'``

    .. code-block:: python
      :emphasize-lines: 5

      src.person.factory(
          first_name=first_name,
          year_of_birth=year_of_birth,
          last_name='doe',
          sex='M',
      )

    since the values are the same as the default values, I can call the :ref:`function<functions>` without them

    .. code-block:: python
      :emphasize-lines: 2-3

      src.person.factory(
          first_name=first_name,
          year_of_birth=year_of_birth,
      )

* I remove the commented lines from ``test_person.py``

  .. code-block:: python
    :lineno-start: 40

        def test_function_w_default_keyword_arguments(self):
            first_name = random.choice((
                'jane', 'joe', 'john', 'person',
            ))
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    year_of_birth=year_of_birth,
                ),
                dict(
                    first_name=first_name,
                    last_name='doe',
                    sex='M',
                    age=this_year()-year_of_birth,
                )
            )

  the terminal_ still shows green

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* ``first_name`` and ``year_of_birth`` are made the same way in both tests, I can remove this repetition by adding :ref:`attributes<AttributeError>` to the ``TestPerson`` :ref:`class<classes>`

  .. NOTE:: the ...(ellipsis) represents code that does not need to change in this part

  .. code-block:: python
    :linenos:
    :emphasize-lines: 13-18

    import datetime
    import random
    import src.person
    import unittest


    def this_year():
        return datetime.datetime.now().year


    class TestPerson(unittest.TestCase):

        first_name = random.choice((
            'jane', 'joe', 'john', 'person',
        ))
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )

        def test_takes_keyword_arguments(self):
            ...

  I can use them in ``test_takes_keyword_arguments`` with ``self.`` the same way I use the ``assert`` :ref:`methods<functions>` since they now belong to the ``TestPerson`` :ref:`class<classes>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 2-5,10-13

        def test_takes_keyword_arguments(self):
            # first_name = random.choice((
            #    'jane', 'joe', 'john', 'person',
            # ))
            first_name = self.first_name
            last_name = random.choice((
                'doe', 'smith', 'blow', 'public',
            ))
            sex = random.choice(('F', 'M'))
            # year_of_birth = random.randint(
            #    this_year()-120, this_year()
            # )
            year_of_birth = self.random_year_of_birth

            self.assertEqual(
                ...

  the test is still green. I do the same thing in ``test_function_w_default_keyword_arguments``

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-9

        def test_function_w_default_keyword_arguments(self):
            # first_name = random.choice((
            #    'jane', 'joe', 'john', 'person',
            # ))
            first_name = self.first_name
            # year_of_birth = random.randint(
            #    this_year()-120, this_year()
            # )
            year_of_birth = self.random_year_of_birth

            self.assertEqual(
                ...

  the terminal_ still shows green

* I remove the commented lines from ``test_takes_keyword_arguments``

  .. code-block:: python
    :lineno-start: 20

        def test_takes_keyword_arguments(self):
            first_name = self.first_name
            last_name = random.choice((
                'doe', 'smith', 'blow', 'public',
            ))
            sex = random.choice(('F', 'M'))
            year_of_birth = self.random_year_of_birth

            self.assertEqual(
                ...

  and remove the commented lines from ``test_function_w_default_keyword_arguments``

  .. code-block:: python
    :lineno-start: 43

        def test_function_w_default_keyword_arguments(self):
            first_name = self.first_name
            year_of_birth = self.random_year_of_birth

            self.assertEqual(
                ...

  still green

* since the :ref:`variables<test_attribute_error_w_variables>` point to :ref:`class attributes<test_attribute_error_w_class_attributes>`, I can use them directly and comment out ``first_name`` and ``year_of_birth`` in ``test_takes_keyword_arguments``

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 2,7,11,14,17,20

        def test_takes_keyword_arguments(self):
            # first_name = self.first_name
            last_name = random.choice((
                'doe', 'smith', 'blow', 'public',
            ))
            sex = random.choice(('F', 'M'))
            # year_of_birth = self.random_year_of_birth

            self.assertEqual(
                src.person.factory(
                    first_name=self.first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=self.random_year_of_birth,
                ),
                dict(
                    first_name=self.first_name,
                    last_name=last_name,
                    sex=sex,
                    age=this_year()-self.random_year_of_birth,
                )
            )

  the test is still green. I make the same change in ``test_function_w_default_keyword_arguments``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2-3,7-8,11,14

        def test_function_w_default_keyword_arguments(self):
            # first_name = self.first_name
            # year_of_birth = self.random_year_of_birth

            self.assertEqual(
                src.person.factory(
                    first_name=self.first_name,
                    year_of_birth=self.random_year_of_birth,
                ),
                dict(
                    first_name=self.first_name,
                    last_name='doe',
                    sex='M',
                    age=this_year()-self.random_year_of_birth,
                )
            )

  all tests are still passing

* I remove the commented lines from ``test_takes_keyword_arguments``

  .. code-block:: python
    :lineno-start: 20

        def test_takes_keyword_arguments(self):
            last_name = random.choice((
                'doe', 'smith', 'blow', 'public',
            ))
            sex = random.choice(('F', 'M'))

            self.assertEqual(
                ...

  and in ``test_function_w_default_keyword_arguments``

  .. code-block:: python
    :lineno-start: 41

        def test_function_w_default_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name=self.first_name,
                    year_of_birth=self.random_year_of_birth
                ),
                dict(
                    first_name=self.first_name,
                    last_name='doe',
                    sex='M',
                    age=this_year()-self.random_year_of_birth,
                )
            )

  the tests are still passing

* both tests have the same random values for ``first_name`` and ``year_of_birth``, they were not always the same before the change. I add the `unittest.TestCase.setUp`_ :ref:`method<functions>` to make sure they both get new random values before each test runs

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3-9

    class TestPerson(unittest.TestCase):

        def setUp(self):
            first_name = random.choice((
                'jane', 'joe', 'john', 'person',
            ))
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )

        def test_takes_keyword_arguments(self):
            ...

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: 'TestPerson' object has no attribute 'first_name'

  because there is no longer a :ref:`class<classes>` :ref:`attribute<AttributeError>` named ``first_name``, it is now a :ref:`variable<test_attribute_error_w_variables>` in the `unittest.TestCase.setUp`_ :ref:`method<functions>` and the other :ref:`methods<functions>` cannot reach it

* I add ``self.`` to make it a :ref:`class<classes>` :ref:`attribute<AttributeError>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

        def setUp(self):
            self.first_name = random.choice((
                'jane', 'joe', 'john', 'person',
            ))
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )

        def test_takes_keyword_arguments(self):
            ...

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: 'TestPerson' object has no attribute 'year_of_birth'

* same problem, same solution

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5

        def setUp(self):
            self.first_name = random.choice((
                'jane', 'joe', 'john', 'person',
            ))
            self.random_year_of_birth = random.randint(
                this_year()-120, this_year()
            )

        def test_takes_keyword_arguments(self):
            ...

  and both tests are green again!

  ``self.first_name`` and ``self.random_year_of_birth`` are given random values before the first test, then given random values again before the second test. That was a lot, but we got through it.

----

*********************************************************************************
test_person_tests
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I close ``test_person.py``
* I want to write the solution without looking at the tests and delete all the text in ``person.py``. The terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.person' has no attribute 'factory'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add the name

  .. code-block:: python
    :linenos:

    factory

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'factory' is not defined

* I point it to :ref:`None`

  .. code-block:: python
    :linenos:

    factory = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

* when I make it a :ref:`function<functions>`

  .. code-block:: python
    :linenos:

    def factory():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: factory() got an unexpected keyword argument 'first_name'

  I add the keyword argument to the :ref:`function<functions>` definition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def factory(first_name):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: factory() got an unexpected keyword argument 'last_name'

  I add the keyword argument

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def factory(first_name, last_name):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: factory() got an unexpected keyword argument 'sex'

  when I add the keyword argument

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def factory(
            first_name, last_name,
            sex
        ):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: factory() got an unexpected keyword argument 'year_of_birth'

  I add the missing keyword argument

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != {'first_name': X, 'last_name': Y, 'sex': Z, 'age': A}

* I change the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-10

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': 'john',
            'last_name': 'blow',
            'sex': 'F',
            'age': 20,
        }

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'smith', 'sex': 'M', 'age': 50}
    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 73}
    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'john', 'last_name': 'smith', 'sex': 'M', 'age': 77}
    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'public', 'sex': 'M', 'age': 98}

  the values of ``first_name``, ``last_name``, ``sex`` and ``age`` change every time the test runs

* I make the :ref:`dictionary<dictionaries>` in the `return statement`_ use the ``first_name`` input parameter instead of a value that does not change

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': first_name,
            'last_name': 'blow',
            'sex': 'F',
            'age': 20,
        }

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': X, 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': X, 'last_name': 'public', 'sex': 'M', 'age': 69}
    AssertionError: {'first_name': X, 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': X, 'last_name': 'blow', 'sex': 'M', 'age': 97}
    AssertionError: {'first_name': X, 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': X, 'last_name': 'smith', 'sex': 'M', 'age': 74}
    AssertionError: {'first_name': X, 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': X, 'last_name': 'public', 'sex': 'M', 'age': 19}

  the ``first_name`` now matches, and the values of ``last_name``, ``sex`` and ``age`` change every time the test runs

* I use the ``last_name`` input parameter in the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': 'F',
            'age': 20,
        }

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': X, 'last_name': Y, 'sex': 'F', 'age': 20} != {'first_name': X, 'last_name': Y, 'sex': 'M', 'age': 3}
    AssertionError: {'first_name': X, 'last_name': Y, 'sex': 'F', 'age': 20} != {'first_name': X, 'last_name': Y, 'sex': 'M', 'age': 118}
    AssertionError: {'first_name': X, 'last_name': Y, 'sex': 'F', 'age': 20} != {'first_name': X, 'last_name': Y, 'sex': 'M', 'age': 19}
    AssertionError: {'first_name': X, 'last_name': Y, 'sex': 'F', 'age': 20} != {'first_name': X, 'last_name': Y, 'sex': 'M', 'age': 95}

  the values for ``first_name``, and ``last_name`` now match, the values of ``sex`` and ``age`` change every time the test runs

* When I add the ``sex`` input parameter to the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': 20,
        }

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 20} != {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 1}
    AssertionError: {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 20} != {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 90}
    AssertionError: {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 20} != {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 113}
    AssertionError: {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 20} != {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 58}

  the ``first_name``, ``last_name`` and ``sex`` match, the value of ``age`` changes every time the test runs

* I add the ``year_of_birth`` input parameter to the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': year_of_birth,
        }

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 2022} != {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 2}
    AssertionError: {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 2024} != {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 0}
    AssertionError: {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 1981} != {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 43}
    AssertionError: {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 1969} != {'first_name': X, 'last_name': Y, 'sex': Z, 'age': 55}

  the test expects the difference between the current year and the ``year_of_birth`` to get the ``age``

* I add an `import statement`_ at the top of the file

  .. code-block:: python
    :linenos:

    import datetime


    def factory(
        ...

  then I use it to get the current year for the age calculation

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 9

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: factory() missing 2 required positional arguments: 'last_name' and 'sex'

* I add a default value for ``last_name``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2

    def factory(
            first_name, last_name=None,
            sex, year_of_birth,
        ):
        ...

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: parameter without a default follows parameter with a default

* I add a default value for ``sex``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    def factory(
            first_name, last_name=None,
            sex=None, year_of_birth,
        ):
        ...

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: parameter without a default follows parameter with a default

* I add a default value for ``year_of_birth``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    def factory(
            first_name, last_name=None,
            sex=None, year_of_birth=None,
        ):

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': X, 'last_name': None, 'sex': None, 'age': Y} != {'first_name': X, 'last_name': 'doe', 'sex': 'M', 'age': Y}

  the values for ``last_name`` and ``sex`` do not match the expectation

* I change the default value for ``last_name`` to match

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2

    def factory(
            first_name, last_name='doe',
            sex=None, year_of_birth=None,
        ):
        ...

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'first_name': X, 'last_name': Y, 'sex': None, 'age': Z} != {'first_name': Z, 'last_name': Y, 'sex': 'M', 'age': Z}

* when I make the default value of the ``sex`` argument match the expectation

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6

    import datetime


    def factory(
            first_name, last_name='doe',
            sex='M', year_of_birth=None
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  both tests pass! I think I am pretty good at this

*************************************************************************************
review
*************************************************************************************

I ran tests to make a :ref:`function<functions>` that takes in :ref:`keyword arguments<test_functions_w_keyword_arguments>` as input, has default values for some of them, performs an action based on an input and returns a :ref:`dictionary <dictionaries>` as output

I also ran into the following :ref:`Exceptions<errors>`

* :ref:`AssertionError`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError`
* :ref:`TypeError`
* SyntaxError_


----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a person: tests and solution>`

----

*********************************************************************************
what is next?
*********************************************************************************

you know

* :ref:`how to make a test driven development environment`
* :ref:`how to raise AssertionError with assert methods<AssertionError>`
* :ref:`how to write functions<functions>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<None>`
* :ref:`what is True and False in Python<booleans>`
* :ref:`how to write programs that make decisions<booleans: truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<lists: list comprehensions>`
* :ref:`how to make dictionaries with functions<how to make a person>` - this chapter

:ref:`Would you like to test dictionaries?<dictionaries>`

----

*********************************************************************************
please leave a review
*********************************************************************************

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 5 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->