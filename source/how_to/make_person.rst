.. include:: ../links.rst

#################################################################################
how to make a person
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/A7bCTJhr14g?si=QRx1U5esOaK7khD8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

This is an exercise in making :doc:`dictionaries </data_structures/dictionaries>` with :doc:`/functions/functions`

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
test_function_w_keyword_arguments
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``person`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh person

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 person

  it makes the folders and files that are needed, installs packages, runs the first test and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_person.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_person.py:7`` with the mouse to open it
* then change ``True`` to ``False`` to make the test pass
* and change ``test_failure`` to ``test_function_w_keyword_arguments``

  .. code-block:: python

    class TestPersonFactory(unittest.TestCase):

        def test_function_w_keyword_arguments(self):
            self.assertEqual(
                src.person.factory(),
                None
            )

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

* then add an `import statement`_ for the ``person`` :ref:`module<ModuleNotFoundError>`

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

* and open up ``person.py`` from the ``src`` folder to add a :ref:`function<functions>`

  .. code-block:: python

    def factory():
        return None

  the terminal shows a passing test

* I want the :ref:`function<functions>` to take in a keyword argument named ``first_name``

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name='first_name',
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

* then add the name as an input parameter to the :ref:`function<functions>`

  .. code-block:: python

    def factory(first_name):
        return None

  and the test passes

* I also want the :ref:`function<functions>` to take in a keyword argument named ``last_name``

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name='first_name',
                last_name='last_name',
            ),
            None
        )

  which gives me another :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'last_name'

* when I add the name to the :ref:`function<functions>` definition

  .. code-block:: python

    def factory(first_name, last_name):
        return None

  the terminal shows a passing test

* I want the :ref:`function<functions>` to take in a keyword argument named ``sex``

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name='first_name',
                last_name='last_name',
                sex='M',
            ),
            None
        )

  the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'sex'

* I add the name to the :ref:`function<functions>` definition

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex
        ):
        return None

  and the test is green again

* I want the :ref:`function<functions>` to take in a keyword argument and give it the result of calling another :ref:`function<functions>` as the value for it

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
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

* I add the :ref:`function<functions>` above the :ref:`class<classes>` definition

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

  I add the name to the :ref:`function<functions>` definition

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return None

  and the test passes

* I want the ``factory`` :ref:`function<functions>` to return a :ref:`dictionary<dictionaries>` as output, so I change the expectation in the assertion

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=this_year()
            ),
            dict()
        )

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != {}

  when I make the `return statement`_ match the expectation

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {}

  the test passes because ``{}`` and ``dict()`` are the same

* I want the :ref:`dictionary<dictionaries>` to have a key named ``first_name`` with the same value as what was given in the call to the ``factory`` :ref:`function<functions>`

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name='first_name',
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

* I copy the value from the right then use it to replace the empty :ref:`dictionary<dictionaries>` in the `return statement`_

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {'first_name': 'first_name'}

  and the test passes

* ``'first_name'`` appears twice in the test, if I want a different value for it, I have to make a change in two places. I add a variable to remove the repetition

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
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

    def test_function_w_keyword_arguments(self):
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

* I want the :ref:`dictionary<dictionaries>` to have a key named ``last_name`` with the same value as what was given in the call to the ``factory`` :ref:`function<functions>`

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
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

* I copy the value from the terminal then use it to replace the `return statement`_

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': 'jane',
            'last_name': 'last_name'
        }

  and the terminal shows green again

* there is a repetition of ``'last_name'`` so I add a variable to remove it like I did with ``first_name``

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
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

  then I change the value

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = 'doe'
        ...

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'last_name'} != {'first_name': 'jane', 'last_name': 'doe'}

* I copy the value from the terminal then use it to replace the `return statement`_

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

* I add a key named ``sex`` to the :ref:`dictionary<dictionaries>` with the same value as what was given in the call to the ``factory`` :ref:`function<functions>`

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
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

  I copy the value from the right side then use it to replace the `return statement`_

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

  and the terminal shows green again

* I add a variable to remove the repetition in the test

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
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

  still green

* when I change the value of the ``sex`` variable

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        ...

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M'} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'}

  I copy the value from the terminal then use it to replace the `return statement`_

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': 'jane',
            'last_name': 'doe',
            'sex': 'F'
        }

  and the test is green again

* I add ``age`` to the expectation with a calculation

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
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
                age=this_year()-this_year(),
            )
        )

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'

  I cannot do subtraction with :ref:`None` and I want the value for the current year

* I add an `import statement`_

  .. code-block:: python

    import datetime
    import src.person
    import unittest

  datetime_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_ that is used for dates and times

* I change the `return statement`_ in the ``this_year`` :ref:`function <functions>` to get the current year

  .. code-block:: python

    def this_year():
        return datetime.datetime.now().year

  this returns the ``year`` attribute of the ``datetime`` object returned by the `now <https://docs.python.org/3/library/datetime.html#datetime.datetime.now>`_ :ref:`method<functions>` of the ``datetime`` :ref:`class <classes>`, from the datetime_ :ref:`module<ModuleNotFoundError>`. I could also use the `today <https://docs.python.org/3/library/datetime.html#datetime.date.today>`_ :ref:`method<functions>` to get the same result

  .. code-block:: python

    def this_year():
        return datetime.datetime.today().year

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F'} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0}

  the new :ref:`dictionary<dictionaries>` has a value for ``age``

* when I copy it from the terminal and use it to replace the `return statement`_

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

* I add a variable to remove duplication

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
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

refactor: make it better
#################################################################################

I  want to use random values for ``year_of_birth``

* first I add an `import statement`_

  .. code-block:: python

    import datetime
    import random
    import src.person
    import unittest

  random_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_, that is used to make fake random numbers

* then I make the ``year_of_birth`` variable use random numbers

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        ...

  ``random.randint(this_year()-120, this_year())`` gives me a random number from 120 years ago, up to and including the current year which is returned by ``this_year()``. The terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 2}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 7}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 14}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 0} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 60}

  I use the age calculation from the expectation

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

  and get a NameError_

  .. code-block:: python

    NameError: name 'this_year' is not defined

  because I called a :ref:`function<functions>` that does not exist in ``person.py``. I change the call to the ``this_year()`` :ref:`function<functions>` to its `return statement`_ from ``test_person.py``

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

  and the terminal shows another NameError_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

  I add an `import statement`_ to ``person.py``

  .. code-block:: python

    import datetime


    def factory(
    ...

  and the terminal shows a passing test

* I add randomness to the ``sex`` variable

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = 'doe'
        sex = random.choice(('F', 'M'))
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        ...

  ``random.choice(('F', 'M'))`` randomly gives me ``F`` or ``M`` and the terminal shows random success or an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 56} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 56}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 76} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 76}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 109} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 109}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 115} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 115}

  when I change the `return statement`_ to use the ``sex`` input parameter

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

* I use `random.choice`_ with the ``last_name`` variable

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
        first_name = 'jane'
        last_name = random.choice((
            'doe', 'smith', 'bloggs', 'public',
        ))
        sex = random.choice(('F', 'M'))
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        ...

  and get random success or an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 51} != {'first_name': 'jane', 'last_name': 'smith', 'sex': 'F', 'age': 51}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 54} != {'first_name': 'jane', 'last_name': 'bloggs', 'sex': 'M', 'age': 54}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'F', 'age': 110} != {'first_name': 'jane', 'last_name': 'public', 'sex': 'F', 'age': 110}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 116} != {'first_name': 'jane', 'last_name': 'public', 'sex': 'M', 'age': 116}

  I change the `return statement`_ to use the ``last_name`` input parameter

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

* I do the same thing for the ``first_name`` variable

  .. code-blocK:: python

    def test_function_w_keyword_arguments(self):
        first_name = random.choice((
            'jane', 'joe', 'john', 'person',
        ))
        last_name = random.choice((
            'doe', 'smith', 'bloggs', 'public',
        ))
        sex = random.choice(('F', 'M'))
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        ...

  and get random success or an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'jane', 'last_name': 'public', 'sex': 'F', 'age': 6} != {'first_name': 'john', 'last_name': 'public', 'sex': 'F', 'age': 6}
    AssertionError: {'first_name': 'jane', 'last_name': 'smith', 'sex': 'M', 'age': 19} != {'first_name': 'person', 'last_name': 'smith', 'sex': 'M', 'age': 19}
    AssertionError: {'first_name': 'jane', 'last_name': 'bloggs', 'sex': 'M', 'age': 59} != {'first_name': 'person', 'last_name': 'bloggs', 'sex': 'M', 'age': 59}
    AssertionError: {'first_name': 'jane', 'last_name': 'smith', 'sex': 'F', 'age': 117} != {'first_name': 'joe', 'last_name': 'smith', 'sex': 'F', 'age': 117}

  when I change the `return statement`_ to use the ``first_name`` input parameter

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

  the terminal shows a passing test.

----

*************************************************************************************
test_function_w_default_keyword_arguments
*************************************************************************************

I want to see what would happen if I try to make a person without a value for the ``last_name`` variable

red: make it fail
#################################################################################

* I make a copy of ``test_function_w_keyword_arguments`` and paste it below
* then change the name to ``test_function_w_default_keyword_arguments`` and remove the ``last_name`` variable

  .. code-block:: python

    def test_function_w_default_keyword_arguments(self):
        first_name = random.choice((
            'jane', 'joe', 'john', 'person',
        ))
        sex = 'M'
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )
    ...

  which gives me a NameError_

  .. code-block:: python

    NameError: name 'last_name' is not defined

green: make it pass
#################################################################################

* I remove ``last_name`` from the call to the ``factory`` :ref:`function<functions>`

  .. code-block:: python

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

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() missing 1 required positional argument: 'last_name'

  the ``factory`` :ref:`function<functions>` is called with 3 arguments in the test but the definition takes 4

* I add a default value for ``last_name``

  .. code-block:: python

    def factory(
            first_name, last_name=None,
            sex, year_of_birth
        ):
        ...

  and the terminal shows a SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

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

  and get another SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

* I give the ``year_of_birth`` parameter a default value

  .. code-block:: python

    def factory(
            first_name, last_name=None,
            sex=None, year_of_birth=None
        ):
        ...

  and the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'last_name' is not defined

  the value for the ``last_name`` key in the expected :ref:`dictionary<dictionaries>` points to a variable that no longer exists

* I change the expectation for ``last_name``

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
    AssertionError: {'first_name': 'john', 'last_name': None, 'sex': 'M', 'age': 83} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'M', 'age': 83}

  the ``factory`` :ref:`function<functions>` returns a :ref:`dictionary<dictionaries>` with a value of :ref:`None` for ``last_name`` and the test expects ``'doe'``

* When I make the default value for ``last_name`` in the :ref:`function<functions>` match the expectation

  .. code-block:: python

    def factory(
            first_name, last_name='doe',
            sex, year_of_birth
        ):
        ...

  the terminal shows passing tests. When no value is given for the ``last_name`` argument to the ``factory`` :ref:`function<functions>` it uses ``'doe'`` because that is the default value in the :ref:`function<functions>` signature, it is same as calling it with ``last_name='doe'``

  .. code-block:: python

    src.person.factory(
        first_name=first_name,
        sex=sex,
        year_of_birth=year_of_birth,
        last_name='doe',
    )

* I remove the ``sex`` variable to see what happens if I do not know the value for it

  .. code-block:: python

    def test_function_w_default_keyword_arguments(self):
        first_name = random.choice((
            'john', 'joe', 'jane', 'person',
        ))
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        ...

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'sex' is not defined

* I remove it from the call to the ``factory`` :ref:`function<functions>`

  .. code-block:: python

    self.assertEqual(
        src.person.factory(
            first_name=first_name,
            year_of_birth=year_of_birth,
        ),
        {
            'first_name': first_name,
            'last_name': 'doe',
            'sex': sex,
            'age': this_year()-year_of_birth,
        }
    )

  and get another NameError_

  .. code-block:: python

    NameError: name 'sex' is not defined

  the value in the :ref:`dictionary<dictionaries>` refers to a variable that no longer exists. I change the expectation

  .. code-block:: python

    self.assertEqual(
        src.person.factory(
            first_name=first_name,
            year_of_birth=year_of_birth,
        ),
        {
            'first_name': first_name,
            'last_name': 'doe',
            'sex': 'M',
            'age': this_year()-year_of_birth,
        }
    )

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'joe', 'last_name': 'doe', 'sex': None, 'age': 4} != {'first_name': 'joe', 'last_name': 'doe', 'sex': 'M', 'age': 4}
    AssertionError: {'first_name': 'jane', 'last_name': 'doe', 'sex': None, 'age': 32} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 32}
    AssertionError: {'first_name': 'john', 'last_name': 'doe', 'sex': None, 'age': 45} != {'first_name': 'john', 'last_name': 'doe', 'sex': 'M', 'age': 45}
    AssertionError: {'first_name': 'person', 'last_name': 'doe', 'sex': None, 'age': 58} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 58}

  the ``factory`` :ref:`function<functions>` returns a :ref:`dictionary<dictionaries>` with a value of :ref:`None` for ``sex`` and the test expects a value of ``'M'``

* when I add a default value to match the expectation

  .. code-block:: python

    def factory(
            first_name, last_name='doe',
            sex='M', year_of_birth=None
        ):
        ...

  the terminal shows passing tests. When no value is given for the ``sex`` argument to the ``factory`` :ref:`function<functions>` it uses ``'M'`` because that is the default value in the :ref:`function<functions>` signature, it is same as calling it with ``sex='M'``

  .. code-block:: python

    src.person.factory(
        first_name=first_name,
        year_of_birth=year_of_birth,
        last_name='doe',
        sex='M',
    )

  since the values are the same as the default values, I can call the :ref:`function<functions>` without them

  .. code-block:: python

    src.person.factory(
        first_name=first_name,
        year_of_birth=year_of_birth,
    )

refactor: make it better
#################################################################################

* ``first_name`` and ``year_of_birth`` are made the same way in both tests, I can remove this repetition with :ref:`class<classes>` attributes

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

  then use them in the tests with ``self`` the same way I do the ``assert`` :ref:`methods<functions>`

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
        first_name = self.first_name
        last_name = random.choice((
            'doe', 'smith', 'bloggs', 'public',
        ))
        sex = random.choice(('F', 'M'))
        year_of_birth = self.year_of_birth

        ...

    def test_function_w_default_keyword_arguments(self):
        first_name = self.first_name
        year_of_birth = self.year_of_birth

        ...

  the terminal still shows green

* since the variables point to class attributes, I can use them directly in place of the variables

  .. code-block:: python

    def test_function_w_keyword_arguments(self):
        last_name = random.choice((
            'doe', 'smith', 'bloggs', 'public',
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

    def test_function_w_default_keyword_arguments(self):
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

  all tests are still passing

* both tests now have the same values for ``self.first_name`` and ``self.year_of_birth`` since I made them :ref:`class<classes>` attributes, they were not always the same before the change. I can use the `unittest.TestCase.setUp`_ :ref:`method<functions>` which runs before every test to make sure they are assigned to random values right before each test

  .. code-block:: python

    class TestPerson(unittest.TestCase):

        def setUp(self):
            first_name = random.choice((
                'jane', 'joe', 'john', 'person',
            ))
            year_of_birth = random.randint(
                this_year()-120, this_year()
            )

        def test_function_w_keyword_arguments(self):
            ...

  the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: 'TestPerson' object has no attribute 'first_name'

  because there is no longer a class attribute named ``first_name``, it is now local to the `unittest.TestCase.setUp`_ :ref:`method<functions>` and the other :ref:`methods<functions>` cannot reach it

* I add ``self.`` to make it a class attribute

  .. code-block:: python

    def setUp(self):
        self.first_name = random.choice((
            'jane', 'joe', 'john', 'person',
        ))
        year_of_birth = random.randint(
            this_year()-120, this_year()
        )

  which gives me another :ref:`AttributeError`

  .. code-block:: python

    AttributeError: 'TestPerson' object has no attribute 'year_of_birth'

* I make the same change for ``year_of_birth``

  .. code-block:: python

    def setUp(self):
        self.first_name = random.choice((
            'jane', 'joe', 'john', 'person',
        ))
        self.year_of_birth = random.randint(
            this_year()-120, this_year()
        )

  and both tests are green again

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

  I want to write the solution without looking at the tests

.. _test_person_tests_green:

green: make it pass
#################################################################################

* I add the name

  .. code-block:: python

    factory

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'factory' is not defined

* I point it to :ref:`None`

  .. code-block:: python

    factory = None

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* when I make it a :ref:`function<functions>`

  .. code-block:: python

    def factory():
        return None

  the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'first_name'

  I add the keyword argument to the :ref:`function<functions>` definition

  .. code-block:: python

    def factory(first_name):
        return None

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'last_name'

  I add the keyword argument

  .. code-block:: python

    def factory(first_name, last_name):
        return None

  and the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'sex'

  when I add the keyword argument

  .. code-block:: python

    def factory(first_name, last_name, sex):
        return None

  I get a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'year_of_birth'

  I add the missing keyword argument

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return None

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != {'first_name': 'john', 'last_name': 'bloggs', 'sex': 'M', 'age': 20}
    AssertionError: None != {'first_name': 'john', 'last_name': 'smith', 'sex': 'F', 'age': 31}
    AssertionError: None != {'first_name': 'jane', 'last_name': 'bloggs', 'sex': 'M', 'age': 55}
    AssertionError: None != {'first_name': 'person', 'last_name': 'smith', 'sex': 'F', 'age': 97}

* I copy the value from the terminal to replace :ref:`None` in the `return statement`_

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': 'john',
            'last_name': 'bloggs',
            'sex': 'F',
            'age': 20
        }

  which gives me another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'john', 'last_name': 'bloggs', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'bloggs', 'sex': 'M', 'age': 50}
    AssertionError: {'first_name': 'john', 'last_name': 'bloggs', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'doe', 'sex': 'M', 'age': 73}
    AssertionError: {'first_name': 'john', 'last_name': 'bloggs', 'sex': 'F', 'age': 20} != {'first_name': 'john', 'last_name': 'bloggs', 'sex': 'F', 'age': 77}
    AssertionError: {'first_name': 'john', 'last_name': 'bloggs', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'public', 'sex': 'F', 'age': 98}

  the values for ``first_name``, ``last_name``, ``sex`` and ``age`` change

* I make the :ref:`dictionary<dictionaries>` in the `return statement`_ use the ``first_name`` input parameter

  .. code-block:: python

    def factory(
            first_name, last_name,
            sex, year_of_birth
        ):
        return {
            'first_name': first_name,
            'last_name': 'bloggs',
            'sex': 'F',
            'age': 20
        }

  and still have an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'person', 'last_name': 'bloggs', 'sex': 'F', 'age': 20} != {'first_name': 'person', 'last_name': 'public', 'sex': 'F', 'age': 69}
    AssertionError: {'first_name': 'joe', 'last_name': 'bloggs', 'sex': 'F', 'age': 20} != {'first_name': 'joe', 'last_name': 'bloggs', 'sex': 'F', 'age': 97}
    AssertionError: {'first_name': 'john', 'last_name': 'bloggs', 'sex': 'F', 'age': 20} != {'first_name': 'john', 'last_name': 'smith', 'sex': 'M', 'age': 74}
    AssertionError: {'first_name': 'john', 'last_name': 'bloggs', 'sex': 'F', 'age': 20} != {'first_name': 'john', 'last_name': 'public', 'sex': 'F', 'age': 19}

  the ``last_name``, ``sex`` and ``age`` change

* I use the ``last_name`` input parameter in the `return statement`_

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

    AssertionError: {'first_name': 'jane', 'last_name': 'bloggs', 'sex': 'F', 'age': 20} != {'first_name': 'jane', 'last_name': 'bloggs', 'sex': 'M', 'age': 3}
    AssertionError: {'first_name': 'joe', 'last_name': 'smith', 'sex': 'F', 'age': 20} != {'first_name': 'joe', 'last_name': 'smith', 'sex': 'F', 'age': 118}
    AssertionError: {'first_name': 'joe', 'last_name': 'bloggs', 'sex': 'F', 'age': 20} != {'first_name': 'joe', 'last_name': 'bloggs', 'sex': 'M', 'age': 19}
    AssertionError: {'first_name': 'joe', 'last_name': 'bloggs', 'sex': 'F', 'age': 20} != {'first_name': 'joe', 'last_name': 'bloggs', 'sex': 'M', 'age': 95}

  the values for ``sex`` and ``age`` change

* When I add the ``sex`` input parameter to the `return statement`_

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
    AssertionError: {'first_name': 'joe', 'last_name': 'bloggs', 'sex': 'F', 'age': 20} != {'first_name': 'joe', 'last_name': 'bloggs', 'sex': 'F', 'age': 113}
    AssertionError: {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 20} != {'first_name': 'person', 'last_name': 'doe', 'sex': 'M', 'age': 58}

  the ``age`` is different

* I add the ``year_of_birth`` input parameter to the `return statement`_

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
    AssertionError: {'first_name': 'jane', 'last_name': 'bloggs', 'sex': 'F', 'age': 1981} != {'first_name': 'jane', 'last_name': 'bloggs', 'sex': 'F', 'age': 43}
    AssertionError: {'first_name': 'person', 'last_name': 'smith', 'sex': 'M', 'age': 1969} != {'first_name': 'person', 'last_name': 'smith', 'sex': 'M', 'age': 55}

  I need the difference between the current year and the ``year_of_birth`` to get the ``age``

* I add an `import statement`_ for the datetime_ :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

    import datetime


    def factory(
    ...

  then use it to get the current year for the age calculation

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

  and the terminal shows a :ref:`TypeError`

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

  the terminal shows the same SyntaxError_

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

  both tests pass!

*************************************************************************************
review
*************************************************************************************

I ran tests to make a :ref:`function<functions>` that takes in keyword arguments as input, has default values for some of them, performs an action based on an input and returns a :doc:`dictionary </data_structures/dictionaries>` as output

I also encountered the following :ref:`Exceptions<Exceptions>`

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`
* SyntaxError_

Would you like to know :doc:`how to test that an Exception is raised?</how_to/exception_handling_tests>`

----

:doc:`/code/code_person_factory`
