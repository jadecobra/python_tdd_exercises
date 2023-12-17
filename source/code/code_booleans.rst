
##################################
Data Structures: Booleans: Tests
##################################

Here is the code in ``tests/test_booleans.py``

.. code-block:: python

    import unittest


    class TestBooleans(unittest.TestCase):

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse('')
            self.assertFalse(())
            self.assertFalse([])
            self.assertFalse(set())
            self.assertFalse({})

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-1.2)
            self.assertTrue(2.3)
            self.assertTrue('text')
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue({1, 2, 3, 'n'})
            self.assertTrue({'key': 'value'})