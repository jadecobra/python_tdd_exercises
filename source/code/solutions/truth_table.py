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