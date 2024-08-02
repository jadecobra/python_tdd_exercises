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
  :depth: 2

----

*********************************************************************************
test_person_factory
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

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard then click on ``tests/test_person.py:7`` with the mouse to open it
* and change ``True`` to ``False`` to make ``test_failure`` pass
* then change ``test_failure`` to ``test_person_factory``

  .. code-block:: python

    class TestPersonFactory(unittest.TestCase):

        def test_person_factory(self):
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

refactor: make it better
#################################################################################

* I want to pass in values for ``first_name``, ``last_name``, ``year_of_birth`` and ``sex`` and have the :ref:`function<functions>` return a :doc:`dictionary </data_structures/dictionaries>` with ``first_name``, ``last_name``, ``sex`` and ``age`` calculated from the ``year_of_birth``, so I add more details to ``test_person_factory``

  .. code-block:: python

    def test_person_factory(self):
        self.assertEqual(
            src.person.factory(
                first_name="baby",
                last_name="doe",
                year_of_birth=this_year(),
                sex="F"
            ),
            {
                "first_name": "baby",
                "last_name": "last_name",
                "sex": "F",
                "age": this_year() - this_year()
            }
        )

  the terminal shows a NameError_ for the call to the ``this_year`` :ref:`function<functions>`

  .. code-block:: python

    NameError: name 'this_year' is not defined

* I add a definition for ``this_year`` to the top of ``test_person.py``

  .. code-block:: python

    import unittest
    import src.person


    def this_year():
        return None


    class TestPersonFactory(unittest.TestCase):
    ...

  the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'first_name'

  the ``person.factory`` :ref:`function<functions>` signature does not allow it take inputs and the test sends four arguments when it calls the :ref:`function<functions>`

* I add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* then add a keyword argument for ``first_name`` to the ``factory`` function

  .. code-block:: python

    def factory(first_name=None):
    ...

  the terminal shows a :ref:`TypeError` for the next argument

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'last_name'

* after adding a keyword argument for ``last_name``  to the ``factory`` function

  .. code-block:: python

    def factory(first_name=None, last_name=None):
    ...

  the terminal shows another :ref:`TypeError` for the next keyword argument

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'year_of_birth'

* I add each keyword to the ``factory`` function until I get a :ref:`TypeError` for the line where I subtract ``this_year() - this_year()``

  .. code-block:: python

      def factory(
          first_name=None, last_name=None,
          year_of_birth=None, sex=None
      ):
      ...

  which gives me a :ref:`TypeError`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'

  because I cannot do subtraction with :ref:`None`, the ``this_year`` function currently returns :ref:`None` and the ``age`` calculation uses it

* I import the datetime_

  .. code-block:: python

    import datetime
    import src.person
    import unittest

  datetime_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_, that is used for dates and times, I will use it to return the current year

* I change the `return statement`_ in the ``this_year`` :ref:`function <functions>` to add a call that returns the current year

  .. code-block:: python

    def this_year():
        return datetime.datetime.now().year

  ``datetime.datetime.now().year`` returns the ``year`` attribute of the object returned by the ``now`` :ref:`method<functions>` of the ``datetime.datetime`` :ref:`class <classes>`, which is a representation of the current local date and time. I could also use ``today`` or ``utcnow`` instead of ``now`` to get the same value

* the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != {'first_name': 'sibling', 'last_name': 'last_name', 'sex': 'F', 'age': 0}

  the ``factory`` :ref:`function<functions>` returns :ref:`None` and the test expects a :doc:`dictionary </data_structures/dictionaries>` with keys and values

* I copy the expected value from the terminal and paste it as the return value

  .. code-block:: python

    def factory(
        first_name=None, last_name=None,
        year_of_birth=None, sex=None
    ):
        return {
            'first_name': 'sibling',
            'last_name': 'last_name',
            'sex': 'F',
            'age': 0
        }

  the terminal shows the test passed

*********************************************************************************
test_factory_w_variable_inputs
*********************************************************************************

red: make it fail
#################################################################################

* The ``factory`` :ref:`function<functions>` currently returns the exact same dictionary every time, it does not care about the inputs, it is a :doc:`singleton function </functions/test_singleton_functions>`. It has to use the inputs to be useful. I add another test to ``test_person.py`` with a different set of inputs

  .. code-block:: python

    def test_factory_w_variable_inputs(self):
        self.assertEqual(
            src.person.factory(
                first_name="me",
                last_name="my_last_name",
                year_of_birth=1983,
                sex="M",
            ),
            {
                "first_name": "me",
                "last_name": "my_last_name",
                "sex": "M",
                "age": this_year() - 1983
            }
        )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'sibling', 'last_name': 'last_name', 'sex': 'F', 'age': 0} != {'first_name': 'me', 'last_name': 'my_last_name', 'sex': 'M', 'age': 41}

  because the expected and returned dictionaries are different

green: make it pass
#################################################################################

* I make ``factory`` use the input provided for ``first_name``

  .. code-block:: python

    def factory(
        first_name=None, last_name=None,
        year_of_birth=None, sex=None
    ):
        return {
            'first_name': first_name,
            'last_name': 'last_name',
            'sex': 'F',
            'age': 0
        }

  and the terminal shows an :ref:`AssertionError` with no difference for the values of ``first_name``

* I repeat the same move for every other input except ``age``

  .. code-block:: python

    def factory(
        first_name=None, last_name=None,
        year_of_birth=None, sex=None,
    ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': 0
        }

* For ``age`` to be accurate it has to be a calculation based on the current year. I have a :ref:`function<functions>` that returns the current year and I have the ``year_of_birth`` as input, I also have this line in the test ``this_year() - 1983``. I can try the calculation

  .. code-block:: python

    def factory(
        first_name=None, last_name=None,
        year_of_birth=None, sex=None,
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

  because I called a function that does not exist in ``person.py``

* I change ``this_year()`` to the return value from ``test_person_factory.this_year``

  .. code-block:: python

    def factory(
        first_name=None, last_name=None,
        year_of_birth=None, sex=None,
    ):
        return {
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
            'age': datetime.datetime.now().year - year_of_birth,
        }

  the terminal shows another NameError_

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

* I add an `import statement`_ at the beginning of ``person.py``

  .. code-block:: python

    import datetime



    def factory(
    ...

  and the terminal shows passing tests, time for a victory dance

refactor: make it better
#################################################################################

There is some repetition in the test. If I want to test with a different value for any of the arguments passed to ``person.factory``, I would have to make the change in 2 places - once in the argument passed to the :ref:`function<functions>` and then again in the resulting :doc:`dictionary </data_structures/dictionaries>`. I can refactor this to make it easier to make changes to the test when I want,  especially since the programming gods told me `not to repeat myself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_.

  .. code-block:: python

    def test_factory_w_variable_inputs(self):
        first_name = "me"
        last_name = "my_last_name"
        sex = "M"
        year_of_birth = 1983

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
                sex=sex,
            ),
            {
                "first_name": first_name,
                "last_name": last_name,
                "sex": sex,
                "age": this_year() - year_of_birth,
            }
        )

  I remove the duplication by making a variable for each of the inputs that is passed to the ``factory`` :ref:`function<functions>` and reference the variables in the :ref:`function<functions>` call. I now only need to make a change in one place when I want, for example

  .. code-block:: python

      def test_factory_w_variable_inputs(self):
          first_name = "john"
          last_name = "doe"
          sex = "M"
          year_of_birth = 1942

          self.assertEqual(
              src.person.factory(
                  first_name=first_name,
                  last_name=last_name,
                  year_of_birth=year_of_birth,
                  sex=sex,
              ),
              {
                  "first_name": first_name,
                  "last_name": last_name,
                  "sex": sex,
                  "age": this_year() - year_of_birth,
              }
          )

* I make the same change to ``test_person_factory``

  .. code-block:: python

    def test_person_factory(self):
        first_name = "baby"
        last_name = "last_name"
        sex = "F"
        year_of_birth = this_year()

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
                sex=sex
            ),
            {
                "first_name": first_name,
                "last_name": last_name,
                "sex": sex,
                "age": this_year() - year_of_birth
            }
        )

* I remove ``test_factory_w_variable_inputs`` because it is now the same test as ``test_person_factory``

----

*************************************************************************************
test_factory_w_last_name_default_keyword_argument
*************************************************************************************

red: make it fail
==================

* I add a failing test for default values to ``test_person.py``

  .. code-block:: python

    def test_factory_w_last_name_default_keyword_argument(self):
        first_name = "child_a"
        sex = "M"
        year_of_birth = 2014

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
                sex=sex,
            ),
            {
                "first_name": first_name,
                "last_name": "doe",
                "sex": sex,
                "age": this_year() - year_of_birth
            }
        )

  the terminal shows an :ref:`AssertionError` because the value for ``last_name`` does not match the expected value

  .. code-block:: python

    AssertionError: {'first_name': 'child_a', 'last_name': None, 'sex': 'M', 'age': 10} != {'first_name': 'child_a', 'last_name': 'doe', 'sex': 'M', 'age': 10}

* The test expects a value of ``"doe"`` but ``person.factory`` returns :ref:`None`. When I make the default value for ``last_name`` in the :ref:`function<functions>` match the expectation

  .. code-block:: python

    def factory(
        first_name=None, last_name="doe",
        year_of_birth=None, sex=None
    ):
    ...

  the terminal shows passing tests. When no value is given for the ``last_name`` argument to ``person.factory`` it uses ``"doe"`` because that is the default value in the :ref:`function<functions>` signature

.. _test_factory_w_sex_default_keyword_argument:

*************************************************************************************
test_factory_w_sex_default_keyword_argument
*************************************************************************************

red: make it fail
#################################################################################

* I add a test to try another default value

  .. code-block:: python


    def test_factory_w_sex_default_keyword_argument(self):
        first_name = "person"
        year_of_birth = 1900

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
            ),
            {
                "first_name": first_name,
                "last_name": "doe",
                "age": this_year() - year_of_birth,
                "sex": "M"
            }
        )

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'first_name': 'person', 'last_name': 'last_name', 'sex': None, 'age': 124} != {'first_name': 'person', 'last_name': 'last_name', 'age': 124, 'sex': 'M'}

  there is a difference in the values for ``sex``

green: make it pass
#################################################################################

* I set the default value for the parameter in ``person.factory``

  .. code-block:: python

    def factory(
        first_name=None, last_name="doe",
        year_of_birth=None, sex="M"
    ):
    ...

  and the terminal shows passing tests

----

*************************************************************************************
review
*************************************************************************************

I ran the following tests to make a :ref:`function<functions>` that returns a :doc:`dictionary </data_structures/dictionaries>` as output, takes in keyword arguments as input, has default values for when a value is not given for a certain input and perform an action based on a given input

* `test_person_factory`_
* `test_factory_w_variable_inputs`_
* `test_factory_w_last_name_default_keyword_argument`_
* `test_factory_w_sex_default_keyword_argument`_

I also encountered the following :ref:`Exceptions<Exceptions>`

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`

Would you like to know :doc:`/how_to/exception_handling_tests`?

----

:doc:`/code/code_person_factory`
