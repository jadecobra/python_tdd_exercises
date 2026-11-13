.. meta::
  :description: In-depth TDD tutorial for Python dictionaries as key-value data structures. Master creating dicts, accessing items, methods like keys/values/items, iteration, and testing with assertions and unittest. Learn through red-green-refactor with examples that distinguish dicts from other structures, building on the AssertionError, None, and booleans chapters. Covers common patterns and beginner gotchas for dicts.
  :keywords: Jacob Itegboje, Pumping Python, python dictionaries tutorial, python dict key value, dict methods python, testing dictionaries unittest, TDD dict python, Python basic objects dictionaries, dict vs list, python dict iteration, unittest assert dict, red green refactor dictionaries, python dict best practices, python dict for beginners, key value pair testing, python dict TDD tutorial

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
.. _more_on_lists: https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists
.. _dict: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
.. _dict class: dict_
.. _dictionary: dict_
.. _dictionaries: dictionary_


#################################################################################
what is a dictionary?
#################################################################################

A dictionary_ also known as a Mapping is a way to keep :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`. The :ref:`values<test_values_of_a_dictionary>` can be any :ref:`Python object<everything is an object>`. I add tests to see which of :ref:`the Python basic data types<basic objects>` I can use as :ref:`keys<test_keys_of_a_dictionary>` .

I think this is the most important :ref:`data structure<basic objects>` because it can hold all the others, same as with :ref:`lists<what is a list?>` and tuples_. In programming I have had to work with JSON_ which I can read and write as dictionaries_.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/tests/test_dictionaries.py
  :language: python
  :linenos:

----

*********************************************************************************
questions about dictionaries
*********************************************************************************

* :ref:`what is a dictionary?`
* :ref:`how can I empty a dictionary?<test_clear_empties_a_dictionary>`
* :ref:`how can I copy a dictionary<test_copy_a_dictionary>`
* :ref:`how can I make a dictionary from an iterable?<test_fromkeys_makes_a_dictionary_from_an_iterable>`
* :ref:`how can I get a value that is in a dictionary?<test_get_value_of_a_key_in_a_dictionary>`
* :ref:`how can I look at the key-value pairs in a dictionary as a list of tuples?<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`
* :ref:`how can I look at only the keys in a dictionary?<test_keys_of_a_dictionary>`
* :ref:`how can I remove a key-value pair from a dictionary?<test_pop_removes_given_key_from_a_dictionary_and_returns_its_value>`
* :ref:`how can I remove the last key-value pair from a dictionary?<test_popitem_removes_and_returns_last_key_value_pair_from_a_dictionary>`
* :ref:`how can I add a key with a default value to a dictionary?<test_setdefault_adds_given_key_to_a_dictionary>`
* :ref:`how can I update a dictionary?<test_update_a_dictionary>`
* :ref:`how can I add the key-value pairs from one dictionary to another?<test_update_a_dictionary>`
* :ref:`how can I look at only the values in a dictionary?<test_values_of_a_dictionary>`
* :ref:`what causes KeyError?<test_key_error>`

*********************************************************************************
start the project
*********************************************************************************

* I open a terminal_
* I give ``dictionaries`` as the first argument to the :ref:`makePythonTdd<makePythonTdd with variables>` program_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :caption: terminal
        :emphasize-lines: 1

        ./makePythonTdd.sh dictionaries

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :caption: terminal
        :emphasize-lines: 1

        .\makePythonTdd.ps1 dictionaries

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 10
    :emphasize-text: tests/test_dictionaries.py:7

    ======================== FAILURES ==========================
    ______________ Testdictionaries.test_failure _________________

    self = <tests.test_dictionaries.Testdictionaries testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_dictionaries.py:7: AssertionError
    ================== short test summary info ==================
    FAILED tests/test_dictionaries.py::Testdictionaries::test_failure - AssertionError: True is not false
    ===================== 1 failed in X.YZs =====================

* I open ``test_dictionaries.py`` from the ``tests`` folder_ then put the cursor on line 7

* I change :ref:`assertFalse<another way to test if something is grouped as False>` to :ref:`assertTrue<another way to test if something is grouped as True>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 4
    :emphasize-lines: 4-5

    class Testdictionaries(unittest.TestCase):

        def test_failure(self):
            # self.assertFalse(True)
            self.assertTrue(True)


    # Exceptions seen

  the test passes.

* I change ``Testdictionaries`` to ``TestDictionaries`` to match :ref:`Python convention<conventions>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :linenos:
    :emphasize-lines: 4

    import unittest


    class TestDictionaries(unittest.TestCase):

        def test_failure(self):

* I open a new terminal_ then `change directory`_ to ``dictionaries``

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd dictionaries

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git add .

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'setup project'

----

*********************************************************************************
test_making_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change :ref:`test_failure` to ``test_making_a_dictionary`` then add an :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :linenos:
  :emphasize-lines: 6-7

  import unittest


  class TestDictionaries(unittest.TestCase):

      def test_making_a_dictionary(self):
          self.assertEqual(dict(), None)

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: {} != None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation to match

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 6
  :emphasize-lines: 2

      def test_making_a_dictionary(self):
          self.assertEqual(dict(), {})


  # Exceptions seen

the test passes. These are two ways to make an empty :ref:`dictionary<what is a dictionary?>`

* the dict_ constructor - ``dict()``
* curly braces - ``{}``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for a :ref:`dictionary<what is a dictionary?>` with things in it

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 6
    :emphasize-lines: 3

        def test_making_a_dictionary(self):
            self.assertEqual(dict(), {})
            self.assertEqual(dict(0), {})


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :caption: terminal

    TypeError: 'int' object is not iterable

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<how to test that an Exception is raised>` seen

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 11
    :emphasize-lines: 3
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # TypeError

* I change the value given to ``dict()`` to a tuple_

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 7
    :emphasize-lines: 2

            self.assertEqual(dict(), {})
            self.assertEqual(dict((0, 1)), {})


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: none

    TypeError: cannot convert dictionary update
               sequence element #0 to a sequence

* I try a :ref:`keyword argument<test_keyword_arguments>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 7
    :emphasize-lines: 2

            self.assertEqual(dict(), {})
            self.assertEqual(dict(key='value'), {})

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {'key': 'value'} != {}

* I change the expectation to match the values in the terminal_

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 6
    :emphasize-lines: 3

        def test_making_a_dictionary(self):
            self.assertEqual(dict(), {})
            self.assertEqual(dict(key='value'), {'key': 'value'})


    # Exceptions seen

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'add test_making_a_dictionary'

:ref:`I know how to make a dictionary<test_making_a_dictionary>`.

I used a string_ as a :ref:`key<test_keys_of_a_dictionary>` in this test. Next I test other :ref:`Python basic data types<basic objects>` to see which ones I can use as :ref:`keys<test_keys_of_a_dictionary>`.

----

*********************************************************************************
test_making_a_dictionary_w_none_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to see if I can use :ref:`None<what is None?>` as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 8
  :emphasize-lines: 3-4

          self.assertEqual(dict(key='value'), {'key': 'value'})

      def test_making_a_dictionary_w_none_as_a_key(self):
          self.assertEqual({None: 'boom'}, {None: 'bap'})


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: {None: 'boom'} != {None: 'bap'}

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``'bap'`` to ``'boom'``

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 10
    :emphasize-lines: 2

        def test_making_a_dictionary_w_none_as_a_key(self):
            self.assertEqual({None: 'boom'}, {None: 'boom'})


    # Exceptions seen

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'add test_making_a_dictionary_w_none_as_a_key'

I can use strings_ and :ref:`None<what is None?>` as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`

----

*********************************************************************************
test_making_a_dictionary_w_a_boolean_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to see if I can use a :ref:`boolean<what are booleans?>` as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 11
  :emphasize-lines: 3-4

          self.assertEqual({None: 'boom'}, {None: 'boom'})

      def test_making_a_dictionary_w_a_boolean_as_a_key(self):
          self.assertEqual({False: 'boom'}, {False: 'bap'})


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: {False: 'boom'} != {False: 'bap'}

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``'bap'`` to ``'boom'``

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 13
    :emphasize-lines: 2

        def test_making_a_dictionary_w_a_boolean_as_a_key(self):
            self.assertEqual({False: 'boom'}, {False: 'boom'})


    # Exceptions seen

  the test passes.

I can use :ref:`False<test_what_is_false>` as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`other boolean<test_what_is_true>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 13
    :emphasize-lines: 2-5

        def test_making_a_dictionary_w_a_boolean_as_a_key(self):
            self.assertEqual(
                {False: 'boom', True: 'bap'},
                {False: 'boom'}
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {False: 'boom', True: 'bap'} != {False: 'boom'}

* I add the new :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to the expectation

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 13
    :emphasize-lines: 4

        def test_making_a_dictionary_w_a_boolean_as_a_key(self):
            self.assertEqual(
                {False: 'boom', True: 'bap'},
                {False: 'boom', True: 'bap'}
            )


    # Exceptions seen

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_a_dictionary_w_a_boolean_as_a_key'

I can use strings_, :ref:`booleans<what are booleans?>` and :ref:`None<what is None?>` as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`.

----

*********************************************************************************
test_making_a_dictionary_w_a_number_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a failing test to see if I can use a number as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
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

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: {0: 'boom'} != {0: 'bap'}

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``'bap'`` to ``'boom'``

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 19
  :emphasize-lines: 4

      def test_making_a_dictionary_w_a_number_as_a_key(self):
          self.assertEqual(
              {0: 'boom'},
              {0: 'boom'}
          )


  # Exceptions seen

the test passes.

I can use an integer_ as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I want to see if I can use a float_ as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`. I add a float_ to the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 19
    :emphasize-lines: 3

        def test_making_a_dictionary_w_a_number_as_a_key(self):
            self.assertEqual(
                {0: 'boom', 0.1: 'bap'},
                {0: 'boom'}
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {0: 'boom', 0.1: 'bap'} != {0: 'boom'}

* I add the new :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to the expectation

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 19
    :emphasize-lines: 4

        def test_making_a_dictionary_w_a_number_as_a_key(self):
            self.assertEqual(
                {0: 'boom', 0.1: 'bap'},
                {0: 'boom', 0.1: 'bap'}
            )

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_a_dictionary_w_a_number_as_a_key'

I can use strings_, numbers (floats_ and integers_), :ref:`booleans<what are booleans?>` and :ref:`None<what is None?>` as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`.

----

*********************************************************************************
test_making_a_dictionary_w_a_tuple_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to see if I can use a tuple_ (anything in parentheses (``()``) separated by a comma) as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
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

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: {(0, 1): 'boom'} != {(0, 1): 'bap'}

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``'bap'`` to ``'boom'``

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 25
    :emphasize-lines: 4

        def test_making_a_dictionary_w_a_tuple_as_a_key(self):
            self.assertEqual(
                {(0, 1): 'boom'},
                {(0, 1): 'boom'}
            )


    # Exceptions seen

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_a_dictionary_w_a_tuple_as_a_key'


I can use tuples_, strings_, numbers (floats_ and integers_), :ref:`booleans<what are booleans?>` and :ref:`None<what is None?>` as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`.

----

*********************************************************************************
test_making_a_dictionary_w_a_list_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for making a :ref:`dictionary<what is a dictionary>` with a :ref:`list` (anything in square brackets (``[]``)) as a :ref:`key<test_keys_of_a_dictionary>`

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
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

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: cannot use 'list' as a dict key
             (unhashable type: 'list')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I remove the things around the new :ref:`dictionary<what is a dictionary?>` then change the :ref:`key<test_keys_of_a_dictionary>` and :ref:`value<test_values_of_a_dictionary>` for fun

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 31
    :emphasize-lines: 3

        def test_making_a_dictionary_w_a_list_as_a_key(self):

                {[3, 2, 1]: 'BOOM!!!'}


    # Exceptions seen

  the terminal_ still shows :ref:`TypeError<what causes TypeError?>`

* I add :ref:`assertRaises<another way to test if an Exception is raised>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 31
    :emphasize-lines: 2

        def test_making_a_dictionary_w_a_list_as_a_key(self):
            with self.assertRaises(TypeError):
                {[3, 2, 1]: 'BOOM!!!'}

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_a_dictionary_w_a_list_as_a_key'

I cannot use a :ref:`list<what is a list?>` as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`.

----

*********************************************************************************
test_making_a_dictionary_w_a_set_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with a set_ (single items in curly braces (``{}``)) as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 32
  :emphasize-lines: 4-5

          with self.assertRaises(TypeError):
              {[3, 2, 1]: 'BOOM!!!'}

      def test_making_a_dictionary_w_a_set_as_a_key(self):
          {{3, 2, 1}: 'BOOM!!!'}


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: unhashable type: 'set'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`assertRaises<another way to test if an Exception is raised>` to handle the :ref:`Exception<how to test that an Exception is raised>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 35
    :emphasize-lines: 2-3

        def test_making_a_dictionary_w_a_set_as_a_key(self):
            with self.assertRaises(TypeError):
                {{3, 2, 1}: 'BOOM!!!'}


    # Exceptions seen

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_a_dictionary_w_a_set_as_a_key'

I cannot use :ref:`lists` or sets_ as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`.

----

*********************************************************************************
test_making_a_dictionary_w_a_dictionary_as_a_key
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with a :ref:`dictionary<what is a dictionary?>` as a :ref:`key in a dictionary<test_keys_of_a_dictionary>`

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 36
  :emphasize-lines: 4-6

          with self.assertRaises(TypeError):
              {[3, 2, 1]: 'BOOM!!!'}

      def test_making_a_dictionary_w_a_dictionary_as_a_key(self):
          a_dictionary = {'key': 'value'}
          {a_dictionary: 'BOOM!!!'}


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: unhashable type: 'dict'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`assertRaises<another way to test if an Exception is raised>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 39
    :emphasize-lines: 3-4

        def test_making_a_dictionary_w_a_dictionary_as_a_key(self):
            a_dictionary = {'key': 'value'}
            with self.assertRaises(TypeError):
                {a_dictionary: 'BOOM!!!'}


    # Exceptions seen

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_a_dictionary_w_a_dictionary_as_a_key'

I cannot use :ref:`dictionaries<what is a dictionary?>`, sets_ or :ref:`lists` as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`. They are not hashable_, which means they can change in their lifetime.

----

*********************************************************************************
test_dir_dict
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test with the `dir built-in function`_ to see the :ref:`attributes<what is an object attribute?>` and :ref:`methods<what is a method?>` of :ref:`dictionaries<what is a dictionary?>`

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 41
  :emphasize-lines: 4-8

          with self.assertRaises(TypeError):
              {a_dictionary: 'BOOM!!!'}

      def test_dir_dict(self):
          self.assertEqual(
              dir(dict),
              []
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: Lists differ: [
      '__class__', '__class_getitem__', '__cont[530 chars]ues'
  ] != []

It also gives me a message about how to show the full difference between the two :ref:`lists`

.. code-block:: python

  Diff is 720 characters long. Set self.maxDiff to None to see it.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add maxDiff_ to the :ref:`test_dir_dict`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 44
    :emphasize-lines: 2

        def test_dir_dict(self):
            self.maxDiff = None
            self.assertEqual(
                dir(dict),
                []
            )

  the terminal_ is my friend, and shows the full difference between the two :ref:`lists`.

* I copy (:kbd:`ctrl/command+c`) and paste (:kbd:`ctrl/command+v`) the expected values from the terminal_ then use `find and replace`_ to remove the extra characters

  .. note::

    results can be different because of the Python_ version.

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 44
    :emphasize-lines: 6-51

        def test_dir_dict(self):
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

  the test passes.

* I copy the names that do NOT have double underscores (``__``) and paste them below the test to make a TODO list that I use to test what I can do with :ref:`dictionaries<what is a dictionary?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

  the test is still green.

----

*********************************************************************************
test_dir_dict with extend and sort
*********************************************************************************

The :ref:`attributes and methods of the dictionary object<test_dir_dict>` are the :ref:`attributes and methods of 'object'<test_dir_object>` with extra things. I can make the :ref:`attributes and methods of the dictionary object<test_dir_dict>` by adding the "extra" to the :ref:`attributes and methods of 'object'<test_dir_object>`, since they are both :ref:`lists<what is a list?>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

I add a :ref:`variable<what is a variable?>` for the :ref:`attributes and methods of the dict object<test_dir_dict>`, then add an :ref:`assertion<what is an assertion?>` for it, in :ref:`test_dir_dict`

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 44
  :emphasize-lines: 3-9

      def test_dir_dict(self):
          self.maxDiff = None
          dir_dict = dir(object)
          dir_dict.extend((
              'clear', 'copy', 'fromkeys',
              'get', 'items', 'keys',
              'pop', 'popitem', 'setdefault',
              'update', 'values'
          ))
          self.assertEqual(
              dir(dict),
              dir_dict
          )
          self.assertEqual(
              dir(dict),

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: Lists differ: [
      '__class__', '__class_getitem__', '__contains__',
      '__dela[514 chars]ues'
  ] != [
      '__class__', '__delattr__', '__dir__', '__doc__',
      '__eq__[361 chars]ues'
  ]

with a note about the difference

.. code-block:: python
  :caption: terminal

  First list contains 11 additional elements.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the eleven additional elements

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 47
    :emphasize-lines: 2-5

            dir_dict.extend((
                '__class_getitem__', '__contains__',
                '__delitem__', '__getitem__', '__ior__',
                '__iter__', '__len__', '__or__',
                '__reversed__', '__ror__', '__setitem__',
                'clear', 'copy', 'fromkeys',
                'get', 'items', 'keys',
                'pop', 'popitem', 'setdefault',
                'update', 'values'
            ))
            self.assertEqual(
                dir(dict),
                dir_dict
            )

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`.

* I add a :ref:`call to the sort method<test_sort_a_list>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 47
    :emphasize-lines: 11

            dir_dict.extend((
                '__class_getitem__', '__contains__',
                '__delitem__', '__getitem__', '__ior__',
                '__iter__', '__len__', '__or__',
                '__reversed__', '__ror__', '__setitem__',
                'clear', 'copy', 'fromkeys',
                'get', 'items', 'keys',
                'pop', 'popitem', 'setdefault',
                'update', 'values'
            ))
            dir_dict.sort()
            self.assertEqual(
                dir(dict),
                dir_dict
            )
            self.assertEqual(
                dir(dict),

  the test passes because :ref:`all objects inherit from 'object'<test_making_an_object_w_object>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertion<what is an assertion?>` from :ref:`test_dir_dict`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 58

            self.assertEqual(
                dir(dict),
                dir_dict
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

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'add test_dir_dict'

:ref:`All objects inherit attributes and methods from 'object'<test_making_an_object_w_object>`.

----

*********************************************************************************
test_clear_empties_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for the `clear method`_

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 58
    :emphasize-lines: 6-8

            self.assertEqual(
                dir(dict),
                dir_dict
            )

        def test_clear(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.clear())


    'clear',

  still green. The `clear method`_ returns :ref:`None<what is None?>`

* I add an :ref:`assertion<what is an assertion?>` to see what clear_ did to the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 63
    :emphasize-lines: 4

        def test_clear(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.clear())
            self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {} != {'key': 'value'}

  the `clear method`_ emptied the :ref:`dictionary<what is a dictionary?>`, :ref:`same as it does with lists<test_clear_empties_a_list>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation to match

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 63
  :emphasize-lines: 4

      def test_clear(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.clear())
          self.assertEqual(a_dictionary, {})


  'clear',

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 58
    :emphasize-lines: 6

            self.assertEqual(
                dir(dict),
                dir_dict
            )

        def test_clear_empties_a_dictionary(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.clear())
            self.assertEqual(a_dictionary, {})


    'clear',

* I remove clear_ from the TODO list

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 66

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

----

I add a test for the `copy method`_

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 66
  :emphasize-lines: 3-5

          self.assertEqual(a_dictionary, {})

      def test_copy(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.copy())


  'copy',
  'fromkeys',

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: {'key': 'value'} is not None

this `copy method`_ returns a copy of the :ref:`dictionary<what is a dictionary?>`, :ref:`same as with lists<test_copy_a_list>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the value to the :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 68
  :emphasize-lines: 3-6

      def test_copy(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(
              a_dictionary.copy(),
              {'key': 'value'}
          )


  'copy',

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: {'key': 'value'} is not None : {'key': 'value'}

I change :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertEqual<test_assertEqual>`

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 68
  :emphasize-lines: 3

      def test_copy(self):
          a_dictionary = {'key': 'value'}
          self.assertEqual(
              a_dictionary.copy(),
              {'key': 'value'}
          )

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 66
    :emphasize-lines: 3

            self.assertEqual(a_dictionary, {})

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
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 70

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

:ref:`I know how to copy a dictionary<test_copy_a_dictionary>`.

----

*********************************************************************************
test_fromkeys_makes_a_dictionary_from_an_iterable
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the next :ref:`method<what is a method?>` from the TODO list

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 70
  :emphasize-lines: 6-8

          self.assertEqual(
              a_dictionary.copy(),
              {'key': 'value'}
          )

      def test_fromkeys(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.fromkeys())


  'fromkeys',

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: fromkeys expected at least 1 argument,
             got 0

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I pass a value to the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 75
    :emphasize-lines: 3

        def test_fromkeys(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.fromkeys(0))


    'fromkeys',

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :caption: terminal

    TypeError: 'int' object is not iterable

* I change the value to a tuple_

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 75
    :emphasize-lines: 3-5

        def test_fromkeys(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.fromkeys((0, 1))
            )


    'fromkeys',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {0: None, 1: None}
                    is not None

  the `fromkeys method`_ returns a :ref:`dictionary<what is a dictionary?>` that uses the values in the :ref:`iterable<what is an iterable?>` as :ref:`keys<test_keys_of_a_dictionary>`, and :ref:`None<what is None?>` as their default :ref:`values<test_values_of_a_dictionary>`. It reminds me of a :ref:`list comprehension<test_making_a_list_w_a_list_comprehension>`.

* I add the :ref:`dictionary<what is a dictionary?>` as the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 75
    :emphasize-lines: 5

        def test_fromkeys(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.fromkeys((0, 1)),
                {0: None, 1: None}
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {0: None, 1: None}
                    is not None : {0: None, 1: None}

* I change :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertEqual<test_assertEqual>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 75
    :emphasize-lines: 3

        def test_fromkeys(self):
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                a_dictionary.fromkeys((0, 1)),
                {0: None, 1: None}
            )


    'fromkeys',

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` to see what happened to ``a_dictionary``

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 75
    :emphasize-lines: 7

        def test_fromkeys(self):
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                a_dictionary.fromkeys((0, 1)),
                {0: None, 1: None}
            )
            self.assertEqual(a_dictionary, {})


    'fromkeys',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {'key': 'value'} != {}

  the :ref:`dictionary<what is a dictionary?>` did not change

* I remove ``self.assertEqual(a_dictionary, {})``
* I change ``a_dictionary.fromkeys((0, 1))`` to use the :ref:`dict class<what is a dictionary?>` instead of ``a_dictionary``

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 75
    :emphasize-lines: 4

        def test_fromkeys(self):
            a_dictionary = {'key': 'value'}
            self.assertEqual(
                dict.fromkeys((0, 1)),
                {0: None, 1: None}
            )


    'fromkeys',

  the test is still green.

* I remove ``a_dictionary`` since it is no longer used

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 75

        def test_fromkeys(self):
            self.assertEqual(
                dict.fromkeys((0, 1)),
                {0: None, 1: None}
            )


    'fromkeys',

  still green.

* the :ref:`dictionary<what is a dictionary?>` made with the `fromkeys method`_ has :ref:`None<what is None?>` as the default values. When I :ref:`called<how to call a function with input>` the :ref:`method<what is a method?>` without inputs the terminal_ showed :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :caption: terminal

    TypeError: fromkeys expected at least 1 argument,
               got 0

  I add a second :ref:`assertion<what is an assertion>` to see what happens when I give :ref:`None<what is None?>` as the second input

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 75
    :emphasize-lines: 6-9

        def test_fromkeys(self):
            self.assertEqual(
                dict.fromkeys((0, 1)),
                {0: None, 1: None}
            )
            self.assertEqual(
                dict.fromkeys((0, 1), None),
                {0: None, 1: None}
            )


    'fromkeys',

  the test is still green.

* I change the second input, I think this will fail

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 75
    :emphasize-lines: 7

        def test_fromkeys(self):
            self.assertEqual(
                dict.fromkeys((0, 1)),
                {0: None, 1: None}
            )
            self.assertEqual(
                dict.fromkeys((0, 1), 'default'),
                {0: None, 1: None}
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {0: 'default', 1: 'default'}
                 != {0: None, 1: None}

* I change the values in the expectation to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 80
    :emphasize-lines: 3

            self.assertEqual(
                dict.fromkeys((0, 1), 'default'),
                {0: 'default', 1: 'default'}
            )


    'fromkeys',

  the test is green again.

* This is like a :ref:`dict comprehension<dict comprehensions>` because it made a :ref:`dictionary<what is a dictionary?>` using the items from an :ref:`iterable<what is an iterable?>` as :ref:`keys<test_keys_of_a_dictionary>`

  .. code-block:: python
    :caption: dictionaries80/tests/test_dictionaries.py
    :lineno-start: 80
    :emphasize-lines: 5-8

            self.assertEqual(
                dict.fromkeys((0, 1), 'default'),
                {0: 'default', 1: 'default'}
            )
            self.assertEqual(
                {key: 'value' for key in (0, 1)},
                {}
            )


    'fromkeys',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {0: 'value', 1: 'value'} != {}

* I change the expectation to match

  .. code-block:: python
    :caption: dictionaries80/tests/test_dictionaries.py
    :lineno-start: 84
    :emphasize-lines: 3

            self.assertEqual(
                {key: 'value' for key in (0, 1)},
                {0: 'value', 1: 'value'}
            )


    'fromkeys',

  the test passes.

* I change the name of the test

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 70
    :emphasize-lines: 6

            self.assertEqual(
                a_dictionary.copy(),
                {'key': 'value'}
            )

        def test_fromkeys_makes_a_dictionary_from_an_iterable(self):
            self.assertEqual(
                dict.fromkeys((0, 1)),
                {0: None, 1: None}
            )

* I remove fromkeys_ from the TODO list

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 84

            self.assertEqual(
                {key: 'value' for key in (0, 1)},
                {0: 'value', 1: 'value'}
            )


    'get',
    'items',
    'keys',
    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_fromkeys_makes_a_dictionary_from_an_iterable'

:ref:`I know how to make a dictionary from an iterable<tesT_fromkeys_makes_a_dictionary_from_an_iterable>`.

----

*********************************************************************************
test_get_value_of_a_key_in_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the `get method`_

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
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

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: get expected at least 1 argument, got 0

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a value to the call

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 118
  :emphasize-lines: 1

          self.assertIsNone(a_dictionary.get(0))

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* the `get method`_ also expected at least 1 argument, I add :ref:`None<what is None?>` to the call

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 118
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.get(0, None))

  the test is still green.

* I change the second argument, I think this will fail

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 118
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.get(0, 'default'))

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 'default' is not None

* I add the expectation

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 116
    :emphasize-lines: 3-6

        def test_get(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.get(0, 'default'),
                'default'
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 'default' is not None : default

* I change :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertEqual<test_assertEqual>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 118
    :emphasize-lines: 1

            self.assertEqual(
                a_dictionary.get(0, 'default'),
                'default'
            )

  the test passes.

* I change ``0`` in the call to make it clearer

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 118
    :emphasize-lines: 2
    :emphasize-text: not_in_dictionary

            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                'default'
            )

  the test is still green.

* I want to see what happens when I use the `get method`_ with a :ref:`key<test_keys_of_a_dictionary>` that is in the :ref:`dictionary<what is a dictionary?>`, I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 'value' != 'default'

  I get ``'value'`` back

* I change the expectation to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 122
    :emphasize-lines: 3

            self.assertEqual(
                a_dictionary.get('key', 'default'),
                'value'
            )

  the test passes.

  .. note::

    The `get method`_ has a :ref:`condition<if statements>`

    - if the :ref:`key<test_keys_of_a_dictionary>` is NOT in the :ref:`dictionary<what is a dictionary?>`, it returns the default argument
    - if the :ref:`key<test_keys_of_a_dictionary>` is in the :ref:`dictionary<what is a dictionary?>`, it returns its :ref:`value<test_values_of_a_dictionary>`

* I change the name of the test

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

  the test is still green.

* I remove get_ from the TODO list

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

----

I add the next test from the TODO list

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
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

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: dict_items([('key', 'value')]) is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I copy the ``dict_items`` :ref:`object<everything is an object>` from the terminal_ and paste  it as the expectation

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 128
    :emphasize-lines: 2-5

            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.items(),
                dict_items([('key', 'value')])
            )

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python
    :caption: terminal

    NameError: name 'dict_items' is not defined

  this new :ref:`object<everything is an object>` has a :ref:`list<what is a list?>` and :ref:`I know how to work with lists<what is a list?>`, just like :ref:`dict_items<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`

* I add :ref:`NameError<test_catching_name_error>` to the list of :ref:`Exceptions<how to test that an Exception is raised>` seen

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 145
    :emphasize-lines: 4
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # TypeError
    # NameError

* I remove the stuff around the :ref:`list<what is a list?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 129
    :emphasize-lines: 3

            self.assertIsNone(
                a_dictionary.items(),
                [('key', 'value')]
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: dict_items([('key', 'value')]) is not None : [('key', 'value')]

* I pass the call to the `items method`_ to ``list()`` to see if it is :ref:`iterable<what is an iterable?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 129
    :emphasize-lines: 2

            self.assertIsNone(
                list(a_dictionary.items()),
                [('key', 'value')]
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: [('key', 'value')] is not None : [('key', 'value')]

  the values are the same

* I change :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertEqual<test_assertEqual>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 129
    :emphasize-lines: 1

            self.assertEqual(
                list(a_dictionary.items()),
                [('key', 'value')]
            )

  the test passes.

This works because the `items method`_ returns an :ref:`iterable<what is an iterable?>` of the key-value pairs of the :ref:`dictionary<what is a dictionary?>`. The ``dict_items`` :ref:`object<everything is an object>` is :ref:`iterable<what is an iterable?>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another key-value pair to the :ref:`dictionary<what is a dictionary?>` to see what the :ref:`method<what is a method?>` does when there is more than one

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 127
    :emphasize-lines: 2-5

        def test_items(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                list(a_dictionary.items()),
                [('key', 'value')]
            )


    'items',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [('key0', 'value0'), ('keyN', [0, 1, 2, 'n'])] != [('key', 'value')]

* I change the expectation to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 132
    :emphasize-lines: 3-6

            self.assertEqual(
                list(a_dictionary.items()),
                [
                    ('key0', 'value0'),
                    ('keyN', [0, 1, 2, 'n']),
                ]
            )

  the test passes.

* I change the name of the test

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 127
    :emphasize-lines: 1

        def test_items_returns_iterable_of_key_value_pairs_of_a_dictionary(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                list(a_dictionary.items()),
                [
                    ('key0', 'value0'),
                    ('keyN', [0, 1, 2, 'n']),
                ]
            )


    'items',

* I remove items_ from the TODO list

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 132

            self.assertEqual(
                list(a_dictionary.items()),
                [
                    ('key0', 'value0'),
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

----

I add a new test

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 132
  :emphasize-lines: 9-11

              self.assertEqual(
                  list(a_dictionary.items()),
                  [
                      ('key0', 'value0'),
                      ('keyN', [0, 1, 2, 'n']),
                  ]
              )

      def test_keys(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.keys())


  'keys',

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: dict_keys(['key']) is not None

this looks like the error in :ref:`test_items_returns_iterable_of_key_value_pairs_of_a_dictionary`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I copy the ``dict_keys`` :ref:`object<everything is an object>` from the terminal_ and paste it as the expectation

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 140
    :emphasize-lines: 3-6

        def test_keys(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.keys(),
                dict_keys(['key'])
            )

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python
    :caption: terminal

    NameError: name 'dict_keys' is not defined

  the ``dict_keys`` :ref:`object<everything is an object>` has a :ref:`list<what is a list?>`

* I use the :ref:`list<what is a list?>` in the ``dict_keys`` :ref:`object<everything is an object>` as the expectation

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 140
    :emphasize-lines: 5

        def test_keys(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.keys(),
                ['key']
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: dict_keys(['key']) is not None : ['key']

* I pass the call to the `keys method`_ to ``list()`` to see if ``dict_keys`` is :ref:`iterable<what is an iterable?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 142
    :emphasize-lines: 2

            self.assertIsNone(
                list(a_dictionary.keys()),
                ['key']
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: ['key'] is not None : ['key']

* I change :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertEqual<test_assertEqual>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 142
    :emphasize-lines: 1

            self.assertEqual(
                list(a_dictionary.keys()),
                ['key']
            )

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to the :ref:`dictionary<what is a dictionary?>` to see what the `keys method`_ returns when there are multiple

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 140
    :emphasize-lines: 2-5

        def test_keys(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                list(a_dictionary.keys()),
                ['key']
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: ['key0', 'keyN'] != ['key']

* I change the expectation to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 145
    :emphasize-lines: 3

            self.assertEqual(
                list(a_dictionary.keys()),
                ['key0', 'keyN']
            )

  the test passes.

* I change the name of the test

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 140
    :emphasize-lines: 1

        def test_keys_of_a_dictionary(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                list(a_dictionary.keys()),
                ['key0', 'keyN']
            )


    'keys',

* I remove keys_ from the TODO list

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 145

            self.assertEqual(
                list(a_dictionary.keys()),
                ['key0', 'keyN']
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

----

I wonder if the `pop method`_ of :ref:`dictionaries<what is a dictionary?>` behaves the same way as the :ref:`pop method of lists<test_pop_removes_and_returns_last_item_from_a_list>`. I add a test for it

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 145
  :emphasize-lines: 6-8

          self.assertEqual(
              list(a_dictionary.keys()),
              ['key0', 'keyN']
          )

      def test_pop(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.pop())


  'pop',

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: pop expected at least 1 argument, got 0

this `pop method`_ is different from the :ref:`pop method of lists<test_pop_removes_and_returns_last_item_from_a_list>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I pass a value to the call

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 152
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.pop(0))

  the terminal_ is my friend, and shows :ref:`KeyError<test_key_error>`

  .. code-block:: python
    :caption: terminal

    KeyError: 0

* I add :ref:`KeyError<test_key_error>` to the list of :ref:`Exceptions<how to test that an Exception is raised>` seen

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 162
    :emphasize-lines: 5
    :emphasize-text: KeyError

    # Exceptions seen
    # AssertionError
    # TypeError
    # NameError
    # KeyError

* I remove the things around the call in the test and change the value given to make it clearer

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 150
    :emphasize-lines: 3
    :emphasize-text: not_in_dictionary

        def test_pop(self):
            a_dictionary = {'key': 'value'}
            a_dictionary.pop('not_in_dictionary')

  the terminal_ is my friend, and shows :ref:`KeyError<test_key_error>`

  .. code-block:: python
    :caption: terminal

    KeyError: 'not in dictionary'

* I add :ref:`assertRaises<another way to test if an Exception is raised>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 150
    :emphasize-lines: 4-5

        def test_pop(self):
            a_dictionary = {'key': 'value'}

            with self.assertRaises(KeyError):
                a_dictionary.pop('not_in_dictionary')

  the test passes. When I call the `pop method`_ with a :ref:`key<test_keys_of_a_dictionary>` that is not in the :ref:`dictionary<what is a dictionary?>` it raises :ref:`KeyError<test_key_error>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I called the `pop method`_ without input, the terminal_ showed :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :caption: terminal

    TypeError: pop expected at least 1 argument, got 0

  I add another :ref:`assertion<what is an assertion?>` to see what happens when I call it with 2 arguments

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 153
    :emphasize-lines: 3

            with self.assertRaises(KeyError):
                a_dictionary.pop('not_in_dictionary')
            self.assertIsNone(a_dictionary.pop('not_in_dictionary', None))

  the test is still green.

* I change the second argument, I think this will fail

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 155
    :emphasize-lines: 1
    :emphasize-text: default

            self.assertIsNone(a_dictionary.pop('not_in_dictionary', 'default'))

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 'default' is not None

* I add the expectation

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 155
    :emphasize-lines: 1-4

            self.assertIsNone(
                a_dictionary.pop('not_in_dictionary', 'default'),
                'default'
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 'default' is not None : default

* I change :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertEqual<test_assertEqual>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 155
    :emphasize-lines: 1

            self.assertEqual(
                a_dictionary.pop('not_in_dictionary', 'default'),
                'default'
            )

  the test passes.

* I add another :ref:`assertion<what is an assertion?>` to see what happens when I call the `pop method`_ with a :ref:`key<test_keys_of_a_dictionary>` that is in the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 'value' != 'default'

  I get ``'value'`` back. The `pop method`_ returns the value of the given :ref:`key<test_keys_of_a_dictionary>` from the :ref:`dictionary<what is a dictionary?>`

* I change the expectation to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 159
    :emphasize-lines: 3

            self.assertEqual(
                a_dictionary.pop('key', 'default'),
                'value'
            )

  the test passes.

* I add another :ref:`assertion<what is an assertion?>` to see what the `pop method`_ did to the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 159
    :emphasize-lines: 5

            self.assertEqual(
                a_dictionary.pop('key', 'default'),
                'value'
            )
            self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {} != {'key': 'value'}

  the `pop method`_ removes the :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` and returns the :ref:`value<test_values_of_a_dictionary>` of the given :ref:`key<test_keys_of_a_dictionary>` from the :ref:`dictionary<what is a dictionary?>`

* I change the expectation to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 163
    :emphasize-lines: 1

            self.assertEqual(a_dictionary, {})

  the test passes.

* I change the name of the test

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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
    :caption: dictionaries/tests/test_dictionaries.py
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

----

I add a failing test for the next item in the TODO list

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 163
  :emphasize-lines: 3-5

          self.assertEqual(a_dictionary, {})

      def test_popitem(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.popitem())


  'popitem',

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: ('key', 'value') is not None

the `popitem method`_ returns the :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in the :ref:`dictionary<what is a dictionary?>` as a tuple_

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the value from the terminal_ as the expectation

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 166
  :emphasize-lines: 2-5

          a_dictionary = {'key': 'value'}
          self.assertIsNone(
              a_dictionary.popitem(),
              ('key', 'value')
          )

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: ('key', 'value') is not None : ('key', 'value')

I change :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertEqual method<test_assertEqual>`

.. code-block::
  :lineno-start: 167
  :emphasize-lines: 1

          self.assertEqual(
              a_dictionary.popitem(),
              ('key', 'value')
          )

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` to see what the `popitem method`_ did to the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 167
    :emphasize-lines: 5

            self.assertEqual(
                a_dictionary.popitem(),
                ('key', 'value')
            )
            self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {} != {'key': 'value'}

  popitem_ removes and returns the :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` from the :ref:`dictionary<what is a dictionary?>`

* I change the value to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 171
    :emphasize-lines: 1

            self.assertEqual(a_dictionary, {})

  the test passes.

* this operation does not take input, I change the :ref:`dictionary<what is a dictionary?>` to see what happens

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 165
    :emphasize-lines: 2-5

        def test_popitem(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                a_dictionary.popitem(),
                ('key', 'value')
            )
            self.assertEqual(a_dictionary, {})

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Tuples differ: ('keyN', [0, 1, 2, 'n']) != ('key', 'value')

  popitem_ removes and returns the last :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` from a :ref:`dictionary<what is a dictionary?>`

* I change the expectation in the first :ref:`assertEqual method<test_assertEqual>` to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 170
    :emphasize-lines: 3

            self.assertEqual(
                a_dictionary.popitem(),
                ('keyN', [0, 1, 2, 'n'])
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {'key0': 'value0'} != {}

* I change the value in the second :ref:`assertEqual method<test_assertEqual>` to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 174
    :emphasize-lines: 1

            self.assertEqual(a_dictionary, {'key0': 'value0'})

  the test passes.

* I change the name of the test

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 165
    :emphasize-lines: 1

        def test_popitem_removes_and_returns_last_key_value_pair_from_a_dictionary(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                a_dictionary.popitem(),
                ('keyN', [0, 1, 2, 'n'])
            )
            self.assertEqual(a_dictionary, {'key0': 'value0'})


    'popitem',

* I remove popitem_ from the TODO list

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 174

            self.assertEqual(a_dictionary, {'key0': 'value0'})


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

----

I add a test for the `setdefault method`_

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 174
  :emphasize-lines: 3-5

          self.assertEqual(a_dictionary, {'key0': 'value0'})

      def test_setdefault(self):
          a_dictionary = {'key': 'value'}
          self.assertIsNone(a_dictionary.setdefault())


  'setdefault',

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: setdefault expected at least 1 argument, got 0

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I pass a value in the call

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 178
  :emphasize-lines: 1

          self.assertIsNone(a_dictionary.setdefault(0))

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* The error message showed that the :ref:`method<what is a method?>` expects at least 1 argument, I add a second argument

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 178
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.setdefault(0, None))

  the test is still green.

* I change the second argument, I think this will fail

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 178
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.setdefault(0, 'default'))

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 'default' is not None

* I add the expectation

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 177
    :emphasize-lines: 2-5

            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.setdefault(0, 'default'),
                'default'
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 'default' is not None : default

* I change :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertEqual<test_assertEqual>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 178
    :emphasize-lines: 1

            self.assertEqual(
                a_dictionary.setdefault(0, 'default'),
                'default'
            )

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` to see what setdefault_ did to the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 178
    :emphasize-lines: 5

            self.assertEqual(
                a_dictionary.setdefault(0, 'default'),
                'default'
            )
            self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {'key': 'value', 0: 'default'} != {'key': 'value'}

  setdefault_ adds the given :ref:`key<test_keys_of_a_dictionary>` to the :ref:`dictionary<what is a dictionary?>` with the default :ref:`value<test_values_of_a_dictionary>` and returns the default value

* I change the expectation to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

  the test passes.

* I change the ``0`` given in the call to the `setdefault method`_ be clearer

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 178
    :emphasize-lines: 2

            self.assertEqual(
                a_dictionary.setdefault('new_key', 'default'),
                'default'
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {'key': 'value', 'new_key': 'default'} != {'key': 'value', 0: 'default'}

* I change the expectation to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

* I add an :ref:`assertion<what is an assertion?>` to see what happens when I use setdefault_ with a :ref:`key<test_keys_of_a_dictionary>` that is already in the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 'value' != 'default'

  setdefault_ returns the :ref:`value<test_values_of_a_dictionary>` for a :ref:`key in a dictionary<test_keys_of_a_dictionary>`, if the :ref:`key<test_keys_of_a_dictionary>` is in the :ref:`dictionary<what is a dictionary?>`

* I change the expectation to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 182
    :emphasize-lines: 3

            self.assertEqual(
                a_dictionary.setdefault('key', 'default'),
                'value'
            )

  the test passes.

  .. note::

    setdefault_ has a :ref:`condition<if statements>`

    - if the :ref:`key<test_keys_of_a_dictionary>` is NOT in the :ref:`dictionary<what is a dictionary?>` it adds it with a default value of :ref:`None<what is None?>` and returns :ref:`None<what is None?>`
    - if the :ref:`key<test_keys_of_a_dictionary>` is NOT in the :ref:`dictionary<what is a dictionary?>` and I call setdefault_ with a second argument, it adds the :ref:`key<test_keys_of_a_dictionary>` to the :ref:`dictionary<what is a dictionary?>` with the second argument as the :ref:`value<test_values_of_a_dictionary>` and returns the second argument
    - if the :ref:`key<test_keys_of_a_dictionary>` is in the :ref:`dictionary<what is a dictionary?>` it returns its :ref:`value<test_values_of_a_dictionary>` from the :ref:`dictionary<what is a dictionary?>`

* I change the name of the test

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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
    :caption: dictionaries/tests/test_dictionaries.py
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

----

* I add a test for the next :ref:`method<what is a method?>` from the TODO list

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

* I add an :ref:`assertion<what is an assertion?>` to see what it did to the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 194
    :emphasize-lines: 4

        def test_update(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.update())
            self.assertEqual(a_dictionary, {})

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {'key': 'value'} != {}

  the :ref:`dictionary<what is a dictionary?>` did not change

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the values in the expectation to match the terminal_

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 197
  :emphasize-lines: 1

          self.assertEqual(a_dictionary, {'key': 'value'})

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a value to the call to the `update method`_ to see what happens

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 194
    :emphasize-lines: 3

        def test_update(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.update(0))
            self.assertEqual(a_dictionary, {'key': 'value'})

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :caption: terminal

    TypeError: 'int' object is not iterable

* I change the value to a tuple_

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 196
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.update((0, 1)))

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :caption: terminal

    TypeError: cannot convert dictionary update sequence element #0 to a sequence

  I had the same error message when I tried to :ref:`make a dictionary with things in it<test_making_a_dictionary>`

* I try a :ref:`keyword argument<test_keyword_arguments>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 196
    :emphasize-lines: 1

            self.assertIsNone(a_dictionary.update(new_key=[0, 1, 2, 'n']))

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {'key': 'value', 'new_key': [0, 1, 2, 'n']} != {'key': 'value'}

* I add the new :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to the expectation

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` to see what happens when I give a :ref:`key<test_keys_of_a_dictionary>` that is already in the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 194
    :emphasize-lines: 4

        def test_update(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(a_dictionary.update(new_key=[0, 1, 2, 'n']))
            self.assertIsNone(a_dictionary.update(key='updated value'))
            self.assertEqual(

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {'key': 'updated value', 'new_key': [0, 1, 2, 'n']} != {'key': 'value', 'new_key': [0, 1, 2, 'n']}

  the `update method`_ changes the :ref:`value<test_values_of_a_dictionary>` for a :ref:`key<test_keys_of_a_dictionary>` that is already in a :ref:`dictionary<what is a dictionary?>`

* I change the expectation to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 198
    :emphasize-lines: 4

            self.assertEqual(
                a_dictionary,
                {
                    'key': 'updated value',
                    'new_key': [0, 1, 2, 'n'],
                }
            )

  the test passes.

* since the `update method`_ takes :ref:`keyword arguments<test_keyword_arguments>`, I can give it a :ref:`dictionary<what is a dictionary?>` as input. I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: {'key[14 chars]lue', 'new_key': [0, 1, 2, 'n'], 'another_key': {0, 1, 2, 'n'}} != {'key[14 chars]lue', 'new_key': [0, 1, 2, 'n']}

  I can use the `update method`_ to add :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` from one :ref:`dictionary<what is a dictionary?>` to another

* I change the expectation in the :ref:`assertEqual method<test_assertEqual>` to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

  the test passes.

* I change the name of the test

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

  the test is still green.

* I remove update_ from the TODO list

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

----

I add a test for the last :ref:`method<what is a method?>` in my TODO list

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
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

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: dict_values(['value']) is not None

this is like :ref:`test_items_returns_iterable_of_key_value_pairs_of_a_dictionary` and  :ref:`test_keys_of_a_dictionary`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the expected value

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 210
    :emphasize-lines: 3-6

        def test_values(self):
            a_dictionary = {'key': 'value'}
            self.assertIsNone(
                a_dictionary.values,
                dict_values(['value'])
            )

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python
    :caption: terminal

    NameError: name 'dict_values' is not defined

* I remove the things around the :ref:`list<what is a list?>` in the ``dict_values`` :ref:`object<everything is an object>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 212
    :emphasize-lines: 3

            self.assertIsNone(
                a_dictionary.values(),
                ['value']
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: dict_values(['value']) is not None : ['value']

* I use ``list()`` to see if ``dict_values`` is :ref:`iterable<what is an iterable?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 212
    :emphasize-lines: 2

            self.assertIsNone(
                list(a_dictionary.values()),
                ['value']
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: ['value'] is not None : ['value']

* I change :ref:`assertIsNone<another way to test if something is None>` to :ref:`assertEqual<test_assertEqual>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 212
    :emphasize-lines: 1

            self.assertEqual(
                list(a_dictionary.values()),
                ['value']
            )

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`dictionary<what is a dictionary?>` to see what happens when it has more than one :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 210
    :emphasize-lines: 2-5

        def test_values(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                list(a_dictionary.values()),
                ['value']
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: ['value0', [0, 1, 2, 'n']] != ['value']

* I change the values in the expectation

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 215
    :emphasize-lines: 3-6

            self.assertEqual(
                list(a_dictionary.values()),
                [
                    'value0',
                    [0, 1, 2, 'n'],
                ]
            )

  the test passes.

* I change the name of the test

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 210
    :emphasize-lines: 1

        def test_values_of_a_dictionary(self):
            a_dictionary = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            self.assertEqual(
                list(a_dictionary.values()),
                [
                    'value0',
                    [0, 1, 2, 'n'],
                ]
            )


    'values'

* I remove values_ from the TODO list

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 215

            self.assertEqual(
                list(a_dictionary.values()),
                [
                    'value0',
                    [0, 1, 2, 'n']
                ]
            )


    # Exceptions seen

:ref:`I know how to look at the values of a dictionary<test_values_of_a_dictionary>`

----

*********************************************************************************
test_key_error
*********************************************************************************

`KeyError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#KeyError>`_ is an important :ref:`Exception<how to test that an Exception is raised>` to know when working with a :ref:`dictionary<what is a dictionary?>`. It happened earlier in :ref:`my test for the pop method<test_pop_removes_given_key_from_a_dictionary_and_returns_its_value>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for getting the :ref:`value<test_values_of_a_dictionary>` of a :ref:`key<test_keys_of_a_dictionary>` that is in a :ref:`dictionary<what is a dictionary?>`

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 215
  :emphasize-lines: 9-11

          self.assertEqual(
              list(a_dictionary.values()),
              [
                  'value0',
                  [0, 1, 2, 'n']
              ]
          )

      def test_key_error(self):
          a_dictionary = {'key': 'value'}
          self.assertEqual(a_dictionary['key'], '')


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: 'value' != ''

I get ``'value'`` back. I can get the value for a :ref:`key<test_key_error>` in a :ref:`dictionary<what is a dictionary?>` by giving the :ref:`key<test_key_error>` in ``[]``, the same way :ref:`I can get items from a list <test_getting_items_of_a_list>` by giving the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` in ``[]``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the value in the expectation to match the terminal_

.. code-block:: python
  :caption: dictionaries/tests/test_dictionaries.py
  :lineno-start: 225
  :emphasize-lines: 1

          self.assertEqual(a_dictionary['key'], 'value')

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`, this time for a :ref:`key<test_keys_of_a_dictionary>` that is not in the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 225
    :emphasize-lines: 2

            self.assertEqual(a_dictionary['key'], 'value')
            self.assertEqual(a_dictionary['not_in_dictionary'])

  the terminal_ is my friend, and shows :ref:`KeyError<test_key_error>`

  .. code-block:: python
    :caption: terminal

    KeyError: 'not_in_dictionary'

* I change the :ref:`assertEqual method<test_assertEqual>` to :ref:`assertRaises<another way to test if an Exception is raised>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 225
    :emphasize-lines: 3-4

            self.assertEqual(a_dictionary['key'], 'value')

            with self.assertRaises(KeyError):
                a_dictionary['not_in_dictionary']

  the test passes.

* I can use the `get method`_ when I do not want to get :ref:`KeyError<test_key_error>` with a :ref:`key<test_keys_of_a_dictionary>` that is not in a :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 227
    :emphasize-lines: 3-6

            with self.assertRaises(KeyError):
                a_dictionary['not_in_dictionary']
            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                ''
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 'default' != ''

* I change the expectation

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 229
    :emphasize-lines: 3

            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                'default'
            )

  the test passes. This is a repetition of :ref:`test_get_value_of_a_key_in_a_dictionary`, here is another one

* The `pop method`_ raised :ref:`KeyError<test_key_error>` when I gave it a :ref:`key<test_keys_of_a_dictionary>` that was not in the :ref:`dictionary<what is a dictionary?>`, I add a failing line for it

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 229
    :emphasize-lines: 6

            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                'default'
            )

            a_dictionary.pop('not_in_dictionary')

  the terminal_ is my friend, and shows :ref:`KeyError<test_key_error>`

  .. code-block:: python
    :caption: terminal

    KeyError: 'not_in_dictionary'

* I add :ref:`assertRaises<another way to test if an Exception is raised>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 229
    :emphasize-lines: 6-7

            self.assertEqual(
                a_dictionary.get('not_in_dictionary', 'default'),
                'default'
            )

            with self.assertRaises(KeyError):
                a_dictionary.pop('not_in_dictionary')

  the test passes.

* I can give a second argument when I do not want the `pop method`_ to raise :ref:`KeyError<test_key_error>` when the :ref:`key<test_keys_of_a_dictionary>` is not in the :ref:`dictionary<what is a dictionary?>`. I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 234
    :emphasize-lines: 3-6

            with self.assertRaises(KeyError):
                a_dictionary.pop('not_in_dictionary')
            self.assertEqual(
                a_dictionary.pop('not_in_dictionary', 'default'),
                ''
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 'default' != ''

* I change the expectation to match

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
    :lineno-start: 236
    :emphasize-lines: 3

            self.assertEqual(
                a_dictionary.pop('not_in_dictionary', 'default'),
                'default'
            )

  the test passes.

* The `popitem method`_ also raises :ref:`KeyError<test_key_error>` when called on an empty :ref:`dictionary<what is a dictionary?>`

  .. code-block::
    :lineno-start: 236
    :emphasize-lines: 6

            self.assertEqual(
                a_dictionary.pop('not_in_dictionary', 'default'),
                'default'
            )

            {}.popitem()

  the terminal_ is my friend, and shows :ref:`KeyError<test_key_error>`

  .. code-block:: python
    :caption: terminal

    KeyError: 'popitem(): dictionary is empty'

  I cannot remove the last :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` from a :ref:`dictionary<what is a dictionary?>` that has no :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`

* I add :ref:`assertRaises<another way to test if an Exception is raised>`

  .. code-block:: python
    :caption: dictionaries/tests/test_dictionaries.py
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

  the test passes.

:ref:`I know what causes KeyError<test_key_error>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_dictionaries.py``

* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``dictionaries``

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

  the terminal_ is my friend, and shows

  .. code-block:: PowerShell

    ...\pumping_python

  I am back in the ``pumping_python`` directory_.


----

*********************************************************************************
review
*********************************************************************************

Dictionaries_ are also known as Mappings, they contain :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` and any :ref:`object<everything is an object>` can be used as values.

I ran tests to show that I can make a :ref:`dictionary<what is a dictionary?>` with ``dict()`` or curly braces ``{}``, then I ran these tests to see what :ref:`Python basic data types<basic objects>` I can use as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`

* :ref:`test_making_a_dictionary_w_none_as_a_key`
* :ref:`test_making_a_dictionary_w_a_boolean_as_a_key`
* :ref:`test_making_a_dictionary_w_a_number_as_a_key`
* :ref:`test_making_a_dictionary_w_a_tuple_as_a_key`
* :ref:`test_making_a_dictionary_w_a_list_as_a_key`
* :ref:`test_making_a_dictionary_w_a_set_as_a_key`
* :ref:`test_making_a_dictionary_w_a_dictionary_as_a_key`

I also ran these tests for the :ref:`methods of dictionaries<test_dir_dict>`

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

and a test for the important :ref:`Exception<how to test that an Exception is raised>` to know when working with :ref:`dictionaries<what is a dictionary?>` - :ref:`KeyError<test_key_error>`

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

* :ref:`I know how to make a Python Test Driven Development environment manually<how to make a Python Test Driven Development environment manually>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`I know what causes AttributeError<what causes AttributeError?>`.
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`I know how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions in programs>`
* :ref:`how to raise TypeError<what causes TypeError?>`
* :ref:`what you can do with Lists<what is a list?>`
* :ref:`how to use list comprehensions<list comprehensions>`
* :ref:`what you can do with dictionaries<dictionaries>`

:ref:`Would you like to use dictionaries in the calculator tests?<how to make a calculator 6>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->