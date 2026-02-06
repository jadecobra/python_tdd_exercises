import src.telephone
import unittest


class TestTelephone(unittest.TestCase):

    def test_passing_a_string(self):
        self.assertEqual(
            src.telephone.text("hello"),
            "I got: hello"
        )
        self.assertEqual(
            src.telephone.text("yes"),
            "I got: yes"
        )

    def test_passing_a_class(self):
        self.assertEqual(
            src.telephone.text(object),
            "I got: <class 'object'>"
        )

    def test_passing_none(self):
        self.assertEqual(
            src.telephone.text(None),
            "I got: None"
        )

    def test_passing_a_boolean(self):
        self.assertEqual(
            src.telephone.text(True),
            "I got: True"
        )
        self.assertEqual(
            src.telephone.text(False),
            "I got: False"
        )

    def test_passing_an_integer(self):
        self.assertEqual(
            src.telephone.text(1234),
            "I got: 1234"
        )

    def test_passing_a_float(self):
        self.assertEqual(
            src.telephone.text(1.234),
            "I got: 1.234"
        )

    def test_passing_a_tuple(self):
        self.assertEqual(
            src.telephone.text((1, 2, 3, "n")),
            "I got: (1, 2, 3, 'n')"
        )

    def test_passing_a_list(self):
        self.assertEqual(
            src.telephone.text([1, 2, 3, "n"]),
            "I got: [1, 2, 3, 'n']"
        )

    def test_passing_a_dictionary(self):
        self.assertEqual(
            src.telephone.text({
                'key1': 'value1',
                'keyN': [1, 2, 3, 'n'],
            }),
            "I got: {'key1': 'value1', 'keyN': [0, 1, 2, 'n']}"
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError