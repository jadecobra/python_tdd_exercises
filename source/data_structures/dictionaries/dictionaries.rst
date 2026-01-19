.. meta::
  :description: Master Python dictionaries with TDD! Learn :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`s, methods, and testing techniques in this hands-on guide. Start coding now!
  :keywords: Jacob Itegboje, Python dictionaries, Test-Driven Development, Python programming, data structures, unit testing, Python tutorial, coding guide

.. include:: ../../links.rst

.. _clear: https://docs.python.org/3/library/stdtypes.html#dict.clear
.. _clear method: clear_
.. _copy: https://docs.python.org/3/library/stdtypes.html#dict.copy
.. _copy method: copy_
.. _fromkeys: https://docs.python.org/3/library/stdtypes.html#dict.fromkeys
.. _fromkeys method: fromkeys_
.. _get: https://docs.python.org/3/library/stdtypes.html#dict.get
.. _get method: get_
.. _items: https://docs.python.org/3/library/stdtypes.html#dict.items
.. _items method: items_
.. _keys: https://docs.python.org/3/library/stdtypes.html#dict.keys
.. _keys method: keys_
.. _pop: https://docs.python.org/3/library/stdtypes.html#dict.pop
.. _pop method: pop_
.. _popitem: https://docs.python.org/3/library/stdtypes.html#dict.popitem
.. _popitem method: popitem_
.. _setdefault: https://docs.python.org/3/library/stdtypes.html#dict.setdefault
.. _setdefault method: setdefault_
.. _update: https://docs.python.org/3/library/stdtypes.html#dict.update
.. _update method: update_
.. _values: https://docs.python.org/3/library/stdtypes.html#dict.values

#################################################################################
dictionaries
#################################################################################

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: ../../code/tests/test_dictionaries.py
  :language: python
  :linenos:

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``dictionaries``
* I open ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` in the :ref:`editor<2 editors>`

  .. TIP:: Here is a quick way to open ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` if you are using `Visual Studio Code`_

    .. code-block:: python
      :emphasize-lines: 1

      code makePythonTdd.sh

    on `Windows`_ without `Windows Subsystem for Linux`_ use

    .. code-block:: python
      :emphasize-lines: 1

      code makePythonTdd.ps1

* I change everywhere I have ``list_comprehensions`` to the name of this project

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2, 3, 5, 12, 20

    #!/bin/bash
    mkdir dictionaries
    cd dictionaries
    mkdir src
    touch src/dictionaries.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestDictionaries(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError
    " > tests/test_dictionaries.py

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``makePythonTdd.ps1`` NOT ``makePythonTdd.sh``

    .. code-block:: PowerShell
      :linenos:
      :emphasize-lines: 1-2, 4, 11, 18

      mkdir dictionaries
      cd dictionaries
      mkdir src
      New-Item src/dictionaries.py
      mkdir tests
      New-Item tests/__init__.py

      "import unittest


      class TestDictionaries(unittest.TestCase):

          def test_failure(self):
              self.assertFalse(True)

      # Exceptions seen
      # AssertionError
      " | Out-File tests/test_dictionaries.py

* I run the program_ in the terminal_

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``makePythonTdd.ps1`` NOT ``makePythonTdd.sh``

    .. code-block:: python
      :emphasize-lines: 1

      ./makePythonTdd.ps1

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 10
    :emphasize-text: tests/test_dictionaries.py:7

    ================================= FAILURES =================================
    ____________________________ TestDictionaries.test_failure _____________________________

    self = <tests.test_dictionaries.TestDictionaries testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_dictionaries.py:7: AssertionError
    ================================ short test summary info =================================
    FAILED tests/test_dictionaries.py::TestDictionaries::test_failure - AssertionError: True is not false
    ============================ 1 failed in X.YZs =============================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_dictionaries.py:7`` to open it in the :ref:`editor<2 editors>`

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
test_making_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I change ``test_failure`` to ``test_making_a_dictionary`` then add an assertion_

.. code-block:: python
  :linenos:
  :emphasize-lines: 6-7

  import unittest


  class TestDictionaries(unittest.TestCase):

      def test_making_a_dictionary(self):
          self.assertEqual(dict(), None)

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: {} != None

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the expectation to match

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 2

      def test_making_a_dictionary(self):
          self.assertEqual(dict(), {})

the test passes. These are two ways to make an empty dictionary_

* ``dict()``
* curly braces - ``{}``

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>`, this time with input to make a dictionary_ with things in it

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

        def test_making_a_dictionary(self):
            self.assertEqual(dict(), {})
            self.assertEqual(dict(0), {})

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'int' object is not iterable

* I add :ref:`TypeError` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # TypeError

* I change the value given to ``dict()`` to a tuple_

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

            self.assertEqual(dict(), {})
            self.assertEqual(dict((0, 1)), {})

  the terminal_ shows :ref:`TypeError`

  .. code-block:: none

    TypeError: cannot convert dictionary update sequence element #0 to a sequence

* I try a :ref:`keyword argument<test_functions_w_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

            self.assertEqual(dict(), {})
            self.assertEqual(dict(key='value'), {})

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key': 'value'} != {}

* I change the expectation to match the values in the terminal_

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 1

            self.assertEqual(dict(key='value'), {'key': 'value'})

  the test passes.

:ref:`I know how to make a dictionary<test_making_a_dictionary>`. I used a string_ as a :ref:`key<test_keys_of_a_dictionary>` in this test. Next I test other :ref:`Python basic data types<data structures>` to see which ones I can use as :ref:`keys<test_keys_of_a_dictionary>`

----

*********************************************************************************
test_making_a_dictionary_w_none_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test to see if I can use :ref:`None<what is None?>` as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

.. code-block:: python
  :lineno-start: 8
  :emphasize-lines: 3-4

          self.assertEqual(dict(key='value'), {'key': 'value'})

      def test_making_a_dictionary_w_none_as_a_key(self):
          self.assertEqual({None: 'boom'}, {None: 'bap'})


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: {None: 'boom'} != {None: 'bap'}

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change ``'bap'`` to ``'boom'``

.. code-block:: python
  :lineno-start: 11
  :emphasize-lines: 1

          self.assertEqual({None: 'boom'}, {None: 'boom'})

the test passes. I can use strings_ and :ref:`None<what is None?>` as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`

----

*********************************************************************************
test_making_a_dictionary_w_a_boolean_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test to see if I can use a :ref:`boolean<what are booleans?>` as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 4-5

      def test_making_a_dictionary_w_none_as_a_key(self):
          self.assertEqual({None: 'boom'}, {None: 'boom'})

      def test_making_a_dictionary_w_a_boolean_as_a_key(self):
          self.assertEqual({False: 'boom'}, {False: 'bap'})


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: {False: 'boom'} != {False: 'bap'}

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change ``'bap'`` to ``'boom'``

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 1

          self.assertEqual({False: 'boom'}, {False: 'boom'})

the tests passes. I can use :ref:`False<test_what_is_false>` as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

I add an :ref:`assertion<what is an assertion?>` for the :ref:`other boolean<test_what_is_true>`

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 3-4

      def test_making_a_dictionary_w_a_boolean_as_a_key(self):
          self.assertEqual(
              {False: 'boom', True: 'bap'},
              {False: 'boom'}
          )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: {False: 'boom', True: 'bap'} != {False: 'boom'}

I add the new :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to the expectation

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 3

          self.assertEqual(
              {False: 'boom', True: 'bap'},
              {False: 'boom', True: 'bap'}
          )

the test passes. I can use strings_, :ref:`booleans<what are booleans?>` and :ref:`None<what is None?>` as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`

----

*********************************************************************************
test_making_a_dictionary_w_a_number_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test to see if I can use a number as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

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


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: {0: 'boom'} != {0: 'bap'}

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change ``'bap'`` to ``'boom'``

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 3

          self.assertEqual(
              {0: 'boom'},
              {0: 'boom'}
          )

the test passes. I can use an integer_ as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

I want to see if I can use a float_ as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`. I add a float_ to the dictionary_

.. code-block:: python
  :lineno-start: 19
  :emphasize-lines: 3

      def test_making_a_dictionary_w_a_number_as_a_key(self):
          self.assertEqual(
              {0: 'boom', 0.1: 'bap'},
              {0: 'boom'}
          )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: {0: 'boom', 0.1: 'bap'} != {0: 'boom'}

I add the new :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to the expectation

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 3

          self.assertEqual(
              {0: 'boom', 0.1: 'bap'},
              {0: 'boom', 0.1: 'bap'}
          )

the test passes. I can use strings_, numbers (floats_ and integers_), :ref:`booleans<what are booleans?>` and :ref:`None<what is None?>` as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`

----

*********************************************************************************
test_making_a_dictionary_w_a_tuple_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test to see if I can use a tuple_ (anything in parentheses (``()``), separated by a comma) as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 6-10

          self.assertEqual(
              {0: 'boom', 0.1: 'bap'},
              {0: 'boom', 0.1: 'bap'}
          )

      def test_making_a_dictionary_w_a_tuple_as_a_key(self):
          self.assertEqual(
              {(0, 1): 'boom'},
              {(0, 1): 'bap'}
          )


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: {(0, 1): 'boom'} != {(0, 1): 'bap'}

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change ``'bap'`` to ``'boom'``

.. code-block:: python
  :lineno-start: 26

          self.assertEqual(
              {(0, 1): 'boom'},
              {(0, 1): 'boom'}
          )

the test passes. I can use tuples_, strings_, numbers (floats_ and integers_), :ref:`booleans<what are booleans?>` and :ref:`None<what is None?>` as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`

----

*********************************************************************************
test_making_a_dictionary_w_a_list_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for :ref:`lists` (anything in square brackets (``[]``))

.. code-block:: python
  :lineno-start: 26
  :emphasize-lines: 6-9

          self.assertEqual(
              {(0, 1): 'boom'},
              {(0, 1): 'boom'}
          )

      def test_making_a_dictionary_w_a_list_as_a_key(self):
          self.assertEqual(
              {[0, 1]: 'boom'},
          )


  # Exceptions seen

the terminal_ shows :ref:`TypeError`

.. code-block:: python

  TypeError: unhashable type: 'list'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I remove the things around the new dictionary_ then change the :ref:`key<test_keys_of_a_dictionary>` and :ref:`value<test_values_of_a_dictionary>` for fun

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 3

        def test_making_a_dictionary_w_a_list_as_a_key(self):

            {[3, 2, 1]: 'BOOM!!!'}


  the terminal_ still shows :ref:`TypeError`

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2

        def test_making_a_dictionary_w_a_list_as_a_key(self):
            with self.assertRaises(TypeError):
                {[3, 2, 1]: 'BOOM!!!'}

  the test passes. I cannot use a :ref:`list<lists>` as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

----

*********************************************************************************
test_making_a_dictionary_w_a_set_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add another test with a set_ (single items in curly braces (``{}``)) as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

.. code-block:: python
  :lineno-start: 32
  :emphasize-lines: 4-5

          with self.assertRaises(TypeError):
              {[3, 2, 1]: 'BOOM!!!'}

      def test_making_a_dictionary_w_a_set_as_a_key(self):
          {{3, 2, 1}: 'BOOM!!!'}


  # Exceptions seen

the terminal_ shows :ref:`TypeError`

.. code-block:: python

  TypeError: unhashable type: 'set'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add assertRaises_ to handle the :ref:`Exception<errors>`

.. code-block:: python
  :lineno-start: 35
  :emphasize-lines: 2-3

      def test_making_a_dictionary_w_a_set_as_a_key(self):
          with self.assertRaises(TypeError):
              {{3, 2, 1}: 'BOOM!!!'}

the test is green again. I cannot use :ref:`lists` or sets_ as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`

----

*********************************************************************************
test_making_a_dictionary_w_a_dictionary_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add another test, this time for a dictionary_

.. code-block:: python
  :lineno-start: 36
  :emphasize-lines: 4-6

          with self.assertRaises(TypeError):
              {[3, 2, 1]: 'BOOM!!!'}

      def test_making_a_dictionary_w_a_dictionary_as_a_key(self):
          a_dictionary = {'key': 'value'}
          {a_dictionary: 'BOOM!!!'}


  # Exceptions seen

the terminal_ shows :ref:`TypeError`

.. code-block:: python

  TypeError: unhashable type: 'dict'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add assertRaises_

.. code-block:: python
  :lineno-start: 39
  :emphasize-lines: 3-4

      def test_making_a_dictionary_w_a_dictionary_as_a_key(self):
          a_dictionary = {'key': 'value'}
          with self.assertRaises(TypeError):
              {a_dictionary: 'BOOM!!!'}


  # Exceptions seen

the test passes. I cannot use dictionaries_, sets_ or :ref:`lists` as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`. They are not hashable_, which means they can change in their lifetime

----

*********************************************************************************
test_attributes_and_methods_of_dictionaries
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test with the `dir built-in function`_ to see the :ref:`attributes<AttributeError>` and :ref:`methods<what is a function?>` of dictionaries_

.. code-block:: python
  :lineno-start: 41
  :emphasize-lines: 4-8

          with self.assertRaises(TypeError):
              {a_dictionary: 'BOOM!!!'}

      def test_attributes_and_methods_of_dictionaries(self):
          self.assertEqual(
              dir(dict),
              []
          )


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: Lists differ: ['__class__', '__class_getitem__', '__cont[530 chars]ues'] != []

It also gives me a message about how to show the full difference between the two :ref:`lists`

.. code-block:: python

  Diff is 720 characters long. Set self.maxDiff to None to see it.

`unittest.TestCase.maxDiff`_ is a :ref:`class attribute<test_attribute_error_w_class_attributes>` that is used to set the maximum length of differences between 2 items that the terminal_ shows

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

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

  the terminal_ shows the full difference between the two :ref:`lists`.

* I copy (:kbd:`ctrl/command+c`) and paste (:kbd:`ctrl/command+v`) the expected values from the terminal_ then use `find and replace`_ to remove the extra characters

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


    # Exceptions seen

  the terminal_ still shows green

----

*********************************************************************************
test_clear_empties_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add a test for the first :ref:`method<what is a function?>`

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

  still green. The `clear method`_ returns :ref:`None<what is None?>`

* I add an :ref:`assertion<what is an assertion?>` to see what clear_ did to the dictionary_

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 4

        def test_clear(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.clear())
            self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {} != {'key': 'value'}

  the `clear method`_ emptied the dictionary_, :ref:`same as it does with lists<test_clear_empties_a_list>`

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the values to match

.. code-block:: python
  :lineno-start: 98
  :emphasize-lines: 4

      def test_clear(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.clear())
          self.assertEqual(a_dictionary, {})

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I change the name of the test

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 1

        def test_clear_empties_a_dictionary(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.clear())
            self.assertEqual(a_dictionary, {})


    'clear',

* I remove clear_ from the TODO list

  .. code-block:: python
    :lineno-start: 101

            self.assertEqual(a_dictionary, {})


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

:ref:`I know how to empty a dictionary<test_clear_empties_a_dictionary>`

----

*********************************************************************************
test_copy_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for the `copy method`_

.. code-block:: python
  :lineno-start: 101
  :emphasize-lines: 3-5

          self.assertEqual(a_dictionary, {})

      def test_copy(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.copy())


  'copy',
  'fromkeys',

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: {'key': 'value'} is not None

this :ref:`method<what is a function?>` returns a copy of the dictionary_, :ref:`same as with lists<test_copy_a_list>`

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the value to the :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :lineno-start: 103
  :emphasize-lines: 3-6

      def test_copy(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(
              a_dictionary.copy(),
              {'key': 'value'}
          )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

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

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I change the name of the test

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
    :lineno-start: 105

            self.assertEqual(
                a_dictionary.copy(),
                {'key': 'value'}
            )


    'fromkeys',
    'get',
    'items',
    'keys',
    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

:ref:`I know how to copy a dictionary<test_copy_a_dictionary>`

----

*********************************************************************************
test_fromkeys_makes_a_dictionary_from_an_iterable
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for the next :ref:`method<what is a function?>` from the TODO list

.. code-block:: python
  :lineno-start: 105
  :emphasize-lines: 6-8

          self.assertEqual(
              a_dictionary.copy(),
              {'key': 'value'}
          )

      def test_fromkeys(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.fromkeys())


  'fromkeys',

the terminal_ shows :ref:`TypeError`

.. code-block:: python

  TypeError: fromkeys expected at least 1 argument, got 0

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I pass a value to the call

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 3

        def test_fromkeys(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.fromkeys(0))

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'int' object is not iterable

* I change the value to a tuple_

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.fromkeys((0, 1)))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {0: None, 1: None} is not None

  the `fromkeys method`_ returns a dictionary_ that uses the values in the :ref:`iterable<what is an iterable?>` as :ref:`keys<test_keys_of_a_dictionary>` with default values of :ref:`None<what is None?>`. It reminds me of a :ref:`list comprehension<list comprehensions>`

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

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

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another `assert method`_ to see what happened to ``a_dictionary``

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key': 'value'} != {}

  the dictionary_ did not change

* I remove the last line I added
* then change the call to fromkeys_ to use the `dict class`_

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

* the dictionary_ made with the `fromkeys method`_ has :ref:`None<what is None?>` as the default values. When I called the :ref:`method<what is a function?>` without inputs the terminal_ showed :ref:`TypeError`

  .. code-block:: python

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {0: 'default', 1: 'default'} != {0: None, 1: None}

* I change the values in the expectation to match

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 3

            self.assertEqual(
                dict.fromkeys((0, 1), 'default'),
                {0: 'default', 1: 'default'}
            )

  the test is green again. This is like a dict_ comprehension because it made a dictionary_ using the items from the :ref:`iterable<what is an iterable?>` as :ref:`keys<test_keys_of_a_dictionary>`

* I change the name of the test

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
    :lineno-start: 111

            self.assertEqual(
                dict.fromkeys((0, 1), 'default'),
                {0: 'default', 1: 'default'}
            )


    'get',
    'items',
    'keys',
    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

:ref:`I know how to make a dictionary from an iterable<tesT_fromkeys_makes_a_dictionary_from_an_iterable>`

----

*********************************************************************************
test_get_value_of_a_key_in_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for the `get method`_

.. code-block:: python
  :lineno-start: 111
  :emphasize-lines: 6-8

          self.assertEqual(
              dict.fromkeys((0, 1), 'default'),
              {0: 'default', 1: 'default'}
          )

      def test_get(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.get())


  'get',

the terminal_ shows :ref:`TypeError`

.. code-block:: python

  TypeError: get expected at least 1 argument, got 0

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a value to the call

.. code-block:: python
  :lineno-start: 118
  :emphasize-lines: 1

          self.assertIsNone(a_dictionary.get(0))

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* the `get method`_ also expected at least 1 argument, I add :ref:`None<what is None?>` to the call

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'default' is not None

* I add the expectation

  .. code-block:: python
    :lineno-start: 116
    :emphasize-lines: 3-6

        def test_get(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.get(0, 'default'),
                'default'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

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

* I change ``0`` in the call to be clearer

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 2
    :emphasize-text: not_in_dictionary

            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                'default'
            )

  the test is still green

* I want to see what happens when I use the `get method`_ with a :ref:`key<test_keys_of_a_dictionary>` that is in the dictionary_, I add another :ref:`assertion<what is an assertion?>`

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'value' != 'default'

  I get ``'value'`` back

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 3

            self.assertEqual(
                a_dictionary.get('key', 'default'),
                'value'
            )

  the test passes

  .. NOTE::

    The `get method`_ has a :ref:`condition<if statements>`

    - when the :ref:`key<test_keys_of_a_dictionary>` is NOT in the dictionary_, it returns the default argument
    - when the :ref:`key<test_keys_of_a_dictionary>` is in the dictionary_, it returns its :ref:`value<test_values_of_a_dictionary>`

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
    :lineno-start: 122

            self.assertEqual(
                a_dictionary.get('key', 'default'),
                'value'
            )


    'items',
    'keys',
    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

:ref:`I know how to get the value of a key that is in a dictionary<test_get_value_of_a_key_in_a_dictionary>`

----

*********************************************************************************
test_items_returns_iterable_of_key_value_pairs_of_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add the next test from the TODO list

.. code-block:: python
  :lineno-start: 122
  :emphasize-lines: 6-8

          self.assertEqual(
              a_dictionary.get('key', 'default'),
              'value'
          )

      def test_items(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.items())


  'items',

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: dict_items([('key', 'value')]) is not None

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I copy the ``dict_items`` :ref:`object<what is a class?>` from the terminal_ and paste  it as the expectation

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 2-5

            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.items(),
                dict_items([('key', 'value')])
            )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'dict_items' is not defined

  this new :ref:`object<what is a class?>` has a :ref:`list<lists>` and :ref:`I know how to work with lists<lists>`, just like :ref:`dict_items<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 4
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # TypeError
    # NameError

* I remove the stuff around the :ref:`list<lists>`

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 3

            self.assertIsNone(
                a_dictionary.items(),
                [('key', 'value')]
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: dict_items([('key', 'value')]) is not None : [('key', 'value')]

* I pass the call to the `items method`_ to ``list()`` to see if it is :ref:`iterable<what is an iterable?>`

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 2

            self.assertIsNone(
                list(a_dictionary.items()),
                [('key', 'value')]
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

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

This works because the `items method`_ returns an :ref:`iterable<what is an iterable?>` of the key-value pairs of the dictionary_. The ``dict_items`` :ref:`object<what is a class?>` is :ref:`iterable<what is an iterable?>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another key-value pair to the dictionary_ to see what the :ref:`method<what is a function?>` does when there is more than one

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

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
    :lineno-start: 132

            self.assertEqual(
                list(a_dictionary.items()),
                [
                    ('key1', 'value1'),
                    ('keyN', [0, 1, 2, 'n']),
                ]
            )


    'keys',
    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

  all tests are still passing

:ref:`I know how to look at the key-value pairs in a dictionary as a list of tuples<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`

----

*********************************************************************************
test_keys_of_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test

.. code-block:: python
  :lineno-start: 132
  :emphasize-lines: 9-11

              self.assertEqual(
                  list(a_dictionary.items()),
                  [
                      ('key1', 'value1'),
                      ('keyN', [0, 1, 2, 'n']),
                  ]
              )

      def test_keys(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.keys())


  'keys',

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: dict_keys(['key']) is not None

this looks like the error in :ref:`test_items_returns_iterable_of_key_value_pairs_of_a_dictionary`

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I copy the ``dict_keys`` :ref:`object<what is a class?>` from the terminal_ and paste it as the expectation

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

  .. code-block:: python

    NameError: name 'dict_keys' is not defined

  the ``dict_keys`` :ref:`object<what is a class?>` has a :ref:`list<lists>`

* I use the :ref:`list<lists>` in the ``dict_keys`` :ref:`object<what is a class?>` as the expectation

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 5

        def test_keys(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.keys(),
                ['key']
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: dict_keys(['key']) is not None : ['key']

* I pass the call to the `keys method`_ to ``list()`` to see if ``dict_keys`` is :ref:`iterable<what is an iterable?>`

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 2

            self.assertIsNone(
                list(a_dictionary.keys()),
                ['key']
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

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

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to the dictionary_ to see what the `keys method`_ returns when there are multiple

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Lists differ: ['key1', 'keyN'] != ['key']

* I change the expectation to match

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
    :lineno-start: 145

            self.assertEqual(
                list(a_dictionary.keys()),
                ['key1', 'keyN']
            )


    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

:ref:`I know how to look at the keys in a dictionary<test_keys_of_a_dictionary>`

----

*********************************************************************************
test_pop_removes_given_key_from_a_dictionary_and_returns_its_value
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I wonder if the `pop method`_ of dictionaries_ behaves the same way as the :ref:`pop method of lists<test_pop_removes_and_returns_last_item_from_a_list>`. I add a test for it

.. code-block:: python
  :lineno-start: 145
  :emphasize-lines: 6-8

          self.assertEqual(
              list(a_dictionary.keys()),
              ['key1', 'keyN']
          )

      def test_pop(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.pop())


  'pop',

the terminal_ shows :ref:`TypeError`

.. code-block:: python

  TypeError: pop expected at least 1 argument, got 0

this `pop method`_ is different from the :ref:`pop method of lists<test_pop_removes_and_returns_last_item_from_a_list>`

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I pass a value to the call

  .. code-block:: python
    :lineno-start: 152
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.pop(0))

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: 0

* I add :ref:`KeyError<test_key_error>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 162
    :emphasize-lines: 5
    :emphasize-text: KeyError

    # Exceptions seen
    # AssertionError
    # TypeError
    # NameError
    # KeyError

* I remove the things around the call in the test and change the value given to be clearer

  .. code-block:: python
    :lineno-start: 150
    :emphasize-lines: 3
    :emphasize-text: not_in_dictionary

        def test_pop(self):
            a_dictionary = {'key': 'value'}
            a_dictionary.pop('not_in_dictionary')

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: 'not in dictionary'

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 150
    :emphasize-lines: 4-5

        def test_pop(self):
            a_dictionary = {'key': 'value'}

            with self.assertRaises(KeyError):
                a_dictionary.pop('not_in_dictionary')

  the test passes. When I call the `pop method`_ with a :ref:`key<test_keys_of_a_dictionary>` that is not in the dictionary_ it raises :ref:`KeyError<test_key_error>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* When I called the `pop method`_ without input, the terminal_ showed :ref:`TypeError`

  .. code-block:: python

    TypeError: pop expected at least 1 argument, got 0

  I add another :ref:`assertion<what is an assertion?>` to see what happens when I call it with 2 arguments

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 3

            with self.assertRaises(KeyError):
                a_dictionary.pop('not_in_dictionary')
            self.assertIsNone(a_dictionary.pop('not_in_dictionary', None))

  the test is still green

* I change the second argument, expecting a failure

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 1
    :emphasize-text: default

            self.assertIsNone(a_dictionary.pop('not_in_dictionary', 'default'))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'default' is not None

* I add the expectation

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 1-4

            self.assertIsNone(
                a_dictionary.pop('not_in_dictionary', 'default'),
                'default'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'default' is not None : default

* I change assertIsNone_ to assertEqual_

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 1

            self.assertEqual(
                a_dictionary.pop('not_in_dictionary', 'default'),
                'default'
            )

  the test passes

* I add another :ref:`assertion<what is an assertion?>` to see what happens when I call the `pop method`_ with a :ref:`key<test_keys_of_a_dictionary>` that is in the dictionary_

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 5-8

            self.assertEqual(
                a_dictionary.pop('not_in_dictionary', 'default'),
                'default'
            )
            self.assertEqual(
                a_dictionary.pop('key', 'default'),
                'default'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'value' != 'default'

  I get ``'value'`` back. The `pop method`_ returns the value of the given :ref:`key<test_keys_of_a_dictionary>` from the dictionary_

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 3

            self.assertEqual(
                a_dictionary.pop('key', 'default'),
                'value'
            )

  the test passes

* I add another :ref:`assertion<what is an assertion?>` to see what the `pop method`_ did to the dictionary_

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 5

            self.assertEqual(
                a_dictionary.pop('key', 'default'),
                'value'
            )
            self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {} != {'key': 'value'}

  the `pop method`_ removes the :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` and returns the :ref:`value<test_values_of_a_dictionary>` of the given :ref:`key<test_keys_of_a_dictionary>` from the dictionary_

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 163
    :emphasize-lines: 1

            self.assertEqual(a_dictionary, {})

  the test passes

* I change the name of the test

  .. code-block:: python
    :lineno-start: 150
    :emphasize-lines: 1

        def test_pop_removes_given_key_from_a_dictionary_and_returns_its_value(self):
            a_dictionary = {'key': 'value'}

            with self.assertRaises(KeyError):
                a_dictionary.pop('not_in_dictionary')
            self.assertEqual(
                a_dictionary.pop('not_in_dictionary', 'default'),
                'default'
            )
            self.assertEqual(
                a_dictionary.pop('key', 'default'),
                'value'
            )
            self.assertEqual(a_dictionary, {})


    'pop',

* I remove pop_ from the TODO list

  .. code-block:: python
    :lineno-start: 163

            self.assertEqual(a_dictionary, {})


    'popitem',
    'setdefault',
    'update',
    'values'

:ref:`I know how to remove a key and its value from a dictionary<test_pop_removes_given_key_from_a_dictionary_and_returns_its_value>`

----

*********************************************************************************
test_popitem_removes_and_returns_last_key_value_pair_from_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test for the next item in the TODO list

.. code-block:: python
  :lineno-start: 163
  :emphasize-lines: 3-5

          self.assertEqual(a_dictionary, {})

      def test_popitem(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.popitem())


  'popitem',

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: ('key', 'value') is not None

the `popitem method`_ returns the :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in the dictionary_ as a tuple_

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the value from the terminal_ as the expectation

.. code-block:: python
  :lineno-start: 166
  :emphasize-lines: 2-5

          a_dictionary = {'key': 'value'}
          self.assertIsNone(
              a_dictionary.popitem(),
              ('key', 'value')
          )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: ('key', 'value') is not None : ('key', 'value')

I change assertIsNone_ to assertEqual_

.. code-block::
  :lineno-start: 167
  :emphasize-lines: 1

          self.assertEqual(
              a_dictionary.popitem(),
              ('key', 'value')
          )

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>` to see what the `popitem method`_ did to the dictionary_

  .. code-block:: python
    :lineno-start: 167
    :emphasize-lines: 5

            self.assertEqual(
                a_dictionary.popitem(),
                ('key', 'value')
            )
            self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {} != {'key': 'value'}

  popitem_ removes and returns the :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` from the dictionary_

* I change the value to match

  .. code-block:: python
    :lineno-start: 171
    :emphasize-lines: 1

            self.assertEqual(a_dictionary, {})

  the test passes

* this operation does not take input, I change the dictionary_ to see what happens

  .. code-block:: python
    :lineno-start: 165
    :emphasize-lines: 2-5

        def test_popitem(self):
            a_dictionary = {
                'key1': 'value1',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                a_dictionary.popitem(),
                ('key', 'value')
            )
            self.assertEqual(a_dictionary, {})

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('keyN', [0, 1, 2, 'n']) != ('key', 'value')

  popitem_ removes and returns the last :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` from a dictionary_

* I change the expectation in the first assertEqual_ to match

  .. code-block:: python
    :lineno-start: 170
    :emphasize-lines: 3

            self.assertEqual(
                a_dictionary.popitem(),
                ('keyN', [0, 1, 2, 'n'])
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key1': 'value1'} != {'key': 'value'}

* I change the value in the second assertEqual_ to match

  .. code-block:: python
    :lineno-start: 174
    :emphasize-lines: 1

            self.assertEqual(a_dictionary, {'key1': 'value1'})

  the test passes

* I change the name of the test

  .. code-block:: python
    :lineno-start: 165
    :emphasize-lines: 1

        def test_popitem_removes_and_returns_last_key_value_pair_from_a_dictionary(self):
            a_dictionary = {
                'key1': 'value1',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                a_dictionary.popitem(),
                ('keyN', [0, 1, 2, 'n'])
            )
            self.assertEqual(a_dictionary, {'key1': 'value1'})


    'popitem',

* I remove popitem_ from the TODO list

  .. code-block:: python
    :lineno-start: 174

            self.assertEqual(a_dictionary, {'key1': 'value1'})


    'setdefault',
    'update',
    'values'

:ref:`I know how to remove the last key-value pair from a dictionary<test_popitem_removes_and_returns_last_key_value_pair_from_a_dictionary>`

----

*********************************************************************************
test_setdefault_adds_given_key_to_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for the `setdefault method`_

.. code-block:: python
  :lineno-start: 174
  :emphasize-lines: 3-5

          self.assertEqual(a_dictionary, {'key1': 'value1'})

      def test_setdefault(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.setdefault())


  'setdefault',

the terminal_ shows :ref:`TypeError`

.. code-block:: python

  TypeError: setdefault expected at least 1 argument, got 0

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I pass a value in the call

.. code-block:: python
  :lineno-start: 178
  :emphasize-lines: 1

          self.assertIsNone(a_dictionary.setdefault(0))

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* The error message showed that the :ref:`method<what is a function?>` expects at least 1 argument, I add a second argument

  .. code-block:: python
    :lineno-start: 178
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.setdefault(0, None))

  the test is still green

* I change the second argument expecting a failure

  .. code-block:: python
    :lineno-start: 178
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.setdefault(0, 'default'))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'default' is not None

* I add the expectation

  .. code-block:: python
    :lineno-start: 177
    :emphasize-lines: 2-5

            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.setdefault(0, 'default'),
                'default'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'default' is not None : default

* I change assertIsNone_ to assertEqual_

  .. code-block:: python
    :lineno-start: 178
    :emphasize-lines: 1

            self.assertEqual(
                a_dictionary.setdefault(0, 'default'),
                'default'
            )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` to see what setdefault_ did to the dictionary_

  .. code-block:: python
    :lineno-start: 178
    :emphasize-lines: 5

            self.assertEqual(
                a_dictionary.setdefault(0, 'default'),
                'default'
            )
            self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key': 'value', 0: 'default'} != {'key': 'value'}

  setdefault_ adds the given :ref:`key<test_keys_of_a_dictionary>` to the dictionary_ with the default :ref:`value<test_values_of_a_dictionary>` and returns the default value

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 176
    :emphasize-lines: 7-13

        def test_setdefault(self):
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                a_dictionary.setdefault(0, 'default'),
                'default'
            )
            self.assertEqual(
                a_dictionary,
                {
                    'key': 'value',
                    0: 'default',
                }
            )

  the test passes

* I change the ``0`` given in the call to the `setdefault method`_ be clearer

  .. code-block:: python
    :lineno-start: 178
    :emphasize-lines: 2

            self.assertEqual(
                a_dictionary.setdefault('new_key', 'default'),
                'default'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key': 'value', 'new_key': 'default'} != {'key': 'value', 0: 'default'}

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 181
    :emphasize-lines: 5

            self.assertEqual(
                a_dictionary,
                {
                    'key': 'value',
                    'new_key': 'default',
                }
            )

  the test is green again

* I add an :ref:`assertion<what is an assertion?>` to see what happens when I use setdefault_ with a :ref:`key<test_keys_of_a_dictionary>` that is already in the dictionary_

  .. code-block:: python
    :lineno-start: 176
    :emphasize-lines: 7-10

        def test_setdefault(self):
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                a_dictionary.setdefault('new_key', 'default'),
                'default'
            )
            self.assertEqual(
                a_dictionary.setdefault('key', 'default'),
                'default'
            )
            self.assertEqual(
                a_dictionary,
                {
                    'key': 'value',
                    'new_key': 'default',
                }
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'value' != 'default'

  setdefault_ returns the :ref:`value<test_values_of_a_dictionary>` for a :ref:`key in a dictionary<test_keys_of_a_dictionary>` when the :ref:`key<test_keys_of_a_dictionary>` is in the dictionary_

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 182
    :emphasize-lines: 3

            self.assertEqual(
                a_dictionary.setdefault('key', 'default'),
                'value'
            )

  the test passes

  .. NOTE::

    setdefault_ has a :ref:`condition<if statements>`

    - when the :ref:`key<test_keys_of_a_dictionary>` is NOT in the dictionary_ it adds it with a default value of :ref:`None<what is None?>` and returns :ref:`None<what is None?>`
    - when the :ref:`key<test_keys_of_a_dictionary>` is NOT in the dictionary_ and I call setdefault_ with a second argument, it adds the :ref:`key<test_keys_of_a_dictionary>` to the dictionary_ with the second argument as the :ref:`value<test_values_of_a_dictionary>` and returns the second argument
    - when the :ref:`key<test_keys_of_a_dictionary>` is in the dictionary_ it returns its :ref:`value<test_values_of_a_dictionary>` from the dictionary_

* I change the name of the test

  .. code-block:: python
    :lineno-start: 176
    :emphasize-lines: 1

        def test_setdefault_adds_given_key_to_a_dictionary(self):
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                a_dictionary.setdefault('new_key', 'default'),
                'default'
            )
            self.assertEqual(
                a_dictionary.setdefault('key', 'default'),
                'value'
            )
            self.assertEqual(
                a_dictionary,
                {
                    'key': 'value',
                    'new_key': 'default',
                }
            )


    'setdefault',

* I remove setdefault_ from the TODO list

  .. code-block:: python
    :lineno-start: 186

            self.assertEqual(
                a_dictionary,
                {
                    'key': 'value',
                    'new_key': 'default',
                }
            )


    'update',
    'values'

:ref:`I know how to add a key with a default value to a dictionary<test_setdefault_adds_given_key_to_a_dictionary>`

----

*********************************************************************************
test_update_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add a test for the next :ref:`method<what is a function?>` from the TODO list

  .. code-block:: python
    :lineno-start: 186
    :emphasize-lines: 9-11

            self.assertEqual(
                a_dictionary,
                {
                    'key': 'value',
                    'new_key': 'default',
                }
            )

        def test_update(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.update())


    'update',

  the test is green. The `update method`_ returns :ref:`None<what is None?>`

* I add an :ref:`assertion<what is an assertion?>` to see what it did to the dictionary_

  .. code-block:: python
    :lineno-start: 194
    :emphasize-lines: 4

        def test_update(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.update())
            self.assertEqual(a_dictionary, {})

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key': 'value'} != {}

  the dictionary_ did not change

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the values in the expectation to match the terminal_

.. code-block:: python
  :lineno-start: 197
  :emphasize-lines: 1

          self.assertEqual(a_dictionary, {'key': 'value'})

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add a value to the call to the `update method`_ to see what happens

  .. code-block:: python
    :lineno-start: 194
    :emphasize-lines: 3

        def test_update(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.update(0))
            self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'int' object is not iterable

* I change the value to a tuple_

  .. code-block:: python
    :lineno-start: 196
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.update((0, 1)))

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: cannot convert dictionary update sequence element #0 to a sequence

  I had the same error message when I tried to :ref:`make a dictionary with things in it<test_making_a_dictionary>`

* I try a :ref:`keyword argument<test_functions_w_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 196
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.update(new_key=[0, 1, 2, 'n']))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key': 'value', 'new_key': [0, 1, 2, 'n']} != {'key': 'value'}

* I add the new :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to the expectation

  .. code-block:: python
    :lineno-start: 196
    :emphasize-lines: 2-8

            self.assertIsNone(a_dictionary.update(new_key=[0, 1, 2, 'n']))
            self.assertEqual(
                a_dictionary,
                {
                    'key': 'value',
                    'new_key': [0, 1, 2, 'n'],
                }
            )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` to see what happens when I give a :ref:`key<test_keys_of_a_dictionary>` that is already in the dictionary_

  .. code-block:: python
    :lineno-start: 194
    :emphasize-lines: 4

        def test_update(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.update(new_key=[0, 1, 2, 'n']))
            self.assertIsNone(a_dictionary.update(key='updated value'))
            self.assertEqual(

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key': 'updated value', 'new_key': [0, 1, 2, 'n']} != {'key': 'value', 'new_key': [0, 1, 2, 'n']}

  the `update method`_ changes the :ref:`value<test_values_of_a_dictionary>` for a :ref:`key<test_keys_of_a_dictionary>` that is already in a dictionary_

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 198
    :emphasize-lines: 4

            self.assertEqual(
                a_dictionary,
                {
                    'key': 'updated value',
                    'new_key': [0, 1, 2, 'n'],
                }
            )

  the test passes

* since the `update method`_ takes :ref:`keyword arguments<test_functions_w_keyword_arguments>`, I can give it a dictionary_ as input. I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 194
    :emphasize-lines: 5-7

        def test_update(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.update(new_key=[0, 1, 2, 'n']))
            self.assertIsNone(a_dictionary.update(key='updated value'))
            self.assertIsNone(a_dictionary.update(
                {'another_key': {0, 1, 2, 'n'}}
            ))
            self.assertEqual(

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key[14 chars]lue', 'new_key': [0, 1, 2, 'n'], 'another_key': {0, 1, 2, 'n'}} != {'key[14 chars]lue', 'new_key': [0, 1, 2, 'n']}

  I can use the `update method`_ to add :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` from one dictionary_ to another

* I change the expectation in the assertEqual_ to match

  .. code-block:: python
    :lineno-start: 201
    :emphasize-lines: 6

            self.assertEqual(
                a_dictionary,
                {
                    'key': 'updated value',
                    'new_key': [0, 1, 2, 'n'],
                    'another_key': {0, 1, 2, 'n'},
                }
            )

  the test passes

* I change the name of the test

  .. code-block:: python
    :lineno-start: 194
    :emphasize-lines: 1

        def test_update_a_dictionary(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.update(new_key=[0, 1, 2, 'n']))
            self.assertIsNone(a_dictionary.update(key='updated value'))
            self.assertIsNone(a_dictionary.update(
                {'another_key': {0, 1, 2, 'n'}}
            ))
            self.assertEqual(
                a_dictionary,
                {
                    'key': 'updated value',
                    'new_key': [0, 1, 2, 'n'],
                    'another_key': {0, 1, 2, 'n'}
                }
            )


    'update',

  the test is still green

* I remove update_ from the TODO list

  .. code-block:: python
    :lineno-start: 201

            self.assertEqual(
                a_dictionary,
                {
                    'key': 'updated value',
                    'new_key': [0, 1, 2, 'n'],
                    'another_key': {0, 1, 2, 'n'}
                }
            )


    'values'

:ref:`I know how to add key-value pairs from one dictionary to another<test_update_a_dictionary>`

----

*********************************************************************************
test_values_of_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for the last :ref:`method<what is a function?>` in my TODO list

.. code-block:: python
  :lineno-start: 201
  :emphasize-lines: 10-12

          self.assertEqual(
              a_dictionary,
              {
                  'key': 'updated value',
                  'new_key': [0, 1, 2, 'n'],
                  'another_key': {0, 1, 2, 'n'},
              }
          )

      def test_values(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.values())


  'values'

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: dict_values(['value']) is not None

this is like :ref:`test_items_returns_iterable_of_key_value_pairs_of_a_dictionary` and  :ref:`test_keys_of_a_dictionary`

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add the expected value

  .. code-block:: python
    :lineno-start: 210
    :emphasize-lines: 3-6

        def test_values(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.values,
                dict_values(['value'])
            )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'dict_values' is not defined

* I remove the things around the :ref:`list<lists>` in the ``dict_values`` :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 212
    :emphasize-lines: 3

            self.assertIsNone(
                a_dictionary.values(),
                ['value']
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: dict_values(['value']) is not None : ['value']

* I use ``list()`` to see if ``dict_values`` is :ref:`iterable<what is an iterable?>`

  .. code-block:: python
    :lineno-start: 212
    :emphasize-lines: 2

            self.assertIsNone(
                list(a_dictionary.values()),
                ['value']
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ['value'] is not None : ['value']

* I change assertIsNone_ to assertEqual_

  .. code-block:: python
    :lineno-start: 212
    :emphasize-lines: 1

            self.assertEqual(
                list(a_dictionary.values()),
                ['value']
            )

  the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I change the dictionary_ to see what happens when it has more than one :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`

  .. code-block:: python
    :lineno-start: 210
    :emphasize-lines: 2-5

        def test_values(self):
            a_dictionary = {
                'key1': 'value1',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                list(a_dictionary.values()),
                ['value']
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Lists differ: ['value1', [0, 1, 2, 'n']] != ['value']

* I change the values in the expectation

  .. code-block:: python
    :lineno-start: 215
    :emphasize-lines: 3-6

            self.assertEqual(
                list(a_dictionary.values()),
                [
                    'value1',
                    [0, 1, 2, 'n'],
                ]
            )

  the test passes

* I change the name of the test

  .. code-block:: python
    :lineno-start: 210
    :emphasize-lines: 1

        def test_values_of_a_dictionary(self):
            a_dictionary = {
                'key1': 'value1',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                list(a_dictionary.values()),
                [
                    'value1',
                    [0, 1, 2, 'n'],
                ]
            )


    'values'

* I remove values_ from the TODO list

  .. code-block:: python
    :lineno-start: 215

            self.assertEqual(
                list(a_dictionary.values()),
                [
                    'value1',
                    [0, 1, 2, 'n']
                ]
            )


    # Exceptions seen

:ref:`I know how to look at the values of a dictionary<test_values_of_a_dictionary>`

----

*********************************************************************************
test_key_error
*********************************************************************************

`KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ is an important :ref:`Exception<errors>` to know when working with a dictionary_. It happened earlier in :ref:`my test for the pop method<test_pop_removes_given_key_from_a_dictionary_and_returns_its_value>`

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for getting the :ref:`value<test_values_of_a_dictionary>` of a :ref:`key<test_keys_of_a_dictionary>` that is in a dictionary_

.. code-block:: python
  :lineno-start: 215
  :emphasize-lines: 9-11

          self.assertEqual(
              list(a_dictionary.values()),
              [
                  'value1',
                  [0, 1, 2, 'n']
              ]
          )

      def test_key_error(self):
          a_dictionary = {'key': 'value'}
          self.assertEqual(a_dictionary['key'], '')


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'value' != ''

I get ``'value'`` back. I can get the value for a :ref:`key<test_key_error>` in a dictionary_ by giving the :ref:`key<test_key_error>` in ``[]``, the same way :ref:`I can get items from a list <test_getting_items_of_a_list>` by giving the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` in ``[]``

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the value in the expectation to match the terminal_

.. code-block:: python
  :lineno-start: 225
  :emphasize-lines: 1

          self.assertEqual(a_dictionary['key'], 'value')

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>`, this time for a :ref:`key<test_keys_of_a_dictionary>` that is not in the dictionary_

  .. code-block:: python
    :lineno-start: 225
    :emphasize-lines: 2

            self.assertEqual(a_dictionary['key'], 'value')
            self.assertEqual(a_dictionary['not_in_dictionary'])

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: 'not_in_dictionary'

* I change the assertEqual_ to assertRaises_

  .. code-block:: python
    :lineno-start: 225
    :emphasize-lines: 3-4

            self.assertEqual(a_dictionary['key'], 'value')

            with self.assertRaises(KeyError):
                a_dictionary['not_in_dictionary']

  the test passes

* I can use the `get method`_ when I do not want to get :ref:`KeyError<test_key_error>` with a :ref:`key<test_keys_of_a_dictionary>` that is not in a dictionary_

  .. code-block:: python
    :lineno-start: 227
    :emphasize-lines: 3-6

            with self.assertRaises(KeyError):
                a_dictionary['not_in_dictionary']
            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                ''
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'default' != ''

* I change the expectation

  .. code-block:: python
    :lineno-start: 229
    :emphasize-lines: 3

            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                'default'
            )

  the test passes. This is a repetition of :ref:`test_get_value_of_a_key_in_a_dictionary`, here is another one

* The `pop method`_ raised :ref:`KeyError<test_key_error>` when I gave it a :ref:`key<test_keys_of_a_dictionary>` that was not in the dictionary_, I add a failing line for it

  .. code-block:: python
    :lineno-start: 229
    :emphasize-lines: 6

            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                'default'
            )

            a_dictionary.pop('not_in_dictionary')

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: 'not_in_dictionary'

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 229
    :emphasize-lines: 6-7

            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                'default'
            )

            with self.assertRaises(KeyError):
                a_dictionary.pop('not_in_dictionary')

  the test passes

* I can give a second argument when I do not want the `pop method`_ to raise :ref:`KeyError<test_key_error>` when the :ref:`key<test_keys_of_a_dictionary>` is not in the dictionary_. I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 234
    :emphasize-lines: 3-6

            with self.assertRaises(KeyError):
                a_dictionary.pop('not_in_dictionary')
            self.assertEqual(
                a_dictionary.pop('not_in_dictionary', 'default'),
                ''
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'default' != ''

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 236
    :emphasize-lines: 3

            self.assertEqual(
                a_dictionary.pop('not_in_dictionary', 'default'),
                'default'
            )

  the test passes

* The `popitem method`_ also raises :ref:`KeyError<test_key_error>` when called on an empty dictionary_

  .. code-block::
    :lineno-start: 236
    :emphasize-lines: 6

            self.assertEqual(
                a_dictionary.pop('not_in_dictionary', 'default'),
                'default'
            )

            {}.popitem()

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: 'popitem(): dictionary is empty'

  I cannot remove the last :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` from a dictionary_ that has no :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 223
    :emphasize-lines: 19-20

        def test_key_error(self):
            a_dictionary = {'key': 'value'}
            self.assertEqual(a_dictionary['key'], 'value')

            with self.assertRaises(KeyError):
                a_dictionary['not_in_dictionary']
            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                'default'
            )

            with self.assertRaises(KeyError):
                a_dictionary.pop('not_in_dictionary')
            self.assertEqual(
                a_dictionary.pop('not_in_dictionary', 'default'),
                'default'
            )

            with self.assertRaises(KeyError):
                {}.popitem()


    # Exceptions seen
    # AssertionError
    # TypeError
    # NameError
    # KeyError

  the test passes

:ref:`I know what causes KeyError<test_key_error>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_dictionaries.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard, the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

.. NOTE:: on Windows_ without `Windows Subsystem for Linux`_

  * the terminal_ shows

    .. code-block:: PowerShell

      (.venv) ...\pumping_python\dictionaries

  * I deactivate the `virtual environment`_

    .. code-block:: PowerShell
      :emphasize-lines: 1

      deactivate

    the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

    .. code-block:: PowerShell

      ...\pumping_python\dictionaries

  * I `change directory`_ to the parent of ``dictionaries``

    .. code-block:: shell
      :emphasize-lines: 1

      cd ..

    the terminal_ shows

    .. code-block:: PowerShell

      ...\pumping_python

    I am back in the ``pumping_python`` directory_


----

*********************************************************************************
review
*********************************************************************************

Dictionaries_ are also known as Mappings, they contain :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` and any :ref:`object<what is a class?>` can be used as values.

I ran tests to show that I can make a dictionary_ with ``dict()`` or curly braces ``{}``, then I ran the following tests to see what :ref:`Python basic data types<data structures>` I can use as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`

* :ref:`test_making_a_dictionary_w_none_as_a_key`
* :ref:`test_making_a_dictionary_w_a_boolean_as_a_key`
* :ref:`test_making_a_dictionary_w_a_number_as_a_key`
* :ref:`test_making_a_dictionary_w_a_tuple_as_a_key`
* :ref:`test_making_a_dictionary_w_a_list_as_a_key`
* :ref:`test_making_a_dictionary_w_a_set_as_a_key`
* :ref:`test_making_a_dictionary_w_a_dictionary_as_a_key`

I also ran these tests for the :ref:`methods of dictionaries<test_attributes_and_methods_of_dictionaries>`

* :ref:`test_clear_empties_a_dictionary`
* :ref:`test_copy_a_dictionary`
* :ref:`test_fromkeys_makes_a_dictionary_from_an_iterable`
* :ref:`test_get_value_of_a_key_in_a_dictionary`
* :ref:`test_items_returns_iterable_of_key_value_pairs_of_a_dictionary`
* :ref:`test_keys_of_a_dictionary`
* :ref:`test_pop_removes_given_key_from_a_dictionary_and_returns_its_value`
* :ref:`test_popitem_removes_and_returns_last_key_value_pair_from_a_dictionary`
* :ref:`test_setdefault_adds_given_key_to_a_dictionary`
* :ref:`test_update_a_dictionary`
* :ref:`test_values_of_a_dictionary`

and a test for the important :ref:`Exception<errors>` to know when working with dictionaries_ - :ref:`KeyError<test_key_error>`

----

:ref:`How many questions can you answer after going through this chapter?<questions about dictionaries>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<data structures: dictionaries: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to write functions<what is a function?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<list comprehensions>`
* :ref:`what you can do with dictionaries<dictionaries>`

:ref:`Would you like to use dictionaries in the calculator tests?<how to make a calculator 6>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please leave a 5 star review. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->