
#################################
Truth Table: Tests and Solutions
#################################


tests
-----

Here is the code in ``tests/test_tree.py``

.. code-block:: python

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



solutions
---------

Here are the solutions in ``tree.py``

.. code-block:: python

    def tree(number):
        star_generator = (
            "".join(("X" for i in range(i)))
            for i in range(number // 2, 0, -1)
        )
        return [
            f"{stars}"
            f"{'*' * (number - (len(stars) * 2))}"
            f"{stars}" for stars in star_generator
        ]
