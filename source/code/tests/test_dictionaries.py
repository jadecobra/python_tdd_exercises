import src.dictionaries
import unittest


class TestDictionaries(unittest.TestCase):

    def test_make_a_dictionary_w_dict_constructor(self):
        self.assertEqual(dict(key='value'), {'key': 'value'})

    def test_make_a_dictionary_w_curly_braces(self):
        self.assertEqual({'key': 'value'}, dict(key='value'))

    def test_make_a_dictionary_w_numbers_as_keys(self):
        self.assertEqual({0: 'boom'}, {0: 'boom'})
        self.assertEqual({0.1: 'bap'}, {0.1: 'bap'})

    def test_make_a_dictionary_w_booleans_as_keys(self):
        self.assertEqual({False: 'boom'}, {False: 'boom'})
        self.assertEqual({True: 'bap'}, {True: 'bap'})

    def test_make_a_dictionary_w_tuples_as_keys(self):
        self.assertEqual(
            {(0, 1): 'value'},
            {(0, 1): 'value'}
        )

    def test_make_a_dictionary_w_lists_as_keys(self):
        with self.assertRaises(TypeError):
            {[3, 2, 1]: 'BOOM!'}

    def test_make_a_dictionary_w_sets_as_keys(self):
        with self.assertRaises(TypeError):
            {{3, 2, 1}: 'BOOM!'}

    def test_make_a_dictionary_w_dictionaries_as_keys(self):
        a_dictionary = {'key': 'value'}
        with self.assertRaises(TypeError):
            {a_dictionary: 'BOOM!'}

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

    def test_clear_empties_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(a_dictionary.clear())
        self.assertEqual(a_dictionary, {})

    def test_copy_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary.copy(), {'key': 'value'})
        self.assertEqual(a_dictionary, {'key': 'value'})

    def test_fromkeys_makes_a_dictionary_from_an_iterable(self):
        self.assertEqual(
            dict.fromkeys((0, 1, 2, 3)),
            {0: None, 1: None, 2: None, 3: None}
        )

    def test_get_value_of_key_from_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary.get('key'), 'value')
        self.assertIsNone(a_dictionary.get(0))

    def test_items_returns_keys_and_values_of_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(list(a_dictionary.items()), [('key', 'value')])

    def test_keys_of_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(list(a_dictionary.keys()), ['key'])

    def test_pop_removes_and_returns_key_w_value_from_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary.pop('key'), 'value')
        self.assertEqual(a_dictionary, {})

        with self.assertRaises(KeyError):
            a_dictionary.pop(0)

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

    def test_values_of_a_dictionary(self):
        a_dictionary = {
            'a_key': 'a value',
            'another_key': 'another value',
        }
        self.assertEqual(
            list(a_dictionary.values()),
            ['a value', 'another value']
        )

    def test_key_error(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(a_dictionary['key'], 'value')

        with self.assertRaises(KeyError):
            a_dictionary['this_key_does_not_exist']
        with self.assertRaises(KeyError):
            {}.popitem()
        with self.assertRaises(KeyError):
            a_dictionary.pop('this_key_does_not_exist')

        self.assertIsNone(a_dictionary.get('this_key_does_not_exist'))


# Exceptions Encountered
# AssertionError
# TypeError
