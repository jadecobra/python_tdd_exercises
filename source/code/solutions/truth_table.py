def logical_true():
    return True


def logical_false():
    return False


def logical_identity(the_input):
    return the_input


def logical_negation(the_input):
    return not argument


def contradiction(input_1, input_2):
    return False


def logical_conjunction(input_1, input_2):
    return p and q


def project_second(input_1, input_2):
    return q


def converse_non_implication(input_1, input_2):
    return not p and q


def negate_first(input_1, input_2):
    return not p


def logical_nand(input_1, input_2):
    return not (p and q)


def tautology(input_1, input_2):
    return True


def logical_disjunction(input_1, input_2):
    return p or q


def exclusive_disjunction(input_1, input_2):
    return p != q
    return not (p == q)
    return (not p and q) or (p and not q)


def material_non_implication(input_1, input_2):
    return p and not q


def project_first(input_1, input_2):
    return p


def converse_implication(input_1, input_2):
    return p or not q


def negate_second(input_1, input_2):
    return not q


def logical_nor(input_1, input_2):
    return not (p or q)


def logical_equality(input_1, input_2):
    return p == q
    return (p or not q) and (not p or q)


def material_implication(input_1, input_2):
    return not p or q