.. include:: ../links.rst

dictionaries
==============================

.. contents:: table of contents
  :local:
  :depth: 1

----

This chapter goes over `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ in Python. Dictionaries, also called Mappings, are key-value pairs that represent data, values can be any Python :ref:`object<classes>`.

I think this is the most important data structure to know as it can hold all the other data structures and in your programming journey you will come across JSON_ which you can read and write as `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

----

how to make a dictionary with strings as keys
------------------------------------------------

red: make it fail
#################################################################################

I add a file called ``test_dictionaries.py`` to the ``tests`` folder with the following import statements

.. code-block:: python

  import unittest
  import dictionaries

the terminal shows :ref:`ModuleNotFoundError`  which I add to the list of Exceptions_ encountered

.. code-block:: python

  # Exceptions Encountered
  # ModuleNotFoundError

green: make it pass
#################################################################################

adding a file called ``dictionaries.py`` to the project folder makes the test pass

refactor: make it better
#################################################################################

* I add a failing test to show how to make a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

  .. code-block:: python

    class TestDictionaries(unittest.TestCase):

      def test_making_dictionaries_w_strings_as_keys(self):
          self.assertEqual(
              dictionaries.a_dict(),
              {"key": "value"}
          )

  the terminal shows :ref:`AttributeError` which I add to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # ModuleNotFoundError
    # AttributeError

* I add a :ref:`function<functions>` definition to ``dictionaries.py``

  .. code-block:: python

    def a_dict():
        return None

  and the terminal shows :ref:`AssertionError` since the :ref:`function<functions>` I defined returns :ref:`None` instead of a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

  .. code-block:: python

    AssertionError: None != {'key': 'value'}

* I make the `return statement`_ send an empty `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

  .. code-block:: python

    def a_dict():
        return {}

  the terminal still shows :ref:`AssertionError` but with a return value that looks more like what is expected

  .. code-block:: python

      E    AssertionError: {} != {'key': 'value'}

  - ``AssertionError: {} != {'key': 'value'}`` shows that 2 values are not equal
  - the value on the left ``{}`` is what the :ref:`function<functions>` returns, in other words the result of calling ``dictionaries.a_dict()`` from the test
  - the value on the right ``{'key': 'value'}`` is what is expected
  - ``!=`` means ``not equal to``

* I make the `return statement`_ with the expected values and I get a passing test. YES! We are off to a good start

  .. code-block:: python

    def a_dict():
        return {'key': 'value'}

* it is also possible to make a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ using the dict_ constructor_. I add another test to ``test_making_dictionaries_w_strings_as_keys``

  .. code-block:: python

    def test_making_dictionaries_w_strings_as_keys(self):
        self.assertEqual(
            dictionaries.a_dict(),
            {'key': 'value'}
        )
        self.assertEqual(
            dictionaries.a_dict(),
            dict(key='key')
        )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

      AssertionError: {'key': 'value'} != {'key': 'key'}


  so I change the test to make it pass

  .. code-block:: python

    self.assertEqual(
        dictionaries.a_dict(),
        dict(key='value')
    )

  the terminal shows passing tests, because ``dict(key='value')`` and ``{'key': 'value'}`` are 2 ways of representing the same thing
* I can add another test to make sure, even though it repeats the 2 tests above

  .. code-block:: python

    def test_making_dictionaries_w_strings_as_keys(self):
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
            dict(key='key')
        )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} != {'key': 'key'}

* I change the test to make it pass

  .. code-block:: python

    self.assertEqual(
        {"key": "value"},
        dict(key='value')
    )

----

how to make a dictionary with numbers as keys
------------------------------------------------

red: make it fail
#################################################################################

I add a failing test to ``TestDictionaries``

.. code-block:: python

  def test_making_dictionaries_w_numbers_as_keys(self):
      self.assertEqual(
          {1: 'boom'},
          {'one': 'boom'}
      )

the terminal shows :ref:`AssertionError` since the 2 values are different

.. code-block:: python

  AssertionError: {1: 'boom'} != {'one': 'boom'}


green: make it pass
#################################################################################

I make the values in the test to make it pass

.. code-block:: python

  def test_making_dictionaries_w_numbers_as_keys(self):
      self.assertEqual(
          {1: 'boom'},
          {1: 'boom'}
      )

the terminal shows passing tests showing that integers_ can be used as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys

refactor: make it better
#################################################################################

* I know I can use integers_ and strings_ as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys. I want to add a test to see if I can use floats_

  .. code-block:: python

    def test_making_dictionaries_w_numbers_as_keys(self):
        self.assertEqual(
            {1: 'boom'},
            {1: 'boom'}
        )
        self.assertEqual(
            {2.5: 'works'},
            {2.5: 'fails'}
        )

  the terminal shows :ref:`AssertionError` since the values are different

  .. code-block:: python

    AssertionError: {2.5: 'works'} != {2.5: 'fails'}
    - {2.5: 'works'}
    + {2.5: 'fails'}

* I make the values in the test to make it pass

  .. code-block:: python

    def test_making_dictionaries_w_numbers_as_keys(self):
      self.assertEqual(
          {1: 'boom'},
          {1: 'boom'}
      )
      self.assertEqual(
          {2.5: 'works'},
          {2.5: 'works'}
      )

  the terminal shows passing tests showing that I can use integers_ and floats_ as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys

----

how to make a dictionary with booleans as keys
-------------------------------------------------

I wonder if it is possible to use :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>` as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys

red: make it fail
#################################################################################

I add a test to find out if it is possible to use :ref:`False<test_what_is_false>` as a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ key

.. code-block:: python

  def test_making_dictionaries_w_booleans_as_keys(self):
      self.assertEqual(
          {False: 'boom'},
          {False: 'bap'}
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python
  :force:

  AssertionError: {False: 'boom'} != {False: 'bap'}
  - {False: 'boom'}
  ?           ^^^

  + {False: 'bap'}
  ?           ^^

green: make it pass
#################################################################################

I make the values to make them match and tests are green again. Sweet!

.. code-block:: python

  def test_making_dictionaries_w_booleans_as_keys(self):
      self.assertEqual(
          {False: 'boom'},
          {False: 'boom'}
      )

I can use :ref:`False<test_what_is_false>` as a key in a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

refactor: make it better
#################################################################################

* I add a test to find out if it is possible to use :ref:`True<test_what_is_true>` as a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ key

  .. code-block:: python

    def test_making_dictionaries_w_booleans_as_keys(self):
        self.assertEqual(
            {False: 'boom'},
            {False: 'boom'}
        )
        self.assertEqual(
            {True: 'bap'},
            {True: 'boom'}
        )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python
    :force:

    AssertionError: {True: 'bap'} != {True: 'boom'}
    - {True: 'bap'}
    ?          ^^

    + {True: 'boom'}
    ?

* and I make the values to make the tests pass

  .. code-block:: python

    def test_making_dictionaries_w_booleans_as_keys(self):
        self.assertEqual(
            {False: 'boom'},
            {False: 'boom'}
        )
        self.assertEqual(
            {True: 'bap'},
            {True: 'bap'}
        )

So far from the tests, I see that I can use :ref:`booleans`, floats_, integers_ and strings_ as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys

----

how to make a dictionary with tuples as keys
----------------------------------------------

red: make it fail
#################################################################################

I add a test to ``TestDictionaries`` to see if I can use tuples as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys

.. code-block:: python

  def test_making_dictionaries_w_tuples_as_keys(self):
      self.assertEqual(
          {(1, 2): "value"},
          {(1, 2): "key"}
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python
  :force:

  AssertionError: {(1, 2): 'value'} != {(1, 2): 'key'}
  - {(1, 2): 'value'}
  ?           ^^^^

  + {(1, 2): 'key'}
  ?           ^ +

green: make it pass
#################################################################################

I make the values to make the test pass

.. code-block:: python

  self.assertEqual(
      {(1, 2): "value"},
      {(1, 2): "value"}
  )

the tests so far show that I can use tuples_, :ref:`booleans`, floats_, integers_, and strings_ as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys

----

Can I make a Dictionary with a list as a key?
-------------------------------------------------

red: make it fail
#################################################################################

I add a test to ``TestDictionaries`` using a :ref:`list <lists>` as a key

.. code-block:: python

  def test_making_dictionaries_w_lists_as_keys(self):
      {[1, 2]: "BOOM"}

the terminal shows :ref:`TypeError` because only `hashable <https://docs.python.org/3/glossary.html#term-hashable>`_ types can be used as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys and :ref:`lists` are not `hashable <https://docs.python.org/3/glossary.html#term-hashable>`_

.. code-block::

  E    TypeError: unhashable type: 'list'

I add :ref:`TypeError` to the list of Exceptions_ encountered

.. code-block:: python

  # Exceptions Encountered
  # ModuleNotFoundError
  # AttributeError
  # TypeError

green: make it pass
#################################################################################

I can use ``self.assertRaises`` to make sure that an error is raised by some code without having it crash the tests. I use it here to make sure that Python raises :ref:`TypeError` when I try to make a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with a :ref:`list <lists>` as the key

.. code-block:: python

  def test_making_dictionaries_w_lists_as_keys(self):
      with self.assertRaises(TypeError):
          {[1, 2]: "BOOM"}

see :doc:`/how_to/exception_handling_tests` for more details on why that worked.

From the test I see that I cannot make a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with a :ref:`list <lists>` as a key

----

Can I make a Dictionary with a set as a key?
------------------------------------------------

I try a similar test using a set as a key

red: make it fail
#################################################################################

.. code-block:: python

  def test_making_dictionaries_w_sets_as_keys(self):
      {{1, 2}: "BOOM"}

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: unhashable type: 'set'

green: make it pass
#################################################################################

I use ``self.assertRaises`` to handle the exception

.. code-block:: python

  def test_making_dictionaries_w_sets_as_keys(self):
      with self.assertRaises(TypeError):
          {{1, 2}: "BOOM"}

Tests are green again. I cannot use a set_ or a :ref:`list <lists>` as a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ key

----

Can I make a Dictionary with a dictionary as a key?
-------------------------------------------------------

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_making_dictionaries_w_dictionaries_as_keys(self):
      a_dictionary = {"key": "value"}
      {a_dictionary: "BOOM"}

and the terminal shows :ref:`TypeError`

.. code-block:: python

  >       {a_dictionary: "BOOM"}
  E       TypeError: unhashable type: 'dict'

green: make it pass
#################################################################################

I add an :ref:`how to test that an Exception is raised` to the test to test the findings

.. code-block:: python

    def test_making_dictionaries_w_dictionaries_as_keys(self):
        a_dictionary = {"key": "value"}
        with self.assertRaises(TypeError):
            {a_dictionary: "BOOM"}

and the terminal shows passing tests. I cannot use a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_, set_ or a :ref:`list <lists>` as a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ key

----

from these tests I know that I can make `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with the following data structures as keys

* strings_
* :ref:`booleans`
* integers_
* floats_
* tuples_

and I cannot make `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with the following data structures as keys

* :ref:`lists`
* sets_
* `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

----

how to access dictionary values
-------------------------------

The tests so far show how to make `dictionaries <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ and what objects can be used as ``keys``. The following tests show how to access the values of a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

red: make it fail
#################################################################################

I add a test to ``TestDictionaries`` in ``test_dictionaries.py``

.. code-block:: python

  def test_accessing_dictionary_values(self):
      a_dictionary = {"key": "value"}
      self.assertEqual(a_dictionary["key"], "bob")

the terminal shows :ref:`AssertionError` because ``bob`` is not equal to ``value``. I can get a value for a key by providing the key in square brackets to the dictionary

.. code-block:: python

  AssertionError: 'value' != 'bob'

green: make it pass
#################################################################################

I make the expected value to make the tests pass

.. code-block:: python

  def test_accessing_dictionary_values(self):
      a_dictionary = {"key": "value"}
      self.assertEqual(a_dictionary["key"], "value")

refactor: make it better
#################################################################################

* I can also show all the values of a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ as a :ref:`list <lists>` without the keys

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

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['value1', 'value2', 'value3', 'valueN'] != []

* the tests pass when I make the values in the test to make them match the result

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

* I can also show the keys of a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ as a :ref:`list <lists>`

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

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['key1', 'key2', 'key3', 'keyN'] != []

* I add the values to the empty list in the test to make it pass

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

----

how to get a value when the key does not exist
-----------------------------------------------

Sometimes when I try to access values in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_, I use a key that does not exist or misspell a key that does exist

red: make it fail
#################################################################################

I add a test for both cases

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

and the terminal shows a KeyError_

.. code-block:: python

  >       a_dictionary['non_existent_key']
  E       KeyError: 'non_existent_key'

KeyError_ is raised when a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ is called with a ``key`` that does not exist.

green: make it pass
#################################################################################

* I add KeyError_ to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # ModuleNotFoundError
    # AttributeError
    # TypeError
    # KeyError

* then add an :ref:`how to test that an Exception is raised` to make sure that the error is raised

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

* the terminal shows KeyError_ for the next line where I misspelled the key

  .. code-block:: python

    >       a_dictionary['ky1']
    E       KeyError: 'ky1'

  and I add it to the :ref:`how to test that an Exception is raised` to make the test pass

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

refactor: make it better
#################################################################################

What if I want to access a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with a key that does not exist and not have Python raise an error when it does not find the key?


* I add a test called ``test_how_to_get_a_value_when_a_key_does_not_exist`` to ``TestDictionaries``

  .. code-block:: python

    def test_how_to_get_a_value_when_a_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary['non_existent_key'])

  the terminal shows KeyError_ because ``non_existent_key`` does not exist in ``a_dictionary``

  .. code-block:: python

    >       self.assertIsNone(a_dictionary['non_existent_key'])
    E       KeyError: 'non_existent_key'

* I can use the `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ :ref:`method<functions>` when I do not wantPython to raise KeyError_ for a key that does not exist

  .. code-block:: python

    def test_how_to_get_a_value_when_a_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary.get('non_existent_key'))

  the terminal shows a passing test. This means that when I use the `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ :ref:`method<functions>` and the ``key`` does not exist, I get :ref:`None` as the result.
* I can state the above explicitly, from the `Zen of Python`_: ``Explicit is better than implicit``

  .. code-block:: python

    def test_how_to_get_a_value_when_a_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary.get('non_existent_key'))
        self.assertIsNone(a_dictionary.get('non_existent_key', False))

  the terminal shows :ref:`AssertionError` because :ref:`False<test_what_is_false>` is not :ref:`None`

  .. code-block:: python

    >       self.assertIsNone(a_dictionary.get('non_existent_key', False))
    E       AssertionError: False is not None

  so I make the value to make the test pass

  .. code-block:: python

    self.assertIsNone(a_dictionary.get('non_existent_key', None))

  the terminal shows passing tests.
* The `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ :ref:`method<functions>` takes in 2 inputs

  - the ``key``
  - the ``default value`` wanted when the ``key`` does not exist

* I can also use the `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ :ref:`method<functions>` to get the value for an existing key

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

  the terminal shows :ref:`AssertionError` because ``value1`` which is the value for ``key1`` in ``a_dictionary`` is not equal to :ref:`None`

  .. code-block:: python

    >       self.assertEqual(a_dictionary.get('key1', None), None)
    E       AssertionError: 'value1' != None

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

Do you think you could write an implementation for the ``get`` method after reading :doc:`/how_to/exception_handling_programs`?

how to view the attributes and methods of a dictionary
-------------------------------------------------------

The chapter on :ref:`classes` shows how to view the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of an object. Let us look at the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of `dictionaries <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

red: make it fail
#################################################################################

I add a new test to ``TestDictionaries``

.. code-block:: python

  def test_dictionary_attributes(self):
      self.maxDiff = None
      self.assertEqual(
          dir(dictionaries.a_dict()),
          []
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: ['__class__', '__class_getitem__', '__cont[530 chars]ues'] != []

green: make it pass
#################################################################################

I copy the expected values shown in the terminal to make the test pass

.. note::

  Your results may vary based on your version of Python


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
              '__getstate__',
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
              'update',
              'values'
          ]
      )


refactor: make it better
#################################################################################

I see some of the :ref:`methods<functions>` I have tested so far and others I did not. You can write tests for the others to show what they do and/or `read more about dictionaries <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_.

* `clear <https://docs.python.org/3/library/stdtypes.html#dict.clear>`_
* `copy <https://docs.python.org/3/library/stdtypes.html#dict.copy>`_
* `fromkeys <https://docs.python.org/3/library/stdtypes.html#dict.fromkeys>`_
* `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ - gets the ``value`` for a ``key`` and returns a default value or :ref:`None` when the key does not exist
* `items <https://docs.python.org/3/library/stdtypes.html#dict.items>`_
* `keys <https://docs.python.org/3/library/stdtypes.html#dict.keys>`_ - returns a view of the ``keys`` in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
* `pop <https://docs.python.org/3/library/stdtypes.html#dict.pop>`_
* `popitem <https://docs.python.org/3/library/stdtypes.html#dict.popitem>`_
* `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_
* `change <https://docs.python.org/3/library/stdtypes.html#dict.change>`_
* `values <https://docs.python.org/3/library/stdtypes.html#dict.values>`_ - returns a view of the ``values`` in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

how to set a default value for a given key
-------------------------------------------

Let us say I want to find out more about the `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_ method

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_set_default_for_a_given_key(self):
      a_dictionary = {'bippity': 'boppity'}
      a_dictionary['another_key']

and the terminal shows KeyError_

green: make it pass
#################################################################################

I add ``self.assertRaises`` to make sure that KeyError_ gets raised for the test to pass

.. code-block:: python

  def test_set_default_for_a_given_key(self):
      a_dictionary = {'bippity': 'boppity'}

      with self.assertRaises(KeyError):
          a_dictionary['another_key']

refactor: make it better
#################################################################################

* Then I add a test for `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_

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

  the terminal shows :ref:`AssertionError` because ``a_dictionary`` has changed, it has a new key which was not there before

  .. code-block:: python

    AssertionError: {'bippity': 'boppity', 'another_key': None} != {'bippity': 'boppity'}
    - {'another_key': None, 'bippity': 'boppity'}
    + {'bippity': 'boppity'}


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

  - when I first try to access the value for ``another_key`` in ``a_dictionary`` I get KeyError_ because it does not exist in the `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
  - after using `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_ and passing in ``another_key`` as the key, it gets added to the `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ so I do not get KeyError_ when I try to access it again

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

* I now add a test for setting the default value to something other th :ref:`None`

  .. code-block:: python

    a_dictionary.setdefault('a_new_key', 'a_default_value')
    self.assertEqual(
        a_dictionary,
        {
            'bippity': 'boppity',
            'another_key': None
        }
    )

  the terminal shows :ref:`AssertionError` since ``a_dictionary`` now has a new ``key`` and ``value``

  .. code-block:: python

    AssertionError: {'bippity': 'boppity', 'another_key': None, 'a_new_key': 'a_default_value'} != {'bippity': 'boppity', 'another_key': None}
    - {'a_new_key': 'a_default_value', 'another_key': None, 'bippity': 'boppity'}
    + {'another_key': None, 'bippity': 'boppity'}

* I add the new values to the test to make it pass

  .. code-block:: python

    self.assertEqual(
        a_dictionary,
        {
            'bippity': 'boppity',
            'another_key': None,
            'a_new_key': 'a_default_value',
        }
    )

  all tests pass, and I add what I know about `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_ to the list of :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

test_adding_2_dictionaries
---------------------------------------------------

What if I want to add the ``keys`` and ``values`` of one `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ to another?

red: make it fail
#################################################################################

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

the terminal shows :ref:`AssertionError` because the values of ``a_dictionary`` were changed when I called the `update <https://docs.python.org/3/library/stdtypes.html#dict.update>`_ :ref:`method<functions>` on it

.. code-block:: python

  AssertionError: {'bas[37 chars]xide', 'traditional': 'chewing stick', 'browni[31 chars]gar'} != {'bas[37 chars]xide'}
  + {'basic': 'toothpaste', 'whitening': 'peroxide'}
  - {'basic': 'toothpaste',
  -  'browning': 'tobacco',
  -  'decaying': 'sugar',
  -  'traditional': 'chewing stick',
  -  'whitening': 'peroxide'}


green: make it pass
#################################################################################

I make the values to make the test pass

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

how to remove an item from a dictionary
----------------------------------------

I can remove an item from a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with the `pop <https://docs.python.org/3/library/stdtypes.html#dict.pop>`_ method. It deletes the ``key`` and ``value`` from the `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ and returns the ``value``

red: make it fail
#################################################################################

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

the terminal shows :ref:`AssertionError`

.. code-block:: python

  >       self.assertEqual(a_dictionary.pop("basic"), None)
  E       AssertionError: 'toothpaste' != None

green: make it pass
#################################################################################

* I add the right value to the test to make it pass

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

* then add a test to make sure that ``a_dictionary`` has changed

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

  the terminal shows :ref:`AssertionError` showing that ``a_dictionary`` is different

  .. code-block:: python
    :force:

    AssertionError: {'whitening': 'peroxide', 'traditional': 'c[53 chars]gar'} != {'basic': 'toothpaste', 'whitening': 'perox[76 chars]gar'}
    + {'basic': 'toothpaste',
    - {'browning': 'tobacco',
    ? ^

    +  'browning': 'tobacco',
    ? ^

       'decaying': 'sugar',
       'traditional': 'chewing stick',
       'whitening': 'peroxide'}

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

I ran tests to show

* how to make a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
* What objects can be used as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys
* What objects cannot be used as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys
* how to view `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys
* how to view `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ values
* how to view the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
* how to set a default value for a key
* how to change a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with another `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ and
* how to remove an item from a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

I alsop ran into the following Exceptions_

* :ref:`AssertionError`
* :ref:`ModuleNotFoundError`
* :ref:`AttributeError`
* :ref:`TypeError`
* NameError_

Would you like to test :ref:`functions?<functions>`

----

:doc:`/code/code_dictionaries`