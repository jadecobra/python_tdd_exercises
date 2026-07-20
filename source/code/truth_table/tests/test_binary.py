import src.truth_table
import unittest


CASE_1 = True, True
CASE_2 = True, False
CASE_3 = False, True
CASE_4 = False, False

class TestBinaryOperations(unittest.TestCase):

    def test_contradiction(self):
        contradiction = src.truth_table.contradiction
        self.assertFalse(contradiction(*CASE_1))
        self.assertFalse(contradiction(*CASE_2))
        self.assertFalse(contradiction(*CASE_3))
        self.assertFalse(contradiction(*CASE_4))

    def test_logical_conjunction(self):
        logical_conjunction = (
            src.truth_table.logical_conjunction
        )
        self.assertTrue(logical_conjunction(*CASE_1))
        self.assertFalse(logical_conjunction(*CASE_2))
        self.assertFalse(logical_conjunction(*CASE_3))
        self.assertFalse(logical_conjunction(*CASE_4))

    def test_project_second(self):
        project_second = src.truth_table.project_second
        self.assertTrue(project_second(*CASE_1))
        self.assertFalse(project_second(*CASE_2))
        self.assertTrue(project_second(*CASE_3))
        self.assertFalse(project_second(*CASE_4))

    def test_converse_non_implication(self):
        converse_non_implication = (
            src.truth_table.converse_non_implication
        )
        self.assertFalse(converse_non_implication(*CASE_1))
        self.assertFalse(converse_non_implication(*CASE_2))
        self.assertTrue(converse_non_implication(*CASE_3))
        self.assertFalse(converse_non_implication(*CASE_4))

    def test_negate_first(self):
        negate_first = src.truth_table.negate_first
        self.assertFalse(negate_first(*CASE_1))
        self.assertFalse(negate_first(*CASE_2))
        self.assertTrue(negate_first(*CASE_3))
        self.assertTrue(negate_first(*CASE_4))

    def test_logical_nand(self):
        nand = src.truth_table.logical_nand
        self.assertFalse(nand(*CASE_1))
        self.assertTrue(nand(*CASE_2))
        self.assertTrue(nand(*CASE_3))
        self.assertTrue(nand(*CASE_4))

    def test_tautology(self):
        tautology = src.truth_table.tautology
        self.assertTrue(tautology(*CASE_1))
        self.assertTrue(tautology(*CASE_2))
        self.assertTrue(tautology(*CASE_3))
        self.assertTrue(tautology(*CASE_4))

    def test_logical_disjunction(self):
        logical_disjunction = (
            src.truth_table.logical_disjunction
        )
        self.assertTrue(logical_disjunction(*CASE_1))
        self.assertTrue(logical_disjunction(*CASE_2))
        self.assertTrue(logical_disjunction(*CASE_3))
        self.assertFalse(logical_disjunction(*CASE_4))

    def test_exclusive_disjunction(self):
        xor = src.truth_table.exclusive_disjunction
        self.assertFalse(xor(*CASE_1))
        self.assertTrue(xor(*CASE_2))
        self.assertTrue(xor(*CASE_3))
        self.assertFalse(xor(*CASE_4))

    def test_material_non_implication(self):
        material_non_implication = (
            src.truth_table.material_non_implication
        )
        self.assertFalse(material_non_implication(*CASE_1))
        self.assertTrue(material_non_implication(*CASE_2))
        self.assertFalse(material_non_implication(*CASE_3))
        self.assertFalse(material_non_implication(*CASE_4))

    def test_project_first(self):
        project_first = src.truth_table.project_first
        self.assertTrue(project_first(*CASE_1))
        self.assertTrue(project_first(*CASE_2))
        self.assertFalse(project_first(*CASE_3))
        self.assertFalse(project_first(*CASE_4))

    def test_converse_implication(self):
        converse_implication = (
            src.truth_table.converse_implication
        )
        self.assertTrue(converse_implication(*CASE_1))
        self.assertTrue(converse_implication(*CASE_2))
        self.assertFalse(converse_implication(*CASE_3))
        self.assertTrue(converse_implication(*CASE_4))

    def test_negate_second(self):
        negate_second = src.truth_table.negate_second
        self.assertFalse(negate_second(*CASE_1))
        self.assertTrue(negate_second(*CASE_2))
        self.assertFalse(negate_second(*CASE_3))
        self.assertTrue(negate_second(*CASE_4))

    def test_logical_nor(self):
        logical_nor = src.truth_table.logical_nor
        self.assertFalse(logical_nor(*CASE_1))
        self.assertFalse(logical_nor(*CASE_2))
        self.assertFalse(logical_nor(*CASE_3))
        self.assertTrue(logical_nor(*CASE_4))

    def test_logical_equality(self):
        logical_equality = (
            src.truth_table.logical_equality
        )
        self.assertTrue(logical_equality(*CASE_1))
        self.assertFalse(logical_equality(*CASE_2))
        self.assertFalse(logical_equality(*CASE_3))
        self.assertTrue(logical_equality(*CASE_4))

    def test_material_implication(self):
        material_implication = (
            src.truth_table.material_implication
        )
        self.assertTrue(material_implication(*CASE_1))
        self.assertFalse(material_implication(*CASE_2))
        self.assertTrue(material_implication(*CASE_3))
        self.assertTrue(material_implication(*CASE_4))


# Exceptions seen
# AttributeError
# TypeError
# AssertionError
# SyntaxError