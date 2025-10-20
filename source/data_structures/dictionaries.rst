.. meta::
  :description: Master Python dictionaries with TDD! Learn key-value pairs, methods, and testing techniques in this hands-on guide. Start coding now!
  :keywords: Jacob Itegboje, Python dictionaries, Test-Driven Development, Python programming, data structures, unit testing, Python tutorial, coding guide

.. include:: ../links.rst

.. _clear: https://docs.python.org/3/library/stdtypes.html#dict.clear
.. _copy: https://docs.python.org/3/library/stdtypes.html#dict.copy
.. _pop: https://docs.python.org/3/library/stdtypes.html#dict.pop
.. _popitem: https://docs.python.org/3/library/stdtypes.html#dict.popitem
.. _dictionary: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
.. _dictionaries: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

.. danger:: DANGER WILL ROBINSON! Though the code works, this chapter is still UNDER CONSTRUCTION it may look completely different when I am done

#################################################################################
dictionaries
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

A dictionary_ also known as a Mapping contains key-value pairs, the values can be any Python_ :ref:`object<classes>`. I will add tests for the keys to see which :ref:`data types<data structures>` I can use.

I think this is the most important :ref:`data structure<data structures>` to know because they can hold all the other :ref:`data structures`. In programming I have had to work with JSON_ which I can read and write as dictionaries_ in Python

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
test_making_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I change ``test_failure``

.. code-block:: python

  class TestDictionaries(unittest.TestCase):

      def test_making_a_dictionary(self):
          self.assertEqual(dict(), None)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {} != None

green: make it pass
#################################################################################

I change the expectation to match

.. code-block:: python

  self.assertEqual(dict(), {})

the test passes. These are two ways to make an empty dictionary_

refactor: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>`, this time with input

  .. code-block:: python
    :emphasize-lines: 2

    self.assertEqual(dict(), {})
    self.assertEqual(dict(0), {})

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'int' object is not iterable

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # TypeError

* I change the value to a tuple_ since it is an iterable_

  .. code-block:: python
    :emphasize-lines: 2

    self.assertEqual(dict(), {})
    self.assertEqual(dict((0, 1)), {})

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: cannot convert dictionary update sequence element #0 to a sequence

* I try a keyword argument

  .. code-block:: python
    :emphasize-lines: 2

    self.assertEqual(dict(), {})
    self.assertEqual(dict(key='value'), {})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} != {}

  I change the expectation to match the values in the terminal

  .. code-block:: python

    self.assertEqual(dict(key='value'), {'key': 'value'})

  the terminal shows green again. I can make a dictionary_ with the dict_ constructor_ or curly braces(``{}``) and I used a string_ as a key in this test

----

*********************************************************************************
test_making_a_dictionary_w_none_as_a_key
*********************************************************************************

red: make it fail
#################################################################################

I add a test to see if I can use :ref:`None` as a key in a dictionary_

.. code-block:: python

  def test_making_a_dictionary(self):
      ...

  def test_making_a_dictionary_w_none_as_a_key(self):
      self.assertEqual({None: 'boom'}, {None: 'bap'})

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {None: 'boom'} != {None: 'bap'}

green: make it pass
#################################################################################

I change ``'bap'`` to ``'boom'``

.. code-block:: python

  self.assertEqual({None: 'boom'}, {None: 'boom'})

the test passes. I can use :ref:`None` and strings_ as keys in a dictionary_

----

*********************************************************************************
test_making_a_dictionary_w_a_boolean_as_a_key
*********************************************************************************

red: make it fail
#################################################################################

I add a test to see if I can use a :ref:`boolean<booleans>` as a key in a dictionary_

.. code-block:: python

    def test_making_a_dictionary_w_none_as_a_key(self):
        ...

    def test_making_a_dictionary_w_a_boolean_as_a_key(self):
        self.assertEqual({False: 'boom'}, {False: 'bap'})

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {False: 'boom'} != {False: 'bap'}

green: make it pass
#################################################################################

I change ``'bap'`` to ``'boom'``

.. code-block:: python

  self.assertEqual({False: 'boom'}, {False: 'boom'})

the tests passes. I can use :ref:`False<test_what_is_false>` as a key in a dictionary_

refactor: make it better
#################################################################################

I add :ref:`True<test_what_is_true>` to the :ref:`assertion<AssertionError>`

.. code-block:: python

  def test_making_a_dictionary_w_a_boolean_as_a_key(self):
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

the test passes. I can use :ref:`booleans`, :ref:`None` and strings_ as keys in a dictionary_

----

*********************************************************************************
test_making_a_dictionary_w_a_number_as_a_key
*********************************************************************************

red: make it fail
#################################################################################

I add a failing test to see if I can use a number as a key in a dictionary_

.. code-block:: python

  def test_making_a_dictionary_w_a_boolean_as_a_key(self):
      ...

  def test_making_a_dictionary_w_a_number_as_a_key(self):
      self.assertEqual({0: 'boom'}, {0: 'bap'})

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {0: 'boom'} != {0: 'bap'}

green: make it pass
#################################################################################

I change ``'bap'`` to ``'boom'``

.. code-block:: python

  self.assertEqual({0: 'boom'}, {0: 'boom'})

the test passes. I can use an integer_ as a key in a dictionary_

refactor: make it better
#################################################################################

I want to see if I can use a float_ as a key in a dictionary_

.. code-block:: python

  def test_making_a_dictionary_w_a_number_as_a_key(self):
      self.assertEqual(
          {0: 'boom', 0.1: 'bap'},
          {0: 'boom'}
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {0: 'boom', 0.1: 'bap'} != {0: 'boom'}

I add the new key-value pair to the expectation

.. code-block:: python

  self.assertEqual(
      {0: 'boom', 0.1: 'bap'},
      {0: 'boom', 0.1: 'bap'}
  )

the test passes. I can use numbers, :ref:`booleans`, :ref:`None` and strings_ as keys in a dictionary_

----

*********************************************************************************
test_making_a_dictionary_w_a_tuple_as_a_key
*********************************************************************************

red: make it fail
#################################################################################

I add a test to see if I can use a tuple_ as a key in a dictionary_

.. code-block:: python

  def test_making_a_dictionary_w_a_number_as_a_key(self):
      ...

  def test_making_a_dictionary_w_a_tuple_as_a_key(self):
      self.assertEqual(
          {(0, 1): 'boom'},
          {(0, 1): 'bap'}
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {(0, 1): 'boom'} != {(0, 1): 'bap'}

green: make it pass
#################################################################################

I change ``'bap'`` to ``'boom'``

.. code-block:: python

  self.assertEqual(
      {(0, 1): 'boom'},
      {(0, 1): 'boom'}
  )

the test passes. I can use tuples_, numbers (floats_ and integers_), :ref:`booleans`, :ref:`None` and strings_ as keys in a dictionary_

----

*********************************************************************************
test_making_a_dictionary_w_a_list_as_a_key
*********************************************************************************

red: make it fail
#################################################################################

I add a test for :ref:`lists`

.. code-block:: python

  def test_making_a_dictionary_w_a_tuple_as_a_key(self):
      ...

  def test_making_a_dictionary_w_a_list_as_a_key(self):
      self.assertEqual(
          {[0, 1]: 'boom'},
      )

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: unhashable type: 'list'

green: make it pass
#################################################################################

I remove the things around the new dictionary_ then change the key and value for fun

.. code-block:: python
  :emphasize-lines: 3

  def test_making_a_dictionary_w_a_list_as_a_key(self):

      {[3, 2, 1]: 'BOOM!!!'}

the terminal still shows :ref:`TypeError`, I add assertRaises_

.. code-block:: python
  :emphasize-lines: 2

  def test_making_a_dictionary_w_a_list_as_a_key(self):
      with self.assertRaises(TypeError):
          {[3, 2, 1]: 'BOOM!!!'}

the test passes. I cannot use a :ref:`list<lists>` as a key in a dictionary_

----

*********************************************************************************
test_making_a_dictionary_w_a_set_as_a_key
*********************************************************************************

red: make it fail
#################################################################################

I try another test with a set_ as a key in a dictionary_

.. code-block:: python

  def test_making_a_dictionary_w_a_list_as_a_key(self):
      ...

  def test_making_a_dictionary_w_a_set_as_a_key(self):
      {{3, 2, 1}: 'BOOM!!!'}

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: unhashable type: 'set'

green: make it pass
#################################################################################

I add assertRaises_

.. code-block:: python
  :emphasize-lines: 2

  def test_making_a_dictionary_w_a_set_as_a_key(self):
      with self.assertRaises(TypeError):
          {{3, 2, 1}: 'BOOM!!!'}

the test is green again. I cannot use a :ref:`lists` or sets_ as keys in a dictionary_

----

*********************************************************************************
test_making_a_dictionary_w_a_dictionary_as_a_key
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

  def test_making_a_dictionary_w_a_set_as_a_key(self):
      ...

  def test_making_a_dictionary_w_a_dictionary_as_a_key(self):
      a_dictionary = {'key': 'value'}
      {a_dictionary: 'BOOM!!!'}

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: unhashable type: 'dict'

green: make it pass
#################################################################################

I add assertRaises_

.. code-block:: python
  :emphasize-lines: 3

  def test_making_a_dictionary_w_a_dictionary_as_a_key(self):
      a_dictionary = {'key': 'value'}
      with self.assertRaises(TypeError):
          {a_dictionary: 'BOOM!!!'}

the test passes. I cannot use a dictionaries_, sets_ or :ref:`lists` as keys in a dictionary_ they are not hashable_, which means they can change

----

*********************************************************************************
test_attributes_and_methods_of_dictionaries
*********************************************************************************

red: make it fail
#################################################################################

I add a new test with the dir_ :ref:`function<functions>` to see the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of `dictionaries <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_

.. code-block:: python

  def test_attributes_and_methods_of_dictionaries(self):
      self.assertEqual(
          dir(dict),
          []
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: ['__class__', '__class_getitem__', '__cont[530 chars]ues'] != []

It also gives me a message to show the full difference between the two :ref:`lists`

.. code-block:: python

  Diff is 720 characters long. Set self.maxDiff to None to see it.

green: make it pass
#################################################################################

I move the terminal to right side of the screen, then add `maxDiff`_ to the test

.. code-block:: python
  :emphasize-lines: 3

  def test_attributes_and_methods_of_dictionaries(self):
      self.maxDiff = None
      self.assertEqual(
          dir(dict),
          []
      )

the terminal shows the difference between the two :ref:`lists`. I copy and paste the expected values from the terminal then use `find and replace`_ to remove the extra characters

.. note::

  results can be different because of Python_ version

.. code-block:: python

  def test_attributes_and_methods_of_dictionaries(self):
      self.maxDiff = None
      self.assertEqual(
          dir(src.dictionaries.a_dict()),
          [
              '__class__',
              ...
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

the test passes and I move the terminal back to the bottom. I copy the names that do NOT have double underscores (__) to make a TODO list of tests

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

red: make it fail
#################################################################################

* I add a test for the first :ref:`method<functions>`

  .. code-block:: python

      def test_attributes_and_methods_of_dictionaries(self):
          ...

      def test_clear(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.clear())

  the terminal shows green. The clear_ :ref:`method<functions>` returns :ref:`None`

* I add an :ref:`assertion<AssertionError>` to see what it did to the dictionary_

  .. code-block:: python

    self.assertIsNone(a_dictionary.clear())
    self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {} != {'key': 'value'}

  the clear_ :ref:`method<functions>` emptied the dictionary_, same as it does with :ref:`lists`

green: make it pass
#################################################################################

I change the values to match

.. code-block:: python

  self.assertEqual(a_dictionary, {})

the test passes

refactor: make it better
#################################################################################

* I rename the test

  .. code-block:: python

    def test_clear_empties_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(a_dictionary.clear())
        self.assertEqual(a_dictionary, {})

* I remove clear_ from the TODO list

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
      ...

  def test_copy(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.copy())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {'key': 'value'} is not None

this :ref:`method<functions>` returns a copy of the dictionary_

green: make it pass
#################################################################################

I add the value to the :ref:`assertion<AssertionError>`

.. code-block:: python

  self.assertIsNone(a_dictionary.copy(), {'key': 'value'})

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {'key': 'value'} is not None : {'key': 'value'}

I change assertIsNone_ to assertEqual_

.. code-block:: python

  self.assertEqual(a_dictionary.copy(), {'key': 'value'})

the test passes

refactor: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>` to see what happens to the dictionary_ after the call

  .. code-block:: python

    self.assertEqual(a_dictionary.copy(), {'key': 'value'})
    self.assertEqual(a_dictionary, {})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} != {}

  it stays the same. I change the values to match

  .. code-block:: python

    self.assertEqual(a_dictionary, {'key': 'value'})

  the test is green again. This :ref:`method<functions>` also works the same way with :ref:`lists`

* I rename the test

  .. code-block:: python

    def test_copy_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary.copy(), {'key': 'value'})
        self.assertEqual(a_dictionary, {'key': 'value'})

* I remove copy_ from the TODO list

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

I change the value to a tuple_

.. code-block:: python

  self.assertIsNone(a_dictionary.fromkeys((0, 1)))

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {0: None, 1: None} is not None

the fromkeys_ :ref:`method<functions>` returns a dictionary_ that uses the values in the iterable_ as keys with default values of :ref:`None`. I add the expected values

.. code-block:: python

  self.assertIsNone(
      a_dictionary.fromkeys((0, 1)),
      {0: None, 1: None}
  )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {0: None, 1: None} is not None : {0: None, 1: None}

I change assertIsNone_ to assertEqual_

.. code-block:: python

  self.assertEqual(
      a_dictionary.fromkeys((0, 1)),
      {0: None, 1: None}
  )

the test passes

refactor: make it better
#################################################################################

* I add another assert_ method to see what happens to the first dictionary_ in the test

  .. code-block:: python

    self.assertEqual(
        a_dictionary.fromkeys((0, 1)),
        {0: None, 1: None}
    )
    self.assertEqual(a_dictionary, {})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} != {}

  the dictionary_ did not change

* I remove the :ref:`assertion<AssertionError>` then change the call to use the dict_ :ref:`class<classes>`

  .. code-block:: python
    :emphasize-lines: 4

    def test_fromkeys(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(
            dict.fromkeys((0, 1)),
            {0: None, 1: None}
        )

  the test is still green. I remove ``a_dictionary`` since it is not used

  .. code-block:: python

    def test_fromkeys(self):
        self.assertEqual(
            dict.fromkeys((0, 1)),
            {0: None, 1: None}
        )

* the dictionary_ made with the fromkeys_ :ref:`method<functions>` has :ref:`None` as the default values. When I called the :ref:`method<functions>` without inputs the terminal showed :ref:`TypeError`

  .. code-block:: python

    TypeError: fromkeys expected at least 1 argument, got 0

  I add a second input to see what will happen

  .. code-block:: python

    self.assertEqual(
        dict.fromkeys((0, 1), None),
        {0: None, 1: None}
    )

  the terminal still shows green. I change the second input expecting a failure

  .. code-block:: python

    self.assertEqual(
        dict.fromkeys((0, 1), 'default'),
        {0: None, 1: None}
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {0: 'default', 1: 'default'} != {0: None, 1: None}

  I change the values to match

  .. code-block:: python

    self.assertEqual(
        dict.fromkeys((0, 1), 'default'),
        {0: 'default', 1: 'default'}
    )

  the test is green again. This is like a dict comprehension because it made a dictionary_ using the items from the iterable_ as keys

* I rename the test

  .. code-block:: python

    def test_fromkeys_makes_a_dictionary_from_an_iterable(self):
        self.assertEqual(
            dict.fromkeys((0, 1), 'default'),
            {0: 'default', 1: 'default'}
        )

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
test_get_value_of_a_key_in_a_dictionary
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

I add a value to the call

.. code-block:: python

  self.assertIsNone(a_dictionary.get(0))

the terminal shows green

refactor: make it better
#################################################################################

* this :ref:`method<functions>` also expected at least 1 argument, I add :ref:`None` to the call

  .. code-block:: python

    self.assertIsNone(a_dictionary.get(0, None))

  the terminal still shows green. I change the second argument expecting a failure

  .. code-block:: python

    self.assertIsNone(a_dictionary.get(0, 'default'))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'default' is not None

  I add the expectation

  .. code-block:: python

    self.assertIsNone(a_dictionary.get(0, 'default'), 'default')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'default' is not None : default

  I change the :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(
        a_dictionary.get(0, 'default'),
        'default'
    )

  the test passes. I change the ``0`` to be more descriptive

  .. code-block:: python

    self.assertEqual(
        a_dictionary.get('not_in_dictionary', 'default'),
        'default'
    )

* I want to see what would happen if I use the get_ :ref:`method<functions>` with a key that is in the dictionary_

  .. code-block:: python

    self.assertEqual(
        a_dictionary.get('not_in_dictionary', 'default'),
        'default'
    )
    self.assertEqual(
        a_dictionary.get('key', 'default'),
        'default'
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'value' != 'default'

  the get_ :ref:`method<functions>` has a condition. When the key is NOT in the dictionary_, it returns the default argument, when the key is in the dictionary_, it returns its value. I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        a_dictionary.get('key', 'default'),
        'value'
    )

  the test passes

* I change the name of the test

  .. code-block:: python

    def test_get_value_of_a_key_in_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(
            a_dictionary.get('not_in_dictionary', 'default'),
            'default'
        )
        self.assertEqual(
            a_dictionary.get('key', 'default'),
            'default'
        )

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
test_items_returns_iterable_of_key_value_pairs_of_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add the next test from the list

.. code-block:: python

  def test_get_value_of_a_key_in_a_dictionary(self):
      ...

  def test_items(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.items())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: dict_items([('key', 'value')]) is not None

green: make it pass
#################################################################################

I copy the value from the terminal and paste it as the expectation

.. code-block:: python

  self.assertIsNone(a_dictionary.items(), dict_items([('key', 'value')]))

the terminal shows NameError_

.. code-block:: python

  NameError: name 'dict_items' is not defined

this new :ref:`object<classes>` contains a :ref:`list<lists>` and I know how to work with :ref:`lists`, I remove the stuff around it

.. code-block:: python

  self.assertIsNone(a_dictionary.items(), [('key', 'value')])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: dict_items([('key', 'value')]) is not None : [('key', 'value')]

I pass the call to the items_ :ref:`method<functions>` to the :ref:`list<lists>` constructor_ to see what happens

.. code-block:: python

  self.assertIsNone(list(a_dictionary.items()), [('key', 'value')])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [('key', 'value')] is not None : [('key', 'value')]

the values are the same, I change assertIsNone_ to assertEqual_

.. code-block:: python

  self.assertEqual(list(a_dictionary.items()), [('key', 'value')])

the test passes. This works because the items_ :ref:`method<functions>` returns an iterable_ of the key-value pairs of the dictionary_

refactor: make it better
#################################################################################

* I add another key-value pair to the dictionary_ to see what the :ref:`method<functions>` does when there is more than one key-value pair

  .. code-block:: python

    def test_items(self):
        a_dictionary = {
            'key1': 'value1',
            'keyN': [0, 1, 2, 'n'],
        }
        self.assertEqual(list(a_dictionary.items()), [('key', 'value')])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [('key1', 'value1'), ('keyN', [0, 1, 2, 'n'])] != [('key', 'value')]

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        list(a_dictionary.items()),
        [
            ('key1', 'value1'),
            ('keyN', [0, 1, 2, 'n']),
        ]
    )

  the test passes

* I change the name of the test

  .. code-block:: python

    def test_items_returns_iterable_of_key_value_pairs_of_a_dictionary(self):
        a_dictionary = {
            'key1': 'value1',
            'keyN': [0, 1, 2, 'n'],
        }
        self.assertEqual(
            list(a_dictionary.items()),
            [
                ('key1', 'value1'),
                ('keyN', [0, 1, 2, 'n']),
            ]
        )

* I remove items_ from the TODO list

  .. code-block:: python

    'keys',
    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

  all tests are still passing

----

*********************************************************************************
test_keys_of_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

  def test_items_returns_iterable_of_key_value_pairs_of_a_dictionary(self):
      ...

  def test_keys(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.keys())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: dict_keys(['key']) is not None

this looks like the error in :ref:`test_items_returns_iterable_of_key_value_pairs_of_a_dictionary`

green: make it pass
#################################################################################

I copy the value from the terminal and paste it as the expectation

.. code-block:: python

  self.assertIsNone(a_dictionary.keys(), dict_keys(['key']))

the terminal shows NameError_

.. code-block:: python

  NameError: name 'dict_keys' is not defined

the ``dict_keys`` :ref:`object<classes>` contains a :ref:`list<lists>`, I will use it as the expectation instead

.. code-block:: python

  self.assertIsNone(a_dictionary.keys(), ['key'])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: dict_keys(['key']) is not None : ['key']

I pass the call to the keys_ :ref:`method<functions>` to the :ref:`list<lists>` constructor_

.. code-block:: python

  self.assertIsNone(list(a_dictionary.keys()), ['key'])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: ['key'] is not None : ['key']

I change assertIsNone_ to assertEqual_

.. code-block:: python

  self.assertEqual(list(a_dictionary.items()), [('key', 'value')])

the test passes

refactor: make it better
#################################################################################

* I add another key-value pair to the dictionary_ to see what the keys_ :ref:`method<functions>` returns when there are multiple

  .. code-block:: python

    def test_keys(self):
        a_dictionary = {
            'key1': 'value1',
            'keyN': [0, 1, 2, 'n'],
        }
        self.assertEqual(list(a_dictionary.keys()), ['key'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['key1', 'keyN'] != ['key']

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(list(a_dictionary.keys()), ['key1', 'keyN'])

  the test passes

* I change the name of the test

  .. code-block:: python

    def test_keys_of_a_dictionary(self):
        a_dictionary = {
            'key1': 'value1',
            'keyN': [0, 1, 2, 'n'],
        }
        self.assertEqual(list(a_dictionary.keys()), ['key1', 'keyN'])

* I remove keys_ from the TODO list

  .. code-block:: python

    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

----

*********************************************************************************
test_pop_removes_given_key_from_a_dictionary_and_returns_its_value
*********************************************************************************

red: make it fail
#################################################################################

I wonder if the next :ref:`method<functions>` is the same as the one in :ref:`test_pop_removes_and_returns_last_item_from_a_list`, I add a test for it

.. code-block:: python

  def test_keys_of_a_dictionary(self):
      ...

  def test_pop(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.pop())

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: pop expected at least 1 argument, got 0

this pop_ :ref:`method<functions>` is different from the one in :ref:`lists`

green: make it pass
#################################################################################

* I pass a value to the call

  .. code-block:: python

    self.assertIsNone(a_dictionary.pop(0))

  the terminal shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: 0

* I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # KeyError

* I remove the things around the call and change the value given to be more descriptive

  .. code-block:: python

    a_dictionary = {'key': 'value'}
    a_dictionary.pop('not in dictionary')

  the terminal shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: 'not in dictionary'

  I add assertRaises_

  .. code-block:: python

    a_dictionary = {'key': 'value'}

    with self.assertRaises(KeyError):
        a_dictionary.pop('not in dictionary')

  the test passes, calling the pop_ :ref:`method<functions>` with a key that is not in the dictionary_ raises a :ref:`KeyError <test_key_error>`

refactor: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    a_dictionary = {'key': 'value'}
    self.assertIsNone(a_dictionary.pop('key'))

    with self.assertRaises(KeyError):
        a_dictionary.pop('not in dictionary')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'value' is not None

  the pop_ :ref:`method<functions>` returns the value of the given key from the dictionary_. I add the expectation

  .. code-block:: python

    self.assertIsNone(a_dictionary.pop('key'), 'value')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'value' is not None : value

  I change assertIsNone_ to assertEqual_

  .. code-block:: python

    self.assertEqual(a_dictionary.pop('key'), 'value')

  the test passes

* I add another :ref:`assertion<AssertionError>` to see what the :ref:`method<functions>` did to the dictionary_

  .. code-block:: python

    self.assertEqual(a_dictionary.pop('key'), 'value')
    self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {} != {'key': 'value'}

  pop_ :ref:`method<functions>` removes the key-value pair and returns the value of the given key from the dictionary_. I change the expectation to match

  .. code-block:: python

    self.assertEqual(a_dictionary, {})

  the test passes

* I rename the test

  .. code-block:: python

    def test_pop_removes_given_key_from_a_dictionary_and_returns_its_value(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary.pop('key'), 'value')
        self.assertEqual(a_dictionary, {})

        with self.assertRaises(KeyError):
            a_dictionary.pop('not in dictionary')

* I remove pop_ from the TODO list

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

  def test_pop_removes_given_key_from_a_dictionary_and_returns_its_value(self):
      ...

  def test_pop_item(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.popitem())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: ('key', 'value') is not None

the popitem_ :ref:`method<functions>` returns the key-value pair as a tuple_

green: make it pass
#################################################################################

I add the value from the terminal as an expectation

.. code-block:: python

  self.assertIsNone(a_dictionary.popitem(), ('key', 'value'))

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: ('key', 'value') is not None : ('key', 'value')

I change assertIsNone_ to assertEqual_

.. code-block:: python

  self.assertEqual(a_dictionary.popitem(), ('key', 'value'))

the test passes

refactor: make it better
#################################################################################

* I want to know what the popitem_ :ref:`method<functions>` did to the dictionary_

  .. code-block:: python

    self.assertEqual(a_dictionary.popitem(), ('key', 'value'))
    self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {} != {'key': 'value'}

  popitem_ removes and returns the key-value pair from the dictionary_

* I change the value

  .. code-block:: python

    self.assertEqual(a_dictionary, {})

  the test passes

* this operation does not take input, I change the dictionary_ to see how it responds

  .. code-block:: python

    a_dictionary = {
        'key1': 'value1',
        'keyN': [0, 1, 2, 'n'],
    }

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ('keyN', [0, 1, 2, 'n']) != ('key', 'value')

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(a_dictionary.popitem(), ('keyN', [0, 1, 2, 'n']))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key1': 'value1'} != {'key': 'value'}

  I change the value to match

  .. code-block:: python

    self.assertEqual(a_dictionary, {'key1': 'value1'})

  the test passes

* I add another call to the :ref:`method<functions>`

  .. code-block:: python

    self.assertEqual(a_dictionary, {'key1': 'value1'})
    self.assertEqual(a_dictionary.popitem(), ('keyN', [0, 1, 2, 'n']))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Tuples differ: ('key1', 'value1') != ('keyN', [0, 1, 2, 'n'])

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_dictionary.popitem(), ('key1', 'value1'))

  the test passes. popitem_ removes and returns the last key-value pair from a dictionary_

* I change the name of the test

  .. code-block:: python

    def test_popitem_removes_and_returns_last_key_value_pair_from_a_dictionary(self):
        a_dictionary = {
            'key1': 'value1',
            'keyN': [0, 1, 2, 'n'],
        }
        self.assertEqual(a_dictionary.popitem(), ('keyN', [0, 1, 2, 'n']))
        self.assertEqual(a_dictionary, {'key1': 'value1'})
        self.assertEqual(a_dictionary.popitem(), ('key1', 'value1'))

* I remove popitem_ from the TODO list

  .. code-block:: python

    'setdefault',
    'update',
    'values'

----

*********************************************************************************
test_setdefault_adds_given_key_to_a_dictionary
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

* I add an :ref:`assertion<AssertionError>` to see what it did to the dictionary_

  .. code-block:: python

    self.assertIsNone(a_dictionary.setdefault(0))
    self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value', 0: None} != {'key': 'value'}

  setdefault_ adds the given key to the dictionary_ with a default value of :ref:`None` and returns the default value

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

* I change the name of the value given

  .. code-block:: python

    a_dictionary = {'key': 'value'}
    self.assertIsNone(a_dictionary.setdefault('new_key'))
    self.assertEqual(
        a_dictionary,
        {
            'key': 'value',
            0: None,
        }
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value', 'new_key': None} != {'key': 'value', 0: None}

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        a_dictionary,
        {
            'key': 'value',
            'new_key': None,
        }
    )

  the test is green again

* I add an :ref:`assertion<AssertionError>` to see what happens when the key is already in the dictionary_

  .. code-block:: python

    self.assertIsNone(a_dictionary.setdefault('new_key'))
    self.assertIsNone(a_dictionary.setdefault('key'))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'value' is not None

  setdefault_ returns the value for a key in a dictionary_ when the key is in the dictionary_. I add the value to the :ref:`assertion<AssertionError>`

  .. code-block:: Python

    self.assertIsNone(a_dictionary.setdefault('key'), 'value')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'value' is not None : value

  I change assertIsNone_ to assertEqual_

  .. code-block:: python

    self.assertEqual(a_dictionary.setdefault('key'), 'value')

  the test passes

* It looks like setdefault_ has a condition where it sets a default value when the key is not in the dictionary_ and returns the value when the key is in it. I change the first :ref:`assertion<AssertionError>` to find out

  .. code-block:: python

    self.assertIsNone(a_dictionary.setdefault('new_key', None))

  the terminal still shows green. I change the given default value expecting a failure

  .. code-block:: python

    self.assertIsNone(a_dictionary.setdefault('new_key', 'default'))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'default' is not None

  I add the expected value

  .. code-block:: python

    self.assertIsNone(a_dictionary.setdefault('new_key', 'default'), 'default')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'default' is not None : default

  I change assertIsNone_ to assertEqual_

  .. code-block:: python

    self.assertEqual(a_dictionary.setdefault('new_key', 'default'), 'default')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value', 'new_key': 'default'} != {'key': 'value', 'new_key': None}

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        a_dictionary,
        {
            'key': 'value',
            'new_key': 'default',
        }
    )

  the test passes

* I try the same thing with the second :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_dictionary.setdefault('key', 'default'), 'value')

  the terminal still shows green. setdefault_ adds a given key to the dictionary_ with a given default value and returns the default value if the key is not in the dictionary. It returns the value for a key that is already in the dictionary_

* I rename the test

  .. code-block:: python

    def test_setdefault_adds_given_key_to_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary.setdefault('new_key', 'default'), 'default')
        self.assertEqual(a_dictionary.setdefault('key', 'default'), 'value')
        self.assertEqual(
            a_dictionary,
            {
                'key': 'value',
                'new_key': 'default',
            }
        )

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

    def test_setdefault_adds_given_key_to_a_dictionary(self):
        ...

    def test_update(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(a_dictionary.update())

  the test is green. The update_ :ref:`method<functions>` returns :ref:`None`

* I add an :ref:`assertion<AssertionError>` to see what it did to the dictionary_

  .. code-block:: python

    self.assertIsNone(a_dictionary.update())
    self.assertEqual(a_dictionary, {})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} != {}

  the dictionary_ stayed the same

green: make it pass
#################################################################################

I change the values in the expectation to match the terminal

.. code-block:: python

  self.assertEqual(a_dictionary, {'key': 'value'})

the test passes

refactor: make it better
#################################################################################

* I add a value to the call to see what would happen

  .. code-block:: python

    self.assertIsNone(a_dictionary.update(0))

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'int' object is not iterable

  I change the value to a tuple_

  .. code-block:: python

    self.assertIsNone(a_dictionary.update((0, 1)))

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: cannot convert dictionary update sequence element #0 to a sequence

  I had this same error message in :ref:`test_making_a_dictionary`. I try a keyword argument

  .. code-block:: python

    self.assertIsNone(a_dictionary.update(new_key='new value'))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value', 'new_key': 'new value'} != {'key': 'value'}

  I add the new key-value pair to the :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(
        a_dictionary,
        {
            'key': 'value',
            'new_key': 'new value'
        }
    )

  the test passes

* I add an :ref:`assertion<AssertionError>` to see what would happen if I give a key that is already in the dictionary_

  .. code-block:: python

    self.assertIsNone(a_dictionary.update(new_key='new value'))
    self.assertIsNone(a_dictionary.update(key='updated value'))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'updated value', 'new_key': 'new value'} != {'key': 'value', 'new_key': 'new value'}

  the update_ :ref:`method<functions>` changes the value for a key that is already in a dictionary_. I change the expectation to match. I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        a_dictionary,
        {
            'key': 'updated value',
            'new_key': 'new value'
        }
    )

  the test passes

* since the update_ :ref:`method<functions>` takes keyword arguments it means I should be able to give it a dictionary_ as input. I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertIsNone(a_dictionary.update({'another_key': 'another_value'}))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'updated value', 'new_key': 'new value', 'another_key': 'another_value'} != {'key': 'updated value', 'new_key': 'new value'}

  the update_ :ref:`method<functions>` adds the key-value pairs from the given dictionary_ to the existing one. I change the expectation to match

  .. code-block:: python

    self.assertEqual(
        a_dictionary,
        {
            'key': 'updated value',
            'new_key': 'new value',
            'another_key': 'another_value',
        }
    )

  the test passes

* I rename the test

  .. code-block:: python

    def test_update_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(a_dictionary.update(new_key='new value'))
        self.assertIsNone(a_dictionary.update(key='updated value'))
        self.assertIsNone(a_dictionary.update({'another_key': 'another_value'}))
        self.assertEqual(
            a_dictionary,
            {
                'key': 'updated value',
                'new_key': 'new value',
                'another_key': 'another_value',
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

this is like :ref:`test_items_returns_iterable_of_key_value_pairs_of_a_dictionary` and  :ref:`test_keys_of_a_dictionary`

green: make it pass
#################################################################################

I add the expected value

.. code-block:: python

  self.assertIsNone(a_dictionary.values, dict_values(['value']))

the terminal shows NameError_

.. code-block:: python

  NameError: name 'dict_values' is not defined

I use the :ref:`list<lists>` in the ``dict_values`` object_

.. code-block:: python

  self.assertIsNone(a_dictionary.values(), ['value'])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: dict_values(['value']) is not None : ['value']

I change assertIsNone_ to assertEqual_

.. code-block:: python

  self.assertEqual(a_dictionary.values(), ['value'])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: dict_values(['value']) != ['value']

I pass the call to the :ref:`list<lists>` constructor_

.. code-block:: python

  self.assertEqual(list(a_dictionary.values()), ['value'])

the test passes

refactor: make it better
#################################################################################

* I change the dictionary_

  .. code-block:: python

    a_dictionary = {
        'key1': 'value1',
        'keyN': [0, 1, 2, 'n'],
    }

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['value1', [0, 1, 2, 'n']] != ['value']

  I change the values in the expectation

  .. code-block:: python

        self.assertEqual(
            list(a_dictionary.values()),
            ['value1', [0, 1, 2, 'n']]
        )

  the test passes

* I rename the test

  .. code-block:: python

    def test_values_of_a_dictionary(self):
        a_dictionary = {
            'key1': 'value1',
            'keyN': [0, 1, 2, 'n'],
        }
        self.assertEqual(
            list(a_dictionary.values()),
            ['value1', [0, 1, 2, 'n']]
        )

* I remove values_ from the TODO list

----

*********************************************************************************
test_key_error
*********************************************************************************

The `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ is an important Exception_ to know when working with a dictionary_

red: make it fail
#################################################################################

I add a test for getting the value of a key that is in a dictionary_

.. code-block:: python

    def test_values_of_a_dictionary(self):
        ...

    def test_key_error(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary['key'], '')

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'value' != ''

I can get the value for a key in a dictionary_ by giving it in ``[]``, this is like :ref:`viewing items in a list <test_getting_items_of_a_list>`

green: make it pass
#################################################################################

I change the value in the expectation to match the terminal

.. code-block:: python

  self.assertEqual(a_dictionary['key'], 'value')

the test passes

refactor: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_dictionary['key'], 'value')
    self.assertEqual(a_dictionary['not_in_dictionary'])

  the terminal shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: 'key_not_in_dictionary'

  I change the assertEqual_ to assertRaises_

  .. code-block:: python

    self.assertEqual(a_dictionary['key'], 'value')

    with self.assertRaises(KeyError):
        a_dictionary['not_in_dictionary']

  the test passes

* I add an :ref:`assertion<AssertionError>` to show that I can use the get_ :ref:`method<functions>` if I do not want to get :ref:`KeyError<test_key_error>` with a key that is not in a dictionary_

  .. code-block:: python

    self.assertEqual(a_dictionary['key'], 'value')
    self.assertEqual(a_dictionary.get('not_in_dictionary', 'default'), 'value')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'default' != 'value'

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_dictionary.get('not_in_dictionary', 'default'), 'default')

  the test passes

* Earlier on in :ref:`test_pop_removes_given_key_from_a_dictionary_and_returns_its_value` the pop_ :ref:`method<functions>` raised :ref:`KeyError<test_key_error>` with a key that was not in the dictionary_, I add an :ref:`assertion<AssertionError>` for it

  .. code-block:: python

    with self.assertRaises(KeyError):
        a_dictionary['not_in_dictionary']
    a_dictionary.pop('not_in_dictionary')

  the terminal shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: 'not_in_dictionary'

  I add assertRaises_

  .. code-block:: python

    with self.assertRaises(KeyError):
        a_dictionary['not_in_dictionary']
    with self.assertRaises(KeyError):
        a_dictionary.pop('not_in_dictionary')

  the test passes

* The popitem_ :ref:`method<functions>` also raises :ref:`KeyError<test_key_error>` when called on an empty dictionary_

  .. code-block::

    with self.assertRaises(KeyError):
        a_dictionary.pop('not_in_dictionary')
    {}.popitem()

  the terminal shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: 'popitem(): dictionary is empty'

  I add assertRaises_

  .. code-block:: python

    with self.assertRaises(KeyError):
        a_dictionary.pop('not_in_dictionary')
    with self.assertRaises(KeyError):
        {}.popitem()

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

Would you like to :ref:`test functions?<functions>`

----

:doc:`/code/code_dictionaries`