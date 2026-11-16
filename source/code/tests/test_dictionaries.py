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
            {[3, 2, 1]: 'BOOM!!!'}

    def test_making_a_dictionary_w_a_set_as_a_key(self):
        with self.assertRaises(TypeError):
            {{3, 2, 1}: 'BOOM!!!'}

    def test_making_a_dictionary_w_a_dictionary_as_a_key(self):
        a_dictionary = {'key': 'value'}
        with self.assertRaises(TypeError):
            {a_dictionary: 'BOOM!!!'}

    def test_dir_dict(self):
        self.maxDiff = None
        dir_dict = dir(object)
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

    def test_clear_empties_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(a_dictionary.clear())
        self.assertEqual(a_dictionary, {})

    def test_copy_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(
            a_dictionary.copy(),
            {'key': 'value'}
        )

    def test_fromkeys_makes_a_dictionary_from_an_iterable(self):
        self.assertEqual(
            dict.fromkeys((0, 1)),
            {0: None, 1: None}
        )
        self.assertEqual(
            dict.fromkeys((0, 1), 'default'),
            {0: 'default', 1: 'default'}
        )
        self.assertEqual(
            {key: 'value' for key in (0, 1)},
            {0: 'value', 1: 'value'}
        )

    def test_get_value_of_a_key_in_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertIsNone(
            a_dictionary.get('not in dictionary')
        )
        self.assertEqual(
            a_dictionary.get(
                'not in dictionary', 'default'
            ),
            'default'
        )
        self.assertEqual(
            a_dictionary.get('key', 'default'),
            'value'
        )

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

    def test_keys_of_a_dictionary(self):
        a_dictionary = {
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        }
        self.assertEqual(
            list(a_dictionary.keys()),
            ['key0', 'keyN']
        )

    def test_pop_removes_given_key_from_a_dictionary_and_returns_its_value(self):
        a_dictionary = {'key': 'value'}

        with self.assertRaises(KeyError):
            a_dictionary.pop('not_in_dictionary')

        self.assertIsNone(
            a_dictionary.pop('not_in_dictionary',  None)
        )
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
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        }
        self.assertEqual(
            a_dictionary.popitem(),
            ('keyN', [0, 1, 2, 'n'])
        )
        self.assertEqual(a_dictionary, {'key0': 'value0'})

    def test_setdefault_adds_given_key_to_a_dictionary(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(
            a_dictionary.setdefault('new_key', 'new value'),
            'new value'
        )
        self.assertEqual(
            a_dictionary.setdefault('key', 'default'),
            'value'
        )
        self.assertEqual(
            a_dictionary,
            {
                'key': 'value',
                'new_key': 'new value',
            }
        )

    def test_update_a_dictionary(self):
        a_dictionary = {'key': 'value'}

        for key, value in (
            ('key', 'updated value'),
            ('new_key', [0, 1, 2, 'n']),
            ('another_key', {0, 1, 2, 'n'}),
        ):
            self.assertIsNone(
                a_dictionary.update({key: value})
            )

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
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        }
        self.assertEqual(
            list(a_dictionary.values()),
            ['value0', [0, 1, 2, 'n']]
        )

    def test_key_error(self):
        a_dictionary = {'key': 'value'}
        self.assertEqual(
            a_dictionary['key'], 'value'
        )

        with self.assertRaises(KeyError):
            a_dictionary['not_in_dictionary']
        self.assertEqual(
            a_dictionary.get(
                'not_in_dictionary', 'default'
            ),
            'default'
        )

        with self.assertRaises(KeyError):
            a_dictionary.pop('not_in_dictionary')
        self.assertEqual(
            a_dictionary.pop(
                'not_in_dictionary', 'default'
            ),
            'default'
        )

        with self.assertRaises(KeyError):
            {}.popitem()


# Exceptions seen
# AssertionError
# TypeError
# NameError
# KeyError