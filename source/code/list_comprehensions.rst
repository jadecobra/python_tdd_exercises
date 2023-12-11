
List Comprehensions: Tests and Solutions
==========================================


tests
-----

Here is the code in ``tests/test_list_comprehensions.py``

.. code-block:: python

    import list_comprehensions
    import unittest


    class TestListComprehensions(unittest.TestCase):

        def test_creating_a_list_from_an_iterable(self):
            collection = range(10)
            a_list = []
            self.assertEqual(a_list, [])

            for element in collection:
                a_list.append(element)
            self.assertEqual(a_list, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            self.assertEqual(list(collection), a_list)
            self.assertEqual(
                list_comprehensions.make_a_list(collection),
                a_list
            )

        def test_creating_a_list_with_a_for_loop(self):
            collection = range(10)
            a_list = []
            self.assertEqual(a_list, [])

            for element in collection:
                a_list.append(element)

            self.assertEqual(a_list, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            self.assertEqual(
                list_comprehensions.for_loop(collection),
                a_list
            )

        def test_creating_lists_with_list_comprehensions(self):
            collection = range(10)
            a_list = []
            self.assertEqual(a_list, [])

            for element in collection:
                a_list.append(element)

            self.assertEqual(a_list, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            self.assertEqual([element for element in collection], a_list)
            self.assertEqual(
                list_comprehensions.list_comprehension(collection),
                a_list
            )

        def test_list_comprehensions_with_conditions_i(self):
            collection = range(10)

            even_numbers = []
            self.assertEqual(even_numbers, [])

            for element in collection:
                if element % 2 == 0:
                    even_numbers.append(element)

            self.assertEqual(even_numbers, [0, 2, 4, 6, 8])
            self.assertEqual(
                [element for element in collection if element % 2 == 0],
                even_numbers
            )
            self.assertEqual(
                list_comprehensions.get_even_numbers(collection),
                even_numbers
            )

        def test_list_comprehensions_with_conditions_ii(self):
            collection = range(10)
            odd_numbers = []
            self.assertEqual(odd_numbers, [])

            for element in collection:
                if element % 2 != 0:
                    odd_numbers.append(element)

            self.assertEqual(odd_numbers, [1, 3, 5, 7, 9])
            self.assertEqual(
                [element for element in collection if element % 2 == 0],
                odd_numbers
            )
            self.assertEqual(
                list_comprehensions.get_odd_numbers(collection),
                odd_numbers
            )

    # Exceptions Encountered
    # AssertionError
    # NameError
    # ModuleNotFoundError
    # AttributeError
    # TypeError


solutions
----------

Here are the solutions in ``list_comprehensions.py``

.. code-block:: python

    def make_a_list(argument):
        return list(argument)

    def for_loop(argument):
        result = []
        for element in argument:
            result.append(element)
        return result

    def list_comprehension(argument):
        return [element for element in argument]

    def get_even_numbers(argument):
        return [element for element in argument if element % 2 == 0]

    def get_odd_numbers(argument):
        return [element for element in argument if element % 2 != 0]