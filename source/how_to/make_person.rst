.. include:: ../links.rst

#################################################################################
how to make a person
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/A7bCTJhr14g?si=QRx1U5esOaK7khD8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

This is an exercise in making :doc:`dictionaries </data_structures/dictionaries>`  with :doc:`/functions/functions`. It assumes familiarity with those concepts, though you can still try out the chapter even if you are not.

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
test_person_factory_w_keyword_arguments
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``person`` as the project name

  .. code-block:: python

    ./makePythonTdd.sh person

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 person

  and it shows an :ref:`AssertionError` after making files and folders for the project

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_person.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_person.py:7`` with the mouse to open it
* and change ``True`` to ``False`` to make ``test_failure`` pass
* then change ``test_failure`` to ``test_person_factory_w_keyword_arguments``

  .. code-block:: python

    class TestPersonFactory(unittest.TestCase):

        def test_person_factory_w_keyword_arguments(self):
            self.assertEqual(person.factory(), None)

  and get a NameError_

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

* then add a keyword argument for ``first_name`` to the ``factory`` :ref:`function<functions>`

  .. code-block:: python

    def factory(first_name=None):
    ...

  and the test passes

* I also want the :ref:`function<functions>` to take a value for a last name and it to the test

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

* after adding a keyword argument for ``last_name``  to the ``factory`` function

  .. code-block:: python

    def factory(first_name=None, last_name=None):
    ...

  the terminal shows a passing test

* I want it to also take in a value for the person's sex

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name='first_name',
                last_name='last_name',
                sex='F'
            ),
            None
        )

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'sex'

* I add the name to the :ref:`function<functions>` with a default value of :ref:`None`

  .. code-block:: python

    def factory(
        first_name=None, last_name=None,
        sex=None
    ):
        return None

  and the test is green again

* I also want the :ref:`function<functions>` to take a value for the year the person was born

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name='first_name',
                last_name='last_name',
                sex='F',
                year_of_birth=this_year()
            ),
            None
        )

  and get a NameError_

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

  which gives me a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'year_of_birth'

  when I add the name to the :ref:`function<functions>`

  .. code-block:: python

    def factory(
        first_name=None, last_name=None,
        sex=None, year_of_birth=None
    ):
        return None

  the test passes

* I change the expectation of the test to a :ref:`dictionary<dictionaries>`

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name='first_name',
                last_name='last_name',
                sex='F',
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
        first_name=None, last_name=None,
        sex=None, year_of_birth=None
    ):
        return {}

  the test is green again

* I want the output to contain the value given for ``first_name``

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                last_name='last_name',
                sex='F',
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

  and the test passes

* there is some repetition in the test. I typed ``'first_name'`` twice, and if I have to change it, will have to do it in 2 places in the test, and again in the ``factory`` :ref:`function<functions>`. To follow the `The Do Not Repeat Yourself (DRY) Principle`_, I will remove this repetition with a variable

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'first_name'

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                last_name='last_name',
                sex='F',
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

* I copy the value from the terminal and use it to replace the `return statement`

  .. code-block:: python

    def factory(
            first_name=None, last_name=None,
            sex=None, year_of_birth=None
        ):
        return {'first_name': 'jane}

  and the test is green again

* I want the output to also have the last name

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'jane'

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                last_name='last_name',
                sex='F',
                year_of_birth=this_year()
            ),
            dict(
                first_name=first_name,
                last_name='last_name',
            )
        )

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane'} != {'first_name': 'jane', 'last_name': 'last_name'}

* I copy the value from the terminal and paste it to replace the `return statement`_

  .. code-block:: python

    def factory(
        first_name=None, last_name=None,
        sex=None, year_of_birth=None
    ):
        return {
            'first_name': 'jane',
            'last_name': 'last_name'
        }

  and the test passes

* I have a repetition and a fixed value in the `return statement`_, I add a variable to remove it from the test

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = 'last_name'

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                last_name=last_name,
                sex='F',
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
            first_name=None, last_name=None,
            sex=None, year_of_birth=None
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
        }

  and the test passes

* I add ``sex`` to the expectation in the test

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = 'doe'

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                last_name=last_name,
                sex='F',
                year_of_birth=this_year()
            ),
            dict(
                first_name=first_name,
                last_name=last_name,
                sex='F',
            )
        )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe'} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'}

  I copy the value from the terminal and paste it to replace the `return statement`_

  .. code-block:: python

    def factory(
            first_name=None, last_name=None,
            sex=None, year_of_birth=None
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'F'
        }

  and the terminal shows a passing test

* I remove the repetition in the test by adding a variable

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
            )
        )

  and the test is still green

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
        first_name=None, last_name=None,
        year_of_birth=None, sex=None
    ):
        return {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0}

  the test passes

* I add a variable to remove the repetition of ``this_year()``

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

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 5}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 6}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 23}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 111}

  I copy the age calculation from the expectation

  .. code-block:: python

    def factory(
            first_name=None, last_name=None,
            sex=None, year_of_birth=None
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': this_year() - year_of_birth,
        }

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'this_year' is not defined

  because I called a function that does not exist in ``person.py``. I change ``this_year()`` to the return value from ``test_person_factory_w_keyword_arguments.this_year``

  .. code-block:: python

    def factory(
            first_name=None, last_name=None,
            sex=None, year_of_birth=None
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
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

  ``random.choice(('F', 'M'))`` gives me a random value from ``F`` or ``M`` and the terminal shows random successes or :ref:`AssertionErrors<AssertionError>`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 15} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 15}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 87} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 87}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 93} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 93}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 94} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 94}

  when I change the `return statement`_ to use the input parameter for ``sex``

  .. code-block:: python

    def factory(
            first_name=None, last_name=None,
            sex=None, year_of_birth=None,
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  the test passes with no more random failures

* I use the `random.choice`_ with the ``last_name`` variable

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = random.choice((
            'doe', 'smith', 'blow', 'public'
        ))
        sex = random.choice(('F', 'M'))
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        ...

  and get random successes or :ref:`AssertionErrors<AssertionError>`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 19} != {'first_name': 'jane', 'last_name': 'blow', 'sex': 'M', 'age': 19}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 60} != {'first_name': 'jane', 'last_name': 'public', 'sex': 'M', 'age': 60}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 77} != {'first_name': 'jane', 'last_name': 'smith', 'sex': 'F', 'age': 77}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 114} != {'first_name': 'jane', 'last_name': 'blow', 'sex': 'M', 'age': 114}

  I change the `return statement`_ to use the input parameter

  .. code-block:: python

    def factory(
            first_name=None, last_name=None,
            sex=None, year_of_birth=None,
        ):
        return {
            'first_name': 'jane',
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  and the test is green again

* I do the same thing for the ``first_name`` variable

  .. code-blocK:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = random.choice((
            'jane', 'joe', 'john', 'person'
        ))
        last_name = random.choice((
            'doe', 'smith', 'blow', 'public'
        ))
        sex = random.choice(('F', 'M'))
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        ...

  and the terminal shows a random :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'public', 'sex': 'F', 'age': 24} != {'first_name': 'person', 'last_name': 'public', 'sex': 'F', 'age': 24}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 35} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 35}
    AssertionError: {'first_name': 'jane', 'last_name': 'smith', 'sex': 'F', 'age': 119} != {'first_name': 'joe', 'last_name': 'smith', 'sex': 'F', 'age': 119}
    AssertionError: {'first_name': 'jane', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'joe', 'last_name': 'blow', 'sex': 'F', 'age': 20}

  I change the `return statement`_ to use the input parameter

  .. code-block:: python

    def factory(
            first_name=None, last_name=None,
            sex=None, year_of_birth=None,
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

I want to see what would happens if I try to make a person without giving a value for the ``last_name``

red: make it fail
#################################################################################

* I make a copy of ``test_person_factory_w_keyword_arguments`` and paste it below
* then change the name to ``test_person_factory_w_default_keyword_arguments`` and remove the ``last_name`` variable

  .. code-block:: python

    def test_person_factory_w_default_keyword_arguments(self):
        first_name = random.choice((
            'john', 'joe', 'jane', 'person'
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
                last_name="doe",
                sex=sex,
                age=this_year() - year_of_birth
            )
        )

  the terminal shows an :ref:`AssertionError` because the value for ``last_name`` does not match the expected value

  .. code-block:: python

    AssertionError: {'first_name': 'john', 'last_name': None, 'sex': 'F', 'age': 1} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'F', 'age': 1}
    AssertionError: {'first_name': 'john', 'last_name': None, 'sex': 'M', 'age': 44} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'M', 'age': 44}
    AssertionError: {'first_name': 'john', 'last_name': None, 'sex': 'F', 'age': 65} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'F', 'age': 65}
    AssertionError: {'first_name': 'john', 'last_name': None, 'sex': 'F', 'age': 118} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'F', 'age': 118}

  the test expects a value of ``"doe"`` but ``person.factory`` returns :ref:`None`

green: make it pass
#################################################################################

* When I make the default value for ``last_name`` in the :ref:`function<functions>` match the expectation

  .. code-block:: python

    def factory(
        first_name=None, last_name='doe',
        year_of_birth=None, sex=None
    ):
    ...

  the terminal shows passing tests. When no value is given for the ``last_name`` argument to ``person.factory`` it uses ``'doe'`` because that is the default value in the :ref:`function<functions>` signature, it is same as calling it with ``last_name='doe'``

* I remove ``sex`` from the :ref:`function<functions>` call then change the expectation

  .. code-block:: python

    def test_person_factory_w_default_keyword_arguments(self):
        first_name = random.choice((
            'john', 'joe', 'jane', 'person'
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

    AssertionError: {'first_name': 'person', 'last_name': 'doe', 'sex': None, 'age': 2} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 2}
    AssertionError: {'first_name': 'person', 'last_name': 'doe', 'sex': None, 'age': 5} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 5}
    AssertionError: {'first_name': 'john', 'last_name': 'doe', 'sex': None, 'age': 68} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'M', 'age': 68}
    AssertionError: {'first_name': 'joe', 'last_name': 'doe', 'sex': None, 'age': 82} != {'first_name': 'joe', 'last_name': 'doe', 'sex': 'M', 'age': 82}

  I add a default value to match the expectation

  .. code-block:: python

    def factory(
            first_name=None, last_name='doe',
            sex='M', year_of_birth=None
        ):
        ...

  and the terminal shows passing tests

refactor: make it better
#################################################################################

* I have duplication for ``first_name`` that I can remove with a :ref:`function<functions>`

  .. code-block:: python

    ...
    import unittest


    def this_year():
    ...


    def a_random_first_name():
        return random.choice((
            'john', 'joe', 'jane', 'person'
        ))



  then add calls to it in both tests

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = a_random_first_name()
        ...

    def test_person_factory_w_default_keyword_arguments(self):
        first_name = a_random_first_name()
        ...

  the terminal still shows passing tests

* I add a :ref:`function<functions>` to remove the duplication of the ``year_of_birth``

  .. code-block:: python

    ...
    def this_year():
        ...


    def a_random_first_name():
        return random.choice((
            'john', 'joe', 'jane', 'person'
        ))


    def a_random_year():
        return random.randint(
            this_year()-120, this_year()
        )


    ...

  then add calls to the :ref:`function<functions>`

  .. code-block:: python

    def test_person_factory_w_keyword_arguments(self):
        first_name = a_random_first_name()
        last_name = random.choice((
            'doe', 'smith', 'blow', 'public'
        ))
        sex = random.choice(('F', 'M'))
        year_of_birth = a_random_year()
        ...

    def test_person_factory_w_default_keyword_arguments(self):
        first_name = a_random_first_name()
        year_of_birth = a_random_year()
        ...

  and all tests are still passing

----

*********************************************************************************
test_person_tests
*********************************************************************************

.. _test_person_tests_red:

red: make it fail
#################################################################################

* I close ``test_person.py``
* then delete the text in ``person.py`` and the terminal shows an :ref:`AttributeError`

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

    def factory(first_name=None):
        return None

  which gives me another :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'last_name'

  I add the keyword argument

  .. code-block:: python

    def factory(first_name=None, last_name=None):
        return None

  and the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'sex'

  I add the keyword argument

  .. code-block:: python

    def factory(
            first_name=None, last_name=None,
            sex=None
        ):
        return None

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'year_of_birth'

  when I add the keyword argument

  .. code-block:: python

    def factory(
            first_name=None, last_name=None,
            sex=None, year_of_birth=None
        ):
        return None

  I get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != {'first_name': 'john', 'last_name': 'smith', 'sex': 'F', 'age': 31}
    AssertionError: None != {'first_name': 'jane', 'last_name': 'blow', 'sex': 'M', 'age': 55}
    AssertionError: None != {'first_name': 'person', 'last_name': 'smith', 'sex': 'F', 'age': 97}
    AssertionError: None != {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20}

* I copy the value from the terminal and use it to replace :ref:`None` in the `return statement`_

  .. code-block:: python

    def factory(
            first_name=None, last_name=None,
            sex=None, year_of_birth=None
        ):
        return {
            'first_name': 'john',
            'last_name': 'blow',
            'sex': 'F',
            'age': 20
        }

  the terminal shows another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'joe', 'last_name': 'public', 'sex': 'M', 'age': 98}
    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 73}
    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'blow', 'sex': 'M', 'age': 50}
    AssertionError: {'first_name': 'john', 'last_name': 'blow', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'public', 'sex': 'F', 'age': 98}

  the values for ``first_name``, ``last_name``, ``sex`` and ``age`` change

* I make the `return statement`_ use the input parameters for ``first_name``

  .. code-block:: python

    def factory(
            first_name=None, last_name=None,
            sex=None, year_of_birth=None
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
            first_name=None, last_name=None,
            sex=None, year_of_birth=None
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

* When I add ``sex`` to the `return statement`_

  .. code-block:: python

    def factory(
            first_name=None, last_name=None,
            sex=None, year_of_birth=None
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
        first_name=None, last_name=None,
        sex=None, year_of_birth=None
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
            first_name=None, last_name=None,
            sex=None, year_of_birth=None
        ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.today().year - year_of_birth,
        }

  and get another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'john', 'last_name': None, 'sex': None, 'age': 12} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'M', 'age': 12}
    AssertionError: {'first_name': 'person', 'last_name': None, 'sex': None, 'age': 48} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 48}
    AssertionError: {'first_name': 'john', 'last_name': None, 'sex': None, 'age': 76} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'M', 'age': 76}
    AssertionError: {'first_name': 'john', 'last_name': None, 'sex': None, 'age': 45} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'M', 'age': 45}

  the values for ``last_name`` and ``sex`` are different, they are both :ref:`None` which is the default value for the keyword arguments

* I change the default value for ``last_name``

  .. code-block:: python

    def factory(
            first_name=None, last_name='doe',
            sex=None, year_of_birth=None
        ):

  and the terminal shows another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'joe', 'last_name': 'doe', 'sex': None, 'age': 22} != {'first_name': 'joe', 'last_name': 'doe', 'sex': 'M', 'age': 22}
    AssertionError: {'first_name': 'person', 'last_name': 'doe', 'sex': None, 'age': 96} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 96}
    AssertionError: {'first_name': 'person', 'last_name': 'doe', 'sex': None, 'age': 117} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 117}
    AssertionError: {'first_name': 'person', 'last_name': 'doe', 'sex': None, 'age': 12} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 12}

* when I make the default value for ``sex`` match the expectation

  .. code-block:: python

    def factory(
            first_name=None, last_name='doe',
            sex='M', year_of_birth=None
        ):

  all the tests pass!

*************************************************************************************
review
*************************************************************************************

I ran the following tests to make a :ref:`function<functions>` that takes in keyword arguments as input, has default values for when a value is not given, performs an action based on an input, and returns a :doc:`dictionary </data_structures/dictionaries>` as output

* `test_person_factory_w_keyword_arguments`_
* `test_person_factory_w_default_keyword_arguments`_

I also encountered the following :ref:`Exceptions<Exceptions>`

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`

Would you like to know :doc:`/how_to/exception_handling_tests`?

----

:doc:`/code/code_person_factory`
