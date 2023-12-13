
booleans: Tests
================

Here is the code in ``tests/test_booleans.py``

.. code-block:: python

    import unittest


    class TestBooleans(unittest.TestCase):

        def test_what_is_false(self):
            self.assertFalse(None)
            self.assertFalse(False)
            self.assertFalse(0)
            self.assertFalse("")
            self.assertFalse(())
            self.assertFalse([])
            self.assertFalse({})
            self.assertFalse(dict())
            self.assertIsInstance(False, bool)

        def test_what_is_true(self):
            self.assertTrue(True)
            self.assertTrue(1)
            self.assertTrue(-1)
            self.assertTrue("text")
            self.assertTrue((1, 2, 3, "n"))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue({1, 2, 3, "n"})
            self.assertTrue({
                "a": 1,
                "b": 2,
                "c": 3,
                "n": "n"
            })
            self.assertIsInstance(True, bool)