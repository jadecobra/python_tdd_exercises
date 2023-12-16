
##################################
booleans: False: Tests
##################################

Here is the code in ``tests/test_false.py``

.. code-block:: python

    import unittest


    class TestFalse(unittest.TestCase):

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse("")
            self.assertFalse(())
            self.assertFalse([])
            self.assertFalse(set())
            self.assertFalse({})