
#################################
Truth Table: Tests and Solutions
#################################


tests
-----

Here is the code in ``tests/test_truth_table.py``

.. code-block:: python

    import unittest
    import truth_table


    class TestNullaryOperations(unittest.TestCase):

        def test_logical_true(self):
            self.assertTrue(truth_table.logical_true())

        def test_logical_false(self):
            self.assertFalse(truth_table.logical_false())


    class TestUnaryOperations(unittest.TestCase):

        def test_logical_identity(self):
            self.assertTrue(truth_table.logical_identity(True))
            self.assertFalse(truth_table.logical_identity(False))

        def test_logical_negation(self):
            self.assertFalse(truth_table.logical_negation(True))
            self.assertTrue(truth_table.logical_negation(False))


    class TestBinaryOperations(unittest.TestCase):

        def test_logical_conjunction(self):
            self.assertTrue(truth_table.logical_conjunction(True, True))
            self.assertFalse(truth_table.logical_conjunction(True, False))
            self.assertFalse(truth_table.logical_conjunction(False, True))
            self.assertFalse(truth_table.logical_conjunction(False, False))

        def test_logical_disjunction(self):
            self.assertTrue(truth_table.logical_disjunction(True, True))
            self.assertTrue(truth_table.logical_disjunction(True, False))
            self.assertTrue(truth_table.logical_disjunction(False, True))
            self.assertFalse(truth_table.logical_disjunction(False, False))

        def test_logical_implication(self):
            self.assertTrue(truth_table.logical_implication(True, True))
            self.assertFalse(truth_table.logical_implication(True, False))
            self.assertTrue(truth_table.logical_implication(False, True))
            self.assertTrue(truth_table.logical_implication(False, False))

        def test_logical_equality_or_logical_biconditional(self):
            self.assertTrue(truth_table.logical_equality(True, True))
            self.assertFalse(truth_table.logical_equality(True, False))
            self.assertFalse(truth_table.logical_equality(False, True))
            self.assertTrue(truth_table.logical_equality(False, False))

        def test_exclusive_disjunction(self):
            self.assertFalse(truth_table.exclusive_disjunction(True, True))
            self.assertTrue(truth_table.exclusive_disjunction(True, False))
            self.assertTrue(truth_table.exclusive_disjunction(False, True))
            self.assertFalse(truth_table.exclusive_disjunction(False, False))

        def test_logical_nand(self):
            self.assertFalse(truth_table.logical_nand(True, True))
            self.assertTrue(truth_table.logical_nand(True, False))
            self.assertTrue(truth_table.logical_nand(False, True))
            self.assertTrue(truth_table.logical_nand(False, False))

        def test_logical_nor(self):
            self.assertFalse(truth_table.logical_nor(True, True))
            self.assertFalse(truth_table.logical_nor(True, False))
            self.assertFalse(truth_table.logical_nor(False, True))
            self.assertTrue(truth_table.logical_nor(False, False))

        def test_converse_non_implication(self):
            self.assertFalse(truth_table.converse_non_implication(True, True))
            self.assertFalse(truth_table.converse_non_implication(True, False))
            self.assertTrue(truth_table.converse_non_implication(False, True))
            self.assertFalse(truth_table.converse_non_implication(False, False))

        def test_material_non_implication(self):
            self.assertFalse(truth_table.material_non_implication(True, True))
            self.assertTrue(truth_table.material_non_implication(True, False))
            self.assertFalse(truth_table.material_non_implication(False, True))
            self.assertFalse(truth_table.material_non_implication(False, False))

        def test_negate_first(self):
            self.assertFalse(truth_table.negate_first(True, True))
            self.assertFalse(truth_table.negate_first(True, False))
            self.assertTrue(truth_table.negate_first(False, True))
            self.assertTrue(truth_table.negate_first(False, False))

        def test_negate_second(self):
            self.assertFalse(truth_table.negate_second(True, True))
            self.assertTrue(truth_table.negate_second(True, False))
            self.assertFalse(truth_table.negate_second(False, True))
            self.assertTrue(truth_table.negate_second(False, False))

        def test_project_first(self):
            self.assertTrue(truth_table.project_first(True, True))
            self.assertTrue(truth_table.project_first(True, False))
            self.assertFalse(truth_table.project_first(False, True))
            self.assertFalse(truth_table.project_first(False, False))

        def test_project_second(self):
            self.assertTrue(truth_table.project_second(True, True))
            self.assertFalse(truth_table.project_second(True, False))
            self.assertTrue(truth_table.project_second(False, True))
            self.assertFalse(truth_table.project_second(False, False))

        def test_converse_implication(self):
            self.assertTrue(truth_table.converse_implication(True, True))
            self.assertTrue(truth_table.converse_implication(True, False))
            self.assertFalse(truth_table.converse_implication(False, True))
            self.assertTrue(truth_table.converse_implication(False, False))

        def test_tautology(self):
            self.assertTrue(truth_table.tautology(True, True))
            self.assertTrue(truth_table.tautology(True, False))
            self.assertTrue(truth_table.tautology(False, True))
            self.assertTrue(truth_table.tautology(False, False))

        def test_contradiction(self):
            self.assertFalse(truth_table.contradiction(True, True))
            self.assertFalse(truth_table.contradiction(True, False))
            self.assertFalse(truth_table.contradiction(False, True))
            self.assertFalse(truth_table.contradiction(False, False))


    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError
    # SyntaxError


solutions
---------

Here are the solutions in ``truth_table.py``

.. code-block:: python

    def logical_true():
        return True

    def logical_false():
        return False

    def logical_identity(value):
        return value

    def logical_negation(value):
        return not value

    def logical_conjunction(p, q):
        return p and q

    def logical_disjunction(p, q):
        return p or q

    def logical_implication(p, q):
        return not p or q

    def logical_equality(p, q):
        return p == q

    def exclusive_disjunction(p, q):
        return p != q

    def logical_nand(p, q):
        return not (p and q)

    def logical_nor(p, q):
        return not (p or q)

    def converse_non_implication(p, q):
        return not p and q

    def material_non_implication(p, q):
        return p and not q

    def negate_first(p, q):
        return not p

    def negate_second(p, q):
        return not q

    def project_first(p, q):
        return p

    def project_second(p, q):
        return q

    def converse_implication(p, q):
        return p or not q

    def tautology(p, q):
        return True

    def contradiction(p, q):
        return False