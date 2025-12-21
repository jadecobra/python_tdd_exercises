import unittest


class TestStrings(unittest.TestCase):

    def test_making_a_string(self):
        self.assertEqual(str(), '')
        self.assertEqual(str(None), 'None')
        self.assertEqual(str(False), 'False')
        self.assertEqual(str(True), 'True')
        self.assertEqual(str(0), '0')
        self.assertEqual(str(0.0), '0.0')
        self.assertEqual(str((0, 1, 2, 'n')), "(0, 1, 2, 'n')")
        self.assertEqual(str([0,1 ,2 , 'n']), "[0, 1, 2, 'n']")
        self.assertEqual(str({0, 1, 2, 'n'}), "{0, 1, 2, 'n'}")
        self.assertEqual(str({'key': 'value'}), "{'key': 'value'}")

    def test_attributes_and_methods_of_strings(self):
        self.maxDiff = None
        self.assertEqual(
            dir(str),
            [
                '__add__',
                '__class__',
                '__contains__',
                '__delattr__',
                '__dir__',
                '__doc__',
                '__eq__',
                '__format__',
                '__ge__',
                '__getattribute__',
                '__getitem__',
                '__getnewargs__',
                '__getstate__',
                '__gt__',
                '__hash__',
                '__init__',
                '__init_subclass__',
                '__iter__',
                '__le__',
                '__len__',
                '__lt__',
                '__mod__',
                '__mul__',
                '__ne__',
                '__new__',
                '__reduce__',
                '__reduce_ex__',
                '__repr__',
                '__rmod__',
                '__rmul__',
                '__setattr__',
                '__sizeof__',
                '__str__',
                '__subclasshook__',
                'capitalize',
                'casefold',
                'center',
                'count',
                'encode',
                'endswith',
                'expandtabs',
                'find',
                'format',
                'format_map',
                'index',
                'isalnum',
                'isalpha',
                'isascii',
                'isdecimal',
                'isdigit',
                'isidentifier',
                'islower',
                'isnumeric',
                'isprintable',
                'isspace',
                'istitle',
                'isupper',
                'join',
                'ljust',
                'lower',
                'lstrip',
                'maketrans',
                'partition',
                'removeprefix',
                'removesuffix',
                'replace',
                'rfind',
                'rindex',
                'rjust',
                'rpartition',
                'rsplit',
                'rstrip',
                'split',
                'splitlines',
                'startswith',
                'strip',
                'swapcase',
                'title',
                'translate',
                'upper',
                'zfill',
            ]
        )

    def test_capitalize_a_string(self):
        a_string = 'text'
        self.assertEqual(a_string.capitalize(), 'Text')

    def test_casefold_removes_the_case_from_a_string(self):
        a_string = 'TeXt'
        self.assertEqual(a_string.casefold(), 'text')

    def test_center_a_string_with_characters(self):
        a_string = 'text'
        self.assertEqual(a_string.center(10), '   text   ')
        self.assertEqual(a_string.center(10, '-'), '---text---')

    def test_count_number_of_timems_given_item_is_in_a_string(self):
        a_string = 'text'
        self.assertEqual(a_string.count('not_in_string'), 0)
        self.assertEqual(a_string.count('t'), 2)
        self.assertEqual(a_string.count('e'), 1)
        self.assertEqual(a_string.count('x'), 1)

    def test_encode_returns_byte_version_of_string(self):
        a_string = 'text'
        self.assertEqual(a_string.encode(), b'text')
        self.assertEqual(a_string.encode(encoding='utf-8'), b'text')
        self.assertEqual(a_string.encode(encoding='utf-16'), b'\xff\xfet\x00e\x00x\x00t\x00')

    def test_endswith_checks_if_string_ends_with_given_string(self):
        a_string = 'text'
        self.assertFalse(a_string.endswith('0'))

        self.assertTrue(a_string.endswith('t'))
        self.assertTrue(a_string.endswith('xt'))

    def test_expandtabs_changes_tabs_to_spaces(self):
        a_string = '\ttext'
        self.assertEqual(a_string.expandtabs(), '        text')
        self.assertEqual(a_string.expandtabs(0), 'text')
        self.assertEqual(a_string.expandtabs(4), '    text')

    def test_find_position_a_string_in_a_string(self):
        a_string = 'text'
        self.assertEqual(a_string.find('0', 0), -1)
        self.assertEqual(a_string.find('t', 0), 0)
        self.assertEqual(a_string.find('e', 0),  1)
        self.assertEqual(a_string.find('x', 0), 2)
        self.assertEqual(a_string.find('t', 2),  3)
        self.assertEqual(a_string.find('ex'), 1)

    def test_format_allows_passing_values_to_a_string(self):
        name = 'joe'
        self.assertEqual(
            'Hello, my name is {name}'.format(name=name),
            'Hello, my name is joe'
        )

    def test_format_map_uses_a_dictionary_to_pass_values_to_a_string(self):
        a_dictionary = {
            'first_name': 'Jane',
            'last_name': 'Doe',
        }
        self.assertEqual(
            'My name is {first_name} {last_name}'.format_map(a_dictionary),
            'My name is Jane Doe'
        )

    def test_index(self):
        a_string = 'text'

        with self.assertRaises(ValueError):
            a_string.index('not_in_string')

        self.assertEqual(a_string.index('t', 0), 0)
        self.assertEqual(a_string.index('x', 0), 2)
        self.assertEqual(a_string.index('t', 1), 3)
        self.assertEqual(a_string.index('e', 0), 1)
        self.assertEqual(a_string.index('ex', 0), 1)

    def test_isalnum_checks_if_a_string_is_a_number_or_alphabet(self):
        self.assertFalse(''.isalnum())
        self.assertFalse('$'.isalnum())

        self.assertTrue('text'.isalnum())
        self.assertTrue('0'.isalnum())

    def test_isalpha_checks_if_a_string_is_alphabets_only(self):
        self.assertFalse(''.isalpha())
        self.assertFalse('1234'.isalpha())
        self.assertFalse('!@#$'.isalpha())
        self.assertFalse('å∫ç∂'.isalpha())

        self.assertTrue('text'.isalpha())

    def test_isascii_checks_if_a_string_has_only_ascii_characters(self):
        self.assertFalse('å∫ç∂'.isascii())
        self.assertFalse('åbcd'.isascii())

        self.assertTrue(''.isascii())
        self.assertTrue('text'.isascii())
        self.assertTrue('1234'.isascii())
        self.assertTrue('!@#$'.isascii())

    def test_isdecimal_checks_if_every_character_in_a_string_is_a_number(self):
        self.assertFalse(''.isdecimal())
        self.assertFalse('!@#$'.isdecimal())
        self.assertFalse('text'.isdecimal())
        self.assertFalse('1.234'.isdecimal())
        self.assertFalse('1,234'.isdecimal())

        self.assertTrue('1234'.isdecimal())

    def test_isdigit_checks_if_every_character_in_a_string_is_a_number(self):
        self.assertFalse('text'.isdigit())
        self.assertFalse(''.isdigit())
        self.assertFalse('!@#$'.isdecimal())
        self.assertFalse('1.234'.isdigit())
        self.assertFalse('1,234'.isdigit())

        self.assertTrue('1234'.isdigit())

    def test_isidentifier_checks_if_a_string_can_be_used_as_a_name_in_python(self):
        self.assertFalse(''.isidentifier())
        self.assertFalse('1234'.isidentifier())
        self.assertFalse('å∫ç∂'.isidentifier())
        self.assertFalse('-'.isidentifier())
        self.assertFalse('1234_text'.isidentifier())

        self.assertTrue('text'.isidentifier())
        self.assertTrue('_'.isidentifier())
        self.assertTrue('text_1234'.isidentifier())

    def test_islower_checks_if_a_string_is_lowercase(self):
        self.assertFalse(''.islower())
        self.assertFalse('1234'.islower())
        self.assertFalse('TEXT'.islower())
        self.assertFalse('Text'.islower())

        self.assertTrue('text'.islower())

'islower',
'isnumeric',
'isprintable',
'isspace',
'istitle',
'isupper',
'join',
'ljust',
'lower',
'lstrip',
'maketrans',
'partition',
'removeprefix',
'removesuffix',
'replace',
'rfind',
'rindex',
'rjust',
'rpartition',
'rsplit',
'rstrip',
'split',
'splitlines',
'startswith',
'strip',
'swapcase',
'title',
'translate',
'upper',
'zfill',



# Exceptions Encountered
# AssertionError
# TypeError
# ValueError