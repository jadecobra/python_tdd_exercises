.. include:: ../links.rst

#################################################################################
how to make a person
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/A7bCTJhr14g?si=QRx1U5esOaK7khD8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

This is an exercise in making :doc:`dictionaries </data_structures/dictionaries>`  with :doc:`/functions/functions`, it assumes familiarity with those concepts, but is not required.

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
test_person_factory_w_keyword_arguments
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``person`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh person

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 person

  it makes the folders and files for the project, installs packages, runs the first test and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_person.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_person.py:7`` with the mouse to open it
* then change ``True`` to ``False`` to make the test pass
* and change ``test_failure`` to ``test_person_factory_w_keyword_arguments``

  .. code-block:: python

    class TestPersonFactory(unittest.TestCase):

        def test_person_factory_w_keyword_arguments(self):
            self.assertEqual(person.factory(), None)

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'src' is not defined


green: make it pass
#################################################################################

* I add it to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

* then add an `import statement`_ for the ``person`` module

  .. code-block:: python

    import src.person
    import unittest

  which gives me an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'person' has no attribute 'factory'

* I add it to the list of exceptions

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* then open up ``person.py`` from the ``src`` folder to add a :ref:`function<functions>`

  .. code-block:: python

    def factory():
        return None

  the terminal shows a passing test

* I want the ``factory`` :ref:`function<functions>` to take in a value for a person's first name

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name='first_name'
            ),
            None
        )

  the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'first_name'

* I add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* then add a keyword argument named ``first_name`` to the ``factory`` :ref:`function<functions>`

  .. code-block:: python

    def factory(first_name):
        return None

  and the test passes

* I also want the :ref:`function<functions>` to take a keyword argument named ``last_name``

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name='first_name',
                last_name='last_name'
            ),
            None
        )

  which gives me another :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'last_name'

* when I add the name to the ``factory`` function

  .. code-block:: python

    def factory(first_name, last_name):
        return None

  the terminal shows a passing test

* I want the ``factory`` :ref:`function<functions>` to also take in a keyword argument named ``sex``

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name='first_name',
                last_name='last_name',
                sex='M'
            ),
            None
        )

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'sex'

* I add the name to the :ref:`function<functions>`

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex
        ):
        return None

  and the test is green again

* I also want ``factory`` to take a keyword argument named ``year_of_birth`` and assign it to the result of calling a :ref:`function<functions>` that returns the current year

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=this_year()
            ),
            None
        )

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'this_year' is not defined

* I add a definition for ``this_year`` to the top of ``test_person.py``

  .. code-block:: python

    import unittest
    import src.person


    def this_year():
        return None


    class TestPersonFactory(unittest.TestCase):
    ..

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'year_of_birth'

  when I add the name to the :ref:`function<functions>`

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return None

  the test passes

* I want the ``factory`` :ref:`function<functions>` to return a :ref:`dictionary<dictionaries>` as output, so I change the expectation in the assertion

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=this_year()
            ),
            dict()
        )

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != {}

  when I make the `return statement`_ match the expectation

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {}

  the test is green again

* I want the :ref:`dictionary<dictionaries>` to have a key named ``first_name`` with the same value as was given in the call to the ``factory`` :ref:`function<functions>`

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                last_name='last_name',
                sex='M',
                year_of_birth=this_year()
            ),
            dict(
                first_name='first_name',
            )
        )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {} != {'first_name': 'first_name'}

* I copy the value from the right side and paste it to replace the empty :ref:`dictionary<dictionaries>` in the `return statement`_

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {'first_name': 'first_name'}

  and the test passes

* ``'first_name'`` appears twice in the test, if I have to change it, I have to make the change in 2 places. To follow `The Do Not Repeat Yourself (DRY) Principle`_ I remove the repetition with a variable

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
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

  the terminal still shows green. I now only need to change the value of ``first_name`` in one place

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'jane'
        ...

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'first_name'} != {'first_name': 'jane'}

* I copy the value from the terminal and use it to replace the `return statement`_

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {'first_name': 'jane}

  and the test is green again

* I also want the :ref:`dictionary<dictionaries>` to have a key named ``last_name`` with the same value as was given in the call to the ``factory`` :ref:`function<functions>`

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
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

  which gives me an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane'} != {'first_name': 'jane', 'last_name': 'last_name'}

* I copy the value from the terminal and paste it to replace the `return statement`_

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': 'jane',
            'last_name': 'last_name'
        }

  and the test passes

* there is a repetition for ``last_name`` same as with ``first_name``, I add a variable to remove it

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
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

  then change the value

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = 'doe'
        ...

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'last_name'} != {'first_name': 'jane', 'last_name': 'doe'}

* I copy the value from the terminal and paste it to replace the `return statement`_

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
        }

  and the test passes

* I add a key named ``sex`` to the :ref:`dictionary<dictionaries>` with the same value as was given in the call to the ``factory`` :ref:`function<functions>`

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = 'doe'

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
                sex='M',
            )
        )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe'} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M'}

  I copy the value from the terminal and paste it to replace the `return statement`_

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'M'
        }

  and the terminal shows a passing test

* I remove the repetition in the test by adding a variable

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = 'doe'
        sex = 'M'

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=this_year()
            ),
            dict(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
            )
        )

  and the test is still green

* when I change the value of the ``sex`` variable

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        ...

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M'} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'}

* I add ``age`` to the expectation

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=this_year()
            ),
            dict(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                age=this_year() - this_year(),
            )
        )

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'

  I cannot do subtraction with :ref:`None`

* I add an `import statement`_ for the datetime_ :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

    import datetime
    import src.person
    import unittest

  datetime_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_, that is used for dates and times, I will use it to return the current year

* I change the `return statement`_ in the ``this_year`` :ref:`function <functions>` to add a call that returns the current year

  .. code-block:: python

    def this_year():
        return datetime.datetime.now().year

  ``datetime.datetime.now().year`` returns the ``year`` attribute of the object returned by the ``now`` :ref:`method<functions>` of the ``datetime.datetime`` :ref:`class <classes>`, which is a representation of the current local date and time. I could also use ``today`` instead of ``now`` to get the same value

  .. code-block:: python

    def this_year():
        return datetime.datetime.today().year

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0}

* when I copy the value from the terminal and use it to replace the `return statement`_ in ``factory``

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'F',
            'age': 0
        }

  the test passes

* I add a variable for the year of birth

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
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
                age=this_year() - year_of_birth,
            )
        )

refactor: make it better
#################################################################################

I  want to use random values to test the ``factory`` :ref:`function<functions>` because it returns the same :ref:`dictionary<dictionaries>` every time it is called, I want it to be able to take in different inputs and return them

* first I add a new `import statement`_

  .. code-block:: python

    import datetime
    import random
    import src.person
    import unittest

  random_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_, that is used to make fake random numbers

* I change the ``year_of_birth`` value to use random numbers

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        ...

  ``random.randint(this_year()-120, this_year())`` gives me a random number from 120 year ago up to the current year which is returned by ``this_year()`` and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 2}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 7}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 14}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 60}

  I copy the age calculation from the expectation

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'F',
            'age': this_year() - year_of_birth,
        }

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'this_year' is not defined

  because I called a function that does not exist in ``person.py``. I change ``this_year()`` to the return value from ``test_person_factory_w_keyword_arguments.this_year``

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'F,
            'age': datetime.datetime.now().year - year_of_birth,
        }

  the terminal shows another NameError_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

  I add an `import statement`_ at the beginning of ``person.py``

  .. code-block:: python

    import datetime



    def factory(
    ...

  and the terminal shows a passing test, time for a victory dance

* I use random values for the ``sex`` variable

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = 'doe'
        sex = random.choice(('F', 'M'))
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        ...

  ``random.choice(('F', 'M'))`` gives me a random value from ``F`` or ``M`` and the terminal shows random successes or an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 56} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 56}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 76} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 76}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 109} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 109}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 115} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 115}

  when I change the `return statement`_ to use the input parameter for ``sex``

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': sex,
            'age': datetime.datetime.now().year - year_of_birth,
        }

  the test passes with no more random failures

* I use the `random.choice`_ with the ``last_name`` variable

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = random.choice((
            'doe', 'smith', 'blow', 'public',
        ))
        sex = random.choice(('F', 'M'))
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        ...

  and get random success or an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 51} != {'first_name': 'jane', 'last_name': 'bloggs', 'sex': 'F', 'age': 51}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 54} != {'first_name': 'jane', 'last_name': 'bloggs', 'sex': 'M', 'age': 54}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 110} != {'first_name': 'jane', 'last_name': 'bloggs', 'sex': 'F', 'age': 110}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 116} != {'first_name': 'jane', 'last_name': 'blow', 'sex': 'M', 'age': 116}

  I change the `return statement`_ to use the input parameter for ``last_name``

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': 'jane',
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  and the test is green again

* I use random values for the ``first_name`` variable

  .. code-blocK:: python

    def test_person_factory_w_keyword_arguments(self):
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

  and get a random :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'public', 'sex': 'F', 'age': 6} != {'first_name': 'john', 'last_name': 'public', 'sex': 'F', 'age': 6}
    AssertionError: {'first_name': 'jane', 'last_name': 'smith', 'sex': 'M', 'age': 19} != {'first_name': 'person', 'last_name': 'smith', 'sex': 'M', 'age': 19}
    AssertionError: {'first_name': 'jane', 'last_name': 'public', 'sex': 'M', 'age': 59} != {'first_name': 'person', 'last_name': 'public', 'sex': 'M', 'age': 59}
    AssertionError: {'first_name': 'jane', 'last_name': 'smith', 'sex': 'F', 'age': 117} != {'first_name': 'joe', 'last_name': 'smith', 'sex': 'F', 'age': 117}

  I change the `return statement`_ to use the input parameter for ``first_name``

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  and the test is green again. Time for a victory dance!

----

*************************************************************************************
test_person_factory_w_default_keyword_arguments
*************************************************************************************

I want to see what would happen if I try to make a person without giving a value for the ``last_name``

red: make it fail
#################################################################################

* I make a copy of ``test_person_factory_w_keyword_arguments`` and paste it below
* then change the name to ``test_person_factory_w_default_keyword_arguments`` and remove the ``last_name`` variable

  .. code-block:: python

    def test_person_factory_w_default_keyword_arguments(self):
        first_name = random.choice((
            'john', 'joe', 'jane', 'person',
        ))
        sex = "M"
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
                sex=sex,
            ),
            dict(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                age=this_year() - year_of_birth
            )
        )

  the terminal shows a :ref:`TypeError`

    TypeError: factory() missing 1 required positional argument: 'last_name'

  because I called the ``factory`` :ref:`function<functions>` with 3 arguments in the test but the definition takes 4


green: make it pass
#################################################################################

* I add a default value for ``last_name``

  .. code-block:: python

    def factory(
            first_name, last_name=None,
            sex, year_of_birth
        ):
        ...

  the terminal shows a SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  I broke a Python rule by having a parameter that does not have a default value come after a parameter that has one

* I add it to the list of :ref:`Exceptions<exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* then add a default value for the ``sex`` parameter

  .. code-block:: python

    def factory(
            first_name, last_name=None,
            sex=None, year_of_birth
        ):
        ...

  which gives me another SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  for the ``year_of_birth`` input parameter

* I assign a default value to the ``year_of_birth`` parameter

  .. code-block:: python

    def factory(
            first_name, last_name=None,
            sex=None, year_of_birth=None
        ):
        ...

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'last_name' is not defined

  the ``last_name`` key in the expected :ref:`dictionary<dictionaries>` needs a value

* I set the expectation for ``last_name``

  .. code-block:: python

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

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'joe', 'last_name': None, 'sex': 'F', 'age': 28} != {'first_name': 'joe', 'last_name': 'doe', 'sex': 'F', 'age': 28}
    AssertionError: {'first_name': 'person', 'last_name': None, 'sex': 'M', 'age': 33} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 33}
    AssertionError: {'first_name': 'jane', 'last_name': None, 'sex': 'F', 'age': 70} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 70}
    AssertionError: {'first_name': 'jane', 'last_name': None, 'sex': 'F', 'age': 83} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 83}

  the `factory` :ref:`function<functions>` returns a :ref:`dictionary<dictionaries>` with a value of :ref:`None` for the ``last_name`` and the test expects a value of ``doe``

* When I make the default value for ``last_name`` in the :ref:`function<functions>` match the expectation

  .. code-block:: python

    def factory(
            first_name, last_name='doe',
            sex, year_of_birth
        ):
        ...

  the terminal shows passing tests. When no value is given for the ``last_name`` argument to ``person.factory`` it uses ``'doe'`` because that is the default value in the :ref:`function<functions>` signature, it is same as calling it with ``last_name='doe'``

  .. code-block:: python

    src.person.factory(
        first_name=first_name,
        sex=sex,
        last_name='doe',
        year_of_birth=year_of_birth,
    )

* I want to see what happens if I remove ``sex`` from the :ref:`function<functions>` call then change the expectation

  .. code-block:: python

    def test_person_factory_w_default_keyword_arguments(self):
        first_name = random.choice((
            'john', 'joe', 'jane', 'person',
        ))
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
            ),
            {
                "first_name": first_name,
                "last_name": "doe",
                "sex": 'M',
                "age": this_year() - year_of_birth
            }
        )

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'joe', 'last_name': 'doe', 'sex': None, 'age': 4} != {'first_name': 'joe', 'last_name': 'doe', 'sex': 'M', 'age': 4}
    AssertionError: {'first_name': 'joe', 'last_name': 'doe', 'sex': None, 'age': 32} != {'first_name': 'joe', 'last_name': 'doe', 'sex': 'M', 'age': 32}
    AssertionError: {'first_name': 'john', 'last_name': 'doe', 'sex': None, 'age': 45} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'M', 'age': 45}
    AssertionError: {'first_name': 'john', 'last_name': 'doe', 'sex': None, 'age': 58} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'M', 'age': 58}

  I add a default value to match the expectation

  .. code-block:: python

    def factory(
            first_name, last_name='doe',
            sex='M', year_of_birth=None
        ):
        ...

  and the terminal shows passing tests

refactor: make it better
#################################################################################

* I have duplication for ``first_name`` that I can remove with :ref:`class<classes>` attributes

  .. code-block:: python

    ...
    class TestPerson(unittest.TestCase):

        first_name = random.choice((
            'jane', 'joe', 'john', 'person',
        ))
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )

        ...

  then reference them in the tests

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = self.first_name
        last_name = random.choice((
            'doe', 'smith', 'blow', 'public',
        ))
        sex = random.choice(('F', 'M'))
        year_of_birth = self.year_of_birth

        ...

    def test_person_factory_w_default_keyword_arguments(self):
        first_name = self.first_name
        year_of_birth = self.year_of_birth

  the terminal still shows green

* and I remove the variables because they are no longer needed

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        last_name = random.choice((
            'doe', 'smith', 'blow', 'public',
        ))
        sex = random.choice(('F', 'M'))

        self.assertEqual(
            src.person.factory(
                first_name=self.first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=self.year_of_birth
            ),
            dict(
                first_name=self.first_name,
                last_name=last_name,
                sex=sex,
                age=this_year()-self.year_of_birth,
            )
        )

    def test_person_factory_w_default_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name=self.first_name,
                year_of_birth=self.year_of_birth
            ),
            dict(
                first_name=self.first_name,
                last_name='doe',
                sex='M',
                age=this_year()-self.year_of_birth,
            )
        )

  all tests are still passing, and now both tests have the same values for ``self.first_name`` and ``self.year_of_birth``

* for the values to be different, as they were before I added the :ref:`class<classes>` attributes, I can use the `unittest.TestCase.setUp`_ :ref:`method<functions>` which runs before every test

  .. code-block:: python

    class TestPerson(unittest.TestCase):

        def setUp(self):
            self.first_name = random.choice((
                'jane', 'joe', 'john', 'person',
            ))
            self.year_of_birth = random.randint(
                this_year()-120, this_year()
            )

        ...

  the terminal still shows green

----

*********************************************************************************
test_person_tests
*********************************************************************************

.. _test_person_tests_red:

red: make it fail
#################################################################################

* I close ``test_person.py``
* then delete all the text in ``person.py`` and the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.person' has no attribute 'factory'

  see if you can tell what :ref:`Exceptions<Exceptions>` will show up as I go along

.. _test_person_tests_green:

green: make it pass
#################################################################################

* I add the name

  .. code-block:: python

    factory

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'factory' is not defined

* I assign it to :ref:`None`

  .. code-block:: python

    factory = None

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I make it a :ref:`function<functions>`

  .. code-block:: python

    def factory():
        return None

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'first_name'

  then add the keyword argument to the :ref:`function<functions>`

  .. code-block:: python

    def factory(first_name):
        return None

  which gives me another :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'last_name'

  I add the keyword argument

  .. code-block:: python

    def factory(first_name, last_name):
        return None

  and the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'sex'

  I add the keyword argument

  .. code-block:: python

    def factory(first_name, last_name, sex):
        return None

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'year_of_birth'

  when I add the keyword argument

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return None

  I get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != {'first_name': 'john', 'last_name': 'blow', 'sex': 'M', 'age': 20}
    AssertionError: None != {'first_name': 'john', 'last_name': 'smith', 'sex': 'F', 'age': 31}
    AssertionError: None != {'first_name': 'jane', 'last_name': 'blow', 'sex': 'M', 'age': 55}
    AssertionError: None != {'first_name': 'person', 'last_name': 'smith', 'sex': 'F', 'age': 97}

* I copy the value from the terminal and use it to replace :ref:`None` in the `return statement`_

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': 'john',
            'last_name': 'blow',
            'sex': 'F',
            'age': 20
        }

  the terminal shows another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'blow', 'sex': 'M', 'age': 50}
    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 73}
    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'john', 'last_name': 'bloggs', 'sex': 'F', 'age': 77}
    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'public', 'sex': 'F', 'age': 98}

  the values for ``first_name``, ``last_name``, ``sex`` and ``age`` change

* I make the `return statement`_ use the input parameters for ``first_name``

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': first_name,
            'last_name': 'blow',
            'sex': 'F',
            'age': 20
        }

  and still have an :ref:`AssertionError`

  .. code-block

    AssertionError: {'first_name': 'person', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'person', 'last_name': 'public', 'sex': 'F', 'age': 69}
    AssertionError: {'first_name': 'joe', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'joe', 'last_name': 'blow', 'sex': 'F', 'age': 97}
    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'john', 'last_name': 'smith', 'sex': 'M', 'age': 74}
    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'john', 'last_name': 'public', 'sex': 'F', 'age': 19}

  the ``last_name``, ``sex`` and ``age`` change

* I use the input parameter for ``last_name`` in the `return statement`_

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': 'F',
            'age': 20
        }

  and get another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'blow', 'sex': 'M', 'age': 3}
    AssertionError: {'first_name': 'joe', 'last_name': 'smith', 'sex': 'F', 'age': 20} != {'first_name': 'joe', 'last_name': 'smith', 'sex': 'F', 'age': 118}
    AssertionError: {'first_name': 'joe', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'joe', 'last_name': 'blow', 'sex': 'M', 'age': 19}
    AssertionError: {'first_name': 'joe', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'joe', 'last_name': 'blow', 'sex': 'M', 'age': 95}

  the values for ``sex`` and ``age`` change

* When I use the ``sex`` parameter in the `return statement`_

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': 20
        }

  the terminal shows another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'joe', 'last_name': 'doe', 'sex': 'M', 'age': 20} != {'first_name': 'joe', 'last_name': 'doe', 'sex': 'M', 'age': 1}
    AssertionError: {'first_name': 'joe', 'last_name': 'public', 'sex': 'F', 'age': 20} != {'first_name': 'joe', 'last_name': 'public', 'sex': 'F', 'age': 90}
    AssertionError: {'first_name': 'joe', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'joe', 'last_name': 'blow', 'sex': 'F', 'age': 113}
    AssertionError: {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 20} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 58}

  the ``age`` is different

* I add the input parameter to the `return statement`_

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': year_of_birth,
        }

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'joe', 'last_name': 'doe', 'sex': 'M', 'age': 2022} != {'first_name': 'joe', 'last_name': 'doe', 'sex': 'M', 'age': 2}
    AssertionError: {'first_name': 'jane', 'last_name': 'smith', 'sex': 'M', 'age': 2024} != {'first_name': 'jane', 'last_name': 'smith', 'sex': 'M', 'age': 0}
    AssertionError: {'first_name': 'jane', 'last_name': 'blow', 'sex': 'F', 'age': 1981} != {'first_name': 'jane', 'last_name': 'blow', 'sex': 'F', 'age': 43}
    AssertionError: {'first_name': 'person', 'last_name': 'smith', 'sex': 'M', 'age': 1969} != {'first_name': 'person', 'last_name': 'smith', 'sex': 'M', 'age': 55}

  the ``year_of_birth``is not the ``age`` but the difference between the current year and the ``year_of_birth``

* I add an `import statement`_ for the datetime_ :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

    import datetime


    def factory(
    ...

  then add a call to it for the age calculation

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() missing 2 required positional arguments: 'last_name' and 'sex'

* I add a default value for ``last_name``

  .. code-block:: python

    def factory(
            first_name, last_name=None,
            sex, year_of_birth
        ):
        ...

  and get a SyntaxError_

* When I add a default value for ``sex``

  .. code-block:: python

    def factory(
            first_name, last_name=None,
            sex=None, year_of_birth
        ):
        ...

  the terminal shows another SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

* I add a default value for ``year_of_birth``

  .. code-block:: python

    def factory(
            first_name, last_name=None,
            sex=None, year_of_birth=None
        ):

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'person', 'last_name': None, 'sex': None, 'age': 76} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 76}
    AssertionError: {'first_name': 'john', 'last_name': None, 'sex': None, 'age': 101} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'M', 'age': 101}
    AssertionError: {'first_name': 'joe', 'last_name': None, 'sex': None, 'age': 23} != {'first_name': 'joe', 'last_name': 'doe', 'sex': 'M', 'age': 23}
    AssertionError: {'first_name': 'person', 'last_name': None, 'sex': None, 'age': 29} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 29}

  the values for ``last_name`` and ``sex`` do not match the expectation

* I change the default value for ``last_name``

  .. code-block:: python

    def factory(
            first_name, last_name='doe',
            sex=None, year_of_birth=None
        ):
        ...

  and get another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'john', 'last_name': 'doe', 'sex': None, 'age': 51} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'M', 'age': 51}
    AssertionError: {'first_name': 'joe', 'last_name': 'doe', 'sex': None, 'age': 18} != {'first_name': 'joe', 'last_name': 'doe', 'sex': 'M', 'age': 18}
    AssertionError: {'first_name': 'person', 'last_name': 'doe', 'sex': None, 'age': 3} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 3}
    AssertionError: {'first_name': 'person', 'last_name': 'doe', 'sex': None, 'age': 67} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 67}

* when I make the default value for ``sex`` match the expectation

  .. code-block:: python

    def factory(
            first_name, last_name='doe',
            sex='M', year_of_birth=None
        ):
        ...

  all the tests pass!

*************************************************************************************
review
*************************************************************************************

I ran tests to make a :ref:`function<functions>` that takes in keyword arguments as input, has default values for when one is not given, performs an action based on an input, and returns a :doc:`dictionary </data_structures/dictionaries>` as output. I also encountered the following :ref:`Exceptions<Exceptions>`

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`
* SyntaxError_

Would you like to know :doc:`/how_to/exception_handling_tests`?

----

:doc:`/code/code_person_factory`
