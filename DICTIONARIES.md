# Dictionaries

We are going to cover dictionaries in python In this chapter using Test Driven Development

### Prerequisites

- [Setup a Test Driven Development Environment](./TDD_SETUP.md)
- [Data Structures](./DATA_STRUCTURES.md)

---

## How to create a dictionary with strings as keys

Dictionaries/Mappings are key, value pairs that we can use to represent data. `values` can be any of the [data structures](./DATA_STRUCTURES.md) including dictionaries

### <span style="color:red">**RED**</span>: make it fail

first we add a file named `test_dictionaries.py` to the `tests` folder with the following text

```python
import unittest
import dictionaries
```

the terminal gives us a [ModuleNotFoundError](./MODULE_NOT_FOUND_ERROR.md), and we add it to our list of exceptions encountered
```python
# Exceptions Encountered
# ModuleNotFoundError
```

### <span style="color:green">**GREEN**</span>: make it pass

add a file named `dictionaries.py` to the project folder and the test passes

### <span style="color:orange">**REFACTOR**</span>: make it better

- we will now proceed to look at the ways we can create a dictionary, by adding a failing test
    ```python


    class TestDictionaries(unittest.TestCase):

        def test_creating_dictionaries_with_strings_as_keys(self):
            self.assertEqual(dictionaries.a_dict(), {"key": "value"})
    ```
    the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md) and we add it to our list of exceptions encountered
    ```python
    # Exceptions Encountered
    # ModuleNotFoundError
    # AttributeError
    ```
- add a definition for a function to `dictionaries.py`
    ```python
    def a_dict():
        return None
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md) since the function we defined returns `None` not a dictionary
- update the return statement to return an empty dictionary
    ```python
    def a_dict():
        return {}
    ```
    the terminal still shows an [AssertionError](./ASSERTION_ERROR.md) but now our return value looks more like what is expected
    ```python
    E       AssertionError: {} != {'key': 'value'}
    E       - {}
    E       + {'key': 'value'}
    ```
    - the value on the left `{}` is what our function returns and the value on the right `{'key': 'value'}` is what is expected
    - the `!=` symbol means `not equal to`
- update the return statement with the expected values
    ```python
    def a_dict():
        return {'key': 'value'}
    ```
    ***VOILA!*** The tests pass and you now know how to create a `dictionary`
- it is also possible to create a dictionary by using the `dict` keyword. add another test to `test_creating_dictionaries_with_strings_as_keys`
    ```python
    def test_creating_dictionaries_with_strings_as_keys(self):
        self.assertEqual(dictionaries.a_dict(), {'key': 'value'})
        self.assertEqual(dictionaries.a_dict(), dict(key='value'))
    ```
    the terminal shows passing tests, which means `dict(key='value')` and `{'key': 'value'}` produce the same results
- we can add another test to confirm this assumption even though it repeats the two tests above
    ```python
    def test_creating_dictionaries_with_strings_as_keys(self):
        self.assertEqual(dictionaries.a_dict(), {"key": "value"})
        self.assertEqual(dictionaries.a_dict(), dict(key='value'))
        self.assertEqual({"key": "value"}, dict(key='value'))
    ```

## How to create a dictionary with numbers as keys

### <span style="color:red">**RED**</span>: make it fail

add a failing test to `TestDictionaries`

```python
    def test_creating_dictionaries_with_numbers_as_keys(self):
        self.assertEqual({1: 'boom'}, {'one': 'boom'})
```

the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md) since the two values are different

### <span style="color:green">**GREEN**</span>: make it pass

update the test to make it pass

```python
    def test_creating_dictionaries_with_numbers_as_keys(self):
        self.assertEqual({1: 'boom'}, {1: 'boom'})
```

the terminal updates to show passing tests

### <span style="color:orange">**REFACTOR**</span>: make it better

- Our knowledge of dictionaries is growing. We know we can use `integers` and `strings` as dictionary keys. Can we use `floats`? We are going to find out by adding a test
    ```python
        def test_creating_dictionaries_with_numbers_as_keys(self):
            self.assertEqual({1: 'boom'}, {'one': 'boom'})
            self.assertEqual({2.5: 'works'}, {2.5: 'fails'})
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md) since the values are different
- update the value on the right to make it pass
    ```python
    def test_creating_dictionaries_with_numbers_as_keys(self):
        self.assertEqual({1: 'boom'}, {'one': 'boom'})
        self.assertEqual({2.5: 'works'}, {2.5: 'works'})
    ```
    the terminal shows passing tests

## How to create a dictionary with booleans as keys

Is it possible for us to use `False` or `True` as `dictionary` keys?

### <span style="color:red">**RED**</span>: make it fail

```python
    def test_creating_dictionaries_with_booleans_as_keys(self):
        self.assertEqual({False: 'boom'}, {False: 'bap'})
```

the terminal shows an [AssertionError](./ASSERTION_ERROR.md)

### <span style="color:green">**GREEN**</span>: make it pass

update the return values to make them match and we are green again

```python
    def test_creating_dictionaries_with_booleans_as_keys(self):
        self.assertEqual({False: 'boom'}, {False: 'boom'})
```

### <span style="color:orange">**REFACTOR**</span>: make it better

- add a test for using `True` as a `dictionary` key
    ```python
    def test_creating_dictionaries_with_booleans_as_keys(self):
        self.assertEqual({False: 'boom'}, {False: 'boom'})
        self.assertEqual({True: 'bap'}, {True: 'boom'})
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)
- update the values to make the tests pass
    ```python
    def test_creating_dictionaries_with_booleans_as_keys(self):
        self.assertEqual({False: 'boom'}, {False: 'boom'})
        self.assertEqual({True: 'bap'}, {True: 'bap'})
    ```
- We now know that we can use `booleans`, `floats`, `integers` and `strings` as keys in a dictionary

## How to create a dictionary with tuples as keys

### <span style="color:red">**RED**</span>: make it fail

add a test to `TestDictionaries`

```python
    def test_creating_dictionaries_with_tuples_as_keys(self):
        self.assertEqual({(1, 2): "value"}, {(1, 2): "key"})
```

the terminal shows an [AssertionError](./ASSERTION_ERROR.md)

### <span style="color:green">**GREEN**</span>: make it pass

we update the values to make it pass

```python
        self.assertEqual({(1, 2): "value"}, {(1, 2): "value"})
```

and update our knowledge of creating dictionaries to say we can use `tuples`, `booleans`, `floats`, `integers`, and `strings` as keys in a dictionary

## Can we create a Dictionary with lists as keys?

### <span style="color:red">**RED**</span>: make it fail

let us add a test to `TestDictionaries` using a list as a key

```python
    def test_creating_dictionaries_with_lists_as_keys(self):
        {[1, 2]: "BOOM"}
```

the terminal shows a [TypeError](./ASSERTION_ERROR.md) because only `hashable` types can be used as dictionary keys and [lists](./LISTS.md) are not `hashable`
```
E       TypeError: unhashable type: 'list'
```

we also update our list of exceptions encountered
```python
# Exceptions Encountered
# ModuleNotFoundError
# AttributeError
# TypeError
```

### <span style="color:green">**GREEN**</span>: make it pass

In [Exception Handling](./EXCEPTION_HANDLING.md) we learn how to use `self.assertRaises` to confirm that an error is raised by some code without having it crash our tests. We will do the same here to confirm that creating a dictionary with a `list` as the key raises a [TypeError](./TYPE_ERROR.md)

```python
    def test_creating_dictionaries_with_lists_as_keys(self):
        with self.assertRaises(TypeError):
            {[1, 2]: "BOOM"}
```

all green here

## Can we create a Dictionary with sets as keys?

### <span style="color:red">**RED**</span>: make it fail
let us try a similar test using a set as a key

```python
    def test_creating_dictionaries_with_sets_as_keys(self):
        {{1, 2}: "BOOM"}
```

the terminal shows a [TypeError](./ASSERTION_ERROR.md)

### <span style="color:green">**GREEN**</span>: make it pass
which we handle using `self.assertRaises`
```python
    def test_creating_dictionaries_with_sets_as_keys(self):
        with self.assertRaises(TypeError):
            {{1, 2}: "BOOM"}
```

all tests are passing

## Can we create a Dictionary with dictionaries as keys?

### <span style="color:red">**RED**</span>: make it fail
add a new test
```python
    def test_creating_dictionaries_with_dictionaries_as_keys(self):
        a_dictionary = {"key": "value"}
        {a_dictionary: "BOOM"}
```

and the terminal shows a [TypeError](./TYPE_ERROR.md)

### <span style="color:green">**GREEN**</span>: make it pass
we add a handler to confirm our findings
```python
    def test_creating_dictionaries_with_dictionaries_as_keys(self):
        a_dictionary = {"key": "value"}
        with self.assertRaises(TypeError):
            {a_dictionary: "BOOM"}
```

all tests pass and we now know that we can create dictionaries with the following [data structures](./DATA_STRUCTURES.md) as keys
- strings
- booleans
- integers
- floats
- tuples

---

## How to access dictionary values

From the tests above we learned how to create `dictionaries`, and what we can use as `keys`. How do we access the values of a dictionary?
### <span style="color:red">**RED**</span>: make it fail

we are going to add a test to `TestDictionaries` in `test_dictionaries.py`

```python
    def test_accessing_dictionary_values(self):
        a_dictionary = {"key": "value"}
        self.assertEqual(a_dictionary["key"], "bob")
```

the terminal displays a failing test with an [AssertionError](./ASSERTION_ERROR.md) because `bob` is not equal to `value`

### <span style="color:green">**GREEN**</span>: make it pass

update the expected value to make the tests pass

```python
    def test_accessing_dictionary_values(self):
        a_dictionary = {"key": "value"}
        self.assertEqual(a_dictionary["key"], "value")
```

### <span style="color:orange">**REFACTOR**</span>: make it better

- we can also display the values of a dictionary as a list without the keys, add a test
    ```python
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
    ```
    the terminal gives us an [AssertionError](./ASSERTION_ERROR.md)
- update the values to make the test pass
    ```python
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
    ```
- we can do the same thing with the keys of the dictionary, add another test
    ```python
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
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)
- update the test to make it pass
    ```python
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
    ```

## How to get a value when the key does not exist

Sometimes we might try to access values in a dictionary but use a key that does not exist in the dictionary or misspell a key that does exist
### <span style="color:red">**RED**</span>: make it fail

add a test

```python
    def test_dictionaries_raise_key_error_when_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        a_dictionary['non_existent_key']
        a_dictionary['ky1']
```

the terminal updates to show a [KeyError](https://docs.python.org/3/library/exceptions.html?highlight=keyerror#KeyError). A `KeyError` is raised when a `dictionary` is called with a `key` that does not exist.

### <span style="color:green">**GREEN**</span>: make it pass

- add `KeyError` to our running list of list of exceptions encountered
    ```python
    # Exceptions Encountered
    # ModuleNotFoundError
    # AttributeError
    # TypeError
    # KeyError
    ```
- let us add an exception handler to make it pass
    ```python
        def test_dictionaries_raise_key_error_when_key_does_not_exist(self):
            a_dictionary = {
                'key1': 'value1',
                'key2': 'value2',
                'key3': 'value3',
                'keyN': 'valueN',
            }
            with self.assertRaises(KeyError):
                a_dictionary['non_existent_key']
    ```
- the terminal shows a `KeyError` for the next line where we misspelled the key and we add it to the exception handler to make it pass
    ```python
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
    ```

### <span style="color:orange">**REFACTOR**</span>: make it better

What if we want to call a dictionary and not have python raise an error when it does not find the key? We could use the `get` function
- add a test to `TestDictionaries`
    ```python
    def test_how_to_get_a_value_when_a_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary['non_existent_key'])
    ```
    as expected the terminal updates to show a `KeyError`
- update the test using the `get` method
    ```python
    def test_how_to_get_a_value_when_a_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary.get('non_existent_key'))
    ```
    the terminal updates to show a passing test. This means that when we use the `get` method and the `key` does not exist, we get `None` as the `return` value.
- let us state the above explicitly because `Explicit is better than implicit` see [Zen of Python](https://peps.python.org/pep-0020/)
    ```python
    def test_how_to_get_a_value_when_a_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary.get('non_existent_key'))
        self.assertIsNone(a_dictionary.get('non_existent_key', None))
    ```
    the terminal shows passing tests. The `get` method takes in 2 inputs
        - the `key`
        - the `value` it should return if the `key` does not exist
- If you have gone through [Exception Handling](./EXCEPTION_HANDLING.md), we can assume the definition of the [get](https://docs.python.org/3/library/stdtypes.html#dict.get) method of the dictionary object looks something like this
    ```python
    def get(dictionary, key, default=None):
        try:
            return dictionary[key]
        except KeyError:
            return default
    ```
- let us try the `get` method with an existing key
    ```python
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
    ```
    the terminal updates to show an [Assertion Error](./ASSERTION_ERROR.md) because `value1` is not equal to `None`
- update the test to make it pass

## How to view the attributes and methods of a dictionary

[Classes](./CLASSES.md) covers how to view the `attributes` and `methods` of an object. let us do the same for `dictionaries`

### <span style="color:red">**RED**</span>: make it fail

add a test to `TestDictionaries`

```python
    def test_dictionary_attributes(self):
        self.maxDiff = None
        self.assertEqual(
            dir(dictionaries.a_dict()),
            []
        )
```

the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)

### <span style="color:green">**GREEN**</span>: make it pass

copy the expected values shown in the terminal to make the test pass
> WARNING: Your results may vary depending on your python version

```python
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
```

the tests pass

### <span style="color:orange">**REFACTOR**</span>: make it better

We see some of the methods we have covered so far and others we did not. You can write tests on the others to discover what they do and/or [read more about dictionaries](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict). let us list out what we know so far and you can fill in the others as you learn them
- clear
- copy
- fromkeys
- get - gets the `value` for a `key` and returns a default value or `None` if the key does not exist
- items
- keys - returns the list of `keys` in a dictionary
- pop
- popitem
- setdefault
- update
- values - returns the list of `values` in a dictionary

## How to set a default value for a given key

let us test the `setdefault` method

### <span style="color:red">**RED**</span>: make it fail

add a failing test

```python
    def test_set_default_for_a_given_key(self):
        a_dictionary = {'bippity': 'boppity'}
        a_dictionary['another_key']
```

the terminal updates to show a `KeyError`

### <span style="color:green">**GREEN**</span>: make it pass

add a `self.assertRaises` to confirm that the `KeyError` gets raised, allowing the test to pass

```python
    def test_set_default_for_a_given_key(self):
        a_dictionary = {'bippity': 'boppity'}

        with self.assertRaises(KeyError):
            a_dictionary['another_key']
```

### <span style="color:orange">**REFACTOR**</span>: make it better

- add a test for `setdefault`
    ```python
    def test_set_default_for_a_given_key(self):
        a_dictionary = {'bippity': 'boppity'}

        with self.assertRaises(KeyError):
            a_dictionary['another_key']

        a_dictionary.setdefault('another_key')
        self.assertEqual(a_dictionary, {'bippity': 'boppity'})
    ```
    the terminal updates to show that `a_dictionary` has changed, by giving us an [AssertionError](./ASSERTION_ERROR.md). It has a new key which was not there before
- update the test to make it pass
    ```python
    def test_set_default_for_a_given_key(self):
        a_dictionary = {'bippity': 'boppity'}

        with self.assertRaises(KeyError):
            a_dictionary['another_key']

        a_dictionary.setdefault('another_key')
        self.assertEqual(a_dictionary, {'bippity': 'boppity', 'another_key': None})
    ```
- What if we want to add a `key` but set the default value to something other than `None`? Good question, let us add a test to find out
    ```python
        a_dictionary.setdefault('a_new_key', 'a_default_value')
        self.assertEqual(a_dictionary, {'bippity': 'boppity', 'another_key': None})
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md) since `a_dictionary` now has a new `key` and `value`
- update the test to make it pass
    ```python
        self.assertEqual(
            a_dictionary,
            {
                'bippity': 'boppity',
                'another_key': None,
                'a_new_key': 'a_default_value',
            }
        )
    ```
    all tests pass, and we update the list of methods with what we now know about `setdefault`

## How to update a Dictionary with another dictionary

What if we have a dictionary and want to `add` the `keys` and `values` of another dictionary to it?

### <span style="color:red">**RED**</span>: make it fail

add a test to `TestDictionaries`

```python
    def test_adding_two_dictionaries(self):
        a_dictionary = {
            "basic": "toothpaste",
            "whitening": "peroxide",
        }
        a_dictionary.update({
            "non_basic": "chewing stick",
            "browning": "tobacco",
            "decaying": "sugar"
        })
        self.assertEqual(
            a_dictionary,
            {"basic": "toothpaste", "whitening": "peroxide"}
        )
```

the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md) because the values of `a_dictionary` were updated when we called the `update` method on it

### <span style="color:green">**GREEN**</span>: make it pass

update values to make it pass

## How to remove an item from a dictionary

We can remove an item from a dictionary with the `pop` method. It deletes the key and value from the dictionary and returns the value

### <span style="color:red">**RED**</span>: make it fail

add a failing test to `TestDictionaries`

```python
    def test_pop(self):
        a_dictionary = {
            "basic": "toothpaste",
            "whitening": "peroxide",
            "non_basic": "chewing stick",
            "browning": "tobacco",
            "decaying": "sugar"
        }
        self.assertEqual(a_dictionary.pop("basic"), None)
```

the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)

### <span style="color:green">**GREEN**</span>: make it pass

update the test with the right value to make it pass