
###########################################################
Data Structures: List Comprehensions: Tests and Solutions
###########################################################

tests
-----

Here is the code in ``tests/test_list_comprehensions.py``

.. code-block:: python

    import list_comprehensions
    import unittest


    class TestListComprehensions(unittest.TestCase):

        def setUp(self):
            self.a_list = []
            self.assertEqual(self.a_list, [])
            self.container = range(10)

        def test_creating_a_list_from_an_iterable(self):
            for item in self.container:
                self.a_list.append(item)
            self.assertEqual(
                self.a_list,
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            )
            self.assertEqual(list(self.container), self.a_list)
            self.assertEqual(
                list_comprehensions.make_a_list(self.container),
                self.a_list
            )

        def test_creating_a_list_with_a_for_loop(self):
            for item in self.container:
                self.a_list.append(item)

            self.assertEqual(
                self.a_list,
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            )
            self.assertEqual(
                list_comprehensions.for_loop(self.container),
                self.a_list
            )

        def test_creating_lists_with_list_comprehensions(self):
            for item in self.container:
                self.a_list.append(item)

            self.assertEqual(
                self.a_list,
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            )
            self.assertEqual(
                [item for item in self.container],
                self.a_list
            )
            self.assertEqual(
                list_comprehensions.list_comprehension(self.container),
                self.a_list
            )

        def test_list_comprehensions_with_conditions_i(self):
            for item in self.container:
                if item % 2 == 0:
                    self.a_list.append(item)

            self.assertEqual(self.a_list, [0, 2, 4, 6, 8])
            self.assertEqual(
                [item for item in self.container if item % 2 == 0],
                self.a_list
            )
            self.assertEqual(
                list_comprehensions.get_even_numbers(self.container),
                self.a_list
            )

        def test_list_comprehensions_with_conditions_ii(self):
            for item in self.container:
                if item % 2 != 0:
                    self.a_list.append(item)

            self.assertEqual(self.a_list, [1, 3, 5, 7, 9])
            self.assertEqual(
                [item for item in self.container if item % 2 != 0],
                self.a_list
            )
            self.assertEqual(
                list_comprehensions.get_odd_numbers(self.container),
                self.a_list
            )


    # Exceptions Encountered
    # AssertionError
    # NameError
    # ModuleNotFoundError


solutions
----------

Here are the solutions in ``list_comprehensions.py``

.. code-block:: python

    def make_a_list(iterable):
        return list(iterable)

    def for_loop(iterable):
        result = []
        for item in iterable:
            result.append(item)
        return result

    def list_comprehension(iterable):
        return [item for item in iterable]

    def get_even_numbers(iterable):
        return [item for item in iterable if item % 2 == 0]

    def get_odd_numbers(iterable):
        return [item for item in iterable if item % 2 != 0]