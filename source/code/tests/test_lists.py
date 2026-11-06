import unittest


class Testlists(unittest.TestCase):

    def test_making_a_list(self):
        self.assertEqual(list(), [])
        self.assertEqual(list((0, 1, 2, 'n')), [0, 1, 2, 'n'])

    def test_dir_list(self):
        self.maxDiff = None

        dir_list = dir(object)
        dir_list.extend((
            '__add__', '__class_getitem__',
            '__contains__', '__delitem__',
            '__getitem__', '__iadd__',
            '__imul__', '__iter__', '__len__',
            '__mul__', '__reversed__',
            '__rmul__', '__setitem__',
            'append', 'clear', 'copy',
            'count', 'extend', 'index',
            'insert', 'pop', 'remove',
            'reverse', 'sort',
        ))
        dir_list.sort()
        self.assertEqual(dir(list), dir_list)

    def test_append_adds_item_to_end_of_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.append('n+1'))
        self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])

    def test_clear_empties_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.clear())
        self.assertEqual(a_list, [])

    def test_copy_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])

    def test_count_number_of_times_item_is_in_a_list(self):
        a_list = [0, 1, 2, 1, 'n', 1]
        self.assertEqual(a_list.count(0), 1)
        self.assertEqual(a_list.count(1), 3)
        self.assertEqual(a_list.count('not in list'), 0)

    def test_extend_adds_items_from_an_iterable_to_end_of_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.extend((2, 1, 0)))
        self.assertEqual(a_list, [0, 1, 2, 'n', 2, 1, 0])

        another_list = [0, 1, 2, 'n']
        for number in (2, 1, 0):
            another_list.append(number)
        self.assertEqual(another_list, a_list)

    def test_index_returns_first_position_of_item_in_a_list(self):
        a_list = ['1st', '2nd', '3rd', '...last', '1st']
        self.assertEqual(a_list.index('1st', 0), 0)
        self.assertEqual(a_list.index('3rd', 0), 2)
        self.assertEqual(a_list.index('2nd', 0), 1)
        self.assertEqual(a_list.index('...last', 0), 3)
        self.assertEqual(a_list.index('1st', 1), 4)

        with self.assertRaises(ValueError):
            a_list.index('not in list')

    def test_insert_item_at_position_in_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.insert(0, -1))
        self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])
        self.assertIsNone(a_list.insert(3, 1.5))
        self.assertEqual(a_list, [-1, 0, 1, 1.5, 2, 'n'])

    def test_pop_removes_and_returns_last_item_from_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertEqual(a_list.pop(), 'n')
        self.assertEqual(a_list, [0, 1, 2])
        self.assertEqual(a_list.pop(), 2)
        self.assertEqual(a_list, [0, 1])

    def test_remove_first_time_item_is_in_a_list(self):
        a_list = [0, 1, 0, 2, 0, 'n']
        self.assertIsNone(a_list.remove(0))
        self.assertEqual(a_list, [1, 0, 2, 0, 'n'])

        with self.assertRaises(ValueError):
            a_list.remove('not in list')

    def test_reverse_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.reverse())
        self.assertEqual(a_list, ['n', 2, 1, 0])

    def test_sort_a_list(self):
        with self.assertRaises(TypeError):
            [0, 1, 2, 'n'].sort()

        a_list = [0, 1, -1, 2, -2, 3, -3]
        self.assertIsNone(a_list.sort())
        self.assertEqual(a_list, [-3, -2, -1, 0, 1, 2, 3])

    def test_getting_items_of_a_list(self):
        a_list = ['1st', '2nd', '3rd', '...last']
        self.assertEqual(a_list[0], '1st')
        self.assertEqual(a_list[a_list.index('1st')], '1st')
        self.assertEqual(a_list[-4], '1st')
        self.assertEqual(a_list[2], '3rd')
        self.assertEqual(a_list[-2], '3rd')
        self.assertEqual(a_list[1], '2nd')
        self.assertEqual(a_list[-3], '2nd')
        self.assertEqual(a_list[3], '...last')
        self.assertEqual(a_list[-1], '...last')

    def test_setting_items_in_a_list(self):
        a_list = ['1st', '2nd', '3rd', '...last']
        a_list[-1] = '4th'
        self.assertEqual(
            a_list, ['1st', '2nd', '3rd', '4th']
        )

    def test_getting_parts_of_a_list_aka_slicing(self):
        a_list = ['a', 'b', 'c', 'd']
        self.assertEqual(a_list[0:2], ['a', 'b'])
        self.assertEqual(a_list[:2], ['a', 'b'])
        self.assertEqual(a_list[1:4], ['b', 'c', 'd'])
        self.assertEqual(a_list[1:], ['b', 'c', 'd'])
        self.assertEqual(a_list[0:3], ['a', 'b', 'c'])
        self.assertEqual(a_list[1:3], ['b', 'c'])
        self.assertEqual(a_list[:], a_list.copy())

    def test_index_error(self):
        a_list = ['a', 'b', 'c', 'd']

        with self.assertRaises(IndexError):
            a_list[4]
        with self.assertRaises(IndexError):
            a_list[-5]
        with self.assertRaises(IndexError):
            [].pop()
        with self.assertRaises(IndexError):
            [][-1]


# Exceptions seen
# AssertionError
# TypeError
# ValueError
# IndexError