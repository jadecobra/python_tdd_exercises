
Person Factory
==============

This is an exercise in creating :doc:`data structures: dictionaries` with :doc:`functions`. It assumes you are familiar with :doc:`functions` and :doc:`data structures: dictionaries` though you can attempyt it even if you are not



How to use dictionaries as factories in python
-----------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

create a file called ``test_person_factory.py`` in the ``tests`` folder and add the following

.. code-block:: python

  import unittest
  import person


  class TestPersonFactory(unittest.TestCase):

    def test_person_factory(self):
      self.assertEqual(person.factory(), None)

the terminal updates to show a ``ModuleNotFoundError`` and I add it to the list of exceptions encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* create a file called ``person.py`` in the ``{PROJECT_NAME}`` folder and the terminal updates to show an :doc:`AttributeError` which I add to the list of exceptions

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* create a function called ``factory`` in ``person.py`` and the terminal shows passing tests

  .. code-block:: python

    def factory():
      return None

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* I will now add more details to ``test_person_factory``

  .. code-block:: python

  def test_person_factory(self):
    self.assertEqual(
      person.factory(
        first_name="sibling",
        last_name="last_name",
        year_of_birth=this_year(),
        sex="F"
      ),
      {
        "first_name": "sibling",
        "last_name": "last_name",
        "sex": "F",
        "age": this_year() - this_year()
      }
    )

  the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ is raised for ``this_year``

* I add the new exception to the running list

  .. code-block:: python

   # Exceptions Encountered
   # AssertionError
   # ModuleNotFoundError
   # AttributeError
   # NameError

* add a definition for ``this_year`` to the top of ``test_person_factory.py``

  .. code-block:: python

    import unittest
    import person

    def this_year():
      return None
    ...

  the terminal updates to show a :doc:`TypeError` since the ``person.factory`` function signature does not allow arguments to be passed to it.

* I update the list of exceptions encountered

  .. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError
  # AttributeError
  # NameError
  # TypeError

* add a keyword argument for ``first_name`` to the ``factory`` function

  .. code-block:: python

    def factory(first_name=None):
      return None

  the terminal updates to show a :doc:`TypeError` for the next keyword argument

* add a keyword argument for ``last_name``  to the ``factory`` function

  .. code-block:: python

   def factory(first_name=None, last_name=None):
    return None

  the terminal updates to show a :doc:`TypeError` for the next keyword argument

* I update the ``factory`` function definition for each keyword until I geta :doc:`TypeError` for the line where I subtract ``this_year() - this_year()`` because I cannot perform a subtraction operation on :doc:`None <data_structures_none>` and the ``this_year`` function currently returns :doc:`None <data_structures_none>`
* update the definition for ``this_year`` using a function from the `datetime <https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime>`_ library that returns the current year I am in

  .. code-block:: python

  import unittest
  import person
  import datetime

  def this_year():
    return datetime.datetime.now().year


  - I import the ``datetime`` library so I can use its :doc:`functions` and :doc:`classes`
  - I return the ``year`` attribute of the object returned by the ``now`` :doc:`method <functions>` of the ``datetime.datetime`` class, which is a representation of the current local date and time, I could also use ``today`` or ``utcnow`` to achieve the same result
  - I get the ``year`` attribute of the object returned since that is all I am interested in

* the terminal updates to show an :doc:`AssertionError` since the ``person.factory`` function returns :doc:`None <data_structures_none>` but the test expectsa :doc:`data structures: dictionaries`. I should update the function to return an empty dictionary

  .. code-block:: python

    def factory(first_name=None, last_name=None, year_of_birth=None, sex=None):
      return {}

  the terminal updates to show the differences between the :doc:`data structures: dictionaries` returned by the ``factory`` function and the one expected in the test

* I update the empty ``dictionary`` in the ``factory`` function to match the expected results

  .. code-block:: python

    def factory(first_name=None, last_name=None, year_of_birth=None, sex=None):
      return {
       "age": 0,
       "first_name": "sibling",
       "last_name": "last_name",
       "sex": "F",
      }

  *LOVELY!* the tests pass! Even though the tests pass, the factory function currently returns the exact same dictionary every time, regardless of what information is given to it. To make it more useful I need it to be able to use the inputs given.

* add another test to ``test_person_factory.py`` with a different set of inputs

  .. code-block:: python

   def test_person_factory_takes_in_variable_inputs(self):
    self.assertEqual(
      person.factory(
        first_name="me",
        last_name="last_name",
        year_of_birth=1983,
        sex="M",
      ),
      {
        "first_name": "me",
        "last_name": "last_name",
        "sex": "M",
        "age": this_year() - 1983
      }
    )

  the terminal updates to show an :doc:`AssertionError` because the expected and returned dictionaries are different

* modify the ``factory`` function to use the input provided for ``first_name``

  .. code-block:: python

    def factory(first_name=None, last_name=None, year_of_birth=None, sex=None):
      return {
       'age': 0,
       'first_name': first_name,
       'last_name': 'last_name',
       'sex': 'F',
      }

  the terminal updates to show an :doc:`AssertionError` but it no longer shows a difference for ``first_name``. Good, What if I repeat it step by step for every other input until the only error left is for the age

* For the age to be accurate it has to be a calculation based on the current year. I have a function that returns the current year and I have the ``year_of_birth`` as input, I also have this line in the test ``this_year() - 1983``. Since ``1983`` is the ``year_of_birth`` in this case. I can try updating the ``factory`` function to use that calculation

  .. code-block:: python

   def factory(first_name=None, last_name=None, year_of_birth=None, sex=None):
    return {
      'age': this_year() - year_of_birth,
      'first_name': first_name,
      'last_name': last_name,
      'sex': sex,
    }

  the terminal updates to show a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ since I am calling a function that does not exist in ``person.py``

* replace ``this_year()`` with the return value from ``test_person_factory.this_year`` and add an import statement

  .. code-block:: python

   import datetime

   def factory(first_name=None, last_name=None, year_of_birth=None, sex=None):
    return {
      'age': datetime.datetime.now().year - year_of_birth,
      'first_name': first_name,
      'last_name': last_name,
      'sex': sex,
    }

  *HOORAY!* the terminal updates to show passing tests

* I will now add another test to ``test_person.py``, this time for default values

  .. code-block:: python

  def test_person_factory_with_default_keyword_arguments(self):
    self.assertEqual(
      person.factory(
       first_name="child_a",
       year_of_birth=2014,
       sex="M",
      ),
      {
       "first_name": "child_a",
       "last_name": "last_name",
       "sex": "M",
       "age": this_year() - 2014
      }
    )

  the terminal updates to show an :doc:`AssertionError` since the value for ``last_name`` does not match the expected value

* since I now have 3 tests with the same value for ``last_name`` I could use that value as the default value in the absence of any other examples. modify the default value for ``last_name`` in the ``person.factory`` definition

  .. code-block:: python

    def factory(first_name=None, last_name="last_name", year_of_birth=None, sex=None):

  the terminal updates to show passing tests

* what if I try another default value, this time say for sex. add a test to ``test_person_factory_with_default_keyword_arguments``

  .. code-block:: python

   self.assertEqual(
    person.factory(
      first_name="person",
      year_of_birth=1900,
    ),
    {
      "first_name": "person",
      "last_name": "last_name",
      "age": this_year() - 1900,
      "sex": "M"
    }
   )

  the terminal updates to show an :doc:`AssertionError`

* since 3 out of the 4 persons created have ``M`` as their sex and 1 has ``F`` as their sex, I could set the majority as the default value to reduce the number of repetitions. modify the default value for the parameter in ``person.factory``

  .. code-block:: python

    def factory(first_name=None, last_name="last_name", year_of_birth=None, sex='M'):

  the terminal updates to show passing tests.