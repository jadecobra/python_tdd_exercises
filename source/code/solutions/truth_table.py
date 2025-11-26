def logical_true():
    return True


def logical_false():
    return False


def logical_identity(the_input):
    return the_input


def logical_negation(the_input):
    return not the_input


def contradiction(input_1, input_2):
    return False


def logical_conjunction(input_1, input_2):
    return input_1 and input_2


def project_second(input_1, input_2):
    return input_2


def converse_non_implication(input_1, input_2):
    return not input_1 and input_2


def negate_first(input_1, input_2):
    return not input_1


def logical_nand(input_1, input_2):
    return not (input_1 and input_2)


def tautology(input_1, input_2):
    return True


def logical_disjunction(input_1, input_2):
    return input_1 or input_2


def exclusive_disjunction(input_1, input_2):
    return input_1 != input_2
    return not input_1 == input_2
    return (not input_1 and input_2) or (input_1 and not input_2)


def material_non_implication(input_1, input_2):
    return input_1 and not input_2


def project_first(input_1, input_2):
    return input_1


def converse_implication(input_1, input_2):
    return input_1 or not input_2


def negate_second(input_1, input_2):
    return not input_2


def logical_nor(input_1, input_2):
    return not (input_1 or input_2)


def logical_equality(input_1, input_2):
    return input_1 == input_2
    return (input_1 or not input_2) and (not input_1 or input_2)


def material_implication(input_1, input_2):
    return not input_1 or input_2