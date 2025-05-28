import unittest


class TestLists(unittest.TestCase):

    def test_make_a_list(self):
        self.assertEqual(list((0, 1, 2, 3)), [0, 1, 2, 3])

    def test_make_a_list_w_square_brackets(self):
        self.assertEqual([0, 1, 2, 3], list((0, 1, 2, 3)))

    def test_make_a_list_from_an_iterable(self):
        iterable = range(4)
        self.assertEqual(list(iterable), [0, 1, 2, 3])

    def test_add_to_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertIsNone(a_list.append(4))
        self.assertEqual(a_list, [0, 1, 2, 3, 4])

    def test_remove_from_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertIsNone(a_list.remove(2))
        self.assertEqual(a_list, [0, 1, 3])

    def test_remove_from_a_list_when_item_occurs_multiple_times(self):
        a_list = [0, 2, 1, 2, 3, 2]
        self.assertIsNone(a_list.remove(2))
        self.assertEqual(a_list, [0, 1, 2, 3, 2])

    def test_remove_from_list_when_item_does_not_exist(self):
        a_list = [0, 1, 2, 3]
        with self.assertRaises(ValueError):
            a_list.remove(4)

    def test_remove_last_item_from_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list.pop(), 3)
        self.assertEqual(a_list, [0, 1, 2])

    def test_remove_last_item_from_empty_list(self):
        with self.assertRaises(IndexError):
            [].pop()

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
        self.assertEqual(a_list[1:3], ['2nd', '3rd'])
        self.assertEqual(a_list[1:4], ['2nd', '3rd', '... last'])

    def test_index_error(self):
        a_list = ['a', 'b', 'c', 'd']

        with self.assertRaises(IndexError):
            a_list[4]
        with self.assertRaises(IndexError):
            a_list[-5]

    def test_attributes_and_methods_of_a_list(self):
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


# Exceptions Encountered
# AssertionError
# TypeError
# ValueError
# IndexError