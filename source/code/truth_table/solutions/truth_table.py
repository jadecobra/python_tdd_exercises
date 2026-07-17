def logical_negation(something):
    return not something


def logical_identity(something):
    return something


def logical_true():
    return True


def logical_false():
    return False


def tautology(first, second):
    return True


def project_second(first, second):
    return second


def project_first(first, second):
    return first


def negate_second(first, second):
    return not second


def negate_first(first, second):
    return not first


def material_non_implication(first, second):
    return first and not second


def material_implication(first, second):
    return not first or second


def logical_nor(first, second):
    return not (first or second)


def logical_nand(first, second):
    return not (first and second)


def logical_equality(first, second):
    return (not first or second) and (first or not second)


def logical_disjunction(first, second):
    return first or second


def logical_conjunction(first, second):
    return first and second


def exclusive_disjunction(first, second):
    return (not (first and second)) and (first or second)


def converse_non_implication(first, second):
    return not first and second


def converse_implication(first, second):
    return first or not second


def contradiction(first, second):
    return False