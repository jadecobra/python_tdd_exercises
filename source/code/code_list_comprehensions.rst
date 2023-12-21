
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

        def test_creating_a_list_from_an_iterable(self):
            container = range(10)
            a_list = []
            self.assertEqual(a_list, [])

            for item in container:
                a_list.append(item)
            self.assertEqual(
                a_list,
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            )
            self.assertEqual(list(container), a_list)
            self.assertEqual(
                list_comprehensions.make_a_list(container),
                a_list
            )

        def test_creating_a_list_with_a_for_loop(self):
            container = range(10)
            a_list = []
            self.assertEqual(a_list, [])

            for item in container:
                a_list.append(item)

            self.assertEqual(
                a_list,
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            )
            self.assertEqual(
                list_comprehensions.for_loop(container),
                a_list
            )

        def test_creating_lists_with_list_comprehensions(self):
            container = range(10)
            a_list = []
            self.assertEqual(a_list, [])

            for item in container:
                a_list.append(item)

            self.assertEqual(
                a_list,
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            )
            self.assertEqual(
                [item for item in container],
                a_list
            )
            self.assertEqual(
                list_comprehensions.list_comprehension(container),
                a_list
            )

        def test_list_comprehensions_with_conditions_i(self):
            container = range(10)
            even_numbers = []
            self.assertEqual(even_numbers, [])

            for item in container:
                if item % 2 == 0:
                    even_numbers.append(item)

            self.assertEqual(even_numbers, [0, 2, 4, 6, 8])
            self.assertEqual(
                [item for item in container if item % 2 == 0],
                even_numbers
            )
            self.assertEqual(
                list_comprehensions.get_even_numbers(container),
                even_numbers
            )

        def test_list_comprehensions_with_conditions_ii(self):
            container = range(10)
            odd_numbers = []

            for item in container:
                if item % 2 != 0:
                    odd_numbers.append(item)

            self.assertEqual(odd_numbers, [1, 3, 5, 7, 9])
            self.assertEqual(
                [item for item in container if item % 2 != 0],
                odd_numbers
            )
            self.assertEqual(
                list_comprehensions.get_odd_numbers(container),
                odd_numbers
            )

    # Exceptions Encountered
    # AssertionError
    # NameError
    # ModuleNotFoundError
    # AttributeError


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