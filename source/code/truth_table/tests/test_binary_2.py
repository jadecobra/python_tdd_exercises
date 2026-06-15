import src.truth_table
import unittest


class TestBinaryOperations(unittest.TestCase):

    def test_contradiction(self):
        contradiction = src.truth_table.contradiction
        self.assertFalse(contradiction(True, True))
        self.assertFalse(contradiction(True, False))
        self.assertFalse(contradiction(False, True))
        self.assertFalse(contradiction(False, False))

    def test_logical_conjunction(self):
        logical_conjunction = (
            src.truth_table.logical_conjunction
        )
        self.assertTrue(
            logical_conjunction(True, True)
        )
        self.assertFalse(
            logical_conjunction(True, False)
        )
        self.assertFalse(
            logical_conjunction(False, True)
        )
        self.assertFalse(
            logical_conjunction(False, False)
        )

    def test_project_second(self):
        project_second = src.truth_table.project_second
        self.assertTrue(project_second(True, True))
        self.assertFalse(project_second(True, False))
        self.assertTrue(project_second(False, True))
        self.assertFalse(project_second(False, False))

    def test_converse_non_implication(self):
        converse_non_implication = (
            src.truth_table.converse_non_implication
        )
        self.assertFalse(
            converse_non_implication(True, True)
        )
        self.assertFalse(
            converse_non_implication(True, False)
        )
        self.assertTrue(
            converse_non_implication(False, True)
        )
        self.assertFalse(
            converse_non_implication(False, False)
        )

    def test_negate_first(self):
        negate_first = src.truth_table.negate_first
        self.assertFalse(negate_first(True, True))
        self.assertFalse(negate_first(True, False))
        self.assertTrue(negate_first(False, True))
        self.assertTrue(negate_first(False, False))

    def test_logical_nand(self):
        logical_nand = src.truth_table.logical_nand
        self.assertFalse(logical_nand(True, True))
        self.assertTrue(logical_nand(True, False))
        self.assertTrue(logical_nand(False, True))
        self.assertTrue(logical_nand(False, False))

    def test_tautology(self):
        tautology = src.truth_table.tautology
        self.assertTrue(tautology(True, True))
        self.assertTrue(tautology(True, False))
        self.assertTrue(tautology(False, True))
        self.assertTrue(tautology(False, False))

    def test_logical_disjunction(self):
        logical_disjunction = (
            src.truth_table.logical_disjunction
        )
        self.assertTrue(logical_disjunction(True, True))
        self.assertTrue(logical_disjunction(True, False))
        self.assertTrue(logical_disjunction(False, True))
        self.assertFalse(logical_disjunction(False, False))


# Exceptions seen
# AttributeError
# TypeError
# AssertionError
# SyntaxError