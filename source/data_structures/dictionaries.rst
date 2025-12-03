.. meta::
  :description: Master Python dictionaries with TDD! Learn :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`s, methods, and testing techniques in this hands-on guide. Start coding now!
  :keywords: Jacob Itegboje, Python dictionaries, Test-Driven Development, Python programming, data structures, unit testing, Python tutorial, coding guide

.. include:: ../links.rst

.. _clear: https://docs.python.org/3/library/stdtypes.html#dict.clear
.. _copy: https://docs.python.org/3/library/stdtypes.html#dict.copy
.. _pop: https://docs.python.org/3/library/stdtypes.html#dict.pop
.. _popitem: https://docs.python.org/3/library/stdtypes.html#dict.popitem
.. _dictionary: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
.. _dictionaries: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
.. _dict: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

.. danger:: DANGER WILL ROBINSON! Though the code works, this chapter is still UNDER CONSTRUCTION it may look completely different when I am done

#################################################################################
dictionaries
#################################################################################

----

A dictionary_ also known as a Mapping is a way to keep :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`, the :ref:`values<test_values_of_a_dictionary>` can be any Python_ :ref:`object<classes>`. I add tests for the :ref:`keys<test_keys_of_a_dictionary>` to see which of :ref:`the Python basic data types<data structures>` I can use.

I think this is the most important :ref:`data structure<data structures>` to know because they can hold all the other :ref:`data structures`. In programming I have had to work with JSON_ which I can read and write as dictionaries_

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``dictionaries`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh dictionaries

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: python

      ./makePythonTdd.ps1 dictionaries

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_dictionaries.py:7: AssertionError

* I hold ``ctrl`` (Windows/Linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_dictionaries.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change ``True`` to ``False`` to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestDictionaries(unittest.TestCase):

----

*********************************************************************************
test_making_a_dictionary
*********************************************************************************

RED: make it fail
#################################################################################

I change ``test_failure`` to ``test_making_a_dictionary`` then add an assertion_

.. code-block:: python
  :linenos:
  :emphasize-lines: 6-7

  import unittest


  class TestDictionaries(unittest.TestCase):

      def test_making_a_dictionary(self):
          self.assertEqual(dict(), None)

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: {} != None

GREEN: make it pass
#################################################################################

I change the expectation to match

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 2

      def test_making_a_dictionary(self):
          self.assertEqual(dict(), {})

the test passes. These are two ways to make an empty dictionary_ one

* with the constructor_ - ``dict()`` and with
* curly braces - ``{}``

REFACTOR: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>`, this time with input

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

        def test_making_a_dictionary(self):
            self.assertEqual(dict(), {})
            self.assertEqual(dict(0), {})

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'int' object is not iterable

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_dictionaries.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # TypeError

* I change the value to a tuple_ since it is an iterable_

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

            self.assertEqual(dict(), {})
            self.assertEqual(dict((0, 1)), {})

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: cannot convert dictionary update sequence element #0 to a sequence

* I try a :ref:`keyword argument<test_functions_w_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

            self.assertEqual(dict(), {})
            self.assertEqual(dict(key='value'), {})

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'key': 'value'} != {}

  I change the expectation to match the values in the terminal_

  .. code-block:: python

    self.assertEqual(dict(key='value'), {'key': 'value'})

  the test passes.

I can make a dictionary_ with the dict_ constructor_ or curly braces(``{}``) and I used a string_ as a :ref:`key<test_keys_of_a_dictionary>` in this test. Next I test the Python_ basic :ref:`data types<data structures>` to see which ones I can use as keys

----

*********************************************************************************
test_making_a_dictionary_w_none_as_a_key
*********************************************************************************

RED: make it fail
#################################################################################

I add a test to see if I can use :ref:`None` as a :ref:`key<test_keys_of_a_dictionary>` in a dictionary_

.. code-block:: python
  :lineno-start: 8
  :emphasize-lines: 3-4

          self.assertEqual(dict(key='value'), {'key': 'value'})

      def test_making_a_dictionary_w_none_as_a_key(self):
          self.assertEqual({None: 'boom'}, {None: 'bap'})


  # Exceptions Encountered

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: {None: 'boom'} != {None: 'bap'}

GREEN: make it pass
#################################################################################

I change ``'bap'`` to ``'boom'``

.. code-block:: python
  :lineno-start: 11
  :emphasize-lines: 1

          self.assertEqual({None: 'boom'}, {None: 'boom'})

the test passes. I can use :ref:`None` and strings_ as :ref:`keys<test_keys_of_a_dictionary>` in a dictionary_

----

*********************************************************************************
test_making_a_dictionary_w_a_boolean_as_a_key
*********************************************************************************

RED: make it fail
#################################################################################

I add a test to see if I can use a :ref:`boolean<booleans>` as a :ref:`key<test_keys_of_a_dictionary>` in a dictionary_

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 4-5

      def test_making_a_dictionary_w_none_as_a_key(self):
          self.assertEqual({None: 'boom'}, {None: 'boom'})

      def test_making_a_dictionary_w_a_boolean_as_a_key(self):
          self.assertEqual({False: 'boom'}, {False: 'bap'})


  # Exceptions Encountered

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: {False: 'boom'} != {False: 'bap'}

GREEN: make it pass
#################################################################################

I change ``'bap'`` to ``'boom'``

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 1

          self.assertEqual({False: 'boom'}, {False: 'boom'})

the tests passes. I can use :ref:`False<test_what_is_false>` as a :ref:`key<test_keys_of_a_dictionary>` in a dictionary_

REFACTOR: make it better
#################################################################################

I add an :ref:`assertion<AssertionError>` for the :ref:`other boolean<test_what_is_true>`

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 3-4

      def test_making_a_dictionary_w_a_boolean_as_a_key(self):
          self.assertEqual(
              {False: 'boom', True: 'bap'},
              {False: 'boom'}
          )

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: {False: 'boom', True: 'bap'} != {False: 'boom'}

I add the new :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to the expectation

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 3

          self.assertEqual(
              {False: 'boom', True: 'bap'},
              {False: 'boom', True: 'bap'}
          )

the test passes. I can use :ref:`booleans`, :ref:`None` and strings_ as :ref:`keys<test_keys_of_a_dictionary>` in a dictionary_

----

*********************************************************************************
test_making_a_dictionary_w_a_number_as_a_key
*********************************************************************************

RED: make it fail
#################################################################################

I add a failing test to see if I can use a number as a :ref:`key<test_keys_of_a_dictionary>` in a dictionary_

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 4-8

              {False: 'boom', True: 'bap'}
          )

      def test_making_a_dictionary_w_a_number_as_a_key(self):
          self.assertEqual(
              {0: 'boom'},
              {0: 'bap'}
          )


  # Exceptions Encountered

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: {0: 'boom'} != {0: 'bap'}

GREEN: make it pass
#################################################################################

I change ``'bap'`` to ``'boom'``

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 3

          self.assertEqual(
              {0: 'boom'},
              {0: 'boom'}
          )

the test passes. I can use an integer_ as a :ref:`key<test_keys_of_a_dictionary>` in a dictionary_

REFACTOR: make it better
#################################################################################

I want to see if I can use a float_ as a :ref:`key<test_keys_of_a_dictionary>` in a dictionary_

.. code-block:: python

      def test_making_a_dictionary_w_a_number_as_a_key(self):
          self.assertEqual(
              {0: 'boom', 0.1: 'bap'},
              {0: 'boom'}
          )

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: {0: 'boom', 0.1: 'bap'} != {0: 'boom'}

I add the new :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to the expectation

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 3

          self.assertEqual(
              {0: 'boom', 0.1: 'bap'},
              {0: 'boom', 0.1: 'bap'}
          )

the test passes. I can use numbers (floats_ and integers_), :ref:`booleans`, :ref:`None` and strings_ as :ref:`keys<test_keys_of_a_dictionary>` in a dictionary_

----

*********************************************************************************
test_making_a_dictionary_w_a_tuple_as_a_key
*********************************************************************************

RED: make it fail
#################################################################################

I add a test to see if I can use a tuple_ (anything in parentheses (``()``)) as a :ref:`key<test_keys_of_a_dictionary>` in a dictionary_

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 4-8

              {0: 'boom', 0.1: 'bap'}
          )

      def test_making_a_dictionary_w_a_tuple_as_a_key(self):
          self.assertEqual(
              {(0, 1): 'boom'},
              {(0, 1): 'bap'}
          )


  # Exceptions Encountered

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: {(0, 1): 'boom'} != {(0, 1): 'bap'}

GREEN: make it pass
#################################################################################

I change ``'bap'`` to ``'boom'``

.. code-block:: python
  :lineno-start: 26

          self.assertEqual(
              {(0, 1): 'boom'},
              {(0, 1): 'boom'}
          )

the test passes. I can use tuples_, numbers (floats_ and integers_), :ref:`booleans`, :ref:`None` and strings_ as :ref:`keys<test_keys_of_a_dictionary>` in a dictionary_

----

*********************************************************************************
test_making_a_dictionary_w_a_list_as_a_key
*********************************************************************************

RED: make it fail
#################################################################################

I add a test for :ref:`lists` (anything in square brackets (``[]``))

.. code-block:: python
  :lineno-start: 28
  :emphasize-lines: 4-8

              {(0, 1): 'boom'}
          )

      def test_making_a_dictionary_w_a_list_as_a_key(self):
          self.assertEqual(
              {[0, 1]: 'boom'},
          )


  # Exceptions Encountered

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: unhashable type: 'list'

GREEN: make it pass
#################################################################################

I remove the things around the new dictionary_ then change the :ref:`key<test_keys_of_a_dictionary>` and :ref:`value<test_values_of_a_dictionary>` for fun

.. code-block:: python
  :lineno-start: 31
  :emphasize-lines: 2-4

      def test_making_a_dictionary_w_a_list_as_a_key(self):

          {[3, 2, 1]: 'BOOM!!!'}


the terminal_ still shows :ref:`TypeError`. I add assertRaises_

.. code-block:: python
  :lineno-start: 31
  :emphasize-lines: 2

      def test_making_a_dictionary_w_a_list_as_a_key(self):
          with self.assertRaises(TypeError):
              {[3, 2, 1]: 'BOOM!!!'}

the test passes. I cannot use a :ref:`list<lists>` as a :ref:`key<test_keys_of_a_dictionary>` in a dictionary_

----

*********************************************************************************
test_making_a_dictionary_w_a_set_as_a_key
*********************************************************************************

RED: make it fail
#################################################################################

I add another test with a set_ (single items in a curly braces (``{}``)) as a :ref:`key<test_keys_of_a_dictionary>` in a dictionary_

.. code-block:: python
  :lineno-start: 33
  :emphasize-lines: 3-4

              {[3, 2, 1]: 'BOOM!!!'}

      def test_making_a_dictionary_w_a_set_as_a_key(self):
          {{3, 2, 1}: 'BOOM!!!'}


  # Exceptions Encountered

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: unhashable type: 'set'

GREEN: make it pass
#################################################################################

I add assertRaises_ to handle the :ref:`Exception<errors>`

.. code-block:: python
  :lineno-start: 35
  :emphasize-lines: 2-3

      def test_making_a_dictionary_w_a_set_as_a_key(self):
          with self.assertRaises(TypeError):
              {{3, 2, 1}: 'BOOM!!!'}

the test is green again. I cannot use :ref:`lists` or sets_ as :ref:`keys<test_keys_of_a_dictionary>` in a dictionary_

----

*********************************************************************************
test_making_a_dictionary_w_a_dictionary_as_a_key
*********************************************************************************

RED: make it fail
#################################################################################

I add another test, this time for a dictionary_

.. code-block:: python
  :lineno-start: 37
  :emphasize-lines: 3-5

              {{3, 2, 1}: 'BOOM!!!'}

      def test_making_a_dictionary_w_a_dictionary_as_a_key(self):
          a_dictionary = {'key': 'value'}
          {a_dictionary: 'BOOM!!!'}


  # Exceptions Encountered

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: unhashable type: 'dict'

GREEN: make it pass
#################################################################################

I add assertRaises_

.. code-block:: python
  :lineno-start: 39
  :emphasize-lines: 3-4

      def test_making_a_dictionary_w_a_dictionary_as_a_key(self):
          a_dictionary = {'key': 'value'}
          with self.assertRaises(TypeError):
              {a_dictionary: 'BOOM!!!'}


  # Exceptions Encountered

the test passes. I cannot use dictionaries_, sets_ or :ref:`lists` as :ref:`keys<test_keys_of_a_dictionary>` in a dictionary_. They are not hashable_, which means they can change in their lifetime

----

*********************************************************************************
test_attributes_and_methods_of_dictionaries
*********************************************************************************

RED: make it fail
#################################################################################

I add a new test with the dir_ :ref:`function<functions>` to see the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of dictionaries_

.. code-block:: python
  :lineno-start: 42
  :emphasize-lines: 4-7

              {a_dictionary: 'BOOM!!!'}

      def test_attributes_and_methods_of_dictionaries(self):
          self.assertEqual(
              dir(dict),
              []
          )


  # Exceptions Encountered

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: ['__class__', '__class_getitem__', '__cont[530 chars]ues'] != []

It also gives me a message about how to show the full difference between the two :ref:`lists`

.. code-block:: python

  Diff is 720 characters long. Set self.maxDiff to None to see it.

maxDiff_ is a :ref:`class attribute<test_attribute_error_w_class_attributes>` that is used to set the maximum length of differences between 2 items that the terminal_ shows

GREEN: make it pass
#################################################################################

* I move the terminal_ to right side of the screen
* I add maxDiff_ to the test

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2

        def test_attributes_and_methods_of_dictionaries(self):
            self.maxDiff = None
            self.assertEqual(
                dir(dict),
                []
            )

  the terminal_ shows the full difference between the two :ref:`lists`. I copy and paste the expected values from the terminal_ then use `find and replace`_ to remove the extra characters

  .. note::

    results can be different because of the Python_ version.

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 6-51

        def test_attributes_and_methods_of_dictionaries(self):
            self.maxDiff = None
            self.assertEqual(
                dir(dict),
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

  the test passes

* I copy the names that do NOT have double underscores (__) and paste them below the test to make a TODO list that I use to test what I can do with dictionaries_

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 7-17

                    'update',
                    'values'
                ]
            )


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

  the terminal still shows green

* I move the terminal_ back to the bottom of the screen

----

*********************************************************************************
test_clear_empties_a_dictionary
*********************************************************************************

RED: make it fail
#################################################################################

* I add a test for the first :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 6-8

                    'update',
                    'values'
                ]
            )

        def test_clear(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.clear())


    'clear',
    'copy',

  the terminal_ shows green. The clear_ :ref:`method<functions>` returns :ref:`None`

* I add an :ref:`assertion<AssertionError>` to see what clear_ did to the dictionary_

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 4

        def test_clear(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.clear())
            self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {} != {'key': 'value'}

  the clear_ :ref:`method<functions>` emptied the dictionary_, :ref:`same as it does with lists<test_clear_empties_a_list>`

GREEN: make it pass
#################################################################################

I change the values to match

.. code-block:: python
  :lineno-start: 98
  :emphasize-lines: 4

      def test_clear(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.clear())
          self.assertEqual(a_dictionary, {})

the test passes

REFACTOR: make it better
#################################################################################

* I rename the test

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 1

        def test_clear_empties_a_dictionary(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.clear())
            self.assertEqual(a_dictionary, {})


    'clear',
    'copy',

* I remove clear_ from the TODO list

  .. code-block:: python
    :lineno-start: 104

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

RED: make it fail
#################################################################################

I add a test for the next :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 101
  :emphasize-lines: 3-5

          self.assertEqual(a_dictionary, {})

      def test_copy(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.copy())


  'copy',
  'fromkeys',

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: {'key': 'value'} is not None

this :ref:`method<functions>` returns a copy of the dictionary_, :ref:`same as with lists<test_copy_a_list>`

GREEN: make it pass
#################################################################################

I add the value to the :ref:`assertion<AssertionError>`

.. code-block:: python
  :lineno-start: 103
  :emphasize-lines: 3-6

      def test_copy(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(
              a_dictionary.copy(),
              {'key': 'value'}
          )

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: {'key': 'value'} is not None : {'key': 'value'}

I change assertIsNone_ to assertEqual_

.. code-block:: python
  :lineno-start: 103
  :emphasize-lines: 3

      def test_copy(self):
          a_dictionary = {'key': 'value'}
          self.assertEqual(
              a_dictionary.copy(),
              {'key': 'value'}
          )

the test passes

REFACTOR: make it better
#################################################################################

* I rename the test

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 1

        def test_copy_a_dictionary(self):
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                a_dictionary.copy(),
                {'key': 'value'}
            )


    'copy',
    'fromkeys',

* I remove copy_ from the TODO list

  .. code-block:: python
    :lineno-start: 111

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

RED: make it fail
#################################################################################

I add a test for the next :ref:`method<functions>` from the TODO list

.. code-block:: python
  :lineno-start: 107
  :emphasize-lines: 4-6

              {'key': 'value'}
          )

      def test_fromkeys(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.fromkeys())


  'fromkeys',

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: fromkeys expected at least 1 argument, got 0

GREEN: make it pass
#################################################################################

* I pass a value to the call

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 3

        def test_fromkeys(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.fromkeys(0))

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'int' object is not iterable

* I change the value to a tuple_

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.fromkeys((0, 1)))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {0: None, 1: None} is not None

  the fromkeys_ :ref:`method<functions>` returns a dictionary_ that uses the values in the iterable_ as :ref:`keys<test_keys_of_a_dictionary>` with default values of :ref:`None`

* I add the dictionary_ as an expectation

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 3-6

        def test_fromkeys(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.fromkeys((0, 1)),
                {0: None, 1: None}
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {0: None, 1: None} is not None : {0: None, 1: None}

* I change assertIsNone_ to assertEqual_

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 1

            self.assertEqual(
                a_dictionary.fromkeys((0, 1)),
                {0: None, 1: None}
            )

  the test passes

REFACTOR: make it better
#################################################################################

* I add another `assert method`_ to see what happens to the first dictionary_ in the test

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 7

        def test_fromkeys(self):
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                a_dictionary.fromkeys((0, 1)),
                {0: None, 1: None}
            )
            self.assertEqual(a_dictionary, {})

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'key': 'value'} != {}

  the dictionary_ did not change

* I remove the last line I added
* I change the call fromkeys_ to use the dict_ :ref:`class<classes>` instead

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 4

        def test_fromkeys(self):
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                dict.fromkeys((0, 1)),
                {0: None, 1: None}
            )


    'fromkeys',

  the test is still green

* I remove ``a_dictionary`` since it is not used

  .. code-block:: python
    :lineno-start: 110

        def test_fromkeys(self):
            self.assertEqual(
                dict.fromkeys((0, 1)),
                {0: None, 1: None}
            )


    'fromkeys',

  still green

* the dictionary_ made with the fromkeys_ :ref:`method<functions>` has :ref:`None` as the default values. When I called the :ref:`method<functions>` without inputs the terminal_ showed :ref:`TypeError`

  .. code-block:: shell

    TypeError: fromkeys expected at least 1 argument, got 0

  I add a second input to the call to see what happens

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 2

            self.assertEqual(
                dict.fromkeys((0, 1), None),
                {0: None, 1: None}
            )

  the terminal_ still shows green

* I change the second input expecting a failure

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 2

            self.assertEqual(
                dict.fromkeys((0, 1), 'default'),
                {0: None, 1: None}
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {0: 'default', 1: 'default'} != {0: None, 1: None}

  I change the values to match

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 2-3

            self.assertEqual(
                dict.fromkeys((0, 1), 'default'),
                {0: 'default', 1: 'default'}
            )

  the test is green again. This is like a dict_ comprehension because it made a dictionary_ using the items from the iterable_ as :ref:`keys<test_keys_of_a_dictionary>`

* I rename the test

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 1

        def test_fromkeys_makes_a_dictionary_from_an_iterable(self):
            self.assertEqual(
                dict.fromkeys((0, 1), 'default'),
                {0: 'default', 1: 'default'}
            )


    'fromkeys',
    'get',

* I remove fromkeys_ from the TODO list

  .. code-block:: python
    :lineno-start: 117

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

RED: make it fail
#################################################################################

I add a test for the get_ :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 107
  :emphasize-lines: 4-6

              {0: 'default', 1: 'default'}
          )

      def test_get(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.get())


  'get',

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: get expected at least 1 argument, got 0

GREEN: make it pass
#################################################################################

I add a value to the call

.. code-block:: python
  :lineno-start: 118
  :emphasize-lines: 1

          self.assertIsNone(a_dictionary.get(0))

the test passes

REFACTOR: make it better
#################################################################################

* the get_ :ref:`method<functions>` also expected at least 1 argument, I add :ref:`None` to the call

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.get(0, None))

  the terminal_ still shows green

* I change the second argument expecting a failure

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.get(0, 'default'))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'default' is not None

* I add the expectation

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 3-6

        def test_get(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.get(0, 'default'),
                'default'
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'default' is not None : default

* I change assertIsNone_ to assertEqual_

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 1

            self.assertEqual(
                a_dictionary.get(0, 'default'),
                'default'
            )

  the test passes

* I change ``0`` in the call to get_ to be more descriptive

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 2

            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                'default'
            )

  the test is still green

* I want to see what happens when I use the get_ :ref:`method<functions>` with a :ref:`key<test_keys_of_a_dictionary>` that is in the dictionary_, I add another :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 5-8

            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                'default'
            )
            self.assertEqual(
                a_dictionary.get('key', 'default'),
                'default'
            )


    'get',

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'value' != 'default'

  I get ``'value'`` back. I change the expectation to match

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 3

            self.assertEqual(
                a_dictionary.get('key', 'default'),
                'value'
            )

  the test passes.

  The get_ :ref:`method<functions>` has a :ref:`condition<booleans>`

  - When the :ref:`key<test_keys_of_a_dictionary>` is NOT in the dictionary_, it returns the default argument
  - When the :ref:`key<test_keys_of_a_dictionary>` is in the dictionary_, it returns its :ref:`value<test_values_of_a_dictionary>`.

* I change the name of the test

  .. code-block:: python
    :lineno-start: 116
    :emphasize-lines: 1

        def test_get_value_of_a_key_in_a_dictionary(self):
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                'default'
            )
            self.assertEqual(
                a_dictionary.get('key', 'default'),
                'value'
            )


    'get',

  the test is still green

* I remove get_ from the TODO list

  .. code-block:: python
    :lineno-start: 128

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

RED: make it fail
#################################################################################

I add the next test from the TODO list

.. code-block:: python
  :lineno-start: 124

              'value'
          )

      def test_items(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.items())


  'items',

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: dict_items([('key', 'value')]) is not None

GREEN: make it pass
#################################################################################

* I copy the ``dict_items`` :ref:`object<classes>` from the terminal_ and paste it as the expectation

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 1-4

            self.assertIsNone(
                a_dictionary.items(),
                dict_items([('key', 'value')])
            )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'dict_items' is not defined

  this new :ref:`object<classes>` has a :ref:`list<lists>` and I know how to work with :ref:`lists`

* I remove the stuff around the :ref:`list<lists>`

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 3

            self.assertIsNone(
                a_dictionary.items(),
                [('key', 'value')]
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: dict_items([('key', 'value')]) is not None : [('key', 'value')]

* I pass the call to the items_ :ref:`method<functions>` to the :ref:`list<lists>` constructor_ to see if it is iterable_

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 2

            self.assertIsNone(
                list(a_dictionary.items()),
                [('key', 'value')]
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: [('key', 'value')] is not None : [('key', 'value')]

  the values are the same

* I change assertIsNone_ to assertEqual_

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 1

            self.assertEqual(
                list(a_dictionary.items()),
                [('key', 'value')]
            )

  the test passes.

  This works because the items_ :ref:`method<functions>` returns an iterable_ of the key-value pairs of the dictionary_. The ``dict_items`` :ref:`object<classes>` is iterable_

REFACTOR: make it better
#################################################################################

* I add another key-value pair to the dictionary_ to see what the :ref:`method<functions>` does when there is more than one

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 2-5

        def test_items(self):
            a_dictionary = {
                'key1': 'value1',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                list(a_dictionary.items()),
                [('key', 'value')]
            )


    'items',

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [('key1', 'value1'), ('keyN', [0, 1, 2, 'n'])] != [('key', 'value')]

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 132
    :emphasize-lines: 3-6

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
    :lineno-start: 127
    :emphasize-lines: 1

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


    'items',

* I remove items_ from the TODO list

  .. code-block:: python
    :lineno-start: 141

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

RED: make it fail
#################################################################################

I add a new test

.. code-block:: python
  :lineno-start: 136
  :emphasize-lines: 5-7

                  ('keyN', [0, 1, 2, 'n']),
              ]
          )

      def test_keys(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.keys())


  'keys',

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: dict_keys(['key']) is not None

this looks like the error in :ref:`test_items_returns_iterable_of_key_value_pairs_of_a_dictionary`

GREEN: make it pass
#################################################################################

* I copy the ``dict_keys`` :ref:`object<classes>` from the terminal_ and paste it as the expectation

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 3-6

        def test_keys(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.keys(),
                dict_keys(['key'])
            )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'dict_keys' is not defined

  the ``dict_keys`` :ref:`object<classes>` contains a :ref:`list<lists>`

* I use the :ref:`list<lists>` in the ``dict_keys`` :ref:`object<classes>` as the expectation instead

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 5

        def test_keys(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.keys(),
                ['key']
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: dict_keys(['key']) is not None : ['key']

* I pass the call to the keys_ :ref:`method<functions>` to the :ref:`list<lists>` constructor_ to see if ``dict_keys`` is iterable_

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 2

            self.assertIsNone(
                list(a_dictionary.keys()),
                ['key']
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: ['key'] is not None : ['key']

  I change assertIsNone_ to assertEqual_

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 1

            self.assertEqual(
                list(a_dictionary.keys()),
                ['key']
            )

  the test passes

REFACTOR: make it better
#################################################################################

* I add another :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to the dictionary_ to see what the keys_ :ref:`method<functions>` returns when there are multiple

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 2-5

        def test_keys(self):
            a_dictionary = {
                'key1': 'value1',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                list(a_dictionary.keys()),
                ['key']
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['key1', 'keyN'] != ['key']

  I change the expectation to match

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 3

            self.assertEqual(
                list(a_dictionary.keys()),
                ['key1', 'keyN']
            )

  the test passes

* I change the name of the test

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 1

        def test_keys_of_a_dictionary(self):
            a_dictionary = {
                'key1': 'value1',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                list(a_dictionary.keys()),
                ['key1', 'keyN']
            )


    'keys',

* I remove keys_ from the TODO list

  .. code-block:: python
    :lineno-start: 151

    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

----

*********************************************************************************
test_pop_removes_given_key_from_a_dictionary_and_returns_its_value
*********************************************************************************

RED: make it fail
#################################################################################

I wonder if the next :ref:`method<functions>` is the same as the one in :ref:`test_pop_removes_and_returns_last_item_from_a_list`, I add a test for it

.. code-block:: python

  def test_keys_of_a_dictionary(self):
      ...

  def test_pop(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.pop())

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: pop expected at least 1 argument, got 0

this pop_ :ref:`method<functions>` is different from the one in :ref:`lists`

GREEN: make it pass
#################################################################################

* I pass a value to the call

  .. code-block:: python

    self.assertIsNone(a_dictionary.pop(0))

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 0

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_dictionaries.py``

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # KeyError

* I remove the things around the call and change the value given to be more descriptive

  .. code-block:: python

    a_dictionary = {'key': 'value'}
    a_dictionary.pop('not in dictionary')

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'not in dictionary'

  I add assertRaises_

  .. code-block:: python

    a_dictionary = {'key': 'value'}

    with self.assertRaises(KeyError):
        a_dictionary.pop('not in dictionary')

  the test passes, calling the pop_ :ref:`method<functions>` with a key that is not in the dictionary_ raises a :ref:`KeyError <test_key_error>`

REFACTOR: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    a_dictionary = {'key': 'value'}
    self.assertIsNone(a_dictionary.pop('key'))

    with self.assertRaises(KeyError):
        a_dictionary.pop('not in dictionary')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'value' is not None

  the pop_ :ref:`method<functions>` returns the value of the given key from the dictionary_. I add the expectation

  .. code-block:: python

    self.assertIsNone(a_dictionary.pop('key'), 'value')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'value' is not None : value

  I change assertIsNone_ to assertEqual_

  .. code-block:: python

    self.assertEqual(a_dictionary.pop('key'), 'value')

  the test passes

* I add another :ref:`assertion<AssertionError>` to see what the :ref:`method<functions>` did to the dictionary_

  .. code-block:: python

    self.assertEqual(a_dictionary.pop('key'), 'value')
    self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {} != {'key': 'value'}

  pop_ :ref:`method<functions>` removes the :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` and returns the value of the given key from the dictionary_. I change the expectation to match

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

RED: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_pop_removes_given_key_from_a_dictionary_and_returns_its_value(self):
      ...

  def test_pop_item(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.popitem())

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: ('key', 'value') is not None

the popitem_ :ref:`method<functions>` returns the :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` as a tuple_

GREEN: make it pass
#################################################################################

I add the value from the terminal_ as an expectation

.. code-block:: python

  self.assertIsNone(a_dictionary.popitem(), ('key', 'value'))

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: ('key', 'value') is not None : ('key', 'value')

I change assertIsNone_ to assertEqual_

.. code-block:: python

  self.assertEqual(a_dictionary.popitem(), ('key', 'value'))

the test passes

REFACTOR: make it better
#################################################################################

* I want to know what the popitem_ :ref:`method<functions>` did to the dictionary_

  .. code-block:: python

    self.assertEqual(a_dictionary.popitem(), ('key', 'value'))
    self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {} != {'key': 'value'}

  popitem_ removes and returns the :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` from the dictionary_

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

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ('keyN', [0, 1, 2, 'n']) != ('key', 'value')

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(a_dictionary.popitem(), ('keyN', [0, 1, 2, 'n']))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'key1': 'value1'} != {'key': 'value'}

  I change the value to match

  .. code-block:: python

    self.assertEqual(a_dictionary, {'key1': 'value1'})

  the test passes

* I add another call to the :ref:`method<functions>`

  .. code-block:: python

    self.assertEqual(a_dictionary, {'key1': 'value1'})
    self.assertEqual(a_dictionary.popitem(), ('keyN', [0, 1, 2, 'n']))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Tuples differ: ('key1', 'value1') != ('keyN', [0, 1, 2, 'n'])

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_dictionary.popitem(), ('key1', 'value1'))

  the test passes. popitem_ removes and returns the last :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` from a dictionary_

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

RED: make it fail
#################################################################################

I add a test

.. code-block:: python

  def test_setdefault(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.setdefault())

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: setdefault expected at least 1 argument, got 0

GREEN: make it pass
#################################################################################

I pass a value in the call

.. code-block:: python

  self.assertIsNone(a_dictionary.setdefault(0))

the test passes

REFACTOR: make it better
#################################################################################

* I add an :ref:`assertion<AssertionError>` to see what it did to the dictionary_

  .. code-block:: python

    self.assertIsNone(a_dictionary.setdefault(0))
    self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

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

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

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

* I add an :ref:`assertion<AssertionError>` to see what happens when the :ref:`key<test_keys_of_a_dictionary>` is already in the dictionary_

  .. code-block:: python

    self.assertIsNone(a_dictionary.setdefault('new_key'))
    self.assertIsNone(a_dictionary.setdefault('key'))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'value' is not None

  setdefault_ returns the value for a key in a dictionary_ when the :ref:`key<test_keys_of_a_dictionary>` is in the dictionary_. I add the value to the :ref:`assertion<AssertionError>`

  .. code-block:: Python

    self.assertIsNone(a_dictionary.setdefault('key'), 'value')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'value' is not None : value

  I change assertIsNone_ to assertEqual_

  .. code-block:: python

    self.assertEqual(a_dictionary.setdefault('key'), 'value')

  the test passes

* It looks like setdefault_ has a condition where it sets a default value when the :ref:`key<test_keys_of_a_dictionary>` is not in the dictionary_ and returns the value when the :ref:`key<test_keys_of_a_dictionary>` is in it. I change the first :ref:`assertion<AssertionError>` to find out

  .. code-block:: python

    self.assertIsNone(a_dictionary.setdefault('new_key', None))

  the terminal_ still shows green. I change the given default value expecting a failure

  .. code-block:: python

    self.assertIsNone(a_dictionary.setdefault('new_key', 'default'))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'default' is not None

  I add the expected value

  .. code-block:: python

    self.assertIsNone(a_dictionary.setdefault('new_key', 'default'), 'default')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'default' is not None : default

  I change assertIsNone_ to assertEqual_

  .. code-block:: python

    self.assertEqual(a_dictionary.setdefault('new_key', 'default'), 'default')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

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

  the terminal_ still shows green. setdefault_ adds a given key to the dictionary_ with a given default value and returns the default value if the :ref:`key<test_keys_of_a_dictionary>` is not in the dictionary_. It returns the value for a key that is already in the dictionary_

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

RED: make it fail
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

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'key': 'value'} != {}

  the dictionary_ stayed the same

GREEN: make it pass
#################################################################################

I change the values in the expectation to match the terminal_

.. code-block:: python

  self.assertEqual(a_dictionary, {'key': 'value'})

the test passes

REFACTOR: make it better
#################################################################################

* I add a value to the call to see what happens

  .. code-block:: python

    self.assertIsNone(a_dictionary.update(0))

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'int' object is not iterable

  I change the value to a tuple_

  .. code-block:: python

    self.assertIsNone(a_dictionary.update((0, 1)))

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: cannot convert dictionary update sequence element #0 to a sequence

  I had this same error message in :ref:`test_making_a_dictionary`. I try a keyword argument

  .. code-block:: python

    self.assertIsNone(a_dictionary.update(new_key='new value'))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'key': 'value', 'new_key': 'new value'} != {'key': 'value'}

  I add the new :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to the :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(
        a_dictionary,
        {
            'key': 'value',
            'new_key': 'new value'
        }
    )

  the test passes

* I add an :ref:`assertion<AssertionError>` to see what happens if I give a key that is already in the dictionary_

  .. code-block:: python

    self.assertIsNone(a_dictionary.update(new_key='new value'))
    self.assertIsNone(a_dictionary.update(key='updated value'))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

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

* since the update_ :ref:`method<functions>` takes :ref:`keyword arguments<test_functions_w_keyword_arguments>` it means I should be able to give it a dictionary_ as input. I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertIsNone(a_dictionary.update({'another_key': 'another_value'}))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'key': 'updated value', 'new_key': 'new value', 'another_key': 'another_value'} != {'key': 'updated value', 'new_key': 'new value'}

  the update_ :ref:`method<functions>` adds the :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`s from the given dictionary_ to the existing one. I change the expectation to match

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

RED: make it fail
#################################################################################

I add a test for the last :ref:`method<functions>`

.. code-block:: python

  def test_update_a_dictionary(self):
      ...

  def test_values(self):
      a_dictionary = {'key': 'value'}
      self.assertIsNone(a_dictionary.values())

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: dict_values(['value']) is not None

this is like :ref:`test_items_returns_iterable_of_key_value_pairs_of_a_dictionary` and  :ref:`test_keys_of_a_dictionary`

GREEN: make it pass
#################################################################################

I add the expected value

.. code-block:: python

  self.assertIsNone(a_dictionary.values, dict_values(['value']))

the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: shell

  NameError: name 'dict_values' is not defined

I use the :ref:`list<lists>` in the ``dict_values`` :ref:`object<classes>`

.. code-block:: python

  self.assertIsNone(a_dictionary.values(), ['value'])

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: dict_values(['value']) is not None : ['value']

I change assertIsNone_ to assertEqual_

.. code-block:: python

  self.assertEqual(a_dictionary.values(), ['value'])

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: dict_values(['value']) != ['value']

I pass the call to the :ref:`list<lists>` constructor_

.. code-block:: python

  self.assertEqual(list(a_dictionary.values()), ['value'])

the test passes

REFACTOR: make it better
#################################################################################

* I change the dictionary_

  .. code-block:: python

    a_dictionary = {
        'key1': 'value1',
        'keyN': [0, 1, 2, 'n'],
    }

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

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

The `KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ is an important :ref:`Exception<errors>` to know when working with a dictionary_

RED: make it fail
#################################################################################

I add a test for getting the value of a key that is in a dictionary_

.. code-block:: python

    def test_values_of_a_dictionary(self):
        ...

    def test_key_error(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary['key'], '')

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 'value' != ''

I can get the value for a key in a dictionary_ by giving it in ``[]``, this is like :ref:`viewing items in a list <test_getting_items_of_a_list>`

GREEN: make it pass
#################################################################################

I change the value in the expectation to match the terminal_

.. code-block:: python

  self.assertEqual(a_dictionary['key'], 'value')

the test passes

REFACTOR: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_dictionary['key'], 'value')
    self.assertEqual(a_dictionary['not_in_dictionary'])

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

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

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

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

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

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

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

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

I ran tests for dictionaries_

* they contain :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`s
* any :ref:`object<classes>` can be used as values
* strings_, :ref:`booleans`, integers_, floats_ and tuples_ can be used as keys
* they can be represented with ``{}``
* they can be made with the dict_ constructor_

Would you like to :ref:`test How to make a Person?<how to make a person>`

----

:ref:`data structures: dictionaries: tests`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->