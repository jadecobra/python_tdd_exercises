import src.telephone
import unittest


class TestTelephone(unittest.TestCase):

    def test_passing_a_string(self):
        self.assertEqual(
            src.telephone.text("hello"),
            "I received: hello"
        )
        self.assertEqual(
            src.telephone.text("yes"),
            "I received: yes"
        )

    def test_passing_a_class(self):
        self.assertEqual(
            src.telephone.text(object),
            "I received: <class 'object'>"
        )

    def test_passing_none(self):
        self.assertEqual(
            src.telephone.text(None),
            "I received: None"
        )

    def test_passing_a_boolean(self):
        self.assertEqual(
            src.telephone.text(True),
            "I received: True"
        )
        self.assertEqual(
            src.telephone.text(False),
            "I received: False"
        )

    def test_passing_an_integer(self):
        self.assertEqual(
            src.telephone.text(1234),
            "I received: 1234"
        )

    def test_passing_a_float(self):
        self.assertEqual(
            src.telephone.text(1.234),
            "I received: 1.234"
        )

    def test_passing_a_tuple(self):
        self.assertEqual(
            src.telephone.text((1, 2, 3, "n")),
            "I received: (1, 2, 3, 'n')"
        )

    def test_passing_a_list(self):
        self.assertEqual(
            src.telephone.text([1, 2, 3, "n"]),
            "I received: [1, 2, 3, 'n']"
        )

    def test_passing_a_dictionary(self):
        self.assertEqual(
            src.telephone.text({
                'key1': 'value1',
                'keyN': [1, 2, 3, 'n'],
            }),
            "I received: {'key1': 'value1', 'keyN': [0, 1, 2, 'n']}"
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError