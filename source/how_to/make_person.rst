.. include:: ../links.rst

#################################################################################
how to make a person
#################################################################################

.. raw:: html

  <iframe style="border-radius:10px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/A7bCTJhr14g?si=QRx1U5esOaK7khD8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

This is an exercise in making :doc:`dictionaries </data_structures/dictionaries>`  with :doc:`/functions/functions`. It assumes familiarity with those concepts, though you can still try out the chapter even if you are not.

.. contents:: table of contents
  :local:
  :depth: 2

---

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

  the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'person' has no attribute 'factory'



green: make it pass
#################################################################################

* which I add to the list of exceptions

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError

* then make a function called ``factory`` in ``person.py`` and the test passes

  .. code-block:: python

    def factory():
        return None

refactor: make it better
#################################################################################

* I want to pass in values for ``first_name``, ``last_name``, ``year_of_birth``, ``sex`` and have the :ref:`function<functions>` return a :doc:`dictionary </data_structures/dictionaries>` with the ``first_name``, ``last_name``, ``sex`` and ``age`` calculated from the ``year_of_birth``, so I add more details to ``test_person_factory``

  .. code-block:: python

    def test_person_factory(self):
        self.assertEqual(
            person.factory(
                first_name="baby",
                last_name="last_name",
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

* I add it to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # NameError

* then add a definition for ``this_year`` to the top of ``test_person.py``

  .. code-block:: python

    import unittest
    import person

    def this_year():
        return None


    class TestPersonFactory(unittest.TestCase):
    ...

  the terminal shows a :ref:`TypeError` since the ``person.factory`` :ref:`function<functions>` signature does not allow it accept inputs and the test sends four arguments when it calls the :ref:`function<functions>`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'first_name'

* I add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # NameError
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

  a :ref:`TypeError` is raised because I cannot perform a subtraction operation on :ref:`None` and the ``this_year`` function currently returns :ref:`None`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'

* I import the datetime_ library in ``test_person.py`` to use it to return the current year

  .. code-block:: python

    import datetime
    import person
    import unittest

  ``import datetime`` imports the ``datetime`` library so I can use its :doc:`/functions/functions` and :ref:`classes`
* then I add a call in the ``this_year`` :ref:`function <functions>` in ``test_person.py`` to return the current year

  .. code-block:: python

    def this_year():
        return datetime.datetime.now().year

  - ``return datetime.datetime.now().year`` returns the ``year`` attribute of the object returned by the ``now`` :ref:`method<functions>` of the ``datetime.datetime`` :ref:`class <classes>`, which is a representation of the current local date and time. I could also use ``today`` or ``utcnow`` instead of ``now`` to achieve the same result
  - I get the ``year`` attribute of the object returned since that is `all I need to get by <https://www.youtube.com/watch?v=XW1HNWqdVbk>`_

* the terminal shows an :ref:`AssertionError` since the ``person.factory`` function returns :ref:`None` and the test expects a :doc:`dictionary </data_structures/dictionaries>` with keys and values.

  .. code-block:: python

    AssertionError: None != {'first_name': 'sibling', 'last_name': 'last_name', 'sex': 'F', 'age': 0}

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

.. _test_factory_w_variable_inputs:

test_factory_w_variable_inputs
---------------------------------------------------------------------------------

red: make it fail
#################################################################################
* The factory function currently returns the exact same dictionary every time, regardless of what inputs it gets. It is a :doc:`singleton function </functions/test_singleton_functions>`. To be more useful it has to use the inputs it is given. I add another test to ``test_person.py`` with a different set of inputs

  .. code-block:: python

    def test_factory_w_variable_inputs(self):
        self.assertEqual(
            person.factory(
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

  the terminal shows an :ref:`AssertionError` because the expected and returned dictionaries are different

  .. code-block:: python

    AssertionError: {'first_name': 'sibling', 'last_name': 'last_name', 'sex': 'F', 'age': 0} != {'first_name': 'me', 'last_name': 'my_last_name', 'sex': 'M', 'age': 41}

green: make it pass
#################################################################################

* I make the ``factory`` function use the input provided for ``first_name``

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

* I repeat the same move for every other input until the only error left is for ``age``

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

* For ``age`` to be accurate it has to be a calculation based on the current year. I have a function that returns the current year and I have the ``year_of_birth`` as input, I also have this line in the test ``this_year() - 1983``. I can try making the ``factory`` function use that calculation

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

  the terminal shows a NameError_ since I am calling a function that does not exist in ``person.py``

  .. code-block:: python

    NameError: name 'this_year' is not defined

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

  the terminal shows another NameError_ this time for the ``datetime`` module

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

* When I call the ``factory`` :ref:`function<functions>` passing in values for ``first_name``, ``last_name``, ``sex`` and ``year_of_birth``, it returns a :doc:`dictionary </data_structures/dictionaries>` that has the ``first_name``, ``last_name``, ``sex`` and ``age`` of the person

* I noticed that there is some repetition in the test. If I want to test with a different value for any of the arguments passed to ``person.factory``, I would have to make the change in 2 places - once in the argument passed to the :ref:`function<functions>` and then again in the resulting :doc:`dictionary </data_structures/dictionaries>`. I can refactor this to make it easier to make changes to the test when I want,  especially since the programming gods told me `not to repeat myself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

  .. code-block:: python

    def test_factory_w_variable_inputs(self):
        first_name = "me"
        last_name = "my_last_name"
        sex = "M"
        year_of_birth = 1983

        self.assertEqual(
            person.factory(
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
              person.factory(
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
            person.factory(
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

----

*************************************************************************************
test_factory_w_default_keyword_arguments
*************************************************************************************

red: make it fail
==================

* I add a failing test for default values to ``test_person.py``

  .. code-block:: python

    def test_factory_w_default_keyword_arguments(self):
        first_name = "child_a"
        sex = "M"
        year_of_birth = 2014

        self.assertEqual(
            person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
                sex=sex,
            ),
            {
                "first_name": first_name,
                "last_name": "last_name",
                "sex": sex,
                "age": this_year() - year_of_birth
            }
        )

  the terminal shows an :ref:`AssertionError` because the value for ``last_name`` does not match the expected value

  .. code-block:: python

    AssertionError: {'first_name': 'child_a', 'last_name': None, 'sex': 'M', 'age': 10} != {'first_name': 'child_a', 'last_name': 'last_name', 'sex': 'M', 'age': 10}

* The test expects a value of ``"last_name"`` but ``person.factory`` currently returns :ref:`None`. When I make the default value for ``last_name`` in the ``person.factory`` definition to match the expectation

  .. code-block:: python

    def factory(
        first_name=None, last_name="last_name",
        year_of_birth=None, sex=None
    ):
    ...

  the terminal shows passing tests. When no value is given for the ``last_name`` argument to ``person.factory`` it uses ``"last_name"`` because that is the defined default value in the :ref:`function<functions>` signature

.. _test_factory_w_sex_default_keyword_argument:

*************************************************************************************
test_factory_w_sex_default_keyword_argument
*************************************************************************************

red: make it fail
#################################################################################

* I add a test called ``test_factory_w_sex_default_keyword_argument`` to try another default value

  .. code-block:: python


    def test_factory_w_sex_default_keyword_argument(self):
        first_name = "person"
        year_of_birth = 1900

        self.assertEqual(
            person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
            ),
            {
                "first_name": first_name,
                "last_name": "last_name",
                "age": this_year() - year_of_birth,
                "sex": "M"
            }
        )

  the terminal shows an :ref:`AssertionError`, there is a difference in the values for ``sex``

  .. code-block:: python

    AssertionError: {'first_name': 'person', 'last_name': 'last_name', 'sex': None, 'age': 124} != {'first_name': 'person', 'last_name': 'last_name', 'age': 124, 'sex': 'M'}

green: make it pass
#################################################################################

* 3 out of the 4 persons made in the tests have ``M`` as their sex and 1 person has ``F`` as the value for sex. I set the default value for the parameter in ``person.factory`` to the majority to reduce the number of repetitions

  .. code-block:: python

    def factory(
        first_name=None, last_name="last_name",
        year_of_birth=None, sex="M"
    ):
    ...

  and the terminal shows passing tests

----

*************************************************************************************
review
*************************************************************************************

From the tests above I can make a :ref:`function<functions>` that

* return a :doc:`dictionary </data_structures/dictionaries>` as output
* take in keyword arguments as input
* have default values for when a value is not given for a certain input
* perform an action based on a given input

I also encountered the following :ref:`Exceptions<Exceptions>`

* :ref:`AssertionError`
* :ref:`AttributeError`
* NameError_
* :ref:`TypeError`

Would you like to know :doc:`/how_to/exception_handling_tests`?

----

:doc:`/code/code_person_factory`