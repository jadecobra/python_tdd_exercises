import itertools
import src.truth_table
import unittest


class TestBinaryOperations(unittest.TestCase):

    def test_binary_operations(self):
        for first, second in itertools.product(
            (False, True), repeat=2
        ):
            for operation, expectation in (
                ('contradiction', False),
                (
                    'logical_conjunction',
                    (first, second) == (True, True)
                ),
                ('project_second', second),
                (
                    'converse_non_implication',
                    (first, second) == (False, True)
                ),
                ('negate_first', not first),
                (
                    'logical_nand',
                    (first, second) != (True, True)
                ),
                ('tautology', True),
                (
                    'logical_disjunction',
                    (first, second) != (False, False)
                ),
                (
                    'exclusive_disjunction',
                    first != second
                ),
                (
                    'material_non_implication',
                    (first, second) == (True, False)
                ),
                ('project_first', first),
                (
                    'converse_implication',
                    (first, second) != (False, True)
                ),
                ('negate_second', not second),
                (
                    'logical_nor',
                    (first, second) == (False, False)
                ),
                (
                    'logical_equality',
                    first == second
                ),
                (
                    'material_implication',
                    (first, second) != (True, False)
                ),
            ):
                with self.subTest(
                    operation,
                    first=first, second=second
                ):
                    self.assertEqual(
                        src.truth_table.__getattribute__(
                            operation
                        )(first, second),
                        expectation
                    )


# Exceptions seen
# AttributeError
# TypeError
# AssertionError
# SyntaxError