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
            telephone.text(1234),
            "I received this message: 1234"
        )
        self.assertEqual(
            telephone.text(1.234),
            "I received this message: 1.234"
        )
        self.assertEqual(
            telephone.text((1, 2, 3, 'n')),
            "I received this message: (1, 2, 3, 'n')"
        )
        self.assertEqual(
            telephone.text([1, 2, 3, 'n']),
            "I received this message: [1, 2, 3, 'n']"
        )
        self.assertEqual(
            telephone.text({1, 2, 3, 'n'}),
            "I received this message: {1, 2, 3, 'n'}"
        )
        self.assertEqual(
            telephone.text({
                'key1': 'value1',
                'keyN': 'valueN'
            }),
            "I received this message: {'key1': 'value1', 'keyN': 'valueN'}"
        )

# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError