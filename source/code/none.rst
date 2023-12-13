
none: Tests
================

Here is the code in ``tests/test_none.py``

.. code-block:: python

    import unittest


    class TestDataStructures(unittest.TestCase):

        def test_none_is_none(self):
            self.assertIsNone(None)

        def test_is_none_a_boolean(self):
            self.assertIsNotNone(True)
            self.assertIsNotNone(False)
            self.assertNotIsInstance(None, bool)

        def test_is_none_an_integer(self):
            self.assertIsNotNone(-1)
            self.assertIsNotNone(0)
            self.assertIsNotNone(1)
            self.assertNotIsInstance(None, int)

        def test_is_none_a_float(self):
            self.assertIsNotNone(-1.1)
            self.assertIsNotNone(0.2)
            self.assertNotIsInstance(None, float)

        def test_is_none_a_string(self):
            self.assertIsNotNone('')
            self.assertIsNotNone("text")
            self.assertNotIsInstance(None, str)

        def test_is_none_a_tuple(self):
            self.assertIsNotNone(())
            self.assertIsNotNone((1, 2, 3, 'n'))
            self.assertNotIsInstance(None, tuple)

        def test_is_none_a_list(self):
            self.assertIsNotNone([])
            self.assertIsNotNone([1, 2, 3, "n"])
            self.assertNotIsInstance(None, list)

        def test_is_none_a_set(self):
            self.assertIsNotNone({})
            self.assertIsNotNone({1, 2, 3, "n"})
            self.assertNotIsInstance(None, set)

        def test_is_none_a_dictionary(self):
            self.assertIsNotNone(dict())
            self.assertIsNotNone({
                "a": 1,
                "b": 2,
                "c":  3,
                "n": "n"
            })
            self.assertNotIsInstance(None, dict)

    # Exceptions Encountered
    # AssertionError