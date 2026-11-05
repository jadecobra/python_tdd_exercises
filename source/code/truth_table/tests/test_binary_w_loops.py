import src.truth_table
import unittest


class TestBinaryOperations(unittest.TestCase):

    def test_binary_operations(self):
        booleans = (False, True)
        for first in booleans:
            for second in booleans:
                for operation, expectation in (
                    (src.truth_table.contradiction, False),
                    (
                        src.truth_table.logical_conjunction,
                        (first, second) == (True, True)
                    ),
                    (src.truth_table.project_second, second),
                    (
                        src.truth_table.converse_non_implication,
                        (first, second) == (False, True)
                    ),
                    (src.truth_table.negate_first, not first),
                    (
                        src.truth_table.logical_nand,
                        (first, second) != (True, True)
                    ),
                    (src.truth_table.tautology, True),
                    (
                        src.truth_table.logical_disjunction,
                        (first, second) != (False, False)
                    ),
                    (
                        src.truth_table.exclusive_disjunction,
                        first != second
                    ),
                    (
                        src.truth_table.material_non_implication,
                        (first, second) == (True, False)
                    ),
                    (src.truth_table.project_first, first),
                    (
                        src.truth_table.converse_implication,
                        (first, second) != (False, True)
                    ),
                    (src.truth_table.negate_second, not second),
                    (
                        src.truth_table.logical_nor,
                        (first, second) == (False, False)
                    ),
                    (
                        src.truth_table.logical_equality,
                        first == second
                    ),
                    (
                        src.truth_table.material_implication,
                        (first, second) != (True, False)
                    ),
                ):
                    with self.subTest(
                        operation.__name__,
                        first=first,
                        second=second
                    ):
                        self.assertEqual(
                            operation(first, second),
                            expectation
                        )


# Exceptions seen
# AttributeError
# TypeError
# AssertionError
# Syntaxerror