import unittest
import src.truth_table


class TestNullaryOperations(unittest.TestCase):

    def test_logical_true(self):
        self.assertTrue(src.truth_table.logical_true())

    def test_logical_false(self):
        self.assertFalse(src.truth_table.logical_false())


class TestUnaryOperations(unittest.TestCase):

    def test_logical_identity(self):
        self.assertTrue(src.truth_table.logical_identity(True))
        self.assertFalse(src.truth_table.logical_identity(False))

    def test_logical_negation_aka_not(self):
        self.assertFalse(src.truth_table.logical_negation(True))
        self.assertTrue(src.truth_table.logical_negation(False))


class TestBinaryOperations(unittest.TestCase):

    def test_contradiction(self):
        self.assertFalse(src.truth_table.contradiction(True, True))
        self.assertFalse(src.truth_table.contradiction(True, False))
        self.assertFalse(src.truth_table.contradiction(False, True))
        self.assertFalse(src.truth_table.contradiction(False, False))

    def test_logical_conjunction(self):
        self.assertTrue(src.truth_table.logical_conjunction(True, True))
        self.assertFalse(src.truth_table.logical_conjunction(True, False))
        self.assertFalse(src.truth_table.logical_conjunction(False, True))
        self.assertFalse(src.truth_table.logical_conjunction(False, False))

    def test_project_second(self):
        self.assertTrue(src.truth_table.project_second(True, True))
        self.assertFalse(src.truth_table.project_second(True, False))
        self.assertTrue(src.truth_table.project_second(False, True))
        self.assertFalse(src.truth_table.project_second(False, False))

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))
        self.assertTrue(src.truth_table.converse_non_implication(False, True))
        self.assertFalse(src.truth_table.converse_non_implication(False, False))

    def test_negate_first(self):
        self.assertFalse(src.truth_table.negate_first(True, True))
        self.assertFalse(src.truth_table.negate_first(True, False))
        self.assertTrue(src.truth_table.negate_first(False, True))
        self.assertTrue(src.truth_table.negate_first(False, False))

    def test_logical_nand(self):
        self.assertFalse(src.truth_table.logical_nand(True, True))
        self.assertTrue(src.truth_table.logical_nand(True, False))
        self.assertTrue(src.truth_table.logical_nand(False, True))
        self.assertTrue(src.truth_table.logical_nand(False, False))

    def test_tautology(self):
        self.assertTrue(src.truth_table.tautology(True, True))
        self.assertTrue(src.truth_table.tautology(True, False))
        self.assertTrue(src.truth_table.tautology(False, True))
        self.assertTrue(src.truth_table.tautology(False, False))

    def test_logical_disjunction(self):
        self.assertTrue(src.truth_table.logical_disjunction(True, True))
        self.assertTrue(src.truth_table.logical_disjunction(True, False))
        self.assertTrue(src.truth_table.logical_disjunction(False, True))
        self.assertFalse(src.truth_table.logical_disjunction(False, False))

    def test_exclusive_disjunction(self):
        self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
        self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
        self.assertTrue(src.truth_table.exclusive_disjunction(False, True))
        self.assertFalse(src.truth_table.exclusive_disjunction(False, False))

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))
        self.assertTrue(src.truth_table.material_non_implication(True, False))
        self.assertFalse(src.truth_table.material_non_implication(False, True))
        self.assertFalse(src.truth_table.material_non_implication(False, False))

    def test_project_first(self):
        self.assertTrue(src.truth_table.project_first(True, True))
        self.assertTrue(src.truth_table.project_first(True, False))
        self.assertFalse(src.truth_table.project_first(False, True))
        self.assertFalse(src.truth_table.project_first(False, False))

    def test_converse_implication(self):
        self.assertTrue(src.truth_table.converse_implication(True, True))
        self.assertTrue(src.truth_table.converse_implication(True, False))
        self.assertFalse(src.truth_table.converse_implication(False, True))
        self.assertTrue(src.truth_table.converse_implication(False, False))


# Exceptions seen
# AssertionError
# AttributeError
# TypeError
# SyntaxError