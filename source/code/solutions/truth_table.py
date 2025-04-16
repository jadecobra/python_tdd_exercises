def logical_true():
    return True


def logical_false():
    return False


def logical_identity(argument):
    return argument


def logical_negation(argument):
    return not argument


def contradiction(p, q):
    return False


def logical_conjunction(p, q):
    return p and q


def project_second(p, q):
    return q


def converse_non_implication(p, q):
    return not p and q


def negate_first(p, q):
    return not p


def logical_nand(p, q):
    return not (p and q)


def tautology(p, q):
    return True


def logical_disjunction(p, q):
    return p or q


def exclusive_disjunction(p, q):
    return p != q
    return not (p == q)
    return (not p and q) or (p and not q)


def material_non_implication(p, q):
    return p and not q


def project_first(p, q):
    return p


def converse_implication(p, q):
    return p or not q


def negate_second(p, q):
    return not q


def logical_nor(p, q):
    return not (p or q)


def logical_equality(p, q):
    return p == q
    return (p or not q) and (not p or q)


def material_implication(p, q):
    return not p or q