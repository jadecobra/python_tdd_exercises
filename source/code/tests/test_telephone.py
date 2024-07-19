import src.telephone
import unittest


class TestTelephone(unittest.TestCase):

    def test_passing_a_string(self):
        self.assertEqual(
            src.telephone.text('hello'),
            "I received this message: hello"
        )
        self.assertEqual(
            src.telephone.text('yes'),
            "I received this message: yes"
        )

    def test_passing_a_class(self):
        self.assertEqual(
            src.telephone.text(object),
            "I received this message: <class 'object'>"
        )

    def test_passing_None(self):
        self.assertEqual(
            src.telephone.text(None),
            "I received this message: None"
        )

    def test_passing_a_boolean(self):
        self.assertEqual(
            src.telephone.text(True),
            "I received this message: True"
        )
        self.assertEqual(
            src.telephone.text(False),
            "I received this message: False"
        )

    def test_passing_an_integer(self):
        self.assertEqual(
            src.telephone.text(1234),
            "I received this message: 1234"
        )

    def test_passing_a_float(self):
        self.assertEqual(
            src.telephone.text(1.234),
            "I received this message: 1.234"
        )

    def test_passing_a_tuple(self):
        self.assertEqual(
            src.telephone.text((1, 2, 3, 'n')),
            "I received this message: (1, 2, 3, 'n')"
        )

    def test_passing_a_list(self):
        self.assertEqual(
            src.telephone.text([1, 2, 3, 'n']),
            "I received this message: [1, 2, 3, 'n']"
        )

    def test_passing_a_dictionary(self):
        self.assertEqual(
            src.telephone.text({
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