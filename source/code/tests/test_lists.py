import unittest


class TestLists(unittest.TestCase):

    def test_make_a_list_w_list_constructor(self):
        self.assertEqual(list((0, 1, 2, 3)), [0, 1, 2, 3])

    def test_make_a_list_w_square_brackets(self):
        self.assertEqual([0, 1, 2, 3], list((0, 1, 2, 3)))

    def test_make_a_list_w_an_iterable(self):
        self.assertEqual(list(range(0, 4)), [0, 1, 2, 3])

    def test_attributes_and_methods_of_lists(self):
        self.maxDiff = None
        self.assertEqual(
            dir(list),
            [
                '__add__',
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
                '__iadd__',
                '__imul__',
                '__init__',
                '__init_subclass__',
                '__iter__',
                '__le__',
                '__len__',
                '__lt__',
                '__mul__',
                '__ne__',
                '__new__',
                '__reduce__',
                '__reduce_ex__',
                '__repr__',
                '__reversed__',
                '__rmul__',
                '__setattr__',
                '__setitem__',
                '__sizeof__',
                '__str__',
                '__subclasshook__',
                'append',
                'clear',
                'copy',
                'count',
                'extend',
                'index',
                'insert',
                'pop',
                'remove',
                'reverse',
                'sort'
            ]
        )

    def test_append_adds_to_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertIsNone(a_list.append(4))
        self.assertEqual(a_list, [0, 1, 2, 3, 4])

    def test_clear_empties_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertIsNone(a_list.clear())
        self.assertEqual(a_list, [])

    def test_copy_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list.copy(), [0, 1, 2, 3])
        self.assertEqual(a_list, [0, 1, 2, 3])

    def test_count_number_of_times_item_is_in_a_list(self):
        a_list = [0, 2, 1, 2, 3, 2]
        self.assertEqual(a_list.count(0), 1)
        self.assertEqual(a_list.count(2), 3)
        self.assertEqual(a_list.count(9), 0)

    def test_extend_makes_a_list_longer(self):
        a_list = [0, 1, 2, 3]
        self.assertIsNone(a_list.extend((4, 5, 6, 7)))
        self.assertEqual(a_list, [0, 1, 2, 3, 4, 5, 6, 7])

    def test_index_returns_position_of_item_in_a_list(self):
        a_list = ['1st', '2nd', '3rd', '... last']
        self.assertEqual(a_list.index('1st'), 0)
        self.assertEqual(a_list.index('3rd'), 2)
        self.assertEqual(a_list.index('2nd'), 1)
        self.assertEqual(a_list.index('... last'), 3)

        with self.assertRaises(ValueError):
            a_list.index(0)

    def test_insert_places_item_at_given_index_in_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertIsNone(a_list.insert(0, 1))
        self.assertEqual(a_list, [1, 0, 1, 2, 3])

    def test_pop_removes_and_returns_last_item_in_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list.pop(), 3)
        self.assertEqual(a_list, [0, 1, 2])

    def test_remove_first_instance_of_item_in_a_list(self):
        a_list = [0, 2, 1, 2, 3, 2]
        self.assertIsNone(a_list.remove(2))
        self.assertEqual(a_list, [0, 1, 2, 3, 2])

    def test_reverse_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertIsNone(a_list.reverse())
        self.assertEqual(a_list, [3, 2, 1, 0])

    def test_sort_a_list(self):
        a_list = [0, 2, 1, 2, 3, 2]
        self.assertIsNone(a_list.sort())
        self.assertEqual(a_list, [0, 1, 2, 2, 2, 3])

    def test_view_items_in_a_list(self):
        a_list = ['1st', '2nd', '3rd', '... last']
        self.assertEqual(a_list[0], '1st')
        self.assertEqual(a_list[-4], '1st')
        self.assertEqual(a_list[2], '3rd')
        self.assertEqual(a_list[-2], '3rd')
        self.assertEqual(a_list[1], '2nd')
        self.assertEqual(a_list[-3], '2nd')
        self.assertEqual(a_list[3], '... last')
        self.assertEqual(a_list[-1], '... last')

    def test_view_parts_of_a_list(self):
        a_list = ['1st', '2nd', '3rd', '... last']
        self.assertEqual(a_list[0:2], ['1st', '2nd'])
        self.assertEqual(a_list[0:3], ['1st', '2nd', '3rd'])
        self.assertEqual(a_list[1:4], ['2nd', '3rd', '... last'])
        self.assertEqual(a_list[1:3], ['2nd', '3rd'])

    def test_index_error(self):
        a_list = ['a', 'b', 'c', 'd']

        with self.assertRaises(IndexError):
            a_list[4]
        with self.assertRaises(IndexError):
            a_list[-5]
        with self.assertRaises(IndexError):
            [].pop()


# Exceptions Encountered
# AssertionError
# TypeError
# ValueError
# IndexError