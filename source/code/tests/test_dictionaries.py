import unittest


class TestDictionaries(unittest.TestCase):

    def test_making_a_dictionary(self):
        self.assertEqual(dict(), {})
        self.assertEqual(dict(key='value'), {'key': 'value'})

    def test_making_a_dictionary_w_none_as_a_key(self):
        self.assertEqual({None: 'boom'}, {None: 'boom'})

    def test_making_a_dictionary_w_a_boolean_as_a_key(self):
        self.assertEqual(
            {False: 'boom', True: 'bap'},
            {False: 'boom', True: 'bap'}
        )

    def test_making_a_dictionary_w_a_number_as_a_key(self):
        self.assertEqual(
            {0: 'boom', 0.1: 'bap'},
            {0: 'boom', 0.1: 'bap'}
        )

    def test_making_a_dictionary_w_a_tuple_as_a_key(self):
        self.assertEqual(
            {(0, 1): 'boom'},
            {(0, 1): 'boom'}
        )

    def test_making_a_dictionary_w_a_list_as_a_key(self):
        with self.assertRaises(TypeError):
            {[3, 2, 1]: 'BOOM!'}

    def test_making_a_dictionary_w_a_set_as_a_key(self):
        with self.assertRaises(TypeError):
            {{3, 2, 1}: 'BOOM!'}

    def test_making_a_dictionary_w_a_dictionary_as_a_key(self):
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

    def test_fromkeys_makes_a_dictionary_from_an_iterable(self):
        self.assertEqual(
            dict.fromkeys((0, 1), 'default'),
            {0: 'default', 1: 'default'}
        )

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

    def test_keys_of_a_dictionary(self):
        a_dictionary = {
            'key1': 'value1',
            'keyN': [0, 1, 2, 'n'],
        }
        self.assertEqual(
            list(a_dictionary.keys()),
            ['key1', 'keyN']
        )

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

    def test_update_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(a_dictionary.update(new_key=[0, 1, 2, 'n']))
        self.assertIsNone(a_dictionary.update(key='updated value'))
        self.assertIsNone(a_dictionary.update({'another_key': {0, 1, 2, 'n'}}))
        self.assertEqual(
            a_dictionary,
            {
                'key': 'updated value',
                'new_key': [0, 1, 2, 'n'],
                'another_key': {0, 1, 2, 'n'},
            }
        )

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


# Exceptions Encountered
# AssertionError
# TypeError
# NameError
# KeyError