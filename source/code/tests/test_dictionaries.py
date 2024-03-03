import dictionaries
import unittest


class TestDictionaries(unittest.TestCase):

    def test_making_dictionaries_with_strings_as_keys(self):
        self.assertEqual(
            dictionaries.a_dict(),
            {"key": "value"}
        )
        self.assertEqual(
            dictionaries.a_dict(),
            dict(key='value')
        )
        self.assertEqual(
            {"key": "value"},
            dict(key='value')
        )

    def test_making_dictionaries_with_numbers_as_keys(self):
        self.assertEqual(
            {1: 'boom'},
            {1: 'boom'}
        )
        self.assertEqual(
            {2.5: 'works'},
            {2.5: 'works'}
        )

    def test_making_dictionaries_with_booleans_as_keys(self):
        self.assertEqual(
            {False: 'boom'},
            {False: 'boom'}
        )
        self.assertEqual(
            {True: 'bap'},
            {True: 'bap'}
        )

    def test_making_dictionaries_with_tuples_as_keys(self):
        self.assertEqual(
            {(1, 2): "value"},
            {(1, 2): "value"}
        )

    def test_making_dictionaries_with_lists_as_keys(self):
        with self.assertRaises(TypeError):
            {[1, 2]: "BOOM"}

    def test_making_dictionaries_with_sets_as_keys(self):
        with self.assertRaises(TypeError):
            {{1, 2}: "BOOM"}

    def test_making_dictionaries_with_dictionaries_as_keys(self):
        a_dictionary = {"key": "value"}
        with self.assertRaises(TypeError):
            {a_dictionary: "BOOM"}

    def test_accessing_dictionary_values(self):
        a_dictionary = {"key": "value"}
        self.assertEqual(a_dictionary["key"], "value")

    def test_listing_dictionary_values(self):
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

    def test_listing_dictionary_keys(self):
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

    def test_how_to_get_a_value_when_a_key_does_not_exist(self):
        a_dictionary = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'keyN': 'valueN',
        }
        self.assertIsNone(a_dictionary.get('non_existent_key'))
        self.assertIsNone(a_dictionary.get('non_existent_key', None))
        self.assertEqual(a_dictionary.get('key1', None), 'value1')

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

    def test_set_default_for_a_given_key(self):
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

        a_dictionary.setdefault('a_new_key', 'a_default_value')
        self.assertEqual(
            a_dictionary,
            {
                'bippity': 'boppity',
                'another_key': None,
                'a_new_key': 'a_default_value',
            }
        )

    def test_adding_two_dictionaries(self):
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

    def test_pop(self):
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


# Exceptions Encountered
# ModuleNotFoundError
# AttributeError
# TypeError
# KeyError