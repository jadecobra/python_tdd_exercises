
Data Structures: Dictionaries
=============================

This chapter covers dictionaries in python using Test Driven Development. I think this is the most important data structure to know as it can contain all the other data structures and in your programming journey you will come across JSON which converts nicely to dictionaries.

Prerequisites
-------------


* :doc:`How to Setup a Test Driven Development Environment`
* :doc:`Data Structures </data structures>`

----

How to create a dictionary with strings as keys
------------------------------------------------

Dictionaries/Mappings are key, value pairs that represent data. ``values`` can be any of the :doc:`Data Structures </data structures>` including dictionaries

RED: make it fail
^^^^^^^^^^^^^^^^^

first I add a file called ``test_dictionaries.py`` to the ``tests`` folder with the following import statements

.. code-block:: python

   import unittest
   import dictionaries

the terminal displays a :doc:`ModuleNotFoundError`\ , and I add it to the list of exceptions encountered

.. code-block:: python

   # Exceptions Encountered
   # ModuleNotFoundError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

after adding a file called ``dictionaries.py`` to the project folder, the test passes

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* I will now proceed to look at the ways I can create a dictionary, by adding a failing test

  .. code-block:: python

   class TestDictionaries(unittest.TestCase):

       def test_creating_dictionaries_with_strings_as_keys(self):
           self.assertEqual(
               dictionaries.a_dict(),
               {"key": "value"}
           )

  the terminal updates to show an :doc:`AttributeError` and I add it to the list of exceptions encountered

  .. code-block:: python

   # Exceptions Encountered
   # ModuleNotFoundError
   # AttributeError

* I add a function definition to ``dictionaries.py``

  .. code-block:: python

       def a_dict():
           return None

  and the terminal updates to show an :doc:`AssertionError` since the function I defined returns :doc:`None </data structures: None>` instead of a dictionary
* I then update the return statement to return an empty dictionary

  .. code-block:: python

       def a_dict():
           return {}

  the terminal still shows an :doc:`AssertionError` but now the return value looks more like to what is expected

  .. code-block:: python

     E       AssertionError: {} != {'key': 'value'}
     E       - {}
     E       + {'key': 'value'}

  - the ``AssertionError:`` shows that two values are not equal
  - the value on the left ``{}`` is what the function returns, in other words the result of calling ``dictionaries.a_dict()`` from the test
  - the value on the right ``{'key': 'value'}`` is what is expected
  - the ``!=`` symbol means ``not equal to``

* I update the return statement with the expected values and I get a passing test. YES!

  .. code-block:: python

    def a_dict():
        return {'key': 'value'}

* it is also possible to create a dictionary by using the `dict <https://docs.python.org/3/library/stdtypes.html#dict>`_ class. I add another test to ``test_creating_dictionaries_with_strings_as_keys``

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

  the terminal shows passing tests, because ``dict(key='value')`` and ``{'key': 'value'}`` produce the same results
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

the terminal updates to show an :doc:`AssertionError` since the two values are different

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I update the test to make it pass

.. code-block:: python

    def test_creating_dictionaries_with_numbers_as_keys(self):
        self.assertEqual(
            {1: 'boom'},
            {1: 'boom'}
        )

the terminal updates to show passing tests confirming that `integers <https://docs.python.org/3/library/functions.html?highlight=int#int>`_ can be used as dictionary keys

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

* I know I can use `integers <https://docs.python.org/3/library/functions.html?highlight=int#int>`_ and `strings <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ as dictionary keys. I want to add a test to see if I can use `floats <https://docs.python.org/3/library/functions.html?highlight=float#float>`_

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

  the terminal updates to show an :doc:`AssertionError` since the values are different
* I update the value on the right to make it pass

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

  the terminal displays passing tests confirming that I can use `integers <https://docs.python.org/3/library/functions.html?highlight=int#int>`_ and `floats <https://docs.python.org/3/library/functions.html?highlight=float#float>`_ as keys in a dictionary.

How to create a dictionary with booleans as keys
-------------------------------------------------

Is it possible to use :doc:`False </data structures: booleans>` or :doc:`True </data structures: booleans>` as `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ keys?

RED: make it fail
^^^^^^^^^^^^^^^^^

.. code-block:: python

    def test_creating_dictionaries_with_booleans_as_keys(self):
        self.assertEqual(
            {False: 'boom'},
            {False: 'bap'}
        )

the terminal outputs an :doc:`AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

when I update the values to make them match I am green again

.. code-block:: python

  def test_creating_dictionaries_with_booleans_as_keys(self):
      self.assertEqual(
        {False: 'boom'},
        {False: 'boom'}
    )

I can use :doc:`False </data structures: booleans>` as a key in a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* I add a test for using :doc:`True </data structures: booleans>` as a key in a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

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

  the terminal updates to show an :doc:`AssertionError`
* I then update the values to make the tests pass

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

* So far from the tests I see that I can use `booleans <https://docs.python.org/3/library/stdtypes.html#boolean-type-bool>`_, `floats <https://docs.python.org/3/library/functions.html?highlight=float#float>`_, `integers <https://docs.python.org/3/library/functions.html?highlight=int#int>`_ and `strings <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ as keys in a dictionary

How to create a dictionary with tuples as keys
----------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test to ``TestDictionaries``

.. code-block:: python

  def test_creating_dictionaries_with_tuples_as_keys(self):
      self.assertEqual(
        {(1, 2): "value"},
        {(1, 2): "key"}
    )

the terminal outputs an :doc:`AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I update the values to make the test pass

.. code-block:: python

  self.assertEqual(
      {(1, 2): "value"},
      {(1, 2): "value"}
  )

and update my knowledge of creating dictionaries to say I can use `tuples <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_, `booleans <https://docs.python.org/3/library/stdtypes.html#boolean-type-bool>`_, `floats <https://docs.python.org/3/library/functions.html?highlight=float#float>`_, `integers <https://docs.python.org/3/library/functions.html?highlight=int#int>`_, and `strings <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_ as keys in a dictionary

Can I create a Dictionary with lists as keys?
----------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test to ``TestDictionaries`` using a list as a key

.. code-block:: python

  def test_creating_dictionaries_with_lists_as_keys(self):
      {[1, 2]: "BOOM"}

the terminal shows a :doc:`TypeError` because only `hashable <https://docs.python.org/3/glossary.html#term-hashable>`_ types can be used as dictionary keys and :doc:`lists` are not `hashable <https://docs.python.org/3/glossary.html#term-hashable>`_

.. code-block::

   E       TypeError: unhashable type: 'list'

I also update the list of exceptions encountered to include :doc:`TypeError`

.. code-block:: python

   # Exceptions Encountered
   # ModuleNotFoundError
   # AttributeError
   # TypeError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

From :doc:`/exception handling` I can use ``self.assertRaises`` to confirm that an error is raised by some code without having it crash the tests. I will use it here to confirm that when I try to create a dictionary with a ``list`` as the key, python raises a :doc:`TypeError`

.. code-block:: python

    def test_creating_dictionaries_with_lists_as_keys(self):
        with self.assertRaises(TypeError):
            {[1, 2]: "BOOM"}


Can I create a Dictionary with sets as keys?
---------------------------------------------

What if I try a similar test using a set as a key

RED: make it fail
^^^^^^^^^^^^^^^^^

.. code-block:: python

    def test_creating_dictionaries_with_sets_as_keys(self):
        {{1, 2}: "BOOM"}

the terminal responds with a :doc:`TypeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

which I handle using ``self.assertRaises``

.. code-block:: python

    def test_creating_dictionaries_with_sets_as_keys(self):
        with self.assertRaises(TypeError):
            {{1, 2}: "BOOM"}

I am green again

Can I create a Dictionary with dictionaries as keys?
-----------------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a new test

.. code-block:: python

    def test_creating_dictionaries_with_dictionaries_as_keys(self):
        a_dictionary = {"key": "value"}
        {a_dictionary: "BOOM"}

and the terminal outputs a :doc:`TypeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I add a handler to confirm the findings

.. code-block:: python

       def test_creating_dictionaries_with_dictionaries_as_keys(self):
           a_dictionary = {"key": "value"}
           with self.assertRaises(TypeError):
               {a_dictionary: "BOOM"}

all tests pass and I know that I can create dictionaries with the following :doc:`/data structures` as keys

* `strings <https://docs.python.org/3/library/string.html?highlight=string#module-string>`_
* `booleans <https://docs.python.org/3/library/stdtypes.html#boolean-type-bool>`_
* `integers <https://docs.python.org/3/library/functions.html?highlight=int#int>`_
* `floats <https://docs.python.org/3/library/functions.html?highlight=float#float>`_
* `tuples <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_

----

How to access dictionary values
------------------------

The tests cover how to create `dictionaries  <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_, and what I can use as ``keys``. This part covers how to access the values of a dictionary

RED: make it fail
^^^^^^^^^^^^^^^^^

I am going to add a test to ``TestDictionaries`` in ``test_dictionaries.py`` for this

.. code-block:: python

    def test_accessing_dictionary_values(self):
        a_dictionary = {"key": "value"}
        self.assertEqual(a_dictionary["key"], "bob")

the terminal displays a failing test with an :doc:`AssertionError` because ``bob`` is not equal to ``value``

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I update the expected value to make the tests pass

.. code-block:: python

    def test_accessing_dictionary_values(self):
        a_dictionary = {"key": "value"}
        self.assertEqual(a_dictionary["key"], "value")

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* I can also display the values of a dictionary as a list without the keys

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

  the terminal outputs an :doc:`AssertionError`
* I update the values to make the test pass

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
            ['value1', 'value2', 'value3', 'valueN']
        )

* I can also display the keys of a dictionary as a list

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

  the terminal updates to show an :doc:`AssertionError`
* I update the test to make it pass

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
            ['key1', 'key2', 'key3', 'keyN']
        )

How to get a value when the key does not exist
-----------------------------------------------

Sometimes I can try to access values in a dictionary with a key that does not exist in the dictionary or misspell a key that does exist

RED: make it fail
^^^^^^^^^^^^^^^^^

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

the terminal updates to show a `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=keyerror#KeyError>`_. A `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ is raised when a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ is called with a ``key`` that does not exist.

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I add `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # ModuleNotFoundError
    # AttributeError
    # TypeError
    # KeyError

* then add an exception handler to acknowledge the error is raised

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

* the terminal shows a `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ for the next line where I misspelled the key and I add it to the exception handler to make it pass as well

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

What if I want to call a dictionary and not have python raise an error when it does not find the key? I could use the `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ :doc:`method <functions>`


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

  as expected the terminal updates to show a `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ because the ``non_existent_key`` does not exist in ``a_dictionary``
* I update the test using the `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ :doc:`method <functions>`

  .. code-block:: python

    def test_how_to_get_a_value_when_a_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary.get('non_existent_key'))

  the terminal updates to show a passing test. This means that when I use the `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ :doc:`method <functions>` and the ``key`` does not exist, I get :doc:`None </data structures: None>` as the ``return`` value.
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
* The `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ :doc:`method <functions>` takes in 2 inputs

  - the ``key``
  - the ``default value`` it should return if the ``key`` does not exist

* I can also use the `get <https://docs.python.org/3/library/stdtypes.html#dict.get>`_ :doc:`method <functions>` with an existing key

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

  the terminal updates to show an `Assertion Error <./AssertionError.rst>`_ because ``value1`` is not equal to :doc:`None </data structures: None>`
* I update the test to make it pass

How to view the attributes and methods of a dictionary
------------------------------------------------------

:doc:`classes` covers how to view the ``attributes`` and ``methods`` of an object. Let us look at the attributes and :doc:`methods <functions>` of  `dictionaries  <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ to help understand them better

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

the terminal updates to show an :doc:`AssertionError`

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
            'update',
            'values'
        ]
    )

the tests pass

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

I see some of the :doc:`methods <functions>` I have covered so far and others I did not. I  could write tests on the others to discover what they do and/or `read more about dictionaries <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_.

If you want more practice you could list out what has been covered so far, and write tests for the others and fill in details as you learn them


* clear
* copy
* fromkeys
* get - gets the ``value`` for a ``key`` and returns a default value or :doc:`None </data structures: None>` if the key does not exist
* items
* keys - returns the list of ``keys`` in a dictionary
* `pop <https://docs.python.org/3/library/stdtypes.html#dict.pop>`_
* popitem
* `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_
* `update <https://docs.python.org/3/library/stdtypes.html#dict.update>`_
* values - returns the list of ``values`` in a dictionary

How to set a default value for a given key
------------------------------------------

Let us say I want to take a look at the `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_ method for instance

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test

.. code-block:: python

  def test_set_default_for_a_given_key(self):
      a_dictionary = {'bippity': 'boppity'}
      a_dictionary['another_key']

the terminal shows a `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I add a ``self.assertRaises`` to confirm that the `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ gets raised, allowing the test to pass

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
        self.assertEqual(a_dictionary, {'bippity': 'boppity'})

  the terminal updates to show that ``a_dictionary`` has changed, by giving us an :doc:`AssertionError`. It has a new key which was not there before

* I update the test to make it pass

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

  when I first try to access the value for ``another_key`` in ``a_dictionary``, I get a `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ because the key does not exist in the dictionary. After using `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_ and passing in ``another_key`` as the key, it gets added to the dictionary so I will not get an error when I try accessing it again

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

* I will now add a test for setting the default value to something other than :doc:`None </data structures: None>`

  .. code-block:: python

    a_dictionary.setdefault('a_new_key', 'a_default_value')
    self.assertEqual(
        a_dictionary,
        {
            'bippity': 'boppity',
            'another_key': None
        }

    )

  the terminal updates to show an :doc:`AssertionError` since ``a_dictionary`` now has a new ``key`` and ``value``
* I update the test to make it pass

  .. code-block:: python

    self.assertEqual(
        a_dictionary,
        {
            'bippity': 'boppity',
            'another_key': None,
            'a_new_key': 'a_default_value',
        }
    )

  all tests pass, and I update the list of :doc:`methods <functions>` with what I now know about `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_

How to update a dictionary with another dictionary
--------------------------------------------------

What if I have a dictionary and want to add the ``keys`` and ``values`` of one dictionary to another?

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
          {"basic": "toothpaste", "whitening": "peroxide"}
      )

the terminal displays an :doc:`AssertionError` because the values of ``a_dictionary`` were updated when I called the `update <https://docs.python.org/3/library/stdtypes.html#dict.update>`_ :doc:`method <functions>` on it

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I update the values to make it pass


How to remove an item from a dictionary
---------------------------------------

I can remove an item from a dictionary with the `pop <https://docs.python.org/3/library/stdtypes.html#dict.pop>`_ method. It deletes the ``key`` and ``value`` from the dictionary and returns the ``value``

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

the terminal updates to show an :doc:`AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I update the test with the right value to make it pass

---

WOW! You made it this far as I went through dictionaries. You now know
* How to create a dictionary
* What objects can be used as dictionary keys
* What objects cannot be used as dictionary keys
* How to view dictionary keys
* How to view dictionary values
* How to view the attributes and methods of a dictionary
* How to set a default value for a key
* How to update a dictionary with another dictionary
* How to remove an item from a dictionary