.. include:: ../links.rst

#################################################################################
dictionaries
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

A `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ also known as a Mapping contains key-value pairs, the values can be any any Python :ref:`object<classes>` but not the keys.

I think this is the most important data structure to know as it can hold all the other data structures and in your programming journey you will come across JSON_ which you can read and write as `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ in Python

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal to run :ref:`makePythonTdd.sh` with ``dictionaries`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh dictionaries

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 dictionaries

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_dictionaries.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_dictionaries.py:7`` to open it in the editor
* then change ``True`` to ``False`` to make the test pass

----

*********************************************************************************
test_make_a_dictionary_w_dict_constructor
*********************************************************************************

red: make it fail
#################################################################################

I change ``test_failure``

.. code-block:: python

  class TestDictionaries(unittest.TestCase):

      def test_make_a_dictionary_w_dict_constructor(self):
          self.assertEqual(dict(key='value'), None)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {'key': 'value'} != None

green: make it pass
#################################################################################

I copy the value from the terminal and paste it to replace :ref:`None`

.. code-block:: python

  self.assertEqual(dict(key='value'), {'key': 'value'})

the test passes

*********************************************************************************
test_make_a_dictionary_w_curly_braces
*********************************************************************************

I can make a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with the `dict <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ constructor_ and the passing test shows I can make one with ``{}``.

red: make it fail
#################################################################################

I add a test

.. code-block:: python

    def test_make_a_dictionary_w_dict_constructor(self):
        ...

    def test_make_a_dictionary_w_curly_braces(self):
        self.assertEqual({'key': 'value'}, dict(key='key'))

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {'key': 'value'} != {'key': 'key'}

green: make it pass
#################################################################################

I make the values match

.. code-block:: python

  self.assertEqual({'key': 'value'}, dict(key='value'))

the test passes

----

*********************************************************************************
test_make_a_dictionary_w_numbers_as_keys
*********************************************************************************

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_make_a_dictionary_w_numbers_as_keys(self):
      self.assertEqual({0: 'boom'}, {'zero': 'boom'})

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {0: 'boom'} != {'zero': 'boom'}

green: make it pass
#################################################################################

I change the key in the exception

.. code-block:: python

  def test_make_a_dictionary_w_numbers_as_keys(self):
      self.assertEqual({0: 'boom'}, {0: 'boom'})


the test passes. I can use integers_ keys in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

refactor: make it better
#################################################################################

I add an assertion for floats_

.. code-block:: python

  self.assertEqual({0: 'boom'}, {0: 'boom'})
  self.assertEqual({0.1: 'bap'}, {'0.1': 'bap'})

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {0.1: 'bap'} != {'0.1': 'bap'}

I make the keys match

.. code-block:: python

  self.assertEqual({0.1: 'bap'}, {0.1: 'bap'})

the test passes. I can use integers_ and floats_ as keys in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

----

*********************************************************************************
test_make_a_dictionary_w_booleans_as_keys
*********************************************************************************

I wonder if it is possible to use :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>` as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys

red: make it fail
#################################################################################

I add a test

.. code-block:: python

    def test_make_a_dictionary_w_numbers_as_keys(self):
        ...

    def test_make_a_dictionary_w_booleans_as_keys(self):
        self.assertEqual({False: 'boom'}, {'False': 'boom'})

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {False: 'boom'} != {'False': 'boom'}

green: make it pass
#################################################################################

I match the keys

.. code-block:: python

  self.assertEqual({False: 'boom'}, {False: 'boom'})

I can use :ref:`False<test_what_is_false>` as a key in a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

refactor: make it better
#################################################################################

I add another assertion

.. code-block:: python

  self.assertEqual({False: 'boom'}, {False: 'boom'})
  self.assertEqual({True: 'bap'}, {'True': 'bap'})

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {True: 'bap'} != {'True': 'bap'}

I change the expectation

.. code-block:: python

  self.assertEqual({True: 'bap'}, {True: 'bap'})

the test passes. I can use a boolean_ as a key in a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

----

*********************************************************************************
test_make_a_dictionary_w_tuples_as_keys
*********************************************************************************

red: make it fail
#################################################################################

I add a test for tuples_

.. code-block:: python

  def test_make_a_dictionary_w_booleans_as_keys(self):
      ...

  def test_make_a_dictionary_w_tuples_as_keys(self):
      self.assertEqual(
          {(0, 1): 'value'},
          {(0, 1): 'key'}
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {(0, 1): 'value'} != {(0, 1): 'key'}

green: make it pass
#################################################################################

I make the values match

.. code-block:: python

  self.assertEqual(
      {(0, 1): 'value'},
      {(0, 1): 'value'}
  )

the test passes

----

*********************************************************************************
test_make_a_dictionary_w_lists_as_keys
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

  def test_make_a_dictionary_w_tuples_as_keys(self):
      ...

  def test_make_a_dictionary_w_lists_as_keys(self):
      self.assertEqual(
          {[3, 2, 1]: 'BOOM!'},
          {[3, 2, 1]: 'bap'}
      )

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: unhashable type: 'list'

only hashable_ objects_ can be used as `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ keys and :ref:`lists` are not hashable_

I add :ref:`TypeError` to the list of Exceptions_ encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # TypeError

green: make it pass
#################################################################################

I change the assertEqual_ to assertRaises_

.. code-block:: python

  def test_make_a_dictionary_w_lists_as_keys(self):
      with self.assertRaises(TypeError):
          {[3, 2, 1]: 'BOOM!'}

see :doc:`/how_to/exception_handling_tests` for more details on why that worked. I cannot make a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with a :ref:`list <lists>` as a key

----

*********************************************************************************
test_make_a_dictionary_w_sets_as_keys
*********************************************************************************

red: make it fail
#################################################################################

I try the same thing with a set_ as a key

.. code-block:: python

  def test_make_a_dictionary_w_sets_as_keys(self):
      {{3, 2, 1}: 'BOOM!'}

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: unhashable type: 'set'

green: make it pass
#################################################################################

I add assertRaises_

.. code-block:: python

  def test_make_a_dictionary_w_sets_as_keys(self):
      with self.assertRaises(TypeError):
          {{3, 2, 1}: 'BOOM!'}

the test is green again. I cannot use a set_ as a key in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

----

*********************************************************************************
test_make_a_dictionary_w_dictionaries_as_keys
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_make_a_dictionary_w_sets_as_keys(self):
      ...

  def test_make_a_dictionary_w_dictionaries_as_keys(self):
      a_dictionary = {'key': 'value'}
      {a_dictionary: 'BOOM!'}

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: unhashable type: 'dict'

green: make it pass
#################################################################################

I add assertRaises

.. code-block:: python

    def test_make_a_dictionary_w_dictionaries_as_keys(self):
        a_dictionary = {'key': 'value'}
        with self.assertRaises(TypeError):
            {a_dictionary: 'BOOM!'}

the test passes. I cannot use a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_, set_ or :ref:`list <lists>` as a key in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ they are not hashable_

----

*********************************************************************************
test_attributes_and_methods_of_dictionaries
*********************************************************************************

I can use the the dir_ :ref:`function<functions>` to look at the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of `dictionaries <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_attributes_and_methods_of_dictionaries(self):
      self.assertEqual(
          dir(dict),
          []
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: ['__class__', '__class_getitem__', '__cont[530 chars]ues'] != []

It also gives me a message to view the entire difference between the two :ref:`lists`

.. code-block:: python

  Diff is 720 characters long. Set self.maxDiff to None to see it.

green: make it pass
#################################################################################

I add `unittest.TestCase.maxDiff`_

.. code-block:: python

  def test_attributes_and_methods_of_dictionaries(self):
      self.maxDiff = None
      self.assertEqual(
          dir(dict),
          []
      )

the terminal shows the entire difference between the two :ref:`lists`. I copy and paste the expected values from the terminal

.. note::

  Your results can be different because of your version of Python

.. code-block:: python

  def test_attributes_and_methods_of_dictionaries(self):
      self.maxDiff = None
      self.assertEqual(
          dir(src.dictionaries.a_dict()),
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

the test passes. I make a TODO list with the names that do not have double underscores (__)

.. code-block:: python

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

  # Exceptions Encountered
  # AssertionError
  # TypeError

----

*********************************************************************************
test_clear_empties_a_dictionary
*********************************************************************************

I add a test for the :ref:`method<functions>`

.. code-block:: python

    def test_attributes_and_methods_of_dictionaries(self):
        ...

    def test_clear(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(a_dictionary.clear())

the terminal shows green. The `clear <https://docs.python.org/3/library/stdtypes.html#dict.clear>`_ :ref:`method<functions>` returns :ref:`None`

red: make it fail
#################################################################################

I add an assertion to see what changed in the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

.. code-block:: python

  self.assertIsNone(a_dictionary.clear())
  self.assertEqual(a_dictionary, {'key': 'value'})

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {} != {'key': 'value'}

the `clear <https://docs.python.org/3/library/stdtypes.html#dict.clear>`_ :ref:`method<functions>` empties the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

green: make it pass
#################################################################################

I change the values to match

.. code-block:: python

  self.assertEqual(a_dictionary, {})

the test passes. ``{}`` is how Python represents an empty `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

refactor: make it better
#################################################################################

* I rename the test

  .. code-block:: python

    def test_clear_empties_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(a_dictionary.clear())
        self.assertEqual(a_dictionary, {})

  the test is still passing

* I remove `clear <https://docs.python.org/3/library/stdtypes.html#dict.clear>`_ from the TODO list

  .. code-block:: python

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

----

*********************************************************************************
test_copy_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add a test for the next :ref:`method<functions>`

.. code-block:: python

  def test_clear_empties_a_dictionary(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.clear())
      self.assertEqual(a_dictionary, {})

  def test_copy(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.copy())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {'key': 'value'} is not None

the `copy <https://docs.python.org/3/library/stdtypes.html#dict.copy>`_ :ref:`method<functions>` returns a copy of the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_


green: make it pass
#################################################################################

I change the assert_ :ref:`method<functions>` then add the expected value

.. code-block:: python

  def test_copy(self):
      a_dictionary = {'key': 'value'}
      self.assertEqual(a_dictionary.copy(), {'key': 'value'})

the test passes

refactor: make it better
#################################################################################

* I add another assertion to see what happens to the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ after the call

  .. code-block:: python

    self.assertEqual(a_dictionary.copy(), {'key': 'value'})
    self.assertEqual(a_dictionary, {})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} != {}

  it stays the same. I change the values to match

  .. code-block:: python

    self.assertEqual(a_dictionary, {'key': 'value'})

  the test is green again

* I rename the test

  .. code-block:: python

    def test_copy_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary.copy(), {'key': 'value'})
        self.assertEqual(a_dictionary, {'key': 'value'})

  the test is still green

* I remove `copy <https://docs.python.org/3/library/stdtypes.html#dict.copy>`_ from the TODO list

  .. code-block:: python

    'fromkeys',
    'get',
    'items',
    'keys',
    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

----

*********************************************************************************
test_fromkeys_makes_a_dictionary_from_an_iterable
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

  def test_copy_a_dictionary(self):
      ...

  def test_fromkeys(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.fromkeys())

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: fromkeys expected at least 1 argument, got 0

green: make it pass
#################################################################################

I pass a value to the call

.. code-block:: python

  self.assertIsNone(a_dictionary.fromkeys(0))

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: 'int' object is not iterable

I change the value passed in to a tuple_

.. code-block:: python

  self.assertIsNone(a_dictionary.fromkeys((0, 1, 2, 3)))

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {0: None, 1: None, 2: None, 3: None} is not None

the `fromkeys <https://docs.python.org/3/library/stdtypes.html#dict.fromkeys>` :ref:`method<functions>` returns a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ that uses the iterable_ given as keys with default values of :ref:`None`. I change the assertion then add the expected values

.. code-block:: python

  def test_fromkeys(self):
      a_dictionary = {'key': 'value'}
      self.assertEqual(
          a_dictionary.fromkeys((0, 1, 2, 3)),
          {0: None, 1: None, 2: None, 3: None}
      )

the test passes

refactor: make it better
#################################################################################

* I add an assert_ statement to see what happens to the first `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ in the test

  .. code-block:: python

    self.assertEqual(
        a_dictionary.fromkeys((0, 1, 2, 3)),
        {0: None, 1: None, 2: None, 3: None}
    )
    self.assertEqual(a_dictionary, {})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} != {}

  the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ did not change

* I remove it and the assertion

  .. code-block:: python

    def test_fromkeys(self):
        self.assertEqual(
            a_dictionary.fromkeys((0, 1, 2, 3)),
            {0: None, 1: None, 2: None, 3: None}
        )

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'a_dictionary' is not defined

  I change the call to use the `dict <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ constructor_

  .. code-block:: python

    def test_fromkeys(self):
        self.assertEqual(
            dict.fromkeys((0, 1, 2, 3)),
            {0: None, 1: None, 2: None, 3: None}
        )

  the test passes

* I rename the test

  .. code-block:: python

    def test_fromkeys_makes_a_dictionary_from_an_iterable(self):
        self.assertEqual(
            dict.fromkeys((0, 1, 2, 3)),
            {0: None, 1: None, 2: None, 3: None}
        )

  still green

* I remove fromkeys_ from the TODO list

  .. code-block:: python

    'get',
    'items',
    'keys',
    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

----

*********************************************************************************
test_get_value_of_key_from_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

  def test_fromkeys_makes_a_dictionary_from_an_iterable(self):
      ...

  def test_get(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.get())

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: get expected at least 1 argument, got 0

green: make it pass
#################################################################################

* I add a value to the call

  .. code-block:: python

    self.assertIsNone(a_dictionary.get('key'))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'value' is not None

  the get_ :ref:`method<functions>` returns the value for the key it is given from the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

* I change the assertion then add the expected value

  .. code-block:: python

    def test_get(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary.get('key'), 'value')

  the test passes

refactor: make it better
#################################################################################

* I add an assertion to see if the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ changed

  .. code-block:: python

    self.assertEqual(a_dictionary.get('key'), 'value')
    self.assertEqual(a_dictionary, {})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} != {}

  it stayed the same

* I remove the new statement, I want to see what happens when I give the get_ :ref:`method<functions>` a key that is not in the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

  .. code-block:: python

    self.assertEqual(a_dictionary.get('key'), 'value')
    self.assertEqual(a_dictionary.get(0), {})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != {}

  the get_ :ref:`method<functions>` returns :ref:`None` when the given key is not in the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_. I remove the expectation and change the assertion

  .. code-block:: python

    self.assertIsNone(a_dictionary.get(0))

  the test passes

* I change the name of the test

  .. code-block:: python

    def test_get_value_of_key_from_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary.get('key'), 'value')
        self.assertIsNone(a_dictionary.get(0))

  the test is still green

* I remove get_ from the TODO list

  .. code-block:: python

    'items',
    'keys',
    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

----

*********************************************************************************
test_items_returns_keys_and_values_of_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add a test for the next :ref:`method<functions>`

.. code-block:: python

  def test_get_value_of_key_from_dictionary(self):
      ...

  def test_items(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.items())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: dict_items([('key', 'value')]) is not None

the items_ :ref:`methods<functions>` returns a ``dict_items`` object_ that contains the keys and values of the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

green: make it pass
#################################################################################

I copy and paste the value from the terminal

.. code-block:: python

  self.assertIsNone(a_dictionary.items(), dict_items([('key', 'value')]))

the terminal shows :ref:`AssertionError`

.. code-block:: python

  NameError: name 'dict_items' is not defined

the ``dict_items`` object has a :ref:`list<lists>` that contains a tuple_, I use that

.. code-block:: python

  self.assertIsNone(a_dictionary.items(), [('key', 'value')])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: dict_items([('key', 'value')]) is not None : [('key', 'value')]

I change the assertion and wrap the call in the :ref:`list<lists>` constructor

.. code-block:: python

  self.assertEqual(list(a_dictionary.items()), [('key', 'value')])

the test passes

refactor: make it better
#################################################################################

* I rename the test

  .. code-block:: python

    def test_items_returns_keys_and_values_of_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(list(a_dictionary.items()), [('key', 'value')])

  the test is still green

* I remove items_ from the TODO list

  .. code-block:: python

    'keys',
    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

----

*********************************************************************************
test_keys_returns_keys_of_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add the next test

.. code-block:: python

  def test_items_returns_keys_and_values_of_dictionary(self):
      ...

  def test_keys(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.keys())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: dict_keys(['key']) is not None

this is like :ref:`test_items_returns_keys_and_values_of_dictionary`

green: make it pass
#################################################################################

I copy and paste the values from the terminal then change the assertion

.. code-block:: python

  def test_keys(self):
      a_dictionary = {'key': 'value'}
      self.assertEqual(a_dictionary.keys(), dict_keys(['key']))

the terminal shows NameError_

.. code-block:: python

  NameError: name 'dict_keys' is not defined

the keys_ :ref:`method<functions>` returns ``dict_keys`` object_ that has the keys of the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_. I change the expectation to a :ref:`list<lists>` and use the :ref:`list<lists>` constructor_ to wrap the call

.. code-block:: python

  self.assertEqual(list(a_dictionary.keys()), ['key'])

the test passes

refactor: make it better
#################################################################################

* I rename the test

  .. code-block:: python

    def test_keys_returns_keys_of_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(list(a_dictionary.keys()), ['key'])

  the test is still green

* I remove keys_ from the TODO list

  .. code-block:: python

    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

----

*********************************************************************************
test_pop_removes_and_returns_key_w_value_from_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add a test for the next :ref:`method<functions>`

.. code-block:: python

  def test_keys_returns_keys_of_dictionary(self):
      ...

  def test_pop(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.pop())

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: pop expected at least 1 argument, got 0

green: make it pass
#################################################################################

I pass a value to the call

.. code-block:: python

  def test_pop(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.pop(0))

the terminal shows KeyError_

.. code-block:: python

  KeyError: 0

I change the assertion to assertRaises_

.. code-block:: python

  def test_pop(self):
      a_dictionary = {'key': 'value'}

      with self.assertRaises(KeyError):
          a_dictionary.pop(0)

calling the `pop <https://docs.python.org/3/library/stdtypes.html#dict.pop>`_ :ref:`method<functions>` with a key that is not in the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ raises a KeyError_

refactor: make it better
#################################################################################

* I add another assertion

  .. code-block:: python

    def test_pop(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(a_dictionary.pop('key'))

        with self.assertRaises(KeyError):
            a_dictionary.pop(0)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'value' is not None

  the `pop <https://docs.python.org/3/library/stdtypes.html#dict.pop>`_ :ref:`method<functions>` returns the value from the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ for the key it is given

* I change the assertion to assertEqual_ and paste the value from the terminal

  .. code-block:: python

    a_dictionary = {'key': 'value'}
    self.assertEqual(a_dictionary.pop('key'), 'value')

  the test passes

* I add another assertion to see what happens to the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

  .. code-block:: python

    self.assertEqual(a_dictionary.pop('key'), 'value')
    self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {} != {'key': 'value'}

  `pop <https://docs.python.org/3/library/stdtypes.html#dict.pop>`_ :ref:`method<functions>` removes the key-value pair and returns the value from the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ for the key it is given

* I change the value expectation to match

  .. code-block:: python

    self.assertEqual(a_dictionary, {})

  the test passes

* I rename the test

  .. code-block:: python

    def test_pop_removes_and_returns_key_w_value_from_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary.pop('key'), 'value')
        self.assertEqual(a_dictionary, {})

        with self.assertRaises(KeyError):
            a_dictionary.pop(0)

  the test is still passings

* I remove `pop <https://docs.python.org/3/library/stdtypes.html#dict.pop>`_ from the TODO list

  .. code-block:: python

    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

----

*********************************************************************************
test_popitem
*********************************************************************************

red: make it fail
#################################################################################

green: make it pass
#################################################################################

refactor: make it better
#################################################################################

----

*********************************************************************************
test_setdefault
*********************************************************************************

red: make it fail
#################################################################################

green: make it pass
#################################################################################

refactor: make it better
#################################################################################

----

*********************************************************************************
test_update
*********************************************************************************

red: make it fail
#################################################################################

green: make it pass
#################################################################################

refactor: make it better
#################################################################################

----

*********************************************************************************
test_values
*********************************************************************************

red: make it fail
#################################################################################

green: make it pass
#################################################################################

refactor: make it better
#################################################################################

----

*********************************************************************************
how to access dictionary values
*********************************************************************************

The tests so far show how to make `dictionaries <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ and what objects can be used as ``keys``. The following tests show how to access the values of a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

red: make it fail
#################################################################################

I add a test to ``TestDictionaries`` in ``test_dictionaries.py``

.. code-block:: python

  def test_get_a_value_from_a_dictionary(self):
      a_dictionary = {"key": "value"}
      self.assertEqual(a_dictionary["key"], "bob")

the terminal shows :ref:`AssertionError` because ``bob`` is not equal to ``value``. I can get a value for a key by providing the key in square brackets to the dictionary

.. code-block:: python

  AssertionError: 'value' != 'bob'

green: make it pass
#################################################################################

I make the expected value to make the tests pass

.. code-block:: python

  def test_get_a_value_from_a_dictionary(self):
      a_dictionary = {"key": "value"}
      self.assertEqual(a_dictionary["key"], "value")

refactor: make it better
#################################################################################

* I can also show all the values of a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ as a :ref:`list <lists>` without the keys

  .. code-block:: python

    def test_list_dictionary_values(self):
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

    def test_list_dictionary_values(self):
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

    def test_list_dictionary_keys(self):
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

    def test_list_dictionary_keys(self):
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

*********************************************************************************
how to get a value when the key does not exist
*********************************************************************************

Sometimes when I try to access values in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_, I use a key that does not exist or misspell a key that does exist

red: make it fail
#################################################################################

I add a test for both cases

.. code-block:: python

  def test_key_error(self):
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

    def test_key_error(self):
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

    def test_key_error(self):
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


* I add a test called ``test_get_value_when_key_does_not_exist`` to ``TestDictionaries``

  .. code-block:: python

    def test_get_value_when_key_does_not_exist(self):
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

* I can use the get_ :ref:`method<functions>` when I do not wantPython to raise KeyError_ for a key that does not exist

  .. code-block:: python

    def test_get_value_when_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary.get('non_existent_key'))

  the terminal shows a passing test. This means that when I use the get_ :ref:`method<functions>` and the ``key`` does not exist, I get :ref:`None` as the result.
* I can state the above explicitly, from the `Zen of Python`_: ``Explicit is better than implicit``

  .. code-block:: python

    def test_get_value_when_key_does_not_exist(self):
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
* The get_ :ref:`method<functions>` takes in 2 inputs

  - the ``key``
  - the ``default value`` wanted when the ``key`` does not exist

* I can also use the get_ :ref:`method<functions>` to get the value for an existing key

  .. code-block:: python

    def test_get_value_when_key_does_not_exist(self):
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

    def test_get_value_when_key_does_not_exist(self):
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

----

*********************************************************************************
how to set a default value for a given key
*********************************************************************************

Let us say I want to find out more about the `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_ method

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_set_default_for_key(self):
      a_dictionary = {'bippity': 'boppity'}
      a_dictionary['another_key']

and the terminal shows KeyError_

green: make it pass
#################################################################################

I add ``self.assertRaises`` to make sure that KeyError_ gets raised for the test to pass

.. code-block:: python

  def test_set_default_for_key(self):
      a_dictionary = {'bippity': 'boppity'}

      with self.assertRaises(KeyError):
          a_dictionary['another_key']

refactor: make it better
#################################################################################

* Then I add a test for `setdefault <https://docs.python.org/3/library/stdtypes.html#dict.setdefault>`_

  .. code-block:: python

    def test_set_default_for_key(self):
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

    def test_set_default_for_key(self):
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

    def test_set_default_for_key(self):
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

----

*********************************************************************************
test_adding_2_dictionaries
*********************************************************************************

What if I want to add the ``keys`` and ``values`` of one `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ to another?

red: make it fail
#################################################################################

I add another test to ``TestDictionaries``

.. code-block:: python

  def test_add_two_dictionaries(self):
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

  def test_add_two_dictionaries(self):
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

----

*********************************************************************************
how to remove an item from a dictionary
*********************************************************************************

I can remove an item from a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with the `pop <https://docs.python.org/3/library/stdtypes.html#dict.pop>`_ method. It deletes the ``key`` and ``value`` from the `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ and returns the ``value``

red: make it fail
#################################################################################

I add a failing test to ``TestDictionaries``

.. code-block:: python

  def test_pop_item_from_dictionary(self):
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

    def test_pop_item_from_dictionary(self):
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

    def test_pop_item_from_dictionary(self):
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

    def test_pop_item_from_dictionary(self):
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