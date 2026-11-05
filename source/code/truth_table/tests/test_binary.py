import src.truth_table
import unittest


TT = True, True
TF = True, False
FT = False, True
FF = False, False


class TestBinaryOperations(unittest.TestCase):

    def test_contradiction(self):
        contradiction = src.truth_table.contradiction
        self.assertFalse(contradiction(*TT))
        self.assertFalse(contradiction(*TF))
        self.assertFalse(contradiction(*FT))
        self.assertFalse(contradiction(*FF))

    def test_logical_conjunction(self):
        logical_conjunction = (
            src.truth_table.logical_conjunction
        )
        self.assertTrue(logical_conjunction(*TT))
        self.assertFalse(logical_conjunction(*TF))
        self.assertFalse(logical_conjunction(*FT))
        self.assertFalse(logical_conjunction(*FF))

    def test_project_second(self):
        project_second = src.truth_table.project_second
        self.assertTrue(project_second(*TT))
        self.assertFalse(project_second(*TF))
        self.assertTrue(project_second(*FT))
        self.assertFalse(project_second(*FF))

    def test_converse_non_implication(self):
        converse_non_implication = (
            src.truth_table.converse_non_implication
        )
        self.assertFalse(converse_non_implication(*TT))
        self.assertFalse(converse_non_implication(*TF))
        self.assertTrue(converse_non_implication(*FT))
        self.assertFalse(converse_non_implication(*FF))

    def test_negate_first(self):
        negate_first = src.truth_table.negate_first
        self.assertFalse(negate_first(*TT))
        self.assertFalse(negate_first(*TF))
        self.assertTrue(negate_first(*FT))
        self.assertTrue(negate_first(*FF))

    def test_logical_nand(self):
        nand = src.truth_table.logical_nand
        self.assertFalse(nand(*TT))
        self.assertTrue(nand(*TF))
        self.assertTrue(nand(*FT))
        self.assertTrue(nand(*FF))

    def test_tautology(self):
        tautology = src.truth_table.tautology
        self.assertTrue(tautology(*TT))
        self.assertTrue(tautology(*TF))
        self.assertTrue(tautology(*FT))
        self.assertTrue(tautology(*FF))

    def test_logical_disjunction(self):
        logical_disjunction = (
            src.truth_table.logical_disjunction
        )
        self.assertTrue(logical_disjunction(*TT))
        self.assertTrue(logical_disjunction(*TF))
        self.assertTrue(logical_disjunction(*FT))
        self.assertFalse(logical_disjunction(*FF))

    def test_exclusive_disjunction(self):
        xor = src.truth_table.exclusive_disjunction
        self.assertFalse(xor(*TT))
        self.assertTrue(xor(*TF))
        self.assertTrue(xor(*FT))
        self.assertFalse(xor(*FF))

    def test_material_non_implication(self):
        material_non_implication = (
            src.truth_table.material_non_implication
        )
        self.assertFalse(material_non_implication(*TT))
        self.assertTrue(material_non_implication(*TF))
        self.assertFalse(material_non_implication(*FT))
        self.assertFalse(material_non_implication(*FF))

    def test_project_first(self):
        project_first = src.truth_table.project_first
        self.assertTrue(project_first(*TT))
        self.assertTrue(project_first(*TF))
        self.assertFalse(project_first(*FT))
        self.assertFalse(project_first(*FF))

    def test_converse_implication(self):
        converse_implication = (
            src.truth_table.converse_implication
        )
        self.assertTrue(converse_implication(*TT))
        self.assertTrue(converse_implication(*TF))
        self.assertFalse(converse_implication(*FT))
        self.assertTrue(converse_implication(*FF))

    def test_negate_second(self):
        negate_second = src.truth_table.negate_second
        self.assertFalse(negate_second(*TT))
        self.assertTrue(negate_second(*TF))
        self.assertFalse(negate_second(*FT))
        self.assertTrue(negate_second(*FF))

    def test_logical_nor(self):
        logical_nor = src.truth_table.logical_nor
        self.assertFalse(logical_nor(*TT))
        self.assertFalse(logical_nor(*TF))
        self.assertFalse(logical_nor(*FT))
        self.assertTrue(logical_nor(*FF))

    def test_logical_equality(self):
        logical_equality = (
            src.truth_table.logical_equality
        )
        self.assertTrue(logical_equality(*TT))
        self.assertFalse(logical_equality(*TF))
        self.assertFalse(logical_equality(*FT))
        self.assertTrue(logical_equality(*FF))

    def test_material_implication(self):
        material_implication = (
            src.truth_table.material_implication
        )
        self.assertTrue(material_implication(*TT))
        self.assertFalse(material_implication(*TF))
        self.assertTrue(material_implication(*FT))
        self.assertTrue(material_implication(*FF))


# Exceptions seen
# AttributeError
# TypeError
# AssertionError
# SyntaxError