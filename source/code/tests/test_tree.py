import tree
import unittest


class TestProjectName(unittest.TestCase):

    def test_failure(self):
        self.assertEqual(
            tree.tree(10),
            [
                "XXXXXXXXXX",
                "XXXX**XXXX",
                "XXX****XXX",
                "XX******XX",
                "X********X"
            ]
        )
        self.assertEqual(
            tree.tree(11),
            [
                "XXXXX*XXXXX",
                "XXXX***XXXX",
                "XXX*****XXX",
                "XX*******XX",
                "X*********X",
            ],
        )