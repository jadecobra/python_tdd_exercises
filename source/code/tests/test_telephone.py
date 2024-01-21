import telephone
import unittest


class TestTelephone(unittest.TestCase):

    def test_text_messages(self):
        self.assertEqual(
            telephone.text('hello'),
            'I received this message: hello'
        )
        self.assertEqual(
            telephone.text('yes'),
            'I received this message: yes'
        )
        self.assertEqual(
            telephone.text(None),
            'I received this message: None'
        )
        self.assertEqual(
            telephone.text(bool),
            "I received this message: <class 'bool'>"
        )
        self.assertEqual(
            telephone.text(int),
            "I received this message: <class 'int'>"
        )
        self.assertEqual(
            telephone.text(float),
            "I received this message: <class 'float'>"
        )
        self.assertEqual(
            telephone.text(tuple),
            "I received this message: <class 'tuple'>"
        )
        self.assertEqual(
            telephone.text(list),
            "I received this message: <class 'list'>"
        )
        self.assertEqual(
            telephone.text(set),
            "I received this message: <class 'set'>"
        )
        self.assertEqual(
            telephone.text(dict),
            "I received this message: <class 'dict'>"
        )

# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError