
How to pass values: Tests and Solution
=======================================


tests
-----

Here is the code in ``tests/test_passing_values.py``

.. code-block:: python

    import unittest
    import telephone


    class TestPassingValues(unittest.TestCase):

        def test_text_messages(self):
            self.assertEqual(
                telephone.Telephone.text('hello'),
                'I received this message: hello'
            )
            self.assertEqual(
                telephone.Telephone.text('yes'),
                'I received this message: yes'
            )
            self.assertEqual(
                telephone.Telephone.text(None),
                "I received this message: None"
            )
            self.assertEqual(
                telephone.Telephone.text(bool),
                "I received this message: <class 'bool'>"
            )
            self.assertEqual(
                telephone.Telephone.text(int),
                "I received this message: <class 'int'>"
            )
            self.assertEqual(
                telephone.Telephone.text(float),
                "I received this message: <class 'float'>"
            )
            self.assertEqual(
                telephone.Telephone.text(tuple),
                "I received this message: <class 'tuple'>"
            )
            self.assertEqual(
                telephone.Telephone.text(list),
                "I received this message: <class 'list'>"
            )
            self.assertEqual(
                telephone.Telephone.text(set),
                "I received this message: <class 'set'>"
            )
            self.assertEqual(
                telephone.Telephone.text(dict),
                "I received this message: <class 'dict'>"
            )

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError

solution
---------

Here is the solution in ``telephone.py``

.. code-block:: python

    class Telephone(object):

    def text(value):
        return f'I received this message: {value}'