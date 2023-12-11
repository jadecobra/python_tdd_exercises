
booleans: Tests
================

Here is the code in ``tests/test_booleans.py``

.. code-block:: python

    import unittest


    class TestLists(unittest.TestCase):

        def test_creating_a_list_with_the_list_keyword(self):
            self.assertEqual(list((0, 1, 2, 3)), [0, 1, 2, 3])

        def test_creating_a_list_with_square_brackets(self):
            self.assertEqual([0, 1, 2, 3], list((0, 1, 2, 3)))

        def test_adding_an_item_to_a_list(self):
            a_list = [0, 1, 2, 3]
            self.assertEqual(a_list, [0, 1, 2, 3])
            a_list.append(4)
            self.assertEqual(a_list, [0, 1, 2, 3, 4])

        def test_removing_any_item_from_a_list(self):
            a_list = [0, 1, 2, 3]
            self.assertEqual(a_list, [0, 1, 2, 3])
            a_list.remove(2)
            self.assertEqual(a_list, [0, 1, 3])

        def test_removing_an_item_from_a_list_when_multiple_exist(self):
            a_list = [0, 2, 1, 2, 3, 2]
            self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])
            a_list.remove(2)
            self.assertEqual(a_list, [0, 1, 2, 3, 2])

        def test_removing_the_last_item_of_a_list(self):
            a_list = [0, 1, 2, 3]
            self.assertEqual(a_list, [0, 1, 2, 3])
            last_item = a_list.pop()
            self.assertEqual(last_item, 3)
            self.assertEqual(a_list, [0, 1, 2])

        def test_getting_items_in_a_list(self):
            a_list = ['first', 'second', 'third', 'fourth']
            self.assertEqual(a_list, ['first', 'second', 'third', 'fourth'])
            self.assertEqual(a_list[0], 'first')
            self.assertEqual(a_list[2], 'third')
            self.assertEqual(a_list[1], 'second')
            self.assertEqual(a_list[3], 'fourth')
            self.assertEqual(a_list[-1], 'fourth')
            self.assertEqual(a_list[-3], 'second')
            self.assertEqual(a_list[-2], 'third')
            self.assertEqual(a_list[-4], 'first')

        def test_indexing_with_a_number_greater_than_the_length_of_the_list(self):
            a_list = ['a', 'b', 'c', 'd']
            with self.assertRaises(IndexError):
                a_list[5]

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
    # IndexError
