
booleans: Tests
================

Here is the code in ``tests/test_true.py``

.. code-block:: python

    import unittest


    class TestTrue(unittest.TestCase):

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
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