
Data Structures: Dictionaries
=============================

This chapter covers `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ in python.

Dictionaries/Mappings are key-value pairs that represent data. ``values`` can be any of the python data structures including `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

I think this is the most important data structure to know as it can contain all the other data structures and in your programming journey you will come across JSON which you can use as `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

How to create a dictionary with strings as keys
------------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a file called ``test_dictionaries.py`` to the ``tests`` folder with the following import statements

.. code-block:: python

  import unittest
  import dictionaries

the terminal displays a :doc:`/exceptions/ModuleNotFoundError`\  which I add to the list of exceptions encountered

.. code-block:: python

  # Exceptions Encountered
  # ModuleNotFoundError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

adding a file called ``dictionaries.py`` to the project folder makes the test pass

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

* I add a failing test to explore how to create a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

  .. code-block:: python

    class TestDictionaries(unittest.TestCase):

      def test_creating_dictionaries_with_strings_as_keys(self):
          self.assertEqual(
              dictionaries.a_dict(),
              {"key": "value"}
          )

  the terminal shows an :doc:`/exceptions/AttributeError` which I add to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # ModuleNotFoundError
    # AttributeError

* I add a function definition to ``dictionaries.py``

  .. code-block:: python

    def a_dict():
        return None

  and the terminal shows an :doc:`/exceptions/AssertionError` since the function I defined returns :doc:`None <data_structures_none>` instead of a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
* I then change the return statement to return an empty `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

  .. code-block:: python

    def a_dict():
        return {}

  the terminal still shows an :doc:`/exceptions/AssertionError` but now the return value looks more like what is expected

  .. code-block:: python

      E    AssertionError: {} != {'key': 'value'}
      E    - {}
      E    + {'key': 'value'}

  - ``AssertionError:`` shows that two values are not equal
  - the value on the left ``{}`` is what the function returns, in other words the result of calling ``dictionaries.a_dict()`` from the test
  - the value on the right ``{'key': 'value'}`` is what is expected
  - the ``!=`` symbol means ``not equal to``

* I change the return statement with the expected values and I get a passing test. YES! We are off to a good start

  .. code-block:: python

    def a_dict():
        return {'key': 'value'}

* it is also possible to create a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ using the `dict <https://docs.python.org/3/library/stdtypes.html#dict>`_ constructor. I add another test to ``test_creating_dictionaries_with_strings_as_keys``

  .. code-block:: python

    def test_creating_dictionaries_with_strings_as_keys(self):
        self.assertEqual(
            dictionaries.a_dict(),
            {'key': 'value'}
        )
        self.assertEqual(
            dictionaries.a_dict(),
            dict(key='value')
        )

  the terminal shows passing tests, because ``dict(key='value')`` and ``{'key': 'value'}`` are two ways of representing the same thing
* I can add another test to confirm, even though it repeats the two tests above

  .. code-block:: python

    def test_creating_dictionaries_with_strings_as_keys(self):
        self.assertEqual(
            dictionaries.a_dict(),
            {"key": "value"}
        )
        self.assertEqual(
            dictionaries.a_dict(),
            dict(key='value')
        )
        self.assertEqual(
            {"key": "value"},
            dict(key='value')
        )

How to create a dictionary with numbers as keys
------------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test to ``TestDictionaries``

.. code-block:: python

  def test_creating_dictionaries_with_numbers_as_keys(self):
      self.assertEqual(
          {1: 'boom'},
          {'one': 'boom'}
      )

the terminal shows an :doc:`/exceptions/AssertionError` since the two values are different

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the test to make it pass

.. code-block:: python

  def test_creating_dictionaries_with_numbers_as_keys(self):
      self.assertEqual(
          {1: 'boom'},
          {1: 'boom'}
      )

the terminal shows passing tests confirming that `integers <https://docs.python.org/3/library/functions.html?highlight=int#int>`_ can be used as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

* I know I can use `integers <https://docs.python.org/3/library/functions.html?highlight=int#int>`_ and `strings <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys. I want to add a test to see if I can use `floats <https://docs.python.org/3/library/functions.html?highlight=float#float>`_

  .. code-block:: python

    def test_creating_dictionaries_with_numbers_as_keys(self):
        self.assertEqual(
            {1: 'boom'},
            {1: 'boom'}
        )
        self.assertEqual(
            {2.5: 'works'},
            {2.5: 'fails'}
        )

  the terminal shows an :doc:`/exceptions/AssertionError` since the values are different
* I change the value on the right to make it pass

  .. code-block:: python

    def test_creating_dictionaries_with_numbers_as_keys(self):
      self.assertEqual(
          {1: 'boom'},
          {1: 'boom'}
      )
      self.assertEqual(
          {2.5: 'works'},
          {2.5: 'works'}
      )

  the terminal displays passing tests confirming that I can use `integers <https://docs.python.org/3/library/functions.html?highlight=int#int>`_ and `floats <https://docs.python.org/3/library/functions.html?highlight=float#float>`_ as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys

How to create a dictionary with booleans as keys
-------------------------------------------------

I wonder if it is possible to use :doc:`False </data_structures/data_structures_booleans>` or :doc:`True </data_structures/data_structures_booleans>` as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys?

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test to find out if it is possible to use :doc:`False </data_structures/data_structures_booleans>` as a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ key

.. code-block:: python

  def test_creating_dictionaries_with_booleans_as_keys(self):
      self.assertEqual(
          {False: 'boom'},
          {False: 'bap'}
      )

the terminal shows an :doc:`/exceptions/AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

when I change the values to make them match tests are green again. Sweet!

.. code-block:: python

  def test_creating_dictionaries_with_booleans_as_keys(self):
      self.assertEqual(
          {False: 'boom'},
          {False: 'boom'}
      )

I can use :doc:`False </data_structures/data_structures_booleans>` as a key in a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

* I add a test to find out if it is possible to use :doc:`True </data_structures/data_structures_booleans>` as a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ key

  .. code-block:: python

    def test_creating_dictionaries_with_booleans_as_keys(self):
        self.assertEqual(
            {False: 'boom'},
            {False: 'boom'}
        )
        self.assertEqual(
            {True: 'bap'},
            {True: 'boom'}
        )

  the terminal shows an :doc:`/exceptions/AssertionError`
* and I change the values to make the tests pass

  .. code-block:: python

    def test_creating_dictionaries_with_booleans_as_keys(self):
        self.assertEqual(
            {False: 'boom'},
            {False: 'boom'}
        )
        self.assertEqual(
            {True: 'bap'},
            {True: 'bap'}
        )

* So far from the tests, I see that I can use `booleans <https://docs.python.org/3/library/stdtypes.html#boolean-type-bool>`_, `floats <https://docs.python.org/3/library/functions.html?highlight=float#float>`_, `integers <https://docs.python.org/3/library/functions.html?highlight=int#int>`_ and `strings <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys

How to create a dictionary with tuples as keys
----------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test to ``TestDictionaries`` to see if I can use tuples as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys

.. code-block:: python

  def test_creating_dictionaries_with_tuples_as_keys(self):
      self.assertEqual(
          {(1, 2): "value"},
          {(1, 2): "key"}
      )

the terminal shows an :doc:`/exceptions/AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the values to make the test pass

.. code-block:: python

  self.assertEqual(
      {(1, 2): "value"},
      {(1, 2): "value"}
  )

the tests so far show that I can use `tuples <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_, `booleans <https://docs.python.org/3/library/stdtypes.html#boolean-type-bool>`_, `floats <https://docs.python.org/3/library/functions.html?highlight=float#float>`_, `integers <https://docs.python.org/3/library/functions.html?highlight=int#int>`_, and `strings <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys

Can I create a Dictionary with lists as keys?
----------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test to ``TestDictionaries`` using a :doc:`list <data_structures_lists>` as a key

.. code-block:: python

  def test_creating_dictionaries_with_lists_as_keys(self):
      {[1, 2]: "BOOM"}

the terminal shows a :doc:`/exceptions/TypeError` because only `hashable <https://docs.python.org/3/glossary.html#term-hashable>`_ types can be used as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys and :doc:`lists </data_structures/data_structures_lists>` are not `hashable <https://docs.python.org/3/glossary.html#term-hashable>`_

.. code-block::

  E    TypeError: unhashable type: 'list'

I also add the error to the list of exceptions encountered to include :doc:`/exceptions/TypeError`

.. code-block:: python

  # Exceptions Encountered
  # ModuleNotFoundError
  # AttributeError
  # TypeError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I can use ``self.assertRaises`` to confirm that an error is raised by some code without having it crash the tests. I will use it here to confirm that when I try to create a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with a :doc:`list <data_structures_lists>` as the key, python raises a :doc:`/exceptions/TypeError`

.. code-block:: python

  def test_creating_dictionaries_with_lists_as_keys(self):
      with self.assertRaises(TypeError):
          {[1, 2]: "BOOM"}

see :doc:`/exception_handling` for more details on why that worked and ``self.assertRaises``

Can I create a Dictionary with sets as keys?
---------------------------------------------

I try a similar test using a set as a key

RED: make it fail
^^^^^^^^^^^^^^^^^

.. code-block:: python

  def test_creating_dictionaries_with_sets_as_keys(self):
      {{1, 2}: "BOOM"}

the terminal responds with a :doc:`/exceptions/TypeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

which I handle using ``self.assertRaises``

.. code-block:: python

  def test_creating_dictionaries_with_sets_as_keys(self):
      with self.assertRaises(TypeError):
          {{1, 2}: "BOOM"}

Tests are green again

Can I create a Dictionary with dictionaries as keys?
-----------------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test

.. code-block:: python

  def test_creating_dictionaries_with_dictionaries_as_keys(self):
      a_dictionary = {"key": "value"}
      {a_dictionary: "BOOM"}

and the terminal shows a :doc:`/exceptions/TypeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I add an exception handler to confirm the findings

.. code-block:: python

    def test_creating_dictionaries_with_dictionaries_as_keys(self):
        a_dictionary = {"key": "value"}
        with self.assertRaises(TypeError):
            {a_dictionary: "BOOM"}

from these passing tests I know that I can create `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with the following data structures as keys

* `strings <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_
* `booleans <https://docs.python.org/3/library/stdtypes.html#boolean-type-bool>`_
* `integers <https://docs.python.org/3/library/functions.html?highlight=int#int>`_
* `floats <https://docs.python.org/3/library/functions.html?highlight=float#float>`_
* `tuples <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_

I CANNOT create `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with the following data structures as keys

* :doc:`lists <data_structures_lists>`
* `sets <https://docs.python.org/3/tutorial/datastructures.html#sets>`_
* `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

----

How to access dictionary values
-------------------------------

The tests so far cover how to create `dictionaries <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ and what objects can be used as ``keys``.

The following tests cover how to access the values of a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test to ``TestDictionaries`` in ``test_dictionaries.py``

.. code-block:: python

  def test_accessing_dictionary_values(self):
      a_dictionary = {"key": "value"}
      self.assertEqual(a_dictionary["key"], "bob")

the terminal displays an :doc:`/exceptions/AssertionError` because ``bob`` is not equal to ``value``. I can get a value for a key by providing the key in square brackets to the dictionary

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the expected value to make the tests pass

.. code-block:: python

  def test_accessing_dictionary_values(self):
      a_dictionary = {"key": "value"}
      self.assertEqual(a_dictionary["key"], "value")

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* I can also display the values of a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ as a :doc:`list <data_structures_lists>` without the keys

  .. code-block:: python

    def test_listing_dictionary_values(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertEqual(
            list(a_dictionary.values()), []
        )

  the terminal shows an :doc:`/exceptions/AssertionError`
* and I change the values in the test to make them match the expectation

  .. code-block:: python

    def test_listing_dictionary_values(self):
      a_dictionary = {
          'key1': 'value1',
          'key2': 'value2',
          'key3': 'value3',
          'keyN': 'valueN',
      }
      self.assertEqual(
          list(a_dictionary.values()),
          [
              'value1',
              'value2',
              'value3',
              'valueN',
          ]
      )

* I can also display the keys of a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ as a :doc:`list <data_structures_lists>`

  .. code-block:: python

    def test_listing_dictionary_keys(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertEqual(
            list(a_dictionary.keys()),
            []
        )

  the terminal shows an :doc:`/exceptions/AssertionError`
* I change the test to make it pass

  .. code-block:: python

    def test_listing_dictionary_keys(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertEqual(
            list(a_dictionary.keys()),
            [
                'key1',
                'key2',
                'key3',
                'keyN',
            ]
        )

How to get a value when the key does not exist
-----------------------------------------------

Sometimes I try to access values in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with a key that does not exist in the `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ or misspell a key that does exist

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test for both cases and the terminal shows a `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=keyerror#KeyError>`_.

.. code-block:: python

  def test_dictionaries_raise_key_error_when_key_does_not_exist(self):
      a_dictionary = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3',
        'keyN': 'valueN',
      }
      a_dictionary['non_existent_key']
      a_dictionary['ky1']

A `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ is raised when a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ is called with a ``key`` that does not exist.

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I add `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # ModuleNotFoundError
    # AttributeError
    # TypeError
    # KeyError

* then add an exception handler to confirm the error is raised

  .. code-block:: python

    def test_dictionaries_raise_key_error_when_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        with self.assertRaises(KeyError):
            a_dictionary['non_existent_key']
        a_dictionary['ky1']


* the terminal shows a `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ for the next line where I misspelled the key and I add it to the exception handler to make the test pass

  .. code-block:: python

    def test_dictionaries_raise_key_error_when_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        with self.assertRaises(KeyError):
            a_dictionary['non_existent_key']
            a_dictionary['ky1']

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

What if I want to access a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with a key that does not exist and not have python raise an error when it does not find the key?


* I add a test to ``TestDictionaries``

  .. code-block:: python

    def test_how_to_get_a_value_when_a_key_does_not_exist(self):
        a_dictionary = {
          'key1': 'value1',
          'key2': 'value2',
          'key3': 'value3',
          'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary['non_existent_key'])

  as expected the terminal shows a `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ because the ``non_existent_key`` does not exist in ``a_dictionary``
* I can use the `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ :doc:`method </functions/functions>` when I do not want python to raise a `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ for a key that does not exist

  .. code-block:: python

    def test_how_to_get_a_value_when_a_key_does_not_exist(self):
        a_dictionary = {
          'key1': 'value1',
          'key2': 'value2',
          'key3': 'value3',
          'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary.get('non_existent_key'))

  the terminal shows a passing test. This means that when I use the `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ :doc:`method </functions/functions>` and the ``key`` does not exist, I get :doc:`None <data_structures_none>` as the result.
* I can state the above explicitly because ``Explicit is better than implicit`` see `Zen of Python <https://peps.python.org/pep-0020/>`_

  .. code-block:: python

    def test_how_to_get_a_value_when_a_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary.get('non_existent_key'))
        self.assertIsNone(a_dictionary.get('non_existent_key', None))

  the terminal shows passing tests.
* The `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ :doc:`method </functions/functions>` takes in 2 inputs

  - the ``key``
  - the ``default value`` wanted when the ``key`` does not exist

* I can also use the `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ :doc:`method </functions/functions>` to get the value for an existing key

  .. code-block:: python

    def test_how_to_get_a_value_when_a_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary.get('non_existent_key'))
        self.assertIsNone(a_dictionary.get('non_existent_key', None))
        self.assertEqual(a_dictionary.get('key1', None), None)

  the terminal shows an `Assertion Error <./AssertionError.rst>`_ because ``value1`` which is the value for ``key1`` in ``a_dictionary`` is not equal to :doc:`None <data_structures_none>`
* I change the test to make it pass.

  .. code-block:: python

    def test_how_to_get_a_value_when_a_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary.get('non_existent_key'))
        self.assertIsNone(a_dictionary.get('non_existent_key', None))
        self.assertEqual(a_dictionary.get('key1', None), 'value1')

Do you think you could write an implementation for the ``get`` method after reading :doc:`/exception_handling`

How to view the attributes and methods of a dictionary
------------------------------------------------------

:doc:`class </classes>` covers how to view the ``attributes`` and ``methods`` of an object. Let us look at the attributes and :doc:`methods </functions/functions>` of  `dictionaries <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ to help understand them better

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test to ``TestDictionaries``

.. code-block:: python

  def test_dictionary_attributes(self):
      self.maxDiff = None
      self.assertEqual(
          dir(dictionaries.a_dict()),
          []
      )

the terminal shows an :doc:`/exceptions/AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I copy the expected values shown in the terminal to make the test pass

.. warning::

  Your results may vary based on your python version


.. code-block:: python

  def test_dictionary_attributes(self):
      self.maxDiff = None
      self.assertEqual(
          dir(dictionaries.a_dict()),
          [
              '__class__',
              '__class_getitem__',
              '__contains__',
              '__delattr__',
              '__delitem__',
              '__dir__',
              '__doc__',
              '__eq__',
              '__format__',
              '__ge__',
              '__getattribute__',
              '__getitem__',
              '__gt__',
              '__hash__',
              '__init__',
              '__init_subclass__',
              '__ior__',
              '__iter__',
              '__le__',
              '__len__',
              '__lt__',
              '__ne__',
              '__new__',
              '__or__',
              '__reduce__',
              '__reduce_ex__',
              '__repr__',
              '__reversed__',
              '__ror__',
              '__setattr__',
              '__setitem__',
              '__sizeof__',
              '__str__',
              '__subclasshook__',
              'clear',
              'copy',
              'fromkeys',
              'get',
              'items',
              'keys',
              'pop',
              'popitem',
              'setdefault',
              'change',
              'values'
          ]
      )


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

I see some of the :doc:`methods </functions/functions>` I have covered so far and others I did not. I  could write tests for the others to discover what they do and/or `read more about dictionaries <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_.

* clear
* copy
* fromkeys
* get - gets the ``value`` for a ``key`` and returns a default value or :doc:`None <data_structures_none>` when the key does not exist
* items
* keys - returns a view of the ``keys`` in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
* `pop <https://docs.python.org/3/library/stdtypes.html#dict.pop>`_
* `popitem <https://docs.python.org/3/library/stdtypes.html#dict.popitem>`_
* `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_
* `change <https://docs.python.org/3/library/stdtypes.html#dict.change>`_
* values - returns a view of the ``values`` in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

How to set a default value for a given key
------------------------------------------

Let us say I want to find out more about the `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_ method

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test and the terminal shows a `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_

.. code-block:: python

  def test_set_default_for_a_given_key(self):
      a_dictionary = {'bippity': 'boppity'}
      a_dictionary['another_key']

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I add ``self.assertRaises`` to confirm that a `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ gets raised for the test to pass

.. code-block:: python

  def test_set_default_for_a_given_key(self):
      a_dictionary = {'bippity': 'boppity'}

      with self.assertRaises(KeyError):
          a_dictionary['another_key']

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

* I then add a test for `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_

  .. code-block:: python

    def test_set_default_for_a_given_key(self):
        a_dictionary = {'bippity': 'boppity'}

        with self.assertRaises(KeyError):
            a_dictionary['another_key']

        a_dictionary.setdefault('another_key')
        self.assertEqual(
            a_dictionary,
            {'bippity': 'boppity'}
        )

  the terminal shows that ``a_dictionary`` has changed, by giving us an :doc:`/exceptions/AssertionError`. It has a new key which was not there before

* I change the test to make it pass

  .. code-block:: python

    def test_set_default_for_a_given_key(self):
        a_dictionary = {'bippity': 'boppity'}

        with self.assertRaises(KeyError):
            a_dictionary['another_key']

        a_dictionary.setdefault('another_key')
        self.assertEqual(
            a_dictionary,
            {
              'bippity': 'boppity',
              'another_key': None
            }
        )

  when I first try to access the value for ``another_key`` in ``a_dictionary`` I get a `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ because it does not exist in the `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

  After using `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_ and passing in ``another_key`` as the key, it gets added to the `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ so I will not get an error when I try to access it again

  .. code-block:: python

    def test_set_default_for_a_given_key(self):
        a_dictionary = {'bippity': 'boppity'}

        with self.assertRaises(KeyError):
            a_dictionary['another_key']

        a_dictionary.setdefault('another_key')
        self.assertEqual(
            a_dictionary,
            {
              'bippity': 'boppity',
              'another_key': None
            }
        )
        self.assertIsNone(a_dictionary['another_key'])

* I will now add a test for setting the default value to something other than :doc:`None <data_structures_none>`

  .. code-block:: python

    a_dictionary.setdefault('a_new_key', 'a_default_value')
    self.assertEqual(
        a_dictionary,
        {
          'bippity': 'boppity',
          'another_key': None
        }
    )

  the terminal shows an :doc:`/exceptions/AssertionError` since ``a_dictionary`` now has a new ``key`` and ``value``
* I change the test to make it pass

  .. code-block:: python

    self.assertEqual(
        a_dictionary,
        {
          'bippity': 'boppity',
          'another_key': None,
          'a_new_key': 'a_default_value',
        }
    )

  all tests pass, and I add what I know about `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_ to the list of attributes and :doc:`methods </functions/functions>` of `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

How to update a dictionary with another dictionary
--------------------------------------------------

What if I want to add the ``keys`` and ``values`` of one `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ to another?

RED: make it fail
^^^^^^^^^^^^^^^^^

I add another test to ``TestDictionaries``

.. code-block:: python

  def test_adding_two_dictionaries(self):
      a_dictionary = {
          "basic": "toothpaste",
          "whitening": "peroxide",
      }
      a_dictionary.update({
          "traditional": "chewing stick",
          "browning": "tobacco",
          "decaying": "sugar",
      })
      self.assertEqual(
          a_dictionary,
          {
              "basic": "toothpaste",
              "whitening": "peroxide",
          }
      )

the terminal displays an :doc:`/exceptions/AssertionError` because the values of ``a_dictionary`` were changed when I called the `update <https://docs.python.org/3/library/stdtypes.html#dict.update>`_ :doc:`method </functions/functions>` on it

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the values to make it pass

.. code-block:: python

  def test_adding_two_dictionaries(self):
      a_dictionary = {
          "basic": "toothpaste",
          "whitening": "peroxide",
      }
      a_dictionary.update({
          "traditional": "chewing stick",
          "browning": "tobacco",
          "decaying": "sugar",
      })
      self.assertEqual(
          a_dictionary,
          {
              "basic": "toothpaste",
              "whitening": "peroxide",
              "traditional": "chewing stick",
              "browning": "tobacco",
              "decaying": "sugar",
          }
      )

How to remove an item from a dictionary
---------------------------------------

I can remove an item from a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with the `pop <https://docs.python.org/3/library/stdtypes.html#dict.pop>`_ method. It deletes the ``key`` and ``value`` from the `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ and returns the ``value``

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test to ``TestDictionaries``

.. code-block:: python

  def test_pop(self):
      a_dictionary = {
        "basic": "toothpaste",
        "whitening": "peroxide",
        "traditional": "chewing stick",
        "browning": "tobacco",
        "decaying": "sugar",
      }
      self.assertEqual(a_dictionary.pop("basic"), None)

the terminal shows an :doc:`/exceptions/AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I change the test with the right value to make it pass

  .. code-block:: python

    def test_pop(self):
        a_dictionary = {
          "basic": "toothpaste",
          "whitening": "peroxide",
          "traditional": "chewing stick",
          "browning": "tobacco",
          "decaying": "sugar",
        }
        self.assertEqual(a_dictionary.pop("basic"), "toothpaste")

* then add a test to confirm that ``a_dictionary`` has changed

  .. code-block:: python

    def test_pop(self):
        a_dictionary = {
            "basic": "toothpaste",
            "whitening": "peroxide",
            "traditional": "chewing stick",
            "browning": "tobacco",
            "decaying": "sugar",
        }
        self.assertEqual(a_dictionary.pop("basic"), "toothpaste")
        self.assertEqual(
            a_dictionary,
            {
                "basic": "toothpaste",
                "whitening": "peroxide",
                "traditional": "chewing stick",
                "browning": "tobacco",
                "decaying": "sugar",
            }
        )

  the terminal responds with an :doc:`/exceptions/AssertionError` confirming that ``a_dictionary`` is different

* The test passes when I remove the key-value pairs of ``basic`` and ``toothpaste``

  .. code-block:: python

    def test_pop(self):
        a_dictionary = {
            "basic": "toothpaste",
            "whitening": "peroxide",
            "traditional": "chewing stick",
            "browning": "tobacco",
            "decaying": "sugar",
        }
        self.assertEqual(a_dictionary.pop("basic"), "toothpaste")
        self.assertEqual(
            a_dictionary,
            {
                "whitening": "peroxide",
                "traditional": "chewing stick",
                "browning": "tobacco",
                "decaying": "sugar",
            }
        )

----

WOW! You made it to the end of the chapter on `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ and now know

* How to create a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
* What objects can be used as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys
* What objects cannot be used as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys
* How to view `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys
* How to view `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ values
* How to view the attributes and :doc:`methods </functions/functions>` of a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
* How to set a default value for a key
* How to change a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with another `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
* How to remove an item from a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_