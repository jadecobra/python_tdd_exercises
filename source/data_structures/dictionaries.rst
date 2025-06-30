.. include:: ../links.rst

#################################################################################
dictionaries
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

A `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ also known as a Mapping contains key-value pairs, the values can be any Python :ref:`object<classes>` but not the keys. I think this is the most important data structure to know as it can hold all the other data structures. In your programming journey you will come across JSON_ which you can read and write as `dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ in Python

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
test_make_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I change ``test_failure``

.. code-block:: python

  class TestDictionaries(unittest.TestCase):

      def test_make_a_dictionary(self):
          self.assertEqual(dict(), None)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {} != None

green: make it pass
#################################################################################

I copy the value from the terminal and paste it to replace :ref:`None`

.. code-block:: python

  self.assertEqual(dict(), {})

this is how to make an empty dictionary. I can make a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ with the dict_ constructor_ or curly braces(``{}``)

refactor: make it better
#################################################################################

* I add another assertion, this time with input

  .. code-block:: python

    self.assertEqual(dict(), {})
    self.assertEqual(dict(0), {})

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'int' object is not iterable

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError

* I change the value to an iterable_

  .. code-block:: python

    self.assertEqual(dict(), {})
    self.assertEqual(dict((0, 1)), {})

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: cannot convert dictionary update sequence element #0 to a sequence

* I try a keyword argument instead

  .. code-block:: python

    self.assertEqual(dict(), {})
    self.assertEqual(dict(key='value'), {})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} != {}

  I change the expectation to match the values in the terminal

  .. code-block:: python

    self.assertEqual(dict(key='value'), {'key': 'value'})

  the terminal shows green again. This test uses strings_ as keys

----

*********************************************************************************
test_make_a_dictionary_w_none_as_a_key
*********************************************************************************

red: make it fail
#################################################################################

I add a test where I use :ref:`None` as a key in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

.. code-block:: python

  def test_make_a_dictionary_w_none_as_a_key(self):
      self.assertEqual({None: 'boom'}, {None: 'bap'})

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {None: 'boom'} != {None: 'bap'}

green: make it pass
#################################################################################

I change ``'bap'`` to ``'boom'``

.. code-block:: python

  self.assertEqual({None: 'boom'}, {None: 'boom'})

the test passes. I can use :ref:`None` as a key in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

----

*********************************************************************************
test_make_a_dictionary_w_a_boolean_as_a_key
*********************************************************************************

red: make it fail
#################################################################################

I add a test where I use a boolean_ as a key in a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_

.. code-block:: python

    def test_make_a_dictionary_w_none_as_a_key(self):
        ...

    def test_make_a_dictionary_w_a_boolean_as_a_key(self):
        self.assertEqual({False: 'boom'}, {False: 'bap'})

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {False: 'boom'} != {False: 'bap'}

green: make it pass
#################################################################################

I change ``'bap'`` to ``'boom'``

.. code-block:: python

  self.assertEqual({False: 'boom'}, {False: 'boom'})

the tests passes. I can use :ref:`False<test_what_is_false>` as a key in a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

refactor: make it better
#################################################################################

I add :ref:`True<test_what_is_true>` as a key

.. code-block:: python

  def test_make_a_dictionary_w_a_boolean_as_a_key(self):
      self.assertEqual(
          {False: 'boom', True: 'bap'},
          {False: 'boom'}
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {False: 'boom', True: 'bap'} != {False: 'boom'}

I add the new key-value pair to the expectation

.. code-block:: python

  self.assertEqual(
      {False: 'boom', True: 'bap'},
      {False: 'boom', True: 'bap'}
  )

the test passes. I can use a boolean_ as a key in a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

----

*********************************************************************************
test_make_a_dictionary_w_numbers_as_keys
*********************************************************************************

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_make_a_dictionary_w_a_boolean_as_a_key(self):
      ...

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
test_make_a_dictionary_w_tuples_as_keys
*********************************************************************************

red: make it fail
#################################################################################

I add a test for tuples_

.. code-block:: python

  def test_make_a_dictionary_w_a_boolean_as_a_key(self):
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

I can use the dir_ :ref:`function<functions>` to see the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of `dictionaries <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

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

  your results can be different because of your Python version

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
test_get_value_of_key_from_a_dictionary
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

    def test_get_value_of_key_from_a_dictionary(self):
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
test_pop_removes_key_and_returns_its_value_from_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add a test for the next :ref:`method<functions>`

.. code-block:: python

  def test_get_value_of_key_from_a_dictionary(self):
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

    def test_pop_removes_key_and_returns_its_value_from_a_dictionary(self):
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
test_keys_of_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add the next test

.. code-block:: python

  def test_pop_removes_key_and_returns_its_value_from_a_dictionary(self):
      ...

  def test_keys(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.keys())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: dict_keys(['key']) is not None

this is like :ref:`test_pop_removes_key_and_returns_its_value_from_a_dictionary`

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

    def test_keys_of_a_dictionary(self):
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
test_pop_removes_and_returns_key_w_value_from_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add a test for the next :ref:`method<functions>`

.. code-block:: python

  def test_keys_of_a_dictionary(self):
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

the terminal shows :ref:`KeyError <test_key_error>`

.. code-block:: python

  KeyError: 0

I change the assertion to assertRaises_

.. code-block:: python

  def test_pop(self):
      a_dictionary = {'key': 'value'}

      with self.assertRaises(KeyError):
          a_dictionary.pop(0)

calling the `pop <https://docs.python.org/3/library/stdtypes.html#dict.pop>`_ :ref:`method<functions>` with a key that is not in the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ raises a :ref:`KeyError <test_key_error>`

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

    def test_pop_removes_and_returns_key_w_value_from_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary.pop('key'), 'value')
        self.assertEqual(a_dictionary, {})

        with self.assertRaises(KeyError):
            a_dictionary.pop(0)

  the test is still passings

* I remove `pop <https://docs.python.org/3/library/stdtypes.html#dict.pop>`_ from the TODO list

  .. code-block:: python

    'popitem',
    'setdefault',
    'update',
    'values'

----

*********************************************************************************
test_popitem_removes_and_returns_last_key_value_pair_from_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_pop_removes_and_returns_key_w_value_from_a_dictionary(self):
      ...

  def test_pop_item(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.popitem())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: ('key', 'value') is not None

the `popitem <https://docs.python.org/3/library/stdtypes.html#dict.popitem>`_ :ref:`method<functions>` returns the key-value pair as a tuple_

green: make it pass
#################################################################################

I change the assertion and paste the value from the terminal

.. code-block:: python

    a_dictionary = {'key': 'value'}
    self.assertEqual(a_dictionary.popitem(), ('key', 'value'))

the test passes

refactor: make it better
#################################################################################

* I want to know what the `popitem <https://docs.python.org/3/library/stdtypes.html#dict.popitem>`_ :ref:`method<functions>` does to the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

  .. code-block:: python

    self.assertEqual(a_dictionary.popitem(), ('key', 'value'))
    self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {} != {'key': 'value'}

  `popitem <https://docs.python.org/3/library/stdtypes.html#dict.popitem>`_ removes and returns the key-value pair given from the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

* I change the value

  .. code-block:: python

    self.assertEqual(a_dictionary, {})

  the test passes

* I add another assertion

  .. code-block:: python

    self.assertEqual(a_dictionary, {})
    self.assertEqual(a_dictionary.popitem(), None)

  the terminal shows :ref:`KeyError <test_key_error>`

  .. code-block:: python

    KeyError: 'popitem(): dictionary is empty'

  I change the assertion to assertRaises_

  .. code-block:: python

    self.assertEqual(a_dictionary, {})

    with self.assertRaises(KeyError):
        a_dictionary.popitem()

  the test passes

* this operation does not take input, I change the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ to see how it behaves

  .. code-block:: python

    a_dictionary = {
        'key1': 'value1',
        'key2': 'value2'
    }

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ('key2', 'value2') != ('key', 'value')

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        a_dictionary.popitem(),
        ('key2', 'value2')
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key1': 'value1'} != {}

  I change the value to match

  .. code-block:: python

    self.assertEqual(a_dictionary, {'key1': 'value1'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: KeyError not raised

  I change the assertRaises_ to assertEqual_

  .. code-block:: python

    self.assertEqual(
        a_dictionary.popitem(),
        ('key1', 'value1')
    )

  `popitem <https://docs.python.org/3/library/stdtypes.html#dict.popitem>`_ returns the last key-value pair in the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

* I add another call to the :ref:`method<functions>` that should fail

  .. code-block:: python

    self.assertEqual(
        a_dictionary.popitem(),
        ('key1', 'value1')
    )
    a_dictionary.popitem()

  the terminal shows :ref:`KeyError <test_key_error>`

  .. code-block:: python

    KeyError: 'popitem(): dictionary is empty'

  I add assertRaises_

  .. code-block:: python

    self.assertEqual(
        a_dictionary.popitem(),
        ('key1', 'value1')
    )

    with self.assertRaises(KeyError):
        a_dictionary.popitem()

  the test passes

* I change the name of the test

  .. code-block:: python

    def test_popitem_removes_and_returns_last_key_value_pair_from_a_dictionary(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2'
        }
        self.assertEqual(
            a_dictionary.popitem(),
            ('key2', 'value2')
        )
        self.assertEqual(a_dictionary, {'key1': 'value1'})
        self.assertEqual(
            a_dictionary.popitem(),
            ('key1', 'value1')
        )

        with self.assertRaises(KeyError):
            a_dictionary.popitem()

* I remove `popitem <https://docs.python.org/3/library/stdtypes.html#dict.popitem>`_ from the TODO list

  .. code-block:: python

    'setdefault',
    'update',
    'values'

----

*********************************************************************************
test_setdefault_adds_key_w_a_default_value_to_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

  def test_setdefault(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.setdefault())

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: setdefault expected at least 1 argument, got 0

green: make it pass
#################################################################################

I pass a value in the call

.. code-block:: python

  self.assertIsNone(a_dictionary.setdefault(0))

the test passes

refactor: make it better
#################################################################################

* I add an assertion to see what changed in the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

  .. code-block:: python

    self.assertIsNone(a_dictionary.setdefault(0))
    self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value', 0: None} != {'key': 'value'}

  setdefault_ adds the given key to the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ with a default value of :ref:`None` and returns the default value

* I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        a_dictionary,
        {
            'key': 'value',
            0: None,
        }
    )

  the test passes

* I add another test to see what happens when the key is already in the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

  .. code-block:: python

    self.assertEqual(
        a_dictionary,
        {
            'key': 'value',
            0: None,
        }
    )
    self.assertIsNone(a_dictionary.setdefault('key'))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'value' is not None

  setdefault_ returns the value for the key in a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ when the key already exists

* I paste the value from the terminal then change the assertion to assertEqual_

  .. code-block:: python

    self.assertEqual(
        a_dictionary.setdefault('key'), 'value'
    )

  the test passes

* I rename the test

  .. code-block:: python

    def test_setdefault_adds_key_w_a_default_value_to_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(a_dictionary.setdefault(0))
        self.assertEqual(
            a_dictionary,
            {
                'key': 'value',
                0: None,
            }
        )
        self.assertEqual(
            a_dictionary.setdefault('key'), 'value'
        )

  the test is still green

* I remove setdefault_ from the TODO list

  .. code-block:: python

    'update',
    'values'

----

*********************************************************************************
test_update_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

* I add a test for the next :ref:`method<functions>`

  .. code-block:: python

    def test_update(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(a_dictionary.update())

  the test is green. The update_ :ref:`method<functions>` returns :ref:`None`

* I add an assertion to see what it does to the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

  .. code-block:: python

        self.assertIsNone(a_dictionary.update())

    self.assertEqual(a_dictionary, {})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} != {}

  the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ stayed the same, the test has to get better

green: make it pass
#################################################################################

I change the values in the expectation to match the terminal

.. code-block:: python

  self.assertEqual(a_dictionary, {'key': 'value'})

the test passes

refactor: make it better
#################################################################################

* I check the Python documentation for the update_ :ref:`method<functions>` and see that it takes a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ as input. I add one to the call

  .. code-block:: python

    def test_update(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(a_dictionary.update({'key1': 'value1'}))
        self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value', 'key1': 'value1'} != {'key': 'value'}

  the update_ :ref:`method<functions>` adds the key-value pairs from the given `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ to the existing one

* I change the expectation to match the values from the terminal

  .. code-block:: python

    self.assertIsNone(a_dictionary.update({'key1': 'value1'}))
    self.assertEqual(
        a_dictionary,
        {
            'key': 'value',
            'key1': 'value1'
        }
    )

  the test passes

* I add another assertion

  .. code-block:: python

    self.assertIsNone(a_dictionary.update({'key1': 'value1'}))
    self.assertIsNone(a_dictionary.update(another_key='another value'))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value', 'key1': 'value1', 'another_key': 'another value'} != {'key': 'value', 'key1': 'value1'}

  the update_ :ref:`method<functions>` accepts keyword arguments. I change the values to match

  .. code-block:: python

    self.assertEqual(
        a_dictionary,
        {
            'key': 'value',
            'key1': 'value1',
            'another_key': 'another value'
        }
    )

  the test passes

* I want to know what would happen if the key already exists in the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

  .. code-block:: python

    self.assertIsNone(a_dictionary.update(another_key='another value'))
    self.assertIsNone(a_dictionary.update(key='new value'))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'new value', 'key1': 'value1', 'another_key': 'another value'} != {'key': 'value', 'key1': 'value1', 'another_key': 'another value'}

  the update_ :ref:`method<functions>` changes the value for an existing key in a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_. I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        a_dictionary,
        {
            'key': 'new value',
            'key1': 'value1',
            'another_key': 'another value'
        }
    )

  the test passes

* I rename the test

  .. code-block:: python

    def test_update_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(a_dictionary.update({'key1': 'value1'}))
        self.assertIsNone(a_dictionary.update(another_key='another value'))
        self.assertIsNone(a_dictionary.update(key='new value'))
        self.assertEqual(
            a_dictionary,
            {
                'key': 'new value',
                'key1': 'value1',
                'another_key': 'another value'
            }
        )

  the test is still green

* I remove update_ from the TODO list

  .. code-block:: python

    'values'

----

*********************************************************************************
test_values_of_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add a test for the last :ref:`method<functions>`

.. code-block:: python

  def test_update_a_dictionary(self):
        ...

  def test_values(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.values())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: dict_values(['value']) is not None

this is like :ref:`test_pop_removes_key_and_returns_its_value_from_a_dictionary` and  :ref:`test_keys_of_a_dictionary`

green: make it pass
#################################################################################

I change the assertIsNone_ to assertEqual_ and change the expectation to a list

.. code-block:: python

  a_dictionary = {'key': 'value'}
  self.assertEqual(a_dictionary.values(), ['value'])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: dict_values(['value']) != ['value']

I wrap the call in the :ref:`list<lists>` constructor_

.. code-block:: python

  self.assertEqual(list(a_dictionary.values()), ['value'])

the test passes

refactor: make it better
#################################################################################

* I add more keys and values to the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

  .. code-block:: python

    def test_values(self):
        a_dictionary = {
            'a_key': 'a value',
            'another_key': 'another value',
        }

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['a value', 'another value'] != ['value']

  I change the values

  .. code-block:: python

    self.assertEqual(
        list(a_dictionary.values()),
        ['a value', 'another value']
    )

  the test passes

* I rename the test

  .. code-block:: python

    def test_values_of_a_dictionary(self):
        a_dictionary = {
            'a_key': 'a value',
            'another_key': 'another value',
        }
        self.assertEqual(
            list(a_dictionary.values()),
            ['a value', 'another value']
        )

  the test passes

* I remove values_ from the TODO list

----

*********************************************************************************
test_key_error
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

    def test_values_of_a_dictionary(self):
        ...

    def test_key_error(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary['key'], '')

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'value' != ''

I can get the value for a key in a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ by giving it in ``[]``, this is like :ref:`viewing items in a list <test_get_items_from_a_list>`

green: make it pass
#################################################################################

I change the value in the expectation to match the terminal

.. code-block:: python

  self.assertEqual(a_dictionary['key'], 'value')

the test passes

refactor: make it better
#################################################################################

* I add another assertion

  .. code-block:: python

    self.assertEqual(a_dictionary['key'], 'value')
    self.assertEqual(a_dictionary['key_not_in_dictionary'], 'value')

  the terminal shows `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_

  .. code-block:: python

    KeyError: 'key_not_in_dictionary'

  I change the assertEqual_ to assertRaises_

  .. code-block:: python

    self.assertEqual(a_dictionary['key'], 'value')

    with self.assertRaises(KeyError):
        a_dictionary['key_not_in_dictionary']

  the test passes

* I know from :ref:`test_popitem_removes_and_returns_last_key_value_pair_from_a_dictionary` that I get `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_  when I call the :ref:`method<functions>` on an empty `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

  .. code-block::

    with self.assertRaises(KeyError):
        a_dictionary['key_not_in_dictionary']
    {}.popitem()

  the terminal shows `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_

  .. code-block:: python

    KeyError: 'popitem(): dictionary is empty'

  I add assertRaises_

  .. code-block:: python

    with self.assertRaises(KeyError):
        a_dictionary['key_not_in_dictionary']
    with self.assertRaises(KeyError):
        {}.popitem()

* I also get `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ when I call :ref:`pop <test_pop_removes_and_returns_key_w_value_from_a_dictionary>` with a key that does not exist in the `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

  .. code-block:: python

    with self.assertRaises(KeyError):
        {}.popitem()
    a_dictionary.pop('key_not_in_dictionary')

  the terminal shows `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_

  .. code-blocK:: python

    KeyError: 'key_not_in_dictionary'

  I add assertRaises_

  .. code-block:: python

    with self.assertRaises(KeyError):
        {}.popitem()
    with self.assertRaises(KeyError):
        a_dictionary.pop('key_not_in_dictionary')

* I can use the get_ :ref:`method<functions>` to avoid the `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ when the key does not exist in a `dictionary <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

  .. code-block:: python

    with self.assertRaises(KeyError):
        a_dictionary.pop('key_not_in_dictionary')


    self.assertEqual(
        a_dictionary.get('key_not_in_dictionary'),
        'value'
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 'value'

  I remove the expected value and change assertEqual_ to assertIsNone_

  .. code-block:: python

    with self.assertRaises(KeyError):
        a_dictionary.pop('key_not_in_dictionary')

    self.assertIsNone(a_dictionary.get('key_not_in_dictionary'))

  the test is green again

----

*********************************************************************************
review
*********************************************************************************

I ran tests for `dictionaries <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

* they contain key-value pairs
* any :ref:`object<classes>` can be used as values
* strings_, :ref:`booleans`, integers_, floats_ and tuples_ can be used as keys
* they can be represented with ``{}``
* they can be made with the `dict <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_ constructor_

Would you like to test :ref:`functions?<functions>`

----

:doc:`/code/code_dictionaries`