.. meta::
  :description: Learn to build a Python person dictionary with a factory function using TDD. This tutorial covers keyword arguments, default values, and exception handling.
  :keywords: Jacob Itegboje, python dictionary from function, python factory function tutorial, python tdd with pytest, create person object in python, python function with default :ref:`keyword argument<test_functions_w_keyword_arguments>`s, python test driven development example, handling exceptions in python unit tests, python dictionary with random values

.. include:: ../links.rst

.. _now: https://docs.python.org/3/library/datetime.html#datetime.datetime.now
.. _now method: now_
.. _today: https://docs.python.org/3/library/datetime.html#datetime.date.today
.. _today method: today_
.. _random.choice: https://docs.python.org/3/library/random.html#random.choice
.. _choice method: `random.choice`_
.. _random.choice method: `random.choice`_

#################################################################################
how to make a person
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/MAzF1fF-mwg?si=4mUekNwDAFGboUlM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

This is an exercise in making :ref:`dictionaries` with :ref:`functions<what is a function?>`. I think they are the 2 most important things in Python_

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/tests/test_person.py
  :language: python
  :linenos:

-----

*********************************************************************************
start the project
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``person`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh person

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: shell

      ./makePythonTdd.ps1 person

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 3
    :emphasize-text: test_person

    E       AssertionError: True is not false

    tests/test_person.py:7: AssertionError

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_person.py:7`` to put the cursor on line 7 in the :ref:`editor<2 editors>`

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

* I change the name of the :ref:`class<what is a class?>` to match the :ref:`CapWords format<CapWords>` to follow :ref:`Python convention<conventions>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestPerson(unittest.TestCase):

----

*********************************************************************************
test_factory_takes_keyword_arguments
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change ``test_failure`` to ``test_factory_takes_keyword_arguments``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-10

    import unittest


    class TestPerson(unittest.TestCase):

        def test_factory_takes_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(),
                None
            )


    # Exceptions seen
    # AssertionError

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'src' is not defined

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 13
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

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.person' has no attribute 'factory'

  there is nothing in ``person.py`` with that name

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``person.py`` from the ``src`` folder in the :ref:`editor<2 editors>`

* I add a :ref:`function<what is a function?>` to ``person.py``

  .. code-block:: python
    :linenos:

    def factory():
        return None

  the test passes

----

* I want the :ref:`function<what is a function?>` to take in a :ref:`keyword argument<test_functions_w_keyword_arguments>` called ``first_name``. I add it to the test in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3-5

        def test_factory_takes_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name='first_name',
                ),
                None
            )


    # Exceptions seen

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'first_name'

  the test calls the ``factory`` :ref:`function<what is a function?>` with input, but the definition in ``person.py`` does not take any input

* I add :ref:`TypeError` to the list of :ref:`Exceptions<errors>` seen in ``test_person.py``

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
    :emphasize-lines: 1

    def factory(first_name):
        return None

  the test passes

-----

* I want the :ref:`function<what is a function?>` to take in a :ref:`keyword argument<test_functions_w_keyword_arguments>` called ``last_name``. I add it to the test in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_factory_takes_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name='first_name',
                    last_name='last_name',
                ),
                None
            )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: factory() got an unexpected keyword argument 'last_name'. Did you mean 'first_name'?

  the test calls the ``factory`` :ref:`function<what is a function?>` with 2 inputs, but the definition in ``person.py`` only takes 1 input


* I add ``last_name`` to the :ref:`function<what is a function?>` definition in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def factory(first_name, last_name):
        return None

  the test passes

----

* I want the :ref:`function<what is a function?>` to take in a :ref:`keyword argument<test_functions_w_keyword_arguments>` called ``sex``. I add it to the test in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6

        def test_factory_takes_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                ),
                None
            )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'sex'

  the test calls the ``factory`` :ref:`function<what is a function?>` with 3 inputs, but the definition in ``person.py`` only takes 2 inputs

* I add ``sex`` as an input parameter to the ``factory`` :ref:`function<what is a function?>` in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def factory(
            first_name, last_name,
            sex,
        ):
        return None

  the test passes

----

* I want the :ref:`function<what is a function?>` to take in a :ref:`keyword argument<test_functions_w_keyword_arguments>` for ``year_of_birth`` and give it the result of calling another :ref:`function<what is a function?>`. I add it to the test in ``test_person.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 7

        def test_factory_takes_keyword_arguments(self):
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

  .. code-block:: python

    NameError: name 'this_year' is not defined

  there is nothing with that name in this file_

* I add a definition for the ``this_year`` :ref:`function<what is a function?>` above the :ref:`class<what is a class?>` definition in ``test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    import src.person
    import unittest


    def this_year():
        return None


    class TestPerson(unittest.TestCase):

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'year_of_birth'

  the test calls the ``factory`` :ref:`function<what is a function?>` with 4 inputs, but the definition in ``person.py`` only takes 3 inputs

* I add the name to the :ref:`function<what is a function?>` definition in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return None

  the test passes

----

* I want the ``factory`` :ref:`function<what is a function?>` to return a :ref:`dictionary<dictionaries>` as output, I change the expectation of the :ref:`assertion<what is an assertion?>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 9

        def test_factory_takes_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth=this_year(),
                ),
                dict()
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != {}

* I change :ref:`None<what is None?>` to a :ref:`dictionary<what is a dictionary?>` in the `return statement`_ in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {}

  the test passes because ``{}`` and ``dict()`` are two ways to :ref:`make the empty dictionary<test_making_a_dictionary>`

----

* I want the expected :ref:`dictionary<dictionaries>` in the test to have a :ref:`key<test_keys_of_a_dictionary>` called ``first_name`` with the same :ref:`value<test_values_of_a_dictionary>` as what is given when the ``factory`` :ref:`function<what is a function?>` is called. I add the :ref:`key<test_keys_of_a_dictionary>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 10

        def test_factory_takes_keyword_arguments(self):
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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

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

* I typed ``'first_name'`` two times in the test, which means I have to make a change in 2 places when I want a different :ref:`value<test_values_of_a_dictionary>`. I add a :ref:`variable<what is a variable?>` to remove the repetition in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2

        def test_factory_takes_keyword_arguments(self):
            first_name = 'first_name'

            self.assertEqual(

* I use the :ref:`variable<what is a variable?>` as the value for ``first_name`` in the call to ``src.person.factory`` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 3-4

            self.assertEqual(
                src.person.factory(
                    # first_name='first_name',
                    first_name=first_name,
                    last_name='last_name',
                    sex='M',
                    year_of_birth=this_year(),
                ),

  the test is still green

* I use the :ref:`variable<what is a variable?>` as the :ref:`value<test_values_of_a_dictionary>` for the ``first_name`` :ref:`key<test_keys_of_a_dictionary>` in the expected :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2-3

                dict(
                    # first_name='first_name',
                    first_name=first_name,
                )

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 11

        def test_factory_takes_keyword_arguments(self):
            first_name = 'first_name'

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    last_name='last_name',
                    sex='M',
                    year_of_birth=this_year(),
                ),
                dict(
                    first_name=first_name,
                )
            )


    # Exceptions seen

  I now only need to change the value of ``first_name`` in one place

* I change ``'first_name'`` to ``'jane'``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2

        def test_factory_takes_keyword_arguments(self):
            first_name = 'jane'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

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

----

* I want the expected :ref:`dictionary<dictionaries>` to have a :ref:`key<test_keys_of_a_dictionary>` called ``last_name`` with the same :ref:`value<test_values_of_a_dictionary>` as what is given in the call to the ``factory`` :ref:`function<what is a function?>`. I add it to the expectation in ``test_person.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 10

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 2

    E       - {'first_name': 'jane'}
    E       + {'first_name': 'jane', 'last_name': 'last_name'}

* I change the `return statement`_ in ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-8

    def factory(
            first_name, last_name,
            sex, year_of_birth,
        ):
        return {
            'first_name': 'jane',
            'last_name': 'last_name',
        }

  the test passes

* ``'last_name'`` happens two times in the test, I add a :ref:`variable<what is a variable?>` to remove the repetition like I did with ``'first_name'`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

        def test_factory_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'last_name'

            self.assertEqual(

* I use the new :ref:`variable<what is a variable?>` in the call to ``src.person.factory`` in the  :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 4-5

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    # last_name='last_name',
                    last_name=last_name,
                    sex='M',
                    year_of_birth=this_year(),
                ),

  the test is still green

* I use the :ref:`variable<what is a variable?>` in the expected :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-4

                dict(
                    first_name=first_name,
                    # last_name='last_name',
                    last_name=last_name,
                )

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 11

        def test_factory_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'last_name'

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
                )
            )


    # Exceptions seen

  the test is still green

* I change the value from ``'last_name'`` to ``'doe'``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

        def test_factory_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 5

    E       - {'first_name': 'jane', 'last_name': 'last_name'}
    E       ?                                      ^^^^^^^^
    E
    E       + {'first_name': 'jane', 'last_name': 'doe'}
    E       ?                                      ^^

  the :ref:`values<test_values_of_a_dictionary>` for the ``last_name`` :ref:`key<test_keys_of_a_dictionary>` are different in the 2 :ref:`dictionaries<what is a dictionary?>`

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

----

* I add a :ref:`key<test_keys_of_a_dictionary>` called ``sex`` to the :ref:`dictionary<dictionaries>` with the same :ref:`value<test_values_of_a_dictionary>` as what is given in the call to the ``factory`` :ref:`function<what is a function?>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 11

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 3

    E       - {'first_name': 'jane', 'last_name': 'doe'}
    E       + {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M'}
    E       ?                                          ++++++++++++

* I add a new :ref:`key<test_keys_of_a_dictionary>` to the `return statement`_ in ``person.py``

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

  the test passes

* I add a :ref:`variable<what is a variable?>` to remove the repetition of the value for ``sex`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

        def test_factory_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'M'

            self.assertEqual(

* I use the :ref:`variable<what is a variable?>` in the call to ``src.person.factory`` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5-6

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    last_name=last_name,
                    # sex='M',
                    sex=sex,
                    year_of_birth=this_year(),
                ),

  the test is still green

* I use the :ref:`variable<what is a variable?>` in the expected :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 4-5

                dict(
                    first_name=first_name,
                    last_name=last_name,
                    # sex='M',
                    sex=sex,
                )

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 11

        def test_factory_takes_keyword_arguments(self):
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


    # Exceptions seen

* I change the value of the ``sex`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

        def test_factory_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 5

    E       - {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M'}
    E       ?                                                    ^
    E
    E       + {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'}
    E       ?                                                    ^

* I change the `return statement`_ in ``person.py``

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

----

* I want the ``factory`` :ref:`function<what is a function?>` to return the age of the person it makes. I add a :ref:`key<test_keys_of_a_dictionary>` to the expectation in ``test_person.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 12

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

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'

  :ref:`I cannot do arithmetic with None<test_calculator_raises_type_error>` and I want the value for this year

* I add an `import statement`_ for the `datetime module`_ at the top of ``test_person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import datetime
    import src.person
    import unittest


    def this_year():
        return None

  datetime_ is a :ref:`module<what is a module?>` from the `Python standard library`_ that is used for dates and times

* I change the `return statement`_ in the ``this_year`` :ref:`function <what is a function?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def this_year():
        return datetime.datetime.now().year

  .. TIP:: I can also use the `today method`_ to get the same value

    .. code-block:: python
      :lineno-start: 6
      :emphasize-lines: 2

      def this_year():
          return datetime.datetime.today().year

  The terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 3

    E       - {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'}
    E       + {'age': 0, 'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'}
    E       ?  ++++++++++

  the new :ref:`dictionary<dictionaries>` has a :ref:`value<test_values_of_a_dictionary>` for the ``'age'`` :ref:`key<test_keys_of_a_dictionary>`.

  Here is what ``datetime.datetime.now().year`` or ``datetime.datetime.today().year`` means

  - ``datetime`` is the `datetime module`_
  - ``.datetime`` is a call to the `datetime object`_ in the `datetime module`_. Wait a minute, that is the same name again. Do I have to remember all this?
  - ``.now()`` is a call to the `now method`_ of the `datetime.datetime object`_ from the `datetime module`_, it returns a `datetime.datetime object`_. Oh boy
  - ``.today()`` is a call to the `today method`_ of the `datetime.datetime object`_ from the `datetime module`_, it returns a `datetime.datetime object`_
  - ``.year`` asks for the value of the ``year`` :ref:`class attribute<test_attribute_error_w_class_attributes>` of the `datetime.datetime object`_ returned by the `now method`_ or `today method`_ of the `datetime.datetime object`_ from the `datetime module`_

  that was a lot of words, they become clearer in the chapters on :ref:`classes<what is a class?>` and :ref:`AttributeError<what causes AttributeError?>`.


* I add a :ref:`key<test_keys_of_a_dictionary>` for ``age`` to the `return statement`_ in ``person.py``

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

* I add a :ref:`variable<what is a variable?>` for ``year_of_birth`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 5

        def test_factory_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = this_year()

            self.assertEqual(

* I use the :ref:`variable<what is a variable?>` in the call to ``src.person.factory`` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 6-7

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    # year_of_birth=this_year(),
                    year_of_birth=year_of_birth,
                ),

  the test is still green

* I use the :ref:`variable<what is a variable?>` in the expected :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 5-6

                dict(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    # age=this_year()-this_year(),
                    age=this_year()-year_of_birth,
                )

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 12

        def test_factory_takes_keyword_arguments(self):
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


    # Exceptions seen

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* the only difference between the call to the ``factory`` :ref:`function<what is a function?>` and the expected :ref:`dictionary<what is a dictionary?>` in the :ref:`assertion<what is an assertion?>` is that one has a year of birth and the other does a calculation with the year of birth. The other things are the same. I add a :ref:`dictionary<what is a dictionary?>` to remove the repetition

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 6-10

        def test_factory_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = this_year()
            a_person = dict(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
            )

            self.assertEqual(

* I use the new :ref:`variable<what is a variable?>` with a starred expression in the call to ``src.function.factory`` like I did in :ref:`test_functions_w_unknown_arguments`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-6

            self.assertEqual(
                src.person.factory(
                    # first_name=first_name,
                    # last_name=last_name,
                    # sex=sex,
                    **a_person,
                    year_of_birth=year_of_birth,
                ),

  the test is still green

* I do the same thing in the expectation

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2-5

                dict(
                    # first_name=first_name,
                    # last_name=last_name,
                    # sex=sex,
                    **a_person,
                    age=this_year()-year_of_birth,
                )

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 23

            self.assertEqual(
                src.person.factory(
                    **a_person,
                    year_of_birth=year_of_birth,
                ),
                dict(
                    **a_person,
                    age=this_year()-year_of_birth,
                )
            )
  green

* I use the values of ``first_name``, ``last_name`` and the ``sex`` :ref:`variables<what is a variable?>` in the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 7-12

        def test_factory_takes_keyword_arguments(self):
            first_name = 'jane'
            last_name = 'doe'
            sex = 'F'
            year_of_birth = this_year()
            a_person = dict(
                # first_name=first_name,
                # last_name=last_name,
                # sex=sex,
                first_name='jane',
                last_name='doe',
                sex='F',
            )

  still green

* I remove the commented lines and the ``first_name``, ``last_name`` and ``sex`` :ref:`variables<what is a variable?>` since they are no longer used

  .. code-block:: python
    :lineno-start: 12

        def test_factory_takes_keyword_arguments(self):
            year_of_birth = this_year()
            a_person = dict(
                first_name='jane',
                last_name='doe',
                sex='F',
            )

            self.assertEqual(
                src.person.factory(
                    **a_person,
                    year_of_birth=year_of_birth,
                ),
                dict(
                    **a_person,
                    age=this_year()-year_of_birth,
                )
            )


    # Exceptions seen

  green

----

*********************************************************************************
test factory with random values
*********************************************************************************

I want to use random values in the test. I add an `import statement`_ at the top of ``test_person.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2

  import datetime
  import random
  import src.person
  import unittest

random_ is a :ref:`module<what is a module?>` from the `Python standard library`_ that is used to make fake random numbers

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I use a random integer_ for the ``year_of_birth`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2-5

        def test_factory_takes_keyword_arguments(self):
            # year_of_birth = this_year()
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            a_person = dict(

  Here is what the new line means

  - ``random`` is the `random module`_
  - ``.randint`` is a call to the `randint method`_ from the `random module`_. Okay, this one does not use the same name again
  - ``this_year()-120`` returns this year minus ``120``
  - ``this_year()`` returns ``datetime.datetime.now().year`` which is the value for the current year
  - ``random.randint(this_year()-120, this_year())`` gives me a random number from 120 years ago, up to and also the current year which is returned by the call to ``this_year()``

* I use :kbd:`ctrl+s` (Windows_/Linux_) or :kbd:`command+s` (MacOS_) to save the file_ a few times to run the tests. When the age is not ``0``, the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 5

    E       - {'age': 0, 'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'}
    E       ?         ^
    E
    E       + {'age': X, 'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'}
    E       ?         ^

  .. NOTE:: ``X`` is for the random age

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the age calculation from ``test_person.py`` to the `return statement`_ in ``person.py``

  .. code-block:: python
    :linenos:
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

  .. code-block:: python

    NameError: name 'this_year' is not defined

  because I used a name that is not defined in ``person.py``

* I use the `return statement`_ of the ``this_year()`` :ref:`function<what is a function?>` from ``test_person.py`` to change ``this_year()`` in ``person.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 5
    :emphasize-text: datetime now

        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'F,
            'age': datetime.datetime.now().year - year_of_birth,
        }

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

* I add an `import statement`_ for the `datetime module`_ at the top of ``person.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import datetime


    def factory(

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented ``# year_of_birth = this_year()`` line from ``test_person.py``

* I add randomness to the ``sex`` :ref:`key<test_keys_of_a_dictionary>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 8-9
    :emphasize-text: ) ,

        def test_factory_takes_keyword_arguments(self):
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            a_person = dict(
                first_name='jane',
                last_name='doe',
                # sex='F',
                sex=random.choice(('F', 'M')),
            )

            self.assertEqual(

  - ``random`` is the `random module`_
  - ``.choice`` is a call to the `random.choice method`_ from the `random module`_, it returns a random value from the :ref:`iterable<what is an iterable?>` it is given in parentheses
  - ``('F', 'M')`` is a tuple_ with values for the `random.choice method`_ to choose from randomly
  - ``random.choice(('F', 'M'))`` randomly gives me ``F`` or ``M`` every time the test runs

* I use :kbd:`ctrl+s` (Windows_/Linux_) or :kbd:`command+s` (MacOS_) to run the test a few times and it passes when ``sex`` is randomly ``'F'``.

  When ``sex`` is randomly ``'M'``, the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 5

    E       - {'age': X, 'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'}
    E       ?                                                              ^
    E
    E       + {'age': X, 'first_name': 'jane', 'last_name': 'doe', 'sex': 'M'}
    E       ?                                                              ^

* I add the ``sex`` input parameter instead of a value that does not change to the `return statement`_ in ``person.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 4

        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': sex,
            'age': datetime.datetime.now().year - year_of_birth,
        }

  the test passes with no more random failures

* I remove ``# sex = 'F'`` from ``test_person.py``

----

* I use `random.choice`_ with the ``last_name`` :ref:`key<test_keys_of_a_dictionary>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3-6
    :emphasize-text: ) ,

            a_person = dict(
                first_name='jane',
                # last_name='doe',
                last_name=random.choice((
                    'doe', 'smith', 'blow', 'public',
                )),
                sex=random.choice(('F', 'M')),
            )

* I use :kbd:`ctrl+s` (Windows_/Linux_) or :kbd:`command+s` (MacOS_) to run the test a few times and it passes when ``last_name`` is ``'doe'``.

  When ``last_name`` is not ``doe``, the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 5

    E       - {'age': X, 'first_name': 'jane', 'last_name': 'doe', 'sex': A}
    E       ?                                                ^^^
    E
    E       + {'age': X, 'first_name': 'jane', 'last_name': Z, 'sex': A}
    E       ?                                               ^

  .. NOTE:: ``Z`` is for the random last name and ``A`` is for the random sex value

* I use the ``last_name`` input parameter as the :ref:`value<test_values_of_a_dictionary>` for the ``'last_name'`` :ref:`key<test_keys_of_a_dictionary>` in the `return statement`_ in ``person.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3

        return {
            'first_name': 'jane',
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  and the test is green again

----

* I remove ``# last_name = 'doe'`` then add randomness to the ``first_name`` :ref:`key<test_keys_of_a_dictionary>` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2-5
    :emphasize-text: ) ,

            a_person = dict(
                # first_name='jane',
                first_name=random.choice((
                    'jane', 'joe', 'john', 'person',
                )),
                last_name=random.choice((
                    'doe', 'smith', 'blow', 'public',
                )),
                sex=random.choice(('F', 'M')),
            )

  I use :kbd:`ctrl+s` (Windows_/Linux_) or :kbd:`command+s` (MacOS_) to run the test a few times and it passes when ``first_name`` is ``'jane'``.

  When ``first_name`` is not ``'jane'`` the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 5

    E       - {'age': X, 'first_name': 'jane', 'last_name': Z, 'sex': A}
    E       ?                          ^^^^^^
    E
    E       + {'age': X, 'first_name': Y, 'last_name': Z, 'sex': A}
    E       ?                          ^

  .. NOTE:: ``Y`` is for the random first name

* I add the ``first_name`` input parameter to the `return statement`_ in ``person.py``

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

  the test passes

* I remove the commented line ``# first_name = 'jane'`` from ``test_person.py``

* I add a :ref:`function<what is a function?>` for the calls to the `random.choice method`_ with a starred expression like in :ref:`test_functions_w_unknown_arguments`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    import unittest


    def choose(*choices):
        return random.choice(choices)


    def this_year():

* I use the new :ref:`function<what is a function?>` in the test

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-11
    :emphasize-text: ) ,

            a_person = dict(
                # first_name=random.choice((
                #     'jane', 'joe', 'john', 'person',
                # )),
                # last_name=random.choice((
                #     'doe', 'smith', 'blow', 'public',
                # )),
                # sex=random.choice(('F', 'M')),
                first_name=choose('jane', 'joe', 'john', 'person'),
                last_name=choose('doe', 'smith', 'blow', 'public'),
                sex=choose('F', 'M'),
            )

            self.assertEqual(

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 17

        def test_factory_takes_keyword_arguments(self):
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            a_person = dict(
                first_name=choose('jane', 'joe', 'john', 'person'),
                last_name=choose('doe', 'smith', 'blow', 'public'),
                sex=choose('F', 'M'),
            )

            self.assertEqual(
                src.person.factory(
                    **a_person,
                    year_of_birth=year_of_birth,
                ),
                dict(
                    **a_person,
                    age=this_year()-year_of_birth,
                )
            )


    # Exceptions seen

  still green

----

*************************************************************************************
test_factory_w_default_arguments
*************************************************************************************

I want to see what happens when I try to make a person without a value for the ``last_name`` argument

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I copy ``test_factory_takes_keyword_arguments`` and paste it below in ``test_person.py``
* I change the name of the new test to ``test_factory_w_default_arguments``, then comment out the ``last_name`` :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in the ``a_person`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 12-20, 22-31

            self.assertEqual(
                src.person.factory(
                    **a_person,
                    year_of_birth=year_of_birth,
                ),
                dict(
                    **a_person,
                    age=this_year()-year_of_birth,
                )
            )

        def test_factory_w_default_arguments(self):
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            a_person = dict(
                first_name=choose('jane', 'joe', 'john', 'person'),
                # last_name=choose('doe', 'smith', 'blow', 'public'),
                sex=choose('F', 'M'),
            )

            self.assertEqual(
                src.person.factory(
                    **a_person,
                    year_of_birth=year_of_birth,
                ),
                dict(
                    **a_person,
                    age=this_year()-year_of_birth,
                )
            )


    # Exceptions seen

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() missing 1 required positional argument: 'last_name'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a default value for ``last_name`` in the ``factory`` :ref:`function<what is a function?>` in ``person.py`` to make it a choice

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2

    def factory(
            first_name, last_name=None,
            sex, year_of_birth,
        ):

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  I cannot put a parameter that does NOT have a default value after a parameter that has a default value

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen in ``test_person.py``

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I add a default value for ``sex`` in the ``factory`` :ref:`function<what is a function?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    def factory(
            first_name, last_name=None,
            sex=None, year_of_birth,
        ):

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

* I add a default value for ``year_of_birth``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    def factory(
            first_name, last_name=None,
            sex=None, year_of_birth=None,
        ):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block::
    :emphasize-lines: 2

    E       - {'age': X, 'first_name': Y, 'last_name': None, 'sex': 'F'}
    E       ?                           -------------------
    E
    E       + {'age': X, 'first_name': Y, 'sex': 'F'

  .. NOTE:: ``X`` is for the random age, ``Y`` is for the random first name

  the ``factory`` :ref:`function<what is a function?>` returns a :ref:`dictionary<what is a dictionary?>` with a :ref:`key<test_keys_of_a_dictionary>` called ``'last_name'``, the test does not expect a :ref:`dictionary<what is a dictionary?>` with a :ref:`key<test_keys_of_a_dictionary>` called ``'last_name'``

* I add a :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` for ``last_name`` in the expectation of ``test_factory_w_default_arguments`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 3

                dict(
                    **a_person,
                    last_name='doe',
                    age=this_year()-year_of_birth,
                )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block::
    :emphasize-lines: 2, 5

    E       - {'age': X, 'first_name': Y, 'last_name': None, 'sex': A}
    E       ?                                          ^ -
    E
    E       + {'age': X, 'first_name': Y, 'last_name': 'doe', 'sex': A}
    E       ?                                          ^^  +

  the ``factory`` :ref:`function<what is a function?>` returns a :ref:`dictionary<dictionaries>` with a :ref:`value<test_values_of_a_dictionary>` of :ref:`None<what is None?>` for ``last_name`` and the test expects ``'doe'``

* I change the default value for ``last_name`` in the ``factory`` :ref:`function<what is a function?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2

    def factory(
            first_name, last_name='doe',
            sex=None, year_of_birth=None,
        ):

  the test passes

  .. NOTE:: When the ``factory`` :ref:`function<what is a function?>` is called with no value for the ``last_name`` argument, it uses ``'doe'`` because that is the default value in the :ref:`function<what is a function?>` definition, it is the same as calling it with ``last_name='doe'``

    .. code-block:: python
      :emphasize-lines: 5

      src.person.factory(
          first_name=first_name,
          sex=sex,
          year_of_birth=year_of_birth,
          last_name='doe',
      )

    see :ref:`test_functions_w_default_arguments` for more

----

* I remove the commented line from ``test_factory_w_default_arguments`` in ``test_person.py``

* I comment out the ``sex`` :ref:`key<test_keys_of_a_dictionary>` in ``test_factory_w_default_arguments`` to see what happens when I call the ``factory`` :ref:`function<what is a function?>` without it

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 7

        def test_factory_w_default_arguments(self):
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            a_person = dict(
                first_name=choose('jane', 'joe', 'john', 'person'),
                # sex=choose('F', 'M'),
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2

    E       - {'age': X, 'first_name': Y, 'last_name': 'doe', 'sex': None}
    E       ?                                               -------------
    E
    E       + {'age': X, 'first_name': Y, 'last_name': 'doe'}

  the ``factory`` :ref:`function<what is a function?>` returns a :ref:`dictionary<what is a dictionary?>` with a :ref:`key<test_keys_of_a_dictionary>` called ``'sex'``, the test does not expect a :ref:`dictionary<what is a dictionary?>` with a :ref:`key<test_keys_of_a_dictionary>` called ``'sex'``

* I add a :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` for ``sex`` in the expectation of ``test_factory_w_default_arguments`` in ``test_person.py``

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 4

                dict(
                    **a_person,
                    last_name='doe',
                    sex='M',
                    age=this_year()-year_of_birth,
                )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 5

    E       - {'age': X, 'first_name': Y, 'last_name': Z, 'sex': None}
    E       ?                                                    ^^^^
    E
    E       + {'age': X, 'first_name': Y, 'last_name': Z, 'sex': 'M'}
    E       ?                                                    ^^^

  the ``factory`` :ref:`function<what is a function?>` returns a :ref:`dictionary<dictionaries>` with a :ref:`value<test_values_of_a_dictionary>` of :ref:`None<what is None?>` for ``sex`` and the test expects ``'M'``

* I change the default value for ``sex`` in the ``factory`` :ref:`function<what is a function?>` in ``person.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    def factory(
            first_name, last_name='doe',
            sex='M', year_of_birth=None,
        ):

  the test passes

  .. NOTE:: When the ``factory`` :ref:`function<what is a function?>` is called with no value for the ``sex`` argument, it uses ``'M'`` because that is the default value in the :ref:`function<what is a function?>` definition, it is the same as calling it with ``sex='M'``

    .. code-block:: python
      :emphasize-lines: 5

      src.person.factory(
          first_name=first_name,
          year_of_birth=year_of_birth,
          last_name='doe',
          sex='M',
      )

    since the values are the same as the default values, I can call the :ref:`function<what is a function?>` without them

    .. code-block:: python
      :emphasize-lines: 2-3

      src.person.factory(
          first_name=first_name,
          year_of_birth=year_of_birth,
      )

    see :ref:`test_functions_w_default_arguments` for more

----

* I remove the commented line ``# sex=choose('F', 'M'),`` from ``test_factory_w_default_arguments`` in ``test_person.py``

* I do not need the ``a_person`` :ref:`dictionary<what is a dictionary?>` in ``test_factory_w_default_arguments`` because it has only one :ref:`key<test_keys_of_a_dictionary>`. I can use a :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 4

            a_person = dict(
                first_name=choose('jane', 'joe', 'john', 'person'),
            )
            first_name = choose('jane', 'joe', 'john', 'person')

            self.assertEqual(

* I use the :ref:`variable<what is a variable?>` in the call to ``src.person.factory`` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 4

            self.assertEqual(
                src.person.factory(
                    **a_person,
                    first_name=first_name,
                    year_of_birth=year_of_birth,
                ),

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: src.person.factory() got multiple values for keyword argument 'first_name'

  because the ``**a_person`` :ref:`dictionary<what is a dictionary?>` has a :ref:`key<test_keys_of_a_dictionary>` called ``first_name``, the call to ``src.person.factory`` gets called with the same name two times

* I comment out ``a_person,`` in the call to ``src.person.factory``

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 3

            self.assertEqual(
                src.person.factory(
                    # **a_person,
                    first_name=first_name,
                    year_of_birth=year_of_birth,
                ),

  the terminal_ randomly shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 5

    E       - {'age': X, 'first_name': Y, 'last_name': 'doe', 'sex': 'M'}
    E       ?                          ^
    E
    E       + {'age': X, 'first_name': B, 'last_name': 'doe', 'sex': 'M'}
    E       ?                          ^

  because the :ref:`values<test_values_of_a_dictionary>` for ``first_name`` randomly change in both :ref:`dictionaries<what is a dictionary?>`

* I use the ``first_name`` :ref:`variable<what is a variable?>` in the expectation

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 3

                dict(
                    **a_person,
                    first_name=first_name,
                    last_name='doe',
                    sex='M',
                    age=this_year()-year_of_birth,
                )

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: dict() got multiple values for keyword argument 'first_name'

* I comment out ``**a_person,`` in the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2

                  dict(
                      # **a_person,
                      first_name=first_name,
                      last_name='doe',
                      sex='M',
                      age=this_year()-year_of_birth,
                  )

  the test passes

* I remove the commented lines and the ``a_person`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 38

        def test_factory_w_default_arguments(self):
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            first_name = choose('jane', 'joe', 'john', 'person')

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


    # Exceptions seen

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* ``first_name`` and ``year_of_birth`` are made the same way in both tests. I add  the `setUp method`_ to the ``TestPerson`` :ref:`class<what is a class?>` with a :ref:`class attribute (variable)<test_attribute_error_w_class_attributes>` to remove the repetition of the ``year_of_birth`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3-6

    class TestPerson(unittest.TestCase):

        def setUp(self):
            self.random_year_of_birth = random.randint(
                this_year()-120, this_year()
            )

        def test_factory_takes_keyword_arguments(self):

  I can use the :ref:`class attribute<test_attribute_error_w_class_attributes>` directly

* I point ``year_of_birth`` in ``test_factory_takes_keyword_arguments`` to the :ref:`class attribute<test_attribute_error_w_class_attributes>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2-5

        def test_factory_takes_keyword_arguments(self):
            # year_of_birth = random.randint(
            #     this_year()-120, this_year()
            # )
            year_of_birth = self.random_year_of_birth
            a_person = dict(

  the test is still green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the call to ``src.person.factory`` in  the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 4-5

            self.assertEqual(
                src.person.factory(
                    **a_person,
                    # year_of_birth=year_of_birth,
                    year_of_birth=self.random_year_of_birth,
                ),

  still green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the expectation

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3-4

                dict(
                    **a_person,
                    # age=this_year()-year_of_birth,
                    age=this_year()-self.random_year_of_birth,
                )

  green

* I remove the commented lines and the ``year_of_birth`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 22

        def test_factory_takes_keyword_arguments(self):
            a_person = dict(
                first_name=choose('jane', 'joe', 'john', 'person'),
                last_name=choose('doe', 'smith', 'blow', 'public'),
                sex=choose('F', 'M'),
            )

            self.assertEqual(
                src.person.factory(
                    **a_person,
                    year_of_birth=self.random_year_of_birth,
                ),
                dict(
                    **a_person,
                    age=this_year()-self.random_year_of_birth,
                )
            )

        def test_factory_w_default_arguments(self):

* I point the ``year_of_birth`` :ref:`variable<what is a variable?>` in ``test_factory_w_default_arguments`` to the :ref:`class attribute<test_attribute_error_w_class_attributes>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 2-5

        def test_factory_w_default_arguments(self):
            # year_of_birth = random.randint(
            #     this_year()-120, this_year()
            # )
            year_of_birth = self.random_year_of_birth
            first_name = choose('jane', 'joe', 'john', 'person')

  the test is still green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the call to ``src.person.factory`` in  the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 4-5

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    # year_of_birth=year_of_birth,
                    year_of_birth=self.random_year_of_birth,
                ),

  still green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 5-6

                dict(
                    first_name=first_name,
                    last_name='doe',
                    sex='M',
                    # age=this_year()-year_of_birth,
                    age=this_year()-self.random_year_of_birth,
                )

  green

* I remove the commented lines and the ``year_of_birth`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 40

        def test_factory_w_default_arguments(self):
            first_name = choose('jane', 'joe', 'john', 'person')

            self.assertEqual(
                src.person.factory(
                    first_name=first_name,
                    year_of_birth=self.random_year_of_birth,
                ),
                dict(
                    first_name=first_name,
                    last_name='doe',
                    sex='M',
                    age=this_year()-self.random_year_of_birth,
                )
            )


    # Exceptions seen

  the tests are still green

----

* I add a :ref:`class attribute (variable)<test_attribute_error_w_class_attributes>` for ``first_name`` to the `setUp method`_ to remove repetition of the :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5

        def setUp(self):
            self.random_year_of_birth = random.randint(
                this_year()-120, this_year()
            )
            self.random_first_name = choose('jane', 'joe', 'john', 'person')

        def test_factory_takes_keyword_arguments(self):

  I can use the :ref:`class attribute<test_attribute_error_w_class_attributes>` directly

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` as the :ref:`value<test_values_of_a_dictionary>` for the ``first_name`` :ref:`key<test_keys_of_a_dictionary>` in the ``a_person`` :ref:`dictionary<what is a dictionary?>` in ``test_factory_takes_keyword_arguments``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-4

        def test_factory_takes_keyword_arguments(self):
            a_person = dict(
                # first_name=choose('jane', 'joe', 'john', 'person'),
                first_name=self.random_first_name,
                last_name=choose('doe', 'smith', 'blow', 'public'),
                sex=choose('F', 'M'),
            )

  the test is still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 21

        def test_factory_takes_keyword_arguments(self):
            a_person = dict(
                first_name=self.random_first_name,
                last_name=choose('doe', 'smith', 'blow', 'public'),
                sex=choose('F', 'M'),
            )

            self.assertEqual(
                src.person.factory(
                    **a_person,
                    year_of_birth=self.random_year_of_birth,
                ),
                dict(
                    **a_person,
                    age=this_year()-self.random_year_of_birth,
                )
            )

        def test_factory_w_default_arguments(self):

  still green

* I point the ``first_name`` :ref:`variable<what is a variable?>` in ``test_factory_w_default_arguments`` to the :ref:`class attribute<test_attribute_error_w_class_attributes>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2-3

        def test_factory_w_default_arguments(self):
            # first_name = choose('jane', 'joe', 'john', 'person')
            first_name = self.random_first_name

            self.assertEqual(

  green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the call to ``src.person.factory`` in  the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 3-4

            self.assertEqual(
                src.person.factory(
                    # first_name=first_name,
                    first_name=self.random_first_name,
                    year_of_birth=self.random_year_of_birth,
                ),

  still green

* I use the :ref:`class attribute<test_attribute_error_w_class_attributes>` in the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2-3

                dict(
                    # first_name=first_name,
                    first_name=self.random_first_name,
                    last_name='doe',
                    sex='M',
                    age=this_year()-self.random_year_of_birth,
                )

  the test is still green

* I remove the commented lines and the ``first_name`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 41

        def test_factory_w_default_arguments(self):
            self.assertEqual(
                src.person.factory(
                    first_name=self.random_first_name,
                    year_of_birth=self.random_year_of_birth,
                ),
                dict(
                    first_name=self.random_first_name,
                    last_name='doe',
                    sex='M',
                    age=this_year()-self.random_year_of_birth,
                )
            )


    # Exceptions seen

  the tests are still green

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

* I close ``test_person.py`` in the :ref:`editor<2 editors>`
* then I delete all the text in ``person.py``. The terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.person' has no attribute 'factory'

  there is nothing in ``person.py`` with the name ``factory``

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

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'factory' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    factory = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  ``factory`` points to :ref:`None<what is None?>` which is not callable_ like a :ref:`function<what is a function?>`

* I make ``factory`` a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def factory():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'first_name'

  the test called the :ref:`function<what is a function?>` with a :ref:`keyword argument<test_functions_w_keyword_arguments>`

* I add ``first_name`` to the :ref:`function<what is a function?>` definition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def factory(first_name):
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'year_of_birth'

  the test called the :ref:`function<what is a function?>` with another :ref:`keyword argument<test_functions_w_keyword_arguments>`

* I add ``year_of_birth`` to the :ref:`function<what is a function?>` definition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def factory(first_name, year_of_birth):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != {'first_name': X, 'last_name': 'doe', 'sex': 'M', 'age': A}

  the tests expect a :ref:`dictionary<what is a dictionary?>` and the ``factory`` :ref:`function<what is a function?>` returns :ref:`None<what is None?>`

* I make the :ref:`function<what is a function?>` return a :ref:`dictionary<what is a dictionary?>` instead of :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-7

    def factory(first_name, year_of_birth):
        return {
            'first_name': 'john',
            'last_name': 'doe',
            'sex': 'M',
            'age': 55,
        }

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. ATTENTION:: Some of your values will be different because the test uses random values

  .. code-block:: shell

    E       - {'age': 55, 'first_name': 'john', 'last_name': 'doe', 'sex': 'M'}
    E       ?         ^^                  ^^
    E
    E       + {'age': X, 'first_name': Y, 'last_name': 'doe', 'sex': 'M'}
    E       ?         ^                ^

  the :ref:`values<test_values_of_a_dictionary>` of the ``age`` and ``first_name`` :ref:`keys<test_keys_of_a_dictionary>` change randomly

* I use the ``first_name`` input parameter in the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def factory(first_name, year_of_birth):
        return {
            'first_name': first_name,
            'last_name': 'doe',
            'sex': 'M',
            'age': 55,
        }

  the first name matches and when the ages are different, the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    E       - {'age': 55, 'first_name': Y, 'last_name': 'doe', 'sex': A}
    E       ?         ^^
    E
    E       + {'age': X, 'first_name': Y, 'last_name': 'doe', 'sex': A}
    E       ?         ^

  sometimes the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: factory() got an unexpected keyword argument 'last_name'. Did you mean 'first_name'?

* I use the ``year_of_birth`` input parameter in the `return statement`_ for the :ref:`value<test_values_of_a_dictionary>` of ``age``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6

    def factory(first_name, year_of_birth):
        return {
            'first_name': first_name,
            'last_name': 'doe',
            'sex': 'M',
            'age': year_of_birth,
        }

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 5

    E       - {'age': ABCD, 'first_name': 'john', 'last_name': 'doe', 'sex': 'M'}
    E       ?         ^^^^
    E
    E       + {'age': X, 'first_name': 'john', 'last_name': 'doe', 'sex': 'M'}
    E       ?         ^

  the :ref:`value<test_values_of_a_dictionary>` the ``factory`` :ref:`function<what is a function?>` returned for the ``age`` :ref:`key<test_keys_of_a_dictionary>` has 4 digits (a year), and the test expects the difference between that :ref:`value<test_values_of_a_dictionary>` and the current year

* I add an `import statement`_ for the `datetime module`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import datetime


    def factory(

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I use the `datetime module`_ to get the current year for the ``age`` calculation

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5

        return {
            'first_name': first_name,
            'last_name': 'doe',
            'sex': 'M',
            'age': datetime.datetime.today().year - year_of_birth,
        }

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: factory() got an unexpected keyword argument 'last_name'. Did you mean 'first_name'?

  the test called the :ref:`function<what is a function?>` with another :ref:`keyword argument<test_functions_w_keyword_arguments>`

* I add a new input parameter to the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1-4
    :emphasize-text: last_name

    def factory(
            first_name, year_of_birth,
            last_name,
        ):
        return {

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() missing 1 required positional argument: 'last_name'

  the test called the :ref:`function<what is a function?>` with another argument and Python_ took it is a positional argument for ``last_name``

* I add a default value for ``last_name`` so Python_ does not take it is a :ref:`positional argument<test_functions_w_positional_arguments>` when a name is not given

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    def factory(
            first_name, year_of_birth,
            last_name=None,
        ):
        return {

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'sex'

  another :ref:`keyword argument<test_functions_w_keyword_arguments>`

* I add the name to the definition of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3
    :emphasize-text: sex

    def factory(
            first_name, year_of_birth,
            last_name=None, sex,
        ):

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  I cannot put a parameter that does NOT have a default value after a parameter that has a default value

* I add a default value for ``sex``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def factory(
            first_name, year_of_birth,
            last_name=None, sex=None,
        ):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    E       - {'age': X, 'first_name': Y, 'last_name': 'doe', 'sex': 'M'}
    E       ?                                           ^^^
    E
    E       + {'age': X, 'first_name': Y, 'last_name': Z, 'sex': A}
    E       ?                                          ^         ^

  the values for ``last_name`` and ``sex`` change  every time the tests run

* I use the ``sex`` input parameter in the `return statement`_

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 4

        return {
            'first_name': first_name,
            'last_name': 'doe',
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 5

    E       - {'age': X, 'first_name': Y, 'last_name': Z, 'sex': None}
    E       ?                                                    ^^^^
    E
    E       + {'age': X, 'first_name': Y, 'last_name': Z, 'sex': 'M'}
    E       ?                                                    ^^^

  the test expects ``'M'`` as the :ref:`value<test_values_of_a_dictionary>` of ``sex`` and the :ref:`function<what is a function?>` returns :ref:`None<what is None?>` which is its default value

* I change the default value of ``sex`` to ``'M'``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    def factory(
            first_name, year_of_birth,
            last_name=None, sex='M',
        ):

  the test passes when the ``last_name`` is randomly ``'doe'``.

  When the ``last_name`` is not ``'doe'``, the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 2, 5

    E       - {'age': X, 'first_name': Y, 'last_name': 'doe', 'sex': A}
    E       ?                                          ^^^^^
    E
    E       + {'age': X, 'first_name': Y, 'last_name': Z, 'sex': A}
    E       ?                                          ^

  the ``last_name`` :ref:`value<test_values_of_a_dictionary>` is different between the two :ref:`dictionaries<what is a dictionary?>`

* I use the ``last_name`` input parameter in the `return statement`_

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3

        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block::
    :emphasize-lines: 2, 5

    E       - {'age': X, 'first_name': Y, 'last_name': None, 'sex': A}
    E       ?                                          ^ -
    E
    E       + {'age': X, 'first_name': Y, 'last_name': 'doe', 'sex': A}
    E       ?                                          ^^  +

  the test expects ``'doe'`` as the :ref:`value<test_values_of_a_dictionary>` of ``last_name`` and the :ref:`function<what is a function?>` returns :ref:`None<what is None?>` which is its default value

* I change the default value for ``last_name`` to match the expectation

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6

    import datetime


    def factory(
            first_name, year_of_birth,
            last_name='doe', sex='M',
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  the test passes with no more random failures. I am getting pretty good at this.

----

This solution only has 2 parameters with default values

.. code-block:: python
  :emphasize-text: None

  def factory(
          first_name, year_of_birth,
          last_name='doe', sex='M',
      ):

which is a little bit different from the first solution where I had 3 parameters with default values

.. code-block:: python
  :emphasize-text: None

  def factory(
          first_name, last_name='doe',
          sex='M', year_of_birth=None,
      ):

new things can be learned from repetition

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``person.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and use :kbd:`q` on the keyboard to leave the tests and the terminal_ goes back to the command line, the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_

.. NOTE:: on Windows_ without `Windows Subsystem for Linux`_

  * the terminal_ shows

    .. code-block:: PowerShell

      (.venv) ...\pumping_python\person

  * I deactivate the `virtual environment`_

    .. code-block:: python
      :emphasize-lines: 1

      deactivate

    the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

    .. code-block:: python

      ...\pumping_python\person

  * I `change directory`_ to the parent of ``person``

    .. code-block:: python
      :emphasize-lines: 1

      cd ..

    the terminal_ shows

    .. code-block:: python

      ...\pumping_python

    I am back in the ``pumping_python`` directory_

----

*************************************************************************************
review
*************************************************************************************

I ran tests to make a :ref:`function<what is a function?>` that takes in :ref:`keyword arguments<test_functions_w_keyword_arguments>` as input, has default values for some of them, performs an action based on an input and returns a :ref:`dictionary <dictionaries>` as output

I also saw the following :ref:`Exceptions<errors>`

* :ref:`AssertionError<what causes AssertionError?>`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError<what causes AttributeError?>`
* :ref:`TypeError`
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

you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<list comprehensions>`
* :ref:`what you can do with Dictionaries<dictionaries>`
* :ref:`how to make dictionaries with functions<how to make a person>`

:ref:`Would you like to put it all together in classes?<what is a class?>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->