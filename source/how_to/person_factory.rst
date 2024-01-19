
#######################
How to create a person
#######################

This is an exercise in creating :doc:`dictionaries </data_structures/dictionaries>`  with :doc:`/functions/functions`. It assumes familiarity with those concepts, though you can still try out the chapter even if you are not.

****************
Prerequisites
****************

:doc:`How to create a Test Driven Development Environment </how_to/create_tdd_environment>` with ``person`` as the project name

----

***********************************************
How to use dictionaries as factories in Python
***********************************************

RED: make it fail
==================

I add an import statement and replace ``test_failure`` with a failing test in ``test_person.py``

.. code-block:: python

  import person
  import unittest


  class TestPersonFactory(unittest.TestCase):

      def test_person_factory(self):
          self.assertEqual(person.factory(), None)

the terminal shows an :doc:`/exceptions/AttributeError`

.. code-block:: python

  AttributeError: module 'person' has no attribute 'factory'

which I add to the list of exceptions

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # AttributeError


GREEN: make it pass
====================

* I create a function called ``factory`` in ``person.py`` and the terminal shows the test passed

  .. code-block:: python

    def factory():
        return None

REFACTOR: make it better
=========================

* I want to pass in values for ``first_name``, ``last_name``, ``year_of_birth``, ``sex`` and have the :doc:`function </functions/functions>` return a :doc:`dictionary </data_structures/dictionaries>` with the ``first_name``, ``last_name``, ``sex`` and ``age`` calculated from the ``year_of_birth``, so I add more details to ``test_person_factory``

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

  the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ for the call to the ``this_year`` :doc:`function </functions/functions>`

  .. code-block:: python

    NameError: name 'this_year' is not defined

* I add it to the list of exceptions encountered

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

  the terminal shows a :doc:`/exceptions/TypeError` since the ``person.factory`` :doc:`function signature </functions/functions>` does not allow it to accept inputs and the test sends four arguments when it calls the :doc:`function </functions/functions>`

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'first_name'

* I add the error to the list of exceptions encountered

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

  the terminal shows a :doc:`/exceptions/TypeError` for the next argument

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'last_name'

* after adding a keyword argument for ``last_name``  to the ``factory`` function

  .. code-block:: python

    def factory(first_name=None, last_name=None):
        ...

  the terminal shows another :doc:`/exceptions/TypeError` for the next keyword argument

  .. code-block:: python

    TypeError: factory() got an unexpected keyword argument 'year_of_birth'

* I add each keyword to the ``factory`` function until I get a :doc:`/exceptions/TypeError` for the line where I subtract ``this_year() - this_year()``

  .. code-block:: python

      def factory(
          first_name=None, last_name=None,
          year_of_birth=None, sex=None
      ):
          ...

  a :doc:`/exceptions/TypeError` is raised because I cannot perform a subtraction operation on :doc:`None </data_structures/none>` and the ``this_year`` function currently returns :doc:`None </data_structures/none>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'

* I import the `datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime>`_ library in ``test_person.py`` to use it to return the current year

  .. code-block:: python

    import datetime
    import person
    import unittest

  ``import datetime`` imports the ``datetime`` library so I can use its :doc:`/functions/functions` and :doc:`classes </classes/classes>`
* then I add a call in the ``this_year`` :doc:`function <functions/functions>` in ``test_person.py`` to return the current year

  .. code-block:: python

    def this_year():
        return datetime.datetime.now().year

  - ``return datetime.datetime.now().year`` returns the ``year`` attribute of the object returned by the ``now`` :doc:`method </functions/functions>` of the ``datetime.datetime`` :doc:`class </classes/classes>`, which is a representation of the current local date and time. I could also use ``today`` or ``utcnow`` instead of ``now`` to achieve the same result
  - I get the ``year`` attribute of the object returned since that is `all I need to get by <https://www.youtube.com/watch?v=XW1HNWqdVbk>`_

* the terminal shows an :doc:`/exceptions/AssertionError` since the ``person.factory`` function returns :doc:`None </data_structures/none>` and the test expects a :doc:`dictionary </data_structures/dictionaries>` with keys and values.

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

* The factory function currently returns the exact same dictionary every time, regardless of what inputs it gets. It is a :doc:`singleton function </functions/functions_singleton>`. To be more useful it has to use the inputs it is given. I add another test to ``test_person.py`` with a different set of inputs

  .. code-block:: python

    def test_person_factory_takes_in_variable_inputs(self):
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

  the terminal shows an :doc:`/exceptions/AssertionError` because the expected and returned dictionaries are different

  .. code-block:: python

    AssertionError: {'first_name': 'sibling', 'last_name': 'last_name', 'sex': 'F', 'age': 0} != {'first_name': 'me', 'last_name': 'my_last_name', 'sex': 'M', 'age': 41}

* I change the ``factory`` function to use the input provided for ``first_name``

  .. code-block:: python

    def factory(
        first_name=None, last_name=None,
        year_of_birth=None, sex=None
    ):
        return {
            "age": 0,
            "first_name": first_name,
            "last_name": "last_name",
            "sex": "F",
        }

  the terminal shows an :doc:`/exceptions/AssertionError` with no difference for the values of ``first_name``

* I repeat the same move for every other input until the only error left is for ``age``

  .. code-block:: python

    def factory(
        first_name=None, last_name=None,
        year_of_birth=None, sex=None,
    ):
        return {
            "first_name": first_name,
            "last_name": last_name,
            "sex": sex,
            "age": 0
        }

* For ``age`` to be accurate it has to be a calculation based on the current year. I have a function that returns the current year and I have the ``year_of_birth`` as input, I also have this line in the test ``this_year() - 1983``. I can try making the ``factory`` function use that calculation

  .. code-block:: python

    def factory(
        first_name=None, last_name=None,
        year_of_birth=None, sex=None,
    ):
        return {
            "first_name": first_name,
            "last_name": last_name,
            "sex": sex,
            "age": this_year() - year_of_birth,
        }

  the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ since I am calling a function that does not exist in ``person.py``

  .. code-block:: python

    NameError: name 'this_year' is not defined

* I replace ``this_year()`` with the return value from ``test_person_factory.this_year``

  .. code-block:: python

    def factory(
        first_name=None, last_name=None,
        year_of_birth=None, sex=None,
    ):
        return {
            "first_name": first_name,
            "last_name": last_name,
            "sex": sex,
            "age": datetime.datetime.now().year - year_of_birth,
        }

  the terminal shows another `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ this time for the ``datetime`` module

  .. code-block:: python

    NameError: name 'datetime' is not defined. Did you forget to import 'datetime'

* I add an import statement at the beginning of ``person.py``

  .. code-block:: python

    import datetime

    def factory(
    ...

  *HOORAY!* the terminal shows passing tests, time for a victory dance.

* When I call the ``factory`` :doc:`function </functions/functions>` passing in values for ``first_name``, ``last_name``, ``sex`` and ``year_of_birth``, I get a :doc:`dictionary </data_structures/dictionaries>` that contains the ``first_name``, ``last_name``, ``sex`` and ``age`` of the person

* I noticed that there is some repetition in the test. If I want to test with a different value for any of the arguments passed to ``person.factory``, I would have to make the change in 2 places - once in the argument passed to the :doc:`function </functions/functions>` and then again in the resulting :doc:`dictionary </data_structures/dictionaries>`. I can refactor this to make it easier to make changes to the test when I want,  especially since the programming gods told me `not to repeat myself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

  .. code-block:: python

    def test_person_factory_takes_in_variable_inputs(self):
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

  I remove the duplication by creating a variable for each of the inputs that is passed to the ``factory`` :doc:`function </functions/functions>` and reference the variables in the :doc:`function </functions/functions>` call. I now only need to make a change in one place when I want, for example

  .. code-block:: python

      def test_person_factory_takes_in_variable_inputs(self):
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

***************************************************
How to use default keyword arguments in functions
***************************************************

RED: make it fail
==================

* I add a failing test for default values to ``test_person.py``

  .. code-block:: python

    def test_person_factory_with_default_keyword_arguments(self):
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

  the terminal shows an :doc:`/exceptions/AssertionError` because the value for ``last_name`` does not match the expected value

* The test expects a value of ``"last_name"`` but ``person.factory`` currently returns :doc:`None </data_structures/none>`. When I change the default value for ``last_name`` in the ``person.factory`` definition to match the expectation

  .. code-block:: python

    def factory(
        first_name=None, last_name="last_name",
        year_of_birth=None, sex=None
    ):
        ...

  the terminal shows passing tests. When no value is given for the ``last_name`` argument to ``person.factory`` it uses ``"last_name"`` because that is the defined default value in the :doc:`function signature </functions/functions>`

* I add a test called ``test_person_factory_with_sex_default_keyword_arguments`` to try another default value

  .. code-block:: python


    def test_person_factory_with_sex_default_keyword_arguments(self):
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

  the terminal shows an :doc:`/exceptions/AssertionError`, there is a difference in the values for ``sex``

* 3 out of the 4 persons created in the tests have ``M`` as their sex and 1 person has ``F`` as the value for sex. I set the default value for the parameter in ``person.factory`` to the majority to reduce the number of repetitions

  .. code-block:: python

    def factory(
        first_name=None, last_name="last_name",
        year_of_birth=None, sex="M"
    ):
        ...

  and the terminal shows passing tests

----

That's it, from the tests above you can create a :doc:`function </functions/functions>` that

* returns a :doc:`dictionary </data_structures/dictionaries>` as output
* takes in keyword arguments as inputs
* has default values for when a value is not given for a certain input
* performs a calculation based on a given input to return an output based on an input

You also encountered the following exceptions

* :doc:`/exceptions/AssertionError`
* :doc:`/exceptions/AttributeError`
* `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_
* :doc:`/exceptions/TypeError`

----

:doc:`/code/code_person_factory`